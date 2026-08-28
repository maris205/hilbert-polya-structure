# Test report

Run from the package root:

```text
python3 -B code/c222_double_integrator_producer.py
python3 -B code/c222_double_integrator_checker.py
python3 -B code/c222_double_integrator_sympy_crosscheck.py
python3 -B code/c222_double_integrator_replay.py
python3 -B code/c222_double_integrator_mutation.py
```

All five commands pass.  The checker is producer-independent and enforces
recursive exact-key closure.  It reconstructs the branch from `F_a`, proves
the radicand positive, checks both durations, directly integrates both arcs,
places the switch on the braking parabola, confirms the terminal state and
evaluates the HJB derivative identity.  SymPy separately reconstructs both
sign branches, direct braking, reflection and parabolic scaling.  Replay uses
a clean subprocess and temporary directory.  Mutation testing repairs the
payload hash after each semantic/schema change and separately checks a stale
hash, preventing the checksum from acting as the only validator.
