# C154 source audit

## Source lock

The only source data are the substitution `0 -> 01`, `1 -> 10`, the
period-three word `234`, and their single interface at coordinates `-1,0`.
The alphabets `{0,1}` and `{2,3,4}` are disjoint.  The map is the left shift
`(sigma x)_j=x_(j+1)`, and the system is the closure of the full two-sided
orbit of the frozen interface point.  No bibliography or priority claim is
used.

## Proof boundary

Positive shifts move every fixed observation window into the Thue--Morse
tail; uniform recurrence supplies every point of the two-sided language
subshift as a subsequential limit.  Negative shifts move a fixed window into
the periodic tail, and the three residue classes modulo three give exactly
the three phases.  A bounded shift sequence is eventually constant, so these
cases exhaust the closure.  The unique cross-alphabet pair `40` isolates
each interface point and proves wandering.

The full `Z`-orbit is dense by construction, but this is deliberately not
called forward topological transitivity.  In fact `U={sigma x}` and `V={x}`
are open and `sigma^n(U)` misses `V` for all `n>=0`.  Thue--Morse
aperiodicity is reproduced with all-window certificates rather than inferred
from one seed mismatch.  Finite windows and the 60-period ledger are replay
sentinels, not theorem cutoffs.

No target/arithmetic data, natural operator, or Route-B input is used.  Scope:
`NO_BAD_EULER_OR_ROOT_NUMBER`.
