# Final QA — P137 rank-feedback p-group splitting

**Date:** 2026-09-01 UTC.  **Result:** **PASS**.  **Internal status:**
**GO_INTERNAL**.  **External status:** **HOLD_EXTERNAL**.

## 1. Final payload and review closure

The anonymous manuscript, five-entry verified bibliography, paper-local
verifier and canonical transcript, plans/evidence ledgers, two independent
hostile reviews, and three immutable round PDFs are present.  Review A and
Review B each returned critical 0, major 0, repair-level minor 0.  No theorem
or source repair was required.

`main.pdf`, `main_round0_original.pdf`, `main_round1.pdf`, and
`main_round2.pdf` are byte-identical: 400,794 bytes, five A4 pages, SHA-256
`7f21edb43343eb6889816c875c6a840fe0c2992de5364e299af536294b3bd5f0`.

## 2. Mathematical gate

Both reviewers independently reconstructed the group/type identity,
fixed/recurrent classification, Gaussian fixed OGF, pointwise marker budget,
sharp clock

```text
D(n)=ceil((sqrt(8n+1)-3)/2),
```

the uniqueness of `(n)`, and the rank-summed every-target fibre/image
criterion.  Independent hostile enumeration covered dynamics through weight
22 and fibres through weight 20 without importing the shipped verifier.

## 3. Exact and build replay

The canonical paper-local run replays byte for byte with
`TOTAL_ASSERTIONS=18504770` and `STATUS=PASS`.  It covers all 1,295,970
partitions through weight 50 and all 81,155 targets through weight 35.
An isolated four-stage build from only `main.tex` and `references.bib`
reproduces the final PDF byte for byte.  The settled LaTeX/BibTeX logs contain
no warning, error, undefined citation/reference, bad box, or rerun request.

## 4. PDF, sources, and anonymity

All 33 font rows are embedded, subsetted, and Unicode-mapped.  The PDF is A4,
rotation zero, unencrypted, form-free, JavaScript-free, searchable, and has
blank identifying metadata.  Every page was rasterized and inspected; no
clipping, overlap, malformed glyph, or identity leak was found.  The visible
author is `Anonymous`.

All five bibliography entries are cited and resolved against primary or
publisher records.  Finite-abelian-group classification, cyclic kernel/image
formulas, torsion context, Ferrers/Gaussian enumeration, and generic partition
dynamics remain explicit zero-credit inputs.  The P126/P135/P115 internal
firewall passed.

## 5. Decision

**PASS / GO_INTERNAL.**  The theorem and artifact package is coherent and
reproducible.  **HOLD_EXTERNAL.**  Bounded owner non-hits and internal review
do not authorize novelty, priority, authorship, posting, submission,
specialist contact, or release.
