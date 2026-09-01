# C279 executable surface

- `c279_path_tv_producer.py`: exact block-based producer; enumerates all
  19,530 inputs in the frozen grid and five rational stress cases.
- `c279_path_tv_checker.py`: producer-independent coordinate/edge-flux engine;
  imports no producer code and reconstructs every retained digest and witness.
- `c279_path_tv_sympy_crosscheck.py`: independent symbolic incidence,
  plateau-flux, dissipation, Poincare, KKT-recovery, and simultaneous-event
  reconstruction.
- `c279_path_tv_replay.py`: two unrelated fresh temporary trees, compared byte
  for byte with each other and the canonical evidence.
- `c279_path_tv_mutation.py`: 58 repaired-hash semantic attacks plus a distinct
  stale-hash control against the real checker.
- `c279_release_manifest.py`: complete 28-file release and PDF closure,
  including semantic locks for the Steidl and Hoefling direct-prior-art
  boundary.

Run from this package directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c279_path_tv_producer.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c279_path_tv_checker.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c279_path_tv_sympy_crosscheck.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c279_path_tv_replay.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c279_path_tv_mutation.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c279_release_manifest.py
```

All dynamic values and event times are exact `fractions.Fraction` objects.
