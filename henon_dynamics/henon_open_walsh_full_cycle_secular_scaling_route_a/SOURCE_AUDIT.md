# C158 source audit

## Frozen source

C158 uses exactly the C148/C153 three-symbol Walsh gate: normalized DFT
`F3`, projector `P=diag(1,0,1)`, one-site gate `A=F3^*P`, and cyclic tensor
shift `B_k`.  One application of `B_k` is one tick; the paper's full cycle is
exactly `k` ticks.  The secular convention is `E_k(z)=det(I-zB_k^k)`.

The scaling convention is fixed once: for a nonzero eigenvalue `rho` of
`C_k=B_k^k`, set `X_k=k^(-1)log|rho|` and weight by its algebraic
multiplicity among the `2^k` surviving eigenvalues.  Secular-zero inverse
radii and phases are not silently substituted.

## Evidence and independence

The producer uses exact `Q(sqrt(3),i)` Newton coefficients, literal dense
Kronecker matrices through `k=3`, and exact binomial integers through `k=24`.
Decimal logarithms are sentinels only.  The checker imports no producer code,
reconstructs all algebra and combinatorics, and repeats literal matrices.
SymPy separately computes one-site and moved-hole characteristic polynomials,
`k<=2` Kronecker determinants, tensor traces, and modulus identities.  Replay
requires byte identity; each hostile semantic mutation has a repaired hash.

## Firewall

No target table or divisor, prime input, arithmetic local or Euler factor,
root number, automorphy datum, Hilbert--Polya operator, self-adjoint limit, or
Route-B input is used.  Literal scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.
