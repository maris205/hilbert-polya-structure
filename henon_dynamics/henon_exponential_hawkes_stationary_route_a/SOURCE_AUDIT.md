# Source audit

## Frozen primary source

- Alan G. Hawkes, “Spectra of some self-exciting and mutually exciting point
  processes,” *Biometrika* **58** (1971), 83–90.
- DOI: `10.1093/biomet/58.1.83`.
- Verified use: the conditional-intensity definition, the same-event Dirac
  contribution to complete covariance, and the point-spectrum convention.

The paper defines its spectral density with an overall `1/(2*pi)`.  HCS-C265
freezes instead

`S(omega)=integral exp(-i omega t) Gamma(dt)`

with no prefactor.  The manuscript states this conversion every time a
spectral formula is used.

## Claim boundary

The primary source is not cited as evidence of workspace or literature
novelty.  The package contribution is the repository-local closure of one
complete theorem/evidence/release contract.  The self-contained proofs use
only generator algebra, subcritical cluster construction, Fourier inversion,
and Lagrange inversion.

## Nearest repository owners

- C208: linear birth--death branching, not an event-driven conditional
  intensity.
- C214: Brownian diffusion with exogenous Poisson resetting.
- C233: M/M/infinity immigration--death dynamics.
- C246: TCP/AIMD with state-dependent jump rate and multiplicative decrease.
- C263: exchangeable Pólya reinforcement, not chronological self-excitation.

No earlier owner contains Hawkes affine count/intensity transforms together
with the three-way covariance separation.

## Integrity statement

No target prime/zero table, local arithmetic datum, Euler factor, root number,
automorphy statement, target functional equation, or Hilbert--Pólya operator
is used.  Scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.
