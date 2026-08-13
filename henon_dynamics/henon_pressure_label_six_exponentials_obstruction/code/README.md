# HCS-P48 code

`c48_pressure_labels.py` reconstructs three exact H6 survivor orbits, their
chronological monodromy matrices and minimal polynomials.  It then computes
an exact degree-32 primitive element for the compositum of their multiplier
fields and emits the deterministic certificate in `../results/`.

Run:

```bash
bash run_c48.sh
```

The computation is symbolic.  Decimal multiplier values are display-only;
no floating-point comparison is used in the theorem.
