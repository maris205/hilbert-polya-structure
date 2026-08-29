# Hostile mutation audit

`c235_rps_mutation.py` constructs 25 mutations.  They cover stale and repaired
payload hashes, altered turning roots/periods/product levels, parameter and
row counts, mutation states and derivatives, contraction and tangent rows,
source/evaluator/scope locks, Route-A flags, unknown top-level/nested keys,
and citation/nonclaim closure.  Every mutant is rejected by the independent
checker: `PASS 25/25`.  The added semantic mutation removes the required
`a>0` hypothesis from the conservative-period theorem and is rejected after
repairing the payload hash.

The repaired-hash cases are important: rejection is based on independently
recomputed mathematics and schema closure, not only on a stale digest.
