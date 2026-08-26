# Paper 17 optional-artifact activation remediation gate v2

Gate date: **2026-08-16 (Asia/Shanghai)**  
Verdict: **PASS TO ONE BLUEPRINT AMENDMENT V2; C0/M1/m0 REMAINS OPEN**

```text
OPEN_FINDING=M-03_OPTIONAL_FIGURE_ACTIVATION_AMBIGUITY
CRITICAL_FINDINGS=0
MAJOR_FINDINGS=1
MINOR_FINDINGS=0
BLUEPRINT_AMENDMENT_V2_AUTHORIZED=true
SOURCE_CITATION_PREFLIGHT_AUTHORIZED=false
```

The first two findings are closed on the effective base-plus-v1 planning
record.  This gate authorizes only the smallest deterministic activation rule
for optional figures F1 and F2.  It does not reopen or alter their claims,
owners, captions, limitations, source data, transformations, or associations.

## 1. Exact authority tuple

| Authority | SHA-256 | Lines | Bytes |
|---|---|---:|---:|
| `notes/composition_blueprint.md` | `eac20a67f3638444add12f90ac5dede4c8b3f4ca1773a8afe5586e18d1bff10d` | 554 | 36,343 |
| `notes/composition_blueprint_amendment_v1.md` | `cfebb477128a3e1a99cb3f9fbedf3e3fce6709cc92d621f6909663f2fc25bddc` | 410 | 23,112 |
| `notes/pre_manuscript_source_gate.md` | `98282784211647b9c842110f5bdc04afbc7190b45c9089f0d77d4e7d61c7d68e` | 601 | 30,763 |
| `notes/pre_manuscript_source_remediation_gate.md` | `cbde68a9d03204ded7b74c7947b67f106eaf092a59568a64b610d34276c38e52` | 208 | 9,004 |
| `notes/proof_audit.md` | `c6810e95d15e1ccf0f1dd48045b0f890ebd98fe637c20a9a5e153e10fa1c4934` | 310 | 20,874 |
| `notes/phase2_integrated_gate.md` | `3d1b732bf02a6b2f73b9515a0531fdb77d7960d379c22393079c9e3d200c53c0` | 429 | 24,323 |
| `notes/route_audit.md` | `d70ba9d029ae598863e44dbb049c49607063f682de8f7d8a8e5f2074ae531d15` | 211 | 13,035 |

The seven Stage-17 YAML hashes, the P10 owner row, original M-01/M-02 closure,
and every mathematical/owner/Route boundary remain unchanged.

## 2. Sole authorized author write

Exactly one file may be created:

```text
papers/17-open-groupoid-interfaces/notes/composition_blueprint_amendment_v2.md
```

The effective planning record will be the immutable base plus amendments v1
and v2 in that order.  No existing file may be rewritten by the author lane.

## 3. Exact M-03 activation contract

Amendment v2 must freeze one deterministic predicate `ARTIFACT_ACTIVE(a)`:

```text
ARTIFACT_ACTIVE(T1)=true
ARTIFACT_ACTIVE(T2)=true
ARTIFACT_ACTIVE(T3)=true
ARTIFACT_ACTIVE(T4)=true

ARTIFACT_ACTIVE(F1)=true iff F1 has an explicit ADOPTED decision and its
  code-native artifact, generator/source hash, and current six-key trace are
  frozen together at a later authorized artifact freeze.
ARTIFACT_ACTIVE(F2)=true iff F2 has an explicit ADOPTED decision and its
  code-native artifact, generator/source hash, and current six-key trace are
  frozen together at a later authorized artifact freeze.
```

Before such a freeze, F1/F2 remain `OPTIONAL_UNDECIDED` and impose no visible
manuscript-citation obligation.  A later composition decision must put each
figure in exactly one of two terminal branches:

```text
ADOPTED_AND_FROZEN_ACTIVE
OMITTED_BY_COMPOSITION
```

The omitted branch must carry an explicit receipt containing artifact ID,
`OMITTED_BY_COMPOSITION`, a nonempty rationale, zero manuscript figure/table
object, zero substantive manuscript mention, and zero activated claim
obligation.  Omission cannot delete or weaken the underlying TN claim: every
claim remains in its mandatory table/prose association already frozen by v1.

For every artifact `a`, both trace obligations are conditional on the same
predicate:

```text
ARTIFACT_ACTIVE(a) => FORWARD(a) and REVERSE(a)
not ARTIFACT_ACTIVE(a) => no manuscript citation/use of a is permitted
```

For a TN claim associated with multiple artifacts, its unique source marker
must cite every and only active associated artifact.  Inactive optional
figures are excluded from that join; all active mandatory tables remain.

The misleading v1 aggregate must be superseded exactly as follows:

```text
UNCONDITIONAL_FORWARD_OBLIGATIONS=4_OF_4:T1,T2,T3,T4
UNCONDITIONAL_REVERSE_OBLIGATIONS=4_OF_4:T1,T2,T3,T4
CONDITIONAL_FORWARD_OBLIGATIONS=2_OF_2:F1,F2
CONDITIONAL_REVERSE_OBLIGATIONS=2_OF_2:F1,F2
ASSOCIATION_ARRAYS_FROZEN=6_OF_6
ACTIVE_OBLIGATIONS_FROZEN=ALL_AND_ONLY_ACTIVE_ARTIFACTS
```

This activation rule may not force either optional figure to be adopted and
may not turn a source-preflight decision into a figure decision.

## 4. Non-regression and authorization stop

Amendment v2 must preserve: Technical Note, `STANDALONE_PASS=false`, TN-00
through TN-14, seven owners, four exploratory/three rejected, all A2--A4
`FAIL`, Route B false, four mandatory tables, at most two optional code-native
figures, the bilingual eight-fact ledger, P9/P10/P11 source ceilings, controls
as diagnostics only, and every declaration/release stop.

It authorizes no source acquisition, citation audit, manuscript, BibTeX,
artifact, README, build, release, Route/control change, Git operation, or
public synchronization.

## 5. Required append-only independent closure

After v2 stable bytes are externally hashed, the same independent gate lane
must review the effective base+v1+v2 tuple from scratch and append only to
`notes/pre_manuscript_source_gate.md`.  It must preserve both historical
prefixes, including the complete current 30,763-byte / 601-line prefix at:

```text
98282784211647b9c842110f5bdc04afbc7190b45c9089f0d77d4e7d61c7d68e
```

The re-review must test mandatory, adopted-F1, omitted-F1, adopted-F2,
omitted-F2, both-adopted, and both-omitted branches; repeated-marker joins;
zero mention for omitted figures; unchanged 18 associations; and all existing
owner/source/Route/non-regression boundaries.  Only `PASS C0/M0/m0` may
authorize the later local-only source/citation preflight lane.

```text
P17_OPTIONAL_ARTIFACT_REMEDIATION_GATE_V2=PASS_TO_ONE_AMENDMENT_V2
OPEN_FINDINGS=C0/M1/m0
SOLE_AUTHOR_WRITE=notes/composition_blueprint_amendment_v2.md
SOLE_REVIEW_WRITE=append_only:notes/pre_manuscript_source_gate.md
ALL_DOWNSTREAM_AUTHORIZED=false
THIS_FILE_SELF_HASH=EXTERNAL_BY_CONSTRUCTION
```
