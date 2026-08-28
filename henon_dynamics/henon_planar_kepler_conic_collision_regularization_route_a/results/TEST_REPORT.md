# Test report

Executed from the package root:

```text
python3 code/c216_kepler_producer.py
python3 code/c216_kepler_checker.py
python3 code/c216_kepler_sympy_crosscheck.py
python3 code/c216_kepler_replay.py
python3 code/c216_kepler_mutation.py
```

Expected release statuses:

```text
C216_PRODUCER_PASS
C216_CHECKER_PASS (260 assertions)
C216_SYMPY_PASS (17 checks)
C216_REPLAY_PASS
C216_MUTATION_PASS (25 total rejections; unknown-key included)
```

The checker recomputes the Runge–Lenz identities, conic sign, period, radial action quadrature, scattering angle, radial collision times, Levi–Civita constraint, and fixed-shell boundary without importing producer functions.  Mutation tests repair the payload hash before changing values, and separately test an unrepaired stale hash.
