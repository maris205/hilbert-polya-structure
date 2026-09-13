# Review Summary

**Problem:** construct the normalized generic cover of actual
exact-period-\(n\) cycles for
\(H_{a,c}(x,y)=(ay+x^d+c,x)\), determine its cycle monodromy, and decide
whether \(\tau\) and pointwise derivative trace \(\rho\) each generate the
cycle field.

**Initial approach:** an overly broad embedded formal-period subscheme inside
the full cyclic algebra, with normalization, special-fiber, torsor, monodromy,
and primitive-coordinate properties treated as automatic.

**Date:** 2026-08-16 UTC

**Rounds:** 2 proposal rounds plus source-lock R1

**Current gate:** `SOURCE_LOCKED_V2 / PENDING_INDEPENDENT_R2 / NO_CODE /
NO_RESULTS`

**Criteria binding:** `criteria_binding_unavailable`

## Problem Anchor

> For the normalized two-parameter Hénon family
> \(H_{a,c}(x,y)=(ay+x^d+c,x)\), with fixed integers \(d,n\ge2\), construct
> the generic cover of actual exact-period-\(n\) cycles without confusing the
> full fixed scheme, formal-period points, or special fibers; determine its
> cycle monodromy; and decide whether the cycle observables
> \(\tau=\sum_i z_i\) and
> \(\rho=\operatorname{tr}(DH_{a,c}^{n})\) each generate the generic
> primitive-cycle field.

## Round-by-Round Resolution Log

| Round | Main concern | Repair or simplification | Status after round |
|---:|---|---|---|
| 1 | formal period, actual period, full fixed scheme, and normalization were conflated | retained \(B_n\) only as the rank-\(d^n\) full algebra; moved actual exact period to the generic idempotent field \(E_n\); introduced relative normalization \(S\) | construction repaired in proposal; proof still required |
| 1 | scalar special fiber and cyclic quotient were assumed to behave well | required finite normalization, miracle flatness, same-rank comparison, nilpotent exclusion, and Reynolds base change | exact special fiber became a theorem obligation |
| 1 | monodromy comparison direction was unsafe | fixed good-special-line image as a subgroup of global image and used the time-shift centralizer for the upper bound | group argument focused |
| 1 | \(\tau\), \(\rho\), field trace, determinant, non-base, and primitive were mixed | separated observable definitions, non-base lemmas, and the later \(S_{r-1}\) maximal-stabilizer step | PC2 made auditable |
| 2 | check whether the repair created a sprawling general-Hénon project | froze exactly PC1 and PC2 for \(A=\mathbb Q[a,c]\), fixed \(d,n\ge2\), and cut every extra family/observable/scan | focus tight |
| 2 | check the \(r=1\) exception and proof boundaries | locked the exact \((2,2)\) formulas as a degree-one boundary; capped validation at three proof audits and barred machine proof claims | GO to source proof, not theorem certification |
| Source R1 | v1 lifecycle header contradicted the frozen lock; Morton (1996) direct scalar generators and Cantat--Dujardin (2026) trace-spectrum adjacency were under-disclosed | made the v2 state normative, preserved v1/R1, corrected the direct-collision map, and added a conservative post-Morton rescore without changing PC1/PC2 | `REPAIR_REQUIRED` repaired in v2; fresh independent R2 pending |

## Direct-Prior Correction

Morton (1996) is direct PC2 prior art on the scalar fiber:

- for every \(d\ge2\), the orbit-shift fixed field for \(z^d+c\) is generated
  by the scalar multiplier
  \(d^n\prod_i z_i^{d-1}=\rho|_{a=0}\);
- for \(d=2\), the scalar orbit sum
  \(\sum_i f_c^i(z)=\tau|_{a=0}\) also generates that fixed field.

These results are imported, not new.  PC2's residual delta is the passage
through PC1's two-parameter normalization, exact scalar fiber, and global
\(S_r\) cycle cover; the \(d\ge3\) \(\tau\) asymptotic remains a separate
source-proof input.

Cantat--Dujardin (2026) directly define formal-period derivative-trace
multisets and prove finite map determination from finitely many trace spectra.
That is close observable-level adjacency, but not PC2: it concerns
several-period formal spectra and finite recovery of the map, rather than one
fixed actual-period cycle cover and primitive generation of its function
field.

## Mandatory Counterexample Record

The repaired package retains four small examples because each destroys a
specific invalid inference:

1. \(f_t(z)=z^2+t\), \((t,z)=(-3/4,-1/2)\): formal period two but actual
   period one.
2. \(\mathbb Q[a,t]/(t^2-a)\): generically separable with nonreduced special
   fiber at \(a=0\).
3. \(\mathbb Q[t^2,t^3]\subsetneq\mathbb Q[t]\): same function field does
   not identify an embedded algebra with its normalization.
4. \((d,n)=(2,2)\): \(r=1\),
   \(\tau=a-1\), and \(\rho=4a^2-6a+4+4c\); degree-one primitivity is not
   nontrivial monodromy evidence.

## Overall Evolution

- The Problem Anchor was preserved verbatim.
- The dominant contribution is now geometric and precise: a single-field
  generic actual-period block, its geometrically integral relative
  normalization, its exact reduced scalar special fiber, and the full
  symmetric cycle cover.
- PC2 is dependent rather than parallel: it uses that same \(S_r\) cover to
  globalize primitive-generator conclusions whose scalar \(\rho\) case, and
  scalar quadratic \(\tau\) case, are already in Morton (1996).
- The proposal explicitly distinguishes the derivative-matrix trace \(\rho\)
  from both a field trace and \((-a)^n\), and defines both multiplication
  characteristic polynomials basis-freely on \(\bigwedge_A^rS_0\).
- The \((2,2)\) case prevents a false universal non-base formulation.
- No frontier-model primitive is forced into a pure exact-algebra problem.
- No \((d,n)\) grid, parameter scan, prime/modulus scan, or exploratory value
  table is admitted.

## Final Gate Evidence

### Majority

- novelty: 6.8 / 10
- standalone size: 7.4 / 10
- proof-completion confidence: 0.74
- verdict: GO to frozen source proof

### Dissent

- novelty: 4.5 / 10
- standalone size: 3.9 / 10
- concern: without the exact Hénon normalization/special-fiber theorem and
  separate PC2 proof, the result risks becoming a short corollary of scalar
  dynatomic monodromy

The two assessments are reported separately and are not averaged.

### Corrected independent R1 provisional range

- novelty: 4.8--5.5 / 10
- standalone size: 4.5--5.5 / 10
- disposition: leans toward the historical dissent

This conservative post-Morton range is not a consensus, an average, or a
silent replacement of either historical record.  Fresh independent R2 must
adjudicate the corrected v2 package.

## Final Status

- Anchor status: preserved
- Focus status: tight, two claims only
- Modernity status: appropriately exact and intentionally non-frontier
- Strongest component: PC1 normalized primitive-cycle cover and full
  \(S_r\) cycle monodromy
- Supporting component: PC2 separate primitive coordinates
- Direct-prior boundary: Morton scalar generators imported; Cantat--Dujardin
  formal trace-spectrum rigidity adjacent but distinct
- R1 theorem audit: no mathematical blocker
- Next authority: fresh hash-bound independent R2 of source-lock v2

## Review-Limit Disclosure

No target venue was given, so `criteria_binding_unavailable` remains active.
The role-separated refinement/review records available here use one model
family.  They may share correlated blind spots and do not count as cross-model
validation or as an independent source-proof pass.

## Artifacts

- Historical initial proposal: `INITIAL_PROPOSAL.md`
- Round-1 review: `round-1-review.md`
- Round-1 full refinement: `round-1-refinement.md`
- Round-2 review: `round-2-review.md`
- Clean final proposal: `FINAL_PROPOSAL.md`
- Score provenance: `score-history.md`
