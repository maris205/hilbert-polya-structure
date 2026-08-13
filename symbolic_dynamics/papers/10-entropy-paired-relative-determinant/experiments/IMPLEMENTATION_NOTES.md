# SD-C12 Implementation Notes

Run from the Paper10 directory:

    python code/sdc12_relative_determinant_experiment.py
    pytest -q code/test_sdc12_relative_determinant_experiment.py
    sha256sum -c results/SHA256SUMS.txt

Dependencies are numpy, sympy, and pytest. The full run takes about 16
seconds on the development CPU. It internally generates 32,769 tensor atoms
for the 16,384-pair convergence audit.

Exact rational-product coefficients are formed by truncated local-factor
convolution and checked after multiplication by the complete denominator.
This avoids global symbolic expression swell while remaining exact.

Random pairing controls are restricted to fixed width-eight entropy blocks.
This makes bounded overlap part of the frozen theorem. Global unbounded
random matchings are outside scope and are not reported as trace-class
passes.

No crossing census, target root, or Riemann-zero file is used. Run with
PYTHONDONTWRITEBYTECODE=1 and pytest option -p no:cacheprovider when a
cache-free artifact tree is required.
