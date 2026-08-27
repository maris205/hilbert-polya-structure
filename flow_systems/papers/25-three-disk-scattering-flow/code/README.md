# P25 code status — Round 2 executed

`round2_three_disk_ledger.py` performs four separated operations:

1. exact enumeration of primitive oriented cyclic words through length 12;
2. center-polygon proxy construction, always labeled `MODELING_CHOICE`;
3. actual reflection-orbit solution using variational BFGS plus an independent
   least-squares stationarity solve, visibility and residual checks;
4. paraxial monodromy/half-density calculation and deterministic target-free
   neighboring, shuffle, random, and composite controls.

The monodromy product is evaluated at 80 decimal digits and compared with a
separate binary64 product.  The high-precision rebuild protects the unit
determinant check from cancellation on long unstable words; only the
finite-difference return map counts as an independent stability calculation.

Dependencies recorded by the receipt are Python 3, NumPy 2.4.4, and SciPy
1.16.1.  Commands:

```bash
python3 code/test_round2_three_disk_ledger.py -v
python3 code/round2_three_disk_ledger.py
python3 code/round2_three_disk_ledger.py --verify-existing
```

The second full command regenerates all 2,241 rows and requires an exact
byte-for-byte match.  No prime or zero data are read.  The direct
finite-difference return-map validation remains open on highly unstable rows;
the code does not promote those rows beyond `NUMERICAL_OBSERVATION` for the
stability statistic.
