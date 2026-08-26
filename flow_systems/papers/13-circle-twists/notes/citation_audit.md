# Paper 13 final citation and source-integrity audit

Frozen: **2026-08-15 (Asia/Shanghai)**  
Mode: **independent ARS final citation, integrity, claim-alignment,
formatter, PDF/visual, originality, and source-exclusion audit**  
Candidate: **Technical Note: Gauge-Trivial Circle Twists and
Constant-Diagonal Corona Records for Indiscrete Real Actions**  
Verdict: **PASS — REVIEW FREEZE 2 EXACT LOCK; C0/M0/m0, with explicit
external-release conditions**

This is a post-manuscript audit. The candidate manuscript, bibliography,
figures, retained PDF, package README, project README, proofs, controls,
Route records, source files, and locks were read-only. The reserved control
lane was not rerun, and no Git or public synchronization operation was
performed. Temporary build, text, and raster outputs were confined to
`/tmp`. The only workspace artifact created by this audit is this report.

## 1. Exact candidate and evidence lock

### 1.1 REVIEW FREEZE 2 candidate

Every supplied candidate hash was independently recomputed before the audit
write and matched exactly.

| Artifact | Bytes | SHA-256 | Result |
|---|---:|---|---|
| `paper/README.md` | 20,956 | `499a4618a0bab9e0a266ca81382a0a084b5016dda45ac0553224171dd4682502` | exact; full package receipt and six-key trace read |
| `paper/manuscript.tex` | 54,338 | `c8c9b7522e9bf63a30ed199fe3468d642cb3e572e324680ccd6893857fbe9701` | exact; full source read |
| `paper/references.bib` | 5,834 | `661aa0a948e8a06538cb300106e91bc9d72e91bf26e9515fdb9a074d0f394292` | exact; all 17 records read |
| `paper/figures/owner_support_firewall.tex` | 3,217 | `130ad2f1833a91970629311e1cf21bc848d826afcda941e9b0ad3367cb8f2360` | exact; native TikZ read and rendered |
| `paper/figures/generic_constant_diagonal.tex` | 2,820 | `727160835b9190b8d3a854825ea30735e4f59813be50a6f7960f3da735558d44` | exact; native TikZ read and rendered |
| `paper/paper.pdf` | 183,120 | `4082ca13a6daadb72ccc30a34fc5160f5920247d3fa3436562349ccc5a9c43c2` | exact; 15-page A4 retained review PDF |
| project `README.md` | 3,511 | `729d2de14046f3004fdcd231a4d0d287e62c9b6e1af95cb592a5918df071120d` | exact; current Technical Note / NOTE-branch entry point |

REVIEW FREEZE 1 is not the candidate audited here. Its tuple and the round-1
peer report remain historical provenance only.

### 1.2 Binding Paper 13 inputs

| Evidence artifact | SHA-256 | Binding role |
|---|---|---|
| `notes/composition_blueprint.md` | `af7b20a7e1091a876acfa4c22a9f8ba0e9c19b3accd1fe1c1376f6c13fcc48fd` | composition, owner, Technical Note, bibliography, and trace contract |
| `notes/proof_audit.md` | `e2f8fb8df4f3418fb3ff0fb60c87f9c7a4ae26cc7470c8c14aec3f86f6df1a63` | integrated proof and owner audit |
| `notes/pre_manuscript_citation_audit.md` | `3ed75cf27d63c84629e02d3b402de8d3e9f419923f9fec43e60fb0b319b5dd73` | 17-record seed, manifestations, locators, and claim ceilings |
| `notes/phase3_v2_note_disposition_gate.md` | `b60c88a33bb3bb5c4f87448aaaf8f2d4020fa945bc9f204fd81d07ea85d7d03e` | `PASS_TO_TECHNICAL_NOTE` and release hold |
| `notes/phase3_v2_standalone_review.md` | `ee31c644f9569abecae91ce0ca1054ad480485670caf41cf289a8e3f5ccb0c0e` | binding `NOTE_OR_MERGE`; standalone Major retained |
| `notes/phase3_v2_controls_review.md` | `c89a503f0cd624f4a9f119e12fedd0a2c7d6a5b2d55613a1a0e42f3e19917789` | stable replacement-control receipt and diagnostic ceiling |
| `notes/route_audit.md` | `2603502519e087a5023be2fec91e8b332a37d93a1368300a8e103680d6c5b0b9` | exact ten-owner Route adjudication |
| `notes/peer_review_round1.md` | `abca2855cb223390341f44962559c6a82ff1daf21ae84da0a822e7f6c1c52071` | historical Freeze-1 report and bounded repair authority |

The principal hashes are mutually consistent. The NOTE disposition is not a
waiver: it is the precise publication class authorized by the upstream gate.

### 1.3 Corrected Paper 12 identity and historical-receipt boundary

Paper 12 received an append-only bibliographic correction after the Paper 13
upstream audits were frozen. The current available corrected identity was
recomputed as follows:

| Paper 12 artifact | Current SHA-256 | Status relevant to Paper 13 |
|---|---|---|
| project `README.md` | `3f30055125e5f6593b4f8806c75ab3349675112e574f69e7238d9f7bd2ef9428` | corrected receipt |
| `paper/README.md` | `18eea91a1ed775cc03a14614af4662e3967be3aec66dd6bd58fc09819932db25` | corrected receipt |
| `paper/manuscript.tex` | `c6ad0f8c22d68840198d744a615da06e8b062d5ccdbeedb7f4ee76bf35073163` | unchanged; cited theorem source |
| `notes/proof_audit.md` | `c2b0fc4ce4764b476de8623c7a1b37e33d51da4a1c318c133313956abf4af6ab` | unchanged; owner firewall |
| `paper/references.bib` | `b763e9c07e3265d878bfc8b4caf44fb6c92ef12e7fac59b8af0bdeb703876175` | corrected Stacks title |
| `paper/figures/same_carrier_diagonal.tex` | `a83148600d497dd1b91510f5707a1b1a9402c35689013a1fa904978206ff5cf1` | unchanged |
| `paper/figures/packet_four_way_firewall.tex` | `9a52c273e91878d4dd74f96bd27fe299be39d98cdbebdda6bc800d89184b6908` | unchanged |
| `paper/paper.pdf` | `9d6747e9f33c6ab3724beb35daedbb0efaff73691ed344374366f2392541ec15` | corrected rendered reference |
| `notes/citation_audit.md` | `79089b2487b6b21c10c1f10a4918fb29602d265877483d7a325634d15ec70a3a` | append-only correction relock |

The older Paper 12 PDF and bibliography hashes recorded in the immutable
Paper 13 pre-manuscript audit are historical receipts, not assertions of the
current Paper 12 release identity. This does not weaken a Paper 13 imported
claim: the Paper 12 manuscript, proof audit, theorem labels, and Section 8
variance source are byte-identical. Moreover, the Paper 13 preaudit and
Paper 13 bibliography already use the correct Stacks Tag `0B1W` title,
“Colimits of spaces.” Paper 12's peer/release receipts still require their
coordinated relock before a public batch release; that is an external-release
condition, not a Paper 13 citation defect.

## 2. Acceptance standard, severity, and disposition

The audit applied the ARS final-integrity standard:

1. inspect every bibliography record and every citation command;
2. verify exact source identity, manifestation, locator, and claim ceiling;
3. enforce owner, topology, category, variance, and theorem-strength limits;
4. rebind the five local companion identities and their imported premises;
5. check strict six-key artifact traces in both directions;
6. run a clean documented build and compare retained/fresh text and rasters;
7. inspect PDF metadata, fonts, attachments, every page, and both figures;
8. conduct a bounded originality screen; and
9. clear the seven specified AI-research failure modes.

Severity meanings are: **Critical** for a defect invalidating the core or
source integrity; **Major** for a blocking exact-lock defect; and **Minor**
for a local error not changing the result. The final open-finding ledger is:

```text
critical 0; major 0; minor 0; retained unverifiable claim 0
```

The separate standalone review's `C0/M1/m0`, `NOTE_OR_MERGE`, and
`STANDALONE_PASS=false` remain binding. They are classification facts, not
findings against a candidate that openly and consistently presents itself as
a Technical Note on the NOTE branch.

### 2.1 Closure of the Freeze-1 peer findings

| Historical finding | Freeze-2 closure |
|---|---|
| M1: six traces lacked claim text, exact source/transformation detail, and forward links | closed: all six entries now bind exact source paths/hashes, reproducible manual transformations, claim text plus locators, manuscript labels, explicit artifact IDs, and reverse links |
| M2: project README was an obsolete Phase-1 stub | closed: the project entry point now gives the exact title, Technical Note / NOTE disposition, result ceiling, candidate tuple, and `RELEASE_AUTHORIZED=false` |
| m1: Chinese abstract receipt said 433 Han characters | closed: the package receipt reproducibly records 409 prose-body Han characters and 26 keyword-value Han characters, or 435 under the separately named combined count |

The round-1 non-counted clarity suggestion concerning “second partial
derivative” does not alter the displayed construction or its use of
`partial_2`; it is not a citation or integrity finding.

## 3. Independent build, text, PDF, and visual verification

### 3.1 Documented and independent builds

The documented Freeze-2 build at `/tmp/p13-freeze2-final.ZK0vNp` remains
available. Its `manuscript.pdf` is byte-identical to the retained PDF:

```text
4082ca13a6daadb72ccc30a34fc5160f5920247d3fa3436562349ccc5a9c43c2
```

An independent clean source copy was built at
`/tmp/p13-citation-freeze2.cpa6x7` with the exact sequence:

```text
XeLaTeX -> BibTeX -> XeLaTeX -> XeLaTeX -> XeLaTeX
```

All five commands returned zero. Source, bibliography, and figure hashes in
the temporary build equal the Freeze-2 tuple. The fresh PDF is 183,123 bytes
with SHA-256
`f00a15a2cce2a56c104f683c19328c1017229eee9186fab470bb345d8a3cb0d7`.
Its binary differs from the retained 183,120-byte PDF only at ordinary
build-dependent PDF serialization/metadata level; semantic and rendered
identity were checked directly:

| Check | Result |
|---|---|
| retained/fresh `pdftotext -layout` | byte-identical; SHA-256 `fe95efd4cb38f2dde1b45a8d92df686f74379261aaf23d032e3db2f1e0b76a6a` |
| retained/fresh 144-DPI page renders | all 15 PNG pairs byte-identical |
| final LaTeX log | no unresolved citation/reference, rerun request, actionable warning/error, overfull/underfull box, or missing character |
| BibTeX | `warning$ -- 0` |
| labels and cross-references | 26 unique labels; 23 unique cross-reference targets; zero duplicate or missing target |
| extracted layout text | 7,391 whitespace tokens; zero U+FFFD; zero `??` sentinel |

The transient first-pass warnings and box messages clear in the stabilized
five-command build and are not present in the final log.

### 3.2 PDF hygiene and complete visual review

The retained PDF is unencrypted PDF 1.5 with 15 unrotated A4 pages. Title,
subject, keywords, and `AUTHOR TO CONFIRM` author metadata agree with the
source. `pdfinfo` reports no custom metadata, metadata stream, suspect flag,
form, or JavaScript. Ghostscript parses every page successfully.

All eight used font faces are embedded, subsetted, and Unicode mapped:
TeX Gyre Termes regular/bold/italic, TeX Gyre Termes Math, TeX Gyre Cursor
regular/italic, and Noto Serif CJK regular/bold. `pdfimages -list` reports no
raster image objects; `pdfdetach -list` reports zero embedded files; and
`pdfsig` reports no signature. Binary-string and extracted-text screens found
no absolute workspace path, source-PDF basename, source `.tex`/`.bib`
filename, preflight filename, or 64-hex internal hash in the PDF.

Every retained page was inspected at rendered detail. There is no clipping,
collision, illegible equation, missing glyph, bad float, blank artifact, or
anomalous whitespace. Tables 1--4 and the bibliography are readable. Figure
1 on page 5 and Figure 2 on page 11 were additionally rendered at 360 DPI and
viewed at original detail. Their arrow directions, branches, labels,
firewalls, and captions are legible and agree with the surrounding claims.
Because all retained/fresh page rasters are byte-identical, the complete
visual review also covers the independent fresh rendering.

### 3.3 Bilingual abstract ledger

The English abstract has 215 prose words: `detex` gives 217 tokens when its
two environment-name sentinels are retained, and 215 after those sentinels
are excluded. The independently composed Simplified Chinese prose body has
409 Unicode `Script=Han` characters. The six Chinese keyword values add 26;
the separately named body-plus-keyword-values count is 435. These values are
inside the required ranges.

The twelve ordered facts match in both languages: Technical Note and
non-standalone status; prior real-line/standard mechanisms; ownership by
Papers 2, 8, 9, 11, and 12; frozen signs; separate test/maximal/reduced
records; exactly four tag-forgotten outputs; support split; selected
component isometries; generic-after-isometries diagonal lemma; nonselective
fixed-prime cases; finite controls as diagnostics; and no topology/global
completion/trace/determinant/spectral promotion. Neither abstract contains
a citation, hash, control total, Route code, or author placeholder.

## 4. Citation graph and bibliography closure

A source parser and the stabilized build give the same closed graph:

| Quantity | Count |
|---|---:|
| citation commands | 18 |
| key occurrences | 19 |
| unique cited keys | 17 |
| bibliography records | 17 |
| missing citation keys | 0 |
| orphan bibliography records | 0 |
| duplicate DOI strings | 0 |
| placeholder identifiers | 0 |

`Sorkin1978Triviality` and `Austad2021Spectral` occur twice; each other key
occurs once. All 18 citation-bearing contexts were read in their surrounding
paragraphs.

The bibliography contains twelve external records and five exact local
companion records. The companion share is 5/17, or 29.4%, which triggers the
advisory internal-citation review. It is nevertheless justified here: all
five are load-bearing premises with distinct owners; every one is labelled
as an unpublished companion manuscript; Table 1 subtracts them before the
residual contribution; and the Technical Note explicitly retains
`STANDALONE_PASS=false`. None is decorative padding.

The Stacks record adds `year = {n.d.}` to the mechanically consumable seed.
That is a permitted formatting field, not an invented numeric publication
date or an identity change; the preaudit expressly permits venue-formatting
changes while freezing identity, version, date, DOI, status, and URL facts.

## 5. External-source metadata and canonical records

Metadata were verified against official publisher, society, project, DOI,
or author manifestations current on 2026-08-15. The bibliography values and
the official records agree subject to the qualifications stated below.

| Key | Exact verified identity | Canonical official/primary record | Qualification |
|---|---|---|---|
| `Sorkin1978Triviality` | Rafael Sorkin, “The triviality of continuous multipliers for the real line,” *International Journal of Theoretical Physics* 17(5), 369--376 (1978), DOI `10.1007/BF00674107` | [Springer article](https://link.springer.com/article/10.1007/BF00674107) | author is Rafael Sorkin, without an imported middle initial; audited use is official abstract only |
| `Austad2021Spectral` | Are Austad, “Spectral Invariance of *-Representations of Twisted Convolution Algebras with Applications in Gabor Analysis,” *Journal of Fourier Analysis and Applications* 27(3), Article 56 (2021), DOI `10.1007/s00041-021-09860-z` | [Springer article](https://link.springer.com/article/10.1007/s00041-021-09860-z) | Article 56 is an article number, not a page range |
| `Leptin1968Darstellungen` | H. Leptin, “Darstellungen verallgemeinerter L1-Algebren,” *Inventiones Mathematicae* 5(3), 192--215 (1968), DOI `10.1007/BF01425550` | [Springer article](https://link.springer.com/article/10.1007/BF01425550) | printed locator is Satz 6 on p. 204 |
| `Hulanicki1964WeakContainment` | A. Hulanicki, “Groups whose regular representation weakly contains all unitary representations,” *Studia Mathematica* 24(1), official registry 27--59 (1964), DOI `10.4064/sm-24-1-27-59` | [IMPAN article record](https://www.impan.pl/pl/wydawnictwa/czasopisma-i-serie-wydawnicze/studia-mathematica/all/24/1/95703/groups-whose-regular-representation-weakly-contains-all-unitary-representations); [DOI](https://doi.org/10.4064/sm-24-1-27-59) | official scan visibly begins at printed p. 37; registry pagination 27--59 is correctly retained and the anomaly is disclosed |
| `Hulanicki1966Folner` | A. Hulanicki, “Means and Fölner condition on locally compact groups,” *Studia Mathematica* 27(2), 87--104 (1966), DOI `10.4064/sm-27-2-87-104` | [IMPAN article record](https://www.impan.pl/en/publishing-house/journals-and-series/studia-mathematica/all/27/2/96164/means-and-folner-condition-on-locally-compact-groups); [DOI](https://doi.org/10.4064/sm-27-2-87-104) | no issue/page discrepancy found |
| `Kleppner1965Multipliers` | Adam Kleppner, “Multipliers on Abelian groups,” *Mathematische Annalen* 158(1), 11--34 (1965), DOI `10.1007/BF01370393` | [Springer article](https://link.springer.com/article/10.1007/BF01370393) | used only for Section 7 Borel terminology |
| `PackerRaeburn1989Twisted` | Judith A. Packer and Iain Raeburn, “Twisted crossed products of C*-algebras,” *Mathematical Proceedings of the Cambridge Philosophical Society* 106(2), 293--311 (1989), DOI `10.1017/S0305004100078129` | [Cambridge article](https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/twisted-crossed-products-of-calgebras/79B8947245C46351F7F003D7F3BFBC39); [DOI](https://doi.org/10.1017/S0305004100078129) | Cambridge's later online-publication date is digitization metadata, not the issue year |
| `BussHolkarMeyer2018Universal` | Alcides Buss, Rohit D. Holkar, and Ralf Meyer, “A universal property for groupoid C*-algebras. I,” *Proceedings of the London Mathematical Society* (3) 117(2), 345--375 (2018), DOI `10.1112/plms.12131` | [Wiley/LMS article](https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/plms.12131); [arXiv 1612.04963v2](https://arxiv.org/abs/1612.04963v2) | technical locators use final accepted arXiv v2, revised 7 February 2018 |
| `Williams2007CrossedProducts` | Dana P. Williams, *Crossed Products of C*-Algebras*, Mathematical Surveys and Monographs 134, AMS, Providence (2007), ISBN `978-0-8218-4242-3`, DOI `10.1090/surv/134` | [AMS book record](https://bookstore.ams.org/view?ProductCode=SURV%2F134); [author manuscript v3.1](https://math.dartmouth.edu/~dana/cpcsa/draft3.1.pdf) | publication identity is 2007; technical locators use the author's 6 September 2006 draft 3.1 |
| `AustadOrtega2022Uniqueness` | Are Austad and Eduard Ortega, “C*-uniqueness Results for Groupoids,” *International Mathematics Research Notices* 2022(4), 3057--3073 (2022), DOI `10.1093/imrn/rnaa225` | [Oxford article](https://academic.oup.com/imrn/article/2022/4/3057/5901311); [arXiv 2005.06208v1](https://arxiv.org/abs/2005.06208v1) | online publication in 2020 does not replace the 2022 issue year; locators use v1, 13 May 2020 |
| `Tu2004NonHausdorff` | Jean-Louis Tu, “Non-Hausdorff groupoids, proper actions and K-theory,” *Documenta Mathematica* 9, 565--597 (2004), DOI `10.4171/DM/178` | [EMS article](https://ems.press/journals/dm/articles/8965109) | no issue number is manufactured |
| `Stacks0B1W` | The Stacks Project Authors, Section 5.29, Tag `0B1W`, “Colimits of spaces,” no fixed numeric year | [stable official tag](https://stacks.math.columbia.edu/tag/0B1W) | `n.d.` plus access date is honest; no DOI, journal, volume, issue, or pages are invented |

No metadata discrepancy changes a cited claim. The two date distinctions,
the Hulanicki scan anomaly, article-number status, draft/version locators,
and abstract-only Sorkin ceiling are all visible rather than silently
normalized away.

## 6. Manifestations, locators, and claim ceilings

### 6.1 Retained research manifestations

The Paper 13 `framework_sources.sha256` ledger revalidated all six PDFs and
six sidecars: 12/12 `OK`. The inherited Paper 11 framework ledger revalidated
all five PDFs and five sidecars: 10/10 `OK`. No source was downloaded or
added during this audit.

Nine cited technical manifestations were inspected through preflight
sidecars and exact bytes. Every sidecar has schema `pdf_read_preflight/1`,
verdict `PASS`, equal declared/enumerated/reader page counts, and an empty
warnings array.

| Manifestation | PDF SHA-256 | Pages | Principal locator read |
|---|---|---:|---|
| Austad--Ortega arXiv v1 | `c4b7b1cb7e225e3873b1071deb844b047ba0f1404aac4ca97002862aec2682c7` | 13 | pp. 1, 3 |
| Austad 2021 | `9edaf338a3d1f2f1b503a3709f20fceaa2bf1a6624a8d6fce0d80f3f15c77bc3` | 22 | formulas pp. 5--6; Proposition 2.4, printed p. 7 |
| Hulanicki 1966 | `eacf80abfbd7dc7320b4130ff2a2028d98cbd89b48bcf8ee62562d3e79f64f4a` | 10 | printed pp. 87--88 |
| Hulanicki 1964 | `a30bcf1bda9699b56f1a846f15bc46f0ce420fb42f114fdc22d564d0a6f321fa` | 12 | visible printed pp. 56--58; scan starts at 37 |
| Kleppner 1965 issue scan | `75f9f5e62e47e8c9dc885a5eba74ccbdfaefa296c02b1fcc5de8fbcf9dd51264` | 73 | Section 7, article printed p. 28 |
| Leptin 1968 | `0bde30eba4eb8cee42bed5285e32272994090d04fc8880f841799ed75c96039c` | 25 | Satz 6, printed p. 204 |
| Buss--Holkar--Meyer arXiv v2 | `8be7896ed1aab1138b8ccf067ebfbba0f8b7d8a1dc8713fbf6c2f173ffe647e6` | 30 | Corollary 6.2 p. 21; Theorem 7.1 p. 23 |
| Tu 2004 | `ff88e322eee65d2d6dd083697c82febb3759268f9b36083264a3e20b6e586897` | 34 | Definition 1.1, printed p. 567; Definition 4.6, printed p. 583 |
| Williams draft 3.1 | `3dbc1fb9e96191a278e0d59feb4981d3bbea4faa4df609d1886c81125bffe9c2` | 540 | Lemma 2.27 and Remarks 2.29--2.30 pp. 52--55; Theorem 4.30 p. 138; Definitions/Theorem 7.7/7.13 pp. 198--199 |

There is no Sorkin full-text PDF in the audited corpus; only the official
Springer title and abstract are used. Packer--Raeburn is used only at
publisher/title background level, with no imported theorem locator. Stacks
is a live official web source. Those manifestation limits are correctly
disclosed and are not papered over by secondary summaries.

### 6.2 Claim-to-source alignment

| Source | Licensed use in the manuscript | Enforced ceiling | Result |
|---|---|---|---|
| Sorkin | existence-level prior credit for continuous real-line remultiplication | no imported normalization, sign, proof step, or actual-owner transfer | PASS |
| Packer--Raeburn | standard twisted/crossed-product background | no theorem locator or originality credit | PASS |
| Kleppner | historical Borel multiplier/similarity terminology | not a source for a continuous trivializer | PASS |
| Austad / Leptin | ordinary time-group twisted formulas and amenable maximal/reduced endpoint | no actual non-Hausdorff owner theorem | PASS |
| Hulanicki 1964/1966 | group-level amenability, mean, and weak-containment context | no actual completion theorem; scan/registry distinction visible | PASS |
| Buss--Holkar--Meyer | ordinary transformation-groupoid component bridge without the cited second-countability obstruction | no twisted actual record | PASS |
| Williams | ordinary universal dense algebra, regular norm, homogeneous-space model, and amenable-action endpoint | no inference of C*-faithfulness from the group-valued multiplier map; no whole-component max/r equality | PASS |
| Austad--Ortega / Tu | named Hausdorff/étale and locally Hausdorff comparator domains | comparator exclusion only, not a theorem that no framework exists | PASS |
| Stacks | arbitrary set-indexed coproduct topology | no action, cardinality, Haar measure, completion, or Paper 13 theorem | PASS |

Every external claim remains at or below the exact source ceiling. The
manuscript's direct sign, support, norm, and diagonal proofs carry the
mathematical burden that the sources do not license.

## 7. Local companion identities and imported premises

All five companion records are honest URL-free, DOI-free `@unpublished`
entries. Their exact source identities and cited premises were rechecked.

| Companion | Manuscript TeX | Proof audit | Current PDF | Current BibTeX | Imported premise / locator |
|---|---|---|---|---|---|
| Paper 2, *Arithmetic Period Packets and the Missing Trace* | `72c34a0a30279ed7c070917a2c9242b8e9cb0a37a56779c246fa2cae04097fdc` | `aaab83c32eb9d6c172be192dbb14acc6ed927a972d61c24a90dbfe94ecd0dbae` | `86a60810f1f2a975bc5e694cb854a7de4bb796168f9a273888c013f84323a183` | `cdeab58c00d1129612c444a712485aa8163b3411d0527ca58cd5f6047c38d1a3` | fixed-prime continuum lower bound; `prop:uncountable` |
| Paper 8, *Isotropy Averaging Erases Returns* | `c58392dcd2b92125ff46d9fbaee90d134210e36dbaa516fd359d89c08a6729fa` | `1bbcc8f7faadb331ff0840c26472ee16722894b6dff2cae2687216e4638a5990` | `fad0f602edf4d2300b91bd7b356e363da3ab776c645288a14f39ae171aea262a` | `a0d3300c8f7cc093db47e8339adcc079f3d2a993d68d862a37e8d1d79cf0f35e` | one-orbit standard proxy, trace/return boundary, local/packet firewall, positive-time scalar ledger |
| Paper 9, *Indiscrete Prime Packets in Deninger's Rational-Witt Flow* | `24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb` | `c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8` | `c55e4f45fe5f58841864e9af695c4664bdb1a77cff6e087fd2869d4ecd385e02` | `0e4054e00ea1d09ce71d8f16fa2a051216d34f76aa437663012e726caf950f35` | actual packet, topology, stabilizer, period, bare quotient; `cor:packet`, `cor:orbit` |
| Paper 11, *Continuous Convolution Collapse on Indiscrete Arithmetic Orbit Groupoids* | `eb1aa4d7060cf1aa53a729e7c7be89a5724a6133ef3bf000cb800bf786de1002` | `03f17606b0c9d69b496d2766c0a404b0d090698101150a800de4c2108ddc6b28` | `15d207568a61590852697511df2faf4cb06fd06047574c3dc3413e352c14840d` | `33afa817ff529cd0d98a791e4ea68c0e4a34bd57158774a6c51c43174b72d877` | actual time collapse and untwisted test/maximal/reduced author records; `thm:phi`, `thm:star-algebra`, `thm:completions` |
| Paper 12, *Marked Time Cohomology and Orbitwise Standardization of Indiscrete Arithmetic Action Groupoids* | `c6ad0f8c22d68840198d744a615da06e8b062d5ccdbeedb7f4ee76bf35073163` | `c2b0fc4ce4764b476de8623c7a1b37e33d51da4a1c318c133313956abf4af6ab` | `9d6747e9f33c6ab3724beb35daedbb0efaff73691ed344374366f2392541ec15` | `b763e9c07e3265d878bfc8b4caf44fb6c92ef12e7fac59b8af0bdeb703876175` | all-degree factorization, same-carrier standardization, compact components, `J`, comparator; `thm:factorization`, `cor:packet-comparison` |

Paper 12 Section 8, Proposition 8.1 is additionally bound by exact source
SHA-256
`77258319c1e1cbcc08501e33e3c60a03acd71a62342898f3535375e6159f77e8`
for the variance direction used in Figure 1. No companion is credited with a
stronger result than its exact local bytes support.

## 8. Technical Note, claim, priority, controls, and Route boundaries

The candidate consistently uses the authorized Technical Note / NOTE branch
and displays `STANDALONE_PASS=false` on page 1, in the introduction, in the
conclusion, and in both READMEs. It does not present itself as a standalone
classification or as an owner-specific corona obstruction.

The substantive ceilings are maintained throughout:

- no globally named actual twisted groupoid completion is asserted;
- actual, bare, deliberately discrete, and standard owners remain distinct;
- maximal and reduced records remain separately typed;
- component statements concern selected constant-in-unit images, not whole
  component algebras;
- the arbitrary-index constant-diagonal theorem appears only after the
  component isometries;
- fixed-prime cases are unconditional for both completion types but
  nonselective and recover no prime or period; and
- no trace, determinant, zeta object, analytic continuation, quantization,
  spectral operator, or Route-B object is promoted.

The control receipt is reported exactly as frozen: 176/176 tests, 12 CSVs,
2,665 body rows, 67 negative controls, and 13 generated artifacts. The
controls were not rerun and are described only as finite diagnostics. They
are not used as proofs of a continuum, arbitrary-index, norm, or corona
claim.

The ten-owner Route record is also reported exactly: three exploratory and
seven rejected Route-A owners; every A2/A3/A4 coordinate fails; determinant
status is `NONE_BY_DESIGN_NO_DETERMINANT_OBJECT`; and Route B is false. The
dated phrase `SUPPORTED_WITHIN_SEARCH` is explicitly bounded to the
2026-08-15 search and proves no absence, novelty, priority, or standalone
weight. No “first” or priority superlative is smuggled into the note.

## 9. Strict six-key trace and bidirectional linkage

The package README contains exactly six fenced artifact records. Each has
exactly these six nonempty top-level keys, in this order, and no extra key:

```text
artifact_id -> source_data -> transformation -> caption_claim ->
supported_manuscript_claims -> limitations
```

There are exactly four manuscript tables and two manuscript figures, so the
trace graph is complete rather than selective.

| Artifact ID | Manuscript artifact | Forward trace | Reverse trace | Ceiling | Result |
|---|---|---|---|---|---|
| `P13-TAB-02-PRIOR-SUBTRACTION` | Table 1, `tab:prior-subtraction` | proof audit, blueprint, and citation preaudit hashes resolve | adjacent prose names the artifact ID and package trace section | attribution/subtraction, not novelty evidence | PASS |
| `P13-TAB-01-OWNER-DICTIONARY` | Table 2, `tab:owner-dictionary` | proof audit and blueprint hashes resolve | adjacent prose names the artifact ID and states the exact typing limit | dictionary, not mathematical evidence | PASS |
| `P13-FIG-01-OWNER-SUPPORT` | Figure 1, `fig:owner-support` | proof audit, core proof, support proof, and Paper 12 Proposition 8.1 source hashes resolve; figure-source hash exact | pre-figure and post-support prose name the artifact ID; README points to the equation/theorem/label | schematic only; no topology or completion transfer | PASS |
| `P13-TAB-03-NONRETENTION` | Table 3, `tab:nonretention` | support-proof hash resolves | opening Section 4 prose names the artifact ID and table | exactly four registered outputs, not every invariant | PASS |
| `P13-FIG-02-GENERIC-DIAGONAL` | Figure 2, `fig:generic-diagonal` | corona-proof and standalone-review hashes resolve; figure-source hash exact | pre-figure prose names the artifact ID; README points to component/generic/prime results | no owner-specific obstruction, prime selection, or whole-corona classification | PASS |
| `P13-TAB-04-LIMITATIONS` | Table 4, `tab:limitations` | controls review, Route audit, and standalone-review hashes resolve | adjacent prose names the artifact ID and package trace section | controls/Route/search are not mathematical proof | PASS |

All hash-addressed trace sources were rehashed and matched. Captions agree
with adjacent prose. Every listed claim points to its artifact, every
artifact points back to claim text plus locator, and there is no untraced
table/figure or orphan trace entry. Both figures are original native-vector
TikZ compositions; no source figure was copied and no raster surrogate is
embedded.

## 10. Package and source-PDF exclusion

The review package contains exactly six retained paths:

```text
README.md
manuscript.tex
references.bib
paper.pdf
figures/owner_support_firewall.tex
figures/generic_constant_diagonal.tex
```

Research-source PDFs and their preflight sidecars remain under internal
`notes/sources/` directories, outside `paper/`. No research-source PDF,
source basename, preflight sidecar, or checksum ledger is copied into the
review package. The generated `paper.pdf` has no attachment and no raster
image object, and leaks no local source path or basename.

Because this audit was expressly forbidden to use Git or perform a release,
it does not assert index, staged-tree, archive, remote-upload, attachment-set,
hidden-path, or fresh-clone exclusion. Those real release-system checks must
be run against the actual public artifact set before authorization.

## 11. Bounded originality screen

The pre-hold screen split the Freeze-1 substantive manuscript body into 70
eligible prose units after excluding display, table, figure, and list starts
and units shorter than 25 alphabetic tokens. Every odd unit plus five
high-risk even units was sampled: 40/70 units, or 57.1%. One distinctive
phrase from each sampled unit was searched case-insensitively and after
normalization across Papers 1--12, then as an exact quoted web query.

The sampled units were:

```text
1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,
41,43,45,47,49,51,53,55,57,59,61,63,65,67,69,16,24,40,64,70
```

Representative probes included “problem addressed here is narrow but
sign-sensitive,” “continuous second partial,” “restriction statement is
intentionally cohomological,” “origin-free constant-in-the-unit map,”
“selected-image qualification is substantive,” “controls were not rerun,”
“historical first-run implementation finding,” and “standalone status does
not change.” None produced a same-work exact match in Papers 1--12 or a
suspicious exact external occurrence.

Freeze 2 adds or changes seven trace-linkage prose loci. All seven were
targeted separately, including the phrases “subtraction ledger used in this
introduction,” “fixes the owner, topology, analytic domain, and completion
labels,” “owner/pullback directions and the zero/finite/infinite support
firewall,” “exactly the support branch displayed,” “generic theorem,
including its zero/finite/infinite branches,” and “cannot collapse the layers
into a single pass label.” They yielded no exact match in Papers 1--12 and no
suspicious exact quoted web result.

This is a bounded exact-phrase screen of 47 probes, not a universal guarantee
against paraphrase-level overlap. It found no evidence of unattributed exact
copying or boilerplate substitution.

## 12. Seven AI-research failure modes

| Failure mode | Evidence examined | Assessment |
|---|---|---|
| implementation bug or invalid computation | direct proofs, frozen replacement-control review, exact receipt, no unauthorized rerun | clear; finite computation is not used to carry an infinite theorem |
| citation failure or source hallucination | 17/17 graph, official metadata, exact manifestations, locators, claim ceilings | clear |
| hallucinated experimental result | stable reviewed 176/176 receipt and independently reproducible manuscript build, text, and rasters | clear |
| shortcut, leakage, or target reliance | no fitting, empirical model, random sample, or target-guided optimization; controls are diagnostic only | not applicable / clear |
| bug reframed as novelty | historical first-run control issue remains historical; current proof is direct; search status is bounded | clear |
| fabricated methodology or irreproducibility | hashes, manifests, preflights, companion tuples, build sequence, and retained/fresh identities align | clear |
| frame lock or one-sided validation | actual/bare/discrete/standard owners, max/r types, zero/finite/infinite branches, comparator exclusions, and negative Route records are visible | clear |

## 13. Findings and external-release conditions

### 13.1 Open findings

No Critical, Major, or Minor citation/source-integrity finding remains in the
exact REVIEW FREEZE 2 tuple.

### 13.2 Conditions not satisfied by this audit

The following are visible external-release gates, not silently completed
facts and not authorization to publish:

1. Replace every `AUTHOR TO CONFIRM` item with verified human decisions:
   author list/order, affiliations, correspondence, CRediT roles, funding,
   competing interests, acknowledgments, ethics wording, data/code
   coordinates, license, and final tool-assistance disclosure.
2. Complete the coordinated Paper 12 peer/release relock. Treat the older
   Paper 12 PDF/Bib values inside immutable Paper 13 upstream audits as
   historical receipts, and update the two Paper 13 README status sentences
   from “pending” to the final batch outcome before public release. Rebind
   any resulting receipt hashes; no Paper 13 theorem or bibliography edit is
   presently required.
3. Refresh DOI resolution, publisher metadata, source status, and the live
   Stacks title on the actual submission date.
4. Provide immutable public identities for the five companion manuscripts,
   or include the exact source-locked companion artifacts needed to verify
   the imported premises.
5. Run real release-system exclusion checks against the Git index/stage,
   archive, upload set, attachments, hidden paths, and a fresh clone; confirm
   that internal research-source PDFs and preflight files are absent.
6. Apply venue-specific formatting, repository, rights, accessibility, and
   disclosure requirements without weakening the citation and owner
   ceilings audited here.
7. Preserve `RELEASE_AUTHORIZED=false` until the batch-wide public-sync gate
   explicitly changes it.

## 14. Final exact-lock verdict

**PASS — REVIEW FREEZE 2 EXACT LOCK; critical 0, major 0, minor 0, retained
unverifiable claim 0.**

The 17-record citation graph is closed; all external metadata, manifestations,
locators, and claim ceilings are accurate; all five companion premises are
bound to exact current identities; the corrected Paper 12 release identity
is distinguished from immutable historical receipts; the Technical Note /
NOTE / non-standalone disposition is honest; the six artifact traces work in
both directions; the clean build, extracted text, and all page rasters agree;
the full PDF and figures are clean; and the strongest source-PDF exclusion
available without a real release operation passes.

This is a candidate citation/source-integrity PASS. It is not journal
acceptance, standalone approval, public-release authorization, or a
substitute for the explicit external gates in Section 13.2.

---

## 15. Receipt-only README and Paper-12 status relock

Relock date: **2026-08-15 (Asia/Shanghai)**  
Pre-addendum historical-prefix extent: **37,152 bytes; 516 lines**  
Pre-addendum historical-prefix SHA-256:
`2dddbf954555809463a2b4b5455959a27dd4646c4544e6097b94c3c8d311f2c0`  
Disposition: **PASS — STATUS-ONLY CITATION/SOURCE-INTEGRITY RELOCK;
C0/M0/m0; `PUBLIC_RELEASE_AUTHORIZED=false`**

This append-only addendum supersedes only the two active README receipts and
the Paper-12 completion status recorded in the report above. The entire
37,152-byte report above remains its exact historical byte prefix. No
manuscript, bibliography, figure, retained PDF, peer report, technical
release report, proof, source manifestation, control, result, Route record,
lock, or Git state was edited or regenerated for this relock. The only
workspace write made by this relock is this append to
`notes/citation_audit.md`.

### 15.1 Exact README delta and inverse proof

The two current status indexes independently rehash as follows:

| Status index | Historical bytes / SHA-256 | Current bytes / SHA-256 |
|---|---|---|
| project `README.md` | 3,511 / `729d2de14046f3004fdcd231a4d0d287e62c9b6e1af95cb592a5918df071120d` | 4,689 / `ae381531aed12d99c9498d7f2f77afb4899045f5eae2b37cab2431bc855f8990` |
| `paper/README.md` | 20,956 / `499a4618a0bab9e0a266ca81382a0a084b5016dda45ac0553224171dd4682502` | 22,350 / `d259e121d7f3a3112171f98bb798a1ae8cc2c723dbb37a99de7310f80474ee9d` |

The current project README has exactly five once-only inverse replacement
anchors. Applying them as an in-memory byte transform reconstructs **65
lines, 3,511 bytes**, and historical SHA-256
`729d2de14046f3004fdcd231a4d0d287e62c9b6e1af95cb592a5918df071120d`.
Its exact three-hunk historical-to-current comparison is:

```diff
@@ -8,10 +8,11 @@
 - Article type: **Technical Note**.
 - Retained disposition: **NOTE branch**.
 - Binding standalone flag: `STANDALONE_PASS=false`.
-- Manuscript stage: **REVIEW FREEZE 2 final internal candidate**, awaiting
-  independent re-review; this is not an external-release approval.
-- External release: `RELEASE_AUTHORIZED=false`. Author order, affiliations,
-  correspondence, CRediT roles, funding, competing interests,
+- Manuscript stage: **REVIEW FREEZE 2 final internal candidate**. Independent
+  peer, citation/source-integrity, and technical release audits each PASS with
+  C0/M0/m0; this is not an external-release approval.
+- External release: `PUBLIC_RELEASE_AUTHORIZED=false`. Author order,
+  affiliations, correspondence, CRediT roles, funding, competing interests,
   acknowledgments, public repository coordinates, license, venue language,
   and final tool disclosure remain `AUTHOR TO CONFIRM`.
 - A retained review PDF and the strict six-key trace ledger are in
@@ -37,13 +38,14 @@
 | `paper/figures/owner_support_firewall.tex` | 3,217 | `130ad2f1833a91970629311e1cf21bc848d826afcda941e9b0ad3367cb8f2360` |
 | `paper/figures/generic_constant_diagonal.tex` | 2,820 | `727160835b9190b8d3a854825ea30735e4f59813be50a6f7960f3da735558d44` |
 | `paper/paper.pdf` | 183,120 | `4082ca13a6daadb72ccc30a34fc5160f5920247d3fa3436562349ccc5a9c43c2` |
-| `paper/README.md` | 20,956 | `499a4618a0bab9e0a266ca81382a0a084b5016dda45ac0553224171dd4682502` |
+| `paper/README.md` | 22,350 | `d259e121d7f3a3112171f98bb798a1ae8cc2c723dbb37a99de7310f80474ee9d` |
 
 The candidate was built cleanly in `/tmp/p13-freeze2-final.ZK0vNp` with
 XeLaTeX, BibTeX, and three further XeLaTeX passes. The retained PDF is the
 byte-identical 15-page A4 build output. The SHA-256 of this parent status
-index is supplied in the external REVIEW FREEZE 2 handoff so that it need not
-self-record its own digest.
+index is not self-recorded. A downstream release receipt must bind this
+corrected parent README together with the corrected package README; neither
+README embeds the release-audit digest.
 
 ## Evidence and release boundary
 
@@ -53,13 +55,29 @@
 `af7b20a7e1091a876acfa4c22a9f8ba0e9c19b3accd1fe1c1376f6c13fcc48fd`,
 pre-manuscript citation PASS
 `3ed75cf27d63c84629e02d3b402de8d3e9f419923f9fec43e60fb0b319b5dd73`,
-and bounded peer report
-`abca2855cb223390341f44962559c6a82ff1daf21ae84da0a822e7f6c1c52071`.
+final REVIEW FREEZE 2 citation/source-integrity PASS
+`2dddbf954555809463a2b4b5455959a27dd4646c4544e6097b94c3c8d311f2c0`,
+and final REVIEW FREEZE 2 peer PASS
+`5ef641045f027e3d731f50d950f239c92c2c56771b1384abd6e873a6ee2a75aa`.
+The technical release audit also records PASS C0/M0/m0 on REVIEW FREEZE 2;
+the downstream release receipt will bind the status-corrected README bytes.
 The reviewed finite receipt remains diagnostic only: 176/176 tests, 12 CSVs,
 2,665 body rows, 67 negative controls, and 13 generated artifacts.
 
-A Paper 12 upstream bibliographic-title correction is pending the coordinated
-batch relock. This bounded Paper 13 revision did not mechanically edit its
-locked upstream research files or the literal audited 17-record bibliography
-seed. Any later batch metadata relock must be coordinated and rehashed before
-external release.
+The coordinated Paper 12 bibliographic-title correction and its technical
+relocks are complete:
+
+| Current Paper 12 artifact | SHA-256 |
+|---|---|
+| `paper/references.bib` | `b763e9c07e3265d878bfc8b4caf44fb6c92ef12e7fac59b8af0bdeb703876175` |
+| `paper/paper.pdf` | `9d6747e9f33c6ab3724beb35daedbb0efaff73691ed344374366f2392541ec15` |
+| `notes/citation_audit.md` | `79089b2487b6b21c10c1f10a4918fb29602d265877483d7a325634d15ec70a3a` |
+| `notes/peer_review_round1.md` | `f3eaef077677144470e3f0417cb418009f0d340a8cd2856ac6cff74cf337438a` |
+| `notes/release_audit.md` | `53afb3642812e981d0bb38b7166982c8818b7ef7085d96277dddd8f632d8d99b` |
+
+The load-bearing Paper 12 manuscript and Proposition-8.1 proof identities are
+unchanged. Older Paper 12 identities in immutable Paper 13 upstream receipts
+remain historical receipts. This status-only Paper 13 correction did not edit
+locked upstream research files, the literal audited 17-record bibliography
+seed, controls, Route records, or any release system. Consequently,
+`PUBLIC_RELEASE_AUTHORIZED=false` remains binding.
```

The package README has exactly four once-only inverse replacement anchors.
Applying them in memory reconstructs **248 lines, 20,956 bytes**, and
historical SHA-256
`499a4618a0bab9e0a266ca81382a0a084b5016dda45ac0553224171dd4682502`.
Its exact three-hunk historical-to-current comparison is:

```diff
@@ -18,14 +18,21 @@
   competing interests, acknowledgments, public repository coordinates,
   licenses, venue-specific ethics wording, and final tool-disclosure wording
   remain `AUTHOR TO CONFIRM`.
-- A retained `paper.pdf` is present for review. Release authorization remains
-  false. No Git action or public synchronization was performed.
+- The independent peer, citation/source-integrity, and technical release
+  audits each PASS with C0/M0/m0 on REVIEW FREEZE 2.
+- A retained `paper.pdf` is present for review.
+  `PUBLIC_RELEASE_AUTHORIZED=false`; no Git action or public synchronization
+  was performed.
 - The parent `../README.md` was updated only under the explicit bounded
   post-review authorization, replacing its obsolete Phase-1 stub with this
   Technical Note / NOTE-branch / external-release-hold status.
-- A Paper 12 upstream bibliographic-title correction remains pending the batch
-  relock. This bounded revision did not mechanically alter any locked P13
+- The Paper 12 upstream bibliographic-title correction and its citation,
+  peer, and release relocks are complete at the exact identities recorded
+  below. This status-only revision did not mechanically alter any locked P13
   research, proof, control, Route, citation-gate, or bibliography input.
+- These README bytes postdate the first exact-lock release audit. A downstream
+  release receipt must bind both corrected README byte identities; neither
+  README self-binds or embeds the release-audit digest.
 
 ## Frozen upstream controls
 
@@ -45,9 +52,25 @@
 | `notes/phase3_v2_controls_review.md` | `c89a503f0cd624f4a9f119e12fedd0a2c7d6a5b2d55613a1a0e42f3e19917789` | replacement-controls review, PASS C0/M0/m0 |
 | `results/manifest.json` | `26a41e2920d9a3743cc1b681aa1e32d601dc12e5fded15b3c6349840bd9094c2` | frozen controls manifest |
 | `notes/route_audit.md` | `2603502519e087a5023be2fec91e8b332a37d93a1368300a8e103680d6c5b0b9` | ten-record Route audit |
-| `notes/peer_review_round1.md` | `abca2855cb223390341f44962559c6a82ff1daf21ae84da0a822e7f6c1c52071` | REVIEW FREEZE 1 peer report, C0/M2/m1, bounded revision authority |
+| `notes/peer_review_round1.md` | `5ef641045f027e3d731f50d950f239c92c2c56771b1384abd6e873a6ee2a75aa` | final REVIEW FREEZE 2 peer report, PASS C0/M0/m0 |
+| `notes/citation_audit.md` | `2dddbf954555809463a2b4b5455959a27dd4646c4544e6097b94c3c8d311f2c0` | final REVIEW FREEZE 2 citation/source-integrity report, PASS C0/M0/m0 |
 | `papers/12-marked-time-cohomology/notes/phase3_orbitwise_standardization_h1_proofs.md` | `77258319c1e1cbcc08501e33e3c60a03acd71a62342898f3535375e6159f77e8` | unedited upstream source for the Section 8, Proposition 8.1 variance premise |
 
+The completed corrected Paper 12 technical tuple and relocks are:
+
+| Current Paper 12 artifact | SHA-256 |
+|---|---|
+| `paper/references.bib` | `b763e9c07e3265d878bfc8b4caf44fb6c92ef12e7fac59b8af0bdeb703876175` |
+| `paper/paper.pdf` | `9d6747e9f33c6ab3724beb35daedbb0efaff73691ed344374366f2392541ec15` |
+| `notes/citation_audit.md` | `79089b2487b6b21c10c1f10a4918fb29602d265877483d7a325634d15ec70a3a` |
+| `notes/peer_review_round1.md` | `f3eaef077677144470e3f0417cb418009f0d340a8cd2856ac6cff74cf337438a` |
+| `notes/release_audit.md` | `53afb3642812e981d0bb38b7166982c8818b7ef7085d96277dddd8f632d8d99b` |
+
+The Paper 12 manuscript and Proposition-8.1 proof identities used by Paper 13
+remain unchanged. Older Paper 12 byte identities in immutable Paper 13
+upstream receipts remain historical receipts rather than current release
+identities.
+
 The replacement controls were not rerun during manuscript composition. The
 manuscript reports only the frozen reviewed receipt: 176/176 tests, 12 CSVs,
 2,665 body rows, 67 negative controls, and 13 generated artifacts. Those
@@ -64,10 +87,10 @@
 | `figures/generic_constant_diagonal.tex` | 2,820 | `727160835b9190b8d3a854825ea30735e4f59813be50a6f7960f3da735558d44` |
 | `paper.pdf` | 183,120 | `4082ca13a6daadb72ccc30a34fc5160f5920247d3fa3436562349ccc5a9c43c2` |
 
-This README deliberately does not self-record its own hash. Its final SHA-256
-and the final SHA-256 of the parent `../README.md` are supplied in the external
-REVIEW FREEZE 2 handoff. The parent index records this package README digest,
-so no circular self/cross-hash is embedded here.
+This README deliberately does not self-record its own hash. The parent index
+records this package README digest one-way, and a downstream release receipt
+must bind both corrected README byte identities. No README embeds its own
+digest or the digest of `notes/release_audit.md`.
 
 ## Clean build and inspection receipt
```

Thus the current README files are related to the historical exact-lock files
by status and receipt substitutions only. The inverse hashes prove the old
identities rather than merely restating them. Neither diff touches a
mathematical claim, bibliography field, source locator, figure/table trace,
control result, Route record, or rendered-manuscript input.

### 15.2 Unchanged REVIEW FREEZE 2 scholarly tuple

The current scholarly tuple was rehashed immediately before this append:

| Artifact | Bytes | SHA-256 | Relock result |
|---|---:|---|---|
| `paper/manuscript.tex` | 54,338 | `c8c9b7522e9bf63a30ed199fe3468d642cb3e572e324680ccd6893857fbe9701` | unchanged |
| `paper/references.bib` | 5,834 | `661aa0a948e8a06538cb300106e91bc9d72e91bf26e9515fdb9a074d0f394292` | unchanged |
| `paper/figures/owner_support_firewall.tex` | 3,217 | `130ad2f1833a91970629311e1cf21bc848d826afcda941e9b0ad3367cb8f2360` | unchanged |
| `paper/figures/generic_constant_diagonal.tex` | 2,820 | `727160835b9190b8d3a854825ea30735e4f59813be50a6f7960f3da735558d44` | unchanged |
| `paper/paper.pdf` | 183,120 | `4082ca13a6daadb72ccc30a34fc5160f5920247d3fa3436562349ccc5a9c43c2` | unchanged; retained 15-page A4 output |

The package still contains exactly the same six paths; only its README bytes
changed. The final peer report remains
`5ef641045f027e3d731f50d950f239c92c2c56771b1384abd6e873a6ee2a75aa`
and records REVIEW FREEZE 2 exact-lock PASS C0/M0/m0. The first technical
release audit remains
`45eccf26308a0845d0b0bf49cbab0d2120b9c77edbb4418d3832ed22130501ed`
and records technical PASS C0/M0/m0 on the unchanged scholarly tuple. Its
build, text/raster, visual, font, PDF, trace, control, Route, and source-
exclusion findings are unaffected by the two status-index substitutions.
That historical release report does not itself bind the corrected README
bytes; the downstream status-only release receipt remains a separate lane.

No rebuild was warranted or performed: `manuscript.tex`, `references.bib`,
both figure sources, and the retained PDF are byte-identical to the audited
tuple, while neither README is an input to the manuscript build. No control,
Route, Git, archive, upload, attachment, or public-sync operation was run.

### 15.3 Citation graph and source-integrity inheritance

A fresh read-only source parse returns exactly **18 citation commands, 19 key
occurrences, 17 unique cited keys, and 17 unique bibliography records**, with
zero missing keys, zero orphan records, zero duplicate bibliography keys, and
zero duplicate DOI strings. These are the same counts and sets as Section 4.

Because the manuscript, literal 17-record bibliography seed, figures, PDF,
and all source/claim locators retain their audited hashes, there is no
citation-context, metadata, manifestation, locator, companion-premise,
claim-ceiling, or strict-trace drift to reopen. This narrow status relock does
not invent a new live-web or source-full-text verification event; it preserves
the exhaustive verification in the exact historical prefix on demonstrably
unchanged scholarly bytes.

### 15.4 Completed Paper-12 correction boundary

The corrected Paper-12 artifacts named by both current READMEs independently
rehash exactly as follows:

| Paper-12 artifact | SHA-256 | Current status |
|---|---|---|
| `paper/references.bib` | `b763e9c07e3265d878bfc8b4caf44fb6c92ef12e7fac59b8af0bdeb703876175` | corrected Stacks title |
| `paper/paper.pdf` | `9d6747e9f33c6ab3724beb35daedbb0efaff73691ed344374366f2392541ec15` | corrected rendered bibliography |
| `notes/citation_audit.md` | `79089b2487b6b21c10c1f10a4918fb29602d265877483d7a325634d15ec70a3a` | correction-freeze citation PASS |
| `notes/peer_review_round1.md` | `f3eaef077677144470e3f0417cb418009f0d340a8cd2856ac6cff74cf337438a` | correction-freeze peer PASS C0/M0/m0 |
| `notes/release_audit.md` | `53afb3642812e981d0bb38b7166982c8818b7ef7085d96277dddd8f632d8d99b` | correction-freeze technical release PASS C0/M0/m0 |

The Paper-12 completion condition formerly listed in Section 13.2 item 2 is
therefore closed for this status receipt. Older Paper-12 and README hashes in
the immutable prefix remain valid historical receipts, not current-release
assertions. Paper 12's load-bearing manuscript, proof audit, and Proposition-
8.1 source identity remain unchanged, so no Paper-13 imported premise moved.

The remaining external gates in Section 13.2 are not silently closed: human
authorship/declaration decisions, immutable public companion identities or a
self-contained accepted substitute, venue and submission-day source/policy
checks, real release-system source-PDF exclusion, and explicit public-release
authorization remain mandatory.

### 15.5 Relock verdict and receipt

**PASS — STATUS-ONLY CITATION/SOURCE-INTEGRITY RELOCK; C0/M0/m0.** The two
current README identities are exact, their guarded inverse substitutions
reconstruct both historical hashes byte for byte, the corrected Paper-12
technical relocks are complete, and the Paper-13 scholarly tuple and 17/17
citation graph have no byte or semantic drift. This is not a rebuild, a new
source-verification event, a downstream release-audit receipt, journal
acceptance, standalone approval, or public-release authorization.

```text
P13_CITATION_STATUS_RELOCK=PASS
P13_FINDINGS=C0/M0/m0
P13_HISTORICAL_PREFIX_BYTES=37152
P13_HISTORICAL_PREFIX_LINES=516
P13_HISTORICAL_PREFIX_SHA256=2dddbf954555809463a2b4b5455959a27dd4646c4544e6097b94c3c8d311f2c0
P13_PARENT_README_SHA256=ae381531aed12d99c9498d7f2f77afb4899045f5eae2b37cab2431bc855f8990
P13_PARENT_README_INVERSE_SHA256=729d2de14046f3004fdcd231a4d0d287e62c9b6e1af95cb592a5918df071120d
P13_PACKAGE_README_SHA256=d259e121d7f3a3112171f98bb798a1ae8cc2c723dbb37a99de7310f80474ee9d
P13_PACKAGE_README_INVERSE_SHA256=499a4618a0bab9e0a266ca81382a0a084b5016dda45ac0553224171dd4682502
P13_FREEZE2_MANUSCRIPT_SHA256=c8c9b7522e9bf63a30ed199fe3468d642cb3e572e324680ccd6893857fbe9701
P13_FREEZE2_BIB_SHA256=661aa0a948e8a06538cb300106e91bc9d72e91bf26e9515fdb9a074d0f394292
P13_FREEZE2_PDF_SHA256=4082ca13a6daadb72ccc30a34fc5160f5920247d3fa3436562349ccc5a9c43c2
P13_CITATION_GRAPH=PASS_17_OF_17
P13_P12_RELEASE_SHA256=53afb3642812e981d0bb38b7166982c8818b7ef7085d96277dddd8f632d8d99b
P13_REBUILD_PERFORMED=false
P13_CONTROLS_RERUN=false
P13_GIT_OR_PUBLIC_SYNC_PERFORMED=false
P13_PUBLIC_RELEASE_AUTHORIZED=false
P13_FINAL_REPORT_SHA256=RECORDED_EXTERNALLY
```

This enlarged report deliberately does not embed its own digest. Its final
SHA-256 is recorded in the external handoff after the file is closed.
