# HCS-C366 — Krawtchouk XX mirror inversion

This package proves the complete single- and many-particle dynamics of the
engineered Krawtchouk XX chain.  Its main increment is a convention-exact
Fock-space mirror theorem, including the fermionic reordering phase and full
Gaussian-binomial energy multiplicities, rather than five fragments of a
one-particle computation.

Start with [THEOREM_PACKAGE.md](THEOREM_PACKAGE.md), then inspect the
[source audit](SOURCE_AUDIT.md), [evidence report](results/RESULTS.md), and
[paper PDF](paper/main.pdf).

Route-A result:

```text
(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)
overall = ROUTE_A_REJECTED
route_b_invocation_allowed = false
scope = NO_BAD_EULER_OR_ROOT_NUMBER
```

The package contains 27 content-addressed payloads plus one self-excluded
release manifest.

The final exact receipt contains 65,534 Fock states, 231 formal all-time
endpoint cells, and 136 full Gaussian $q$-binomial coefficient polynomials.
Its producer-independent checker owns every nested key, coordinate, and leaf
type; finite computation remains regression evidence rather than the proof.
