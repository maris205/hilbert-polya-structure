# Paper 17 pre-manuscript source-gate remediation authorization

Gate date: **2026-08-16 (Asia/Shanghai)**  
Gate role: owner/orchestrator exact-byte authorization after the first
independent composition/source gate  
Verdict: **PASS TO ONE BLUEPRINT AMENDMENT V1; C0/M2/m0 REMAIN OPEN**

```text
CRITICAL_FINDINGS=0
MAJOR_FINDINGS=2
MINOR_FINDINGS=0
OPEN_FINDINGS=M-01,M-02
BLUEPRINT_AMENDMENT_V1_AUTHORIZED=true
INDEPENDENT_APPEND_ONLY_REREVIEW_REQUIRED=true
SOURCE_CITATION_PREFLIGHT_AUTHORIZED=false
```

This gate does not close either finding and is not a source audit.  It permits
one versioned planning amendment and one fresh independent re-review of that
amendment.  It does not permit edits to the frozen base blueprint or any
source acquisition, bibliography, manuscript, table, figure, README, build,
release, Route, control, Git, or public artifact.

## 1. Exact authority tuple

The following current files were read and re-hashed before this authorization:

| Authority | SHA-256 | Lines | Bytes | Role |
|---|---|---:|---:|---|
| `notes/phase2_postroute_note_gate.md` | `981ce692e1aea1a067f9792a4c10ddaede4e89eeedc64c2c1ea7d6da27ed35d3` | 384 | 20,891 | ordered composition authority |
| `notes/proof_audit.md` | `c6810e95d15e1ccf0f1dd48045b0f890ebd98fe637c20a9a5e153e10fa1c4934` | 310 | 20,874 | integrated mathematical/owner ceiling |
| `notes/composition_blueprint.md` | `eac20a67f3638444add12f90ac5dede4c8b3f4ca1773a8afe5586e18d1bff10d` | 554 | 36,343 | immutable base blueprint |
| `notes/pre_manuscript_source_gate.md` | `c3feaea13b78d598d50435e8e8016038a28b661729e5490c57cb8285a98e0edf` | 369 | 19,661 | independent HOLD, C0/M2/m0 |
| `notes/phase2_integrated_gate.md` | `3d1b732bf02a6b2f73b9515a0531fdb77d7960d379c22393079c9e3d200c53c0` | 429 | 24,323 | seven-owner registry |
| `notes/route_audit.md` | `d70ba9d029ae598863e44dbb049c49607063f682de8f7d8a8e5f2074ae531d15` | 211 | 13,035 | four exploratory / three rejected |

The seven Stage-17 YAML hashes remain the exact ordered ledger already bound
by the base blueprint and source gate.  This remediation may not change their
owner IDs, dispositions, coordinates, paths, or bytes.  Every A2, A3, and A4
value remains `FAIL`, and Route B remains false.

## 2. Sole authorized author artifact

Exactly one new file may be created:

```text
papers/17-open-groupoid-interfaces/notes/composition_blueprint_amendment_v1.md
```

The amendment must bind the six authority files in Section 1 by exact path and
SHA-256.  It must identify the effective planning record as
`composition_blueprint.md + composition_blueprint_amendment_v1.md`, without
rewriting or silently superseding the historical bytes of either the base
blueprint or first independent gate.

No other write is authorized during amendment authorship.

## 3. M-01 exact repair contract: six bidirectional trace plans

The amendment must replace the effective meaning of the six bare-ID
`supported_manuscript_claims` arrays for T1--T4 and F1--F2.  It must print all
six authoritative replacement arrays in full.  Each array item must contain
all three fields:

```text
claim_id=<one exact TN-00...TN-14 identifier>
claim_text=<complete, affirmative or explicitly negative claim sentence>
planned_manuscript_locator=<future section plus unique literal source marker>
```

The locator must name the planned section and one unique literal marker of the
form `TRACE_CLAIM:TN-XX`; a section number alone, a topic phrase, `see paper`,
or a bare TN ID is invalid.  The future manuscript lane must preserve those
markers in source and replace or augment the planning locator with exact
line/page or theorem/table/figure locators at artifact freeze.  Claim text is
the primary trace value; the TN ID is only an additional join key.

The amendment must cover, without wildcard, every existing base association:

```text
T1 = TN-02,TN-04,TN-08,TN-10,TN-14
T2 = TN-03,TN-05,TN-06,TN-07
T3 = TN-12
T4 = TN-13,TN-14
F1 = TN-08,TN-10,TN-14
F2 = TN-12,TN-13,TN-14
```

For each of the six artifacts the amendment must also state the two future
audit obligations separately:

1. **Forward:** every listed claim text and marker must occur at the declared
   manuscript location and substantively cite the artifact.
2. **Reverse:** every substantive manuscript use of the artifact must resolve
   to one listed claim record; incidental layout pointers are excluded, but
   no data- or inference-bearing use may be omitted.

The other five trace keys remain unchanged in role and must remain nonempty
where the base blueprint requires content.  This remediation does not
authorize creation of any actual table or figure, and deferred F1/F2 generator
paths and hashes remain obligations for a later artifact freeze.

## 4. M-02 exact repair contract: Paper-10 source owner

The effective minimum primary/local source registry must add exactly one
explicit local-owner row:

```text
slug=paper10-separated-reflection-owner
path=papers/10-separated-reflection/paper/manuscript.tex
sha256=27bae88814f16263de444bb1650e4a550d0f0eca327f3c551d7c2097f353d315
role=prior separated/continuous-observable/Borel/measurable/positive-finite-measure collapse and subtraction only
locator=claim ledger lines 132-135; Theorems P10-1 through P10-4 and their scope stops, lines 201-306
```

The amendment must state that this row supports TN-11's explicit “builds on”
and prior-subtraction wording only.  It does not support Paper-17's direct
topos/quantale equivalence, localic-reconstruction inference, fixed-prime
substitution, Route result, or novelty/standalone credit.  It may not import
P10's proxy, copied-component, measure-selection, operator, trace, determinant,
or Route fields into any Paper-17 owner.

The effective minimum registry after amendment must therefore contain exactly
the three named external framework sources plus the three local owners P9,
P10, and P11.  A later source lane may add a source only through a separately
recorded claim need; it may not silently expand the claim surface.

## 5. Frozen non-regression boundaries

The amendment must preserve all of the following exactly:

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

No theorem statement, hypothesis, proof locator, external-source role,
owner/domain token, Route coordinate, control count, declaration boundary,
word/page target, or release stop may be widened under this remediation.

## 6. Required independent append-only re-review

After the amendment author declares stable bytes and supplies its exact
SHA-256, line count, and byte count, a fresh independent reviewer must:

1. re-read the ARS citation, integrity, claim/reference-alignment, and
   figure/table-trace contracts;
2. independently re-hash every file in Section 1 and the amendment;
3. re-audit all six trace arrays item by item for claim text, unique marker,
   forward coverage, reverse coverage, and correct owner/domain;
4. re-audit the new P10 row, exact local hash/locators, TN-11 use, and negative
   source-role ceiling;
5. recheck TN-00--TN-14, the seven-owner firewall, bilingual eight-fact
   ledger, Route counts, declarations, and all downstream stops from scratch;
   and
6. append its closure only to `notes/pre_manuscript_source_gate.md`, preserving
   the exact first 19,661 bytes and 369 lines at SHA-256
   `c3feaea13b78d598d50435e8e8016038a28b661729e5490c57cb8285a98e0edf`.

Only an effective `PASS C0/M0/m0` may authorize the next independent
source/citation preflight lane.  A reviewer may not repair the amendment or
base blueprint while reviewing them.

## 7. Downstream authorization state

Until the re-review closes both findings, every downstream surface remains
false:

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

```text
P17_PRE_MANUSCRIPT_SOURCE_REMEDIATION_GATE=PASS_TO_ONE_BLUEPRINT_AMENDMENT_V1
OPEN_FINDINGS=C0/M2/m0
SOLE_AUTHOR_WRITE=notes/composition_blueprint_amendment_v1.md
SOLE_REVIEW_WRITE=append_only:notes/pre_manuscript_source_gate.md
THIS_FILE_SELF_HASH=EXTERNAL_BY_CONSTRUCTION
```
