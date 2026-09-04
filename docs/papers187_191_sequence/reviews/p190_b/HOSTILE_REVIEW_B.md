# P190 process-separated Hostile Review B

## Verdict

`PASS / C=0 M=0 m=0 / ACCEPTED_NO_CHANGE / OWNER_AMBER / HOLD_EXTERNAL`

Review B re-opened every theorem, boundary case, fibre count, and package
receipt for `papers/190-brandt-sandwich-erosion/` without importing the
author verifier or Review-A code. No file in the paper directory was edited.

## Independent attack surface

- Temporal theorem: rederived from the literal filter `uvu` and a cyclic
  good-edge induction, including `n=1` and `m=1,2`.
- One-step inverse theorem: attacked by reviewer-owned anchor-gap
  decomposition plus literal zero-transition dynamic programming, not by the
  author's matrix code or Review A's integer-word walk tables.
- Package boundary: the nine pinned inputs in `PINNED_INPUTS.sha256` were
  checked byte-for-byte; `main_round2.pdf` and live `main.pdf` are each
  byte-identical to the pinned Round-1 receipt.
- Artifact boundary: a fresh source-only build from only `main.tex` and
  `references.bib` reproduced the accepted PDF hash exactly.

The deterministic control exhausts the same 26 parameter boxes as the author
package and records `exact_assertions=1438171`. That finite pressure is a
regression receipt only; it is not proof, ownership, or novelty clearance.

## Findings

- Critical: `0`
- Major: `0`
- Minor: `0`

No manuscript repair is requested. Review B accepts only a byte-identical
Round-2 receipt of the accepted Round-1 manuscript. `OWNER_AMBER` and
`HOLD_EXTERNAL` remain mandatory, and the bounded search non-hit remains
non-novelty evidence rather than a priority certificate.
