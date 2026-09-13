from copy import deepcopy
from pathlib import Path
import shutil

import pytest

from candidate_v1.bootstrap.canonical import canonical_bytes, strict_canonical_load, strict_load_bytes
from candidate_v1.bootstrap.constants import (
    RUNTIME_RELATIVE,
    SOURCE_LOCK_SHA256,
    SOURCE_REVIEW_SHA256,
)
from candidate_v1.bootstrap.static_audit import collect_static_audit


def test_strict_canonical_json_rejects_ambiguous_values():
    for payload in (
        b'{"x":1,"x":2}\n',
        b'{"x":1.0}\n',
        b'{"x":NaN}\n',
        b'{"x":Infinity}\n',
    ):
        with pytest.raises(ValueError):
            strict_load_bytes(payload)
    for value in ({1: "integer key"}, {1: "a", "1": "b"}, {"x": 1.0}, {"x": object()}):
        with pytest.raises(TypeError):
            canonical_bytes(value)
    exact = {"a": [True, None, -2], "z": {"k": "v"}}
    assert strict_canonical_load(canonical_bytes(exact)) == exact
    with pytest.raises(ValueError):
        strict_canonical_load(b'{"z":1, "a":2}\n')


def test_static_audit_and_exact_private_fixture_schemas_close(paper_root, tmp_path):
    record = collect_static_audit(paper_root)
    assert record["exact_engine_count"] == 2
    assert record["third_engine_count"] == 0
    assert record["registered_entry_file_count"] == 1
    assert record["registered_transaction_function_count"] == 1
    assert record["schema_file_count"] == 11
    assert record["exact_reviewed_schema_hash_count"] == 11
    assert [item["path"] for item in record["recursive_schema_audits"]] == sorted({
        "code/candidate_v1/shared/capability.schema.json",
        "code/candidate_v1/shared/durable_claim.schema.json",
        "code/candidate_v1/shared/execution_stage.schema.json",
        "code/candidate_v1/shared/raw_result.schema.json",
        "code/candidate_v1/shared/result_manifest.schema.json",
        "code/candidate_v1/shared/terminal.schema.json",
        "code/candidate_v1/shared/track_envelope.schema.json",
        "code/candidate_v1/track_q/certificate.schema.json",
        "code/candidate_v1/track_q/private_fixture.schema.json",
        "code/candidate_v1/track_r/certificate.schema.json",
        "code/candidate_v1/track_r/private_fixture.schema.json",
    })
    assert record["definitions_contract_sha256"] == (
        "3c77fd28005786c03bf6dbbffc28cc5fcbc01aa1d8134a19b2ba593a622aef2c"
    )
    assert "$.observable_names.rho:string" in record["definitions_field_inventory"]
    assert record["shared_schema_scientific_field_count"] == 0
    assert record["shared_arithmetic_helper_count"] == 0
    assert record["shared_scientific_implementation_count"] == 0
    assert record["private_fixture_contracts"] == {
        "Q": {
            "schema_mode": "EXACT_CONST_SCHEMA_PLUS_ENGINE_VALIDATOR_AND_HASH_BINDING",
            "validator": "_q_validate_inputs",
        },
        "R": {
            "schema_mode": "EXACT_CONST_SCHEMA_PLUS_ENGINE_VALIDATOR_AND_HASH_BINDING",
            "validator": "_r_validate_inputs",
        },
    }
    assert all(item["recursive_open_node_count"] == 0 for item in record["recursive_schema_audits"])

    mutated_root = tmp_path / "neutral-definitions-mutation"
    shutil.copytree(paper_root, mutated_root)
    definitions_path = mutated_root / "code/candidate_v1/shared/definitions.json"
    definitions = strict_canonical_load(definitions_path.read_bytes())
    definitions["n4_cycle_product_coefficients"] = [1, 2, 3]
    definitions_path.write_bytes(canonical_bytes(definitions))
    with pytest.raises(RuntimeError, match="exact reviewed contract drift"):
        collect_static_audit(mutated_root)

    for index, relative in enumerate(
        (
            "code/candidate_v1/track_s/engine.py",
            "code/rogue_global.py",
            "code/scripts/run_registered_twice.py",
        )
    ):
        inventory_root = tmp_path / ("inventory-mutation-" + str(index))
        shutil.copytree(paper_root, inventory_root)
        rogue_path = inventory_root / relative
        rogue_path.parent.mkdir(parents=True, exist_ok=True)
        rogue_path.write_text("# unauthorized package entry\n", encoding="utf-8")
        with pytest.raises(RuntimeError, match="entire code package exact path inventory drift"):
            collect_static_audit(inventory_root)

    schema_root = tmp_path / "reviewed-schema-mutation"
    shutil.copytree(paper_root, schema_root)
    capability_path = schema_root / "code/candidate_v1/shared/capability.schema.json"
    capability = strict_load_bytes(capability_path.read_bytes())
    capability["properties"]["machine_proof_authority"] = {"type": "string"}
    capability["required"].append("machine_proof_authority")
    capability_path.write_bytes(canonical_bytes(capability))
    with pytest.raises(RuntimeError, match="exact reviewed schema contract drift"):
        collect_static_audit(schema_root)

    for index, relative in enumerate(
        (
            "code/scripts/run_registered_once.py",
            "code/candidate_v1/orchestrator/registered.py",
            "code/candidate_v1/adjudicator/adjudicate.py",
        )
    ):
        fingerprint_root = tmp_path / ("critical-fingerprint-mutation-" + str(index))
        shutil.copytree(paper_root, fingerprint_root)
        critical_path = fingerprint_root / relative
        critical_path.write_text(
            critical_path.read_text(encoding="utf-8")
            + "\n\ndef unauthorized_alternate_entry():\n    return None\n",
            encoding="utf-8",
        )
        with pytest.raises(RuntimeError, match="exact critical Python fingerprint drift"):
            collect_static_audit(fingerprint_root)


def test_source_bindings_and_absent_runtime_are_exact(paper_root):
    record = collect_static_audit(paper_root)
    assert record["source_lock_sha256"] == SOURCE_LOCK_SHA256
    assert record["source_review_sha256"] == SOURCE_REVIEW_SHA256
    runtime = paper_root / RUNTIME_RELATIVE
    assert not runtime.exists()
    assert not runtime.is_symlink()
