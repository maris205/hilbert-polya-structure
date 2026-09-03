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
        "c4c24dede98316f569d30fa231e2cf5cd3e89c82d4f971abac00e7ba11a292e1",
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
    NOTES
    / "stage4_prime_layout_superseded_attempt2_20260904/stage4_prime_revision_patch_round2.json"
)
archived_patch = json.loads(archived_patch_path.read_text(encoding="utf-8"))
second_patch = json.loads(second_patch_path.read_text(encoding="utf-8"))
current_op_metadata = [
    {key: value for key, value in operation.items() if key != "new_text"}
    for operation in patch["ops"]
]
archived_op_metadata = [
    {key: value for key, value in operation.items() if key != "new_text"}
    for operation in archived_patch["ops"]
]
second_op_metadata = [
    {key: value for key, value in operation.items() if key != "new_text"}
    for operation in second_patch["ops"]
]
same_top_level_bindings_first = {
    key: value for key, value in patch.items() if key != "ops"
} == {
    key: value for key, value in archived_patch.items() if key != "ops"
}
same_top_level_bindings_second = {
    key: value for key, value in patch.items() if key != "ops"
} == {
    key: value for key, value in second_patch.items() if key != "ops"
}


def remove_scoped_sloppy_controls(text: str) -> str:
    return text.replace(r"\begingroup\sloppy" + "\n", "").replace(r"\par\endgroup", "")


semantic_text_equal_to_second_after_control_removal = all(
    remove_scoped_sloppy_controls(current["new_text"]) == second["new_text"]
    for current, second in zip(patch["ops"], second_patch["ops"], strict=True)
)
semantic_text_equal_to_first_after_layout_removal = all(
    remove_scoped_sloppy_controls(current["new_text"]).replace(r"\allowbreak{}", "")
    == archived["new_text"].replace(r"\allowbreak{}", "")
    for current, archived in zip(patch["ops"], archived_patch["ops"], strict=True)
)
allowbreak_delta = {
    current["block_id"]: current["new_text"].count(r"\allowbreak{}")
    - archived["new_text"].count(r"\allowbreak{}")
    for current, archived in zip(patch["ops"], archived_patch["ops"], strict=True)
}
expected_allowbreak_delta = {
    "B0048": 0,
    "B0049": 0,
    "B0080": 0,
    "B0084": 7,
    "B0089": 0,
    "B0107": 7,
    "B0112": 13,
    "B0113": 3,
}
sloppy_open_delta = {
    current["block_id"]: current["new_text"].count(r"\begingroup\sloppy")
    - second["new_text"].count(r"\begingroup\sloppy")
    for current, second in zip(patch["ops"], second_patch["ops"], strict=True)
}
sloppy_close_delta = {
    current["block_id"]: current["new_text"].count(r"\par\endgroup")
    - second["new_text"].count(r"\par\endgroup")
    for current, second in zip(patch["ops"], second_patch["ops"], strict=True)
}
expected_sloppy_delta = {
    "B0048": 0,
    "B0049": 0,
    "B0080": 0,
    "B0084": 0,
    "B0089": 0,
    "B0107": 1,
    "B0112": 1,
    "B0113": 1,
}
current_text_by_block = {row["block_id"]: row["new_text"] for row in patch["ops"]}
scoped_control_placement = (
    current_text_by_block["B0107"].startswith(
        r"\section*{Data and Materials Availability}"
        + "\n"
        + r"\begingroup\sloppy"
        + "\n"
    )
    and current_text_by_block["B0107"].endswith(r"\par\endgroup")
    and current_text_by_block["B0112"].startswith(r"\begingroup\sloppy" + "\n")
    and current_text_by_block["B0112"].endswith(r"\par\endgroup")
    and current_text_by_block["B0113"].startswith(r"\begingroup\sloppy" + "\n")
    and current_text_by_block["B0113"].endswith(r"\par\endgroup")
)
check(
    "layout_reemission_semantic_neutrality_across_attempts",
    same_top_level_bindings_first
    and same_top_level_bindings_second
    and current_op_metadata == archived_op_metadata == second_op_metadata
    and semantic_text_equal_to_second_after_control_removal
    and semantic_text_equal_to_first_after_layout_removal
    and allowbreak_delta == expected_allowbreak_delta
    and sloppy_open_delta == expected_sloppy_delta
    and sloppy_close_delta == expected_sloppy_delta
    and scoped_control_placement,
    {
        "first_superseded_patch_sha256": sha256(archived_patch_path),
        "second_superseded_patch_sha256": sha256(second_patch_path),
        "current_patch_sha256": sha256(patch_path),
        "same_top_level_bindings_first": same_top_level_bindings_first,
        "same_top_level_bindings_second": same_top_level_bindings_second,
        "same_ordered_operation_metadata": (
            current_op_metadata == archived_op_metadata == second_op_metadata
        ),
        "semantic_text_equal_to_second_after_control_removal": (
            semantic_text_equal_to_second_after_control_removal
        ),
        "semantic_text_equal_to_first_after_layout_removal": (
            semantic_text_equal_to_first_after_layout_removal
        ),
        "allowbreak_delta_by_block": allowbreak_delta,
        "sloppy_open_delta_by_block": sloppy_open_delta,
        "sloppy_close_delta_by_block": sloppy_close_delta,
        "scoped_control_placement": scoped_control_placement,
    },
)
check(
    "attempt2_five_overfull_boxes_preserved_as_incident_evidence",
    (
        NOTES
        / "stage4_prime_layout_superseded_attempt2_20260904/stage4_prime_revision_round2.preflight.log"
    )
    .read_text(encoding="utf-8")
    .count(r"Overfull \hbox")
    == 5
    and "reduced the layout failures from seven to five"
    in (NOTES / "stage4_prime_layout_preflight_incident_round2.md").read_text(
        encoding="utf-8"
    )
    and "maximum `69.53595pt`"
    in (NOTES / "stage4_prime_layout_preflight_incident_round2.md").read_text(
        encoding="utf-8"
    ),
    {
        "attempt2_overfull_boxes": 5,
        "attempt2_result": "FAIL_CLOSED_LAYOUT_ONLY",
        "current_writer_build_status": "NOT_RUN",
    },
)

expected_layout_tokens = {
    "B0084": [
        r"\texttt{902f1acb\allowbreak{}ee591692\allowbreak{}f8c5f533\allowbreak{}39590044\allowbreak{}8911d66f\allowbreak{}eda7904d\allowbreak{}5e56513f\allowbreak{}39804b3d}",
    ],
    "B0107": [
        r"\texttt{p29-\allowbreak{}source-\allowbreak{}inventory-\allowbreak{}to-\allowbreak{}literature-\allowbreak{}matrix-\allowbreak{}crosswalk/\allowbreak{}1.0}",
    ],
    "B0112": [
        r"\texttt{SPLIT\_\allowbreak{}IDEAL\_\allowbreak{}CODOMAIN\_\allowbreak{}OBSTRUCTION}",
        r"\texttt{PERFORMANCE\_\allowbreak{}MECHANISM\_\allowbreak{}HASH\_\allowbreak{}MISMATCH\_\allowbreak{}STOP}",
        r"\texttt{PERFORMANCE\_\allowbreak{}POPULATION\_\allowbreak{}RECONCILIATION\_\allowbreak{}STOP}",
        r"\texttt{REPLAY\_\allowbreak{}FIRST\_\allowbreak{}MISMATCH\_\allowbreak{}STOP}",
    ],
    "B0113": [
        r"\texttt{CONTROL\_\allowbreak{}LABEL\_\allowbreak{}DEPENDENCE\_\allowbreak{}STOP}",
    ],
}
layout_token_failures: list[str] = []
for block_id, tokens in expected_layout_tokens.items():
    current_text = next(row["new_text"] for row in patch["ops"] if row["block_id"] == block_id)
    archived_text = next(
        row["new_text"] for row in archived_patch["ops"] if row["block_id"] == block_id
    )
    for token in tokens:
        raw_token = token.replace(r"\allowbreak{}", "")
        if current_text.count(token) != 1:
            layout_token_failures.append(f"{block_id}: chunked token count is not one")
        if raw_token in current_text:
            layout_token_failures.append(f"{block_id}: raw offending token remains")
        if archived_text.count(raw_token) != 1:
            layout_token_failures.append(f"{block_id}: superseded raw token count is not one")
check(
    "layout_offending_tokens_have_discretionary_breaks",
    not layout_token_failures,
    {
        "blocks": {block_id: len(tokens) for block_id, tokens in expected_layout_tokens.items()},
        "token_count": sum(len(tokens) for tokens in expected_layout_tokens.values()),
        "failures": layout_token_failures,
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
        "incident_sha256": "c4c24dede98316f569d30fa231e2cf5cd3e89c82d4f971abac00e7ba11a292e1",
        "first_superseded_patch_path": "notes/stage4_prime_layout_superseded_20260904/stage4_prime_revision_patch_round2.json",
        "first_superseded_patch_sha256": "843a25c2ea3f18ce7f53151fcbbb0cc5ecd1c52394758b8a1fc3cc1e72fa7dc8",
        "second_superseded_patch_path": "notes/stage4_prime_layout_superseded_attempt2_20260904/stage4_prime_revision_patch_round2.json",
        "second_superseded_patch_sha256": "26df9d32270950dcfe0ac323430ab714e5666507aee4fe084486f315584f0402",
        "current_patch_sha256": sha256(patch_path),
        "semantic_neutrality": "PASS_AFTER_REMOVING_SCOPED_SLOPPY_CONTROLS_TO_ATTEMPT2_AND_ALL_LAYOUT_CONTROLS_TO_ATTEMPT1",
        "static_breakpoint_validation": "PASS",
        "static_scoped_sloppy_validation": "PASS",
        "scoped_sloppy_blocks": ["B0107", "B0112", "B0113"],
        "build_status": "NOT_RUN_BY_WRITER",
        "overfull_box_status": "PENDING_SEPARATE_APPLICATOR_BUILD_PREFLIGHT",
    },
    "stage4_5_status": "NOT_STARTED",
    "stage5_status": "NOT_AUTHORIZED",
}
print(json.dumps(output, ensure_ascii=False, indent=2))
raise SystemExit(0 if verdict == "PASS_WRITER_EMISSION_ONLY" else 1)
