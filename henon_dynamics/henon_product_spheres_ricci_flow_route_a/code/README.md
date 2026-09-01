# Executable certificate

Run from the package root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c281_ricci_producer.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c281_ricci_checker.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c281_ricci_sympy_crosscheck.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c281_ricci_replay.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c281_ricci_mutation.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c281_release_manifest.py
```

The checker never imports the producer.  It reconstructs factor clocks,
curvature and volume formulas, the volume-normalized gauge, collapse ties,
all finite normalized-time tails, exact schemas and vector lengths, and every
boundary classification directly from the JSON fields.  The mutation audit
repairs each tampered payload hash before invoking the checker; its final
control changes content without repairing the hash.  The manifest separately
parses the Route-A YAML with duplicate/merge/alias rejection and exact
axis-to-tuple consistency.
