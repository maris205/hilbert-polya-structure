# C129 research question

Can the all-period graph-directed Hardy--Fredholm owner of C124 acquire an
exact, source-defined phase that distinguishes some affine translation
assignments while retaining trace class, the complete power-trace law, and the
primitive-cycle product?

A falsifying companion question is essential: what remains invisible after
one frozen finite character is added?

## Answer certified here

Yes, in a deliberately limited sense. Integer branch translations define a
fixed character `chi(m)=zeta_5^m`. Multiplying each branch weight by its phase
gives a trace-class weighted-composition operator on the same Hardy space. Its
power traces, lattice Fredholm product, and primitive repetition identity hold
at every order.

Two translation triples have the same linear part, unordered image centers,
graph, rational weights, and entire untwisted determinant. Nevertheless their
twisted symbolic determinants already differ in degree one, and so do their
Hardy Fredholm determinants. At the trivial character both constructions
degenerate exactly to C124.

This is finite-quotient sensitivity, not reconstruction: one character cannot
recover translations beyond residues and branch assignment, and no target
divisor is compared. Strict verdict:

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)
ROUTE_A_EXPLORATORY
route_b_invocation_allowed: false
```
