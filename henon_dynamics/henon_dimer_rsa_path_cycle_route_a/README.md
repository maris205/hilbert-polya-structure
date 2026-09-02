# HCS-C291 — finite path/cycle dimer RSA

This self-contained Route-A package reconstructs the finite random sequential
adsorption of dimers on a path and a simple cycle.  A uniformly random edge
order is scanned once; an edge is accepted exactly when both endpoints are
unmatched.  The output is a **maximal** matching.  It need not be a maximum
matching.

The all-size theorem closes the path PGF convolution and its Riccati ordinary
generating function, the triangular system for every factorial moment, the
exact mean, the variance asymptotic
`exp(-4) n + 2 exp(-4) + o(1)`, and the exact support.  Conditioning on the
first cycle edge gives the exact identity `G_n(z)=z F_{n-2}(z)`, including its
mean boundary correction and variance law.

## Reproduce

From this directory, with Python 3, SymPy, PyYAML, LuaLaTeX, `pdfinfo`,
`pdffonts`, and `pdftotext` available:

```bash
PYTHONDONTWRITEBYTECODE=1 TZ=UTC python -B code/c291_dimer_rsa_producer.py
PYTHONDONTWRITEBYTECODE=1 TZ=UTC python -B code/c291_dimer_rsa_checker.py
PYTHONDONTWRITEBYTECODE=1 TZ=UTC python -B code/c291_dimer_rsa_sympy_crosscheck.py
PYTHONDONTWRITEBYTECODE=1 TZ=UTC python -B code/c291_dimer_rsa_replay.py
PYTHONDONTWRITEBYTECODE=1 TZ=UTC python -B code/c291_dimer_rsa_mutation.py
PYTHONDONTWRITEBYTECODE=1 TZ=UTC python -B code/c291_release_manifest.py
```

The producer uses first-edge convolution.  The checker does not import it: it
counts every labeled edge order by a processed-edge/matched-vertex bitmask
dynamic enumeration, then separately rebuilds the all-order moment triangle.
The finite tables are regression oracles, not proofs of the all-`n` theorem.

Frozen source commit: `7fbe9db30cc460a82883533d7cfb2edd988c5b65`.
Evaluation date: 2026-09-02.  Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.
Obstruction: `HEN-O275`.  Route A is rejected with
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`; Route B is not authorized.
