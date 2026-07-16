# Source Ladders

Read the section matching the task's primary altitude. Use the universal source
quality rules for every task. Search adjacent altitudes only when the problem
crosses those boundaries.

## Contents

- [Universal Source Quality](#universal-source-quality)
- [Implementation and Bug Ladder](#implementation-and-bug-ladder)
- [Dependency, API, and Integration Ladder](#dependency-api-and-integration-ladder)
- [Architecture and Engineering Process Ladder](#architecture-and-engineering-process-ladder)
- [Product, Organization, and Strategy Ladder](#product-organization-and-strategy-ladder)
- [Search Construction](#search-construction)
- [Rejection Reasons](#rejection-reasons)

## Universal Source Quality

Prefer evidence in this order, adjusted for the claim:

1. Direct observation of the current system or users
2. Current local source, tests, history, traces, and decisions
3. Governing specifications, official documentation, and upstream source/tests
4. Original research, datasets, benchmarks, and first-party postmortems
5. Mature independent implementations and detailed issue discussions
6. High-quality secondary synthesis that cites primary sources
7. Community discussion, examples, and popularity signals

Authority alone is insufficient. A primary source can be stale, address another
version, or describe a different context. Verify date, version, scope, incentives,
and whether the source reports observed evidence or a recommendation.

Treat repeated reports that derive from one source as one evidence lineage.
Prefer sources with falsifiable claims, reproducible artifacts, disclosed
limitations, and a clear relationship to the mechanism under investigation.

## Implementation and Bug Ladder

Search in this order:

1. Reproduce the behavior and capture the smallest discriminating evidence.
2. Trace the local code path, state changes, events, ownership, and recent history.
3. Find similar working and failing behavior in the same repository.
4. Identify the governing platform, language, browser, framework, or dependency
   contract at the exact version in use.
5. Read upstream source, types, tests, changelog, and relevant maintainer issues.
6. Compare mature implementations that operate under similar constraints.
7. Search postmortems, historical fixes, and analogous mechanisms in other stacks.

Ask:

- Is this the same failure mechanism or only the same visible symptom?
- Which layer owns the invariant that is being violated?
- Does the proposed precedent rely on focus, timing, ordering, layout, caching,
  retries, implicit state, undefined behavior, or another hidden condition?
- Is the behavior intentional according to the governing contract?
- Did a version change introduce or retire the precedent?
- What test would distinguish the leading mechanisms?

For a UI movement bug, for example, separately investigate focus movement,
navigation or fragment behavior, explicit scroll calls, layout shifts, browser
restoration, virtualization, and component-library focus management. Do not
search "stop scrolling" and assume these mechanisms share a fix.

## Dependency, API, and Integration Ladder

Search in this order:

1. Inventory existing local dependencies and supported capabilities.
2. Verify the exact API contract, version, types, authentication, limits, and
   lifecycle in official documentation and source.
3. Inspect official examples and tests, then read failure and migration guidance.
4. Compare established alternatives with compatible maintenance and licenses.
5. Examine security history, release cadence, dependency graph, vendor risk,
   operational burden, and exit cost.
6. Compare the smallest supported integration with a bounded local implementation.

Ask:

- Does an existing dependency already provide the behavior?
- Is configuration sufficient, or is a wrapper hiding a contract mismatch?
- Does the package solve the whole requirement or one superficial part?
- What long-term ownership is added by adopting, wrapping, or building?
- Can the integration be removed or replaced without rewriting the product?

Do not equate package availability with reuse value. Reject dependency bloat,
abandoned packages, incompatible security models, and abstractions that obscure
the underlying contract.

## Architecture and Engineering Process Ladder

Search in this order:

1. Map the current architecture, owner boundaries, failure modes, and decision history.
2. Identify the invariant or quality attribute the decision must protect.
3. Read governing standards and reference architectures where they truly apply.
4. Study production postmortems and migrations, including failed or reversed ones.
5. Compare systems at similar scale, team capability, compliance, and workload.
6. Examine benchmarks and cost models with their datasets and assumptions.
7. Use distant analogues only after abstracting the shared mechanism.

Ask:

- Is the proposed pattern solving the current bottleneck or an imagined future one?
- Which constraints differ: scale, latency, consistency, staffing, regulation,
  deployment, data shape, or reversibility?
- What operational complexity and new failure modes does the precedent introduce?
- Can a thin vertical slice or reversible decision test the premise?
- Does the source report a successful result, or merely describe what was built?

Treat architecture fashion and large-company precedent skeptically. Their scale,
organizational boundaries, and tolerance for operational cost may not transfer.

## Product, Organization, and Strategy Ladder

Search in this order:

1. Start with direct user behavior, interviews, support evidence, usage data, and
   existing product constraints.
2. Identify historical attempts inside the organization and why they succeeded,
   failed, or were abandoned.
3. Study comparable products, including products that removed or reversed the idea.
4. Find original market research, experiments, financial evidence, and case studies.
5. Examine adjacent industries and historical analogues at the mechanism level.
6. Map regulatory, organizational, incentive, distribution, and timing differences.

Ask:

- Is there evidence of a user problem, or only evidence that a feature exists?
- What behavior changed after the precedent launched?
- Which selection effects, incentives, distribution advantages, or market timing
  explain the apparent success?
- What comparable attempts failed or were discontinued?
- Which parts are commodity priors and which are genuinely differentiating?
- What is the smallest falsifiable test before committing to the full idea?

Competitor parity is not product validation. A successful precedent can reveal a
mechanism or expectation without proving that the same solution belongs in the
current product.

## Search Construction

Build searches from the fingerprint rather than copying the user's wording:

- exact mechanism plus platform or version;
- invariant plus failure mode;
- official component name plus source, tests, issue, changelog, or deprecation;
- rejected or failed versions of the leading approach;
- alternative terminology used by standards or maintainers;
- the same mechanism in a distant domain;
- local symbols, error text, events, metrics, or historical commits.

After the broad pass, refine vocabulary using terms found in primary sources.
Search explicitly for evidence that contradicts the leading candidate.

## Rejection Reasons

Use concrete rejection reasons:

- different mechanism
- incompatible version or platform
- unmet precondition
- violates a local invariant or owner boundary
- unacceptable security, privacy, accessibility, or reliability risk
- dependency or operational cost exceeds the value
- evidence is stale, circular, anecdotal, or unreproducible
- source reports adoption but not outcome
- local proof falsified the transfer
- requires a materially different product or architecture decision

Do not reject a prior merely because adaptation is required. Do not accept one
merely because it is authoritative or popular.
