# Repository update

Candidate HCS-C16 is released as an explicit quaternionic $S$-arithmetic
worked example with scoped Route-A obstructions.

- Computation source/results commit: `24553c8`.
- Complete release tag: `hcs-c16-v1`.
- Target branch: `main`.
- Remote: `git@github.com:maris205/hilbert-polya-structure.git`.
- Release manifest: `results/release_manifest.json`.

The complete package includes the paper and PDF, derivation and source audit,
Route-A record, exact algebraic certificates, high-precision finite tables,
hardened independent checker, mutation tests, and root research registries.

Reproduce and verify from this project directory:

```bash
python code/s_arithmetic_clock.py --output results
python code/independent_check.py \
  --results results --output results/independent_check.json
(cd code && python -m unittest -v test_s_arithmetic_clock.py)
python code/release_manifest.py --verify
```

The internal four-file artifact manifest detects accidental changes to the
producer outputs. The broader release manifest binds the full listed package.
Neither self-issued manifest is a cryptographic signature; repository access
control and the Git tag provide the external provenance anchor.
