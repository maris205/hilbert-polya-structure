# Final QA — P179

**Disposition:** `ROUND2_DUAL_REVIEW_FREEZE / OWNER_AMBER / HOLD_EXTERNAL`.

- The final paper gives the complete spectrum, arbitrary-block absorption
  CDF, every labelled source-target kernel, and both inverse censuses, with
  `n>=1`, `t=0`, and the impossible `n-1` singleton layer closed.
- Author control: 252,320 exact assertions, including 127,202 direct
  support-formula comparisons; canonical replay PASS.
- Reviewer A/B controls: 120,977 and 209,583 assertions; manifests and fresh
  canonical replays on the corrected Round-2 source PASS; zero open findings.
- Round 0 PDF:
  `c0a97f79c22799e90b3c2bd95d0060b4b75b38b28536332e5d60fe38f2a5f923`.
  Round 1 PDF:
  `9c6018baa87f9e772a46e70cafb59cc804f6711c3a1b82852327df4b00f8bd7d`.
  Round 2 and live PDF:
  `6c93451aa6116c32164ee0d255315f88e0299b60c2ba17879d73c75309e1773c`.
- Two cold directories initialized with only `main.tex` and `references.bib`
  reproduce the final PDF byte for byte.
- PDF: 3 A4 pages, 256,926 bytes, 20/20 fonts embedded/subsetted/Unicode,
  blank identifying metadata, no encryption or JavaScript.
- Settled logs contain no warning, unresolved citation/reference, bad box,
  rerun request, or error.  All 3 final pages were rasterized and inspected;
  no clipping, overlap, blank page, formula, or bibliography defect appears.
- Bibliography/citation key sets agree (3/3).  Exact programs are proof
  regression/falsification controls and are not experiments.

The owner search remains bounded; no novelty, priority, or external release
is claimed or authorized.
