# Code

`c63_height_flat_pressure.py` rebuilds the odd primitive mixed-axis
polynomials, applies the integral scaling, computes finite factor/height
diagnostics, locks the all-period theorem payload, and rejects 25 hostile
mutations.  `independent_check.py` separately reconstructs periods through
9 and uses exact rational Sturm intervals to check the uniform root bound.

Run:

```bash
bash code/run_c63.sh
```

The numerical root heights are diagnostics only.  The pressure theorem uses
the exact all-period height sandwich and does not depend on root finding.
