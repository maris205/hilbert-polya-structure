# Citation Verification

Verification date and bounded-search cutoff: **2026-08-14 UTC**.

Scope: primary publisher, society/library, and arXiv records for the eleven
sources frozen in Paper 9.  This is a metadata-and-claim-role lock, not an
exhaustive literature review and not evidence of priority.

The citation package is bound to source-lock SHA-256
`662809d40f7e409e439983774a36349b90f265616a488061fda3c5b9064c2d49`,
proof SHA-256
`47216ad4021d3476bfd0850ebec24c9ceafb5af8c0573214182fd2d0da7b2daa`,
raw-result SHA-256
`448de06e92bd7ab4e5374e5d1f57413df45859cd3476ff14b2691b63ac364fab`,
independent result-review SHA-256
`aa0c7db555f11920c7305be508f6cfff62375970e112e9f720111831da20b3bd`,
and passing strict manifest SHA-256
`8ca12744638a47b6e4fa3239a60a19d79229d2b9596ae4fe4b2f66a399618f92`.

## Verification rules

1. A source supports only the role recorded below.
2. Gaspari 1994 and Baake--Neumärker--Roberts 2013 are direct novelty
   collisions, not generic background.
3. Classical zeta/weighted-product sources delimit scope; Paper 9 claims no
   transfer-operator, determinant, or continuation novelty.
4. Tan--Li 2025 and Chandra 2026 are cited as arXiv preprints.  Their
   arXiv-issued DataCite DOIs are not journal DOIs.
5. The bibliography key set must be exactly the eleven headings below, with
   no unverified auxiliary source.

## Source-by-source lock

### `Gaspari1994` — direct prime-lattice classification collision

- Gregory Gaspari, “The Arnold cat map on prime lattices,” *Physica D:
  Nonlinear Phenomena* **73**(4), 352--372 (1994).
- DOI: <https://doi.org/10.1016/0167-2789(94)90105-8>.
- Publisher record:
  <https://www.sciencedirect.com/science/article/pii/0167278994901058>.
- **Verified role:** the publisher abstract explicitly states that, for
  prime (p\ne5), all nonzero lattice points have a common period and that
  the orbit decomposition is determined.  This must be cited beside C1.
- **Prohibited use:** no Paper-9 priority claim for common prime-shell periods
  or orbit decomposition.

### `PercivalVivaldi1987` — foundational arithmetic cat-map context

- Ian C. Percival and Franco Vivaldi, “Arithmetical properties of strongly
  chaotic motions,” *Physica D: Nonlinear Phenomena* **25**(1--3), 105--130
  (1987).
- DOI: <https://doi.org/10.1016/0167-2789(87)90096-0>.
- Publisher record:
  <https://www.sciencedirect.com/science/article/pii/0167278987900960>.
- **Verified role:** modular and quadratic-integer classification of periodic
  cat-map orbits.
- **Prohibited use:** not evidence for the scalar denominator obstruction.

### `DysonFalk1992` — discrete period arithmetic context

- Freeman J. Dyson and Harold Falk, “Period of a Discrete Cat Mapping,”
  *The American Mathematical Monthly* **99**(7), 603--614 (1992).
- DOI: <https://doi.org/10.1080/00029890.1992.11995900>.
- Stable record: <https://www.jstor.org/stable/2324989>.
- Publisher record:
  <https://www.tandfonline.com/doi/abs/10.1080/00029890.1992.11995900>.
- **Verified role:** classical discrete-cat period context.
- **Prohibited use:** no attribution of the Paper-9 weight obstruction to
  this article.

### `BaakeRobertsWeiss2008` — finite/rational-lattice Euler-product collision

- Michael Baake, John A. G. Roberts, and Alfred Weiss, “Periodic orbits of
  linear endomorphisms on the 2-torus and its lattices,” *Nonlinearity*
  **21**, 2427--2446 (2008).
- DOI: <https://doi.org/10.1088/0951-7715/21/10/012>.
- Primary manuscript: <https://arxiv.org/abs/0808.3489>.
- **Verified role:** the primary record explicitly studies global/local orbit
  counting and dynamical-zeta analogues on finite lattices.
- **Prohibited use:** Paper 9 cannot claim a new finite-lattice Euler product
  or global/local toral-zeta theory.

### `BaakeNeumaerkerRoberts2013` — boundary-cycle and symmetry collision

- Michael Baake, Natascha Neumärker, and John A. G. Roberts, “Orbit
  structure and (reversing) symmetries of toral endomorphisms on rational
  lattices,” *Discrete and Continuous Dynamical Systems* **33**(2), 527--553
  (2013).
- DOI: <https://doi.org/10.3934/dcds.2013.33.527>.
- Publisher record:
  <https://www.aimsciences.org/article/doi/10.3934/dcds.2013.33.527>.
- **Verified role:** Appendix A.1 is the direct cycle-generating-polynomial
  collision for the standard cat map, including the (p=2) and (p=5)
  boundaries; the article also supplies symmetry/centralizer context.
- **Prohibited use:** Paper 9 neither discovers these boundary cycles nor
  rules out a centralizer quotient.

### `ArtinMazur1965` — classical fixed-point exponential

- Michael Artin and Barry Mazur, “On periodic points,” *Annals of
  Mathematics*, Second Series, **81**(1), 82--99 (1965).
- DOI/stable record: <https://doi.org/10.2307/1970384>.
- Issue record: <https://www.jstor.org/stable/i307331>.
- **Verified role:** classical fixed-point exponential and periodic-point
  zeta framework.
- **Prohibited use:** no novelty claim for grouping fixed points by primitive
  cycles.

### `Ruelle1976` — weighted zeta and analytic machinery boundary

- David Ruelle, “Zeta-functions for expanding maps and Anosov flows,”
  *Inventiones Mathematicae* **34**(3), 231--242 (1976).
- DOI: <https://doi.org/10.1007/BF01403069>.
- **Verified role:** weighted dynamical-zeta and operator-theoretic prior art.
- **Prohibited use:** the finite scalar degree argument is not a new transfer
  theorem and excludes no matrix/Fredholm/cohomological cancellation.

### `ParryPollicott1990` — primitive/repetition and H\"older-weight formalism

- William Parry and Mark Pollicott, *Zeta Functions and the Periodic Orbit
  Structure of Hyperbolic Dynamics*, Astérisque **187--188** (1990),
  Soci\'et\'e Math\'ematique de France.
- DOI: <https://doi.org/10.24033/ast.28>.
- Primary library record:
  <https://numdam.org/item/AST_1990__187-188__1_0/>.
- The SMF product record and Numdam catalogue report different physical page
  totals, so the locked bibliography intentionally omits a total-page field.
- **Verified role:** standard primitive-orbit/repetition and weighted-product
  framework.
- **Prohibited use:** Paper 9 does not extend the analytic theory or prove
  that richer determinants cannot cancel multiplicity.

### `BaakeLauPaskunas2010` — ordinary toral zeta boundary

- Michael Baake, Eike Lau, and Vytautas Paskunas, “A note on the dynamical
  zeta function of general toral endomorphisms,” *Monatshefte für
  Mathematik* **161**(1), 33--42 (2010).
- DOI: <https://doi.org/10.1007/s00605-009-0118-y>.
- Primary manuscript: <https://arxiv.org/abs/0810.1855>.
- **Verified role:** the arXiv record binds the journal metadata and states
  the ordinary Artin--Mazur/Lefschetz toral-zeta result.
- **Prohibited use:** the externally relabeled prime-shell product is not
  “the” dynamical zeta function of the cat map.

### `TanLi2025` — contemporary prime-power cycle context

- Kai Tan and Chengqing Li, “The Graph Structure of a Class of Permutation
  Maps over Ring (\mathbb Z_{p^k}),” arXiv:2506.20118 [math.NT] (2025).
- Primary record: <https://arxiv.org/abs/2506.20118>.
- Submitted 25 June 2025; arXiv record lists 11 pages and one figure.
- **Verified role:** exact cycle-length distributions and lifting over
  prime-power rings, with the cat map as a canonical example.
- **Prohibited use:** no broad claim of new finite-ring cat-map cycle
  analysis.

### `Chandra2026` — contemporary finite-permutation product collision

- Aryaman Chandra, “Arithmetic Landscape Functions of a Discrete Cat Map,”
  arXiv:2607.24857 [math.DS] (2026).
- Primary record: <https://arxiv.org/abs/2607.24857>.
- Submitted 26 July 2026; arXiv record lists 15 pages and six figures.
- **Verified role:** finite-torus Green-function and exact cycle-product/
  determinant packaging.
- **Prohibited use:** Paper 9 claims no determinant, Green-function,
  localization, or spectral-landscape novelty.

## Collision and wording audit

| Frozen component | Closest verified collision | Allowed Paper-9 delta |
|---|---|---|
| common nonramified prime-shell period and orbit decomposition | Gaspari 1994 | re-derive in split/inert notation and isolate the lower bound used by the obstruction |
| (p=2,5) cycle boundaries | Baake--Neumärker--Roberts 2013, Appendix A.1 | place both boundaries in one all-prime multiplicity audit |
| finite-lattice cycle Euler products | Baake--Roberts--Weiss 2008; Chandra 2026 | distinguish raw returns from external one-time orbit labels |
| weighted primitive/repetition product | Ruelle 1976; Parry--Pollicott 1990 | elementary, explicitly scoped scalar denominator-degree test |
| prime-power cycle structure | Tan--Li 2025 | no new finite-ring classification claim |

The defensible position remains:

> Classical prime-lattice orbit structure forces a multiplicity exponent in
> the most direct prime-shell orbit product; ordinary nonzero scalar weights
> cannot remove it, and the exact fractional repair is shell-global and
> non-specific.

Absence of an exact A0 decision package in this bounded search is not evidence
of historical priority.  The novelty score remains **2.5--3/10** after the
passing experiment.

## Mechanical closure required before manuscript use

- `paper/references.bib` must parse with exactly eleven unique keys.
- The plan citation keys, this ledger's headings, and the BibTeX keys must be
  identical.
- No `[VERIFY]`, placeholder DOI, unverified journal status, or unused entry
  is permitted.
- A fresh independent plan/figure reviewer must check metadata, claim roles,
  and key-set equality before manuscript drafting.
