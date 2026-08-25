# HCS-C149: finite periodic skeleton attached to Thue--Morse

This package forms the compact disjoint union of the aperiodic minimal
Thue--Morse component and four tagged cycles of lengths `1,2,3,5`.  It proves
the all-period fixed-count formula, the exact primitive skeleton, and

```text
zeta_Y(z)=1/((1-z)(1-z^2)(1-z^3)(1-z^5)).
```

The construction makes periodic content nonempty at a precise structural
cost: every nonempty finite disjoint attachment destroys minimality.  It is
not called almost minimal and is not an intrinsic repair inside the
Thue--Morse subshift.  The strict verdict is
`(A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`, overall `ROUTE_A_REJECTED`.

Run the six scripts in `code/` in producer, checker, SymPy, replay, mutation,
manifest order.  Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`;
`route_b_invocation_allowed=false`.
