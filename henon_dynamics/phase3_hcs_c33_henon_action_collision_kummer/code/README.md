# HCS-C33 Phase-3 code

## Components

- `c33_kummer_producer.py` derives the chronological marker, action curve,
  collision field, node, Hill gates, Kummer norm, modular controls, and
  conservative Route-A decision using exact SymPy arithmetic.
- `c33_kummer_checker.py` imports no producer code.  It reconstructs the
  same mathematical object independently and enforces a strict JSON schema.
- `test_c33.py` contains regression and rehashed adversarial mutations.
- `c33_hash_manifest.py` freezes the complete project release.
- `run_c33.sh` is the read-only-by-default reproduction entrypoint.

## Exactness

All theorem-level operations use integer or rational arithmetic.  Elements
of \(\mathbb Q[A]/(P_9)\) are reduced to the canonical power basis.  The
finite-field controls use exact modular arithmetic.  No numerical root
finder or floating-point threshold contributes to a promoted claim.

## Expected runtime

The producer and checker each spend most of their time on exact
discriminants, resultants, and quotient-field gcds.  A cold full mutation
suite takes several minutes because its first audit reconstructs the whole
certificate.  Subsequent mutations reuse only immutable mathematical replay
caches inside the checker; each mutated payload is still schema- and
semantics-checked.

## Run

```bash
./run_c33.sh
```

The default run verifies hashes before and after, reproduces both released
JSON files into a temporary directory, compares them byte-for-byte, and runs
the tests.  It does not refresh any released artifact.

Release preparation alone uses:

```bash
./run_c33.sh --refresh-manifest
```

After refreshing, rerun the default command before committing.
