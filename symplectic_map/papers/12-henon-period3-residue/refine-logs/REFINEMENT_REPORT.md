# Refinement Report

**Problem:** effective low-period multiplier separation on the normalized
quartic Henon fiber whose formal fixed-point trace multiset is \(0^4\).

**Initial approach:** one quartic fiber classification and exact
period-three identity.

**Date:** 2026-08-16 UTC

**Rounds:** 2 / 3

**Final score:** 9.3 / 10

**Final verdict:** READY for independent source-lock correctness review

## Problem Anchor

The invariant anchor across both rounds is:

> determine the first formal trace period that separates conjugacy on the
> complete normalized quartic fiber whose formal fixed-point trace multiset is
> \(0^4\), together with the
> smallest degree-uniform algebraic explanation.

## Output Files

- Review summary: REVIEW_SUMMARY.md
- Final proposal: FINAL_PROPOSAL.md
- Initial proposal: INITIAL_PROPOSAL.md
- Round-1 review: round-1-review.md
- Round-2 review: round-2-review.md
- Score history: score-history.md

## Score Evolution

| Round | Problem Fidelity | Method Specificity | Contribution Quality | Frontier Leverage | Feasibility | Validation Focus | Venue Readiness | Overall | Verdict |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 10.0 | 5.0 | 5.0 | 9.0 | 8.0 | 5.0 | 5.0 | 6.7 | REVISE |
| 2 | 9.7 | 9.4 | 9.2 | 9.5 | 8.9 | 9.0 | 8.7 | 9.3 | READY |

## Round-by-Round Review Record

| Round | Main concern | Change | Result |
|---:|---|---|---|
| 1 | Exact quartic identity was sharp but looked like one elimination on a known family | Added a single all-\(m\) trace-residue mechanism, quotient coordinate, explicit slope certificate, and proof/audit contract | mechanism and paper mass repaired |
| 2 | Expansion could drift to universal separation or become protocol-heavy | Froze quartic-first structure, kept \(D_m\ne0\) open, isolated \((8,9)\) as non-evidentiary diagnostics, and relegated governance to provenance | READY without drift |

## Post-Refinement Proof Closure

The round scores above are historical proposal-review scores and are not
retroactively changed. After Round 2, the old proof risks were closed in the
current bound proof-package candidate (SHA-256
`36f2edd5a1a25960a2c656adaeb07fbd4251c61b51c9e0a0382200460b589ba9`):

1. Step 7 supplies complete root-triple Newton--Puiseux order bounds and
   trace descent, excluding the two higher invariant powers.
2. Step 9 starts from a terminating normal-form recurrence, identifies its
   Laurent expansion with a finite sum over admissible decorated tuples, and
   evaluates each local fiber by the binomial identity (9.14). The congruence,
   unique distinguished coordinate, and transfer-flow equations give the
   exact \((k,u,v)\) sum, including the separate \(j=0\) incoming-pattern
   audit and its vanishing exceptional type.
3. Step 12 independently derives \(D_2=-1572864\) by tensor Laurent residues
   before completing the quartic integer ledger.
4. Step 13 proves the local fixed-branch multiplicity needed for exact-period
   subtraction, formal exact length \(60\), and cyclewise division by three.

These are proof-package dispositions, not a SOURCE_LOCK_PASS. A fresh
independent reviewer still must verify the frozen hashes and the mathematics.

## Final Proposal Snapshot

1. Every normalized monic-centered quartic with formal fixed-point trace multiset
   \(0^4\) is \(p=(x^2-L)^2\).
2. Periods one and two are blind on that complete fiber.
3. The formal exact-period-three second trace moment is
   \(-1296000-1572864L^3\), hence an affine conjugacy coordinate and the
   minimal separator.
4. For every \(m\ge2\), the corresponding \(m\)-th deformed moment has the
   two-term form
   \(C_m\varepsilon^{3m}+D_ma^{2m-1}\varepsilon^{2m}\), with an exact
   nested-binomial certificate for \(D_m\).
5. Universal \(D_m\ne0\) remains open.

## Method Evolution Highlights

1. Replaced an isolated symbolic calculation with a weighted
   complete-intersection trace/residue proof.
2. Added only one supporting generalization, not a collection of unrelated
   claims.
3. Separated proof from implementation audit: the all-\(m\) theorem is proved
   in the bound proof-package candidate; \((8,9)\) only detects code
   disagreement and cannot substitute for source review.
4. Preserved nonreduced scheme semantics through nilpotent multiplication
   spectra and formal-cycle subtraction.

## Pushback and Drift Log

| Reviewer pressure or risk | Author response | Outcome |
|---|---|---|
| Quartic-only package lacked paper mass | accepted; added one uniform mechanism | focused upgrade |
| Temptation to claim all-\(m\) separation | rejected because universal slope nonvanishing is unproved | explicit open conjecture |
| Temptation to add height, prime, zero, or unstable-spectrum routes | rejected as anchor drift | no third contribution |
| Temptation to use a finite degree table as proof | rejected; finite tuple restricted to implementation falsification | proof/audit boundary preserved |
| Temptation to add a third engine | rejected; mismatch remains terminal | simpler and more honest audit |

## Remaining Weaknesses

1. Source-lock v2 binds every Step-7 root pattern and the complete Step-9
   recurrence/Laurent/fiber enumeration; independent v2 review is still
   required before these author proofs become implementation authority.
2. The Step-12 independent quartic derivation and Step-13 local fixed-branch
   argument must likewise survive that hash-bound review; implementation is
   not authorized beforehand.
3. Novelty is specialist and borderline rather than broad: independent
   external estimates remain 6.1--6.5/10.
4. Submission-time literature status and forward citations of the 2026 direct
   precedent must be rechecked.

## Raw Reviewer Records

The complete reviewer texts are preserved without synthesis edits in:

- round-1-review.md
- round-2-review.md

Their SHA-256 bindings are carried by the source lock.

## Next Steps

1. Preserve the source-lock v1 `REPAIR_REQUIRED` review unchanged.
2. Obtain a fresh independent v2 `SOURCE_LOCK_PASS` bound to the repaired
   strict source lock.
3. Only after that verdict, design implementation; no code or registered run
   is authorized by this refinement report.
