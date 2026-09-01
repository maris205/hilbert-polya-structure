# P31 Devil's Advocate Report — Checkpoint 1

Date: **2026-09-01 UTC**  
Review mode: **independent cross-review of Phase-1 scoping only**  
Reviewed artifacts: `stage1_phase1_rq_brief.md` and
`stage1_phase1_methodology_blueprint.md`

## Verdict: REVISE

The object typing, finite source lock, exact-witness requirement, inverse/power
separation, and A1-only kill gates are strong. No Critical issue was found.
Two Major ambiguities nevertheless prevent the current design from answering
its own “unique-owner taxonomy” RQ without an analyst-dependent aggregation
choice. They must be repaired before Checkpoint 1 can pass.

## Critical issues

No Critical issues identified.

## Major issues

### P31-DA-1 — “Unique owner” and cell-local no-double-credit are different estimands

- **Severity:** Major
- **Type:** Scope / method / construct validity
- **Location:** RQ Brief, “No-double-credit rule”; Methodology Blueprint,
  “Primary multiplicity” and P5.
- **Problem:** The design calls the output a unique-owner taxonomy, but the
  primary view counts one owner once in every `(source word, prime, Hecke
  degree)` cell. The same global oriented owner may therefore receive primary
  credit in multiple source-word/prime groups. That may be the correct Hecke-
  incidence estimand, but it is not a global unique-owner quotient. The files do
  not freeze how cross-group appearances enter the three group-law moments,
  their denominators, or their kernel predicates.
- **Impact:** A taxonomy change could be caused by the chosen grouping and
  weighting operator rather than by newly resolved primitive ownership. Two
  implementations could share the same exact owner ledger yet report different
  “owner-level” laws without violating the current prose.
- **Required revision:** Separate and name at least two exact objects:
  `(i)` a global oriented-owner quotient with one row per owner and `(ii)` a
  correspondence-incidence table keyed by owner, source word, prime, branch,
  and degree. Freeze equations for all three recomputed laws, including the
  summation index, unit of analysis, denominator, conflict propagation, and
  treatment of one owner appearing in multiple groups. Rename the primary
  estimand if cell-local incidence, rather than global owner uniqueness, is
  intended.

### P31-DA-2 — The negative conjugacy certificate is promised, not yet operationally specified

- **Severity:** Major
- **Type:** Feasibility / method
- **Location:** FINER Feasible `5/5`; Methodology Blueprint P3–P4 and the
  unresolved-pair kill gate.
- **Problem:** P3 says the integral intertwiner problem will be reduced to a
  Pell-type equation, reduced modulo the centralizer, and searched over a
  complete cycle. It does not freeze the exact reduction theorem, termination
  invariant, candidate-pair universe, negative-certificate schema, or the
  conditions under which the proposed reduction is valid. A finite input panel
  does not by itself make nonconjugacy decidable by the described implementation.
- **Impact:** The method may prove positive merges while leaving negative rows
  unresolved. Because the RQ asks what closed taxonomy remains and requires
  zero unresolved rows, the claimed `5/5` feasibility and the primary endpoint
  are currently more confident than the method warrants.
- **Required revision:** Mark solver feasibility as provisional pending Phase-2
  source verification; freeze the exact conjugacy-decision theorem and its
  preconditions before execution; specify the complete set of pair buckets and
  the machine-checkable fields of both positive and negative certificates.
  Define the scientifically valid fallback endpoint if completeness cannot be
  established—an explicit “ownership ledger not closed” obstruction, not a
  partial taxonomy—and reduce the Feasible score unless the complete procedure
  is independently established.

## Minor issues

### P31-DA-3 — Adversarial fixtures are not actually frozen

- **Severity:** Minor
- **Type:** Reproducibility / moving-goalpost risk
- **Location:** “Frozen controls,” final paragraph.
- **Problem:** Fixtures are said to be selected by fixed height/lexicographic
  order, but the height function, height bound, fixture count, exact subgroup-
  split construction, and public manifest are absent.
- **Recommendation:** Freeze a fixture-generation specification and manifest
  before outcomes: height definition, bounds, counts by fixture type, expected
  verdicts, and hashes. Do not select additional fixtures after collision
  classes are visible.

### P31-DA-4 — “Independent” verification could share the same theorem defect

- **Severity:** Minor
- **Type:** Reliability
- **Location:** certificate layer and target-blind plan, Steps 5–6.
- **Problem:** Byte-identical rebuilds test determinism, not correctness, and a
  read-only verifier can reproduce the same mistaken reduction assumptions.
- **Recommendation:** Require the verifier to check witness equations and
  completeness certificates from a separately stated mathematical contract;
  include small exhaustive fixtures for which subgroup conjugacy can be decided
  by an independently bounded enumeration.

## Observations and strengths

- Inversion, primitive powers, Hecke degree, and incidence multiplicity are
  correctly treated as separate typed fields.
- A degree conflict has a genuine kill gate instead of an outcome-dependent
  tie-breaker.
- The design correctly refuses to turn a finite owner ledger into an Euler
  product or A2 result.
- An unchanged taxonomy is explicitly admissible, reducing positive-result
  bias.

## Strongest counter-argument

> This is not yet a unique-owner experiment: it constructs global owner IDs but
> then permits the same owner to be credited once in every Hecke cell, so the
> reported kernel taxonomy can be a property of the chosen incidence grouping
> rather than of primitive ownership.

The current blueprint does not defeat that criticism because it does not state
the exact aggregation equations or distinguish global-owner and cell-incidence
estimands in the output contract.

## What's missing

1. Exact formulas for each of the three recomputed scalar-law moments and kernel
   predicates after owner canonicalization.
2. A global-owner-to-correspondence-incidence schema and an explicit rule for
   owners occurring across multiple source-word/prime groups.
3. The theorem, preconditions, termination measure, and negative-certificate
   schema for the full `Gamma_0(11)` conjugacy decision.
4. A complete candidate-pair accounting identity showing which of the
   `138 choose 2` pairs are ruled out by invariants and which receive a witness
   or nonconjugacy certificate.
5. A frozen adversarial-fixture manifest with exact selection bounds.
6. A predeclared fallback artifact for a scientifically honest but unclosed
   owner ledger.

## Stress-test results

| Test | Result | Reason |
|---|---|---|
| Remove the inherited `2/2/134` taxonomy—does the RQ still stand? | PASS | Exact owner closure remains meaningful, although the comparison endpoint becomes less informative. |
| Flip the expected result—could all 138 instances be distinct owners? | PASS | The design admits zero collisions and an unchanged taxonomy. |
| Duplicate one owner across two source-word/prime groups—does the primary estimand remain unambiguous? | **FAIL** | Cell-local unit weighting and “unique-owner” language give no single frozen global aggregation rule. |
| Give one owner two degrees inside one group—does the design resist repair by fiat? | PASS | `OWNER_DEGREE_CONFLICT` stops the degree-moment recomputation. |
| Supply a same-trace pair with no conjugator found inside a large bound—can the method issue a valid negative decision? | **FAIL until revised** | Bounded failure is correctly rejected, but the complete negative-certificate procedure is not operationally frozen. |
| Change the ambient subgroup from `Gamma_0(11)` to `PSL(2,Z)`—does the result generalize? | NO, appropriately | The simpler-parent quotient is a control and cannot replace subgroup ownership. |
| “So what?”—is the significance justified? | PARTIAL | Closing the A1 accounting gap matters, but the paper must first separate global owners from repeated Hecke incidences. |

## Issue dispositions required for Checkpoint-1 replay

| Issue | Required disposition | Checkpoint effect |
|---|---|---|
| P31-DA-1 | **Must revise:** freeze global-owner and correspondence-incidence schemas plus exact aggregation equations; rename the estimand if necessary. | Blocks PASS while unresolved. |
| P31-DA-2 | **Must revise:** bind a complete conjugacy-decision contract and honest fallback endpoint; recalibrate feasibility. | Blocks PASS while unresolved. |
| P31-DA-3 | **Should revise before execution:** publish the frozen fixture manifest and selection rule. | Minor; does not alone block progression. |
| P31-DA-4 | **Should revise before execution:** make verification contract-independent and add exhaustive small fixtures. | Minor; does not alone block progression. |

## Checkpoint conclusion

Checkpoint 1 should be replayed after the two Major revisions. No Phase-2
source work, computation, claim registration, or Route promotion is authorized
by this review.
