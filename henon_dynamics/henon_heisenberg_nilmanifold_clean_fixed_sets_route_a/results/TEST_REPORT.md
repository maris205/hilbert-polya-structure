# C146 test report

The producer, independent checker, SymPy reconstruction, byte replay, and
hostile mutation suite pass on the frozen evidence.  The checker passes 687
assertions, SymPy passes 87 checks, replay is byte-identical, and all 31 hostile
receipts (30 repaired-hash semantic mutations plus one stale hash) are rejected.

Validation covers all 20 ledger rows, exact lattice/group identities, the
central multiplier, stability singularity, Lefschetz cancellation, Lucas
formula, period-two counterexample, strict claim flags, Route-A tuple, and
Route-B prohibition.
