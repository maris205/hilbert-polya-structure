# Exact control results

## Frozen command

Run from this paper directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p144.py
```

The canonical transcript is `verification_output.txt`.  Byte-identical replay:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p144.py | cmp - verification_output.txt
```

The accepted terminus is

```text
TOTAL_ASSERTIONS=6005502
STATUS=PASS
```

## Coverage

| Control | Exact coverage |
|---|---:|
| Semilengths | `1..12` |
| Dyck states | 290,511 |
| Fixed/terminal targets | 82,500 |
| Exact assertions | 6,005,502 |
| Random samples | 0 |
| Floating-point comparisons | 0 |

For every state, the audit checks Dyck validity, unique factor concatenation,
factor primitivity, closure, the fixed/nonfixed dichotomy, exact one-factor
drop, every closed-form iterate, endpoint, pointwise depth, and terminal
fixity.  For every size it checks the Catalan total, primitive fixed census,
all ballot layers, the unique deepest source, all basin partitions, and the
unique maximum fibre.  For every fixed target it checks the full depth profile
and constructs and verifies the claimed unique source at every feasible depth.

## Complete size census

| `n` | states | fixed targets | max depth | max fibre | assertions |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 0 | 1 | 24 |
| 2 | 2 | 1 | 1 | 2 | 44 |
| 3 | 5 | 2 | 2 | 3 | 102 |
| 4 | 14 | 5 | 3 | 4 | 277 |
| 5 | 42 | 14 | 4 | 5 | 828 |
| 6 | 132 | 42 | 5 | 6 | 2,620 |
| 7 | 429 | 132 | 6 | 7 | 8,594 |
| 8 | 1,430 | 429 | 7 | 8 | 28,901 |
| 9 | 4,862 | 1,430 | 8 | 9 | 99,024 |
| 10 | 16,796 | 4,862 | 9 | 10 | 344,335 |
| 11 | 58,786 | 16,796 | 10 | 11 | 1,211,914 |
| 12 | 208,012 | 58,786 | 11 | 12 | 4,308,839 |

## Independence and interpretation boundary

The literal update is implemented from the positions of the first two returns
to height zero.  The predicted iterate is implemented separately from the
initial primitive-factor list.  The two representations are compared at every
step, which reduces the risk of verifying a formula against the same code path
that defined it.

The layer formula is evaluated by exact binomial arithmetic.  Basin profiles
are accumulated from the enumerated functional graph and then compared with
the constructive inverse formula.  No hash-based probabilistic equality,
floating point, or sampling is used.

These controls can expose a false boundary case, nonunique deepest state,
missing source, extra source, or incorrect layer formula.  They do not replace
the all-parameter proofs and do not provide priority or owner clearance.
