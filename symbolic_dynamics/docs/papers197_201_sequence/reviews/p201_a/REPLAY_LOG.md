# P201 Review A replay receipt

Working directory: repository root. Two fresh sequential processes:

```
python3 -B docs/papers197_201_sequence/reviews/p201_a/verify_independent.py > docs/papers197_201_sequence/reviews/p201_a/RUN1.txt
python3 -B docs/papers197_201_sequence/reviews/p201_a/verify_independent.py > docs/papers197_201_sequence/reviews/p201_a/RUN2.txt
cmp docs/papers197_201_sequence/reviews/p201_a/RUN1.txt docs/papers197_201_sequence/reviews/p201_a/RUN2.txt
```

Both exited successfully and cmp returned zero. Each contains 9,726,250
assertions, with the terminal status
`PASS_MATHEMATICS_AND_EXACT_OCL_COLLISION; P201_ADMISSION_CRITICAL_NOT_REVIEW_PASS`.
Their SHA-256 is
`03871403c941ec90416e00f385d072f6a11b4797ced225ba6c5fe4de1014fbe0`.
`CANONICAL.txt` is an exact copy of this observed transcript, subsequently
byte-compared to both runs. The earlier `INITIAL_MATH_RUN.txt` is retained
as provenance from before the historical conjugacy checks were added; it is
not the canonical or a substitute for either current-code replay.

Input pins are root-relative. Top-level and QA manifests exclude themselves
and are checked from their respective directories. These receipts establish
bounded execution reproducibility, not originality or admissibility.
