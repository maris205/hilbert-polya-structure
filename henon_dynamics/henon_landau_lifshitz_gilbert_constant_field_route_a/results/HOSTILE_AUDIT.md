# Hostile-audit checklist

The release gate must reject every altered flow cell, pole eigenvalue,
sampled-set label, theorem fragment, route verdict, scope flag, citation,
unknown key, stale hash, row-count mutation and missing-row mutation.  All
five boundary rows are locked field-by-field (condition, flow, energy and
fixed-set semantics), including repaired-payload-hash cases.  The corrected
Lakshmanan DOI is likewise tested both with a stale and a repaired hash.  The
successful audit is `PASS 37/37` and is never used to promote a Route-A claim.
