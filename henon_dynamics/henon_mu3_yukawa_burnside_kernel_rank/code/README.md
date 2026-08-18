# C63 code

`c63_kernel.py` independently reconstructs the 25-class character matrix from
the frozen C61 action and C62 stabilizer element sets.  It emits the rank,
nullity, canonical matrix, relation vectors, and source hashes.
`c63_kernel_checker.py` validates the strict prefreeze contract, while
`c63_kernel_replay_checker.py` independently rebuilds the ambient group,
conjugacy classes, subgroup representatives, and matrix from source bytes.
`c63_mutation_test.py` exercises hostile semantic mutations.  The outputs are
finite-group evidence only.
