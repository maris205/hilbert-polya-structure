# P168 source verification and subtraction log

**Metadata check:** 2026-09-03 UTC  
**Rule:** cited claims checked on primary publisher/preprint surfaces  
**External lifecycle:** `GREEN_OWNER_THIN / HOLD_EXTERNAL`

## Literal convention searched

The search fixed the actual iterate rather than the raw inverse function:

```text
A <= F_(p^4)  ->  span_Fp {a^(-1): a in A, a != 0}.
```

Exact combinations of `span of inverses`, `inverse-span dynamics`, `subspace
lattice`, `functional graph`, `quartic`, `preimage/fibre`, and `zeta` were
queried together with the known inverse-subspace papers.  No inspected source
stated the complete iterated graph or all-time fibre atlas.  This bounded
non-hit is not a novelty or priority result.

## Verified cited records

| Key | Primary metadata | Claim actually supported | Credit in P168 |
|---|---|---|---|
| `KolomeecBykov2024` | N. Kolomeec, D. Bykov, *Designs, Codes and Cryptography* 92(2), 467--476 (2024), DOI `10.1007/s10623-023-01316-3` | Springer abstract: for patched inversion on `F_{p^n}`, an affine `F_p`-subspace of size greater than two has affine image iff it is a nonzero scalar subfield | **direct theorem input; zero contribution** |
| `FainaEtAl2002` | G. Faina, G. Kiss, S. Marcugini, F. Pambianco, *European Journal of Combinatorics* 23(1), 31--35 (2002), DOI `10.1006/eujc.2001.0525` | Elsevier abstract: the inverse of a projective line in the cyclic model is a normal rational curve in a suitable subspace | **direct geometric input; zero contribution** |
| `LavrauwZanella2014` | M. Lavrauw, C. Zanella, *Journal of Geometry* 105(1), 103--110 (2014), DOI `10.1007/s00022-013-0197-8` | Springer abstract: detailed inverse-line geometry; for small fields the construction gives independent `(q+1)`-tuples | **direct geometric input; zero contribution** |
| `Mattarei2007` | S. Mattarei, *Israel Journal of Mathematics* 159, 343--347 (2007), DOI `10.1007/s11856-007-0050-6` | Springer abstract: classification of inversion-closed additive subgroups, including the odd-characteristic trace-zero alternative | background only; zero contribution |
| `Csajbok2013` | B. Csajbók, *Finite Fields and Their Applications* 19(1), 55--66 (2013), DOI `10.1016/j.ffa.2012.10.005` | Elsevier abstract: equal-dimensional subspaces with large inverse intersections, using finite-field/Singer geometry | background only; zero contribution |
| `ArtinMazur1965` | M. Artin, B. Mazur, *Annals of Mathematics* 81(1), 82--99 (1965), DOI `10.2307/1970384` | primary journal record for the periodic-point zeta framework | terminology/conversion only; zero contribution |

The article years use print issue years: Kolomeec--Bykov appeared online in
2023 and in volume 92 in 2024; Lavrauw--Zanella appeared online in 2013 and in
volume 105 in 2014.  `references.bib` uses the print issue years consistently.

## Stable primary links

- <https://link.springer.com/article/10.1007/s10623-023-01316-3>
- <https://www.sciencedirect.com/science/article/pii/S0195669801905256>
- <https://link.springer.com/article/10.1007/s00022-013-0197-8>
- <https://link.springer.com/article/10.1007/s11856-007-0050-6>
- <https://www.sciencedirect.com/science/article/pii/S1071579712000937>
- <https://doi.org/10.2307/1970384>

Author preprints used to check mathematical wording:

- <https://arxiv.org/abs/2206.14980>
- <https://arxiv.org/abs/1311.4309>
- <https://arxiv.org/abs/math/0511538>

## Claim subtraction

The equality-case classification is not merely related work: it is an
essential cited lemma.  The inverse-line rank calculation in the manuscript
is included for self-containment, but the normal-rational-curve and
small-field independence phenomena are already published.  The manuscript
therefore does not claim either result.

The residual is the degree-four finite-dynamical integration:

```text
sharp binary/odd depth dichotomy
+ complete functional graph and image stabilization
+ complete all-time every-target fibres.
```

Fixed-cycle and zeta formulas are short consequences once the direct inputs
are accepted; they are secondary parts of the package, not independent
ownership evidence.

## Bibliography integrity

The six BibTeX entries were retrieved or cross-checked against DOI/Crossref
metadata and then normalized to the publisher's print record.  Every entry is
cited in `main.tex`; no uncited record, `[VERIFY]` marker, or invented source
remains.

## Decision boundary

The source status remains `HOLD_EXTERNAL`.  A later source owning the literal
iteration, the degree-four graph, or the target-fibre atlas reopens the slot.
No external posting or submission follows from this Round-0 bibliography
check.
