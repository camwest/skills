---
name: write-standalone-docs
description: Draft or revise reports, strategy documents, memos, specifications, proposals, and other durable artifacts so they make sense without the chat, meeting, screenshot, or task that produced them. Use when converting conversation into a document or reviewing prose for ghost arguments, invisible interlocutors, leaked instructions, commissioning-context residue, dangling references, or irrelevant process provenance.
---

# Write Standalone Docs

Create an artifact that a cold reader can understand, assess, and reuse without access to its production conversation. Preserve the underlying reasoning, evidence, uncertainty, and useful disagreement; remove only context that belongs to the drafting process rather than the document.

## Core distinction

Treat source material as three different things:

1. **Domain evidence and decisions** may enter the artifact. Cite or attribute them at the level the audience needs.
2. **Commissioning constraints** shape the artifact but normally do not appear in it. Translate requests about structure, tone, or emphasis into the document itself.
3. **Production residue** stays out. This includes task instructions, chat choreography, drafting commentary, and rebuttals whose target exists only in the source conversation.

Treat the user-assistant exchange that commissioned the artifact as production context by default. Do not relabel it as an interview, internal strategy discussion, or first-party research to give unsupported claims provenance. It becomes domain evidence only when the user explicitly supplies it as a meeting record, interview, decision log, legal record, or other source that the artifact is meant to analyze.

Do not confuse standalone writing with neutral or bloodless writing. A standalone document may argue strongly, use first or second person deliberately, quote a conversation as evidence, or rebut a named proposition. The requirement is that the document supplies the audience, antecedent, and evidentiary role for each one.

## Workflow

### 1. Establish the artifact contract

Before drafting or revising, identify:

- the intended reader;
- the decision, action, or understanding the document should enable;
- what the reader may safely be assumed to know;
- which sources or people must remain attributable;
- whether the requested output is the clean artifact, an audit, or both.

Infer these from the request and source material when safe. Ask only when the answer would materially change the document.

### 2. Classify the inputs

Sort the useful source material into:

- **claims and decisions**;
- **observations and evidence**;
- **counterarguments and trade-offs**;
- **preferences about the deliverable**;
- **production metadata**.

Move the first three into the artifact when relevant. Convert preferences into structure or editorial choices. Exclude production metadata unless the artifact is explicitly about the production process.

For interviews, customer calls, research threads, and legal or operational records, the conversation itself may be evidence. In that case, attribute the observation because it supports a claim—not because it happened to be available in the task.

Do not infer source metadata that was not supplied. A current date, file owner, participant name, job title, or supposed meeting purpose is not evidence of when, by whom, or why a source was created.

### 3. Draft affirmative, inspect contrasts

Lead sections with the proposition the document supports. When using contrast, criticism, or rebuttal, make its target visible in the artifact.

Apply these tests:

- **Antecedent test:** Can the reader identify what this sentence responds to?
- **Evidence test:** Is the contrast supported by a source, observation, or explicit alternative in the document?
- **Audience test:** Is the speaker behind `we`, `you`, `they`, or a named person unambiguous and relevant?
- **Delete-the-chat test:** Would the paragraph still make sense if the source conversation disappeared?
- **Document-purpose test:** Does this detail help the reader use or assess the artifact?

If a sentence fails, rewrite it as an affirmative rule, name the alternative it evaluates, add the missing evidence, or remove it.

Keep the substantive scope stable. A standalone-document pass is not permission to invent policy, expand the strategy, resolve legal or technical questions, or upgrade a preference into a fact. Label unsupported material as a hypothesis, preserve an explicit placeholder, or report the evidence gap outside the artifact when the gap is not itself useful to the reader.

### 4. Run the residue scan

For a local Markdown or text artifact, run the scanner bundled with this skill, where `<skill-dir>` is the directory containing this SKILL.md:

```bash
python3 <skill-dir>/scripts/audit_conversation_residue.py PATH
```

The scanner reports high-confidence production references and lower-confidence review cues with line numbers. It never proves that a sentence is wrong and never rewrites text. Review every hit in context; valid instructions, quotations, or documented alternatives may remain.

Use `--format json` for structured output, `--fail-on review` when every cue should fail a check, and `--fail-on none` for an advisory-only scan. Directories are scanned recursively for common text formats.

### 5. Perform a cold-reader pass

Read the entire artifact from the title down without consulting the source conversation. Check:

- the purpose and audience are discoverable;
- every pronoun and deictic reference has a usable antecedent;
- every rebuttal exposes the proposition it rebuts;
- names, screenshots, chats, and task references have a necessary evidentiary role;
- the audit trail records sources and observations, not drafting choreography;
- uncertainty is stated as uncertainty rather than conversational hedging;
- section transitions follow the document's logic rather than the order of the chat;
- removing the source task would not erase a premise needed to understand the conclusion.

Then read only the headings and first sentence of each section. They should form a coherent argument on their own.

### 6. Return a clean handoff

When asked to edit a file, edit the artifact itself and summarize the categories changed outside it. Do not add a self-congratulatory preface, a list of user instructions followed, or a hidden explanation of the drafting process to the artifact.

When asked only to review, report concrete spans with proposed rewrites. Distinguish:

- confirmed production residue;
- context-dependent candidates;
- intentional, valid references that should remain.

## Rewrite patterns

Use these transformations as patterns, not mechanical substitutions:

| Source-shaped prose | Standalone form |
|---|---|
| “As requested, this report covers …” | State the report's purpose directly. |
| “We discussed three risks.” | Name the evidence source or present the three risks. |
| “Calling X a design partner creates false confidence.” | Define the obligations required for design-partner status and explain the evidence gap. |
| “This is not the answer.” | State the decision criterion the proposal fails. |
| “I think adoption is weak.” | “Adoption is a working hypothesis because …” |
| “The screenshot shows …” | Attribute the specific observed behavior if the screenshot is evidence; otherwise state the behavior. |
| “See above” or “as noted earlier” | Name the section, claim, or evidence being referenced. |
| “The source task asked for an audit trail.” | Include an audit trail without mentioning the task. |

Read [review-patterns.md](references/review-patterns.md) when a hit is ambiguous or when designing a document-specific audit.

## Guardrails

- Preserve factual meaning, citations, commitments, and material uncertainty.
- Do not erase a first-person customer view that is itself evidence.
- Do not promote the commissioning chat into evidence or cite the commissioner merely because no better source is available.
- Do not invent source dates, roles, titles, or provenance from the current task context.
- Do not ban second person from instructions; make the intended reader clear.
- Do not remove negation or disagreement merely because it is sharp.
- Do not invent an external opponent to make an argument feel motivated.
- Do not replace a specific source with vague authority such as “research shows.”
- Do not let a clean style hide a missing premise. Supply the premise or narrow the claim.
- Do not treat scanner output as a verdict.

## Completion criteria

The artifact is ready only when:

1. a cold reader can state its purpose and main claim without the source conversation;
2. every material contrast has a visible target and rationale;
3. each conversational source reference is either necessary evidence or removed;
4. the audit trail can be followed to real sources;
5. the scanner has no unexplained high-confidence hits;
6. the rewrite has not silently expanded the artifact's substantive claims;
7. the final handoff keeps editorial commentary outside the artifact.
