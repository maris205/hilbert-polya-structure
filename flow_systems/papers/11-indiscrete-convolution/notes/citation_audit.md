# Paper 11 final citation and source-integrity audit

Frozen: **2026-08-15 (Asia/Shanghai)**  
Mode: **ARS final integrity verification; 100% references, citation contexts,
externally checkable claims, and figure/table trace**  
Candidate: **Continuous Convolution Collapse on Indiscrete Arithmetic Orbit
Groupoids**  
Verdict: **PASS — FINAL CITATION/SOURCE-INTEGRITY; C0/M0/m0, with explicit
external standalone-release conditions**

This report is the post-manuscript audit. It supersedes no source, proof,
Route, manuscript, bibliography, PDF, README, or lock file. The only workspace
artifact created by this audit is this report. The audit first detected bare
Green/MRW/BGR proxy-ladder citations, held the candidate, and then re-ran the
affected and global checks only after the author supplied the pinpoint-only
tuple below. The final text now prints the required proposition/theorem and
physical/printed-page locators at both proxy-ladder uses.

## 1. Exact candidate and evidence lock

### 1.1 Final manuscript package

| Artifact | SHA-256 | Audit result |
|---|---|---|
| `paper/manuscript.tex` | `eb1aa4d7060cf1aa53a729e7c7be89a5724a6133ef3bf000cb800bf786de1002` | exact final source inspected |
| `paper/paper.pdf` | `15d207568a61590852697511df2faf4cb06fd06047574c3dc3413e352c14840d` | 16-page A4 locked candidate inspected |
| `paper/references.bib` | `33afa817ff529cd0d98a791e4ea68c0e4a34bd57158774a6c51c43174b72d877` | ten-entry bibliography inspected exhaustively |
| `paper/README.md` | `86d87e66417ba387f0fc1ed8c4d7b037519f22bb72932b0b18f22d3d5e4625b6` | build receipt and strict trace inspected |
| `paper/figures/convention_split.tex` | `fe816b5c5f8cea2e3ee94380773cb3d452e3af05e639a8ced2a290a1ead073b4` | native TikZ source inspected |
| `paper/figures/proxy_action_blind.tex` | `8cc369786047490df518e61c37d232fdc29b49fde7a81da440b7b6c713652c64` | native TikZ source inspected |
| Paper-11 `README.md` | `5d1df0d898ae95bceb45e02eb0612bcd6af2c736061f80102567cd6bf54ca61f` | parent receipt agrees with the tuple |

### 1.2 Frozen audit inputs

| Evidence artifact | SHA-256 | Role |
|---|---|---|
| `notes/proof_audit.md` | `03f17606b0c9d69b496d2766c0a404b0d090698101150a800de4c2108ddc6b28` | integrated proof and owner audit |
| `notes/composition_blueprint.md` | `4b6bfa27c83f72858ac5f0d03c0b9964f93e914fc1d4fdfced619327bcdfc30b` | frozen composition/source plan |
| `notes/pre_manuscript_citation_audit.md` | `f9781bf65cec6ec4a29890164ea08c8dda4e6c152ebe2388ef56945b0e66e8ef` | manifestation, locator, and attribution gates |
| `notes/phase2_framework_source_audit.md` | `a2345046972cc00d3031abdc214442359d0f78c7c0daf7d513ea26f924fb7439` | framework-domain verification |
| `notes/phase2_owner_proxy_audit.md` | `18116cf52c2359a840c9996fb6424fae56260f590990fac79704c040245fa761` | owner/proxy theorem-strength ledger |
| `notes/phase2_novelty_search.md` | `024398a3575cf41a7f33c6950dc1c8de8a8d5f4ec81675f8760ce7c7a87ac24e` | bounded exact-package search |
| `notes/phase3_core_proofs.md` | `4e79446d4a9bb861211186ffd3aa3b42899bc382fbf215a5a453495e5fbb0a66` | P11-1--P11-5 direct proofs |
| `notes/phase3_proxy_ownership_proofs.md` | `46603a1c2185cec1ffb3e7a2cb0f70873abf995edcc104977ac3d360d76e6401` | P11-6--P11-8 direct proofs and proxy bounds |
| `notes/phase3_peer_review.md` | `b16027be916e4e6b8787bce8692dd8461f1e79fb29ea73b9b1d67f530341ad5c` | independent mathematical review |
| `notes/route_audit.md` | `9203d37cfaa28a45a7548a9864de614c81bf6ea199b4a6736e1c5aaa84335011` | seven-record Route audit |
| `notes/sources/framework_source_manifest.md` | `b3b61a5bdfd206cb8cc4a8bf574373bc6485d96b22547698ac69fb3a9e36812f` | five exact retained manifestations |
| `notes/sources/framework_sources.sha256` | `057e9c32b2f654c765f40f0ddd40014c12876d22c0567470fdf04a2eb0fd2e7f` | five PDFs plus five preflight sidecars |
| `results/indiscrete_convolution_controls_manifest.json` | `de55c58ad7efc133b0d0865f392a30b52f6b05f89f64878cea0910b7eab557ea` | deterministic controls receipt |

All hashes above were recomputed from the final workspace before this report
was written.

## 2. Acceptance standard and final severity ledger

The audit applied the ARS final-integrity rules:

1. verify every bibliography record and every citation command, not a sample;
2. verify every imported assertion against the exact cited manifestation and
   locator;
3. distinguish source-owned facts from author definitions and direct results;
4. verify every externally checkable number, Route record, and current/search
   statement;
5. trace every figure and table through all six required keys in both
   directions;
6. run a clean build, text extraction, font/PDF checks, and visual inspection;
7. screen at least 50% of substantive prose for originality; and
8. clear all seven specified AI-research failure modes.

Final finding counts are: **critical 0; major 0; minor 0; retained unverifiable
claim 0**. The Paper-9 immutable public identity, author declarations, venue
policy, and public-sync file-list check are explicit release conditions rather
than hidden or fabricated facts; they are listed in Section 13.

## 3. Final build, label, text, and visual verification

An independent clean build was made in a new temporary directory with
XeLaTeX/BibTeX/XeLaTeX/XeLaTeX. All four commands returned zero.

| Check | Result |
|---|---|
| Rebuilt source SHA | `eb1aa4d7060cf1aa53a729e7c7be89a5724a6133ef3bf000cb800bf786de1002`, identical to lock |
| Rebuilt Bib SHA | `33afa817ff529cd0d98a791e4ea68c0e4a34bd57158774a6c51c43174b72d877`, identical to lock |
| Rebuilt PDF SHA | `afd4f2163335cf9affb06cbf9c18aa88a9841619f161b173b42cefb63ae9658c`; binary variation is creation/subset metadata only |
| Locked/rebuilt extracted-layout text | byte-identical, SHA `89743a4df0788d988b7c09a625e8761d30bda1d39590ef9c11492e6ed95096fc` |
| Locked/rebuilt 144-DPI page renders | 16/16 byte-identical PNG pairs |
| Final-round diagnostics | no missing citation/reference, undefined target, overfull/underfull box, missing character, or fatal error |
| Benign build messages | only `unicode-math`/`mathtools` command-ownership warnings |
| Bibliography | `plainnat`; 10 `\bibitem` records; no BibTeX warning or error |
| PDF structure | 16 A4 pages; unencrypted; `Suspects: no`; no JavaScript |
| Text extraction | 6,730 whitespace-delimited tokens; zero U+FFFD; zero `??`/undefined sentinels |
| Labels | 56 total, 0 duplicate, 0 reference to a missing label |
| Equation labels | 26 `eq:*`: 22 numbered `equation` environments and four numbered `align` entries |
| Fonts | seven fonts; every font embedded, subsetted, and Unicode mapped |
| Retained build artifacts | `paper/paper.pdf` is the only PDF and the only build artifact at `paper/` top level |

All 16 locked pages were inspected at original render detail. The final
pinpoint-only change affects rendered pp. 3 and 11; both were re-inspected for
wrapping, collision, clipping, and margin safety. The bibliography on p. 16
was also re-inspected. No visual defect was found. Equation numbers remain
correct, and the Young term renders the intended centered dot in
`\zeta(\,\cdot-v)`, not the literal word `cdot`.

## 4. Citation graph and minimum bibliography

The final source contains **21 citation commands**, **22 cited-key uses**, and
**10 unique keys**. All ten bibliography entries are cited, no citation key is
absent from the Bib file, and no uncited Bib entry remains.

| Key | Uses | Retention reason |
|---|---:|---|
| `Deninger2026` | 1 | load-bearing arithmetic set/action/stabilizer/period source |
| `Wang2026Packets` | 1 | load-bearing companion topology theorem |
| `Tu2004` | 2 | framework terminology and domain ceiling |
| `MuhlyWilliams2008` | 2 | raw patch-span practice and standing hypotheses |
| `Exel2011` | 2 | independent etale boundary |
| `BussHolkarMeyer2018` | 4 | Hausdorff boundary and full proxy bridge |
| `Williams2007` | 4 | group-R harmonic analysis and proxy tensor ceiling |
| `Green1978` | 2 | retained proxy Morita-strength ladder |
| `MuhlyRenaultWilliams1987` | 2 | retained proxy full Morita-strength ladder |
| `BrownGreenRieffel1977` | 2 | retained proxy stable-isomorphism ladder |

This is the smallest bibliography for the text as frozen: seven core entries
plus the three actually discussed proxy-ladder sources. Paper 10 is not a
mathematical premise and is correctly absent. Morishita is not used and is
correctly absent. Author self-citation is **1/10 = 10%**, below the ARS 15%
advisory threshold. There are no decorative or secondary-source citations.

## 5. Metadata, manifestation, DOI, and currentness audit

### 5.1 Exhaustive ten-record metadata check

| Key | Official/primary verification and exact manifestation | Result |
|---|---|---|
| `Deninger2026` | [arXiv `1807.06400`, v4 dated 2024-02-07](https://arxiv.org/abs/1807.06400) and [final journal record](https://www.sciencedirect.com/science/article/pii/S0019357724000491): *Indagationes Mathematicae* 37(1), 25--136 (2026), DOI `10.1016/j.indag.2024.05.007` | PASS. Final 2026 metadata plus explicit v4 locator note; no page-system hybrid. |
| `Wang2026Packets` | exact local companion release PDF, SHA `c55e4f45fe5f58841864e9af695c4664bdb1a77cff6e087fd2869d4ecd385e02`, 21 pages | PASS for review package. No DOI or URL invented; immutable public identity remains a standalone-release condition. |
| `Tu2004` | [official EMS record](https://ems.press/journals/dm/articles/8965109), *Documenta Mathematica* 9, 565--597 (2004), DOI `10.4171/DM/178` | PASS. |
| `MuhlyWilliams2008` | [official NYJM Monographs record](https://nyjm.albany.edu/m/2008/3.htm) and [official view PDF](https://nyjm.albany.edu/m/2008/3v.pdf), volume 3 (2008) | PASS. The official record provides no publication DOI; none was invented. |
| `Exel2011` | [official arXiv history](https://arxiv.org/abs/0812.4087), [author publication list](https://mtm.ufsc.br/~exel/publications/), and DOI [`10.1090/S0002-9939-2010-10477-X`](https://doi.org/10.1090/S0002-9939-2010-10477-X) | PASS. Published title/DOI are paired; the note truthfully identifies the differently titled arXiv v3 technical manifestation. |
| `BussHolkarMeyer2018` | [final accepted arXiv v2](https://arxiv.org/abs/1612.04963v2) and DOI [`10.1112/plms.12131`](https://doi.org/10.1112/plms.12131), PLMS 117(2), 345--375 (2018) | PASS. Technical pages are explicitly v2 pages. |
| `Williams2007` | [AMS monograph record](https://bookstore.ams.org/view?ProductCode=SURV%2F134), DOI [`10.1090/surv/134`](https://doi.org/10.1090/surv/134), and [author Version 3.1 page](https://math.dartmouth.edu/~dana/cpcsa/) | PASS. Published 528-page metadata and 540-page draft locator system are explicitly distinguished. |
| `Green1978` | DOI [`10.1007/BF02392308`](https://doi.org/10.1007/BF02392308), *Acta Mathematica* 140, 191--250 (1978) | PASS. |
| `MuhlyRenaultWilliams1987` | [official Journal of Operator Theory record](https://jot.theta.ro/jot/archive/1987-017-001/1987-017-001-001.html), 17(1), 3--22 (1987) | PASS. No DOI appears in the official record; none was invented. |
| `BrownGreenRieffel1977` | [official journal PDF](https://msp.org/pjm/1977/71-2/pjm-v71-n2-p06-s.pdf) and DOI [`10.2140/pjm.1977.71.349`](https://doi.org/10.2140/pjm.1977.71.349), PJM 71(2), 349--363 (1977) | PASS. |

### 5.2 Bounded current-fact screen

Cutoff: **2026-08-15**. Exact-title, DOI, version-history, and
correction/retraction searches were refreshed for all nine external works.
The official records above did not expose a retraction or a correction that
changes a cited claim or locator. Williams's [official errata](https://math.dartmouth.edu/~dana/errata/cpcsa-errata.pdf),
current through October 2025, lists no correction to the cited printed pages
26, 82, 138, 198, or 199. This is a bounded currentness screen, not a claim
that no correction can ever exist. A submission-day refresh remains proper.

## 6. Citation-context, locator, and theorem-strength alignment

Every one of the 21 citation commands was read in context. Overview repeats
and framework-table repeats were checked against the same source text rather
than assumed from an earlier citation.

| Source / uses | Exact verified locator(s) | Licensed claim in the manuscript | Boundary confirmed |
|---|---|---|---|
| Deninger / 1 | arXiv v4 physical pp. 32--33, Eqs. (35),(38),(39); pp. 38--39, Section 6 and Thm. 6.1 | fixed-prime set, right positive-real action, `N_x0^Z`/`p^Z` isotropy, logarithmic period | no topology, groupoid, or convolution attribution |
| Paper 9 / 1 | p. 11, Cor. 5.3 | every actual inherited orbit in `Gamma_p` is nonempty, nontrivial, indiscrete; set stabilizer and `log p` retained | no standard-circle topology and no fabricated external identity |
| Tu / 2 | physical 3/printed 567 Def. 1.1; physical 17/printed 581 Section 4.1; physical 19/printed 583 Def. 4.6 | quasi-compact/compact distinction, raw Hausdorff-open span, framework/Haar domain | used only for terminology and `NOT_APPLICABLE`, never as a positive actual-owner theorem |
| Muhly--Williams / 2 | pp. 3--7; Prop. 4.4, pp. 21--23 | accepted raw patch span and exact locally-Hausdorff/Hausdorff-unit/compact-Hausdorff-neighborhood assumptions | no invocation after hypotheses fail |
| Exel / 2 | arXiv v3 physical/printed p. 1, Section 1 | locally compact Hausdorff unit and local-homeomorphism range/source boundary | no positive theorem for the actual non-Hausdorff unit |
| Buss--Holkar--Meyer / 4 | v2 pp. 1--2; p. 23, Section 7.1 and Thm. 7.1 | Hausdorff standing hypothesis; full standard transformation-groupoid/full crossed-product bridge | no reduced bridge, actual bridge, or completion extension of `I` |
| Williams / 4 | draft 3.1 physical/printed 38/26 Ex. 1.80; 94/82 Prop. 3.1; 210--211/198--199 Exs. 7.9/7.11 and Thm. 7.13; 150/138 Eq. (4.63), Thm. 4.30 | Fourier sign/model, group reduced norm and amenable full/reduced equality, separate unstabilized full proxy tensor model | group/proxy use only after author transport; no actual-groupoid amenability or norm map |
| Green / 2 | Prop. 3, physical 13/printed 203, printed at both uses | full-level imprimitivity/Morita strength | no algebra isomorphism, stability, or actual theorem |
| MRW / 2 | Thm. 2.8, physical 8/printed 10, printed at both uses | groupoid equivalence gives full strong Morita equivalence | no stable isomorphism, no actual theorem, and no decorative Thm. 3.1 citation |
| Brown--Green--Rieffel / 2 | Thm. 1.2, physical 4/printed 351, printed at both uses | stable isomorphism under the theorem's strictly-positive-element hypotheses | no cancellation of compact operators and no actual theorem |

The final locator repair is exact: the introduction and Completion-stop
paragraph both give Green Prop. 3, MRW Thm. 2.8, and BGR Thm. 1.2 with the
audited physical/printed offsets. MRW Thm. 3.1 is correctly absent because
the manuscript does not use MRW's independent transitive tensor route.
BHM Thm. 7.1 and Williams Eq. (4.63)/Thm. 4.30 remain separately named, so
full bridge, Morita equivalence, stable isomorphism, and unstabilized tensor
isomorphism are not conflated.

## 7. Exhaustive claim and attribution verification

### 7.1 Author mathematical results

The manuscript has one definition and 18 result environments: one lemma, 11
theorems, three propositions, and three corollaries. All 18 results and all
26 numbered equations were checked against the two direct-proof files, the
integrated proof audit, and the final manuscript proof. No theorem depends on
the finite controls.

| Proof family | Final result environments covered | Result |
|---|---|---|
| P11-1 | actual product topology; quasi-compact projection criterion; topological-groupoid proposition | PASS |
| P11-2 | continuous T0-target and measurable countably-separated-target factorization | PASS |
| P11-3 | exact global continuous/global-QC function classification | PASS |
| P11-4 | author range-fibre family, Radon/full-support and invariance contract | PASS |
| P11-5 | author global-QC convolution and involution `*`-algebra | PASS |
| P11-6 | exact source fibres, dense-domain kernel, bounded extension, regular `*`-representation, reduced norm, separately transported completions | PASS |
| P11-7 | raw HOpen-zero diagnostic; one-sided `J`; strict test-function map `I` with proper image and completion stop | PASS |
| P11-8 | generic action blindness, adversarial controls, and rational-Witt fixed-orbit application | PASS |

The owner split is exact:

- Deninger owns only the fixed-prime set/action/stabilizer/period inputs.
- Paper 9 owns only the inherited nontrivial-indiscrete topology input.
- Paper 11 owns the transformation groupoid, global-QC/HOpen definitions,
  fibres, convolution, operators, norms, transports, `J`, `I`, and
  action-blind theorem.
- Williams's group-R results apply only after the author transport is proved.
- Tu/MW/Exel/BHM are finite framework-domain comparators.
- Green/MRW/BGR/BHM/Williams proxy strengths remain proxy-only.

There is no claim that the author completions are standard actual-groupoid
`C*(G)` objects, no claim that HOpen zero has a norm or completion, and no
claim that `I` extends beyond test functions.

### 7.2 Reproducibility and numerical claims

The complete suite was re-run in a temporary copy without altering checked-in
results. It returned 57/57 tests, 12 CSV artifacts with 642 data rows, and 5/5
intentional negatives. Strict verification passed for checked-in results and
two fresh generations; all 13 generated artifacts were byte-identical across
the three sets, and the forbidden cache/bytecode scan passed. Independent CSV
row and SHA recounts agree with manifest
`de55c58ad7efc133b0d0865f392a30b52f6b05f89f64878cea0910b7eab557ea`.
The manuscript consistently describes these as finite witnesses and
regression guards, not universal proofs.

### 7.3 Route and novelty claims

All seven Stage-11 files were re-hashed:

```text
ce52ba0fddf39652a37992ff7babeb590bfcb5ce8853ee6aa87b2c877634e551
25908c995d5a1f2a6f8478d62715e7cf4fc653b76ae2f6bf9fdfe71f8cc3c6d7
e904f85d078e84188f6d40a07e3e1fb1c7426068b8c4a9c4a773df221fd2cfac
fb1f8bf736099a2eca5175d818ad7a00f7f1de2d0ddb699135e035ab311d8830
775fb3ac86771744d3f15f708a73fc634992f770a8d7b3d04f570563054a6ccd
45887d091bb97853febaf0329e7035655e69ec44c49ee7919ce55a8ef3de24b5
23480710707367d9f77b4896a7c85e073b17dcc5a4f8aae3814bff972d27ba1b
```

The filename order differs from the manuscript's deliberate table order, but
the ID-to-hash and ID-to-tuple maps agree exactly in both directions. Exactly
three records are exploratory negative priors and four are rejected; all
seven have `A4_FAIL`; all Route-B flags are false; no Route-B record exists.
No A-coordinate is spliced across owners.

The dated novelty sentence is also correctly bounded: as of 2026-08-15, the
documented Phase-2 search found no precedent for the exact combined
rational-Witt actual-orbit convention-split package. It expressly declines
absolute priority and makes no priority claim for the generic topology,
group-R convolution, HOpen literature, or transformation-groupoid theory.
That wording matches the search evidence and its limitations.

## 8. Strict figure/table trace in both directions

The final manuscript has exactly two figures and two tables. The README has
exactly four corresponding trace entries. A mechanical indentation/key check
found exactly one each of the six required top-level keys per entry, in the
required order: `artifact_id`, `source_data`, `transformation`,
`caption_claim`, `supported_manuscript_claims`, and `limitations`. Thus the
ledger contains 4 x 6 = 24 required keys, with zero missing, duplicate, or
extra artifact entry.

| Artifact | Source-to-artifact check | Artifact-to-claim check | Limitation surfaced | Verdict |
|---|---|---|---|---|
| `fig:convention-split` | P11-3/P11-6 anchors and native TikZ SHA `fe816b5c...073b4` reproduce the two logical branches | caption plus source-adjacent prose equivalent bind global-QC nonzero versus raw HOpen zero | diagnostic-only HOpen; finite framework audit; no universal nonexistence | PASS both directions |
| `fig:proxy-action-blind` | P11-7/P11-8, controls-manifest SHA `de55c58a...557ea`, and native TikZ SHA `8cc36978...52c64` reproduce the arrows and stop | caption plus source-adjacent prose equivalent bind one-sided topology, proper `A_const`, no norm arrow, and action blindness | test-function level only; no completion or arithmetic promotion | PASS both directions |
| `tab:framework-applicability` | framework audit SHA `a2345046...7439` and preaudit SHA `f9781bf6...e8ef` support every row | table caption and adjacent boundary prose restrict the result to the named frameworks | finite named-framework audit, not universal theory nonexistence | PASS both directions |
| `tab:route-ledger` | route audit SHA `9203d37c...5011` and all seven exact YAML hashes reproduce every row and ordered full-hash/tuple ledger | caption, full ledgers, and adjacent verdict prose bind the 3/4 split, all A4 failures, and Route-B false | no coordinate splicing; `NOT_TESTABLE` preserved; all Route-B flags false | PASS both directions |

Figure 1's normal float placement puts the rendered figure on p. 4 while its
explicit prose equivalent remains on p. 3; the source-level trace and
cross-reference resolve correctly. No unlisted figure/table or untraced
substantive artifact use was found. Every `limitations` field is nonempty and
is visible in a caption or adjacent prose.

## 9. Exact local-source read integrity

### 9.1 Paper-11 retained framework sources

`sha256sum -c framework_sources.sha256` returned 10/10 OK. Every PDF was read
only after its same-stem preflight reported PASS, equal declared/enumerated/
reader counts, and an empty warning array.

| Source | Pages | PDF SHA-256 | Preflight SHA-256 |
|---|---:|---|---|
| Tu 2004 | 34 | `ff88e322eee65d2d6dd083697c82febb3759268f9b36083264a3e20b6e586897` | `e82c95d4c3fd668d43c324db0631216372cc67505234a73e2ddc9ebf875884af` |
| Muhly--Williams 2008 | 87 | `7a7c16f132f1df35f8bf304206e998796834cd23a31836dd4e15108f91806f20` | `1040a947effc1cc639d2530e6da7e4ec52743bf664574de92a60934b079345c4` |
| Exel arXiv v3 | 12 | `01b1ac9a6f98444438c654b2e4d8b69ff6058e15c02ae6704e6d254f457c3a99` | `6f36c1bfcc3b497d1c4f9f99ff3aafa880452967dd99807cdd7c228e0c71cf77` |
| BHM arXiv v2 | 30 | `8be7896ed1aab1138b8ccf067ebfbba0f8b7d8a1dc8713fbf6c2f173ffe647e6` | `c288efb2dca89ca8fd47bd9371decb7d042853dd6b60b35897df2f70214bfb59` |
| Williams draft 3.1 | 540 | `3dbc1fb9e96191a278e0d59feb4981d3bbea4faa4df609d1886c81125bffe9c2` | `80a77e556a133a33f2db2667e79bac8219fc7babfba1487aec93f54e5d01c86c` |

The locator content listed in Section 6 was independently reread from these
exact bytes.

### 9.2 Inherited companion and proxy-ladder sources

Because the inherited Paper-8 proxy sidecars had recorded `UNAVAILABLE` when
`pypdf` was absent, this audit generated new non-workspace temporary sidecars
with `pdf_read_preflight/1.0.0` and `pypdf 6.15.0` before rereading the exact
pages. All five returned PASS with zero warnings:

| Source | Pages | Exact PDF SHA-256 | Fresh result |
|---|---:|---|---|
| Deninger v4 | 119 | `edd0bc8c2efb601ed7574e8eceae40e8cde21d0e4b2bc8c4ce7e60d8e1f82a09` | PASS; pp. 32--33 and 38--39 reread |
| Paper 9 release PDF | 21 | `c55e4f45fe5f58841864e9af695c4664bdb1a77cff6e087fd2869d4ecd385e02` | PASS; p. 11 reread |
| Green 1978 | 60 | `bca0701f16e965424563004c5e6d9eec2a9310e05b860857f23d97b2f8819b3d` | PASS; physical 13/printed 203 Prop. 3 reread |
| MRW 1987 | 20 | `16723f6b3b3d90f220a4bc0814ed8374817ae2025c8eef9822f520a8da7b6629` | PASS; physical 8/printed 10 Thm. 2.8 visually reread |
| BGR 1977 | 19 | `d2b64846c0dd59668f261782ae832df1bb7dad15479d5bb5c2e7aeec37fd19c8` | PASS; physical 4/printed 351 Thm. 1.2 reread |

Temporary sidecars were deliberately not added to the workspace; this audit
records the exact PDF hashes, page counts, and PASS outcomes.

## 10. Source-PDF license and public-sync boundary

All five Paper-11 retained source PDFs are classified
`LOCAL_RESEARCH_ONLY`. The adjacent `.gitignore` excludes `*.pdf` and states
that public synchronization is limited to manifests, checksum ledgers, and
read-integrity sidecars unless a manifestation-level redistribution licence
is separately documented. Paper 8 and Paper 9 carry the same default PDF
exclusion.

The package README explicitly excludes:

- `notes/sources/*.pdf`;
- inherited Deninger bytes; and
- inherited Green/MRW/BGR proxy-source bytes.

Downloadability, an open-access label, an author-hosted copy, or arXiv hosting
was not treated as redistribution permission. Public audit material may
carry canonical links, metadata, locators, checksums, and preflight JSON, but
not these source PDF bytes by default.

The workspace is not a Git worktree, so an index/staging/remote/fresh-clone
exclusion test cannot be performed here. The claim in the manuscript package
is only that source PDFs are outside the **proposed** public synchronization
set, not that a public push has occurred. A mechanical proposed-file-list
check is therefore an explicit release condition in Section 13.

## 11. Originality/plagiarism screen

### 11.1 Sampling method and coverage

The sampling frame used blank-line LaTeX blocks between `begin{document}` and
the bibliography, stripped commands/markup for counting, retained blocks
with at least 25 alphabetic tokens, and excluded display/table/figure/list
container starts. This yielded 71 records. The centered title/metadata record
and three declaration records were excluded, leaving **67 substantive body
units**.

The deterministic sample took every odd-numbered unit from 1 through 67 and
added high-risk even units 4, 58, 66, and 68. Coverage is **38/67 = 56.7%**,
above the required 50%. It spans the abstract, source framing, definitions,
topology, proofs, analytic construction, proxy ladder, action blindness,
controls, Route ledger, novelty statement, and conclusion.

Each search phrase below was normalized only to remove TeX/math glyphs and
submitted as an exact-quoted web query. The returned result text was inspected
for the exact phrase. The same phrase set was searched case-insensitively and
literally across Papers 1--10.

```text
001 every continuous arrow map to a T0 target factors uniquely through real time
003 actual orbit without silently replacing its topology by the ordinary circle topology
004 they do not license the same terminology on an arbitrary non-Hausdorff owner
005 These are not competing names for one standard algebra
007 No boundedness theorem is available for a proxy norm
009 direct global-QC convolution algebra and unit-regular calculation
011 No ordinary-circle topology is imported into the orbit
013 support means the closure of its nonzero set in the ambient product topology
015 These are not denoted C star G or reduced C star G
017 The opens of G are exactly X times U with U open
019 their time projections cover the compact set
021 The composable-pair chart is a homeomorphism
023 A map F from G to Y is continuous if and only if there is a unique continuous
025 The separation hypothesis is sharp a nonconstant map from a nontrivial indiscrete
027 membership cannot distinguish two equal-time unit labels
029 Exact global function classification
031 positive full-support Radon measure on that locally compact Hausdorff fibre
033 define using the range-first coordinates
035 Uniform continuity of a compactly supported continuous function yields
037 reflection invariance of Lebesgue measure gives
039 For arbitrary L2 vectors the equality is an L2 identity
041 The convolution is continuous so it represents a nonzero L2 class
043 Completion of the two named norms gives author-defined isomorphisms
045 Equality is credited to amenability of the group R not to amenability of the actual groupoid
047 The two records therefore form a genuine convention split
049 a nonempty proper unit-coordinate subset and therefore not actual-open
051 unit-constant functions reproduce the formulas
053 These strengths are not interchangeable and remain proxy-only
055 the global convolution conclusion remains true but the HOpen-zero statement does not
057 independent prime composite or arbitrary labels and independent positive periods
058 a nontrivial action of R on a finite set would be a false control
059 The analytic output retains none of p a Lp the action the orbit decomposition
061 These finite checks are witnesses and regression guards
063 No A-coordinate is borrowed from another owner
065 Their direct proofs do not turn them into standard actual-groupoid objects
066 documented bounded Phase-2 search located no precedent for the exact
067 generic theorem separates the host from its analytic shadow
068 the erased group-R completion and the standard proxy may not be spliced together
```

### 11.2 Results and bounded conclusion

- External exact-phrase screen: **0/38 suspicious exact occurrences in the
  returned result text**. Irrelevant loose-token results were not treated as
  matches.
- Local Papers 1--10 exact-phrase screen: **0/38 matches**.
- No unattributed quotation, copied proof passage, or source-like stylistic
  block was found in the sampled units.
- Expected names, theorem titles, mathematical notation, and short standard
  phrases were not misclassified as originality concerns.

Verdict: **PASS for the required >=50% originality sample**. This is a
bounded exact-phrase and local-corpus screen, not a claim that paraphrase
similarity can be ruled out universally.

## 12. Seven AI-research failure modes

| Failure mode | Evidence | Verdict |
|---|---|---|
| 1. Implementation bug or invalid computation | clean independent control reproduction, strict negatives, row/hash recount, and direct proofs independent of code | CLEAR |
| 2. Citation failure or source hallucination | 10/10 metadata, 21/21 contexts, exact manifestations/locators, zero orphan/dangling key | CLEAR |
| 3. Hallucinated experimental result | every reported count and hash matches the regenerated manifest/artifacts | CLEAR |
| 4. Shortcut, leakage, or target reliance | no empirical model, target-zero table, fitting, randomness, or external dataset; adversarial action/label/period controls are explicit | CLEAR / not empirically applicable |
| 5. Bug reframed as novelty | negative result follows direct generic proof and adversarial cases; no “unexpected bug” language or absolute priority claim | CLEAR |
| 6. Fabricated methodology or reproducibility | README commands, standard-library-only implementation, fresh runs, and artifacts agree byte-for-byte | CLEAR |
| 7. Frame lock or one-sided interpretation | owner split, framework non-applicability, generic countercontrols, completion stop, limitations, and negative Route ledger are all retained | CLEAR |

No mode is `SUSPECTED` or `INSUFFICIENT_INFORMATION` for a retained
manuscript claim.

## 13. External standalone-release conditions

The following items do not invalidate the review candidate, because the
manuscript and README disclose them rather than assert invented values. They
must be resolved before standalone public release or submission where
applicable:

1. replace Paper 9's `AUTHOR TO CONFIRM` note with its real immutable public
   repository/release/archive identity; do not fabricate a DOI or URL;
2. confirm final author list, affiliation, corresponding-author status,
   CRediT roles, funding, conflicts, acknowledgments, venue, licence,
   repository tag, archive/DOI, and release date;
3. adapt the AI-assistance and availability language to the chosen venue's
   then-current policy;
4. refresh DOI/correction/retraction and Williams-errata checks immediately
   before submission; and
5. in an actual Git/publication worktree, mechanically enumerate the proposed
   sync set and prove that no retained research-source PDF is staged or
   uploaded.

These are visible release gates. None is silently filled, and none is used as
a premise of a mathematical theorem.

## 14. Final verdict

**PASS — FINAL CITATION/SOURCE-INTEGRITY.** The exact final tuple in Section 1
has:

- complete and minimal citation coverage;
- correct metadata, DOI/URL policy, manifestation notes, and pinpoint
  locators;
- exact source-theorem strength and owner attribution;
- 100% checked mathematical/imported/factual/Route claim families;
- strict four-entry, six-key, bidirectional figure/table trace;
- clean build, text, labels, fonts, PDF structure, and visual rendering;
- a 56.7% originality sample with no suspicious exact match;
- all seven AI failure modes clear; and
- an explicit source-PDF redistribution boundary.

There is **no remaining metadata, manifestation, locator, citation-graph, or
source-integrity blocker**. Paper 9's immutable public identity and the other
items in Section 13 remain external standalone-release conditions and must
not be fabricated.

## 15. Receipt-only project-README status-correction re-lock

Addendum date: **2026-08-15 (Asia/Shanghai)**  
Pre-addendum historical-prefix SHA-256:
`23bc34be1d21a61cead4e982c6d86749ab34470c0efc274be1bec047e54a6179`  
Historical-prefix extent: **32,935 bytes; 479 lines**  
Disposition: **PASS — FINAL CITATION/SOURCE-INTEGRITY RE-LOCK; C0/M0/m0;
PUBLIC RELEASE REMAINS UNAUTHORIZED**

This append-only addendum supersedes only the active project-README receipt in
Section 1.1.  The entire report above is retained as an exact byte prefix.
No manuscript, bibliography, figure, PDF, paper-package README, proof/source
record, peer report, release report, control artifact, pipeline record, or Git
state was edited or regenerated for this re-lock.

### 15.1 Exact one-hunk delta and status truth

The former 56-line, 3,461-byte project README had SHA-256
`5d1df0d898ae95bceb45e02eb0612bcd6af2c736061f80102567cd6bf54ca61f`.
The current 56-line, 3,525-byte README has SHA-256
`1380928a1d9e46e4a82395a2a3059bc1c1a8a33a9450ecd6d7e31adfb1a86a64`.
An exact inverse replacement of the current status paragraph reconstructs the
former SHA byte-for-byte.  A unified comparison contains exactly one hunk,
five removed lines and five added lines:

```diff
@@ -3,11 +3,11 @@
-Status: Phase 1--3 evidence and composition gates PASS; the manuscript package
-is complete and ready for independent manuscript peer review. It is not yet
-labeled standalone-released because the independent review, author
-confirmations, immutable Paper-9 public identity, and public-release gate
-remain outstanding.
+Status: Phase 1--3 evidence and composition gates PASS; manuscript peer review,
+the final citation/source-integrity audit, and the technical release audit all
+PASS with C0/M0/m0. Public release remains unauthorized pending the human
+declarations, immutable Paper-9 public identity, chosen venue and then-current
+policy, and real public-synchronization/source-PDF-exclusion gates.
```

The new paragraph is a truthful status receipt.  The independent manuscript
peer report, SHA-256
`864f102b2b4dbadc3ff36807d0fec564375e6235e5a0319e26dcb2de5487dc36`,
records **PASS — C0/M0/m0**.  The exact historical citation-audit prefix named
above records **PASS — FINAL CITATION/SOURCE-INTEGRITY — C0/M0/m0**.  The
technical release audit, SHA-256
`fc3527d42bcbf20446f91e55ef440f875d52457c329d3a58671a2affd20ebf5b`,
records technical **PASS — C0/M0/m0** while expressly withholding any claim
of completed public synchronization or standalone release.  Thus the old
README SHA is retired only as the active project-status receipt; it remains a
valid historical byte identity in the prefix and the two independent reports.

### 15.2 Unchanged final candidate tuple

All candidate hashes were recomputed independently.  They remain exactly:

| Artifact | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `eb1aa4d7060cf1aa53a729e7c7be89a5724a6133ef3bf000cb800bf786de1002` |
| `paper/references.bib` | `33afa817ff529cd0d98a791e4ea68c0e4a34bd57158774a6c51c43174b72d877` |
| `paper/figures/convention_split.tex` | `fe816b5c5f8cea2e3ee94380773cb3d452e3af05e639a8ced2a290a1ead073b4` |
| `paper/figures/proxy_action_blind.tex` | `8cc369786047490df518e61c37d232fdc29b49fde7a81da440b7b6c713652c64` |
| `paper/paper.pdf` | `15d207568a61590852697511df2faf4cb06fd06047574c3dc3413e352c14840d` |
| `paper/README.md` | `86d87e66417ba387f0fc1ed8c4d7b037519f22bb72932b0b18f22d3d5e4625b6` |
| project `README.md` | `1380928a1d9e46e4a82395a2a3059bc1c1a8a33a9450ecd6d7e31adfb1a86a64` |

The receipt-only README correction changes no candidate theorem, proof,
claim, citation marker, bibliography field, locator, figure/table trace,
rendered page, control result, or release boundary.  Accordingly no build or
control rerun was warranted or performed.

### 15.3 Citation graph, claim alignment, and source boundary

An independent source parse still finds **21 citation commands, 22 cited-key
uses, and 10 unique cited keys**.  The BibTeX file still has **10 unique
entries**; the cited-key and bibliography-key sets are identical, with zero
dangling citation and zero orphan entry.  Because the manuscript, BibTeX,
figures, PDF, and strict trace README retain their exact audited hashes, the
claim-to-source contexts, manifestation notes, pinpoint locators, owner
ceilings, and four-entry six-key bidirectional trace have no byte or semantic
drift.  This narrow receipt re-lock does not invent a new external metadata or
full-text verification event; it preserves the exhaustive checks in the
historical prefix on demonstrably unchanged content.

The source-exclusion boundary is also unchanged.  The adjacent
`notes/sources/.gitignore`, SHA-256
`ea6768f2a011e92a3f0d4fca2e9212908efb2c6514bacdd4b448730092f09133`,
still excludes `*.pdf`.  The five retained Paper-11 research-source PDFs
remain outside `paper/`; the source manifest and checksum ledger remain
`b3b61a5bdfd206cb8cc4a8bf574373bc6485d96b22547698ac69fb3a9e36812f`
and
`057e9c32b2f654c765f40f0ddd40014c12876d22c0567470fdf04a2eb0fd2e7f`,
respectively.  The `paper/` tree contains exactly one PDF, the generated
`paper.pdf`, and no top-level build auxiliary.  This workspace remains outside
a Git worktree, so no tracked/staged/remote/fresh-clone exclusion claim is
made.

### 15.4 Re-lock verdict

**PASS — C0/M0/m0 at the exact tuple in Section 15.2.**  The status correction
is receipt-only, the citation graph and source boundaries are unchanged, and
the pre-addendum report remains an exact byte prefix.  Public release remains
**false/unauthorized** until the human declarations, immutable Paper-9 public
identity, venue/policy choices, and real Git/publication-system
source-PDF-exclusion checks in Section 13 are closed.
