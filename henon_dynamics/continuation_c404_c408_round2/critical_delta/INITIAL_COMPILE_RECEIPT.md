# C406 initial manuscript compilation receipt

Status: `INITIAL_COMPILE_SUCCESS_PENDING_NONAUTHOR_MANUSCRIPT_REVIEW`.
Date: 2026-09-06. This records one actual initial build, not the later
two-fresh-build reproducibility test or final all-page visual QA.

## Actual output

- Article: **The critical second Weyl coefficient of a harmonic delta chain**.
- Main PDF: `paper/main.pdf`; immutable initial-build copy:
  `paper/initial_build/main.pdf`.
- PDF SHA-256: `43f04734234a9e21e41ad0eaff5e199c642935228475c4207e7a4cee14bec1a9`.
- Size: **403,808 bytes**. Total: **13 A4 pages**.
- Mathematical body and disclosure: pages 1–12. References: page 13.
- Anonymous author block; no imposed ML venue or page quota.
- All 24 font records are embedded, subsetted Type 1 fonts, with Unicode
  mappings. No Type 3 font is reported.
- No PDF CreationDate or ModDate field is present in `pdfinfo` output.

## Executed build

Working directory:

    /root/autodl-tmp/hilbert-polya-structure/henon_dynamics/continuation_c404_c408_round2/critical_delta/paper

Executed command:

    bash build_initial.sh 01

The script exports exactly

    SOURCE_DATE_EPOCH=1788652800
    FORCE_SOURCE_DATE=1
    TZ=UTC
    LC_ALL=C

and invokes

    latexmk -pdf -recorder -interaction=nonstopmode -halt-on-error \
      -file-line-error -outdir=initial_build main.tex

The TeX preamble sets `pdfinfoomitdate=1`, empty `pdftrailerid`, and
`pdfsuppressptexinfo=15`. The source epoch is 2026-09-06 00:00:00 UTC.
These controls configure the initial build; byte equality across two
fresh independent output directories has **not** yet been tested.

Actual tools reported by the build:

- latexmk 4.76, dated 20 November 2021;
- pdfTeX 3.141592653-2.6-1.40.22, TeX Live 2022/dev/Debian;
- LaTeX2e 2021-11-15, patch level 1;
- BibTeX 0.99d.

One build job completed successfully with exit code 0. Latexmk performed
three pdfLaTeX passes and two BibTeX passes to settle references.
No source edit or failed build attempt was needed after this initial
compile started. The full multi-pass stdout is retained in
`paper/initial_build/compile_attempt_01.stdout.log`.

## Final-pass diagnostics and inspection

The final `main.log` and `main.blg` contain:

- LaTeX/BibTeX warnings: **0**;
- unresolved references or citations: **0**;
- overfull or underfull boxes: **0**;
- multiply defined labels or TeX errors: **0**.

The earlier passes contain expected temporary undefined citations and
references; they are retained in the stdout log and are not mislabeled
as final-pass defects. The final PDF text contains no `??`, `[?]`,
TODO/FIXME/XXX, or unresolved verification marker. All eight section
files are included by `main.tex`; there are no orphaned TeX sections.
Exactly four bibliography keys are cited and resolved in `main.aux`.

The first and last PDF pages were rendered and visually inspected at
100 dpi. Title/abstract, anonymity, and the four references render
legibly with no clipping in those previews. This is a limited initial
sanity check, **not** all-page visual clearance. Root coordinates
the later all-page QA of the final reviewed PDF.

## Source and artifact freeze

`paper/SOURCE_INPUTS.sha256` binds the master file, macros, bibliography,
all eight sections, build script, and citation audit.
`paper/INITIAL_ARTIFACTS.sha256` binds both initial PDF copies and the
actual final log, BibTeX outputs, recorder, auxiliary files, stdout,
PDF metadata, font listing, and extracted text.

Reviewed upstream files remain unchanged:

- `PROOF_PACKAGE.md`:
  `5ae8f666d9fe091ce40ff4317aa7acc6a0f6c3735049d016bfdfff5192feb3ca`;
- `SOURCE_AUDIT.md`:
  `2b87777ac7ae2a2ed57d156710b60ea82d5e631f953adc9491e07f37082daecd`;
- `PAPER_PLAN.md`:
  `a9a6391e23b05b76368b7699b4c5caa2027521cbada51ce240bc47d701a02dac`;
- original proof/source cross-review:
  `85eb51dcf8ef48c839392ea7d4c676357d84a1d0f5b1044c2bbe0d27dcef0f27`.

## Mathematical and review scope

The complete argument is in the PDF: quantitative compactness and cuts;
per-cell normalization; the band bottom and threshold phase analysis;
the uniform mesh/ring/chain estimate; tail exclusion; head estimate;
block coordinate-change Rayleigh bounds; cumulative telescoping error;
the endpoint-controlled Riemann sum; coefficient continuity, strict
monotonicity and limits; and all domain inclusions needed for rate-free,
hard and soft comparisons. The soft theorem only asserts divergence of
the centered coefficient and retains `n b_n -> infinity` separately.

No numerical experiment, external-model review, upload, Git operation,
or global project edit was performed. The paper-write and paper-compile
skills and their required writing/citation references guided the modular
draft, verified four-entry bibliography, and actual build checks; the
admitted plain mathematical-article plan overrides ML quotas and old
external-review defaults.

The drafting assistant previously reviewed the underlying proof package.
That earlier review is not an independent manuscript review of this
later draft. The initial TeX/Bib/PDF snapshot is now frozen for the
separately assigned non-author manuscript reviewer. Final changes,
two fresh builds, all-page QA and final sealing remain root-coordinated.
