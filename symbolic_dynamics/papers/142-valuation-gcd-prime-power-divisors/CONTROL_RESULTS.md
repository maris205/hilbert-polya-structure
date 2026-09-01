# P142 exact control results

Status: `ROUND-0 FROZEN CONTROL / HOLD_EXTERNAL`.

## Frozen command

Run from this paper directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p142.py
cmp -s verification_output.txt \
  <(PYTHONDONTWRITEBYTECODE=1 python3 verify_p142.py)
```

The replay is accepted only if `cmp` exits zero and the transcript ends with

```text
TOTAL_ASSERTIONS=319074
STATUS=PASS
```

The frozen transcript SHA-256 is
`038c6655f517df31e0ecfbba257823169619347fd1b3d27354cdd3dc428f7fa1`.

## Exact coverage

| Control | Coverage |
|---|---:|
| Odd primes | `3,5,7,11` |
| Odd-prime exponent boxes | every `2<=e<=128` for each prime: 508 boxes |
| Odd-prime states / orbit starts | 33,528 / 33,528 |
| Every-target fibre cells | 33,528 |
| Fixed iterates per box | `k=1,...,12` |
| Binary exponent boxes | every `2<=e<=48`: 47 boxes |
| Binary states | 1,222 |
| Binary equal-valuation cases | 16 |
| Total Boolean assertions | 319,074 |

Every odd-prime state recomputes the literal integer gcd and compares its
valuation with `min(2a,e-a)`.  The complete functional graph is then checked
against the recurrent set, fixed/complement-cycle classification, pointwise
entry law, sharp deepest set, temporal polynomial, image interval, and exact
fibre set for every target.  The binary lane independently checks the extra
factor at every equal-valuation state.

## Selected frozen profiles

| `e` | `L` | `U` | recurrent `R` | fixed `A` | max depth | unique deepest | depth histogram |
|---:|---:|---:|---:|---:|---:|---:|---|
| 2 | 1 | 1 | 2 | 2 | 1 | 2 | `0:2, 1:1` |
| 3 | 1 | 2 | 3 | 1 | 1 | 3 | `0:3, 1:1` |
| 4 | 2 | 2 | 2 | 2 | 2 | 3 | `0:2, 1:2, 2:1` |
| 8 | 3 | 5 | 4 | 2 | 3 | 7 | `0:4, 1:2, 2:2, 3:1` |
| 16 | 6 | 10 | 6 | 2 | 4 | 15 | `0:6, 1:4, 2:4, 3:2, 4:1` |
| 32 | 11 | 21 | 12 | 2 | 5 | 31 | `0:12, 1:6, 2:8, 3:4, 4:2, 5:1` |
| 64 | 22 | 42 | 22 | 2 | 6 | 63 | `0:22, 1:12, 2:16, 3:8, 4:4, 5:2, 6:1` |
| 128 | 43 | 85 | 44 | 2 | 7 | 127 | `0:44, 1:22, 2:32, 3:16, 4:8, 5:4, 6:2, 7:1` |

The smallest binary obstruction is `(e,a)=(3,1)`:

```text
gcd(2^3, 2^2 + 2^2) = 2^3,
```

whereas the odd-prime exponent rule would predict exponent `2`.

## Interpretation boundary

The verifier is deterministic, dependency-free, and exact.  It uses no
network, third-party package, random sample, or floating-point operation.  It
can expose a wrong valuation, missed boundary, false recurrence claim,
incorrect temporal coefficient, nonunique deepest state, or bad fibre.  It
cannot replace the symbolic proofs or establish novelty, priority, ownership,
or external readiness.
