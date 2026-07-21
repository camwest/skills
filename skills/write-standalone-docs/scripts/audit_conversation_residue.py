#!/usr/bin/env python3
"""Surface possible conversational residue in durable text artifacts.

This is a heuristic review aid. It does not determine whether a match is wrong
and it never rewrites the source file.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Sequence


TEXT_SUFFIXES = {".md", ".mdx", ".txt", ".rst", ".adoc"}


@dataclass(frozen=True)
class Rule:
    rule_id: str
    severity: str
    pattern: re.Pattern[str]
    reason: str


@dataclass(frozen=True)
class Finding:
    path: str
    line: int
    severity: str
    rule_id: str
    reason: str
    text: str


def compile_rule(rule_id: str, severity: str, pattern: str, reason: str) -> Rule:
    return Rule(rule_id, severity, re.compile(pattern, re.IGNORECASE), reason)


RULES: tuple[Rule, ...] = (
    compile_rule(
        "chat-antecedent",
        "high",
        r"\b(?:as|like)\s+(?:you|we)\s+(?:asked|said|discussed|agreed|noted|mentioned|decided)\b",
        "Depends on a prior exchange that may not be available to the reader.",
    ),
    compile_rule(
        "conversation-reference",
        "high",
        r"\b(?:our|the|this|that|source)\s+(?:conversation|chat|thread)\b",
        "Names the production conversation instead of the underlying evidence.",
    ),
    compile_rule(
        "request-reference",
        "high",
        r"\b(?:your|the|this|source)\s+(?:request|prompt|instructions?|task)\b",
        "Exposes commissioning or task metadata in the artifact.",
    ),
    compile_rule(
        "turn-reference",
        "high",
        r"\b(?:previous|earlier|prior|last)\s+(?:message|turn|reply|response)\b",
        "Points to conversation structure unavailable in the artifact.",
    ),
    compile_rule(
        "attachment-reference",
        "high",
        r"\b(?:attached|provided|shared)\s+(?:screenshot|image|file|document)\b",
        "Refers to attachment choreography rather than identifying the source.",
    ),
    compile_rule(
        "answer-reference",
        "review",
        r"\b(?:the|this|that)\s+(?:answer|response)\s+(?:is|should|must|needs?\s+to|does|doesn't|does not)\b",
        "May answer an invisible interlocutor or an unstated question.",
    ),
    compile_rule(
        "speaker-hedge",
        "review",
        r"\b(?:I|we)\s+(?:think|believe|feel|guess|would argue)\b",
        "May need an explicit hypothesis, owner, or evidence basis.",
    ),
    compile_rule(
        "second-person",
        "review",
        r"\b(?:you|your|yours)\b",
        "Check that the intended reader is explicit and consistently addressed.",
    ),
    compile_rule(
        "rhetorical-rebuttal",
        "review",
        r"^\s*(?:but|worse|actually|obviously|clearly|instead|on the contrary|calling\b)",
        "Check that the proposition being rebutted is visible in the artifact.",
    ),
    compile_rule(
        "draft-reference",
        "review",
        r"\b(?:this|the)\s+(?:draft|write-?up|deliverable)\b",
        "May describe the production artifact rather than its subject.",
    ),
)


def iter_files(inputs: Sequence[str]) -> Iterable[Path]:
    seen: set[Path] = set()
    for raw in inputs:
        path = Path(raw).expanduser()
        if path.is_file():
            resolved = path.resolve()
            if resolved not in seen:
                seen.add(resolved)
                yield resolved
            continue
        if path.is_dir():
            for candidate in sorted(path.rglob("*")):
                if candidate.is_file() and candidate.suffix.lower() in TEXT_SUFFIXES:
                    resolved = candidate.resolve()
                    if resolved not in seen:
                        seen.add(resolved)
                        yield resolved
            continue
        raise FileNotFoundError(raw)


def scan_file(path: Path) -> list[Finding]:
    findings: list[Finding] = []
    in_fence = False
    in_frontmatter = False
    frontmatter_possible = True

    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        stripped = line.strip()
        if frontmatter_possible and line_number == 1 and stripped == "---":
            in_frontmatter = True
            continue
        if in_frontmatter:
            if stripped == "---":
                in_frontmatter = False
                frontmatter_possible = False
            continue
        frontmatter_possible = False
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence or not stripped:
            continue

        for rule in RULES:
            if rule.pattern.search(line):
                findings.append(
                    Finding(
                        path=str(path),
                        line=line_number,
                        severity=rule.severity,
                        rule_id=rule.rule_id,
                        reason=rule.reason,
                        text=stripped,
                    )
                )
    return findings


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Surface possible conversation residue in Markdown and text artifacts."
    )
    parser.add_argument("paths", nargs="+", help="Files or directories to scan")
    parser.add_argument(
        "--format",
        choices=("text", "json"),
        default="text",
        dest="output_format",
        help="Output format (default: text)",
    )
    parser.add_argument(
        "--fail-on",
        choices=("none", "high", "review"),
        default="high",
        help="Exit 1 at or above this threshold (default: high)",
    )
    return parser.parse_args(argv)


def should_fail(findings: Sequence[Finding], threshold: str) -> bool:
    if threshold == "none":
        return False
    if threshold == "high":
        return any(finding.severity == "high" for finding in findings)
    return bool(findings)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    try:
        files = list(iter_files(args.paths))
    except FileNotFoundError as error:
        print(f"error: path does not exist: {error}", file=sys.stderr)
        return 2

    if not files:
        print("error: no supported text files found", file=sys.stderr)
        return 2

    try:
        findings = [finding for path in files for finding in scan_file(path)]
    except (OSError, UnicodeError) as error:
        print(f"error: unable to scan input: {error}", file=sys.stderr)
        return 2

    if args.output_format == "json":
        print(json.dumps([asdict(finding) for finding in findings], indent=2))
    else:
        for finding in findings:
            print(
                f"{finding.path}:{finding.line}: "
                f"[{finding.severity.upper()} {finding.rule_id}] {finding.text}"
            )
            print(f"  {finding.reason}")
        high_count = sum(finding.severity == "high" for finding in findings)
        review_count = len(findings) - high_count
        print(
            f"Scanned {len(files)} file(s): "
            f"{high_count} high-confidence, {review_count} review cue(s)."
        )

    return 1 if should_fail(findings, args.fail_on) else 0


if __name__ == "__main__":
    raise SystemExit(main())
