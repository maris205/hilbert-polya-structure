# P215 ordinary article build plan — source only

`BUILD_NOT_AUTHORIZED / NO_PDF / PAGE_COUNT_UNMEASURED`.
The intended length is 4–6 pages including references; correctness and
legibility take precedence over that unmeasured target. No source was
expanded or compressed to manufacture a page count.

## Local source inputs

main.tex, math_commands.tex, references.bib, and the five section files:
0_abstract.tex, 1_setup.tex, 2_clock.tex, 3_inverse.tex, 4_scope.tex.
The class is article[11pt], packages amsmath, amssymb and amsthm, and
bibliography style plain. There is no external picture, local style,
generated table, conference template or font override. All actual
installed class/package/style/font implementations remain build dependencies;
their names here are not provenance evidence.

## Descriptive future procedure, not a grant

After full source reception and separate authorization, root must bind a
fresh physical source-only work directory, actual engine/BibTeX resources,
environment/reproducibility settings, complete input pins and output capture.
The usual stages would be one pdfLaTeX pass, one BibTeX pass and two
resolving pdfLaTeX passes, all with full exit/log records. No engine has
been queried or invoked in this source task. Shell escape is not requested.

Every successful build still needs unresolved-reference/citation checks,
font diagnostics/embedding, box warnings, actual page count and actual
rendered-page inspection. A PDF/image hash is not a visual inspection.
No old PDF or auxiliary product may seed a source-only build.

An initial build would not replace the two physical source-only terminal
builds and final all-page views after the required manuscript A/B deltas.
The current package supplies no build log, PDF, canonical layout result,
diagnostic count, rendered page or viewing receipt.
