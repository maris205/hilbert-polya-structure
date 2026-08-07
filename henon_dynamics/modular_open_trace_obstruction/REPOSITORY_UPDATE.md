# Repository update

Candidate HCS-C18 is prepared for release as a modular open-scattering
trace-closure obstruction with a projector-resolved scope boundary.

- Computation/source commit: `0be4b276fbeffa21385aea1ec1a59dfef01da90b`.
- Complete release tag: `hcs-c18-v1`.
- Target branch: `main`.
- Remote: `git@github.com:maris205/hilbert-polya-structure.git`.
- Release manifest: `results/release_manifest.json`.

The package contains the theorem note and compiled PDF, derivation and source
audit, object-wise Route-A record, exact integer certificates, five-point
high-precision squarefree matrix controls, a non-importing independent
checker, adversarial tamper tests, two post-revision PASS reviews, and updated
research registries.

Reproduce and verify from this project directory:

```bash
python code/open_trace.py --output results
python code/independent_check.py \
  --results results --output results/independent_check.json
python -m unittest discover -s code -p 'test_*.py' -v
python code/release_manifest.py --verify
```

The release manifest binds the listed package files with SHA-256. It is a
consistency ledger, not a cryptographic signature; the SSH Git remote and
release tag provide the external provenance anchor.
