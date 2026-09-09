# C425 final manuscript build and inspection report

2026-09-09 UTC. **FINAL_BUILD_GATE_PASS; AUTHOR STOP-WRITE;
PENDING_COORDINATOR_SEAL.** This is the author-side final build receipt,
not a formal Route-A evaluation, a release seal, an additional manuscript
review or a claim of human peer review.

## Reviewed version and adjudication

The coordinator adopted both actual assigned nonauthor manuscript
reports. Round 1 requested one minor P1 correction: the abstract must
state containment in a finite union of whole periodic lines, rather than
identify a finite orbit with a whole line. Only that two-line abstract
substitution was implemented. Round 2 explicitly closes P1 and reports
zero mathematical/source must-fixes, zero new minor findings and zero
further requested manuscript changes. Its PASS was explicitly adopted
by the coordinator before these final builds.

The complete raw records, freshly read for this closure, are preserved:

| Review | Lines | SHA-256 |
| --- | ---: | --- |
| [ROUND1_REVIEW_RAW.md](ROUND1_REVIEW_RAW.md) | 230 | `e7e8a2cf840d37d52dc1dad9120342d60e711684a627e64dad6f8a61e5adb81e` |
| [ROUND2_REVIEW_RAW.md](ROUND2_REVIEW_RAW.md) | 203 | `c5f8224db870115d6e11e0ebbaba341c176c09717510f70b7349eeb583d8d202` |

Both local raw files were actually byte-compared with their assigned
reports under `../../manuscript_reviews/`. No third review, numerical
score or external-model thread is invented. Round 2 is a **no-change
round**: `main_round2.pdf` is a labelled byte-identical copy of
`main_round1.pdf`, not a purported new revised build. The separately
authorized final pair below consists of two real builds.

## Exactly two fresh final builds

A read-only startup check found no `build_final_*` directory, final
report, README or round-2 alias and no live C425 build process. The
earlier final-build authorization had not been executed. The following
two commands were then run once each from this manuscript directory:

| Actual command | Exit | Final output |
| --- | ---: | --- |
| `bash build.sh build_final_01` | 0 | 12 pages, 378223 bytes |
| `bash build.sh build_final_02` | 0 | 12 pages, 378223 bytes |

The unchanged `build.sh` refuses pre-existing or nested build-directory
names. Both output directories were new. No old directory was cleaned,
overwritten or reused; no third final build was attempted. Each saved
784-line `compile.log` records three pdfLaTeX passes and two BibTeX
passes, ending in latexmk's completed-target message. These internal
passes are not separate final builds, reviews or mathematical runs.
The first passes' unresolved-reference warnings and intermediate
11-page output remain in the complete logs; the final output and final
engine log, not those transient passes, determine the result.

The previously recorded initial history remains untouched: one failed
and three successful changed-input initial builds, followed by one
successful P1 revision build. Nothing was relabelled as this final pair.

## Identical inputs and PDF bytes

[FINAL_INPUT_MANIFEST.sha256](FINAL_INPUT_MANIFEST.sha256) records all
13 reproducibility inputs: `main.tex`, `math_commands.tex`,
`references.bib`, `build.sh` and all nine active section files. Its
SHA-256 is
`c9e8e11efeca9502f0b610847910736f613aa283f77f3f81a01d05c443b2b878`.
It is byte-identical to the first-revision manifest and to the manifest
copy in each final build directory.

All 13 current inputs passed `sha256sum -c` before the first build,
between builds and after the second build. Each final directory retains
the exact 13 inputs in `source_snapshot/`; each snapshot passed the same
manifest. Individual `cmp` checks confirmed equality between both
snapshots, the active inputs and the revised build's snapshot. All
12 inputs other than the already-adopted abstract substitution also
remain byte-identical to `baseline_source/`. No TeX, bibliography,
build-script, theorem or mathematical-program input changed in this
finalization. The existing `ROUND1_SOURCE_DIFF.patch` remains the
complete baseline-to-final source content diff.

The following PDFs are actually byte-identical by `cmp`:

- [main.pdf](main.pdf), [main_round1.pdf](main_round1.pdf) and
  [main_round2.pdf](main_round2.pdf);
- `build_round1_01/main.pdf`;
- [build_final_01/main.pdf](build_final_01/main.pdf) and
  [build_final_02/main.pdf](build_final_02/main.pdf).

Their common SHA-256 is
`e7330f65920c40c566b01ee0d864d9f5a023c70010954e8af633c325f92c1dcb`.
Thus the active final PDF is exactly the reviewed version and exactly
the newly rebuilt final output; an unnecessary overwrite was avoided.
The original `baseline.pdf`, `main_round0_original.pdf` and
`build_initial_04/main.pdf` retain their original identity:
`aa6c4ee4bbc6f55bcf2934caccc927bf36aef872bf230466541c0f3de7b2f207`.

## Deterministic environment and build records

Both final invocations used the existing settings:

```text
SOURCE_DATE_EPOCH=1788912000
FORCE_SOURCE_DATE=1
TZ=UTC
LC_ALL=C
```

`main.tex` continues to set `\pdfinfoomitdate=1`, `\pdftrailerid{}` and
`\pdfsuppressptexinfo=15`. The actual tools are pdfTeX
3.141592653-2.6-1.40.22 (TeX Live 2022/dev/Debian), LaTeX2e
2021-11-15 patch level 1, latexmk 4.76, BibTeX 0.99d and Poppler
22.02.0. latexmk read `/etc/LatexMk`. Both builds retain `compile.log`,
`main.log`, `main.blg`, `main.bbl`, `main.aux`, `main.out`,
`main.fls` and `main.fdb_latexmk`, including actual system dependencies.

| Saved record | SHA-256 |
| --- | --- |
| `build_final_01/compile.log` | `6261449c7c934c3e1371e25e30392e2fe6ecd5d9d87da28b974143194da5b6a7` |
| `build_final_02/compile.log` | `57d38a93c3abc0325ece45744db7248201ee517fa05360fbd91e145897897cab` |
| `build_final_01/main.log` | `f0d7da4122281abfbe204542123f5301fbac7503cdd69af9761594ec9b1a1a2a` |
| `build_final_02/main.log` | `8a5bfe71f6d04f57da83eb6960d1591d8d1ae432520f09765a277c4c59e10de6` |
| Either final `main.blg` | `181ab0f7c0ec15c33ff2c5c62a204b9c17ee617ebb1df05766bbd5280c7cd98f` |

Different log hashes reflect the distinct output paths; the PDF equality
is the actual deterministic-output test. Hash equality establishes byte
identity, not mathematical correctness or software portability.

## Complete final quality checks

Both final PDFs were inspected with `pdfinfo` and `pdffonts`; the raw
outputs are saved in each final directory as `pdfinfo.txt` and
`pdffonts.txt` and match between directories. The PDF is version 1.5,
US letter, unencrypted, with no JavaScript. The author field is
`Anonymous`; creation/modification metadata dates are absent. The
visible manuscript date is correctly retained as 9 September 2026.
All 23 Type 1 font resources are embedded and subset, with Unicode maps.

Each final `main.log` and `main.blg` has zero remaining warning/error,
undefined-reference/citation, overfull/underfull-box, missing-character,
emergency-stop or fatal-error matches. All nine section files are
included from `main.tex`; no active section is orphaned. The actual
final auxiliary file resolves all nine citation commands to exactly
six bibliography keys. No `??`, `[?]`, `[VERIFY]`, TODO, FIXME or XXX
marker was found in the final extracted text or active manuscript.

`pdftotext -layout` was run on both newly built PDFs. Both 614-line
text files match each other and the reviewed revision text by actual
`cmp`; their common SHA-256 is
`5241eab7a02aeb54ab8351f7c30284c7fcff93aa6085fd6e5e6ccd6fa3041d85`.
All 614 lines of `build_final_02/pdf_text.txt` were freshly read, not
merely hash-checked or replaced by the reviewer's earlier read.

The actual final second PDF was freshly rendered with:

```text
pdftoppm -png -scale-to 1400 build_final_02/main.pdf build_final_02/pdf_pages/page
```

Every one of `page-01.png` through `page-12.png` was separately viewed:

| Final pages | Visual coverage and result |
| --- | --- |
| 1–3 | Revised abstract, full main theorem, source-ownership prose, Table 1 and native clock; readable, no observed clipping or overlap |
| 4–6 | Maximum proof, Table 2, exact edge identities and all height-forcing cases; readable displays and complete proof continuations |
| 7–9 | Table 3, backward line exhaustion, finite core, exact period labels and start of the output procedure; no observed collision or missing glyph |
| 10–12 | Remaining procedure, level-count and zeta formulas, scope/evidence statement and all six references; all five public DOIs visibly rendered, local C421 status explicit |

This is an actual 12-of-12 final-page inspection. The first final PDF
was not rendered a second time because its bytes are identical. Pages
1–11 contain the complete article, and page 12 contains references;
there is no proof appendix missing from the PDF. No target venue or
page limit was assigned, so venue-compliance certification is not claimed.

## Final author boundary

The `auto-paper-improvement-loop` skill guided preservation of both raw
reviews and honest no-change round-2 closure; the batch's current-team
review authority superseded external-model/ML-venue defaults. The
`paper-compile` and `henon-route-a-batch` skills guided the two fresh
builds, identical-input comparison, final logs/fonts/text checks and
actual every-page visual inspection. No source fix was required here.

One initial documentation patch was rejected atomically for targeting
the state file twice in one patch; it caused no source change or build
attempt and was corrected before either final build. No failed build
or mathematical execution is hidden by that bookkeeping correction.

Only this C425 manuscript directory was written. Mathematical programs,
finite-core enumeration, old-certificate reruns, TeX changes, new source
retrievals, other-paper writes, evaluation writes, external uploads and
Git mutations during this finalization: **zero**. C424 was not reopened.
The historical `BUILD_REPORT.md`, `DRAFT_HANDOFF.md` and
`ROUND1_HANDOFF.md` remain unchanged snapshots of their earlier stages;
their pending-gate wording does not override this current final receipt.

The author has completed the delegated final-build gate and now stops
writing. Coordinator-owned formal-evaluation disposition, shared batch
checks, release sealing and synchronization are not certified by this
report. Current handoff state: **pending coordinator seal**.
