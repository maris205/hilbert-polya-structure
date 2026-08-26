# Deterministic separated-reflection controls

`separated_reflection_controls.py` is the standard-library-only finite
regression layer for Paper 10. It writes ten CSV tables and one SHA-256
manifest. `test_separated_reflection_controls.py` tests the pure finite
constructions, exact active design tuple, artifact and implementation tamper
detection, and two fresh byte-identical generations.

Run from this directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v test_separated_reflection_controls.py
PYTHONDONTWRITEBYTECODE=1 python3 separated_reflection_controls.py --output-dir ../results
PYTHONDONTWRITEBYTECODE=1 python3 separated_reflection_controls.py --output-dir ../results --verify-only
```

The topology controls exhaust every function from indiscrete sets of sizes
`1,2,3,5` to two-point discrete, Sierpinski, and indiscrete targets. The
measurable controls exhaust maps to discrete measurable targets of sizes two
and three. Further tables check Dirac values on the exact measurable ledger,
finite cyclic algebraic versus continuous characters, both proxy-map
directions, tagged coproduct `K0` classes, exact component masses, finite
prefixes with separately declared symbolic `ell1` gates, label neutrality,
and external `log`-label growth witnesses.

`--verify-only` rewrites nothing. It checks every artifact hash, byte size and
row count, recomputes the metric ledger, and verifies the active protocol,
candidate, amendment, and six implementation-file hashes. The generated
manifest is excluded from its own implementation ledger to avoid
self-reference.

The finite circle mesh is explicitly a discrete proxy. A nontrivial algebraic
homomorphism in that table is deliberately typed as noncontinuous for the
indiscrete source. Likewise, finite `ell1` prefixes and finitely many increasing
`log` labels do not decide the corresponding infinite statements.

These controls are not mathematical proofs of `P10-1`--`P10-10`, actual
Deninger packet/orbit/`Q_p` collapse, full-circle character collapse, an
infinite component-measure theorem, `log p` unboundedness, source-global
aggregation, or Route credit. No network, random generator, external dataset,
target-zero table, fitting, timestamp, nonstandard package, trace, or
determinant is used.
