#!/usr/bin/env python3
"""Rebind audit-only P30 runtime provenance after the P31 count-check fix.

No evidence text, claim, verdict, timestamp, or scientific input is changed.
Default: preview and validate. --publish uses the exact validated preview bytes.
"""
import argparse
import hashlib
import json
from pathlib import Path
import runpy
import tempfile

ROOT = Path(__file__).resolve().parents[1]
BUILDER_SHA = "c24f848afc99f10e6301b159c57cfa82e408dd45073a996a338c1d9cfd85fb8c"
OLD_VALIDATOR_SHA = "79ca4b364a0bbe7cdbd50b347ba8e7906476d5a00dba4f32fd590638b5d613a5"
OLD_MANIFEST_SHA = "41a23fe588d75fc53dcf4d483bbc069d543c7599684ed4815d04f6753159b782"
OLD_VALIDATION_SHA = "b8ac8088598e5246215f550cde62dbd8d637a7e0d85de0ac17e5c4f164ebd648"


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def differences(left, right, path=""):
    if type(left) is not type(right):
        raise RuntimeError(f"type changed: {path}")
    if isinstance(left, dict):
        if left.keys() != right.keys():
            raise RuntimeError(f"keys changed: {path}")
        return sum((differences(left[k], right[k], path + "/" + k) for k in left), [])
    if isinstance(left, list):
        if len(left) != len(right):
            raise RuntimeError(f"array length changed: {path}")
        return sum((differences(a, b, path + "/" + str(i)) for i, (a, b) in enumerate(zip(left, right))), [])
    return [] if left == right else [path]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--validator-sha", required=True)
    parser.add_argument("--publish", type=Path)
    args = parser.parse_args()
    builder = ROOT / "tools/rebuild_round10_stage4_5_p30_p31_dispatch.py"
    assert digest(builder.read_bytes()) == BUILDER_SHA
    m = runpy.run_path(str(builder), run_name="r10_descriptor_rebind")
    cfg = next(c for c in m["CONFIGS"] if c["paper_id"] == "P30")
    paper = ROOT / "papers" / cfg["slug"]
    notes = paper / "notes"
    validator = ROOT / "tools/audit_round10_stage4_5_round2.rb"
    assert digest(validator.read_bytes()) == args.validator_sha != OLD_VALIDATOR_SHA
    names = m["CHANGED_NAMES"]
    old = {name: (notes / name).read_bytes() for name in names}
    assert digest(old["stage4_5_round2_output_manifest.json"]) == OLD_MANIFEST_SHA
    assert digest(old["stage4_5_round2_validation_receipt.json"]) == OLD_VALIDATION_SHA
    state = {"paper": paper, "notes": notes,
             "input_manifest": json.loads((notes / "stage4_5_round2_input_manifest.json").read_bytes()),
             "archive_rows": json.loads(old["stage4_5_round2_semantic_attempt5_supersession_incident.json"])["archived_artifacts"]}
    objects = {name: json.loads(raw) for name, raw in old.items() if name.endswith(".json")}
    for name, obj in objects.items():
        assert m["jraw"](obj) == old[name], name
    catalog_name = "stage4_5_round2_local_claim_dependency_catalog.json"
    runtime = [d for d in objects[catalog_name]["dependencies"]
               if d["binding_chain"]["type"] == "CURRENT_AUTHORIZED_AUDIT_EXECUTION"]
    assert len(runtime) == 1
    assert runtime[0]["component_id"] == "P30-S45R2-E1-107:current_round2_audit_execution"
    desc = runtime[0]["binding_chain"]["validator"]
    assert desc == {"repo_path": "tools/audit_round10_stage4_5_round2.rb",
                    "sha256": OLD_VALIDATOR_SHA, "bytes": 62262}
    desc.update(sha256=args.validator_sha, bytes=validator.stat().st_size)
    candidate = dict(old)
    candidate.update({name: m["jraw"](obj) for name, obj in objects.items()})

    def refresh(obj):
        if isinstance(obj, dict):
            if "archive_path" in obj:
                return
            path = obj.get("path", obj.get("repo_path"))
            if isinstance(path, str) and "sha256" in obj:
                matched = next((name for name in names if path in (
                    "notes/" + name, str((notes / name).relative_to(ROOT)))), None)
                if matched:
                    obj["sha256"] = digest(candidate[matched])
                    if "bytes" in obj:
                        obj["bytes"] = len(candidate[matched])
            for value in obj.values():
                refresh(value)
        elif isinstance(obj, list):
            for value in obj:
                refresh(value)

    for _ in range(30):
        before = dict(candidate)
        for obj in objects.values():
            refresh(obj)
        candidate.update({name: m["jraw"](obj) for name, obj in objects.items()})
        if candidate == before:
            break
    else:
        raise RuntimeError("descriptor graph did not converge")
    changed = {name: raw for name, raw in candidate.items() if raw != old[name]}
    diff = {name: differences(json.loads(old[name]), json.loads(raw)) for name, raw in changed.items()}
    assert all(p.rsplit("/", 1)[-1] in {"sha256", "bytes"} for paths in diff.values() for p in paths)
    assert candidate["stage4_5_round2_evidence_rows.json"] == old["stage4_5_round2_evidence_rows.json"]
    assert candidate["stage4_5_round2_semantic_attempt5_supersession_incident.json"] == old["stage4_5_round2_semantic_attempt5_supersession_incident.json"]
    assert candidate["stage4_5_round2_attempt_lineage.json"] == old["stage4_5_round2_attempt_lineage.json"]
    with tempfile.TemporaryDirectory(prefix="r10-p30-rebind-validation-") as tmp:
        m["validate_candidates"](cfg, state, candidate, Path(tmp))
    if args.publish:
        preview = args.publish
        assert preview.is_dir() and not preview.is_symlink()
        assert {p.name for p in preview.iterdir()} == names
        assert all((preview / name).is_file() and not (preview / name).is_symlink()
                   and (preview / name).read_bytes() == raw for name, raw in candidate.items())
        archive = notes / "stage4_5_round2_TEMP9_PRE_VALIDATOR_COUNT_REBIND_archive"
        assert not archive.exists()
        archive_rows = list(json.loads(old["stage4_5_round2_output_manifest.json"])["artifacts"])
        archive_rows += [m["artifact"]("notes/" + name, old[name]) for name in (
            "stage4_5_round2_output_manifest.json", "stage4_5_round2_validation_receipt.json")]
        for row in archive_rows:
            original = m["resolve_package_binding_path"](paper, row["path"])
            assert digest(original.read_bytes()) == row["sha256"] and original.stat().st_size == row["bytes"]
            row["archive_path"] = "notes/" + archive.name + "/" + Path(row["path"]).name
        assert len({Path(r["archive_path"]).name for r in archive_rows}) == len(archive_rows)
        m["archive_old"]({"paper": paper, "archive": archive, "archive_rows": archive_rows})
        m["publish"](state, changed)
        m["validate_final"](cfg, state)
        print("PASS_EXACT_DESCRIPTOR_REBIND_PUBLISHED", len(changed), "archive", len(archive_rows))
    else:
        preview = Path(tempfile.mkdtemp(prefix="r10-p30-validator-rebind-")) / "P30"
        preview.mkdir()
        for name, raw in candidate.items():
            (preview / name).write_bytes(raw)
        print("PASS_DESCRIPTOR_ONLY_PREVIEW", preview)
    print(json.dumps({"changed_json_pointers": diff, "descriptors": [
        m["artifact"](name, raw) for name, raw in sorted(changed.items())]}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
