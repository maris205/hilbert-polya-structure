# Final QA — P149 iterated endpoint-peak extraction

**Date:** 2026-09-01 UTC.  **Result:** **PASS / GO_INTERNAL**.  
**External status:** **HOLD_EXTERNAL**.

The final anonymous manuscript is 4 A4 pages and 374,480 bytes.  Its SHA-256
is `7a9e801bfecc08000db82ea37ff9b1e206e4e3ec0ca211c46481db1f401bbacb`;
`main.pdf` and `main_round2.pdf` are byte-identical.  Distinct Round-0 and
Round-1 artifacts remain preserved.

The canonical verifier replays byte for byte with 1,228,181 exact assertions
and `P149_THEOREM_INTERFACES_PASS`.  It covers all 409,113 permutations
through rank nine, full image sets through five iterates, every feasible
section through rank eight, every recursive clock witness, and every target
fibre through rank eight with independent subset-DP linear-extension counts.
Enumeration is falsification pressure, not proof.

Two fresh directories containing only `main.tex` and `references.bib` were
built by `pdflatex -> bibtex -> pdflatex -> pdflatex`; both PDFs reproduce the
canonical artifact byte for byte.  Settled logs have no undefined citation or
reference, rerun request, bad box, duplicate label, or BibTeX warning.  All
9/9 bibliography entries are cited and resolved.

The PDF is A4, rotation zero, unencrypted, form-free, JavaScript-free, and has
blank identifying metadata.  All fonts are embedded.  All 4/4 pages were
rasterized at 120 dpi and inspected after the Ji/Fu repair; no clipping,
overlap, broken formula, unresolved marker, or illegible reference was found.

Review A's 0 Critical / 1 Major / 2 Minor findings and Review B's 0 Critical /
1 Major / 1 Minor findings are all closed.  Ji owns the exact static
two-zero convention, Fu is a one-sided neighbour, and no priority is assigned
to Carlitz--Scoville without direct original-text inspection.  This QA
certifies internal consistency only; novelty, priority, authorship, posting,
submission, contact, and external release remain unauthorized.
