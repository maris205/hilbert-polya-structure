# Citation Verification

Verification date and search cutoff: **2026-08-14 UTC**.

Scope: primary publisher records, society/library records, and author-posted
or arXiv primary manuscripts. This is a metadata-and-claim-role lock for
Paper 8, not an exhaustive literature review and not proof that no closer
statement exists.

> `FINAL RESULT MANIFEST / POST-RUN ANALYZER CLOSURE: PASS`.
> The read-only V2 closure is bound to manifest SHA-256
> `045f3c3d935cd5670e900a210be9d26a2e272bd715c8e0b997da6510efd7d49f`
> and independent Round-2 `POSTRUN_ANALYZER_PASS` review SHA-256
> `42e4e2010be2d5cbb51a2ceb1fd9a1f8048bcec17daa2767c9f38cebaaa6fdcd`.
> This status update changes no citation metadata or claim role.

> **ROUND-1 BOUNDED CITATION CLOSURE: PASS AUTHOR SIDE / AWAITING
> INDEPENDENT ROUND 2.**  The revision adds only the locally verified
> ordinary-period references `KannanEtAl2011Periods` and
> `Seibt2003Period`.  The resulting 14-key bibliography compiles without a
> BibTeX warning and has SHA-256
> `0fd74e7688739c8a3eb44ea995f950250c0a9afcfc99699824bd57e753e21ba9`.
> No network re-resolution was repeated during this bounded revision; all
> identifiers and URLs remain tied to the verified 2026-08-14 cutoff and the
> local novelty/citation records.  This author-side closure is not an
> independent Round-2 verdict.

## Verification rules

1. A source may support only the role recorded below.
2. Flatters' imported theorem must retain its positive quadratic norm-one
   hypotheses. Paper 8's negative-trace conversion is not attributed to it.
3. Classical dynamical-zeta/transfer and quantum-cat sources delimit scope;
   Paper 8 claims no novelty in those fields.
4. Recent sources without verified journal publication are cited as arXiv
   preprints. An arXiv-issued DataCite DOI is not described as a journal DOI.
5. Titles, authors, years, venues, volumes/issues, pages, and identifiers in
   `paper/references.bib` were checked against the records linked here.

## Source-by-source lock

### `Flatters2009Primitive` — verified journal article and primary theorem text

- Anthony Flatters, “Primitive Divisors of Some Lehmer--Pierce Sequences,”
  *Journal of Number Theory* **129**(1), 209--219 (2009).
- Journal DOI: <https://doi.org/10.1016/j.jnt.2008.05.008>.
- Publisher record: <https://www.sciencedirect.com/science/article/pii/S0022314X08001224>.
- Primary manuscript: <https://arxiv.org/abs/0708.2190>;
  theorem text: <https://arxiv.org/html/0708.2190v1>.
- **Allowed use:** Theorem 1.4 for primitive rational prime divisors beyond
  index 12 for positive norm-one quadratic units; Theorem 3.1 and its table
  for the norm-one small-index classification, including the standard unit
  \((3+\sqrt5)/2\) and the fact needed at indices (7,9,11).
- **Attribution guard:** the theorem text states different behavior for
  norm (-1) units. Paper 8 applies the norm-one result to (B=-M) and then
  proves its own odd/(4\mid n)/half-index period conversion. Never write
  “Flatters proves the negative-trace carrier theorem.”

### `Gaspari1994Arnold` — verified journal article

- Gregory Gaspari, “The Arnold Cat Map on Prime Lattices,” *Physica D:
  Nonlinear Phenomena* **73**(4), 352--372 (1994).
- DOI: <https://doi.org/10.1016/0167-2789(94)90105-8>.
- Publisher record: <https://www.sciencedirect.com/science/article/pii/0167278994901058>.
- **Allowed use:** classical fixed-prime-lattice common-period and orbit
  decomposition context, with (p=5) recognized as exceptional/ramified.
- **Non-use:** it does not establish Paper 8's cross-prime prescribed-period
  theorem or its packaged exception set.

### `PercivalVivaldi1987Arithmetic` — verified journal article

- Ian C. Percival and Franco M. Vivaldi, “Arithmetical Properties of Strongly
  Chaotic Motions,” *Physica D: Nonlinear Phenomena* **25**(1--3), 105--130
  (1987).
- DOI: <https://doi.org/10.1016/0167-2789(87)90096-0>.
- Publisher record: <https://www.sciencedirect.com/science/article/pii/0167278987900960>.
- **Allowed use:** classical modular-arithmetic and quadratic-ideal
  classification of generalized cat-map periodic orbits.
- **Non-use:** not evidence of priority for Paper 8's exact packaged theorem.

### `DysonFalk1992Period` — verified journal article; dual identifier recorded

- Freeman J. Dyson and Harold Falk, “Period of a Discrete Cat Mapping,”
  *The American Mathematical Monthly* **99**(7), 603--614 (1992).
- Current publisher DOI: <https://doi.org/10.1080/00029890.1992.11995900>.
- Publisher record: <https://www.tandfonline.com/doi/abs/10.1080/00029890.1992.11995900>.
- Legacy JSTOR stable DOI/identifier used in older bibliographies:
  <https://doi.org/10.2307/2324989>.
- **Allowed use:** global period/order behavior of a discrete cat mapping on
  rational lattices.
- **BibTeX decision:** use the current publisher DOI in the `doi` field and
  preserve the JSTOR identifier in `note`; do not list them as two papers.

### `KannanEtAl2011Periods` — verified journal article and primary PDF

- V. Kannan, I. Subramania Pillai, K. Ali Akbar, and B. Sankararao,
  “The Set of Periods of Periodic Points of a Toral Automorphism,”
  *Topology Proceedings* **37**, 219--232 (2011).
- Primary journal PDF:
  <https://topology.nipissingu.ca/tp/reprints/v37/tp37014.pdf>.
- **Allowed use:** the ordinary-period baseline: for a hyperbolic
  two-torus automorphism, the period set is \(\mathbb N\) or
  \(\mathbb N\setminus\{2\}\).
- **Non-use:** the theorem imposes no additive-order or denominator
  constraint and does not prove the cross-prime carrier theorem recorded in
  Paper 8.

### `Seibt2003Period` — verified journal article

- Peter Seibt, “A Period Formula for Torus Automorphisms,” *Discrete and
  Continuous Dynamical Systems* **9**(4), 1029--1048 (2003).
- DOI and publisher record:
  <https://doi.org/10.3934/dcds.2003.9.1029>.
- **Allowed use:** rational-lattice/global matrix period-formula context.
- **Non-use:** it does not impose prime additive order and is not evidence
  for Paper 8's prescribed cross-prime carrier theorem.

### `BaakeRobertsWeiss2008Periodic` — verified journal article

- Michael Baake, John A. G. Roberts, and Alfred Weiss, “Periodic Orbits of
  Linear Endomorphisms on the 2-Torus and Its Lattices,” *Nonlinearity*
  **21**(10), 2427--2446 (2008).
- DOI: <https://doi.org/10.1088/0951-7715/21/10/012>.
- Primary manuscript/journal reference: <https://arxiv.org/abs/0808.3489>.
- **Allowed use:** global/local orbit counts, rational-lattice orbit
  structure, and local dynamical-zeta context.
- **Non-use:** no claim that its zeta constructions are extended here.

### `BaakeNeumaerkerRoberts2013Orbit` — verified journal article

- Michael Baake, Natascha Neumärker, and John A. G. Roberts, “Orbit Structure
  and (Reversing) Symmetries of Toral Endomorphisms on Rational Lattices,”
  *Discrete and Continuous Dynamical Systems* **33**(2), 527--553 (2013).
- DOI: <https://doi.org/10.3934/dcds.2013.33.527>.
- Publisher record: <https://www.aimsciences.org/article/doi/10.3934/dcds.2013.33.527>.
- Primary manuscript: <https://arxiv.org/abs/1205.1003>.
- **Allowed use:** rational-lattice orbit structure and symmetry context.
- **Non-use:** not an imported quantum result despite the publisher abstract's
  note about relevance to quantum cat maps.

### `TanLi2025Graph` — verified arXiv preprint only

- Kai Tan and Chengqing Li, “The Graph Structure of a Class of Permutation
  Maps over Ring \(\mathbb Z_{p^k}\),” arXiv:2506.20118 [math.NT], submitted
  25 June 2025, 11 pages, one figure.
- Primary record: <https://arxiv.org/abs/2506.20118>.
- arXiv-issued DOI: <https://doi.org/10.48550/arXiv.2506.20118>.
- **Status decision:** no stable final journal venue or journal DOI was
  verified at the cutoff; cite as a 2025 preprint. Do not infer publication
  metadata from headers in an experimental HTML rendering.
- **Allowed use:** recent neighboring work on cycle distributions and lifting
  over \(\mathbb Z_{p^k}\), including cat-map examples.

### `Chandra2026Arithmetic` — verified arXiv preprint only

- Aryaman Chandra, “Arithmetic Landscape Functions of a Discrete Cat Map,”
  arXiv:2607.24857 [math.DS], submitted 26 July 2026, 15 pages, six figures.
- Primary record: <https://arxiv.org/abs/2607.24857>.
- arXiv-issued DOI: <https://doi.org/10.48550/arXiv.2607.24857>.
- **Allowed use:** recent neighboring transfer/Green-function and
  orbit-length-landscape context; it blocks any broad novelty suggestion for
  a spectral object that merely records cat-map orbit length.
- **Non-use:** Paper 8 imports none of its Green, transfer, zeta, or
  perturbation identities and makes no transfer-operator novelty claim.

### `Ruelle1976Zeta` — verified journal article

- David Ruelle, “Zeta-Functions for Expanding Maps and Anosov Flows,”
  *Inventiones Mathematicae* **34**(3), 231--242 (1976).
- DOI: <https://doi.org/10.1007/BF01403069>.
- Author-hosted primary article PDF:
  <https://www.ihes.fr/~ruelle/PUBLICATIONS/%5B45%5D.pdf>.
- **Allowed use:** foundational dynamical-zeta context for hyperbolic
  dynamics.
- **Non-use:** Paper 8 constructs no new dynamical zeta or transfer operator.

### `ParryPollicott1990Zeta` — verified research monograph

- William Parry and Mark Pollicott, *Zeta Functions and the Periodic Orbit
  Structure of Hyperbolic Dynamics*, *Astérisque* nos. 187--188, Société
  Mathématique de France (1990).
- DOI: <https://doi.org/10.24033/ast.28>.
- Society record: <https://smf.emath.fr/publications/zeta-functions-and-periodic-orbit-structure-hyperbolic-dynamics>.
- Numdam bibliographic/full-text record:
  <https://numdam.org/item/AST_1990__187-188__1_0/>.
- **Metadata note:** the society product page currently reports 284 pages,
  while the Numdam bibliographic record reports 272 pages and other
  bibliographies often report 268 pages of main text. The BibTeX entry omits
  `pagetotal` rather than choosing among non-equivalent counts.
- **Allowed use:** standard periodic-orbit/zeta/transfer formalism context.
- **Non-use:** no transfer or zeta novelty is claimed by Paper 8.

### `HannayBerry1980Quantization` — verified journal article

- J. H. Hannay and M. V. Berry, “Quantization of Linear Maps on a
  Torus---Fresnel Diffraction by a Periodic Grating,” *Physica D: Nonlinear
  Phenomena* **1**(3), 267--290 (1980).
- DOI: <https://doi.org/10.1016/0167-2789(80)90026-3>.
- Publisher record: <https://www.sciencedirect.com/science/article/pii/0167278980900263>.
- **Allowed use:** foundational quantum-cat/torus-map context.
- **Non-use:** the classical torsion-order label is not presented as a
  quantized observable or operator construction.

### `KurlbergRudnick2000Hecke` — verified journal article and primary preprint

- Pär Kurlberg and Zeév Rudnick, “Hecke Theory and Equidistribution for the
  Quantization of Linear Maps of the Torus,” *Duke Mathematical Journal*
  **103**(1), 47--77 (2000).
- DOI: <https://doi.org/10.1215/S0012-7094-00-10314-6>.
- Primary manuscript: <https://arxiv.org/abs/chao-dyn/9901031>.
- Institutional publication record:
  <https://cris.tau.ac.il/en/publications/hecke-theory-and-equidistribution-for-the-quantization-of-linear-/>.
- **Allowed use:** Hecke symmetries and equidistribution in quantum cat maps,
  solely to delimit the quantum literature.
- **Non-use:** Paper 8 proves no quantum equidistribution, degeneracy, or
  operator theorem.

## Claim-to-citation map

| Paper 8 statement | Required citations | What remains Paper 8's own derivation |
|---|---|---|
| Positive-trace carriers for all (n>12) | `Flatters2009Primitive` | determinant/norm identification for (M), kernel-to-carrier lemma, formulation |
| Negative-trace carriers for all (n>12) | `Flatters2009Primitive` | the complete three-case conversion through (B=-M), including half-index and (p\ne2) arguments |
| Standard-cat small determinant exceptions | `Flatters2009Primitive` | conversion from determinant divisors to carriers; direct exclusions |
| Standard-cat prime-lattice period profiles | `Gaspari1994Arnold` plus direct proof | exact mod-(2,3,5) verification and (p=5) Jordan count |
| Ordinary period-set baseline without additive-order constraint | `KannanEtAl2011Periods`, `Seibt2003Period` | the extra prime-additive-order condition and cross-prime synthesis |
| Broader arithmetic/rational-lattice context | `PercivalVivaldi1987Arithmetic`, `DysonFalk1992Period`, both Baake entries | the cross-prime prescribed-period synthesis |
| Recent fixed-ring/landscape collision boundary | `TanLi2025Graph`, `Chandra2026Arithmetic` | no imported theorem; bounded novelty positioning only |
| Zeta/transfer boundary | `Ruelle1976Zeta`, `ParryPollicott1990Zeta` | no zeta or transfer construction |
| Quantization boundary | `HannayBerry1980Quantization`, `KurlbergRudnick2000Hecke` | no quantization construction |

## Final bibliography checks

- [x] Every planned citation key has one entry in `paper/references.bib`.
- [x] No unverified journal metadata is assigned to Tan--Li or Chandra.
- [x] Both Dyson--Falk identifiers are documented without duplicate entries.
- [x] Parry--Pollicott pagination ambiguity is not encoded as a false exact
      value.
- [x] Diacritics in Neumärker, Pär, and Zeév are preserved through BibTeX
      escapes.
- [x] No citation is used to imply transfer/quantization novelty.
- [x] No citation is used to imply that a bounded search proves priority.
- [x] Kannan et al. and Seibt are used only for the unconstrained
      ordinary-period/rational-lattice baseline, not for the prime-order
      carrier theorem.
- [x] The revised 14-entry bibliography compiles with 14 cited keys, zero
      missing or unused key, and zero BibTeX warning.
- [x] URL re-resolution was not repeated in Round 1; the verified cutoff is
      retained explicitly rather than silently reporting a new online check.
