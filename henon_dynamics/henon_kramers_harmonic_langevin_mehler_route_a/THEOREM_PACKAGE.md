# Theorem package — HCS-C237

Let \(X_t=(Q_t,P_t)^T\) solve
\[
dQ_t=P_tdt,\qquad dP_t=(-\omega^2Q_t-\gamma P_t)dt
 +\sqrt{2\gamma/\beta}\,dW_t,
\quad \omega,\beta>0,\ \gamma\geq0.
\]
Set \(A=\left[\begin{smallmatrix}0&1\\-\omega^2&-\gamma\end{smallmatrix}\right]\),
\(\alpha=\gamma/2\), and \(\Sigma=\operatorname{diag}((\beta\omega^2)^{-1},\beta^{-1})\).

## All-damping matrix flow

With \(\nu=(\omega^2-\alpha^2)^{1/2}\) in the underdamped regime and
\(\delta=(\alpha^2-\omega^2)^{1/2}\) in the overdamped regime,
\[
M_t=e^{-\alpha t}
\begin{pmatrix}c+\alpha s&s\\-\omega^2s&c-\alpha s\end{pmatrix},
\]
where \((c,s)=(\cos\nu t,\sin(\nu t)/\nu)\), \((1,t)\), or
\((\cosh\delta t,\sinh(\delta t)/\delta)\), respectively.  Thus
\(M_0=I\), \(\dot M=AM\), \(\det M_t=e^{-\gamma t}\).  At
\(\gamma=2\omega\), this is
\(M_t=e^{-\omega t}[I+t(A+\omega I)]\).

## Mehler transition and invariant law

For \(\gamma>0,t>0\),
\[
 X_t\mid X_0=x\sim\mathcal N(M_tx,\,C_t),\qquad
 C_t=\Sigma-M_t\Sigma M_t^T.
\]
The Lyapunov identity
\(A\Sigma+\Sigma A^T+BB^T=0\),
\(B=(0,\sqrt{2\gamma/\beta})^T\), proves this formula and
\(C_t\succ0\) for positive time.  The centered Gibbs density
\[
 \pi(q,p)=\frac{\beta\omega}{2\pi}
 \exp[-\tfrac\beta2(\omega^2q^2+p^2)]
\]
is invariant; it is unique for \(\omega>0,\gamma>0\).  At \(\gamma=0\),
the transition is a Dirac mass at \(M_tx\) and \(M_t\Sigma M_t^T=\Sigma\).

## Hypoellipticity and correlations

\([B,AB]\) has determinant \(-2\gamma/\beta\), hence rank two exactly for
\(\gamma>0\).  Under stationarity,
\(\operatorname{Cov}(X_t,X_0)=M_t\Sigma\), so
\[
C_{QQ}=m_{11}/(\beta\omega^2),\quad C_{QP}=m_{12}/\beta,
\quad C_{PQ}=m_{21}/(\beta\omega^2),\quad C_{PP}=m_{22}/\beta.
\]

## Rate and boundaries

The eigenvalues are \(-\gamma/2\pm\sqrt{\gamma^2/4-\omega^2}\).  The
drift spectral-abscissa decay exponent is
\[
r(\omega,\gamma)=
\begin{cases}\gamma/2,&0\leq\gamma\leq2\omega,\\
\gamma/2-\sqrt{\gamma^2/4-\omega^2},&\gamma\geq2\omega.
\end{cases}
\]
It is maximized at the critical value \(r=\omega\).  The critical matrix
has a polynomial prefactor, so the exact-rate statement is an asymptotic
exponent/spectral-abscissa statement, not a uniform bound
\(\|M_t\|\leq Ce^{-\omega t}\).  For every \(r'<\omega\), a standard
exponential bound follows.  At \(\gamma=0\) the oscillator is Hamiltonian,
has many invariant energy measures, and does not mix.  At \(\omega=0\),
position is unconfined; no finite Gibbs probability with the displayed
covariance exists.

No full nonnormal \(L^2\) spectrum, arithmetic determinant, or
Hilbert--Pólya operator is claimed.
