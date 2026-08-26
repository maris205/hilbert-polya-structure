# C176 verification plan

This is a theorem package, so no GPU or statistical experiment is appropriate.

1. Freeze the undirected loopless multigraph, sink, stable-height convention, reduced Laplacian, nonnegative addition vector, recurrent phase space, and one addition--stabilization clock.
2. Prove stabilization uniqueness and the burning/unique-recurrent-representative bridge to `K=Z^r/Delta Z^r`.
3. Derive the Smith `lcm` order formula and the adjugate `D/gcd` formula, including `b=0` and `r=0`.
4. Prove uniform exact orbit length, fixed counts, zeta, finite Koopman determinant, character spectrum, inversion reversal, and self-adjointness iff `L<=2`.
5. Exhibit and verify the path counterexample separating all stable configurations from the recurrent restriction.
6. Enumerate all 30 connected simple-graph isomorphism types with two through five vertices, every sink, and zero/unit/all-ones sources. Use Dhar burning, exact stabilization, determinants and adjugates.
7. Check with a producer-independent simultaneous-burning/highest-unstable implementation; verify low/high toppling orders agree, recurrent signatures are class-unique, and inversion reverses every tested translation.
8. Cross-check all 780 Smith and adjugate orders in SymPy; byte-replay evidence and reject repaired-hash and stale-hash mutations.
9. Compile three materially distinct bilingual manuscript rounds and require deterministic final bytes, embedded fonts, clean logs, visual snapshots, and a 27-payload self-excluded manifest.

Falsifier: two recurrent representatives in one class, a nonuniform recurrent cycle length, disagreement between the two order formulas, a wrong fixed/spectral multiplicity, failure of reversal, self-adjointness outside `L<=2`, promotion of the full stable set to a permutation, or any positive scope flag rejects the package.
