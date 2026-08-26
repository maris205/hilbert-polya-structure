# P71 Stage 2.5 source-search ledger

Audit date: 2026-08-26 (UTC).  Search horizon: public material indexed or
published through 2026-08-26.  This ledger records bounded bibliographic,
claim-support, phrase-overlap, and nearest-neighbour searches.  All links are
direct links to the evidence source rather than search-results pages.

## A. Bibliography-entry verification

Protocol: every `references.bib` item was Web-searched independently and
compared field by field with a DOI/publisher record or arXiv primary record.
Relevant abstract/theorem text was opened when a citation supported a factual
claim.  `VERIFIED` requires all recorded fields to agree; `MISMATCH` means the
work exists but the BibTeX record is inaccurate or incomplete; `NOT_FOUND`
would be used only after three different exact/author/identifier searches.
No item reached `NOT_FOUND`.

### A1. `LameiMehdipour2025` — VERIFIED

- Queries: `"2502.11272"`; `"Zip Shift Space" Lamei Mehdipour`.
- Primary evidence: [arXiv record](https://arxiv.org/abs/2502.11272) and
  [arXiv full text](https://arxiv.org/html/2502.11272v1).
- Fields: Sanaz Lamei and Pouya Mehdipour — match; title — match; year 2025 —
  match; identifier 2502.11272 — match; primary class `math.DS` — match.
- Content inspected: formal definition, finite-to-one local-homeomorphism
  statement, sliding-block/conjugacy discussion, and periodic setting.  These
  support P71's background attribution.

### A2. `MehdipourJangjooye2025` — VERIFIED

- Queries: `"2505.24647"`; `"Square Entropy and Uniform n-to-1 Bernoulli Transformations"`.
- Primary evidence: [arXiv record](https://arxiv.org/abs/2505.24647) and
  [arXiv full text](https://arxiv.org/html/2505.24647v1).
- Fields: authors — match; title — match; year 2025 — match; identifier —
  match; primary class `math.DS` — match.
- Content inspected: abstract and principal-results discussion on square
  entropy, full uniform `n`-to-one zip shifts, intrinsic ergodicity, and the
  uniform Bernoulli characterization.

### A3. `MartinsMattosVarao2026` — VERIFIED

- Queries: `"10.1007/s10884-025-10479-7"`; `"Folding and Metric Entropies for Extended Shifts"`; `"2407.01828"`.
- Primary evidence: [publisher DOI record](https://doi.org/10.1007/s10884-025-10479-7),
  [arXiv record](https://arxiv.org/abs/2407.01828), and
  [arXiv full text](https://arxiv.org/html/2407.01828v2).
- Fields: Neemias Martins, Pedro G. Mattos, Régis Varão — match; published
  title — match; journal — match; year 2026 — match; DOI and arXiv identifier —
  match.  The absence of volume/pages in the current BibTeX is consistent with
  the authoritative record available to this audit and is not marked missing.
- Content inspected: Theorem A identifies metric entropy with the entropy of
  the positive-symbol distribution; Theorem B gives folding entropy through
  fibre/conditional weights.  Those are precisely the results P71
  owner-subtracts and then specializes to its equilibrium weights.

### A4. `Bowen1973` — VERIFIED

- Queries: `"10.1090/S0002-9947-1973-0338317-X"`; `"Topological Entropy for Noncompact Sets" Bowen`.
- Primary evidence: [AMS DOI record](https://doi.org/10.1090/S0002-9947-1973-0338317-X).
- Fields: Rufus Bowen — match; title — match; *Transactions of the American
  Mathematical Society* — match; volume 184 — match; pages 125–136 — match;
  year 1973 and DOI — match.
- Content inspected: article scope/definition for entropy on noncompact sets,
  supporting P71's use of Bowen entropy for level sets.

### A5. `BarreiraSaussolSchmeling2002` — VERIFIED

- Queries: `"10.1016/S0022-314X(02)00003-3"`; `"Distribution of Frequencies of Digits via Multifractal Analysis"`.
- Primary evidence: [publisher article page](https://www.sciencedirect.com/science/article/pii/S0022314X02000033)
  and [DOI](https://doi.org/10.1016/S0022-314X(02)00003-3).
- Fields: Luis Barreira, Benoît Saussol, Jörg Schmeling — match; title,
  journal, volume 97, issue 2, pages 410–438, year 2002, DOI — all match.
- Content inspected: publisher abstract, which treats digit-frequency level
  sets through multifractal analysis.  P71 cites it only as adjacent context.

### A6. `MehdipourSalarinoghabiGibrim2026` — MISMATCH

- Queries: `"10.1063/5.0300898"`; `"Zip Cellular Automata" Mehdipour Salarinoghabi Gibrim`; `site:pubs.aip.org "Zip cellular automata"`.
- Primary evidence: [DOI](https://doi.org/10.1063/5.0300898) and
  [AIP publisher page](https://pubs.aip.org/aip/adv/article/16/1/015201/3376058/Zip-cellular-automata).
- Fields: authors, title, journal, volume 16, issue 1, year 2026, and DOI —
  match.  The authoritative article identifier **015201** is absent from the
  BibTeX record.  AIP Advances uses an article number in place of a page range,
  so strict field-completeness status is `MISMATCH`.
- Content inspected: abstract/scope, supporting the limited claim that zip
  cellular automata are a recent adjacent direction.
- Objective correction: add `pages = {015201}` (or an equivalent explicit
  `eid/article-number` field supported by the build style).

### A7. `MehdipourLamei2026` — VERIFIED

- Queries: `"10.21494/ISTE.OP.2026.1442"`; `"Zip Shift Encoding of M-to-1 Local Homeomorphisms"`.
- Primary evidence: [publisher page](https://www.openscience.fr/Zip-Shift-encoding-of-M-TO-1-local-homeomorphisms)
  and [publisher PDF](https://www.openscience.fr/IMG/pdf/iste_apam26v17n2_2.pdf).
- Fields: Pouya Mehdipour and Sanaz Lamei — match; title — match; *Advances in
  Pure and Applied Mathematics* — match; volume 17, issue 2, pages 20–29,
  year 2026, DOI — all match.
- Content inspected: abstract/introduction on zip-shift encodings of
  finite-to-one local homeomorphisms, matching P71's adjacent-work statement.

Bibliography summary: 6 `VERIFIED`, 1 `MISMATCH`, 0 `NOT_FOUND`.

## B. Ghost/dangling citation check

- BibTeX keys found (7): `LameiMehdipour2025`,
  `MehdipourJangjooye2025`, `MartinsMattosVarao2026`, `Bowen1973`,
  `BarreiraSaussolSchmeling2002`, `MehdipourSalarinoghabiGibrim2026`, and
  `MehdipourLamei2026`.
- Distinct cited keys (7): the same set.
- External citation occurrences checked: 17.
- Undefined/ghost citation keys: 0.  Uncited bibliography entries: 0.
- Citation graph: `PASS`; this does not erase the article-number mismatch in A6.

## C. Citation-context verification — 17/17 contexts (100%)

| Location | Citation | Contextual claim | Direct content evidence | Verdict |
|---|---|---|---|---|
| `sections/1_introduction.tex:6–9` | `LameiMehdipour2025` | formal zip space, sliding blocks, local homeomorphism, periodic setting | [full text](https://arxiv.org/html/2502.11272v1) | VERIFIED |
| `sections/1_introduction.tex:8–11` | `MartinsMattosVarao2026` | same map is called extended shift; Bernoulli metric/folding entropies computed | [Theorems A–B](https://arxiv.org/html/2407.01828v2) | VERIFIED |
| `sections/1_introduction.tex:14–16` | `MehdipourJangjooye2025` | uniform theory covers square entropy and intrinsic ergodicity | [full text](https://arxiv.org/html/2505.24647v1) | VERIFIED |
| `sections/1_introduction.tex:50–54` | `MartinsMattosVarao2026` | metric/folding formulae are prior; P71 substitutes equilibrium weights | [Theorems A–B](https://arxiv.org/html/2407.01828v2) | VERIFIED |
| `sections/1_introduction.tex:56–57` | `Bowen1973` | noncompact-set entropy supplies level-set notion | [AMS record](https://doi.org/10.1090/S0002-9947-1973-0338317-X) | VERIFIED |
| `sections/1_introduction.tex:57–59` | `BarreiraSaussolSchmeling2002` | digit-frequency multifractals are adjacent context | [publisher page/abstract](https://www.sciencedirect.com/science/article/pii/S0022314X02000033) | VERIFIED |
| `sections/2_model_extension.tex:12–15` | `LameiMehdipour2025` | displayed formula is the full one-block zip shift | [full text](https://arxiv.org/html/2502.11272v1) | VERIFIED |
| `sections/2_model_extension.tex:14–17` | `MartinsMattosVarao2026` | same formula defines the extended shift | [full text](https://arxiv.org/html/2407.01828v2) | VERIFIED |
| `sections/3_pressure.tex:69–71` | `MartinsMattosVarao2026` | ensuing corollary imports their entropy formulae | [Theorems A–B](https://arxiv.org/html/2407.01828v2) | VERIFIED |
| `sections/3_pressure.tex:82–89` | `MartinsMattosVarao2026` | Theorem A gives metric entropy; Theorem B gives fibre/conditional folding entropy | [Theorems A–B](https://arxiv.org/html/2407.01828v2) | VERIFIED |
| `sections/5_multifractal.tex:3–12` | `Bowen1973` | Bowen entropy is used for possibly noncompact level sets | [AMS record](https://doi.org/10.1090/S0002-9947-1973-0338317-X) | VERIFIED |
| `sections/6_examples.tex:35–38` | `MehdipourJangjooye2025` | uniform profile is adjacent to uniform `n`-to-one theory | [full text](https://arxiv.org/html/2505.24647v1) | VERIFIED |
| `sections/7_scope.tex:3–5` | `LameiMehdipour2025` | definitions/local homeomorphism/sliding blocks/periodic setting are prior | [full text](https://arxiv.org/html/2502.11272v1) | VERIFIED |
| `sections/7_scope.tex:5–7` | `MehdipourJangjooye2025` | uniform intrinsic ergodicity/square entropy are prior | [full text](https://arxiv.org/html/2505.24647v1) | VERIFIED |
| `sections/7_scope.tex:7–12` | `MartinsMattosVarao2026` | exact map and Theorems A–B are owner-subtracted | [full text](https://arxiv.org/html/2407.01828v2) | VERIFIED |
| `sections/7_scope.tex:14–16` | `MehdipourSalarinoghabiGibrim2026` | zip cellular automata are adjacent | [publisher page](https://pubs.aip.org/aip/adv/article/16/1/015201/3376058/Zip-cellular-automata) | VERIFIED-CONTENT; BibTeX incomplete |
| `sections/7_scope.tex:15–17` | `MehdipourLamei2026` | encoding of finite-to-one local homeomorphisms is adjacent | [publisher PDF](https://www.openscience.fr/IMG/pdf/iste_apam26v17n2_2.pdf) | VERIFIED |

## D. Verbatim-phrase screening ledger (Phase D1)

Method: 21 of 68 nonempty prose/theorem/proof paragraphs or paragraph-like
blocks were selected (30.9%), with at least one from the abstract and every
major section.  Each query is an 8–12 word verbatim phrase after harmless TeX
normalization.  All searches were quoted.

| Section | Quoted query | Result |
|---|---|---|
| Abstract | `"The full pressure curve is also a complete invariant inside this family"` | NO_EXACT_RELEVANT_MATCH |
| Introduction | `"A zip shift records future symbols in one alphabet and past symbols"` | NO_EXACT_RELEVANT_MATCH |
| Introduction | `"A nonuniform fibre profile changes the question: the orbit sees a sequence"` | NO_EXACT_RELEVANT_MATCH |
| Introduction | `"This paper gives one closed theorem package for that observable"` | NO_EXACT_RELEVANT_MATCH |
| Model/natural extension | `"The natural extension of a full zip shift is the ordinary full"` | NO_EXACT_RELEVANT_MATCH |
| Model/natural extension | `"These coordinate formulae are continuous and inverse to one another"` | NO_EXACT_RELEVANT_MATCH |
| Model/natural extension | `"Invariance makes these finite-dimensional distributions consistent, so they define the lift"` | NO_EXACT_RELEVANT_MATCH |
| Model/natural extension | `"This ordinary fact is not the invariant used below"` | NO_EXACT_RELEVANT_MATCH |
| Pressure | `"For any shift-invariant measure, its entropy rate is bounded by"` | NO_EXACT_RELEVANT_MATCH |
| Pressure | `"Thus the curve contains both alphabet sizes, while its curvature records"` | NO_EXACT_RELEVANT_MATCH |
| Periodic/rigidity | `"The same exponential sum appears without a variational argument when periodic"` | NO_EXACT_RELEVANT_MATCH |
| Periodic/rigidity | `"Every fixed point arises uniquely in this way. Its local degrees"` | NO_EXACT_RELEVANT_MATCH |
| Periodic/rigidity | `"Conjugacy preserves local degree pointwise because it bijects the preimage sets"` | NO_EXACT_RELEVANT_MATCH |
| Periodic/rigidity | `"This recovers the whole profile from the curve and proves"` | NO_EXACT_RELEVANT_MATCH |
| Multifractal | `"At later times its surviving old-past coordinates remain inside that block"` | NO_EXACT_RELEVANT_MATCH |
| Multifractal | `"Countable stability of Bowen entropy gives the upper bound"` | NO_EXACT_RELEVANT_MATCH |
| Multifractal | `"Equality holds by distributing mass uniformly within each fibre"` | NO_EXACT_RELEVANT_MATCH |
| Examples | `"The ordinary topological entropy cannot distinguish fibre profiles with the same"` | NO_EXACT_RELEVANT_MATCH |
| Scope | `"The formal zip-shift definitions, local homeomorphism results, sliding block codes"` | NO_EXACT_RELEVANT_MATCH |
| Scope/control disclosure | `"These are regression checks only; all formulae are proved symbolically"` | NO_EXACT_RELEVANT_MATCH |
| Conclusion | `"Its logarithm generates a pressure curve that simultaneously determines equilibrium measures"` | NO_EXACT_RELEVANT_MATCH |

No exact relevant phrase match was located.  This is a bounded overlap screen,
not a plagiarism determination or originality certificate.  Phase D2 status
is exactly: `NOT_RUN_AUTHOR_IDENTITIES_UNAVAILABLE`.

## E. Nearest-neighbour/alternate-term search ledger

### E1. Degree pressure, equilibrium states, and curvature

- `"zip shift" "topological pressure" local degree`
- `"extended shift" thermodynamic formalism folding entropy`
- `"preimage-count potential" pressure symbolic dynamics`
- `"zip shift" equilibrium state pressure`

No public paper was located that states P71's exact finite-sum formula together
with its equilibrium weights and curvature criterion.  However, the
[UFV author/research profile](https://nit.ufv.br/pesquisador/pouya-mehdipour/)
lists an active 2024–present project titled **“Formalismo Termodinâmico para
Mapas Zip Shift”**, expressly aimed at formulating thermodynamic formalism and
phase transitions for zip-shift maps.  This is not evidence that P71's theorem
has already appeared, but it is a same-family active-work collision signal.

### E2. Profile recovery, periodic weights, and conjugacy

- `"zip shift" conjugacy "fibre profile"`
- `"zip shift" "degree-weighted" periodic zeta`
- `"finite-to-one shift" "local degree" conjugacy invariant`
- `"zip shift" periodic point degree profile`

No exact fibre-profile/pressure-curve recovery theorem or degree-weighted zeta
identity was located.  The closest current topological neighbour is
[Lamei–Mehdipour–Vargas, *S-Expansiveness and Zip Shift Maps in Symbolic Dynamics*](https://arxiv.org/abs/2510.12980),
which studies S-expansiveness, shadowing, factors, and ordinary zip-shift
topology.  It does not state P71's weighted profile theorem in its abstract,
but it belongs in the current-work boundary.  Earlier formal/periodic ownership
remains with [Lamei–Mehdipour](https://arxiv.org/abs/2502.11272).

### E3. Degree-exponent Bowen spectrum

- `"zip shift" multifractal spectrum local degree`
- `"degree exponent" Bowen entropy preimage multiplicity`
- `"Birkhoff spectrum" "log local degree" symbolic`
- `"zip shift" "multifractal" entropy`

No exact zip-shift degree-exponent spectrum was located.  Nearest general
method sources are [Bowen's noncompact-set entropy](https://doi.org/10.1090/S0002-9947-1973-0338317-X)
and [digit-frequency multifractals](https://doi.org/10.1016/S0022-314X(02)00003-3),
both already owner-subtracted.  The same-system entropy neighbour is
[Martins–Mattos–Varão](https://arxiv.org/abs/2407.01828), whose metric/folding
formulae are explicitly not claimed as P71's isolated contribution.

### E4. Additional exact-family neighbours

- [Zip cellular automata](https://doi.org/10.1063/5.0300898) — distinct
  cellular-automaton direction; already cited.
- [Zip-shift encoding of finite-to-one local homeomorphisms](https://doi.org/10.21494/ISTE.OP.2026.1442)
  — broader encoding direction; already cited.
- [2026 SBMAC zip-shift encoding proceedings paper](https://proceedings.sbmac.org.br/sbmac/article/download/5137/5196)
  — adjacent encoding/topological material; no exact pressure package located.

Search-bounded conclusion: no indexed source was found that states the exact
pressure/equilibrium/spectrum/profile-recovery package.  This is **not** a
global novelty or priority certificate.  Collision risk is **HIGH** for the
pressure part because an exact-family thermodynamic-formalism project is
publicly active, even though no matching theorem text was found.  The current
scope paragraph anticipates such work generically but should identify the live
project and the 2025 S-expansiveness paper before any release.  Specialist
exact-neighbour review is required; external release remains `HOLD`.

## F. Tool limitations

- The audit used public web/arXiv/publisher/author-institution pages.  It did
  not have exhaustive subscription databases, private manuscripts, referee
  files, author correspondence, or works not indexed on the public web.
- A project description is a collision signal, not theorem text and not proof
  of prior publication.
- Search engines normalize punctuation, accents, hyphens, and TeX; phrase
  misses cannot establish authorship or originality.
- Search results and versions can change after 2026-08-26.  This ledger cannot
  certify global priority, author identity, or undisclosed research.
