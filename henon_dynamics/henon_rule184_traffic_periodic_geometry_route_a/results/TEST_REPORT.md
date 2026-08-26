# C175 test report

Commands and required terminal statuses:

```text
python code/c175_rule184_producer.py       -> C175_PRODUCER_PASS
python code/c175_rule184_checker.py        -> C175_INDEPENDENT_CHECK_PASS (34,545 assertions)
python code/c175_sympy_crosscheck.py       -> C175_SYMPY_PASS (25,563 checks)
python code/c175_replay.py                 -> C175_REPLAY_PASS
python code/c175_mutation.py               -> C175_MUTATION_PASS (17/17 rejected)
python code/c175_release_manifest.py       -> C175_MANIFEST_PASS (27 payload files)
```

The producer uses the polynomial local rule, while the checker independently enumerates moving particles and dynamically detects initial-cycle membership. SymPy recomputes cyclic-independent-set counts, Möbius inversion, product coefficients and gap conservation. Replay compares fresh bytes. Sixteen semantic mutations repair the payload hash; one additional mutation leaves it stale.

Paper release gates require pairwise distinct round PDF hashes, `main.pdf == main_round2.pdf`, two clean fixed-epoch builds with identical bytes, embedded fonts, no warning or bad-box/glyph issue, and visual snapshots of every page. See `paper/COMPILE_REPORT.md`.
