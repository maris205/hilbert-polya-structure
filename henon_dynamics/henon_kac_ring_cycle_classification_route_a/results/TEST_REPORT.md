# C170 test report

Commands and expected statuses:

```text
python code/c170_kac_ring_producer.py       -> C170_PRODUCER_PASS
python code/c170_kac_ring_checker.py        -> C170_INDEPENDENT_CHECK_PASS (114056 assertions)
python code/c170_sympy_crosscheck.py        -> C170_SYMPY_PASS (221 checks)
python code/c170_replay.py                  -> C170_REPLAY_PASS
python code/c170_mutation.py                -> C170_MUTATION_PASS (17/17 rejected)
python code/c170_release_manifest.py        -> C170_MANIFEST_PASS (27 payload files)
```

The checker independently re-enumerates every marker word through \(N=10\) and recomputes configuration digests. SymPy verifies representative determinant and characteristic polynomials through \(N=12\), plus every marker word through \(N=6\). Replay regenerates evidence in a temporary directory. Mutations include repaired hashes and one stale hash.

Paper gates require pairwise distinct round hashes, `main.pdf == main_round2.pdf`, two fixed-epoch clean builds with identical bytes, embedded fonts, and no layout/reference/glyph warnings. Final details are in `paper/COMPILE_REPORT.md`.
