# P26 code

## Round 3

`round3_conjugacy_owner.py` builds the exact bounded-conjugacy ledger and the
direct translation-covariance ledger.  It imports the frozen Round-2 matrix,
enumeration, eta-product, and quadrature definitions instead of duplicating
them.  Run its five tests with:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v test_round3_conjugacy_owner.py
```

Canonical two-run reproduction is owned by
`../experiments/reproduce_round3.sh`.

## Round 2

`round2_experiment.py` is a Python-standard-library-only deterministic
generator.  It:

1. enumerates primitive cyclic `LR` necklaces through word length 9;
2. forms exact integer matrices from `L=[[1,1],[0,1]]` and
   `R=[[1,0],[1,1]]`, then selects the `Gamma_0(11)` condition `c mod 11=0`;
3. records exact primitive/repetition owners and hyperbolic lengths;
4. writes its signed period proxy explicitly as
   `first_variation_coefficient_dT_depsilon_at_0` under the frozen period law;
5. integrates the level-11 eta-product one-form on invariant-axis segments;
6. performs q-cutoff, quadrature, basepoint, orientation, and direct `M^2`
   repetition cross-checks; and
7. builds bounded PSL2Z-invariant `j`-based, period-permutation, and full-parent
   length controls.

The `j` control is norm-matched only by finite-ledger RMS.  It is not a global
function-space norm identity.  Likewise, the positive-word enumeration is not
a complete `Gamma_0(11)` conjugacy-class enumeration.

Run the tests from this directory with:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v test_round2_experiment.py
```

All 7 tests pass.  Canonical two-run reproduction is owned by
`../experiments/reproduce.sh`; do not hand-edit generated result files.
