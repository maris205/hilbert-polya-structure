# Code

`c52_abel_escape.py` is the certificate producer.  It computes the exact
period-four packets, the uniform cyclotomic correction, finite Abel rows and
scaled-index Laplace transforms.

`independent_check.py` does not import the producer.  It recomputes totients,
Möbius values, packet logarithms, boundary constants, convergence sentinels,
dependency hashes and claim boundaries through a separate implementation.

`test_c52.py` contains unit and adversarial controls.  Run the entire package
with:

```bash
bash code/run_c52.sh
```

The finite computations certify formulas and provenance.  The asymptotic
Abel law, Gamma profile and tagged-space obstruction are proved in
`../PROOF_PACKAGE.md`.
