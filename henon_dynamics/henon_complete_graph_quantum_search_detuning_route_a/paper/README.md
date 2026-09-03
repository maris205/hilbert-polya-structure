# C323 paper builds

`main.tex` is one auditable source controlled by the `\CRevisionRound` macro.

- round 0 proves the complete bright/dark spectrum, exact success law,
  perfect-search iff theorem, and first hitting time;
- round 1 adds the integer critical-detuning sequence, complete-graph
  global-phase equivalence, and every missing-sector face;
- round 2 adds the exact evidence ledger, source/collision audit, and strict
  Route-A boundary.

`main.pdf` must be byte-identical to `main_round2.pdf`.  The release gate
builds each round twice in fresh directories under a fixed epoch, rejects any
LaTeX/package/layout/reference warning, verifies extracted revision tokens,
rasterizes every page, and requires every listed font to be embedded and
subset.
