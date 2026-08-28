# P95 — Minimal-slack no-repeat shifts

Status: **mechanically sealed internal Stage 2 GO / external HOLD**.

For `q >= 3`, this note studies the `q`-color shift in which a color cannot
repeat within the next `q-2` sites.  The concrete advance is a three-part
exact theorem package:

1. using the known Ruskey--Williams Cayley graph as an explicitly cited
   presentation, the no-repeat shift is mixing with entropy `log 2` and
   uniform Parry measure;
2. its initial periodic ledger consists of two `q!` islands at periods
   `q-1` and `q`, separated from all shorter and immediately later periods
   by exact zeros; and
3. the first return of one color under the Parry measure is
   `(q-2)+Geom(1/2)`, giving conditional return generating function
   `(2-z)/(2-z-z^(q-1))`.

Run the exact control with:

```bash
python3 code/verify_no_repeat.py
```

Build the manuscript with the four-stage command in [BUILD.md](BUILD.md).
The two hostile-review passes are recorded in `HOSTILE_REVIEW.md`; the final
log, font, extracted-text, and page-render checks are recorded in
`FINAL_QA.md`. The sealed package manifest verifies with
`sha256sum -c SHA256SUMS`.

No public release, submission, author contact, or priority claim is
authorized.
