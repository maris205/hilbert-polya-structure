# Source audit and claim boundary

## Primary sources

1. Lowell S. Brown and Gerald Gabrielse, “Precision spectroscopy of a charged
   particle in an imperfect Penning trap,” *Physical Review A* 25, no. 4
   (1982), 2423(R)–2425(R). DOI:
   [10.1103/PhysRevA.25.2423](https://doi.org/10.1103/PhysRevA.25.2423).
   The official APS record is cited in the final-round Hamiltonian section for
   the ideal-trap Hamiltonian/frequency normalization and its model lineage.
2. Lowell S. Brown and Gerald Gabrielse, “Geonium theory: Physics of a single
   electron or ion in a Penning trap,” *Reviews of Modern Physics* 58, no. 1
   (1986), 233–311. DOI:
   [10.1103/RevModPhys.58.233](https://doi.org/10.1103/RevModPhys.58.233).
   The official review is cited in the final-round signed-action section for
   the modified-cyclotron/magnetron terminology and the physical interpretation
   of the magnetron mode.

Both references were checked through official APS/DOI records and are linked
to their precise roles by formal citations in the final-round paper.  They
support model lineage and terminology only; this package makes no
literature-priority claim.  No displayed formula or proof step is outsourced:
the exact all-parameter theorem and its proof stand on the formulas and local
derivations given in the package.

## Source-to-claim map

| Claim class | Support | Status |
|---|---|---|
| Ideal Hamiltonian/frequency normalization | Brown–Gabrielse 1982, formally cited at equation (1) | verified model lineage only |
| Modified-cyclotron/magnetron terminology | Brown–Gabrielse 1986, formally cited before the signed normal form | verified terminology only |
| Exact flow, threshold, Jordan and unstable atlas | analytic derivation in C274 | proved here |
| Signed actions/Krein signs | direct Hamiltonian substitution | proved here |
| Active-mode periods and strobe dimensions | block-rotation/Jordan proof | proved here |
| Regression counts | hashed C274 receipt | independently checked |

## Neighbor distinction

C268's constant electromagnetic Lorentz flow has uniform spacetime fields and
no spatial quadrupole trap.  C274 instead combines a quadrupole saddle with
magnetic stabilization, producing the nontrivial threshold, a critical radial
Jordan collision, and a negative magnetron action.  A plain harmonic oscillator
likewise lacks this gyroscopic signed-energy structure.

## Explicit exclusions

No source is used to justify imperfect-trap accuracy, damping, many-body
effects, experimental performance, arithmetic local data, Euler factors, root
numbers, automorphy, a target counting law, a target divisor, or a
Hilbert--Polya operator.  The firewall is
`NO_BAD_EULER_OR_ROOT_NUMBER`.
