# C88 hostile mutation audit

All `40/40` semantic mutations are rejected by the independently rebuilt
expected receipt.  The audit covers schema, status, scope, all six predecessor
hashes, definitions, model dimensions, coordinate binding, target identity
and order, attainable times, minimal supports, hit bitsets and hashes,
hit/nonhit counts, reduced CDF and survival probabilities, pivotal totals and
patterns, first-passage counts and probabilities, survival counts,
expectations, inclusion and cover data, monotonicity flags, the C83 top-row
binding, exhaustive-check flags, and a prohibited claim flag.

Each mutation is canonical JSON and crosses the same semantic validation
boundary used for the frozen evidence.  Rejection therefore tests content,
not merely malformed serialization.
