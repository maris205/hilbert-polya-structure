# Hostile audit

The suite killed **63/63** attacks.

- 39 semantic JSON attacks were repaired with fresh section and payload
  hashes before checking. They covered identity, source, normalization,
  Doob energy, boundary, spectrum, gap, owner collisions, references,
  firewall flags and boolean typing, route tuple, dimension rows, partition
  labels, exact norms, and kernel values.
- One stale-hash mutation checked that changing data without repairing its
  digest also fails.
- Duplicate-key and nonfinite-number JSON attacks fail closed.
- Twenty-one strict-YAML and publication-surface attacks covered duplicate and
  non-string keys, aliases and merge syntax, timestamp coercion, unknown
  fields, type coercion, tuple and Route-B changes, owner-token and
  normalization changes, evaluator identity/version, full source-commit
  binding, arithmetic controls, per-layer artifacts/metrics, claim boundaries,
  round-two clues, escaped-versus-literal `quad`/`qquad` controls, generic
  replacement titles, and later-round title leakage.

The checker imports no producer code. Exact combinatorics use an independent
partition recurrence, and kernel determinants use an explicit Leibniz sum.
