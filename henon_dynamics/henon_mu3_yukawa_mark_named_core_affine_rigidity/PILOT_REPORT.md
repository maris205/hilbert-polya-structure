# C74 pilot report

Status: **PASS**.

For `Q = Z/9 + Z/3 + Z/2`, the matrix form

```text
(x,y,z) -> (a*x + 3*b*y mod 9, c*x + d*y mod 3, z)
```

has 243 odd-part endomorphism matrices.  Adjoining the two endomorphisms of
the `Z/2` factor gives 486 endomorphisms of `Q`; restricting to the identity
dyadic component and nonzero diagonal residues gives 108 automorphisms.
Therefore
`|Aff(Q)| = 54*108 = 5832`.

The 16 named occurrences contain 10 distinct points with multiplicities
`5,2,2,1,1,1,1,1,1,1`.  Exhaustive affine enumeration gives trivial
stabilizers for both the occurrence multiset and the underlying 10-point set.
The occurrence-overlap histogram is

```text
0:1435, 1:1339, 2:1068, 3:771, 4:621, 5:265, 6:134, 7:87,
8:26, 9:29, 10:35, 11:7, 12:10, 13:2, 14:2, 16:1.
```

The distinct-point overlap histogram is

```text
0:1435, 1:1346, 2:1139, 3:929, 4:628, 5:275, 6:63, 7:14, 8:2, 10:1.
```

The maximum nonidentity occurrence overlap is 14, attained by exactly two
linear inverse witnesses.  C73's order `345600` is consequently a
combinatorial hypergraph order, not an induced affine symmetry order.
