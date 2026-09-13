"""Noncomputing, capability-gated comparison of two sealed envelopes."""

import hashlib
import json
import os
from pathlib import Path


def _a_unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("adjudicator duplicate JSON key")
        result[key] = value
    return result


def _a_reject_constant(value):
    raise ValueError("adjudicator non-finite JSON value: " + value)


def _a_reject_float(value):
    raise ValueError("adjudicator floating JSON value: " + value)


def _a_load(data):
    return json.loads(
        data.decode("utf-8"),
        object_pairs_hook=_a_unique_object,
        parse_constant=_a_reject_constant,
        parse_float=_a_reject_float,
    )


def _a_exact_json(value):
    if value is None or type(value) in (bool, int, str):
        return value
    if type(value) is list:
        return [_a_exact_json(item) for item in value]
    if type(value) is tuple:
        return [_a_exact_json(item) for item in value]
    if type(value) is dict:
        result = {}
        for key, item in value.items():
            if type(key) is not str or key in result:
                raise TypeError("adjudicator canonical key")
            result[key] = _a_exact_json(item)
        return result
    raise TypeError("adjudicator non-exact evidence type: " + type(value).__name__)


def _a_canonical(value):
    return json.dumps(
        _a_exact_json(value), sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("utf-8")


def _a_read(path):
    before = path.lstat()
    if not path.is_file() or path.is_symlink():
        raise RuntimeError("adjudicator unsafe read")
    descriptor = os.open(os.fspath(path), os.O_RDONLY | os.O_NOFOLLOW)
    try:
        chunks = []
        while True:
            chunk = os.read(descriptor, 65536)
            if not chunk:
                break
            chunks.append(chunk)
        opened = os.fstat(descriptor)
    finally:
        os.close(descriptor)
    after = path.lstat()
    identity = lambda item: (
        item.st_dev, item.st_ino, item.st_mode, item.st_size, item.st_mtime_ns, item.st_ctime_ns
    )
    if identity(before) != identity(opened) or identity(opened) != identity(after):
        raise RuntimeError("adjudicator unstable read")
    data = b"".join(chunks)
    if len(data) != before.st_size:
        raise RuntimeError("adjudicator short read")
    return data


def _a_write(path, data):
    descriptor = os.open(
        os.fspath(path), os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600
    )
    try:
        offset = 0
        while offset < len(data):
            written = os.write(descriptor, data[offset:])
            if written < 1:
                raise OSError("adjudicator short write")
            offset += written
        os.fsync(descriptor)
    finally:
        os.close(descriptor)
    directory = os.open(os.fspath(path.parent), os.O_RDONLY | os.O_DIRECTORY)
    try:
        os.fsync(directory)
    finally:
        os.close(directory)


def _a_same(left, right):
    if type(left) is not type(right):
        return False
    if type(left) is dict:
        return set(left) == set(right) and all(_a_same(left[key], right[key]) for key in left)
    if type(left) is list:
        return len(left) == len(right) and all(
            _a_same(left[index], right[index]) for index in range(len(left))
        )
    return left == right


def _a_validate_schema_node(node):
    if type(node) is not dict or not node:
        raise ValueError("types-only recursive schema node")
    if set(node) == {"enum"}:
        values = node["enum"]
        if (type(values) is not list or not values
                or any(type(value) is not str for value in values)
                or len(set(values)) != len(values)):
            raise ValueError("types-only enum node")
        return
    node_type = node.get("type")
    if node_type == "object":
        if set(node) != {"additionalProperties", "properties", "required", "type"}:
            raise ValueError("types-only object schema keys")
        properties = node["properties"]
        required = node["required"]
        if (node["additionalProperties"] is not False
                or type(properties) is not dict or not properties
                or type(required) is not list
                or len(required) != len(set(required))
                or set(required) != set(properties)):
            raise ValueError("types-only object schema closure")
        for child in properties.values():
            _a_validate_schema_node(child)
        return
    if node_type == "array":
        if not {"items", "type"}.issubset(node) or set(node).difference(
            {"items", "maxItems", "minItems", "type"}
        ):
            raise ValueError("types-only array schema keys")
        if ("minItems" in node) != ("maxItems" in node):
            raise ValueError("types-only array bound pair")
        if "minItems" in node and (
            type(node["minItems"]) is not int
            or type(node["maxItems"]) is not int
            or node["minItems"] < 1
            or node["maxItems"] != node["minItems"]
        ):
            raise ValueError("types-only array exact bounds")
        _a_validate_schema_node(node["items"])
        return
    if node_type == "string":
        if set(node).difference({"pattern", "type"}) or "type" not in node:
            raise ValueError("types-only string schema keys")
        if "pattern" in node and type(node["pattern"]) is not str:
            raise ValueError("types-only string pattern")
        return
    if node_type == "integer":
        if set(node) != {"type"}:
            raise ValueError("types-only integer schema keys")
        return
    raise ValueError("types-only unsupported schema node")


def _a_validate_types_only_schema(schema):
    required = {"additionalProperties", "properties", "required", "schema", "type"}
    if type(schema) is not dict or set(schema) != required:
        raise ValueError("types-only schema keys")
    if schema["schema"] != "HENON_PERIOD3_TYPES_ONLY_ENVELOPE_SCHEMA_V1":
        raise ValueError("types-only schema identity")
    if schema["additionalProperties"] is not False or schema["type"] != "object":
        raise ValueError("types-only schema closure")
    recursive_root = dict(schema)
    del recursive_root["schema"]
    _a_validate_schema_node(recursive_root)
    envelope_keys = {
        "candidate_id",
        "coefficient_diagnostics",
        "definitions_sha256",
        "private_witness_sha256",
        "quartic",
        "schema",
        "track",
    }
    properties = schema["properties"]
    if type(properties) is not dict or set(properties) != envelope_keys:
        raise ValueError("types-only schema envelope properties")
    if type(schema["required"]) is not list or set(schema["required"]) != envelope_keys:
        raise ValueError("types-only schema envelope required")
    quartic_keys = {
        "cyclewise_moment",
        "exact_period_three_length",
        "fiber_normal_form",
        "fixed_length",
        "fixed_moment",
        "normalized_conjugacy_coordinate",
        "period_one_characteristic_polynomial",
        "period_two_characteristic_polynomial",
        "pointwise_moment",
        "quotient_rank",
    }
    quartic = properties["quartic"]
    if (type(quartic) is not dict
            or set(quartic) != {"additionalProperties", "properties", "required", "type"}
            or quartic["additionalProperties"] is not False
            or quartic["type"] != "object"
            or type(quartic["properties"]) is not dict
            or set(quartic["properties"]) != quartic_keys
            or type(quartic["required"]) is not list
            or set(quartic["required"]) != quartic_keys):
        raise ValueError("types-only schema quartic closure")
    for moment_name in ("cyclewise_moment", "pointwise_moment"):
        moment = quartic["properties"][moment_name]
        if (type(moment) is not dict
                or set(moment) != {"additionalProperties", "properties", "required", "type"}
                or moment["additionalProperties"] is not False
                or moment["type"] != "object"
                or set(moment["properties"]) != {"terms", "variable"}
                or set(moment["required"]) != {"terms", "variable"}):
            raise ValueError("types-only schema moment closure")
        terms = moment["properties"]["terms"]
        if (type(terms) is not dict or terms.get("type") != "array"
                or type(terms.get("minItems")) is not int or terms["minItems"] != 2
                or type(terms.get("maxItems")) is not int or terms["maxItems"] != 2):
            raise ValueError("types-only schema moment terms")
    forbidden = {
        "expected",
        "acceptance",
        "recurrence",
        "admissible",
        "generalized_binomial",
        "H_value",
        "A_value",
        "E_value",
    }
    serialized = _a_canonical(schema).decode("ascii")
    if any(token in serialized for token in forbidden):
        raise ValueError("types-only schema contains scientific or acceptance content")


def _a_validate_moment(moment):
    if type(moment) is not dict or set(moment) != {"terms", "variable"}:
        raise ValueError("quartic moment keys")
    if type(moment["variable"]) is not str or not moment["variable"]:
        raise ValueError("quartic moment variable")
    terms = moment["terms"]
    if type(terms) is not list or len(terms) != 2:
        raise ValueError("quartic moment term count")
    exponents = []
    for term in terms:
        if type(term) is not dict or set(term) != {"coefficient", "exponent"}:
            raise ValueError("quartic moment term keys")
        if type(term["coefficient"]) is not int or type(term["exponent"]) is not int:
            raise ValueError("quartic moment term exact types")
        exponents.append(term["exponent"])
    if exponents != sorted(exponents) or len(set(exponents)) != len(exponents):
        raise ValueError("quartic moment canonical term order")


def _a_validate_quartic(quartic):
    quartic_keys = {
        "cyclewise_moment",
        "exact_period_three_length",
        "fiber_normal_form",
        "fixed_length",
        "fixed_moment",
        "normalized_conjugacy_coordinate",
        "period_one_characteristic_polynomial",
        "period_two_characteristic_polynomial",
        "pointwise_moment",
        "quotient_rank",
    }
    if type(quartic) is not dict or set(quartic) != quartic_keys:
        raise ValueError("quartic envelope keys")
    _a_validate_moment(quartic["cyclewise_moment"])
    _a_validate_moment(quartic["pointwise_moment"])
    for key in ("exact_period_three_length", "fixed_length", "fixed_moment", "quotient_rank"):
        if type(quartic[key]) is not int:
            raise ValueError("quartic envelope integer type")
    for key in (
        "fiber_normal_form",
        "normalized_conjugacy_coordinate",
        "period_one_characteristic_polynomial",
        "period_two_characteristic_polynomial",
    ):
        if type(quartic[key]) is not str or not quartic[key]:
            raise ValueError("quartic envelope string type")


def _a_validate_envelope(envelope, track):
    required = {
        "candidate_id",
        "coefficient_diagnostics",
        "definitions_sha256",
        "private_witness_sha256",
        "quartic",
        "schema",
        "track",
    }
    if type(envelope) is not dict or set(envelope) != required:
        raise ValueError("envelope keys")
    if envelope["schema"] != "HENON_PERIOD3_TRACK_OUTPUT_V1":
        raise ValueError("envelope schema")
    if envelope["candidate_id"] != "henon_period3_residue_v1" or envelope["track"] != track:
        raise ValueError("envelope identity")
    for key in ("definitions_sha256", "private_witness_sha256"):
        value = envelope[key]
        if type(value) is not str or len(value) != 64 or any(ch not in "0123456789abcdef" for ch in value):
            raise ValueError("envelope digest")
    diagnostics = envelope["coefficient_diagnostics"]
    if type(diagnostics) is not list or len(diagnostics) != 2:
        raise ValueError("coefficient diagnostic count")
    if [record.get("index") for record in diagnostics] != [8, 9]:
        raise ValueError("coefficient diagnostic order")
    for record in diagnostics:
        if type(record) is not dict or set(record) != {"final_integer", "index"}:
            raise ValueError("coefficient diagnostic keys")
        if type(record["index"]) is not int or type(record["final_integer"]) is not int:
            raise ValueError("coefficient diagnostic exact types")
    _a_validate_quartic(envelope["quartic"])


def _a_validate_ledger(ledger):
    root_keys = {
        "candidate_id",
        "coefficient_boundary",
        "counter_expectations",
        "negative_reason_codes",
        "quartic_expected",
        "schema",
    }
    if type(ledger) is not dict or set(ledger) != root_keys:
        raise ValueError("private ledger root keys")
    if ledger["schema"] != "HENON_PERIOD3_PRIVATE_ACCEPTANCE_LEDGER_V1":
        raise ValueError("private ledger schema")
    if ledger["candidate_id"] != "henon_period3_residue_v1":
        raise ValueError("private ledger candidate")
    boundary = ledger["coefficient_boundary"]
    if (type(boundary) is not dict
            or set(boundary) != {"comparison", "expected_value_storage_count", "indices"}
            or boundary["comparison"] != "track_q_final_integer_equals_track_r_final_integer"
            or type(boundary["expected_value_storage_count"]) is not int
            or boundary["expected_value_storage_count"] != 0
            or boundary["indices"] != [8, 9]
            or any(type(value) is not int for value in boundary["indices"])):
        raise ValueError("private ledger coefficient boundary")
    counters = ledger["counter_expectations"]
    if type(counters) is not dict or not counters:
        raise ValueError("private ledger counter expectations")
    for key, value in counters.items():
        if type(key) is not str:
            raise ValueError("private ledger counter key")
        if key == "registered_coefficient_check_order":
            if value != [8, 9] or any(type(item) is not int for item in value):
                raise ValueError("private ledger counter order")
        elif type(value) is not int or value < 0:
            raise ValueError("private ledger counter exact type")
    reasons = ledger["negative_reason_codes"]
    if type(reasons) is not dict or set(reasons) != {"K00" + str(index) for index in range(1, 9)}:
        raise ValueError("private ledger reason keys")
    if any(type(value) is not str or not value for value in reasons.values()):
        raise ValueError("private ledger reason types")
    _a_validate_quartic(ledger["quartic_expected"])


def _a_capability():
    try:
        token = os.read(3, 600)
    except OSError as exc:
        raise RuntimeError("adjudicator launch capability missing") from exc
    finally:
        try:
            os.close(3)
        except OSError:
            pass
    try:
        text = token.decode("ascii")
    except UnicodeDecodeError as exc:
        raise RuntimeError("adjudicator capability is not ASCII") from exc
    parts = text.rstrip("\n").split(":")
    if (not text.endswith("\n") or len(parts) != 7
            or parts[0] != "HENON_PERIOD3_ADJUDICATE_V1"
            or any(
                type(value) is not str
                or len(value) != 64
                or any(character not in "0123456789abcdef" for character in value)
                for value in parts[1:]
            )):
        raise RuntimeError("adjudicator launch capability invalid")
    return {
        "claim_sha256": parts[1],
        "adjudicator_sha256": parts[2],
        "schema_sha256": parts[3],
        "ledger_sha256": parts[4],
        "q_sha256": parts[5],
        "r_sha256": parts[6],
    }


def main():
    if len(os.sys.argv) != 1:
        raise RuntimeError("adjudicator accepts no arguments")
    capability = _a_capability()
    adjudicator_path = Path(__file__).absolute()
    project_root = adjudicator_path.parents[3]
    stage_root = project_root / "runtime/candidate_v1/staging"
    read_log = []
    claim_path = project_root / "runtime/candidate_v1/official/durable_claim.json"
    claim_data = _a_read(claim_path)
    read_log.append("runtime/candidate_v1/official/durable_claim.json")
    claim = _a_load(claim_data)
    if claim_data != _a_canonical(claim):
        raise ValueError("adjudicator durable claim is not canonical")
    if (hashlib.sha256(claim_data).hexdigest() != capability["claim_sha256"]
            or type(claim) is not dict
            or claim.get("candidate_id") != "henon_period3_residue_v1"
            or claim.get("run_id") != "R100"
            or claim.get("state") != "STARTED"):
        raise ValueError("adjudicator durable claim binding")
    adjudicator_data = _a_read(adjudicator_path)
    read_log.append("code/candidate_v1/adjudicator/adjudicate.py")
    if hashlib.sha256(adjudicator_data).hexdigest() != capability["adjudicator_sha256"]:
        raise ValueError("adjudicator executable digest")
    preledger_paths = {
        "schema": project_root / "code/candidate_v1/shared/result_envelope.schema.json",
        "q": stage_root / "track_q/sealed_envelope.json",
        "r": stage_root / "track_r/sealed_envelope.json",
    }
    loaded = {}
    digests = {}
    for key, path in preledger_paths.items():
        data = _a_read(path)
        read_log.append({
            "schema": "code/candidate_v1/shared/result_envelope.schema.json",
            "q": "runtime/candidate_v1/staging/track_q/sealed_envelope.json",
            "r": "runtime/candidate_v1/staging/track_r/sealed_envelope.json",
        }[key])
        loaded[key] = _a_load(data)
        if key in ("q", "r") and data != _a_canonical(loaded[key]):
            raise ValueError("adjudicator input envelope is not canonical")
        digests[key] = hashlib.sha256(data).hexdigest()
    if (digests["schema"] != capability["schema_sha256"]
            or digests["q"] != capability["q_sha256"]
            or digests["r"] != capability["r_sha256"]):
        raise ValueError("adjudicator preledger digest binding")
    _a_validate_types_only_schema(loaded["schema"])
    _a_validate_envelope(loaded["q"], "Q")
    _a_validate_envelope(loaded["r"], "R")
    ledger_path = project_root / "code/candidate_v1/adjudicator/acceptance_ledger.json"
    ledger_data = _a_read(ledger_path)
    read_log.append("code/candidate_v1/adjudicator/acceptance_ledger.json")
    ledger = _a_load(ledger_data)
    loaded["ledger"] = ledger
    digests["ledger"] = hashlib.sha256(ledger_data).hexdigest()
    if digests["ledger"] != capability["ledger_sha256"]:
        raise ValueError("adjudicator ledger digest binding")
    _a_validate_ledger(ledger)
    if loaded["q"]["definitions_sha256"] != loaded["r"]["definitions_sha256"]:
        raise ArithmeticError("definition digest disagreement")
    if not _a_same(loaded["q"]["quartic"], ledger["quartic_expected"]):
        raise ArithmeticError("Q quartic record does not match private ledger")
    if not _a_same(loaded["r"]["quartic"], ledger["quartic_expected"]):
        raise ArithmeticError("R quartic record does not match private ledger")
    q_values = loaded["q"]["coefficient_diagnostics"]
    r_values = loaded["r"]["coefficient_diagnostics"]
    if not _a_same(q_values, r_values):
        raise ArithmeticError("isolated coefficient boundary disagreement")
    output = {
        "schema": "HENON_PERIOD3_NONCOMPUTING_ADJUDICATION_V1",
        "candidate_id": "henon_period3_residue_v1",
        "acceptance_status": "EXACT_IMPLEMENTATION_AGREEMENT",
        "definitions_sha256": loaded["q"]["definitions_sha256"],
        "input_sha256": {
            "track_q_envelope": digests["q"],
            "track_r_envelope": digests["r"],
            "types_only_schema": digests["schema"],
            "private_acceptance_ledger": digests["ledger"],
        },
        "quartic": loaded["q"]["quartic"],
        "coefficient_diagnostics": q_values,
        "comparison_only": True,
        "source_theorem_verdict_emitted": False,
    }
    _a_write(stage_root / "final/adjudicated_science.json", _a_canonical(output))
    access_log = {
        "schema": "HENON_PERIOD3_ADJUDICATOR_LOGICAL_ACCESS_LOG_V1",
        "reads": [
            *read_log,
        ],
        "writes": [
            "runtime/candidate_v1/staging/final/adjudicated_science.json",
            "runtime/candidate_v1/staging/final/access_log.json",
        ],
    }
    _a_write(stage_root / "final/access_log.json", _a_canonical(access_log))


if __name__ == "__main__":
    main()
