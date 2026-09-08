# C422 manuscript revision — round 1

2026-09-08 UTC. Status: `ROUND1_TWO_OPTIONAL_FIXES_IMPLEMENTED;
FRESH_BUILD_SUCCESS; ROUND2_FULL_REVIEW_PENDING`.

This is the C422 author's response and build receipt, not a second
independent review or a new mathematical proof certification. The
coordinator authorized exactly the two optional items in the complete
[round-1 nonauthor review](../../manuscript_reviews/round1/C422_REVIEW.md).
That 268-line review was read in full before editing. Its verdict is PASS
with **0 mandatory fixes**; no numerical score or score improvement is
invented here. Its SHA256 is
`342d7cb4e6e51a6b6ad370372cd3488b6d27ec374d290f4d4293599ac2deb62f`.

## Responses to every requested item

| Review item | Author response | Actual change and verification |
| --- | --- | --- |
| Section 5, optional item 1: keep Theorem 1.1 together | Accepted | Added `needspace` in `main.tex:9` and the single local `\Needspace{14\baselineskip}` before the theorem in `sections/01_introduction.tex:26`. The complete statement, state domain and bound now appear together on PDF page 2. No theorem text was removed or changed. |
| Section 5, optional item 2: identify Stacks 33.39.3 as a Definition | Accepted | At `sections/07_periods.tex:40`, replaced the collective “Lemmas 33.39.2--33.39.4” locator with “Lemma 33.39.2, Definition 33.39.3 and Lemma 33.39.4”. The link and citation key are unchanged. Directly reopened the [Stacks source](https://stacks.math.columbia.edu/tag/0C3Q), which labels the middle item Definition. The expanded citation is correctly rendered on PDF page 13. |

No other manuscript change was authorized or made. The only three changed
TeX/Bib files are `main.tex`, `sections/01_introduction.tex` and
`sections/07_periods.tex`; the first two implement one local layout fix.
All 14 other actual TeX/Bib inputs remain byte-identical to the baseline.
The source-index file `figures/latex_includes.tex` also remains unchanged.

The two main theorems, seven native branches, zero exceptional-line
coordinates, arbitrary nonzero phases, characteristics two and three,
all-finite-fibre proof, ordinary least-period clock and target-arithmetic
limitations are unchanged. No new experiment, enumeration, discriminant,
source integral or mathematical computation was added or rerun.

## Preservation before editing

Before the patch, all 17 live build inputs were checked against the
baseline hashes in `BUILD_REPORT.md`; all returned OK. The PDF hash was
also verified before copying.

- [Original source snapshot](source_snapshot_round0/main.tex): contains
  all 18 TeX/Bib files in their relative layout, including the annotated
  table index that is not a compiler input. The snapshot was made before
  either approved edit.
- [Original PDF copy](main_round0_original.pdf): an exact copy of the
  already preserved [baseline build PDF](build_round0_attempt2/main.pdf).
- [Baseline input manifest](source_snapshot_round0/source_inputs.sha256):
  records the 17 actual compiler inputs. Its checks pass when run from
  `source_snapshot_round0/`, and its SHA256 is
  `cff20c04eb813e61e8606e537c7da8770f7061b3c2792902829c79b9e9f75908`.
- The failed `build_round0/` and successful `build_round0_attempt2/`
  directories, raw logs and historical `BUILD_REPORT.md` were not cleaned,
  overwritten or relabeled as revised builds.

Both copies of the baseline PDF still have SHA256
`25f78d8224a3582200ceec838c6df6ed15da22fc79bb6917f49fcf05b51f0888`.

## Actual fresh build

After confirming `build_round1/` did not exist, it was created. From the
C422 paper directory the actual invocation was:

```bash
set -o pipefail
env SOURCE_DATE_EPOCH=1788825600 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C \
  latexmk -pdf -outdir=build_round1 -interaction=nonstopmode \
  -halt-on-error main.tex 2>&1 | tee build_round1/compile.log
```

Actual command exit: **0**. One fresh build used three pdfLaTeX passes
and two BibTeX passes, as recorded by the full command log. Intermediate
undefined citations before convergence are retained in that log; the
final engine/BibTeX logs have no warnings or unresolved citations. Those
normal convergence passes are not multiple reviews or reproducibility
builds. No cleanup command or old build rerun was used.

The environment remains pdfTeX 1.40.22, TeX Live 2022/dev/Debian,
LaTeX2e 2021-11-15 patch 1, latexmk 4.76 and BibTeX 0.99d, with
`/etc/LatexMk` read as shown by the actual log. The added package was
already installed: `needspace` v1.3d dated 2010-09-12, at
`/usr/share/texlive/texmf-dist/tex/latex/needspace/needspace.sty`, SHA256
`5ae673ce2a80fb868c954373252294d9e6469feeb78b445182772fd043eb0914`.
No package installation or toolchain update occurred.

## Revised artifacts and identity

- [Round-1 PDF](build_round1/main.pdf): **14 pages, 352364 bytes**,
  SHA256 `ecdb73cf225c34164a9f27d4ef2b56dc67485fb805307dfc56cd48e6420ffdae`.
- [Complete build output](build_round1/compile.log): SHA256
  `83f4017d0b2117635333b312516c37f5d0ea783c1ad1b0169b289d1c36c5daa8`.
- [Final engine log](build_round1/main.log): SHA256
  `a8489f922165017adf91a89629c0911e0339d9375bfcfcb60b96d58b9af6e6d0`.
- [Revised source snapshot](build_round1/source_snapshot/main.tex): all
  18 TeX/Bib files, preserved separately from the original snapshot.
- [Revised 17-input manifest](build_round1/source_snapshot/source_inputs.sha256):
  SHA256 `19a5a9e3dca4adce3731c181d4429833f8cf3fbef549f1127ad32d2fc406dc7f`.
  All 17 inputs pass both against the snapshot and against the live paper
  files. Paths in this manifest are relative to the source root.
- [Extracted PDF text](build_round1/main.txt) and 14 individually
  inspected PNG pages in `build_round1/pages/` are retained.

The three changed input hashes are:

```text
d212289fdb5ff08ca28c50b7e87f8d419f6caf702c5d986c4326b32535fa679b  main.tex
9f3090629e4ddc9ef19e02682a656327d91b657ee04980301d245d250115e6b2  sections/01_introduction.tex
258a8a23fa6972d04ea30ee5bcc3d73dc79f344de0bd205d572b657c53e52d15  sections/07_periods.tex
```

## Checks performed after the build

The two changed section files and preamble patch were reread and their
three exact diffs inspected. The remaining input hashes were compared
to the untouched original snapshot. `pdfinfo`, `pdffonts`,
`pdftotext -layout` and `pdftoppm -png -r 100` completed successfully.

The final `main.log` and `main.blg` contain zero matches for `Warning`,
`Overfull`, `Underfull`, `undefined` or `Error`. The extracted PDF has
no `??`, `[?]`, `TODO`, `FIXME`, `XXX` or `VERIFY` markers. All 19 font
rows are embedded/subsetted Type 1 fonts with Unicode mappings. The PDF
is unencrypted US letter, PDF 1.5, with no JavaScript or form; it is not
tagged for accessibility. Metadata retains Anonymous Authors.

All 14 revised page images were actually opened, in groups 01–07 and
08–14. Page 1 ends before the theorem, and page 2 contains all of
Theorem 1.1, including both displayed equations. The extra white space
at the end of page 1 is the intended local break. The revised Stacks
locator on page 13 is legible and within the margin. Tables, matrix
entries, proof endings and the full bibliography remain present without
clipping or overlap. Section 8 now continues onto page 14 before the
bibliography; the total remains 14 pages, with no hard page limit or
appendix. This is author visual verification, not round-2 review.

One read-only manifest-hash command initially used paper-relative paths
while its working directory was the revised snapshot. That lookup
reported missing paths, changed no file, and was rerun from the correct
paper directory; both original and revised manifest checks then passed.

## Remaining gates and integrity boundary

The coordinator must still arrange an actual second independent
full-manuscript review of the revised text and PDF. The existence of this
revision and its successful compilation does not meet that requirement.
Any later accepted correction must receive its own truthful response
and artifact identity. Final same-input two-directory comparison,
source freeze, release/page audit, Route-A evaluation and batch/Git
integration remain coordinator-owned and are not asserted complete.

`auto-paper-improvement-loop` governed preservation of real source/PDF
versions and the itemized response; `paper-compile` governed the actual
fresh build and log/text/font/page checks. Their example external-model,
ML-venue, invented-score, synthetic-experiment and cleanup steps were
not used under this narrower approved mathematical-article task. No
shared registry/release record, historical proof file or Git state was
modified, and no external manuscript upload or paid reviewer was used.
