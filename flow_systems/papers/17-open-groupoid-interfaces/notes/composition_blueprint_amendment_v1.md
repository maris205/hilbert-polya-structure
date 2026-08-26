# Paper 17 composition blueprint amendment v1

Amendment date: **2026-08-16 (Asia/Shanghai)**  
Record status: **AUTHOR REMEDIATION RECORD — STABLE ONLY AFTER EXTERNAL HASHING**  
Document ceiling: **future Technical Note planning only**  
Formal gate status: **`C0/M2/m0` remains open pending independent append-only re-review**

This is neither a manuscript nor a source audit. It performs only the two
repairs authorized by the frozen pre-manuscript source-remediation gate:
(1) six claim-text-primary trace-array replacements and (2) one exact Paper-10
local-owner registry row. It creates no publication artifact and grants no
downstream authorization.

## 1. Exact one-way authority binding

The amendment binds the following six authorities by exact repository-relative
path and SHA-256. The binding is one-way: none of these frozen records depends
on this amendment.

| Bound authority | SHA-256 | Lines | Bytes | Role |
|---|---|---:|---:|---|
| `papers/17-open-groupoid-interfaces/notes/phase2_postroute_note_gate.md` | `981ce692e1aea1a067f9792a4c10ddaede4e89eeedc64c2c1ea7d6da27ed35d3` | 384 | 20,891 | ordered-composition authority |
| `papers/17-open-groupoid-interfaces/notes/proof_audit.md` | `c6810e95d15e1ccf0f1dd48045b0f890ebd98fe637c20a9a5e153e10fa1c4934` | 310 | 20,874 | integrated mathematical, owner, domain, control, max-prior, and Route ceiling |
| `papers/17-open-groupoid-interfaces/notes/composition_blueprint.md` | `eac20a67f3638444add12f90ac5dede4c8b3f4ca1773a8afe5586e18d1bff10d` | 554 | 36,343 | immutable base blueprint |
| `papers/17-open-groupoid-interfaces/notes/pre_manuscript_source_gate.md` | `c3feaea13b78d598d50435e8e8016038a28b661729e5490c57cb8285a98e0edf` | 369 | 19,661 | first independent HOLD at `C0/M2/m0` |
| `papers/17-open-groupoid-interfaces/notes/phase2_integrated_gate.md` | `3d1b732bf02a6b2f73b9515a0531fdb77d7960d379c22393079c9e3d200c53c0` | 429 | 24,323 | exact seven-owner registry |
| `papers/17-open-groupoid-interfaces/notes/route_audit.md` | `d70ba9d029ae598863e44dbb049c49607063f682de8f7d8a8e5f2074ae531d15` | 211 | 13,035 | four-exploratory/three-rejected Route disposition |

The sole authorization for this record is also bound exactly:

```text
AUTHORIZING_GATE_PATH=papers/17-open-groupoid-interfaces/notes/pre_manuscript_source_remediation_gate.md
AUTHORIZING_GATE_SHA256=cbde68a9d03204ded7b74c7947b67f106eaf092a59568a64b610d34276c38e52
AUTHORIZING_GATE_LINES=208
AUTHORIZING_GATE_BYTES=9004
```

The seven Stage-17 YAML identities and bytes remain frozen exactly as follows;
this amendment changes no owner, coordinate, disposition, or hash.

| Frozen Stage-17 owner ID | SHA-256 |
|---|---|
| `GEN-INDISC-R-ACTION-TOPOS-QF-CONTROL` | `77db1521f1d7cdc9e030e1c26148472e4fe4a772bc4a7c90c27dcabc26822672` |
| `GEN-INDISC-Z-ACTION-TOPOS-CONTROL` | `47c04d015036dcefc95f315bd862996cd3653885b09584d27ee7e07c1492848e` |
| `DEN-EF-ORBIT-ACTION-GRPD` | `6ea677a679197d053520de03bade7fb3fcba89c6b10aa9eb8a97955883f7ae9d` |
| `DEN-EF-PACKET-ACTION-GRPD-P` | `d3469e7cf52ed9e84ed3a5f79fcf5ca593a6e60e7bdab8a43b47398c24c5cb91` |
| `DEN-EF-ORBIT-STD-CIRCLE-PROXY` | `163dc6153aafc66bb3209ea51cf8199c32d997e921bcac6707f328aacb4de673` |
| `DEN-EF-ORBIT-STD-CIRCLE-COMPARISON-P` | `b191133dfb4a892b78800dac2b435c0ec58e80cc1ced745cdea08112d7bca727` |
| `UNMARKED-PERIOD-SCALING-CONTROL` | `d1de29ee6708c7846b6f03198fbd9335edfd3c6683928201772513681de58e14` |

The effective planning record is exactly:

```text
papers/17-open-groupoid-interfaces/notes/composition_blueprint.md
+ papers/17-open-groupoid-interfaces/notes/composition_blueprint_amendment_v1.md
```

The base bytes and the first independent gate bytes remain historical and
immutable. This amendment does not rewrite or silently supersede either one.
Its only effective replacements are the six arrays in Section 2 below; its
only registry addition is the Paper-10 row in Section 4. Every other base
blueprint statement remains in force.

## 2. M-01 authoritative claim-text-primary replacement arrays

The six arrays below replace only the effective meaning of the six bare-ID
`supported_manuscript_claims` arrays in base-blueprint Section 9. Claim text is
the primary trace value; `claim_id` is an additional join key only.

Each `planned_manuscript_locator` contains a future section and an exact
literal source marker. A marker is unique to one TN claim record and must occur
exactly once in future manuscript source. Repetition of the same marker in
different artifact arrays below is an intentional many-artifacts-to-one-claim
join to that single future occurrence; it does not authorize duplicate
manuscript occurrences. No wildcard, alias, section-only locator, or bare ID
may replace these records. At artifact freeze, the marker must be retained and
the planning locator must be replaced or augmented by an exact line/page,
theorem, table, or figure locator.

### 2.1 T1 — `T1_OWNER_DOMAIN_INTERFACE_FIREWALL`

```yaml
supported_manuscript_claims:
  - claim_id: TN-02
    claim_text: "For the frozen nonempty globally indiscrete right-`H` owner, `G(X,H)` is an open topological groupoid, and its usual nondiscrete-`R` specialization is non-etale."
    planned_manuscript_locator: "Section 3, Generic joint interface; TRACE_CLAIM:TN-02"
  - claim_id: TN-04
    claim_text: "For a nonempty globally indiscrete owner, connected usual `R` gives `B(G(X,R)) ~= Set`, whereas discrete `Z` gives the nontrivial falsifier `B(G(X,Z)) ~= BZ`."
    planned_manuscript_locator: "Section 3, Generic joint interface; TRACE_CLAIM:TN-04"
  - claim_id: TN-08
    claim_text: "The actual inherited owner has `Set/O(R)/2`, whereas the separately imposed standard-circle owner has `BZ/O(S_L x R)/O(S_L)`, with no topology, provenance, or coordinate transfer between them."
    planned_manuscript_locator: "Section 4, Localic gate and actual/standard firewall; TRACE_CLAIM:TN-08"
  - claim_id: TN-10
    claim_text: "Fixed-prime application occurs only after the generic theorem and imports from Paper 9 only actual packet/orbit indiscreteness and the literal stabilizer `(log p)Z`, without recovering `p` or numerical `log p` from the plain interface."
    planned_manuscript_locator: "Section 5, Scale obstruction and fixed-prime application; TRACE_CLAIM:TN-10"
  - claim_id: TN-14
    claim_text: "On the evaluated plain owners and interfaces, no `C*`-algebra, Haar system, measure, trace, determinant, completed divisor, Weil compression, natural quantization, or standard-to-actual transfer is constructed."
    planned_manuscript_locator: "Section 7, Route outcome and limitations; TRACE_CLAIM:TN-14"
```

```text
FORWARD_T1=Every listed claim text and marker must occur at its declared manuscript location and substantively cite T1.
REVERSE_T1=Every substantive manuscript use of T1 must resolve to one listed claim record; incidental layout pointers are excluded, but no data-bearing or inference-bearing use may be omitted.
```

### 2.2 T2 — `T2_THEOREM_PREMISE_EVIDENCE_SEPARATION`

```yaml
supported_manuscript_claims:
  - claim_id: TN-03
    claim_text: "For every nonempty globally indiscrete right-`H`-set in the frozen domain, `B(G(X,H)) ~= B_cont(H)` by a direct classifying-topos calculation."
    planned_manuscript_locator: "Section 3, Generic joint interface; TRACE_CLAIM:TN-03"
  - claim_id: TN-05
    claim_text: "For the frozen globally indiscrete owner, the bare arrow-open quantale is `O(H)` with base frame `2`, and for usual nondiscrete `R` it is nonunital."
    planned_manuscript_locator: "Section 3, Generic joint interface; TRACE_CLAIM:TN-05"
  - claim_id: TN-06
    claim_text: "The bare quantale `O(H)`, the composable-pair comparison `q_H`, and local compactness are distinct premises, and localic reconstruction follows only when the registered conjunction holds."
    planned_manuscript_locator: "Section 4, Localic gate and actual/standard firewall; TRACE_CLAIM:TN-06"
  - claim_id: TN-07
    claim_text: "For the nonsober actual owner, point loss occurs in the passage `Top -> Loc` rather than through a failure of the Protin--Resende reconstruction theorem on its localic input."
    planned_manuscript_locator: "Section 4, Localic gate and actual/standard firewall; TRACE_CLAIM:TN-07"
```

```text
FORWARD_T2=Every listed claim text and marker must occur at its declared manuscript location and substantively cite T2.
REVERSE_T2=Every substantive manuscript use of T2 must resolve to one listed claim record; incidental layout pointers are excluded, but no data-bearing or inference-bearing use may be omitted.
```

### 2.3 T3 — `T3_FINITE_CONTROL_RECEIPT`

```yaml
supported_manuscript_claims:
  - claim_id: TN-12
    claim_text: "The final finite package comprises nine CSVs, 3,436 rows, 84 explicit negatives, 3,352 nonnegative rows, 48 semantic and 42 package mutation classes, 180 passing replacement-run tests, two fresh generations, three byte-identical copies, and zero frozen residue, all as diagnostic and serialization evidence only."
    planned_manuscript_locator: "Section 6, Finite diagnostic controls; TRACE_CLAIM:TN-12"
```

```text
FORWARD_T3=Every listed claim text and marker must occur at its declared manuscript location and substantively cite T3.
REVERSE_T3=Every substantive manuscript use of T3 must resolve to one listed claim record; incidental layout pointers are excluded, but no data-bearing or inference-bearing use may be omitted.
```

### 2.4 T4 — `T4_STAGE17_ROUTE_DISPOSITION`

```yaml
supported_manuscript_claims:
  - claim_id: TN-13
    claim_text: "The seven Stage-17 owners yield four exploratory and three rejected Route-A dispositions; every owner's A2, A3, and A4 value is `FAIL`, and Route B is false."
    planned_manuscript_locator: "Section 7, Route outcome and limitations; TRACE_CLAIM:TN-13"
  - claim_id: TN-14
    claim_text: "On the evaluated plain owners and interfaces, no `C*`-algebra, Haar system, measure, trace, determinant, completed divisor, Weil compression, natural quantization, or standard-to-actual transfer is constructed."
    planned_manuscript_locator: "Section 7, Route outcome and limitations; TRACE_CLAIM:TN-14"
```

```text
FORWARD_T4=Every listed claim text and marker must occur at its declared manuscript location and substantively cite T4.
REVERSE_T4=Every substantive manuscript use of T4 must resolve to one listed claim record; incidental layout pointers are excluded, but no data-bearing or inference-bearing use may be omitted.
```

### 2.5 F1 — `F1_OWNER_INTERFACE_FIREWALL`

```yaml
supported_manuscript_claims:
  - claim_id: TN-08
    claim_text: "The actual inherited owner has `Set/O(R)/2`, whereas the separately imposed standard-circle owner has `BZ/O(S_L x R)/O(S_L)`, with no topology, provenance, or coordinate transfer between them."
    planned_manuscript_locator: "Section 4, Localic gate and actual/standard firewall; TRACE_CLAIM:TN-08"
  - claim_id: TN-10
    claim_text: "Fixed-prime application occurs only after the generic theorem and imports from Paper 9 only actual packet/orbit indiscreteness and the literal stabilizer `(log p)Z`, without recovering `p` or numerical `log p` from the plain interface."
    planned_manuscript_locator: "Section 5, Scale obstruction and fixed-prime application; TRACE_CLAIM:TN-10"
  - claim_id: TN-14
    claim_text: "On the evaluated plain owners and interfaces, no `C*`-algebra, Haar system, measure, trace, determinant, completed divisor, Weil compression, natural quantization, or standard-to-actual transfer is constructed."
    planned_manuscript_locator: "Section 7, Route outcome and limitations; TRACE_CLAIM:TN-14"
```

```text
FORWARD_F1=Every listed claim text and marker must occur at its declared manuscript location and substantively cite F1.
REVERSE_F1=Every substantive manuscript use of F1 must resolve to one listed claim record; incidental layout pointers are excluded, but no data-bearing or inference-bearing use may be omitted.
```

### 2.6 F2 — `F2_EVIDENCE_TO_ROUTE_CEILING`

```yaml
supported_manuscript_claims:
  - claim_id: TN-12
    claim_text: "The final finite package comprises nine CSVs, 3,436 rows, 84 explicit negatives, 3,352 nonnegative rows, 48 semantic and 42 package mutation classes, 180 passing replacement-run tests, two fresh generations, three byte-identical copies, and zero frozen residue, all as diagnostic and serialization evidence only."
    planned_manuscript_locator: "Section 6, Finite diagnostic controls; TRACE_CLAIM:TN-12"
  - claim_id: TN-13
    claim_text: "The seven Stage-17 owners yield four exploratory and three rejected Route-A dispositions; every owner's A2, A3, and A4 value is `FAIL`, and Route B is false."
    planned_manuscript_locator: "Section 7, Route outcome and limitations; TRACE_CLAIM:TN-13"
  - claim_id: TN-14
    claim_text: "On the evaluated plain owners and interfaces, no `C*`-algebra, Haar system, measure, trace, determinant, completed divisor, Weil compression, natural quantization, or standard-to-actual transfer is constructed."
    planned_manuscript_locator: "Section 7, Route outcome and limitations; TRACE_CLAIM:TN-14"
```

```text
FORWARD_F2=Every listed claim text and marker must occur at its declared manuscript location and substantively cite F2.
REVERSE_F2=Every substantive manuscript use of F2 must resolve to one listed claim record; incidental layout pointers are excluded, but no data-bearing or inference-bearing use may be omitted.
```

## 3. Six-key trace preservation and coverage closure

For every artifact above, the base blueprint remains authoritative for the
other five trace keys and their exact nonempty contents:
`artifact_id`, `source_data`, `transformation`, `caption_claim`, and
`limitations`. This amendment changes none of those values. The effective
six-key record for each artifact is those five immutable base values plus its
full replacement `supported_manuscript_claims` array in Section 2.

F1 and F2 remain optional planning proposals subject to the base limit of at
most two code-native vector figures. Their generator paths and final hashes
remain `REQUIRED_AT_ARTIFACT_FREEZE`; this amendment neither creates nor
pretends to freeze a generator or artifact. T1--T4 also remain future artifacts
only. No table, figure, image, generator, or data transformation is produced
here.

| Artifact | Exact effective associations | Items | Forward frozen | Reverse frozen |
|---|---|---:|---|---|
| T1 | `TN-02,TN-04,TN-08,TN-10,TN-14` | 5 | yes | yes |
| T2 | `TN-03,TN-05,TN-06,TN-07` | 4 | yes | yes |
| T3 | `TN-12` | 1 | yes | yes |
| T4 | `TN-13,TN-14` | 2 | yes | yes |
| F1 | `TN-08,TN-10,TN-14` | 3 | yes | yes |
| F2 | `TN-12,TN-13,TN-14` | 3 | yes | yes |

```text
AUTHORITATIVE_REPLACEMENT_ARRAYS=6_OF_6
BASE_ASSOCIATIONS_COVERED=18_OF_18
ITEMS_WITH_EXACT_CLAIM_ID=18_OF_18
ITEMS_WITH_COMPLETE_CLAIM_TEXT=18_OF_18
ITEMS_WITH_SECTION_AND_LITERAL_MARKER=18_OF_18
DISTINCT_CLAIM_MARKERS=11
FORWARD_OBLIGATIONS_FROZEN=6_OF_6
REVERSE_OBLIGATIONS_FROZEN=6_OF_6
OTHER_FIVE_TRACE_KEYS=UNCHANGED_FROM_BASE_AND_NONEMPTY
ACTUAL_ARTIFACT_CREATION_AUTHORIZED=false
```

## 4. M-02 exact Paper-10 source-owner row

The following is the sole row added to the effective minimum source registry:

```text
slug=paper10-separated-reflection-owner
path=papers/10-separated-reflection/paper/manuscript.tex
sha256=27bae88814f16263de444bb1650e4a550d0f0eca327f3c551d7c2097f353d315
role=prior separated/continuous-observable/Borel/measurable/positive-finite-measure collapse and subtraction only
locator=claim ledger lines 132-135; Theorems P10-1 through P10-4 and their scope stops, lines 201-306
```

This row supports only TN-11's explicit “builds on” wording and prior
subtraction. Its four bounded prior roles are the registered P10-1 separated
universal-image collapse, P10-2 continuous-observable collapse, P10-3
Borel/measurable-map collapse on the stated target domain, and P10-4
positive-finite-measure collapse. Their source scope stops remain part of the
locator and cannot be dropped.

The row supplies no support for Paper 17's direct topos/quantale equivalence,
localic-reconstruction inference, fixed-prime substitution, Route result, or
novelty/standalone credit. It does not authorize a general priority claim. It
does not promote the source to standard Borel, compact Hausdorff, Gelfand, or
`C*`-spectral scope, and it supplies no Radon, Haar, invariant-probability,
state, representation, support, disintegration, signed/complex-measure,
operator, trace, or determinant structure.

No P10 proxy, copied-component, measure-selection, operator, trace,
determinant, or Route field may be imported into any Paper-17 owner. In
particular, no P10 field can populate the seven-owner firewall, any A0--A4
coordinate, or the actual/standard comparison.

The effective minimum registry now contains exactly these six records and no
seventh implied record:

| Registry class | Exact source slug | Effective role |
|---|---|---|
| external framework | `moerdijk-1988-classifying-topos` | unchanged base framework role |
| external framework | `forssell-2013-subgroupoids` | unchanged base open-groupoid/equivariant-sheaf/site role |
| external framework | `protin-resende-2012-quantales` | unchanged base quantale/localic-reconstruction role and scope warning |
| local owner P9 | `paper9-actual-owner` | unchanged base actual packet/orbit indiscreteness and literal-stabilizer role only |
| local owner P10 | `paper10-separated-reflection-owner` | the exact TN-11 builds-on/prior-subtraction role frozen above only |
| local owner P11 | `paper11-range-first-owner` | unchanged base range-first/standard-circle/formula owner role |

```text
EFFECTIVE_MINIMUM_REGISTRY_COUNT=6
EXTERNAL_FRAMEWORK_SOURCE_COUNT=3
LOCAL_OWNER_SOURCE_COUNT=3
LOCAL_OWNERS=P9,P10,P11
P10_SUPPORTED_CLAIMS=TN-11_ONLY
P10_SUPPORT_MODE=BUILDS_ON_AND_PRIOR_SUBTRACTION_ONLY
```

A later source lane may add a source only for a separately recorded claim
need. It may not silently enlarge the claim surface. This amendment does not
download, inspect remotely, acquire, cite visibly, or generate a bibliography
entry for any source.

## 5. Frozen non-regression boundaries

The remediation authorization's exact constants are preserved:

```text
DOCUMENT_TYPE_PLANNED=TECHNICAL_NOTE
STANDALONE_PASS=false
TN_CLAIM_IDS=TN-00_THROUGH_TN-14
OWNER_FIREWALL_COUNT=7
STAGE17_ROUTE_A_FILES=7
STAGE17_ROUTE_B_FILES=0
ROUTE_DISPOSITION=4_EXPLORATORY_3_REJECTED
A2_A3_A4_POSITIVE_COUNT=0
PLANNED_TABLES=4
MAX_CODE_NATIVE_VECTOR_FIGURES=2
BILINGUAL_FACT_ORDER=8
CONTROLS_ARE_DIAGNOSTIC_ONLY=true
DETERMINANT_OBJECT_AUTHORIZED=false
STANDARD_TO_ACTUAL_TRANSFER_AUTHORIZED=false
```

Equivalently, all seven Stage-17 owners retain the value `FAIL` at A2, A3, and
A4; Route B remains false; four Route-A owners remain exploratory and
three remain rejected. “Exploratory” grants no analytic, spectral,
determinant, publication, or standalone credit. The owner firewall retains
exactly seven tokens, and no owner, domain, coordinate, or topology transfer
is introduced.

No theorem statement, hypothesis, proof locator, external-source role,
owner/domain token, Route coordinate, control count, declaration boundary,
word/page target, bilingual fact or omission, or release stop is widened by
this amendment. TN-00 through TN-14 remain the full planned claim surface.
The four tables, maximum two optional code-native vector figures, eight-fact
English/Chinese order, same-omission ledger, declarations plan, Technical Note
word/page ceiling, and Route-table-before-References order remain exactly as
specified by the base blueprint.

The following negative boundary remains explicit: Paper 17 constructs no
`C*`-algebra, Haar system, measure, state, representation, trace, determinant,
completed divisor, zero fit, Weil compression, natural quantization, or
standard-to-actual transfer. Controls remain diagnostic and serialization
evidence only, not theorem proof or Route promotion.

## 6. Downstream authorization remains false

Until a fresh independent append-only re-review closes both findings at an
effective `PASS C0/M0/m0`, every downstream surface remains false:

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
```

This amendment cannot close M-01 or M-02 itself. A fresh independent reviewer
must re-hash the six Section-1 authorities and this file, audit all 18 array
items and all twelve direction obligations, verify the P10 bytes/locators/role
and negative ceiling, and append any closure only to the first independent
source gate while preserving its exact first 369 lines and 19,661 bytes.

## 7. Author self-audit and release state

The author-side remediation is internally complete only under the following
ledger; formal finding closure remains reserved to the independent reviewer:

```text
M01_AUTHOR_REPAIR_COMPLETE=true
M02_AUTHOR_REPAIR_COMPLETE=true
FORMAL_M01_CLOSED=false
FORMAL_M02_CLOSED=false
INDEPENDENT_APPEND_ONLY_REREVIEW_REQUIRED=true
SOURCE_CITATION_PREFLIGHT_AUTHORIZED=false
EFFECTIVE_GATE_STATE=HOLD_C0_M2_m0_PENDING_REREVIEW
AMENDMENT_SELF_HASH=EXTERNAL_BY_CONSTRUCTION
```

Self-audit assertions:

1. all six authorized replacement arrays are printed in full and preserve the
   exact 5/4/1/2/3/3 base association cardinalities;
2. all 18 items carry an exact TN ID, complete claim sentence, future section,
   and literal `TRACE_CLAIM:TN-XX` join marker;
3. each artifact has distinct forward and reverse future audit obligations;
4. the five remaining trace keys and their nonempty base contents are not
   altered, and F1/F2 generator paths and hashes remain deferred;
5. the exact P10 path, SHA-256, ledger locator, theorem/scope-stop locator,
   TN-11-only role, and full negative ceiling are present;
6. the effective minimum registry is exactly three named external framework
   records plus the three local owners P9, P10, and P11;
7. Technical Note status, `STANDALONE_PASS=false`, all seven owners, 4/3 Route
   disposition, all A2--A4 failures, Route B false, controls ceiling,
   bilingual/declaration/artifact limits, and every downstream false are
   preserved; and
8. this record does not authorize or contain a manuscript, bibliography,
   citation audit, source acquisition, table, figure, build, Route/control
   change, Git mutation, README edit, release, or public sync.

The stable SHA-256, line count, and byte count for this file must be computed
externally after its final byte is frozen; they must not be embedded into the
file whose hash they describe.
