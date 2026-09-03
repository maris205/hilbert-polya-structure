# C320 hostile audit

Fourteen evidence mutations attack source identity, scope, verdict,
series order, theta2 constant, the E2 bridge, a nontrivial theta coefficient,
an ODE residual, numerical theta and `S` data, a reciprocal collision, an
axis equilibrium, and the audited count.  Each is tried with stale and
adversarially repaired payload digests.

Ten YAML attacks cover identity, verdict, Route-B authorization, scope,
duplicate and non-string keys, an unknown key, a missing required key, an
unquoted timestamp-like scalar, and anchors/aliases.  The parser forbids
merges, aliases, duplicate/non-string keys, and implicit timestamps.  All
Three additional repaired-digest attacks target a nested extra field, a
duplicate coordinate, and formerly unowned nonclaim content.  All 44
attacks are rejected; a repaired-digest `nan` attack separately verifies
that complex decimals are canonical finite strings, bringing the total to
46.  Date, canonical-rational, enumeration-schema, evaluator-authority, and
evidence-to-YAML lock mutations raise the final total to 56/56 rejected.
