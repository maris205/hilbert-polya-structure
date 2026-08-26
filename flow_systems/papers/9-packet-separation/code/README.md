# Deterministic packet-separation controls

`packet_separation_controls.py` is the standard-library-only regression layer
for Paper 9. It generates eight target-free CSV tables and one SHA-256
manifest. `test_packet_separation_controls.py` tests the same pure functions,
the exact active design tuple, artifact/implementation tamper detection, and
two fresh byte-identical generations.

Run from this directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v test_packet_separation_controls.py
PYTHONDONTWRITEBYTECODE=1 python3 packet_separation_controls.py --output-dir ../results
PYTHONDONTWRITEBYTECODE=1 python3 packet_separation_controls.py --output-dir ../results --verify-only
```

The simultaneous-approximation control constructs `q=m/p^k` using exact
integer arithmetic. For every finite modulus `M` prime to `p`, it checks

```text
m = a p^k (mod M),
m p^(-k) = a (mod M),
|m/p^k-c| <= M/(2p^k).
```

The numerator and rational residues are both recorded so a numerator-only
congruence cannot masquerade as convergence of `q`. Exact `Fraction` values
own the test; decimal errors are stable display fields.

Finite cyclic rows evaluate the rational exponent modulo groups of order
prime to `p`, record the exact character exponent and kernel, and label the
single initial residue-character stage. The action rows compare the locked
inverse time action with a deliberately wrong sign. Other tables cover the
`p^Z`-only circle, unit-exponent normalization, time/transverse distinctness,
and growing finite prefixes of an excluded infinite-kernel exponent.

`--verify-only` rewrites nothing. It checks every CSV hash, byte size and row
count; recomputes the metric ledger; and verifies the active protocol,
candidate, amendment, and six implementation-file hashes. The manifest is
excluded from its own implementation ledger to avoid self-reference.

These are finite falsification and regression controls. They do not prove CRT
density in the infinite product, source-topology convergence, packet/orbit
indiscreteness, relation nonclosedness, a Hausdorff theorem, Paper-8
supersession, or any Route coordinate.

No network, random generator, external dataset, Riemann-zero table, fitted
clock/residue/weight, nonstandard package, groupoid completion, trace, or
determinant is used.
