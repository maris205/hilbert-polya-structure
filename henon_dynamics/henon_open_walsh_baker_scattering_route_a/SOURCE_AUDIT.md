# C148 source audit

## Source class

C148 is an internally defined exact linear-dynamical construction.  It uses no
downloaded data, literature table, fit, target divisor, or external numerical
observation.  All entries lie in `Q(sqrt(3),i)`.  The only inputs are the
three-point unitary DFT, the frozen rank-two projector, tensor products, and a
cyclic factor shift.

## Frozen conventions

- `omega=exp(2*pi*i/3)=(-1+i*sqrt(3))/2`.
- `F3[j,l]=omega^(j*l)/sqrt(3)` for indices `0,1,2`.
- `P=diag(1,0,1)` and `A=F3^* P`; projector order is not interchangeable in
  matrix geometry, even though the chosen order control is spectrally similar.
- Qutrit words are lexicographically ordered.
- One clock tick is one application of
  `B_k(v0,...,v_(k-1))=(v1,...,v_(k-1),A*v0)`.
- `D_k(z)=det(I_(3^k)-z B_k)`.
- Exact coefficient receipts use the ordered basis
  `(1,sqrt(3),i,sqrt(3)*i)`.
- Polynomials are frozen for `k=1,...,5`; the trace theorem itself has no
  period cutoff.

## Independence and replay

The producer uses a four-coordinate exact field, direct sparse propagation,
permutation-cycle traces, and Newton identities.  The standard-library checker
imports no producer module and reconstructs Fourier/Gram identities, all 363
small-`k` source-vector instances of `B_k^k=A^(tensor k)`, 60 direct trace
sentinels, every polynomial coefficient, controls, and boundaries.  SymPy
independently builds literal sparse matrices for `k=1,2`, verifies the
one-qutrit characteristic polynomial, and reconstructs all `k=1,...,5`
coefficients.  Byte replay and repaired-hash hostile mutations are separate
processes.

## Firewall

No target zeros or divisors, primes, arithmetic local data, Euler factors,
root numbers, automorphy input, Hilbert--Polya object, or Route-B input appears.
The antiunitary question is explicitly left unasserted.  Literal scope:
`NO_BAD_EULER_OR_ROOT_NUMBER`.
