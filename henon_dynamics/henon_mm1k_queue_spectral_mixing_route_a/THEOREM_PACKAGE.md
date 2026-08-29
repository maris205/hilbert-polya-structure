# Theorem package

## Frozen model

States are `0,1,…,K`; `K` includes the customer in service.  For positive
rates, the row-generator is

\[
 Q_{0,0}=-\lambda,\quad Q_{0,1}=\lambda,
\]
\[
 Q_{n,n-1}=\mu,\ Q_{n,n}=-(\lambda+\mu),\ Q_{n,n+1}=\lambda
 \quad(0<n<K),
\]
with `Q_{K,K-1}=mu, Q_{K,K}=-mu`.  At `K=0`, `Q=[0]`.

## Main theorem

For `lambda,mu>0` and `K>=1`, let `rho=lambda/mu` and
`Z_K=sum_{r=0}^K rho^r`.  Then
`pi_n=rho^n/Z_K`, and with `D_pi=diag(pi)` the matrix
`S=D_pi^(1/2) Q D_pi^(-1/2)` is symmetric tridiagonal with off-diagonal
`sqrt(lambda*mu)`.  Its spectrum consists of `0` and

\[
 \nu_j=-(\lambda+\mu)+2\sqrt{\lambda\mu}\cos\frac{j\pi}{K+1},
 \qquad j=1,\ldots,K.
\]

For `theta_j=j*pi/(K+1)`, a normalized eigenvector has components
`v_j(n)=C_j[sin((n+1)theta_j)-sqrt(mu/lambda) sin(n theta_j)]`.
Together with `v_0(n)=sqrt(pi_n)`, these modes give

\[
 P_t(i,j)=\sqrt{\frac{\pi_j}{\pi_i}}
 \sum_{m=0}^{K}v_m(i)v_m(j)e^{\nu_m t},
 \quad \nu_0=0.
\]

The gap is
`gamma_K=lambda+mu-2sqrt(lambda*mu)cos(pi/(K+1))`, and reversibility gives

\[
 \|P_t(i,\cdot)-\pi\|_{TV}
 \le \frac12\sqrt{\pi_i^{-1}-1}\,e^{-\gamma_Kt}.
\]

## Boundaries and capacity limits

`K=0` is a one-state chain.  If `lambda=0`, state 0 absorbs; if `mu=0`,
state K absorbs; if both vanish every state absorbs.  At equal positive rates
the finite law is uniform, whereas the infinite chain is null recurrent.  As
`K→∞`, `rho<1` gives `pi_n→(1-rho)rho^n` and
`gamma_K→(sqrt(mu)-sqrt(lambda))^2`; `rho=1` gives
`gamma_K~lambda*pi^2/(K+1)^2` and no stationary probability; `rho>1` gives
`pi_n^K→0` for every fixed n (mass escape), again with no stationary
probability.  No continuous-spectrum decomposition of the infinite generator
is claimed.

## Evidence boundary

The 20 stationary rows, 60 spectral rows, 240 kernel rows, 240 mixing links,
16 capacity-limit rows and 8 boundary rows are regression controls.  The
producer-independent checker and exact SymPy identities verify the displayed
theorem; the rows do not replace the proof.  This source-local result is not
C208 branching, C220 TASEP, an arithmetic object, or a Hilbert–Pólya operator.
