# Test report

Date: 2026-08-14

Command:

```bash
bash code/run_c53.sh
```

Results:

- producer: PASS;
- certificate core digest: `213f066f548f40bf4b5fc666cf709e116415e236c40de8c2afc4923c8148a9e5`;
- dependency locks recomputed: 7/7;
- independent checker: PASS;
- orbit sentinels: 4/4;
- exact packet rows checked independently: 280;
- adversarial mutations rejected: 9;
- unit tests: 11/11 PASS in 40.506 seconds;
- producer/embedding formula maximum error: below \(10^{-55}\);
- generated `__pycache__`: none.

The independent checker rejects physical-only height, doubled
half-cyclotomic coefficient, shape-one Gamma, source-typing mutation and
all continuation/determinant/operator promotions.
