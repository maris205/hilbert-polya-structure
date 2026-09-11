# P197 Review B replay log

## Replay 1

From `docs/papers197_201_sequence/reviews/p197_b/`:

```
python3 -B verify_independent.py > RUN1.txt
```

A fresh process exited zero and emitted 4,833,354 assertions. Its full
output was inspected; the terminal status is
`PASS_BOUNDED_INDEPENDENT_REVIEW_B; NO_NOVELTY_CERTIFICATION`.

## Replay 2

From the same directory, after Replay 1 completed:

```
python3 -B verify_independent.py > RUN2.txt
cmp RUN1.txt RUN2.txt
```

The second fresh process exited zero with the same count. The byte
comparison returned zero. After creating `CANONICAL.txt` from the actual
observed output, both runs were byte-compared against that canonical.
All three have SHA-256
`eb91b1d2dbe7b4c95556359a234286e6806253577b0f9703b1714c66051ae512`.

The first exploratory run before these two also completed, but is not
substituted for either recorded fresh process. No author or Review-A code
was imported, and their assertion counts were not combined with this one.
These are repeatability checks, not independent experiments or a novelty
certificate. Root replay remains a separate required action.

Input pins are validated from repository root. `SHA256SUMS` covers every
top-level regular file except itself, plus `qa/SHA256SUMS`. The latter
covers every nested QA file except itself, from the QA directory. The
top-level manifest does not redundantly enumerate all nested files.
