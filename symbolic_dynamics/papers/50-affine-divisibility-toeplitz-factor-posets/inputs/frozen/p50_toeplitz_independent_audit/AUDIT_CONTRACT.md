# Reciprocal audit contract

## Scope and frozen input

This directory is an auditor-owned, read-only reciprocal audit of
`/tmp/p50_toeplitz_stage2`.  The builder declared that package stopped and
frozen before this audit began.  Its self-excluding manifest has SHA-256

```text
c070bd76d8a28e1b918fa040d9346db32776f238e7081d8c3504648b137a583e
```

No audit command writes into the candidate.  Reproductions are directed to
auditor-owned subdirectories here.  This package is not an authority,
manuscript, publication artifact, priority claim, or mirror.

## Claims re-audited from definitions

Fix an integer `p>=3`.  For nonzero `m`, let `nu_p(m)` be the largest `e>=0`
for which `p^e` divides `m`; for composite `p` this is only a divisibility
exponent.  Let `u` be a periodic directive of least period `h>=2`, with exact
finite support and unequal cyclic neighbors, and put

```text
L(k) = (p-1)k+1,
x(k) = u_{nu_p(L(k))},
r_N  = (p^N-1)/(p-1).
```

The audit re-proves:

1. the exact one-hole skeleton and essential powers `p^N`;
2. normal simple-Toeplitz form and aperiodicity;
3. the initial-block common-position period is `p^(N+1)` exactly for prime
   `p`, while every composite `p` has the strict counterperiod `ell*p^N`;
4. the high-center identity for every nonzero offset;
5. collapse of every same-base, onto, pointed sliding-block factor to the
   unique surjective letter quotient, at arbitrary finite CHL radius;
6. classification of pointed factor classes by independent-block
   partitions of the cyclic adjacency graph, ordered by refinement, with
   the stated graphical Stirling and chromatic identities.

Wrong-base maps, nonpointed maps, arbitrary Toeplitz factors, and a lattice
claim are outside the contract.  The status vocabulary is restricted to
`PROVABLE AS STATED`, `DISPROVABLE`, or `OPEN/HOLD` for mathematical claims,
and to `STAGE2_CLEAN` or `HOLD` for the terminal audit decision.

