# P199 Review A replay receipt

Two fresh saved executions on 2026-09-05 UTC:

```text
python3 -u docs/papers197_201_sequence/reviews/p199_a/verify_word_orbits.py
```

Both exited zero. Their complete stdout files, first captured separately
in `/tmp/p199-review-a.4kMTHt/reviewer_run1.txt` and `reviewer_run2.txt`,
were compared with cmp and agreed byte for byte; copied evidence is in
qa/. Both equal CANONICAL.txt. An earlier development run also passed,
but it is not counted as either of these two saved fresh replays.

Verifier SHA-256:
`e8e423c20ee66ea5e90f1b8f0463416b49c128c3f3d13e4b40cf43a7eab19ba3`.
Canonical and each saved stdout SHA-256:
`b302b308a27c506b0a5d030a8f59612cc6a9afe2f57f9b5938172b64a3e30851`.
Per run: 146,600 sources, 146,600 targets, 1,926,465 assertions.

A separate fresh execution of frozen Round0 `code/verify.py` exited zero
and its stdout matched the author's canonical byte for byte:
`0b9a1f131984c427db95d8443470a280129b4863b4f92e817e484f99fc13c0ff`,
1,496,779 assertions. This is author replay, not an independent reviewer
implementation or an additional review. Its stdout is preserved in qa/.

PINNED_INPUTS.sha256 paths are relative to the research workspace root.
SHA256SUMS paths are relative to this review directory; it excludes
itself and covers all top-level review files plus the qa/ submanifest.
The qa/ manifest separately covers its generated logs and images and
also excludes itself. No manifest claims self-hashing.
