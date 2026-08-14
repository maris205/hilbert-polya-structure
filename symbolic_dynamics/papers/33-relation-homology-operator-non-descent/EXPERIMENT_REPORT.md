# Experiment Report — Paper 33 / SD-C35

## Status

`PASS` for the negative claim and `STOP` for the positive Route-A candidate.

The experiment validates the implementation of the direct proofs: Manin-rank
formula, universal cusp survivor, filled cross-diamond collapse, matched
source relabel naturality, generic action controls, character controls, and
operator non-descent.

## Frozen command

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/generate_results.py \
  --cutoff 192 --random-trials 64 --seed 330000 --result-dir results
```

## Census

| Metric | Value |
|---|---:|
| moduli | 191 |
| prime / prime-power composite / mixed composite | 43 / 14 / 134 |
| relative quotient nonzero | 191 / 191 |
| prime / prime-power / mixed relative survivors | 43 / 14 / 134 |
| relative Betti sum, prime / prime-power / mixed | 611 / 189 / 3994 |
| cuspidal nonzero, prime / prime-power / mixed | 38 / 9 / 130 |
| cusp `R,S` witness returns | 191 / 191 |
| original adjacency descends | 0 / 191 |
| matched opaque relabel exact | 191 / 191 |
| random controls residual nonzero | 64 / 64 |
| cross cycle rank before / after filling | 31 / 0 |
| honest characters killing identity cycle words | 0 / 6 |
| honest characters killing both chain norm polynomials | 2 / 6 |
| zero-superdimension differences retaining cusp `SR` | 15 / 15 |
| deterministic tests | 25 / 25 |
| source-oracle hits | 0 |

## Interpretation

The positive repair fails before analytic continuation or target-zero data:
relative homology survives on every composite stratum, cross diamonds collapse
the linkage they were meant to refine, and the inherited adjacency does not
descend to the quotient.  A scalar homology determinant is trace class on
`Re(s)>2`, but its clock is a block identity clock, not the inherited edge
marker.

## Hashes

The final prototype aggregate frozen by the research stage was

```text
c5c5f34673590f98e89e6229354a8dc8fc851677c7af8702d4bf54a87e8037d4
```

After authority evaluation, double-run certification, and result freezing, the
authority result ledger is

```text
c194f21ca97758649537473f847559e1600460eaea593a68deda5bcb2811c420
```
