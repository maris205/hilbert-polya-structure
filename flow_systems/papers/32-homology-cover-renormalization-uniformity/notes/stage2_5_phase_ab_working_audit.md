# P32 Stage 2.5 Phase A/B working audit

Scope: read-only integrity verification of registered references and sampled
citation contexts. This note does not edit the manuscript or bibliography, run
scientific computation, or evaluate either roadmap.

Audit date: `2026-09-02 UTC`  
Mode: Stage 2.5 pre-review  
Reference population: 26/26 registered BibTeX entries  
Citation-context sample: 8/26 cited-reference contexts (`30.8%`)  
Network route: ordinary browser search; no programmatic verification client and
no cross-model upload

## Frozen inputs

| Artifact | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `246545c14b5d7c3e43f7aad8b421b254ded52bf82efc1182b4c4bfe3ef6232c9` |
| `paper/references.bib` | `e699c96196377892d3aa1f280e6a5117001c3cec37a511a3d1c08fdc52127de9` |
| `notes/stage1_phase2_source_verification.tsv` | `7ab194dd2a26a53aa8bc2908c91048fc10b682b73ddf6d93023ef5b94e865e08` |
| `notes/stage1_phase5_citation_integrity_review.md` | `cc345a03315881aff5ced8c995580c7fbed8f3a76ccdb0aed1ca7b7f46a7a059` |

The Stage-2 key map is identity-preserving: each BibTeX key equals its frozen
`source_id` byte-for-byte.

## Method and verdict vocabulary

Every entry received a fresh exact-title/author/year or exact-identifier browser
query. The table records the literal query and the selected authoritative stable
URL. Metadata were compared field-by-field with the frozen BibTeX. A `VERIFIED`
verdict means the work exists and the registered author/title/year/venue and
available volume/issue/pages/identifier agree with an authoritative publisher,
DOI, journal, society, preprint-server, or institutional record. Third-party
discrepancies are kept visible and do not override a primary record.

## Phase A — 100% reference verification

| Source / key | Exact search query | Selected authoritative top URL | Fields confirmed | Verdict | Conflict or correction |
|---|---|---|---|---|---|
| P32-S01 | `10.1007/BF00146825 Cannon Combinatorial Structure Cocompact Discrete Hyperbolic Groups` | https://doi.org/10.1007/BF00146825 | author, title, Geometriae Dedicata, 1984, 16(2), 123--148, DOI | VERIFIED | None. |
| P32-S02 | `10.1142/S0218196706002986 Epstein Holt Linearity Conjugacy Word-Hyperbolic 2006` | https://doi.org/10.1142/S0218196706002986 | two authors, title, journal, 2006, 16(2), 287--305, DOI | VERIFIED | Third-party DBLP reports 287--306. The article first page and AMS references report 287--305, confirming the already-authorized frozen correction; no new edit. |
| P32-S03 | `10.1142/S0218196705002529 Bridson Howie Conjugacy Finite Subsets Hyperbolic Groups` | https://people.maths.ox.ac.uk/bridson/papers/BHowIJAC/ | two authors, title, IJAC, 2005, 15(4), 725--756, DOI | VERIFIED | None. Author-hosted primary manuscript and DOI agree. |
| P32-S04 | `10.1142/S0218196713500203 Buckley Holt finite lists conjugacy hyperbolic` | https://doi.org/10.1142/S0218196713500203 | two authors, title, IJAC, 2013, 23(5), 1127--1150, DOI | VERIFIED | None. |
| P32-S05 | `10.1070/IM1990v035n01ABEH000693 Lysenok algorithmic properties hyperbolic groups root extraction` | https://www.mathnet.ru/eng/im1275 | author, title, journal, 1990, 35(1), 145--163, DOI | VERIFIED | None. MathNet abstract explicitly includes root extraction. |
| P32-S06 | `arXiv 2511.12862 Word Length Formulae Normal Forms Conjugacy Classes Surface Groups` | https://arxiv.org/abs/2511.12862 | Ke Wang, Qiang Zhang, Xuezhi Zhao; exact title; 2025; arXiv:2511.12862; v1/v2 record | VERIFIED | Non-peer-reviewed preprint. The primary record uses a symmetric presentation; no mapping to P32's frozen marked presentation is supplied. |
| P32-S07 | `10.1017/S0017089500005632 Jassim Finite Abelian Surface Coverings` | https://www.cambridge.org/core/services/aop-cambridge-core/content/view/16D851320AFFD99149963011091B02D9/S0017089500005632a.pdf/finite_abelian_surface_coverings.pdf | author, title, Glasgow Math. J., 1984, 25(2), 207--218, DOI | VERIFIED | None. |
| P32-S08 | `10.2307/1971195 Sunada Riemannian Coverings Isospectral Manifolds` | https://annals.math.princeton.edu/1985/121-1/p04 | author, title, Annals, 1985, 121(1), 169--186, DOI | VERIFIED | None. |
| P32-S09 | `10.1215/S0012-7094-87-05515-3 Phillips Sarnak Geodesics Homology Classes` | https://collaborate.princeton.edu/en/publications/geodesics-in-homology-classes/ | two authors, title, Duke Math. J., 1987, 55(2), 287--297, DOI | VERIFIED | None. |
| P32-S10 | `10.2307/2374542 Katsuda Sunada Homology Closed Geodesics Compact Riemann Surface` | https://doi.org/10.2307/2374542 | two authors, title, AJM, 1988, 110(1), 145--155, DOI | VERIFIED | None. |
| P32-S11 | `10.1007/BF02699875 Katsuda Sunada Closed Orbits Homology Classes` | https://www.numdam.org/item/PMIHES_1990__71__5_0/ | two authors, title, Publ. Math. IHES, 1990, 71, 5--32, DOI | VERIFIED | None. |
| P32-S12 | `"10.1007/978-3-031-27704-7_10"` | https://link.springer.com/chapter/10.1007/978-3-031-27704-7_10 | two authors, exact chapter title, book, 2023, 85--90, DOI | VERIFIED | None. Exact chapter `_10` was separately checked to avoid confusion with chapter `_8`, `Homological Wideness`. |
| P32-S13 | `Selberg 1956 "Harmonic Analysis and Discontinuous Groups" 20 47 87` | https://www.i-scholar.in/index.php/JIMSIMS/article/view/146884 | Atle/A. Selberg, exact title, J. Indian Math. Soc., 1956, 20, 47--87 | VERIFIED | **Stage-1 status upgrade:** the authoritative journal record and CERN catalogue close existence and metadata. The former `PLAUSIBLE` label is no longer appropriate; BibTeX itself needs no change. |
| P32-S14 | `10.1007/BF01403069 Ruelle Zeta-Functions Expanding Maps Anosov Flows` | https://doi.org/10.1007/BF01403069 | author, title, Inventiones, 1976, 34(3), 231--242, DOI | VERIFIED | None. |
| P32-S15 | `10.2307/2006982 Parry Pollicott Prime Number Theorem Closed Orbits Axiom A` | https://annals.math.princeton.edu/1983/118-3/p07 | two authors, exact title, Annals, 1983, 118(3), 573--591, DOI | VERIFIED | None. |
| P32-S16 | `10.5802/jtnb.657 Brenner Spinu Artin Formalism Selberg Zeta finite index` | https://jtnb.centre-mersenne.org/articles/10.5802/jtnb.657/ | two authors, exact title, JTNB, 2009, 21(1), 59--75, DOI | VERIFIED | None. |
| P32-S17 | `10.4007/annals.2013.178.2.6 Giulietti Liverani Pollicott erratum arXiv 2203.04917` | https://doi.org/10.4007/annals.2013.178.2.6 | three authors, title, Annals, 2013, 178(2), 687--773, DOI | VERIFIED | Companion erratum is real and scope-material: https://arxiv.org/abs/2203.04917. It corrects the Section 7 spectral-gap part and states the first meromorphic-continuation part is unaffected. |
| P32-S18 | `10.24033/ASENS.2290 Dyatlov Zworski Dynamical Zeta Anosov Flows Microlocal` | https://www.numdam.org/articles/10.24033/asens.2290/ | two authors, exact title, Ann. ENS, 2016, 49(3), 543--577, DOI | VERIFIED | None. |
| P32-S19 | `10.1007/BF02392732 Lalley Renewal Theorems Symbolic Dynamics Geodesic Flows` | https://www.stat.uchicago.edu/~lalley/Papers/acta.pdf | author, exact title, Acta Math., 1989, 163, 1--55, DOI | VERIFIED | None. Author-hosted primary PDF corroborates the DOI record. |
| P32-S20 | `10.1007/BF01076325 Margulis Applications Ergodic Theory Manifolds Negative Curvature 1969` | https://m.mathnet.ru/php/archive.phtml?jrnid=faa&option_lang=eng&paperid=2746&wshow=paper | author, title, English journal, 1969, 3(4), 335--336, DOI | VERIFIED | None. MathNet also records the Russian-original pagination 89--90; the BibTeX correctly uses the English version. |
| P32-S21 | `10.1017/S0143385700007434 Sharp Closed Orbits Homology Classes Anosov Flows` | https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/closed-orbits-in-homology-classes-for-anosov-flows/23E771B97833D5EC2D10517CC7F789B8 | author, title, ETDS, 1993, 13(2), 387--408, DOI | VERIFIED | None. Publisher page was posted online later but identifies the 1993 issue. |
| P32-S22 | `10.1353/AJM.1998.0041 Pollicott Sharp Exponential Error Terms Growth Functions Negatively Curved Surfaces` | https://doi.org/10.1353/AJM.1998.0041 | two authors, title, AJM, 1998, 120(5), 1019--1042, DOI | VERIFIED | None. |
| P32-S23 | `10.1090/S0002-9947-1949-0032593-5 Neumann On Ordered Division Rings` | https://doi.org/10.1090/S0002-9947-1949-0032593-5 | B. H. Neumann, title, Transactions AMS, 1949, 66(1), 202--252, DOI | VERIFIED | None. AMS volume index confirms title, author, volume, and pages. |
| P32-S24 | `Snellman 1998 A Graded Subring of an Inverse Limit of Polynomial Rings Stockholm thesis` | https://su.diva-portal.org/smash/record.jsf?pid=diva2%3A195258 | author, exact title, Stockholm University doctoral thesis, 1998, ISBN and institutional record | VERIFIED | None. |
| P32-S25 | `10.1017/FMP.2021.19 Chiu de Fernex Docampo Embedding Codimension Space Arcs` | https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/embedding-codimension-of-the-space-of-arcs/718B33B69515A2C0B476099F6A09B391 | three authors, exact title, Forum Math. Pi, 2022, 10, e4, DOI | VERIFIED | None. DOI suffix reflects 2021 acceptance/registration; publication year 2022 is correct. |
| P32-S26 | `site:dlmf.nist.gov/4.6 DLMF Power Series 4.6` | https://dlmf.nist.gov/4.6 | NIST DLMF project, section title, power-series content, current version 1.2.7 / 2026-06-15 | VERIFIED | None. This is a mutable institutional reference; the registered 2026 year matches the current frozen access/version context. |

### Phase A closure and ghost-citation replay

- Reference existence: `26 VERIFIED / 0 NOT_FOUND / 0 MISMATCH`.
- Bibliographic edits required: `0`.
- BibTeX keys: `26`, all unique.
- In-text cited keys: `26`, all unique.
- Orphans: `0`; dangling citations: `0`; duplicate BibTeX keys: `0`.
- P32-S13 is upgraded from the Stage-1 `PLAUSIBLE` state to `VERIFIED` on the
  basis of the authoritative journal record plus the independent CERN catalogue.
- P32-S02's known page-range conflict was replayed and remains resolved in favor
  of the primary 287--305 record.

## Phase B — deterministic citation-context sample

Selection rule: take the first key in each of the five citation-bearing
literature subsections; force the three registered priority surfaces P32-S06,
P32-S13, and P32-S17; then top up in full manuscript citation order to
`ceil(0.30 * 26) = 8`. Because S13 is already a subsection seed, the resulting
sample is P32-S01, S02, S06, S07, S13, S17, S19, and S23. All citation-bearing
major subsections are represented.

| Context | Exact manuscript locator | Cited key | Source evidence used | Verdict and boundary |
|---|---|---|---|---|
| cocompact hyperbolic-group combinatorial structure | `manuscript.tex:161-166`, §2.1 | P32-S01 | exact DOI metadata and source synopsis | ACCURATE_WITH_BOUNDARY. It is used only as adjacent normal-form/decision background; no genus-two owner interface is attributed to it. |
| word-hyperbolic conjugacy | `manuscript.tex:161-166`, §2.1 | P32-S02 | article first page/abstract and primary page-range evidence | ACCURATE_WITH_BOUNDARY. It supports a conjugacy algorithmic precedent, while the manuscript explicitly distinguishes prefix exhaustion and project serialization. |
| surface-group normal forms, conjugacy, roots | `manuscript.tex:167-171`, §2.1 | P32-S06 | primary arXiv title, abstract, author list, and symmetric-presentation statement | ACCURATE_WITH_EXPLICIT_PRESENTATION_GAP. The source does advertise conjugacy and root-finding algorithms, is a non-peer-reviewed preprint, and uses the symmetric presentation; the manuscript correctly says no mapping to the frozen marked presentation has been established. |
| finite abelian surface covers | `manuscript.tex:193-197`, §2.2 | P32-S07 | Cambridge primary PDF introduction and exact metadata | ACCURATE_WITH_BOUNDARY. It supports finite abelian surface-cover structure but not P32's lift multiplicities or normalization. |
| historical Selberg trace/zeta context and existence state | `manuscript.tex:218-222`, §2.3 | P32-S13 | authoritative Journal of the Indian Mathematical Society record; CERN catalogue corroboration | **MINOR_STATE_DRIFT.** The historical trace-formula context is accurate and background-only, but line 219 says existence `remains PLAUSIBLE`; Phase A now positively verifies the record. Recommended future edit: replace only that stale state label with `VERIFIED`, preserving the background-only boundary. |
| corrected Anosov-zeta continuation scope | `manuscript.tex:229-235`, §2.3 | P32-S17 | original DOI plus primary erratum arXiv:2203.04917 | ACCURATE_AND_PRECISE. The erratum says Section 7's spectral-gap result is affected while the first meromorphic-continuation part is unaffected; the manuscript admits exactly the latter and excludes the former/dependent counting claims. |
| renewal methods as a tail candidate | `manuscript.tex:246-249`, §2.4 | P32-S19 | author-hosted Acta paper, contents, and overview | ACCURATE_WITH_BOUNDARY. The source provides symbolic renewal/geodesic-counting methods; the manuscript calls it only a possible ingredient and expressly withholds the exact compact-uniform transfer. |
| ordered-division-ring / well-ordered-support background | `manuscript.tex:261-266`, §2.5 | P32-S23 | DOI/AMS volume index plus the documented Mal'cev--Neumann series connection | ACCURATE_WITH_BOUNDARY. It is used as formal background only; lines 268--273 explicitly deny that it defines P32's coefficient ring, topology, or normalization. |

### Phase B result

- Checked: `8/26 = 30.8%` of cited-reference contexts.
- Clean/bounded: `7`; minor state drift: `1`; serious/medium distortion: `0`.
- No numerical misquotation, cherry-picking, or unauthorized source-to-project
  promotion was found.
- All sampled citations remain anchorless in the manuscript's ARS markers. This
  audit verifies the displayed broad context against authoritative records; it
  does not convert `anchor=none` into a passage-level human-read attestation and
  does not silently clear the Stage-1 locator limitation for unsampled claims.

## Findings to forward

### `P32-AB-MINOR-01` — stale existence-state label

- Location: `paper/manuscript.tex:218-222`, specifically line 219.
- Current text: P32-S13's source-existence state `remains PLAUSIBLE`.
- Evidence: the authoritative journal record confirms Selberg, exact title,
  volume 20 (1956), pages 47--87; CERN independently catalogues the same work.
- Disposition: Phase A verdict is `VERIFIED`; BibTeX is correct. A future
  authorized manuscript patch should change only the state word and retain
  `background-only` plus all no-promotion boundaries.
- Severity: MINOR. The current wording understates evidence rather than
  fabricating or overstating source support.

Preserve these non-blocking observations in the batch synthesis:

1. P32-S06's preprint status and presentation-mapping gap are accurately stated.
2. P32-S17's correction limitation is accurately and narrowly stated.
3. P32-S02's third-party 287--306 page discrepancy does not invalidate the
   primary-supported frozen 287--305 entry.
4. No cover calculation, tail proof, coefficient comparison, limit, or Route
   result follows from this Phase A/B audit.

