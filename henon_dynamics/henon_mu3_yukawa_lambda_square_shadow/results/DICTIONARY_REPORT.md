# C62 fixed-field dictionary report

The G4 producer groups the complete C62 stabilizer element sets by ambient
`W(E_6)` conjugacy. The resulting dictionary has 16 type labels. The labels
are attached to explicit subgroup conjugacy classes, not to a hash, an
orbit-table position, or a stabilizer order alone.

Structural checks passed:

- every recorded core is trivial;
- every field degree satisfies `degree = 51840 / |S|`;
- plus and minus type sets differ for both the exterior-square and
  symmetric-square atlases;
- several stabilizer orders split into multiple type labels, demonstrating
  that subgroup order is not a sufficient field identifier.

The output remains `PREFREEZE_G4_PASS`. It is a fixed-field dictionary for
the finite permutation actions and does not claim arithmetic field resolvents,
discriminants, Euler factors, root numbers, or bad-prime classifications.

Checker command:

```text
python code/c62_dictionary_checker.py
```
