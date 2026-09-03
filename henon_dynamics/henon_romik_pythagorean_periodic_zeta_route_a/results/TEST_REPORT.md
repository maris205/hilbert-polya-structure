# Test report

- Producer: PASS, 9,840 word rows and payload SHA-256
  `4900fc4f72fdcd61e5f09e0be92c6d6ade46326fe3d0f73536aa59e8667b5810`.
- Independent checker: PASS, 290,403 exact checks; it imports no producer.
- SymPy lane: PASS, 2,833 symbolic/exact checks.
- Isolated byte replay: PASS, 6,025,765 identical bytes.
- Hostile mutation lane: PASS, 72/72 rejected, including repaired-hash,
  nested ownership, JSON/YAML parser, and optimized-Python attacks.
- Paper: PASS, fresh two-build determinism for all three substantive rounds,
  pairwise-distinct round hashes, main=round2, embedded/subset fonts, clean
  logs, nonempty raster pages, clean extracted text, and visual inspection.
- Closure: PASS, exactly 28 physical files and 27 self-excluding manifest
  payload files; the release checker refuses stale manifests and sidecars.

Evidence file SHA-256:
`756fe52e75e29486eed3f6e2f75edf4ec5e0273c2e17caac14a93e2ce9bac2bb`.
