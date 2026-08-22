# Experiment plan

1. Freeze the 3-cycle Laplacian and rational parameters `a=7`, `kappa=1/5`.
2. Produce canonical rational evidence for fixed and period-two witnesses.
3. Recompute the map and monodromies in an independent checker.
4. Verify symplectic, reversor, and exact-primitive identities in SymPy.
5. Compare the coupled monodromy to the `kappa=0` control and reconstruct its
   determinant from one longitudinal and two transverse modes.
6. Run replay and hostile mutation audits, then compile the paper twice in
   isolated directories with a fixed `SOURCE_DATE_EPOCH`.

Success means internal consistency of this finite certificate. It does not
mean that A1 or A2 has been promoted globally.
