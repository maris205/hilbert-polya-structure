# C129 code

- `c129_phase_producer.py`: exact `Q[Z/5]` evidence, orbit ledger, traces,
  coefficients, and controls.
- `c129_phase_checker.py`: independent standard-library reconstruction; it
  imports no producer code.
- `c129_sympy_crosscheck.py`: independent symbolic matrices, group-ring
  reduction, finite sections, and cycle solves.
- `c129_replay.py`: byte-for-byte producer replay.
- `c129_mutation.py`: 35 repaired-claim-hash hostile mutations, including both
  alternate-translation and trivial-character controls, the operator and
  trace-formula headlines, the complete progress record, and schema-addition
  attempts.
- `c129_release_manifest.py`: 27-payload content-addressed release ledger.

All scripts use exact arithmetic. No network access or external dataset is
required.
