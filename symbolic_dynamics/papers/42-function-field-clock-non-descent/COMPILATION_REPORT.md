# Paper 42 compilation report

Status: `FINAL_WRITER_COMPILE_CLEAN`.

Title: **Finite-Field Clocks Do Not Become Rational Primes: Exact Factor
Non-Descent for the Full Shift**.

This report records the final writer-only build after the independent Round-2
review. The mutable research pointer remains SHA-256
`19fd82ebecf5f203bcc39d198f771e100c7b7ed52a4fdd8760bc20f972c0b976`.
No integration code, experiment, result, evaluation, Route provenance, root
README, Git, mirror, or paper-manifest byte was changed by this build.

## Deterministic accessibility build

Two independent empty out-of-tree directories were populated from the same
final 18-entry writer state. Each used the following environment and exact
230-byte ASCII command-line argument (no trailing newline):

```text
TZ=UTC
SOURCE_DATE_EPOCH=1786924800
FORCE_SOURCE_DATE=1
INJECT=\RequirePackage{cmap}\RequirePackage{accsupp}\AtBeginDocument{\let\origlongrightarrow\longrightarrow\renewcommand{\longrightarrow}{\BeginAccSupp{method=hex,unicode,ActualText=2192}\origlongrightarrow\EndAccSupp{}}}\input{main.tex}
pdflatex -jobname=main -interaction=nonstopmode -halt-on-error -file-line-error "$INJECT"
bibtex main
pdflatex -jobname=main -interaction=nonstopmode -halt-on-error -file-line-error "$INJECT"
pdflatex -jobname=main -interaction=nonstopmode -halt-on-error -file-line-error "$INJECT"
pdflatex -jobname=main -interaction=nonstopmode -halt-on-error -file-line-error "$INJECT"
```

The injection argument SHA-256 is
`f6e13d2320dc02f60ed3b4de75f5b1ce58601de5c958042025586dac6ab084b1`.
Loading `cmap` before the document supplies complete math-font Unicode maps;
the `accsupp` wrapper assigns U+2192 as the actual text of each visually
unchanged long arrow. It changes no protected source and no visible page
content. The two final PDFs compare byte-for-byte equal.

- pdfTeX: `3.141592653-2.6-1.40.22` (TeX Live 2022/dev/Debian);
- BibTeX: `0.99d` (TeX Live 2022/dev/Debian);
- fixed epoch: `1786924800`;
- PDF SHA-256:
  `b64df6a2054f9ed4047feb679170211f29f44faf253abbe21d11763360708139`;
- byte size: `430898`;
- format: PDF 1.5, 14 A4 pages;
- metadata: title exact, author `Anonymous Authors`, no host path.

## Final log, citation, font, and text QA

The final logs from both builds have:

- 0 TeX/BibTeX errors;
- 0 package or LaTeX warnings;
- 0 undefined citations or references;
- 0 multiply defined labels;
- 0 overfull boxes;
- 0 underfull boxes.

All four bibliography entries are cited and resolve. The PDF reports 26 font
rows; all 26 are embedded, subset, and equipped with Unicode maps.

Default, layout, and raw `pdftotext` extraction each contain zero illegal
C0/DEL characters, exactly three U+2192 arrows, and zero malformed `−→`
sequences. `pdftotext -bbox-layout` emits well-formed XML. Extracted text has
no unresolved reference, drafting, verification, or host-path marker. The
Stage-A `PENDING_FIRST_ARTIFACT_COMMIT` literal is required provenance, not an
unresolved placeholder.

## Page-by-page visual QA

All 14 pages were rasterized and inspected. There is no clipping, overlap,
blank page, missing graphic, illegible label, table spill, footer collision,
or orphaned heading. The three figures are pure TikZ. The dense canonical
publication block and Route tuple remain inside the text block and readable.
At 120 dpi, every final page is pixel-identical to the already visually
accepted Round-1 PDF; the accessibility repair therefore changed only the
machine-readable text layer.

## Writer scientific QA

The unique canonical publication block records final CLEAN fields only:
main/independent checks `11/11` and `11/11`, science SHA-256
`078d98da2f3c89c0f5f4e7ef6be84066ee60a1c1d82c86788de675ad349b7848`,
source resolution `29/29`, sole retrospective survivor `SD-C01`, zero theorem
and positive-control failures, six repair rows with zero classification
failures, Route checks `21/21` and `13/13`, all `2246` mutations with zero
survivors, integrity `56/56`, first materialization/idempotence `49 -> 0`, and
the exact 95-entry result ledger at SHA-256
`2ba51004cc37fa5ec2da98b6e4e5f65e9c73bb6d373f8da0009879e9ced97d0b`.

The text retains the retrospective chronology
`RETROSPECTIVE_STATIC_SEAL_FROZEN_BEFORE_AUTHORITY_MATERIALIZATION`, assigns no
novelty or priority credit, preserves the exact Stage-A pending provenance,
and keeps `STOP_DUPLICATE` as an external literature-collision boundary.

## Final 18-source publication map

The map is C-sorted by relative path and excludes this report and the
generated PDF.

```text
bb1f51e04b315759c1e330495f2b12e00b26f738daa1612129baf0f37455d309  PAPER_PLAN.md
c75a512828578d175311cbf927b48d5494f12d026b62b233bd6ee737d45cf139  WRITER_HANDOFF.md
0967f63be8aac400aacf3bb4c52320bde06e46676be147ca17000d46c41dd81d  figures/repair_ownership.tex
fc40878c53c96684a66994d13f250406cad2091067d2ae1f126370920a650b40  figures/source_target_types.tex
48a99c60efce57054562f7860cb8327c0595ee5c46996eebd8750a3e9e795249  figures/three_obstructions.tex
c7bb96126efaecaa321b925c5596440f7c14626130853e22ed3039bfbb4bec22  main.tex
ef07d87de6388fb003f8aa9aed6c87f761c52d544b3f74ef2869bcc30a7b4fa4  math_commands.tex
c0f3cb0ce7681c6fe85b83c2ada76bb46682496c78dba170fc23102bf42acd5d  references.bib
f1710325a3fa005fbabbbd3fb22f8d2eda7a408e5301e95283b8bf21ab372c8f  sections/0_abstract.tex
64a533bcc624b55e48790291250172f4ab6fb805e275997a8eae858faacea911  sections/1_introduction.tex
1b92b0cb69214293f16a57df93205143144ebebbe2e64b2dad982c207b7b4a5c  sections/2_prior_scope.tex
ce0a91542f7e7253642388398e0495ebf9324df8231e8919cd3a404f218c20e0  sections/3_source_ledger.tex
0c946bc45aa921bb469a34868a32734b4313236d5716a5e3e5eed07bea223e75  sections/4_non_descent.tex
0bcc0f30bf89bd961553911cff704087fc1f0d42240c466d4790ad3d14451d58  sections/5_repairs_ownership.tex
6542614f0931813d15b40e3b3d18dd193c093c2a91308615dd32950decda1869  sections/6_route_reproducibility.tex
e6b5bc2de48d05bd2f835576aa2ab28ef0408e7092827017ce5ffa29a9de3ed1  sections/7_conclusion.tex
3ebc63a50a683e548f102d0ffefba84013cb9284e5f3a558d97c4fce96529141  sections/A_exact_details.tex
9614ad5ead4e2f89461a023eaa2abe2b68cb354e94eb22b7dd57a87f6938b96e  sections/B_boundaries.tex
```

## Authority installation boundary

Only `main.pdf`, this `COMPILATION_REPORT.md`, and the self-excluding writer
manifest are installed or updated from the writer lane. No `.aux`, `.bbl`,
`.blg`, `.log`, `.out`, cache, raster, or build-directory artifact is
installed. Root governance, Git, mirror, and the paper manifest remain outside
this writer action.
