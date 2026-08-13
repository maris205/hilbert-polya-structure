# HCS-C38 — Hénon \(\mu_3\) Augmentation Euler Superproduct

This project constructs a genuinely non-scalar order-three reversing
symmetry of the homogeneous area-preserving Hénon generating kernel.  Its
two-step finite-field quantization admits an integral augmentation
superdeterminant with an exact chronological trace formula and a proved,
nonzero Euler germ on

\[
\operatorname{Re}s>1.
\]

The same raw candidate is stopped exactly: its first split-prime coefficient
at \(p=7\) is nonreal, so it fails the conjugation symmetry required of a
Riemann dynamical determinant.  Exact modular controls also show that virtual
rank two does not collapse the local numerator and denominator to bounded
degree.

## Main results

- \(H_0g=g^{-1}H_0\) and \(U_pR_p=R_p^{-1}U_p\).
- \(T_p=U_p^2\) preserves the three cubic character sectors.
- The nontrivial sectors are unitarily isospectral.
- The integral augmentation factor is
  \[
  D_p^{\rm aug}(z)
  =\frac{D_{p,0}(z)^2}{D_{p,1}(z)D_{p,2}(z)}.
  \]
- Its logarithmic moments retain exact twisted Hénon chronology.
- Deligne's smooth-cubic bound gives an analytic, zero-free Euler half-plane.
- All nine split primes through 73 give exact characteristic-polynomial
  controls showing no trivial/nontrivial
  sector cancellation.
- A seven-term cyclotomic calculation proves the raw product is not of real
  type.

## Route-A decision

\[
(\mathrm{A1\_WEAK},
 \mathrm{A2\_ANALYTIC\_DETERMINANT},
 \mathrm{A3\_FAIL},
 \mathrm{A4\_NATURAL\_QUANTIZATION}).
\]

Overall: `ROUTE_A_REJECTED`.  Route B is not authorized.

The only serious successor is a separately constructed self-dual Eisenstein
object pairing \(\psi\) and \(\psi^{-1}\), with a global functional equation
and fixed-rank cohomological cancellation.  Multiplication by the conjugate
factor alone is not such an object.

## Reproduce

From this directory:

~~~bash
./code/run_c38.sh
~~~

The default runner is read-only: it regenerates artifacts under a temporary
directory, compares them byte for byte, runs the independent checker and
mutation tests, and verifies the hash manifest.

## Project layout

- `DERIVATION_PACKAGE.md`: complete mathematical chain and scope.
- `EXPERIMENT_PLAN.md`: frozen claims, controls, and stop/go gates.
- `code/`: exact producer, independent checker, tests, and runner.
- `results/`: released certificate, audit report, and summaries.
- `paper/`: compiled manuscript.
