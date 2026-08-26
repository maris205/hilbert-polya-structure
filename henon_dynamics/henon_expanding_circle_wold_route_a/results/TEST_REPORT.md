# C177 test report

Commands and terminal statuses:

```text
python code/c177_expanding_circle_producer.py -> C177_PRODUCER_PASS (132, 1595, 352 rows)
python code/c177_expanding_circle_checker.py  -> C177_INDEPENDENT_CHECK_PASS (3980 assertions)
python code/c177_sympy_crosscheck.py          -> C177_SYMPY_PASS (3927 checks)
python code/c177_replay.py                    -> C177_REPLAY_PASS
python code/c177_mutation.py                  -> C177_MUTATION_PASS (19/19 rejected)
python code/c177_release_manifest.py          -> C177_MANIFEST_PASS (27 payload files)
```

The producer and checker share no implementation imports. The checker independently reconstructs Möbius counts, Wold roots/levels, adjoint images, and sharp correlation denominators. SymPy checks zeta logarithms and source algebra. Replay compares canonical bytes. Mutation testing repairs hashes for 18 semantic corruptions and separately tests one stale hash.

Paper gates: three pairwise-distinct round hashes; `main.pdf == main_round2.pdf`; two fresh fixed-epoch final builds byte-identical; all fonts embedded/subset; no warning, layout, glyph, reference, citation, or rerun diagnostic; both rendered pages visually inspected.
