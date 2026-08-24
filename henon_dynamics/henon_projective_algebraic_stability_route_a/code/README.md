# Exact code — C121

Run in this order from the package root:

```bash
python code/c121_projective_producer.py
python code/c121_projective_checker.py
python code/c121_sympy_crosscheck.py
python code/c121_replay.py
python code/c121_mutation.py
python code/c121_release_manifest.py
```

The producer uses an exact recursive expression-DAG certificate through
iterate eight instead of expanding a degree-256 bivariate polynomial.  The
checker independently reconstructs the whole ledger and imports no producer
code.  SymPy separately checks the inverse, projective base points, a small
expanded iterate prefix, fixed points, cycle, monodromy, and parameter
controls.  The release manifest must be run only after the final PDF and all
three preserved round PDFs exist.
