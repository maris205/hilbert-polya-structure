# Internal hostile review — P91

Audit date: 2026-08-28 UTC
Disposition: **internal GO / external HOLD**
Reviewer status: an independent-in-workflow internal audit by an agent that
did not write the initial P91 draft. This document is not and does not claim
to be external peer review.

## Round 1 — attack of the submitted draft

### Findings and implemented repairs

1. **The row orientation was vulnerable to a silent transpose.** The proof
   now displays both reflection conjugations and states explicitly that the
   matrix acts on column functions by row sums. Literal group-law code is
   compared entry by entry with the canonical directed matrix.
2. **The spectral factorization did not close its dimension ledger.** The
   revision names `V_0`, `V_t`, and `V_Q`, proves invariance and mutual
   disjointness, and records
   `(2N-c-2)+(c-1)+3=2N`. The nonzero cubic constant and `t>0` then give rank
   `c+2`, rather than leaving rank implicit.
3. **The endpoint `N=t` was incompletely separated.** It is now identified as
   the `2N`-symbol full shift, with all-ones adjacency matrix, characteristic
   polynomial, entropy `log(2N)`, and zeta `1/(1-2Nz)` stated explicitly.
4. **The first two trace formulas were quoted too quickly.** The proof now
   gives `tr Q=2t` and `tr Q^2=2t(N+t)` before adding the repeated
   `t`-eigenvalues, and verifies the endpoint reduction.
5. **The rigidity root and reverse implication needed admissibility details.**
   With `S=F_1`, the genuine root satisfies `t<=S/2`, whereas the other root
   is `3S/2-t>=S`. The reverse direction now constructs bijections on `R_T`,
   `R_U`, the coset index set, and each coset fiber, yielding an explicit
   directed graph isomorphism.
6. **The control checked outcomes but not the invariant spaces themselves.**
   It now checks basis vectors of the zero spaces, the coset-difference
   `t`-eigenspace, and each quotient basis vector. A twentieth presentation
   adds a second nonisomorphic collapse at `(N,t)=(16,4)`.
7. **Owner language was stronger than its evidence.** The manuscript now
   dates the bounded search, calls it non-exhaustive, and makes no absolute
   priority claim.

Round-1 control after these repairs: **12,175 exact assertions**, all passed.
The revised PDF compiled without errors.

## Round 1 independent derivation ledger

- In `A semidirect {0,1}`, rotation conjugation of `(a,1)` gives
  `(a+2y,1)`, while reflection conjugation gives `(2y-a,1)`. Requiring the
  result to equal the involution `(a,1)` yields `y in A[2]` and `y in a+A[2]`
  respectively. This matches the three directed successor classes.
- The identity rotation is reachable from every vertex, reaches every
  vertex, and has a loop; the adjacency matrix is therefore primitive.
- On functions constant on `R_T`, `R_U`, and all reflections, direct row sums
  give
  `Q=[[t,N-t,N],[0,0,N],[t,0,t]]`.
- Internal zero-sum vectors are killed, reflection-coset differences have
  eigenvalue `t`, and the quotient has the displayed cubic. The dimensions
  exhaust all `2N` coordinates, so no hidden spectral block remains.
- Substituting `lambda=1/z` into the characteristic factor, or computing
  `det(I-zM)`, gives the stated zeta signs. Direct traces give `F_1=N+t` and
  `F_2=t(3N+t)`.
- Period counts recover `(N,t)` by the admissible quadratic root. Equal
  parameters give isomorphic canonical directed graphs and hence a one-block
  conjugacy; the claim is only within this family.

No contradiction was found in these rederivations.

## Round 2 — reattack of the repaired draft

The second pass targeted the trivial group, all elementary-two endpoints,
empty `R_U`, divisibility of `t`, zeta signs, and the possibility of a second
admissible quadratic root.

- The text now records that `T=A[2]` is a subgroup, so `t` divides `N` and
  `c=N/t` is a positive integer.
- For `N=t`, the semidirect action is trivial, `G` is abelian of exponent two,
  and every ordered pair satisfies the relation; the all-ones endpoint and
  all first-period formulas are consistent even for `N=t=1`.
- For `N>t`, the second quadratic root is at least `S`, so it cannot meet
  `x<=S/2`; uniqueness does not depend on a numerical approximation.
- The exact controls again passed all 20 presentations, including both
  same-parameter/nonisomorphic pairs.
- Log, citation, font, text-extraction, and four-page visual inspections found
  no production defect.

No further theorem change was required in Round 2.

## Bounded owner/scope audit

Queries through 2026-08-28 combined `generalized dihedral`, `reverser graph`,
`reversing relation`, `hgh^{-1}=g^{-1}`, `shift of finite type`, `spectrum`,
and `zeta`. The search recovered literature on reversing symmetries and on
commuting graphs of generalized dihedral groups, but no direct treatment of
this exact directed relation shift or its `(N,t)` zeta/rigidity package.

This negative result is only a bounded keyword check. The group calculations,
equitable decomposition, and SFT determinant identity are classical, so an
unindexed or differently named owner remains plausible. The manuscript
therefore avoids an absolute novelty claim.

## Residual risks and verdict

- **Mathematics:** low residual risk after complete spectral rederivation,
  endpoint separation, and exact group/canonical cross-checks.
- **Scope:** low if rigidity remains explicitly restricted to the reverser
  shifts `X_A` constructed here.
- **Owner/novelty:** medium because the exact object may appear under
  different relation-graph terminology.
- **Verdict:** GO for internal Stage 2 use; HOLD for posting, submission, or
  priority language.
