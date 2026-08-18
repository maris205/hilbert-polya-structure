# HCS-C61 I61/P61 release handoff

Status: **`I61_PAPER_INTEGRATED / P61_HANDOFF_READY / PROMOTION_PENDING`**.

This handoff follows the C60 convention: the frozen C61 code/results and
13-file formal target-lock package remain byte-stable machine inputs, while
paper and release provenance are additive.  The protected
`henon_dynamics/codex_prompt.md` is external guard material and is not staged.

## I61 paper identity

- Title: `Zeta-Equivalent Tensor Algebras of the Hénon Gassmann Twins and an Explicit Fourier Descent`.
- Source files: `paper/README.md`, `paper/main.tex`, `paper/references.bib`.
- Paper source aggregate: `b35138c8497f7f9f0e5cb3db426c9c3b667f1395fc2d8a221fe737ce24633bf6`.
- PDF: `paper/main.pdf`, 9 A4 pages, SHA-256
  `7fc2af35298df1eaa15b2ec842b83e7aade01288f34826c382f96f2461c578e8`.
- Compilation report: `paper/COMPILATION_REPORT.md`.
- Hostile paper audit: `paper/HOSTILE_AUDIT.md`, verdict
  `PAPER_HOSTILE_PASS`.

## Machine/formal bindings

- Official refresh/replay: `57/57` in both cycles.
- Payload: `b7fb70451433fd4c93fd9d60a338426362f42c4594ff4de5a35e25f49819ab1a`.
- Certificate: `c6d64787e91c78e7e7f74b88720ebf169c13d8200f78c585abe63d4e1b9b2dec`.
- Check report: `4b8b3bd21209cc9346ac7e38fbb9771d0b8b33de0cd28ccbb117beaa95e8c161`.
- Scoped manifest: `eb48ffb2ec728ca9d1966cfd22b6a9f2eba447bcf872d2068f4604112d19a6d1`.
- Formal root aggregate: `c5fc87d395e1e76d602d58bcbdba448e333a987c22d265aae80e1f4107a3dc28`.
- Route: `c773812c949bc4197b4ad5e9e2076ddd5a5d4594d5fb8884ba7109812c3fb40b`.
- Batch target-lock input: `13a626b4f43cf560bf194268d503e41ba1bbded16ad59e305c24b9045ee1d814`.
- Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Promotion gates

I61 is paper-complete and P61 is handoff-ready.  Promotion is not asserted
until the release-wide manifest, final C57--C61 audit, fresh remote reconcile,
commit, and push have all passed.  This document does not rewrite the frozen
target-lock files and does not grant `promotion_authorized` by itself.
