# P207 manuscript A — actual source-only build and page inspection

2026-09-06 UTC. Independent reviewer `batch197_lzk_gate`.
One actual A-stage source-only cold build completed with exit zero.
Its seven-page PDF is raw-byte-identical to the reviewed Round0 PDF:
407,557 bytes, SHA-256
`5e74fa6a334f1cbc23837632b364729d97111b231e1ef8c3fd6a40a8dbc78759`.
All seven pages were rendered and actually opened by this reviewer.

## Executed build

The project's `paper-compile` skill supplied source-only build, diagnostic,
font and visual checks. Its default latexmk route is unavailable here;
the disclosed existing pdflatex/BibTeX fallback was used. The shared batch
script was read in full and is pinned in CONTEXT_SOURCE_PINS.sha256; it
was not changed. It copies only main.tex, math_commands.tex, references.bib
and the six sections into a fresh mktemp directory, compiles there, then
moves the complete successful build into this review's owned directory.
No author PDF or auxiliary file was a build input.

Actual command, from the workspace root:

```sh
bash /root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/qa/cold_build.sh /root/autodl-tmp/symbolic_dynamics/papers/207-upper-neighbor-rank-dynamics/frozen_round0 /root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/reviews/p207_a/cold_build_01 /root/autodl-tmp/symbolic_dynamics/papers/207-upper-neighbor-rank-dynamics/frozen_round0/main.pdf
```

The actual command returned `SOURCE_ONLY_BUILD_COMPLETE`, the PDF hash
above and exit zero in 1.636293713 seconds. Because the script uses
`set -euo pipefail`, this includes the actual raw `cmp` against the frozen
PDF after pdflatex/BibTeX/pdflatex/pdflatex. No second A cold build or
post-review terminal build is claimed by this report.

The retained [build directory](cold_build_01/) contains all nine source
hashes, exact sources, all pass stdout, final LaTeX log, BibTeX stdout/log,
recorder files, PDF, extracted text, metadata, fonts and diagnostics.
Engine: pdfTeX 3.141592653-2.6-1.40.22, TeX Live 2022/dev/Debian;
BibTeX 0.99d; kpathsea 6.3.4/dev. Settings actually used:
`SOURCE_DATE_EPOCH=1704067200`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`, `LC_ALL=C`.
DIAGNOSTICS.txt is zero bytes: no final undefined/reference/citation,
overfull or warning hit. The extracted text has no TODO/FIXME/XXX/[VERIFY]
or unresolved `??` marker. All 31 font rows are embedded. PDF metadata
has no author identity, encryption, JavaScript or forms; page size is A4.

## Actual visual review

Actual rendering command:

```sh
pdftoppm -r 105 -png docs/papers204_208_sequence/reviews/p207_a/cold_build_01/main.pdf docs/papers204_208_sequence/reviews/p207_a/page_views/page
```

It exited zero. I actually opened pages 1–3, then pages 4–7, using the
newly rendered PNGs. Since this PDF is raw-identical to the frozen PDF,
these are views of the exact frozen manuscript, not a look-alike layout.
Their equality to author image hashes does not substitute for this actual
inspection.

| Page | Checked content and visual result |
|---|---|
| 1 | Anonymous title, accurate computer-assisted/nonsharp abstract, literal strict rule, source-access and scope paragraph; readable, no clipped equation |
| 2 | Radius-six domains, full 11-word/extension coverage, uniform bound and start of core proof; proof split is coherent |
| 3 | Core converse, role-transition table, determinant, recurrence and seed formula; subscripts and matrix display intact |
| 4 | Seed meeting/H(3) boundary and complete positive-run source table; no lost table rows or overlapping text |
| 5 | All eight kernels, full inverse trace, precise norm exponents and first mixed cases; matrices readable and inside margins |
| 6 | Remaining strict mixed inequality, length budget, all equality branches, classical adapters and limits; no cropped proof text |
| 7 | Four references with DOI/URL rendering; intentionally sparse references-only page, no missing glyph or broken visual URL |

Actual PNG SHA-256 values:

```text
1 ae0bc555f8857f08f53d4246d55ca0a48da25f409159df55a5fe2ddebc028410
2 2e3869358de479de69e13f83fd7c73c6306fd4045a37f0d2c3fe4e7e431869ff
3 b998823379bbba47d70aef9da25ecb3abd8703627a692a6dda4445b22717e9e9
4 769d9d58dab1430bf8d39359285dce4416e0e0824ebee54940c135f83cf622df
5 a539f2796c5d5c5ac4072ca9fcedd7e5a2c81d400df5f2d2f9a4ae72fe628ff7
6 c383a5807d6ed22fd9fa12580cfbede229b296646ab4c5d7ea60b63bad23da4d
7 4497cef8cab1e0f2ec938cb8fb8a58a7c9d4cc187e19e7ad25b86cd372514b14
```

No build or visual repair is requested. The author's earlier failed and
overfull builds remain historical evidence outside this review; none is
counted as this successful cold build. This report does not grant a
manuscript delta, Round1, Review B or terminal artifact acceptance.
`OWNER_AMBER / HOLD_EXTERNAL`.
