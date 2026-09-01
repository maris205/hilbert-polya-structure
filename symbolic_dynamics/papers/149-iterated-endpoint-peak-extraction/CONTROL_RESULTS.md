# Exact control results — P149

## Canonical replay

From this paper directory run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p149.py
PYTHONDONTWRITEBYTECODE=1 python3 verify_p149.py | cmp - verification_output.txt
```

The verifier uses exact integers and a subset dynamic program.  It has no
randomness, floating point, timestamp, network, or third-party dependency.

## Frozen coverage

| Control | Exact coverage |
|---|---:|
| Source ranks | `1 <= n <= 9` |
| Permutation states | 409,113 |
| Iterate-image ranks | every state, `1 <= k <= 5` |
| Explicit right sections | every feasible target, `n <= 8`, `1 <= k <= 5` |
| Comparison-poset fibres | every feasible target, `n <= 8` |
| Recursive deepest witnesses | every `1 <= n <= 9`, including intermediate rank saturation |
| Total exact assertions | 1,228,181 |

The exact one-step image sizes through rank 9 are

```text
1, 1, 3, 3, 9, 9, 33, 33, 153.
```

The maximum tails are

```text
0, 1, 2, 2, 3, 3, 3, 3, 4.
```

## Interpretation boundary

The program can expose a boundary-peak convention error, a false packing
bound, a bad terminal-tail section, an infeasible iterate lift, a non-sharp
witness, or a missing comparison-word fibre.  It does not prove the
all-parameter theorem and does not establish novelty, priority, or release
clearance.  External status is `HOLD_EXTERNAL`.

