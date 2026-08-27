# C196 compile report

Status: PASS.

## Frozen build

- Engine: LuaHBTeX 1.14.0 (TeX Live 2022/dev/Debian).
- Epoch: `SOURCE_DATE_EPOCH=1787788800`, `FORCE_SOURCE_DATE=1`, UTC.
- Two successful LuaLaTeX passes per artifact; A4 page geometry.

| artifact | pages | bytes | SHA-256 | substantive increment |
|---|---:|---:|---|---|
| `main_round0_original.pdf` | 2 | 150,592 | `2e24674136745c31b864676a29cbb5f37046b9375c0d15da2b46c06137704a28` | signs, simplicity, Newton/completeness, traces |
| `main_round1.pdf` | 2 | 156,448 | `e0707ed751677e8ac58dec6b0048b54f41daaa4b25b550d1835e259c75257b45` | forward/inverse global atlas |
| `main_round2.pdf` | 3 | 171,267 | `efa8b97487763be814a0e3c5b65fe56616a377e3e2aacc7d97e26e611061b008` | both ends, reversal, aperiodicity, schema-closed evidence and exact Route-A tokens |
| `main.pdf` | 3 | 171,267 | `efa8b97487763be814a0e3c5b65fe56616a377e3e2aacc7d97e26e611061b008` | byte-identical round-2 release |

The revision hashes are pairwise distinct; the source changed and was
recompiled between stages.

## Determinism and release checks

Two fresh directories, each seeded only with final `main.tex`, were built
twice at the fixed epoch.  Both hashes equal the release PDF hash above.

- Final and fresh logs: no warnings, undefined references, missing
  characters, overfull/underfull boxes, fatal messages, or errors.
- `pdffonts`: every font embedded and subsetted.
- Text extraction: both abstracts, all formulas, the Route-A tuple, scope,
  declarations, and both DOI references retained.
- Visual audit: all three pages rendered at 140 dpi and inspected; no clipping,
  overlap, collision, broken glyph, blank page, or illegible equation.
- Page 3 intentionally leaves whitespace below compact declarations and
  references; this is not a missing-content defect.
