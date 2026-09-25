# Evidence — `ASFS-SCOUT-20260918-REC01`

This package is an exact hand-audited Pre-P0 screen. The only inputs are the
four frozen branches in [candidate-card.md](../candidate-card.md). The
noninjectivity witness is the pair `(5,3,0,0)`, `(5,4,0,0)`, both mapping to
`(5,2,0,0)`. The prime clock calculation follows directly from the first
integer `d` with `d^2>p`. No code, large search, external data, prime table,
or numerical approximation was used.

The result is deliberately bounded: it does not classify all states and does
not support a global impossibility theorem. A new history-preserving reversible
scanner would require a new frozen candidate ID and a fresh P0 card.

The exact path `(4,2,0,0) -> (6,3,1,1) -> (7,2,1,0)` is retained as a control:
the moving escape prevents return to the original composite state but need not
remain unbounded after the updated integer becomes prime. The countably many
prime cycles indexed by fixed `k` are likewise part of the full carrier and
are not discarded by a clean-register convention.
