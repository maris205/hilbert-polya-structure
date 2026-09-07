# P209 actual source-only author builds

2026-09-07 UTC. **TWO_AUTHOR_BUILDS_PASSED / NOT_TERMINAL_ACCEPTANCE /
OWNER_AMBER / HOLD_EXTERNAL.** These are two physical author-stage builds,
not the later post-review terminal gate.

Both builds began in new directories containing only the eight specified
TeX/bibliography sources: `main.tex`, `math_commands.tex`, `references.bib`,
the abstract, and four body sections. No auxiliary file, bibliography
product, PDF or PNG was copied into either initial source directory.
The actual initial source inventories are
[build 01](author_build_01/SOURCE_ONLY_INITIAL.json) and
[build 02](author_build_02/SOURCE_ONLY_INITIAL.json).

## Actual commands and output

From the workspace root, the two actual outer commands were:

```sh
/usr/bin/env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/python3.10 -I -S -B -X pycache_prefix=/root/autodl-tmp/symbolic_dynamics/papers/209-ordered-fibre-threading/launcher_author_build_01/never_created_launcher_cache /root/autodl-tmp/symbolic_dynamics/papers/209-ordered-fibre-threading/launch_author.py build author_build_01
/usr/bin/env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/python3.10 -I -S -B -X pycache_prefix=/root/autodl-tmp/symbolic_dynamics/papers/209-ordered-fibre-threading/launcher_author_build_02/never_created_launcher_cache /root/autodl-tmp/symbolic_dynamics/papers/209-ordered-fibre-threading/launch_author.py build author_build_02
```

Both outer recorders actually exited zero. `latexmk` was unavailable, so
the installed engine and bibliography tools were used directly:
`pdflatex -no-shell-escape -recorder -interaction=nonstopmode -halt-on-error`,
then BibTeX, then two more identical TeX passes. Exact argv, environment,
cwd, pre-spawn attempts, exit codes and full stdout/stderr for every
command are retained in each build directory. Each TeX pass also has its
own complete `.log`, `.fls` and `.aux` copy; first-pass messages were not
replaced with the final-pass log. The final `.bbl` and `.blg` are preserved.

| Actual result | Build 01 | Build 02 |
|---|---:|---:|
| Pages, including references | 4 | 4 |
| PDF bytes | 280,267 | 280,267 |
| Embedded fonts | 20 | 20 |
| Final undefined/overfull/underfull/rerun/warning entries | 0/0/0/0/0 | 0/0/0/0/0 |
| Known inputs including copied sources | 118,409 | 118,409 |
| TeX resource files | 113,733 | 113,733 |
| Actually consumed external TeX/style files | 131 | 131 |
| Runtime/configuration files | 4,598 | 4,598 |
| Actual linkage commands, each exit zero | 110 | 110 |
| Complete nonself build payloads | 680 | 680 |

The inner originals are [build 01 receipt](author_build_01/RECEIPT.json)
and [build 02 receipt](author_build_02/RECEIPT.json); outer full-stream
receipts are [01](launcher_author_build_01/RECEIPT.json) and
[02](launcher_author_build_02/RECEIPT.json). Both PDFs have SHA256
`ca2e381904905939e121b7931641b050ba24657c16661df3bb5008c88c28884f`.
The separate finalization receipt records the subsequent actual raw PDF
comparison and live PDF adoption; matching digests alone are not labelled
an executed `cmp`.

Build 01's complete seal is
`75993f66283d19066dcbeaed011c238ad194e98eaec6dd6b12386f99cafddae6`;
build 02's is
`514f75cec0fa3e288c686979a1baa6b69704d91c0fd31e5ed78d5f4302b8636f`.
The corresponding ten-payload launcher seals are
`39ff6800968423e04994eca06b1a32a065bba8d874b7563adce68a79c28528f1`
and `e10f900d85c47702a78e423d62ea5b551f8ef0ccc641515b4d1543548e0288ab`.

## Build key and limits

The build environment sets `SOURCE_DATE_EPOCH=1788652800`,
`FORCE_SOURCE_DATE=1`, `openin_any=p`, `openout_any=p`, and separate
absent `TEXMFHOME`, `TEXMFCONFIG`, `TEXMFVAR` roots for each build.
The engine's actual resolved user roots were queried and stayed absent.
The complete TeX resource forest, bibliography/style sources, formats,
fonts, Poppler/fontconfig inputs, configured local font directory including
hidden files, loader/locale/gconv, and optional user/XDG configuration
presence were pinned before child execution and recaptured afterwards.
Every `.fls` external input is covered; generated local auxiliaries are
recorded separately rather than mislabelled original sources.

Recorded mapped/imported files have no uncovered dependency or bytecode.
These sampled observations and conservative inventories are not continuous
or grandchild tracing and do not establish OS-hermetic reproducibility.

Each build passed on its first actual attempt. No source correction,
numerical rerun, hidden replacement build or manuscript change was needed.
All 70 already-pinned science/framing inputs remain unchanged. The four-page
note lies within the assigned approximately four-to-six-page scope; its
complete proofs are in the main text, with no missing proof appendix.

Every page of both PDFs was actually viewed individually, as documented in
[PAGE_VIEWS.md](PAGE_VIEWS.md). The immutable build receipts correctly
retain their earlier `NOT_YET_VIEWED_RENDER_NOT_A_VIEW` status; the later
viewing record supplements them without rewriting their history. Anonymous
author/running heads, equations, body text and all four references are
legible. No clipping, overlap, missing symbols or layout defect was found.
