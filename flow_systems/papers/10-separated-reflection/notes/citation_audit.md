# Paper 10 final citation/source-integrity audit

Frozen: **2026-08-14 (Asia/Shanghai)**  
Role: independent final citation, manifestation, build, PDF, and release-boundary
auditor.  No manuscript, bibliography, figure, PDF, proof, Route, control, or
source-lock byte was edited by this audit.

## 1. Verdict

**ACCEPT — exact internal-batch candidate locked; public/journal release remains
subject to two explicit post-batch mechanical conditions.**

The final candidate has zero missing citations, zero orphan references, zero
unsupported cited claims, zero unresolved locator defects, and zero candidate-byte
build or visual blockers.  M2--M4 are closed.  M1 is represented truthfully by an
exact companion-PDF hash and no invented current URL; its immutable public identity
is deliberately deferred until batch synchronization.  The source-PDF exclusion is
declared and protected by a local ignore rule, but must still be demonstrated on the
actual fresh-clone/staged public payload.

These two external release conditions do not request a change to the locked
manuscript/Bib/PDF bytes:

- **R1 — companion identity:** after Paper 9 is synchronized, verify a stable public
  release/tag/commit identity for the exact Paper-9 PDF SHA-256
  `c55e4f45fe5f58841864e9af695c4664bdb1a77cff6e087fd2869d4ecd385e02`
  before journal submission.  The present Bib entry correctly says that no public
  URL is asserted.
- **R2 — public payload:** in the real Git worktree/fresh clone, require zero
  `papers/10-separated-reflection/notes/sources/*.pdf` files in the tracked, staged,
  release, or synchronization payload.  The ignore file is a guard, not evidence of
  the final index state.

Finding counts on the locked candidate: **C0 / M0 / m0**.  External protected
release conditions: **R1--R2**.

## 2. Exact candidate bytes

| Artifact | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `27bae88814f16263de444bb1650e4a550d0f0eca327f3c551d7c2097f353d315` |
| `paper/references.bib` | `201e997ad953ebc1f27bd4c068400be656a1b9b6fbc4a231443ad8c2770e98b1` |
| `paper/paper.pdf` | `30c22eb8bbfd256cede958df86ce7f985889441a295d52e2ac5acfb3d59e2ce4` |
| `paper/figures/owner_collapse_and_proxy.tex` | `d5be1f45dbf4c5b3c7668d326e416166941dd9dbb7b7d0c64d076a8f41d03421` |
| `paper/figures/copied_coproduct_ledger.tex` | `e4bceb3b3bb67d6a837014c44d226ce2131ca7cdd4184cdd4aa8da12f8f90291` |
| `paper/README.md` | `6ffd4dd3ac4e4df27016ee4192652f2e1297e37a92f845d1f6964274bceeb3c7` |
| `README.md` | `a60142e1b1eb013d0b8d9dfa22d83afe7ec61efcd5524df4814407634bb0538e` |
| `notes/sources/.gitignore` | `6cbf9577be5add7a925718f4047f672fe46d991772fd451f428390aa323b6d3f` |

The locked PDF is 19 A4 pages, unencrypted, with the declared title, author,
subject, and keywords.  Its `pdftotext -layout` SHA-256 is
`6975224f340f1506c766d7f61af45685bace908c56a16d3670cd16f614101cd5`.

## 3. Citation/BibTeX census

| Metric | Result |
|---|---:|
| In-text citation commands | 10 |
| Unique citation keys | 9 |
| BibTeX entries | 9 |
| In-text keys absent from BibTeX | 0 |
| BibTeX entries absent from the text | 0 |
| Duplicate keys or duplicate source aliases | 0 |
| Known publication DOIs omitted | 0 |
| Self-cited unique entries | 1/9 (11.1%) |
| Self-cited citation commands | 1/10 (10.0%) |

The numerical `unsrtnat` reference order is the order of first appearance and
renders as `[1]`--`[9]`.  The arXiv-only items retain exact eprint version and URL
identifiers; their arXiv-issued DataCite DOI aliases are not substituted for the
version-pinned manifestation identifiers.  All three cited journal manifestations
with publication DOIs include those DOIs: Deninger, Cagliari--Mantovani, and
Hernández-Arzusa--Hernández.

## 4. Claim--citation and locator audit

Every cited claim was checked against the retained exact manifestation or the
stable authoritative web section.  Physical page means the PDF page counted from
one; printed pagination is stated separately where it differs.

| Occurrence/key | Manuscript-owned claim | Exact controlling evidence | Verdict |
|---|---|---|---|
| 1. `Deninger2026` | finite-kernel/set coordinates, suspension action, packet and stabilizer | arXiv `1807.06400v4`, physical pp. 32--33, Eqs. (35), (38)--(39), and pp. 38--39, Section 6/Theorem 6.1 | **SUPPORTED**; journal DOI metadata is separated from the arXiv locator manifestation |
| 2. `Wang2026Packet` | actual packet, every inherited orbit, and time-orbit quotient are nonempty, nontrivial indiscrete spaces | exact Paper-9 PDF SHA `c55e4f45...e02`, Theorem 5.1 and Corollaries 5.2--5.4 | **SUPPORTED**; no false current public URL |
| 3 and 6. `Pirttimaki2021` | topological indistinguishability, quotient topology/terminology, `T_0` quotient, induced-map context | arXiv `1905.01157v2`, physical pp. 4--6, 9, 12--13 | **SUPPORTED**; author corrected to Teemu Pirttimäki |
| 4. `CagliariMantovani2003` | `T_0` reflection unit and unique-factorization vocabulary | inspected author preprint, physical pp. 3--4 | **SUPPORTED**; published DOI `10.1016/S0166-8641(02)00370-X` |
| 5. `HernandezArzusaHernandez2020` | reflection/epireflection vocabulary and separated reflective examples | arXiv `1704.01146v2`, physical pp. 2--6 | **SUPPORTED**; DOI/PDF title is *Reflections...*, while the arXiv record label is transparently distinguished as *Epireflections...* |
| 7. `FremlinMeasureCh11Dev` | sigma-algebra, generated Borel algebra, positive countable additivity and Dirac convention | exact results-only Chapter 11 PDF SHA `0cb220af...d5d`, physical pp. 4--6 | **SUPPORTED**; front-matter 30.9.02 and later section dates are disclosed rather than collapsed into a false single-version claim |
| 8. `HoermannCStar2026` | norm/SOT/WOT on one `B(H)` carrier and their Hausdorff separation | exact lecture notes version 2026-08-06, Section 4.1, physical p. 43 / printed p. 39 | **SUPPORTED**; no carrier transfer or representation claim |
| 9. `Preston2008` | standard-Borel and countably-separated definitions/implication | arXiv `0809.3066v1`, physical p. 3 and physical p. 13, Section 3 | **SUPPORTED** |
| 10. `StacksCoproduct0B1W` | tagged carrier and componentwise coproduct topology | Stacks Project Section 5.29 opening, Section Tag `0B1W` | **SUPPORTED**; the Bib entry no longer misassigns the section tag to Lemma 5.29.1 (whose tag is `0B1X`) |

The graph also passes the ownership test:

- Deninger owns set/action/stabilizer inputs, not the inherited indiscrete theorem.
- Paper 9 owns only that imported actual-topology theorem.
- Paper 10 proves the separated images, observable/measurable/measure collapses,
  transported-law classification, proxy directions, and copied-coproduct results.
- No citation transfers a source-packet fact to the proxy or copied coproduct, and
  no control/Route artifact is used as scholarly proof.
- The novelty sentence remains search-bounded and dated; it does not say “first”,
  “novel”, “unprecedented”, or claim global absence.
- Radon is used only to state an explicit nonclaim/limitation; no convention is
  silently imported into `Mfin`.

## 5. M1--M4 closure

| Gate | Final status | Exact disposition |
|---|---|---|
| M1 — Paper-9 identity | **DEFERRED EXTERNAL RELEASE CONDITION, CANDIDATE-TRUTHFUL** | `@unpublished` gives author/title/year and the exact cited PDF hash, asserts no URL, and explicitly requires immutable public identity after batch sync.  This is R1, not an invented current identifier. |
| M2 — Hernández title/version family | **CLOSED** | Bib separates the DOI/published and PDF title *Reflections...* from the arXiv-record label *Epireflections...* and pins `v2`/date for locators. |
| M3 — Fremlin development manifestation | **CLOSED** | Bib declares results-only development status, front-matter and later section-date variation, physical-page semantics, URL, and exact PDF SHA. |
| M4 — Hofmann year / Lipsman DOI | **CLOSED BY OMISSION** | Neither optional source is cited or retained in BibTeX; no year or DOI is guessed. |

The bounded metadata checks found no Crossref correction/retraction relation for the
three journal DOI records as of the audit date.  This is a metadata check, not a
claim that no future correction can occur.

## 6. Independent build and PDF integrity

An isolated directory containing only the locked `manuscript.tex`,
`references.bib`, and the two locked TikZ sources was built with:

```text
latexmk -xelatex -interaction=nonstopmode -halt-on-error \
  -file-line-error -jobname=paper manuscript.tex
```

Results:

- exit status `0`;
- 19 pages, matching the locked PDF;
- zero undefined citations and zero undefined references;
- zero LaTeX warnings, zero `Label(s) may have changed`, zero missing-character
  warnings, and zero overfull boxes in the final clean log;
- independent build PDF SHA-256
  `0545638b65473fb88350a0b02c82bdf83b8150299dd560433a0f53661d5016a0`;
- independent and locked PDFs have the same layout-text SHA-256
  `6975224f340f1506c766d7f61af45685bace908c56a16d3670cd16f614101cd5`.

The PDF container hashes differ because generated container metadata is not
byte-deterministic; equal locked source hashes, page count, and layout-text hash,
together with the clean build, establish source-to-PDF content consistency.

`pdffonts` reports every used TeX Gyre and Noto CJK font as embedded, subsetted,
and Unicode-mapped.  Representative visual inspection covered pp. 1, 3, 5, 8,
10--14, 16, and 18--19, including both native figures, the main ledger, theorem
displays, the protected-hash appendix, and every rendered reference.  No clipping,
overlap, truncated URL/DOI, broken glyph, false page number, or unreadable reference
was found.

## 7. Source locks and public-sync exclusion

The retained corpus contains exactly 12 PDFs and 12 adjacent preflight JSON
sidecars.  Both checksum ledgers pass when evaluated from the repository root:

| Lock | SHA-256 / result |
|---|---|
| `notes/sources/scope_source_manifest.md` | `38fd6557eba364eff748b35a62ac28bf768b75a259e1e7631099149f67118140` |
| `notes/sources/scope_sources.sha256` | `222c1a6d9552c82890bcc3846245fb4c636eef981a5937b7355d45f5626497aa`; 14/14 files OK |
| `notes/sources/dom-source-manifest.md` | `49e20c34eff26915780f43b5df7d5b6635fa35d6225b63ea476cbeab1c14af21` |
| `notes/sources/dom-sources.sha256` | `34ed23b73f01f5027deaa5084bce250d5f77c1dbcd02c38627c950e5803d13ce`; 10/10 files OK |

The manuscript's Data and Code Availability section explicitly excludes all twelve
third-party PDFs from public synchronization while permitting manifests, checksum
ledgers, preflight sidecars, canonical endpoints, locators, and hashes.  The local
`notes/sources/.gitignore` contains `*.pdf` and is locked above.  Because the working
directory supplied to this audit is not a Git worktree, tracked/staged status cannot
be inferred here; R2 therefore remains a mandatory fresh-clone/index check.

## 8. Protected project hashes

All 15 protected hashes printed in the manuscript appendix match the on-disk bytes:

| Protected artifact | SHA-256 |
|---|---|
| `notes/research_protocol.md` | `4fe51d7dc9514dea101178995dec73e120ab7032b11c06ecd4bc0efadf9cbc58` |
| `notes/candidate_lock.md` | `4cc6cae36630e13623d638a5eac7daaab084eef9549f4ca3bd44b026a32d26cf` |
| `notes/phase1_design_amendment.md` | `e0e3fb42c2285b8c5da521f05588581e7981de8957e33aa3cf237f653d1c432f` |
| `notes/phase1_final_gate.md` | `bdc5e3698110695a84f392c47bb907b7cf8ddc8807ea9af04654791090e4ab68` |
| `notes/phase2_source_novelty_audit.md` | `8b4a2ff1ed911765faa294c43cfbfb9f4986624e972ee4bcb509b12321e658fa` |
| `notes/phase2_domain_source_audit.md` | `8dbc4e6487d342bcf352a4b0161bc1c4f17800d07556a3d11b49ce900b3aa582` |
| `notes/phase2_precedent_search.md` | `68aef453788251edb0e7aad631ea58ca1794fc23e255d5c96b3d8c39030d5719` |
| `notes/phase2_final_gate.md` | `1421ada08a7192e14e7edf4ab9982523c275063dee0c23c1d2f076ac4bf13ffb` |
| `notes/proof_audit.md` | `efda522ead9efebfc3f59f0688f2dfd3fe63f63ff4efd4377068485d1a4acc3a` |
| `results/separated_reflection_controls_manifest.json` | `edc2461873b237ee5050ab24612ca1065e256d33147ccca66fdcf99159e68215` |
| `notes/phase3_peer_review.md` | `cd075d267865812c2368679346a2dfde9a5a976d4306b4dc61664adf5f8a3a7e` |
| `notes/phase3_final_gate.md` | `ec672859dd28e433f82a392685b7816c421b55c096f334bc3ca803dc87a68541` |
| `notes/route_audit.md` | `fded0943eb3c628e90b407c14aece688b1a79f8be4510c02e98010592b9ca4ee` |
| `notes/pre_manuscript_citation_audit.md` | `9b9ee072cdc44129084ee28945574bd59750dbbec39008301fea7eef3c1d6850` |
| `notes/composition_blueprint.md` | `b2b2aa203abe4bed3067279049ad12296fe51917043f8ecb0b88714150dbd50e` |

## 9. Final disposition

- Candidate-byte citation/source/build/visual verdict: **ACCEPT**.
- Required manuscript/Bib/PDF correction: **none**.
- Exact candidate remains protected by the hashes in Section 2.
- Before public/journal release: execute **R1** and **R2** and record their
  outcomes without weakening the present no-false-URL and no-third-party-PDF
  boundaries.
