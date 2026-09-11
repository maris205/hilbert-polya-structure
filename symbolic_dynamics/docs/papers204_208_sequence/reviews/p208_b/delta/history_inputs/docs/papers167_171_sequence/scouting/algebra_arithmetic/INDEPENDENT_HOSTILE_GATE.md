# Independent hostile gate — quartic inverse-span dynamics

**Reviewer:** coordinator, independently rederived after the algebra scout  
**Date:** 2026-09-03  
**Verdict:** `GREEN_OWNER_THIN / ELIGIBLE_FOR_INTERNAL_P168 / HOLD_EXTERNAL`

## 1. Literal-map and proof audit

The reviewed self-map is

```text
J(A)=span_Fp {a^(-1): a in A, a != 0},  J(0)=0,
```

on every `F_p`-linear subspace of `F_{p^4}`.  The following deductions were
checked independently of the bounded output.

1. Inversion is injective on nonzero points, so `dim J(A)>=dim A` by finite
   cardinality.  Equality makes patched inversion a bijection from `A` to
   `J(A)`, hence `J^2(A)=A`.  Conversely recurrence forces equality by rank
   monotonicity.  Thus all periods divide two.
2. The Kolomeec--Bykov classification applies to equality cases of size
   greater than two.  Lines, including binary lines of size two, are handled
   directly.  The resulting recurrent states are exactly `0`, the full field,
   scalar `F_p`-lines, and scalar copies of `F_{p^2}`.
3. For a plane `xi<1,alpha>`, the inverse projective representatives are
   `1` and `(alpha-t)^(-1)` for `t in F_p`.  Clearing denominators proves that
   any at most `deg(alpha)` of them (including `1`) are independent.  A
   non-subfield plane therefore has inverse-span dimension `min(p+1,4)`: it
   maps to a hyperplane only for `p=2`, and to the full field for every odd
   prime.  Every hyperplane maps to the full field by monotonicity and the
   equality classification.
4. Gaussian coefficients give
   `L=p^3+p^2+p+1`, `P=(p^2+1)(p^2+p+1)`, `Q=p^2+1`, and recurrent count
   `R=2+L+Q`.  Inversion on the cyclic scalar quotients gives
   `F=2+gcd(2,L)+gcd(2,Q)` fixed states and `(R-F)/2` two-cycles.
5. At `p=2`, twisted scalar equivariance and transitivity on hyperplanes make
   the 30 non-subfield-plane sources equidistribute over 15 hyperplanes, so
   each has exactly two predecessors.  Rank monotonicity excludes every other
   unlisted predecessor.  This proves the full all-time fibre atlas, rather
   than merely its total mass.

No mathematical counterexample was found.  The `p=2` size-two line exception,
zero state, full-field self-loop, non-subfield-plane nonimage, and `t>=2`
stabilization were all included explicitly.

## 2. Exact-replay audit and one repaired finding

Both scout programs were rerun from the current tree.  The 17-system breadth
program passed.  The focused verifier reconstructed `F_16`, `F_81`, and
`F_625`, enumerated all RREF subspaces, and recomputed every directed edge and
all target fibres.

The first independent replay found a real evidence-integrity mismatch:
`verify_qis.py` had gained explicit time-three/time-four fibre checks after
the initial freeze, but `QIS_CANONICAL.txt` still carried the earlier assertion
count.  The mathematical edge digests were unchanged.  The scout repaired the
canonical transcript and narrative, then ran two new processes and bytewise
comparisons.  The final counts are

```text
p=2:  1,486 checks
p=3: 18,456 checks
p=5: 12,812 checks
total: 32,754 checks
```

Final pinned hashes reported and independently spot-checked:

```text
verify_qis.py       827f84c7368d97488f9a21a270894d02a16e2000c93af062349d5c1147d9e2d9
QIS_CANONICAL.txt   01f5373f1a7801ba16b33db1bd2d71eb5d609766b0ac8dd4c1e4aed11e96f1ad
```

This finding is closed.  It is recorded because a stale successful transcript
would not satisfy the batch's exact-evidence standard.

## 3. Owner subtraction

Primary-source inspection confirms two strong direct owners:

- Kolomeec--Bykov directly classify affine subspaces whose patched inverse
  image is again an affine subspace; their theorem supplies the essential
  equality-case classification.
- Faina--Kiss--Marcugini--Pambianco and Lavrauw--Zanella directly own the
  normal-rational-curve geometry of inverse projective lines, including the
  small-field independent-tuple phenomenon.

Those facts, inverse-closed subgroup results, Gaussian subspace counts,
Singer actions, cyclic-quotient inversion, and generic zeta conversion receive
zero contribution credit.  A bounded exact-map search found no source stating
the iteration's quartic characteristic dichotomy or complete target-fibre
graph, but that non-hit has no positive novelty weight.

The retained contribution is only the integrated finite-dynamical result:

```text
sharp binary/odd temporal dichotomy
+ complete functional graph and image stabilization
+ complete all-time, every-target fibre atlas.
```

This is narrower than the author-side description and must remain visibly
owner-dependent.

## 4. Internal collision audit

The closest occupied papers do not transfer the retained conjunction.

- P109 uses images under one fixed nilpotent linear map and decreasing Jordan
  flags; QIS is a rational pointwise span with increasing rank and scaled
  subfield recurrence.
- P102 uses a nonlinear group-algebra norm on elements; inversion on scalar
  quotients appears here only after the recurrent subspaces are classified.
- P137's rank is a feedback selector; QIS has no rank-dependent branch in its
  definition.
- P165 shortens coordinate codes using low-weight supports; QIS is
  coordinate-free and its binary anomaly is projective-line cardinality.

Generic subspace, rank, period, fibre, and zeta vocabulary earns no separation
credit.  The literal map and both operative proof axes remain distinct.

## 5. Decision and hard ceiling

The candidate clears the internal mathematical and value gate at
`GREEN_OWNER_THIN`.  It may be drafted as P168 only if the manuscript:

1. states the two direct geometric inputs before the residual claims;
2. does not claim the recurrent classification or inverse-line geometry as
   new;
3. presents the sharp characteristic anomaly and full fibre graph as the
   residual;
4. retains `HOLD_EXTERNAL` and no novelty/priority wording; and
5. undergoes two manuscript-level hostile reviews after Round 0.

A later direct owner of the literal iteration or its full graph reopens the
slot immediately.
