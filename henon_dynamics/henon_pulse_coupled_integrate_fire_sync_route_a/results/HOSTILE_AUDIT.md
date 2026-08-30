# Hostile mutation audit

`c245_pulse_if_mutation.py` applies 41 no-op-guarded edits to event states,
simultaneous avalanche waves, pairwise old-block containment, cluster partitions and counts, cycle labels, parameter
grids, theorem/identity/citation metadata, source/evaluator locks, epoch,
scope flags, Route-A tuple, and unknown keys.  Recomputing the payload hash
does not make a semantic mutation acceptable: the independent checker rejects
all 41/41.  One stale-hash case is also rejected before semantic comparison.
