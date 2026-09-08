# C422 first baseline manuscript build

2026-09-08 UTC. Status: `BASELINE_PDF_BUILT; TWO_MANUSCRIPT_REVIEWS_PENDING`.
This is the first complete manuscript, not a final reviewed or sealed
paper. The coordinator authorized it after the global
[outline PASS](../../REVIEW_OUTLINE.md) and
[batch-plan closure](../../BATCH_PLAN.md), both read in full here.

## Actual deliverables

- [Baseline PDF](build_round0_attempt2/main.pdf): **14 pages,
  352,517 bytes**; the main article, including the preparation disclosure,
  ends on page 13, and references occupy page 14. No appendix.
- [Master source](main.tex), [notation](math_commands.tex),
  [verified bibliography](references.bib), nine section files (abstract
  plus eight numbered sections), and five standalone proof tables.
- [Detailed plan](PAPER_PLAN.md) and
  [source/evidence map](SOURCES_AND_EVIDENCE.md).
- [Complete successful command log](build_round0_attempt2/compile.log),
  [final engine log](build_round0_attempt2/main.log), and
  [BibTeX log](build_round0_attempt2/main.blg).
- [Original failed command log](build_round0/compile.log) and
  [original failed engine log](build_round0/main.log), preserved.

The source directory itself has no generated `main.pdf`; the actual
baseline is in the named build directory. No fictitious round-one or
round-two PDF has been created.

## Format and mathematical coverage

English anonymous `article`, 11 pt, US letter, one-inch margins, Latin
Modern text/math fonts. There is no journal template or page limit.
The standalone text contains:

- all seven native branches and all seven inverse-state cases;
- all eight blowups, all boundary classes, all four accessible charts
  and every forward-extension formula;
- the complete integral lattice solution, uniform-pole lemma and four
  face-polynomial endpoint relations;
- the credited source matrix integral, cyclotomic specialization,
  extension across special points and credited nonzero leading term;
- the arbitrary-finite-fibre component argument, Cartier reducedness
  step and arithmetic-genus calculation;
- smooth and singular rational-point bounds and the exact ordinary
  native/phase-return least-period conversion.

No core proof is replaced by a local Markdown link. Characteristics two
and three, singular fibres and zero exceptional-line coordinates remain
in scope. The bin distribution, explicit discriminant, generic
smoothness and external target arithmetic remain unclaimed.

## Commands, environment and exact outcomes

Working directory for all commands below:
`/root/autodl-tmp/hilbert-polya-structure/henon_dynamics/research_c419_c423/papers/C422_painleve_bound`.

Prerequisites were found at `/usr/bin`: `pdflatex`, `latexmk`, `bibtex`,
`pdfinfo`, `pdffonts`, `pdftotext` and `pdftoppm`.
The actual versions reported were pdfTeX 3.141592653-2.6-1.40.22
(TeX Live 2022/dev/Debian), LaTeX2e 2021-11-15 patch level 1,
latexmk 4.76 (20 November 2021), BibTeX 0.99d, and Poppler
`pdfinfo` 22.02.0.
The compiler read `/etc/LatexMk` as shown in the raw command logs.

Both build attempts used the explicitly supplied environment
`SOURCE_DATE_EPOCH=1788825600`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`,
`LC_ALL=C`. These settings are recorded inputs, not a claim that
two independent builds were compared. Final two-fresh-directory
determinism remains a separate later release gate.

First attempt, after creating the previously nonexistent `build_round0`:

```bash
set -o pipefail
env SOURCE_DATE_EPOCH=1788825600 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C \
  latexmk -pdf -outdir=build_round0 -interaction=nonstopmode \
  -halt-on-error main.tex 2>&1 | tee build_round0/compile.log
```

Actual command exit: **12**, with one failed `pdflatex` execution and
no PDF. The unused local `\AA` macro collided with LaTeX's existing
accent command. The unused definition was removed from
`math_commands.tex` using a patch. No mathematical expression changed.
The original logs and other failed-build artifacts remain in place.

Second attempt, in the separately created fresh `build_round0_attempt2`:

```bash
set -o pipefail
env SOURCE_DATE_EPOCH=1788825600 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C \
  latexmk -pdf -outdir=build_round0_attempt2 -interaction=nonstopmode \
  -halt-on-error main.tex 2>&1 | tee build_round0_attempt2/compile.log
```

Actual command exit: **0**. Latexmk automatically executed three
`pdflatex` passes and two `bibtex` passes to resolve the bibliography
and cross-references. These are passes of one baseline build, not three
independent build tests or review versions. The first passes' temporary
undefined citations/references remain visible in `compile.log`; the
final `main.log` has none.

There was no cleanup/delete command, repeated old build, mathematical
census, evaluator invocation, GPU/API computation or Git mutation.

## Text, font and page checks actually performed

`pdfinfo`, `pdffonts`, `pdftotext -layout` and `pdftoppm` all exited 0.
The final PDF metadata lists only “Anonymous Authors”; its size is
612 by 792 points and PDF version 1.5. It is unencrypted and has no
JavaScript or forms. Its raw creation/modification dates are both
`D:20260908000000Z`. The PDF is not tagged for accessibility, which is
reported rather than claimed otherwise.

The full extracted text was read. The first combined tool response
truncated the middle of the extraction, so pages 7–9 and page 6 were then
extracted and read separately, closing that reading gap. A text scan found no
`??`, `[?]`, `TODO`, `FIXME`, `XXX` or `VERIFY` markers.
All four bibliography records are actually cited. The nine section
files are all included by `main.tex`; the five tables are included by
their owning section files. `figures/latex_includes.tex` is an annotated
table index, not an additional unused section or duplicated table input.

Final `main.log` and `main.blg` scans found **zero** warning,
overfull/underfull, undefined-reference, undefined-citation or error
matches. An `rg` exit of 1 for those scans means no matches, not a
failed compilation. All **19** entries reported by `pdffonts` are
embedded, subsetted Type 1 fonts, with Unicode mappings.

All 14 pages were rendered at 100 dpi and **individually visually
inspected** in page order. The inspected files are in
`build_round0_attempt2/pages/`, from `page-01.png` through `page-14.png`.
Tables, matrix entries, superscripts, equation numbers, proof endings,
page numbers and references are visible; there is no clipped or
overlapping content. This is author baseline inspection, not the
future independent final-page release audit.

Nonblocking presentation items for the manuscript reviewers: Theorem 1.1
continues from page 1 to page 2; ordinary prose/long proofs also cross
page boundaries. The bibliography style lowercases parts of the Stacks
and lecture titles. These do not remove content or obstruct the proof;
no mandatory mathematical correction is known at author handoff.

## Baseline identity

PDF SHA256:
`25f78d8224a3582200ceec838c6df6ed15da22fc79bb6917f49fcf05b51f0888`.

Final engine-log SHA256:
`be5bcb9a302a00e41ca5d35052743c7054e3a52badf6f36144c844ea4958a014`.

Successful whole-command-log SHA256:
`4ce202b0343fa78e2c2644a99d781dc3280254e5db6fb983921265f48b64fa00`.

The 17 actual TeX/Bib inputs to this baseline had these SHA256 values:

```text
564840828baae625d4dd4515f100585aadd0bc02e2a849e8776f48de2c1b8c69  main.tex
50c055e943b66980853288ea09641c9cdc5064f703fd317f8bc4622896d3453b  math_commands.tex
553a07c31a4cbb3ad2b1e961f3a4c1f1add8e3eb5be3ab9a8729dc5501c81d58  references.bib
057093c18cec5d3d9f8d826c32b2d011583018ba6b76ac0c840c3ba8bc55cb56  sections/00_abstract.tex
ffbd2de66e56fe7777930ee33150460519d6317f21ad6e6003e30ff5199609ed  sections/01_introduction.tex
4359ee4aa79df33c026d5d91cebe6ca840007eb858ff79eaaf9fe36156a93dc2  sections/02_states.tex
f365eaff5524e20bdab9205e416804d003d92ce19d422bdcfb4d64bf854cf0bc  sections/03_surface.tex
839c71833939ef7e3fa96b520f241637cb4f0591a4953dbbf3c44c7c8e20b34b  sections/04_poles.tex
9dd8a1b45b4233f2092d9176e27dfcd3ee4c5f5969452753782dcea00aff8d13  sections/05_integral.tex
2b9aefb6b9a8137e847b779c14a7add5f413e2e0922c7e136e91808213a558ab  sections/06_fibres.tex
ad550c0b5d1896049a443db49225df880774bfd3e59b79bea3f45b91fb082916  sections/07_periods.tex
a569e88ffec7f53940f3997499f7936bda20fbba9f20306f88dce29699924c49  sections/08_conclusion.tex
b3b73e23dd7e2161d3f86e3f74bf710adb0c157b96247a2254c847794e3c5c00  figures/TABLE_ownership.tex
626d2edbb0fd0ed1f5d9a9dfe1dad0264b3ca9b4e256a6813517e8d011ddb6f0  figures/TABLE_native.tex
f64ad80ddac8bb307c43f2a8ffa733eda642d3c8ade88c807bca2783f63da2a8  figures/TABLE_inverse.tex
2be75f747f16020d502c920de1ac1c7aa3e671033e48bff0f54b052764c48c52  figures/TABLE_blowups.tex
82357e6773f53e9e2ab4d7a3598e6295ba5d110f378ef229a4d92d7908f3cd92  figures/TABLE_faces.tex
```

These identify the baseline input bytes. They are not a mathematical
certificate, signature, formal evaluation or final release manifest.

## Remaining authorized workflow

The coordinator will arrange two actual nonauthor full-manuscript
review/revision rounds. They must read the new complete text and compare
it to the accepted proof; the earlier proof PASS is not reused as a
review of these TeX/PDF files. Required fixes and affected rechecks will
be recorded without inventing changes or improving scores.

Formal Route-A evaluation, independent final build/page verification,
two-directory byte comparison, sealing, global status and Git
integration remain coordinator-owned. No external submission or upload
is implied by this baseline build.

Skill receipt: `paper-writing` retained the planning, exact-table,
drafting, compilation and two-review stages; `paper-figure` produced
the five standalone theorem/branch tables, not fabricated data plots.
`paper-write` and the fully read writing/citation references governed
source attribution and complete modular proofs. `paper-compile` led
to the real build/fix and text/font/page checks. All ML venue/page
defaults and named unavailable external-review examples remain
overridden by the approved mathematical-article/current-team contract.
