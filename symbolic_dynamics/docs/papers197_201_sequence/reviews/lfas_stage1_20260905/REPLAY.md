# LFAS independent Stage-1 replay receipt

2026-09-05 UTC. The initial complete run passed; after canonical freeze,
two fresh subprocess runs matched it byte for byte.

```
for run in 1 2; do
  python docs/papers197_201_sequence/reviews/lfas_stage1_20260905/verify_independent.py |
    cmp - docs/papers197_201_sequence/reviews/lfas_stage1_20260905/CANONICAL.txt
done
```

Control code SHA256:
`e110cdd18f717f104c55c0174fd5ec9d2b4f5b2ccc5357b82976f86be3bf0774`.
Canonical transcript SHA256:
`d1c0119a74fccecf1f3721c01e24d8a7d6f251b680cdb4ed287bf4e8a459c197`.

Each run covers 13 complete boxes / 273,040 source states and 38 wide
witnesses, with 3,595,488 assertions. Each target is checked against its
complete brute incoming source set, including targets with zero sources.
Graph peeling independently identifies recurrent states and depths.
The author verifier was inspected but not imported or used to generate the
reviewer's expectations. This receipt is for the independent verifier,
not a replay claim about the author's frozen transcript.
