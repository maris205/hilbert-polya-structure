# Preregistration — SD-C31

Freeze date: 2026-08-14 UTC, before manuscript integration.

This file transcribes the frozen exact-counterterm preregistration.  It does not retroactively widen the tested class after observing controls.

## Question

Can a source-natural finite-cutoff subtraction remove only the diagonal prime-harmonic divergence of the Paper 28 critical quadratic ledger while retaining a mixed invariant that is specific to the divisibility source?

## Frozen construction

For a finite pointed poset with zeta matrix (Z), Möbius inverse (M=Z^{-1}), positive diagonal metric (W), and source covers (A(P)), define

\[
q_x=ZE_xM,
\qquad
G_{xy}=\operatorname{Tr}(q_xq_y^\sharp),
\qquad
X^\sharp=W^{-1}X^*W.
\]

On the critical line the finite quadratic ledger is

\[
Q_F(t)=D_F+M_F(t),
\quad
D_F=2\sum_{x\in F}\frac{G_{xx}}{\nu(x)},
\]

\[
M_F(t)=4\sum_{x<y\in F}
\frac{G_{xy}}{\sqrt{\nu(x)\nu(y)}}
\cos\!\left(t\log\frac{\nu(y)}{\nu(x)}\right).
\]

For the divisibility baseline, the analytic Gram is frozen at
\(eta=2\) in units of (C_\eta):

\[
g_{pp}=1+p^{-4},
\qquad
g_{pq}=\bigl((p^4+1)(q^4+1)\bigr)^{-1}
\quad(p\ne q).
\]

## Admissible counterterm class

A tested counterterm is:

1. real and quadratic in the active coefficient field;
2. reference-independent along the frozen active-cutoff tower;
3. additive over atoms and unordered atom pairs;
4. local to at most two atoms;
5. linear in native Gram contractions on each local pair;
6. equivariant under transported pointed-poset isomorphisms and compatible with the declared cutoff embeddings.

It may depend on the rooted one- or two-atom incidence/roof/Gram type.  It may not inspect printed numeric atom names, primality, target zeros, an arithmetic lookup table, or coefficients tuned after viewing the baseline.

The two minimal diagonal schemes are

\[
C_{\mathrm{full},F}=2\sum_{x\in F}\frac{G_{xx}}{\nu(x)},
\qquad
C_{\mathrm{lead},F}=2C_\eta\sum_{x\in F}\frac1{\nu(x)}.
\]

Their difference is a convergent atom-local shift.  At
\(eta=2\), the frozen family of extra shifts is

\[
S_{k,F}=2C_\eta\sum_{x\in F}\nu(x)^{-(5+k)},
\qquad k=0,1,2,
\]

with coefficients chosen from the preregistered rational grid.

## Primary claims and gates

### C1 — finite-part nonuniqueness

Pointed-isomorphism naturality and cutoff compatibility determine the leading divergent germ but not the finite part.  The `full` and `lead` schemes are both admissible and differ by a nonzero convergent local shift.  Exact diagonal decomposition, transport, prefix compatibility, rational Cauchy tails, and distinct residual values are required.

### C2 — arithmetic-selectivity no-go in the frozen class

After either diagonal subtraction, the surviving mixed Fourier ledger is a two-atom Gram invariant.  A local natural multiplier preserving it on the divisibility baseline also preserves it on matched controls; cancelling that local control mechanism cancels the baseline mechanism.  The gate requires nonzero baseline mixed and fourth-order ledgers, exact relabel invariance, mutated-cover/composite-only/generic-DAG/random-inventory controls, preregistered coefficient enumeration, and an independent symbolic coefficient contradiction.

### Ownership

The honest functional
\(\det_3(I-z\mathcal B_s)\) deletes powers one and two.  Chiral parity deletes odd powers, so the first visible logarithmic coefficient is order four.  A restored quadratic finite part defines

\[
\mathfrak D_{\mathcal R}(s,z)
=\det{}_3(I-z\mathcal B_s)
\exp\!\left[-\frac{z^2}{2}
\operatorname{FP}_{\mathcal R}\operatorname{Tr}(\mathcal B_s^2)
\right].
\]

This is a new, scheme-dependent holomorphic functional.  It is not an ordinary Fredholm determinant and not
\(\det_2\).  Reflection symmetry is tested coefficientwise.  The quadratic exponential is zero-free in (z), so it does not change the auxiliary-(z) divisor of
\(\det_3\).

## Frozen controls

The run order is: divisibility sanity checks; baseline cutoffs (12,18,30); relabeled copies; compatible-prefix checks; a mutated-cover fixture; a composite-only fixture; a seeded generic DAG (`29031`); a seeded random inventory/star control (`29032`); coefficient enumeration; ownership checks; independent evaluation; unit tests; and a fresh double run.

## Interpretation rule

`GO` means that scoped source-natural diagonal finite parts exist and their finite-scheme freedom can be classified.  `STOP` means that no tested local rule turns the residual mixed Gram phase into an arithmetic selector.  Neither outcome may be upgraded to a universal no-go for arbitrary global isomorphism invariants.
