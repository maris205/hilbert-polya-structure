# C169 test report

Commands and expected terminal statuses:

```text
python code/c169_skew_shift_producer.py       -> C169_PRODUCER_PASS
python code/c169_skew_shift_checker.py        -> C169_INDEPENDENT_CHECK_PASS (1574 assertions)
python code/c169_sympy_crosscheck.py          -> C169_SYMPY_PASS (940 checks)
python code/c169_replay.py                    -> C169_REPLAY_PASS
python code/c169_mutation.py                  -> C169_MUTATION_PASS (17/17 rejected)
python code/c169_release_manifest.py          -> C169_MANIFEST_PASS (27 payload files)
```

The producer and checker share no implementation imports. SymPy recomposes the affine iterates and reversal independently. Replay compares bytes from a temporary output. Mutation testing repairs the payload hash for 16 semantic mutations and also tests one stale hash.

Paper release gates require pairwise distinct round PDF hashes, `main.pdf == main_round2.pdf`, two clean fixed-epoch builds with identical final bytes, embedded fonts, and no overfull/underfull, undefined-reference, rerun, or missing-glyph warnings. See `paper/COMPILE_REPORT.md` for final hashes.
