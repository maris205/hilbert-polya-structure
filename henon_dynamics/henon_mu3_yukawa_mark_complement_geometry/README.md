# HCS-C71 complement intersection geometry

Status: **PREFREEZE_COMPLETE_NOT_RELEASED**.

C71 studies all complements of the fixed C69 factor
`D ~= Z/8 + (Z/2)^2` in `C=D direct-sum K`.  Every complement is the graph
of a unique `f in Hom(K,D)`, so pair intersections are controlled by the image
type of `f-g`.  There are `2^41` complements, and from every fixed complement
the within-complement intersection-index spectrum is

```text
index 1:              1
index 2:          28665
index 4:      117600270
index 8:    70111567864
index 16: 1030892519424
index 32: 1097901539328
```

The common intersection of all complements is
`8C ~= Z/3 + Z/18`, of order `54`, while all complements together generate
`C`.  Among the named classes, the sixteen elements `8[S_j]` have orders

```text
9,3,3,3,1,1,9,3,2,1,3,3,1,1,9,9.
```

No one or two named elements generate `8C`; exactly 25 named triples do, and
every one contains `S9`.

Entry points:

- `code/c71_complement_geometry.py`: source-bound subgroup-poset producer;
- `code/c71_complement_geometry_checker.py`: independent formula checker;
- `code/c71_group_lattice_crosscheck.py`: GAP/SymPy cross-check;
- `code/c71_complement_geometry_replay_checker.py`: clean replay;
- `code/c71_mutation_test.py`: hostile semantic mutations;
- `results/c71_complement_geometry_evidence.json`: canonical evidence;
- `paper/main.pdf`: compiled manuscript.

Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.  No canonical complement, complete
kernel-type classification, full Burnside-ring, arithmetic/local,
Euler-factor, root-number, automorphy, or Hilbert--Polya claim is made.
