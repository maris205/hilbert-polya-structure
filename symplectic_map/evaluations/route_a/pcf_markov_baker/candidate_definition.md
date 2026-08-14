# Candidate definition: `pcf_markov_baker_v1`

## Status

`DESIGN_FROZEN / PRE_A0_STRUCTURAL_CANDIDATE`

This is a new candidate.  It does not reopen, tune, or repair
`henon_homotopy_v2_shadow_transport`.

## Parent and parameter provenance

Let \(u\) be the unique real root in
\((3859/2500,15437/10000)\) of

\[
u^3-2u^2+2u-2=0,
\]

and set \(d=u-1\).  For \(f_u(x)=1-u x^2\),

\[
0\mapsto1\mapsto-d\mapsto d\mapsto d.
\]

The parameter is inherited solely through this exact PCF property.  No sealed
result from the H\'enon project, prime table, multiplier match, or Riemann zero
was used to select it.

## Symbolic factor

On the invariant core \([-d,1]\), use

\[
I_0=[-d,0],\qquad I_1=[0,d],\qquad I_2=[d,1].
\]

The allowed transitions and parent-branch orientations are

\[
A=\begin{pmatrix}
0&0&1\\
0&0&1\\
1&1&0
\end{pmatrix},
\qquad
W=\begin{pmatrix}
0&0&1\\
0&0&-1\\
-1&-1&0
\end{pmatrix}.
\]

The two-sided shift \(\Sigma_A\) is the branch-history object.  Its one-sided
future itinerary factors onto the quadratic core through the usual nested
cylinder coding.  This factor is not asserted to be a smooth coordinate
projection and is not one-to-one on all partition boundaries.

## Labeled compact phase space

Let \(\lambda=\sqrt2\) and choose normalized Perron--Frobenius vectors

\[
r=\ell=(1/2,1/2,1/\sqrt2),\qquad \ell^{\mathsf T}r=1.
\]

The phase space is the compact labeled disjoint union

\[
X=R_0\sqcup R_1\sqcup R_2,
\qquad R_i=[0,r_i]\times[0,\ell_i],
\]

with the standard two-form on each rectangle.  Thus the component areas are
\(1/4,1/4,1/2\).

For every allowed edge \(i\to j\), partition \(R_i\) into a vertical strip
of width \(r_j/\lambda\), partition \(R_j\) into a horizontal strip of height
\(\ell_i/\lambda\), and map the first affinely to the second.  Source strips
are ordered by target label and destination strips by source label.  The
linear part is

\[
DB_{ij}=\operatorname{diag}
\left(W_{ij}\lambda,W_{ij}/\lambda\right).
\]

Branch interiors are exact symplectic.  A deterministic implementation uses a
declared half-open convention; the closed-boundary mathematical object is a
two-sided piecewise-affine relation.  No global \(C^1\) claim is made.

## Frozen clocks and determinant conventions

- Iteration period: \(n_\gamma\).
- Branch-baker instability clock:
  \(\ell_\gamma=\log|\Lambda_{u,\gamma}|\).
- Primary unsigned structural object:
  \(\zeta_A(z)=\det(I-zA)^{-1}\).
- Separate inherited factor-orientation diagnostic:
  \(D_{\mathrm{or}}(z)=\det(I-zW)\).
- Parent-core Artin--Mazur zeta: derived by an explicit boundary quotient.
- Parent factor-orientation-weighted zeta: a convention-specific object,
  explicitly distinct from the Lefschetz fixed-point-index zeta.

The objects above are never algebraically spliced into a Riemann-targeted
determinant.  Route-A A2 is not open.
The entries of \(W\) encode one-dimensional parent-branch orientation, not
the symplectic orientation of a two-dimensional branch and not a Maslov
phase.

## Arithmetic origin

The only claimed origin is an attributed, unverified mod-2 symbolic shadow of
the earlier quadratic-map program.  The candidate asks whether branch
resolution preserves that symbolic carrier and whether anything stronger
emerges.  It does not assume a rational-prime correspondence.

## Pre-test exact predictions

\[
\det(I-zA)=1-2z^2,
\qquad A\text{ has eigenvalues }0,\sqrt2,-\sqrt2,
\]

and the primitive orbit counts for periods 1--20 are

```text
0, 2, 0, 1, 0, 2, 0, 3, 0, 6,
0, 9, 0, 18, 0, 30, 0, 56, 0, 99
```

for a total of 226 cycles.  A primitive period \(2k\) cycle has multiplier
moduli \(2^k\) and \(2^{-k}\).  Hence its instability length is \(k\log2\),
and the corresponding multiplier-clock product, if written only as a
structural diagnostic, is predicted to reduce to

\[
Z_u(s)=\frac{1}{1-2^{1-s}}.
\]

This identity is the unsigned Euler product of the constant-slope,
unquotiented SFT/baker (initially for \(\operatorname{Re}s>1\), with its
elementary meromorphic continuation).  It is not the multiplier zeta of the
nonlinear quadratic parent.  The corresponding \(W\)-weighted SFT product is
identically one.

Also,

\[
W^3=0,\qquad D_{\mathrm{or}}(z)=1.
\]

The symbolic period-two cycle \(1\leftrightarrow2\) collapses to the parent
fixed point \(d\); it is the sole periodic boundary quotient.  Therefore

\[
\zeta_f(z)=\frac{1+z}{1-2z^2}.
\]

With the frozen branch-orientation convention, the corresponding weighted
parent object is \(1-z\).  This must not be called a Lefschetz zeta: the
interval-map Lefschetz zeta is \(1/(1-z)\).

These predictions are frozen as falsification targets, not reported results.
The parent determinant and boundary-period mechanism are also direct-prior-art
reproduction targets: the former appears explicitly for
\(K_{\sqrt2}=RLR^\infty\) in *The Real Teapot* (2025), while Hofbauer's
Markov-diagram framework already treats periodic coding discrepancies at
monotonicity boundaries.  Neither is a novelty claim here.

## General finite-clock obstruction under test

If a finite-edge Markov--baker map has finite-memory, locally constant block
lengths \(\{L_e\}_{e\in E}\) (after the standard finite block recoding),
every periodic length lies in
\(\operatorname{span}_{\mathbb Q}\{L_e:e\in E\}\).  The prime logarithms are
rationally linearly independent.  Thus such a clock contains at most the
dimension of that span many distinct exact prime logarithms and cannot
contain \(\log p\) for every rational prime.  This rules out an
exact all-prime ledger for the frozen class but not for countable-state or
non-locally-constant geometric extensions.

The finite shift and its baker realization are used only as a branch-history
carrier.  No claim is made that this zero-dimensional symbolic object is
homeomorphic to the full inverse-limit continuum of the parent map.

## Data boundaries

Allowed: exact algebraic parameter data, graph combinatorics, generated cycle
coordinates, Jacobians, branch signs, controls, source metadata, and software
diagnostics.

Forbidden: all Riemann zeros, target-zero fitting, external prime tables,
post-hoc edge lengths, post-hoc phases, manually inserted von Mangoldt
weights, sealed H\'enon test artifacts, and any code path importing the first
paper's transport implementation.

## Route status before verification

```text
A0: OPEN but analytically predicted to fail for the locally constant clock
A1: OPEN
A2: STOP_SCOPED
A3: STOP_SCOPED
A4: formal generic baker precedent only; STOP_SCOPED
Route B: forbidden
```
