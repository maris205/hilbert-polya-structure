# Quaternionic $S$-arithmetic height-clock assessment

**Candidate:** HCS-C16

**Research status:** explicit arithmetic example with scoped Route-A obstructions

**Hilbert--Pólya status:** scoped Route-A assessment; the tested baseline is not promoted

## Outcome

This project tests the compact quaternionic $S$-arithmetic space

\[
\Gamma\backslash(\mathbb H\times T_{13})
\]

as a source of a real/$p$-adic arithmetic clock. The explicit example has a
rank-two joint clock, but its regular classes belong to periodic-flat geometry
rather than to an isolated-orbit rank-one flow.

Take

\[
B=(-1,3)_{\mathbb Q},\qquad
\varepsilon=2+\sqrt3,\qquad
\pi=4+\sqrt3.
\]

The quaternion algebra $B$ is ramified at $2$ and $3$ and split at infinity
and at $13$. For the projective $S$-unit classes

\[
\gamma_{m,n}=[\varepsilon^m\pi^n],
\]

the local calculation gives

\[
\ell_\infty(\gamma_{m,n})=|mA+nC|,
\qquad
\ell_{13}(\gamma_{m,n})=|n|,
\]

where

\[
A=2\log(2+\sqrt3),\qquad
C=\log\frac{4+\sqrt3}{4-\sqrt3}.
\]

The signed clock matrix has determinant $A\ne0$. Thus the two selected local
coordinates are independent in this centralizer lattice.

## Scoped obstructions

The ratio $C/A$ is irrational. Continued-fraction convergents therefore give
primitive directions with

\[
\ell_\infty\longrightarrow0,
\qquad
\ell_{13}\longrightarrow\infty.
\]

High-precision reproducible numerical examples are:

| $(m,n)$ | $\ell_\infty$ | $\ell_{13}$ |
|---:|---:|---:|
| $(-6,17)$ | $0.04113913165$ | $17$ |
| $(-19,54)$ | $0.02425898145$ | $54$ |
| $(-44,125)$ | $0.00737883124$ | $125$ |
| $(-113,321)$ | $0.00212248772$ | $321$ |

The theorem is the continued-fraction construction, not the finite table. It
implies that the one-flat class product

\[
\prod_{\substack{(m,n)\ \mathrm{primitive}/\{\pm1\}}}
\left(1-e^{-s\ell_\infty(m,n)}\right)^{-1}
\]

has no ordinary finite, nonzero infinite-product limit for any
$\operatorname{Re}s>0$: along the proved sequence, its local factors do not
approach one.

For a bi-hyperbolic class,

\[
\operatorname{Min}(\gamma)
=\operatorname{Axis}_\infty(\gamma)
\times\operatorname{Axis}_{13}(\gamma)
\cong\mathbb R^2.
\]

The quotient of this minimum flat by the rank-two centralizer is a compact
flat torus. Its image in the arithmetic orbifold should be understood as an
immersed periodic flat, with a possible finite Weyl quotient. Closed
geodesics occur in parallel families, so an unweighted product over group
classes is not automatically a rank-one Ruelle determinant.

## Positive arithmetic structure

If $r_\gamma$ denotes the eigenvalue ratio, defined up to inversion, the
standard normalized absolute logarithmic Weil height gives

\[
H(\gamma)=\ell_\infty(\gamma)
+(\log13)\ell_{13}(\gamma)=2h(r_\gamma).
\]

This proper homogeneous scalarization is intrinsic to the chosen arithmetic
data. On the explicit centralizer flat, primitive directions modulo inversion
satisfy the proved geometry-of-numbers asymptotic

\[
N_H(R)\sim\frac{6}{\pi^2A\log13}R^2.
\]

The finite counts $36,577,9211,36857$ at $R=20,80,320,640$ are
high-precision reproducible numerical checks of this asymptotic, not exact
symbolic proofs and not evidence for a global prime-geodesic theorem.

## Spectral baseline

On the compact arithmetic surface, a normalized fixed-prime Hecke operator is
bounded, self-adjoint, and commutes with the hyperbolic Laplacian. A bounded
Hecke perturbation of $\sqrt{\Delta+1}$ retains

\[
N(T)\sim cT^2
\]

by the surface Weyl law and the min--max principle. A fixed affine rescaling
therefore cannot produce the Riemann--von Mangoldt order $T\log T$ from this
full compact-surface baseline.

This does not exclude a canonically defined sparse projection, a
conductor-growing family, a scattering construction, or a new unbounded
operator. None of those alternatives is constructed here.

## Proof and computation boundary

The mathematical proofs establish the ramification and lattice setup, the
centralizer and primitive/repetition law, the joint clock, the irrational
near-wall sequence, the one-flat divergence, the height identity and
asymptotic constant, and the bounded-Hecke Weyl statement.

The code supplies reproducible checks and finite illustrations. Algebraic
identities use exact rational arithmetic. Real logarithms and finite boundary
decisions use a high-precision `Decimal` policy; these numerical counts are not
called exact. The proofs do not depend on a finite enumeration cutoff.

## Reproduction

From this directory:

```bash
python code/s_arithmetic_clock.py --output results
python code/independent_check.py \
  --results results --output results/independent_check.json
(cd code && python -m unittest -v test_s_arithmetic_clock.py)
python code/release_manifest.py --verify
```

The release environment is Python 3.12.3 and uses only the standard library.
See `AUTO_REVIEW.md` for adversarial-review findings and remaining limitations.

## Directory guide

- `paper/`: manuscript source and compiled PDF.
- `code/`: producer, independent checker, and regression tests.
- `results/`: machine-readable certificates and numerical count tables.
- `evaluations/route_a/`: scoped internal Route-A ruling.
- `DERIVATION_PACKAGE.md`: theorem statements and derivations.
- `SOURCE_AUDIT.md`: source and novelty boundary.
- `EXPERIMENT_PLAN.md`: frozen arithmetic object, controls, and falsifiers.
- `IDEA_REPORT.md`: candidate choice and system-switch rationale.
- `AUTO_REVIEW.md`: adversarial-review record.
- `COMPILE_REPORT.md`: manuscript build validation.
- `REPOSITORY_UPDATE.md`: source commit, release tag, and verification steps.
- `results/release_manifest.json`: SHA-256 binding for the complete release
  file set.

## Claim boundary

This project is an explicit arithmetic example with scoped Route-A
obstructions. It does not construct a Riemann dynamical determinant, prove a
new general higher-rank trace formula, establish a global prime-geodesic
theorem, or rule out all Hecke/Lefschetz, non-spherical, conductor-growing,
scattering, or unbounded-operator constructions.
