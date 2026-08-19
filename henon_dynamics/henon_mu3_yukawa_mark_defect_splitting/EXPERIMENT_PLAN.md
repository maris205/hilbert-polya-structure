# C69 exact experiment plan

1. Bind the C64, C65, C66, and C68 evidence and manifest bytes.
2. Form `U=[u1 u2 u3]` and `Delta=diag(8,2,2)`.
3. Verify an integer `3 x 16` matrix `R` satisfies `RM=0 mod Delta` and
   `RU=I mod Delta`.
4. Build the full preimage lattice `L` of zero under `R mod Delta`, exhibit a
   column basis `B`, and verify its index is 32.
5. Compute the integral presentation `N=B^{-1}M`, verify `BN=M`, and determine
   its Smith invariants and order.
6. Derive the exact number of retractions from the torsor
   `Ret(C,D) = rho0 + Hom(C/D,D)`.
7. Repeat the central calculations with an independent checker and SymPy, then
   run clean replay and hostile semantic mutations.
8. Compile twice from clean LaTeX state and require byte-identical PDFs.

Kill the candidate if any congruence, integrality, determinant, Smith, order,
count, source-binding, scope, or reproducibility gate fails.
