# C337 hostile audit

The mutation lane repairs the outer evidence payload hash after semantic mutations.  For YAML attacks it also repairs both nested raw and semantic evaluation hashes before repairing the outer hash.  Rejection therefore cannot be attributed merely to a stale carrier digest.

The 133 attacks include:

- duplicate, nonfinite and non-object JSON;
- missing and unowned evidence fields, including nested row fields;
- theorem, parity, Bessel phase, moment, boundary, reference, collision and enumeration changes;
- scope escalation, target-zero claims, Route-A acceptance and Route-B authorization;
- YAML duplicate keys, merge keys, anchors, aliases, non-string keys, timestamp/type changes and unknown fields;
- deletion and rewriting of evaluator authority and `evidence_status`;
- one repaired-hash mutation for every one of the 70 scalar/list leaves in the evaluator YAML.

Result: 133/133 rejected by the producer-independent checker.  This demonstrates exact raw/semantic evaluator locking and owned-field validation; it does not prove the analytic theorem, which is closed in `THEOREM_PACKAGE.md`.
