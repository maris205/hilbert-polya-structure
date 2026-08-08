# HCS-C19 source and novelty audit

## Primary source lock

The foundational repository source is Paper 5:

- `../docs/prior_work/papers/5-An Area-Preserving Henon-Map Model.pdf`.

Its recurrence is conjugate away from \(a=0\) to the Hamiltonian form used in
the following primary source:

- A. Endler and J. A. C. Gallas, “Conjugacy classes and chiral doublets in
  the Hénon Hamiltonian repeller,” *Physics Letters A* 356 (2006), 1--7,
  <https://doi.org/10.1016/j.physleta.2006.04.042>;
  author PDF: <https://inaesp.org/PublicJG/conjugacy_classes_PLA_356_1_2006.pdf>.

Endler--Gallas explicitly publish

\[
S_7(\sigma)=C_7(\sigma)^2D_7(\sigma),
\qquad C_7(\sigma)=\sigma^2-2\sigma-a,
\]

and a degree-seven coordinate polynomial.  They also explain that the square
records pairs of chiral cycles exchanged by reversal.  The last line of their
printed Eq. (16), however, reads

\[
-2a^3+6a^2+2a+3(a^3-4a^2+a-2)\sigma.
\]

The repository's initial transcription silently used

\[
-2a^3+6a^2+2a+3+(a^3-4a^2+a-2)\sigma.
\]

The adversarial audit caught this difference.  The literal source expression
has a degree-42 \(x\)-discriminant after the chiral substitution and fails an
exact \(\mathbb F_{103}\) period-seven orbit.  The second expression passes
that orbit exactly and was therefore frozen as the adopted correction.  The
generic neighbor theorem in `NEIGHBOR_CORRESPONDENCE.md` independently proves
that its seven generic roots form an exact Hénon 7-cycle.  We do not claim
that the publisher or authors issued an erratum or that the adopted component
exhausts the full saturated period-seven scheme.

Accordingly, the chiral classification and factor \(C_7\) are prior work.
The exact diagnosis, the generic Hénon reconstruction, the ordered-edge time
lift, and the arithmetic geometry of the explicit septic are the present
contributions.

The existing repository project
`../henon_dihedral_chronology_obstruction/` already proves that the period-six
coarse marker components have genus zero and warns that ordinary dihedral
quotients discard nontrivial time sectors.  HCS-C19 begins at period seven and
studies a different intermediate quotient: the coordinate-root cover before
orientation is restored.

## Search result

A targeted source search found the published period-seven polynomial and the
general chiral-class/counting literature, but no source computing the genus,
normalization branches, or local Frobenius polynomials of this exact septic.
The defensible novelty statement is therefore provisional and narrow:

> a generic dynamical and arithmetic-geometric analysis of an adopted
> correction to a previously published Hénon coordinate equation.

It is not “the first arithmetic study of the Hénon map,” nor a new theory of
Hénon chiral cycles.  A broader novelty claim would require a systematic
database and citation search beyond the targeted audit recorded here.

## Claim ledger

| Claim | Status | Source/evidence |
|---|---|---|
| Paper-5/Hamiltonian conjugacy for \(a\ne0\) | proved algebraically | direct substitution |
| \(C_7\), chiral doublets, intended coordinate-carrier method | prior work | Endler--Gallas 2006 |
| literal Eq. (16) fails; adopted formula passes exact cycles at one fibre | exact specialization certificate | \(\mathbb F_{103}\) audit |
| adopted roots generically form one exact Hénon 7-cycle | proved here | quotient-field subresultant, neighbor sum, monodromy blocks |
| ordered-edge cover has generic degree 14 and \(\tau\) of exact order 7 | proved here | neighbor graph and dihedral identities |
| scalar septic is geometrically integral | proved here | specialization plus geometric inertia |
| its characteristic-zero normalization has genus 3 | proved here | branch analysis and two genus computations |
| three branch-corrected finite-prime numerator tables | exactly computed and independently checked as candidates | `results/` |
| adopted curve exhausts the full saturated period-seven scheme | open/not claimed | only one generic component is certified |
| selected-prime simultaneous normalization/good reduction | open/not claimed | requires full residual resolution or equinormalization theorem |
| complete bad-reduction set | open/not claimed | needs a global regular model |
| genus and equivariant Frobenius traces of the oriented cover | open | next major experiment |
| Riemann divisor or Hilbert--Pólya operator | not claimed | Route-A exploratory ruling |
