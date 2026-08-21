# C80 results

Canonical evidence SHA-256:
`8d27428b14dbd7354e9c8308ad76b1108e3f551702165833301509cd52de7df5`.

The 20 target distributions (in row order) are recorded in the JSON receipt.
The final target `Q` has

```text
tau_Q: 0 -> 30400, 1 -> 32704, 2 -> 2368, 3 -> 64.
```

The first two target rows are respectively constant zero (the trivial target)
and a balanced one-bit threshold (`32768/32768`).  Every deleted-cardinality
row sums to `binom(16,k)`, and every target has threshold zero on the full
support.  Target inclusion monotonicity holds for all 65536 profiles.

The receipt's profile rows are ordered by retained mask and include both the
retained and complementary deletion mask, making replay byte-independent of
implicit ordering conventions.
