# C318 paper builds

`main.tex` is one auditable source with a release-controlled
`\CRevisionRound` macro.

- round 0: complete finite open-chain characteristic and edge theorem;
- round 1: adds bulk winding, parity, boundary faces, and propagation;
- round 2: adds the quench corollary, evidence, collision, and Route-A
  boundaries.

`main.pdf` must be byte-identical to `main_round2.pdf`.  The release script
builds each round twice in fresh directories under a fixed epoch, rejects
any LaTeX/package/layout/reference warning, verifies extracted revision
tokens, rasterizes every page, and requires every listed font to be embedded
and subset.
