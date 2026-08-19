# HCS-C72 named-coordinate core atlas

Status: **PREFREEZE_COMPLETE_NOT_RELEASED**.

C72 turns the C71 universal core `8C ~= Z/3 + Z/18` into an exhaustive
coordinate atlas.  In the basis `(8[S1],8[S3],8[S9])`, all sixteen named
classes receive unique coordinates in `Z/9 + Z/3 + Z/2`.  Exact closure of
all `65536` named supports reaches precisely 20 subgroups, equal as a set to
the complete abstract subgroup lattice of `8C`.

The number of full-core generating supports by size is

```text
3:25, 4:224, 5:940, 6:2461, 7:4504, 8:6095, 9:6269,
10:4950, 11:2992, 12:1364, 13:455, 14:105, 15:15, 16:1.
```

Exactly 25 supports are inclusion-minimal; all are triples containing `S9`.
This minimum is relative to the named presentation.  The abstract core is
two-generated.

Entry points:

- `code/c72_coordinate_core_atlas.py`: source-bound exhaustive producer;
- `code/c72_coordinate_core_atlas_checker.py`: independent lattice/group checker;
- `code/c72_group_crosscheck.py`: GAP cross-check;
- `code/c72_coordinate_core_atlas_replay_checker.py`: clean replay;
- `code/c72_mutation_test.py`: hostile semantic mutations;
- `results/c72_coordinate_core_atlas_evidence.json`: canonical evidence;
- `paper/main.pdf`: compiled manuscript.

Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.  No canonical Smith coordinates, full
Burnside-ring, arithmetic/local, Euler-factor, root-number, automorphy, or
Hilbert--Polya claim is made.
