# Results

- 32 regular negative-energy resolvent cells and three isolated physical poles.
- 28 exact scattering cells with unit flux.
- Three normalized attractive bound-state cells.
- Eight 80-digit heat/relative-trace cells.
- Independent duplicate-rejecting checker: 1,726 assertions, including
  unique/complete cell grids, interface reconstruction, numerical inverse
  Laplace heat reconstruction, and integrated diagonal resolvent traces.
- Symbolic reconstruction: 46 checks.
- Replay: two isolated outputs byte-identical to the retained evidence.
- Mutation suite: 30/30 attacks rejected, including repaired-hash theorem
  heat/resolvent edits, duplicate/drop resolvent and heat cells, raw duplicate
  keys, unknown/missing keys, type confusion, and stale hashes.

The evidence payload hash is recorded inside
`c288_delta_evidence.json`.  The finite grid is an audit, not the proof of the
all-parameter theorem.
