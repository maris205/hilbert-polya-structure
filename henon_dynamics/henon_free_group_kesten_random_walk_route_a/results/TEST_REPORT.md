# Test report

All commands run from the package root with Python bytecode disabled.

- Producer: `C355_PRODUCER_PASS`; 1,156 radial rows and 260 return rows reported.
- Independent checker: PASS; 1,997 rows and 9,483 exact scalar cells.
- SymPy: PASS; 237 exact symbolic checks.
- Replay: PASS; two isolated directories, 345,608 byte evidence, byte-identical to checked evidence.
- Hostile suite: PASS; 74/74 attacks rejected.
- Optimized mode: producer, checker, SymPy, replay, mutation, and release entry points reject both `python -O` and `python -OO`.
- YAML: duplicate, anchor, alias, merge, non-string key, implicit date spelling, unknown field, root type, identity, branch status, and Route-B attacks rejected.
- JSON: duplicate keys, nonfinite constants, root type, stale payload hash, repaired semantic hashes, nested extras, row omission, and row duplication rejected.

The release script additionally performs fresh double builds of all three revision PDFs, font/text/raster gates, exact 27-payload closure, and manifest replay.
