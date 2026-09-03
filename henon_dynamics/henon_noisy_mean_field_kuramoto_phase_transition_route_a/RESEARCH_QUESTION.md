# Research question and frozen contract

## Question

For the identical-frequency noisy mean-field Kuramoto Fokker–Planck equation on the circle,

\[
 \partial_t p=D\,\partial_\theta^2p-
 \partial_\theta\!\left(Kr[p]\sin(\psi[p]-\theta)p\right),
 \qquad \int_{-\pi}^{\pi}p\,d\theta=1,
\]

with (D>0), (K\geq0), and

\[
 z[p]=\int_{-\pi}^{\pi}e^{i\theta}p(\theta)\,d\theta
      =r[p]e^{i\psi[p]},
\]

can one close in one proof the global probability flow, Lyapunov identity, complete stationary atlas, exact synchronization threshold, uniform linear spectrum, and critical branch expansion?

## Frozen answer

Yes. Nonnegative (C^{2+\gamma}) unit-mass data generate a unique global classical flow, positive for every (t>0). The free energy

\[
 \mathcal F[p]=D\int p\log p\,d\theta-\frac K2|z[p]|^2
\]

dissipates exactly. Every nonnegative (C^2) stationary probability density is either (1/(2\pi)) or

\[
 q_{\kappa,\psi}(\theta)=
 \frac{e^{\kappa\cos(\theta-\psi)}}{2\pi I_0(\kappa)},
 \qquad \kappa=\frac KD\frac{I_1(\kappa)}{I_0(\kappa)}.
\]

Strict decrease of (I_1(\kappa)/(\kappa I_0(\kappa))), proved through an exact coefficient-ratio/Turán argument, gives uniform uniqueness for (K\leq2D) and one positive concentration modulo phase for (K>2D). At the uniform density the real Fourier eigenvalues are (0) for mass, (K/2-D) with multiplicity two at frequency one, and (-Dn^2) with multiplicity two for (n\geq2). If (\delta=K/D-2\downarrow0), then

\[
 \kappa^2=4\delta+\frac23\delta^2+O(\delta^3),\qquad
 r^2=\delta-\frac56\delta^2+O(\delta^3).
\]

## Evidence boundary

The infinite-dimensional theorem is proved analytically. The JSON ledger checks exact Bessel coefficients, positive-series tail bounds, certified stationary-root brackets, and finite Fourier blocks. It is not a discretized proof of the PDE.

The release remains Route-A rejected and inside `NO_BAD_EULER_OR_ROOT_NUMBER`.
