# Independent Stage-2 cross-audit report

## Gate results

| Gate | Result |
|---|---|
| Frozen manifest and exact file set | PASS |
| C0 cylinder/Frostman proof | PASS |
| C1--C2 exact counts and finite unions | PASS |
| Constant convolution and Fourier boundary | PASS |
| `p=2` closed formulas | PASS |
| `L`-level denominator, monotonicity, error, convergence | PASS |
| Four-state strict max-SCC example | PASS |
| Independent arithmetic replay | PASS |
| Six negative controls | PASS |
| BLW/2021/2022 owner subtraction | PASS |
| Active package immutability and hygiene | PASS |

## Independent replay

The separately written implementation completed `56,710` exact assertions.
It independently reproduced:

- `360` parameter cases and `6,219` one-level compositions;
- `4,734` residue-contraction comparisons;
- `816` recursive component and `1,086` recursive feeder integer counts;
- `175` two-phase parameter cases and `1,050` fixed-composition formulas;
- `10,212` `L`-level compositions and prefix-denominator checks;
- all `36` active selected optimizers, including their exact rational
  prime-log forms;
- `39` exact `p|d^L` hits;
- all `6` negative controls.

The independently obtained maximum coefficient errors are exactly `2/93` at
cycle index two and `2/24573` at cycle index six, matching the frozen
evidence.  It also rederived every advertised active count and verified all
active evidence hashes.

Two consecutive full independent replays produced the identical canonical
JSON SHA-256
`fa2e1a36fa71217da4710d43b86513ac75b0e9425ee0fe6bb5d82018e6a55e5a`.

## Negative controls

The independent controls reject unconditional divisibility necessity, a
single missing core edge, a core-to-feeder return, an incomplete feeder row,
all three invalid parameter boundaries, and an arbitrary Hausdorff max-SCC
formula.  In particular, the missing-edge depth-one count is `5`, not the
complete-block prediction `8`, and the four-state exact dimensions are
`log(2)/3` and `log(2)/2`.

## Status

The terminal snapshot is byte-for-byte equal to the initial snapshot.  The
active package still has manifest SHA-256
`bea7a189ea0b3472cc6b469eb36e6460b60c4bae66265659b19af6e89883f0da`,
all `16` self-excluding entries verify, and cache, symbolic-link, and
nonregular counts are all zero.

```text
STAGE2_CLEAN
```
