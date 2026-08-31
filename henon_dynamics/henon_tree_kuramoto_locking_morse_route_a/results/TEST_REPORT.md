# Test report

Run from the package root with bytecode disabled:

```text
PYTHONDONTWRITEBYTECODE=1 python -B code/c259_kuramoto_producer.py
PYTHONDONTWRITEBYTECODE=1 python -B code/c259_kuramoto_checker.py
PYTHONDONTWRITEBYTECODE=1 python -B code/c259_kuramoto_sympy_crosscheck.py
PYTHONDONTWRITEBYTECODE=1 python -B code/c259_kuramoto_replay.py
PYTHONDONTWRITEBYTECODE=1 python -B code/c259_kuramoto_mutation.py
PYTHONDONTWRITEBYTECODE=1 python -B code/c259_release_manifest.py
```

The producer, producer-independent exhaustive checker, SymPy cross-check,
byte replay, and hostile semantic mutation suite pass.  The checker rederives
all 477,330 assertions rather than importing producer logic; symbolic work
closes 261 identities.  The release gate reruns the entire stack and checks
fixed-epoch PDFs, extracted claim literals, embedded/subset fonts,
three-round distinction, scope locks, and exact 27-file payload closure.
