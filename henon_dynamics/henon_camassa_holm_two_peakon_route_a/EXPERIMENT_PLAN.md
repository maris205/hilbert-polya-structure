# C278 executable experiment plan

## Claim-driven checks

1. Generate 15 same-sign rows from three `(P,D)` chambers and five times.
   Reconstruct the cosh branch, momenta, energy, centre coordinate, and both
   reduced ODE residuals.
2. Generate 12 signed rows from three `D^2>P^2` chambers and four distances
   from collision.  Check the sinh/coth branch, invariant reconstruction,
   opposite signs, and collision scalings.
3. Generate 15 `alpha` rows.  Check momentum conservation, prescribed energy
   loss, the post-collision `D_+^2`, and the sticky `alpha=1` boundary.
4. Use a producer-independent checker that imports no producer code.
5. Re-derive conservation, branch residuals, and limiting coefficients in
   SymPy.
6. Re-run the producer into two unrelated temporary paths and demand exact
   byte identity with the retained JSON.
7. Repair hashes after 41 semantic attacks and require every altered payload
   to fail against the actual independent checker; the attacks include model,
   proof, scope-key, nested-row, reference-metadata, and schema mutations.
   Retain a stale-hash control as a separate test.

Finite rows audit conventions and implementation.  The analytic proof of the
distributional reduction and separation of variables remains indispensable.
