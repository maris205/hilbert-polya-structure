# C337 executable lanes

From the package root, with bytecode disabled:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c337_kicked_rotor_producer.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c337_kicked_rotor_checker.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c337_kicked_rotor_sympy_crosscheck.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c337_kicked_rotor_replay.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c337_kicked_rotor_mutation.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c337_release_manifest.py --write
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c337_release_manifest.py
```

The checker is producer-independent.  Each Python entry point explicitly refuses optimized execution.  The release manifest excludes itself from the 27-payload hash ledger.
