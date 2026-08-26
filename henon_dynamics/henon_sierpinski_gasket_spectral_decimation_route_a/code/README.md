# C184 executable certificate

Run from the package root:

```bash
python3 code/c184_spectral_decimation_producer.py
python3 code/c184_spectral_decimation_checker.py
python3 code/c184_sympy_crosscheck.py
python3 code/c184_replay.py
python3 code/c184_mutation.py
python3 code/c184_release_manifest.py
```

The producer uses integer polynomial recurrence, an explicit
triangle-refinement graph, and numerical finite-graph diagonalization as a
regression sentinel.  The checker imports no producer code: it constructs
the graph by independent IFS edge copies, reconstructs characteristic
polynomials with a different coefficient algebra, uses exact Bareiss
determinants and characteristic evaluations, and repeats the finite
eigenspectrum test.  The separate SymPy program computes direct graph
characteristic polynomials through level four and reconstructs the all-level
recurrence through level five.  The mutation suite contains 70 repaired-hash
semantic attacks and one stale-hash attack.

The finite checks are not the proof of the all-level theorem.  The proof and
the precise Fukushima--Shima ownership boundary are in `THEOREM_PACKAGE.md`
and `paper/main.tex`.
