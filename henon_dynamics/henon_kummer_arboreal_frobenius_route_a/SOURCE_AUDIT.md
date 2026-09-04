# Source audit

## Verified authoritative sources

- Rafe Jones, *Galois representations from pre-image trees: an arboreal
  survey*, Publications mathématiques de Besançon (2013), pp. 107--136,
  DOI `10.5802/pmb.a-154`.  The publisher page and full text establish the
  preimage-tree/Galois framework and the Frobenius fixed-point density
  viewpoint.
- Serge Lang, *Algebra*, third edition, GTM 211, Springer (2002), DOI
  `10.1007/978-1-4613-0041-0`.  The official Springer record verifies the
  edition metadata; Chapter VI, Section 9, Theorem 9.1 is the cited
  binomial irreducibility criterion.
- Lawrence C. Washington, *Introduction to Cyclotomic Fields*, second
  edition, GTM 83, Springer (1997), DOI
  `10.1007/978-1-4612-1934-7`.  The official record verifies the
  cyclotomic-field reference.
- Jürgen Neukirch, *Algebraic Number Theory*, Springer (1999), DOI
  `10.1007/978-3-662-03983-0`.  The official record verifies the
  Chebotarev/number-field reference.

DOI targets and publisher metadata were checked during the C374 release.
No title, author, year, or DOI was supplied from unaudited memory.

## Package-owned derivation

The paper proves rather than cites the specialization-specific steps:

- nonsquareness of `sqrt(2)` in every `Q(zeta_(2^n))`;
- the exact radical--cyclotomic intersection;
- the parity relation `(-1)^b=(2/a)`;
- surjectivity by degree and exact cardinality;
- all restriction maps and their four-element kernels;
- the complete fixed-root count and closed density formula.

## Evidence boundary

Level and prime enumeration validates code and records exact finite
receipts.  It does not establish irreducibility, the all-level group, an
inverse limit, or a density theorem.

## Route-A control audit

Three A0 controls are separated from the theorem and from A1.  For
neighboring basepoint `3`, every prime above `3` in the 2-power cyclotomic
field has valuation one because `3` is unramified.  Thus `3` is not a
square there; Capelli makes `X^(2^n)-3` irreducible over the cyclotomic
field, so the radical--cyclotomic intersection is `Q` and the affine image
is full.  This proves that basepoint 3 has no copy of the basepoint-two
shared `Q(sqrt(2))` character cut.

The simpler ambient full affine group is also exhaustively enumerated at
levels 3--12.  It contains exactly `2^(2n-5)` elements with four fixed
roots, the stratum excluded by the basepoint-two parity condition.  Finally,
the exact ledger of 25 odd composites below 100 separates five prime powers
`9,25,27,49,81`, retained as the repetition classes `Frob_p^r`, from twenty
mixed composites having at least two distinct prime factors.  Only the mixed
labels lack a single-prime Frobenius owner.  Finite empirical density is
explicitly assigned no A0 credit.

None of these A0 controls fills the A1 gap.  The package has a fixed-root
law, not a complete all-level primitive/repeated orbit atlas with
orientation, phase, multiplicity weights, monodromy, stability, an
intrinsic prime-to-orbit period law, and the six mandatory A1 controls.
Strict v0.2 therefore records `A1_WEAK` and `ROUTE_A_EXPLORATORY`.

## Collision audit

HCS-C12A owns the universal finite-permutation trace/zeta mechanism.
C33/C34/C38--C40 use the word Kummer for Hill square classes and cubic
channels, not an arboreal radical tower.  C56 owns a single degree-27
finite étale `W(E6)` fiber.  C179 is a congruence/Zsigmondy return tower.
C369 is a fixed quartic `S4` all-good-prime atlas.  C374 is distinct: it
owns the compatible all-level basepoint-two preimage fields, their unique
quadratic entanglement, index-two 2-adic affine image, and root-prime law.
