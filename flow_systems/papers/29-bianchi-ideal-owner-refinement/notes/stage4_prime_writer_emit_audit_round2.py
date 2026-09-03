from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

from jsonschema import Draft202012Validator

WORKSPACE = Path(__file__).resolve().parents[3]
PAPER = Path(__file__).resolve().parents[1]
NOTES = Path(__file__).resolve().parent
ARS_SCHEMA = Path(
    "/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/"
    "skills/academic-research-suite/ars/shared/contracts/patch/"
    "revision_patch.schema.json"
)

AUTHORITY_ROOTS = {
    "BATCH_ROUND10_STAGE4_PRIME_EXECUTION_STAGE4_5_AND_ROUND5_AUTHORIZATION_RECEIPT.json":
        "4cc48a512c35dc31ccff0b1ff80472eed04fc454d83f4410277bd2fe356e4e4c",
    "BATCH_ROUND10_STAGE4_PRIME_EXECUTION_STAGE4_5_AND_ROUND5_INPUT_FREEZE.json":
        "081f28e0ade1af62d8f5d56d90b83ff543e1019ab1931473ff95754e81855e98",
    "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P29_P32.json":
        "3a17181450f040e274f1fa6c31386ff2593c04f409013908bfad759d408d65fa",
}

SUPPORT_EXPECTED = {
    "stage4_prime_authority_validation_round2.json":
        "397d55dd634e0cbe3169c01e097eba6b23f6454350d4595fc361c71cba654a29",
    "stage4_prime_literature_replay_round2.raw.json":
        "3c7139a23df40b3f9315af74aa6fbacc7cbc06f7d349e9b4e785e45ad2ed28f3",
    "stage4_prime_literature_screening_ledger_round2.json":
        "a38a89f7802f6199ebe4de94217075abfe61b1707d7c0b730dd99989da2e0f81",
    "stage4_prime_literature_screening_ledger_round2.tsv":
        "2d4bf2fb0c63f0c9904fcd16dab90296278499c4611c83214482950fd8c6acb2",
    "stage4_prime_inventory_matrix_crosswalk_round2.json":
        "fde57cac6ae3a41d9d895eff6a7a480b1b9f560bed4f271ec7aa97eda8929016",
    "stage4_prime_inventory_matrix_crosswalk_round2.tsv":
        "c208570909fcf8b1e9902c5fac1471ce3a8392b04cdbdb91848cc933465300b9",
    "stage4_prime_sf_literal_01_definition_round2.json":
        "902f1acbee591692f8c5f533395900448911d66feda7904d5e56513f39804b3d",
    "stage4_prime_references_round2.bib":
        "c78ea003596e5c27fb1332643db2654dd6a67f96b9ba25b923cd2af655540555",
    "stage4_prime_replay_references_round2.bib":
        "2e8f56d531e08dfa16259531acdbbd934877ae0ca6d18cc30604be86f364446c",
}

LAYOUT_LINEAGE_EXPECTED = {
    "stage4_prime_layout_preflight_incident_round2.md":
        "4b5dab4e3527d920b23a95dd5825c3af55de28050733c5d859b6bc2b2f32bb7c",
    "stage4_prime_layout_superseded_20260904/stage4_prime_revision_patch_round2.json":
        "843a25c2ea3f18ce7f53151fcbbb0cc5ecd1c52394758b8a1fc3cc1e72fa7dc8",
    "stage4_prime_layout_superseded_20260904/stage4_prime_revision_round2.tex":
        "7cce1c333bcdca7ef4eb2eca5f7d9f4fbbc1b7b4f97911aa5d4f995c7d3cd1ed",
    "stage4_prime_layout_superseded_20260904/stage4_prime_revision_round2.tex.apply-report.json":
        "9a399cecb749a728d7bf61a7e5dc4bbdbdc51bd4053971b9d1778ccffd71a17b",
    "stage4_prime_layout_superseded_attempt2_20260904/stage4_prime_revision_patch_round2.json":
        "26df9d32270950dcfe0ac323430ab714e5666507aee4fe084486f315584f0402",
    "stage4_prime_layout_superseded_attempt2_20260904/stage4_prime_revision_round2.tex":
        "c4e8e617a4d87a30c25b245edca1439a959cf952be4e24ef2cae218b04125ffa",
    "stage4_prime_layout_superseded_attempt2_20260904/stage4_prime_revision_round2.tex.apply-report.json":
        "8033de7722d4ac308001f134fc275f9453550893c0aee34c91cdaba0cc7d2f59",
    "stage4_prime_layout_superseded_attempt2_20260904/stage4_prime_revision_round2.preflight.log":
        "f4ddedb4b895bc03b9cbb2d8eb099c367fc1fd3155da380b25558ac9ecd345bb",
    "stage4_prime_layout_superseded_attempt2_20260904/stage4_prime_revision_round2.preflight.pdf":
        "9e475424fce8c0556023a49f710c876e0634370ec7f98d8012f35d09f2f2247c",
    "stage4_prime_layout_superseded_attempt3_20260904/stage4_prime_revision_patch_round2.json":
        "d02911b1f000716d703c68934dca899120de00c2f8d311778d55d9b7793f7135",
    "stage4_prime_layout_superseded_attempt3_20260904/stage4_prime_revision_round2.tex":
        "3eb2aae993d6e513688705cb0d6eebe63d0e2012ef01415573e1db420b7970d6",
    "stage4_prime_layout_superseded_attempt3_20260904/stage4_prime_revision_round2.tex.apply-report.json":
        "8283d3770118134528217e03c2c25b5c8c1b8ed3e1a4f7d566b50144fd77c155",
    "stage4_prime_layout_superseded_attempt3_20260904/manuscript.log":
        "ef117499b02f846a9c591780c6859041b3a26965053cb0c268122ba3e711072d",
    "stage4_prime_layout_superseded_attempt3_20260904/manuscript.pdf":
        "b7f37eda750195f8d1fdcec72f96a51149f2341ac2a112cbed849a24c98a5843",
    "stage4_prime_layout_superseded_attempt3_20260904/p29-stage4-prime-attempt3-bibtex.out":
        "5d29263f97349aa03b65987179a5c7b6e122091607ef026acaf07098763a373b",
    "stage4_prime_layout_superseded_attempt3_20260904/p29-stage4-prime-attempt3-pass1.out":
        "fe3447ba33e6d4b01ffb823738857fdcfa6dfdb1317263332fa70a1af02e37f6",
    "stage4_prime_layout_superseded_attempt3_20260904/p29-stage4-prime-attempt3-pass2.out":
        "ed00ca850129feeeebabe0fa938179c100cafc529c9539a7626c029fdcb61790",
    "stage4_prime_layout_superseded_attempt3_20260904/p29-stage4-prime-attempt3-pass3.out":
        "8eaa149aa70349b9f17311c51d03657f084ef4ee108a825ce57032e022c0317e",
    "stage4_prime_layout_superseded_attempt4_20260904/stage4_prime_revision_patch_round2.json":
        "7827a265b0148151c6c317caa8c00782d3bdaec5152edee6e8ad6f2ac3868f77",
    "stage4_prime_layout_superseded_attempt4_20260904/stage4_prime_revision_round2.tex":
        "f6d7548c3ee80b130169f8c6f5d6a8991b5c87eca0ab59a82a19464559a954a5",
    "stage4_prime_layout_superseded_attempt4_20260904/stage4_prime_revision_round2.tex.apply-report.json":
        "c78169154fa0d7af9e4409fbb0c71670daaf6f927f954383c0b71c1f4cf3abf6",
    "stage4_prime_layout_superseded_attempt4_20260904/manuscript.log":
        "33b2b5a23452f81eef32d31099d04a90a6b9aad8d88fbe0984dc3871cebb5aac",
    "stage4_prime_layout_superseded_attempt4_20260904/manuscript.pdf":
        "d9887bd42fa2754931b78762fa364166c7ea14e8b83b84c8e0638fae59d50d3f",
    "stage4_prime_layout_superseded_attempt4_20260904/p29-stage4-prime-attempt4-bibtex.out":
        "5d29263f97349aa03b65987179a5c7b6e122091607ef026acaf07098763a373b",
    "stage4_prime_layout_superseded_attempt4_20260904/p29-stage4-prime-attempt4-pass1.out":
        "5dcadff2b4515609bec4bb4c74016e6ba8f42e9006e1e95562365d2110d4a277",
    "stage4_prime_layout_superseded_attempt4_20260904/p29-stage4-prime-attempt4-pass2.out":
        "f12d7392d0c80af752755bcbe7d15d73d10870abb8ac7578ecb55750ed38ae3e",
    "stage4_prime_layout_superseded_attempt4_20260904/p29-stage4-prime-attempt4-pass3.out":
        "81e05adaf6d27c7c0fbb3b82c1b050d831753a26d84ee1a0e07ec875bb7fb9dd",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(name: str):
    return json.loads((NOTES / name).read_text(encoding="utf-8"))


checks: list[dict] = []


def check(name: str, condition: bool, detail) -> None:
    checks.append({"check": name, "status": "PASS" if condition else "FAIL", "detail": detail})


for rel, expected in AUTHORITY_ROOTS.items():
    path = WORKSPACE / rel
    actual = sha256(path)
    check(f"authority_sha::{rel}", actual == expected, {"expected": expected, "actual": actual})

handoff_path = NOTES / "stage4_prime_writer_authority_handoff.json"
handoff = load(handoff_path.name)
check(
    "writer_authority_handoff_sha",
    sha256(handoff_path) == "371b0d9a7c92f3ef159d9eb5fd6fb8c81c3c0c5c7755173a65f6b2d79c2b6e8f",
    sha256(handoff_path),
)

for rel, expected in SUPPORT_EXPECTED.items():
    actual = sha256(NOTES / rel)
    check(f"support_sha::{rel}", actual == expected, {"expected": expected, "actual": actual})

for rel, expected in LAYOUT_LINEAGE_EXPECTED.items():
    actual = sha256(NOTES / rel)
    check(f"layout_lineage_sha::{rel}", actual == expected, {"expected": expected, "actual": actual})

freeze = json.loads(
    (WORKSPACE / "BATCH_ROUND10_STAGE4_PRIME_EXECUTION_STAGE4_5_AND_ROUND5_INPUT_FREEZE.json")
    .read_text(encoding="utf-8")
)
p29_freeze = next(row for row in freeze["papers"] if row["paper_id"] == "P29")
for entry in p29_freeze["canonical_files"] + p29_freeze["science_files"]:
    path = WORKSPACE / entry["path"]
    check(
        f"frozen_path::{entry['path']}",
        path.is_file() and sha256(path) == entry["sha256"] and path.stat().st_size == entry["bytes"],
        {"expected_sha256": entry["sha256"], "actual_sha256": sha256(path), "bytes": path.stat().st_size},
    )

canonical_bibliography = PAPER / "paper/references.bib"
build_bibliography = NOTES / "stage4_prime_references_round2.bib"
replay_bibliography = NOTES / "stage4_prime_replay_references_round2.bib"
check(
    "build_bibliography_byte_identical_to_canonical",
    build_bibliography.read_bytes() == canonical_bibliography.read_bytes()
    and len(re.findall(r"^@[A-Za-z]+\{", build_bibliography.read_text(encoding="utf-8"), re.MULTILINE))
    == 22,
    {
        "canonical_sha256": sha256(canonical_bibliography),
        "build_input_sha256": sha256(build_bibliography),
        "bytes": build_bibliography.stat().st_size,
        "entries": len(
            re.findall(
                r"^@[A-Za-z]+\{",
                build_bibliography.read_text(encoding="utf-8"),
                re.MULTILINE,
            )
        ),
    },
)
replay_bib_text = replay_bibliography.read_text(encoding="utf-8")
check(
    "replay_bibliography_support_only",
    "notes-side bibliography snapshot" in replay_bib_text
    and "not the canonical bibliography" in replay_bib_text
    and len(re.findall(r"^@[A-Za-z]+\{", replay_bib_text, re.MULTILINE)) == 22,
    {
        "sha256": sha256(replay_bibliography),
        "entries": len(re.findall(r"^@[A-Za-z]+\{", replay_bib_text, re.MULTILINE)),
        "role": "SUPPORT_ONLY_NOT_BUILD_INPUT",
    },
)

source = (NOTES / "stage1_phase2_annotated_bibliography.md").read_text(encoding="utf-8")
query_section = source.split("### Query families and strings executed verbatim", 1)[1].split(
    "Exact DOI calls used to resolve metadata", 1
)[0]
frozen_queries: list[str] = []
inside = False
for line in query_section.splitlines():
    if line == "```text":
        inside = True
    elif line == "```":
        inside = False
    elif inside and line.strip():
        frozen_queries.append(line)

replay = load("stage4_prime_literature_replay_round2.raw.json")
observed_queries = [row["q"] for row in replay["queries"]]
check(
    "frozen_query_exact_replay",
    len(frozen_queries) == 53 and observed_queries == frozen_queries,
    {"frozen": len(frozen_queries), "observed": len(observed_queries)},
)
check(
    "replay_counts",
    replay["counts"]
    == {
        "query_lines": 53,
        "query_success": 48,
        "query_unavailable": 5,
        "inspected_manifestations": 139,
    },
    replay["counts"],
)
check(
    "historical_rows_preserved_unavailable",
    replay["historical_boundary"]["original_session_rejected_row_identifiers"] == "unavailable"
    and replay["historical_boundary"]["original_session_row_level_inclusion_exclusion_decisions"]
    == "unavailable"
    and replay["historical_boundary"]["substitution_with_replay_rows"] is False,
    replay["historical_boundary"],
)

ledger = load("stage4_prime_literature_screening_ledger_round2.json")
screen_counts: dict[str, int] = {}
for row in ledger["rows"]:
    screen_counts[row["screen_decision"]] = screen_counts.get(row["screen_decision"], 0) + 1
check(
    "ledger_row_identity_and_counts",
    len(ledger["rows"]) == 144
    and len({row["row_id"] for row in ledger["rows"]}) == 144
    and screen_counts
    == {
        "EXCLUDED_REPLAY_ONLY": 53,
        "RETAINED_EXISTING_ADMITTED_SOURCE": 19,
        "DUPLICATE_REMOVED": 50,
        "EXCLUDED_SOURCE_TYPE": 15,
        "UNAVAILABLE": 5,
        "EXCLUDED_SCOPE_CRITERION": 2,
    },
    {"rows": len(ledger["rows"]), "screen_counts": screen_counts},
)
check(
    "ledger_no_historical_substitution",
    all(row["historical_row_substitution"] is False for row in ledger["rows"]),
    "all 144 rows false",
)

crosswalk = load("stage4_prime_inventory_matrix_crosswalk_round2.json")
expected_ids = [f"P29-S{i:02d}" for i in range(1, 23)]
check(
    "crosswalk_closed_set",
    crosswalk["crosswalk_status"] == "PASS"
    and crosswalk["observed_ordered_set"] == expected_ids
    and len(crosswalk["rows"]) == 22
    and all(row["status"] == "MATCHED_BY_EXACT_SOURCE_ID_AND_ORDINAL" for row in crosswalk["rows"]),
    {"rows": len(crosswalk["rows"]), "status": crosswalk["crosswalk_status"]},
)

fixture = load("stage4_prime_sf_literal_01_definition_round2.json")
check(
    "sf_literal_01_defined_not_run",
    fixture["fixture_id"] == "SF-LITERAL-01"
    and fixture["status"] == "DEFINED_NOT_RUN"
    and fixture["execution_record"]["executed"] is False
    and fixture["execution_record"]["observed_disposition"] == "NOT_OBSERVED"
    and fixture["execution_record"]["performance_value"] is None,
    fixture["execution_record"],
)

patch_path = NOTES / "stage4_prime_revision_patch_round2.json"
patch = load(patch_path.name)
schema = json.loads(ARS_SCHEMA.read_text(encoding="utf-8"))
schema_errors = sorted(
    Draft202012Validator(schema).iter_errors(patch),
    key=lambda error: tuple(str(part) for part in error.path),
)
check(
    "patch_1_1_schema",
    not schema_errors,
    [{"path": list(error.path), "message": error.message} for error in schema_errors],
)

adjudication = load("stage4_prime_author_adjudication.json")
manifest = load("stage4_prime_base.block-manifest.json")
allowed = {
    row["item_id"]: {
        (target["block_id"], operation)
        for target in row["authorized_targets"]
        for operation in target["allowed_operations"]
    }
    for row in adjudication["author_adjudications"]
    if row["author_triage"] == "will_address"
}
old_hashes = {row["block_id"]: row["old_hash"] for row in manifest["blocks"]}
authorization_failures: list[str] = []
for index, operation in enumerate(patch["ops"]):
    if old_hashes.get(operation["block_id"]) != operation["old_hash"]:
        authorization_failures.append(f"op {index}: stale old_hash")
    for item_id in operation["roadmap_item_ids"]:
        if (operation["block_id"], operation["op"]) not in allowed.get(item_id, set()):
            authorization_failures.append(f"op {index}: unauthorized {item_id}")
    if operation["claim_strength_changes"] or operation["collateral_authorization_ids"]:
        authorization_failures.append(f"op {index}: unauthorized claim/collateral array")
    if "<!--block:" in operation.get("new_text", ""):
        authorization_failures.append(f"op {index}: writer inserted block marker")

exact_blocks = {"B0048", "B0049", "B0080", "B0084", "B0089", "B0107", "B0112", "B0113"}
check(
    "patch_exact_authorized_scope",
    not authorization_failures
    and len(patch["ops"]) == 8
    and {row["block_id"] for row in patch["ops"]} == exact_blocks
    and len({row["block_id"] for row in patch["ops"]}) == len(patch["ops"]),
    authorization_failures,
)
check(
    "patch_exact_bindings",
    patch["base_draft_hash"] == handoff["base_draft"]["sha256"][:12]
    and patch["roadmap_sha256"] == handoff["roadmap"]["sha256"]
    and patch["author_adjudication_sha256"] == handoff["author_adjudication"]["sha256"]
    and patch["author_decision_digest"] == handoff["author_decision_digest"]
    and patch["claim_surface_manifest_sha256"] == handoff["claim_surface_manifest"]["sha256"],
    {
        "base_draft_hash": patch["base_draft_hash"],
        "roadmap_sha256": patch["roadmap_sha256"],
        "author_adjudication_sha256": patch["author_adjudication_sha256"],
        "author_decision_digest": patch["author_decision_digest"],
        "claim_surface_manifest_sha256": patch["claim_surface_manifest_sha256"],
    },
)

archived_patch_path = (
    NOTES / "stage4_prime_layout_superseded_20260904/stage4_prime_revision_patch_round2.json"
)
second_patch_path = (
    NOTES / "stage4_prime_layout_superseded_attempt2_20260904/stage4_prime_revision_patch_round2.json"
)
third_patch_path = (
    NOTES / "stage4_prime_layout_superseded_attempt3_20260904/stage4_prime_revision_patch_round2.json"
)
fourth_patch_path = (
    NOTES / "stage4_prime_layout_superseded_attempt4_20260904/stage4_prime_revision_patch_round2.json"
)
archived_patch = json.loads(archived_patch_path.read_text(encoding="utf-8"))
second_patch = json.loads(second_patch_path.read_text(encoding="utf-8"))
third_patch = json.loads(third_patch_path.read_text(encoding="utf-8"))
fourth_patch = json.loads(fourth_patch_path.read_text(encoding="utf-8"))
patches = [archived_patch, second_patch, third_patch, fourth_patch, patch]
metadata_sets = [
    [{key: value for key, value in operation.items() if key != "new_text"} for operation in item["ops"]]
    for item in patches
]
top_level_bindings = [{key: value for key, value in item.items() if key != "ops"} for item in patches]

attempt4_b0080_literal = r"\texttt{p29-source-inventory-to-literature-matrix-crosswalk/1.0}"
attempt5_literal = r"\path{p29-source-inventory-to-literature-matrix-crosswalk/1.0}"
attempt3_b0107_literal = (
    r"\texttt{p29-\allowbreak{}source-\allowbreak{}inventory-\allowbreak{}to-"
    r"\allowbreak{}literature-\allowbreak{}matrix-\allowbreak{}crosswalk/"
    r"\allowbreak{}1.0}"
)
visible_literal = "p29-source-inventory-to-literature-matrix-crosswalk/1.0"


def inverse_attempt5(text: str) -> str:
    if text.startswith(r"\begingroup\sloppy" + "\n") and text.endswith(r"\par\endgroup"):
        text = text.removeprefix(r"\begingroup\sloppy" + "\n").removesuffix(r"\par\endgroup")
    return text.replace(attempt5_literal, attempt4_b0080_literal)


def remove_scoped_sloppy_controls(text: str) -> str:
    return text.replace(r"\begingroup\sloppy" + "\n", "").replace(r"\par\endgroup", "")


current_by = {row["block_id"]: row for row in patch["ops"]}
first_by = {row["block_id"]: row for row in archived_patch["ops"]}
second_by = {row["block_id"]: row for row in second_patch["ops"]}
third_by = {row["block_id"]: row for row in third_patch["ops"]}
fourth_by = {row["block_id"]: row for row in fourth_patch["ops"]}
changed_from_fourth = [bid for bid in current_by if current_by[bid]["new_text"] != fourth_by[bid]["new_text"]]
attempt4_exact_recovery = all(
    (inverse_attempt5(current_by[bid]["new_text"]) if bid == "B0080" else current_by[bid]["new_text"])
    == fourth_by[bid]["new_text"] for bid in current_by
)
visible_old = attempt4_b0080_literal.removeprefix(r"\texttt{").removesuffix("}")
visible_new = attempt5_literal.removeprefix(r"\path{").removesuffix("}")
literal_rendering_exact = (
    current_by["B0080"]["new_text"].count(attempt5_literal) == 1
    and current_by["B0080"]["new_text"].count(attempt4_b0080_literal) == 0
    and fourth_by["B0080"]["new_text"].count(attempt4_b0080_literal) == 1
    and fourth_by["B0080"]["new_text"].count(attempt5_literal) == 0
    and current_by["B0107"]["new_text"].count(attempt5_literal) == 1
    and current_by["B0107"]["new_text"] == fourth_by["B0107"]["new_text"]
    and visible_old == visible_new == visible_literal
)
b0080_group_exact = (
    current_by["B0080"]["new_text"].startswith(r"\begingroup\sloppy" + "\n")
    and current_by["B0080"]["new_text"].endswith(r"\par\endgroup")
    and fourth_by["B0080"]["new_text"].count(r"\begingroup\sloppy") == 0
    and fourth_by["B0080"]["new_text"].count(r"\par\endgroup") == 0
)
scoped_blocks = ["B0080", "B0107", "B0112", "B0113"]
scoped_control_placement = b0080_group_exact and all(
    current_by[bid]["new_text"].count(r"\begingroup\sloppy") == 1
    and current_by[bid]["new_text"].count(r"\par\endgroup") == 1
    for bid in scoped_blocks
) and all(
    current_by[bid]["new_text"].count(r"\begingroup\sloppy") == 0
    and current_by[bid]["new_text"].count(r"\par\endgroup") == 0
    for bid in current_by if bid not in scoped_blocks
)
allowbreak_delta = {
    bid: current_by[bid]["new_text"].count(r"\allowbreak{}")
    - first_by[bid]["new_text"].count(r"\allowbreak{}") for bid in current_by
}
expected_allowbreak_delta = {
    "B0048": 0, "B0049": 0, "B0080": 0, "B0084": 7,
    "B0089": 0, "B0107": 0, "B0112": 13, "B0113": 3,
}
sloppy_delta = {
    bid: current_by[bid]["new_text"].count(r"\begingroup\sloppy")
    - second_by[bid]["new_text"].count(r"\begingroup\sloppy") for bid in current_by
}
expected_sloppy_delta = {
    "B0048": 0, "B0049": 0, "B0080": 1, "B0084": 0,
    "B0089": 0, "B0107": 1, "B0112": 1, "B0113": 1,
}
check(
    "layout_reemission_semantic_neutrality_across_attempts",
    all(item == top_level_bindings[0] for item in top_level_bindings[1:])
    and all(item == metadata_sets[0] for item in metadata_sets[1:])
    and changed_from_fourth == ["B0080"]
    and attempt4_exact_recovery
    and literal_rendering_exact
    and scoped_control_placement
    and allowbreak_delta == expected_allowbreak_delta
    and sloppy_delta == expected_sloppy_delta,
    {
        "first_superseded_patch_sha256": sha256(archived_patch_path),
        "second_superseded_patch_sha256": sha256(second_patch_path),
        "third_superseded_patch_sha256": sha256(third_patch_path),
        "fourth_superseded_patch_sha256": sha256(fourth_patch_path),
        "current_patch_sha256": sha256(patch_path),
        "same_top_level_bindings_all_attempts": all(item == top_level_bindings[0] for item in top_level_bindings[1:]),
        "same_ordered_operation_metadata_all_attempts": all(item == metadata_sets[0] for item in metadata_sets[1:]),
        "changed_blocks_relative_to_attempt4": changed_from_fourth,
        "attempt4_exact_recovery_after_inverse_layout_substitution_and_group_removal": attempt4_exact_recovery,
        "visible_literal_equivalence": literal_rendering_exact,
        "allowbreak_delta_by_block_relative_to_attempt1": allowbreak_delta,
        "sloppy_delta_by_block_relative_to_attempt2": sloppy_delta,
        "scoped_control_placement": scoped_control_placement,
    },
)
check(
    "attempt4_one_overfull_box_preserved_as_incident_evidence",
    (NOTES / "stage4_prime_layout_superseded_attempt4_20260904/manuscript.log")
    .read_text(encoding="utf-8").count(r"Overfull \hbox") == 1
    and "B0080" in (NOTES / "stage4_prime_layout_preflight_incident_round2.md").read_text(encoding="utf-8")
    and "28.86852pt" in (NOTES / "stage4_prime_layout_preflight_incident_round2.md").read_text(encoding="utf-8"),
    {
        "attempt4_overfull_boxes": 1,
        "attempt4_remaining_block": "B0080",
        "attempt4_result": "FAIL_CLOSED_LAYOUT_ONLY",
        "current_writer_build_status": "NOT_RUN",
    },
)
expected_discretionary_tokens = {
    "B0084": [r"\texttt{902f1acb\allowbreak{}ee591692\allowbreak{}f8c5f533\allowbreak{}39590044\allowbreak{}8911d66f\allowbreak{}eda7904d\allowbreak{}5e56513f\allowbreak{}39804b3d}"],
    "B0112": [
        r"\texttt{SPLIT\_\allowbreak{}IDEAL\_\allowbreak{}CODOMAIN\_\allowbreak{}OBSTRUCTION}",
        r"\texttt{PERFORMANCE\_\allowbreak{}MECHANISM\_\allowbreak{}HASH\_\allowbreak{}MISMATCH\_\allowbreak{}STOP}",
        r"\texttt{PERFORMANCE\_\allowbreak{}POPULATION\_\allowbreak{}RECONCILIATION\_\allowbreak{}STOP}",
        r"\texttt{REPLAY\_\allowbreak{}FIRST\_\allowbreak{}MISMATCH\_\allowbreak{}STOP}",
    ],
    "B0113": [r"\texttt{CONTROL\_\allowbreak{}LABEL\_\allowbreak{}DEPENDENCE\_\allowbreak{}STOP}"],
}
failures=[]
for bid,tokens in expected_discretionary_tokens.items():
    for token in tokens:
        raw=token.replace(r"\allowbreak{}","")
        if current_by[bid]["new_text"].count(token)!=1: failures.append(f"{bid}: chunked token count")
        if raw in current_by[bid]["new_text"]: failures.append(f"{bid}: raw token remains")
check(
    "layout_offending_tokens_have_breakable_rendering",
    not failures and literal_rendering_exact and b0080_group_exact,
    {
        "path_macro_blocks": ["B0080","B0107"],
        "path_macro_literal": visible_literal,
        "visible_literal_equivalence": literal_rendering_exact,
        "scoped_sloppy_blocks": scoped_blocks,
        "failures": failures,
        "build_status": "NOT_RUN_BY_WRITER",
    },
)

chunked_digest_pattern = re.compile(
    r"\\texttt\{(?:[0-9a-f]{8}\\allowbreak\{\}){7}[0-9a-f]{8}\}"
)
expected_display_digests = {
    "B0080": [
        "c4d71637e5676337326d2eb78dcdd64d78b4b116a397c50c54a081d7c5e2650b",
        "67ed7713bd6881d11466dc16755c7660a458c52e07ee072d086d6467f8ad7bd8",
        "bcf5fa7af07f353fbcaaa6fca319e79f173d7a6af070b58276a91fe9a44d8901",
        "219309f0c8cea9106ba162c95f2de266b78b1c5d8e0d541e5b4a0e8122247d2c",
        "3c7139a23df40b3f9315af74aa6fbacc7cbc06f7d349e9b4e785e45ad2ed28f3",
        "a38a89f7802f6199ebe4de94217075abfe61b1707d7c0b730dd99989da2e0f81",
        "2d4bf2fb0c63f0c9904fcd16dab90296278499c4611c83214482950fd8c6acb2",
        "fde57cac6ae3a41d9d895eff6a7a480b1b9f560bed4f271ec7aa97eda8929016",
        "c208570909fcf8b1e9902c5fac1471ce3a8392b04cdbdb91848cc933465300b9",
    ],
    "B0107": [
        "3c7139a23df40b3f9315af74aa6fbacc7cbc06f7d349e9b4e785e45ad2ed28f3",
        "a38a89f7802f6199ebe4de94217075abfe61b1707d7c0b730dd99989da2e0f81",
        "2d4bf2fb0c63f0c9904fcd16dab90296278499c4611c83214482950fd8c6acb2",
        "fde57cac6ae3a41d9d895eff6a7a480b1b9f560bed4f271ec7aa97eda8929016",
        "c208570909fcf8b1e9902c5fac1471ce3a8392b04cdbdb91848cc933465300b9",
    ],
    "B0084": [
        "902f1acbee591692f8c5f533395900448911d66feda7904d5e56513f39804b3d",
    ],
}
display_digests: dict[str, list[str]] = {}
raw_digest_displays: dict[str, list[str]] = {}
for block_id in expected_display_digests:
    new_text = next(row["new_text"] for row in patch["ops"] if row["block_id"] == block_id)
    chunked = chunked_digest_pattern.findall(new_text)
    display_digests[block_id] = [
        token.removeprefix(r"\texttt{")
        .removesuffix("}")
        .replace(r"\allowbreak{}", "")
        for token in chunked
    ]
    raw_digest_displays[block_id] = re.findall(r"\\texttt\{[0-9a-f]{64}\}", new_text)
check(
    "patch_sha_typesetting_breaks",
    display_digests == expected_display_digests
    and all(not rows for rows in raw_digest_displays.values()),
    {
        "policy": "eight-hex chunks joined by semantic-neutral LaTeX allowbreak commands",
        "recovered_digest_counts": {
            block_id: len(rows) for block_id, rows in display_digests.items()
        },
        "raw_unbreakable_digest_counts": {
            block_id: len(rows) for block_id, rows in raw_digest_displays.items()
        },
    },
)
check(
    "patch_not_applied",
    not (NOTES / "stage4_prime_revision_round2.tex").exists()
    and not (NOTES / "stage4_prime_revision_round2.tex.apply-report.json").exists(),
    {
        "output_exists": (NOTES / "stage4_prime_revision_round2.tex").exists(),
        "apply_report_exists": (NOTES / "stage4_prime_revision_round2.tex.apply-report.json").exists(),
    },
)

verdict = "PASS_WRITER_EMISSION_ONLY" if all(row["status"] == "PASS" for row in checks) else "FAIL_CLOSED"
output = {
    "schema_version": "p29-stage4-prime-writer-emit-audit/1.0",
    "paper_id": "P29",
    "validated_date": "2026-09-04",
    "patch": {
        "path": str(patch_path.relative_to(PAPER)),
        "sha256": sha256(patch_path),
        "bytes": patch_path.stat().st_size,
        "ops": len(patch["ops"]),
        "apply_status": "NOT_APPLIED",
    },
    "checks": checks,
    "summary": {
        "checks": len(checks),
        "pass": sum(row["status"] == "PASS" for row in checks),
        "fail": sum(row["status"] == "FAIL" for row in checks),
    },
    "verdict": verdict,
    "layout_remediation": {
        "incident_path": "notes/stage4_prime_layout_preflight_incident_round2.md",
        "incident_sha256": "4b5dab4e3527d920b23a95dd5825c3af55de28050733c5d859b6bc2b2f32bb7c",
        "first_superseded_patch_sha256": "843a25c2ea3f18ce7f53151fcbbb0cc5ecd1c52394758b8a1fc3cc1e72fa7dc8",
        "second_superseded_patch_sha256": "26df9d32270950dcfe0ac323430ab714e5666507aee4fe084486f315584f0402",
        "third_superseded_patch_sha256": "d02911b1f000716d703c68934dca899120de00c2f8d311778d55d9b7793f7135",
        "fourth_superseded_patch_path": "notes/stage4_prime_layout_superseded_attempt4_20260904/stage4_prime_revision_patch_round2.json",
        "fourth_superseded_patch_sha256": "7827a265b0148151c6c317caa8c00782d3bdaec5152edee6e8ad6f2ac3868f77",
        "current_patch_sha256": sha256(patch_path),
        "semantic_neutrality": "PASS_AFTER_INVERSE_B0080_LITERAL_RENDERING_SUBSTITUTION_AND_GROUP_REMOVAL_TO_ATTEMPT4",
        "visible_literal_equivalence": "PASS",
        "current_layout_only_block": "B0080",
        "scoped_sloppy_blocks": ["B0080", "B0107", "B0112", "B0113"],
        "build_status": "NOT_RUN_BY_WRITER",
        "overfull_box_status": "PENDING_SEPARATE_APPLICATOR_BUILD_PREFLIGHT",
    },
    "stage4_5_status": "NOT_STARTED",
    "stage5_status": "NOT_AUTHORIZED",
}
print(json.dumps(output, ensure_ascii=False, indent=2))
raise SystemExit(0 if verdict == "PASS_WRITER_EMISSION_ONLY" else 1)
