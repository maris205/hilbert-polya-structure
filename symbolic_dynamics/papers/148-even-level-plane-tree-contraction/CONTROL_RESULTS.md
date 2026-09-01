# Exact control results — P148

## Canonical replay

From this paper directory run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p148.py
PYTHONDONTWRITEBYTECODE=1 python3 verify_p148.py | cmp - verification_output.txt
```

The verifier uses only Python integers, tuples, and standard-library
combinatorics.  It has no randomness, floating point, timestamp, network, or
third-party dependency.

## Frozen coverage

| Control | Exact coverage |
|---|---:|
| Exact source layers | `1 <= n <= 11` |
| Plane-tree states | 23,714 |
| Every-target/source-size fibre comparisons | all targets of size at most the source bound |
| Labelled iterate skeletons | every state, through absorption plus one step |
| Local block-and-gap factors | degrees 1--10, inserted exponents 0--11 |
| Image-series coefficients | degrees 1--11 |
| Total exact assertions | 216,905 |

The image counts are

```text
1, 1, 2, 3, 5, 9, 17, 34, 71, 153, 338.
```

The formal `H` coefficients through degree 11 are

```text
1, 0, 1, 1, 2, 4, 8, 17, 37, 82, 185.
```

## Interpretation boundary

The program can expose a parity-reset error, order-loss bug, wrong local gap
exponent, missing productive child, false image threshold, or algebraic-series
mismatch.  It does not prove the all-parameter theorem and does not establish
novelty, priority, or release clearance.  External status is `HOLD_EXTERNAL`.

