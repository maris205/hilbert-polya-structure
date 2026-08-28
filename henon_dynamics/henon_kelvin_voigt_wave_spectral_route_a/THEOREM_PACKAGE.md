# Theorem package

Consider
\[
 u_{tt}-u_{xx}-b\,u_{txx}=0,\qquad u(0,t)=u(\pi,t)=0,\qquad b\ge0,
\]
on the energy space \(H_0^1(0,\pi)\times L^2(0,\pi)\).  For \(b>0\) use the
first-order generator
\[
 A(u,v)=(v,(u+bv)_{xx}),\qquad
 D(A)=\{(u,v)\in H_0^1(0,\pi)\times L^2(0,\pi):
 v\in H_0^1(0,\pi),\ u+bv\in H^2(0,\pi)\cap H_0^1(0,\pi)\}.
\]
We use the energy norm
\(\|(u,v)\|_E^2=\int_0^\pi(|u_x|^2+|v|^2)\,dx\).
The normalized Dirichlet frequencies are \(\omega_n=n\), \(n\ge1\).

## Main theorem (Kelvin--Voigt root and gap atlas)

For every \(b>0\), the sine coefficient solves
\[
 q_n''+bn^2q_n'+n^2q_n=0,\qquad
 \lambda_{n,\pm}=\frac{-bn^2\pm\sqrt{b^2n^4-4n^2}}2 .
\]
The regimes are underdamped when \(bn<2\), critical with a defective Jordan
root \(-n\) when \(bn=2\), and overdamped when \(bn>2\).  There are finitely
many underdamped modes and at most one critical mode.  In the overdamped
regime,
\[
 \lambda_{n,+}=-\frac{2n^2}{bn^2+\sqrt{b^2n^4-4n^2}}
 \longrightarrow-\frac1b\quad\text{from below},\qquad
 \lambda_{n,-}\longrightarrow-\infty .
\]

We define the essential spectrum in the Weyl singular-sequence sense.  The
point \(-1/b\) is an essential spectral accumulation point but is not an
energy-space eigenvalue: if \(A(u,v)=-(1/b)(u,v)\), then
\(v=-(1/b)u\) and the second component gives \(b^{-2}u=0\) in \(L^2\),
hence \(u=v=0\).  Equivalently, substituting \(\lambda=-1/b\) in
\[
 \bigl(\lambda^2-(1+b\lambda)\partial_{xx}\bigr)u=0
\]
leaves \(b^{-2}u=0\).  More explicitly, for the slow overdamped roots and
\(e_n(x)=\sqrt{2/\pi}\sin(nx)\), set
\[
 a_n=(n^2+|\lambda_{n,+}|^2)^{-1/2},\qquad
 w_n=(a_ne_n,\lambda_{n,+}a_ne_n).
\]
Then \(\|w_n\|_E=1\), \(w_n\rightharpoonup0\), and
\(\|(A+1/b)w_n\|=|\lambda_{n,+}+1/b|\to0\).  Thus these vectors furnish
the Weyl singular sequence.  Since
\(e^{tA}w_n=e^{t\lambda_{n,+}}w_n\), their image norms tend to
\(e^{-t/b}>0\) for every \(t>0\); hence the positive-time semigroup is
neither compact nor Schatten (and at \(t=0\) it is the identity).

The spectral-abscissa gap is
\[
 \gamma(b)=-\sup_{n\ge1,\pm}\operatorname{Re}\lambda_{n,\pm}
          =\min\!\left(\frac b2,\frac1b\right).
\]
It has the unique maximizer \(b_\star=\sqrt2\) and
\(\gamma(b_\star)=1/\sqrt2\).  This is only a spectral-abscissa assertion; a
critical Jordan block prevents an automatic exact-rate operator-norm bound.
The energy law is
\[
 \frac{d}{dt}\frac12\int_0^\pi(|u_t|^2+|u_x|^2)\,dx
 =-b\int_0^\pi |u_{tx}|^2\,dx\le0 .
\]
At \(b=0\), the roots are \(\pm in\) and the undamped wave group is unitary.

## Proof ledger

The sine expansion gives the quadratic pencil.  The discriminant and the
quadratic formula give all three regimes and the Jordan face.  Rationalizing
the slow overdamped root proves it is strictly below \(-1/b\) and converges
there from below; the fast root diverges to minus infinity.  The first
underdamped real part is \(-b/2\), so comparison with the high-frequency
limit gives the displayed gap.  The two branches meet only at
\(b=\sqrt2\).  The direct substitution above proves the non-eigenvalue claim.
The displayed normalized eigenvectors are orthogonal across sine modes, so
they converge weakly to zero; the eigenvalue equation gives the residual
identity and the slow-root limit makes it vanish.  This proves the Weyl
singular-sequence and noncompactness claims.  Multiplication by \(u_t\) and integration by parts gives the
energy identity.
