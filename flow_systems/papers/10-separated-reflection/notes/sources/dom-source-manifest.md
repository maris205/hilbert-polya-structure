# Paper 10 Phase-2 independent domain-source manifest

Frozen: **2026-08-14 (Asia/Shanghai)**  
Scope: independent domain audit for topological-group separation, `T0`
reflection, operator topologies, measurable/finite-measure terminology,
indiscrete Borel structure, coproduct topology, and topology-direction checks.  
Checksum ledger: `dom-sources.sha256`

## 1. Retained full texts

Every retained file has a distinct `dom-*` name and an adjacent ARS
`pdf_read_preflight/1.0.0` sidecar with verdict `PASS`, identical
declared/enumerated/reader page counts, and no warnings.

| ID | Exact local full text | Canonical endpoint / manifestation | Pages | PDF SHA-256 | Preflight SHA-256 | Redistribution class |
|---|---|---|---:|---|---|---|
| `DOM-HOF-TG` | `dom-topological-groups-waterloo.pdf` | K. H. Hofmann, *Introduction to Topological Groups: An Introductory Course*, Winter 2005 course notes, university-hosted copy: <https://www.math.uwaterloo.ca/~cgodsil/pdfs/topology/topgr.pdf> | 58 | `ba816acc88ffaf1c5aa9a99557fe12ba6b6c0d186b0faf17487296321d79cd4b` | `5b7046d8f563025e368c6090273c4f3cdbfb243d94816f45a7e9fd8b0f6c4730` | `LOCAL_RESEARCH_ONLY`: academic-hosted; no redistribution licence found in the manifestation |
| `DOM-CAG-T0` | `dom-t0-reflection-cagliari.pdf` | F. Cagliari and S. Mantovani, *T0-reflection and injective hulls of fibre spaces*, author-hosted preprint of *Topology and its Applications* 132 (2003), 129--138, DOI `10.1016/S0166-8641(02)00370-X`: <https://www.dm.unibo.it/~cagliari/articoli/toinject.pdf> | 11 | `c9502fc3172103847e2627627cc4cba507dad8e0e7e42d1b67abeb1ee3854634` | `3c76f60257dd370b60149721fa4893812bd855f546eaf9289ff1f91d8f0eb41e` | `LOCAL_RESEARCH_ONLY`: author-hosted; no redistribution licence found in the manifestation |
| `DOM-HOR-OP` | `dom-operator-topologies-vienna.pdf` | G. Hoermann, *C*-Algebras with Aspects of Quantum Physics*, Winter 2023/24 lecture notes, version 2026-08-06, author/university endpoint: <https://www.mat.univie.ac.at/~gue/lehre/2324CStarQP/CAQP.pdf> | 112 | `c496ccc9152e4883742d6f8ed86881b1e46f2758ee2c005a90aee4949643bffc` | `02157b6c2026fb53f92b5e5e8f8ebd86bb3cf70dd7df5c1dfd4bcd7f532cd549` | `LOCAL_RESEARCH_ONLY`: author-hosted; no redistribution licence found in the manifestation |
| `DOM-FRE-MEAS` | `dom-fremlin-measure-spaces-ch11.pdf` | D. H. Fremlin, *Measure Theory* (abridged/results-only), Chapter 11, author/university endpoint: <https://www1.essex.ac.uk/maths/people/fremlin/chap11.ro.pdf> | 10 | `0cb220afe041d52ca5a522604c3bd4a063bd04acdb3b7a03e3c68b53e8830d5d` | `1c66d11241c6c91d65558e68c1a855fe0bccb4e441a3c3139735b9d3913cf539` | `LICENSED_COPYLEFT_CONDITIONAL`: the PDF states the Design Science License; redistribution must preserve its terms and notices |
| `DOM-AND-TOP` | `dom-point-set-topology-andre.pdf` | R. Andre, revised Part-II sample from *Point-set topology with topics: Basic general topology for graduate studies*, university/author endpoint: <https://www.math.uwaterloo.ca/~randre/sets/revised1.pdf> | 176 | `7a21d873d819e8729922a564b6cfc4a6f685b3bbf3b99ca9983493d547db162f` | `419feb8fa5414fc7a35ede7fb66782a2c122b390c1074253b34a8d98e5eb2658` | `LOCAL_RESEARCH_ONLY`: copyrighted book sample; no redistribution licence found in the manifestation |

ASCII transliterations are used in filenames and this manifest only to keep
the ledger portable; the PDFs identify the authors as Guenther Hoermann and
Robert Andre with diacritics.

## 2. Load-bearing locator index

### `DOM-HOF-TG`

- physical p. 5, Exercise E1.3(ii)--(iii): quotient topology on `G/H` and
  `G/H` Hausdorff exactly when `H` is closed;
- physical p. 6, Examples 1.9(ii) and Proposition 1.10(iii): every abstract
  group with the indiscrete topology is a topological group, and a normal
  quotient with quotient topology is a topological group;
- physical pp. 10--11, Theorem 1.17 and Corollaries 1.18--1.19: for a
  topological group, `T0`, closed identity, `T1`, and regular Hausdorff are
  equivalent; quotient by the closure of the identity gives the universal
  Hausdorff group factor. The mathematical overbar is lost in plain-text PDF
  extraction, so the PDF image is controlling.

### `DOM-CAG-T0`

- physical pp. 3--4, Section 2: `Top0` is reflective in `Top`; the unit is
  the topological quotient on indiscrete components and has the displayed
  unique-factorization property into every `T0` space.

### `DOM-HOR-OP`

- physical p. 43 / printed p. 39, Section 4.1: SOT and WOT on the common
  carrier `B(H)` are explicitly Hausdorff locally convex topologies generated
  by the point and matrix-coefficient seminorms; norm is finer than SOT,
  which is finer than WOT.

### `DOM-FRE-MEAS`

- physical p. 4, Section 111A: sigma-algebra definition;
- physical p. 5, Sections 111G and 112A: generated sigma-algebra (including
  the trivial example) and positive countably additive measure;
- physical p. 6, Section 112B(d): Dirac measure, defined by membership of the
  measurable set, and the distinction between a measure's domain and an
  arbitrary subset.

### `DOM-AND-TOP`

- physical pp. 5--6 / printed pp. 39--40, Definition 3.3 and Example 4:
  finer/coarser topologies and the indiscrete topology;
- physical pp. 17--18 / printed pp. 51--52, Theorem 3.11 and following
  paragraph: Borel sigma-algebra generation and the fact that a nonempty
  proper subset is not Borel in an indiscrete space;
- physical pp. 18--19 / printed pp. 52--53, Definition 3.12: tagged free
  union and the disjoint-union topology, with each component clopen.

## 3. Web-only authoritative cross-checks

These pages are cited by stable URL and were not retained as local full
texts:

- The Stacks Project, Tag `0B1W`, gives the coproduct topology and set-level
  disjoint union: <https://stacks.math.columbia.edu/tag/0B1W>.
- Encyclopedia of Mathematics, *Standard Borel space*, gives equivalent
  standard-Borel definitions and explicitly places standard Borel spaces
  inside the countably separated class:
  <https://encyclopediaofmath.org/wiki/Standard_Borel_space>.
- Terence Tao, *245B, notes 0*, lines under Definitions 1--2 and Example 7,
  defines measures and Dirac masses on arbitrary measurable spaces:
  <https://terrytao.wordpress.com/2009/01/01/245b-notes-0-a-quick-review-of-measure-and-integration-theory/>.
- Chao Li, *Class field theory* notes, Definition 32/Remark 25 and Definition
  33, separate quotient-group topology/Hausdorffness from the LCH-Hausdorff
  hypothesis used for Haar/Radon language:
  <https://www.math.columbia.edu/~chaoli/docs/ClassFieldTheory.html>.
- Encyclopedia of Mathematics, *Topological structures*, records `Haus` as an
  extremal epireflective subcategory of `Top`:
  <https://encyclopediaofmath.org/wiki/Topological_structures>.

## 4. Reused Paper-9 primary source by hash

No duplicate Paper-10 copy is retained. The exact arithmetic owner remains
Paper 9's `P9-DEN-DYN-v4`:

- PDF SHA-256
  `edd0bc8c2efb601ed7574e8eceae40e8cde21d0e4b2bc8c4ce7e60d8e1f82a09`;
- preflight SHA-256
  `0526c6a84b907d109db4e2932cbb378b60b172dce8981c034d866e398a25a9e4`;
- Paper-9 source manifest SHA-256
  `8dd678dc33fa7396484c8c8d63a91943f6755da24eedefa0471860fa94e42906`.

Its permitted role remains set/action/stabilizer and exact Deninger-object
ownership. It does not own Paper 10's transported group law, actual-topology
character classification, separated reflections, Borel/measure
classification, fixed-operator observables, or copied coproduct.

## 5. Retention and public-sync boundary

The five PDFs are local verification copies. The four `LOCAL_RESEARCH_ONLY`
PDFs must not be pushed to a public Git repository without separate permission.
The Fremlin file is copyleft but public redistribution is conditional on the
Design Science License and notices, so this audit does not itself authorize a
push. The manifest, `dom-sources.sha256`, URLs, locators, and preflight
sidecars are safe metadata for normal public synchronization.
