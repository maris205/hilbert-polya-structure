# Theorem package — HCS-C229

Let `X_0=x>=0` and

\[
 dX_t=\kappa(\theta-X_t)\,dt+\sigma\sqrt{X_t}\,dW_t,
 \qquad \kappa,\theta,\sigma\ge0.
\]

The square-root coefficient gives a unique nonnegative strong solution.  For
`kappa,theta,sigma>0`, put
`alpha=2*kappa*theta/sigma^2`, `beta=sigma^2/(2*kappa)`, and
`h_t=beta(1-exp(-kappa t))`.  For `u>=0`,

\[
 \mathbb E_x e^{-uX_t}=e^{-\phi_t(u)-\psi_t(u)x},\quad
 \psi_t={u e^{-\kappa t}\over1+h_tu},\quad
 \phi_t=\alpha\log(1+h_tu).
\]

The same Riccati equations cover the faces: for `kappa=0,sigma>0`,
`h_t=sigma^2t/2`, `phi=0`, `psi=u/(1+h_tu)`; for `sigma=0,kappa>0`,
`phi=theta u(1-e^{-kappa t})`, `psi=ue^{-kappa t}`; at both zero,
`psi=u,phi=0`.

When `kappa,sigma>0`, this is the Laplace transform of

\[
 X_t=c_t\,\chi'^2_{4\kappa\theta/\sigma^2}(\lambda_t),\quad
 c_t={\sigma^2(1-e^{-\kappa t})\over4\kappa},\quad
 \lambda_t={4\kappa e^{-\kappa t}x\over\sigma^2(1-e^{-\kappa t})}.
\]

The Feller scale/speed test gives the following complete boundary split for
positive rates: `2*kappa*theta >= sigma^2` means zero is an inaccessible
entrance boundary (including equality); `0<2*kappa*theta<sigma^2` means a
regular, instantaneously reflecting boundary.  If `theta=0` or `kappa=0`
with noise, the dimension is zero and zero is absorbing.  If `sigma=0`,
`X_t=theta+(x-theta)e^{-kappa t}` for `kappa>0`; the deterministic and
constant faces are not classified by the noisy Feller ratio.

On the positive interior, `pi=Gamma(alpha,beta)` is the unique invariant
probability law.  In `z=x/beta`,

\[
 L=\kappa[z\partial_z^2+(\alpha-z)\partial_z],\qquad
 L L_n^{(\alpha-1)}=-\kappa nL_n^{(\alpha-1)}.
\]

With `p_t(x,y)=pi(y)K_t(x,y)`,

\[
 K_t(x,y)=\sum_{n=0}^{\infty}e^{-\kappa nt}{n!\Gamma(\alpha)\over\Gamma(n+\alpha)}
 L_n^{(\alpha-1)}(x/\beta)L_n^{(\alpha-1)}(y/\beta).
\]

The expansion is the exact reversible semigroup kernel for `t>0`; it is not a
finite truncation claim.  The Poincare constant is `1/kappa`, hence
`Var_pi(P_tf)<=e^{-2kappa t}Var_pi(f)`.  For an `L2(pi)` density, chi-square
contracts with the same squared factor and TV is at most half the `L2` factor
times the initial chi-square square root.  The first Laguerre mode attains the
gap, so it is sharp.

Finally, this stochastic semigroup has no intrinsic rational-prime primitive
objects.  It is not a dynamical zeta, target Fredholm determinant, or
Hilbert--Pólya operator; Route B is therefore not invoked.
