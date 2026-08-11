# HCS-C31 methodology blueprint

## Principle

Certify the real pressure root from chronological full-cylinder data:

\[
\text{exact Hénon geometry}
\to
\text{roof intervals on genuine words}
\to
\text{ordered Perron matrices}
\to
\text{pressure signs}
\to
\text{one root interval}.
\]

Finite cycle sections are comparison data, not proof inputs.  Chronology is
never replaced by an averaged transition matrix.

## 1. Dependency and convention lock

Freeze hashes for R058, R059, the instability-roof source, and its old positive
finite-section value.  Freeze

\[
A=\begin{pmatrix}
1&0&1&0\\
1&0&0&0\\
0&1&0&1\\
0&1&0&0
\end{pmatrix}
\]

with source rows, target columns, and state order
\((--,-+,+-,++)\).  A non-palindromic path test must reject \(A^T\).

## 2. Exact analytic preflight

Set

\[
r=\frac{123}{112},\qquad
a_0=\frac{112}{123},\qquad
\rho_0=\frac{\sqrt{17}-\sqrt{13}}2.
\]

Check the exact consequences

\[
\frac{\sqrt{17}}{12}\le|q_i|\le\sqrt{\frac38},
\]

\[
|\mu^u|\le a_0\rho_0,
\qquad
J^u_{\rm ad}\ge J_*:=\rho_0^{-1}
=\frac{\sqrt{17}+\sqrt{13}}2.
\]

The inherited \(773/224\) lower bound remains valid, but it is not the
strongest current uniform expansion bound.

## 3. Adapted-to-Euclidean certificate

Use

\[
e^u_{\rm ad}(z)
=\left(\frac7{48},\frac{41}{256}\mu^u(z)\right).
\]

Verify pointwise

\[
DH_6(z)e^u_{\rm ad}(z)
=\lambda(z)e^u_{\rm ad}(H_6z),
\qquad
\lambda(z)=-12q-r\mu^u(z).
\]

Store

\[
b_u(z)=\log\|e^u_{\rm ad}(z)\|_2,
\qquad
\tau_E^u=\tau_{\rm ad}+b_u\circ H_6-b_u.
\]

The proof uses invariant frames.  Periodic numerical comparisons are
regression tests, not substitutes for the identity.

## 4. Local-basic-set preflight

Let

\[
N=\bigcup_{s,t}N_{st},
\qquad U=\operatorname{int}N.
\]

Check

\[
\Lambda_*\subset U,
\qquad
\Lambda_*=\bigcap_{k\in\mathbb Z}H_6^{-k}(U).
\]

This proves local maximality.  Check \(A^4>0\), so the conjugate SFT is mixing.
Combine with the R058 cones and R059 conjugacy to record compactness,
invariance, hyperbolicity, transitivity, and dense periodic points separately.

The dimension interface is locked to two local statements whose hypotheses
are now checked: Pesin--Sadovskaya (2001), Remark 4.1 (printed page 284), for
the unstable slice, and Barreira (2013), Introduction, Theorem 1.2, for total
dimension on a surface.  Neither statement requires a global Axiom-A
extension or a compact ambient surface.  The applicability fields therefore
record `PROVED`, with the exact theorem locators retained in the certificate.

## 5. Full length-13 cylinder intervals

Use

\[
W=13=2M+1,\qquad M=6.
\]

Vertices are admissible length-\(12\) state words; edges are admissible
length-\(13\) state words.  The exact sizes are

\[
\#V=714,\qquad \#E=1156.
\]

An edge

\[
e=(w_{-6},\ldots,w_6)
\]

runs chronologically from its length-\(12\) prefix to its length-\(12\)
suffix.  Attach the time-zero roof to the edge.

For every edge, directed interval dynamics must certify

\[
q_0(x)\in Q_e,\qquad
\mu_0^u(x)\in M_e
\quad\text{for every }x\in[e].
\]

Directed evaluation of

\[
\tau_{\rm ad}(x)=\log|-12q_0(x)-r\mu_0^u(x)|
\]

must yield

\[
0<\tau_e^-\le\tau_{\rm ad}(x)\le\tau_e^+
\qquad(x\in[e]).
\]

A periodic extension may provide a center but never a full-cylinder bound by
itself.  It needs either the direct interval enclosure or the analytic
variation majorant in the derivation package.

## 6. Ordered transfer matrices

For real \(s\ge0\), define

\[
(L_s^-)_{uv}
=\sum_{e:u\to v}e^{-s\tau_e^+},
\qquad
(L_s^+)_{uv}
=\sum_{e:u\to v}e^{-s\tau_e^-}.
\]

The endpoint reversal is essential.  Potential order gives

\[
\log\rho(L_s^-)
\le P_{\Sigma_A}(-s\tau_{\rm ad})
\le\log\rho(L_s^+).
\]

Bound the Perron roots with outward-rounded Collatz--Wielandt quotients.  A
floating eigenvalue is not a certificate.

## 7. Root signs and final interval

The production checker certifies

\[
\log\rho\!\left(L_{277980/10^6}^-\right)>0,
\qquad
\log\rho\!\left(L_{277987/10^6}^+\right)<0.
\]

Because all roof lower bounds are positive, the true pressure is strictly
decreasing.  Therefore

\[
\boxed{
\frac{277980}{10^6}<h_*<\frac{277987}{10^6}
}.
\]

The old value \(0.277982981676189\ldots\) is opened only after this
independent interval and its proof choices are fixed.

## 8. Independent analytic containment

Codes agreeing on \([-M,M]\) satisfy

\[
|q_0-q_0'|\le 2D_q\rho_0^{M+1},
\qquad D_q=\sqrt{\frac32}.
\]

The graph transform then yields an explicit slope variation \(U_M\) and roof
oscillation

\[
V_M=\frac{12Q_M+rU_M}{J}.
\]

The exact formula and proof are in DERIVATION_PACKAGE.md.  Direct cylinder
intervals must be compatible with this independent bound.

## 9. Interpretation gates

After the pressure checker passes:

1. report the old finite-section value as an independent numerical
   approximation to \(h_*\), not as proof of determinant convergence;
2. identify \(h_*\) with the unstable-slice Hausdorff dimension through
   Pesin--Sadovskaya, Remark 4.1, and identify the total dimension through
   Barreira, Introduction, Theorem 1.2;
3. distinguish a suspension-zeta pole from an inverse-determinant zero;
4. make no arithmetic claim from the positive real pressure root.

## 10. Required certificate fields

Record at minimum:

- dependency hashes and symbolic orientation;
- \(W,M,\#V,\#E\), ordered vertex/edge hashes, and chronology test word;
- exact \(\rho_0,J_*\), coordinate, slope, and angle bounds;
- every \([\tau_e^-,\tau_e^+]\) and its rounding provenance;
- minimum roof lower endpoint;
- sparse matrix hashes and Collatz vectors at both rational endpoints;
- outward pressure signs and
  \((277980/10^6,277987/10^6)\);
- containment status of the old finite-section value;
- separate statuses for pressure, Euclidean bridge, local basic set,
  unstable dimension, total dimension, determinant continuation, and
  arithmetic interpretation.

## 11. Mandatory mutations

Reject:

- transposed adjacency or reversed prefix/suffix chronology;
- word shuffling;
- cylinder centers substituted for intervals;
- \(\tau_e^-\) used in the lower matrix or \(\tau_e^+\) in the upper matrix;
- inward-rounded exponentials or Perron quotients;
- empty or nonpositive roof intervals;
- a Bowen-dimension claim without a theorem-scope record;
- an infinite determinant claim based only on the pressure bracket.

## 12. Status firewall

The pressure enclosure is a computer-assisted result, while the order,
coboundary, local-basic-set, and dimension implications are mathematical
deductions from the certified inequalities and locked source theorems:

~~~text
pressure: NUMERICALLY_CERTIFIED
analytic_pressure_implication: PROVED
unstable_slice_dimension: PROVED
total_Hausdorff_dimension: PROVED

Route-A: (A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)
overall: ROUTE_A_REJECTED
Route B authorized: false
~~~

The first four lines are theorem-ledger statuses.  They do not alter the
allowed Route-A enumeration.
