# Source audit and ownership boundary

## Verified primary and authoritative sources

1. Hidetsugu Sakaguchi, “Cooperative Phenomena in Coupled Oscillator Systems under External Fields,” *Progress of Theoretical Physics* **79**(1), 39–46 (1988), DOI [10.1143/PTP.79.39](https://academic.oup.com/ptp/article/79/1/39/1855689). The publisher record identifies the volume, issue, pages, date, author, and the random-noise/global-coupling setting. This is used as the primary physical source for the noisy coupled-oscillator model.

2. Lorenzo Bertini, Giambattista Giacomin, and Khashayar Pakdaman, “Dynamical aspects of mean field plane rotators and the Kuramoto model,” *Journal of Statistical Physics* **138**, 270–290 (2010), DOI [10.1007/s10955-009-9908-9](https://doi.org/10.1007/s10955-009-9908-9); author manuscript [arXiv:0911.1499](https://arxiv.org/abs/0911.1499). This is used for the reversible mean-field rotator/Kuramoto lineage, Lyapunov structure, stationary profiles, and stability context.

## What this package owns

The package owns a source-local reconstruction under its explicitly frozen normalization. It supplies complete derivations of:

- global classical mass-preserving positive flow for the stated Hölder initial class;
- the free-energy dissipation identity;
- zero stationary flux and von Mises exhaustion;
- strict Bessel quotient monotonicity via an explicit coefficient-pairing proof, with the equivalent strict Turán inequality;
- the exact threshold and uniqueness modulo phase;
- the complete uniform Fourier linearization;
- the analytic two-term critical expansion;
- exact finite Bessel-tail, root-bracket, and Fourier receipts.

## What it does not own

No historical novelty or priority is claimed. No theorem from the cited sources is silently upgraded. In particular, this package does not claim general-initial-data asymptotic convergence, synchronized-profile spectral-gap estimates, disorder, finite-particle limits, Hopf branches, time-periodic solutions, or deterministic \(D=0\) atomic dynamics.

The Route-A evaluation is independent of bibliographic priority. The scope is `NO_BAD_EULER_OR_ROOT_NUMBER`: the source PDE, Bessel functions, and Fourier modes are not interpreted as target arithmetic local data, Euler factors, root numbers, automorphy, a target divisor, a target zero match, a Hilbert–Pólya operator, or Route B.

## Collision boundary

- C322 is a finite-dimensional Kac collision spectral-gap package; C347 is a nonlinear nonlocal parabolic phase transition.
- C339 is Hamiltonian navigation dynamics; C347 is dissipative probability flow.
- C340 is a periodic finite-gap Schrödinger operator; C347 uses Fourier modes only to linearize a probability PDE.

Those mechanisms and theorem outputs are different.
