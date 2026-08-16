# Code

`c75_weighted_divisor.py` certifies the exact weighted Möbius--repetition
regrouping, nonzero channel coefficients, bidisk local-finiteness witnesses,
fixed-positive-weight root geometry, dependency hashes, and claim firewalls.

`independent_check.py` does not import the primary module.  It rebuilds the
weighted coefficient polynomials with sparse dictionaries, reconstructs the
Euler coefficients, and checks all complex roots on three positive-weight
fibers.

`test_c75.py` extends the exact coefficient comparison through degree 100 and
runs twelve tests in normal and optimized modes.

Run `bash code/run_c75.sh` from the project directory or its parent.
