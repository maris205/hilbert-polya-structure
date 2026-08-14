# Results

## Exact theorem ledger

- primitive H6 orbits: 3;
- indices per orbit: 12;
- primitive resultant rows: 36;
- rows covered by the `n>2` square theorem: 30/30;
- nonsquare `n=2` controls: 3/3;
- one-scalar power-law rejections: 3/3;
- half norms that are rational primes in the tested rows: 6;
- inherited dependency locks: 8/8.

Canonical core digest:

```text
3bb27b0da0d23743e65629f5293a6e3166a8a2fe09e9822cfced763a496a05e7
```

## Selected half norms

| signed orbit | index | full primitive norm | half norm | type |
|---|---:|---:|---:|---|
| period 1 | 3 | 361 | 19 | prime |
| period 1 | 4 | 576 | 24 | composite |
| period 3 | 3 | 55,517,401 | 7,451 | prime |
| period 3 | 5 | 3,018,197,578,515,625 | 54,938,125 | composite |
| period 4 | 6 | 332,929 | 577 | prime |

## Repetition control

The minimal trace-field cyclic norms begin as follows:

| orbit | `a_1` | `a_2` | `a_2=a_1^2` |
|---|---:|---:|---|
| period 1 | 28 | 336 | false |
| period 3 signed | 7,220 | 54,323,280 | false |
| period 4 | 576 | 334,080 | false |

Thus the surviving sequence is not the repetition of one fixed scalar Euler
label.

## Strongest positive result

For the period-four unit $L_4=289+24\sqrt{145}$, Flatters' real-quadratic
norm-one theorem implies that every term after the twelfth has a primitive
rational prime divisor.  New primes genuinely occur inside the packet.

## Strongest obstruction

The full multiplier-field norm counts the inversion pair twice and is an
integer square.  It cannot itself be a rational prime.  This is HEN-O89.

## Open theorem

Construct a common H6 packet trace that assembles prime ideals across
primitive orbits while retaining residue degrees, signs, repetition indices,
and pressure normalization.  No current source supplies this interface.
