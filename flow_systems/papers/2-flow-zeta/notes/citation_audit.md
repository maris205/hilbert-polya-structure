# Independent citation and integrity audit

**Project:** `papers/2-flow-zeta`  
**Audited files:** `paper/manuscript.tex`, `paper/references.bib`,
`paper/manuscript.bbl`, `paper/manuscript.blg`, `paper/manuscript.log`, and the
local primary PDFs in `notes/sources/`  
**Audit date:** 2026-08-13  
**Decision:** **REVISE (minor but mandatory bibliographic and production
corrections)**

The central mathematical claims are adequately separated into source facts,
arguments proved in the manuscript, conditional results, and open or
not-testable interfaces. I found no citation whose cited work contradicts the
adjacent claim, no unresolved citation/reference in the build, and no missing
glyph reported by XeLaTeX. The manuscript should nevertheless not be frozen in
its current form: three bibliography records are definitely incomplete or
incorrect, one source version statement should be made more explicit, and the
current PDF has one severe overfull line.

## 1. Audit method and evidence boundary

- Parsed all 19 citation commands. They resolve to 14 unique keys, and all 14
  keys are present in `references.bib`; there are no uncited bibliography
  entries.
- Read the neighboring prose for every citation and compared it with the local
  primary/author PDF. For the Deninger packet assertions I also checked the
  displayed source locations around equations (37)--(40), Theorems 5.2 and 6.1,
  and Section 11.
- Cross-checked DOI metadata through Crossref or the publisher for Deninger,
  Duistermaat--Guillemin, Álvarez López--Kordyukov--Leichtnam,
  Ruelle--Sullivan, Ruelle, Fried, Dyatlov--Zworski, and
  Giulietti--Liverani--Pollicott. The DOI, title, author, year, volume, issue,
  and page fields used in the manuscript agree with those records.
- Cross-checked non-DOI items against arXiv, author/institutional pages, AMS
  metadata, MathNet, and the local PDFs. Search summaries were used only to
  locate primary or publisher records, not as mathematical evidence.
- Audited the final XeLaTeX/BibTeX logs. `manuscript.blg` reports zero BibTeX
  warnings; `manuscript.log` reports neither undefined citations nor undefined
  references.

This is a citation/integrity audit, not an independent re-proof of the new
uncountability and divergence theorems. Those proofs were checked here only for
whether they improperly rely on a citation; they are self-contained.

## 2. Claim-to-source fit

| Citation or source group | Adjacent manuscript claim | Audit result |
|---|---|---|
| Deninger 2026 / arXiv:1807.06400v4 | closed points index compact packets; packet orbits have period `log N x_0`; equations (37)--(39) depend on auxiliary choices; equation (40) is the canonical projection; Section 11 defines a Haar-normalized convolution algebra on another inverse-limit group | **PASS.** The local v4 text directly supports these statements. The manuscript appropriately avoids upgrading the choice-dependent set-level parametrization to a canonical homeomorphism or locally trivial bundle. |
| Deninger 2024 / arXiv:2301.11643v1 | overview-level corroboration of packet compactness/periods; smooth foliated trace formula as motivation; fixed-time operator may fail to be trace class but mollification yields a trace; rational-Witt spaces remain infinite-dimensional and incompletely understood | **PASS WITH VERSION CLARIFICATION.** These claims occur in the local arXiv author version. The bibliography labels the work as the 2024 collected-volume chapter, so the manuscript or entry should explicitly say that the cited theorem/locator evidence was checked in arXiv v1 and the final pagination was not audited. |
| Duistermaat--Guillemin 1975 | clean fixed sets require differential/symplectic/operator data and contribute through canonical densities, not a universal “one component, one count” rule | **PASS.** The manuscript uses this only as an applicability benchmark and does not claim a no-go theorem beyond absent hypotheses. |
| Bourgeois 2003 | Morse--Bott contact conditions require a smooth contact setting, a smooth period set, tangent-kernel equality, and constant-rank data; the paper is contact homology rather than a general flow trace theorem | **PASS mathematically; REVISE metadata.** The claim matches Definition 1 in the local text, but the cited work is a published proceedings chapter, not merely a 2003 “Author manuscript.” |
| Kordyukov 2000/2001 | a relative Duistermaat--Guillemin formula assumes a compact smooth foliated manifold, a transversally elliptic self-adjoint operator, and a clean relative fixed set | **PASS mathematically; REVISE metadata.** The arXiv preprint supports the claim, but a published journal record exists and should be included. |
| Álvarez López--Kordyukov--Leichtnam 2026 | closed smooth codimension-one foliated setting; simple closed orbits; transversely simple preserved leaves; leafwise currents, smoothing b-PDOs and b-trace; b-trace may not vanish on commutators and auxiliary choices can affect the zero-time term | **PASS.** The book DOI, LNM volume 2387, author order, year, and the substantive statements agree with the Springer record and local author text. |
| Renault 2006 | a Haar system is a continuous invariant family of nonzero Radon measures on range fibers; for groupoids existence/uniqueness are not automatic; it enables convolution on `C_c(G)` | **PASS mathematically; REVISE booktitle.** Section 3 says exactly this. The current collected-volume title is wrong (see Section 3 below). |
| Connes 1982 | holonomy-invariant transverse measure is additional data; it yields a Ruelle--Sullivan cycle/current and corresponds to a trace/dimension map on the foliation algebra under the foliation hypotheses | **PASS.** The statement is appropriately qualified by “under the appropriate foliation hypotheses.” |
| Ruelle--Sullivan 1975 | a transverse invariant measure produces the associated current/homology class | **PASS.** The manuscript does not conflate that current with a flow fixed-point trace. |
| Dyatlov--Zworski 2016 | the flat trace requires a wavefront pullback condition and yields the primitive-period/Poincaré-determinant periodic-orbit coefficient for smooth Anosov flows | **PASS.** Equation (1.5) and its surrounding discussion support the displayed benchmark. |
| Ruelle 1976 | original Fredholm/meromorphy result assumes real-analytic hyperbolic dynamics, including analytic stable/unstable foliations for the Anosov-flow result | **PASS.** “Analytic hyperbolic structure” is a defensible compression, though “real-analytic flow and real-analytic stable/unstable foliations” would be more exact. |
| Giulietti--Liverani--Pollicott 2013 plus erratum | smooth Anosov meromorphic continuation via anisotropic spaces; erratum corrects contact spectral-gap analysis while leaving meromorphic continuation unaffected | **PASS.** The erratum abstract states the boundary verbatim in substance. Do not call it “published erratum” unless a journal publication is documented; the audited artifact is an arXiv erratum/preprint. |
| Fried 1986 | exact Ruelle/Selberg relation in the isolated hyperbolic/geodesic setting | **PASS, with a presentation caveat.** The relation is a legitimate benchmark, but the phrase “For a hyperbolic surface” is broader than the paper's audited Fuchsian/compact locally symmetric setting. Prefer “For the compact hyperbolic/Fuchsian benchmark considered there,” or state the precise quotient hypotheses used. |

### Coverage judgment

The paper's new elementary claims do not need external citations: the
uncountability proof, finite-subset product divergence, component-mass theorem,
and abscissa calculation are given in full. Standard compact-group Haar
existence is uncited; that is acceptable in a research manuscript, but adding a
standard theorem reference is optional if the author wants every non-elementary
background theorem documented. The prime-series divergence used in the
abscissa proof is also standard and does not create an integrity gap.

The literature-methods paragraph claims 15 screened work-level candidates, 11
core groups, and two supporting sources. These counts are documented in
`notes/phase2_trace_bibliography.md`; no citation is needed in the manuscript,
but the artifact should remain packaged with the paper.

## 3. Mandatory bibliography corrections

### 3.1 Bourgeois 2003: wrong entry type and missing publication fields

Current entry: `@misc`, note `Author manuscript`.

Publisher and author records identify the work as:

> Frédéric Bourgeois, “A Morse--Bott approach to contact homology,” in
> *Symplectic and Contact Topology: Interactions and Perspectives*, Fields
> Institute Communications 35, American Mathematical Society, 2003, pp. 55--77.

Revise to `@incollection`; add the book title, series, volume 35, AMS as
publisher, and pages 55--77. Keeping the author-PDF URL is useful. Do not
confuse this chapter with the separate 2002 Stanford PhD thesis of the same
title.

### 3.2 Renault 2006: wrong book title

Current entry says `booktitle = {Dynamical Systems and Group Actions}`. AMS
volume 217 is titled *Representation Theory, Dynamical Systems, and Asymptotic
Combinatorics*. A separate AMS volume titled *Dynamical Systems and Group
Actions* is Contemporary Mathematics 567 (2012), so the current record mixes
two different books.

Replace the book title with the volume-217 title; retain `American Mathematical
Society Translations, Series 2`, volume 217, 2006, pages 185--199, and the
author-PDF URL.

### 3.3 Kordyukov: published version omitted

The mathematical citation to arXiv:math/0001182 is valid, but the work also
appeared as:

> Yu. A. Kordyukov, “The trace formula for transversally elliptic operators on
> Riemannian foliations,” *Algebra i Analiz* 12(3) (2000), 81--105; English
> translation, *St. Petersburg Mathematical Journal* 12(3) (2001), 407--422.

Prefer an `@article` record for the English translation with the arXiv fields and
URL retained. At minimum, add the journal publication as a note. This is not a
claim-support problem, but it is required for a publication-ready bibliography.

### 3.4 GLP erratum: source-level author inconsistency and publication label

The arXiv metadata lists Paolo Giulietti, Mark Pollicott, Carlangelo Liverani,
while the PDF title page prints Paolo Giulietti, Carlangelo Liverani, Mark
Pollicott. The current BibTeX follows the arXiv metadata, which is defensible;
record `note = {arXiv:2203.04917v1; author order follows arXiv metadata}` or use
the title-page order consistently with the local audited PDF. More importantly,
change manuscript line 924 from “The published erratum” to “The 2022 erratum”
or “The arXiv erratum” unless a journal publication is added to the record.

### 3.5 Optional completeness improvements

- Add `eprint = {1807.06400}`, `archivePrefix = {arXiv}`, and a URL to
  `Deninger2026` so readers can identify the exact v4 text used for theorem and
  equation locators. The DOI metadata itself is correct.
- Add the chapter-page range and ISBN to `Deninger2024` if final-volume
  pagination can be verified. Until then, explicitly describe arXiv:2301.11643v1
  as the audited manifestation.
- Use the formal Springer publisher string `Springer Cham` or `Springer Nature
  Switzerland AG` for the 2026 LNM volume if desired; the current `Springer` is
  not wrong.

## 4. Wording and source-boundary revisions

1. In the source-lock paragraph, change “the fourth arXiv version underlying
   the 2026 journal article” to something like “arXiv:1807.06400v4, cross-linked
   by DOI to the 2026 journal article.” This avoids implying page-perfect
   identity between the local v4 and version of record, which the source audit
   correctly leaves open.
2. In the overview paragraph, say that the trace-formula statements were
   checked in `arXiv:2301.11643v1`. The current citation prints as a 2024 chapter,
   while all exact local page locators are to the 2023 author version.
3. Replace “The published erratum” with “The 2022 arXiv erratum” unless a
   publication record is documented.
4. Narrow “For a hyperbolic surface” in the Fried benchmark to the precise
   compact/Fuchsian quotient convention used by the cited result.
5. Preserve the current evidential boundary: failure of the ordinary orbitwise
   product is proved; every packet-measured/groupoid/cohomological replacement
   remains open or not testable. No source inspected licenses strengthening that
   to universal nonexistence.

## 5. Build and PDF integrity

### Citation/reference status

- **PASS:** no `Citation ... undefined`, `Reference ... undefined`, or “There
  were undefined references” message in `manuscript.log`.
- **PASS:** BibTeX used all 14 entries and emitted zero warnings in
  `manuscript.blg`.
- **PASS:** no `Missing character` message. The generated PDF is readable,
  unencrypted, 20 pages, US-letter size, PDF 1.5.

### Production issues requiring action

- **Severe overfull line:** `32.99887pt` at manuscript lines 1059--1072. The
  source is the unbreakable monospaced string
  `not_applicable_no_candidate_determinant`. Rephrase it in prose, allow an
  explicit break, use `\path` in a narrower setting, or move the registry token
  to its own displayed/flush-left line. Recompile and require no overfull box
  above 5 pt.
- **Minor table overfulls:** three `1.0216pt` alignment overruns around lines
  950--968. They are tolerable but easy to remove by slightly narrowing columns
  or reducing `\tabcolsep` locally.
- **Font warnings:** Latin Modern lacks the requested small-cap shapes, so
  XeLaTeX substitutes upright forms. This does not corrupt content, but a final
  production pass can replace the font or avoid small caps in table status
  labels.
- **CJK monospaced font:** the current log no longer emits the earlier unknown
  CJK-family warning or missing-glyph warning. Keep the final build log, not an
  earlier log, with the release artifact.
- **Stale build risk:** at audit time `manuscript.tex` was newer than
  `manuscript.log`/`manuscript.pdf` by roughly 32 seconds. Rebuild after all
  revisions and verify that PDF/log timestamps postdate the source.

## 6. Release gate

**Current gate: REVISE.** The mathematical citation-to-claim mapping passes,
and the manuscript's no-go/open boundary is source-faithful. Release can be
marked **PASS** after all of the following are verified:

- Bourgeois and Renault records corrected;
- Kordyukov publication metadata added;
- erratum and version wording corrected;
- Fried benchmark narrowed or explicitly qualified;
- XeLaTeX/BibTeX rerun after the last source edit;
- no undefined citations/references or missing characters;
- no overfull box above 5 pt; and
- final PDF/log are newer than `manuscript.tex` and `references.bib`.

