# Hostile audit

The final suite rejects 80 of 80 attacks. It contains:

- repaired-payload mutations of identifiers, date, source commit, scope,
  evaluator authority, YAML path, model convention, theorem clauses including
  zero reverse exogenous rates, visible-only jump reversal, phantom
  self-routing exclusion, and the invariant-probability lemma,
  collision boundary, nonclaims, source ownership, Route-A tuple, Route B,
  scope flags, representative network/balance/reversal/boundary cells, and the
  finite-evidence role;
- nested extra-key, omitted-row, and duplicated-row attacks on all five ledger
  sections;
- missing and unknown top-level evidence fields;
- stale-hash control, duplicate-key JSON, nonfinite JSON, and non-object JSON;
- duplicate YAML keys, anchors, aliases, merge keys, non-string keys, implicit
  timestamps, unknown fields, wrong scalar types, altered authority/source/
  artifact/evidence-role/source-token/theorem/Route-B fields, and non-mapping
  YAML;
- repaired evidence bindings for semantically modified YAML.

Each attack runs the independent checker in a temporary directory. A surviving
attack fails the mutation lane immediately. The unmodified evidence and YAML
remain unchanged.
