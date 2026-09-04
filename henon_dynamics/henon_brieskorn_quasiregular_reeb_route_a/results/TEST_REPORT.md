# Test report

## Exact lanes

- Producer: PASS — 1,003 pairs, 5,469,178 fixed-time cells, 4,012 orbit
  types, 3,009 rotations, and 103,749 CZ cells.
- Independent checker: PASS — recomputed the full ledger without importing
  producer code.
- SymPy verifier: PASS — 11,041 exact checks across all 1,003 pairs, including
  contact normalization, tangent identities, rotation determinant, lcm and
  denominator facts, sign, count, and RS identities.
- Isolated replay: PASS — two independent outputs, each 3,787,774 bytes, both
  byte-identical to the committed evidence.
- Hostile mutation: PASS — 61 of 61 attacks rejected.
- Unittest smoke suite: PASS — 3 tests.
- Optimized-mode refusal: exercised by the release gate for `-O` and `-OO`.

## Serialization and evaluator locks

- JSON duplicate keys and nonfinite constants are rejected.
- YAML duplicate and non-string keys, merge keys, anchors, aliases, implicit
  timestamps, unknown fields, and type changes are rejected.
- Evaluation raw SHA-256:
  `d452c49bc188141a22e60a5f3e5b7dacd59ecea99de39ce6e33d1f492d90ade1`.
- Evaluation semantic SHA-256:
  `5af9e8955b35292f87189a87fa1cf7a6ca15aa97d339cba822da940f6a3c3eda`.
- Evaluator SHA-256:
  `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.

## Mathematical boundaries tested

- contact-form factor and Reeb angular-speed changes;
- principal and exceptional period/isotropy mutations;
- fixed-class counts and global streaming digest changes;
- rotation denominator, first degeneracy, determinant convention, and CZ
  sequence changes;
- orbifold sign and principal RS index changes;
- trivialization, theorem-contract, Route-A tuple, scope flag, and Route-B
  changes.

All results use ordinary Python. Finite checks remain regression evidence only.
