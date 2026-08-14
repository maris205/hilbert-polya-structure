# PCF Markov--baker verification code

This package implements the source-locked candidate defined in the experiments
directory.

The layers are intentionally separated:

- algebra.py, cycles.py, zeta.py: exact symbolic predictions;
- model.py, controls.py: piecewise-affine candidate and matched controls;
- audit.py: independent high-precision and floating-point audits;
- protocol.py: hash-bound validation/test access gates;
- scripts: non-overwriting JSON command-line entry points.

The code must not import the first paper's package or consume its results.
Prime tables, Riemann zeros, target fitting, and Route B are outside this
candidate.
