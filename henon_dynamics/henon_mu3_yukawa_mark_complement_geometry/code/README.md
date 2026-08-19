# C71 exact certificate code

- `c71_complement_geometry.py` binds C64/C69/C70, explicitly enumerates the
  subgroup poset of `D`, performs exact-image inversion, and computes the
  rational named-coordinate residues.
- `c71_complement_geometry_checker.py` independently uses Birkhoff subgroup
  counts, automorphism orders, epimorphism duality, and a separate rational
  quotient implementation to verify every field.
- `c71_group_lattice_crosscheck.py` uses GAP to enumerate all 38 target
  subgroups and SymPy Smith/Hermite forms to verify `8C` and all named triples.
- `c71_complement_geometry_replay_checker.py` performs a clean-process replay.
- `c71_mutation_test.py` requires rejection of hostile semantic changes.
