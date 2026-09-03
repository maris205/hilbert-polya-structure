# HCS-C340 theorem package

## Frozen convention

Let (m=k^2\in(0,1)), let (K=K(m)), and write
(s(x)=\operatorname{sn}(x\mid m)).  On (L^2(\mathbb R)) define

\[
H_m=-D^2+u(x),\qquad D=\frac{d}{dx},\qquad u(x)=2m s(x)^2,
\]

with domain (H^2(\mathbb R)).  The potential has least real period (2K).
A Floquet multiplier is always measured over this period; `periodic` means
(+1) and `antiperiodic` means (-1).

## Main theorem

The operator (H_m) is self-adjoint, bounded below, and has purely absolutely
continuous spectrum

\[
\sigma(H_m)=[m,1]\cup[1+m,\infty).
\]

Thus its only finite open spectral gap is ((1,1+m)); every higher folded-zone
gap is closed.  The three finite band edges are

\[
H_m\operatorname{dn}=m\operatorname{dn},\qquad
H_m\operatorname{cn}=\operatorname{cn},\qquad
H_m\operatorname{sn}=(1+m)\operatorname{sn}.
\]

Over (2K), `dn` is periodic while `cn` and `sn` are antiperiodic.
Furthermore the formally skew-adjoint third-order operator

\[
A=-4D^3+\{6u-4(1+m)\}D+3u'
\]

commutes with (H_m) and obeys

\[
A^2=-16(H_m-m)(H_m-1)(H_m-1-m).
\]

## Proof

The Jacobi identities give

\[
s''=-(1+m)s+2ms^3,
\]

with analogous formulas

\[
\operatorname{cn}''=(2ms^2-1)\operatorname{cn},\qquad
\operatorname{dn}''=(2ms^2-m)\operatorname{dn}.
\]

Substitution proves the three eigen-equations and their periodicity follows
from the (2K)-shift identities.  Since (u) is real, smooth, periodic, and
bounded, the standard (H^2\) realization of (H_m) is self-adjoint and
bounded below.

Direct differentiation gives

\[
u''=3u^2-4(1+m)u+4m,
\]

and the Jacobi first integral gives

\[
(u')^2=2u^3-4(1+m)u^2+8mu.
\]

Differentiating the first equation yields
(u'''=\{6u-4(1+m)\}u').  Expanding differential-operator compositions with
these two identities proves ([A,H_m]=0) and the displayed polynomial
relation.  This is an operator identity on smooth functions and then on the
natural common core.

For \(\theta\in[-\pi,\pi)\), set

\[
H^j_\theta([0,2K])=
\{f\in H^j([0,2K]):
f^{(\ell)}(2K)=e^{i\theta}f^{(\ell)}(0),\ 0\leq\ell<j\}.
\]

The fiber of \(H_m\) has domain \(H^2_\theta\), while the closed
third-order realization has

\[
D(A_\theta)=H^3_\theta([0,2K]).
\]

All coefficients of \(A\) and the derivatives needed in its Green boundary
form are \(2K\)-periodic.  If \(f,g\in H^3_\theta\), every endpoint product
at \(2K\) equals the corresponding product at zero because the phase
\(e^{i\theta}\) cancels its conjugate.  Three integrations by parts therefore
give \(\langle A_\theta f,g\rangle=-\langle f,A_\theta g\rangle\).  The
adjoint boundary form imposes the same three quasi-periodic conditions, so
\(A_\theta^*=-A_\theta\).  Smooth periodic coefficients also show that
\(A_\theta\) preserves the smooth core of each \(H_m\)-fiber.

Put

\[
R(E)=(E-m)(E-1)(E-1-m).
\]

Decompose (H_m) into self-adjoint quasi-periodic fibers on ([0,2K]).
The operator \(A_\theta\) has the domain above and is skew-adjoint there.
Every fiber eigenfunction is smooth, hence lies in \(D(A_\theta)\).  If (E)
is a fiber eigenvalue, the polynomial relation gives

\[
-\|A\psi\|^2=-16R(E)\|\psi\|^2,
\]

so (R(E)\ge0).  Conversely, for (R(E)>0), the action of (A) on the
two-dimensional solution space of (H_m\psi=E\psi) has distinct eigenvalues
(\pm4i\sqrt{R(E)}).  The corresponding solutions are conjugate and each is
a Bloch vector because monodromy commutes with (A).  If their multipliers
are (\lambda) and (\bar\lambda), invariance of their nonzero Wronskian
under a period gives (|\lambda|^2=1).  Hence (E) belongs to the spectrum.
The three zeros of (R) follow by closure.  Therefore (R(E)\ge0) gives
exactly the two displayed intervals.

Finally, one-dimensional periodic Floquet decomposition has analytic,
nonconstant band functions and no point or singular-continuous part.  Hence
the spectrum is purely absolutely continuous.  Because the upper interval is
connected to infinity, every folded higher gap is closed.  This analytic
argument, not any finite grid, proves completeness.

## Boundary atlas

- At (m=0), (H_0=-D^2), the finite gap closes, and the spectrum is
  ([0,\infty)).
- As (m\uparrow1), (K(m)\to\infty) and
  (u(x)\to2\tanh^2x=2-2\operatorname{sech}^2x) locally.  The lower band
  collapses to the (L^2) level (1); the limiting continuum is
  ([2,\infty)), with the zero-energy state of the unshifted factor appearing
  only as a threshold resonance after the shift.
- Replacing (k) by (-k) leaves (m) and (H_m) unchanged.  Translating
  (x) gives a unitarily equivalent operator.
- Complex (m), or real (m\notin[0,1]), is outside the frozen real
  self-adjoint Jacobi convention.

## Evidence and scope

The cited periodic-operator source supplies the general Floquet direct-integral
and pure-absolute-continuity theorem; the calculation above supplies the
Lam\'e-specific spectral curve and its two bands.

The producer records all 199 reduced rational (m=p/q\) with
(2\le q\le25), including exact band endpoints, cubic coefficients, sign
chambers, and periodicity labels.  The independent checker reconstructs each
row.  A separate SymPy lane composes the differential operators and reduces
the commutator and spectral-curve residuals by both stationary identities.
Those finite receipts protect conventions; they do not prove the infinite
spectrum statement.

The Route-A tuple is
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)` and the overall
verdict is `ROUTE_A_REJECTED`.  Natural self-adjoint quantum dynamics supports
A4, but no target arithmetic, target determinant, target zeros, or
Hilbert--Polya identification follows.
