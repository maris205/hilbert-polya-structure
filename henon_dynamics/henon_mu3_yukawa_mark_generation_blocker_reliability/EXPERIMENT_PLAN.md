# C73 experiment plan

1. Bind C71 and C72 evidence and manifests.
2. Reduce the C72 `Z/9 + Z/3 + Z/2` coordinates through the Frattini
   quotient and classify all projective directions.
3. Prove that the non-isolated minimal-generation hypergraph is the coned
   `K_{1,1,2,5}` and that the six dummy labels are isolated vertices.
4. Compute minimal transversals structurally and by exhaustive deletion.
5. Enumerate all 65536 deletions by size and verify every binomial mass.
6. Derive independent-set, vertex-cover, and destructive-transversal
   polynomials.
7. Derive homogeneous and heterogeneous reliability formulae and compute
   Banzhaf/Shapley coordinate importance.
8. Cross-check block-state and graph polynomial expansions with SymPy and the
   structural direct-product order with GAP, then run clean replay, hostile
   mutations, and two clean paper builds.

Kill gates: confusing minimal blockers with all transversals, conflating three
robustness notions, treating hypergraph automorphisms as core automorphisms,
or expanding past `NO_BAD_EULER_OR_ROOT_NUMBER`.
