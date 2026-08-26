# Paper 12 Phase-3 v4 Route-provenance amendment

Date: **2026-08-15 (Asia/Shanghai)**  
Scope: **a narrow serialization repair for `P12-10`; no mathematical,
source, owner, control, verdict, or Route-coordinate change**

## 1. Authority and exact precedence

This versioned amendment is evaluated together with the unchanged active
Paper-12 tuple:

| Active artifact | SHA-256 |
|---|---|
| `notes/research_protocol.md` | `a32ed2137bed3d6784fdba170a1b1041157907c772c2de12e07e65a087ea919f` |
| `notes/candidate_lock.md` | `654f026cb59ed4df8c81a8f994e8857ce11428f1e7bc7fdb3e06ad254d4acb41` |
| `notes/pipeline_state.md` | `f5ee48cc308df835cbdc840169c51e63da1a80b10e45db87881913fa46bbacbf` |
| `notes/phase3_v4_final_gate.md` | `974a3f1be30aeaced279b31b3d403450e292144802370c7515e3e3ac644f41e0` |
| `notes/phase3_v4_status_relock.md` | `64a63d8b7565add4047875c9610a408d1e4264b8e205e600814de778b93ab90d` |

For `P12-10` serialization only, this amendment supersedes:

1. `research_protocol.md` Section 10's current `artifact_paths` block and the
   immediately following paragraph that requires every displayed path to
   carry a final SHA-256 before `P12-10`; and
2. `candidate_lock.md` Section 6's corresponding `artifact_paths` paragraph
   and its requirement that every displayed path and final SHA-256 already
   exist before `P12-10`.

The superseded wording accidentally requires a Stage-12 YAML to embed its own
final digest and requires the YAML and `route_audit.md` to embed one another's
final digests. Ordinary finite-byte SHA-256 provenance cannot satisfy that
self/cross-reference cycle. This amendment removes only that impossible
serialization condition. Every other protocol and candidate-lock byte,
definition, owner, field, ceiling, and prohibition remains binding.

## 2. Acyclic artifact provenance

For each of the eight frozen Stage-12 Route-A owners, replace the superseded
artifact requirement semantically by:

```text
artifact_provenance:
  hash_bound_upstream_paths:
    papers/12-marked-time-cohomology/notes/proof_audit.md
    papers/12-marked-time-cohomology/results/manifest.json
    papers/12-marked-time-cohomology/notes/phase3_peer_review.md
  output_locator_paths_unhashed:
    papers/12-marked-time-cohomology/notes/route_audit.md
    evaluations/route_a/<candidate_id>/2026-08-15-stage12.yaml
```

The provenance graph is strictly one-way:

```text
stable upstream tuple
  -> eight Stage-12 Route-A YAML files
  -> notes/route_audit.md
  -> composition, manuscript, and release audits
```

The following rules are exact:

1. Every `hash_bound_upstream_paths` file must exist on stable final bytes
   before Route evaluation begins. Its exact SHA-256 must be serialized in
   every applicable YAML and in `route_audit.md`.
2. The two `output_locator_paths_unhashed` values are locators, not upstream
   evidence. A YAML must not embed its own SHA-256 or the SHA-256 of
   `route_audit.md`.
3. After all eight YAML files are stable, `route_audit.md` must bind their
   eight final SHA-256 values and the complete upstream tuple.
4. `route_audit.md` must not embed its own SHA-256. Its final digest is bound
   only by downstream composition and release artifacts.
5. No Route-B file is created. The exact v0.2.0 field
   `route_b_invocation_allowed: false` remains binding.

## 3. Existing YAML schema only

This amendment authorizes no new top-level YAML key. The exact Stage-9--11
Route-A v0.2.0 schema remains binding, including all nine mandatory A2 metric
outputs.

The new amendment and the later integrated Route-authorization gate are
serialized through existing fields only:

- `source_lock.allowed_data` names the unchanged active tuple, this
  provenance amendment, the integrated gate, final proof/peer artifacts, and
  controls manifest;
- `a0.artifacts` carries hash-qualified locks, this amendment, the integrated
  gate, and relevant proof/source evidence;
- `a2.artifacts` carries the hash-qualified controls manifest and any
  owner-relevant CSV;
- the remaining `aN.artifacts` fields carry relevant hash-qualified final
  proof/peer evidence; and
- one existing nested artifacts list may retain the YAML and Route-audit
  output paths as unqualified strings explicitly marked
  `locator-only; SHA-256 intentionally bound downstream`.

Mechanical validators must hash-check only artifacts explicitly qualified by
`sha256:<64 lowercase hexadecimal characters>`. They must still verify that
all frozen output locator paths are exact and that the candidate directory
matches `candidate_id`.

## 4. No-Git and control stability

`code_commit: unavailable-no-git-content-sha256-lock-required` remains a
resolved provenance state, not a placeholder. Exact implementation, proof,
review, manifest, and CSV hashes remain the mandatory substitutes.

The independently audited controls manifest intentionally binds the unchanged
active protocol/candidate/pipeline tuple. This amendment does not mutate those
bytes and therefore does not invalidate strict verification or require a
post-review controls regeneration.

## 5. Authorization boundary

This amendment repairs provenance syntax only. By itself it does **not**
authorize Route evaluation, assign any A0--A4 verdict, grant
`STANDALONE_PASS`, authorize composition/manuscript/release, or alter the
bounded novelty wording `SUPPORTED_WITHIN_SEARCH`.

Route may begin only after an integrated exact-byte gate binds:

- the unchanged active tuple;
- this amendment;
- the final v4 proof;
- the final controls manifest and implementation tuple;
- the independent mathematical, controls, and standalone reviews;
- stable `notes/proof_audit.md`; and
- stable `notes/phase3_peer_review.md`.

```text
AMENDMENT_KIND=ROUTE_PROVENANCE_DAG_ONLY
ACTIVE_LOCK_BYTES_CHANGED=false
MATHEMATICAL_CONTENT_CHANGED=false
OWNER_OR_ROUTE_CEILING_CHANGED=false
CONTROL_BYTES_CHANGED=false
YAML_SCHEMA_CHANGED=false
SELF_HASH_REQUIRED=false
CROSS_HASH_CYCLE_REQUIRED=false
ROUTE_AUTHORIZED_BY_THIS_AMENDMENT=false
```
