# Hostile audit

All 87 attacks were rejected: 62 evidence-JSON attacks and 25 evaluation-YAML attacks.

The JSON suite includes stale payload hashes; unknown/missing keys; source, epoch, evaluator, scope, theorem, proof, Route-A, flag, enumeration, formula, turning-point, orbit-class, boundary, reference, and nonclaim changes; exact-type confusions such as booleans for integers; noncanonical rationals; duplicate/drop rows; duplicate top and nested raw keys; `NaN`; and a top-level array.  The complete canonical boundary, reference, and nonclaim trees are recursively locked by both type and value; attacks forge every class of bibliographic field, a boundary statement, and an affirmative target Euler/root-number claim.  Semantic attacks repair the self-excluding payload hash before validation, so rejection cannot be credited merely to a stale checksum.

The YAML suite includes duplicate top/nested keys, unknown/missing keys, scalar type confusion, source/evaluator/scope/tuple/verdict/Route-B/axis/artifact/owner changes, anchors, aliases, merge keys, and a top-level array.  The canonical evaluation semantic hash is locked after duplicate-safe parsing.

High-value mathematical attacks explicitly target the circular energy domain, action coefficients, apsidal formula, resonance label, primitive radial-cycle type, escape boundary, and the distinction between false scope flags and integer zero.  None escaped.
