# P26 code

## Round 7

`round7_exact_survivors.py` regenerates the four frozen `p=5` degree-one and
degree-five cycle owners, rewrites them in the 12-coset
`Gamma_0(11)\PSL(2,Z)` Schreier model, and computes exact rational homology
and real-structure certificates.  It proves the full finite `a_5^2` moment
condition for all four groups and separates two full complex-period kernels
from two nonzero purely imaginary periods.

Run its thirteen tests with:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v test_round7_exact_survivors.py
```

Default verification and explicit refresh are owned by
`../experiments/reproduce_round7.sh` and
`../experiments/reproduce_round7.sh --refresh`.

## Round 6

`round6_second_variation.py` consumes the same SHA-locked Round-4 cycle-owner
and period-summary ledgers and builds three registered surfaces:

1. 552 inverse-pair/repetition rows checking the exact second-variation
   formulas and the surviving factor `r` after the logarithmic `1/r`;
2. 110 quadratic degree-moment rows for
   `Q_1=lambda_p I(M)^2`, `Q_d=0` for `d>1`; and
3. 165 finite weighted rows at `s={0.125,0.25,0.5}` and repetition cutoff
   `R=4` for the primary scalars `a_p`, `a_p^2`, plus the separately labeled
   secondary negative control `a_p^2-p`.

The generator records a finite/local audit only.  It does not enumerate the
complete primitive population, construct or continue a global zeta, count
roots, compare target zeros, or run formal A2.

Run its twelve tests with:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v test_round6_second_variation.py
```

Canonical two-run reproduction is owned by
`../experiments/reproduce_round6.sh`.

## Round 5

`round5_zeta_variation.py` consumes the SHA-locked Round-4 cycle-owner and
period-summary ledgers.  It freezes reciprocal Ruelle and frozen-stability
Selberg-type log-product conventions and builds three artifacts:

1. a 1,104-row primitive/inverse-orientation/zeta-repetition ledger;
2. a 110-row degree-moment ledger for the all-`s` recurrence obligation,
   including explicit absent degree-one bins; and
3. a 165-row one-sided Hecke-zeta variation ledger at
   `s={0.125,0.25,0.5}` and repetition cutoff `R=4`.

The generator keeps Hecke permutation-cycle degree `d` distinct from zeta
repetition `r`.  It checks exact inverse-sign cancellation and the finite
weighted consequences of the Round-4 period observations.  It does not build
a complete global zeta, run A2, read target-prime/zero tables, or promote a
primitive Euler factorization.

Run its eleven tests with:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v test_round5_zeta_variation.py
```

Canonical two-run reproduction is owned by
`../experiments/reproduce_round5.sh`.

## Round 4

`round4_hecke_correspondence.py` freezes the prime-to-11 weight-two double
coset and builds four ledgers:

1. exact branch endpoint/gluing identities;
2. exact eta-product Hecke coefficient identities plus a target-free
   nonmodular control;
3. exact permutation-cycle owners with finite complete primitive-root
   certificates; and
4. direct complex period sums at two q-cutoff/quadrature configurations.

The script tests the correspondence-cycle relation. It does not construct a
single-prime/single-orbit rule or evaluate a dynamical zeta. Run its eight
tests with:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v test_round4_hecke_correspondence.py
```

Canonical two-run reproduction is owned by
`../experiments/reproduce_round4.sh`.

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
