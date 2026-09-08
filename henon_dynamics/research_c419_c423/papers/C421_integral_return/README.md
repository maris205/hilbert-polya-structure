# C421 — Integral periodic orbits of a cubic three-term recurrence

Current state: **complete final manuscript; both nonauthor full-manuscript
review passes and final PDF production checks passed**. The exact batch
seal and synchronization have separate coordinator records.

The article classifies all ordinary integral periodic orbits of
`T_a(x,y,z)=(y,z,yz+a-x)` for every integer `a`, and gives the exact
oriented cycle counts on every integral invariant level. One application
of the specified map remains the ordinary time step. It includes all
ten table rows, both sporadic cycles, the full signed analytic reduction,
the complete terminating finite certificates, least-period proofs and
the per-level dynamical zeta consequence.

- [Frozen 18-page review baseline](main_round0_original.pdf).
- [Final PDF, 18 pages](main.pdf) and [actual final build report](FINAL_BUILD_REPORT.md).
- [First manuscript review](../../manuscript_reviews/round1/C421_REVIEW.md),
  [actual revision](REVISION_ROUND1.md), and
  [second manuscript review](../../manuscript_reviews/round2/C421_REVIEW.md).
- [Main LaTeX source](main.tex) and [bibliography](references.bib).
- [Full baseline receipt and pending gates](BASELINE_REPORT.md).
- [Frozen production sources](baseline_source/main.tex) and
  [their hashes](BASELINE_SOURCE_SHA256SUMS.txt).
- [Claim-driven plan](PAPER_PLAN.md), [evidence preparation](EVIDENCE_PREPARATION.md)
  and [citation/ownership audit](CITATION_PREPARATION.md).
- [Preserved computational supplement](supplement/README.md), including
  both full raw outputs and the independent implementation/reviews.

The final PDF SHA-256 is
`13fece76ec21d56eacbdcb43303f3acef017e9f9b7f1e0e228f5438cd6761d0c`.
Two fresh stable builds are byte-identical and all 18 final pages were
actually inspected. The initial final pair's trailer-ID comparison failure
and the build-only correction are preserved in the final report.

The preserved historical baseline PDF SHA-256 is
`7fcfe7c00da4590cc44565d2343a5d3e37f233c5ece4798971891e9f145b5e1d`.
Its body occupies pages 1–13, references page 14, and the included
proof-code appendix pages 15–18. All pages were visually inspected;
final author-stage compilation has no unresolved citation/reference,
warning or over/underfull box. These author checks do not replace the
two independent manuscript-review passes.

To compile a separate working copy without rerunning any mathematical
certifier, use a new empty build directory in a copy outside a sealed tree:

```bash
env SOURCE_DATE_EPOCH=1788825600 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C \
  latexmk -pdf -interaction=nonstopmode -halt-on-error \
  '-usepretex=\pdftrailerid{}' -jobname=main -outdir=build_working main.tex
```

The actual baseline command, all three real compilation attempts and
the first-success PDF are preserved in the baseline receipt. Final
two-directory deterministic release checks are now recorded as complete
in the separate final report; the older receipt remains historical.
Do not overwrite the frozen baseline or rerun old evidence programs
inside their preserved supplement directories.

Classical cubic geometry, unforced trace-map families, the known
four-step family and the entire C413 unforced integral result are
explicitly deducted from the claimed increment. The preparation is
AI-assisted and its cited reviews are internal, not human peer review.
The dynamical factors are not target Euler factors or root-number
assertions. No Git integration, remote synchronization or submission
was performed by this author-stage task.
