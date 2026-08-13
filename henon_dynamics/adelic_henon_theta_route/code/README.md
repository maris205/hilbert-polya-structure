# C35 code

The producer uses exact `Fraction` arithmetic to reconstruct the standard
global additive-character product formula on rational phase values.  The
checker is separately implemented and rejects type-confused or rehashed
semantic mutations.

Run from the project directory:

```bash
python code/c35_adelic_theta_producer.py --output results/c35_certificate.json
python code/c35_adelic_theta_checker.py \
  results/c35_certificate.json \
  --output results/c35_independent_check.json
python -m unittest discover -s code -p 'test_c35.py'
```

For a frozen read-only release replay:

```bash
./code/run_c35.sh
```

Only intentional release preparation may replace artifacts:

```bash
./code/run_c35.sh --refresh-manifest
```

The finite rational grid is an interface replay.  The all-rational theta
identity and the all-prime vacuum theorem follow algebraically from the
integral polynomial and self-dual lattice; they are not inferred from the
grid.

The v3 certificate also locks the exact cubic dilation recurrence,
six direct cyclotomic sum controls, the same-space noncompactness witness,
static range-pair theorem, scaling-covariance obstruction, exact fixed-scale
Poisson boundary-defect identity, and conservative Route-A status.
