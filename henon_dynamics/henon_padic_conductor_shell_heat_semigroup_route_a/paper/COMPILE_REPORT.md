# HCS-C283 compile report

All three manuscript stages were built with LuaLaTeX under
`SOURCE_DATE_EPOCH=1788220800`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.  Every
stage received two LuaLaTeX passes in each of two fresh temporary directories.
The paired outputs were byte-identical at every stage.

| Stage | Pages | Bytes | SHA-256 |
|---|---:|---:|---|
| `main_round0_original.pdf` | 2 | 150450 | `fe2f90fbe2892b9c0f5a6557595587d447c7b55b77cee3aa98adb5ddd8c190da` |
| `main_round1.pdf` | 2 | 165789 | `71ecf586633a2af92cd3e8530890e9e64214b7cd94fdacb07e3f12ac6e267ee9` |
| `main_round2.pdf` | 3 | 191119 | `9d789d9533e54eb6228f04dece3595a10281c60ae730d53fd3ae6755a64befde` |
| `main.pdf` | 3 | 191119 | `9d789d9533e54eb6228f04dece3595a10281c60ae730d53fd3ae6755a64befde` |

The settled logs are warning-free: no LaTeX/package warning, overfull or
underfull box, undefined reference, multiply-defined label, or rerun request
remains.  The three revision hashes are distinct, and `main.pdf` is a byte
copy of round 2.

- Font audit: PASS — `pdffonts` reports 24 fonts, all embedded and subset.
- Text audit: PASS — extracted text contains the exact Example 5.1 owner,
  quasi-Schatten convention, VVZ citation, zeta lattice, discrete-scale
  oscillation, finite-quotient reconstruction, boundary, scope, and Route-A
  verdict tokens.
- Visual audit: PASS — all seven pages across the three retained revisions
  were inspected at 150 dpi; equations (including the labelled
  `m\to\infty` arrow), proof boxes, headings, references, accents, and page
  boundaries are legible with no clipping, collision, missing glyph, or blank
  page.

Round 0 contains the frozen character owner and Markov reconstruction.  Round
1 adds heat trace, exact counting/log-periodic scaling, and the sharp Schatten
endpoint.  Round 2 adds the full zeta pole lattice and determinant, all
degenerate faces, finite-quotient DFT evidence, the exact Example 5.1
direct-owner boundary, and the hostile Route-A closure.  The revisions are
therefore substantively different.
