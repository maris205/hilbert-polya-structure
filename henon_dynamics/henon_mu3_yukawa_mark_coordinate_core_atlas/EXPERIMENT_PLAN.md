# C72 experiment plan

1. Bind the exact C64 matrix and the frozen C71 core certificate.
2. Recompute the rational residues of all `8[S_j]`.
3. Prove that `(8[S1],8[S3],8[S9])` gives a `Z/9 + Z/3 + Z/2`
   coordinate model and solve uniquely for all sixteen coordinates.
4. Enumerate all `65536` named supports by subgroup closure.
5. Independently enumerate the complete abstract subgroup lattice of the
   54-element model and compare the two sets, not only their type counts.
6. Record the ten subgroup types by support size and the full-generation
   polynomial.
7. Cross-check the abstract lattice with GAP and each coordinate relation
   with the original integer presentation.
8. Run clean replay, hostile mutations, and two isolated clean LaTeX builds.

Kill gates include source drift, incomplete subgroup coverage, a row that does
not sum to `binomial(16,r)`, a false abstract rank-three claim, or any scope
expansion.
