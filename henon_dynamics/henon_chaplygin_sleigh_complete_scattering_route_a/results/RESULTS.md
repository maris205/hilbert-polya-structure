# C199 results

The executable ledger contains six rational parameter families, both signs of
offset and angular velocity, 12 heteroclinic cases, 36 high-precision states,
and four zero-offset recurrence/straight-line boundaries.  The independent
checker closes 737 assertions; the separate SymPy path closes 61 identities.
Replay is byte exact.  Twelve repaired-hash attacks (including unknown-key and
mathematical attacks) and one stale-hash attack are rejected.

These finite checks audit formulas and conventions; the continuous theorem is
proved symbolically.  Strict result:

```text
(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)
ROUTE_A_REJECTED; route_b_invocation_allowed=false
```
