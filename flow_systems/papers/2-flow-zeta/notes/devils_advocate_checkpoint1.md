# Devil's Advocate Report — Checkpoint 1

Audit date: 2026-08-13  
Reviewed artifact: `notes/research_protocol.md`  
Initial verdict: **REVISE**  
Post-revision verdict: **PASS WITH MAJOR GUARDRAILS**

## Critical issues

No critical issue remains. The question permits a `NOT_TESTABLE`, non-existence, or non-uniqueness outcome and therefore does not depend on successfully manufacturing a trace.

## Major issues and required resolutions

### 1. The packet groupoid was at risk of being assumed before it was sourced

- **Type:** method / construct validity
- **Problem:** calling an object the “periodic packet groupoid” does not prove that the published topological flow supplies a canonical relation, morphism class, topology, Haar system, or convolution domain.
- **Impact:** a researcher could add exactly the structure needed for a trace and then attribute the result to the frozen flow.
- **Required fix:** insert an object-reconstruction go/no-go gate. If the source does not determine the necessary relation and actions, return `NOT_TESTABLE` and name the smallest missing definition.
- **Resolution:** added to the primary sub-question, methodology, and Phase A.

### 2. Haar probability can hide the target normalization

- **Type:** target leakage / normalization
- **Problem:** even if every packet base is a compact homogeneous space with a unique invariant probability, normalizing each base separately forces mass one by definition. That does not derive a single global trace, a canonical lift through the packet fibration, or the coefficient of a fixed-point formula.
- **Impact:** the project could reproduce one Euler factor per prime while merely renaming “count every packet once” as “use probability measure.”
- **Required fix:** split the obligation into (i) invariant probability on a packet base, (ii) canonical lift/disintegration, and (iii) one global trace whose central packet-component masses are derived jointly. Do not promote completion of (i) to A2.
- **Resolution:** the protocol now contains a two-level normalization obligation and a separate `canonical packet-base probability only` outcome.

### 3. Isolated hyperbolic orbits are not automatically a specialization of clean packet families

- **Type:** false analogy / method
- **Problem:** a modular isolated orbit and a positive-dimensional clean family can have different fixed-point trace factors. Collapsing a transverse base to a point is not a theorem connecting the two categories.
- **Impact:** modular Ruelle weights could be imported into the packet problem instead of derived.
- **Required fix:** use `MOD-RUELLE` only to calibrate sign, primitive length, and repetition conventions. Call it a categorical specialization only if a common trace theorem is proved.
- **Resolution:** all “isolated specialization” language has been downgraded to coefficient-level comparison.

### 4. The convergence half-plane was preselected from the target

- **Type:** analytic circularity
- **Problem:** `Re(s)>1` is the expected abscissa after unit packet masses are known. General trace masses may change the abscissa or destroy convergence.
- **Impact:** fixing the half-plane first can smuggle the desired mass growth into the conclusion.
- **Required fix:** derive the abscissa from the trace masses and periods, then compare it with 1.
- **Resolution:** the primary sub-question and Phase D now use a derived abscissa.

## Minor issues

- The finite ledger must enumerate packet indices and repetitions, not claim to enumerate the individual orbits inside a packet. This is now explicit.
- Changing the admissibility condition violates the primary source lock. It is now a versioned sensitivity analysis performed only after the primary verdict.
- A measured/groupoid route that requires a general von Neumann-algebra programme must remain a `ROUND2_CLUE`; it cannot silently become the paper's main object.
- Root-error fields for a nonexistent determinant must be `not_applicable`, not numeric zero. The protocol already enforces this.

## Strongest counter-argument

> The proposed construction may be tautological even if every step is canonical: `Spec Z` already supplies the prime-indexed components, Haar probability supplies mass one on each component, and exponentiating the resulting formal repetition sum merely rewrites the arithmetic Euler product. Without a flow-derived trace theorem and a global normalization across packet components, no dynamical determinant has been constructed.

This counter-argument is not answered by numerical cutoff stability. It is answered only by deriving the trace domain, global component masses, and repetition coefficients from the same frozen object.

## Stress tests

| Test | Result after revision |
|---|---|
| Remove the arithmetic labels but retain an arbitrary compact equal-period bundle. | The same probability recipe may survive; this triggers `PROVES_TOO_MUCH` unless arithmetic functoriality enters the trace construction. |
| Duplicate one packet. | A global additive trace must expose multiplicity; renormalizing both copies to one fails. |
| Rescale an admissible transverse trace by `c>0`. | If all axioms survive, normalization remains non-canonical and A2 fails. |
| Remove the assumed groupoid/convolution algebra. | The protocol now stops at `NOT_TESTABLE` rather than inventing it. |
| Replace the packet family by isolated modular orbits. | Only coefficient conventions are comparable without a common trace theorem. |
| Ask for continuation before a determinant exists. | Blocked by the ordered Phase D and A2/A3 reporting rules. |
| “So what?” | A positive trace would be the first justified A1-to-A2 interface for the arithmetic survivor; a no-go theorem would convert an open multiplicity concern into a reusable obstruction. |

## Final decision

The revised question is answerable as a classification problem and the method now fails closed. Progression to literature investigation is permitted only after user confirmation of the Phase-1 choices.

[DA-DECISION: Score 5/5 | ACTION: Hold guardrails | REASON: the revisions directly address the hidden normalization, category, and analytic-circularity attacks without weakening the falsification standard.]
