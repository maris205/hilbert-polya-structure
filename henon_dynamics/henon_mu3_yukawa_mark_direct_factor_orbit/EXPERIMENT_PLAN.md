# C70 exact experiment plan

1. Rebind the C66 and corrected C69 evidence/manifest bytes.
2. Recover the 2- and 3-primary exponent partitions for `C`, `D`, and `K`.
3. Compute every automorphism order from conjugate partitions.
4. Independently recompute them from endomorphism counts and invertible
   equal-exponent blocks.
5. Compute `Hom(K,D)` in the correct direction and the two stabilizers.
6. Apply orbit--stabilizer to direct factors and ordered decompositions; verify
   all three mass identities.
7. Prove transitivity using elementary-divisor uniqueness and componentwise
   isomorphisms.
8. Count all `D`-type subgroups with the Birkhoff formula and separate the
   non-direct population; count split and all monomorphisms.
9. Verify an explicit `D`-type subgroup whose quotient type shows it is not a
   direct factor.
10. Run SymPy/GAP, replay, hostile mutation, and double-clean-build gates.

Kill the candidate on any source, primary-type, automorphism, Hom-direction,
stabilizer, orbit, counterexample, scope, or reproducibility failure.
