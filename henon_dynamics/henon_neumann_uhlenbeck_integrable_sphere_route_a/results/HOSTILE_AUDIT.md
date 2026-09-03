# Hostile audit

The suite rejects 152/152 attacks.  It repairs the canonical evidence payload
hash after semantic mutations to identity, source commit, epoch, evaluator,
model, theorem contract, references, collision boundary, nonclaims, Route-A
tuple, scope flags, parameter grid, and every row family.  It additionally
tests the positive-$\hbar$ quantum contract and repaired mutations of the
repeated-face bracket, energy identity, differential wedge, and nested witness
schema. Further attacks cover nested extra keys, duplicate/omitted/reordered
coordinates, noncanonical rational and string-`nan` values, duplicate and
nonfinite JSON, root-type changes, and a stale-hash control.

For YAML it attacks duplicate keys, anchors, aliases, merges, non-string keys,
root type, authority changes/deletion, verdicts, evidence-status fields, Route
B, scope flags, implicit date and epoch types, unknown fields, raw whitespace,
and every semantic leaf.  Each YAML attack carries repaired raw/semantic hashes
in a correspondingly repaired evidence artifact, so rejection cannot be
attributed merely to a stale outer digest.
