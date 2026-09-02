# Research question — HCS-C284

Can the classical equal-circulation Thomson polygon be reconstructed from its
source Hamiltonian through the raw Cartesian Hessian, cyclic DFT blocks, sharp
`N=6/7/8` stability threshold, symmetry reduction, and every singular boundary
in one independently executable Route-A package?

The answer is yes for the source-local linear theorem.  The DFT block sign is

`2*(N-1)-m*(N-m)`.

It is positive on every reduced block for `N=3..6`, zero only at
`N=7,m=3,4`, and negative for at least one block for every `N>=8`.

The question deliberately excludes nonlinear stability of the heptagon,
unequal circulations, central vortices, multiple rings, vortex patches,
collisions, and all arithmetic target claims.  Its Route-A outcome is

`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`, `ROUTE_A_REJECTED`, with Route B
locked false.
