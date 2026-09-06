# NCC partial-boundary author replay

2026-09-06 UTC; root authored the proof and this standalone checker.
This is not an independent gate, temporal proof or admission.

The actual initial terminal invocation completed with exit zero and
102,613 assertions; its full output was in the tool result, not silently
retroactively described as the canonical file. A subsequent producer
created the canonical, followed by two fresh producers with complete
stdout/stderr in this directory. All three child processes and the three
raw `cmp` commands exited zero. Each fresh run has 1,900 stdout bytes,
empty stderr, and 102,613 assertions. Commands were run from the workspace:

```sh
python3 docs/papers204_208_sequence/scouting/word_local/verify_ncc_boundary.py
```

The canonical-producing run redirected stdout to the path below; the
following two redirected it to `run1.stdout` and `run2.stdout` here.
Comparisons were canonical/run1, canonical/run2, and run1/run2, using
unmodified raw bytes. Full boxes remain $n=1,\ldots,6$, 50,069 source
words. The test checks invariance, the exact fixed-point criterion,
every constant-target formula, the full generic histogram decoder and
the two named labelled two-cycles. It does not claim a global clock or
a uniform maximum theorem.

| Role | Workspace-relative input | SHA-256 |
|---|---|---|
| Standalone checker | `docs/papers204_208_sequence/scouting/word_local/verify_ncc_boundary.py` | `d0dfa7e211c5364459caef4b237e42235091d5a22b25b5972ed7ed4443d05165` |
| Proof boundary | `docs/papers204_208_sequence/scouting/word_local/NCC_PROOF_BOUNDARY.md` | `d1290db33eed9ef088012c3703720f0313f8a0f25198577f82ef8cce9f418010` |
| Canonical and both stdout files | `docs/papers204_208_sequence/scouting/word_local/NCC_BOUNDARY_CANONICAL.json` | `f46a87611eae893269d87b59785c2aca5cc9e498fa832344ddf526afa3851782` |

A prior read-only helper search attempted a nonexistent
`qa/replay_standalone.py` and exited 2 before any producer ran. That was
a path discovery failure, not a mathematical run or PASS. No existing
receipt, canonical, failed evidence or generic harness was rewritten.
