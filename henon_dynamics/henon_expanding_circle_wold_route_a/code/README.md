# C177 exact verification code

Run, in order:

```bash
python code/c177_expanding_circle_producer.py
python code/c177_expanding_circle_checker.py
python code/c177_sympy_crosscheck.py
python code/c177_replay.py
python code/c177_mutation.py
python code/c177_release_manifest.py
```

The producer writes the canonical finite sentinel. The checker independently reconstructs every periodic, Wold-chain, adjoint, and correlation row. SymPy checks the logarithmic zeta coefficients and exact algebra. Replay requires byte equality; mutation testing repairs hashes before demanding semantic rejection. The finite computations test implementation, while the manuscript proof owns every infinite quantifier.
