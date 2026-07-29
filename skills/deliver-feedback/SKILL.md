---
name: deliver-feedback
description: Turn rough notes, recordings, transcripts, comments, or reactions into concise feedback that a recipient can understand and act on. Use when drafting or revising feedback on a document, proposal, strategy, design, presentation, plan, or other work product; when organizing feedback as I Like / I Wish / I Wonder; or when preserving a sender's evidence, disagreement, uncertainty, and voice while removing repetition and AI-sounding prose.
---

# Deliver Feedback

Convert raw reactions into useful feedback without changing what the sender
believes. Synthesize the material; do not sanitize disagreement, invent praise,
or make uncertain claims sound settled.

## Establish the feedback contract

Identify:

- the recipient and work product;
- the decision, revision, or conversation the feedback should support;
- the sender's relationship to the recipient and preferred level of directness;
- whether the user wants a clean draft, an analysis, or both;
- the delivery format and channel, if specified.

Infer these from the source when safe. Match the sender's vocabulary and
register. Treat drafting as read-only: do not send or publish feedback unless
the user asks.

## Build an evidence ledger

Read the work product and the sender's reactions when both are available.
Separate the input into:

- **Observed:** a specific passage, choice, omission, behavior, or result.
- **Inferred:** the sender's interpretation of that evidence.
- **Uncertain:** a question, doubt, or assumption that needs testing.
- **Requested:** a proposed change or next step.

Keep these distinctions through the rewrite. Do not turn a question into a
finding, infer intent, or attribute a personal trait from the work.

If the source artifact is unavailable, say that the draft reflects the sender's
notes rather than an independent reading. Do not pretend to have verified it.

## Find the few underlying points

Group repeated reactions by the concern beneath them. Preserve a repeated point
only when each instance adds different evidence or affects a different decision.

Rank points by:

1. effect on the recipient's decision or next revision;
2. strength of the supporting evidence;
3. cost of misunderstanding or leaving the issue unresolved.

Prefer a few developed points over an exhaustive transcript recap. Do not drop a
material concern merely to make the sections symmetrical.

## Choose the structure

Honor a requested format. Otherwise choose the smallest structure that fits.

Use **I Like / I Wish / I Wonder** for collaborative feedback on work in
progress:

- **I like:** choices worth preserving, with the reason they work.
- **I wish:** changes the sender wants, tied to a concrete passage or effect.
- **I wonder:** open questions, untested assumptions, and possible alternatives.

Do not force praise or populate an empty section. If the sender has no genuine
positive reaction, omit `I like` and state that choice outside the draft when
useful.

Use direct bullets without headings when the recipient needs a short list of
changes. Use a short narrative when sequence or context matters more than
categorization.

## Draft each point

Each bullet should carry one idea and usually include:

1. the concrete choice or passage;
2. its effect on the sender, reader, decision, or product;
3. the requested change or unresolved question.

Use first person for the sender's judgment: `I lost the distinction between a
loop and a run here.` Use direct observation for evidence: `The pricing table
uses one rate for firms with different account volumes.` Avoid verdicts such as
`This is confusing` when the draft can name what the reader could not
distinguish.

Questions must expose the assumption they test. `I wonder whether one run is
the right pricing unit when each household requires separate reasoning` is more
useful than `I wonder about pricing`.

Preserve sharp feedback when the evidence supports it. Remove insults,
mind-reading, and claims about competence. Critique the work and its effects.

## Keep the sender's voice

- Reuse words and sentence shapes the sender uses naturally.
- Keep meaningful hedges such as `I think`, `I am not sure`, and `I wonder`.
- Cut filler, repeated setup, and transcript artifacts.
- Avoid consultant language, balanced-sounding abstractions, and polished
  conclusions that restate the bullets.
- Vary sentence length. Do not make every bullet follow the same template.
- Keep concrete examples even when they make the draft less tidy.

Do not confuse concision with softness. A short sentence can still state a hard
disagreement.

## Optional anti-slop pass

Use the `unslop` and `stop-slop` skills when they are installed:

1. Run `unslop` to find clustered AI-writing tropes and rewrite only the
   offenders.
2. Run `stop-slop` to cut filler, false contrasts, vague claims, and mechanical
   rhythm.

Check the active skill catalog or installed skill directories before relying on
them. They are optional dependencies and may not exist in another environment.
If either skill is unavailable, finish with the checks below and state briefly
in the handoff which optional skill was not installed.

Do not let an anti-slop pass erase evidence, uncertainty, disagreement, or the
sender's voice.

## Final checks

Before returning the draft, verify:

- every material point traces to the source material;
- no praise, claim, motive, or recommendation was invented;
- observations, inferences, questions, and requests remain distinct;
- each criticism names a concrete choice or effect;
- the recipient can tell what to preserve, change, investigate, or discuss;
- repeated points have been combined without losing distinct evidence;
- the tone sounds like the sender rather than a facilitator or consultant;
- the draft contains no throat-clearing conclusion or forced symmetry;
- no message was sent without explicit authorization.

Return the clean draft first. Add process notes only when the user requested an
audit, a source was unavailable, or an optional anti-slop skill was not
installed.
