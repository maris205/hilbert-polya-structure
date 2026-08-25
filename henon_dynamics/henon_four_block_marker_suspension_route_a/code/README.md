# C139 executable audit

Run, in order:

```bash
python3 code/c139_marker_producer.py
python3 code/c139_marker_checker.py
python3 code/c139_sympy_crosscheck.py
python3 code/c139_replay.py
python3 code/c139_mutation.py
python3 code/c139_release_manifest.py
```

The checker and SymPy program import no producer module.  The finite prefix is
only a sentinel for the separately proved all-period identities.  The mutation
suite includes repaired-payload-hash semantic corruptions and one stale-hash
control.
