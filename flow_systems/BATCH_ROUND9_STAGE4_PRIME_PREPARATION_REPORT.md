# Round 9 Papers 24/26/27/28 — Stage 4′ Preparation Report

## Outcome

Status: **PREPARED — AWAITING EXACT AUTHOR AUTHORITY**.

The Stage 4′ pre-authority tuple is complete for Papers 24, 26, 27, and 28. The four current working revised drafts, current content-neutral block manifests, Round-2 residual roadmaps, Round-2 claim-surface manifests, batch scope manifest, and exact authorization request have been replay-validated.

This report records preparation only. It is not an author adjudication, does not authorize a revision patch, and does not advance any pipeline state. The generic instruction `确认，继续下一轮` permits preparation of the next legal stage but does not supply the six per-item triage decisions or the exact target/operation and support scope required by the prepared request. Prior-round author choices have not been carried forward.

- Exact authorization request: [`BATCH_ROUND9_STAGE4_PRIME_AUTHORIZATION_REQUEST.md`](BATCH_ROUND9_STAGE4_PRIME_AUTHORIZATION_REQUEST.md)
- Request SHA-256: `d2e94cd10b1ca12204c8747b5bc0895f6c642e3a3ff7c08194016ed62fd461ec`
- Machine-readable scope: [`BATCH_ROUND9_STAGE4_PRIME_SCOPE_MANIFEST.json`](BATCH_ROUND9_STAGE4_PRIME_SCOPE_MANIFEST.json)
- Scope-manifest SHA-256: `96206b64bc893493e499ab4c317c5a0e0316ca125d6e096826389173a7d09327`
- Prepared residuals: **6** = 5 `must_fix` + 1 `should_fix`.
- Registered ClaimIntent surfaces: **51/51 exact-once** = P24 10 + P26 17 + P27 10 + P28 14.

## Per-paper prepared tuple

| Paper | Current working revised draft | Current block manifest | Round-2 residual roadmap | Round-2 claim surfaces | Counts |
|---|---|---|---|---|---|
| P24 | `papers/24-bianchi-holonomy-flow/notes/stage4_revision_round1.tex`<br>`b098630fdf8db94b6ae892e86eabafe1832b45ff72122ea722100d3541e46d16` | `papers/24-bianchi-holonomy-flow/notes/stage4_revision_round1.tex.block-manifest.json`<br>`5a7ea3da03bfd2119c31f8e479887561a54f3029d18b35efa642929d57fcb1c9` | `papers/24-bianchi-holonomy-flow/notes/stage4_prime_revision_roadmap.json`<br>`bd30b424da60ee104346e54dce5117efff754d062a0f4f4f771ea94a29becf0e` | `papers/24-bianchi-holonomy-flow/notes/stage4_prime_claim_surface_manifest.json`<br>`7abc5bb40715cc5253c7afd6e272ec951de3ac8b622b9d2b199ccd52b3c0ad6c` | 111 blocks / 2 residuals / 10 surfaces |
| P26 | `papers/26-level11-newform-time-change/notes/stage4_revision_round1.tex`<br>`dea8f3af92bde625008f2987922b3b69d2856abe3b796fdd2af319bf6db3bf37` | `papers/26-level11-newform-time-change/notes/stage4_revision_round1.tex.block-manifest.json`<br>`95517900de1ffade6d8502f67ef3e335fa7ce53a6ded56da84986808037a89d1` | `papers/26-level11-newform-time-change/notes/stage4_prime_revision_roadmap.json`<br>`65590089ab2eca9b227047620a484c2fbc70a56c8b9b50d8c00aea404f236f1f` | `papers/26-level11-newform-time-change/notes/stage4_prime_claim_surface_manifest.json`<br>`07789461deb65e182355498b246106bf02ec4f971f53305795721d3d0a7f1023` | 117 blocks / 2 residuals / 17 surfaces |
| P27 | `papers/27-congruence-inverse-limit-no-go/notes/stage4_revision_round1.tex`<br>`b445b5c8350439e97f6be415c2ea99c948114cb241c3ccb084e5f8263e61be8f` | `papers/27-congruence-inverse-limit-no-go/notes/stage4_revision_round1.tex.block-manifest.json`<br>`76e2dfa5a63c234ad550a87467133e30550fc843b592a3b674d47c1e48d5c51b` | `papers/27-congruence-inverse-limit-no-go/notes/stage4_prime_revision_roadmap.json`<br>`a31b0557a42bcc31c20864ef0cdc7318661e0d02cbe525ae9bf3816506328451` | `papers/27-congruence-inverse-limit-no-go/notes/stage4_prime_claim_surface_manifest.json`<br>`23a352898684469d6241ff05a9289ca310ef22d0495da94c3f98ec0417312df2` | 107 blocks / 1 residual / 10 surfaces |
| P28 | `papers/28-bolza-magnetic-flow/notes/stage4_revision_round1.tex`<br>`884ca28dacf24cabe6f5473c67cb55bdfd1491e87eb6bd763aab7646cfce1bb2` | `papers/28-bolza-magnetic-flow/notes/stage4_revision_round1.tex.block-manifest.json`<br>`06dd296f214c34c862091e62b5ad0435de2d447712bd3e4f46b08cc29384c9b3` | `papers/28-bolza-magnetic-flow/notes/stage4_prime_revision_roadmap.json`<br>`59378ac5cdf61a547fa543cb97f665da49b2769109b523ad71117e2cc0e98fd7` | `papers/28-bolza-magnetic-flow/notes/stage4_prime_claim_surface_manifest.json`<br>`b20b39895c4ffd6ee94ba1d7e231b5767014071d1d1372d1be8c6e829820a9b9` | 126 blocks / 1 residual / 14 surfaces |

## Six frozen residuals awaiting author triage

| Paper | Item | Round-2 verdict | Obligation | Proposed manuscript target/operation pairs |
|---|---|---|---|---|
| P24 | REV-001 | `PARTIALLY_ADDRESSED` | `must_fix` | B0015, B0032, B0034, B0104 / `replace_block` |
| P24 | REV-003 | `PARTIALLY_ADDRESSED` | `must_fix` | B0056, B0065, B0067, B0068, B0075, B0084 / `replace_block` |
| P26 | REV-02 | `PARTIALLY_ADDRESSED` | `must_fix` | B0029, B0030, B0031, B0092 / `replace_block` |
| P26 | REV-04 | `CANNOT_VERIFY` | `should_fix` | B0080, B0081, B0082, B0083, B0093 / `replace_block` |
| P27 | REV-03 | `PARTIALLY_ADDRESSED` | `must_fix` | B0040, B0041, B0042 / `replace_block` |
| P28 | REV-02 | `CANNOT_VERIFY` | `must_fix` | B0048 / `replace_block` |

The exact support scope and the two conditional append-only P26 bibliography entries are enumerated in the request. No claim-strength replacement is proposed or authorized.

## Validation results

- Official `revision-roadmap/1.0` schema, current base-draft hash, block-manifest hash, block order/hash replay, target existence/order, and residual counts: **4/4 PASS**.
- Official `claim-surface-manifest/1.0` schema, roadmap/base bindings, ClaimIntent source hashes, source-claim equality, UTF-8 offsets, declared-block containment, non-overlap, and exact-once occurrence: **4/4 PASS**.
- Independent full-draft exact-once check: **51/51 PASS**.
- Scope-to-filesystem and request tuple-hash projection: **4/4 PASS**; residual projection against the frozen Stage 3′ Round-2 traceability rows: **6/6 PASS**.
- Builder isolated replay: **10/10 generated outputs byte-identical** (four roadmaps, four claim-surface manifests, batch scope, and request).
- Existing P24/P26 support-output receipt bindings used by the request: **4/4 PASS**.
- No Stage 4′ author-adjudication sidecar or revision patch exists or was created by this preparation pass.

During validation, three stale support-path spellings in the builder and its two batch outputs were corrected to the paths actually hash-bound by the existing receipts:

- P24: `results/stage4_loxodromic_d9_jet_collision_profile.csv`.
- P24: `results/stage4_loxodromic_d9_jet_metrics.json`.
- P26: `results/stage4_matched_exact_control_decomposition.csv`.

The corrected builder is `tools/build_round9_stage4_prime_authorization.py`, SHA-256 `2e652a44d14d10df71b6f72717efe4351a97697edd4269f16b8d58bffc4594aa`.

## Replay commands

Official roadmap/block and claim-surface validation:

```bash
ARS_ROOT=/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/skills/academic-research-suite/ars
for p in \
  24-bianchi-holonomy-flow \
  26-level11-newform-time-change \
  27-congruence-inverse-limit-no-go \
  28-bolza-magnetic-flow
do
  python "$ARS_ROOT/scripts/revision_roadmap.py" validate-roadmap \
    "papers/$p/notes/stage4_prime_revision_roadmap.json" \
    --base "papers/$p/notes/stage4_revision_round1.tex" \
    --block-manifest "papers/$p/notes/stage4_revision_round1.tex.block-manifest.json"
  python "$ARS_ROOT/scripts/revision_roadmap.py" render \
    "papers/$p/notes/stage4_prime_revision_roadmap.json" \
    --base "papers/$p/notes/stage4_revision_round1.tex" \
    --block-manifest "papers/$p/notes/stage4_revision_round1.tex.block-manifest.json" \
    --claim-surface "papers/$p/notes/stage4_prime_claim_surface_manifest.json" \
    --artifact-root "papers/$p" >/dev/null
done
```

Independent scope hashes, residual projection, UTF-8 spans, and whole-draft exact-once check:

```bash
python - <<'PY'
from pathlib import Path
import hashlib, json

sha = lambda raw: hashlib.sha256(raw).hexdigest()
scope = json.loads(Path("BATCH_ROUND9_STAGE4_PRIME_SCOPE_MANIFEST.json").read_text())
residuals = surfaces = 0
for row in scope["papers"]:
    root = Path(row["paper_dir"])
    draft = (root / row["base_draft"]).read_bytes()
    block = (root / row["block_manifest"]).read_bytes()
    roadmap_raw = (root / row["roadmap"]).read_bytes()
    claims_raw = (root / row["claim_surface_manifest"]).read_bytes()
    assert sha(draft) == row["base_draft_sha256"]
    assert sha(block) == row["block_manifest_sha256"]
    assert sha(roadmap_raw) == row["roadmap_sha256"]
    assert sha(claims_raw) == row["claim_surface_manifest_sha256"]
    roadmap = json.loads(roadmap_raw)
    claims = json.loads(claims_raw)
    trace = json.loads((root / "notes/stage3_prime_round2_traceability.json").read_text())
    open_ids = [x["item_id"] for x in trace["rows"] if x["final_verdict"] in {"PARTIALLY_ADDRESSED", "CANNOT_VERIFY"}]
    assert [x["id"] for x in roadmap["items"]] == open_ids
    assert [x["item_id"] for x in row["residuals"]] == open_ids
    for surface in claims["surfaces"]:
        text = surface["original_text"].encode()
        assert draft.count(text) == 1
        assert draft[surface["utf8_start"]:surface["utf8_end"]] == text
        assert sha(text) == surface["original_text_sha256"]
    residuals += len(roadmap["items"])
    surfaces += len(claims["surfaces"])
assert residuals == scope["residual_item_count"] == 6
assert surfaces == scope["registered_surface_count"] == 51
print("PASS: 6 residuals; 51/51 surfaces exact-once")
PY
```

Batch and builder hashes:

```bash
sha256sum \
  BATCH_ROUND9_STAGE4_PRIME_SCOPE_MANIFEST.json \
  BATCH_ROUND9_STAGE4_PRIME_AUTHORIZATION_REQUEST.md \
  tools/build_round9_stage4_prime_authorization.py
```

## Frozen boundary

No manuscript, bibliography, PDF, canonical result, README, author adjudication, revision patch, or pipeline-state file was created or changed by this preparation report. Route-A tuples remain unchanged, Route B remains uninvoked, and no canonical-result refresh is authorized. The next write-producing action remains contingent on an exact author response bound to the request SHA-256 above.

Checked at `2026-08-30T12:27:35Z`.
