# P31 Stage 2.5 Phase A/B working audit

Scope: read-only integrity verification of registered references and sampled
citation contexts. This note does not edit the manuscript or bibliography, run
scientific computation, or evaluate either roadmap.

Audit date: `2026-09-02 UTC`  
Mode: Stage 2.5 pre-review  
Reference population: 22/22 registered BibTeX entries  
Citation-context sample: 7/22 cited-reference contexts (`31.8%`)  
Network route: ordinary browser search; no programmatic verification client and
no cross-model upload

## Frozen inputs

| Artifact | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `6023a33a4679a79c7c6cc8be8cf4345813a564b2fd420770618e7afa9547206a` |
| `paper/references.bib` | `b9078a8468e821feb31c6dc01b41c787991e36d376f81298850271573eaf9958` |
| `notes/stage1_phase2_source_verification.tsv` | `a403f1bd96189088e9aa2344355f1199600a07b62a068b145ad082846a31453a` |
| `notes/stage1_phase5_citation_integrity_review.md` | `570138d857202a91eef8d96dd8d7babee7b188f74c3480c27ae75365ed6d5b0d` |

The Stage-2 key map is identity-preserving: each BibTeX key equals its frozen
`source_id` byte-for-byte.

## Method and verdict vocabulary

Every entry received a fresh exact-title/author/year or exact-identifier browser
query. The table records the literal query and the selected authoritative stable
URL. Metadata were compared field-by-field with the frozen BibTeX. A `VERIFIED`
verdict means the work exists and the registered author/title/year/venue and
available volume/issue/pages/identifier agree with an authoritative publisher,
DOI, journal, society, or institutional record. Third-party discrepancies are
kept visible and do not override a primary record.

## Phase A — 100% reference verification

| Source / key | Exact search query | Selected authoritative top URL | Fields confirmed | Verdict | Conflict or correction |
|---|---|---|---|---|---|
| P31-S01 | `10.1112/jlms/s2-1.1.351 Millington Subgroups Classical Modular Group 1969` | https://doi.org/10.1112/jlms/s2-1.1.351 | author, title, journal, 1969, s2-1(1), 351--357, DOI | VERIFIED | None. A later Cambridge reference list renders 1970, but DOI/publisher metadata support the registered 1969 record. |
| P31-S02 | `10.2307/2374900 Kulkarni Arithmetic-Geometric Method Subgroups Modular Group 1991` | https://doi.org/10.2307/2374900 | author, title, journal, 1991, 113(6), 1053--1133, DOI | VERIFIED | None. The 1986 MPIM preprint is a distinct precursor, not a metadata substitute. |
| P31-S03 | `10.1142/S0129167X93000030 Special Polygons Subgroups Modular Group Chan Lang Lim Tan` | https://doi.org/10.1142/S0129167X93000030 | four authors, title, journal, 1993, 4(1), 11--34, DOI | VERIFIED | None. |
| P31-S04 | `10.1112/jlms/51.3.491 Lang Lim Tan algorithm subgroup modular group congruence` | https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/jlms/51.3.491 | three authors, exact title, 1995, 51(3), 491--502, DOI | VERIFIED | None. |
| P31-S05 | `10.1090/S0002-9939-96-03496-X Hsu Identifying Congruence Subgroups 1996` | https://doi.org/10.1090/S0002-9939-96-03496-X | author, title, journal, 1996, 124(5), 1351--1359, DOI | VERIFIED | None. |
| P31-S06 | `10.5802/jtnb.683 Voight Computing Fundamental Domains Fuchsian Groups` | https://jtnb.centre-mersenne.org/articles/10.5802/jtnb.683/ | author, title, journal, 2009, 21(2), 467--489, DOI | VERIFIED | None. |
| P31-S07 | `10.2307/1968204 Latimer MacDuffee Correspondence Classes Ideals Matrices` | https://doi.org/10.2307/1968204 | two authors, title, Annals, 1933, 34(2), 313--316, DOI | VERIFIED | None. |
| P31-S08 | `10.4153/CJM-1949-026-1 Taussky theorem Latimer MacDuffee` | https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/on-a-theorem-of-latimer-and-macduffee/A7185F4D644F242C297630826F6B4781 | author, title, journal, 1949, 1(3), 300--302, DOI | VERIFIED | None. Publisher display uses `Taussky`/later `Taussky-Todd`; registered publication author is not an error. |
| P31-S09 | `10.1090/S0002-9947-1984-0735415-0 Wallace Conjugacy Classes Hyperbolic Matrices SL(n,Z)` | https://doi.org/10.1090/S0002-9947-1984-0735415-0 | author, title, journal, 1984, 283(1), 177--184, DOI | VERIFIED | None. |
| P31-S10 | `10.1080/00927878108822637 Appelgate Onishi Continued Fractions Conjugacy Problem` | https://www.tandfonline.com/doi/abs/10.1080/00927878108822637 | two authors, title, journal, 1981, 9(11), 1121--1130, DOI | VERIFIED | None. |
| P31-S11 | `10.1016/S0049-237X(08)71335-1 Grunewald Solution Conjugacy Problem Arithmetic Groups` | https://doi.org/10.1016/S0049-237X(08)71335-1 | author, chapter title, `Word Problems II`, 1980, vol. 95, 101--139, DOI | VERIFIED | None; book-chapter identity also appears in the reference list of the primary Annals record for P31-S12. |
| P31-S12 | `10.2307/1971091 Grunewald Segal Some General Algorithms I Arithmetic Groups` | https://www.jstor.org/stable/1971091 | two authors, exact title, Annals, 1980, 112(3), 531--583, DOI | VERIFIED | None. |
| P31-S13 | `10.1112/jlms.12246 Eick Hofmann O'Brien conjugacy GL(n,Z) 2019` | https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/jlms.12246 | three authors, exact title, 2019, 100(3), 731--756, DOI | VERIFIED | None. |
| P31-S14 | `10.1016/0022-314X(82)90028-2 Sarnak Class Numbers Indefinite Binary Quadratic Forms` | https://www.sciencedirect.com/science/article/pii/0022314X82900282 | author, title, journal, 1982, 15(2), 229--247, DOI | VERIFIED | None. |
| P31-S15 | `10.1112/jlms/s2-31.1.69 Series Modular Surface Continued Fractions` | https://doi.org/10.1112/jlms/s2-31.1.69 | author, title, journal, 1985, s2-31(1), 69--80, DOI | VERIFIED | None. |
| P31-S16 | `10.1142/S0218196706002986 Epstein Holt Linearity Conjugacy Problem Word-Hyperbolic Groups pages` | https://doi.org/10.1142/S0218196706002986 | two authors, title, journal, 2006, 16(2), 287--305, DOI | VERIFIED | Third-party DBLP reports 287--306. The article first page and AMS references report 287--305, confirming the already-authorized frozen correction; no new edit. |
| P31-S17 | `10.1142/S0218196713500203 Buckley Holt conjugacy finite lists hyperbolic groups` | https://doi.org/10.1142/S0218196713500203 | two authors, title, journal, 2013, 23(5), 1127--1150, DOI | VERIFIED | None. |
| P31-S18 | `10.1088/0951-7715/14/4/201 Baake Roberts Symmetries Reversing Toral Automorphisms` | https://doi.org/10.1088/0951-7715/14/4/201 | two authors, title, Nonlinearity, 2001, 14(4), R1--R24, DOI | VERIFIED | None. |
| P31-S19 | `site:ams.org/notices/200202 Lenstra Solving Pell Equation 182 192` | https://www.ams.org/notices/200202/fea-lenstra.pdf | author, title, Notices, 2002, 49(2), 182--192 | VERIFIED | None. |
| P31-S20 | `10.1007/978-3-662-02945-9 Cohen Course Computational Algebraic Number Theory` | https://link.springer.com/book/10.1007/978-3-662-02945-9 | author, title, Springer/GTM 138, 1993, DOI | VERIFIED | None. The DOI is the later ebook identifier for the registered 1993 book, which Springer explicitly identifies as copyright 1993. |
| P31-S21 | `10.1070/SM2008v199n07ABEH003951 Golovchanskii Smotrov primitive hyperbolic Gamma0 N` | https://www.mathnet.ru/eng/sm3853 | two authors, exact title, Sbornik, 2008, 199(7), 1009--1031, DOI | VERIFIED | None. |
| P31-S22 | `10.1016/0022-314X(85)90049-6 Traina Conjugacy Problem Modular Group Class Number` | https://doi.org/10.1016/0022-314X(85)90049-6 | author, title, JNT, 1985, 21(2), 176--184, DOI | VERIFIED | None. |

### Phase A closure and ghost-citation replay

- Reference existence: `22 VERIFIED / 0 NOT_FOUND / 0 MISMATCH`.
- Bibliographic edits required: `0`.
- BibTeX keys: `22`, all unique.
- In-text cited keys: `22`, all unique.
- Orphans: `0`; dangling citations: `0`; duplicate BibTeX keys: `0`.
- P31-S16's known page-range conflict was replayed and remains resolved in favor
  of the primary 287--305 record.

## Phase B — deterministic citation-context sample

Selection rule: partition cited keys by the four citation-bearing literature
subsections; take the first key in each subsection, then round-robin through the
next key in each subsection in manuscript order until reaching
`ceil(0.30 * 22) = 7`. This yields P31-S01, S07, S15, S14, S02, S08, and S16.
All citation-bearing major subsections are represented.

| Context | Exact manuscript locator | Cited key | Source evidence used | Verdict and boundary |
|---|---|---|---|---|
| finite-index modular-subgroup structure | `manuscript.tex:150-156`, §2.1 | P31-S01 | exact DOI/publisher metadata and frozen source verification | ACCURATE_WITH_BOUNDARY. The work is a modular-subgroup classification precedent; the following prose correctly withholds the project-specific solver/certificate inference. |
| arithmetic-geometric subgroup interface | `manuscript.tex:150-156`, §2.1 | P31-S02 | exact DOI record plus the identifiable MPIM precursor | ACCURATE_WITH_BOUNDARY. It supports an arithmetic-geometric subgroup method, not P31 owner bytes or pair closure. |
| ideal-class/matrix correspondence | `manuscript.tex:182-187`, §2.2 | P31-S07 | exact DOI/title and authoritative bibliographic record | ACCURATE_WITH_BOUNDARY. The cited relation is the work's named subject; the manuscript explicitly prevents transfer to the frozen subgroup. |
| Latimer--MacDuffee refinement | `manuscript.tex:182-187`, §2.2 | P31-S08 | Cambridge article page and article extract | ACCURATE_WITH_BOUNDARY. The paper is a refinement of the stated ideal/matrix correspondence; no oriented `Gamma_0(11)` conclusion is claimed. |
| modular-geodesic coding/reduction context | `manuscript.tex:214-217`, §2.3 | P31-S15 | exact DOI/title/journal metadata | ACCURATE_WITH_BOUNDARY. The prose says only `relevant coding context`, then expressly withholds combined canonicalization and termination. |
| word-hyperbolic conjugacy precedent | `manuscript.tex:218-221`, §2.3 | P31-S16 | article abstract/first page: linear-time conjugacy in word-hyperbolic groups | ACCURATE_WITH_BOUNDARY. The manuscript does not equate this ambient algorithm with its marked subgroup certificate interface. |
| aggregate class-number context | `manuscript.tex:244-246`, §2.4 | P31-S14 | publisher abstract: asymptotic average sizes of class numbers of indefinite forms | ACCURATE_WITH_BOUNDARY. It is used only as aggregate context, and lines 253--258 explicitly deny pair-level sufficiency. |

### Phase B result

- Checked: `7/22 = 31.8%` of cited-reference contexts.
- Passed: `7`; issues: `0`.
- No cherry-picking, numerical misquotation, or promotion beyond the frozen
  source fitness boundary was found in this deterministic sample.
- All sampled citations remain anchorless in the manuscript's ARS markers. This
  audit verifies the displayed broad context against authoritative records; it
  does not convert `anchor=none` into a passage-level human-read attestation and
  does not silently clear the Stage-1 locator limitation for unsampled claims.

## Findings to forward

No correction request is produced for P31 Phase A/B. Preserve the following
non-blocking observations in the batch synthesis:

1. `P31-S16` has a live third-party metadata conflict (`287--306` in DBLP), but
   primary article/AMS evidence supports the frozen `287--305`; current BibTeX is
   correct.
2. The Phase-B sample supports the manuscript's deliberately bounded literature
   characterization. It does not prove the project-specific canonicalizer,
   certificate completeness, or any Route result.

