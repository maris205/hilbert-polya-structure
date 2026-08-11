# HCS-C31 research question: the Bowen-pressure gate

## Decision sought

The certified \(H_6\) survivor already has a positive non-lattice instability
clock and a numerically stable positive finite-cycle-section zero near

\[
s_{\mathrm{fs}}=0.277982981676189\ldots .
\]

HCS-C31 asks one deliberately narrower and more decisive question:

> Is this positive number independently enclosed as the unique real root
> \(h_*\) of \(P_{\Sigma_A}(-s\tau)=0\), with every passage from the Hénon
> geometry to the finite cylinder matrices certified?

Here

\[
H_6(q,p)=(1-6q^2-p,q),
\]

\(\Lambda_*\) is the four-rectangle survivor certified in R058--R059,
\((\Sigma_A,\sigma)\) is its two-sided symbolic model, and

\[
\tau_{\rm ad}(z)
=\log\left|-12q-\frac{123}{112}\mu^u(z)\right|
\]

is the adapted unstable roof.  The symbol \(\mu^u\) denotes the unstable
slope in the normalized tangent coordinates used by the cone certificate.

The intended answer is geometric, not arithmetic.  A positive answer means
that the old positive finite-section value is independently consistent with a
pressure/Bowen benchmark at the certified resolution.  It does not assert
equality or convergence, and it does not make that number a Riemann-like
spectral anomaly.

## Frozen base system

The state order is \((--,-+,+-,++)\), with source rows and target columns,

\[
A=
\begin{pmatrix}
1&0&1&0\\
1&0&0&0\\
0&1&0&1\\
0&1&0&0
\end{pmatrix},
\qquad
\rho(A)=\varphi=\frac{1+\sqrt5}{2}.
\]

The real h-sets are

\[
X_\pm=\pm[1/3,5/8],\qquad
Y_\pm=\pm[5/16,81/128],\qquad
N_{st}=X_s\times Y_t,
\]

and

\[
\Lambda_*=\bigcap_{k\in\mathbb Z}H_6^{-k}
\left(\bigcup_{s,t}N_{st}\right).
\]

To avoid the opposite convention in some inherited prose, this package uses

\[
\Phi:\Sigma_A\longrightarrow\Lambda_*,
\qquad H_6\circ\Phi=\Phi\circ\sigma
\]

for the inverse of the state-itinerary map.

## Exact subquestions

1. **Self-consistent hyperbolicity.**  Can the inherited cone bound be
   sharpened, using the invariant graph itself, to

   \[
   \sup_{\Lambda_*}|\mu^u|
   \le \frac{112}{123}\rho_0,
   \qquad
   J^u_{\rm ad}\ge\rho_0^{-1}
   =\frac{\sqrt{17}+\sqrt{13}}2,
   \]

   where

   \[
   \rho_0=\frac{\sqrt{17}-\sqrt{13}}2.
   \]

2. **Norm-gauge bridge.**  Is the adapted roof explicitly Hölder-cohomologous
   to the Euclidean geometric potential

   \[
   \tau_E^u(z)=\log\|DH_6(z)|_{E^u(z)}\|_2,
   \]

   with identical periodic sums?

3. **Local basic set.**  Do R058--R059 already imply that
   \(\Lambda_*\) is compact, locally maximal, uniformly hyperbolic, and mixing?

4. **Effective pressure.**  Can rigorous roof intervals on every admissible
   length-\(13\) chronological cylinder be converted into nonnegative lower and
   upper transfer matrices whose Perron roots enclose \(P(-s\tau)\), and hence
   prove

   \[
   \frac{277980}{10^6}<h_*<\frac{277987}{10^6}?
   \]

5. **Dimension semantics.**  Do the exact local hypotheses already proved in
   C31 meet the primary-source interfaces needed for

   \[
   h_*=\dim_H(\Lambda_*\cap W^u_{\rm loc}(z)),
   \qquad
   \dim_H\Lambda_*=2h_*
   \]

   The source lock is Pesin--Sadovskaya (2001), Remark 4.1 (printed page 284),
   for the unstable slice, and Barreira (2013), Introduction, Theorem 1.2,
   for the total surface-set dimension.  The audit must verify that neither
   interface imports a global Axiom-A or compact-ambient hypothesis.

6. **Prior-art boundary.**  Does generic BPS pinning/nuclearity contribute a
   new theorem here, or is the project-specific novelty the explicit pressure
   and error certificate?

## Success criterion

The pressure gate passes only when an independent checker verifies all of the
following:

- every length-\(13\) edge is an admissible chronological word;
- its interval \([\tau_e^-,\tau_e^+]\) contains the roof of every bi-infinite
  extension of that word;
- directed-rounding Perron/Collatz bounds prove

  \[
  P(-s_L\tau)>0,\qquad P(-s_U\tau)<0;
  \]

- \(s_L=277980/10^6<s_U=277987/10^6\), and all lower roof bounds
  are positive;
- the old finite-section value lies inside that independently obtained
  interval;
- the dimension conclusions are invoked only through the two exact local
  theorem interfaces above, not inferred from the real-pressure computation
  alone;
- no determinant continuation or arithmetic interpretation is silently
  inferred from the real-pressure computation.

## Decisive falsifiers

The pressure claim fails if one cylinder roof interval misses a valid
extension, if the source/target convention is transposed, if the Perron
inequalities are evaluated without outward rounding, or if the two pressure
signs do not separate a root.  The dimension bridge would fail if either
local theorem required a compact ambient surface or a global Axiom-A
diffeomorphism.  The exact locators above do not: the certified locally
maximal hyperbolic set and one-dimensional bundles meet their stated local
hypotheses.  Thus this former interface blocker is resolved.

## Route-A meaning

Even a successful C31 result is a dynamical-systems control, not a
Hilbert--Pólya construction.  It explains one positive real signal and supplies
an analytic pressure object, but it provides no prime correspondence,
functional equation, Riemann--von Mangoldt law, critical-line symmetry, or
self-adjoint operator.  Route B is not authorized.

The formal Route-A tuple remains

~~~text
(A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)
overall: ROUTE_A_REJECTED
Route B authorized: false
~~~

The separate statements `pressure: NUMERICALLY_CERTIFIED` and
`analytic_pressure_implication: PROVED` are theorem-ledger statuses, not new
Route-A grades.
