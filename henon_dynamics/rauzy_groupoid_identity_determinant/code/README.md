# C29 exact code release

Phase 2 implements two independent programs and a fail-closed release runner.

## Producer

- source-lock the six C25/C26/C28 inputs by SHA-256;
- reconstruct the C25 graph and fixed-frame arrows;
- build formal inverse arrows without identifying them with distinct original
  arrows having opposite endpoints;
- verify state continuity, linear and cyclic non-backtracking, primitivity and
  exact chronological holonomy of `C1,C2`;
- verify `B=AHA`, `C=AKA`, `KYK=YKY`, the expanded C26 word and the order-four
  repetition control;
- enumerate the frozen small-length identity census as regression evidence;
- emit determinant-moment and Route-A scope decisions in canonical JSON;
- derive the C26 24-letter relation from the rank-one braid and substitutions,
  rather than accepting the final word as an input;
- exclude platform and working-directory fields from the canonical payload.

Run it directly with

```bash
python code/c29_producer.py
```

The default output is `results/c29_certificate.json`.

## Independent checker

- do not import the producer;
- implement separate integer matrix multiplication/inversion and word
  reduction;
- reconstruct expected matrices from upstream artifacts rather than copying
  producer output;
- verify the canonical payload digest before semantic fields;
- reject rehashed mutations of chronology, inverse identity, cyclic closure,
  primitivity, gauge invariance, normalized trace and natural-extension scope;
- reconstruct the C26 matrices from frozen elementary Rauzy words and replay
  the derived relation independently;
- keep the exact all-cycle determinant moments separate from primitive-cycle
  classification.

Run it with

```bash
python code/c29_independent_check.py
```

The checker currently passes 14 fail-closed gates and writes
`results/c29_independent_check.json`.

## Test suite

`test_c29.py` contains 38 regression, mutation and fuzz tests.  Mutations are
rehash-aware: except for the explicit stale-digest test, the payload digest is
recomputed before the independent checker is asked to reject the altered
claim.  The tests cover inverse/opposite-edge confusion, chronology, witness
tokens, all-versus-primitive moments, C26 matrix and count changes, repetition
characters, prime-limit order, determinant terminology, natural-extension
identity, the intrinsic-roof firewall and unknown schema fields.

The checker uses recursive type-strict comparison, so rehashed JSON mutations
such as integer-to-boolean or integer-to-float substitutions are rejected.
The suite also builds temporary release trees to verify whole-project file
discovery, required-artifact failure, cache exclusion and protected-file
change detection.

The expensive independent length-nine census is computed once per unit-test
process under a complete topology-and-matrix fingerprint and deep-copied
across identical mutation cases.  The command-line checker never uses that
cache and recomputes the census on every run.  An AST firewall rejects imports
from the producer or dynamic import/evaluation, and a subprocess test locks
both the uncached checker CLI success path and fail-closed exit path.

## Reproduce everything

From any working directory:

```bash
/absolute/path/to/code/run_c29.sh
```

The default runner verifies the existing manifest first, rebuilds the
certificate and checker report in a private temporary directory, runs all
tests, compares the rebuilt JSON byte-for-byte with the frozen artifacts, and
verifies the manifest again.  It never overwrites the official results.  All
Python calls use isolated mode with an empty cache prefix, so caller cwd,
`PYTHONPATH`, user-site packages and old project bytecode cannot affect the
replay.

Manifest refresh is intentionally separate:

```bash
/absolute/path/to/code/run_c29.sh --refresh-manifest
```

Use that option only while preparing an intentional release.  The default
runner never writes or blesses a stale manifest.
