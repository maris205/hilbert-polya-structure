# Paper 17 pre-manuscript source/citation audit

Audit date: **2026-08-17 (Asia/Shanghai)**  
Audit role: independent local-only source acquisition, PDF read-integrity,
claim/reference alignment, owner/locator, and source-exclusion preflight  
Effective verdict: **PASS within the binding Moerdijk metadata-sentinel
ceiling — `C0/M0/m0`**

```text
SOURCE_CITATION_PREFLIGHT_COMPLETED=true
EFFECTIVE_FINDING_COUNTS=C0/M0/m0
RETAINED_UNVERIFIABLE_TECHNICAL_CLAIM_COUNT=0
MOERDIJK_FULLTEXT_AVAILABLE=false
MOERDIJK_METADATA_SENTINEL_CLOSED=true
MOERDIJK_TECHNICAL_CITATION_AUTHORIZED=false
EFFECTIVE_WORK_REGISTRY_COUNT=6
CURRENT_BIB_SEED_COUNT=5
MANUSCRIPT_WRITE_AUTHORIZED=false
BIBLIOGRAPHY_WRITE_AUTHORIZED=false
FIGURE_OR_TABLE_WRITE_AUTHORIZED=false
BUILD_OR_RELEASE_AUTHORIZED=false
GIT_OR_PUBLIC_SYNC_AUTHORIZED=false
NEXT_INDEPENDENT_EXACT_BYTE_GATE_RECOMMENDED=true
```

This audit does **not** authorize a manuscript, bibliography, visible
citation, figure, table, README, build, release, Route/control change, Git
mutation, or public sync. Its PASS means only that a bounded five-work
citation seed and a complete TN-00--TN-14 source/owner/ceiling matrix can be
presented to a fresh exact-byte gate. Any future Moerdijk technical use fails
closed until lawful exact full text, a PASS sidecar, and a claim-specific page
locator exist.

## 1. Method and ARS compliance

The ARS-Codex `academic-research-suite` root skill and the directly applicable
academic pipeline, citation-compliance, integrity-verification,
claim/reference-alignment, formatter, source-exclusion, and figure-trace
instructions were read in full before source acquisition. The controlling
rules applied here were:

1. source existence and correct metadata are separate from claim support;
2. a technical citation requires exact source bytes, an exact locator, and a
   faithful claim/source match;
3. manual local-PDF page anchors are usable only after the unmodified ARS
   PDF preflight returns PASS with no repair warnings;
4. discovery pages, snippets, abstracts, and metadata registries cannot
   substitute for full-text technical evidence;
5. one work with two manifestations remains one bibliographic work;
6. every retained source must have a substantive claim role or a closed
   sentinel role, and source ceilings must prevent ownership transfer; and
7. figure/table trace requirements do not authorize artifacts. No
   publication artifact was created in this lane.

Only primary/official technical sources were used: AMS/DOI metadata, the
official TAC article and PDF, the author arXiv record/PDF, and the official
EMS article/PDF. No review, aggregator, search snippet, or secondary
exposition is used as claim evidence.

## 2. Authorizing gate and frozen-input receipt

The current authorizing gate was read in full and freshly matched its supplied
identity: 839 lines, 42,099 bytes, SHA-256
`1a94c73043e01b7d5861a20357abdb26edf5f7115b47d0552ddab376f197e8f9`.
Its effective Section 12 state is PASS at `C0/M0/m0`, with this local-only
source/citation lane as the sole open write lane and every downstream write
false.

The proof, peer, source-domain, blueprint, amendment, and exact local-owner
records were also read and byte-checked:

| Frozen input | SHA-256 | Lines | Bytes |
|---|---|---:|---:|
| `notes/pre_manuscript_source_gate.md` | `1a94c73043e01b7d5861a20357abdb26edf5f7115b47d0552ddab376f197e8f9` | 839 | 42,099 |
| `notes/proof_audit.md` | `c6810e95d15e1ccf0f1dd48045b0f890ebd98fe637c20a9a5e153e10fa1c4934` | 310 | 20,874 |
| `notes/composition_blueprint.md` | `eac20a67f3638444add12f90ac5dede4c8b3f4ca1773a8afe5586e18d1bff10d` | 554 | 36,343 |
| `notes/composition_blueprint_amendment_v1.md` | `cfebb477128a3e1a99cb3f9fbedf3e3fce6709cc92d621f6909663f2fc25bddc` | 410 | 23,112 |
| `notes/composition_blueprint_amendment_v2.md` | `b95331e40c7c587568522497a73af09ba0d6d9cf0e9a7dac128c93114c8869b1` | 466 | 20,872 |
| `notes/phase2_topos_quantale_proofs.md` | `f6c7475b854b3d00b37d3e7f2edca8e8f2f15d92d67ae8bbcdcd71be127b3bb1` | 641 | 27,767 |
| `notes/phase2_topos_quantale_peer_review.md` | `9ad4817e32c6da461d7e15eee1bd53d24368b7c55751738c86c8b033caeb796e` | 389 | 21,760 |
| `notes/phase1_framework_source_precheck.md` | `9991dc5e27ea8577d4236d38feeb63bfc110e3a3b242b3c17be8607da01f9e64` | 657 | 25,610 |
| `notes/phase1_amendment_v2.md` | `2ce675880b171ee598f8a796edf55f9c695e2e6d0973620371d3ba460c7d1957` | 70 | 2,618 |
| P9 `paper/manuscript.tex` | `24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb` | 752 | 61,831 |
| P10 `paper/manuscript.tex` | `27bae88814f16263de444bb1650e4a550d0f0eca327f3c551d7c2097f353d315` | 602 | 61,214 |
| P11 `paper/manuscript.tex` | `eb1aa4d7060cf1aa53a729e7c7be89a5724a6133ef3bf000cb800bf786de1002` | 1,128 | 50,802 |

The following non-literature diagnostic records remain byte-bound through the
gate and blueprint. Their role is corroboration/receipt, never literature
proof:

| Diagnostic record | SHA-256 | Lines | Bytes |
|---|---|---:|---:|
| `notes/route_audit.md` | `d70ba9d029ae598863e44dbb049c49607063f682de8f7d8a8e5f2074ae531d15` | 211 | 13,035 |
| `notes/phase2_controls_review.md` | `a9acf3c1e6c043b408cce774af3adfdf4a72fdb2f58cf38fbc8bf94f6dc324a1` | 909 | 43,200 |
| `results/manifest.json` | `a15cc81ca8e41b7fd76560304bf713701f416a028558b9d9c5653b58f7ebc254` | 170 | 5,355 |
| `results/actual_standard_owner_controls.csv` | `00973eaf6eb2890ac452093704049f5e090ff134ccec268604df15d36a4bbd82` | 19 | 5,744 |
| `results/dilation_strict_marker_controls.csv` | `ae673db6b04f2c91af86688b957fc9fef629a5c307588c72278a2f4f5811b2eb` | 141 | 29,504 |
| `results/fixed_prime_provenance_controls.csv` | `168e5d57109745c0b4fd20270e7026dc1c7352e9367fef752310c740eac593f5` | 22 | 8,924 |

No frozen input was changed.

## 3. Acquired corpus and PDF read-integrity result

Three PDFs were lawfully acquired into the authorized local-only directory:
the official TAC Forssell article, the author arXiv v2 manifestation of the
same work, and the official EMS Protin--Resende article. The unmodified ARS
`pdf_read_preflight.py` had SHA-256
`b4239af423a18cce6c7473c880b8d125653c107919a31173a198b8dc8210827e`
(1,455 lines, 59,477 bytes) and generated all same-stem sidecars.

| PDF | Exact SHA-256 | Bytes | Page signals | Warning state | Result |
|---|---|---:|---|---|---|
| `forssell-2013-subgroupoids-tac.pdf` | `40372e8c70873d294ecd8ac20bd507b1571eed86c1576e435a0685bfc6023366` | 345,934 | `12/12/12` | `[]` | PASS |
| `forssell-2013-subgroupoids-arxiv-1111.2952v2.pdf` | `4a121f741bb7204ad7ce6a937599a17b051c673b62d55bc51d785087f3339774` | 180,244 | `14/14/14` | `[]` | PASS |
| `protin-resende-2012-quantales-ems.pdf` | `5a32faa1fea2cb07dc6794225f1ebe92b6a8bfbd5cae7d1c21d6df4b8a8d17ed` | 383,791 | `49/49/49` | `[]` | PASS |

The page signals are declared page-tree count, independent recursive
enumeration, and reader count. A non-authoritative `file(1)` heuristic first
printed “6 pages” for TAC and “10 pages” for EMS. This apparent mismatch was
not hidden: ARS returned the agreeing counts above with no warnings, and
`pdfinfo` independently reported 12 and 49 pages. The heuristic output is not
used for any locator.

The exact locator maps are:

- Forssell TAC: physical 2--3 = printed 542--543, Section 2.1; the final
  journal statement is Proposition 2.2. The twelfth physical page is a TAC
  colophon, so the 12-page file is consistent with article pages 541--551.
- Forssell arXiv v2: physical 2--3, Section 2.1; the corresponding statement is
  Proposition 2.1.1. The numbering difference is a real manifestation
  difference, not a citation error.
- Protin--Resende EMS: physical 5--7 = printed 203--205; physical 16--17 =
  printed 214--215 (Theorems 2.41 and 2.45); physical 47--48 = printed
  245--246.

The sidecars, acquisition endpoints, manifestation roles, and exact local
owner registry are frozen in
`notes/sources/paper17_source_manifest.md`.

## 4. Moerdijk exact-full-text fail-closed disposition

The work identity is real and unambiguous. DOI/Crossref metadata confirm Ieke
Moerdijk, the exact title, *Transactions of the AMS* 310(2) (1988), 629--668,
DOI `10.1090/S0002-9947-1988-0973173-9`. However, exact full text was not
lawfully obtainable in this workspace:

| Probe | Observed result |
|---|---|
| canonical AMS record `https://www.ams.org/tran/1988-310-02/S0002-9947-1988-0973173-9/` | HTTP 403 HTML access layer |
| canonical AMS PDF path | HTTP 403 HTML access layer |
| JSTOR stable item/PDF `2000984` | HTTP 200 but `text/html` access-gate bytes, not a PDF |
| author/institutional discovery paths checked | no lawful Paper-I full-text manifestation located |

No bypass was attempted. No HTML gate, secondary host, Paper II, similar-title
paper, search extraction, generated wrapper, or proxy PDF was retained. There
is therefore no Moerdijk sidecar, trusted page count, theorem/definition page,
or technical quotation.

This is a closed sentinel rather than a retained unverifiable claim. Blueprint
TN-03 assigns its equivalence to Paper 17's direct proof and permits
Moerdijk/Forssell only as framework sources; TN-02 already assigns the needed
open-groupoid/equivariant-sheaf framework to Forssell Section 2.1. The verified
Forssell full text therefore supplies the only external framework locator
needed by TN-02--TN-04, while Paper 17 keeps all proof credit. Moerdijk is
retained only to prevent identity drift. Any visible Moerdijk technical
citation remains a hard stop and would reopen a finding.

## 5. External-source claim faithfulness

### Forssell 2013

Printed pp. 542--543 / physical pp. 2--3 explicitly give the open topological
groupoid definition, the equivariant-sheaf setup, the fact that the resulting
category is a Grothendieck topos, and the beginning of the Moerdijk-site
description. This supports framework terminology only. It does not prove the
special action groupoid is open or establish Paper 17's special topos
equivalence.

The official TAC and arXiv v2 bytes agree on the relevant mathematical setup,
but the proposition numbering differs: TAC Proposition 2.2 versus arXiv v2
Proposition 2.1.1. Future citations must name the manifestation they use.

### Protin--Resende 2012

The official EMS bytes support the following bounded roles:

- printed pp. 203--205 distinguish the etale/unital setup from an open
  non-etale groupoid, for which the bare open-set quantale need not be unital;
- Theorem 2.41 at printed pp. 214--215 gives the associated quantale within
  the paper's localic quantal/open-groupoid framework;
- Theorem 2.45 at printed p. 215 states the reconstruction isomorphisms for a
  localic quantal groupoid and a multiplicative semi-open quantal frame; and
- printed pp. 245--246 warn that a sober topological open groupoid is not
  automatically the same as the corresponding localic object and identify
  local compactness of the arrow space as a sufficient condition for the
  displayed frame quotient to be an isomorphism.

The source does not identify bare `O(H)` alone with all reconstruction data;
does not erase the separate `q_H` and local-compactness premises; and does not
state that `Top -> Loc` loses the points of Paper 17's nonsober actual owner.
That point-loss location is Paper 17's typed inference and must be credited
only to its local direct proof.

The source and DOI metadata identify the first author as **M. Clarence
Protin**. The earlier source-gate feasibility paragraph's “Laurent Protin” is
an upstream metadata typo; this authorized manifest/audit corrects it before
any bibliography exists. No unresolved citation record retains the wrong
name.

## 6. TN-00--TN-14 claim-to-source/owner/locator/ceiling matrix

Every claim row below names the direct owner first. External literature is
framework evidence only where expressly shown. “Pass” means the claim has a
verifiable owner/locator and a closed ceiling; it does not authorize drafting.

| Claim and bounded claim text | Direct owner and exact locator | External/local cited source locator | Binding ceiling | Result |
|---|---|---|---|---|
| **TN-00.** The work remains a non-standalone Technical Note with `STANDALONE_PASS=false`. | `proof_audit.md` Sections 1 and 10; `route_audit.md` lines 1--7 and 187--211. | None required. | No literature citation can confer Route or standalone credit. | pass |
| **TN-01.** The range-first action-groupoid convention and operations are frozen. | `phase2_topos_quantale_proofs.md` (2.1)--(2.2), lines 55--91. | P11 lines 255--277. | P11 owns only the formulas/convention; no proxy convention or topology transfer. | pass |
| **TN-02.** `G(X,H)` is open, while the usual-`R` specialization is non-etale. | Paper-17 proof Propositions 3.1--3.3, lines 93--155; peer review lines 86--103. | Forssell TAC Section 2.1, printed p. 542 / physical p. 2; arXiv v2 physical p. 2. | Forssell supplies the definition/framework, not Paper 17's openness or non-etaleness proof. | pass |
| **TN-03.** `B(G(X,H)) ~= B_cont(H)` for a nonempty globally indiscrete right `H`-set. | Paper-17 Lemma 4.1 and Theorem 4.2, equations (4.1)--(4.6), lines 157--244; peer review lines 105--147. | Forssell TAC printed pp. 542--543 / physical pp. 2--3. Moerdijk is sentinel-only and unused. | The equivalence is Paper 17's direct proof; no etale bridge and no Moerdijk technical locator. | pass |
| **TN-04.** Connected usual `R` gives `Set`; discrete `Z` gives nontrivial `BZ`. | Paper-17 Corollaries 4.3--4.4, lines 246--273; the exact `Z` Route control remains a falsifier. | Forssell framework only if terminology needs it; no separate source required for the calculation. | `Z` is a disconnected falsifier, not finite-C3 evidence or external-theorem credit. | pass |
| **TN-05.** The bare arrow-open quantale is `O(H)`, the base is `2`, and usual-`R` bare `O(H)` is nonunital. | Paper-17 Theorem 5.1 and Propositions 5.2--5.3, lines 275--340; peer review lines 161--178. | Protin--Resende printed pp. 203--205 / physical pp. 5--7 and Theorem 2.41 at printed pp. 214--215 / physical pp. 16--17. | External source supplies notation/domain distinctions only; the displayed calculation is Paper 17's proof and is not reconstruction. | pass |
| **TN-06.** Bare `O(H)`, `q_H`, and local compactness are separate; reconstruction uses their registered conjunction. | `phase1_amendment_v2.md` Sections 1--2; Paper-17 Proposition 6.1 and Theorem 6.2, lines 342--386; peer review lines 180--200. | Protin--Resende Theorems 2.41/2.45, printed pp. 214--215 / physical pp. 16--17, plus printed pp. 245--246 / physical pp. 47--48. | No bare-quantale reconstruction, no dropped `q_H`, and no domain enlargement beyond the frozen locally compact setting. | pass |
| **TN-07.** Nonsober point loss occurs at `Top -> Loc`, not as failure of localic reconstruction. | Paper-17 Corollary 6.3, lines 388--403; peer review lines 180--200. | Protin--Resende only for Theorem 2.45's actual localic domain and the printed pp. 245--246 warning. | Point loss is Paper 17's typed inference and may not be attributed to the source theorem. | pass |
| **TN-08.** Actual `Set/O(R)/2` and standard `BZ/O(S_L x R)/O(S_L)` remain different owners. | Paper-17 Theorem 7.1, Proposition 7.2, and Section 8, lines 405--506; owner control is corroboration only. | P11 lines 313--324 for the standard-circle owner. | No topology, coordinate, quantale, or topos transport across actual and standard owners. | pass |
| **TN-09.** Unequal-period simultaneous dilation preserves unmarked plain interfaces; strict time is additional marker structure. | Paper-17 Propositions 9.1--9.2, lines 508--556. | No literature citation required; `dilation_strict_marker_controls.csv` is corroboration only. | The control is not theorem proof; unmarked nonrecovery is not a global impossibility theorem. | pass |
| **TN-10.** Fixed-prime substitution follows the generic theorem and imports only actual indiscreteness and literal `(log p)Z`. | Paper-17 Section 10, lines 558--592. | P9 lines 409--426. | P9 supplies actual packet/orbit indiscreteness and literal set stabilizer only; no ordinary-circle topology or new Paper-17 result. | pass |
| **TN-11.** Prior P10 collapses and P11 formulas are subtracted rather than relabeled as new topos results. | Paper-17 owner-firewall table, lines 593--613. | P10 ledger lines 132--135 and P10-1--P10-4 blocks/scope stops lines 201--306; P11 lines 255--277, 313--324, 337--405, 1079--1087. | P10 is **TN-11 only**, “builds on”/prior subtraction only; no P10-5, operator, proxy, measure selection, trace, determinant, Route, or Paper-17 theorem. P11 has the formula/owner ceiling in the manifest. | pass |
| **TN-12.** The frozen finite diagnostic package has the registered exact counts. | `phase2_controls_review.md` lines 575--909 and `results/manifest.json` lines 1--170, bound above. | None. | Diagnostic/serialization evidence only, never theorem proof or literature evidence. | pass |
| **TN-13.** Seven owners yield four exploratory and three rejected Route-A dispositions; all A2--A4 fail; Route B is false. | `route_audit.md` lines 106--211 and the seven gate-bound Stage-17 YAMLs. | None. | Copy exact enums/counts only; no aggregation, owner transfer, or interpretive promotion. | pass |
| **TN-14.** No listed analytic/spectral/determinant/transfer structure is constructed in the evaluated interface. | Paper-17 proof lines 558--641; `proof_audit.md` Sections 5, 8, and 9; `route_audit.md` lines 118--130 and 148--211. | None. | Scoped absence/limitation only, not impossibility for every enrichment or future owner. | pass |

```text
TN_MATRIX_ROWS=15
TN_MATRIX_PASS=15
TN_MATRIX_FAIL=0
RETAINED_UNVERIFIABLE_TECHNICAL_CLAIMS=NONE
```

## 7. Bibliography-seed and orphan-source audit

The effective registry contains six works, but the currently usable
bibliography seed contains **five**:

1. Forssell 2013 — one work, despite two retained manifestations;
2. Protin--Resende 2012;
3. local owner P9;
4. local owner P10; and
5. local owner P11.

Moerdijk is not a sixth current seed because technical use cannot pass exact
full-text/locator alignment. It may become a sixth seed only after a new
authorized acquisition and exact-byte audit. The arXiv Forssell PDF is a
version check, not a second work or sixth seed.

Every one of the five seeds has a substantive matrix role: Forssell
TN-02--TN-04; Protin--Resende TN-05--TN-07; P9 TN-10; P10 TN-11 only; and P11
TN-01/TN-08/TN-11. There is no convenience source, unused bibliography item,
or separate arXiv duplicate. This audit creates no BibTeX file and does not
require that every framework citation be repeated at every claim.

## 8. Source-exclusion and ownership firewall

The following boundaries are closed and mandatory for the next gate:

- no Moerdijk technical claim, page locator, direct quotation, or bibliography
  entry while the work is metadata-only;
- no Paper II, repository wrapper, search snippet, abstract, or unrelated PDF
  as a Moerdijk Paper-I surrogate;
- no duplicate Forssell TAC/arXiv bibliography entries and no
  manifestation-number mixing;
- no citation of Forssell for Paper 17's direct openness/topos calculations;
- no citation of Protin--Resende for the Paper-17 `Top -> Loc` point-loss
  inference, and no collapse of bare `O(H)`, `q_H`, and local compactness;
- no etale-only quantale/sheaf source imported into the non-etale theorem;
- no P9 standard-topology transfer;
- no P10 use outside TN-11's exact “builds on”/prior-subtraction ceiling;
- no P11 actual/standard owner splice;
- no control, Route row, source manifest, or preflight sidecar cited as a
  mathematical theorem; and
- no source or bibliography entry without a mapped claim need.

The PDFs remain local-only under `notes/sources/.gitignore`; source
availability does not imply redistribution authorization.

## 9. Closed observations and effective finding ledger

| Item | Disposition |
|---|---|
| Moerdijk exact full text unavailable | Closed as metadata-only sentinel; zero technical claim or current bibliography use retained. |
| TAC/arXiv Forssell numbering differs | Closed by manifestation-specific locators: TAC Proposition 2.2; arXiv v2 Proposition 2.1.1. |
| `file(1)` reported misleading PDF page heuristics | Closed transparently by ARS PASS three-signal agreement and independent `pdfinfo` counts. |
| Upstream “Laurent Protin” typo | Closed in the authorized manifest/audit as M. Clarence Protin, verified from the official PDF/DOI metadata before any bibliography exists. |

No item leaves a claim unsupported or a citation ambiguous.

| Severity | Open count |
|---|---:|
| Critical | 0 |
| Major | 0 |
| Minor | 0 |

Effective verdict: **PASS, `C0/M0/m0`, under the binding source-exclusion
ceilings above.**

## 10. Output freeze and checksum closure

The source checksum ledger was verified with `sha256sum -c`: all six entries
returned `OK`. PDF `Lines` below are raw LF-byte counts, not page anchors.

| Authorized output | SHA-256 | Lines | Bytes |
|---|---|---:|---:|
| `notes/sources/.gitignore` | `7aa3d6fc8be69e3c04723aa32c945aeabfddd262829ea29577a04da12681d5ab` | 2 | 87 |
| `notes/sources/forssell-2013-subgroupoids-tac.pdf` | `40372e8c70873d294ecd8ac20bd507b1571eed86c1576e435a0685bfc6023366` | 2,671 raw LF | 345,934 |
| `notes/sources/forssell-2013-subgroupoids-tac.preflight.json` | `06273f1a752fc8fd62673225d96096f20cbc6a0dc940ae6222cbeccfde17376f` | 12 | 434 |
| `notes/sources/forssell-2013-subgroupoids-arxiv-1111.2952v2.pdf` | `4a121f741bb7204ad7ce6a937599a17b051c673b62d55bc51d785087f3339774` | 3,178 raw LF | 180,244 |
| `notes/sources/forssell-2013-subgroupoids-arxiv-1111.2952v2.preflight.json` | `20083976ca71cc4e33ed0ad1a84c1206cbcb01b809c8e4c257f445d4dbb15bac` | 12 | 448 |
| `notes/sources/protin-resende-2012-quantales-ems.pdf` | `5a32faa1fea2cb07dc6794225f1ebe92b6a8bfbd5cae7d1c21d6df4b8a8d17ed` | 3,470 raw LF | 383,791 |
| `notes/sources/protin-resende-2012-quantales-ems.preflight.json` | `7cf17089919d761096a26dc4ffdb97b893aa98522774ab51c3024a529cb7f00e` | 12 | 437 |
| `notes/sources/paper17_sources.sha256` | `2381d5e5445da18f38caa026d3c2e4dfe6026ef944c21a6e32917ded9d6e699d` | 6 | 673 |
| `notes/sources/paper17_source_manifest.md` | `d1d13d9d9193512775db9e4e2bd2dd555e8bfaaef8ae9bce2e7a378b00cef6e9` | 163 | 10,010 |
| `notes/pre_manuscript_citation_audit.md` | `EXTERNAL_BY_CONSTRUCTION` | `EXTERNAL_BY_CONSTRUCTION` | `EXTERNAL_BY_CONSTRUCTION` |

The checksum ledger intentionally covers only exact PDFs and sidecars. It does
not self-hash and does not hash the manifest, `.gitignore`, or this audit.
This audit's final SHA/line/byte identity must be supplied by the external
handoff after the file is closed.

## 11. Recommended next exact-byte gate

A fresh independent gate may re-hash this audit, the manifest, ledger,
`.gitignore`, all three PDFs/sidecars, and P9/P10/P11, then decide whether a
separately authorized composition/bibliography lane may open. That gate should
require all of the following before any write:

1. `C0/M0/m0` remains exact after re-read;
2. current bibliography seeds remain exactly five unless a new claim/source
   amendment is independently authorized;
3. Moerdijk remains absent from visible technical citations and bibliography;
4. Forssell manifestations remain one work and use manifestation-correct
   locators;
5. Protin--Resende is never credited with Paper 17's point-loss inference;
6. the P10 TN-11-only negative ceiling is reproduced verbatim in effect;
7. every manuscript claim/citation pair maps back to one matrix row and no
   source is orphaned; and
8. no downstream permission is inferred from this audit.

If later lawful Moerdijk Paper-I full text becomes available, it requires a
new local PDF, an unmodified-ARS PASS sidecar, an exact definition/theorem page
locator, a claim-faithfulness check, and a fresh independent gate before it can
alter the five-seed state.

```text
NEXT_EXACT_BYTE_GATE_RECOMMENDED=true
NEXT_GATE_AUTHORIZED_BY_THIS_AUDIT=false
MANUSCRIPT_AUTHORIZED_BY_THIS_AUDIT=false
BIBLIOGRAPHY_AUTHORIZED_BY_THIS_AUDIT=false
ALL_DOWNSTREAM_PERMISSIONS=false
THIS_FILE_FULL_SHA256=EXTERNAL_BY_CONSTRUCTION
```

