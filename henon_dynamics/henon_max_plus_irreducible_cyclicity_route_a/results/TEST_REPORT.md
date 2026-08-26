# C188 test report

## Executable checks

- Producer: PASS — 177 matrices, 901 vectors, 441 cycles, 189 critical SCCs,
  5,469 CSR cells and 7,471 propagation cells.
- Independent checker: PASS — 7,924 assertions and no producer import.
- SymPy path: PASS — 10,615 exact checks.
- Replay: PASS — 781,170 bytes and exact SHA-256 match.
- Mutation: PASS — 137 repaired-hash attacks and one stale-hash attack.

## Independence

The producer enumerates elementary cycles and advances powers sequentially.
The checker instead uses Karp's dynamic program for `lambda`, truncated Kleene
closure for critical edges, Tarjan SCCs, directed-distance gcd for cyclicity,
permutation enumeration for cycle-ledger completeness, and binary
exponentiation for powers.  SymPy supplies a third exact-rational type and
reconstructs cycle means, period cells, CSR cells, vector strata and the
symbolic transient-family branches.

## Coverage boundary

The regression covers integral and fractional weights, finite and `-inf`
entries, one- through six-node supports, primitive and imprimitive critical
graphs, multiple critical SCCs, strict smaller vector periods, arbitrary
transient sentinels through 24, and a reducible multirate control.

It does not prove the classical all-irreducible cyclicity or CSR theorem.
Those statements are source-locked in `SOURCE_AUDIT.md`; the executable paths
test the implementation and package-derived consequences.
