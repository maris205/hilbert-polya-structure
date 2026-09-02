# Stage 2.5 Phase A/B working integrity audit — Paper 30

Audit time: 2026-09-02T15:51:27Z (UTC)

Status: working audit sidecar; bounded to reference integrity and sampled citation-context integrity. This file is not a Stage 2.5 verdict, checkpoint, passport, receipt, or authorization artifact.

## Scope and frozen inputs

This audit is read-only with respect to the manuscript, bibliography, PDF, pipeline state, README, claim registry, and all canonical batch artifacts. It did not execute scientific experiments, recompute scientific results, or evaluate Route A/Route B. Web checks were run independently of the inherited Stage-1 verdicts and then compared with the frozen verification and citation-review files.

| Frozen input | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `af270bc06a3f1e00d657fdc875585e3da9ab9b2b7198ad8d096d188a93af9506` |
| `paper/references.bib` | `1b2538b3cfa9e0326112dd3ae086a420032e4edecd06f9e27939d2691d10de6f` |
| `notes/stage1_phase2_source_verification.tsv` | `5442161a39d94fe62d57acb664c2536594500b79d9e6c29cae775d01567c7472` |
| `notes/stage1_phase5_citation_integrity_review.md` | `8c6d1fb63b7c170ca7dc9aae0287a807e2ba83187afcbe87fec5ea2e3c025d3c` |

The source-ID-to-BibTeX-key map is the identity map (`P30-Snn` -> `P30-Snn`). The frozen bibliography contains 26 entries. The frozen manuscript has 26 citation occurrences, 26 distinct cited keys, and 26 `ARS-CITE` markers.

## Method

### Phase A — 100% reference verification

Every bibliography entry was searched again using the exact query shown below. A DOI resolver, publisher page, first-party arXiv record, scholarly-society page, or institutional record was retained as the authoritative top URL. Confirmed fields are abbreviated as `A` author, `T` title, `Y` year, `J/B` journal/book, `V/I` volume/issue, `P` pages/article number, and `D` DOI or arXiv identifier.

`VERIFIED` means that the referenced work exists and the frozen core metadata are confirmed or reconciled against the authoritative publication chronology.

The caveat codes in the last column apply per row:

- `C0`: no correction or retraction indicator surfaced on the authoritative record or exact-query results reviewed in this bounded audit. No structured Crossmark/Retraction Watch search was run, so this is not a retraction-clearance certificate.
- `C1`: affected use is bound to the listed Gaspard–Rice correction companion; the companion is verified, but this is not general retraction clearance.
- `C2`: S17's affected Section-7 use is bound to the first-party S18 erratum; the erratum says the first meromorphicity part is unaffected and corrects the spectral-gap part.
- `C3`: first-party arXiv erratum; existence and metadata are verified, but it is not independent peer-reviewed support.
- `C4`: official issue year is 2010 although online publication occurred in 2009; the frozen 2010 is correct.
- `C5`: official issue year is 2026 although online-first publication occurred in December 2025; the frozen 2026 is correct.

## Phase A results

| Source ID / BibTeX key | Exact query or identifier searched | Authoritative top URL | Existence and metadata verdict | Caveat |
|---|---|---|---|---|
| `P30-S01` | `"10.1063/1.456017" Gaspard Rice` | [AIP DOI](https://doi.org/10.1063/1.456017) | `VERIFIED`; A/T/Y/J/V/I/P/D exact | C1: correction DOI `10.1063/1.457669` |
| `P30-S02` | `"10.1063/1.456018" Gaspard Rice` | [AIP DOI](https://doi.org/10.1063/1.456018) | `VERIFIED`; A/T/Y/J/V/I/P/D exact | C1: correction DOI `10.1063/1.457669` |
| `P30-S03` | `"10.1063/1.456019" Gaspard Rice` | [AIP DOI](https://doi.org/10.1063/1.456019) | `VERIFIED`; A/T/Y/J/V/I/P/D exact | C1: correction DOI `10.1063/1.457670` |
| `P30-S04` | `"10.1103/PhysRevLett.63.823" Cvitanovic Eckhardt` | [APS record](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.63.823) | `VERIFIED`; A/T/Y/J/V/I/P/D exact | C0 |
| `P30-S05` | `"10.1088/0305-4470/24/5/005" Cvitanovic Eckhardt` | [IOP DOI](https://doi.org/10.1088/0305-4470/24/5/005) | `VERIFIED`; A/T/Y/J/V/I/P/D exact | C0 |
| `P30-S06` | `"10.1016/S0370-1573(98)00036-2" Wirzba` | [ScienceDirect record](https://www.sciencedirect.com/science/article/abs/pii/S0370157398000362) | `VERIFIED`; A/T/Y/J/V/I/P/D exact | C0 |
| `P30-S07` | `"10.2307/2373793" Bowen symbolic dynamics hyperbolic flows` | [JSTOR record](https://www.jstor.org/stable/2373793) | `VERIFIED`; A/T/Y/J/V/I/P/D exact | C0 |
| `P30-S08` | `"10.1007/BF01389848" Bowen Ruelle` | [Springer record](https://link.springer.com/article/10.1007/BF01389848) | `VERIFIED`; A/T/Y/J/V/I/P/D exact | C0 |
| `P30-S09` | `"10.5802/aif.1137" Ikawa` | [Centre Mersenne](https://aif.centre-mersenne.org/articles/10.5802/aif.1137/) | `VERIFIED`; A/T/Y/J/V/I/P/D exact | C0 |
| `P30-S10` | `"10.5802/jedp.457" Ikawa` | [Centre Mersenne proceedings](https://proceedings.centre-mersenne.org/articles/10.5802/jedp.457/) | `VERIFIED`; A/T/Y/B/P/D exact | C0; research proceedings, no journal peer-review status inferred |
| `P30-S11` | `"10.1353/ajm.2001.0029" Stoyanov` | [Project MUSE DOI](https://doi.org/10.1353/ajm.2001.0029) | `VERIFIED`; A/T/Y/J/V/I/P/D exact | C0 |
| `P30-S12` | `"10.1088/0951-7715/24/4/005" Stoyanov` | [IOP DOI](https://doi.org/10.1088/0951-7715/24/4/005) | `VERIFIED`; A/T/Y/J/V/I/P/D exact | C0 |
| `P30-S13` | `"10.1007/BF01403069" Ruelle` | [Springer DOI](https://doi.org/10.1007/BF01403069) | `VERIFIED`; A/T/Y/J/V/I/P/D exact | C0 |
| `P30-S14` | `"10.1007/BF02699133" Ruelle` | [Centre Mersenne](https://pmihes.centre-mersenne.org/articles/10.1007/BF02699133/) | `VERIFIED`; A/T/Y/J/V/P/D exact | C0 |
| `P30-S15` | `"10.1007/BF01388795" Pollicott` | [Springer DOI](https://doi.org/10.1007/BF01388795) | `VERIFIED`; A/T/Y/J/V/I/P/D exact | C0 |
| `P30-S16` | `"10.1007/BF02099469" Fried` | [Springer DOI](https://doi.org/10.1007/BF02099469) | `VERIFIED`; A/T/Y/J/V/I/P/D exact | C0 |
| `P30-S17` | `"10.4007/annals.2013.178.2.6" Giulietti Liverani Pollicott` | [Annals article](https://annals.math.princeton.edu/2013/178-2/p06) | `VERIFIED`; A/T/Y/J/V/I/P/D exact | C2: mandatory `P30-S18` boundary for affected Section 7 |
| `P30-S18` | `arXiv 2203.04917 Giulietti Pollicott Liverani errata` | [arXiv](https://arxiv.org/abs/2203.04917) | `VERIFIED`; A/T/Y/arXiv ID and erratum identity exact | C3 |
| `P30-S19` | `"10.1007/s00220-007-0355-7" Bandtlow Jenkinson` | [Springer DOI](https://doi.org/10.1007/s00220-007-0355-7) | `VERIFIED`; A/T/Y/J/V/I/P/D exact | C0 |
| `P30-S20` | `"10.1016/j.aim.2008.02.005" Bandtlow Jenkinson` | [ScienceDirect record](https://www.sciencedirect.com/science/article/pii/S0001870808000492) | `VERIFIED`; A/T/Y/J/V/I/P/D exact | C0 |
| `P30-S21` | `"10.1007/s00211-019-01031-z" Wormell` | [Springer DOI](https://doi.org/10.1007/s00211-019-01031-z) | `VERIFIED`; A/T/Y/J/V/I/P/D exact | C0 |
| `P30-S22` | `"10.1090/S0025-5718-09-02280-7" Bornemann` | [AMS article](https://www.ams.org/mcom/2010-79-270/S0025-5718-09-02280-7/) | `VERIFIED`; A/T/J/V/I/P/D exact; official issue Y reconciled | C4 |
| `P30-S23` | `"10.1070/IM1972v006n06ABEH001919" Livsic` | [Math-Net record](https://www.mathnet.ru/eng/im2373) | `VERIFIED`; A/T/Y/J/V/I/P/D exact; Livšic/Livshits is transliteration | C0 |
| `P30-S24` | `"10.2307/1971334" de la Llave Marco Moriyon` | [Annals article](https://annals.math.princeton.edu/1986/123-3/p03) | `VERIFIED`; A/T/Y/J/V/I/P/D exact | C0 |
| `P30-S25` | `"10.4007/annals.2011.173.2.11" Kalinin` | [Annals article](https://annals.math.princeton.edu/2011/173-2/p11) | `VERIFIED`; A/T/Y/J/V/I/P/D exact | C0 |
| `P30-S26` | `"10.1112/blms.70258" Sharp` | [Wiley record](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/blms.70258) | `VERIFIED`; A/T/J/V/I/article/D exact; official issue Y reconciled | C5 |

### Correction-companion audit trail

The bibliography notes for S01–S03 state companion DOIs but the companions are not separate BibTeX keys. Exact companion searches were therefore also run:

| Affected source(s) | Exact query | Stable record | Result |
|---|---|---|---|
| `P30-S01`, `P30-S02` | `"10.1063/1.457669" erratum Gaspard Rice` | [DOI](https://doi.org/10.1063/1.457669) | First-party erratum identity verified; mandatory for affected use; not a standalone frozen bibliography key. |
| `P30-S03` | `"10.1063/1.457670" erratum Gaspard Rice` | [DOI](https://doi.org/10.1063/1.457670) | First-party erratum identity verified; mandatory for affected use; not a standalone frozen bibliography key. |

### Phase A counts and closure

- References searched: 26/26 (100%), plus both correction-companion DOI records.
- Existence/identity verified: 26/26.
- Rows without an actionable metadata error: 26/26.
- Actionable metadata mismatches: 0/26.
- Exact closure: 26 bibliography keys = 26 distinct cited keys = 26 citation occurrences = 26 `ARS-CITE` source IDs.
- Orphan bibliography entries: 0. Dangling cited keys: 0. Unknown source IDs: 0. Duplicate BibTeX keys: 0.

## Phase B — deterministic citation-context sample

The denominator is 26 citation occurrences (each cited key occurs once), so the minimum sample is `ceil(0.30 * 26) = 8`. Deterministic selection rule: select the first citation in every citation-bearing subsection, then select citation ordinals divisible by four in manuscript order until the target is reached; if still short, add the next remaining occurrence in manuscript order. Sorting the selected set back into manuscript order yields ordinals 1, 4, 8, 9, 12, 17, 19, and 23. This covers all five citation-bearing subsections in `Frozen Literature and Theoretical Frame`.

`SUPPORTED_WITH_BOUNDARY` means the authoritative source record, abstract, or accessible full text supports the cited positive context and the manuscript states a compatible non-transfer boundary. It does **not** freeze a page/theorem/paragraph anchor and does not change the manuscript's existing `anchor=none; claim_to_passage=INCONCLUSIVE` marker.

| Sample | Exact manuscript locator | Cited key | Authoritative evidence locator | Support verdict | Verified support and boundary |
|---|---|---|---|---|---|
| 1 | lines 69–71; § “A determinant-type firewall” | `P30-S01` | [AIP DOI](https://doi.org/10.1063/1.456017); [correction DOI](https://doi.org/10.1063/1.457669) | `SUPPORTED_WITH_BOUNDARY` | The article establishes the classical chaotic-repellor/three-hard-disk setting; formula-level use is correction-bound. The manuscript does not infer a project roof ledger, classical transfer determinant, or numerical certificate from it. |
| 2 | lines 81–83; same subsection | `P30-S04` | [APS abstract](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.63.823) | `SUPPORTED_WITH_BOUNDARY` | Abstract supports periodic-orbit estimates and resonance organization for the three-disk system. It supplies no nuclearity theorem or complete numerical error contract; the manuscript says so. |
| 3 | lines 97–99; same subsection | `P30-S10` | [Centre Mersenne article](https://proceedings.centre-mersenne.org/articles/10.5802/jedp.457/) | `SUPPORTED_WITH_BOUNDARY` | Source scope directly links zeta functions and scattering poles for several convex bodies. It is a proceedings contribution and does not provide the frozen project's roof-ledger certificate or journal-weight claim. |
| 4 | lines 105–107; § “The exact d=6a object map remains prospective” | `P30-S07` | [JSTOR record](https://www.jstor.org/stable/2373793) | `SUPPORTED_WITH_BOUNDARY` | Bowen supports symbolic dynamics/Markov coding for hyperbolic flows. The citation does not identify the exact three-disk Poincaré section, inverse branches, Euclidean-flight roof, or function space; the manuscript leaves those prospective. |
| 5 | lines 117–119; same subsection | `P30-S12` | [arXiv full-text record](https://arxiv.org/abs/0810.1126) | `SUPPORTED_WITH_BOUNDARY` | Source supports conditional spectral estimates for Ruelle transfer operators of Axiom-A flows. It does not choose the project's section, regularity, basis, rank, cutoffs, or hypothesis map. |
| 6 | lines 141–143; § “Roof-agnostic internal calibration” | `P30-S13` | [Springer DOI](https://doi.org/10.1007/BF01403069) | `SUPPORTED_WITH_BOUNDARY` | Source scope supports zeta functions for expanding maps and Anosov flows and the periodic/transfer formal background. Physical three-disk roof specificity is not inferred from the formal identity. |
| 7 | lines 153–155; § “Four numerical components and a separate input-uncertainty channel” | `P30-S19` | [Springer DOI](https://doi.org/10.1007/s00220-007-0355-7) | `SUPPORTED_WITH_BOUNDARY` | Source supports explicit a priori eigenvalue bounds for transfer operators defined from eligible holomorphic data. Application remains conditional on instantiating the project operator space and constants. |
| 8 | lines 183–185; § “Directional Livšic reasoning” | `P30-S23` | [Math-Net record](https://www.mathnet.ru/eng/im2373) | `SUPPORTED_WITH_BOUNDARY` | Source supports periodic-data criteria for cohomological nullity in stated hyperbolic/symbolic systems. The manuscript faithfully uses only the directional boundary: a lawful mismatch may obstruct a fixed relation, whereas finite agreement cannot prove global cohomology. |

### Phase B counts and disposition

- Citation occurrences sampled: 8/26 = 30.8%.
- Citation-bearing subsections covered: 5/5.
- `SUPPORTED_WITH_BOUNDARY`: 8/8.
- Contradicted, distorted, or source-incompatible sampled contexts: 0/8.
- Exact source passage anchors added to the manuscript or canonical records: 0; all frozen `ARS-CITE` markers remain unchanged.

## Bounded disposition

- Phase A working result: **PASS WITH CORRECTION/CHRONOLOGY CAVEATS**; all 26 references exist, core metadata agree, and closure is exact.
- Phase B working result: **PASS WITH BOUNDARIES** for the deterministic 30.8% semantic sample; this is not an upgrade of the frozen passage-anchor status.
- Overall Stage 2.5: **not evaluated by this sidecar**. Other integrity phases, independent-model requirements, structured retraction checks, and any pipeline transition remain outside scope.

