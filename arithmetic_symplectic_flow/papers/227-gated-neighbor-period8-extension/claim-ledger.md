# Claim ledger — ANG-20260918-GNS02

| ID | Claim | Evidence / scope | State |
| --- | --- | --- | --- |
| C1 | The finite test uses the same map, source, unit roof and free-upper-boundary convention as 139. | Frozen [candidate card](candidate-card.md); implementation has no prime or floating-point input. | ESTABLISHED (contract) |
| C2 | The CPU NumPy and CUDA PyTorch paths agree on every reported stage field. | [Computation record](evidence/computation.md), `BACKEND_AGREEMENT exact_stage_records 11`. | ESTABLISHED (finite run) |
| C3 | Through equation 12, the complete capped ledger has nonzero survivors; counts are exact under the declared finite algorithm. | Equations 3--12 are uncapped; output in computation record. | ESTABLISHED (finite prefix) |
| C4 | Equation 13 reaches the new cap after storing 2,000,000 prefixes; the stage is incomplete. | `extensions_seen=2,000,001`, `capped=True`, first un-stored extension is the stop event. | ESTABLISHED (finite stop) |
| C5 | The full infinite period-8 problem is solved, or a period-8 orbit exists. | No finite-prefix implication is asserted. | NOT CLAIMED / OPEN |
| C6 | A new T1/T2, Route-A, Route-B, or analytic result follows from this test. | This package is an evidence extension only; 139's gate labels remain unchanged. | NOT CLAIMED |

The old 139 `CAP=100000` search and its status are preserved byte-for-byte.
