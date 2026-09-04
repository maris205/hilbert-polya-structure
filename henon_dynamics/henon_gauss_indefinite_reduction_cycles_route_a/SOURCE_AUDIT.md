# HCS-C364 Source Audit

## Verified sources

1. J. V. Uspensky, “On the reduction of the indefinite binary quadratic forms,” *Bulletin of the American Mathematical Society* (1930), pp. 710--718. DOI: <https://doi.org/10.1090/S0002-9904-1930-05043-0>.
   - Role: primary historical source for indefinite-form reduction.
   - Boundary: it is not cited as proving the package's software ledger or Route-A assessment.

2. Duncan A. Buell, “Indefinite Forms,” in *Binary Quadratic Forms*, Springer (1989), pp. 21--48. DOI: <https://doi.org/10.1007/978-1-4612-4542-1_3>.
   - Role: authoritative source for discriminant, primitivity, equivalence, reduction, and stabilizer conventions.
   - Boundary: the paper explicitly freezes one convention instead of assuming that every convention in the literature has identical representatives.

The Uspensky and Buell sources also anchor the classical
reduction--automorph cross-section lemma used in the proof: an expanding
positive projective automorph of a reduced indefinite form advances the
oriented continued-fraction cross-section by an integral number of complete
Gauss digits, and complete returns give the converse automorphs. C364 uses
this correspondence only after deriving its exact pair update and proving
that the reduced state permutation has least return time ell. It then deduces
that every positive stabilizer shift is a multiple of ell, so the period
matrix is primitive; this package-local deduction is not attributed to either
source as a new priority claim.

3. Don Bernard Zagier, *Zetafunktionen und quadratische Körper*, Springer (1981). DOI: <https://doi.org/10.1007/978-3-642-61829-1>.
   - Role: authoritative real-quadratic arithmetic context.
   - Boundary: its arithmetic zeta functions are not identified with the finite source Artin--Mazur zeta in C364.

DOI metadata and titles were checked through the DOI resolver on 2026-09-04. No claim of literature priority is made. The proof is a source-local reconstruction from standard reduction and continued-fraction facts, followed by finite permutation linear algebra.

## Claim-to-source boundary

- Lagrange's reduced-irrational periodicity and Gauss reduction are established classical facts.
- The reduction--automorph cross-section lemma is used only for the stated
  stabilizer-generation step; the finite cycle inventory is not evidence for
  that continuous classical correspondence.
- The exact evidence hashes, mutation gates, and finite inventory are package-local results.
- The class-group/narrow-class bridge is intentionally excluded from the theorem contract; no unverified orientation convention is needed.
- “Zeta” in the paper means only the finite Artin--Mazur cycle product. It is not an Euler product over rational primes and is not a completed arithmetic zeta function.

## Workspace collision audit

- C16 owns an S-arithmetic near-wall clock, not fixed-discriminant reduced-state cycles.
- C193 owns a Markoff--Vieta descent tree, not a finite reversible Gauss permutation.
- C330 owns Romik's Pythagorean three-branch dynamics, not primitive indefinite-form reduction.
