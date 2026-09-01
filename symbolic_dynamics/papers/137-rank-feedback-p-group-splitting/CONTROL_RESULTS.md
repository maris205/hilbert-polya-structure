# Exact control results

## Frozen command

Run from this paper directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
```

The canonical byte transcript is `code/verification_output.txt`; a replay is
accepted only if it compares byte for byte and terminates with `STATUS=PASS`.

## Coverage

| Control | Exact coverage |
|---|---:|
| Literal cyclic kernel/image cells | 176 |
| Base cyclic group elements represented | 10,350 |
| Partition states, all weights 1--50 | 1,295,970 |
| Fixed-OGF coefficients | 51 |
| Every-target fibre/image cells, weights 1--35 | 81,155 |
| Zero-fibre targets in that range | 30,923 |
| Total assertions | 18,504,770 |

The cyclic controls use `p in {2,3}`, exponents `1..8`, and feedback ranks
`0..10`.  The partition layer independently compares the direct type step
with factorwise image/kernel exponents.

## Selected exact censuses

| `n` | states | fixed | image | max fibre | max depth | deepest source |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 42 | 23 | 28 | 4 | 3 | `(10)` |
| 25 | 1,958 | 1,046 | 1,234 | 11 | 6 | `(25)` |
| 35 | 14,883 | 7,861 | 9,101 | 15 | 7 | `(35)` |
| 50 | 204,226 | 106,864 | 120,872 | 31 | 9 | `(50)` |

At weight 50 the complete depth histogram is

```text
{0: 106864, 1: 74772, 2: 17910, 3: 3690, 4: 767,
 5: 170, 6: 40, 7: 10, 8: 2, 9: 1}
```

## Interpretation boundary

The audit uses no floating point and no sampling.  It can expose a false
identity, missed boundary condition, nonunique deepest source, or incorrect
fibre count.  It cannot replace the manuscript proofs and cannot establish
novelty, priority, or owner clearance.
