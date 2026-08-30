# C242 hostile audit

The mutation harness repairs the outer payload hash after each edit, then
invokes the producer-independent checker.  It rejects 29/29 mutations,
including stale and repaired hashes, wrong CZ floors, invalid square bounds,
altered multipliers/actions, changed rational resonance or degeneracy, source
and evaluator drift, route-B enablement, forbidden scope flags, unknown keys,
and identity-count drift.

This is a schema/integrity test, not external peer review and not evidence for
an arithmetic or target-zero claim.
