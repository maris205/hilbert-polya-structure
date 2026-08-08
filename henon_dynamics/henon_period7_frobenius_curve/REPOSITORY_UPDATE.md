# Repository update

Candidate HCS-C19 is prepared for release as a generic exact-period-seven
Hénon carrier with a genus-three scalar quotient and degree-14 oriented time
lift.

- Computation/source commit: `PENDING_RELEASE_COMMIT`.
- Complete release tag: `hcs-c19-v1`.
- Target branch: `main`.
- Remote: `git@github.com:maris205/hilbert-polya-structure.git`.

The package contains the source audit, exact genus and neighbor theorems,
compiled paper, two producer/checker certificate pairs, adversarial tests,
append-only Route-A records, three final audit summaries, and a gated roadmap
for the oriented-cover paper.

Reproduce and verify from this project directory:

```bash
python code/c19_producer.py --output results
python code/c19_independent_check.py \
  --certificate results/c19_certificate.json \
  --output results/c19_independent_check.json
python code/c19_neighbor_correspondence.py \
  --output results/c19_neighbor_correspondence.json
python code/c19_neighbor_independent_check.py \
  --certificate results/c19_neighbor_correspondence.json \
  --output results/c19_neighbor_independent_check.json
python -m unittest discover -s code -p 'test_c19.py' -v
```

The SSH remote and annotated release tag provide the external provenance
anchor.  The old timestamped Route-A rejection remains in the repository as
an append-only record of the pre-lift state; the later record is authoritative
for this release.
