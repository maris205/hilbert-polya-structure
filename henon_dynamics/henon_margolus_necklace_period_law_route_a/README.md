# HCS-C165: Margolus necklace period law

This release proves that the binary two-layer Margolus swap automaton on a
ring of `2m` sites is, at the complete `B after A` clock, exactly conjugate
to cyclic rotation of an `m`-letter word over the four-letter alphabet
`{0,1}^2`.

The package contains:

- the all-size fixed, exact-period, primitive-cycle, and finite-zeta law;
- the uniform bound `Pr(period<m)<=m/2^m` with `m=1` retained;
- an explicit reflection reversor, finite Koopman determinant, and
  antiunitary reversal;
- deterministic evidence, a producer-independent checker, SymPy
  reconstruction, byte replay, repaired-hash hostile mutations, bilingual
  paper stages, and a closed release manifest.

Run the exact audit commands listed in `code/README.md`.  The strict Route-A
tuple is

```text
(A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION),
overall ROUTE_A_EXPLORATORY,
route_b_invocation_allowed=false.
```

The model is exactly solvable and is not described as chaotic or interacting.
No target divisor, target global analytic structure, arithmetic local factor,
Euler factor, root number, automorphy object, self-adjoint Hilbert--Polya
operator, or Route-B authorization is claimed.
