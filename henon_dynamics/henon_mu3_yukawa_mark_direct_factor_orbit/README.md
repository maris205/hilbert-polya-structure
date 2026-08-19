# HCS-C70 direct-factor automorphism orbits

Status: **PREFREEZE_COMPLETE_NOT_RELEASED**.

C70 passes from the single C69 factor `D` to the global family of all such
direct factors in the ambient finite abelian group `C`.  The action of
`Aut(C)` is transitive on both:

```text
{D' subset C : D' is a direct factor and D' ~= D},
{(D',K') : C=D' direct-sum K', D'~=D, K'~=K}.
```

The exact orbit sizes are

```text
D-type direct factors:       5846893330432
ordered (D,K) decompositions: 12857454406351852314558464
```

The setwise stabilizer is
`Hom(K,D) semidirect (Aut(D) x Aut(K))`; the ordered-pair stabilizer is
`Aut(D) x Aut(K)`.  Each direct factor has `2^41` complements, reproducing
the second count from the first.  Split embeddings form a third orbit of size
`2245207038885888`.  A Birkhoff count gives `8794482475008` subgroups
isomorphic to `D`, of which `2947589144576` are not direct factors; an explicit
non-factor witnesses the boundary.

Entry points:

- `code/c70_direct_factor_orbit.py`: source-bound producer;
- `code/c70_direct_factor_orbit_checker.py`: independent block-count checker;
- `code/c70_group_crosscheck.py`: SymPy/GAP cross-check;
- `code/c70_direct_factor_orbit_replay_checker.py`: clean replay;
- `code/c70_mutation_test.py`: hostile semantic mutations;
- `results/c70_direct_factor_orbit_evidence.json`: canonical evidence;
- `paper/main.pdf`: compiled manuscript.

Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.  No canonical decomposition, full
Burnside-ring, arithmetic/local, Euler-factor, root-number, automorphy, or
Hilbert--Polya claim is made.
