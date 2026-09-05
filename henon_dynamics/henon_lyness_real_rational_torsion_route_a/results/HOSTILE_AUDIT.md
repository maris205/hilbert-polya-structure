# Hostile evidence audit

Actual run: 38/38 attacks rejected.

31 repaired-payload-hash semantic/type cases cover unknown keys, source/epoch
drift, false-to-zero scope drift, forbidden scope promotion, Route B, A2
promotion, contract extension, missing orbits, nonpositive/unreduced/boolean
rational values, wrong recurrence/energy/Jacobian, Cartesian determinant
confusion, nonprimitive cycles, false nine-cycle return identity, boolean
identity drift, missing cycles, wrong centers, widened pi/cosine bounds,
wrong endpoint interval, denominator/prime-label type drift, unreduced
period fractions, missing denominators and summary drift.

Two actual JSON cases insert a duplicate key or NaN. Five actual YAML cases
insert an unknown field, change false to zero, unquote the evaluation date,
duplicate a field or promote a scope flag. The checker rejects all; --write
release invokes that same strict raw and semantic/type evaluation gate.
The mutations live only in temporary directories. Canonical source evidence
and evaluation files are never overwritten by the attack runner.
