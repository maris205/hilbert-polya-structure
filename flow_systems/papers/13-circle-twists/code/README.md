# Paper 13 deterministic controls

This directory contains the frozen v2 control implementation.

- `generate_controls.py` generates into an explicitly supplied, existing,
  empty directory or verifies a package strictly read-only with
  `--verify-only`.  Candidate CSVs are parsed and checked by their semantic
  family validators before final byte identity, and the manifest is checked
  recursively for proof binding, self-hash, authority, and inventory drift.
- `test_controls.py` exposes exactly 176 independently discoverable
  `unittest` methods and runs the frozen schema, arithmetic, owner, manifest,
  reproduction, isolated mutation, verify-only write-guard, and cleanup
  checks.  Its write-free `--static-precheck` mode verifies all twelve locked
  CSV hashes and the in-memory mutation registry before a serialized run.

All arithmetic used as an oracle is integral.  These controls are finite
diagnostics and policy ledgers; they are not proof evidence for continuum
cardinality, arbitrary-index multiplier identities, completion norm chains,
or corona faithfulness.
