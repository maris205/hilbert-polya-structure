# HCS-C237 — harmonic Kramers--Langevin all-damping certificate

This package gives a source-local theorem for the two-dimensional harmonic
Kramers diffusion
\[
dQ_t=P_t\,dt,\qquad dP_t=(-\omega^2Q_t-\gamma P_t)\,dt
 +\sqrt{2\gamma/\beta}\,dW_t.
\]
The physical domain is \(\omega,\beta>0\), \(\gamma\geq0\); the
\(\omega=0\) unconfined-position face is recorded separately.  The exact
matrix exponential is given in under-, critical-, and over-damped form.  The
same certificate verifies the Gaussian Mehler covariance, Gibbs law,
Kalman bracket, stationary correlations, and the drift spectral-abscissa
rate.  At critical damping the rate has the explicit \(t e^{-\omega t}\)
prefactor, so no sharp pure-exponential norm bound is asserted.

The result is deliberately scoped: it is a classical stochastic semigroup,
not a primitive-orbit zeta, arithmetic determinant, or Hilbert--Pólya
operator.  The Route-A tuple is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` and Route B is not invoked.

Artifacts include the exact evidence JSON, an independent checker, a SymPy
reconstruction, clean byte replay, 32 hostile mutations (including repaired
hash checks for every boundary-row semantic), a three-round
LuaLaTeX paper, and a self-excluded release manifest.  Source lock:
`0ebc633706bc34b8b915a44749423486fd4cd243`; scope:
`NO_BAD_EULER_OR_ROOT_NUMBER`.
