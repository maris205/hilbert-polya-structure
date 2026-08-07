# HCS-C17 computation and independent verification

`modular_clock.py` is the producer for the frozen modular cusp-clock artifacts.
`independent_check.py` is a separate verifier: it does not import the producer
and independently implements integer matrix arithmetic, Euler's totient,
double-coset representatives, Gauss-word enumeration, the power/translation-
length formulas, the Dirichlet series, and the modular scattering coefficient.

From the project directory, generate the default artifacts with:

```bash
python code/modular_clock.py --output results
```

Verify the committed artifacts with 110-decimal-digit recomputation:

```bash
python code/independent_check.py --results results \
  --output results/independent_check.json
```

Run the unit tests with:

```bash
python -m unittest discover -s code -p 'test_*.py' -v
```

After the release metadata has been frozen, verify the complete package with:

```bash
python code/release_manifest.py --verify
```

The verifier checks all six result files and every mathematical row: 400
rigidity-family identities, 48 Chebyshev power identities, 80 double-coset
levels, 274 primitive Gauss-word rows, 96 homogenization rows, and 12
Dirichlet-convergence rows. It also recomputes the physical-line scattering
coefficients. Residuals created by the producer's 80-digit rounding are checked
against a strict threshold and against their summary maxima; substantive values
are compared to independent 110-digit calculations.

The checker reads neither a prime table nor a Riemann-zero table. A nonzero exit
status means an artifact is missing, malformed, inconsistent, or fails an
independent mathematical recomputation.
