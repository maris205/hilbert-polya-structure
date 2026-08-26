# Paper 17 pre-manuscript composition/source/citation gate

Gate date: **2026-08-16 (Asia/Shanghai)**  
Gate role: independent composition/source/citation preflight, before any source
manifest, bibliography, manuscript, publication artifact, build, or release  
Verdict: **HOLD — blueprint amendment and a fresh independent gate are required**

```text
CRITICAL_FINDINGS=0
MAJOR_FINDINGS=2
MINOR_FINDINGS=0
GATE_VERDICT=HOLD
BLUEPRINT_REVISION_REQUIRED=true
NEXT_SOURCE_CITATION_PREFLIGHT_LANE_AUTHORIZED=false
```

This gate is deliberately narrower than a citation audit of a manuscript:
there is no manuscript and no bibliography to audit. It checks whether the
frozen composition blueprint is internally complete enough to authorize the
next local-only source/citation preflight lane. Under the governing rule, any
Critical, Major, or Minor finding keeps that lane and every later lane closed.

No blueprint, source file, PDF, sidecar, manifest, BibTeX file, manuscript,
figure, table, README, build product, Route record, control, Git state, or
public record was created or changed by this review. No remotely inspected PDF
was retained in the workspace. This gate file is the sole authorized write.

## 1. Method and governing audit contract

The review used the ARS-Codex `academic-research-suite` and read its selected
`academic-pipeline` and `academic-paper` workflows in full. The directly
applicable citation, integrity, claim/reference-alignment, visualization, and
figure-trace instructions were also read in full, including the figure
verification reference and claim-verification protocol.

The controlling artifact-trace rule is material here: each artifact must have
all six keys
`artifact_id`, `source_data`, `transformation`, `caption_claim`,
`supported_manuscript_claims`, and `limitations`. Entries under
`supported_manuscript_claims` use claim text as the primary value and may add
a manuscript locator; a bare claim ID is not a compliant substitute. If a
manifest exists later, manifest and claim IDs may be additional join keys.
Forward checking requires every listed claim to cite the artifact; reverse
checking requires every substantive manuscript use of the artifact to be
covered by a listed claim.

Technical assertions about external literature were checked only against
primary or official records. External inspection was used only to verify
existence, metadata, locator feasibility, and direct support; it did not
authorize a local source registry or source acquisition.

## 2. Frozen-input receipt

Every required input below was read in full and matched the supplied SHA-256.
Line and byte counts are recorded to make this gate reproducible.

| Frozen input | SHA-256 | Lines | Bytes | Result |
|---|---|---:|---:|---|
| `notes/phase2_postroute_note_gate.md` | `981ce692e1aea1a067f9792a4c10ddaede4e89eeedc64c2c1ea7d6da27ed35d3` | 384 | 20,891 | match |
| `notes/proof_audit.md` | `c6810e95d15e1ccf0f1dd48045b0f890ebd98fe637c20a9a5e153e10fa1c4934` | 310 | 20,874 | match |
| `notes/composition_blueprint.md` | `eac20a67f3638444add12f90ac5dede4c8b3f4ca1773a8afe5586e18d1bff10d` | 554 | 36,343 | match |
| `notes/phase2_integrated_gate.md` | `3d1b732bf02a6b2f73b9515a0531fdb77d7960d379c22393079c9e3d200c53c0` | 429 | 24,323 | match |
| `notes/route_audit.md` | `d70ba9d029ae598863e44dbb049c49607063f682de8f7d8a8e5f2074ae531d15` | 211 | 13,035 | match |

The seven Stage-17 Route records also matched exactly:

| Frozen owner record | SHA-256 | Lines | Bytes | Result |
|---|---|---:|---:|---|
| `GEN-INDISC-R-ACTION-TOPOS-QF-CONTROL/2026-08-16-stage17.yaml` | `77db1521f1d7cdc9e030e1c26148472e4fe4a772bc4a7c90c27dcabc26822672` | 90 | 7,008 | match |
| `GEN-INDISC-Z-ACTION-TOPOS-CONTROL/2026-08-16-stage17.yaml` | `47c04d015036dcefc95f315bd862996cd3653885b09584d27ee7e07c1492848e` | 89 | 6,224 | match |
| `DEN-EF-ORBIT-ACTION-GRPD/2026-08-16-stage17.yaml` | `6ea677a679197d053520de03bade7fb3fcba89c6b10aa9eb8a97955883f7ae9d` | 89 | 7,378 | match |
| `DEN-EF-PACKET-ACTION-GRPD-P/2026-08-16-stage17.yaml` | `d3469e7cf52ed9e84ed3a5f79fcf5ca593a6e60e7bdab8a43b47398c24c5cb91` | 89 | 7,441 | match |
| `DEN-EF-ORBIT-STD-CIRCLE-PROXY/2026-08-16-stage17.yaml` | `163dc6153aafc66bb3209ea51cf8199c32d997e921bcac6707f328aacb4de673` | 89 | 7,096 | match |
| `DEN-EF-ORBIT-STD-CIRCLE-COMPARISON-P/2026-08-16-stage17.yaml` | `b191133dfb4a892b78800dac2b435c0ec58e80cc1ced745cdea08112d7bca727` | 89 | 7,249 | match |
| `UNMARKED-PERIOD-SCALING-CONTROL/2026-08-16-stage17.yaml` | `d1de29ee6708c7846b6f03198fbd9335edfd3c6683928201772513681de58e14` | 89 | 6,839 | match |

The seven YAMLs preserve four `exploratory` and three `rejected` outcomes.
Every owner fails A2, A3, and A4; Route B is false; no determinant object is
registered. No YAML provides a hidden coordinate, owner splice, analytic
promotion, or standalone-paper credit.

For claim-locator verification, the review also opened the complete symbolic
proof and the claim-relevant peer-review/local-owner passages. Their current
hashes were:

```text
phase2_topos_quantale_proofs.md=f6c7475b854b3d00b37d3e7f2edca8e8f2f15d92d67ae8bbcdcd71be127b3bb1
phase2_topos_quantale_peer_review.md=9ad4817e32c6da461d7e15eee1bd53d24368b7c55751738c86c8b033caeb796e
paper9_manuscript.tex=24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb
paper10_manuscript.tex=27bae88814f16263de444bb1650e4a550d0f0eca327f3c551d7c2097f353d315
paper11_manuscript.tex=eb1aa4d7060cf1aa53a729e7c7be89a5724a6133ef3bf000cb800bf786de1002
```

These are audit observations, not a source manifest and not permission to
freeze or cite any local owner in a manuscript.

## 3. Findings

### M-01 — all six planned artifact traces use bare claim IDs

Severity: **Major**

Blueprint Sections 9/T1--T4/F1--F2 populate
`supported_manuscript_claims` as follows:

```text
T1=[TN-02,TN-04,TN-08,TN-10,TN-14]
T2=[TN-03,TN-05,TN-06,TN-07]
T3=[TN-12]
T4=[TN-13,TN-14]
F1=[TN-08,TN-10,TN-14]
F2=[TN-12,TN-13,TN-14]
```

Each value is a bare internal ID. Although TN-00--TN-14 have claim text in a
separate matrix, the six trace records themselves do not carry the required
claim-text primary value or a planned manuscript locator. The blueprint calls
this registry strict, freezes the artifact IDs, and makes a stale or missing
trace release-stopping; consequently the defect cannot be deferred as a
cosmetic drafting choice. In its current shape, the trace cannot independently
support the required forward/reverse substantive-use test and would fail the
ARS claim-bearing artifact integrity contract.

Required repair: version the blueprint and replace every listed item with an
entry containing the exact intended manuscript claim text and a planned
section/paragraph locator. The TN ID may remain as an additional internal join
key. Then verify, artifact by artifact, both directions of the linkage and
retain a nonempty, correctly typed limitations value. No figure or table may
be produced before the repaired trace plans pass a fresh independent gate.

### M-02 — TN-11 requires a P10 preflight that the minimum registry does not bind

Severity: **Major**

TN-11's future source-citation action says to preflight exact P10 and P11 local
locators before any visible citation and to use explicit “builds on” wording.
The minimum source registry binds P9 and P11 local owners, but it contains no
P10 source slug, path, hash requirement, or exact locator. The word “minimum”
could permit the later lane to add P10, while the frozen claim-action matrix
could also be read as requiring P10 before that lane is complete. Those two
readings leave the pre-manuscript source boundary ambiguous. This is not a
claim that P10's content is unavailable: the current local P10 manuscript was
readable and had SHA-256
`27bae88814f16263de444bb1650e4a550d0f0eca327f3c551d7c2097f353d315`.
It is a blueprint completeness defect at a citation-requiring claim.

Required repair: use the recommended resolution and add an explicit
`paper10-separated-reflection-owner` row with the exact local path, frozen
hash, and claim-scoped theorem/line locators for the inherited separated,
continuous-observable, Borel, measurable, and positive-finite-measure
collapses. Alternatively, a versioned amendment may remove the P10 visible
citation action and state why TN-11 does not require it. The two states may not
remain implicit.

## 4. TN-00--TN-14 claim/owner/locator audit

Except for the source-registration ambiguity recorded as M-02, the matrix
does not promote a drafting ledger into literature evidence, move a theorem
between owners, or widen a negative claim into an impossibility result.

| Claim | Independent result | Owner/domain and locator check |
|---|---|---|
| TN-00 | pass | Technical Note status and `STANDALONE_PASS=false` agree with the proof, post-Route, and Route dispositions; no citation can change that status. |
| TN-01 | pass | Range-first operations match the symbolic proof and P11 lines 255--277; P11 remains the local formula owner. |
| TN-02 | pass | Open/non-etale split matches Propositions 3.1--3.3; Forssell is limited to framework definitions rather than Paper-17 proof credit. |
| TN-03 | pass | The sheaf/topos equivalence is the note's direct calculation; Moerdijk/Forssell are framework sources only. |
| TN-04 | pass | Connected usual `R` gives `Set`; discrete `Z` gives `BZ` and remains a falsifier, not finite-C3 credit. |
| TN-05 | pass | Bare `O(H)`, base `2`, and usual-`R` nonunitality match the proof; Protin--Resende supplies definitions/domain, not the direct computation. |
| TN-06 | pass | Bare `O(H)`, `q_H`, and local compactness remain three distinct premises; reconstruction is conditional on the registered conjunction. |
| TN-07 | pass | Nonsober point loss is typed at `Top -> Loc`; it is not mislabeled as failure of localic reconstruction. |
| TN-08 | pass | Actual `Set/O(R)/2` and standard `BZ/O(S_L x R)/O(S_L)` remain separate owners; P11 lines 313--324 support only the standard-circle owner. |
| TN-09 | pass | Unequal-period dilation supports unmarked scale nonrecovery; strict time remains extra marker structure. |
| TN-10 | pass | Fixed-prime substitution occurs after the generic theorem; P9 lines 409--426 supplies only actual indiscreteness and literal stabilizer facts. |
| TN-11 | **M-02** | The mathematical subtraction/firewall is supported, but its P10 visible-citation action lacks an explicit minimum-registry binding. |
| TN-12 | pass | The finite receipt remains diagnostic evidence, not theorem proof; historical and replacement tuples stay distinct. |
| TN-13 | pass | Seven exact YAMLs yield four exploratory/three rejected, all A2--A4 fail, and Route B false without aggregation. |
| TN-14 | pass | The absence list is scoped to the evaluated owner/interface and does not claim impossibility for every enrichment. |

No hidden claim promotion was found in the claim text itself. In particular,
TN-03 is not inferred from an etale-only bridge; TN-05 is not promoted to a
reconstruction theorem; TN-07 does not confuse point loss with localic
failure; and TN-14 remains a scoped construction boundary.

## 5. Seven-owner firewall audit

All seven drafting tokens are present and mutually typed:

```text
GENERIC_R_ACTUAL
GENERIC_Z_FALSIFIER
ACTUAL_ORBIT_P
ACTUAL_PACKET_P
STANDARD_CIRCLE_PROXY
ACTUAL_STANDARD_COMPARISON
UNMARKED_SCALING_CONTROL
```

The allowed outputs and nontransferable fields agree with the proof audit and
Stage-17 records. The blueprint prohibits unlabeled owners, equals/transfer
verbs across owners, proxy-to-actual topology transport, marked-to-unmarked
transport, and coordinate union. No eighth owner or hidden domain expansion
was found. Actual orbit and packet applications inherit only the Paper-9
facts; the standard circle stays separately imposed; the comparison owner
does not merge coordinates; and the scaling control receives no arithmetic,
determinant, operator, or Route credit.

## 6. Bilingual eight-fact and same-omission audit

The abstract ledger has exactly eight facts in a fixed order. It preserves:

1. Technical Note/non-standalone status;
2. the parallel generic topos and bare-quantale computations;
3. the connected-`R`/discrete-`Z` contrast;
4. separation of bare `O(H)`, `q_H`, local compactness, and the `Top -> Loc`
   loss location;
5. the actual/standard owner contrast;
6. unmarked scale nonrecovery and strict marking as extra structure;
7. controls as diagnostics/serialization receipts only; and
8. the exact 4/3 Route disposition, all A2--A4 failure, no determinant, and no
   Route B.

The English/Chinese same-order, same-omission, number, owner-token, hedge, and
Route-count checks are explicit. The omission list excludes priority, DOI,
implementation detail, first-run narrative, analytic/operator promotion,
owner transfer, and Route-B entitlement in both languages. No bilingual fact
or omission is internally contradictory. This is a planning-ledger pass only;
no abstract drafting is authorized.

## 7. T1--T4/F1--F2 trace audit

The blueprint plans exactly four tables and at most two optional code-native
vector figures. It prohibits a fifth table, third figure, bitmap/AI art,
decorative imagery, and screenshots without amendment. Every plan contains
the six named keys, has a nonempty limitation, identifies source evidence,
and keeps controls/Route/owner functions separated.

The sole artifact-registry defect is nevertheless global and blocking:
M-01 affects `supported_manuscript_claims` in **all six** plans. Therefore no
individual T1--T4/F1--F2 plan passes the strict trace gate in the frozen
blueprint. Descriptive manual transformations and the deferred generator
hashes for optional F1/F2 are acceptable as planning statements only; at an
actual artifact freeze they must resolve to precise reproducible derivation or
generator pointers and current hashes.

## 8. Minimum source-registry feasibility

This section records feasibility observations, not a source registry, source
manifest, or citation authorization.

### Moerdijk 1988

- Existence/metadata: verified for Ieke Moerdijk, *The classifying topos of a
  continuous groupoid. I*, *Transactions of the American Mathematical
  Society* 310(2), 629--668 (1988), DOI
  [`10.1090/S0002-9947-1988-0973173-9`](https://doi.org/10.1090/S0002-9947-1988-0973173-9).
- Feasibility result: the DOI/title/venue record is real. The blueprint
  intentionally supplies no theorem/page locator; exact source bytes and the
  precise definition/theorem page must still be opened in a later authorized
  lane. Failure to obtain those bytes remains a hard stop.

### Forssell 2013

- Existence/metadata: verified for Henrik Forssell, *Subgroupoids and quotient
  theories*, *Theory and Applications of Categories* 28(18), 541--551 (2013),
  through the [official TAC volume record](https://www.tac.mta.ca/tac/) and
  the [primary author manuscript](https://arxiv.org/pdf/1111.2952).
- Locator check: Section 2.1 on physical pp. 2--3 contains the open
  topological-groupoid definition, equivariant-sheaf setup, Proposition
  2.1.1, and the following Moerdijk-site paragraph. The proposed journal
  pp. 542--543/arXiv pp. 2--3 manifestation is feasible.

### Protin--Resende 2012

- Existence/metadata: verified for Laurent Protin and Pedro Resende,
  *Quantales of open groupoids*, *Journal of Noncommutative Geometry* 6(2),
  199--247 (2012), DOI `10.4171/JNCG/90`, on the
  [official EMS article page](https://ems.press/journals/jncg/articles/4489).
- Locator check: printed pp. 203--205 contain the registered open-groupoid/open
  quantal-frame definitions; Theorems 2.41 and 2.45 occur at printed
  pp. 214--215; printed pp. 245--246 contain the topological/localic and frame
  quotient/tensor warning plus the local-compactness sufficiency boundary.
  These locators are feasible and do not license an etale-only bridge or bare
  quantale reconstruction claim.

### Exact local owners

- P9 current owner: `papers/9-packet-separation/paper/manuscript.tex`, SHA-256
  `24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb`.
  Lines 409--426 support the packet/orbit indiscreteness and literal
  stabilizer boundary used by TN-10.
- P11 current owner: `papers/11-indiscrete-convolution/paper/manuscript.tex`,
  SHA-256
  `eb1aa4d7060cf1aa53a729e7c7be89a5724a6133ef3bf000cb800bf786de1002`.
  Lines 255--277, 313--324, 337--405, and 1079--1087 are feasible exact
  locators for the range-first formulas, standard-circle owner,
  arrow-open/composable-pair facts, and owner-splice stop.
- P10 is readable, but its missing minimum-registry binding is M-02 and cannot
  be silently repaired in this gate.

No source-existence or metadata contradiction was found among the five
explicit minimum-registry entries. That feasibility result does not override
M-01/M-02 or authorize acquisition, citation, bibliography generation, or
manuscript drafting.

## 9. Declarations and release-stop audit

The blueprint requires data/materials, code, ethics, consent, competing
interests, funding, CRediT contributions, acknowledgements, AI-use, and
limitations declarations. Author/institution/funding/ethics facts must be
author-confirmed, and placeholders or inferred “none/not applicable” values
stop release. This is appropriately conservative; no author fact was inferred
by this gate.

The absolute release stops cover hash drift, any nonzero finding, owner/domain
splice, bare-quantale or standard/marked promotion, controls-as-proof, Route
aggregation/promotion, determinant introduction, Route B, unverified or
orphan citations, bilingual drift, stale trace, declaration gaps, rendering
defects, standalone promotion, missing independent audits, and missing release
authorization. No stop is weakened by source availability.

Because this gate has nonzero Major findings, the following state is binding:

```text
SOURCE_REGISTRY_PREFLIGHT=NOT_AUTHORIZED
NOTES_SOURCES_DIRECTORY_WRITE_AUTHORIZED=false
LOCAL_ONLY_PDF_WRITE_AUTHORIZED=false
SOURCE_SIDECAR_WRITE_AUTHORIZED=false
SOURCE_GITIGNORE_WRITE_AUTHORIZED=false
SOURCE_CHECKSUM_LEDGER_WRITE_AUTHORIZED=false
SOURCE_MANIFEST_WRITE_AUTHORIZED=false
PRE_MANUSCRIPT_CITATION_AUDIT_WRITE_AUTHORIZED=false

COMPOSITION_AUTHORIZED=false
MANUSCRIPT_TEX_WRITE_AUTHORIZED=false
REFERENCES_BIB_WRITE_AUTHORIZED=false
TABLE_OR_FIGURE_WRITE_AUTHORIZED=false
README_WRITE_AUTHORIZED=false
BUILD_AUTHORIZED=false
RELEASE_AUTHORIZED=false
ROUTE_CHANGE_AUTHORIZED=false
CONTROL_CHANGE_AUTHORIZED=false
GIT_MUTATION_AUTHORIZED=false
PUBLIC_SYNC_AUTHORIZED=false
STANDALONE_PASS=false
ROUTE_B=false
```

## 10. Re-entry condition

The smallest valid next action is a versioned amendment of
`composition_blueprint.md` that closes M-01 and M-02 without widening the
TN-00--TN-14 claim surface, owner set, proof/domain, source roles, Route
coordinates, document type, or release permissions. That amendment must then
receive a fresh, from-scratch independent composition/source/citation gate.

Only a later independent `C0/M0/m0` result may authorize the separate,
strictly local source/citation preflight lane. Even then, that lane is limited
to local-only PDFs, sidecars, `.gitignore`, checksum/manifest material under
`notes/sources`, and `notes/pre_manuscript_citation_audit.md`; it still cannot
authorize `manuscript.tex`, `references.bib`, figures, tables, README, build,
release, Route/control edits, Git mutation, or public synchronization.

```text
FINAL_GATE_RECEIPT=HOLD
FINDING_COUNTS=C0/M2/m0
BLUEPRINT_SHA256=eac20a67f3638444add12f90ac5dede4c8b3f4ca1773a8afe5586e18d1bff10d
NEXT_AUTHORIZED_LANE=NONE
ONLY_WRITTEN_FILE=notes/pre_manuscript_source_gate.md
```

## 11. Fresh append-only remediation re-review

Re-review date: **2026-08-16 (Asia/Shanghai)**  
Re-review role: fresh independent composition/source/citation preflight after
the single authorized blueprint amendment  
Effective verdict: **HOLD — the two original findings are repaired, but one new
Major ambiguity prevents source-lane authorization**

This section is append-only. It does not relabel the historical first review.
Before this section was appended, both the first 19,661 bytes and the first 369
lines reproduced the complete original gate at the required digest:

```text
PRESERVED_PREFIX_BYTES=19661
PRESERVED_PREFIX_LINES=369
PRESERVED_PREFIX_SHA256=c3feaea13b78d598d50435e8e8016038a28b661729e5490c57cb8285a98e0edf
PRESERVED_PREFIX_MATCH=true
```

The effective finding ledger after the fresh review is:

```text
ORIGINAL_M01_BARE_ID_TRACE_DEFECT=CLOSED
ORIGINAL_M02_MISSING_P10_REGISTRY_BINDING=CLOSED
NEW_M03_OPTIONAL_FIGURE_ACTIVATION_AMBIGUITY=OPEN
CRITICAL_FINDINGS=0
MAJOR_FINDINGS=1
MINOR_FINDINGS=0
GATE_VERDICT=HOLD
NEXT_SOURCE_CITATION_PREFLIGHT_LANE_AUTHORIZED=false
```

### 11.1 Fresh method and exact-byte receipt

The ARS-Codex `academic-research-suite` was re-read for this review. The
`academic-pipeline` and `academic-paper` workflows and the directly applicable
citation-compliance, integrity-verification, claim/reference-alignment,
visualization/figure-trace, VLM figure-verification, and claim-verification
instructions were read in full. In particular, this review reapplied rather
than inherited the requirements that claim text is primary, a bare identifier
is insufficient, every listed claim must substantively reference its artifact,
every substantive artifact use must resolve in reverse, and all six trace keys
must remain supportable.

Every authority required by the remediation gate was then read from the first
line to the last and independently rehashed. The following fresh receipt
matched exactly:

| Authority | SHA-256 | Lines | Bytes |
|---|---|---:|---:|
| `notes/phase2_postroute_note_gate.md` | `981ce692e1aea1a067f9792a4c10ddaede4e89eeedc64c2c1ea7d6da27ed35d3` | 384 | 20,891 |
| `notes/proof_audit.md` | `c6810e95d15e1ccf0f1dd48045b0f890ebd98fe637c20a9a5e153e10fa1c4934` | 310 | 20,874 |
| `notes/composition_blueprint.md` | `eac20a67f3638444add12f90ac5dede4c8b3f4ca1773a8afe5586e18d1bff10d` | 554 | 36,343 |
| `notes/phase2_integrated_gate.md` | `3d1b732bf02a6b2f73b9515a0531fdb77d7960d379c22393079c9e3d200c53c0` | 429 | 24,323 |
| `notes/route_audit.md` | `d70ba9d029ae598863e44dbb049c49607063f682de8f7d8a8e5f2074ae531d15` | 211 | 13,035 |
| `notes/pre_manuscript_source_remediation_gate.md` | `cbde68a9d03204ded7b74c7947b67f106eaf092a59568a64b610d34276c38e52` | 208 | 9,004 |
| `notes/composition_blueprint_amendment_v1.md` | `cfebb477128a3e1a99cb3f9fbedf3e3fce6709cc92d621f6909663f2fc25bddc` | 410 | 23,112 |
| `papers/10-separated-reflection/paper/manuscript.tex` | `27bae88814f16263de444bb1650e4a550d0f0eca327f3c551d7c2097f353d315` | 602 | 61,214 |

The seven Stage-17 YAMLs were also read in full and freshly matched the exact
ordered digests already printed in Section 2:

```text
77db1521f1d7cdc9e030e1c26148472e4fe4a772bc4a7c90c27dcabc26822672
47c04d015036dcefc95f315bd862996cd3653885b09584d27ee7e07c1492848e
6ea677a679197d053520de03bade7fb3fcba89c6b10aa9eb8a97955883f7ae9d
d3469e7cf52ed9e84ed3a5f79fcf5ca593a6e60e7bdab8a43b47398c24c5cb91
163dc6153aafc66bb3209ea51cf8199c32d997e921bcac6707f328aacb4de673
b191133dfb4a892b78800dac2b435c0ec58e80cc1ced745cdea08112d7bca727
d1de29ee6708c7846b6f03198fbd9335edfd3c6683928201772513681de58e14
```

No input drift was found. The unchanged minimum-registry records remain
feasible: the Moerdijk DOI is exact, the official TAC volume still registers
Forssell's 2013 article at pp. 541--551, and the official EMS record still
registers Protin--Resende 2012 at pp. 199--247 with DOI `10.4171/JNCG/90`.
The exact P9 and P11 local-owner rows retain their frozen hashes and bounded
roles. No PDF or other remote content was retained.

### 11.2 Original M-01 closure and many-artifact join result

All six replacement arrays and all 18 items were audited item by item. Their
cardinalities are exactly `5/4/1/2/3/3`; their associations are exactly:

```text
T1=TN-02,TN-04,TN-08,TN-10,TN-14
T2=TN-03,TN-05,TN-06,TN-07
T3=TN-12
T4=TN-13,TN-14
F1=TN-08,TN-10,TN-14
F2=TN-12,TN-13,TN-14
```

Every item has the complete frozen claim sentence as its primary value, the
correct secondary TN ID, a future section, and the unique literal marker
`TRACE_CLAIM:TN-XX`. The 11 distinct marker records are internally unique.
Where one TN record occurs in multiple artifact arrays, its claim text and
locator are byte-for-byte identical. No hidden claim, owner, domain, wildcard,
alias, section-only locator, or bare-ID substitution was found.

All six forward clauses and all six reverse clauses are present. The five
other keys (`artifact_id`, `source_data`, `transformation`, `caption_claim`,
and `limitations`) remain nonempty and unchanged from the base blueprint.
Their manual derivation pointers, caption ceilings, limitations, and deferred
generator/hash requirements are adequate for future planning; they do not
pretend that an artifact has already been frozen.

The repeated-marker semantics are not ambiguous by themselves. Amendment
Section 2 expressly makes a repeated marker a many-artifacts-to-one-claim join
to one future manuscript occurrence. Read together with the artifact-specific
forward clauses, the single substantive occurrence must cite **every active
associated artifact**, not merely one of them. Thus the following joins apply
whenever the associated artifacts are active:

```text
TN-08 -> T1 + F1
TN-10 -> T1 + F1
TN-12 -> T3 + F2
TN-13 -> T4 + F2
TN-14 -> T1 + T4 + F1 + F2
```

One marker must still occur only once; these joins do not license duplicate
claim occurrences. On this basis, the original bare-ID defect M-01 is formally
closed. The unresolved meaning of “active” for optional F1/F2 is the separate
new Major finding below.

### 11.3 Original M-02 closure

The new P10 row resolves to the exact local owner
`papers/10-separated-reflection/paper/manuscript.tex` at SHA-256
`27bae88814f16263de444bb1650e4a550d0f0eca327f3c551d7c2097f353d315`.
Lines 132--135 are exactly the P10-1 through P10-4 claim-ledger rows. The named
theorems and their scope stops occur at lines 201--226, 228--245, 270--285,
and 287--306. P10-5 happens to occur inside the broad 201--306 span, but the
row names only P10-1 through P10-4 and amendment lines 257--268 expressly
exclude operator, proxy, copied-component, measure-selection, trace,
determinant, Route, and owner-firewall imports. The locator therefore does not
promote P10-5.

The effective role is limited to TN-11's “builds on” wording and prior
subtraction. It supplies no direct Paper-17 theorem, topos/quantale,
fixed-prime, novelty, standalone, operator, analytic, trace, determinant, or
Route credit. The effective registry is exactly the three external framework
records plus P9, P10, and P11, with no implied seventh source. Original M-02 is
formally closed.

### 11.4 New Major finding M-03 — optional figures versus unconditional forward obligations

The base blueprint says at line 275 that figures are optional and may be
omitted if T1/T2 communicates the relation more clearly. Amendment lines
209--214 repeat that F1 and F2 remain optional future planning proposals.
However, amendment lines 176 and 196 unconditionally require every listed
claim text and marker to occur and substantively cite F1 or F2, and lines
232--233 freeze all six forward and reverse obligations. There is no `if
adopted`, `if included`, artifact-activation, or omission branch anywhere in
the effective blueprint.

These rules cannot be jointly applied as written. A permitted omission of F1
would leave the unique TN-08, TN-10, and TN-14 occurrences required to cite a
nonexistent F1. A permitted omission of F2 would analogously leave TN-12,
TN-13, and TN-14 required to cite a nonexistent F2. Reverse coverage would be
vacuous for an omitted figure, but the unconditional forward obligation would
remain unsatisfied. Under the governing integrity and trace rules, the reviewer
cannot silently rewrite “must cite” as “must cite only if adopted.”

Severity is **Major** because the ambiguity controls six figure associations,
including the four-way TN-14 join, and prevents a deterministic future
claim-to-artifact citation audit. The smallest coherent repair is an explicit
activation rule stating that T1--T4 obligations are unconditional, F1/F2
obligations activate if and only if that figure is adopted and frozen, an
omitted figure imposes no manuscript citation obligation, and each unique
claim occurrence cites all active associated artifacts. The generic `6_OF_6`
freeze should be split or qualified so it cannot contradict optionality.

This review does not make that repair and does not modify either blueprint.

### 11.5 Fresh non-regression and fail-closed disposition

Apart from M-03, the full non-regression audit passes. TN-00 through TN-14
remain the complete claim surface; `DOCUMENT_TYPE_PLANNED=TECHNICAL_NOTE` and
`STANDALONE_PASS=false` remain binding. Exactly seven owners remain isolated,
with no actual/standard, strict/unmarked, control/theorem, source/novelty, or
cross-paper field transfer. The English and Chinese ledgers retain the same
eight facts, order, numbers, owner tokens, hedges, and omissions.

The seven Stage-17 records remain four exploratory and three rejected. Every
owner's A2, A3, and A4 value is `FAIL`; Route B is false. Controls remain
diagnostic/serialization evidence only. The declaration requirements,
author-confirmation stops, citation/orphan stops, independent-audit stops,
rendering stops, and release stops are unchanged. No hidden owner, domain,
claim, external-source role, coordinate, publication, analytic, spectral,
operator, determinant, or standalone promotion was found.

Because M-03 remains open, this gate authorizes no source/citation preflight
lane and no later lane:

```text
SOURCE_REGISTRY_PREFLIGHT_AUTHORIZED=false
NOTES_SOURCES_DIRECTORY_WRITE_AUTHORIZED=false
LOCAL_ONLY_PDF_WRITE_AUTHORIZED=false
SOURCE_SIDECAR_WRITE_AUTHORIZED=false
SOURCE_GITIGNORE_WRITE_AUTHORIZED=false
SOURCE_CHECKSUM_LEDGER_WRITE_AUTHORIZED=false
SOURCE_MANIFEST_WRITE_AUTHORIZED=false
PRE_MANUSCRIPT_CITATION_AUDIT_WRITE_AUTHORIZED=false

MANUSCRIPT_TEX_WRITE_AUTHORIZED=false
REFERENCES_BIB_WRITE_AUTHORIZED=false
TABLE_OR_FIGURE_WRITE_AUTHORIZED=false
README_WRITE_AUTHORIZED=false
BUILD_AUTHORIZED=false
RELEASE_AUTHORIZED=false
ROUTE_CHANGE_AUTHORIZED=false
CONTROL_CHANGE_AUTHORIZED=false
GIT_MUTATION_AUTHORIZED=false
PUBLIC_SYNC_AUTHORIZED=false
STANDALONE_PASS=false
ROUTE_B=false
```

```text
FRESH_REREVIEW_RECEIPT=HOLD
EFFECTIVE_FINDING_COUNTS=C0/M1/m0
ORIGINAL_M01_CLOSED=true
ORIGINAL_M02_CLOSED=true
NEW_M03_OPEN=true
NEXT_AUTHORIZED_LANE=NONE
ONLY_WRITTEN_FILE=notes/pre_manuscript_source_gate.md
THIS_FILE_FULL_SHA256=EXTERNAL_BY_CONSTRUCTION
```

## 12. Second fresh append-only v2 closure review

Date: 2026-08-17

Role: independent composition/source/citation preflight reviewer

Effective verdict after this append: **PASS — C0/M0/m0**

This is an append-only re-review. It preserves the M-01, M-02, and M-03
history above and evaluates the effective ordered contract: base blueprint,
amendment v1, then amendment v2. V2 supersedes only the v1 aggregate
obligation language that it expressly identifies.

### 12.1 Prefix, method, and frozen-input receipt

Both required historical prefixes were verified before this append:

| Prefix | Lines | Bytes | SHA-256 | Result |
|---|---:|---:|---|---|
| original source-gate prefix | 369 | 19,661 | c3feaea13b78d598d50435e8e8016038a28b661729e5490c57cb8285a98e0edf | exact |
| complete pre-v2-review file | 601 | 30,763 | 98282784211647b9c842110f5bdc04afbc7190b45c9089f0d77d4e7d61c7d68e | exact |

The ARS academic-pipeline and academic-paper workflows and the directly
applicable citation-compliance, integrity-verification,
claim/reference-alignment, visualization/figure-trace, and
claim-verification rules were reread in full. The controlling test remains
six-key trace closure with claim text primary and both forward and reverse
substantive-use checks.

The following inputs were freshly read and byte-checked:

| Frozen input | SHA-256 | Lines | Bytes |
|---|---|---:|---:|
| notes/pre_manuscript_source_remediation_gate_v2.md | 64f33377f45b37943934da7dffbe70f601acf4aac24b1601a5195944aa1422c9 | 141 | 6,003 |
| notes/composition_blueprint.md | eac20a67f3638444add12f90ac5dede4c8b3f4ca1773a8afe5586e18d1bff10d | 554 | 36,068 |
| notes/composition_blueprint_amendment_v1.md | cfebb477128a3e1a99cb3f9fbedf3e3fce6709cc92d621f6909663f2fc25bddc | 410 | 23,112 |
| notes/composition_blueprint_amendment_v2.md | b95331e40c7c587568522497a73af09ba0d6d9cf0e9a7dac128c93114c8869b1 | 466 | 20,872 |
| notes/proof_audit.md | c6810e95d15e1ccf0f1dd48045b0f890ebd98fe637c20a9a5e153e10fa1c4934 | 310 | 18,084 |
| notes/phase2_integrated_gate.md | 3d1b732bf02a6b2f73b9515a0531fdb77d7960d379c22393079c9e3d200c53c0 | 429 | 21,183 |
| notes/route_audit.md | d70ba9d029ae598863e44dbb049c49607063f682de8f7d8a8e5f2074ae531d15 | 211 | 12,369 |
| papers/10-separated-reflection/paper/manuscript.tex | 27bae88814f16263de444bb1650e4a550d0f0eca327f3c551d7c2097f353d315 | 602 | 61,214 |

The exact P9/P10/P11 manuscript hashes remain, respectively:
24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb,
27bae88814f16263de444bb1650e4a550d0f0eca327f3c551d7c2097f353d315,
and eb1aa4d7060cf1aa53a729e7c7be89a5724a6133ef3bf000cb800bf786de1002.

The seven Stage-17 YAMLs were reread and matched their frozen hashes:

| Owner ID | SHA-256 |
|---|---|
| GEN-INDISC-R-ACTION-TOPOS-QF-CONTROL | 77db1521f1d7cdc9e030e1c26148472e4fe4a772bc4a7c90c27dcabc26822672 |
| GEN-INDISC-Z-ACTION-TOPOS-CONTROL | 47c04d015036dcefc95f315bd862996cd3653885b09584d27ee7e07c1492848e |
| DEN-EF-ORBIT-ACTION-GRPD | 6ea677a679197d053520de03bade7fb3fcba89c6b10aa9eb8a97955883f7ae9d |
| DEN-EF-PACKET-ACTION-GRPD-P | d3469e7cf52ed9e84ed3a5f79fcf5ca593a6e60e7bdab8a43b47398c24c5cb91 |
| DEN-EF-ORBIT-STD-CIRCLE-PROXY | 163dc6153aafc66bb3209ea51cf8199c32d997e921bcac6707f328aacb4de673 |
| DEN-EF-ORBIT-STD-CIRCLE-COMPARISON-P | b191133dfb4a892b78800dac2b435c0ec58e80cc1ced745cdea08112d7bca727 |
| UNMARKED-PERIOD-SCALING-CONTROL | d1de29ee6708c7846b6f03198fbd9335edfd3c6683928201772513681de58e14 |

### 12.2 M-03 adversarial closure

ARTIFACT_ACTIVE is closed over exactly T1, T2, T3, T4, F1, and F2. T1--T4
are unconditionally active planning artifacts; that status neither asserts
existing manuscript bytes nor authorizes creation. F1 and F2 independently
begin OPTIONAL_UNDECIDED and inactive. Each can leave that state exactly once:

1. ADOPTED requires the complete receipt, code-native artifact path and
   current hash, generator path and current hash, current six-key trace
   locator and hash, a positive artifact/generator/trace match, and co-freeze
   at a later authorized freeze point.
2. OMITTED requires the complete receipt, a nonempty composition rationale,
   and independently checked zero artifact objects, zero substantive
   manuscript mentions, and zero activated obligations.

Incomplete, stale, mismatched, inferred, or merely planned evidence cannot
trigger either transition. A terminal state cannot reopen, switch, or be
inferred from absence. The same predicate governs both trace directions:
T1--T4 impose four unconditional forward/reverse obligations; F1 and F2 impose
two conditional forward/reverse obligations, each only when validly ADOPTED.
An inactive figure permits no caption, label, cross-reference, citation,
inference, incidental pointer, or other manuscript use.

The six frozen arrays remain 18 exact associations:

| Artifact | Associated TN records |
|---|---|
| T1 | TN-02, TN-04, TN-08, TN-10, TN-14 |
| T2 | TN-03, TN-05, TN-06, TN-07 |
| T3 | TN-12 |
| T4 | TN-13, TN-14 |
| F1 | TN-08, TN-10, TN-14 |
| F2 | TN-12, TN-13, TN-14 |

Claim text, section plus unique TRACE marker, and repeated TN text remain
exact. A marker occurs once in the future manuscript. Its one substantive
claim occurrence must cite every and only active associated artifacts:

    ACTIVE_JOIN(c) = {a | c is associated with a and ARTIFACT_ACTIVE(a)}.

This many-artifact join never licenses duplicate claim occurrences. Reverse
closure also rejects an active artifact used substantively under an
unassociated TN record.

All seven required branch tests close:

| Branch | Required active optional artifacts | Result |
|---|---|---|
| F1 undecided / F2 undecided | none | PASS |
| F1 adopted / F2 undecided | F1 | PASS |
| F1 omitted / F2 undecided | none; F1 zero-use | PASS |
| F1 undecided / F2 adopted | F2 | PASS |
| F1 undecided / F2 omitted | none; F2 zero-use | PASS |
| both adopted | F1 and F2 | PASS |
| both omitted | none; both zero-use | PASS |

The mixed adopted/omitted terminal combinations are the conjunction of the
matching independent cases. Counterexamples using an incomplete adopted
receipt, stale hash, failed trace match, incomplete omission receipt, inactive
incidental pointer, or active-but-unassociated citation all fail closed. No
hidden adoption, duplicate occurrence, or orphan substantive use remains.

**M-03 disposition: CLOSED.**

### 12.3 M-01, M-02, source, and firewall non-regression

M-01 remains closed. The six arrays retain exact claim text, section plus
unique marker, and consistent duplicate TN text: 18 associations across 11
distinct TN records, six forward clauses, and six reverse clauses. V2 changes
only activation of the two figure obligations and deletes no association.

M-02 remains closed. The exact P10 row binds its path and hash, the ledger at
lines 132--135, and named P10-1 through P10-4 theorem blocks within lines
201--306. Its TN-11-only negative ceiling permits prior-work subtraction and
builds-on wording but no operator, analytic, coordinate, spectral,
determinant, publication, or other P10 result. P10-5 is not promoted.

The minimum registry remains exactly Moerdijk 1988 (DOI
10.1090/S0002-9947-1988-0973173-9), Forssell 2013 Section 2.1,
Protin--Resende 2012 (DOI 10.4171/JNCG/90), and exact local owners P9, P10,
and P11. The external records remain existence- and manifestation-feasible
under the previously verified primary/official records. V2 adds no technical
claim or source. No PDF, manifest, bibliography, or manuscript was created.

TN-00--TN-14, the owner/locator matrix, Technical Note status,
STANDALONE=false, bilingual eight-fact identity, and same-omission rule show
no regression. The seven owners remain four exploratory and three rejected;
every A2, A3, and A4 remains FAIL, and Route B remains false. Controls stay
diagnostic/serialization evidence only. No owner, domain, claim, transfer,
source role, coordinate, publication, analytic, spectral, operator,
determinant, or standalone promotion was found. All declarations,
author-confirmation stops, citation/orphan stops, independent-audit stops,
rendering stops, and release stops remain binding.

### 12.4 Effective finding ledger and narrow authorization

| Finding | Effective status |
|---|---|
| M-01 | CLOSED by v1; no v2 regression |
| M-02 | CLOSED by v1; no v2 regression |
| M-03 | CLOSED by v2 |

Fresh effective counts are **C0/M0/m0** and the effective verdict is
**PASS**.

The only authorized next lane is local-only source acquisition under
papers/17-open-groupoid-interfaces/notes/sources (PDFs, sidecars, its
.gitignore, checksum ledger, and manifest) plus
papers/17-open-groupoid-interfaces/notes/pre_manuscript_citation_audit.md.

    NEXT_SOURCE_CITATION_PREFLIGHT_LANE_AUTHORIZED=true
    SOURCE_CITATION_PREFLIGHT_AUTHORIZED=true
    SOURCE_REGISTRY_PREFLIGHT_AUTHORIZED=true
    LOCAL_ONLY_SOURCE_ACQUISITION_WITHIN_NOTES_SOURCES_AUTHORIZED=true
    NOTES_SOURCES_DIRECTORY_WRITE_AUTHORIZED=true
    LOCAL_ONLY_PDF_WRITE_AUTHORIZED=true
    SOURCE_SIDECAR_WRITE_AUTHORIZED=true
    SOURCE_GITIGNORE_WRITE_AUTHORIZED=true
    SOURCE_CHECKSUM_LEDGER_WRITE_AUTHORIZED=true
    SOURCE_MANIFEST_WRITE_AUTHORIZED=true
    PRE_MANUSCRIPT_CITATION_AUDIT_WRITE_AUTHORIZED=true
    AUTHORIZED_SOURCE_ROOT=papers/17-open-groupoid-interfaces/notes/sources
    AUTHORIZED_AUDIT_PATH=papers/17-open-groupoid-interfaces/notes/pre_manuscript_citation_audit.md

Every downstream or unrelated permission remains false:

    COMPOSITION_WRITE_AUTHORIZED=false
    BLUEPRINT_OR_AMENDMENT_WRITE_AUTHORIZED=false
    MANUSCRIPT_WRITE_AUTHORIZED=false
    MANUSCRIPT_TEX_WRITE_AUTHORIZED=false
    BIBLIOGRAPHY_WRITE_AUTHORIZED=false
    REFERENCES_BIB_WRITE_AUTHORIZED=false
    MANUSCRIPT_CITATION_AUDIT_WRITE_AUTHORIZED=false
    ARTIFACT_FREEZE_AUTHORIZED=false
    FIGURE_ADOPTION_OR_OMISSION_RECEIPT_WRITE_AUTHORIZED=false
    FIGURE_ARTIFACT_WRITE_AUTHORIZED=false
    TABLE_OR_FIGURE_WRITE_AUTHORIZED=false
    README_WRITE_AUTHORIZED=false
    BUILD_AUTHORIZED=false
    RELEASE_AUTHORIZED=false
    ROUTE_CHANGE_AUTHORIZED=false
    CONTROL_CHANGE_AUTHORIZED=false
    GIT_MUTATION_AUTHORIZED=false
    PUBLIC_SYNC_AUTHORIZED=false
    STANDALONE_PASS=false
    ROUTE_B=false

    SECOND_FRESH_REREVIEW_RECEIPT=PASS
    EFFECTIVE_FINDING_COUNTS=C0/M0/m0
    ORIGINAL_M01_CLOSED=true
    ORIGINAL_M02_CLOSED=true
    NEW_M03_CLOSED=true
    ONLY_WRITTEN_FILE=notes/pre_manuscript_source_gate.md
    THIS_FILE_FULL_SHA256=EXTERNAL_BY_CONSTRUCTION

## 13. Append-only metadata correction receipt

The post-append mechanical verification found four byte-count transcription
errors in Section 12.1. The SHA-256 values and line counts there are correct;
the authoritative byte counts are:

| Frozen input | Correct bytes |
|---|---:|
| notes/composition_blueprint.md | 36,343 |
| notes/proof_audit.md | 20,874 |
| notes/phase2_integrated_gate.md | 24,323 |
| notes/route_audit.md | 13,035 |

No input byte, finding analysis, authorization, or verdict changes. This
append-only correction supersedes only the four erroneous Section 12.1 byte
cells. All other Section 12 receipts remain effective.

    REPORT_METADATA_CORRECTIONS=4
    INPUT_SHA256_MISMATCHES=0
    PREFIX_MISMATCHES=0
    EFFECTIVE_FINDING_COUNTS=C0/M0/m0
    EFFECTIVE_VERDICT=PASS
    THIS_FILE_FULL_SHA256=EXTERNAL_BY_CONSTRUCTION
