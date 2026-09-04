# Round-1 report — Hostile Review A, P187–P191

**Close date:** 2026-09-04 UTC. **Decision:**
`5/5 REVIEW_A_ACCEPTED / OPEN C-M-m = 0-0-0 / HOLD_EXTERNAL`.

Each immutable Round-0 manuscript received a process-separated hostile review
by a nonauthor. Reviewer controls used representations and algorithms distinct
from their corresponding author controls, pinned the reviewed source/PDF and
author evidence, replayed canonically in fresh processes, and separated finite
counterexample pressure from the all-parameter written proof.

## Review-A results

| paper | independent attack route | assertions | initial findings C/M/m | Round-1 disposition | Round-1 PDF SHA-256 |
|---:|---|---:|---:|---|---|
| P187 | primewise exponent reconstruction, frozen-level attacks, independent cyclic target count | 1,444,819 | 0/0/0 | `ACCEPTED_NO_CHANGE` | `399ee1fd64a569ef3076e1049a5151e5b4b07d03d2c1592f84c5b2a811fbb8a1` |
| P188 | `frozenset` carrier with backward interval-capacity all-time inverse count | 8,193,247 | 0/0/0 | `ACCEPTED_NO_CHANGE` | `10b881a6200e075ed66514e8f4f8873c433383c8118c6037ad1ecd1d5bcb8bc3` |
| P189 | row-support sets, indegree peeling, reverse BFS, independent one/two-step target reconstruction | 1,493,113 | 0/0/0 | `ACCEPTED_NO_CHANGE` | `6ba00f6b542fdbefd4789e8f23f2d683c642132e989ff7af828436da063d6a81` |
| P190 | base-`q` cyclic words, literal Brandt multiplication, directed-walk fibres and exact eigenspace ranks | 2,615,881 | 0/0/2 | `PASS_DELTA_ACCEPTED` | `81c785768621a2c3450fc67eeabc9b91d8cfda67d1061aad851844b5dd68905d` |
| P191 | cut-mask carrier, graph peeling/BFS, separately coded global and interval inverse automata | 920,748 | 0/0/0 | `ACCEPTED_NO_CHANGE` | `d8675928ecfe528b950af5402097b5f69657efc9cba7c8eb0bb5c27ec96df78b` |
| **total** | **five process-separated attacks** | **14,667,808** | **0/0/2** | **all accepted; open 0/0/0** | — |

The assertion total is exact arithmetic parsed from the final Review-A
canonicals. It is not a sample size and carries no statistical confidence or
novelty implication.

## Accepted delta

P190 had the only requested source change. Two one-token presentation defects
were repaired:

1. `P190-A-MI-01`: removed the empty leading subscript field from Eq. (11),
   leaving the proved matrix entry `(A^{h_j})_{y_{i_j}^*,y_{i_{j+1}}}`.
2. `P190-A-MI-02`: changed `\paragraph{CRediT.}` to
   `\paragraph{CRediT}`, so `amsart` renders exactly one full stop.

No theorem, proof, table, citation, owner statement, or lifecycle boundary
changed. The original Review-A process bound the new source and PDF, repeated
its exact control, visually checked both repaired surfaces, and returned
`PASS_DELTA_ACCEPTED`. The four other Round-1 PDFs are deliberately
byte-identical no-change receipts.

## Review-B authorization and boundary

Review A is closed with zero open Critical, Major, or Minor findings. Review B
must use fresh processes and must reopen every proof, boundary, inverse,
source, and artifact kill switch without inheriting Review A's semantic
conclusions. All papers remain `OWNER_AMBER / HOLD_EXTERNAL`; this report does
not authorize circulation or submission.
