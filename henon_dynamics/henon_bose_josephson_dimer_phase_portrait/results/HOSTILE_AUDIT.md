# C243 hostile audit

The mutation harness repairs the payload hash after each edit and then runs
the independent checker.  It rejects 28/28 mutations: altered fixed-point
stability/frequency or matrices, pole vectors, quartic roots and periods,
crossing/self-trapped/separatrix labels, the pitchfork critical-level claim,
source/evaluator locks, route-B enablement, forbidden scope flags, unknown
keys, and theorem/identity drift.

This is an integrity/schema test, not external peer review and not evidence
for an arithmetic or target-zero claim.
