# P25 code status — Round 3 executed

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
byte-for-byte match.  No prime or zero data are read.

Round 3 adds `round3_return_map_validation.py`.  It does not import or rebuild
the paraxial factor product.  It refines the periodic point against a 100-digit
physical ray-intersection/reflection map and forms direct Jacobians at three
frozen finite-difference scales.  A geometric specular-stationarity fallback is
used only when a rounded input point lies outside direct Newton's cylinder; the
reported stability still comes from the direct ray map.

```bash
python3 code/test_round3_return_map_validation.py -v
python3 code/round3_return_map_validation.py
python3 code/round3_return_map_validation.py --verify-existing
```

The Round-3 result is 2,241/2,241 numerically certified direct checks.  This
closes the finite-cutoff numerical validation gap but does not promote the
aggregate half-density beyond `NUMERICAL_OBSERVATION`.
