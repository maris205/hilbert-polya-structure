# Paper 11 pre-manuscript citation and source-integrity audit

Audit date: **2026-08-15 (Asia/Shanghai)**  
Audit role: **ARS academic-paper citation compliance and research-integrity
preflight**  
Verdict: **PASS FOR MANUSCRIPT DRAFTING — C0/M0/m0 on the frozen source
tuple; final manuscript and public-release gates remain pending**

This is a pre-manuscript audit. It fixes the smallest defensible bibliography,
the exact manifestation and locator rules, and the line between source-owned
facts and Paper-11 author-defined results. It does not certify a bibliography
or citation context that has not yet been written, and it does not authorize a
submission or public synchronization.

The audit is bound to the final composition blueprint
`notes/composition_blueprint.md`, SHA-256
`4b6bfa27c83f72858ac5f0d03c0b9964f93e914fc1d4fdfced619327bcdfc30b`
(743 lines). No source, proof, control, Route, or manuscript artifact was
edited during this audit.

## 1. Exact evidence binding

The following bytes were re-hashed before this report was written.

| Evidence artifact | SHA-256 | Audit use |
|---|---|---|
| `notes/phase2_framework_source_audit.md` | `a2345046972cc00d3031abdc214442359d0f78c7c0daf7d513ea26f924fb7439` | exact framework hypotheses and source locators |
| `notes/sources/framework_source_manifest.md` | `b3b61a5bdfd206cb8cc4a8bf574373bc6485d96b22547698ac69fb3a9e36812f` | five retained manifestations, provenance, and redistribution class |
| `notes/sources/framework_sources.sha256` | `057e9c32b2f654c765f40f0ddd40014c12876d22c0567470fdf04a2eb0fd2e7f` | five-PDF/five-sidecar checksum ledger |
| `notes/phase2_owner_proxy_audit.md` | `18116cf52c2359a840c9996fb6424fae56260f590990fac79704c040245fa761` | Deninger/actual/proxy/group attribution ladder |
| `notes/phase2_novelty_search.md` | `024398a3575cf41a7f33c6950dc1c8de8a8d5f4ec81675f8760ce7c7a87ac24e` | bounded exact-package search and limitations |
| `notes/phase3_core_proofs.md` | `4e79446d4a9bb861211186ffd3aa3b42899bc382fbf215a5a453495e5fbb0a66` | direct `P11-1`--`P11-5` claims |
| `notes/phase3_proxy_ownership_proofs.md` | `46603a1c2185cec1ffb3e7a2cb0f70873abf995edcc104977ac3d360d76e6401` | direct `P11-6`--`P11-8` claims |
| `notes/proof_audit.md` | `03f17606b0c9d69b496d2766c0a404b0d090698101150a800de4c2108ddc6b28` | integrated claim/owner/proof audit |
| `notes/phase3_peer_review.md` | `b16027be916e4e6b8787bce8692dd8461f1e79fb29ea73b9b1d67f530341ad5c` | independent `PASS — C0/M0/m0` |
| `notes/route_audit.md` | `9203d37cfaa28a45a7548a9864de614c81bf6ea199b4a6736e1c5aaa84335011` | seven typed Route-A records and zero Route-B records |
| `notes/composition_blueprint.md` | `4b6bfa27c83f72858ac5f0d03c0b9964f93e914fc1d4fdfced619327bcdfc30b` | final manuscript source/citation plan |
| Paper 9 `notes/source_audit.md` | `20fecdf360d18f9accf3e3ec8467f3beb369a8737761eb6219fef71e9773ac20` | Deninger manifestation and source ceiling |
| Paper 9 `notes/proof_audit.md` | `c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8` | inherited-orbit topology theorem |
| Paper 9 `paper/paper.pdf` | `c55e4f45fe5f58841864e9af695c4664bdb1a77cff6e087fd2869d4ecd385e02` | exact companion manuscript manifestation |

The final blueprint and the integrated proof audit agree on every external
source role. Paper 9 is a load-bearing companion only for the actual orbit's
nonempty, nontrivial, inherited-indiscrete topology. Paper 10 is not a
mathematical premise because Paper 11 proves the arrow-level factorization
and strict test-function comparison directly. Morishita is not in the frozen
citation plan.

## 2. Read-integrity and exact-manifestation check

Running `sha256sum -c framework_sources.sha256` in the Paper-11 source folder
returned **10/10 OK**. Each retained Paper-11 PDF had a same-stem preflight
sidecar with `verdict: PASS`, equal declared/enumerated/reader page counts,
and an empty warning array before any page-level inspection occurred.

| Retained manifestation | Pages | PDF SHA-256 | Directly rechecked locator content |
|---|---:|---|---|
| Tu 2004 official journal PDF | 34 | `ff88e322eee65d2d6dd083697c82febb3759268f9b36083264a3e20b6e586897` | physical 3/printed 567 Def. 1.1; physical 17/printed 581 §4.1; physical 19/printed 583 Def. 4.6 |
| Muhly--Williams 2008 official NYJM view PDF | 87 | `7a7c16f132f1df35f8bf304206e998796834cd23a31836dd4e15108f91806f20` | pp. 3--7; pp. 21--23 Prop. 4.4 |
| Exel arXiv `0812.4087v3` | 12 | `01b1ac9a6f98444438c654b2e4d8b69ff6058e15c02ae6704e6d254f457c3a99` | physical/printed p. 1 §1 |
| Buss--Holkar--Meyer arXiv `1612.04963v2` | 30 | `8be7896ed1aab1138b8ccf067ebfbba0f8b7d8a1dc8713fbf6c2f173ffe647e6` | pp. 1--2; p. 23 §7.1 and Thm. 7.1 |
| Williams author draft 3.1 | 540 | `3dbc1fb9e96191a278e0d59feb4981d3bbea4faa4df609d1886c81125bffe9c2` | physical/printed 38/26, 54/42, 94/82, 150/138, and 210--211/198--199 |

The inherited Deninger v4 PDF was also inspected only after its existing PASS
sidecar was checked: 119 declared/enumerated/reader pages, no warnings, PDF
SHA-256
`edd0bc8c2efb601ed7574e8eceae40e8cde21d0e4b2bc8c4ce7e60d8e1f82a09`.
The verified locators are physical p. 32 Eqs. (35),(38), p. 33 Eq. (39),
p. 38 §6, and p. 39 Thm. 6.1.

### Conditional proxy-ladder sources

The inherited Paper-8 sidecars for Green, Muhly--Renault--Williams, and
Brown--Green--Rieffel recorded `UNAVAILABLE` because that earlier environment
lacked `pypdf`. For this audit, new sidecars were generated in a temporary
directory with `pdf_read_preflight/1.0.0` and `pypdf 6.15.0` against the same
bytes. All three returned PASS with matching page counts and no warnings.
The temporary sidecars and renders were deleted after inspection and were not
added to the repository, as this task permits only the present report.

| Conditional source | Pages / SHA-256 | Locator independently rechecked here | Exact strength |
|---|---|---|---|
| Green 1978 | 60 / `bca0701f16e965424563004c5e6d9eec2a9310e05b860857f23d97b2f8819b3d` | physical 13 / printed 203, Prop. 3 | full-level imprimitivity bimodule; strong Morita equivalence only |
| Muhly--Renault--Williams 1987 | 20 / `16723f6b3b3d90f220a4bc0814ed8374817ae2025c8eef9822f520a8da7b6629` | physical 8 / printed 10, Thm. 2.8; physical 14 / printed 16, Thm. 3.1 | full groupoid Morita equivalence; separately, full transitive-groupoid tensor isomorphism for some positive measure |
| Brown--Green--Rieffel 1977 | 19 / `d2b64846c0dd59668f261782ae832df1bb7dad15479d5bb5c2e7aeec37fd19c8` | physical 4 / printed 351, Thm. 1.2; physical 5 / printed 352, homogeneous-space example | stable isomorphism under strictly-positive-element hypotheses; no cancellation of compact operators |

These three sources are cleared only as conditional proxy-strength citations.
They are not needed in the minimum bibliography below.

## 3. Minimum bibliography lock

The minimum defensible bibliography has **seven** entries: six external
primary/authoritative works and one load-bearing companion manuscript. No
secondary source is used as theorem authority.

| Suggested key | Exact bibliographic record | Manifestation rule and Paper-11 role |
|---|---|---|
| `Deninger2026` | Christopher Deninger, “Dynamical systems for arithmetic schemes,” *Indagationes Mathematicae* **37**(1) (2026), 25--136, DOI [`10.1016/j.indag.2024.05.007`](https://doi.org/10.1016/j.indag.2024.05.007) | Cite the final journal metadata; add `arXiv:1807.06400v4` and a note that all technical locators refer to v4, revised 7 February 2024. Owns only the source set, action, stabilizer, and period. |
| `Wang2026Packets` | Liang Wang, “Indiscrete Prime Packets in Deninger's Rational-Witt Flow: Simultaneous Approximation and a Topological Corrigendum,” companion manuscript (2026) | Cite Cor. 5.3, p. 11, for the actual inherited orbit being nontrivial indiscrete. Do not invent a DOI or URL; insert an immutable public repository/release identifier before standalone release. The exact audit PDF hash is not a substitute for bibliographic metadata. |
| `Tu2004` | Jean-Louis Tu, “Non-Hausdorff groupoids, proper actions and K-theory,” *Documenta Mathematica* **9** (2004), 565--597, DOI [`10.4171/DM/178`](https://doi.org/10.4171/DM/178) | Owns the quasi-compact/compact terminology, Hausdorff-open span convention, and named Haar-system framework domain; never an actual-owner theorem. |
| `MuhlyWilliams2008` | Paul S. Muhly and Dana P. Williams, *Renault's Equivalence Theorem for Groupoid Crossed Products*, *NYJM Monographs* **3** (2008), official record [NYJM](https://nyjm.albany.edu/m/2008/3.htm) | Cite the published monograph manifestation. It has no publication DOI in the official record. Do not assign the arXiv DataCite DOI to the monograph. Owns accepted patch-span practice and its standing hypotheses only. |
| `Exel2011` | Ruy Exel, “Non-Hausdorff étale groupoids,” *Proceedings of the American Mathematical Society* **139**(3) (2011), 897--907, DOI [`10.1090/S0002-9939-2010-10477-X`](https://doi.org/10.1090/S0002-9939-2010-10477-X) | Add `eprint = 0812.4087`, `archivePrefix = arXiv`, and a note that the inspected technical locator is arXiv v3, p. 1, whose title is “Non-Hausdorff groupoids.” Owns only the independent étale boundary. |
| `BussHolkarMeyer2018` | Alcides Buss, Rohit Holkar, and Ralf Meyer, “A universal property for groupoid C*-algebras. I,” *Proceedings of the London Mathematical Society* (3) **117**(2) (2018), 345--375, DOI [`10.1112/plms.12131`](https://doi.org/10.1112/plms.12131) | Add `arXiv:1612.04963v2` and note that locators refer to that final accepted version. Owns the Hausdorff-only boundary and the full standard-proxy groupoid/crossed-product bridge, not a reduced or actual bridge. |
| `Williams2007` | Dana P. Williams, *Crossed Products of C*-Algebras*, Mathematical Surveys and Monographs **134**, American Mathematical Society, Providence, RI, 2007, ISBN `978-0-8218-4242-3`, DOI [`10.1090/surv/134`](https://doi.org/10.1090/surv/134) | Cite the published monograph, while noting that technical physical/printed offsets were checked against author manuscript Version 3.1 (6 September 2006). Owns group-`R` harmonic analysis and standard-proxy results only. |

### Mandatory manifestation normalizations

1. **Exel must not be a title/DOI hybrid.** The retained arXiv v3 title is
   “Non-Hausdorff groupoids” and its arXiv-issued DOI is
   `10.48550/arXiv.0812.4087`. The published title is “Non-Hausdorff étale
   groupoids” and its publication DOI is
   `10.1090/S0002-9939-2010-10477-X`. Use the published record plus an explicit
   v3 locator note; never combine the arXiv title with the journal DOI as if
   that were one exact manifestation. The [official arXiv history](https://arxiv.org/abs/0812.4087),
   [author publication list](https://mtm.ufsc.br/~exel/publications/), and
   [AMS volume index](https://www.ams.org/journals/proc/2011-139-12/proc-139-12-print-matter.pdf)
   establish the distinction.
2. **Muhly--Williams pages belong to the NYJM PDF.** The official arXiv record
   explicitly says that [arXiv `0707.3566v2`](https://arxiv.org/abs/0707.3566)
   has different pagination from the published version. All Paper-11
   locators in this audit refer to the 87-page official NYJM view PDF.
3. **Buss--Holkar--Meyer pages belong to arXiv v2.** The publication metadata
   and DOI are final, but pp. 1--2 and p. 23 are v2 physical pages unless a
   separate final-version page translation is performed.
4. **Williams has two page-count systems.** AMS records a 528-page published
   monograph, while the retained author draft has 540 physical PDF pages.
   Bibliographic pagination must be the publication's; locator notes must
   preserve the audited physical/printed offsets. The DOI is mandatory.
5. **Deninger uses final metadata plus v4 technical pages.** Do not silently
   present arXiv physical pages as journal pages.

### Excluded and conditional entries

- **Paper 10:** exclude from the minimum bibliography. It is contextual, not
  a premise; `P11-2` and the direction/strictness of `I` are proved directly
  in Paper 11.
- **Morishita:** exclude. It is adjacent current work but is not used by the
  frozen argument or blueprint.
- **Green, Muhly--Renault--Williams, and Brown--Green--Rieffel:** add all or
  the exact subset actually discussed only if the manuscript retains the
  proxy-strength ladder. Williams Thm. 4.30 already supplies the precise
  unstabilized proxy tensor model required by the core manuscript.

With the seven-entry minimum, author self-citation is **1/7 = 14.3%**, below
the ARS 15% advisory trigger. Adding Paper 10 without a mathematical need
would make it **2/8 = 25%** and would require an explicit relevance
justification. If the three genuine proxy-ladder sources are added while
Paper 10 remains excluded, the ratio becomes 1/10 = 10%.

## 4. Exact citation locator and use plan

Every citation below must be adjacent to the sentence it supports. A source
may be cited for a definition, standing hypothesis, or comparison ceiling
without being credited for a Paper-11 theorem.

| Source | Exact locator to print or identify | Claim it may support | Claim it may not support |
|---|---|---|---|
| Deninger v4 | physical p. 32 Eqs. (35),(38); p. 33 Eq. (39) | fixed-prime source set and equivariant set bijection | topology or homeomorphism |
| Deninger v4 | physical p. 38 §6; p. 39 Thm. 6.1 | right `+t` suspension flow, stabilizer `p^Z`, period `log p` | transformation groupoid, convolution, or canonical orbit chart |
| Paper 9 exact PDF | Cor. 5.3, p. 11 | every actual inherited orbit is nontrivial indiscrete, while retaining the set stabilizer and period | standard-circle topology or a new Deninger theorem |
| Tu 2004 | physical 3 / printed 567, Def. 1.1 | open-cover quasi-compactness; compact means quasi-compact plus Hausdorff | quasi-compact equals Hausdorff compact |
| Tu 2004 | physical 17 / printed 581, §4.1 | span of zero-extensions from open Hausdorff patches; possible failure of global continuity | the author global-QC function class |
| Tu 2004 | physical 19 / printed 583, Def. 4.6 | exact domain and conditions of Tu's Haar-system framework | an actual `G_act` Haar system |
| Muhly--Williams 2008 | pp. 3--7, especially G1--G4 | locally Hausdorff/local compactness, Hausdorff unit, compact Hausdorff neighborhoods, open range/source, and accepted raw span | framework applicability after those premises fail |
| Muhly--Williams 2008 | pp. 21--23, Prop. 4.4 | patch convolution and completion under the standing assumptions | convolution on the actual author-defined domain |
| Exel arXiv v3 | physical/printed p. 1, §1 | étale boundary with locally compact Hausdorff unit and local-homeomorphism range/source | a positive theorem for the non-Hausdorff actual unit |
| Buss--Holkar--Meyer v2 | pp. 1--2 | construction as written assumes locally compact Hausdorff groupoids | universal nonexistence outside that setting |
| Buss--Holkar--Meyer v2 | p. 23, §7.1 and Thm. 7.1 | full standard Hausdorff transformation-groupoid/crossed-product isomorphism | reduced bridge, actual bridge, or completion map for `I` |
| Williams draft 3.1 | physical 38 / printed 26, Ex. 1.80 | character/Fourier sign `exp(-ixy)` | a Paper-11 sign convention without the displayed transport proof |
| Williams draft 3.1 | physical 54 / printed 42, Eqs. (2.4)--(2.5) | inverse-pullback action and right-to-left conversion | continuity of the actual-to-proxy map |
| Williams draft 3.1 | physical 94 / printed 82, Prop. 3.1 | `C^*(R) ~= C_0(R-hat)` and, after the stated character convention, `C_0(R)` | a standard actual groupoid completion |
| Williams draft 3.1 | physical 150 / printed 138, Eq. (4.63), Thm. 4.30 | normalized quotient measure and unstabilized full proxy tensor model | norm boundedness or completion extension of `I` |
| Williams draft 3.1 | physical 210--211 / printed 198--199, Def. 7.7, Exs. 7.9/7.11, Thm. 7.13 | group reduced norm, abelian amenability, and full/reduced equality for group `R` | amenability of the actual groupoid |

If the optional ladder is retained, use exactly these additional locators:

- Green, Prop. 3, physical 13 / printed 203: full-level imprimitivity and
  strong Morita equivalence only;
- Muhly--Renault--Williams, Thm. 2.8, physical 8 / printed 10: full groupoid
  Morita equivalence; Thm. 3.1, physical 14 / printed 16: a separate full
  transitive-groupoid tensor isomorphism for some positive measure;
- Brown--Green--Rieffel, Thm. 1.2, physical 4 / printed 351, and the example
  on physical 5 / printed 352: stable isomorphism under the stated
  hypotheses, never cancellation of compact operators.

Their exact metadata are:

- Philip Green, “The local structure of twisted covariance algebras,” *Acta
  Mathematica* **140** (1978), 191--250, DOI
  [`10.1007/BF02392308`](https://doi.org/10.1007/BF02392308);
- Paul S. Muhly, Jean N. Renault, and Dana P. Williams, “Equivalence and
  isomorphism for groupoid C*-algebras,” *Journal of Operator Theory*
  **17**(1) (1987), 3--22, [official JOT record](https://jot.theta.ro/jot/archive/1987-017-001/1987-017-001-001.html);
  no publication DOI was located in that official record; and
- Lawrence G. Brown, Philip Green, and Marc A. Rieffel, “Stable isomorphism
  and strong Morita equivalence of C*-algebras,” *Pacific Journal of
  Mathematics* **71**(2) (1977), 349--363, DOI
  [`10.2140/pjm.1977.71.349`](https://doi.org/10.2140/pjm.1977.71.349).

## 5. Author-defined versus source-owned attribution

The manuscript must not use a literature citation to make an author-defined
record look standard. Conversely, direct proof does not erase source credit
for imported group or proxy facts.

| Paper-11 result | Correct owner/credit | Citation treatment |
|---|---|---|
| `P11-1` arrow opens, closures, quasi-compactness, separation, and groupoid structure | Paper 11, direct proof on `X_indisc x R` | Cite Tu only for terminology contrast, not for the theorem. |
| `P11-2` continuous/measurable factorization through time | Paper 11, direct proof | No external theorem attribution; state the exact target separation hypothesis. |
| `P11-3` `Phi:C_c(R)->C_qc^glob(G)` and exact support | Paper 11, author global-QC definition and direct proof | Tu/MW may be cited only to distinguish their different raw patch-span domains. |
| `P11-4` `GLOB-FIBRE-FAMILY`, convolution, involution, and `*`-algebra | Paper 11, author fibre contract and direct proof | Do not call it a retained-source Haar system or cite Tu/MW as its authority. |
| `P11-5` `Ind_x`, faithful reduced norm, and transported completions | Paper 11 for the operator family and transport; Williams for the group-`R` theorem used after transport | “Author-defined source-fibre operator/completion” must precede the Williams identification. |
| `P11-6` no nonempty Hausdorff arrow open and raw HOpen value zero | Paper 11, direct topology proof | Tu/MW/Exel/BHM support the convention and failed-hypothesis table only. HOpen remains `DIAGNOSTIC_ONLY`. |
| `P11-7` one-sided `J`, strict test-level `I`, and image `A_const` | Paper 11, direct proof | BHM/Williams/optional ladder are proxy-only; none licenses a norm or completion map for `I`. |
| `P11-8a` action blindness for every nonempty indiscrete `R`-action | Paper 11, generic theorem | No arithmetic novelty claim and no Paper-10 dependency. |
| `P11-8b` rational-Witt fixed-orbit application | Deninger for set/action/stabilizer; Paper 9 for actual indiscreteness; Paper 11 for the groupoid/analytic consequences | Cite both imported owners at the first specialization; never credit Deninger with topology or Paper 9 with convolution. |
| `P11-9` finite controls | Paper 11 deterministic implementation and manifest | Repository provenance, not an external theorem citation; controls are witnesses, not proofs. |
| `P11-10` Route result | Paper 11 typed Route audit | No scholarly citation can promote it to Route B; all seven owners have `A4_FAIL`. |

Hashes and local paths may appear in an evidence or reproducibility appendix.
They must not be used as substitutes for normal bibliographic citations in
the mathematical prose.

## 6. Currentness, corrections, and bounded search status

### Official record verification

The following current facts were checked on 2026-08-15 against official or
authoritative endpoints:

- Deninger: [arXiv history](https://arxiv.org/abs/1807.06400) identifies v4
  as the 7 February 2024 revision; the [publisher record](https://www.sciencedirect.com/science/article/pii/S0019357724000491)
  gives *Indagationes Mathematicae* 37(1) (January 2026), 25--136, and DOI
  `10.1016/j.indag.2024.05.007`.
- Tu: the [EMS record](https://ems.press/journals/dm/articles/8965109) gives
  the author, title, *Documenta Mathematica* 9 (2004), 565--597, and DOI
  `10.4171/DM/178`.
- Muhly--Williams: the [official NYJM record](https://nyjm.albany.edu/m/2008/3.htm)
  gives both authors, Monographs 3 (2008), and publication date 4 June 2008;
  the [arXiv history](https://arxiv.org/abs/0707.3566) records v2 and warns of
  different pagination.
- Exel: the [arXiv history](https://arxiv.org/abs/0812.4087) identifies v3,
  23 November 2009; the [author's current publication list](https://mtm.ufsc.br/~exel/publications/)
  identifies the 2011 journal title and pages.
- Buss--Holkar--Meyer: the [arXiv history](https://arxiv.org/abs/1612.04963)
  labels v2 the final accepted version; the [publisher record](https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/plms.12131)
  gives the authors, volume/issue/pages, and first-publication date.
- Williams: the [AMS record](https://bookstore.ams.org/SURV/134) gives author,
  title, series 134, year, page count, and ISBN; the [author page](https://math.dartmouth.edu/~dana/cpcsa/)
  supplies the draft and current errata link. The current
  [errata PDF](https://math.dartmouth.edu/~dana/errata/cpcsa-errata.pdf) has
  no entry affecting printed pp. 26, 42, 82, 138, 198, or 199.

A bounded exact-title/DOI and official-record screen located no linked
retraction or correction notice for the six external core works as of the
audit date, apart from Williams's general errata just described. This is a
bounded screen, not a claim of registry completeness. Exel's title change is
a manifestation distinction, not a retraction or correction notice.

### Novelty/search status

The controlling search remains frozen at
`last_searched_at=2026-08-15T00:37:14+08:00`, classification
`SUPPORTED_WITHIN_SEARCH`, exact-package precedents included **0**. Its exact
query ledger is in `notes/phase2_novelty_search.md`. It searched the
[arXiv Export API](https://export.arxiv.org/api/query),
[Crossref Works API](https://api.crossref.org/works), general web discovery,
official source endpoints, and inherited Paper-8--10 ledgers. An example
exact-conjunction request was
[A1 on arXiv](https://export.arxiv.org/api/query?search_query=all%3ADeninger%20AND%20all%3A%22rational%20Witt%22%20AND%20all%3Aindiscrete%20AND%20all%3Agroupoid%20AND%20all%3Aconvolution&start=0&max_results=1),
and an example discovery/calibration request was
[C1 on Crossref](https://api.crossref.org/works?query.bibliographic=Deninger%20rational%20Witt%20actual%20indiscrete%20orbit%20transformation%20groupoid%20convolution&rows=1).

OpenAlex and Semantic Scholar returned HTTP 429; reproducible corpus totals
for zbMATH and MathSciNet were unavailable. General-web total counts were
`NOT_EXPOSED`. None of these limitations may be rewritten as zero hits or
complete coverage.

If the manuscript needs a novelty sentence, the only licensed wording is:

> As of 2026-08-15, the documented bounded Phase-2 search located no
> precedent for the exact rational-Witt actual-orbit convention-split
> package.

This sentence is optional. “First,” “only,” “novel,” “unprecedented,” “no
prior work,” and “complete search” remain prohibited. The generic
indiscrete-product theorem receives no novelty claim.

## 7. Public-sync and licence boundary

The Paper-11 source folder contains exactly five local framework PDFs. Its
`.gitignore`, SHA-256
`ea6768f2a011e92a3f0d4fca2e9212908efb2c6514bacdd4b448730092f09133`,
contains `*.pdf` and states the local-research-only rule.

The release boundary is byte-specific:

- exclude all five `notes/sources/*.pdf` files from GitHub and every other
  public synchronization;
- do not copy or publish the inherited Deninger PDF or the optional inherited
  Green/MRW/BGR PDFs;
- public audit material may include textual manifests, checksum ledgers,
  preflight JSON, canonical URLs, hashes, locators, bibliography, code,
  results, and the author manuscript;
- downloadability, an “open access” label, an author-hosted copy, or arXiv
  hosting does not by itself authorize redistribution of the exact retained
  bytes; and
- Williams's [AMS copyright endmatter](https://www.ams.org/books/surv/134/surv134-endmatter.pdf)
  expressly reserves systematic republication or multiple reproduction to a
  licence, independently confirming the default exclusion for those bytes.

The current workspace snapshot is **not a Git worktree**, so no claim is made
that the final index, staged set, remote branch, or fresh clone contains zero
source PDFs. Before public sync, all of the following must return no PDF
match:

```text
git ls-files | rg '(^|/)notes/sources/.*\.pdf$'
git diff --cached --name-only | rg '(^|/)notes/sources/.*\.pdf$'
fresh-clone file scan for (^|/)notes/sources/.*\.pdf$
```

Paper 9 is load-bearing and currently has no verified public immutable URL in
this snapshot. Before Paper 11 is labeled standalone-released, its
bibliography must point to an exact public companion version using an actual
commit, release, or archive identifier. A DOI is not required and must not be
promised or fabricated.

## 8. Mandatory downstream gates

There is no source-integrity blocker to beginning the manuscript, provided
the seven-entry minimum and the rules above are used. The following gates are
mandatory before later status changes:

1. **Bibliography construction gate:** implement the seven exact records;
   include Williams's DOI; preserve the Deninger/BHM/arXiv locator notes;
   preserve the Exel title/DOI split; assign no DOI to the NYJM monograph.
2. **Citation-context gate:** cite every source only at the audited strength,
   keep every locator adjacent to its claim, and keep all author-defined
   objects visibly author-defined.
3. **Companion resolvability gate:** insert Paper 9's exact immutable public
   identifier before standalone release.
4. **Optional-ladder gate:** if Green/MRW/BGR appear in prose, add the
   corresponding bibliography entries and preserve Morita/stable/unstabilized
   full-level distinctions. Do not cite an entry that is not discussed.
5. **Post-draft citation audit:** verify every citation command resolves;
   every bibliography entry is cited; there are no orphan, decorative, or
   source-dump citations; every page/theorem locator still matches its
   sentence; and the abstract/title/conclusion do not enlarge the source or
   novelty claims.
6. **Currentness refresh:** immediately before submission, refresh DOI,
   correction/retraction, Williams errata, venue citation-style, and AI/data
   policy checks. Record the new cutoff rather than silently replacing this
   frozen one.
7. **Public-sync dry run:** prove zero tracked/staged/fresh-clone source PDFs
   and bind the manuscript availability statement to the actual release
   branch/tag/archive.

## 9. Final pre-manuscript disposition

The frozen source tuple is coherent, primary-source based, manifestation
specific, and sufficient for the planned manuscript. The minimum
bibliography is exactly:

```text
Deninger 2026
Wang, Paper 9 companion (2026)
Tu 2004
Muhly--Williams 2008
Exel 2011 with arXiv-v3 locator note
Buss--Holkar--Meyer 2018 with arXiv-v2 locator note
Williams 2007 with draft-3.1 locator note
```

The most important integrity constraints are that Deninger and Paper 9 own
only the imported arithmetic/topology inputs; Paper 11 owns every actual
groupoid, global-QC, fibre, operator, completion-transport, HOpen-zero,
strict-proxy, and action-blind proof; and the literature sources remain
framework, group, or proxy authorities at their exact stated strengths.

Accordingly, this audit passes the project to manuscript drafting. It does
not pre-approve a future `references.bib`, manuscript citation graph,
submission, or GitHub release; those are the explicit downstream gates above.
