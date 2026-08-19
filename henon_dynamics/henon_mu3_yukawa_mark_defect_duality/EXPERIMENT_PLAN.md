# C68 exact experiment plan

1. Rebind the C64, C65, C66, and C67 evidence and manifest hashes.
2. Recompute the C65 vectors `z_i`, saturation vectors `u_i`, and
   `M z_i = d_i u_i` with `d=(8,2,2)`.
3. Compute the Smith form of `[M | u1 | u2 | u3]` to obtain `C/D`.
4. Enumerate the 32 coefficient classes modulo `d` to prove that `D` has
   invariant factors `(2,2,8)`.
5. Construct the explicit row congruence lattice `A`, transform `M^T` into
   its basis, and compute the dual quotient Smith form.
6. Run an independent checker, clean replay, SymPy cross-check, and hostile
   mutations.  Kill the target if any relation, quotient, or duality gate
   fails.
