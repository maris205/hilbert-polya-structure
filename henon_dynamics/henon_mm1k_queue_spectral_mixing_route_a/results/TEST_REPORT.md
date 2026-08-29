# Test report — HCS-C225

Commands (run from the package root):

```text
python -B code/c225_mm1k_producer.py
python -B code/c225_mm1k_checker.py
python -B code/c225_mm1k_sympy_crosscheck.py
python -B code/c225_mm1k_replay.py
python -B code/c225_mm1k_mutation.py
```

Expected release outputs:

- `C225_PRODUCER_PASS`, 20 stationary / 60 spectral / 240 kernel rows;
- `C225_CHECKER_PASS`, 3655 assertions, producer_imported=false;
- `C225_SYMPY_PASS`, 46 checks and 8 word-algebra checks;
- `C225_REPLAY_PASS`, exact canonical bytes;
- `C225_MUTATION_PASS`, 25 repaired-hash + 1 stale-hash rejection and 2
  unknown-key rejections.

The checker directly reconstructs the generator, Jacobi modes, spectral kernel,
TV inequality, capacity limits and absorbing faces.  It does not import the
producer.  The manifest reruns all commands in clean subprocesses and checks
the 27-payload/28-physical-file closure.
