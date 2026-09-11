# P212 two terminal source-only builds

This exact recipe is enabled only after accepted physical Round2. It has two
valid one-shot identifiers, `terminal01` and `terminal02`, each bound by a
separate grant. It copies only eight TeX/Bib files from frozen_round2 into a
new cold tree, never a PDF or generated product. The two output directories
must be absent; failed partial trees are retained and never retried.

The build preserves the accepted ordinary trust boundary and current 223-row
runtime manifest from the accepted B build. It runs pdflatex, BibTeX, and two
more pdflatex passes with no shell escape and generator suppression; captures
all streams/statuses, eight-product snapshots, FLS/log/AUX/BBL/BLG/PDF,
pdfinfo/fonts/text/final diagnostics, and every 150 dpi page PNG. Pre/post
source and runtime hashes must stay equal. Full artifact reception, PDF pair
comparison and actual page viewing are separate from command success.
