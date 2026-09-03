# Hostile audit

The mutation lane performs 140 attacks.  For semantic JSON attacks it repairs
the canonical payload hash before invoking the checker, so rejection cannot
be attributed to a stale outer digest.

Covered attacks include:

- candidate, obstruction, source commit, scope, evaluator authority/version/
  digest, and both nested evaluation digests;
- edge-law, update-sign, parameter-domain, theorem, tail-domain, source,
  collision, nonclaim, Route-A tuple, overall verdict, Route-B, and scope-flag
  changes;
- spectral rates, multiplicities, low-dimensional block presence, projector
  entries, exhaustive means/second moments/energy, endpoint semantics, and
  enumeration counts;
- extra and missing owned fields;
- duplicate-key, nonfinite, and non-object JSON;
- duplicate-key, anchor/alias, merge, non-string key, implicit timestamp,
  unknown-field, type, whitespace, source, authority, `evidence_status`, A4,
  Route-B, and scope-flag YAML attacks.
- a repaired-hash attack on every scalar or list leaf of the evaluator record:
  each mutation rewrites the YAML, then repairs the nested raw digest, nested
  semantic digest, and outer evidence-payload digest before checking rejection.

All 140 are rejected.  In particular, deleting the nonzero-disagreement domain
of the normalized tail inequality, changing `A4_FORMAL_HINT` to
`A4_ROUTE_B_READY`, or deleting/rewriting an `evidence_status` cannot survive.
