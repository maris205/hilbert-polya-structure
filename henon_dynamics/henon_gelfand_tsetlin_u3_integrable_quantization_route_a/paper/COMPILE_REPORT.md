# Deterministic compile report

LuaLaTeX was run twice in each of two fresh temporary directories per revision with `SOURCE_DATE_EPOCH=1788480000` and `FORCE_SOURCE_DATE=1`. The paired bytes agreed for every revision, and `main.pdf` is byte-identical to round 2.

| Artifact | Substantive closure | Pages | Font rows | Bytes | SHA-256 |
|---|---|---:|---:|---:|---|
| `main_round0_original.pdf` | interlacing and explicit arrow completion | 1 | 17 | 131809 | `e8548a86a5cec5f9e8da9550db40ecc5c8efad6261ce9b2401046d12ca388e8b` |
| `main_round1.pdf` | Thimm torus, exact fiber, translated-annihilator closures, boundaries | 2 | 18 | 147870 | `560766e5d48ee16fefab23059353733c6c9c34b3919879d77b796337e6181835` |
| `main_round2.pdf` | unshifted GT branching labels, receipts, sources, Route-A closure | 2 | 19 | 158086 | `e7b793afabb08f01f2dd8b7a5df71812733147125f1e5271540c14409454de1a` |
| `main.pdf` | exact copy of round 2 | 2 | 19 | 158086 | `e7b793afabb08f01f2dd8b7a5df71812733147125f1e5271540c14409454de1a` |

All settled logs contain zero LaTeX/package warnings, overfull or underfull boxes, undefined references/citations, rerun notices, and missing-character reports. Every font row is embedded and subset. `pdftotext` passed title, round, scope, control-byte, `qquad`, `??`, and `TODO` gates. `pdftoppm` rasterized every page. Both final pages were visually inspected at 130 dpi: equations, symbols, title, source line, footer, and margins are legible with no clipping or collision.
