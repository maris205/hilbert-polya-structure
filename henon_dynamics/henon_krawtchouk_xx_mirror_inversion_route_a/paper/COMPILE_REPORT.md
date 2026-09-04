# Compile report — HCS-C366

All revisions were built twice in fresh temporary directories with two
LuaLaTeX passes per build, `SOURCE_DATE_EPOCH=1788480000`,
`FORCE_SOURCE_DATE=1`, and `TZ=UTC`.  The paired bytes agree.  Settled logs
contain no layout, citation, reference, rerun, missing-character, or backend
warning. Every font row is embedded and subset; every page extracts without
visible garbage after normalization of the three documented math-glyph
markers emitted by Poppler, and every page rasterizes. Both final pages were
also inspected visually at 120 dpi.

| round | pages | font rows | SHA-256 |
|---:|---:|---:|---|
| 0 | 2 | 20 | `2820e5d9dfd2679e7de5aa93f947f0f2e2d12059583756baf2e3f17c16267152` |
| 1 | 2 | 20 | `6b8579c1e2aee7c4683e4210163cea4f2b5ba7d7bd34a0998fd26edd8ba9f49d` |
| 2 | 2 | 18 | `5e0fba2c3c07462971e6e3d76e16b33bcb0b8c2419d779ebe8f344f289338ff5` |

`paper/main.pdf` is byte-identical to Round 2.  The three revision hashes are
pairwise distinct and carry, respectively, the single-particle owner, the
many-body phase plus Gaussian recurrence, and the exact field-revival/Route-A
boundary audit.
