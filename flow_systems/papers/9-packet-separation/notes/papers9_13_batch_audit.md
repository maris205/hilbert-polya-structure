# Papers 9--13 consolidated batch audit

Audit date: **2026-08-15 (Asia/Shanghai)**  
Audit scope: Papers 9, 10, 11, 12, and 13  
Audit mode: independent ARS exact-byte, citation, package, PDF, controls,
Route, provenance, and release-boundary review  
Current technical verdict: **PASS -- C0/M0/m0**  
Public-release flag: **`PUBLIC_RELEASE_AUTHORIZED=false`**

This is the downstream acyclic receipt for the five-paper batch. It binds the
current scholarly packages and current documentation bytes, including the
Paper 13 status READMEs that intentionally postdate its per-paper release
report. It does not edit or supersede any mathematical claim, Route result,
control result, or historical review record. It also does not authorize a Git
operation, public synchronization, journal submission, or publication.

## 1. Executive disposition

| Paper | Current package disposition | Technical findings | Public release |
|---|---|---:|---|
| P9 | accepted internal article package | C0/M0/m0 | false |
| P10 | accepted internal article package | C0/M0/m0 | false |
| P11 | accepted internal article package | C0/M0/m0 | false |
| P12 | accepted internal article package; `STANDALONE_PASS` retained | C0/M0/m0 | false |
| P13 | accepted **Technical Note**, NOTE branch | C0/M0/m0 | false |

Paper 13's separate substantive-weight verdict remains exactly
`STANDALONE_PASS=false`, `NOTE_OR_MERGE`, with standalone `C0/M1/m0`. That
Major is a binding reason for the Technical Note disposition, not a defect in
the Technical Note package and not a finding erased by this audit.

Papers 9--12 retain their previously reviewed manuscript/article
dispositions. The batch-level public-release flag is conservatively false for
all five papers until the external gates in Section 13 close.

## 2. Exact current scholarly and package ledger

Every `paper/` directory contains exactly six regular files: one package
README, one manuscript, one bibliography, two native TikZ figure sources, and
one retained `paper.pdf`. There are no symlinks, auxiliary/cache/log files,
second PDFs, or research-source PDFs in any of the five package directories.

### P9 -- `papers/9-packet-separation`

| Artifact | SHA-256 |
|---|---|
| project `README.md` | `ddad7b1a7a474e7393dec66d60065e9f8ea7fd77af3c7c853b67225404328f2f` |
| `paper/README.md` | `5ac7a34024672d01ce2e8d9cac24036c0e7be9f2516b79da7603a5dfaf04eb34` |
| `paper/manuscript.tex` | `24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb` |
| `paper/references.bib` | `0e4054e00ea1d09ce71d8f16fa2a051216d34f76aa437663012e726caf950f35` |
| `paper/figures/constant_class_convergence.tex` | `abece8b050760a3a85afb88f12875f5eed6a39a7ccbc51e92d4e9adade4f9cb7` |
| `paper/figures/topology_owner_split.tex` | `53b4c678011d90d9cc20cba5e6b37720c14b1f9462cf2e9e1a2e2e81f8b7f1dc` |
| `paper/paper.pdf` | `c55e4f45fe5f58841864e9af695c4664bdb1a77cff6e087fd2869d4ecd385e02` |

### P10 -- `papers/10-separated-reflection`

| Artifact | SHA-256 |
|---|---|
| project `README.md` | `a60142e1b1eb013d0b8d9dfa22d83afe7ec61efcd5524df4814407634bb0538e` |
| `paper/README.md` | `6ffd4dd3ac4e4df27016ee4192652f2e1297e37a92f845d1f6964274bceeb3c7` |
| `paper/manuscript.tex` | `27bae88814f16263de444bb1650e4a550d0f0eca327f3c551d7c2097f353d315` |
| `paper/references.bib` | `201e997ad953ebc1f27bd4c068400be656a1b9b6fbc4a231443ad8c2770e98b1` |
| `paper/figures/copied_coproduct_ledger.tex` | `e4bceb3b3bb67d6a837014c44d226ce2131ca7cdd4184cdd4aa8da12f8f90291` |
| `paper/figures/owner_collapse_and_proxy.tex` | `d5be1f45dbf4c5b3c7668d326e416166941dd9dbb7b7d0c64d076a8f41d03421` |
| `paper/paper.pdf` | `30c22eb8bbfd256cede958df86ce7f985889441a295d52e2ac5acfb3d59e2ce4` |

### P11 -- `papers/11-indiscrete-convolution`

| Artifact | SHA-256 |
|---|---|
| project `README.md` | `1380928a1d9e46e4a82395a2a3059bc1c1a8a33a9450ecd6d7e31adfb1a86a64` |
| `paper/README.md` | `86d87e66417ba387f0fc1ed8c4d7b037519f22bb72932b0b18f22d3d5e4625b6` |
| `paper/manuscript.tex` | `eb1aa4d7060cf1aa53a729e7c7be89a5724a6133ef3bf000cb800bf786de1002` |
| `paper/references.bib` | `33afa817ff529cd0d98a791e4ea68c0e4a34bd57158774a6c51c43174b72d877` |
| `paper/figures/convention_split.tex` | `fe816b5c5f8cea2e3ee94380773cb3d452e3af05e639a8ced2a290a1ead073b4` |
| `paper/figures/proxy_action_blind.tex` | `8cc369786047490df518e61c37d232fdc29b49fde7a81da440b7b6c713652c64` |
| `paper/paper.pdf` | `15d207568a61590852697511df2faf4cb06fd06047574c3dc3413e352c14840d` |

### P12 -- `papers/12-marked-time-cohomology`

| Artifact | SHA-256 |
|---|---|
| project `README.md` | `0026d84cf0a342f1da097dc8212cca7b80a532bc1d1f8cdcf2b40317967ebb20` |
| `paper/README.md` | `f8d7228452fc389e0b26b0de1314f77a270dd7b39ee00590851f2154c2ccfb91` |
| `paper/manuscript.tex` | `c6ad0f8c22d68840198d744a615da06e8b062d5ccdbeedb7f4ee76bf35073163` |
| `paper/references.bib` | `b763e9c07e3265d878bfc8b4caf44fb6c92ef12e7fac59b8af0bdeb703876175` |
| `paper/figures/same_carrier_diagonal.tex` | `a83148600d497dd1b91510f5707a1b1a9402c35689013a1fa904978206ff5cf1` |
| `paper/figures/packet_four_way_firewall.tex` | `9a52c273e91878d4dd74f96bd27fe299be39d98cdbebdda6bc800d89184b6908` |
| `paper/paper.pdf` | `9d6747e9f33c6ab3724beb35daedbb0efaff73691ed344374366f2392541ec15` |

### P13 -- `papers/13-circle-twists`

| Artifact | SHA-256 |
|---|---|
| project `README.md` | `2bac26606bbdb8025bf2c76bc78dcffca7613cc3cece3bd3cec7d18a39f692d7` |
| `paper/README.md` | `b1a7b99e271e0e8c8abe162b802851b25fea10c9d0409a4bb1ad91aaf02b9f5a` |
| `paper/manuscript.tex` | `c8c9b7522e9bf63a30ed199fe3468d642cb3e572e324680ccd6893857fbe9701` |
| `paper/references.bib` | `661aa0a948e8a06538cb300106e91bc9d72e91bf26e9515fdb9a074d0f394292` |
| `paper/figures/owner_support_firewall.tex` | `130ad2f1833a91970629311e1cf21bc848d826afcda941e9b0ad3367cb8f2360` |
| `paper/figures/generic_constant_diagonal.tex` | `727160835b9190b8d3a854825ea30735e4f59813be50a6f7960f3da735558d44` |
| `paper/paper.pdf` | `4082ca13a6daadb72ccc30a34fc5160f5920247d3fa3436562349ccc5a9c43c2` |

The P13 parent README contains the exact one-way pointer to the package
README. Both P13 READMEs contain the current P12 correction-report identities
and explicitly identify this batch audit as the downstream binder for their
post-report status bytes. Neither README self-binds or embeds this report's
digest.

## 3. Current proof, composition, citation, peer, release, and Route ledger

| Paper | Proof audit | Blueprint | Citation audit | Peer review | Release audit | Route audit |
|---|---|---|---|---|---|---|
| P9 | `c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8` | `9258fa741ad8cb60d7b5de4f9220ab64a7aa44a5490ed88c185094c4418a41f5` | `bdba712848cb0872f9d8979858656384963930d6482c519cfa6485c9d5597f49` | `568f0a9653a650431e5ed5e9b7ff32d2f8b12bffcf4087472057bc73ad61e043` | `fdcf73b75c7d44543d79aae3b0c6190f43b5648341c11907e28c522f8f775be5` | `f6e3c0ef065fb675d1f6408a411dba14de1581c5dfe4800dbddb532adaf8e730` |
| P10 | `efda522ead9efebfc3f59f0688f2dfd3fe63f63ff4efd4377068485d1a4acc3a` | `b2b2aa203abe4bed3067279049ad12296fe51917043f8ecb0b88714150dbd50e` | `7f33027e9e42b67dd12b65dd1fcd2238fdf0e7419204ecea746fa45f2cd61e35` | `378c20054417b93cd34361a97a2a5f1952c121872d055732ee578d2e3aef03d3` | `ff4c60fc1d83f7b91a91c64e51f6033bb5ef2705bd2295ddb9570f207032052f` | `fded0943eb3c628e90b407c14aece688b1a79f8be4510c02e98010592b9ca4ee` |
| P11 | `03f17606b0c9d69b496d2766c0a404b0d090698101150a800de4c2108ddc6b28` | `4b6bfa27c83f72858ac5f0d03c0b9964f93e914fc1d4fdfced619327bcdfc30b` | `c7be95522abe4ab4c92494da7458b15319a838de6a391820c1f0f201bbed2498` | `6f949e0f98baf68e27bbf9bac8623c437e601cafdbc2a7a7138d7a71e28f79e8` | `09c1b352c472a07014fcb7e560bc1c34eb43209345b089cf80d16f0b94e0a8d0` | `9203d37cfaa28a45a7548a9864de614c81bf6ea199b4a6736e1c5aaa84335011` |
| P12 | `c2b0fc4ce4764b476de8623c7a1b37e33d51da4a1c318c133313956abf4af6ab` | `b343dd47d4a4e2fc7b8570c33eb3270542732a4062142b1ef79530393000e107` | `19772ee4e6a779aea17924714f0f00bf4fff9f481255fb35b60c5b61edeaa6bf` | `72307244d55a403cb4913fa08f72bb418d039b4a2109718870391dec9e14dbb0` | `dc351172d076b5bd24226def02a381ebda91138d88f3877d6df0810a0a106bd4` | `2baf2b1ea63e5573f4b2673da6329520163ec67d76b002cb6f84fcf45c0ac102` |
| P13 | `e2f8fb8df4f3418fb3ff0fb60c87f9c7a4ae26cc7470c8c14aec3f86f6df1a63` | `af7b20a7e1091a876acfa4c22a9f8ba0e9c19b3accd1fe1c1376f6c13fcc48fd` | `c12aa9d1207d122ac737b47cc9ea69c3e5ea06d457918ab0129f3b2a70f81ccf` | `bd2004cbe55139444089ca95c741f9e15fc8886878855d6be2ed0eb80ceaf78c` | `2b54cc3652c3d32d438f59cbc069523c51ca20544f89cb7a7aaf9e7e2bb632f9` | `2603502519e087a5023be2fec91e8b332a37d93a1368300a8e103680d6c5b0b9` |

The P9 release report predates and therefore does not hash-bind its final
peer report. This batch receipt binds both current reports to the same current
scholarly tuple. It does not rewrite the release report or claim that the
release report itself contained that later edge.

The P9 peer report's `paper.log` digest is a historical, transient review-time
build receipt: `4042b378a758e588e9e9b1bc424438926d4cb183cec12ecda8c3921655eadbc2`.
`paper.log` was never part of the authoritative six-file package and is
intentionally absent now. This audit does not claim that the transient file
remains rehashable.

## 4. Citation, source, and companion integrity

| Paper | Citation commands | Key uses | Unique cited keys | Bib records | Missing | Orphan | Duplicate |
|---|---:|---:|---:|---:|---:|---:|---:|
| P9 | 20 | 20 | 7 | 7 | 0 | 0 | 0 |
| P10 | 10 | 10 | 9 | 9 | 0 | 0 | 0 |
| P11 | 21 | 22 | 10 | 10 | 0 | 0 | 0 |
| P12 | 27 | 31 | 14 | 14 | 0 | 0 | 0 |
| P13 | 18 | 19 | 17 | 17 | 0 | 0 | 0 |

All companion identities and premise locators rehash. P13's five local
companion entries remain honest URL-free, DOI-free `@unpublished` records.
P13's P2/P8/P9/P11/P12 premise identities and Paper 12 Proposition 8.1 proof
identity are exact. Stacks Tag `0B1W` is currently and correctly titled
**“Colimits of spaces”** in the P12 and P13 bibliographies and rendered PDFs.

Across the five local `notes/sources/` directories there are 32 retained
research PDFs. P13 additionally reuses three already audited manifestations,
giving 35 audited PDF/preflight pairs. All 70 PDF/sidecar ledger entries
rehash; every sidecar reports PASS, internal PDF hashes and page counts agree,
and warnings are empty. Current checksum/source-ledger closure is:

| Paper | Source-ledger closure |
|---|---|
| P9 | 14/14 |
| P10 | scope 14/14 and domain 10/10 |
| P11 | 10/10 |
| P12 | 10/10 |
| P13 | 12/12 |

Research PDFs remain under `notes/sources/` and are excluded by local
`.gitignore` policy files. No source PDF occurs in any `paper/` package. The
P9 relative source-ledger path/hash prose and P10 exact Fremlin manifestation
hash are deliberate reproducibility receipts, not embedded binary leakage.
No public manuscript or bibliography exposes an absolute `/root` or `file://`
source locator.

## 5. Retained PDF and visual integrity

| Paper | Pages | Fonts | Layout-text SHA-256 | Frozen raster/visual receipt |
|---|---:|---:|---|---|
| P9 | 21 | 8 | `fb94d76d0b9be5649a836cd8d3f46dbdb8a5c6a7d0e69143d4eda9aee391755d` | 21/21 identical and inspected |
| P10 | 19 | 8 | `6975224f340f1506c766d7f61af45685bace908c56a16d3670cd16f614101cd5` | 19/19 identical and inspected |
| P11 | 16 | 7 | `89743a4df0788d988b7c09a625e8761d30bda1d39590ef9c11492e6ed95096fc` | 16/16 identical and inspected |
| P12 | 18 | 8 | `38adf39f29ac54af206f5c23537025f81a2b00fae1bed294bc4098a257fc10d4` | 18/18 identical and inspected |
| P13 | 15 | 8 | `fe95efd4cb38f2dde1b45a8d92df686f74379261aaf23d032e3db2f1e0b76a6a` | 15/15 identical and inspected |

All five retained files are A4 PDF 1.5 with rotation zero and no encryption.
Ghostscript `nullpage` parsing succeeds. All 39 fonts are embedded, subsetted,
and Unicode mapped. The PDFs contain zero embedded files and zero raster
images; there are no blank/text-empty pages, extraction replacement
characters, forms, JavaScript, suspect objects, or leaked absolute build
paths. The package titles and subjects match their manuscripts. P13's
`AUTHOR TO CONFIRM` metadata is intentional and agrees with its human-release
hold.

The final batch check did not rebuild stable scholarly tuples. It rehashed
the frozen clean-build, retained/fresh byte, raster, and visual receipts and
ran non-mutating PDF inventory/font/attachment/Ghostscript checks.

## 6. Bilingual abstracts and trace contracts

Every manuscript contains an English abstract and an independently written
Simplified Chinese abstract. The frozen fact-order and qualification parity
checks pass.

- P12: 205 English words; 353 Unicode `Script=Han` prose characters; 32
  keyword-value characters; 385 combined; 12-fact parity PASS.
- P13: 215 English words; 409 Han prose characters; 26 keyword-value
  characters; 435 combined; 12-fact parity PASS.
- P9--P11: semantic/fact-ledger parity PASS; their frozen contracts did not
  impose a uniform numerical Han-count convention.

Trace review follows each paper's frozen contract rather than imposing a
later contract retroactively:

- P9: the legacy blueprint has no strict six-key figure/table-trace contract.
- P10: both required native figures have complete six-key entries; its other
  manuscript tables are outside the frozen figure-only contract.
- P11: 4/4 required figure/table entries, six keys each.
- P12: 5/5, six keys each.
- P13: 6/6, six keys each, with matching reverse manuscript identifiers.

All manuscripts also have zero duplicate labels and zero unresolved
references.

## 7. Deterministic-control ledger

No control suite was rerun during this final batch audit. The current
manifests, CSV bodies, binding hashes, and already serialized reproduction
receipts were independently inspected.

| Paper | Manifest SHA-256 | Tests | CSVs | Body rows | Explicit negatives |
|---|---|---:|---:|---:|---:|
| P9 | `52e7a4242f91fcff1b622c9455e90ad3380ae40e742e15bf5b922a3dd4415668` | 20/20 | 8 | 240 | 0 |
| P10 | `edc2461873b237ee5050ab24612ca1065e256d33147ccca66fdcf99159e68215` | 24/24 | 10 | 676 | 0 |
| P11 | `de55c58ad7efc133b0d0865f392a30b52f6b05f89f64878cea0910b7eab557ea` | 57/57 | 12 | 642 | 5 |
| P12 | `7cbce9303393fcd755dda785312e26165656301e5dfbcab53b611e71c6204e95` | 122/122 | 11 | 3,486 | 14 |
| P13 | `26a41e2920d9a3743cc1b681aa1e32d601dc12e5fded15b3c6349840bd9094c2` | 176/176 | 12 | 2,665 | 67 |
| **Total** | -- | **399/399** | **53** | **7,709** | **86** |

All declared CSV/artifact/binding hashes match. The P13 replacement manifest
and final remediation review are authoritative; its superseded first-run
manifest remains historical and contributes no evidence. Finite controls are
diagnostic and are not promoted into proofs of arbitrary-index, continuum,
topological, or completion claims.

## 8. Route ledger

| Paper | Route-A records | Exploratory | Rejected | Route-B records |
|---|---:|---:|---:|---:|
| P9 | 8 | 8 | 0 | 0 |
| P10 | 7 | 5 | 2 | 0 |
| P11 | 7 | 3 | 4 | 0 |
| P12 | 8 | 6 | 2 | 0 |
| P13 | 10 | 3 | 7 | 0 |
| **Total** | **40** | **25** | **15** | **0** |

All 40 Stage-9--13 Route-A YAML hashes match their route audits. Every record
has `route_b_invocation_allowed: false`; all 40 A2, A3, and A4 outcomes fail,
giving 120 exact failed A2--A4 coordinates, and there are zero Stage-9--13
Route-B files. Candidate-directory identities, ordered schemas, evaluator
tuples, artifact hashes, and locator-only provenance rules pass.

## 9. Paper 12 correction and relock history

The final P12 mathematical manuscript and two figure sources are unchanged.
Two bounded receipt corrections are transparently closed:

1. The bibliography changed the Stacks Tag `0B1W` title from the legacy
   “Topological colimits” seed to the official “Colimits of spaces.” The
   retained PDF changed only on bibliography page 18; the clean five-pass
   build, 18-page raster comparison, fonts, PDF hygiene, citation graph, and
   visual inspection all pass.
2. The old Chinese count of 370 used a wider Script-Extensions convention that
   admitted 17 punctuation code points. The reproducible current convention
   gives 353 `Script=Han` prose characters and 32 keyword-value characters,
   or 385 combined. The manuscript text did not change.

The current append-only P12 reports are citation
`19772ee4e6a779aea17924714f0f00bf4fff9f481255fb35b60c5b61edeaa6bf`,
peer
`72307244d55a403cb4913fa08f72bb418d039b4a2109718870391dec9e14dbb0`,
and release
`dc351172d076b5bd24226def02a381ebda91138d88f3877d6df0810a0a106bd4`.
Each preserves and identifies its historical prefixes, closes the prior Minor,
and returns current C0/M0/m0 with public release false.

## 10. Paper 11 and Paper 13 status closures

P11's project README now reports the completed citation, peer, and technical
release audits instead of the earlier review-pending state. Append-only
citation, peer, and release relocks bind that status-only delta; scholarly
files are unchanged.

P13's parent and package READMEs now report the Technical Note / NOTE-branch
status, current P12 identities, and completed internal audits without stale
future-tense claims. Those final README hashes postdate P13's per-paper report
triplet. This batch receipt supplies the intended acyclic downstream edge:

```text
P13 scholarly tuple + c12aa9d... citation + bd2004cb... peer
  + 2b54cc36... release
  -> b1a7b99e... package README
  -> 2bac2660... parent README
  -> this batch audit
```

No README embeds the batch-audit digest, and this report does not embed its
own digest.

## 11. Historical-state interpretation

The P9--P12 `notes/pipeline_state.md` files are immutable gate-time snapshots,
not current release dashboards. Current status is determined by the final
citation, peer, release, and this downstream batch receipt. They are not
rewritten merely to modernize tense.

| Paper | Historical `pipeline_state.md` SHA-256 |
|---|---|
| P9 | `8e2b5d26b138f7fb5052b720ddbda6a868aa71351429f8863b8b144d395513c8` |
| P10 | `75cec92ff33ef52a456304361d6df5c26c055164adecbffb7f603b63e195e5ce` |
| P11 | `317ab9e8b3082b2d8bc75590618a6e86ca742bb8c23a899c3b612ea6304125e6` |
| P12 | `f5ee48cc308df835cbdc840169c51e63da1a80b10e45db87881913fa46bbacbf` |
| P13 | `d98bf49d2eb5c1905ea3625251d787b247f3cf19577ff40f8bc0136186280fd5` |

Historical review findings and superseded hashes remain visible in append-only
reports. Their continued presence is provenance, not a current defect. This
includes P9's transient log receipt, P11's earlier pending-status bytes, P12's
two corrected Minors, and P13's Freeze-1 manuscript findings and rejected
first control manifest.

## 12. Provenance graph and mutation boundary

The audited upstream cross-report graph contains 65 current artifact nodes,
65 unique hashes, and 255 distinct current-hash edges. It has zero self-edges
and zero cyclic strongly connected components. Qualified current hashes
resolve; there are no manifest self-hashes, YAML self-hashes, or report
cycles. All current cross-paper edges point from a higher-numbered paper to a
lower-numbered prerequisite. Under this stored-hash edge convention, this
report adds a new source with outgoing references to the 65 upstream nodes and
no incoming current-hash edge, so it cannot create a cycle. Locator-only paths
remain explicitly unhashed until their documented downstream receipts.

After the bounded prerequisite corrections and append-only relocks documented
in Sections 9--10, the only final consolidation write is this report. The
consolidation pass did not edit scholarly TeX, BibTeX, figures, PDFs, proofs,
controls, generated results, Route YAMLs, source PDFs, or historical gate
records. It did not run Git, stage files, create a commit, push, archive,
upload, or synchronize a public repository.

## 13. Residual external gates

The following are release conditions, not defects in the reviewed bytes:

- human confirmation of author order, affiliations, correspondence, ORCID,
  CRediT roles, funding, conflicts, acknowledgments, responsibility, ethics,
  and final tool/AI disclosure;
- immutable public identities for unpublished companion papers, or approved
  exact source-locked/self-contained replacements;
- venue and article-type selection, template and citation-style conversion,
  licence, accessibility/tagging, repository coordinates, and submission-day
  DOI/metadata/correction/retraction/policy refresh;
- an exact public-payload manifest and explicit human batch-release approval;
- real release-system Git/index/stage/tree/LFS checks plus archive, upload,
  attachment, supplement, hidden-path, remote-sync, and fresh-clone checks
  proving that research-source PDFs cannot enter the public payload.

Until all applicable gates close, the batch remains an internally accepted,
exact-byte technical candidate set and
`PUBLIC_RELEASE_AUTHORIZED=false` remains binding for P9--P13.

## 14. Machine-readable closure block

```text
PAPERS_9_13_BATCH_AUDIT=PASS
CURRENT_TECHNICAL_FINDINGS=C0/M0/m0
P9_TECHNICAL_PACKAGE=PASS
P10_TECHNICAL_PACKAGE=PASS
P11_TECHNICAL_PACKAGE=PASS
P12_TECHNICAL_PACKAGE=PASS
P12_STANDALONE_PASS=true
P13_TECHNICAL_NOTE_PACKAGE=PASS
P13_STANDALONE_PASS=false
P13_NOTE_OR_MERGE=true
P13_STANDALONE_FINDINGS=C0/M1/m0
PAPER_PACKAGE_COUNT=5
FILES_PER_PAPER_PACKAGE=6
RETAINED_PDF_PAGES=21,19,16,18,15
CONTROL_TESTS=399/399
CONTROL_CSVS=53
CONTROL_BODY_ROWS=7709
CONTROL_EXPLICIT_NEGATIVES=86
ROUTE_A_RECORDS=40
ROUTE_EXPLORATORY=25
ROUTE_REJECTED=15
ROUTE_B_RECORDS=0
CURRENT_HASH_GRAPH_ACYCLIC=true
UPSTREAM_CURRENT_HASH_NODES=65
UPSTREAM_CURRENT_HASH_EDGES=255
RESEARCH_SOURCE_PDF_IN_PAPER_PACKAGES=0
GIT_OPERATION_PERFORMED=false
PUBLIC_SYNC_PERFORMED=false
PUBLIC_RELEASE_AUTHORIZED=false
```
