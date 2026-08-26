# Paper 17 composition blueprint amendment v2

Amendment date: **2026-08-16 (Asia/Shanghai)**  
Record role: **optional-artifact activation remediation only**  
Document ceiling: **future Technical Note planning only**  
Formal gate status: **`C0/M1/m0` remains open pending independent append-only re-review**

This amendment freezes only the deterministic activation semantics for the six
already registered publication artifacts. It neither changes their association
arrays nor chooses either optional figure. It is not a manuscript, source
registry, citation audit, figure/table artifact, generator, build, or release.

## 1. Exact authority binding and effective record

The following frozen authorities were read in full and bind this amendment in
the downstream direction:

| Authority | SHA-256 | Lines | Bytes |
|---|---|---:|---:|
| `papers/17-open-groupoid-interfaces/notes/composition_blueprint.md` | `eac20a67f3638444add12f90ac5dede4c8b3f4ca1773a8afe5586e18d1bff10d` | 554 | 36,343 |
| `papers/17-open-groupoid-interfaces/notes/composition_blueprint_amendment_v1.md` | `cfebb477128a3e1a99cb3f9fbedf3e3fce6709cc92d621f6909663f2fc25bddc` | 410 | 23,112 |
| `papers/17-open-groupoid-interfaces/notes/pre_manuscript_source_gate.md` | `98282784211647b9c842110f5bdc04afbc7190b45c9089f0d77d4e7d61c7d68e` | 601 | 30,763 |
| `papers/17-open-groupoid-interfaces/notes/pre_manuscript_source_remediation_gate.md` | `cbde68a9d03204ded7b74c7947b67f106eaf092a59568a64b610d34276c38e52` | 208 | 9,004 |
| `papers/17-open-groupoid-interfaces/notes/proof_audit.md` | `c6810e95d15e1ccf0f1dd48045b0f890ebd98fe637c20a9a5e153e10fa1c4934` | 310 | 20,874 |
| `papers/17-open-groupoid-interfaces/notes/phase2_integrated_gate.md` | `3d1b732bf02a6b2f73b9515a0531fdb77d7960d379c22393079c9e3d200c53c0` | 429 | 24,323 |
| `papers/17-open-groupoid-interfaces/notes/route_audit.md` | `d70ba9d029ae598863e44dbb049c49607063f682de8f7d8a8e5f2074ae531d15` | 211 | 13,035 |

The sole authorization for this author write is:

```text
AUTHORIZING_GATE_PATH=papers/17-open-groupoid-interfaces/notes/pre_manuscript_source_remediation_gate_v2.md
AUTHORIZING_GATE_SHA256=64f33377f45b37943934da7dffbe70f601acf4aac24b1601a5195944aa1422c9
AUTHORIZING_GATE_LINES=141
AUTHORIZING_GATE_BYTES=6003
```

The effective planning record is the following ordered tuple, with every
historical byte preserved:

```text
papers/17-open-groupoid-interfaces/notes/composition_blueprint.md
+ papers/17-open-groupoid-interfaces/notes/composition_blueprint_amendment_v1.md
+ papers/17-open-groupoid-interfaces/notes/composition_blueprint_amendment_v2.md
```

Amendment v1 remains authoritative for the six complete claim-text-primary
association arrays, their 18 items, the other five trace keys, and the P10
source-owner row. This amendment supersedes only v1's unconditional aggregate
wording for the six forward/reverse obligations. It does not rewrite the base,
v1, either source gate, or any mathematical/source/owner/Route authority.

## 2. Deterministic `ARTIFACT_ACTIVE` predicate

The closed artifact domain is:

```text
ARTIFACT_DOMAIN=T1,T2,T3,T4,F1,F2
T1=T1_OWNER_DOMAIN_INTERFACE_FIREWALL
T2=T2_THEOREM_PREMISE_EVIDENCE_SEPARATION
T3=T3_FINITE_CONTROL_RECEIPT
T4=T4_STAGE17_ROUTE_DISPOSITION
F1=F1_OWNER_INTERFACE_FIREWALL
F2=F2_EVIDENCE_TO_ROUTE_CEILING
```

The mandatory tables are unconditionally active:

```text
ARTIFACT_ACTIVE(T1)=true
ARTIFACT_ACTIVE(T2)=true
ARTIFACT_ACTIVE(T3)=true
ARTIFACT_ACTIVE(T4)=true
```

Here, `ARTIFACT_ACTIVE=true` is a planning-state predicate that makes the
artifact's eventual forward and reverse trace obligations live. It does not
assert that artifact bytes currently exist and does not authorize their
creation. T1--T4 remain mandatory future manuscript tables subject to a later
authorized artifact freeze.

For each `f` in `{F1,F2}`, the predicate is true if and only if all of the
following are satisfied together at one later, separately authorized artifact
freeze:

```text
EXPLICIT_FIGURE_DECISION(f)=ADOPTED
TERMINAL_BRANCH(f)=ADOPTED_AND_FROZEN_ACTIVE
CODE_NATIVE_VECTOR_ARTIFACT_PATH(f)=NONEMPTY
CODE_NATIVE_VECTOR_ARTIFACT_SHA256(f)=EXACT_CURRENT_HASH
GENERATOR_SOURCE_PATH(f)=NONEMPTY
GENERATOR_SOURCE_SHA256(f)=EXACT_CURRENT_HASH
CURRENT_SIX_KEY_TRACE_LOCATOR(f)=NONEMPTY
CURRENT_SIX_KEY_TRACE_SHA256(f)=EXACT_CURRENT_HASH
CURRENT_SIX_KEY_TRACE_KEYS(f)=artifact_id,source_data,transformation,caption_claim,supported_manuscript_claims,limitations
CURRENT_SIX_KEY_TRACE_MATCHES_ARTIFACT_AND_GENERATOR(f)=true
ARTIFACT_GENERATOR_TRACE_COFROZEN(f)=true
```

Therefore:

```text
ARTIFACT_ACTIVE(F1)=true iff F1 has an explicit ADOPTED decision and its code-native artifact, generator/source hash, and current six-key trace are synchronously frozen at a later authorized artifact freeze.
ARTIFACT_ACTIVE(F2)=true iff F2 has an explicit ADOPTED decision and its code-native artifact, generator/source hash, and current six-key trace are synchronously frozen at a later authorized artifact freeze.
```

Any missing path, absent hash, stale hash, mismatched trace, omitted trace key,
non-code-native artifact, unsynchronized freeze, absent authorization, or
implicit decision makes the optional predicate false. A source-preflight
decision, manuscript preference, mention in prose, or the existence of the v1
planning array cannot activate a figure.

At the freeze of this amendment:

```text
ARTIFACT_STATE(F1)=OPTIONAL_UNDECIDED
ARTIFACT_STATE(F2)=OPTIONAL_UNDECIDED
ARTIFACT_ACTIVE(F1)=false
ARTIFACT_ACTIVE(F2)=false
OPTIONAL_UNDECIDED_VISIBLE_MANUSCRIPT_CITATION_OBLIGATIONS=0
```

No condition in this record forces F1 or F2 to be adopted.

## 3. Optional-figure state machine and terminal receipts

`OPTIONAL_UNDECIDED` is the only nonterminal optional-figure state. A later
authorized composition decision must place each of F1 and F2 in exactly one,
and only one, terminal branch:

```text
OPTIONAL_UNDECIDED -> ADOPTED_AND_FROZEN_ACTIVE
OPTIONAL_UNDECIDED -> OMITTED_BY_COMPOSITION
```

The first transition is valid only when every conjunct in Section 2 is
satisfied in the same freeze receipt. Merely writing `ADOPTED` is insufficient.
The second transition is valid only with the exact omission receipt below.
Within this effective planning record, a terminal branch cannot be silently
reopened, switched, or inferred; any later change requires new explicit
authority.

### 3.1 Adopted-and-frozen receipt

The future `ADOPTED_AND_FROZEN_ACTIVE` receipt must carry every exact field
below with a nonplaceholder value:

```text
artifact_id=<F1_OWNER_INTERFACE_FIREWALL or F2_EVIDENCE_TO_ROUTE_CEILING>
explicit_figure_decision=ADOPTED
terminal_branch=ADOPTED_AND_FROZEN_ACTIVE
code_native_vector_artifact_path=<nonempty exact path>
code_native_vector_artifact_sha256=<exact current SHA-256>
generator_source_path=<nonempty exact path>
generator_source_sha256=<exact current SHA-256>
current_six_key_trace_locator=<nonempty exact locator>
current_six_key_trace_sha256=<exact current SHA-256>
current_six_key_trace_keys=artifact_id,source_data,transformation,caption_claim,supported_manuscript_claims,limitations
artifact_generator_trace_cofrozen=true
artifact_active=true
```

An adopted receipt with stale or missing artifact, generator, or trace bytes is
invalid and leaves `ARTIFACT_ACTIVE(f)=false`.

### 3.2 Omission receipt

The future `OMITTED_BY_COMPOSITION` receipt must contain exactly the following
required fields and values:

```text
artifact_id=<F1_OWNER_INTERFACE_FIREWALL or F2_EVIDENCE_TO_ROUTE_CEILING>
terminal_branch=OMITTED_BY_COMPOSITION
rationale=<nonempty composition-specific rationale; blank, none, TBD, and placeholder values are invalid>
manuscript_figure_or_table_object_count=0
substantive_manuscript_mention_count=0
activated_claim_obligation_count=0
```

For an omitted figure, `ARTIFACT_ACTIVE(f)=false`; no figure/table object,
caption, label, cross-reference, citation, data-bearing mention,
inference-bearing mention, or other manuscript use of `f` is permitted. The
zero counts must be checked against the complete manuscript, not asserted from
the receipt alone.

Omission removes only the optional figure branch. It cannot delete, weaken,
rephrase, relocate out of scope, or mark optional any underlying TN claim. The
mandatory table/prose support remains:

```text
F1_OMISSION_PRESERVES=TN-08,TN-10,TN-14
F1_MANDATORY_TABLE_ASSOCIATIONS=T1:TN-08,TN-10,TN-14
F2_OMISSION_PRESERVES=TN-12,TN-13,TN-14
F2_MANDATORY_TABLE_ASSOCIATIONS=T3:TN-12;T4:TN-13,TN-14;T1:TN-14
```

## 4. Conditional forward/reverse obligations

For every artifact `a` in the closed domain, both directions use the same
predicate:

```text
ARTIFACT_ACTIVE(a) => FORWARD(a) and REVERSE(a)
not ARTIFACT_ACTIVE(a) => no manuscript citation/use of a is permitted
```

`FORWARD(a)` retains v1's artifact-specific meaning: every claim text and
literal marker in `a`'s frozen association array must occur at its declared
manuscript location and substantively cite `a`. `REVERSE(a)` retains v1's
artifact-specific meaning: every substantive manuscript use of `a` must
resolve to one record in that array; for an active artifact, incidental layout
pointers remain outside substantive reverse coverage. Inactive optional
figures permit no pointer or use at all, so that active-artifact exemption
cannot be used to mention an omitted or undecided figure.

The effective aggregate replaces only v1's misleading unconditional `6_OF_6`
obligation totals:

```text
UNCONDITIONAL_FORWARD_OBLIGATIONS=4_OF_4:T1,T2,T3,T4
UNCONDITIONAL_REVERSE_OBLIGATIONS=4_OF_4:T1,T2,T3,T4
CONDITIONAL_FORWARD_OBLIGATIONS=2_OF_2:F1,F2
CONDITIONAL_REVERSE_OBLIGATIONS=2_OF_2:F1,F2
ASSOCIATION_ARRAYS_FROZEN=6_OF_6
ACTIVE_OBLIGATIONS_FROZEN=ALL_AND_ONLY_ACTIVE_ARTIFACTS
```

The conditional entries are real obligations when, and only when, their
figure is active. This qualification does not alter the six arrays:

```text
T1=TN-02,TN-04,TN-08,TN-10,TN-14
T2=TN-03,TN-05,TN-06,TN-07
T3=TN-12
T4=TN-13,TN-14
F1=TN-08,TN-10,TN-14
F2=TN-12,TN-13,TN-14
ASSOCIATION_ITEM_COUNT=18
DISTINCT_TRACE_CLAIM_MARKERS=11
```

All v1 claim sentences, locators, literal markers, source data,
transformations, caption claims, and limitations remain byte-for-byte the
effective planning values. A future adopted-artifact freeze may only supply
the required current artifact/generator/trace bindings under separate
authorization; it cannot widen those claims or associations.

## 5. Many-artifact joins use every and only active association

For each frozen claim `c`, define:

```text
ACTIVE_JOIN(c)={a | c occurs in the frozen association array for a and ARTIFACT_ACTIVE(a)=true}
```

The one unique future `TRACE_CLAIM:TN-XX` source occurrence must substantively
cite every member of `ACTIVE_JOIN(c)` and no inactive optional artifact. It may
not choose only one active artifact from a multi-artifact join. An inactive F1
or F2 is excluded; T1--T4 are never excluded.

The repeated-marker joins therefore resolve as follows:

| Claim marker | Mandatory active join | Add only if optional figure is active |
|---|---|---|
| `TRACE_CLAIM:TN-08` | T1 | F1 |
| `TRACE_CLAIM:TN-10` | T1 | F1 |
| `TRACE_CLAIM:TN-12` | T3 | F2 |
| `TRACE_CLAIM:TN-13` | T4 | F2 |
| `TRACE_CLAIM:TN-14` | T1 and T4 | F1 and/or F2, each independently if active |

The other active joins are unchanged and mandatory:

```text
TN-02 -> T1
TN-04 -> T1
TN-03 -> T2
TN-05 -> T2
TN-06 -> T2
TN-07 -> T2
```

Every marker still occurs exactly once in future manuscript source. Activation
changes only the set of artifacts cited from that occurrence; it does not
license duplicate claim occurrences or remove the TN claim.

## 6. Seven required branch-test semantics

These are deterministic review cases, not commands and not authorization to
create artifacts. A fresh independent reviewer must evaluate all seven:

| Test | Input state | Required semantic result |
|---|---|---|
| `MANDATORY` | F1 and F2 are `OPTIONAL_UNDECIDED` | Active set is exactly T1--T4; all four tables carry forward/reverse obligations; F1/F2 impose zero citation/use obligations; TN-08/TN-10 join T1, TN-12 joins T3, TN-13 joins T4, and TN-14 joins T1+T4. |
| `ADOPTED_F1` | F1 has a complete synchronized adopted receipt; F2 is inactive | Active set is T1--T4+F1; F1 forward/reverse activate; TN-08 and TN-10 join T1+F1, TN-14 joins T1+T4+F1; no F2 use is permitted. |
| `OMITTED_F1` | F1 has the exact omission receipt; F2 is inactive | F1 remains inactive with zero object, substantive mention, and activated claim obligation; TN-08, TN-10, and TN-14 remain present through their mandatory T1/T4 and prose duties. |
| `ADOPTED_F2` | F2 has a complete synchronized adopted receipt; F1 is inactive | Active set is T1--T4+F2; F2 forward/reverse activate; TN-12 joins T3+F2, TN-13 joins T4+F2, TN-14 joins T1+T4+F2; no F1 use is permitted. |
| `OMITTED_F2` | F2 has the exact omission receipt; F1 is inactive | F2 remains inactive with zero object, substantive mention, and activated claim obligation; TN-12, TN-13, and TN-14 remain present through mandatory T1/T3/T4 and prose duties. |
| `BOTH_ADOPTED` | F1 and F2 each have independent complete synchronized adopted receipts | All six artifacts are active; joins are exactly TN-08→T1+F1, TN-10→T1+F1, TN-12→T3+F2, TN-13→T4+F2, and TN-14→T1+T4+F1+F2; every active artifact carries both directions. |
| `BOTH_OMITTED` | F1 and F2 each have an exact omission receipt | Active set is exactly T1--T4; both optional figures have zero objects, mentions, and activated obligations; joins reduce exactly to TN-08→T1, TN-10→T1, TN-12→T3, TN-13→T4, and TN-14→T1+T4, without deleting any TN claim. |

The one-adopted/one-omitted terminal combinations are the conjunction of the
corresponding independent `ADOPTED_F*` and `OMITTED_F*` cases. No test may
treat source-preflight success, a planning mention, or an incomplete receipt
as activation.

## 7. Frozen non-regression boundaries

The complete mathematical, editorial, owner, source, control, Route, artifact,
bilingual, declaration, and release ceilings remain unchanged:

```text
DOCUMENT_TYPE_PLANNED=TECHNICAL_NOTE
STANDALONE_PASS=false
TN_CLAIM_IDS=TN-00_THROUGH_TN-14
OWNER_FIREWALL_COUNT=7
STAGE17_ROUTE_A_FILES=7
STAGE17_ROUTE_B_FILES=0
ROUTE_DISPOSITION=4_EXPLORATORY_3_REJECTED
A2_A3_A4_POSITIVE_COUNT=0
A2_A3_A4_STATUS=ALL_FAIL
ROUTE_B=false
PLANNED_TABLES=4
MANDATORY_TABLES=T1,T2,T3,T4
MAX_CODE_NATIVE_VECTOR_FIGURES=2
OPTIONAL_CODE_NATIVE_VECTOR_FIGURES=F1,F2
OPTIONAL_FIGURE_ADOPTION_FORCED=false
SOURCE_PREFLIGHT_DECIDES_FIGURE=false
BILINGUAL_FACT_ORDER=8
BILINGUAL_SAME_OMISSION_REQUIRED=true
CONTROLS_ARE_DIAGNOSTIC_ONLY=true
DETERMINANT_OBJECT_AUTHORIZED=false
STANDARD_TO_ACTUAL_TRANSFER_AUTHORIZED=false
DECLARATION_AND_RELEASE_STOPS=UNCHANGED
```

The exact seven drafting owners remain:

```text
GENERIC_R_ACTUAL
GENERIC_Z_FALSIFIER
ACTUAL_ORBIT_P
ACTUAL_PACKET_P
STANDARD_CIRCLE_PROXY
ACTUAL_STANDARD_COMPARISON
UNMARKED_SCALING_CONTROL
```

Their seven Stage-17 record hashes also remain byte-exact:

```text
GEN-INDISC-R-ACTION-TOPOS-QF-CONTROL=77db1521f1d7cdc9e030e1c26148472e4fe4a772bc4a7c90c27dcabc26822672
GEN-INDISC-Z-ACTION-TOPOS-CONTROL=47c04d015036dcefc95f315bd862996cd3653885b09584d27ee7e07c1492848e
DEN-EF-ORBIT-ACTION-GRPD=6ea677a679197d053520de03bade7fb3fcba89c6b10aa9eb8a97955883f7ae9d
DEN-EF-PACKET-ACTION-GRPD-P=d3469e7cf52ed9e84ed3a5f79fcf5ca593a6e60e7bdab8a43b47398c24c5cb91
DEN-EF-ORBIT-STD-CIRCLE-PROXY=163dc6153aafc66bb3209ea51cf8199c32d997e921bcac6707f328aacb4de673
DEN-EF-ORBIT-STD-CIRCLE-COMPARISON-P=b191133dfb4a892b78800dac2b435c0ec58e80cc1ced745cdea08112d7bca727
UNMARKED-PERIOD-SCALING-CONTROL=d1de29ee6708c7846b6f03198fbd9335edfd3c6683928201772513681de58e14
STAGE17_YAML_HASHES_PRESERVED=7_OF_7
```

No owner/domain splice, topology transfer, coordinate union, strict-to-unmarked
transfer, control-to-theorem promotion, cross-paper field import, analytic or
operator promotion, determinant, completed divisor, Weil compression, natural
quantization, Route aggregation, publication promotion, or standalone credit
is introduced. Four owners remain exploratory, three remain rejected, every
owner's A2, A3, and A4 value remains `FAIL`, and Route B remains false.

The exact three-external/three-local minimum source registry and the P9/P10/P11
ceilings remain unchanged. P10 continues to support TN-11's explicit
“builds on” and prior-subtraction wording only; it supplies no Paper-17 direct
theorem, owner, fixed-prime, novelty, standalone, operator, trace, determinant,
or Route credit. Artifact activation cannot enlarge any source role.

All 18 v1 associations, complete claim sentences, locators, unique markers,
six-key trace fields, nonempty limitations, and figure generator/hash-at-freeze
requirements remain frozen. Omission of F1 or F2 never omits a TN claim. The
four mandatory tables, at most two optional code-native vector figures,
eight-fact English/Chinese order and same omissions, author-confirmed
declarations, Technical Note word/page ceiling, and T4-before-References order
remain unchanged.

## 8. Every downstream authorization remains false

This amendment is not the independent closure review. Until an append-only
review of base+v1+v2 returns effective `PASS C0/M0/m0`, all downstream states
remain false:

```text
ALL_DOWNSTREAM_AUTHORIZED=false
SOURCE_CITATION_PREFLIGHT_AUTHORIZED=false
NEXT_SOURCE_CITATION_PREFLIGHT_LANE_AUTHORIZED=false
SOURCE_REGISTRY_PREFLIGHT_AUTHORIZED=false
NOTES_SOURCES_DIRECTORY_WRITE_AUTHORIZED=false
LOCAL_ONLY_PDF_WRITE_AUTHORIZED=false
SOURCE_SIDECAR_WRITE_AUTHORIZED=false
SOURCE_GITIGNORE_WRITE_AUTHORIZED=false
SOURCE_CHECKSUM_LEDGER_WRITE_AUTHORIZED=false
SOURCE_MANIFEST_WRITE_AUTHORIZED=false
PRE_MANUSCRIPT_CITATION_AUDIT_WRITE_AUTHORIZED=false
COMPOSITION_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
MANUSCRIPT_TEX_WRITE_AUTHORIZED=false
BIBLIOGRAPHY_AUTHORIZED=false
REFERENCES_BIB_WRITE_AUTHORIZED=false
CITATION_AUDIT_AUTHORIZED=false
ARTIFACT_FREEZE_AUTHORIZED=false
FIGURE_ARTIFACT_AUTHORIZED=false
TABLE_OR_FIGURE_WRITE_AUTHORIZED=false
README_WRITE_AUTHORIZED=false
BUILD_AUTHORIZED=false
RELEASE_AUTHORIZED=false
ROUTE_CHANGE_AUTHORIZED=false
CONTROL_CHANGE_AUTHORIZED=false
GIT_AUTHORIZED=false
GIT_MUTATION_AUTHORIZED=false
PUBLIC_SYNC_AUTHORIZED=false
NEXT_AUTHORIZED_LANE=NONE
```

No source acquisition or download, local PDF/sidecar/manifest creation,
bibliography, manuscript, table, figure, generator, README, build, release,
Route/control change, Git operation, or public synchronization is authorized
or performed by this record.

## 9. Author self-audit and independent-closure stop

The author-side M-03 repair is complete only as a proposed effective planning
rule; formal closure belongs exclusively to the append-only independent gate:

```text
M03_AUTHOR_REPAIR_COMPLETE=true
FORMAL_M03_CLOSED=false
INDEPENDENT_APPEND_ONLY_REREVIEW_REQUIRED=true
CURRENT_SOURCE_GATE_PREFIX_SHA256=98282784211647b9c842110f5bdc04afbc7190b45c9089f0d77d4e7d61c7d68e
CURRENT_SOURCE_GATE_PREFIX_LINES=601
CURRENT_SOURCE_GATE_PREFIX_BYTES=30763
EFFECTIVE_GATE_STATE=HOLD_C0_M1_m0_PENDING_REREVIEW
AMENDMENT_SELF_HASH=EXTERNAL_BY_CONSTRUCTION
```

Author self-audit assertions:

1. `ARTIFACT_ACTIVE` is defined over exactly T1--T4/F1--F2; T1--T4 are
   mandatory active, while F1/F2 are false in `OPTIONAL_UNDECIDED` state;
2. each optional predicate is true if and only if explicit adoption plus the
   code-native artifact, artifact hash, generator/source hash, and current
   six-key trace are synchronously frozen under later authorization;
3. each optional figure must terminate in exactly
   `ADOPTED_AND_FROZEN_ACTIVE` or `OMITTED_BY_COMPOSITION`, and the omission
   receipt freezes a nonempty rationale plus all three required zero counts;
4. all and only active artifacts carry both forward and reverse obligations;
   inactive optional figures permit no manuscript citation or use;
5. every unique marker cites every and only active associated artifact, with
   the five repeated-marker joins enumerated explicitly;
6. v1's six-obligation aggregate is superseded by four unconditional and two
   conditional obligations without changing any of the six arrays or 18
   associations;
7. all seven required branch-test semantics are specified, including both
   extreme branches and zero-mention checks; and
8. Technical Note/non-standalone status, all TN claims, seven owners,
   P9/P10/P11 ceilings, four-exploratory/three-rejected Route result, all
   A2--A4 failures, Route B false, controls ceiling, bilingual/artifact/
   declaration limits, and every downstream false remain intact.

The stable SHA-256, line count, and byte count for this file must be computed
externally after its final byte is frozen. This amendment cannot declare M-03
formally closed and cannot authorize the next lane.
