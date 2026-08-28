# Hostile audit

The mutation harness copies the receipt to a temporary directory and never
edits the canonical evidence.  It changes source/evaluator locks, the equation
and profile values, residuals, mass/VK data, eigenvalues and threshold,
factorization values, the Pöschl–Teller citation claim, route tuple, scope flags
and summary counts.  Each semantic mutation is rehashed before invoking the
producer-independent checker, so a passing hash cannot hide a changed theorem
or provenance claim.

An unknown root key is rejected by the recursive schema, and a stale-hash
mutation is rejected by the canonical payload check.  No mutation is accepted:
16 repaired-hash/unknown-key rejections and one stale-hash rejection, 17 total.
