#!/usr/bin/env python3
"""Build the static Paper 43 mutation-class registry from the frozen blueprint.

The blueprint freezes classes, not future generated mutation IDs or outcomes.
This builder therefore records all 62 table rows exactly and separately
declares the dynamic exhaustive Route traversal required at run time.
"""

from __future__ import annotations

import base64
import hashlib
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BLUEPRINT = ROOT / "inputs/blueprint/paper43_experiment_blueprint.base64.json"
BLUEPRINT_SHA256 = "4ab7098718be5992281097e250f5158e837938162a5817a2a047f112aa7e07fc"
BLUEPRINT_CONTAINER_SHA256 = "7999713493a69c4cf2a5801fa6cc59a1c638319c4e36040cd103a6d5bdcfc52c"


def slug(value: str) -> str:
    value = value.lower().replace("p39--p42", "p39_p42").replace("a3/a4", "a3_a4")
    value = re.sub(r"[^a-z0-9]+", "_", value).strip("_")
    return value


def profile(domain: str, consumers: list[str], expectation: str =
            "all_designated_consumers_reject_nonzero") -> dict[str, object]:
    return {
        "designated_consumers": sorted(consumers),
        "domain": domain,
        "expectation": expectation,
    }


def main() -> int:
    stored = BLUEPRINT.read_bytes()
    if hashlib.sha256(stored).hexdigest() != BLUEPRINT_CONTAINER_SHA256:
        raise ValueError("frozen blueprint container binding changed")
    value = json.loads(stored.decode("ascii"))
    if set(value) != {"decoded_sha256", "encoding", "payload", "role", "schema"} \
            or value["encoding"] != "base64url_no_padding" \
            or value["schema"] != "paper43-portable-byte-container-v1" \
            or value["role"] != "paper43_experiment_blueprint":
        raise ValueError("frozen blueprint container schema changed")
    payload = value["payload"]
    raw = base64.urlsafe_b64decode(payload + "=" * ((4 - len(payload) % 4) % 4))
    if hashlib.sha256(raw).hexdigest() != BLUEPRINT_SHA256 \
            or value["decoded_sha256"] != BLUEPRINT_SHA256:
        raise ValueError("frozen blueprint binding changed")
    text = raw.decode("utf-8")
    section = text.split("## 9. Adversarial mutation matrix", 1)[1].split("## 10.", 1)[0]
    rows: list[tuple[str, str, str]] = []
    for line in section.splitlines():
        if line.startswith("| ") and not line.startswith("| Class") and not line.startswith("|---"):
            fields = [field.strip() for field in line.strip("|").split("|")]
            if len(fields) != 3:
                raise ValueError("mutation table row shape changed")
            rows.append((fields[0], fields[1], fields[2]))
    if len(rows) != 62:
        raise ValueError("mutation class count changed")
    classes = []
    seen: set[str] = set()
    for index, (name, mutation, rejection) in enumerate(rows):
        identifier = slug(name)
        if identifier in seen:
            identifier = f"{identifier}_{index + 1:02d}"
        seen.add(identifier)
        if index < 40:
            default = profile("raw_packet", ["algorithm_C", "algorithm_F"])
        elif index < 47:
            default = profile(
                "route_card", ["strict_route_validator", "independent_route_auditor"])
        elif index < 53:
            default = profile("static_or_environment", ["read_only_integrity_auditor"])
        elif index < 59:
            default = profile("canonical_output", ["read_only_integrity_auditor"])
        else:
            default = profile(
                "paired_provenance_state",
                ["strict_route_validator", "independent_route_auditor",
                 "read_only_integrity_auditor"],
            )
        allowed = [default]
        classes.append({
            "class": name,
            "class_id": identifier,
            "allowed_instance_contracts": allowed,
            "default_instance_contract": default,
            "mutation": mutation,
            "required_rejection": rejection,
        })
    classes.sort(key=lambda row: row["class_id"])
    if len({row["class_id"] for row in classes}) != 62:
        raise ValueError("mutation class IDs are not unique")
    by_id = {row["class_id"]: row for row in classes}
    raw = profile("raw_packet", ["algorithm_C", "algorithm_F"])
    route = profile("route_card", ["strict_route_validator", "independent_route_auditor"])
    auditor_output = profile("canonical_output", ["read_only_integrity_auditor"])
    auditor_static = profile("static_or_environment", ["read_only_integrity_auditor"])
    authority_overlay = profile(
        "authority_overlay", ["read_only_integrity_auditor"])
    paired_auditor = profile("paired_provenance_state", ["read_only_integrity_auditor"])
    paired_all = profile(
        "paired_provenance_state",
        ["strict_route_validator", "independent_route_auditor",
         "read_only_integrity_auditor"],
    )
    route_output_all = profile(
        "route_card_in_output_tree",
        ["strict_route_validator", "independent_route_auditor",
         "read_only_integrity_auditor"],
    )
    mixed_profiles: dict[str, list[dict[str, object]]] = {
        "artifact_path": [raw, route, route_output_all],
        "check_flag": [raw, auditor_output],
        "factor_target": [raw, auditor_output],
        "finite_p0_period": [raw, auditor_output],
        "finite_p0_product": [raw, auditor_output],
        "fixed_anchor": [raw, auditor_output],
        "fixed_counts": [raw, auditor_output],
        "live_dependency": [raw, auditor_output],
        "marker": [raw, auditor_output],
        "missing_residue": [raw, auditor_output],
        "operator_owner": [raw, auditor_output],
        "path_leak": [raw, auditor_output],
        "periodic_separation": [raw, auditor_output],
        "prime_allocation": [raw, auditor_output],
        "provenance_state_a": [paired_auditor, paired_all, authority_overlay],
        "provenance_state_b": [paired_auditor, paired_all],
        "result_set": [auditor_output, authority_overlay],
        "source_id": [raw, auditor_static],
        "stage_2_scope": [paired_auditor, paired_all, authority_overlay],
    }
    positive_profiles: dict[str, list[dict[str, object]]] = {
        "cache": [profile("static_tree_hygiene", ["static_hygiene_probe"],
                          "exact_positive_control")],
        "cwd_relocation": [
            profile("runtime_environment", ["process_isolation_probe"],
                    "exact_positive_control"),
            profile("relocated_complete_output_tree", ["read_only_integrity_auditor"],
                    "exact_positive_control"),
        ],
        "live_dependency": [profile(
            "portable_source_snapshot", ["portable_snapshot_probe"],
            "exact_positive_control")],
        "module_shadow": [profile(
            "runtime_environment", ["process_isolation_probe"],
            "exact_positive_control")],
        "path_leak": [profile(
            "canonical_payload_hygiene", ["payload_hygiene_probe"],
            "exact_positive_control")],
        "provenance_state_a": [profile(
            "authority_overlay", ["read_only_integrity_auditor"],
            "exact_positive_control")],
        "stage_2_scope": [profile(
            "authority_overlay", ["read_only_integrity_auditor"],
            "exact_positive_control")],
    }
    for class_id, profiles in mixed_profiles.items():
        by_id[class_id]["allowed_instance_contracts"] = profiles
    for class_id, profiles in positive_profiles.items():
        current = by_id[class_id]["allowed_instance_contracts"]
        for item in profiles:
            if item not in current:
                current.append(item)
    for row in classes:
        row["allowed_instance_contracts"] = sorted(
            row["allowed_instance_contracts"],
            key=lambda item: (item["domain"], item["expectation"],
                              item["designated_consumers"]),
        )
    registry = {
        "authority_overlay_coverage": {
            "baseline_exact_writer_and_root_lock": True,
            "publication_artifacts_binary_text_classified": True,
            "publication_changed_paths_bounded": True,
            "unknown_extra_missing_and_unauthorized_reject": True,
            "writer_paths_excluded_from_integration_ledger": True,
        },
        "blueprint_section": "9_Adversarial_mutation_matrix",
        "blueprint_sha256": BLUEPRINT_SHA256,
        "class_count": 62,
        "classes": classes,
        "generated_id_policy": {
            "future_counts_and_hashes_frozen_here": False,
            "id_format": "class_id__zero_padded_instance_index__json_pointer_slug",
            "ids_c_sorted_and_unique_at_run_time": True,
        },
        "instance_contract_policy": {
            "contract_fields": [
                "class_id", "designated_consumers", "domain", "expectation",
                "id", "variant",
            ],
            "mutation_outcome": "REJECT_NONZERO_for_every_exact_designated_consumer",
            "observed_outcome_keys_equal_designated_consumers": True,
            "positive_controls_separate_from_rejection_records": True,
            "producer_emits_per_instance_contract": True,
            "read_only_auditor_rederives_each_contract": True,
        },
        "recursive_route_coverage": {
            "mapping_key_presence": "every_mapping_key_at_every_recursive_path",
            "mapping_unknown_key": "one_unknown_key_at_every_mapping_path",
            "scalar_type": "every_scalar_at_every_recursive_path",
            "scalar_value": "every_scalar_at_every_recursive_path",
            "sequence_member": "every_list_member_at_every_recursive_path",
            "sequence_order": "every_list_with_at_least_two_members",
        },
        "schema": "paper43-static-mutation-class-registry-v3",
    }
    encoded = (json.dumps(registry, sort_keys=True, indent=2, ensure_ascii=True,
                          separators=(",", ": ")) + "\n").encode("ascii")
    sys.stdout.buffer.write(encoded)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
