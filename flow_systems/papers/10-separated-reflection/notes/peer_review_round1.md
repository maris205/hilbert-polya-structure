# Paper 10 independent peer review — round 1 final

## Manuscript information

- **Title:** *Separated Reflections and Observable Collapse of Indiscrete Arithmetic Prime Packets*
- **Author:** Liang Wang
- **Review date:** 2026-08-14 (Asia/Shanghai)
- **Reviewer role:** independent methodology/domain/devil's-advocate reviewer
- **Review focus:** theorem validity, owner and domain typing, source and citation integrity, Route-A/Route-B semantics, deterministic-control claims, declarations, clean build, and complete PDF presentation
- **Final scientific verdict:** **ACCEPT / exact-lock PASS — C0/M0/m0**
- **Confidence:** **5/5**

This verdict is for the exact internal scientific candidate locked below. Public or journal submission remains conditional on the explicitly identified human-confirmation and archival-identity steps in §10.

## 1. Exact candidate and upstream evidence lock

### 1.1 Final candidate tuple

| Artifact | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `27bae88814f16263de444bb1650e4a550d0f0eca327f3c551d7c2097f353d315` |
| `paper/references.bib` | `201e997ad953ebc1f27bd4c068400be656a1b9b6fbc4a231443ad8c2770e98b1` |
| `paper/figures/owner_collapse_and_proxy.tex` | `d5be1f45dbf4c5b3c7668d326e416166941dd9dbb7b7d0c64d076a8f41d03421` |
| `paper/figures/copied_coproduct_ledger.tex` | `e4bceb3b3bb67d6a837014c44d226ce2131ca7cdd4184cdd4aa8da12f8f90291` |
| `paper/paper.pdf` | `30c22eb8bbfd256cede958df86ce7f985889441a295d52e2ac5acfb3d59e2ce4` |
| `paper/README.md` | `6ffd4dd3ac4e4df27016ee4192652f2e1297e37a92f845d1f6964274bceeb3c7` |
| project `README.md` | `a60142e1b1eb013d0b8d9dfa22d83afe7ec61efcd5524df4814407634bb0538e` |

The release-candidate ledger in `paper/README.md` reproduces the five manuscript/Bib/figure/PDF hashes exactly.

### 1.2 Bound scientific locks

| Artifact | SHA-256 |
|---|---|
| `notes/composition_blueprint.md` | `b2b2aa203abe4bed3067279049ad12296fe51917043f8ecb0b88714150dbd50e` |
| `notes/proof_audit.md` | `efda522ead9efebfc3f59f0688f2dfd3fe63f63ff4efd4377068485d1a4acc3a` |
| `results/separated_reflection_controls_manifest.json` | `edc2461873b237ee5050ab24612ca1065e256d33147ccca66fdcf99159e68215` |
| `notes/route_audit.md` | `fded0943eb3c628e90b407c14aece688b1a79f8be4510c02e98010592b9ca4ee` |
| `notes/phase3_peer_review.md` | `cd075d267865812c2368679346a2dfde9a5a976d4306b4dc61664adf5f8a3a7e` |
| `notes/phase3_final_gate.md` | `ec672859dd28e433f82a392685b7816c421b55c096f334bc3ca803dc87a68541` |

The seven Stage-10 Route-A YAML files independently re-hashed to:

| Owner | SHA-256 |
|---|---|
| actual separated reflection | `57bdf64ffcdf66797ba10985082e9bcb42cd64b45bf479a5af8de4d125e123af` |
| actual continuous observables | `a94cc0a8fb48488de0e46bb6f30e845ee3641b5a8517da707e6b1570e212af82` |
| actual Borel/finite measure | `be95f98692bab5eb54ef93edab64b0f0bb8bbf7c0131f7021f559c614de94b0d` |
| actual `Q_p` continuous characters | `9d846ba5577c5424da786a9b28edb471b96a2246ec91cc9d4de5c6767929c146` |
| actual-orbit/standard-circle comparison | `f8b9a454c6ebb14163c78ed1e6bd6c188b8a96522fff1c2ba26f3ab45e022ed1` |
| copied-prime `K0` control | `5b78ea0199d67457b6963664d42934dde04ee93aa78cf7bd642403f81bc9b6d3` |
| copied-prime finite-measure control | `d38e066923abceae8ebbb382c876b08c562dcff554be465ec5a10d887ccf1aad` |

All seven contain exactly nine `A2` validation fields; no Stage-10 Route-B YAML exists.

## 2. Overall assessment

The paper classifies what ordinary separated, continuous, measurable, positive-finite-measure, continuous-character, fixed-operator, and explicitly copied-component interfaces retain from the three nontrivial indiscrete fixed-prime owners imported from Paper 9. It proves singleton separated reflections, constant separated observables, trivial Borel and total-mass measure ledgers, trivial continuous circle characters for a transported law, direction-sensitive failure of the standard-circle proxy, and discrete-label/`ell^1_+` recovery for a declared tagged coproduct. The arguments are elementary but carefully typed, direct, and complete; the owner boundaries prevent credit from moving between actual, proxy, copied, and historical constructions. The bibliography, source locators, controls receipt, six-key figure trace, declarations, and Route records are internally consistent. The strongest limitation is venue-dependent novelty: the general indiscrete-space reductions are standard, while the source-specific topology is inherited from Paper 9. The manuscript now states that limitation explicitly and claims only the exact owner-typed assembly, group-law/circle direction, and copied-component boundary. On that bounded technical-note contribution, the exact candidate merits acceptance.

## 3. Strengths

### S1. Direct universal-property proofs avoid imported categorical assumptions

The paper computes the Kolmogorov quotient and separately verifies the Hausdorff and completely regular Hausdorff factorization properties. This proves the named interfaces without silently assuming a broad reflectivity theorem.

**Evidence Anchor:** `text: manuscript Theorem 3.1 and proof, p.6 — "For each of the three target classes, the unique map"`

### S2. Measure and measurable-map statements use the exact sigma-algebra

The manuscript generates the two-set Borel algebra from the actual topology, places the countable-separation hypothesis on the target, and evaluates Dirac measures only on measurable events. It explicitly refuses Radon, support, Haar, state, trace, signed-measure, and complex-measure promotion.

**Evidence Anchor:** `text: manuscript Theorem 4.2 and boundary paragraph, p.9 — "All Dirac measures δ_x, x ∈ X, coincide with μ_1."`

### S3. Set-bijection, group-law, and topology ownership remain distinct

The fixed bijection `phi_p` transports only the quotient-group law to the actual `ACT-Q-p` carrier. Continuity is then checked against the independently inherited indiscrete topology, and no source-canonical law, abstract-character classification, or transported topology is claimed.

**Evidence Anchor:** `text: manuscript Theorem 5.1 and following boundary paragraph, p.10 — "the specific law is transported to the already fixed actual carrier"`

### S4. The standard-circle comparison has the correct direction

The actual-to-circle bijection is noncontinuous and its inverse is continuous; the manuscript therefore treats the circle as a finer proxy, not as a factor or reflection of the actual orbit.

**Evidence Anchor:** `text: manuscript Theorem 5.2, p.11 — "is not continuous, whereas"`

### S5. Coproduct conclusions are exact and label-neutral

The tagged coproduct is declared as a modeling choice. The proof classifies opens, Borel events, indistinguishability classes, maps to `T0` targets, and positive finite measures before specializing the arbitrary countable label set to primes. Zeros in component-mass vectors and the external/unbounded status of `log p` are handled correctly.

**Evidence Anchor:** `equation: manuscript Theorem 6.1 component-mass bijection and Corollaries 6.2–6.3, pp.11–12`

### S6. Reproducibility claims are sharply bounded

The manuscript reports 24/24 tests, ten CSV artifacts, 676 data rows, verify-only success, and two byte-identical generations against the exact controls-manifest hash. It says explicitly that these finite controls are regression evidence rather than proofs of the infinite or source-specific theorems.

**Evidence Anchor:** `dataset: controls manifest edc2461873b237ee5050ab24612ca1065e256d33147ccca66fdcf99159e68215; manuscript §7, pp.13–14`

### S7. Visual provenance satisfies the strict six-key trace contract

Both native TikZ figures have explicit `artifact_id`, `source_data`, `transformation`, `caption_claim`, `supported_manuscript_claims`, and `limitations` entries. The final figure-source hashes match both the files and the release ledger.

**Evidence Anchor:** `table: paper/README.md § figure_table_trace and strict six-key entries, lines 77–117`

## 4. Weaknesses

None at Critical, Major, Minor, or copyedit threshold remains in the exact candidate.

## 5. Coverage receipt for the empty Weaknesses list

**Covers:** Weaknesses

| Dimension examined | What was checked | Basis for no remaining weakness |
|---|---|---|
| Definitions and quantifiers | nonempty/nontrivial indiscrete sources; `T0`, Hausdorff, CRH, countably separated, fixed-operator targets; arbitrary `p` and orbit label `a` | Every conclusion retains its stated source and target hypotheses; negative controls expose the sharp boundaries. |
| Theorem logic | Lemma 2.1 and P10-1–P10-8, line by line against the proof audit | No circularity, illicit converse, missing case, or theorem stronger than its proof was found. |
| Owner integrity | `ACT-PACKET-p`, `ACT-ORBIT-p-a`, `ACT-Q-p`, `STD-CIRCLE-p`, copied coproduct, historical controls | Actual, proxy, copied, and historical owners are never merged or credited through a bare set bijection. |
| Group and operator domains | ownership of `phi_p`, transported law, continuous versus algebraic characters, common `B(ell^2)` carrier, norm/SOT/WOT | The law is Paper-10-defined and topology-tested; all three operator targets are Hausdorff on the same carrier; representation and unbounded-operator claims are excluded. |
| Measurable and measure domains | topology-generated Borel algebra, countably separated target, finite positive countably additive measures, Dirac equality | Proper singletons are never treated as measurable; no Radon/support/Haar/state/trace language is promoted. |
| Coproduct and weights | coproduct topology, Borel component unions, discrete `K0`, `ell^1_+`, zero masses, prime/composite/arbitrary labels, `log p` | The proof starts with arbitrary countable labels and supplies no intrinsic prime or nonzero-weight selector. |
| Route semantics | roadmap lines 134–138, manuscript §§7.1–7.2, table 2, route audit, seven YAMLs | `A0` arithmetic relevance, `A1` primitive/closed orbits, `A2` zeta/Fredholm, `A3` analytic/Weil compression, and `A4` quantization/operator lift are not swapped; prerequisites and nine validation fields are separate. |
| Citations and bibliography | nine used entries, cited locators, Paper-9 companion identity, Bib/LaTeX resolution | All cited keys resolve; no orphan or ghost citation remains; locator wording matches the inspected sources and companion artifact. |
| Figures and traceability | both native TikZ sources, captions, arrow directions, owner assignments, strict six-key trace | All mathematical nodes have textual/proof owners and explicit limitations; no raster or external figure asset is embedded. |
| Build and PDF | clean temporary build, final PDF text, fonts, metadata, every page, p.12 correction | The clean build succeeds and extracts byte-identical text; all 19 pages are legible; the former QED/Corollary collision is closed. |
| Declarations and release integrity | ethics, CRediT, funding/COI/acknowledgments, AI disclosure, source-PDF exclusion, companion URL boundary | Provisional human-owned fields are conspicuous and are explicitly blocked from journal release; no declaration is fabricated. |

## 6. Theorem-by-theorem adjudication

| Result | Final audit | Boundary verified |
|---|---|---|
| Lemma 2.1 | PASS | A nonempty indiscrete source maps constantly only when the target is `T0`; a nontrivial indiscrete target supplies the sharp counterexample. |
| P10-1 / Theorem 3.1 | PASS | `K0(ACT-Q-p)` is not confused with the already nontrivial `ACT-Q-p`; the three separated universal images are proved directly. |
| P10-2 / Theorem 3.2 | PASS | Equality of function sets and unital `*`-algebras precedes use of the supremum norm; evaluations coincide because all functions are constant. |
| P10-5 operator part / Theorem 3.3 | PASS | Norm, SOT, and WOT are separately Hausdorff on one fixed `B(ell^2(N))`; the result classifies continuous maps, not representations. |
| P10-3 / Theorem 4.1 | PASS | The Borel algebra is exactly `{empty,X}`; countable separation is a target hypothesis; the nontrivial source is neither countably separated nor standard Borel. |
| P10-4 / Theorem 4.2 | PASS | Positive finite countably additive measures are classified by total mass; Dirac equality is asserted only as equality on measurable events. |
| P10-5 group part / Theorem 5.1 | PASS | `phi_p` transports a group law only; indiscrete codomain makes the group operations continuous; continuous circle characters are trivial without classifying algebraic characters. |
| P10-6 / Theorem 5.2 | PASS | `beta_{p,a}` is noncontinuous actual-to-circle; its inverse is continuous; the standard circle remains a finer imposed proxy. |
| Theorem 6.1 | PASS | Opens and Borel events are component unions; `K0` retains discrete labels; `T0` maps factor by labels; finite positive measures are exactly `ell^1_+` component masses. |
| P10-7 / Corollary 6.2 | PASS | Prime labels are retained because the copied coproduct inserts them; no theorem about a source-global suspension is claimed. |
| P10-8 / Corollary 6.3 | PASS | Prime/composite/arbitrary labels have the same abstract classification; `log p` is external, unbounded, and outside both `C_b` and `C_0`. |
| P10-9 | PASS | Deterministic controls are exact finite regression witnesses and are not substituted for proofs. |
| P10-10 | PASS | Five actual/comparison records are exploratory, two copied controls rejected, all fail `A1`–`A4`, and Route B is false. |

## 7. Route-A/Route-B rubric audit

The manuscript's final wording matches `propose-flow-systems.md` lines 134–138 exactly in substance:

| Coordinate | Frozen meaning | Manuscript/YAML status |
|---|---|---|
| `A0` | arithmetic relevance | weak arithmetic relation for five actual/comparison owners; fail for both copied controls |
| `A1` | primitive periodic or closed orbits | fail for all seven |
| `A2` | dynamical zeta or Fredholm determinant | fail for all seven |
| `A3` | analytic structure or Weil-compression compatibility | fail for all seven |
| `A4` | natural quantization or operator lift | fail for all seven |

Same-object identity, prerequisites, and the nine validation fields are correctly described as evidence gates, not alternative definitions of `A2`–`A4`. No prime label, circle character, mass ledger, or historical scalar is spliced across owners. The manuscript correctly declines Route B because no owner supplies a coherent classical-to-quantum continuation.

## 8. Sources, citations, and integrity

- All nine bibliography entries are cited and all citation keys resolve after BibTeX; no uncited entry or missing key was found.
- The Paper-9 companion PDF exists at `papers/9-packet-separation/paper/paper.pdf` and re-hashes to the cited `c55e4f45fe5f58841864e9af695c4664bdb1a77cff6e087fd2869d4ecd385e02`.
- The corrected Paper-9 locator is Theorem 5.1 and Corollaries 5.2–5.4.
- The Stacks citation points to Section 5.29, Tag `0B1W`; the Pirttimäki author and Hernández title/metadata distinction are correct.
- Twelve retained local source PDFs each have a `PASS` read-integrity sidecar. They are verification copies only; `notes/sources/.gitignore` has the locked hash `6cbf9577be5add7a925718f4047f672fe46d991772fd451f428390aa323b6d3f`.
- The manuscript makes no priority or global-absence claim from the bounded search.
- The AI-assistance statement describes literature support, proof-domain checks, controls, Route checking, and drafting while preserving human responsibility and denying target-zero fitting, randomness, and external-model upload.
- The two native figures satisfy forward claim-to-evidence and reverse use-to-evidence traceability. Their captions and cross marks repeat the actual/proxy/copied limitations visible in the prose.

## 9. Reproduction, build, and visual audit

### 9.1 Clean build

The final source tuple was copied to a fresh temporary directory and built with:

```text
latexmk -xelatex -interaction=nonstopmode -halt-on-error paper.tex
```

Result:

- build exit: PASS;
- clean PDF: 19 A4 pages, no encryption, no JavaScript;
- no undefined citations or references;
- no duplicate labels, missing glyphs, BibTeX errors, LaTeX errors, or overfull boxes;
- four harmless underfull boxes only;
- all eight font families reported embedded, subsetted, and Unicode-mapped;
- `pdfimages -list` reported zero embedded raster images;
- Poppler text extracted from the clean PDF and locked release PDF was byte-identical, SHA-256 `6975224f340f1506c766d7f61af45685bace908c56a16d3670cd16f614101cd5`.

The clean-build PDF hash is not expected to match the release PDF because PDF creation metadata is time-dependent; semantic text identity and source identity were checked instead.

### 9.2 PDF read and visual verification

All 19 pages were visually inspected. The bilingual abstract, theorem displays, Tables 1–3, both TikZ figures, declarations, evidence ledger, references, hyperlinks, wrapping, and page boundaries are legible. The round's sole Minor observation—collision between the Corollary 6.2 QED and the Corollary 6.3 heading on p.12—was repaired by the spacing-only addition at manuscript line 437. The final p.12 was re-rendered and the two theorem blocks are now visibly separated. A byte comparison against the fully inspected preceding source confirmed that this `\medskip` was the only manuscript change in the narrow re-lock.

The ARS `pdf_read_preflight.py` script returned `UNAVAILABLE`, not `FAIL`, solely because `pypdf` is not installed; it nevertheless recorded the correct final PDF hash `30c22eb8...`. This is an inspection-channel limitation, not evidence of a malformed PDF. Independent Poppler checks reported 19 pages, consistent metadata, extractable complete text, embedded fonts, and no encryption or JavaScript.

## 10. Strongest counterargument and release conditions

### 10.1 Strongest counterargument

The strongest skeptical case is that the central collapse engine is a standard general consequence of indiscreteness, the arithmetic indiscreteness input belongs to Paper 9, and the copied-component classification is an elementary coproduct calculation. The manuscript itself now makes the crucial concession:

**Evidence Anchor:** `text: manuscript §1.1, p.4 — "None of these elementary statements is presented as new general topology."`

Accordingly, this paper's nonredundant contribution is not a new general-topology theorem. It is the exact owner-typed assembly on the rational-Witt packet/orbit/quotient family, the direct universal-property and measurable/measure ledgers, the transported-law and circle-direction corrections, the copied/global no-splice boundary, and the formal negative Route adjudication. That is a defensible technical-note or research-program contribution. A venue demanding a major standalone theorem may still judge the advance too narrow; this is a venue-fit risk, not a correctness or integrity defect in the present bounded claim.

### 10.2 Mandatory pre-submission confirmations

These items are already declared provisional and therefore are not hidden weaknesses, but they block a public or journal-facing release until a human confirms them:

1. CRediT roles, funding, competing interests, acknowledgments, affiliation wording, target venue, citation style, license, archive/repository identity, and venue-specific AI disclosure.
2. An immutable public identity for companion Paper 9 after final batch synchronization.
3. A fresh-clone or staged-file audit confirming that all twelve third-party source PDFs remain excluded from the public payload.
4. Re-lock of the final public bytes after any venue-template or declaration changes.

## 11. Questions for the author before public submission

1. Is the intended venue/article type compatible with a tightly scoped technical-note contribution whose main value is typed negative classification rather than a new positive spectral construction?
2. Will the human author confirm every provisional declaration and the immutable Paper-9 identity before any journal-facing or public release?

No answer is required to sustain the internal mathematical verdict; both answers affect publication packaging and venue fit.

## 12. Dimension scores

| Dimension | Score | Descriptor | Notes |
|---|---:|---|---|
| Originality (20%) | 72 | Adequate | General engine is standard; exact owner-typed assembly and no-splice corrections are nonredundant within the program. |
| Methodological rigor (25%) | 97 | Exceptional | Direct proofs, sharp countertargets, exact domains, and owner discipline. |
| Evidence sufficiency (25%) | 96 | Exceptional | Proof audit, authoritative sources, deterministic controls, route records, exact hashes, and build receipts align. |
| Argument coherence (15%) | 97 | Exceptional | Theorems proceed from generic reduction to exact owners, comparison maps, copied controls, and Route consequences without domain drift. |
| Writing quality (15%) | 95 | Strong | Precise bilingual abstract, explicit limits, readable theorem order, and clean final PDF. |
| Literature integration | 91 | Strong | Primary/authoritative sources and precise locators; bounded novelty search is accurately framed. |
| Significance and impact | 70 | Adequate | Strong negative structural prior for the roadmap; limited standalone breadth. |
| **Weighted average** | **91.5** | **Accept** | Exact scientific candidate passes; public release remains conditional as stated. |

## 13. Final exact-lock verdict

**ACCEPT — C0/M0/m0.**

No Critical, Major, Minor, citation-integrity, domain, owner, Route, build, or visual defect remains in the exact tuple of §1. The previous round observations concerning abstract wording, Paper-9 locators, Pirttimäki metadata, Stacks metadata, Route-coordinate definitions, Figure-1 owner branches, Figure-2 component visibility, strict six-key traceability, stale hashes, and p.12 theorem spacing were all closed before this lock.

This verdict does not convert provisional human declarations into confirmed declarations and does not authorize public synchronization of third-party source PDFs. It certifies the bounded scientific manuscript and its current internal release-candidate artifacts.
