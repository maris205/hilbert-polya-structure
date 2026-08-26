# P68 Stage 2.5 source-search ledger

Audit date: 2026-08-26 (UTC).  Search horizon: public material indexed or
published through 2026-08-26.  This ledger records the exact bounded searches
used for bibliographic verification, citation-context checking, phrase
screening, and nearest-neighbour screening.  A URL below is the direct source
URL, not a search-results URL.

## A. Bibliography-entry verification

Protocol: every entry in `references.bib` was searched independently.  Fields
were compared against a DOI landing page, publisher page, arXiv record, or the
author's own document.  A source was not accepted merely because a title
appeared in a third-party index.  `VERIFIED` means all recorded fields agree
with primary evidence; `MISMATCH` means the work exists but at least one field
does not agree exactly; `NOT_FOUND` would require three materially different
queries without exact evidence.  No entry reached `NOT_FOUND`.

### A1. `ChandgotiaMarcus2018` — VERIFIED

- Queries: `"10.2140/pjm.2018.294.41"`; `"Mixing Properties for Hom-Shifts" Chandgotia Marcus`.
- Primary evidence: [DOI/publisher record](https://doi.org/10.2140/pjm.2018.294.41) and [publisher PDF](https://msp.org/pjm/2018/294-1/pjm-v294-n1-p03-p.pdf).
- Field comparison: authors Nishant Chandgotia and Brian Marcus — match;
  title — match; *Pacific Journal of Mathematics* — match; volume 294,
  issue 1 — match; pages 41–69 — match; year 2018 — match; DOI — match.
- Content inspected: the abstract and opening scope, not metadata alone.  They
  concern mixing properties of hom-shifts and graph/walk geometry, supporting
  the manuscript's background attribution.

### A2. `Chandgotia2019Lectures` — MISMATCH

- Queries: `"Hom-Shifts, Lecture 4" Nishant Chandgotia`; `"Lecture 4: An introduction to hom-shifts" Chandgotia`; `site:nishantchandgotia.github.io coursekrakow l4.pdf`.
- Primary evidence: [author-hosted lecture PDF](https://nishantchandgotia.github.io/Teaching/2019_Jagiellonian/coursekrakow/l4.pdf).
- Field comparison: author — match; year/course context — match; URL — match;
  item type — acceptable; title — **does not match exactly**.  The document
  title page says **“Lecture 4: An introduction to hom-shifts”**, whereas the
  BibTeX title is **“Hom-Shifts, Lecture 4”**.
- Content inspected: the complete-bipartite phase/product-measure discussion
  and entropy statement in the later lecture slides (approximately slides
  26–32), not the title page alone.  Those pages support the phase/MME
  background attribution.
- Objective correction: replace the BibTeX title with the title printed on the
  author-hosted document.  This is a metadata correction; it does not alter a
  theorem or proof.

### A3. `ChandgotiaThorat2026` — VERIFIED

- Queries: `"2605.02226"`; `"Finitely Dependent Processes on Subshifts" Chandgotia Thorat`.
- Primary evidence: [arXiv abstract record](https://arxiv.org/abs/2605.02226)
  and [arXiv full text](https://arxiv.org/html/2605.02226v2).
- Field comparison: Nishant Chandgotia and Aditya Thorat — match; title —
  match; year 2026 — match; identifier 2605.02226 — match; primary class
  `math.PR` — match.
- Content inspected: abstract/introduction theorem statement.  It states the
  shift-invariant finite-dependence obstruction for graph homomorphisms into a
  fixed finite undirected simple graph without four-cycles.  This supports the
  manuscript's attribution and its explicit hypothesis subtraction.

### A4. `BealBlockGorman2025` — VERIFIED

- Queries: `"2509.24754"`; `"One-Sided Hom Shifts" Béal Block Gorman`.
- Primary evidence: [arXiv abstract record](https://arxiv.org/abs/2509.24754)
  and [arXiv full text](https://arxiv.org/html/2509.24754v1).
- Field comparison: Marie-Pierre Béal and Alexi Block Gorman — match; title —
  match apart from harmless display capitalization; year 2025 — match;
  identifier 2509.24754 — match; primary class `cs.FL` — match.
- Content inspected: abstract and conjugacy-method discussion.  The work treats
  one-sided SFT/Hom-shift conjugacy and Williams-type methods, supporting the
  category boundary stated in P68.

Bibliography summary: 3 `VERIFIED`, 1 `MISMATCH`, 0 `NOT_FOUND`.

## B. Ghost/dangling citation check

- BibTeX keys found (4): `ChandgotiaMarcus2018`,
  `Chandgotia2019Lectures`, `ChandgotiaThorat2026`,
  `BealBlockGorman2025`.
- Distinct keys cited in rendered manuscript source (4): the same set.
- Citation commands/occurrences checked: 10.
- Undefined/ghost citation keys: 0.
- Bibliography entries never cited: 0.
- Result: citation graph `PASS`; this does not override the title-field
  mismatch in A2.

## C. Citation-context verification — 10/10 contexts (100%)

The denominator is every external citation occurrence in `sections/*.tex`.
The source's abstract or relevant full-text passage was inspected in every
case; metadata-only agreement was not treated as claim support.

| Location | Citation | Claim made in context | Direct content evidence | Verdict |
|---|---|---|---|---|
| `sections/1_introduction.tex:3–6` | `ChandgotiaMarcus2018` | hom-shift mixing reflects graph geometry | [publisher PDF](https://msp.org/pjm/2018/294-1/pjm-v294-n1-p03-p.pdf), abstract/opening scope | VERIFIED |
| `sections/1_introduction.tex:9–11` | `Chandgotia2019Lectures` | checkerboard phase and maximal-entropy consequence appear in lectures | [author PDF](https://nishantchandgotia.github.io/Teaching/2019_Jagiellonian/coursekrakow/l4.pdf), complete-bipartite slides | VERIFIED-CONTENT; metadata title mismatch |
| `sections/1_introduction.tex:27–29` | `ChandgotiaThorat2026` | the cited obstruction assumes no four-cycles | [arXiv full text](https://arxiv.org/html/2605.02226v2), main scope/theorem | VERIFIED |
| `sections/1_introduction.tex:47–50` | `BealBlockGorman2025` | one-sided conjugacy uses Williams/amalgamation methods | [arXiv full text](https://arxiv.org/html/2509.24754v1), abstract/method sections | VERIFIED |
| `sections/3_conjugacy.tex:72–74` | `BealBlockGorman2025` | one-sided category lacks the same two-sided dimer access and is treated by amalgamation theory | [arXiv full text](https://arxiv.org/html/2509.24754v1) | VERIFIED; the “lacks access” clause is P68's transparent category comparison |
| `sections/4_finite_dependence.tex:49–53` | `ChandgotiaThorat2026` | broad nonexistence for four-cycle-free targets in dimension at least two | [arXiv full text](https://arxiv.org/html/2605.02226v2) | VERIFIED |
| `sections/7_scope.tex:3–6` | `Chandgotia2019Lectures` | phase/MME product picture is prior background | [author PDF](https://nishantchandgotia.github.io/Teaching/2019_Jagiellonian/coursekrakow/l4.pdf) | VERIFIED-CONTENT; metadata title mismatch |
| `sections/7_scope.tex:6–7` | `ChandgotiaMarcus2018` | general mixing questions are prior work | [publisher PDF](https://msp.org/pjm/2018/294-1/pjm-v294-n1-p03-p.pdf) | VERIFIED |
| `sections/7_scope.tex:7–9` | `ChandgotiaThorat2026` | cited paper owns the four-cycle-free obstruction | [arXiv full text](https://arxiv.org/html/2605.02226v2) | VERIFIED |
| `sections/7_scope.tex:9–12` | `BealBlockGorman2025` | one-sided/tree settings use one-sided amalgamation rather than P68's intrinsic two-sided dimer code | [arXiv full text](https://arxiv.org/html/2509.24754v1) | VERIFIED |

## D. Verbatim-phrase screening ledger (Phase D1)

Method: 18 of 58 nonempty prose/theorem/proof paragraphs or paragraph-like
blocks were selected (31.0%).  At least one paragraph was selected from the
abstract and every major section.  Each query is an 8–12 word verbatim phrase
after harmless TeX normalization.  Searches were run quoted.  “No exact
relevant match” means no indexed result reproduced the phrase in a relevant
mathematical source; irrelevant lexical coincidences were rejected.

| Section | Quoted query | Result |
|---|---|---|
| Abstract | `"The code uses the configuration's intrinsic checkerboard phase to pair sites"` | NO_EXACT_RELEVANT_MATCH |
| Introduction | `"Graph-homomorphism shifts form a concrete class of nearest-neighbour shifts of finite"` | NO_EXACT_RELEVANT_MATCH |
| Introduction | `"Does a conjugacy remember the two part sizes separately, or only"` | NO_EXACT_RELEVANT_MATCH |
| Introduction | `"A finitely dependent process makes sufficiently remote coordinates independent, whereas"` | NO_EXACT_RELEVANT_MATCH |
| Introduction | `"One-sided hom-shift conjugacy uses a different coding category and is"` | NO_EXACT_RELEVANT_MATCH |
| Phase/counts | `"The parity of the length of a lattice path from"` | NO_EXACT_RELEVANT_MATCH |
| Phase/counts | `"Completeness of the bipartite target makes the resulting global configuration valid"` | NO_EXACT_RELEVANT_MATCH |
| Phase/counts | `"Packing and unpacking are continuous and commute with translations"` | NO_EXACT_RELEVANT_MATCH |
| Conjugacy | `"Therefore translating the input translates the anchored dimers and"` | NO_EXACT_RELEVANT_MATCH |
| Conjugacy | `"using a fixed parity origin would not commute with odd translations"` | NO_EXACT_RELEVANT_MATCH |
| Finite dependence | `"All coordinates are independent, so the law is 0-dependent"` | NO_EXACT_RELEVANT_MATCH |
| Finite dependence | `"while the index-two even subaction admits an independent law"` | NO_EXACT_RELEVANT_MATCH |
| Pressure | `"We include the uniqueness argument because it records the role of"` | NO_EXACT_RELEVANT_MATCH |
| Pressure | `"knowing the target part at one site determines it at every site"` | NO_EXACT_RELEVANT_MATCH |
| Periodic data | `"An odd period would identify a site with a site in"` | NO_EXACT_RELEVANT_MATCH |
| Proof-engine table discussion | `"The construction supplies the missing mechanism and also explains why"` | NO_EXACT_RELEVANT_MATCH |
| Scope | `"There are three limitations. First, completeness of the bipartite target"` | NO_EXACT_RELEVANT_MATCH |
| Conclusion | `"A translation-equivariant dimerization converts that freedom into the alphabet"` | NO_EXACT_RELEVANT_MATCH |

Phase D1 is a bounded overlap screen, not a plagiarism determination and not
an originality certificate.  Phase D2 status is exactly:
`NOT_RUN_AUTHOR_IDENTITIES_UNAVAILABLE`.

## E. Nearest-neighbour/alternate-term search ledger

Each core advance was searched under at least three materially different
descriptions.  Searches were run through 2026-08-26.

### E1. Two-sided product classification and intrinsic dimer code

- `"complete bipartite hom-shift" conjugacy product mn`
- `"Hom(Z^d,K_{m,n})" conjugacy`
- `"graph homomorphism shift" "dimer code" bipartite`
- `"complete bipartite graph" hom-shift conjugacy classification`

Result: no public result located that states the exact two-sided
`mn=rs` classification with mutually inverse intrinsic radius-one dimer
codes.  Nearest indexed neighbours are [Chandgotia–Marcus](https://doi.org/10.2140/pjm.2018.294.41)
on hom-shift mixing, the [author lecture](https://nishantchandgotia.github.io/Teaching/2019_Jagiellonian/coursekrakow/l4.pdf)
on complete-bipartite phase/MME structure, and
[Béal–Block Gorman](https://arxiv.org/abs/2509.24754) on a distinct one-sided
conjugacy category.

### E2. Finite dependence under subgroup actions

- `"complete bipartite hom-shift" "finitely dependent"`
- `"checkerboard phase" "finitely dependent" process subgroup`
- `"Hom(Z^d,K_{m,n})" "finite dependence"`
- `"graph homomorphism" complete bipartite "finitely dependent"`

Result: no exact subgroup-dichotomy statement located.  The nearest theorem is
[Chandgotia–Thorat](https://arxiv.org/abs/2605.02226), whose graph hypothesis
excludes four-cycles; P68 explicitly subtracts that owner and notes that
complete bipartite targets with both parts at least two contain four-cycles.

### E3. One-site pressure, equilibrium, and subgroup periodic data

- `"complete bipartite hom-shift" pressure equilibrium one-site potential`
- `"Hom(Z^d,K_{m,n})" "topological pressure"`
- `"complete bipartite graph hom-shift" "periodic point"`
- `"complete bipartite hom-shift" entropy periodic points`

Result: no public source located with P68's combined scalar pressure,
full-action uniqueness, and all finite-index fixed-point formulae.  The lecture
above is the closest source for the zero-potential phase/MME special case.

Search-bounded conclusion: the bounded public search found no exact statement
of the residual P68 theorem package.  This is **not** a global novelty or
priority certificate.  Collision risk is assessed as **MEDIUM** because the
terminology is niche, indexing may be incomplete, and a specialist
exact-neighbour review remains necessary.  External release remains `HOLD`.

## F. Tool limitations

- Public web indexing was available; subscription databases, private drafts,
  conference correspondence, and non-indexed manuscripts were not.
- PDF text extraction and search can normalize accents, hyphenation,
  capitalization, and TeX mathematics; exact-phrase misses are therefore not
  evidence of authorship.
- Search rankings and indexed versions can change after the audit date.
- The ledger verifies the sources and statements actually found.  It cannot
  certify exhaustive global priority, author identity, or undisclosed work.
