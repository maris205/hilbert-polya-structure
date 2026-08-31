# Consolidated hostile-review verdict — P136

Status: **GO_INTERNAL / HOLD_EXTERNAL**.

Independent Review A reconstructed the weighted endpoint integral,
actual-vertex refinement, unit-rate distribution and moments, and disjoint
forest law.  It found one major conceptual defect: prose had conflated the
discrete number of selections with continuous exponential elapsed time.  It
also required exact finite-grid notation and an explicit sigma-field argument
for conditional uniform vertex identities.

Round 1 now defines `T` solely as a discrete selection count.  Component
counts add and their PGFs multiply; continuous forest completion, when viewed
through the exponential embedding, is the maximum of component stopping
times and is not a convolution.  The finite grids and actual-vertex
conditioning proof were made explicit.  The repaired 174,170-assertion
verifier replay and all four PDF pages passed.

Independent Review B rebuilt every endpoint, top-atom, PGF, moment, and forest
identity and confirmed all Round-A repairs.  It found two minor reproducibility
residues: a clean directory needed one extra final LaTeX pass to settle page
labels, and mutable Stage-1 prose still used ambiguous stopping-time language.
The canonical protocol is now five stages (`pdflatex`, `bibtex`, then three
`pdflatex` passes), and all reader-facing prose distinguishes discrete
selection count from elapsed time.  A fresh isolated build reproduced the PDF
byte for byte.  The same reviewer closed both findings, giving **CRITICAL 0 /
MAJOR 0 / MINOR 0** and `GO_INTERNAL`.  Round 2 changes no theorem, verifier,
canonical stdout, or PDF byte.

This verdict certifies only the anonymous internal theorem package.  The
Pitt/Bar-Yehuda process, sunflower carrier, exponential-order construction,
and generic dissociation remain owned background.  Bounded owner search
cannot establish novelty or priority; authorship, posting, submission,
specialist contact, and every external-release action remain **HOLD**.
