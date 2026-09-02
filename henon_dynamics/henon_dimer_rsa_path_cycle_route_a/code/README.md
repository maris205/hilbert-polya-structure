# Code map

- `c291_dimer_rsa_producer.py` constructs canonical exact evidence from the
  first-edge convolution and rational moment recurrences.
- `c291_dimer_rsa_checker.py` is producer-independent.  It uses strict
  duplicate-rejecting JSON and recursive duplicate-rejecting safe YAML, exact
  top/nested schemas, primitive types, frozen values and semantic hashes,
  aggregated enumeration of every labeled edge order through two bitmasks,
  and a separate all-order factorial-moment reconstruction.  `C291_EVIDENCE`
  and `C291_YAML` can redirect hostile-test inputs.
- `c291_dimer_rsa_sympy_crosscheck.py` checks the Riccati, `H_1`, `H_2`, pole
  algebra, finite coefficients, and support shifts symbolically.
- `c291_dimer_rsa_replay.py` rebuilds evidence from two unrelated temporary
  package paths and compares bytes.
- `c291_dimer_rsa_mutation.py` repairs hashes after JSON schema/semantic
  attacks and also tests stale hashes, nonstandard constants, YAML
  schema/type/value changes, and raw top-level/nested duplicate keys.
- `c291_release_manifest.py` reruns every lane, rebuilds each PDF round twice,
  audits logs/fonts/text/layout contracts, and writes the self-excluded exact
  release ledger.

All executable arithmetic is deterministic.  The direct finite order oracle
covers `P_0,...,P_10` and `C_3,...,C_9`; exact factorial rows extend through
`P_20`, while first/second moment recurrence controls extend through `P_200`.
Those windows are tests, not the proof of the all-size theorem.
