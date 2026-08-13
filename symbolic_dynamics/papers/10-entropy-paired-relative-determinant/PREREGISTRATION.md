# SD-C12 Preregistration

## Frozen question

Can entropy-adjacent grading cancel the zero-order divergence of the
tensor-prime atom transfer, preserve every repetition trace, and support an
`s <-> 1-s` completion without importing an adjoint or another system family?

## Frozen construction

```text
D_s^+ = diag(p_1^(-s),p_3^(-s),...)
D_s^- = diag(p_2^(-s),p_4^(-s),...)
R(s,z) = det_F[(I-zD_s^+)(I-zU^*D_s^-U)^(-1)]
H(s,z) = R(s,z)R(1-s,z)
```

Primary normalization: `z=1`. No target zeros are loaded.

## Success criteria

- Trace-norm holomorphy of `D_s^+-U^*D_s^-U` on `Re(s)>0`.
- Exact product and all-order relative trace expansion.
- A common reflected strip containing the full critical line.
- A proof that the critical-line function is nonconstant.
- Exact classification of the resulting prime/repetition signs.

## Stop criteria

- `STOP_POSITIVE_EULER_ORIENTATION` if any prime sector receives a negative
  fixed grading sign.
- `STOP_DIVISOR` if the completed determinant is zero-free in its proved strip.
- `STOP_SCOPED / PROVES_TOO_MUCH` if arbitrary paired inventories satisfy the
  same analytic theorem.
- `ROUTE_A_REJECTED` if the fixed super-parity sign fails the target ledger,
  even when the auxiliary relative determinant is exact.
- `ROUTE_B_LOCKED` unless a fixed self-adjoint operator and exact arithmetic
  trace formula arise from this same object.

## Controls

- reverse the grading orientation;
- shift the adjacent pairing by one rank;
- use blocks larger than two with zero coefficient sum;
- replace primes by sorted composites, random integers, or any matched
  increasing inventory;
- distinguish fixed super-parity from a repeated unitary cocycle phase.
