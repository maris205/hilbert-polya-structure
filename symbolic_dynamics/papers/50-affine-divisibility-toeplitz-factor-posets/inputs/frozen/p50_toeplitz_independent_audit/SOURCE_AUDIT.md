# Independent primary-source and owner audit

## Status and method

**NO_EXACT_COLLISION_FOUND_IN_BOUNDED_SEARCH.**  This is a bounded
owner-subtraction result, not a novelty or priority claim.  Technical scope
was checked against primary journal/publisher or arXiv full text.

## Downarowicz--Kwiatkowski--Lacroix (1995)

T. Downarowicz, J. Kwiatkowski, Y. Lacroix, “A criterion for Toeplitz flows
to be topologically isomorphic and applications,” *Colloquium
Mathematicum* 68 (1995), 219--228.

- DOI and primary record: <https://www.impan.pl/get/doi/10.4064/cm-68-2-219-228>
- Primary PDF: <https://matwbn.icm.edu.pl/ksiazki/cm/cm68/cm6828.pdf>
- Independently retrieved PDF SHA-256:
  `7f2ddf0133ddf5cfbab7f3103056ea1ed7050d2f92b1063f73a48ccd7430965f`.

Theorem 1 was checked in the full PDF.  For Toeplitz sequences with the same
period structure, a homomorphism over zero is characterized at some level
by a function between aligned `t`-symbols that sends each aligned source
symbol to the corresponding target symbol; bijectivity characterizes the
isomorphism case.  The paper defines “over zero” by mapping the chosen
Toeplitz point to the chosen target point.

Owner subtraction: DKL owns the general same-period, over-zero,
aligned-symbol criterion.  It does not assert that every such map in the
present affine one-hole family collapses to a single source-letter quotient,
and it does not identify the kernels with independent-block partitions or
their refinement poset.  The audited CHL theorem is therefore a specialized
radius-zero collapse inside DKL's more general setting, not a substitute for
their theorem.

## Hosseini--Yassawi (2026)

M. Hosseini, R. Yassawi, “Obstacles to topological factoring of Toeplitz
shifts,” *Discrete and Continuous Dynamical Systems* 46 (2026), 413--432.

- DOI and official journal record:
  <https://www.aimsciences.org/article/doi/10.3934/dcds.2025105>
- Versioned source: <https://arxiv.org/abs/2412.04422> (v3 inspected).
- Independently retrieved arXiv v3 source-tar SHA-256:
  `11c352bb3e340e575fe0d82d31f923315cef4d3238229691b60ee3533777b3f8`.
- Extracted v3 `main.tex` SHA-256:
  `4c50b0ffc7f47abffd4a36b7b75cad11bf3b2ba6a4094f48037d03c39532c71b`.

Theorem 1.1 and the constructive-period definition were checked in the
versioned source.  The theorem proves the cross-base necessary condition
`q|p` for a pointed factor between constructive pure-power Toeplitz shifts,
and equality of the bases for pointed conjugacy.  It does not give
cross-base sufficiency or classify same-base maps as letter quotients.

Owner subtraction: Hosseini--Yassawi owns the constructive-period
terminology and the stated cross-base obstruction.  The frozen candidate
leaves all cross-base maps out of scope, proves directly which of its affine
integer-base period structures meet the constructive definition, and adds
only the same-base pointed collapse and partition classification.

## Source-indexing normalization

In the inspected v3 `main.tex`, the displayed definition first writes a word
`B=x_0...x_ell` and then takes the least common multiple over
`i=1,...,ell`, omitting `x_0`; the immediately following initial block is
indexed from zero.  This is recorded as a narrow indexing defect rather than
silently quoted as consistent text.  The candidate's theorem contract
explicitly freezes the common period of all positions.  Section 3 of
`INDEPENDENT_PROOF.md` additionally proves that the prime/composite result
is unchanged even if the displayed omission is read literally, so this
source defect is not a theorem blocker.

## Collision decision

Neither primary owner contains the conjunction of the exact affine object,
all same-base pointed sliding-block maps, arbitrary-radius collapse to a
unique letter quotient, and the independent-partition refinement poset.
The bounded source gate therefore finds no exact collision.  Any later
primary source with that same conjunction and those same quantifiers remains
a stop condition.

