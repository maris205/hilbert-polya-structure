# Paper build

`main.tex` is the final C137 release paper.  The three preserved snapshots are the baseline, the convention/uniformity revision, and the final convergence/boundary revision.  `main.pdf` must be byte-identical to `main_round2.pdf`.

The final is built twice in fresh isolated directories with `SOURCE_DATE_EPOCH=1787529600` and `FORCE_SOURCE_DATE=1`, then checked for deterministic hashes, embedded fonts, zero warnings, and page-by-page visual integrity.
