# Exact control results — P97

Command:

```text
python3 code/verify_sumset_squaring.py
```

Result on 2026-08-29 UTC:

```text
sumset-squaring exact control: PASS
assertions=91509
literal_subsets=10403
literal_ordered_pairs=17139
iterate_identity_cases=[(3, 5, 42), (5, 5, 186), (7, 4, 635)]
pairwise_cd_vosper=[(3, 49, 0), (5, 961, 50), (7, 16129, 882)]
self_vosper_critical={11: 220, 13: 390}
phase p=3 ord2=2 fixed_1..2h=[2, 4, 2, 4] layer_max={2: 1, 3: 0} recurrent_cycles={1: 2, 2: 1}
phase p=5 ord2=4 fixed_1..2h=[2, 2, 2, 6, 2, 2, 2, 6] layer_max={2: 2, 3: 1, 4: 1, 5: 0} recurrent_cycles={1: 2, 4: 1}
phase p=7 ord2=3 fixed_1..2h=[2, 2, 8, 2, 2, 8] layer_max={2: 3, 3: 2, 4: 1, 5: 1, 6: 1, 7: 0} recurrent_cycles={1: 2, 3: 2}
phase p=11 ord2=10 fixed_1..2h=[2, 2, 2, 2, 2, 2, 2, 2, 2, 12, 2, 2, 2, 2, 2, 2, 2, 2, 2, 12] layer_max={2: 4, 3: 3, 4: 2, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 0} recurrent_cycles={1: 2, 10: 1}
phase p=13 ord2=12 fixed_1..2h=[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 14, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 14] layer_max={2: 4, 3: 3, 4: 2, 5: 2, 6: 2, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 0} recurrent_cycles={1: 2, 12: 1}
ap_extremizer_cases=266 prime_orders=[(3, 2), (5, 4), (7, 3), (11, 10), (13, 12), (17, 8), (19, 18), (23, 11), (29, 28), (31, 5), (37, 36), (41, 20), (43, 14)]
endpoint_p2 fixed_1..4=[2, 2, 2, 2] recurrent_points=2
```

The assertion ledger covers:

- separately constructed routes to every registered iterate;
- literal Cauchy–Davenport and safe-range Vosper checks;
- complete functional graphs for five primes;
- all registered fixed counts and recurrent cycle histograms;
- exact reconstruction of registered logarithmic zeta coefficients from the
  cycle product;
- every cardinality-layer maximum in the full enumerations;
- arithmetic-progression extremizers on 266 layers;
- Möbius temporal divisibility, nonnegativity, and reconstruction; and
- strict checks of the empty-set and `p=2` endpoints.

All evidence-bearing operations use integer and finite-set arithmetic.  No
random seed, floating-point theorem check, symbolic simplifier, or
optimization solver enters an assertion.
