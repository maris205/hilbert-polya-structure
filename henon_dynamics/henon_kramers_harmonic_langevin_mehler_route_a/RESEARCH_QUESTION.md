# Research question — HCS-C237

Can one close, without numerical time stepping, the transition, invariant,
correlation, and damping-boundary theorem for the harmonic Langevin/Kramers
system across all \(\gamma\geq0\)?

The answer is yes at the finite-dimensional Gaussian level.  Writing
\(A=\left[\begin{smallmatrix}0&1\\-\omega^2&-\gamma\end{smallmatrix}\right]\),
we derive \(M_t=e^{tA}\) in all three discriminant regimes and use the
Lyapunov identity to obtain
\(\operatorname{Cov}(X_t\mid X_0=x)=\Sigma-M_t\Sigma M_t^T\),
\(\Sigma=\operatorname{diag}((\beta\omega^2)^{-1},\beta^{-1})\).
We also separate the noiseless Hamiltonian face \(\gamma=0\) and the
unconfined face \(\omega=0\).

The question is not whether these modes encode primes or target zeros.  No
such arithmetic origin is present in this model, and no such claim is made.
