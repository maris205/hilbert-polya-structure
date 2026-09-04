# C361 compile report

Frozen engine: LuaHBTeX 1.14.0 (TeX Live 2022/dev/Debian), `SOURCE_DATE_EPOCH=1788480000`, `FORCE_SOURCE_DATE=1`, two passes in each fresh directory.

| Artifact | Revision content | Pages | Fonts | SHA-256 |
|---|---|---:|---:|---|
| `main_round0_original.pdf` | theorem, conventions, complete core proof | 2 | 15 | `dd93e9dbe4f127b1fb676453d618a20d6e8f69cc2124a49499eeecf1b23f9e32` |
| `main_round1.pdf` | round 0 plus sharp boundary atlas and minimal cycle | 2 | 15 | `63269dcd3825ce3adeb9ea5c8690d375210f1d0c856f6817186359b75220a248` |
| `main_round2.pdf` | round 1 plus evidence, source, and scope closure | 2 | 16 | `f8511cec232fa8696d16a3961c36e76304095244123e1823738d41327cfa30d3` |
| `main.pdf` | byte-identical final alias of round 2 | 2 | 16 | `f8511cec232fa8696d16a3961c36e76304095244123e1823738d41327cfa30d3` |

The three revision PDFs are pairwise byte-distinct. Double-fresh builds are byte-identical to stored artifacts. Settled logs contain no LaTeX/package warnings, overfull or underfull boxes, undefined references, or missing glyphs. `pdffonts` reports every font embedded and subset. `pdftotext` finds required title/scope sentinels and no control garbage, bare `qquad`, or `??`; `pdftoppm` rasterizes every page.
