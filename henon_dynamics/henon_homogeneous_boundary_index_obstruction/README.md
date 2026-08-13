# HCS-C37: homogeneous Hénon boundary-index obstruction

C37 closes the anomaly-or-closure gate opened by C36 for

\[
H_0(q,p)=(-6q^2-p,q),\qquad P_0(q)=2q^3.
\]

## Main result

The scalar scaling cocycle

\[
c(a,x)=\frac{\psi(P_0(ax))}{\psi(P_0(x))}
\]

is simultaneously trivial on rational descent and on the full idele-scaling
lift.  The gauge \(\psi(P_0(x))^{-1}\) removes it before or after any
functorial quotient.  Consequently every scaling-site prime loop and every
repetition has Hénon holonomy one.

The natural boundary/index escapes also fail:

- the two pre-Poisson boundary hyperplanes have trace-class projection
  difference with essential codimension zero;
- the real cubic chirp and its log-scaling form are not VMO, with an exact
  shrinking-interval \(L^2\) oscillation lower bound \(51/100\);
- hence the standard Hardy commutator is noncompact and the usual
  restricted-Grassmannian determinant line is unavailable.

The homogeneous Mellin symbol is indeed safe in the open critical strip,
but after its fully derived gamma--trigonometric kinematics are removed the
relative scalar anomaly is identically one.  Strip safety is therefore
compatibility, not a Route-A determinant.

## Scope

The result stops the scalar functorial/standard-Hardy homogeneous anomaly.
It does not rule out a separately constructed nonfunctorial Poisson quotient
with an explicit kernel/index theorem, or a nonscalar graded/projective
cocycle.

## Route A

\[
(A1_{\rm WEAK},A2_{\rm FAIL},
A3_{\rm PARTIAL\ ANALYTIC\ STRUCTURE},A4_{\rm NATURAL\ QUANTIZATION}).
\]

Overall: `ROUTE_A_REJECTED_FOR_SCALAR_HOMOGENEOUS_ANOMALY`.

## Next large door

Scalar chirps are now too gauge-flexible.  The selected successor is a
non-scalar cubic lift: retain the three cubic/Kummer channels as a
\(\mathbb Z/3\)-graded object and test whether their monodromy survives
global Tate product formula and supplies one trace-compatible determinant.
This changes the representation category rather than tuning the stopped
scalar model.

## Reproduction

~~~bash
./code/run_c37.sh
~~~

See [THEOREM_PACKAGE.md](THEOREM_PACKAGE.md),
[DERIVATION_PACKAGE.md](DERIVATION_PACKAGE.md), and
[results/RESULTS.md](results/RESULTS.md).
