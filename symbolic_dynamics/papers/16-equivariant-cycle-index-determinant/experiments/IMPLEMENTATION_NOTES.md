# SD-C18 Implementation Notes

## Reproduction

Run from this paper-project directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python code/sdc18_equivariant_cycle_index_experiment.py --sanity
PYTHONDONTWRITEBYTECODE=1 python code/sdc18_equivariant_cycle_index_experiment.py
PYTHONDONTWRITEBYTECODE=1 python code/test_sdc18_equivariant_cycle_index_experiment.py
sha256sum -c results/SHA256SUMS.txt
```

The generator uses only the Python standard library, runs on CPU, performs no
network request, and reads no external dataset or Riemann-zero table.

## Exact implementation boundary

- Cyclic ordered set partitions are generated as squarefree subset words and
  canonicalized under rotation only; primitivity is checked independently.
- Conjugacy-class fixed sets, cyclic-subgroup marks, orbit sizes, stabilizers,
  and the `S_3` irreducible decomposition are computed with integers.
- The ghost audit compares exact sparse coefficients of `b(x)^r` and
  `b(x^r)`; it never equates scalar powers with Adams images.
- The auxiliary `C_2` character carrier is checked against ordinary scalar
  sign powers in 4,008 edge/power cases.
- Rank-one, stabilizer, and diagonal-superdeterminant certificates use exact
  `Fraction` arithmetic.
- Floating point occurs only in descriptive finite-cutoff Schatten tables.
  Their membership label is assigned from the theorem criterion
  `q Re(s)>1`, not inferred from the displayed finite sum.
- Inventory controls use isolated `random.Random` instances with frozen seeds
  `16000..16015`.

## Determinism and artifact discipline

CSV files use an explicit LF line terminator, JSON keys are sorted, and all
enumerated sets are sorted before serialization. The checksum ledger includes
the two code files and every result artifact except the ledger itself, with
paths resolved from the paper-project root.

The exact tests validate 17 independent obligations. No numerical
approximation is promoted to theorem evidence, and the scalar Euler shadow is
kept separate from the failed character-resolved Fredholm interpretation.
