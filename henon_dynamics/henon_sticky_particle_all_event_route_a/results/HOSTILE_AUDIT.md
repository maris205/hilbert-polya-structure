# Hostile audit

All 66 specimens were rejected.  The 45 evidence-JSON specimens cover stale payload hashes;
repaired-hash theorem, proof, and energy mutations; raw duplicate top-level
and nested keys; raw `NaN`; non-object roots; extra and missing keys; row
duplication/drop; bool/int confusion in counts and member arrays;
noncanonical `1/1`; malformed route and scope values; and corrupted
premerge, event, projection, conservation, weak-balance, reference, and
nonclaim layers.

The other 21 evaluation-YAML attacks cover raw duplicate top/nested keys,
unknown/missing top or nested keys, date-preserving exact types, source and
evaluator locks, tuple/overall/Route-B changes, scope literal and flags, axis
values/keys, theorem status, and a non-object root.  The canonical parsed
semantic hash is locked after duplicate-rejecting safe loading.

The independent checker contains no producer import.  It reconstructs
weighted isotonic states by exhaustive enumeration of every contiguous
partition and discovers active events through block-line intersections.  The
analytic arbitrary-finite theorem remains in the manuscript; the receipt is
not promoted into a proof.
