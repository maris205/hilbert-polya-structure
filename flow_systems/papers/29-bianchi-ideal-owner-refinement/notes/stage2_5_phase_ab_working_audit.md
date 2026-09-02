# Stage 2.5 Phase A/B working integrity audit — Paper 29

Audit time: 2026-09-02T15:51:27Z (UTC)

Status: working audit sidecar; bounded to reference integrity and sampled citation-context integrity. This file is not a Stage 2.5 verdict, checkpoint, passport, receipt, or authorization artifact.

## Scope and frozen inputs

This audit is read-only with respect to the manuscript, bibliography, PDF, pipeline state, README, claim registry, and all canonical batch artifacts. It did not execute scientific experiments, recompute scientific results, or evaluate Route A/Route B. Web checks were run independently of the inherited Stage-1 verdicts and then compared with the frozen verification and citation-review files.

| Frozen input | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `5bee689a055f99819fb6df1f6e992610fe0dea7ebffc87219758116bf06bd034` |
| `paper/references.bib` | `433638db4cd984ab195beb7643a0581b1a9a9dc0b5df46f54634bd704194c253` |
| `notes/stage1_phase2_source_verification.tsv` | `bcf5fa7af07f353fbcaaa6fca319e79f173d7a6af070b58276a91fe9a44d8901` |
| `notes/stage1_phase5_citation_integrity_review.md` | `cb1fd940a7516aadd47c113a7bf4cff59e6cb8e53fc29457294a065fd9356b59` |

The source-ID-to-BibTeX-key map is the identity map (`P29-Snn` -> `P29-Snn`). The frozen bibliography contains 22 entries. The frozen manuscript has 22 citation occurrences, 22 distinct cited keys, and 22 `ARS-CITE` markers.

## Method

### Phase A — 100% reference verification

Every bibliography entry was searched again using the exact query shown below. A DOI resolver, publisher page, first-party arXiv record, scholarly-society page, or institutional record was retained as the authoritative top URL. Confirmed fields are abbreviated as `A` author/editor, `T` title, `Y` year, `J/B` journal/book, `V/I` volume/issue, `P` pages/article number, and `D` DOI or arXiv identifier.

`VERIFIED` means that the referenced work exists and its identity is confirmed. `VERIFIED_WITH_CONFLICT` means identity is confirmed and a non-actionable display discrepancy is preserved. `METADATA_MISMATCH` means the work exists but the frozen BibTeX row contains an actionable metadata error.

The caveat codes in the last column apply per row:

- `C0`: no correction or retraction indicator surfaced on the authoritative record or exact-query results reviewed in this bounded audit. No structured Crossmark/Retraction Watch search was run, so this is not a retraction-clearance certificate.
- `C1`: the original article is correction-bound to the stated companion; the check is not general retraction clearance.
- `C2`: first-party arXiv preprint; existence and metadata are verified, but peer review is not implied.
- `C3`: the original/JSTOR title is “Some general algorithms. I: Arithmetic groups”; the current Annals display says “Strong general algorithms. I: Arithmetic groups.” The conflict is recorded rather than silently normalized.
- `C4`: publisher and author/institutional records give pages 287–305; DBLP displays 287–306. The frozen 287–305 is retained as publisher-supported.
- `C5`: the chapter exists, but the containing-volume editor list is incomplete in the frozen BibTeX row; see finding `P29-AB-MEDIUM-01`.

## Phase A results

| Source ID / BibTeX key | Exact query or identifier searched | Authoritative top URL | Existence and metadata verdict | Caveat |
|---|---|---|---|---|
| `P29-S01` | `10.1016/j.aim.2020.107377 Balkanova Frolenkov` | [DOI record](https://doi.org/10.1016/j.aim.2020.107377) | `VERIFIED`; A/T/Y/J/V/P/D exact | C0 |
| `P29-S02` | `10.2140/ant.2022.16.1845 Kaneko` | [publisher DOI](https://doi.org/10.2140/ant.2022.16.1845) | `VERIFIED`; A/T/Y/J/V/I/P/D exact | C0 |
| `P29-S03` | `10.1093/imrn/rnaa128 Balog Biro Cherubini Laaksonen` | [publisher DOI](https://doi.org/10.1093/imrn/rnaa128) | `VERIFIED`; A/T/Y/J/V/I/P/D exact | C0 |
| `P29-S04` | `10.1515/form.2001.034 Koyama` | [De Gruyter record](https://www.degruyterbrill.com/document/doi/10.1515/form.2001.034/html) | `VERIFIED`; A/T/Y/J/V/I/P/D exact | C0 |
| `P29-S05` | `"10.3792/pjaa.77.130" Nakasuji` | [publisher DOI](https://doi.org/10.3792/pjaa.77.130) | `VERIFIED`; A/T/Y/J/V/I/P/D exact | C0 |
| `P29-S06` | `"10.1002/mana.201700190" Avdispahic` | [Wiley record](https://onlinelibrary.wiley.com/doi/abs/10.1002/mana.201700190) | `VERIFIED`; A/T/Y/J/V/I/P/D exact | C1: mandatory companion `10.1002/mana.201800467` |
| `P29-S07` | `"10.1002/mana.201800467" Avdispahic` | [Wiley correction](https://onlinelibrary.wiley.com/doi/pdf/10.1002/mana.201800467) | `VERIFIED`; A/T/Y/J/V/I/P/D and correction identity exact | C1: correction/addendum to S06; it corrects an exponent and is not an independent mechanism source |
| `P29-S08` | `"10.1093/imrn/rnab048" Dever Milicevic` | [publisher DOI](https://doi.org/10.1093/imrn/rnab048) | `VERIFIED`; A/T/Y/J/V/I/P/D exact | C0 |
| `P29-S09` | `arXiv 2407.17959 Zhi Qi symmetric square large sieve PSL2 Gaussian` | [arXiv](https://arxiv.org/abs/2407.17959) | `VERIFIED`; A/T/Y/arXiv ID exact | C2 |
| `P29-S10` | `"10.1090/S0025-5718-2015-02939-1" Page` | [AMS DOI](https://doi.org/10.1090/S0025-5718-2015-02939-1) | `VERIFIED`; A/T/Y/J/V/I/P/D exact | C0 |
| `P29-S11` | `"10.2307/1971091" Grunewald Segal` | [JSTOR record](https://www.jstor.org/stable/1971091) | `VERIFIED_WITH_CONFLICT`; A/Y/J/V/I/P/D exact; original/JSTOR T supported | C3 |
| `P29-S12` | `"10.1016/j.top.2005.06.002" Preaux` | [publisher DOI](https://doi.org/10.1016/j.top.2005.06.002) | `VERIFIED`; A/T/Y/J/V/I/P/D exact | C0 |
| `P29-S13` | `"10.1142/S0218196706002986" Epstein Holt` | [publisher DOI](https://doi.org/10.1142/S0218196706002986) | `VERIFIED_WITH_CONFLICT`; A/T/Y/J/V/I/D exact; publisher-supported P exact | C4 |
| `P29-S14` | `"10.1112/jlms.12246" Eick Hofmann O'Brien` | [Wiley record](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/jlms.12246) | `VERIFIED`; A/T/Y/J/V/I/P/D exact | C0 |
| `P29-S15` | `"10.1016/S0049-237X(08)71335-1" Grunewald` | [ScienceDirect chapter](https://www.sciencedirect.com/science/chapter/bookseries/pii/S0049237X08713351) | `METADATA_MISMATCH`; chapter A/T/Y/B/series/V/P/D exact; containing-volume A incomplete | C5 |
| `P29-S16` | `"10.1016/0001-8708(71)90027-2" Swan` | [ScienceDirect record](https://www.sciencedirect.com/science/article/pii/0001870871900272) | `VERIFIED`; A/T/Y/J/V/I/P/D exact | C0 |
| `P29-S17` | `"10.1007/978-1-4757-6720-9" Maclachlan Reid` | [Springer book](https://link.springer.com/book/10.1007/978-1-4757-6720-9) | `VERIFIED`; A/T/Y/B/series/V/D exact | C0 |
| `P29-S18` | `"10.1007/978-3-662-03626-6" Elstrodt Grunewald Mennicke` | [Springer book](https://link.springer.com/book/10.1007/978-3-662-03626-6) | `VERIFIED`; A/T/Y/B/series/D exact | C0 |
| `P29-S19` | `"10.1007/978-3-662-02945-9" Henri Cohen` | [Springer book](https://link.springer.com/book/10.1007/978-3-662-02945-9) | `VERIFIED`; A/T/Y/B/series/V/D exact | C0 |
| `P29-S20` | `"10.1090/S0273-0979-1992-00284-7" Lenstra` | [AMS DOI](https://doi.org/10.1090/S0273-0979-1992-00284-7) | `VERIFIED`; A/T/Y/J/V/I/P/D exact; AMS supports 211–244 | C0 |
| `P29-S21` | `"10.5802/jtnb.433" Belabas` | [Centre Mersenne](https://jtnb.centre-mersenne.org/item/JTNB_2004__16_1_19_0/) | `VERIFIED`; A/T/Y/J/V/I/P/D exact | C0 |
| `P29-S22` | `"10.1090/mcom/3913" Belabas Simon` | [AMS DOI](https://doi.org/10.1090/mcom/3913) | `VERIFIED`; A/T/Y/J/V/I/P/D exact | C0 |

### Phase A counts and closure

- References searched: 22/22 (100%).
- Existence/identity verified: 22/22.
- Rows without an actionable metadata error: 21/22.
- Actionable metadata mismatches: 1/22.
- Exact closure: 22 bibliography keys = 22 distinct cited keys = 22 citation occurrences = 22 `ARS-CITE` source IDs.
- Orphan bibliography entries: 0. Dangling cited keys: 0. Unknown source IDs: 0. Duplicate BibTeX keys: 0.

### Actionable finding

`P29-AB-MEDIUM-01` — `P29-S15` omits two editors of *Word Problems II*. The frozen row has only `editor = {Higman, Graham}`. The [1980 AMS publisher advertisement](https://www.ams.org/journals/notices/198002/198002FullIssue.pdf) states “edited by S. I. Adian, W. W. Boone, and G. Higman”; the [CiNii library record](https://ci.nii.ac.jp/ncid/BA04017053) and [Google Books bibliographic record](https://books.google.com/books/about/Word_Problems_II.html?id=W9-AAAAAIAAJ) independently list the same three editors. The chapter identity, author, title, pages 101–139, series volume 95, year, publisher, and DOI remain verified. Severity: **MEDIUM bibliographic metadata error** by analogy with omitted contributor metadata. Proposed later repair, subject to separate authorization:

```bibtex
editor = {Adian, S. I. and Boone, W. W. and Higman, Graham}
```

No bibliography edit was made in this audit.

## Phase B — deterministic citation-context sample

The denominator is 22 citation occurrences (each cited key occurs once), so the minimum sample is `ceil(0.30 * 22) = 7`. Deterministic selection rule: select the first citation in every citation-bearing subsection, then select citation ordinals divisible by four in manuscript order until the target is reached; if still short, add the next remaining occurrence in manuscript order. Sorting the selected set back into manuscript order yields ordinals 1, 4, 8, 12, 16, 19, and 20. This covers all three citation-bearing subsections in `Frozen Literature and Theoretical Frame`.

`SUPPORTED_WITH_BOUNDARY` means the authoritative source record, abstract, or accessible full text supports the cited positive context and the manuscript states a compatible non-transfer boundary. It does **not** freeze a page/theorem/paragraph anchor and does not change the manuscript's existing `anchor=none; claim_to_passage=INCONCLUSIVE` marker.

| Sample | Exact manuscript locator | Cited key | Authoritative evidence locator | Support verdict | Verified support and boundary |
|---|---|---|---|---|---|
| 1 | lines 67–69; § “The Picard/Bianchi object does not itself supply an owner law” | `P29-S01` | [DOI record](https://doi.org/10.1016/j.aim.2020.107377) | `SUPPORTED_WITH_BOUNDARY` | Title/abstract establish a prime-geodesic theorem for the Picard manifold. They do not instantiate the manuscript's class-to-ideal owner map; the sentence uses the source only as object/analytic context. No exact passage anchor is frozen. |
| 2 | lines 79–81; same subsection | `P29-S08` | [authoritative repository full text](https://par.nsf.gov/servlets/purl/10351743) | `SUPPORTED_WITH_BOUNDARY` | Full text treats primitive closed geodesics/conjugacy classes, complex length modulo inversion, and explicitly suppresses the `gamma_0` versus `gamma_0^{-1}` distinction. Its compact cocompact torsion-free setting is not the frozen noncompact level-(3) Picard decision problem; the manuscript preserves that non-transfer boundary. |
| 3 | lines 95–97; same subsection | `P29-S07` | [Wiley correction](https://onlinelibrary.wiley.com/doi/pdf/10.1002/mana.201800467) | `SUPPORTED_WITH_BOUNDARY` | The record is explicitly an erratum/addendum to S06 and corrects an affected analytic exponent. Calling it a correction boundary rather than a new owner mechanism or retraction-clearance record is faithful. |
| 4 | lines 115–117; § “Quotient completeness is a composite certificate target” | `P29-S10` | [first-party preprint record](https://arxiv.org/abs/1206.0087) | `SUPPORTED_WITH_BOUNDARY` | Abstract/full-text scope supports algorithms for arithmetic Kleinian fundamental domains and finite presentations. It does not by itself supply the composite level-(3), maximal-root, conjugacy, inversion, and unoriented canonicalization certificate claimed as still open. |
| 5 | lines 131–133; same subsection | `P29-S12` | [author full text](https://www.jean-philippe-preaux.fr/PDF/CP_in_3M.pdf) | `SUPPORTED_WITH_BOUNDARY` | The source solves conjugacy for fundamental groups of oriented geometrizable 3-manifolds under its stated input class. The manuscript correctly requires an exact reduction before importing it into the frozen projective subgroup problem. |
| 6 | lines 147–149; § “Ideal arithmetic validates outputs but does not choose owners” | `P29-S19` | [Springer book record](https://link.springer.com/book/10.1007/978-3-662-02945-9) | `SUPPORTED_WITH_BOUNDARY` | Book scope supports computational algebraic-number-theory and ideal-factorization algorithms. The negative boundary—such algorithms do not thereby choose a geometric class's literal split-prime branch—is a cautious non-transfer statement. Exact supporting pages were not frozen, so passage-level status remains unresolved. |
| 7 | lines 151–153; same subsection | `P29-S20` | [AMS DOI record](https://doi.org/10.1090/S0273-0979-1992-00284-7) | `SUPPORTED_WITH_BOUNDARY` | Article scope supports effective algorithms in algebraic number theory. Certificate-oriented implementation is a project synthesis, and the source is not represented as supplying a class-to-ideal selection law. No exact passage anchor is frozen. |

### Phase B counts and disposition

- Citation occurrences sampled: 7/22 = 31.8%.
- Citation-bearing subsections covered: 3/3.
- `SUPPORTED_WITH_BOUNDARY`: 7/7.
- Contradicted, distorted, or source-incompatible sampled contexts: 0/7.
- Exact source passage anchors added to the manuscript or canonical records: 0; all frozen `ARS-CITE` markers remain unchanged.

## Bounded disposition

- Phase A working result: **FAIL pending authorization/repair** because `P29-AB-MEDIUM-01` is an actionable omitted-editor metadata error, although all 22 works exist and citation closure is exact.
- Phase B working result: **PASS WITH BOUNDARIES** for the deterministic 31.8% semantic sample; this is not an upgrade of the frozen passage-anchor status.
- Overall Stage 2.5: **not evaluated by this sidecar**. Other integrity phases, independent-model requirements, structured retraction checks, and any pipeline transition remain outside scope.
