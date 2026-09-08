# C420 final build, reproducibility and local publication report

2026-09-08 UTC. Status: **PASS for the authorized local final-build gate.**
Two fresh same-input builds completed, their PDF/BibTeX/text outputs
compare byte-for-byte equal, every page of both final PDFs was actually
viewed, and the selected final PDF is now published locally as
[main.pdf](main.pdf) in this C420 directory, above `paper/`.

This report does not claim human peer review, editorial acceptance,
worldwide priority, external publication, formal evaluation, or completed
whole-batch release checks. Those boundaries remain unchanged.

## Authority, review binding and preserved history

The coordinator fully read the complete 366-line
[second manuscript review](../../manuscript_reviews/round2/C420_REVIEW.md),
accepted its PASS and the disposition of all three optional round-1
items, and explicitly authorized this final-build task. That review has
SHA256 `3c2c1923fa910f55c1a0ea2a345be37a5918d732a38494631ab1969257f3902b`.
The complete 307-line
[first manuscript review](../../manuscript_reviews/round1/C420_REVIEW.md)
has SHA256
`9341ffdac67227001e4615f4019404a00b996650bdf722a651d578e2078844a4`.
The actual two presentation edits and accepted optional non-edit are
recorded in [REVISION_ROUND1.md](REVISION_ROUND1.md); that record was not
changed by this task.

No production TeX/BibTeX input changed after the second review. The final
PDF is byte-identical to the reviewed `builds/round1/main.pdf`, so the
final artifact retains the exact reviewed mathematical and presentation
content. No new mathematical claim or extra review round is inferred
from compiling the same inputs again.

Before execution, the proposed `builds/final1/`, `builds/final2/`, root
`main.pdf`, this report and `README_before_final.md` were confirmed absent.
The old README was copied unchanged to
[README_before_final.md](README_before_final.md) before its current-entry
update. Existing `baseline`, `baseline_polished`, and `round1` directories,
their snapshots, logs, PDFs and receipts remain untouched. No cleanup or
deletion command was run.

Historical PDF SHA256 values checked again during this task:

| Preserved build | PDF SHA256 |
| --- | --- |
| `baseline` | `02155b14e6496bd9d9f64876ea2295d5e380cda9a5e0fc8f464d8ae8c8c391c6` |
| `baseline_polished` | `08967fffb8542a60bdedc4142f2efd7149d26fb9057276bb6ab27fbcce5f10ff` |
| `round1` | `9753a3262ce775b5c289a0870bf4694066cb778c1cd10ada267d4ac5f5e74512` |

The initial two builds had different inputs; their original report is
[COMPILE_REPORT.md](COMPILE_REPORT.md). They are not counted as the
same-input pair reported here or as the two full-manuscript reviews.

## Actual script execution and environment

I read all 53 lines of the existing [build.sh](build.sh) before using it.
`bash -n build.sh` exited 0. All required local commands were available:
`pdflatex`, `latexmk`, `bibtex`, `pdfinfo`, `pdffonts`, `pdftotext`, and
`pdftoppm`. No installation or script repair was necessary.

The script was not modified. Its SHA256, unchanged before and after the
builds, is
`db1d4898ede3309006afedb255cac956eabe254f870c246ea494bba50b9984ac`.
It rejects an existing build directory, makes a complete source snapshot,
records the environment and sorted input hashes, and invokes latexmk with
a fresh build-specific output directory. It compiles the live `paper/`
inputs after snapshotting them; it does not claim a separate container or
hermetic source-working-directory build. Pre/post hashes and snapshot
comparisons verify that those shared inputs remained unchanged.

The two commands actually invoked from the C420 directory were:

```sh
bash build.sh final1
bash build.sh final2
```

The underlying compiler invocation in each script run was:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error \
  -outdir=THE_FRESH_BUILD_DIRECTORY main.tex
```

`THE_FRESH_BUILD_DIRECTORY` above denotes the actual absolute C420
`builds/final1` or `builds/final2` path recorded verbatim in that run's
`compile.stdout.log`; it is explanatory notation, not an executed
literal argument.

| Actual build | Start time, UTC | Script/latexmk exit | Automatic passes | Final PDF |
| --- | --- | --- | --- | --- |
| `final1` | 2026-09-08 10:57:24 | 0 / 0 | 3 pdfLaTeX, 2 BibTeX | 18 pages, 428401 bytes |
| `final2` | 2026-09-08 10:57:35 | 0 / 0 | 3 pdfLaTeX, 2 BibTeX | 18 pages, 428401 bytes |

These are two actual latexmk invocations, each using normal automatic
convergence. There were no failed final-build attempts, source fixes,
manual extra compiler passes, or mathematical-program executions. Initial
passes naturally contain unresolved references/citations before BibTeX
and subsequent LaTeX passes; the raw output is retained without deleting
those transient diagnostics. The clean final logs, not an early pass,
determine the final diagnostic status below.

Both executions set:

```text
SOURCE_DATE_EPOCH=1788825600
FORCE_SOURCE_DATE=1
TZ=UTC
LC_ALL=C
```

The existing master source suppresses volatile PDF dates and trailer IDs.
Recorded tools: pdfTeX 1.40.22 (TeX Live 2022/dev/Debian), latexmk 4.76,
BibTeX 0.99d and Poppler 22.02.0, on Linux 5.15.0-78-generic x86_64.
The complete actual version output is retained in each `environment.txt`.
Reproducibility is established for these same inputs and this recorded
environment; no untested cross-platform guarantee is asserted.

## Source freeze and bytewise comparison

`sha256sum -c builds/round1/source_inputs.sha256` passed all 13 production
inputs before building. Afterward, checks against both final manifests
again passed all 13 inputs. Both final manifests are byte-identical to
the round-1 manifest. Recursive comparisons of each complete final
`source_snapshot/` against `paper/` reported no difference.

The actual `cmp` results were exit 0, no differing bytes, for:

```text
final1/main.pdf             versus final2/main.pdf
final1/main.bbl             versus final2/main.bbl
final1/main.txt             versus final2/main.txt
round1/main.pdf             versus final2/main.pdf
round1/source_inputs.sha256 versus final1/source_inputs.sha256
round1/source_inputs.sha256 versus final2/source_inputs.sha256
```

Here the displayed prefixes abbreviate paths under `builds/`. Both final
font reports also compare equal. A recursive comparison of the two
retained `pages/` directories found no difference in their 18 PNG pairs.
This image comparison supplements, rather than substitutes for, the
actual visual checks below.

| Common final artifact | Size | SHA256 in both final builds |
| --- | --- | --- |
| `main.pdf` | 428401 bytes | `9753a3262ce775b5c289a0870bf4694066cb778c1cd10ada267d4ac5f5e74512` |
| `main.bbl` | 2765 bytes, 64 lines | `b051c16b924d75248cad756ae868cadf6146aaf2d83cd83ab0c44878fd904456` |
| `main.txt` | 59893 bytes, 946 lines | `e828bec18c2013d5c2caa4a17fcde6afeb997bf94d88a7b52dbf8ce8c2f28da1` |
| `source_inputs.sha256` | 13 entries | `ba887f152fc9fe7ca9e69cf74f14a96332bcf04c998f6352786358a65acc147e` |
| `pdffonts.txt` | 27 font rows plus header | `b8e80a4d5cad2e66eb8dc76fdcda8abbd1d94d1e3c006cef1c4b66983e5a13ad` |
| `pdfinfo.txt` | 20 lines | `b2271bb1b6c7cab9dde10d970775e212e5d85832e57a71351eb8ad95c9350436` |
| `main.blg` | final BibTeX log | `afe9cfc935b5bf838c0e354b33aa5de9f0181595e15536fdc65374dfe9dbbe95` |

Complete frozen production-input hashes, copied from the checked manifest:

```text
cc99419382dc6b01564e34a762b18c99de335dc918d648a551f9f451e25a4ae5  paper/figures/latex_includes.tex
44f5150ce545c5a6b801e848c9f85393eb6f5122608c6d74206bdb8d0415050f  paper/main.tex
aaf9277f10a7f753f81991174a0ba2acef0c1b4dcf11f1f54510e179730d22ba  paper/math_commands.tex
eae77180188be6aeb269ae814d7e8883b52f83af48fd9bafbf8bad7c493a4bf8  paper/references.bib
cc9b6665b380f65a6de599f6530ec1872113522a97ff55e3deebe2cdddc4cf6f  paper/sections/0_abstract.tex
19d45eeb780e536a41587ab39b366b97f8d575e28529d9b41552a351d662d839  paper/sections/1_introduction.tex
fa79e899ddd96e15bc4de515b5d8f7964b82449335db04bf2988ddeecb740d6e  paper/sections/2_fixed_cusp_blocks.tex
952dc431f8455a0d9e104ffd6566107bc4f6ed703fc448f98e95d5d6eec3dea2  paper/sections/3_principal_basis.tex
886ecebe518ad28f66e12a14e852d1fe0a25b75ee982eb0bb8403d80a854db99  paper/sections/4_nonreal_square.tex
3e0a323b80a17cc7fa54b9a819f863907e1df80fc335d5a645d2550dbbe534cb  paper/sections/5_phase_parity.tex
e8e4d0a5c68ce09102ed4004a7914e57c141a0f218fd12bbb3b3c15b44126a50  paper/sections/6_arithmetic.tex
33d913a4377193b23dc242f6e7ed26d7ba279ef5495f08c4e43b1b64bd72a73f  paper/sections/7_boundary_levels.tex
86dcfa03cc35503071d3a1aab238bfdf3f47e10c7843084ae770d653c94f1286  paper/sections/8_scope.tex
```

## Final diagnostics and actual page inspection

Both final compiler and BibTeX logs were scanned with the targeted pattern
below; no match was found (the normal `rg` no-match exit is 1):

```text
(^!|LaTeX Warning|Package .* Warning|Class .* Warning|Overfull|Underfull|undefined|There were.*warning|Warning--)
```

Thus each completed build has zero actual errors, final warnings,
undefined references/citations, overfull boxes and underfull boxes. This
does not erase the transient first-pass diagnostics in `compile.stdout.log`.
Generic package descriptions containing the words warning/error and
BibTeX's function counter `warning$ -- 0` are not actual warnings.

Literal searches of the production sources and both final extracted
texts found none of: `TODO`, `FIXME`, `TBD`, `PLACEHOLDER`, `??`, `[?]`,
`[VERIFY]`, or the stale first-baseline disclosure. The final auxiliary
citation/bibcite records and complete final `.bbl` were inspected: all
seven bibliography keys are cited and resolved. No bibliography entry
was removed, and no fresh external metadata or source-access claim is
made by this compilation task. The actual recorder includes all nine
section inputs, the math commands and the table macros; no section is
orphaned from the master manuscript.

Both PDFs are unencrypted US-letter PDF 1.5 files with 18 pages, no
JavaScript, and Anonymous Authors metadata. The main text ends on page
17, where the bibliography begins; the bibliography finishes on page 18.
No venue page quota was provided. Retaining the short final Young-entry
page is the explicitly accepted optional round-1 disposition, not an
unresolved defect or an invented page-limit exception.

The complete `pdffonts.txt` from each build was inspected. All 27 rows
report embedded, subset, Unicode-mapped Type 1 fonts; there are no Type 3
or nonembedded fonts.

Both PDFs were independently rendered with `pdftoppm -png -r 100` into
their respective [final1 pages](builds/final1/pages/) and
[final2 pages](builds/final2/pages/) directories. Both rendering commands
exited 0. **Every one of the 36 page images was actually opened:** pages
01–06, 07–12 and 13–18 of final1, then the same three batches of final2.
This is not merely inference from byte equality or a compiler exit.

| Pages, in each final PDF | Actually inspected | Result |
| --- | --- | --- |
| 1–2 | Title, abstract, complete first theorem, character criterion and ownership table | Readable and correctly placed; no overlap |
| 3–5 | Width-one cusp convention, full Fourier transform, local factors, functional equation and paired blocks | Bars, indices and matrix entries legible; no clipping |
| 6–8 | Complete principal-basis formulas and both central parity cases, cusp normalization | Finite sums and aligned equations within margins |
| 9–10 | Imprimitive scalar factors and determinant/outside-prime obstruction | Products, quotients and conjugations legible |
| 11–14 | Tensor lemma, fixed phase identity, odd central obstruction, complete converse and level-exponent table | No overflow or missing proof continuation |
| 15–16 | Arithmetic converse, capitalized Table 4 reference, exact levels 50 and 100 | Boundary table and explicit commutator legible |
| 17–18 | Stage-neutral disclosure and all seven bibliography entries | No unresolved citation or clipped text; accepted sparse final page retained |

No visual or diagnostic repair was needed, and no production source was
changed after any inspection.

## Retained execution receipts and their hashes

Each final directory contains the actual full `compile.stdout.log`,
`main.log`, `main.blg`, `latexmk_exit_code.txt`, `environment.txt`, normal
LaTeX auxiliaries/recorder, full source snapshot/manifest, PDF, extracted
text, PDF metadata/font reports, PDF checksum record and 18 page renders.
The full raw compiler output remains in those files even where a tool's
display was shortened. The final logs and relevant run-count markers
were inspected separately; shortened display is not described as a full
verbatim read of every raw console line.

| Receipt | SHA256 |
| --- | --- |
| `builds/final1/compile.stdout.log` | `f20f906840cc8c338a4f4746278e428cf52153c8820c48ff03d69578ece824f6` |
| `builds/final1/main.log` | `4f8f399f35fca7c3728116920bbabe0e3572aeaba15860e4da648307230fec1a` |
| `builds/final1/environment.txt` | `f9f997cbaea605365e951f3842c7fc3e11a0200e1608957c66a99aa83efdaaa9` |
| `builds/final2/compile.stdout.log` | `c2b62c4dc408f5a74b5a5e9dd0eeba308da81eb03557a58b8daec6867816b829` |
| `builds/final2/main.log` | `fef0c787a5205d370cb195d7b0a05aaeef405ce9b8eacfb94af460127752bff0` |
| `builds/final2/environment.txt` | `ab597334b6c5f6c0a14b092962dd0a9453d11b298342a548d9fe83b4d0ae40a8` |

The raw console/compiler and environment files contain truthful
directory names, execution details and start times; their different
hashes are expected. The PDF, bibliography and text comparisons above
are actual bytewise equality tests, not normalization of differing PDFs.

## Local publication and handoff

After the build-pair and all-page checks, the actual command
`cp -p -- builds/final2/main.pdf main.pdf` created the C420-root entry.
Its target was checked absent immediately before copying. `cmp main.pdf
builds/final2/main.pdf` exited 0, and fresh `pdfinfo` confirmed 18 pages
and 428401 bytes. The published PDF SHA256 is
`9753a3262ce775b5c289a0870bf4694066cb778c1cd10ada267d4ac5f5e74512`.
No old PDF was overwritten.

The updated [README.md](README.md) points to this final PDF and the actual
review/build records. README SHA256:
`9f0918d36c453cb8e1b5bd1b92d5ab494c9e75cf8b59ca41fea2ac3364cbb4ac`.
The unchanged pre-final README SHA256 is
`a9cc9420d34e91c4b4c9adff569778033cbd22062b4c044e41196e783ab86e65`.
The hash of this report is supplied separately in the handoff, avoiding
a self-referential hash field.

The production-input freeze is the 13-entry manifest above, not a claim
that file permissions prevent future edits. Any later input change
requires renewed substantive/build checks as appropriate. No further
write to this C420 directory is planned after the verified handoff.

This task did not edit any shared registry, evaluator record, other
paper, historical proof or Git state; it did not run old mathematical
programs, external source requests, paid models, external publication
or notifications. Only the authorized C420-local final build artifacts,
local PDF entry, preserved README copy, updated README and this report
were created or changed. Whole-batch release and formal evaluation remain
with the coordinator.
