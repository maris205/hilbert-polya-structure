# HCS-C31 devil's-advocate audit

## Executive verdict

**GO** for the chronological cylinder-pressure certificate and explicit
geometric bridge.  **NO-GO** for presenting the resulting positive real root,
generic BPS nuclearity, or finite-section stability as an arithmetic
breakthrough.

The pressure route supplies a standard invariant whose certified bracket
contains the large stable finite-section signal.  That is a substantial
result, but also a negative Hilbert--Pólya control: the old value is consistent
with expected pressure geometry and is not independent arithmetic evidence.

## 1. A finite-section zero is not an infinite zero

The old number \(0.277982981676189\ldots\) is a zero of a degree-truncated
cycle section after setting \(z=1\).  It was not a proved Fredholm determinant
zero, suspension-zeta pole, or pressure root.

**Response required:** compute pressure independently from cylinder
envelopes.  The new certified result is

\[
\frac{277980}{10^6}<h_*<\frac{277987}{10^6}.
\]

The old value lies inside, so pressure explains it to certified resolution.
This does not prove that the finite cycle sections converge at the boundary.

## 2. A periodic representative does not bound a cylinder

A length-\(13\) word has infinitely many past/future extensions.  Closing it
periodically produces one point, not its roof extrema.

**Response required:** store

\[
\tau_e^-\le\tau(x)\le\tau_e^+
\qquad(x\in[e])
\]

for every extension, using direct interval graph transforms or a proved
representative-plus-tail estimate.

## 3. The matrix order is easy to reverse

For \(s>0\), a larger roof gives a smaller weight.  Thus

\[
L_s^-:e^{-s\tau_e^+},
\qquad
L_s^+:e^{-s\tau_e^-}.
\]

Reversing this convention gives a plausible but invalid interval.  The checker
must test a constant-roof system and mutate the endpoint assignment.

## 4. The slope improvement could be circular

The inequality

\[
M\le\frac{a_0}{\sqrt{17}-rM}
\]

contains \(M\) on both sides.

**Response required:** define \(M=\max|\mu^u|\) by compactness, retain the
inherited \(M\le1/2\), solve the exact quadratic, and exclude the large root
\(a_0/\rho_0>1/2\).  Only then conclude

\[
M\le a_0\rho_0,
\qquad
J^u_{\rm ad}\ge\rho_0^{-1}.
\]

## 5. Adapted expansion is not Euclidean expansion

The multiplier \(|-12q-r\mu|\) uses a nonunit adapted frame.  Hausdorff
dimension uses the Euclidean geometric potential.

**Response required:** retain

\[
DH_6e^u_{\rm ad}
=\lambda e^u_{\rm ad}\circ H_6
\]

and the nonzero coboundary

\[
\tau_E^u-\tau_{\rm ad}
=b_u\circ H_6-b_u.
\]

Periodic sums and pressures agree; pointwise roofs generally do not.

## 6. R059 did not state local maximality

Conjugacy plus uniform hyperbolicity is not a substitute for checking every
basic-set hypothesis.

**Response required:** use strict interior realization to prove

\[
\Lambda_*=\operatorname{Inv}(\operatorname{int}N).
\]

Together with \(A^4>0\), R058 hyperbolicity, and R059 conjugacy, this gives a
local mixing hyperbolic basic set.

## 7. The old compact-ambient objection is resolved by local theorems

McCluskey--Manning state their theorem for a basic set of an Axiom-A
diffeomorphism of a compact surface without boundary.  Applying that literal
formulation directly to the certified map on \(\mathbb R^2\) would create a
scope gap.

**Resolution:** Pesin--Sadovskaya (2001), Remark 4.1 (printed page 284), is
stated for a \(u\)-conformal diffeomorphism on a locally maximal hyperbolic
set and gives the unstable-slice dimension as the zero of the unstable
geometric pressure.  One-dimensional \(E^u\) makes conformality automatic.
Barreira (2013), Introduction, Theorem 1.2, is stated for a locally maximal
hyperbolic set of a \(C^1\) surface diffeomorphism with one-dimensional stable
and unstable bundles and gives the total dimension as the sum of the two
pressure roots.  Theorem 4 supplies local maximality, and Theorems 3 and 7
supply the correct Euclidean potentials and equality of roots.  Hence:

~~~text
local_basic_set: PROVED
unstable_dimension: PROVED
total_dimension: PROVED
~~~

The 1985 erratum deletes the old bifurcation theorem, not the slice-pressure
theorem.  McCluskey--Manning remains useful context, but it is not the source
used to cross the local dimension interface.

## 8. Area preservation alone does not say “twice the root”

The stable and unstable pointwise Euclidean Jacobians are not simple
reciprocals when the bundle angle varies.

**Response required:** retain

\[
J_E^u(z)J_E^s(z)
\frac{\sin\alpha(H_6z)}{\sin\alpha(z)}=1
\]

and

\[
\tau_E^s=\tau_E^u-g+g\circ H_6,
\qquad g=\log\sin\alpha.
\]

Both exact theorem interfaces now apply, so one may state
\(\dim_H\Lambda_*=2h_*\).  Area preservation alone would not have justified
that conclusion; the angle coboundary and the two source theorems remain
essential.

## 9. The absolute \(z\)-radius is weight-specific

The instability-weight trace has the exact certified radius

\[
|z|<
\frac{J_*}{\varphi}
=\frac{\sqrt{17}+\sqrt{13}}{1+\sqrt5}
=2.388286326\ldots .
\]

This improves the inherited \(2.132\ldots\) bound.  It is not the BPS flat
trace weighted by \(|\det(I-DH_6^n)|^{-1}\); the separate scalar-BPS radius near
\(1.312\ldots\) is weaker and answers another question.

## 10. Generic BPS all-word nuclearity is not new

Once the analytic Hénon rectangles and one-step pinning maps meet the BPS
hyperbolic-model hypotheses, unique iterated pinning coordinates,
chronological word kernels, nuclearity of order zero, and the flat-trace
Fredholm identity follow from the classical BPS results.

**Response required:** do not sell “one step to all words,” generic
nuclearity, or a generic trace identity as C31 novelty.  Potential novelty
begins with useful explicit tails or the end-to-end Hénon pressure certificate.

## 11. Pressure is not arithmetic

For a positive Hölder roof, the unique solution of \(P(-s\tau)=0\) is standard.
A leading suspension-zeta pole there is expected under the relevant zeta
theorem; non-lattice behavior controls other boundary points.

The strict Route-A conclusion remains

~~~text
(A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)
overall: ROUTE_A_REJECTED
Route B authorized: false
~~~

The separate ledger statuses
`pressure: NUMERICALLY_CERTIFIED` and
`analytic_pressure_implication: PROVED` do not create a new A2 grade.

There is no prime correspondence, functional equation, critical-line theorem,
Riemann--von Mangoldt law, or self-adjoint operator.

## Final go/no-go

Proceed with C31 as a rigorous pressure/Bowen gate and negative identification
theorem.  If cylinder containment or outward Perron signs fail, report that
obstruction.  Do not replace it with a looser attractive root plot.
