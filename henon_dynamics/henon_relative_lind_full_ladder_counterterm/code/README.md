# Code

Run the complete exact audit from any working directory with

    bash code/run_c73.sh

`c73_full_ladder_counterterm.py` writes the primary JSON certificate,
checks exact formal coefficients, locks all P71/P72 proof/certificate/PDF
dependencies, and rejects hostile claim mutations.  `independent_check.py`
reconstructs the regularized complex pole sums without importing the primary
module.  `test_c73.py` runs eight tests under ordinary and optimized Python.

Floating complex evaluations audit the displayed roots and partial fractions.
The theorem uses the exact root-of-unity cancellation and rational majorants,
not numerical tolerances.
