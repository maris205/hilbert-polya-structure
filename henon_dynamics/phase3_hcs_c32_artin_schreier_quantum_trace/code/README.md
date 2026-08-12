# Phase-3 exact code

The code uses only the Python standard library and exact arithmetic over prime
fields.

## Components

- `c32_morse_gate_producer.py`: registered state scan, exact Hénon/Hessian/Hill
  records, and deterministic construction of the Hessian-congruence matrix;
- `c32_morse_gate_checker.py`: fail-closed independent replay using permutation
  cycles and recursive determinants;
- `test_c32_morse_gate.py`: deterministic, regression, type-confusion, and
  re-signed semantic mutation tests;
- `c32_hash_manifest.py`: fail-closed release inventory and SHA-256 verifier;
- `run_c32_phase3.sh`: read-only release replay against frozen result files.

The producer is not an independent verifier.  A certificate is released only
with the checker report and a passing mutation suite.

## Reproduction

From the Phase-3 directory:

~~~bash
./code/run_c32_phase3.sh
~~~

During explicit release preparation, generate the certificate and checker
report into `results/`, refresh the hash manifest, and then rerun the default
read-only command.

~~~bash
./code/run_c32_phase3.sh --refresh-manifest
./code/run_c32_phase3.sh
~~~
