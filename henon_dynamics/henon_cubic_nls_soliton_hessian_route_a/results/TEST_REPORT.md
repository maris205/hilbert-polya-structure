# Test report

Executed from the package root:

```text
python3 code/c221_nls_producer.py
python3 code/c221_nls_checker.py
python3 code/c221_nls_sympy_crosscheck.py
python3 code/c221_nls_replay.py
python3 code/c221_nls_mutation.py
```

Expected statuses:

```text
C221_PRODUCER_PASS (15 profile, 15 spectrum, 15 factorization rows)
C221_CHECKER_PASS (497 assertions)
C221_SYMPY_PASS (19 checks)
C221_REPLAY_PASS
C221_MUTATION_PASS (17 total rejections)
```

The checker independently recomputes the profile ODE, variational scalings,
VK derivative, Hessian residuals, thresholds, eigenvalues, factorization rows,
and the three-source citation ledger.  Mutations repair the payload hash before
changing values and separately test a citation claim, an unknown root key and a
stale hash.
