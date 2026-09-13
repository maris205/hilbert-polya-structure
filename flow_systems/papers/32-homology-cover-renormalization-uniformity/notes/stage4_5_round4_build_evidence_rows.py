"""Round4 P32 only: official evidence_rows API producer, source replay and collection validation.
Input facts/verdicts are fixed in the current semantic registry; no prior rows or cache are used.
Outputs are new prefix-scoped files, opened exclusively. Failure is retained and not retried here.
"""
import hashlib
import json
import pathlib
import sys
from datetime import datetime, timezone

ARS_SCRIPTS = pathlib.Path("/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.28/skills/academic-research-suite/ars/scripts")
sys.path.insert(0, str(ARS_SCRIPTS))
import evidence_rows as official

ROOT = pathlib.Path.cwd()
PAPER = ROOT / "papers/32-homology-cover-renormalization-uniformity"
PREFIX = PAPER / "notes/stage4_5_round4_"
input_path = pathlib.Path(str(PREFIX) + "official_evidence_build_input.json")
rows_path = pathlib.Path(str(PREFIX) + "evidence_rows.json")
map_path = pathlib.Path(str(PREFIX) + "evidence_source_map.json")
report_path = pathlib.Path(str(PREFIX) + "official_evidence_api_validation.json")

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def load_bound(desc):
    raw = (ROOT / desc["path"]).read_bytes()
    if len(raw) != desc["bytes"] or sha(raw) != desc["sha256"]:
        raise RuntimeError("BOUND_INPUT_MISMATCH: " + desc["path"])
    return raw

def pointer(value, path):
    for part in path.lstrip("/").split("/"):
        part = part.replace("~1", "/").replace("~0", "~")
        value = value[int(part)] if isinstance(value, list) else value[part]
    return value

def write_new(path, value):
    with path.open("x", encoding="utf-8") as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2)
        stream.write("\n")

for path in (rows_path, map_path, report_path):
    if path.exists():
        raise RuntimeError("OUTPUT_ALREADY_EXISTS: " + str(path))
start = datetime.now(timezone.utc).isoformat()
input_raw = input_path.read_bytes()
data = json.loads(input_raw)
draft = load_bound(data["current_draft"])
registry = json.loads(load_bound(data["claim_registry"]))
semantic = json.loads(load_bound(data["semantic_review"]))
claims = {r["claim_id"]: r for r in registry["claims"]}
verdicts = {r["claim"]["claim_id"]: r["verdict"] for r in semantic["rows"]}
source_map, output, pointers = {}, [], []
for item in data["tuples"]:
    row = item["row"]
    claim = claims[row["claim"]["claim_id"]]
    span = claim["draft_span"]
    if draft[span["start_byte"]:span["end_byte"]].decode("utf-8") != row["claim"]["text"]:
        raise RuntimeError("CLAIM_SPAN_MISMATCH: " + claim["claim_id"])
    if verdicts[claim["claim_id"]] != row["verdict"]:
        raise RuntimeError("VERDICT_MISMATCH: " + claim["claim_id"])
    source_text = None
    if item["source_ref"] is not None:
        ref = item["source_ref"]
        raw = (ROOT / ref["path"]).read_bytes()
        if sha(raw) != ref["expected_artifact_sha256"]:
            raise RuntimeError("SOURCE_ARTIFACT_MISMATCH: " + ref["path"])
        source_text = pointer(json.loads(raw), ref["json_pointer"])
        if source_text != ref["expected_text"]:
            raise RuntimeError("SOURCE_POINTER_MISMATCH: " + ref["path"] + ref["json_pointer"])
        slug = row["source"]["ref_slug"]
        if slug in source_map and source_map[slug] != source_text:
            raise RuntimeError("CONFLICTING_SOURCE_TEXT: " + slug)
        source_map[slug] = source_text
        pointers.append({"claim_id": claim["claim_id"], **ref})
    built = official.build(row, source_text, extracted_text=item["extracted_text"])
    # Explicit current-source replay in addition to the builder's internal checks.
    official.validate(built, source_text)
    output.append(built)
official.paginate(output, page=1, page_size=25)
if set(claims) != {r["claim"]["claim_id"] for r in output}:
    raise RuntimeError("CLAIM_POPULATION_MISMATCH")
write_new(rows_path, output)
write_new(map_path, source_map)
report = {
    "schema_version": "round10-stage4.5-round4-official-evidence-api-validation/1.0",
    "paper_id": "P32",
    "started_at_utc": start,
    "completed_at_utc": datetime.now(timezone.utc).isoformat(),
    "input": {"path": str(input_path.relative_to(ROOT)), "sha256": sha(input_raw), "bytes": len(input_raw)},
    "producer": str(ARS_SCRIPTS / "evidence_rows.py"),
    "official_calls": ["build once per tuple without cache", "validate each row against exact current held source", "paginate validates collection uniqueness and claim-level consistency"],
    "status": "PASS",
    "row_count": len(output),
    "unique_claims": len(claims),
    "source_map_count": len(source_map),
    "source_bound_rows": len(pointers),
    "rows": {"path": str(rows_path.relative_to(ROOT)), "sha256": sha(rows_path.read_bytes()), "bytes": rows_path.stat().st_size},
    "source_map": {"path": str(map_path.relative_to(ROOT)), "sha256": sha(map_path.read_bytes()), "bytes": map_path.stat().st_size},
    "scope": "Official schema/source-byte checks only. This does not establish semantic completeness, scientific truth, author facts, source-role theorem support, or integrity PASS."
}
write_new(report_path, report)
print(json.dumps(report, ensure_ascii=False))
