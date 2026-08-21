# C86 theorem package

Let `E` be the faithful 1920-element label permutation group and let `X` be
the 16-cube of support masks.  For support orbits `O_i,O_j`, set

```text
q_ij = #{labels ell : A xor {ell} belongs to O_j},  A in O_i.
```

The number is independent of `A`: label toggling is equivariant under `E`.
Thus `Q=(q_ij)` is the exact strong quotient of the cube adjacency operator.
Every row sums to 16 and

```text
|O_i| q_ij = |O_j| q_ji,
```

so the orbit-size measure is reversible.  The quotient has 3024 states,
30240 nonzero directed arcs, and 15120 unoriented orbit pairs.

Walsh characters of degree `k` have cube eigenvalue `16-2k`.  Averaging a
character over its `E`-orbit gives an invariant eigenfunction, and distinct
dual support orbits give a basis of the invariant functions.  Hence the
complete quotient spectrum is `16-2k`, with multiplicity equal to the number
of `E`-orbits on `k`-subsets:

```text
1,7,27,73,151,252,352,424,450,424,352,252,151,73,27,7,1.
```

The exact repair-level edge flow and the full-core/full-core flow are read
from the same quotient.  The latter is 445696 and independently reproduces
C82's Hamming-distance-one autocorrelation.
