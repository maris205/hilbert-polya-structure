# Hostile mutation audit

The same independent checker is run against twelve temporary altered receipts.
All must fail:

1. parameter mutation;
2. forward-pole divisor mutation;
3. inverse-composition mutation;
4. Jacobian determinant mutation;
5. first-integral formula mutation;
6. invariance remainder mutation;
7. real fixed-count mutation;
8. complex fixed-domain mutation;
9. promotion of a pole root to a valid root;
10. period-two point mutation;
11. monodromy trace mutation;
12. inflation of `A2_FAIL` to a certified-transfer label.

Observed result: `C115_MUTATION_PASS 12/12`.
