# Paper plan

## Target theorem

For every finite group `K`, construct the flat-connection SFT `X_K` over the
nonorientable genus-three surface group and prove that its fixed-point counts
along two explicit finite-index subgroup families recover `|K|` and the multiset
of irreducible pairs `(degree, Frobenius--Schur indicator)`.

## Section map

| Section | Job | Proof obligation |
|---|---|---|
| Abstract | State the exact two spectra, inversion, and `D_8/Q_8` separation | No novelty language |
| 1. Introduction | Motivate orientation-sensitive periodic data and state the main theorem | Credit classical formulas and group-SFT context |
| 2. Background | Fix surface, shift, character, and cover conventions | All left-coset and orientation conventions explicit |
| 3. Flat shift | Give the local holonomy rule and the gauge-count proposition | Prove finite type and spanning-tree gauge bijection |
| 4. Two families | Define `H_n,L_m`, identify cover types and compute both spectra | Indices, Euler characteristics, and genera checked |
| 5. Moment recovery | Prove the finite moment lemma and reconstruct all multiplicities | Handle `nu=0`, zero coefficients, and starting indices |
| 6. `D_8/Q_8` | Give exact formulas and finite values | Orientable equality and odd nonorientable separation |
| 7. Scope and controls | State ownership, limitations, P70 firewall, and computation role | No classification or priority overclaim |
| 8. Conclusion | Summarize the orientation-sensitive mechanism | No new unchecked claim |

## Claim-to-proof table

| ID | Claim | Proof source inside package | Status |
|---|---|---|---|
| C1 | `X_K` is a finite-type `Lambda`-shift | `sections/3_flat_shift.tex` | closed |
| C2 | Fixed flat connections satisfy the gauge-count identity | `sections/3_flat_shift.tex` | closed |
| C3 | `H_n` and `L_m` have the asserted indices and surface types | `sections/4_subgroup_counts.tex` | closed |
| C4 | The exact orientable and nonorientable spectra hold | `sections/4_subgroup_counts.tex` | closed modulo cited classical formula |
| C5 | The joint spectra recover `|K|` and all `(d,nu)` multiplicities | `sections/5_moment_recovery.tex` | closed |
| C6 | `D_8` and `Q_8` have equal orientable and distinct odd nonorientable data | `sections/6_dihedral_quaternion.tex` | closed and computationally checked |

## Tables and figures

- Table 1 compares the two families, cover topology, and normalized moments.
- Table 2 compares the `D_8/Q_8` signatures and spectra.
- No decorative figure is used; `FIGURE_DECISION.md` records the reason.

## Release gate

Internal mathematical package: target `GO`.  External dissemination:
**HOLD** until specialist novelty, surface-presentation convention, and
bibliography audits are independently repeated.
