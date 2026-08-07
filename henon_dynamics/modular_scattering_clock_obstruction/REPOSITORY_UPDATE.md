# Repository update

Candidate HCS-C17 is prepared for release as a modular scattering
open/closed-clock obstruction with stable Selberg closure.

- Computation/source commit: `54839370e988dd419baafd9fcf8945e7c31d7ea6`.
- Complete release tag: `hcs-c17-v1`.
- Target branch: `main`.
- Remote: `git@github.com:maris205/hilbert-polya-structure.git`.
- Release manifest: `results/release_manifest.json`.

The package contains the theorem note and compiled PDF, derivation and source
audit, Route-A record, exact integer certificates, high-precision analytic
controls, a non-importing independent checker, adversarial tamper tests, and
the updated research registries.

Reproduce and verify from this project directory:

```bash
python code/modular_clock.py --output results
python code/independent_check.py \
  --results results --output results/independent_check.json
python -m unittest discover -s code -p 'test_*.py' -v
python code/release_manifest.py --verify
```

The release manifest binds the listed package files with SHA-256.  It is a
consistency ledger, not a cryptographic signature; the SSH Git remote and
release tag provide the external provenance anchor.
