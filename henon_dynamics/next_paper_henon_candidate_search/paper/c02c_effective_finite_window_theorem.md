# Effective finite-window pinning and trace identities for $H_6$

Date: 2026-08-06  
Status: **proved effective specialization; not yet a paper-level operator theorem**

## 1. Dynamical object

Consider the exact area-preserving Hénon map inherited from Paper 5,

\[
H_6(q,p)=(1-6q^2-p,q),
\qquad
DH_6(q,p)=
\begin{pmatrix}-12q&-1\\1&0\end{pmatrix}.
\]

Set

\[
c=\frac{23}{48},\qquad \rho=\frac7{48},\qquad
D_\sigma=\overline D(\sigma c,\rho),
\]

and let an extended sign word
\(\varepsilon_0,\ldots,\varepsilon_{N+1}\) satisfy

\[
\neg(\varepsilon_{i-1}=\varepsilon_{i+1}=+1),
\qquad 1\le i\le N.
\]

All products and neighbor incidences below are chronological.  In particular,
periods one and two retain the repeated incidences created by cyclic closure.

## 2. Effective endpoint theorem

For every
\((u,v)\in D_{\varepsilon_0}\times D_{\varepsilon_{N+1}}\), there is a
unique vector

\[
Q(u,v)=(Q_1(u,v),\ldots,Q_N(u,v))
\in\prod_{i=1}^N D_{\varepsilon_i}
\]

solving

\[
Q_i=\varepsilon_i
\sqrt{\frac{1-Q_{i-1}-Q_{i+1}}6},
\qquad Q_0=u,\quad Q_{N+1}=v,
\]

with the principal square-root branch.  The solution is jointly holomorphic
on a neighborhood of the full closed endpoint bidisk.

Let

\[
a_0=\frac1{\sqrt{17}},\qquad
\kappa=\frac2{\sqrt{17}},\qquad
\beta=\frac{a_0}{1-\kappa}
=\frac1{\sqrt{17}-2}.
\]

Then

\[
|\partial_uQ_i|\le\beta\kappa^{i-1},
\qquad
|\partial_vQ_i|\le\beta\kappa^{N-i}.
\]

Consequently, changing both endpoints from \((u,v)\) to
\((\widetilde u,\widetilde v)\) gives the explicit joint bound

\[
|Q_i(u,v)-Q_i(\widetilde u,\widetilde v)|
\le
\beta\kappa^{i-1}|u-\widetilde u|
+\beta\kappa^{N-i}|v-\widetilde v|.
\]

The two endpoint contributions must be added; replacing this sum by a single
factor \(\beta\) is not justified.

If two adjacent windows are split at the consecutive interface variables
\((q_m,q_{m+1})=(\xi,\eta)\), the left endpoint problem uses \((u,\eta)\)
and the right endpoint problem uses \((\xi,v)\).  Their two matching
equations have a unique solution and recover the direct union solution.
This is a genuine two-coordinate chronological gluing law, not a scalar
average of the interface pair.

Finally,

\[
H_6^N(Q_1(u,v),u)=(v,Q_N(u,v)).
\]

This is the finite-window crossed-map identity.

## 3. Matching, Hill and trace-residue identities

Use the orbit residual

\[
R_i(Q)=1-6Q_i^2-Q_{i-1}-Q_{i+1}
\]

and let \(L_N=D_QR\).  Thus \(L_N\) is tridiagonal with diagonal
\(a_i=-12Q_i\) and adjacent entries \(-1\).  Since \(|a_i|\ge4\), it is
strictly diagonally dominant.  Let \(K_{r,s}\) be its chronological
continuants and \(\theta_N=\det L_N\).  Then

\[
\partial_uQ_i=\frac{K_{i+1,N}}{\theta_N},\qquad
\partial_vQ_i=\frac{K_{1,i-1}}{\theta_N},\qquad
\partial_vQ_1=\partial_uQ_N=\frac1{\theta_N}.
\]

Writing

\[
J_i=DH_6(Q_i,Q_{i-1}),\qquad
M_N=J_N\cdots J_1,
\]

one has the exact chronological formula

\[
M_N=
\begin{pmatrix}
K_{1,N}&-K_{2,N}\\
K_{1,N-1}&-K_{2,N-1}
\end{pmatrix},
\qquad (M_N)_{11}=\det L_N.
\]

Define the endpoint matching map

\[
F_N(u,v)=(Q_N(u,v)-u,\;Q_1(u,v)-v).
\]

At a cyclic solution, let \(C_N\) be the cyclic residual Jacobian, retaining
the chronological multiplicities \(C_1=[a_1-2]\) and

\[
C_2=\begin{pmatrix}a_1&-2\\-2&a_2\end{pmatrix}.
\]

Then, for every \(N\ge1\),

\[
\det C_N=\operatorname{tr}M_N-2=-\det(I-M_N)
\]

and

\[
\boxed{
\det DF_N
=-\frac{\det(I-M_N)}{\det L_N}
=\frac{\det C_N}{\det L_N}.}
\]

The corresponding signed local residue is

\[
\boxed{
\frac1{\det(I-M_N)}
=-\frac{\partial_vQ_1}{\det DF_N}.}
\]

This is a finite-dimensional identity.  It does not by itself construct an
infinite transfer operator.  Moreover, the signed holomorphic denominator
and \(|\det(I-M_N)|\) define different trace conventions; the latter requires
an orientation twist and must not be substituted silently.

## 4. Exact complex-base projective disks

For the true derivative slope map

\[
\phi_q(m)=\frac1{-12q-m},
\]

take the parent fibre disk \(|m|\le R\), where \(R=123/224\), and
\(q\in D_\varepsilon\).  The denominator disk has center
\(-\varepsilon23/4\), radius \(515/224\), and pole clearance \(773/224\).
Its exact reciprocal image is

\[
\phi_q(m)\in
\overline D\left(
-\varepsilon\frac{288512}{1393719},
\frac{115360}{1393719}
\right).
\]

The two child disks are separated by

\[
\frac{448}{1803}\approx0.2484748,
\]

and lie inside the parent with margin

\[
\frac{44903}{173152}\approx0.2593271.
\]

The fibre derivative satisfies

\[
|\partial_m\phi_q(m)|\le
\delta=\left(\frac{224}{773}\right)^2
=\frac{50176}{597529}<1.
\]

However,

\[
12\delta=\frac{602112}{597529}>1.
\]

Thus the fibre is strictly contracting, but these estimates do not prove an
unscaled joint base--fibre contraction.  For an ordered chain
\(m_i=\phi_{Q_i}(m_{i-1})\), the valid endpoint bounds are

\[
|\partial_{m_0}m_N|\le\delta^N,
\]

\[
|\partial_um_N|
\le12\delta\beta\frac{\kappa^N-\delta^N}{\kappa-\delta},
\qquad
|\partial_vm_N|
\le12\delta\beta\frac{1-(\delta\kappa)^N}{1-\delta\kappa}.
\]

## 5. Proof and computational certificate

The complete symbolic derivation, assumptions and proof boundaries are in
`../DERIVATION_PACKAGE.md`.  The proof uses parameter-dependent contraction,
a Neumann-path expansion, continuant identities, exact chronological
monodromy multiplication and reciprocal-disk geometry.

The frozen computation is an adversarial regression certificate, not the
existence proof.  It contains:

- 432 complete open center-endpoint cases through \(N=8\);
- 120 complex endpoint-boundary probes through \(N=3\), with count and
  extrema persisted in the certificate rather than individual CSV rows;
- 120 complete cyclic words through \(N=8\);
- exact two-coordinate gluing plus scalar-average and reversed-order
  expected-fail controls;
- an independent Newton implementation with complete-ID, truncation and
  constant-tamper checks;
- high-precision Newton rechecks of the two worst binary64-conditioned cases.

All frozen checks pass.  The canonical results are in
`../results/c02c_finite_window/`.

## 6. Novelty and paper boundary

After the linear conjugacy \((x,y)=(-6q,6p)\),
Sterling--Dullin--Meiss Theorem 3 already covers the same real forbidden-neighbor
SFT at \(b=1,k=6\) and proves real signed-root existence and uniqueness.
Rugh's analytic hyperbolic pinning construction and
Baladi--Pujals--Sambarino's iterated pinning maps give the qualitative complex
two-variable composition and periodic closure in broader settings.  The BPS
orientation convention produces an absolute determinant denominator, so it
does not directly establish the signed operator proposed here.  Therefore
this theorem is not presented as a new real horseshoe, general pinning theory,
or signed Fredholm construction.

The surviving contribution is an explicit effective specialization for the
determinant-one Paper-5 Hénon family at \(a=6\): full disks, exact constants,
endpoint localization, chronological short-cycle bookkeeping, a signed
matching/Hill identity, complex-base projective disks and independently
checked artifacts.

Current ruling:

`RETAIN_EFFECTIVE_SPECIALIZATION; MANUSCRIPT_HOLD;
NOVELTY_DELTA_UNCONFIRMED`.

The manuscript gate is a trace-compatible cylinder/operator approximation
theorem with a frozen function space, Cauchy kernel, orientation convention,
potential and approximation norm.  Until that theorem is proved, nuclearity,
an infinite Fredholm determinant, Route-A A2 and Hilbert--Pólya are open.
