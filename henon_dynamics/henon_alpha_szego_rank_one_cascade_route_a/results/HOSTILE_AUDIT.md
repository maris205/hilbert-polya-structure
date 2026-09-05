# Hostile audit: 31/31 actual rejections
Every semantic JSON mutation repairs payload_sha256 before invoking the independent checker. These rejections therefore do not rely on stale hashes.

26 semantic attacks: d, Q, M, energy, defect, d_dot, d_ddot, kappa_squared, compact_lower_bound, alpha, b, c, p, velocity, d_star, native_determinant_coefficients, regime, rank-zero-threshold, bool-to-zero, count, dropped row, extra row field, scope flag, Route-B authorization, same-determinant control and source baseline.

2 malformed-document attacks: duplicate JSON key and nonfinite JSON.

3 actual release-write attacks: unknown YAML key, claims_root_number false replaced by integer zero, and removal of evaluation-date quotes. Each attack runs the copied release entry point with --write in a fresh isolated minimal tree, fails with evaluation changed, and creates no manifest.

The independent YAML reader also rejects aliases, anchors, merge keys and duplicate/nonstring keys. Its frozen raw SHA lock precedes write and nonwrite release modes, so semantic equivalence cannot bypass source-byte/type scope.
