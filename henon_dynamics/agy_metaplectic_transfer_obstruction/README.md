# HCS-C25: source-standard AGY metaplectic transfer obstruction

**Date:** 2026-08-10
**Status:** `PROVED_C1_AND_L2_OBSTRUCTION; HOLOMORPHIC_GENERALIZED_TRACE_OPEN`

This round applies the C24 metaplectic obstruction to a transfer operator
that is actually fixed in the Teichmüller-dynamics literature.  The base is
the countable full-branch first-return map constructed by
Avila--Gouëzel--Yoccoz (AGY), not an averaged Rauzy transition matrix and not
another low-period cutoff.

## The large gate

Let `F=L^2(R^2)` carry the oscillator representation and let `U_gamma` be
any coherent metaplectic lift of the symplectic matrix of an AGY return
branch.  On the published bounded-derivative space

\[
E_F=C_b^1(\Delta;F),
\]

consider the unsmoothed twisted transfer operator

\[
(\mathcal L_s^U f)(x)
=\sum_\gamma e^{-s r_\gamma(x)}j_\gamma(x)
  U_\gamma f(h_\gamma x).
\]

The AGY estimates make this a bounded branch sum throughout the source
half-plane `Re(s)>-sigma_0`.  A `C^1` bump supported strictly inside one branch cylinder and
evaluation at one base point give the exact compression

\[
R\mathcal L_s^U J
=e^{-s r_{\gamma_0}(x_0)}j_{\gamma_0}(x_0)
  \varphi(h_{\gamma_0}x_0)U_{\gamma_0}\ne0.
\]

Since `U_gamma0` is unitary on an infinite-dimensional fibre, the compressed
operator is noncompact.  Thus the full operator is noncompact and nonnuclear;
it has no ordinary nuclear Fredholm determinant on this source-standard AGY
vector-valued `C^1` realization.

There is a parallel Hilbert-space statement.  Conjugating by the invariant
density gives branch probabilities `p_gamma` with sum one and a normalized
operator on `L^2(mu;F)`.  It is contractive for `Re(s)>=0`; a cylinder
projection isolates a nonzero weighted composition tensored with
`U_gamma`.  On `Re(s)=0` the operator is the adjoint of an isometric twisted
Koopman operator, hence is a coisometry with essential norm one.  This closes
the natural normalized `L^2` ordinary-determinant realization as well.  This
second obstruction is not oscillator-specific: the scalar normalized
Perron--Frobenius operator is already noncompact throughout `Re(s)>=0` by
the nonatomic branch argument, and is a coisometry on the imaginary axis.
Its role here is an independent space-level robustness test.

## No matrix-collision escape

The chronological matrix does not lose the path when the starting labeled
permutation is fixed.  For the transpose of a path matrix, the true first
Rauzy edge is the unique candidate whose winner row dominates its loser row
componentwise.  Subtracting those rows peels that edge, and the total matrix
entry sum strictly decreases.  Iteration recovers the entire word.

Consequently, distinct AGY return branches based at the same permutation
cannot acquire the same projected symplectic matrix in this four-letter
full-rank model.  Opposite choices in
the metaplectic double cover therefore cannot cancel different branch
operators.  More directly, branch-supported inputs already prevent such
cancellation before any aggregate is formed.

## Deterministic AGY section witness

The source lock uses the state

```text
top    1342
bottom 4321
```

and

```text
eta        = tbttbtbb
gamma_star = t^64 eta^8
```

The word has length 128, is a concatenation of eight complete paths, has a
maximal initial run of 65 top arrows, ends in a bottom arrow, and has
no proper prefix equal to a suffix.  For four intervals, AGY's `3d-4=8`
criterion therefore proves strong positivity, while the two neatness checks
fix one project-chosen AGY-admissible countable first-return model.  A
deterministic spanning-tree construction supplies seven integral state
frames and fourteen fixed-fibre symplectic edge matrices (six identity and
eight nonidentity), so chronological metaplectic edge lifts are genuinely
well defined.  Exact code preserves every edge and later-on-left product;
it does not numerically choose a central sign.

The independent implementation passes all eleven registered checks and
fourteen
mutation/regression tests.  As a non-proof stress sentinel, two independent
programs decode all 35,420 central first returns through elementary length 22
with zero matrix collisions.  The all-length statement comes from the row
subtraction theorem, not this finite window.

## Prior-art boundary

This release makes no blanket novelty claim for either elementary mechanism.
Kerckhoff's simplicial-system cylinders are the classical geometric
antecedent of fixed-start Rauzy decoding; C25 supplies a convention-explicit
row-subtraction inverse from one cumulative matrix.  Bonet--Gómez-Collado--
Jornet--Wolf already show, for operator-weighted composition maps, why a
noncompact point weight obstructs compactness.  C25's additional content is
the exact isolation of one weight from the convergent **multi-branch** AGY
sum, throughout the source half-plane, together with the normalized
Hilbert-space theorem.  Magee--Naud provide a nearby dynamical benchmark:
arbitrary Hilbert unitary twists support norm estimates, whereas their
ordinary Fredholm determinant is restricted to finite-dimensional twists.

Precise citations and the claim boundary are recorded in
[`SOURCE_AUDIT.md`](SOURCE_AUDIT.md) and the paper.  “Not located in the
targeted search” is not used as evidence of novelty.

## Scope

The result closes two standard unsmoothed realizations:

- the AGY `C_b^1` base regularity with the declared oscillator fibre;
- the normalized invariant-measure `L^2` Hilbert realization.

It does **not** prove that `I-z L_s` is never Fredholm, and it does not rule
out a holomorphic space without compactly supported localizers, a flat or
distributional trace, a semifinite determinant, continuous group smoothing,
or a different quantum fibre.  Those are genuinely different candidates and
must be source-locked independently.

No prime table, Riemann-zero table, time fit, unfolding, averaged transition
matrix, heat factor, or oscillator truncation is used.

## Route-A boundary

The independently validated verdict is

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)
ROUTE_A_REJECTED
```

The next authorized large switch is the precise alternative exposed by the
proof: a source-locked holomorphic/no-localizer realization or a
geometrically forced generalized trace.  Small extensions of the periodic
ledger are not authorized.

## Reproduction

```bash
python -m pip install -r requirements.txt
./code/run_c25.sh
```

Primary artifacts:

- [`SOURCE_AUDIT.md`](SOURCE_AUDIT.md) -- published-formula and scope lock;
- [`THEOREM_PACKAGE.md`](THEOREM_PACKAGE.md) -- decoder, `C_b^1`, normalized
  `L^2`, and determinant theorems;
- [`results/c25_certificate.json`](results/c25_certificate.json) -- exact
  graph, section, projective branch, and 128-step decoder trace;
- [`results/c25_independent_check.json`](results/c25_independent_check.json) --
  independent eleven-gate replay;
- [`results/RESULTS.md`](results/RESULTS.md) -- interpreted exact result;
- [`paper/main.pdf`](paper/main.pdf) -- compiled twelve-page technical note;
- [`route_a_evaluation.yaml`](route_a_evaluation.yaml) -- formal Route-A
  decision.
