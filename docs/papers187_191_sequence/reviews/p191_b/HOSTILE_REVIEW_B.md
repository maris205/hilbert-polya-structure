# P191 process-separated Hostile Review B

## Verdict

`PASS / C=0 M=0 m=0 / ACCEPTED_NO_CHANGE / OWNER_AMBER / HOLD_EXTERNAL`

Review B re-opened every theorem, clock bound, fibre factor, endpoint
boundary, and package receipt for `papers/191-prefix-divisibility-cuts/`
without importing the author verifier or Review-A code. No file in the paper
directory was edited.

## Independent attack surface

- Temporal theorem: rederived from literal monotone cut deletion, fixed-state
  characterization, and the permanently retained first cut.
- Sharp clock: reopened by forcing equality in the cut-loss bound and tracing
  the unique witness orbit.
- One-step inverse theorem: attacked by interval-local deleted-cut subset
  grammars, not by the author's global target DP or Review A's recursive
  tuple/binning implementation.
- Package boundary: the nine pinned inputs in `PINNED_INPUTS.sha256` were
  checked byte-for-byte; the formal Review-A package is the paper-local
  `reviews/round1/reviewer_a/` directory, while
  `docs/.../p191_a_preliminary_superseded/` is auxiliary provenance only and
  is intentionally not pinned as formal Review A.
- Artifact boundary: a fresh source-only build from only `main.tex` and
  `references.bib` reproduced the accepted PDF hash exactly.

The deterministic control exhausts every carrier through `N=15` and records
`exact_assertions=164049`. That finite pressure is a regression receipt only;
it is not proof, ownership, or novelty clearance.

## Findings

- Critical: `0`
- Major: `0`
- Minor: `0`

No manuscript repair is requested. Review B accepts only a byte-identical
Round-2 receipt of the accepted Round-1 manuscript. `OWNER_AMBER` and
`HOLD_EXTERNAL` remain mandatory, and the bounded search non-hit remains
non-novelty evidence rather than a priority certificate.
