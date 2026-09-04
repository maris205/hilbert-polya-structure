# Hostile audit: HCS-C363

All 61 attacks were rejected.  Repaired-hash mutations alter identity,
provenance, evaluator, PDE, virial theorem, collision ownership, nonclaims,
references, one cell in each evidence section, section hashes, enumeration,
Route-A status, and forbidden flags.  Omission, duplication, and nested-field
attacks cover every row family.

Parser attacks include missing/extra top-level fields, stale hashes, duplicate
and nonfinite JSON, a wrong JSON root, duplicate YAML keys, anchors, aliases,
merge keys, non-string keys, implicit dates, unknown fields, wrong scalar
types, changed source provenance, promoted A1, unlocked Route B, and a changed
artifact path.

This demonstrates fail-closed finite certification; it is not a numerical
proof of continuum well-posedness or concentration.
