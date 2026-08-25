# C168 source audit

## Frozen source object

- Candidate: `HCS-C168`.
- Source commit: `4342893ce5e2516924181744bfacc01c12e4959d`.
- One-site gate: `A=F4^*diag(1,0,1,1)` with the unitary four-point DFT.
- Clock: one `B_k` application is one tick; `C_k=B_k^k=A^(tensor k)` is one
  complete register cycle of exactly `k` ticks.
- Spectral convention: retain nonzero eigenvalues with algebraic
  multiplicity, normalize their measure by `3^k`, and use
  `phase(rho)=rho/|rho|`.
- Joint normalization:
  `Y_k=(log|rho|+k log(2)/3)/sqrt(k)`.

No parameter is fitted.  The hole position, DFT convention, tensor clock,
and weighting are frozen before computation.

## Allowed evidence

Exact finite-dimensional matrix algebra, tensor-product identities,
multinomial coefficients, Fourier transforms on the circle and on
`Z/4Z`, the elementary iid central limit theorem, and deterministic finite
sentinels derived from the frozen source are allowed.

## Excluded inputs and claims

No target zero/divisor table, prime data, arithmetic local data, Euler
factor, root number, automorphy input, or Hilbert--Polya assumption is used.
No target divisor, functional equation, or counting-law comparison is made.
Route B remains false.  Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Evidence status

The all-`k` claims are proved symbolically.  Ledgers through `k=24` and
Fourier modes through `|m|=24` are implementation sentinels only.  No
external reviewer or acceptance score is represented.
