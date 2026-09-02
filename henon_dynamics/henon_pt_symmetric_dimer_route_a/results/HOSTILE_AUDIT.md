# Hostile integrity audit — C297

All 52 attacks were rejected: 36 evidence-JSON attacks and 16
evaluation-YAML attacks.  Direct evidence and evaluation mutations of the
frozen obstruction ID `HEN-O281` are included.

The JSON suite includes a stale-hash control; repaired-hash changes to the
model, theorem, proof, phase, metric signature, period type, Route-A tuple,
Route-B permission, and scope flags; missing/unknown/duplicate cells; wrong
primitive types; bad references; duplicate raw keys; non-finite constants;
and a non-object top level.

The source-owner boundary is now value-locked rather than pattern-checked:
integer titles, list-valued ownership, and individually substituted fake DOI
identifiers or URLs are rejected.  The Route-B boolean also rejects integer
zero rather than relying on Python's `False == 0` equality.

The complete canonical nonclaim list is recursively type/value locked, and a
repaired-hash attempt to assert target Euler factors and root numbers is
rejected.  All eight boundary cells are likewise exact-tree locked, including
their explanatory text; a forged Hermitian-axis result is rejected.

The YAML suite includes duplicate top and nested keys, unknown and missing
keys, boolean/integer type substitutions, Route-B and scope escalation,
tuple/axis changes, a non-string key, anchor, alias, merge, and top-array
attacks.  The loader keeps the quoted date as a string and refuses every
implicit graph-sharing mechanism.

The audit caught and repaired one derivation-level sign error before release:
the complex Riccati quadratic has discriminant `-4 delta`, not `+4 delta`.
The matrix characteristic discriminant remains `+4 delta`.  Both are now
separately asserted.
