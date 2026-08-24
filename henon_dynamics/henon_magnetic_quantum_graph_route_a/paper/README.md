# Paper build

`main.tex` is the final C138 release paper.  The preserved PDFs record the baseline, the gauge/antiunitary revision, and the final Laurent/orientation-boundary revision.  `main.pdf` must be byte-identical to `main_round2.pdf`.

The final is built twice in fresh isolated directories at `SOURCE_DATE_EPOCH=1787529600`, then checked for deterministic hashes, embedded fonts, zero warnings, and page-by-page visual integrity.
