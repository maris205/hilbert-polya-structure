# C74 experiment plan

1. Rebind the C72 coordinate evidence and C73 symmetry evidence by SHA-256.
2. Enumerate the 243 endomorphism matrices
   `[[a,3b],[c,d]]` of `Z/9 + Z/3`; adjoining the two `Z/2` endomorphisms
   gives 486 endomorphisms of `Q`.  Restrict to the identity dyadic component
   and independently test the resulting 108 automorphisms on all 54 group
   elements.
3. Enumerate all `108 * 54 = 5832` affine maps.
4. Compute the occurrence multiset and distinct-set overlap histograms.
5. Prove and check both affine stabilizers are trivial, and record the two
   nonidentity maps with maximum occurrence overlap.
6. Compare the affine orders with C73's abstract hypergraph order, retaining
   the distinction between core points, duplicate label fibers, and
   combinatorial hypergraph vertices.
7. Run an independent parameter/image cross-check, clean replay, hostile
   semantic mutations, two isolated clean LaTeX builds, and visual inspection.

Kill gates: using `7776` instead of the correct affine order `5832`;
confusing occurrence overlap with pointwise or distinct-point overlap;
claiming that translations preserve subgroup generation; or identifying the
C73 hypergraph automorphism group with a core automorphism group.
