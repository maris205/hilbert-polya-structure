# Executable certificate

- `c280_jeffery_producer.py` writes canonical evidence from exact rational
  parameter conventions and 90-digit projective flows.
- `c280_jeffery_checker.py` does not import producer code.  It independently
  reconstructs every matrix, discriminant, exponential, director, tangent
  vector, shear period, strobe, boundary, lock, and scope flag, and requires
  exact key sets so duplicate/drop-replace rows cannot pass.
- `c280_jeffery_sympy_crosscheck.py` derives the Cayley–Hamilton identities,
  all exponential branches, shear reduction, nilpotent face, and tangent
  normalization exactly.
- `c280_jeffery_replay.py` regenerates evidence in a fresh path and requires
  byte equality.
- `c280_jeffery_mutation.py` repairs the hash after 24 semantic corruptions,
  including duplicate/drop-replace, a consistently recomputed off-grid
  rational parameter, and boundary/convention attacks, and adds one
  stale-hash control; all 25 must fail the independent checker.
- `c280_release_manifest.py` reruns every gate, rebuilds all PDF rounds twice,
  audits fonts/text/logs, and closes exactly 27 payloads.

No checker imports the producer, and no script downloads data or reads prime
or target-zero tables.
