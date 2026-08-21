# HCS-C80 all-20-subgroup threshold-repair atlas

C80 changes the target of repair.  For a deletion set `D` and retained
support `A=L\\D`, and for each of the 20 actual subgroup rows `H` of
`Q=Z/9 + Z/3 + Z/2`, define

```text
tau_H(D) = min{|R| : R subset D and H subset Phi(A union R)}.
```

This is a containment threshold, not an exact-closure repair.  The full-core
row is the one exception: `tau_Q(D)=rho(D)` exactly.  The receipt enumerates
all 65536 masks, stores the complete 20-component profile for every retained
mask, and publishes one deleted-cardinality table and one threshold
distribution for each target row.

Target subgroup orders, in the committed row order, are

```text
1,2,3,3,3,3,6,6,6,6,9,9,9,9,18,18,18,18,27,54.
```

The canonical evidence SHA-256 is
`8d27428b14dbd7354e9c8308ad76b1108e3f551702165833301509cd52de7df5`.
The independent checker reconstructs target-minimal support antichains rather
than trusting the producer's dynamic program; the SymPy check verifies every
cardinality marginal and the C78 polynomial; replay and 13 hostile mutations
also pass.

This is a finite named-support containment atlas.  It does not claim a full
table of marks or Burnside ring, arithmetic/local information, Euler factors,
root numbers, automorphy, or a Hilbert--Polya operator.  Scope firewall:
`NO_BAD_EULER_OR_ROOT_NUMBER`.
