# R400 — Near-Well Period/Action Certificate

## Frozen status

**Zero-input smoke protocol.**  This run may be executed after the orbit
module and its unit tests pass.  It does not load primes, von Mangoldt
weights, zeta zeros, or spectral peak locations.

## Question

For the centered one-step Hénon-warped Hamiltonian

\[
 h_a(q,p)=\frac{|p|^2}{2}+2\pi
 \exp\!\left(\pi|\widetilde H_a(q)|^2\right),
 \qquad a=1.02,
\]

does the fast Lyapunov family born at the unique equilibrium admit a
reproducible numerical certificate consistent with the analytic limits

\[
 T_+(E)=T_+^0+O(E-2\pi),\qquad
 S_+(E)=T_+^0(E-2\pi)+O((E-2\pi)^2),
\]

and with a nonzero limiting Poincaré stability determinant?

This is a classical period/action pilot for a fixed-energy semiclassical
trace theorem.  It is not a high-energy prime-time test.

## Analytic oracle

Put

\[
 c_a=2(\sqrt{1+a}-1),\qquad
 A_a=\begin{pmatrix}-c_a&-1\\1&0\end{pmatrix}.
\]

If \(s_-<s_+\) are the singular values of \(A_a\), then

\[
 \omega_\pm=2\pi s_\pm,
 \qquad T_\pm^0=s_\pm^{-1},
 \qquad \rho=\frac{s_+}{s_-}=s_+^2.
\]

The fast branch has

\[
 T_+^0=s_-,\qquad
 \theta_+^0=\frac{2\pi}{\rho},\qquad
 D_+^0=4\sin^2\!\frac{\pi}{\rho},\qquad
\mathcal A_+^0=\frac{T_+^0}{\sqrt{D_+^0}}.
\]

A fourth-order Taylor expansion of the potential followed by the
Poincaré--Lindstedt solvability condition supplies two additional, non-fitted
oracles:

\[
 T_+(2\pi+\delta)
 =T_+^0-0.02744507562837\,\delta+o(\delta),
\]

\[
 \frac{S_+(2\pi+\delta)}{\delta}
 =T_+^0-0.01372253781419\,\delta+o(\delta).
\]

At \(a=1.02\), the frozen values are approximately

\[
 T_+^0=0.6638439766793,quad
 D_+^0=3.862722044516,quad
 \mathcal A_+^0=0.337768612643.
\]

These values are derived from the Hessian, not fitted to the orbit output.

## Frozen cells

Use the energy excesses

\[
 \delta=E-2\pi\in\{0.01,0.02,0.05,0.10,0.20,0.40\}.
\]

For every cell:

1. shoot a reversible orbit with \(p(0)=p(T/2)=0\);
2. integrate a separate full-period state/variational/action system;
3. archive the trajectory, energy history, monodromy matrix, Floquet
   multipliers, period, action, and optimizer residual;
4. use physical time only.

The full-period integration uses DOP853 with `rtol=2e-12`, `atol=2e-14`,
and 800 nominal steps per period.

## Numerical gates

Every cell must satisfy:

- optimizer success;
- maximum dimensionless shooting residual below \(10^{-9}\);
- scaled full-period closure below \(10^{-9}\);
- maximum energy drift divided by \(\delta\) below \(10^{-9}\);
- monodromy symplectic defect below \(10^{-8}\);
- \(|\operatorname{Im}\det(I-P)|<10^{-9}\);
- \(\operatorname{Re}\det(I-P)>3\), excluding a unit transverse
  multiplier at smoke resolution;
- computed fast periods lie in the preregistered prime-free window
  \(I=[0.60,0.75]\).

## Asymptotic gates

A quadratic fit against the three smallest \(\delta\) values must reproduce:

- the period intercept \(T_+^0\) within \(5\times10^{-6}\);
- the intercept of \(S_+(E)/\delta\) within \(5\times10^{-6}\);
- the stability-determinant intercept \(D_+^0\) within \(2\times10^{-5}\).
- the fitted period slope within \(5\times10^{-5}\) of its analytic
  normal-form value;
- the fitted \(S/\delta\) slope within \(2.5\times10^{-5}\) of its analytic
  normal-form value.

These fits are numerical consistency checks, not proofs of the asymptotic
orders.

## Independent checker

The checker must not import `hp_candidate_search`.  It will:

1. reconstruct all analytic oracle values directly from \(a\);
2. validate the JSON/NPZ binding and stored gates;
3. reimplement the one-step potential, gradient, Hessian, shooting problem,
   variational equations, and action integral;
4. independently re-solve the \(\delta=0.05\) cell;
5. compare period, action, initial state, monodromy invariants, and closure.

## Interpretation

A pass establishes a reproducible classical orbit certificate and validates
the explicit near-well period/action/stability oracle.  Combined with a
separate Lyapunov-centre proof and a published semiclassical trace theorem,
it supports a local nonzero-time trace interface.

It does **not** establish a global wave-trace formula, a high-energy period
law, a prime-power carrier, a Hilbert--Pólya spectrum, zeta-zero agreement,
or RH.
