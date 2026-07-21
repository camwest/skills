# Review patterns

Use this reference to interpret scanner hits and to audit prose the scanner cannot classify reliably.

## Residue taxonomy

### Ghost argument

The document attacks, corrects, or distances itself from a proposition that the document never states and no source establishes.

- Candidate: “Worse, the ordinary customer model creates false confidence.”
- Repair: define the evidence rights the strategy requires, then show which customer model lacks them.
- Keep when: the preceding text or a cited source clearly states the alternative being evaluated.

### Invisible interlocutor

The prose answers a person who is absent from the artifact.

- Candidate: “That does not answer the real question.”
- Repair: state the decision question and the criterion the proposal does not satisfy.
- Keep when: the artifact is a letter, response, dialogue analysis, or transcript synthesis and identifies the speaker and exchange.

### Commissioning residue

The document reports instructions that should have shaped the deliverable silently.

- Candidate: “As requested, the next section is an executive summary.”
- Repair: use the heading `Executive summary` and begin with the conclusion.
- Keep when: the commissioning history is itself in scope, such as a compliance record or change log.

### Process provenance masquerading as evidence

The artifact cites how the draft was produced instead of the underlying source.

- Candidate: “The source task and attached screenshot establish the constraint.”
- Repair: cite the contract clause, observed behavior, interview, or dated record that establishes it.
- Keep when: reproducibility requires a prompt, model, workflow, or transformation history.

Watch for a subtler version: relabeling the commissioning exchange as an “internal discussion,” “first-party observation,” or dated source. That does not make it domain evidence. Unless the user explicitly supplied the exchange as a record to analyze, remove it and calibrate the dependent claim as a hypothesis or evidence gap.

### Dangling deictic reference

Words such as `this`, `that`, `above`, `earlier`, `here`, or `the answer` depend on context the reader cannot locate.

- Candidate: “This is why the second model wins.”
- Repair: name the causal observation or comparison.
- Keep when: the antecedent is immediate and unmistakable.

### Unscoped collective voice

`We`, `our`, or `us` shifts between the author, company, team, reader, and source participants.

- Candidate: “We can retain the data, but we still need access.”
- Repair: name the company or party responsible for each action.
- Keep when: the document establishes a stable organizational author and the antecedent remains clear.

## What not to flatten

Standalone does not mean context-free in the abstract. It means self-sufficient for its intended audience.

Keep:

- direct second-person instructions when the reader is clear;
- attributed first-person testimony when the testimony is evidence;
- explicit counterarguments, falsifiers, and rejected options;
- document navigation such as “see Evidence and priors” when it names a real section;
- the commissioning record when approval, compliance, or reproducibility requires it;
- domain vocabulary the audience understands.

## Review procedure for ambiguous hits

For each hit, record four judgments:

1. **Speaker:** Who is speaking or being answered?
2. **Antecedent:** Where can the reader find the proposition or object referenced?
3. **Evidentiary role:** What claim does this reference support?
4. **Counterfactual:** If the source chat vanished, what premise would be lost?

Choose one disposition:

- `remove`: production residue with no reader value;
- `translate`: a useful commissioning preference that should become structure or criteria;
- `attribute`: source material that is genuine evidence;
- `name`: a valid contrast whose target or actor is implicit;
- `keep`: already understandable and purposeful for the intended audience.

## Whole-document checks the scanner cannot perform

- The executive summary must not rely on definitions introduced only later unless it links or defines them.
- Section order must reflect the argument, not the order of messages or meetings.
- A named source must be sufficiently identified for the audience to assess it.
- The audit trail must separate observed facts, external priors, interpretations, and decisions.
- The audit trail must not invent a source date, participant role, meeting purpose, or research status from task metadata.
- A rhetorical flourish must not substitute for evidence or a decision criterion.
- The final document must not mention its own requested format unless that format is substantively relevant.
