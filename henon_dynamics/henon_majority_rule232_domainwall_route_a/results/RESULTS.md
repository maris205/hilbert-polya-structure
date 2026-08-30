# C251 results

The producer emits `c251_majority_evidence.json` with payload SHA-256
`d683f8fa3c81ea83e2ed9c702f0f694248c1145aa4796c3c39305b66ea4f1b49` (this
value is regenerated whenever the evidence changes).

| gate | receipt |
|---|---:|
| all-size fixed-formula rows | 64 |
| parity/run transfer rows | 216 |
| exhaustive finite-state rows | 14 (all states through (n=14)) |
| sample trajectories | 4 |
| independent checker assertions | 1,855 |
| SymPy identities | 569 |
| hostile mutations | 40/40 |

The fixed counts begin
(2,2,2,6,12,20,30,46,74,122,200,324), matching
(L_n+2cos(n\pi/3)).  The direct state census finds exactly two period-two
states for even (n), zero for odd (n), and no periods above two.  The
maximum fixed-set entry time is $\lfloor(n-1)/2\rfloor$ for $n\ge3$.

These are source-local finite-state results.  No arithmetic or target data are
present.
