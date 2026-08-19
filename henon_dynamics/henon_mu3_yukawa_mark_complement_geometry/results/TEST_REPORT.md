# C71 test report

```text
producer: PREFREEZE_G3_PASS
independent Birkhoff/duality checker: PASS
GAP/SymPy group-lattice cross-check: GROUP_LATTICE_CROSSCHECK_PASS
clean-process replay: REPLAY_PASS
hostile mutation test: PASS, 42/42 mutations rejected
```

The producer enumerates the 38 concrete subgroups of `D` and performs strict
subgroup-poset inversion.  The checker instead multiplies Birkhoff subgroup
counts in `D` by independent epimorphism counts from `K`.  GAP reproduces all
38 subgroups in 10 types.  SymPy independently reconstructs `8C`, its order
and index, all sixteen named orders, and all 25 generating triples.
