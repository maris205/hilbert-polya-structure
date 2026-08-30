# Hostile mutation audit

`c240_contracted_rotation_mutation.py` generates 33 semantic and contract
mutations, recalculates the receipt hash for every repaired mutation, and sends
each one through the independent checker.  The edits cover word identity and
length, carry/rotation/derivative values, affine return states, lower and upper
interval endpoints and closure flags, equality audits, grouped components,
direct suffixes and residuals, counts, source/evaluator locks, fixed epoch,
scope firewall, Route-A tuple and target-match boundary, theorem overclaims,
and unknown top-level keys.

The expected result is `PASS 33/33`: no changed receipt is accepted.  In
particular, a boundary equality cannot be relabelled as an interior point, a
word-certified component cannot be relabelled maximal, and a source-local
factor cannot be relabelled a target determinant.
