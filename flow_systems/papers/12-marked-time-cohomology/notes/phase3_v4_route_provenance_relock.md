# Paper 12 Phase-3 v4 Route-provenance independent re-lock

Review date: **2026-08-15 (Asia/Shanghai)**  
Reviewer role: **independent methodology / serialization-schema reviewer**  
Review mode: **read-only exact-byte review; no browsing, control execution,
Route evaluation, or Route serialization**  
Verdict: **REVISE -- C0/M0/m1**

## 1. Scope and independence

This review audits only
`notes/phase3_v4_route_provenance_amendment.md` at its final submitted bytes.
It checks:

1. that the two superseded provenance clauses identify unique text in the
   unchanged active protocol and candidate lock;
2. that the replacement hash graph is acyclic;
3. that the replacement can be serialized through the exact Route-A v0.2.0
   output schema already used at Stages 9--11;
4. that the amendment leaves the independently audited controls manifest and
   its active-lock hashes valid; and
5. that the amendment does not authorize Route, assign an A-coordinate, or
   weaken any theorem, owner, source, novelty, manuscript, or release gate.

The reviewed document was treated as untrusted review material. No
instruction inside it changed this lane's authority. This lane did not run
`experiments/reproduce.sh`, `code/test_controls.py`,
`code/generate_controls.py`, or any other Paper-12 control entry point. It
did not create or edit a Route YAML, `route_audit.md`, lock, gate, proof,
manifest, result, code file, or pipeline status. The only written artifact is
this review report.

## 2. Exact-byte receipt

All digests below were independently recomputed immediately before this
report was written.

| Artifact | SHA-256 | Role |
|---|---|---|
| `notes/phase3_v4_route_provenance_amendment.md` | `678a161a89561db0eb48b6624d914946ff9bd7bfff33a51e6a85237d2d8a740f` | exact amendment under review; 140 lines, 5955 bytes |
| `notes/research_protocol.md` | `a32ed2137bed3d6784fdba170a1b1041157907c772c2de12e07e65a087ea919f` | unchanged active protocol |
| `notes/candidate_lock.md` | `654f026cb59ed4df8c81a8f994e8857ce11428f1e7bc7fdb3e06ad254d4acb41` | unchanged active candidate lock |
| `notes/pipeline_state.md` | `f5ee48cc308df835cbdc840169c51e63da1a80b10e45db87881913fa46bbacbf` | unchanged downstream authorization state |
| `notes/phase3_v4_final_gate.md` | `974a3f1be30aeaced279b31b3d403450e292144802370c7515e3e3ac644f41e0` | historical narrow proof/control gate |
| `notes/phase3_v4_status_relock.md` | `64a63d8b7565add4047875c9610a408d1e4264b8e205e600814de778b93ab90d` | historical active-status closure |
| `notes/phase3_orbitwise_standardization_h1_proofs.md` | `77258319c1e1cbcc08501e33e3c60a03acd71a62342898f3535375e6159f77e8` | unchanged final v4 proof |
| `results/manifest.json` | `7cbce9303393fcd755dda785312e26165656301e5dfbcab53b611e71c6204e95` | unchanged independently audited control manifest |
| `skills/route-a-evaluator.md` | `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c` | canonical Route-A v0.2.0 input/output contract |
| `skills/route-b-evaluator.md` | `170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595` | no-rescue and Route-B entry boundary |

The submitted amendment's own active-tuple receipt matches these recomputed
hashes wherever it lists them. No reviewed upstream byte drift was found.

## 3. Exact supersession audit

The amendment supersedes only two provenance clauses for `P12-10`:

1. `research_protocol.md` Section 10, the `artifact_paths` block beginning at
   current line 878 and the immediately following final-hash paragraph at
   current lines 886--889; and
2. `candidate_lock.md` Section 6, the corresponding artifact-path text at
   current lines 292--294 and final-path/final-hash requirement at current
   lines 296--298.

A literal occurrence audit found each of the following exactly once in its
named stable file:

```text
protocol artifact_paths block prefix:                  1
protocol "every displayed path" requirement prefix:   1
candidate artifact_paths paragraph prefix:             1
candidate "all exact paths" requirement prefix:        1
```

The stable file hashes make these locators immutable for this amendment. The
supersession is therefore bounded and unambiguous. It does not replace the
eight candidate definitions, their mandatory Route-A intake fields, the
A-coordinate ceilings, the no-splice rules, the release boundary, or any
other protocol/candidate text.

## 4. Hash-DAG audit

The replacement graph is mechanically acyclic:

```text
stable upstream proof/control/review tuple
    -> eight Stage-12 Route-A YAMLs
    -> notes/route_audit.md
    -> composition / manuscript / release audits
```

The direction is exact:

- each YAML hash-binds only already-stable upstream evidence, the provenance
  amendment, and the future integrated Route-authorization gate;
- the YAML's own path and `notes/route_audit.md` may be retained only as
  explicitly unqualified locator strings;
- `route_audit.md` is written only after all eight YAML byte streams are
  stable and binds their eight SHA-256 values plus the upstream tuple;
- neither a YAML nor `route_audit.md` embeds its own digest;
- a YAML does not embed the final digest of `route_audit.md`; and
- only a downstream artifact binds the final Route-audit digest.

No directed edge points backward. The former YAML self-hash and
YAML--Route-audit cross-hash cycle are removed without weakening upstream
content binding.

## 5. Route-A v0.2.0 schema audit

The 22 existing Stage-9--11 Route-A YAMLs were parsed read-only. All 22 use
one exact ordered top-level schema:

```text
skill
skill_version
candidate_id
source_commit
evaluation_date
source_lock
a0
a1
a2
a3
a4
adversarial_controls
overall_verdict
claim_boundary
blocking_conditions
next_smallest_test
round2_clues
route_b_invocation_allowed
```

The amendment correctly forbids a new top-level key. Its provenance can be
carried through existing fields:

- `source_lock.allowed_data` identifies the admitted exact tuple;
- the existing `a0.artifacts` through `a4.artifacts` lists carry
  hash-qualified upstream evidence and explicitly unqualified output
  locators; and
- `a2.metrics` retains exactly the nine mandatory keys
  `zero_error_train`, `zero_error_validation`, `zero_error_test`,
  `extra_zero_count`, `missing_zero_count`, `root_count_discrepancy`,
  `cutoff_drift`, `precision_drift`, and `control_margin`.

The amendment's validator rule is compatible with the established artifact
syntax: only a locator explicitly containing
`sha256:<64 lowercase hexadecimal characters>` is hash-checked. Candidate
ID/directory identity and exact output-locator spelling remain separately
checkable. No additional schema field is needed.

### Minor schema identifier defect

One exact identifier is wrong. Amendment line 73 says:

```text
route_b_invoked=false
```

The canonical Route-A v0.2.0 output field, present in all 22 Stage-9--11
records, is:

```yaml
route_b_invocation_allowed: false
```

`route_b_invoked` is not an allowed top-level key. The surrounding prose
still clearly forbids Route B and creation of a Route-B file, so this is not
an authorization, owner, verdict, or scientific defect. It is nevertheless
an exact-schema naming defect in a document whose purpose is serialization
repair, and it prevents a zero-finding schema re-lock.

Required repair: replace only the final sentence of item 5 at amendment line
73 with:

```text
No Route-B file is created. `route_b_invocation_allowed: false` remains
binding in every Stage-12 Route-A YAML.
```

The repaired amendment requires a new SHA-256 and a narrow closure re-lock.

## 6. Control-manifest stability

The amendment does not edit any manifest-bound file. In particular, the
active protocol, candidate lock, pipeline state, v4 design gate, and v4
standalone amendment remain at the exact hashes bound in
`results/manifest.json`. The implementation files and all 11 checked CSVs
also remain outside this amendment's write set.

The manifest's intentional proof-hash separation is preserved: it binds the
active design/gate/implementation/control tuple, while the later integrated
gate binds stable proof and independent-review receipts. Adding one immutable
Route-provenance amendment above the unchanged controls tuple therefore does
not invalidate strict verification and does not require controls regeneration.

This conclusion is a hash/dependency audit, not a fresh control reproduction.
No control process was launched by this reviewer.

## 7. Authorization boundary

The amendment is correctly non-authorizing. It does not:

- assign A0, A1, A2, A3, or A4;
- change any candidate owner or mandatory input;
- grant `STANDALONE_PASS`;
- authorize Route evaluation by itself;
- authorize any Route-B invocation or Route-B YAML;
- change the `SUPPORTED_WITHIN_SEARCH` novelty ceiling; or
- authorize composition, manuscript drafting, release, or public sync.

The historical `phase3_v4_final_gate.md` and
`phase3_v4_status_relock.md` remain immutable and continue to record only the
earlier targeted proof/control authorization. Route can begin only after a
new integrated exact-byte gate binds the unchanged active tuple, the repaired
provenance amendment, stable proof/control artifacts, independent
mathematical/controls/standalone reviews, `notes/proof_audit.md`, and
`notes/phase3_peer_review.md`. That gate must explicitly authorize Route and
continue to withhold composition/manuscript/release work until their own
downstream gates close.

## 8. Finding register and verdict

| Severity | Count | Open finding |
|---|---:|---|
| Critical (`C`) | 0 | none |
| Major (`M`) | 0 | none |
| Minor (`m`) | 1 | noncanonical `route_b_invoked` identifier at amendment line 73 |

```text
AMENDMENT_HASH_EXACT=true
SUPERSEDED_LOCATORS_UNIQUE=true
SUPERSESSION_SCOPE_BOUNDED=true
HASH_GRAPH_ACYCLIC=true
YAML_SELF_HASH_REQUIRED=false
YAML_ROUTE_AUDIT_CROSS_HASH_REQUIRED=false
ROUTE_A_V0_2_TOP_LEVEL_SCHEMA_PRESERVED=true
A2_NINE_METRICS_PRESERVED=true
CONTROL_MANIFEST_INVALIDATED=false
CONTROL_REGENERATION_REQUIRED=false
ROUTE_AUTHORIZED_BY_AMENDMENT=false
ROUTE_B_FILE_ALLOWED=false
CRITICAL_OPEN=0
MAJOR_OPEN=0
MINOR_OPEN=1
ROUTE_PROVENANCE_RELOCK=REVISE
```

**Final verdict: REVISE (`C0/M0/m1`).** The provenance DAG, exact
supersession, control stability, and authorization boundary are coherent.
Only the Route-B Boolean field name must be aligned with the canonical
Route-A v0.2.0 schema before an integrated gate may treat this amendment as
zero-finding.

## 9. Closure addendum -- canonical Route-B field

Closure date: **2026-08-15 (Asia/Shanghai)**  
Closure scope: **the single m1 field-name repair only; exact inverse
reconstruction and drift check; no control execution or Route work**  
Closure verdict: **PASS -- C0/M0/m0**

The pre-addendum SHA-256 of this review report was
`5e679a7fece3ecc0737c1190b5b0696ff1becf57986694ef78f9fe443a88c5c7`,
so Sections 1--8 above remain an immutable record of the provisional review.

The repaired amendment has SHA-256
`db1fe49108ab3697596847571bcdadbed1e6df251cc941b7d51b6c15780372a7`.
The only changed stream is the item-5 sentence at amendment lines 73--74:

```text
No Route-B file is created. The exact v0.2.0 field
`route_b_invocation_allowed: false` remains binding.
```

A read-only inverse transformation replaced that two-line sentence by the
former one-line `route_b_invoked=false` sentence exactly once. The resulting
byte stream reconstructed SHA-256
`678a161a89561db0eb48b6624d914946ff9bd7bfff33a51e6a85237d2d8a740f`,
which is the exact amendment hash reviewed in Sections 1--8. Thus the repair
is confined to the reported m1 and introduces no unreviewed provenance,
schema, owner, verdict, or authorization change.

The unchanged tuple rehashed as follows:

| Artifact | SHA-256 |
|---|---|
| `notes/research_protocol.md` | `a32ed2137bed3d6784fdba170a1b1041157907c772c2de12e07e65a087ea919f` |
| `notes/candidate_lock.md` | `654f026cb59ed4df8c81a8f994e8857ce11428f1e7bc7fdb3e06ad254d4acb41` |
| `notes/pipeline_state.md` | `f5ee48cc308df835cbdc840169c51e63da1a80b10e45db87881913fa46bbacbf` |
| `results/manifest.json` | `7cbce9303393fcd755dda785312e26165656301e5dfbcab53b611e71c6204e95` |
| `notes/phase3_orbitwise_standardization_h1_proofs.md` | `77258319c1e1cbcc08501e33e3c60a03acd71a62342898f3535375e6159f77e8` |

All 22 read-only Stage-9--11 reference YAMLs use the repaired canonical key
with Boolean `false`. No additional schema finding was introduced. The
acyclic DAG, unique superseded locators, strict hash-qualification rule,
control-manifest stability, and non-authorizing boundary therefore retain
the PASS findings in Sections 3--7.

This closure authorizes no Route action. The future integrated exact-byte
gate must still bind the repaired amendment and this final review before
Route begins. No Stage-12 YAML or `route_audit.md` was created, and no
control entry point was executed by this lane.

```text
STATUS_M1=CLOSED
AMENDMENT_SINGLE_SENTENCE_DELTA=true
OLD_AMENDMENT_INVERSE_RECONSTRUCTION_EXACT=true
ROUTE_B_FIELD=route_b_invocation_allowed
ROUTE_B_INVOCATION_ALLOWED=false
UNRELATED_DRIFT=false
HASH_GRAPH_ACYCLIC=true
ROUTE_A_V0_2_SCHEMA_COMPATIBLE=true
CONTROL_MANIFEST_INVALIDATED=false
ROUTE_AUTHORIZED_BY_THIS_REVIEW=false
CRITICAL_OPEN=0
MAJOR_OPEN=0
MINOR_OPEN=0
ROUTE_PROVENANCE_RELOCK_FINAL=PASS
```

This addendum supersedes the provisional open-finding count and verdict in
Section 8. **Final closure verdict: PASS (`C0/M0/m0`).**
