# Final internal QA — P150

**Date:** 2026-09-01 UTC.  
**Status: ROUND-2 INTERNAL REVIEW ACCEPTED / HOLD_EXTERNAL.**

## Provenance correction and review closure

The earlier version of this file was an own-author round-zero QA snapshot but
used current-tense language after the Review-A repair. Its historical values
remain valid only for `main_round0_original.pdf`: 5 pages, 396,310 bytes,
SHA-256
`d94b53e9a1e496c766e8770e88f588053b7333e702b08177f0647578f90d274d`.
It is not byte-identical to current `main.pdf`.

Hostile Review A returned **ACCEPT WITH MINOR REPAIRS — 0 Critical / 0 Major /
2 Minor**. Both are fixed:

- the owner ledger is replayable and expressly subtracts the primary Lyness
  (1942) and Kanki (2013) records; and
- the proof uses a five-element orbit partition to prove integrality and
  records the `q=3` and characteristic-five boundaries.

Hostile Review B returned **0 Critical / 0 Major / 1 Minor, REVISE**. It
independently closed both Review-A items and accepted every mathematical,
source, computational, build, and visual interface. Its sole Minor was this
file's stale round-zero provenance. The current record fixes that defect;
post-closure unresolved severity is **0 Critical / 0 Major / 0 Minor**.

## Contract and proof audit

The manuscript stays inside the frozen P150 ceiling and proves every required
interface symbolically for an arbitrary odd prime power `q`.

1. **Whole-plane partition.**  The proof first removes the axes and then uses
   the ordered, mutually exclusive tests `y=-1`, `x=-1`, and `1+x+y=0`.
   Coverage is therefore pointwise; the cardinality identity is only a
   consequence.  Parameter exclusions make all exceptional coordinates
   nonzero, so the five strata are genuinely disjoint.
2. **Generic recurrence and tails.**  Each denominator in the five displayed
   rational iterates is certified nonzero by the generic-locus definition.
   The axis arrows and all three exceptional arrows are computed separately.
   Disjointness then makes tail depths `1,2,3` exact.  The boundary field
   `q=3` still has `|E_3|=1`, so the maximum tail is genuinely attained.
3. **Cycle exhaustion.**  Fixed points solve `a^2-a-1=0`; every such root is
   proved to lie in the generic locus, including the characteristic-five
   double-root case.  Inversion on the nonzero axis labels yields precisely
   two 2-cycles and `(q-3)/2` 4-cycles.  Since five is prime, every remaining
   generic state has exact period five.  The disjoint partition excludes all
   further cycles and justifies the stated zeta factors.
4. **Every-target inverse and singular tree.**  A target `(u,v)` forces the
   source second coordinate to equal `u`, leaving the single equation
   `(1+u)inv0(x)=v`.  Its three cases give the `q/0/1` fibre law without
   genericity assumptions.  Applying that law successively to every displayed
   branch proves the distinguished in-tree has neither missing vertices nor
   additional predecessors.
5. **Credit boundary.**  Classical Lyness period five, QRT and cluster
   interpretations, finite-field birational methods, and generic zeta
   bookkeeping are expressly zero credit.  The residual claim is only the
   literal zero-totalized affine completion.  A bounded source non-hit is not
   treated as novelty or ownership evidence.

## Ownership and claim ceiling

Lyness's rational five-cycle, QRT/type-`A_2` cluster interpretations,
projective denominator handling, generic finite-field birational dynamics,
Kanki's distinct extended-space/almost-good-reduction convention, and generic
functional-graph/zeta identities receive zero contribution credit. The
residual is only the literal `inv0(0)=0` all-affine scheduler together with
its exact tails/cycles, all-target fibre/image law, and complete distinguished
in-tree.

The replayed owner search is bounded. Its non-hits do not prove novelty,
priority, ownership completeness, or external clearance.

## Exact-control QA

- A fresh standard-library verifier replay matches `verification_output.txt`
  byte for byte: 31 fields, 110,095 state/target cells each, 2,144,131
  assertions, `STATUS=PASS`.
- The transcript SHA-256 is
  `f95db125148f156dd5ea4a75e2acbf22a68ed565e4c5df6c1399e018acf8f460`.

Computation is exhaustive counterexample pressure over the declared boxes,
not the proof of an all-field theorem or an ownership certificate.

## Artifact QA

| Check | Accepted current value |
|---|---|
| Current PDF | `main.pdf` |
| Pages / size | 5 A4 pages / 403,358 bytes |
| SHA-256 | `26d0a73adb71b2e303ea637b5874939914cffd53f09a2230ded5775484c33dca` |
| References | 5/5 cited and resolved |
| Isolated builds | two source-only builds, both byte-identical to `main.pdf` |
| Visual inspection | 5/5 pages accepted |
| Final log | no unresolved citation/reference, rerun request, build error, or bad box |
| Fonts / PDF | all 29 font rows embedded; A4, unencrypted, no forms/JavaScript, blank identifying metadata |

`main_round1.pdf` is byte-identical to current `main.pdf`. During this
Markdown closure, root separately froze `main_round2.pdf`; a read-only
comparison confirms that it is also 403,358 bytes and byte-identical to
current `main.pdf` at the accepted SHA-256. This closure did not create or
modify the PDF. Root subsequently regenerated and verified the final
paper-local `SHA256SUMS` manifest.

## Declarations and final decision

The manuscript contains Limitations, Data Availability, Ethics Statement,
Author Contributions, Conflict of Interest, and Funding sections and remains
anonymous. The package includes the plan, narrative, claim/evidence and
primary-source ledgers, exact verifier and frozen transcript, build record,
both original hostile reviews, consolidated `HOSTILE_REVIEW.md`, and this
current QA record.

P150 passes the round-2 internal proof, owner-boundary, exact-control,
reproducibility, and visual gates. No Git action, external posting, specialist
contact, submission, novelty/priority claim, or release is authorized.
External status remains `HOLD_EXTERNAL`.
