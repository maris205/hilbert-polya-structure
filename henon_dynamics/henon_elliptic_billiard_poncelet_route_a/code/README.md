# Reproduction commands

Run from the package root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c275_poncelet_producer.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c275_poncelet_checker.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c275_poncelet_sympy_crosscheck.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c275_poncelet_replay.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c275_poncelet_mutation.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c275_release_manifest.py
```

The producer uses 90-digit `mpmath` arithmetic with Jacobi modulus translated
explicitly to software parameter `m=e^2`.  The checker is independent and
uses SciPy double-precision elliptic functions.  SymPy checks exact algebraic
identities and coprime-period logic.  The manifest reruns every gate and closes
the exact 27-payload/28-physical-file release.
