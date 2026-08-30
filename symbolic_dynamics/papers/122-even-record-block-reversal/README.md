# P122 — Even record-block reversal

Status: **ANONYMOUS ROUND-TWO FINAL FREEZE / GO_INTERNAL / EXTERNAL HOLD**.

For a permutation, cut immediately before every left-to-right maximum and
reverse all even-length record blocks synchronously.  The paper proves three
all-size results:

1. every changed state decreases lexicographically and the maximum transient
   depth on `S_n` is exactly `n-1`;
2. every target fibre is in bijection with an explicit family of admissible
   cuts, giving a target-local dynamic program; and
3. the complete one-step image and Garden-of-Eden census is computed for every
   `n` by a weighted five-bit automaton.

Foata's record/cycle correspondence, the all-odd-cycle fixed-point count,
record-position weights, generic descent, and nearby left-to-right-maximum
preimage methods receive zero contribution credit.  A bounded owner search
found no literal-map hit; this is not a novelty or priority certificate.

Run the exact controls with:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
```

The two independent implementations make **1,637,027** exact assertions,
including exhaustive source/target comparison through `n=9` and an aggregate
transfer through `n=30`.  See `BUILD.md` for the reproducible anonymous PDF
build.  Public posting, submission, and priority language remain **HOLD**.
