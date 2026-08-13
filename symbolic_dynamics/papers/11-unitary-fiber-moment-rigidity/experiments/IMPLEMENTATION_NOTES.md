# SD-C13 Implementation Notes

Run from the Paper11 directory:

    python code/sdc13_unitary_fiber_experiment.py
    pytest -q code/test_sdc13_unitary_fiber_experiment.py
    sha256sum -c results/SHA256SUMS.txt

Dependencies are numpy, sympy, and pytest. Atom clocks are generated
internally. Fixed seeds are 0 through 31, and the matched random clock uses
seed 1907.

Formal recurrence variables are kept independent until an explicitly
labelled equal-path specialization. This prevents numerical phase
cancellation from hiding a mixed monomial.

The executable performs no zero search, target comparison, or crossing
census. Run with PYTHONDONTWRITEBYTECODE=1 and pytest option
-p no:cacheprovider for a cache-free artifact tree.
