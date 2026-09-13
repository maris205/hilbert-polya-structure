# Pipeline Summary

**Problem:** normalized actual primitive-cycle cover, monodromy, and natural
cycle-field coordinates for a two-parameter Hénon family.

**Final method thesis:** for fixed \(d,n\ge2\), the generic actual
exact-period block of
\(H_{a,c}(x,y)=(ay+x^d+c,x)\) admits a geometrically integral, finite locally
free relative normalization with exact scalar dynatomic special fiber and full
\(S_r\) cycle monodromy; either \(\tau=\sum z_i\) or the pointwise derivative
trace \(\rho\) separately generates its cycle field.

**Current verdict:** `SOURCE_LOCKED_V2 / PENDING_INDEPENDENT_R2 / NO_CODE /
NO_RESULTS`.  Historical majority and dissent remain preserved.

**Date:** 2026-08-16 UTC

**Criteria:** `criteria_binding_unavailable`; no venue-fit claim.

## Final Deliverables

- Proposal: `refine-logs/FINAL_PROPOSAL.md`
- Review summary: `refine-logs/REVIEW_SUMMARY.md`
- Refinement report: `refine-logs/REFINEMENT_REPORT.md`
- Experiment plan: `experiments/EXPERIMENT_PLAN.md`
- Experiment tracker: `experiments/EXPERIMENT_TRACKER.md`

The experiment artifacts live under `experiments/` because the task-specific
path overrides the pipeline skill's default `refine-logs/` location.

## Contribution Snapshot

- **Dominant contribution (PC1):** full cyclic algebra, generic actual-period
  field, geometrically integral relative normalization, exact \(a=0\) special
  fiber, cyclic quotient, and full \(S_r\) cycle monodromy.
- **Supporting contribution (PC2):** lift scalar generator inputs through the
  two-parameter cover, supply uniform \(\tau\)-generation for all \(d\)
  (especially the separate \(d\ge3\) step), and construct basis-free
  irreducible degree-\(r\) multiplication characteristic polynomials in
  \(A[T]\) for \(\tau\) and \(\rho\).
- **Explicitly rejected complexity:** arbitrary Hénon maps, global embedded
  formal-period schemes, every-fiber smoothness, projective compactification,
  extra observables, computational grids, and external-data scans.

## Must-Prove Claims

1. PC1 in its complete normalized and special-fiber form.
2. PC2 with separate non-base proofs, the later \(S_r\)-stabilizer step, and
   the explicit \((2,2)\) boundary.

## First Audits

1. A1: algebra, actual/formal separation, normalization, and exact special
   fiber.
2. A2: cyclic quotient and correctly directed monodromy comparison.
3. A3: \(\tau/\rho\) categories, separate non-base lemmas, primitive
   stabilizers, and degree-one boundary.

These are proof audits, not GPU experiments.  No code or registered run is
authorized.

## Direct-Prior Boundary

- Morton (1996), p. 336, already gives the scalar fixed-field generator
  \(\rho|_{a=0}\) for every \(d,n\); Corollary 3 and p. 336 give
  \(\tau|_{a=0}\) for \(d=2\).  These scalar generators are imported, not
  claimed as new.
- Cantat--Dujardin (2026), Section 3.2 and Theorem A/Theorem 3.7, give direct
  formal-period trace-spectrum adjacency across finitely many periods for
  parameter reconstruction.  PC2 instead concerns one fixed actual period and
  primitive generation of one cycle field.

## Main Risks

- **Special-fiber risk:** normalization/base change could be asserted too
  quickly.  Mitigation: same-rank comparison plus flat nilpotent exclusion and
  the \(t^2-a\)/cusp falsifiers.
- **Monodromy risk:** subgroup direction or branch hypotheses could be wrong.
  Mitigation: freeze both the special-line lower bound and centralizer upper
  bound.
- **Primitive-coordinate risk:** non-base might be confused with primitive.
  Mitigation: separate infinity-word lemmas followed by the maximal
  \(S_{r-1}\) argument.
- **Novelty risk:** PC2 may read as corollary-like after Morton.  Mitigation:
  lead with PC1, state the imported scalar results exactly, and restrict the
  residual delta to the two-parameter lift, all-\(d\) \(\tau\), and integral
  basis-free \(A[T]\) characteristic polynomials.
- **Review risk:** same-family review can correlate errors.  Mitigation: fresh
  independent source review; no claim of cross-model validation.

## Gate Record

- majority: novelty 6.8/10, standalone size 7.4/10, proof confidence 0.74,
  GO;
- dissent: novelty 4.5/10, standalone size 3.9/10, STOP/MERGE concern.
- corrected independent R1 provisional range: novelty 4.8--5.5/10,
  standalone size 4.5--5.5/10, leaning dissent.

The corrected range is neither a consensus nor a replacement for the
historical records.

## Next Action

Preserve v1 and its R1 review, bind the corrected files into v2, and obtain a
fresh hash-bound independent R2 `SOURCE_LOCK_PASS`.  Do not invoke
`/run-experiment`, create code, or execute a registered audit before that gate.
