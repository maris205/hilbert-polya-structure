# SD-C11 Implementation Notes

Run:

    python code/sdc11_reflection_double_experiment.py
    pytest -q code/test_sdc11_reflection_double_experiment.py
    sha256sum -c results/SHA256SUMS.txt

Dependencies: numpy, sympy, and pytest. Atom generation, cocycle word
reduction, exact path enumeration, fixed seeds, and all output paths are
self-contained. The main run takes roughly 45 seconds on the development
CPU because the exact recurrent word census reaches power 12.

Exact algebra is used for word identity and opaque coefficients. Binary64
is used only for finite reflection, determinant, pairing, and random-DAG
residuals. All numerical conclusions are compared with exact formulas.

At infinite atom count the quadratic trace 2 sum_p 1/p diverges. It is
reported only as a formal/cutoff term; det_3 removes it and starts its honest
trace series at fourth power.

No cache files belong to the artifact set. No Riemann-zero or target-root
file is opened by the executable.
