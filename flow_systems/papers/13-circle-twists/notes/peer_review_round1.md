# Paper 13 independent peer review — round 1 final

## Manuscript information

- **Title:** *Technical Note: Gauge-Trivial Circle Twists and
  Constant-Diagonal Corona Records for Indiscrete Real Actions*
- **Author:** `AUTHOR TO CONFIRM`
- **Review date:** 2026-08-15 (Asia/Shanghai)
- **Reviewer role:** independent ARS methodology/domain/devil's-advocate
  manuscript reviewer
- **Review focus:** theorem and proof validity; normalization and gauge signs;
  owner, topology, support, and completion typing; prior-result subtraction;
  Technical Note positioning; source and citation integrity; Route semantics;
  frozen deterministic controls; strict figure/table trace; clean build; full
  PDF presentation; and package/release hygiene
- **Final exact-lock verdict:** **MAJOR REVISION / exact-lock FAIL — C0/M2/m1**
- **Confidence:** **5/5**

The mathematical Technical Note is correct on the bounded claims reviewed.
Its explicit NOTE disposition and `STANDALONE_PASS=false` status are coherent
and are **not** findings. The exact frozen package nevertheless cannot receive
an integrity PASS because its six artifact traces do not satisfy the binding
claim-text/locator and forward-link contract, and its frozen project-entry
README contradicts the existence, title, and disposition of the completed
manuscript. One local abstract-count receipt is also inaccurate.

This review was read-only with respect to the candidate. The reviewer edited
no manuscript, bibliography, figure, PDF, README, proof, Route record,
control, result, or source artifact; did not run Git; and did not rerun the
reserved deterministic-control lane. Temporary build and rendering outputs
were confined to `/tmp`. The only project write is this report.

## 1. Exact candidate and evidence lock

### 1.1 Stable REVIEW FREEZE tuple

The following hashes and byte sizes were independently recomputed immediately
before this report was written.

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| `paper/README.md` | 13,716 | `50128376f06600d182d4a9d99ff8a41c58cf79cce3420ce293340f309a550304` |
| `paper/manuscript.tex` | 52,840 | `03f9faec39fbdb0dd182cd6bdc3e118b67dd2fc8e46c8414467a8fe6eb9a1226` |
| `paper/references.bib` | 5,834 | `661aa0a948e8a06538cb300106e91bc9d72e91bf26e9515fdb9a074d0f394292` |
| `paper/figures/owner_support_firewall.tex` | 3,217 | `130ad2f1833a91970629311e1cf21bc848d826afcda941e9b0ad3367cb8f2360` |
| `paper/figures/generic_constant_diagonal.tex` | 2,820 | `727160835b9190b8d3a854825ea30735e4f59813be50a6f7960f3da735558d44` |
| `paper/paper.pdf` | 181,086 | `7d481f6d41f4dbefcbbddf7ffe907ecaa973949c6b595299c124a0c5a3d59830` |
| project `README.md` | 961 | `f9017e72e001430c8620daf1efa6119707bf2250b5c09198c8e98535cf1a1242` |

The `paper/` directory contains exactly these six retained package paths:
the package README, manuscript source, bibliography, two native TikZ sources,
and `paper.pdf`. It contains no build auxiliary, research-source PDF, raster
figure, cache, bytecode, or second generated PDF.

### 1.2 Controlling upstream artifacts

The mandated upstream records were read in full and re-hashed. Principal
locks are:

| Evidence artifact | SHA-256 | Role |
|---|---|---|
| `notes/composition_blueprint.md` | `af7b20a7e1091a876acfa4c22a9f8ba0e9c19b3accd1fe1c1376f6c13fcc48fd` | manuscript, owner, NOTE, and trace contract |
| `notes/proof_audit.md` | `e2f8fb8df4f3418fb3ff0fb60c87f9c7a4ae26cc7470c8c14aec3f86f6df1a63` | integrated proof and owner audit |
| `notes/pre_manuscript_citation_audit.md` | `3ed75cf27d63c84629e02d3b402de8d3e9f419923f9fec43e60fb0b319b5dd73` | literal 17-record citation seed and locator ceilings |
| `notes/phase3_v2_note_disposition_gate.md` | `b60c88a33bb3bb5c4f87448aaaf8f2d4020fa945bc9f204fd81d07ea85d7d03e` | `PASS_TO_TECHNICAL_NOTE` gate |
| `notes/phase3_v2_standalone_review.md` | `ee31c644f9569abecae91ce0ca1054ad480485670caf41cf289a8e3f5ccb0c0e` | binding `NOTE_OR_MERGE`, standalone false |
| `notes/phase3_core_twist_proofs.md` | `62dac0782ba74fea9e8318e0835f7f20eede4cc9963c67471797a006b00decbd` | phase lift, smoothing, signs, and twisted records |
| `notes/phase3_core_peer_review.md` | `a96a91adb1474062656cbca4d677019f952b5fb84775bda952b6c996a700e665` | independent core-proof review |
| `notes/phase3_support_retention_proofs.md` | `f8a0672026b2efaaf07af20d90a17e870e8d0e2f849af0eb78d6dcb1573fb811` | four-output and support proofs |
| `notes/phase3_support_peer_review.md` | `ded657fb7022114527e99a8c0bc12d9f70d9b4ca3f976a6335065190d0640bed` | independent support review |
| `notes/phase3_v2_corona_proofs.md` | `81b0f8aaa1cf6277323452c55107cf33d8ad69783eb80998cc0f4f0d9d636858` | selected component and generic diagonal proofs |
| `notes/phase3_v2_corona_peer_review.md` | `0ae271fd99f3290d7d18486cfc98ad8ccf95aa1421619ccd4fdf72865deb28c8` | independent corona review |
| `notes/phase3_v2_controls_review.md` | `c89a503f0cd624f4a9f119e12fedd0a2c7d6a5b2d55613a1a0e42f3e19917789` | replacement-controls review and remediation closure |
| `results/manifest.json` | `26a41e2920d9a3743cc1b681aa1e32d601dc12e5fded15b3c6349840bd9094c2` | stable replacement-controls manifest |
| `notes/route_audit.md` | `2603502519e087a5023be2fec91e8b332a37d93a1368300a8e103680d6c5b0b9` | exact ten-owner Route adjudication |
| `notes/phase2_framework_source_audit.md` | `b47b1d6319c8419d96ca8679e3ff13b531a58f06a8b14afd95ec11f773345592` | framework-source audit |
| `notes/sources/framework_source_manifest.md` | `4712cabd696d6d00205eb1eddd3c0d2dbf6706bfa14c097690a278941128606e` | source manifestation ledger |
| `notes/sources/framework_sources.sha256` | `7fe6067bfc8e16e8b0447df295a887d48c2c04fa5ba25c9cca8acc7afade733f` | six PDFs plus six preflight sidecars |

All ten final Stage-13 Route-A YAMLs were read, schema-checked through their
audited records, and re-hashed to the ten values bound at
`route_audit.md:109–118`. The Paper 2, 8, 9, 11, and 12 manuscript/proof
premises cited by the owner ledger were also read at the frozen digests bound
in the blueprint, proof audit, and Route audit.

## 2. Review method and overall assessment

The review followed the ARS academic-research-suite reviewer workflow and its
methodology, mathematical-domain, devil's-advocate, peer-review, formatter,
citation-compliance, integrity-verification, figure/table-trace, and complete
PDF-visual instructions. Each asserted theorem was checked from definitions
and signs rather than accepted from the control receipt. Citations were
checked against the locally manifested corpus and the pre-manuscript source
gate. Route and control records were inspected without creating a new run.

On scientific content, the note is unusually careful. It distinguishes the
usual time owner, actual globally indiscrete author records, the bare orbit
set, the deliberately discrete index, and the standard coproduct owner. It
keeps maximal and reduced records separate, restricts its isometry theorem to
selected constant-in-unit images, and states the constant-diagonal theorem
only after those isometries. It neither transfers topology nor names a global
actual twisted groupoid completion. The generic corona statement is correctly
nonselective in the prime and is not presented as a determinant, trace,
spectral object, or owner-specific obstruction.

The direct real-line multiplier proof, twisted product/star signs, support
dichotomy, selected component norm chain, arbitrary-index multiplier lemma,
and fixed-prime specialization are mathematically coherent. No Critical or
mathematical Major finding was found. The exact-lock failure is instead at
the integrity and package-status surfaces described in Section 4.

## 3. Strengths

### S1. The Technical Note disposition is visible and intellectually honest

“Technical Note” appears in the source title, PDF metadata, page-one title,
boxed disposition, English and Simplified-Chinese abstracts, introduction,
and conclusion. The manuscript repeatedly records the NOTE branch and
`STANDALONE_PASS=false`, and it explains why the generic reduction leaves
that status unchanged. This is correct positioning, not a weakness.

**Evidence Anchor:** `manuscript.tex:34–37, 79–94, 97–120, 137–170,
1049–1082; PDF pp. 1, 13–14`

### S2. Prior owners are subtracted before the residual contribution

Sorkin is used only at official-abstract existence strength. Standard
twisted-convolution, gauge, amenability, `c_0`-sum, multiplier, and corona
machinery is not claimed as new. Papers 2, 8, 9, 11, and 12 retain their
respective continuum lower bound, proxy/trace boundary, actual packet and
period, untwisted actual records, and factorization/standardization/comparison
results. The residual centre is described as verification and typed
instantiation rather than promotion.

**Evidence Anchor:** `manuscript.tex:160–216; Table 1, PDF pp. 2–3`

### S3. The collapse proof fixes the exact sign rather than importing it

The lift through `exp(i·)`, vanishing connected cocycle defect, symmetric real
cocycle, smoothing argument, and reconstruction `q=delta(h-A)` establish the
declared normalization and the direction `sigma=delta alpha`. The subsequent
product and involution cancellation uses the same orientation. Different
trivializers differ precisely by a continuous character.

**Evidence Anchor:** `manuscript Theorem thm:collapse and equations
eq:gauge-direction–eq:twisted-star, PDF pp. 4–6`

### S4. Owner transports and nonretention are sharply bounded

The twisted actual test product and both completed author records are defined
through the time formula and the Paper-11 bijection; no general non-Hausdorff
twisted groupoid construction is invoked. Exactly four registered outputs are
constant only after their tags are forgotten. Literal stabilizers, embeddings,
topologies, periods, and representation theory remain.

**Evidence Anchor:** `manuscript.tex:512–613; Proposition prop:four and
Table tab:nonretention, PDF pp. 7–8`

### S5. Support and norm arguments do not cross their evidence domains

The product-support identity gives the zero/finite/infinite compact-support
dichotomy without a countability assumption. On each compact standard orbit,
the reduced equality and maximal upper bound close through amenability only at
the ordinary time endpoint. The resulting isometries concern selected
constant-in-unit images, not whole component algebras.

**Evidence Anchor:** `manuscript Theorem thm:support, equations
eq:support-product, eq:reduced-component, eq:max-component, and Theorem
thm:component-isometry, PDF pp. 8–10`

### S6. The corona lemma is genuinely generic and correctly ordered

For an arbitrary nonempty index set, the note proves the bounded-product
description of the multiplier algebra, exact `c_0` membership criterion, and
distance/quotient norm of a constant isometric diagonal. Only afterward does
it instantiate the theorem separately for maximal and reduced component
families. The fixed-prime result uses only infinitude and cannot recover a
prime or period.

**Evidence Anchor:** `manuscript Theorem thm:generic-diagonal and Corollary
cor:prime, Figure 2, PDF pp. 10–12`

### S7. Controls, Route, and source ceilings are conspicuous

The note says that finite controls diagnose finite sign/support/owner/policy
cases and do not prove continuum, arbitrary-index, norm, or corona theorems.
It reports the remediated replacement tuple, not the historical defective
oracle as current evidence. All Route A2–A4 coordinates fail; Route B is
false; exploratory status is not converted into determinant, analytic,
quantization, or priority evidence. The bounded source search is expressly
unable to establish absence, novelty, priority, or standalone status.

**Evidence Anchor:** `manuscript.tex:973–1047; Table 4, PDF pp. 12–13`

### S8. The manuscript PDF is technically strong

The 15-page A4 PDF is clean, compact, readable, and uses two native-vector
figures. The bilingual abstracts have the same twelve-fact order and the same
negative boundaries. Every page, table, equation, figure, declaration, and
bibliography entry is legible; no typography or PDF-structure defect affects
reviewability.

## 4. Findings requiring revision

### M1. The six-key trace has the right key names but fails strict trace content and forward linkage

This is a blocking integrity finding, not a claim that either figure is
visually wrong or that a caption overstates the mathematics.

All six entries at `paper/README.md:143–207` contain exactly the required key
names. Their `supported_manuscript_claims` values, however, are bare internal
IDs or vague topics rather than claim text plus a manuscript locator:

| Artifact | Frozen `supported_manuscript_claims` value | Manuscript linkage found |
|---|---|---|
| `P13-FIG-01-OWNER-SUPPORT` | `P13-1--2; P13-4--5 typing; P13-8 support` | no reference to `fig:owner-support` |
| `P13-FIG-02-GENERIC-DIAGONAL` | `P13-8B component-to-diagonal chain; P13-8C specialization` | no reference to `fig:generic-diagonal` |
| `P13-TAB-01-OWNER-DICTIONARY` | `Convention and typing claims only` | no reference to `tab:owner-dictionary` |
| `P13-TAB-02-PRIOR-SUBTRACTION` | `Introduction attribution` | no reference to `tab:prior-subtraction` |
| `P13-TAB-03-NONRETENTION` | `P13-6--7` | `tab:nonretention` is referenced at `manuscript.tex:551–554`, but the trace still lacks claim text and locator |
| `P13-TAB-04-LIMITATIONS` | `Section 7 limitations` | no reference to `tab:limitations` |

The only substantive artifact cross-reference in the manuscript is therefore
the Table-3 pointer. The `P13-*` artifact and claim IDs do not occur in the
manuscript. This defeats a reviewer’s ability to follow the declared links.

There is a second check-(1) problem. Transformations such as “Native-vector
TikZ transcription” and “Editorial compression” describe intent but do not
give a script/hash or a precise manual-derivation pointer. Figure 1 also names
only “Paper 12 J premise” for one source input, without a file, hash, theorem,
or section locator. The native figure-source paths and frozen hashes are not
bound inside their entries.

The governing ARS integrity rule is explicit: each listed claim must be claim
text plus locator and must actually reference the artifact; a listed claim
that does not cite the artifact is blocking FAIL. Source data must identify a
real file/dataset, and a manual transformation must be precise enough to
reproduce. Having all six key names does not waive those content checks.

**Required repair:** rewrite all six traces as actual structured entries;
bind exact source paths/hashes and precise section/theorem/manual-derivation
pointers; identify each supported claim by its text and manuscript locator;
make each substantive manuscript claim explicitly reference the matching
figure/table; map each artifact ID unambiguously to its manuscript label; and
perform both forward and reverse linkage checks. Rebuild and re-inspect if
the required manuscript cross-references alter layout. No control rerun is
needed for this repair.

### M2. The frozen project-entry README contradicts the completed Technical Note package

The project `README.md` is part of the explicit freeze tuple. It still gives
the superseded working title *Gauge Collapse of Continuous Circle Twists on
Indiscrete Arithmetic Action Groupoids* (`README.md:3–4`), says the project is
at “initial Phase-1” with no proof, control, Route, manuscript, or release
authorization (`README.md:6–8`), and calls the answer unproved with fresh
proof/source obligations (`README.md:10–16`).

The release prohibition remains correct, but the other status statements are
false for the frozen package: a 15-page completed Technical Note, proof audits,
replacement controls, ten Route records, a citation gate, and a retained
review PDF now exist. The package README discloses that its composition scope
did not authorize editing the parent README (`paper/README.md:21–24`), which
explains the mismatch but does not cure it in an exact package whose parent
README is itself bound for review.

This is not a priority overclaim, and the manuscript itself does not conceal
its disposition. It is nevertheless a major package-status defect because the
repository entry point omits the mandatory Technical Note label and presents
the scientific stage as the opposite of the reviewed candidate. A reader who
does not enter `paper/` receives incorrect title, stage, and proof status.

**Required repair:** update the project README to the exact Technical Note
title; state `NOTE branch`, `STANDALONE_PASS=false`, and the current frozen
review stage; summarize the bounded result and its owner/topology/analytic
ceilings; preserve `RELEASE_AUTHORIZED=false` and the batch-wide public-sync
hold; and stop presenting superseded Phase-1 records as current. Then bind the
new parent-README hash in a new review freeze.

### m1. The Simplified-Chinese abstract count receipt is inaccurate

`paper/README.md:116–121` reports 433 Han characters. Counting Unicode Han
code points in the Chinese abstract prose at `manuscript.tex:131` gives **409**.
The six keyword values contribute 26 Han code points, so abstract plus keyword
values would be 435, not 433. The abstract remains comfortably inside the
required 300–500 range and its twelve-slot semantic parity passes; this is a
receipt/method error, not a content failure.

**Required repair:** state 409 Han code points for abstract prose, or document
an exact reproducible counting boundary and method that matches the number
reported.

### Non-counted clarity edit

At `manuscript.tex:421`, “has a jointly continuous second partial derivative”
can be read as a second-order derivative, whereas the next line uses
`partial_2`, the derivative in the second variable. “Has a partial derivative
in its second variable that is jointly continuous” would remove the ambiguity.
The displayed construction and subsequent differentiation are correct, so
this is not included in the severity count.

## 5. Theorem-by-theorem adjudication

| Result | Audit | Boundary verified |
|---|---|---|
| Theorem `thm:collapse` | PASS | The phase lift, real cocycle, smoothing, integration, gauge sign, and character ambiguity are correct. |
| Twisted test and author transports | PASS | Product, star, regular representation, gauge orientation, and time max/reduced endpoint are checked before transport; no global actual twisted groupoid algebra is named. |
| Proposition `prop:four` | PASS | Exactly the four registered tag-forgotten outputs are asserted constant; literal owner data are retained. |
| Theorem `thm:support` | PASS | The support product and zero/finite/infinite compactness split are valid for a nonempty common-period owner and use no countability premise. |
| Theorem `thm:component-isometry` | PASS | Reduced equality and maximal upper bound close separately through time amenability; only selected images are identified. |
| Theorem `thm:generic-diagonal` | PASS | The arbitrary-index `c_0` sum, bounded multiplier product, membership criterion, distance, and corona norm are correct. |
| Corollary `cor:prime` | PASS | The fixed-prime lower bound remains Paper-2-owned, the elementary upper bound closes cardinality, and the application is nonselective for both completion types. |

## 6. Owner, source, citation, and priority audit

The owner matrix passes. The actual author record, bare orbit set, discrete
index, standard owner, component algebras, and multiplier/corona records stay
separate. Pullback points from standard to actual at the owner level and in
the contravariant function direction. Maximal and reduced records are never
collapsed as ambient algebras. The standard topology is not transferred to
the actual quotient, and literal stabilizers and periods survive gauge-class
collapse.

The citation graph closes exactly:

- 18 citation commands;
- 19 key occurrences;
- 17 unique cited keys;
- 17 bibliography records;
- zero missing, orphan, or duplicate records.

The six retained framework PDFs and six preflight sidecars revalidated 12/12
against `framework_sources.sha256`. Source strength is respected: Sorkin is
used at official title/abstract strength only; Austad Proposition 2.4 and
Leptin Satz 6 retain their exact printed locators; the Hulanicki pagination
anomaly is disclosed; Kleppner is used only for Borel terminology; and the
Buss–Holkar–Meyer and Williams uses remain within their audited component and
ordinary crossed-product domains. Austad–Ortega and Tu remain comparators.

Five companion manuscripts form a substantial part of the 17-entry
bibliography, but every one has a distinct load-bearing owner role, is
identified as a companion manuscript, and is subtracted before the note's
contribution. That dependence is precisely why standalone status remains
false. No “first,” priority, global-absence, or novelty superlative appears.
The dated bounded-search statement is correctly limited to
`SUPPORTED_WITHIN_SEARCH` and explicitly cannot establish priority.

## 7. Route and deterministic-controls audit

### 7.1 Route

PASS. The exact ten Stage-13 YAMLs agree with `route_audit.md`:

- three owner-local records are `ROUTE_A_EXPLORATORY`;
- seven are `ROUTE_A_REJECTED`;
- every A2 record fails with the exact nine required metrics;
- every A3 and A4 record fails;
- every determinant status is
  `NONE_BY_DESIGN_NO_DETERMINANT_OBJECT`;
- every `route_b_invocation_allowed` value is false; and
- no Stage-13 Route-B YAML exists.

The manuscript reports these statuses as bounded negative evidence. It does
not splice coordinates, convert “exploratory” into a positive analytic
signal, or use Paper-2/8/9/11/12 outputs to supply missing Route coordinates.

### 7.2 Controls

PASS at the frozen-evidence boundary. In accordance with the exclusive
sole-runner rule, no controls were rerun. The replacement manifest and all 43
bound edge hashes were independently checked. Its aggregate receipt agrees
with the manuscript:

- 176/176 tests passed;
- 12 CSVs contain exactly 2,665 body rows;
- 67 declared negative controls were detected;
- 13 generated artifacts include the manifest;
- two fresh generations and three checked copies have the recorded identity;
  and
- `proof_binding` remains false/separate, so finite diagnostics are not
  represented as proof.

The independent controls review honestly preserves the historical first-run
oracle defect and its append-only remediation closure. The effective stable
replacement finding is C0/M0/m0. Nothing in the manuscript treats a finite
green row as proof of continuum cardinality, an arbitrary-index identity, a
component norm theorem, or corona faithfulness.

## 8. Bilingual and artifact-content audit

The English abstract has 215 `detex` prose words. The Simplified-Chinese
abstract has 409 Han code points by the prose-only method described under m1.
Both meet their target ranges. Their twelve ordered facts agree: Technical
Note/nonstandalone status; prior and companion ownership; sign-exact collapse;
separate test/maximal/reduced records; exactly four nonretained outputs;
support split; selected component isometries; generic-after-isometries
diagonal lemma; nonselective fixed-prime cases; finite controls as diagnosis;
and no topology/global-completion/trace/determinant/spectral promotion.

Both native-vector figures are mathematically faithful. Figure 1 shows owner
and pullback directions while its firewall and caption deny topology transfer
or a global actual completion. The bare-to-discrete arrow is an explicit act
of assigning the discrete topology, not a transfer of the actual quotient
topology. Figure 2 places arbitrary isometric maps and the generic `c_0`
diagonal before separately typed P13 maximal/reduced instantiations; fixed
prime is shown only as an infinite-index example. All four tables agree with
the surrounding prose. The only artifact defect is the trace linkage in M1.

## 9. Independent clean build, PDF structure, and complete visual review

A clean temporary source copy was built at `/tmp/p13-peer.e5wEEt` using the
documented sequence:

```text
XeLaTeX -> BibTeX -> XeLaTeX -> XeLaTeX -> XeLaTeX
```

All commands returned zero. The final LaTeX log has no actionable warning,
undefined citation/reference, rerun request, overfull/underfull box, missing
character, or duplicate label. BibTeX reports `warning$ -- 0`. Ghostscript
null-page parsing returns zero for both the clean and retained PDFs.

The clean PDF is 15 A4 pages and 181,085 bytes. Its binary SHA differs from
the retained 181,086-byte PDF because PDF build metadata and subset prefixes
are not deterministic across independent runs. Their `pdftotext -layout`
outputs are byte-identical with SHA-256
`8bda7feb8166e3cd64ac0d0f22b52fd4666e5050f4bbfdad565599029ac0512d`.

The retained PDF is unencrypted PDF 1.5 with no form, JavaScript, embedded
file, signature, or raster image. Eight used fonts are embedded, subsetted,
and Unicode mapped: TeX Gyre Termes regular/bold/italic, TeX Gyre Termes Math,
TeX Gyre Cursor regular/italic, and Noto Serif CJK regular/bold. Extracted text
and string scans reveal no workspace path, local source basename, TeX/Bib
source leak, replacement glyph, or embedded-source marker.

All 15 retained-PDF pages were rendered and individually inspected at original
view detail. Both figure pages were additionally rendered at 300 dpi and
inspected at original detail. The title/disposition box, both abstracts, all
four tables, every theorem/equation/proof, both figures and captions,
limitations, declarations, and all 17 references are legible and margin-safe.
There is no clipping, overlap, broken link text, missing CJK glyph, anomalous
blank page, malformed float, split caption, or visually misleading route.

## 10. Package hygiene and source-PDF boundary

Within `paper/`, hygiene passes exactly: six declared files, one PDF, and no
auxiliary/cache residue. In the Paper-13 tree, six research-source PDFs remain
under `notes/sources/` together with their six preflight sidecars; the seventh
PDF is `paper/paper.pdf`. The source `.gitignore` excludes `*.pdf`, and the
manifest/checksum ledgers can be published without publishing those local
verification copies.

Git metadata is absent from this workspace snapshot, and this review did not
run Git. Consequently, a real repository index/stage/archive/upload/
attachment/hidden-path/fresh-clone exclusion proof remains an external release
condition. It is not claimed by this review.

## 11. Strongest counterargument and devil's-advocate assessment

The strongest substantive objection is that the real-line multiplier
collapse and the abstract constant-diagonal lemma are standard or elementary,
while the packet, topology, stabilizer, period, continuum lower bound,
untwisted author records, and standardization are owned elsewhere. A venue may
therefore regard the result as too program-specific for a standalone research
article.

The manuscript accepts that objection rather than evading it. It selects the
Technical Note branch, subtracts all prior owners, and makes precision of
signs, domains, transport, support, selected norm images, and reusable typed
instantiation its purpose. On that bounded purpose, the chain is useful and
correct. The generic lemma is not dressed up as prime-sensitive, and the note
does not claim a trace, determinant, zeta function, analytic continuation,
quantization, or spectral operator. Thus venue breadth may remain a judgment
call, but there is no scientific basis for rejecting the note merely because
`STANDALONE_PASS=false`.

The present revision verdict comes solely from independently fixable package
integrity defects. It does not reopen the resolved standalone gate and does
not require a new mathematical or controls program.

## 12. Required closure and release conditions

### 12.1 Requirements for a new exact-lock peer-review candidate

1. Repair all six artifact traces and their manuscript forward/reverse links
   as specified in M1.
2. Update the project-entry README to the current Technical Note title,
   disposition, scientific stage, and release boundary as specified in M2.
3. Correct or reproducibly define the Chinese abstract count receipt in m1.
4. Clean-build a new retained PDF if manuscript cross-reference edits change
   source bytes; repeat log, font, text, and all-page/figure visual checks.
5. Issue a new exact stable freeze tuple. Any changed candidate byte requires
   tuple-specific re-review. The deterministic controls need not be rerun for
   these documentation/linkage repairs.

### 12.2 External pre-submission/public-release conditions

These conditions are already disclosed and are separate from M1–M2/m1:

1. Human confirmation of the author list/order, affiliations, correspondence,
   ORCID if used, CRediT roles, funding, competing interests,
   acknowledgments, ethics wording, and signed responsibility for every claim
   and citation.
2. Confirmation of venue/article type, template, citation style, AI/tool
   disclosure policy, and data/code availability wording.
3. Honest immutable public identities for the five companion dependencies, or
   self-contained replacement premises/proofs wherever a venue requires a
   standalone record.
4. Human authorization of public repository, tag, archive, license, DOI, and
   final release bytes.
5. Repository/index/archive/upload/fresh-clone evidence that no retained
   `notes/sources/*.pdf` byte enters the public payload.

`RELEASE_AUTHORIZED=false` remains correct. This review does not authorize Git
or public synchronization.

## 13. Dimension scores

| Dimension | Score | Assessment |
|---|---:|---|
| Originality (20%) | 68 | Appropriate for a Technical Note after explicit subtraction; no standalone or priority claim. |
| Methodological rigor (25%) | 97 | Direct sign, support, norm, and arbitrary-index proofs are exact and owner-safe. |
| Evidence sufficiency (25%) | 82 | Sources, controls, Route, and build are strong, but strict artifact provenance/linkage fails. |
| Argument coherence (15%) | 96 | The order from time collapse through selected images to the generic diagonal is exceptionally disciplined. |
| Writing quality (15%) | 92 | Clear bilingual positioning and limitations; one count receipt and one derivative phrase need local repair. |
| Literature integration | 94 | Exact source-strength ceilings and companion ownership; no novelty inflation. |
| Significance and impact | 67 | Useful program-level consolidation with intentionally narrow independent weight. |
| **Weighted average** | **86.6** | **Scientifically strong Technical Note; Major Revision because exact integrity/package gates fail.** |

## 14. Final verdict

| Severity | Count |
|---|---:|
| Critical | **0** |
| Major | **2** |
| Minor | **1** |

**MAJOR REVISION / exact-lock FAIL — C0/M2/m1, confidence 5/5.**

The manuscript's mathematics, owner/type discipline, Technical Note
positioning, source ceilings, Route interpretation, frozen controls, build,
fonts, text, and complete visual presentation pass. `STANDALONE_PASS=false`
is an honest retained disposition and carries no penalty. Acceptance of the
exact frozen package is blocked by (M1) noncompliant strict artifact tracing
and (M2) contradictory frozen repository-entry metadata. The abstract-count
receipt is a local minor item.

No concealment or priority overclaim was found in the manuscript itself. A
new candidate that repairs the trace and project-entry status can be reviewed
without reopening the settled mathematical and control lanes unless its
scientific bytes change materially.

### Machine-readable receipt

```text
P13_PEER_REVIEW_ROUND1=MAJOR_REVISION
P13_EXACT_LOCK_PASS=false
P13_FINDINGS=C0/M2/m1
P13_MATHEMATICS=PASS
P13_NOTE_POSITIONING_MANUSCRIPT=PASS
P13_STANDALONE_FALSE_PENALIZED=false
P13_STRICT_TRACE=FAIL_BLOCKING
P13_PARENT_README_STATUS=FAIL_BLOCKING
P13_CONTROL_RERUN_PERFORMED=false
P13_RELEASE_AUTHORIZED=false
```

This report deliberately does not embed its own digest. Its SHA-256 must be
recorded externally with the final review handoff.

---

## REVIEW FREEZE 2 closure and exact-byte relock addendum

**Addendum date:** 2026-08-15 (Asia/Shanghai)  
**Review mode:** independent exact-byte re-review; append-only closure of the
three REVIEW FREEZE 1 findings  
**Scope rule:** this addendum supersedes the REVIEW FREEZE 1 verdict only for
the exact REVIEW FREEZE 2 tuple below.  The first 32,149 bytes of this file
remain the complete historical round-1 report, byte for byte.

### A. Prefix and candidate identity

Before this addendum was written, the historical report prefix had:

```text
PREFIX_BYTES=32149
PREFIX_LINES=568
PREFIX_SHA256=abca2855cb223390341f44962559c6a82ff1daf21ae84da0a822e7f6c1c52071
```

That digest is the exact REVIEW FREEZE 1 report named in the two candidate
READMEs.  After this append, it is a prefix digest rather than the digest of
the enlarged report file; the final enlarged-file digest is intentionally
recorded in the external handoff, avoiding a self-hash.

The independently rehashed REVIEW FREEZE 2 tuple is:

| Frozen path | Bytes | SHA-256 |
|---|---:|---|
| `paper/manuscript.tex` | 54,338 | `c8c9b7522e9bf63a30ed199fe3468d642cb3e572e324680ccd6893857fbe9701` |
| `paper/references.bib` | 5,834 | `661aa0a948e8a06538cb300106e91bc9d72e91bf26e9515fdb9a074d0f394292` |
| `paper/figures/owner_support_firewall.tex` | 3,217 | `130ad2f1833a91970629311e1cf21bc848d826afcda941e9b0ad3367cb8f2360` |
| `paper/figures/generic_constant_diagonal.tex` | 2,820 | `727160835b9190b8d3a854825ea30735e4f59813be50a6f7960f3da735558d44` |
| `paper/paper.pdf` | 183,120 | `4082ca13a6daadb72ccc30a34fc5160f5920247d3fa3436562349ccc5a9c43c2` |
| `paper/README.md` | 20,956 | `499a4618a0bab9e0a266ca81382a0a084b5016dda45ac0553224171dd4682502` |
| parent `README.md` | 3,511 | `729d2de14046f3004fdcd231a4d0d287e62c9b6e1af95cb592a5918df071120d` |

The paper directory contains exactly the six declared package files and no
LaTeX auxiliaries, caches, temporary outputs, or undeclared raster assets.

### B. Exact revision boundary

I compared the frozen manuscript source against REVIEW FREEZE 1 source
`03f9faec39fbdb0dd182cd6bdc3e118b67dd2fc8e46c8414467a8fe6eb9a1226`.
The complete source diff consists of one formatting macro and seven bounded
trace/back-reference insertions:

1. definition of `\TraceRef`;
2. a post-Table-1 reference to `P13-TAB-02-PRIOR-SUBTRACTION`;
3. a post-Table-2 reference to `P13-TAB-01-OWNER-DICTIONARY`;
4. a pre-Figure-1 reference to `P13-FIG-01-OWNER-SUPPORT`;
5. a Table-3 reference to `P13-TAB-03-NONRETENTION`;
6. a second Figure-1 reference after the support theorem;
7. a pre-Figure-2 reference to `P13-FIG-02-GENERIC-DIAGONAL`; and
8. a Table-4 reference to `P13-TAB-04-LIMITATIONS`.

No equation, definition, theorem, proof, mathematical hypothesis, owner
assignment, scholarly citation, bibliography record, or figure source was
changed.  The new prose faithfully restates the neighboring claims and does
not enlarge them.  The package README changes supply the rebuilt trace
ledger and corrected abstract-count convention; the parent README replaces
the obsolete Phase-1 project stub with the exact Technical Note / NOTE-branch
status and release hold.  This is a properly bounded revision of the three
findings, so reopening settled proof or control design was unnecessary.

### C. Finding-by-finding closure

#### M1 — strict six-key trace: CLOSED

The package README now contains six trace entries.  An independent parse
found exactly the following six keys in every entry, in this order, with no
extra trace field:

```text
artifact_id
source_data
transformation
caption_claim
supported_manuscript_claims
limitations
```

The fields are no longer bare IDs or generic descriptions.  Every
`source_data` field names real paths, exact stable hashes, and section or
theorem/proposition locators.  Every `transformation` field identifies a
specific native-vector serialization or row-preserving editorial extraction,
the destination file/table/label, and, for both figures, the exact unchanged
figure-source digest.  Every `caption_claim` is a concrete bounded claim.
Every `supported_manuscript_claims` field gives claim text plus manuscript
section/label/paragraph locators.

The forward/reverse audit is:

| Artifact | Concrete forward locator in the trace | Reverse manuscript use |
|---|---|---|
| `P13-FIG-01-OWNER-SUPPORT` | owner matrix; Paper-12 Proposition 8.1; support proof; Figure 1 source and `fig:owner-support` | before Figure 1 and after `eq:support-product` / `thm:support` (two occurrences) |
| `P13-FIG-02-GENERIC-DIAGONAL` | corona-proof Theorems 4.3, 5.1, 6.2, 6.3, 7.1, 10.1; Figure 2 source and `fig:generic-diagonal` | paragraph immediately before Figure 2 (one occurrence) |
| `P13-TAB-01-OWNER-DICTIONARY` | proof-audit Sections 3--4; blueprint Section 5; `tab:owner-dictionary` | paragraph immediately after Table 2 (one occurrence) |
| `P13-TAB-02-PRIOR-SUBTRACTION` | proof-audit Sections 2.6 and 11; blueprint Section 8; citation audit Sections 7--8; `tab:prior-subtraction` | paragraph immediately after Table 1 (one occurrence) |
| `P13-TAB-03-NONRETENTION` | support-proof Sections 3--5; exact four-row extraction; `tab:nonretention` | Section 4 opening paragraph before `prop:four` (one occurrence) |
| `P13-TAB-04-LIMITATIONS` | controls-review Addendum A4--A7; Route Sections 2--4; standalone Sections 3 and 6--8; `tab:limitations` | final paragraph of Section 7 (one occurrence) |

Thus all six reverse IDs occur in the manuscript; there are seven literal
occurrences because Figure 1 has two distinct substantive uses.  No
substantive artifact-supported use is omitted.  The scientific limitations
are visible in the relevant captions, surrounding discussion, proposition,
or limitations table: topology/completion and owner firewalls, the
zero/finite/infinite split, nonselectivity, the four-output ceiling, the
non-proof status of dictionaries and prior-credit ledgers, and the
proof/control/Route/search evidence ceilings.  The phrases saying that no
source figure was copied are provenance assurances, not additional
scientific conclusions; they are themselves public in the trace ledger and
do not conceal a limitation.

I rehashed every load-bearing trace source named above.  In particular,
`proof_audit.md`, `composition_blueprint.md`, and
`pre_manuscript_citation_audit.md` remain respectively `e2f8fb8...`,
`af7b20a...`, and `3ed75cf...`; the core, support, corona, standalone,
controls-review, and Paper-12 proof locators exist at their named sections.
The trace is therefore concrete, reproducible at the manual/editorial level
claimed, bidirectional, and integrity-gate compliant.

#### M2 — frozen parent status: CLOSED

The parent README is no longer the obsolete Phase-1 stub.  It identifies the
exact title and article type, selects the NOTE branch, states
`STANDALONE_PASS=false`, labels the files REVIEW FREEZE 2, records the exact
candidate tuple, summarizes only the bounded results, preserves every major
ceiling, and states `RELEASE_AUTHORIZED=false` with the author/publication
fields still `AUTHOR TO CONFIRM`.  It also states that controls were not
rerun and that no Git or public synchronization occurred.  These statements
match the manuscript, package README, standalone review, note-disposition
gate, and actual repository state.  `STANDALONE_PASS=false` is the honest
reason for the Technical Note lane and is not a defect in that lane.

#### m1 — Chinese abstract count receipt: CLOSED

The frozen convention is now explicit and reproducible:

- Simplified Chinese abstract prose body: **409** Unicode `Script=Han`
  characters;
- six Chinese keyword values: **26** Han characters;
- separately named body-plus-keyword-values total: **435**;
- English abstract: **215** prose words.

The 409 body count was reproduced independently by both the documented Perl
range extraction and the documented `awk` range extraction; the keyword
command independently returned 26.  The convention excludes the Chinese
heading and label, punctuation, LaTeX commands, and surrounding prose.  The
12 English/Chinese content slots remain aligned, and both abstracts are
within their required ranges.

### D. Independent scientific, source, Route, and controls re-audit

Because the exact source diff does not alter the mathematics, I checked the
new claim-restatement paragraphs against the already line-by-line audited
equations, proofs, and owner ledger, and then rechecked the affected
cross-references in the built output.  The sign convention, range-first
nerve order, direct real-line lift/trivialization, gauge transport,
four-output nonretention ceiling, support product, component isometries,
generic constant-diagonal theorem, finite/infinite branches, and corona-norm
argument remain correct.  Maximal and reduced records stay separately typed;
actual, bare, discrete, and standard owners remain separated; no selected
image is promoted to a whole-algebra equality.  The NOTE positioning,
generic-versus-owner firewall, and all no-trace/no-determinant/no-priority
ceilings remain conspicuous.  No concealment or priority overclaim was
introduced.

The scholarly graph remains exactly 17 unique cited keys against 17 unique
bibliography records, with zero missing and zero orphan records.  The six
frozen local source PDFs and six preflight JSON records passed the checksum
ledger (12/12).  The literal P13 bibliography seed remains unchanged, so the
pre-manuscript citation audit and source-use ceilings continue to apply.

The Route tuple is unchanged and was rehashed without executing any Route or
control workflow:

- `route_audit.md`:
  `2603502519e087a5023be2fec91e8b332a37d93a1368300a8e103680d6c5b0b9`;
- all ten named Stage-13 YAMLs match the audit ledger;
- exactly three owners remain `ROUTE_A_EXPLORATORY`, seven remain
  `ROUTE_A_REJECTED`, every A2--A4 coordinate fails, and Route B remains
  closed.

The frozen diagnostics also remain unchanged:

- `results/manifest.json`:
  `26a41e2920d9a3743cc1b681aa1e32d601dc12e5fded15b3c6349840bd9094c2`;
- `phase3_v2_controls_review.md`:
  `c89a503f0cd624f4a9f119e12fedd0a2c7d6a5b2d55613a1a0e42f3e19917789`.

They continue to report 176/176 tests, 12 CSVs, 2,665 body rows, and 67
negative controls as diagnostics only.  I did **not** rerun controls, invoke
their generator/test/reproduction entry points, or perform any Git or public
synchronization action.

#### Paper 12 current identity boundary

The Paper-12 title/citation correction has since been relocked.  Its current
identities are:

| Current Paper-12 artifact | SHA-256 |
|---|---|
| `paper/references.bib` | `b763e9c07e3265d878bfc8b4caf44fb6c92ef12e7fac59b8af0bdeb703876175` |
| `paper/paper.pdf` | `9d6747e9f33c6ab3724beb35daedbb0efaff73691ed344374366f2392541ec15` |
| `notes/citation_audit.md` | `79089b2487b6b21c10c1f10a4918fb29602d265877483d7a325634d15ec70a3a` |

The load-bearing Paper-12 manuscript and Proposition-8.1 proof identities
remain unchanged at `c6ad0f8...` and `77258319...`.  Consequently, older
Paper-12 bibliography/PDF/citation-audit identities quoted in frozen P13
upstream receipts are historical receipts, not the present Paper-12 release
identity; they neither alter nor invalidate P13's inherited mathematical
premise.  This downstream identity clarification creates no P13 scientific
or citation-graph finding.

### E. Clean build, PDF, and complete affected-page visual audit

I staged only the frozen manuscript, bibliography, two figure sources, and
retained PDF in `/tmp/p13-peer-freeze2.fwfXvf`, then ran XeLaTeX, BibTeX, and
three further XeLaTeX passes.  All commands exited zero.  The final log has
no actionable warnings/errors, undefined references/citations, missing
characters, or overfull/underfull boxes; BibTeX has zero warnings.
Ghostscript null-page parsing passed for the clean and retained PDFs.

The independent clean PDF and retained PDF are both 15-page A4 PDF 1.5
documents.  Their binary digests differ because the toolchain embeds build
metadata, but `pdftotext -layout` output is byte-identical at
`fe95efd4cb38f2dde1b45a8d92df686f74379261aaf23d032e3db2f1e0b76a6a`.
The retained PDF has the declared title, subject, keywords, Technical Note
framing, and review-stage author placeholder; no form, JavaScript,
encryption, attachment, or signature is present.  All eight font faces are
embedded, subset, and Unicode mapped.  `pdfimages -list` reports zero raster
objects.

Pixel comparison against the fully inspected REVIEW FREEZE 1 render found
pages 1, 5--6, and 9--10 unchanged.  I inspected every affected page
(2--4, 7--8, and 11--15) individually at original detail and found no
clipping, overlap, missing glyph, broken reference, bad float, anomalous
whitespace, or misleading trace placement.  Both native-vector figures were
also rendered independently at 360 dpi and inspected at original detail;
their arrows, labels, mathematical branches, captions, and limitation
firewalls are legible and internally consistent.

### F. Superseding verdict for REVIEW FREEZE 2

**ACCEPT / exact-lock PASS — C0/M0/m0, confidence 5/5.**

All three REVIEW FREEZE 1 findings are closed on the exact tuple above.  The
manuscript is mathematically sound within its stated scope, trace-compliant,
source- and owner-honest, visually release-quality for internal review, and
correctly positioned as a Technical Note.  Its retained
`STANDALONE_PASS=false` status is not penalized.  No concealment, priority
claim, standalone overstatement, controls promotion, or Route promotion was
found.

This verdict authorizes only the exact internal candidate lock.  It does not
change `RELEASE_AUTHORIZED=false`, fill author/publication placeholders, or
authorize a controls rerun, Git action, or public release.  Any later byte
change requires a new hash and appropriate bounded re-review.

### Freeze-2 machine-readable receipt

```text
P13_PEER_REVIEW_FREEZE2=ACCEPT
P13_EXACT_LOCK_PASS=true
P13_FINDINGS=C0/M0/m0
P13_ROUND1_PREFIX_BYTES=32149
P13_ROUND1_PREFIX_SHA256=abca2855cb223390341f44962559c6a82ff1daf21ae84da0a822e7f6c1c52071
P13_FREEZE2_MANUSCRIPT_SHA256=c8c9b7522e9bf63a30ed199fe3468d642cb3e572e324680ccd6893857fbe9701
P13_FREEZE2_PDF_SHA256=4082ca13a6daadb72ccc30a34fc5160f5920247d3fa3436562349ccc5a9c43c2
P13_MATHEMATICS=PASS
P13_NOTE_POSITIONING=PASS
P13_STANDALONE_FALSE_PENALIZED=false
P13_STRICT_TRACE=PASS
P13_PARENT_README_STATUS=PASS
P13_BILINGUAL_COUNT=PASS_409_BODY_26_KEYWORDS_435_TOTAL
P13_CITATION_GRAPH=PASS_17_OF_17
P13_ROUTE_REHASH=PASS_10_OF_10_NO_EXECUTION
P13_CONTROLS_REHASH=PASS_NO_RERUN
P13_PDF_VISUAL=PASS_15_A4_AFFECTED_PAGES_AND_BOTH_FIGURES
P13_P12_CURRENT_IDENTITY_BOUND=true
P13_RELEASE_AUTHORIZED=false
P13_FINAL_REPORT_SHA256=RECORDED_EXTERNALLY
```

As with the historical report, this append-only addendum deliberately does
not embed the digest of the enlarged file.  The external handoff must bind
that final SHA-256 together with the prefix receipt above.

---

## REVIEW FREEZE 2 status-only peer relock addendum

**Relock date:** 2026-08-15 (Asia/Shanghai)  
**Scope:** receipt-only re-review of the two corrected README status indexes
and the completed Paper-12 correction identity  
**Disposition:** **ACCEPT / status-only exact-lock PASS — C0/M0/m0;
`PUBLIC_RELEASE_AUTHORIZED=false`**

This addendum is transparent and append-only. The complete peer report before
this heading is preserved verbatim as an exact **47,090-byte, 858-line**
prefix with SHA-256
`5ef641045f027e3d731f50d950f239c92c2c56771b1384abd6e873a6ee2a75aa`.
All earlier hashes and findings remain visible as historical receipts; the
active README and citation bindings are superseded only by this addendum.

### G. Exact README status delta and inverse receipt

I independently applied the two author-literal unified diffs in the final
citation relock backward, in memory, against the current README bytes. The
project README diff has exactly three hunks, 14 removed lines, and 32 added
lines. Its guarded inverse reconstructs exactly **3,511 bytes / 65 lines** at
the required historical SHA-256
`729d2de14046f3004fdcd231a4d0d287e62c9b6e1af95cb592a5918df071120d`.
The package README diff likewise has exactly three hunks, nine removed lines,
and 32 added lines; its inverse reconstructs exactly **20,956 bytes / 248
lines** at SHA-256
`499a4618a0bab9e0a266ca81382a0a084b5016dda45ac0553224171dd4682502`.
The forward identities independently rehash as:

| Status index | Bytes / lines | Current SHA-256 |
|---|---:|---|
| parent `README.md` | 4,689 / 83 | `ae381531aed12d99c9498d7f2f77afb4899045f5eae2b37cab2431bc855f8990` |
| `paper/README.md` | 22,350 / 271 | `d259e121d7f3a3112171f98bb798a1ae8cc2c723dbb37a99de7310f80474ee9d` |

The exact diffs touch status and receipt prose only. They do not touch any
manuscript input, bibliography datum, artifact trace, proof, control result,
Route record, or source manifestation. The current parent README's one-way
binding to the package README is exact; neither README embeds its own digest
or the digest of the downstream release receipt.

### H. Corrected exact tuple and receipt bindings

Independent re-hashing binds this peer relock to:

| Artifact | SHA-256 |
|---|---|
| parent `README.md` | `ae381531aed12d99c9498d7f2f77afb4899045f5eae2b37cab2431bc855f8990` |
| `paper/README.md` | `d259e121d7f3a3112171f98bb798a1ae8cc2c723dbb37a99de7310f80474ee9d` |
| `paper/manuscript.tex` | `c8c9b7522e9bf63a30ed199fe3468d642cb3e572e324680ccd6893857fbe9701` |
| `paper/references.bib` | `661aa0a948e8a06538cb300106e91bc9d72e91bf26e9515fdb9a074d0f394292` |
| `paper/figures/owner_support_firewall.tex` | `130ad2f1833a91970629311e1cf21bc848d826afcda941e9b0ad3367cb8f2360` |
| `paper/figures/generic_constant_diagonal.tex` | `727160835b9190b8d3a854825ea30735e4f59813be50a6f7960f3da735558d44` |
| `paper/paper.pdf` | `4082ca13a6daadb72ccc30a34fc5160f5920247d3fa3436562349ccc5a9c43c2` |
| `notes/citation_audit.md` | `c12aa9d1207d122ac737b47cc9ea69c3e5ea06d457918ab0129f3b2a70f81ccf` |

The citation report's enlarged-file identity above records **PASS —
STATUS-ONLY CITATION/SOURCE-INTEGRITY RELOCK, C0/M0/m0**. The unchanged first
technical release audit remains
`45eccf26308a0845d0b0bf49cbab0d2120b9c77edbb4418d3832ed22130501ed`
and records technical PASS C0/M0/m0 on the same scholarly bytes; as its own
text states, the later downstream release receipt must separately bind the
corrected README bytes.

The completed Paper-12 correction-freeze release receipt independently
rehashes to
`53afb3642812e981d0bb38b7166982c8818b7ef7085d96277dddd8f632d8d99b`
and records technical PASS C0/M0/m0 with public authorization false. Its
load-bearing manuscript and the Proposition-8.1 proof used by Paper 13 remain
unchanged at, respectively,
`c6ad0f8c22d68840198d744a615da06e8b062d5ccdbeedb7f4ee76bf35073163`
and
`77258319c1e1cbcc08501e33e3c60a03acd71a62342898f3535375e6159f77e8`.
The Paper-12 title correction therefore changes no imported Paper-13 premise.

### I. Freeze-1 findings remain closed

**M1 remains CLOSED.** The current package README still parses to exactly six
artifact entries, each with exactly the six required nonempty keys in the
required order. All six artifact IDs occur in the unchanged manuscript:
five occur once and `P13-FIG-01-OWNER-SUPPORT` occurs twice, for seven
substantive forward/reverse links total. The trace text lies outside all three
README status-diff hunks. Its exact source paths, hashes, manual
transformations, claim text and locators, captions, and visible limitations
therefore retain the accepted Freeze-2 review.

**M2 remains CLOSED.** The current parent index gives the exact Technical Note
title and type, NOTE branch, `STANDALONE_PASS=false`, REVIEW FREEZE 2 internal
candidate stage, peer/citation/technical PASS receipts, bounded theorem
summary, and external-release holds. It no longer presents the obsolete
Phase-1 state. The status is truthful at the exact receipts above.

**m1 remains CLOSED.** The manuscript is unchanged, and two independent
documented extractions again return 409 Han code points for the Simplified-
Chinese abstract body; the keyword extraction returns 26, giving the named
435 body-plus-keyword total. The package README retains that exact convention
outside the status hunks.

All scientific review surfaces remain closed by byte identity. The citation
graph independently recounts to 18 commands, 19 uses, and 17 unique in-text
keys exactly equal to the 17 bibliography keys, with no missing or orphan
entry. The six retained source PDFs and six preflight sidecars pass their
checksum ledger 12/12. The Route audit remains
`2603502519e087a5023be2fec91e8b332a37d93a1368300a8e103680d6c5b0b9`
with ten Route-A records, no Route-B authorization, and no execution. The
frozen controls manifest remains
`26a41e2920d9a3743cc1b681aa1e32d601dc12e5fded15b3c6349840bd9094c2`.
The `paper/` package remains exactly six ordinary files with one retained PDF
and no research-source PDF, auxiliary, cache, raster source, or symlink.

No rebuild is warranted because both READMEs are outside the manuscript build
inputs and the TeX, BibTeX, figure, and retained-PDF bytes are unchanged. No
build, control, Route, Git, archive, upload, or synchronization action was
run. This relock changes only `notes/peer_review_round1.md`; it does not edit
the candidate, citation report, release report, controls, pipeline, locks, or
sources.

### J. Status-only peer disposition

| Severity | Count |
|---|---:|
| Critical | **0** |
| Major | **0** |
| Minor | **0** |

**ACCEPT / status-only exact-lock peer PASS — C0/M0/m0, confidence 5/5.**
The two README corrections accurately report the closed technical gates and
completed Paper-12 relock without changing the reviewed scholarly candidate.
`PUBLIC_RELEASE_AUTHORIZED=false` remains binding pending human declarations,
immutable public companion identities, chosen-venue and then-current policy
checks, real public synchronization/source-PDF exclusion, and explicit human
release authorization. Any later byte change to a bound artifact requires a
new tuple-specific review.

```text
P13_PEER_STATUS_RELOCK=ACCEPT
P13_STATUS_EXACT_LOCK_PASS=true
P13_FINDINGS=C0/M0/m0
P13_HISTORICAL_PREFIX_BYTES=47090
P13_HISTORICAL_PREFIX_LINES=858
P13_HISTORICAL_PREFIX_SHA256=5ef641045f027e3d731f50d950f239c92c2c56771b1384abd6e873a6ee2a75aa
P13_PARENT_README_SHA256=ae381531aed12d99c9498d7f2f77afb4899045f5eae2b37cab2431bc855f8990
P13_PARENT_README_INVERSE_SHA256=729d2de14046f3004fdcd231a4d0d287e62c9b6e1af95cb592a5918df071120d
P13_PACKAGE_README_SHA256=d259e121d7f3a3112171f98bb798a1ae8cc2c723dbb37a99de7310f80474ee9d
P13_PACKAGE_README_INVERSE_SHA256=499a4618a0bab9e0a266ca81382a0a084b5016dda45ac0553224171dd4682502
P13_CITATION_STATUS_RELOCK_SHA256=c12aa9d1207d122ac737b47cc9ea69c3e5ea06d457918ab0129f3b2a70f81ccf
P13_P12_RELEASE_SHA256=53afb3642812e981d0bb38b7166982c8818b7ef7085d96277dddd8f632d8d99b
P13_REBUILD_PERFORMED=false
P13_CONTROLS_RERUN=false
P13_GIT_OR_PUBLIC_SYNC_PERFORMED=false
P13_PUBLIC_RELEASE_AUTHORIZED=false
P13_FINAL_REPORT_SHA256=RECORDED_EXTERNALLY
```

This append-only report deliberately does not self-record its enlarged-file
digest. The external handoff must bind the final SHA-256 together with the
historical prefix receipt above.
