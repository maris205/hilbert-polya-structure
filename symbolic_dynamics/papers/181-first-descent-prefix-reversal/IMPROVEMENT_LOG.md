# P181 improvement log

## Round 0 → Round 1

Hostile Review A independently confirmed the five theorem axes through
`S_9`, including exact fibres and maximizers, but found one domain-boundary
Minor: the literal map is meaningful on `S_1` although only `n=2,3` had been
recorded.

The manuscript now gives the complete one-state atlas
`F_1(1)=1`: singleton image and recurrent core, depth zero, and fibre one.
The author verifier replaces its former outside-contract sentinel with eight
explicit checks.  Its total rises from 6,273,063 to 6,273,070 assertions.

Round-1 PDF SHA-256:
`57f62423e760c5a7f4f3add7bd94a559d99468acea3b05082afa5b28e1d24861`.

## Round 1 → Round 2

Review A re-read the repaired source and PDF, replayed both exact controls,
and closed `P181-A-m01` with `0 Critical / 0 Major / 0 Minor` open.  Its
factoradic / indegree-peeling / reverse-BFS control makes 17,364,060
assertions.

A process-separated Review B then reconstructed the map with string
permutations, direct incoming sets, orbit traversal, and an explicit Project
Euler First Sort negative control.  Its 377,591-assertion transcript replays
byte-identically and reports zero open findings.  No theorem source or author
verifier changed in this round.

The Round-2 and live PDFs are byte-identical to the accepted Round-1 PDF:
`57f62423e760c5a7f4f3add7bd94a559d99468acea3b05082afa5b28e1d24861`.
Two source-only cold builds reproduce those bytes.  Round 2 is therefore
internally closed under dual hostile review, while external status remains
`OWNER_AMBER / HOLD_EXTERNAL`.
