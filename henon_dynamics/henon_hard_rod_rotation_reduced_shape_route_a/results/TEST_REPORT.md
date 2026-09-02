# Test report

- deterministic producer: PASS, 149 audited cells
- strict independent checker: PASS, 2,685 assertions, including recursive exact boundary/source/nonclaim contracts
- SymPy/exact finite-group cross-check: PASS, 159,064 identities
- isolated evidence replay: PASS, 2/2
- hostile mutation suite: PASS, 96/96

The checker independently reconstructs pair congruences with a loose winding
scan, aggregates coincidence blocks, canonicalizes quotient shapes, computes
velocity-class stabilizers, applies the lcm criterion, and verifies every
`sigma,c` witness.  It imports no producer implementation.

Both evidence JSON and evaluation YAML reject duplicate keys, non-finite JSON,
unknown or missing keys, wrong exact types, altered theorem/proof text, tuple,
overall verdict, Route-B flag, scope flags, event grids, return witnesses,
the complete boundary/nonclaim trees, every source-metadata field, and the frozen obstruction ID.
The regenerated YAML semantic SHA-256 is
`5e0c4609143ece03f46cab5822ba104af41b2513698dba999f8d4bf86b6e8ed1`.
