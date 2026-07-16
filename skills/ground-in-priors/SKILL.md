---
name: ground-in-priors
description: Research and compare credible precedents before proposing or implementing fixes, features, abstractions, dependencies, architecture, process changes, product ideas, or strategy. Use when explicitly invoked, when an agent is about to invent a non-trivial solution, when only one unsupported approach has been proposed, or when deciding whether to reuse, configure, adapt, compose, or build. Diagnose the actual problem, search repo-local and external priors, test transferability, and treat invention as the last justified option.
---

# Ground in Priors

Use precedent to narrow the solution space before writing a solution. Treat prior
work as evidence, not authority: understand its mechanism, test whether its
assumptions transfer, and adapt only as much as the local context requires.

This is a rigorous research gate. Do not offer a quick mode or silently shorten
the protocol because the task looks small. Scale the breadth of the search to
the decision's uncertainty, blast radius, reversibility, and novelty—not to the
apparent line count of the eventual change.

## Contract

- Freeze the problem and scope before searching for solutions.
- Separate observed facts, sourced claims, inferences, and hypotheses.
- Diagnose bugs before searching for fixes to their symptoms.
- Search local precedent before external precedent.
- Prefer primary and authoritative sources over summaries and popularity.
- Compare multiple independent priors; do not anchor on the first plausible hit.
- Explain why each serious prior does or does not transfer.
- Choose the least-inventive viable path: reuse, configure, adapt, compose, invent.
- Verify the chosen path against the real local system.
- Fail closed when the problem, evidence, or transfer argument is inadequate.
- Preserve the user's original authorization and scope. Research is not permission
  to edit, install, migrate, publish, or expand the task.

Do not treat this skill as blindly pro-library. A dependency, vendor, copied
pattern, or fashionable product can be less suitable than small local code.
External origin is not evidence of quality; local origin is not evidence of
uniqueness.

## Phase 0: Freeze the Problem Fingerprint

Before proposing solutions, record:

- **Observed state:** What is happening now? Cite the reproduction, artifact,
  code path, user evidence, metric, or decision trigger.
- **Desired state:** What outcome must change? Avoid encoding a preferred
  implementation as the goal.
- **Mechanism:** What currently causes the behavior? Mark unknowns explicitly.
- **Constraints:** Versions, platforms, compatibility, ownership, security,
  accessibility, performance, cost, timeline, and user expectations.
- **Scope baseline:** Original request, permitted actions, affected boundary,
  and explicit non-goals.
- **Decision:** State the exact choice the research must inform.

For a bug, reproduce and trace the behavior far enough to distinguish the
symptom from plausible mechanisms. If the mechanism is still unknown, research
diagnostic techniques and governing contracts first. Do not search generic
symptom phrases and mistake their fixes for relevant priors.

For a product or strategy question, distinguish evidence of a user problem from
evidence that another organization shipped a feature. Competitor behavior is a
prior, not validation.

If the fingerprint is too incomplete to guide a credible search, return
`problem-not-understood` with the missing evidence. Continue gathering safe,
in-scope evidence when possible; ask the user only when the missing choice or
access cannot be recovered locally.

## Phase 1: Design the Search

Classify the primary altitude:

- implementation or bug
- dependency, API, or integration
- architecture or engineering process
- product, organization, or strategy

Then read [references/source-ladders.md](references/source-ladders.md) completely
and select the matching ladder. Search outward in this order:

1. **Local reality:** current code, tests, history, existing dependencies,
   adjacent behavior, user evidence, prior decisions.
2. **Authoritative upstream:** specifications, official documentation, source,
   types, tests, changelogs, maintainers, standards, and original research.
3. **Proven precedent:** mature implementations, historical fixes, issue
   discussions, postmortems, comparable products, and measured case studies.
4. **Broader analogues:** other ecosystems, adjacent domains, failed attempts,
   and distant mechanisms that solve the same underlying problem.

Write the search plan before executing it. Name the evidence layers, likely
primary sources, key terms, versions, and unavailable channels. Search by
mechanism and constraint, not only by the user's wording.

Use current sources for facts that can drift. Read the actual source behind
search snippets. For repository-hosted sources, inspect source, tests, history,
and issues with the repository-native tools available in the environment.

## Phase 2: Meet the Evidence Bar

By default, collect:

- at least three credible priors;
- evidence from at least two independent source classes; and
- at least one counterexample, failure mode, or rejected approach.

Treat these as a diversity floor, not a quota. Ten pages repeating the same
claim remain one prior. One authoritative source may decide a standards- or
API-defined question only when local evidence confirms that the exact contract,
version, and conditions apply.

For every material claim, preserve an exact retrieval handle: file and lines,
commit or PR, issue, specification section, documentation page, paper, dataset,
trace, metric, interview, or directly observed artifact. Record source date and
version when they affect transferability.

Label evidence explicitly:

- **Observed:** directly verified in the current task.
- **Sourced:** stated by a cited source.
- **Inferred:** conclusion drawn from observed or sourced evidence.
- **Hypothesized:** plausible but not yet tested.

Do not use an AI-generated answer, search-result snippet, aggregate popularity,
or uncited recollection as the final support for a claim when the underlying
source is available. Do not claim absence from a channel that was unavailable.

## Phase 3: Build Prior Cards

Create a prior card for each serious candidate:

```markdown
### Prior: <name>
- Source: <exact retrieval handle>
- Source class: <local | authoritative | proven | analogous>
- Problem solved: <the source's problem, in its own context>
- Mechanism: <why the approach works>
- Preconditions: <required environment, contract, scale, or behavior>
- Local matches: <conditions that transfer>
- Local mismatches: <conditions that do not transfer>
- Failure modes: <known or plausible limits>
- Transfer class: <reuse | configure | adapt | compose | mechanism-only | reject>
- Falsifier: <evidence that would invalidate this transfer>
```

Read enough of each reference to understand the complete relevant mechanism.
Do not copy a patch, API call, design pattern, or product feature from a partial
example. Prefer a smaller set of deeply understood priors over a long link dump.

## Phase 4: Challenge Transferability

Compare candidates against the frozen fingerprint and actively try to disprove
the leading option:

- Check exact versions, platforms, browser or runtime behavior, scale, data
  shape, security model, accessibility contract, and owner boundary.
- Search for failures, reversals, deprecations, and maintainers' rejected uses.
- Distinguish correlation, convention, and popularity from causal mechanism.
- Identify when multiple sources are not independent because they repeat one
  original claim or implementation.
- Test whether the source solved the same mechanism or merely the same symptom.
- Consider whether exposure to a concrete example is causing design fixation.
  Abstract the mechanism, then compare alternatives at that level.

If the leading prior survives only by changing the task's contract, mark it
non-transferable and escalate the scope decision. Do not quietly redefine the
problem to fit the precedent.

## Phase 5: Pass the Decision Gate

Evaluate options in this order:

1. **Reuse:** Apply an existing local or external solution unchanged.
2. **Configure:** Use an existing capability through supported configuration.
3. **Adapt:** Make the smallest context-specific change around a proven mechanism.
4. **Compose:** Combine a small number of compatible precedents.
5. **Invent:** Design a new mechanism informed by the research.

Choosing a later step requires explicitly rejecting every earlier viable step.
Compare correctness, maintenance, dependency and vendor risk, compatibility,
security, performance, accessibility, reversibility, and local ownership.

Return exactly one decision status:

- `ready-to-reuse`
- `ready-to-configure`
- `ready-to-adapt`
- `ready-to-compose`
- `invention-justified`
- `insufficient-evidence`
- `problem-not-understood`

Use `invention-justified` only when the search coverage is credible, serious
priors failed the transfer test for documented reasons, and the proposed novel
mechanism incorporates what the failed priors taught. "I did not find one" is
not sufficient.

## Phase 6: Define and Run Local Proof

Before implementation, define the smallest proof that discriminates the chosen
approach from rejected alternatives:

- bug: minimal reproduction, regression test, event or data trace;
- dependency or API: version-matched spike, type check, contract test;
- architecture: thin vertical slice, benchmark, failure injection, rollback;
- product or strategy: user evidence, prototype test, falsifiable experiment,
  historical or market check.

When the original request authorizes implementation, proceed after the decision
artifact is complete and the proof plan is credible. Do not request redundant
approval. If the request was research-only, stop at the recommendation. If the
best path requires a new owner boundary, migration, protocol, dependency,
external action, or materially different product decision, stop and request the
authority needed for that expansion.

After implementation, run the proof and relevant regression checks. If the
evidence contradicts the transfer argument, return to the problem fingerprint;
do not stack patches onto a failed premise.

## Scope Governor

Freeze the baseline before searching. Classify each discovery as:

- **Decision-relevant:** changes the choice inside the original boundary.
- **Follow-up:** real but adjacent work for a separate task.
- **Out of scope:** interesting but unrelated.
- **Reframe:** evidence that the original problem or owner boundary is wrong.

Pause and restate the fingerprint when a reframe occurs. Stop rather than
expanding when research turns a narrow fix into a migration, architecture
change, product strategy shift, release-process change, or new public contract.
Preserve useful follow-up evidence without letting it hijack the task.

## Convergence and Stopping

Stop searching when one of these conditions is met:

- an authoritative contract plus local evidence determines the decision;
- a broad pass and a targeted refinement pass converge, with the refinement
  finding no new decision-relevant mechanism, constraint, or serious candidate;
- required evidence channels remain unavailable, producing
  `insufficient-evidence`; or
- the problem remains undiagnosed, producing `problem-not-understood`.

Do not stop at the first plausible answer. Do not pursue theoretical
exhaustiveness after convergence. Report skipped or unavailable channels and
how they limit confidence.

## Required Decision Artifact

Return this structure before presenting or implementing the solution:

```markdown
## Problem fingerprint
Observed state, desired state, mechanism, constraints, scope, decision.

## Search coverage
Layers, queries or retrieval paths, versions, unavailable channels.

## Priors considered
Prior cards with exact retrieval handles.

## Transfer analysis
Comparison, counterevidence, falsifiers, and confidence.

## Decision
One status plus the least-inventive viable path and why earlier steps failed.

## Local proof
Experiment, regression test, measurement, or validation result.

## Remaining uncertainty
What is still unknown, what would change the decision, and scoped follow-ups.
```

Keep the artifact proportional but complete. Evidence paths and transfer logic
must remain visible even when the prose is concise.

## Red Flags

Stop and return to the relevant phase when any of these occur:

- proposing code, architecture, or product behavior before freezing the problem;
- searching a generic symptom before identifying its mechanism;
- presenting one precedent as the answer;
- citing many sources that repeat one underlying claim;
- preferring a library merely because it exists;
- copying source without reading its surrounding contract and tests;
- using popularity as proof of fit;
- ignoring local precedent or an authoritative primary source;
- claiming "nothing exists" without documented coverage;
- listing links without a transfer argument or decision;
- inventing without documenting why reuse, configuration, adaptation, and
  composition failed;
- broadening the task to make a precedent fit;
- continuing implementation after local proof falsifies the premise.

## Final Integrity Check

Before returning a recommendation or starting implementation, verify:

- [ ] The problem fingerprint is evidence-backed and mechanism-aware.
- [ ] The search covered every relevant evidence layer or disclosed omissions.
- [ ] The priors are credible, sufficiently independent, and version-relevant.
- [ ] Every serious prior has a complete transfer analysis.
- [ ] Counterevidence or failure modes were actively sought.
- [ ] The decision ladder was followed in order.
- [ ] The chosen status matches the available evidence.
- [ ] The local proof can falsify the chosen approach.
- [ ] Remaining uncertainty and scope boundaries are explicit.

If any required item fails, do not present the solution as grounded. Continue
safe research or return `insufficient-evidence` / `problem-not-understood`.
