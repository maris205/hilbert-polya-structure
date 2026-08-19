# C74 exact certificate code

Run from this project directory:

```bash
python3 code/c74_named_core_affine_rigidity.py
python3 code/c74_named_core_affine_rigidity_checker.py
python3 code/c74_group_crosscheck.py
python3 code/c74_named_core_affine_rigidity_replay_checker.py
python3 code/c74_mutation_test.py
```

The producer binds the C72 coordinate atlas and C73 symmetry boundary, then
enumerates all `108` automorphisms and all `5832` affine maps of
`Z/9 + Z/3 + Z/2`.  The independent checker reconstructs bijectivity from
the complete 54-point group rather than trusting the producer's unit test.
The cross-check uses an independent parameter count and verifies the two
near-symmetry witnesses.  The certificate distinguishes the 16-label
multiset, its 10-point underlying set, and the C73 16-vertex hypergraph.
