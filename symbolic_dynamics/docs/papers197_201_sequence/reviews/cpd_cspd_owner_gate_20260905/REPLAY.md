# Independent transfer replay

2026-09-05 UTC. Initial run and two fresh post-canonical runs PASS.

```
for run in 1 2; do
  python docs/papers197_201_sequence/reviews/cpd_cspd_owner_gate_20260905/verify_owner_transfer.py |
    cmp - docs/papers197_201_sequence/reviews/cpd_cspd_owner_gate_20260905/CANONICAL.txt
done
```

Each run: 50,069 sources, 3,996 site targets, 140,348 assertions.
Canonical SHA256: `e962713da80dc9b9d550fb98a13ce1ea52c392a2a005f7e4547f517486d42ea1`.
Code SHA256: `46bc277a05d8aeb78d0dc7014877c4be2ec29f0bd2ce683cf41ff3f1881da4b4`.
The first attempted replay wrapper had a Python syntax error before running any control; corrected shell pipelines both passed. No computation failure or theorem repair was hidden.

Primary ICERM PDF was fetched to temporary local storage at
`/tmp/cpd_owner.gkMnoB/fixed_displacement.pdf`; SHA256
`5931201af6bc6516e402253632269501ffa13d1f173514c5f9614e25f837e8f8`.
This 27 MB primary document is not checked into the review package. Its URL and exact inspected page scope are in the gate. Its temporary path is intentionally excluded from portable input-pin verification.
