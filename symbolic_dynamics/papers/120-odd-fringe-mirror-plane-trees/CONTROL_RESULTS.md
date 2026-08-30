# Exact control results — P120

Status: **PASS / finite falsification evidence / external HOLD**.

Command:

```text
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
```

## Canonical result

- status: **PASS**;
- exact assertions: **1,155,278**;
- states enumerated: **82,501**;
- exhaustive phase: the separate empty state and every plane rooted tree of
  orders `1 <= n <= 12`;
- formal-series horizon: every coefficient through `x^30`, with the
  parity-separated elimination checked through `z^15`;
- arithmetic: exact integers only;
- dependencies: Python standard library only, with no random seed, floating
  point, symbolic package, or external data.

The direct carrier/fixed/two-cycle rows through order twelve are:

| `n` | carrier | fixed | two-cycles |
|---:|---:|---:|---:|
| 0 | 1 | 1 | 0 |
| 1 | 1 | 1 | 0 |
| 2 | 1 | 1 | 0 |
| 3 | 2 | 2 | 0 |
| 4 | 5 | 5 | 0 |
| 5 | 14 | 8 | 3 |
| 6 | 42 | 36 | 3 |
| 7 | 132 | 48 | 42 |
| 8 | 429 | 303 | 63 |
| 9 | 1,430 | 368 | 531 |
| 10 | 4,862 | 2,792 | 1,035 |
| 11 | 16,796 | 3,248 | 6,774 |
| 12 | 58,786 | 27,310 | 15,738 |

## Independent lanes

1. Recursive update is compared with an implementation that snapshots every
   old trigger before applying any reversal.
2. Every image is checked for unchanged order, unordered rooted shape,
   fringe-order multiset, and pointwise fringe order under the recursively
   induced vertex transport.
3. The second iterate, root-local fixed criterion, global-mirror involution,
   and iterate-fixed parity through time six are tested state by state.
4. An independent parity recurrence for
   `e(z)=E(sqrt(z))` and `o(z)=O(sqrt(z))/sqrt(z)` is compared with exhaustive
   fixed counts.
5. Both coupled equations are cross-multiplied and checked through `x^30`.
6. The displayed degree-six `P(x,F)` has zero residual through `x^30`; a
   separate sparse-polynomial lane exactly reconstructs
   `Res_B(Res_G(H1,H2),H3)=4*x^2*P` over the integers; the smaller
   parity-elimination polynomial has zero residual through `z^15`.
7. Every row of `code/coefficient_table.csv` is parsed back and compared with
   independently generated exact counts.

The controls falsify both identifications with ordinary mirror symmetry.  In
tuple notation with `()` a leaf, the first `M`-fixed/non-mirror witness is
`((),((),))` at order four.  The first mirror-fixed/non-`M` witness is
`(((),((),)),(((),),()))` at order nine.

The stored transcript `code/verification_output.txt` is canonical.  A
fresh standard-library process was compared with it by `cmp` and was
byte-identical.  The coefficient artifact has **31 data rows plus its
header** and is **837 bytes**.

These controls fix conventions and attack arithmetic.  They do not prove an
infinite theorem, novelty, priority, owner clearance, asymptotics, or
minimality of the algebraic polynomial; those claim boundaries remain as
stated in `CLAIMS_EVIDENCE.md`.
