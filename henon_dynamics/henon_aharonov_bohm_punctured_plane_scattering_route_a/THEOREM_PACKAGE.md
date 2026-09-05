# C383 theorem package

The full proof is maintained in [proof/ANALYTIC_PROOF.md](proof/ANALYTIC_PROOF.md), and its final manuscript rendering is [paper/main.pdf](paper/main.pdf). Proof status is `PROVABLE_AS_STATED` for the explicitly fixed Friedrichs domain.

The chain closes: angular closed form → onto Hankel transform → absolutely continuous spectrum → onto wave operators → two signed half-channel phases → full Abel scattering distribution → local Weber heat kernel → global noncompactness and cutoff determinant obstruction → integer gauge and physical time reversal.

The two ordinary global objects that fail are distinct. The heat semigroup is noncompact even at zero flux because its spectral measure is non-atomic. The scattering correction S minus I is noncompact only at nonzero flux in the chosen cell; it vanishes at zero flux. The manuscript preserves this boundary.

The analytic proof imports the named Hankel transform theorem, Weber integral, and rigorous AB wave-operator existence theorem. It supplies the convention-specific consequences and all cutoff/symmetry arguments. Finite numerical tests do not replace these imported analytic theorems.
