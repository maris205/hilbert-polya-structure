# C424 final fixed-input build and full-PDF inspection

2026-09-09 UTC. Paper-local execution status:
**FINAL_DOUBLE_BUILD_AND_ALL_PAGE_CHECK_COMPLETE — NOT SEALED**.
The coordinator explicitly accepted both actual nonauthor manuscript
reviews as PASS/no-change before authorizing this execution. This report
records exactly two new presentation builds and their inspection, not a
third manuscript review, mathematical execution, formal evaluation or
global release approval. No manuscript input was revised.

## Frozen input identity and true build pair

The existing `scripts/build.sh` was read completely before use. Its
SHA-256 is `325f26d449cf2893d46f218aecf82dc7d7ea31b11b479dcb5bc403b7210baf1e`.
It runs latexmk/pdfLaTeX/BibTeX, then `pdfinfo`, `pdffonts`, `pdftotext`
and a PDF hash. It neither imports nor executes either mathematical
Python file or the receipt renderer.

Both `build/final_frozen_01/` and `build/final_frozen_02/` were checked
to be absent before the pair. They are new directories, not reused
initial or revision builds. The exact successful top-level commands,
run from this paper directory, were:

```bash
bash scripts/build.sh build/final_frozen_01
bash scripts/build.sh build/final_frozen_02
```

Each script invokes the same command apart from its output directory:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error \
  -outdir=build/final_frozen_01 main.tex
```

For the second command the output directory is `build/final_frozen_02`.
The actual script retains the complete console output via `tee` and
uses `set -euo pipefail`; both observed script exit codes were **0**.

| Actual build | Top-level exit | pdfLaTeX runs | BibTeX runs | Final PDF |
| --- | --- | --- | --- | --- |
| `build/final_frozen_01/` | 0 | 3 | 2 | 21 pages, 463423 bytes |
| `build/final_frozen_02/` | 0 | 3 | 2 | 21 pages, 463423 bytes |

The internal counts come from each actual `latexmk.console.log`'s
`Run number ... of rule` records, not from an assumed build recipe.
There were exactly two final build commands, zero failed final builds,
zero retries and no third final build. Their internal passes are not
separate review rounds. All original initial-build directories and
their logs remain preserved.

All 29 entries of `INPUT_MANIFEST.sha256` passed before and after the
pair. The unchanged manifest SHA-256 is
`ea282bedc12d736c9a0e421e5448744504ef742b593d6ebaf07368b27b090f63`.
It was copied without alteration into each final build directory.
Every current listed file also compares byte-for-byte equal to the
preserved source/evidence snapshot `baseline/round0_layout1/`.
This includes both scripts, both full mathematical programs, both JSON
outputs, the complete C412 PDF and all other evidence inputs. No table
regeneration was needed; `tables/residual_rows.tex` remained unchanged.
The author reporting documents and this report are not LaTeX inputs.

## Actual tool environment and deterministic controls

The inspected environment was Linux `5.15.0-78-generic`, x86_64,
GNU/Linux. Executables resolved to `/usr/bin/bash`, `/usr/bin/latexmk`,
`/usr/bin/pdflatex`, `/usr/bin/bibtex`, `/usr/bin/pdfinfo`,
`/usr/bin/pdffonts`, `/usr/bin/pdftotext` and `/usr/bin/pdftoppm`.

- GNU Bash 5.1.16(1)-release.
- Latexmk 4.76, 20 November 2021; actual rc file `/etc/LatexMk`.
- pdfTeX `3.141592653-2.6-1.40.22`, TeX Live 2022/dev/Debian;
  LaTeX2e `<2021-11-15>`, L3 programming layer `<2022-01-21>`.
- BibTeX 0.99d, TeX Live 2022/dev/Debian; `plainnat.bst`.
- Poppler PDF tools 22.02.0 (version checked through `pdfinfo` and
  `pdftoppm`).

Both actual build invocations inherit the unchanged script's exports:
`SOURCE_DATE_EPOCH=1788912000`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`,
`LC_ALL=C`. The unchanged TeX source suppresses PDF dates and trailer
identifiers using its existing pdfTeX controls. These are the recorded
controls for this observed pair, not a promise of identical bytes on
arbitrary future toolchains. Each `main.fls` retains the actual package,
font and file recorder inventory.

## Byte comparison and final selection

`cmp build/final_frozen_01/main.pdf build/final_frozen_02/main.pdf`
returned exit **0**. Both PDF SHA-256 values are
`3a1eadac84dd7fe9b730cde464bbc31a80469963aa984ac3a7117936e7bdf98b`.
This is also the exact digest of the two-round-reviewed PDF.

After inspection, `build/final_frozen_02/main.pdf` was chosen and copied
to `main.pdf`. The resulting main PDF compares equal to both final
builds and to `main_round2.pdf`. The latter had been created before
the pair as a no-change review-stage copy, not labelled a new build.
`main_round0_original.pdf`, `main_round1.pdf`, `main_round2.pdf` and the
reviewed layout-1 baseline all retain that same digest. The genuine
earlier layout-0 PDF remains separately preserved with SHA-256
`95857f7d412d72830ca309733c99519cdb21bb48a53702a3c58ced490989f52d`.

The final text streams from the two new PDFs also compare equal to
each other and to the previously reviewed layout-1 text. The selected
`main.txt` has 1107 lines and SHA-256
`1ba36201727ad9c4db80c492e06e8ef0d099f5bc6df2ee2b52d7f23f59571755`.
It was read completely during this final execution, including both
printed code cores, every receipt row and all references.

## Final diagnostics and retained early-pass messages

Both converged `main.log` files have zero Warning/Error,
undefined-reference/citation, Overfull or Underfull matches. Both
converged `main.blg` files report four entries and no diagnostic
warning/error. The final text has no `??`, `[?]` or `[VERIFY]` marker.

The complete console logs are deliberately **not** described as
warning-free: each fresh first pass has unresolved references/citations
and a 0.57625 pt overfull box at the still-unresolved local-word lemma.
The later normal latexmk passes resolve all of these without a source
change. The early diagnostic appears at line 253 in both console logs;
it is absent from the converged engine logs. It is distinct from the
genuine initial layout-0 10.79245 pt overflow retained in BUILD_HISTORY.
Nothing was suppressed, cleaned away or described as a failed
mathematical run.

Both PDF checks report 22 embedded Type 1 font resources with Unicode
mappings; no unembedded font was found. The selected PDF is not
encrypted, has no JavaScript, uses letter pages of 612 by 792 points,
has visible anonymous authorship, blank Author metadata and no creation/
modification dates. No venue or artificial page limit was assigned.

## Every-page final inspection

New images were generated **from the chosen final build**, not reused
from the old draft, by:

```bash
pdftoppm -png -scale-to 1400 build/final_frozen_02/main.pdf \
  build/final_frozen_02/pages/page
```

Each of the 21 separate images `page-01.png` through `page-21.png`
was actually viewed. The final all-page inspection was complete by
2026-09-09 07:09:51 UTC. The compact page log is:

| Pages actually viewed | Checked content and result |
| --- | --- |
| 1–3 | Abstract, complete theorem and all four family/eleven exception rows; no clipping or missing labels |
| 4–5 | Rational normalization, integrality, upper boundary, height and nonconjugacy witness; displays readable |
| 6–8 | Annulus bounds, six-symbol separation, complete local cases and analytic/finite seam; proof continuations intact |
| 9–11 | Finite completeness, independent reconstruction, all counts/equality proofs, ordinary returns and scope; no collision |
| 12 | Both full imported C412 tables with all index restrictions, recovery formula and appendix transition; legible |
| 13–16 | Both directly included mathematical code cores and explanatory display; complete readable continuation, no clipped lines |
| 17–19 | Checker tail, receipt caption and continued rows from `a=-145` through `a=-14`; headers and continuation markers intact |
| 20 | Receipt tail `a=-13` through control `a=1`, exact `17` row, execution history and source hashes; complete |
| 21 | Four-entry bibliography, source status, DOI/versioned URL text; no missing entry or unresolved marker |

The article occupies pages 1–11, the included appendices pages 12–20
and the bibliography page 21. No final layout defect was found, so
no post-review source repair or additional build was introduced.
The earlier ARS structural-page preflight remains an explicitly
`UNAVAILABLE` advisory in the first review, not a certified structural
PASS. This report's actual text and rendered-page inspections do not
silently upgrade that separate advisory.

## Retained build provenance and boundary

| Actual retained log or recorder | SHA-256 |
| --- | --- |
| `build/final_frozen_01/latexmk.console.log` | `cbc33103df4bca5d5e1c931ae1dfa321f0cc8e63b41ec9473fd8ed8081aaec16` |
| `build/final_frozen_01/main.log` | `87eb699e66eb75ee6ef159c0b172839e87c2339dcf39e55e3819c6be4c70d6c3` |
| `build/final_frozen_01/main.blg` | `1d3998b15260ab86aeea42ce23e3be21a6e7e631975a0543c62163bf5abccff0` |
| `build/final_frozen_01/main.fls` | `dfca49bba48628417ca1f443e2ce795defa4088969cb4da35ef1d4459d82f29a` |
| `build/final_frozen_02/latexmk.console.log` | `3da32865784f54b67fefb322304a4d874fbd880c4214d36ed87a87e84a8b2af5` |
| `build/final_frozen_02/main.log` | `285cb60e0922939eec4d1e4bcbee0f04dcb5115ab57cbff6431bfac508252fec` |
| `build/final_frozen_02/main.blg` | `1d3998b15260ab86aeea42ce23e3be21a6e7e631975a0543c62163bf5abccff0` |
| `build/final_frozen_02/main.fls` | `9bf3ec49fa1338cbc42eb9928ed9175aef925ab1041d774e87949b001908b2af` |

Both final directories additionally retain their actual PDF, metadata,
font report, text, auxiliary/bibliography files and exact input-manifest
copy. Original baseline/failure/diagnostic history is untouched. One
documentation patch initially had a context mismatch and was corrected
before either final build; it changed no manuscript input and was not a
LaTeX attempt or mathematical run.

The paper-compile skill and batch final-build contract governed the two
fresh builds and complete PDF check. The improvement-loop skill governed
honest no-change aliases and coordinator-adjudicated round closure, not
a new external-model call or invented score. Mathematical scripts,
old certificates and the format-only table renderer executed during
this final-build assignment: **zero**.

All writes were confined to this C424 paper directory. No C425 file,
global evaluation, registry, release ledger/manifest, sealed payload or
Git state was touched. This paper-local output is now frozen for the
coordinator; formal evaluation and global sealing remain separate.
