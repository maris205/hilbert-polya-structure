# Hostile audit — HCS-C225

The mutation harness edits copies of the evidence only.  It repairs the
top-level payload hash after each semantic mutation, so a hash-only gate cannot
hide a wrong claim.  Mutations cover source/evaluator/epoch and scope locks,
generator and theorem text, Route-A verdict, citation DOI, grid closure,
stationary weights, eigenvalues/eigenvectors, transient probabilities, mixing
bound, capacity-limit value and boundary convention.  It also injects an
unknown top-level key and an unknown nested row key.  Every repaired mutation
is rejected by the producer-independent checker; an un-repaired stale-hash
mutation is rejected as well.

The audit explicitly guards against promoting a finite characteristic
polynomial to an infinite Fredholm determinant or promoting a formal Jacobi
similarity to a Hilbert--Polya construction.
