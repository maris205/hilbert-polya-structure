# Theorem package: one-dimensional focusing cubic NLS Hessian

Let \(\omega>0\) and
\[
 i\psi_t+\psi_{xx}+2|\psi|^2\psi=0,
 \qquad \psi=e^{i\omega t}Q_\omega,
 \qquad Q_\omega(x)=\sqrt\omega\,\operatorname{sech}(\sqrt\omega x).
\]
For \(M(u)=\int|u|^2\,dx\),
\(H(u)=\frac12\int|u_x|^2dx-\frac12\int|u|^4dx\), and
\(S_\omega=H+\frac\omega2M\), the following all-parameter identities hold:
\[
-Q_\omega''+\omega Q_\omega-2Q_\omega^3=0,
\quad M(Q_\omega)=2\sqrt\omega,
\]
\[
\|Q_\omega'\|_2^2=\frac23\omega^{3/2},\quad
\|Q_\omega\|_4^4=\frac43\omega^{3/2},\quad
H(Q_\omega)=-\frac13\omega^{3/2},\quad
S_\omega(Q_\omega)=\frac23\omega^{3/2},
\quad \frac{d}{d\omega}M(Q_\omega)=\omega^{-1/2}>0.
\]

The real and imaginary Hessians of \(S_\omega\) are
\[
 L_+=-\partial_x^2+\omega-6\omega\operatorname{sech}^2(\sqrt\omega x),
 \qquad
 L_-=-\partial_x^2+\omega-2\omega\operatorname{sech}^2(\sqrt\omega x).
\]
On \(L^2(\mathbb R)\),
\[
 \sigma_{\rm ess}(L_\pm)=[\omega,\infty),
\]
and the complete discrete list is
\[
 \sigma_{\rm disc}(L_+)=\{-3\omega,0\},\qquad
 \sigma_{\rm disc}(L_-)=\{0\}.
\]
The \(-3\omega\) eigenfunction is \(\operatorname{sech}^2(\sqrt\omega x)\);
the zero mode of \(L_+\) is \(Q_\omega'\), and that of \(L_-\) is
\(Q_\omega\).  All listed eigenvalues are simple; \(L_+\) has Morse index one
and \(\ker L_+=\operatorname{span}\{Q_\omega'\}\), while \(L_-\ge0\) and
\(\ker L_-=\operatorname{span}\{Q_\omega\}\).

With \(y=\sqrt\omega x\), define
\(A_\ell=\partial_y+\ell\tanh y\) and
\(A_\ell^*=-\partial_y+\ell\tanh y\).  The scaled operators satisfy
\[
 -\partial_y^2+1-6\operatorname{sech}^2y=A_2^*A_2-3,
 \qquad
 -\partial_y^2+1-2\operatorname{sech}^2y=A_1^*A_1.
\]
The factorization plus the standard Pöschl–Teller ladder (historically
attributed to G. Pöschl and E. Teller, 1933, DOI
10.1007/BF01331132) gives the stated absence of further discrete eigenvalues.
This is a Hessian theorem only; it does not assert full nonlinear orbital or
asymptotic stability.

## Boundary and evidence ledger

As \(\omega\downarrow0\), the profile and all discrete eigenvalues collapse to
the essential threshold.  Reversing the cubic sign removes this bright \(H^1\)
sech branch.  A finite periodic domain has elliptic/cnoidal waves, and
dimensions \(d\ge2\) involve different criticality; both are outside the
owner.  The finite receipt is regression evidence, not a proof by sampling.
