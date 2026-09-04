# C364 Hostile Audit

The 47 attacks cover stale hashes; repaired candidate, evaluator,
evaluation-lock, theorem, boundary, source, collision, nonclaim, Route-A, and
scope mutations; nested extra/changed/duplicated/omitted state and cycle rows;
matrix, reversal, fixed-count, enumeration, square and imprimitive boundary
mutations; unknown top-level fields; duplicate and nonfinite JSON; and
evaluator authority, status, date, artifact type, duplicate key, anchor/alias,
non-string key, source token, and theorem-status YAML attacks.

Twelve of those attacks repair the payload hash after replacing locked JSON
leaves across provenance, firewall, state, cycle, fixed-count, enumeration,
and boundary surfaces with Python-equal values of the wrong type: false versus
0, integer 0 or 1 versus booleans, and integers versus integral floats.
Recursive type-preserving comparison rejects all twelve.

All 47 attacks are rejected. Repaired hashes do not bypass semantic
recomputation or the leaf-type contract.
