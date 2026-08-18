# C63 experiment plan

1. Rebind the frozen C61 ambient action and verify the exact C62 input hashes.
2. Recover one stabilizer representative for each of the 16 C62 type labels,
   checking its canonical element-set digest.
3. Enumerate the 25 conjugacy classes of `W(E_6)` by generator conjugation,
   with deterministic class representatives and centralizer orders.
4. Evaluate each transitive permutation character by
   `|C_G(g)|*|S intersect Cl(g)|/|S|` and verify integrality.
5. Compute an exact rational rank/nullspace and test the three claimed basis
   vectors and the exterior/symmetric relation vectors.
6. Run an independent checker that consumes only the JSON evidence, rejects
   wrong class counts, wrong source hashes, altered matrix entries, and
   unsupported full-Burnside or arithmetic claims.
7. Write and compile the scoped paper, then create a self-excluding manifest.

The first pilot already passed steps 2--5; those values remain selection
chronology until the producer/checker gates pass.
