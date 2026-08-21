"""Exact structural validator for a Stage-0 science envelope."""

from __future__ import annotations

from typing import Any


def exact_type(value: Any, declared: str) -> bool:
    base = {
        "boolean": type(value) is bool,
        "dict": type(value) is dict,
        "integer": type(value) is int,
        "null": value is None,
        "record": type(value) is dict,
        "string": type(value) is str,
        "log_term": (type(value) is dict and set(value) == {"denominator", "numerator", "prime"}
                     and all(type(value[key]) is int for key in value)
                     and value["denominator"] > 0 and value["numerator"] != 0 and value["prime"] >= 2),
        "exponent_term": (type(value) is dict and set(value) == {"exponent", "prime"}
                          and all(type(value[key]) is int for key in value)
                          and value["exponent"] > 0 and value["prime"] >= 2),
    }
    if declared in base:
        return base[declared]
    if declared.startswith("list[") and declared.endswith("]"):
        inner = declared[5:-1]
        return type(value) is list and all(exact_type(item, inner) for item in value)
    return False


def valid_declaration(declared: str) -> bool:
    if declared in {"boolean", "dict", "exponent_term", "integer", "log_term", "null", "record", "string"}:
        return True
    return declared.startswith("list[") and declared.endswith("]") and valid_declaration(declared[5:-1])


def runtime_nodes(value: Any, allowed_scalars: set[str]) -> int:
    if value is None:
        if "null" not in allowed_scalars:
            raise AssertionError("null scalar")
        return 1
    if type(value) is bool:
        if "boolean" not in allowed_scalars:
            raise AssertionError("boolean scalar")
        return 1
    if type(value) is int:
        if "integer" not in allowed_scalars:
            raise AssertionError("integer scalar")
        return 1
    if type(value) is str:
        if "string" not in allowed_scalars:
            raise AssertionError("string scalar")
        return 1
    if type(value) is list:
        return 1 + sum(runtime_nodes(item, allowed_scalars) for item in value)
    if type(value) is dict and all(type(key) is str for key in value):
        return 1 + sum(runtime_nodes(item, allowed_scalars) for item in value.values())
    raise AssertionError("forbidden runtime type")


def exact_record(record: Any, type_map: dict[str, str], known: set[int]) -> None:
    if type(record) is not dict or set(record) != set(type_map):
        raise AssertionError("record keys")
    known.add(id(record))
    for key, declared in type_map.items():
        if not exact_type(record[key], declared):
            raise AssertionError("record value type")


def mark_terms(value: Any, schema: dict[str, Any], known: set[int]) -> None:
    if type(value) is dict:
        keys = set(value)
        log_keys = set(schema.get("exact_log_form_term_keys", []))
        exponent_keys = set(schema.get("exact_integer_exponent_term_keys", []))
        if {"numerator", "denominator"} & keys:
            if keys != log_keys or any(type(value[key]) is not int for key in log_keys):
                raise AssertionError("exact log term")
            if value["denominator"] <= 0 or value["numerator"] == 0 or value["prime"] < 2:
                raise AssertionError("exact log term domain")
            known.add(id(value))
        elif "prime" in keys and "exponent" in keys:
            if keys != exponent_keys or any(type(value[key]) is not int for key in exponent_keys):
                raise AssertionError("exact exponent term")
            if value["exponent"] <= 0 or value["prime"] < 2:
                raise AssertionError("exact exponent term domain")
            known.add(id(value))
        for item in value.values():
            mark_terms(item, schema, known)
    elif type(value) is list:
        for item in value:
            mark_terms(item, schema, known)


def reject_untyped_dicts(value: Any, known: set[int]) -> None:
    if type(value) is dict:
        if id(value) not in known:
            raise AssertionError("undeclared nested record")
        for item in value.values():
            reject_untyped_dicts(item, known)
    elif type(value) is list:
        for item in value:
            reject_untyped_dicts(item, known)


def validate_science(schema: dict[str, Any], contract: dict[str, Any], cases_spec: dict[str, Any], envelope: dict[str, Any]) -> int:
    """Raise on any missing, unknown, mistyped, cross-paper, or untyped field."""
    if schema.get("allowed_scalar_types") != ["boolean", "integer", "null", "string"]:
        raise AssertionError("allowed scalar contract")
    if schema.get("canonical_envelope_keys") != ["payload", "schema", "status"]:
        raise AssertionError("envelope contract")
    if schema.get("canonical_payload_keys") != ["cases", "evidence_class", "project_slug", "state"]:
        raise AssertionError("payload contract")
    if schema.get("case_keys") != ["case_id", "kind", "result"]:
        raise AssertionError("case contract")
    if schema.get("forbidden_numeric_types") != ["binary_float", "boolean_as_integer"] or schema.get("unknown_or_missing_key_rule") != "reject":
        raise AssertionError("strict contract")
    if schema.get("canonical_json") != {"ascii_only": True, "indent": 2, "sort_keys": True, "terminal_newline": True}:
        raise AssertionError("canonical JSON contract")

    known: set[int] = set()
    if type(envelope) is not dict or set(envelope) != set(schema["canonical_envelope_keys"]):
        raise AssertionError("envelope keys")
    known.add(id(envelope))
    if envelope["status"] != "PASS" or envelope["schema"] != schema["science_schema"]:
        raise AssertionError("envelope identity")
    payload = envelope["payload"]
    if type(payload) is not dict or set(payload) != set(schema["canonical_payload_keys"]):
        raise AssertionError("payload keys")
    known.add(id(payload))
    if (payload["project_slug"] != contract["project_slug"] or payload["state"] != "A"
            or payload["evidence_class"] != contract["evidence_class"]
            or type(payload["cases"]) is not list):
        raise AssertionError("payload identity")
    if len(payload["cases"]) != len(cases_spec["cases"]):
        raise AssertionError("case count")

    kinds = {case["kind"] for case in cases_spec["cases"]}
    result_keys = schema["result_keys_by_kind"]
    result_types = schema["result_value_types_by_kind"]
    nested_keys = schema["nested_record_keys_by_kind"]
    nested_types = schema["nested_record_value_types_by_kind"]
    deep_keys = schema.get("deep_record_keys_by_kind", {})
    deep_types = schema.get("deep_record_value_types_by_kind", {})
    if set(result_keys) != kinds or set(result_types) != kinds or set(nested_keys) != kinds or set(nested_types) != kinds:
        raise AssertionError("kind schema coverage")
    if not set(deep_keys) <= kinds or set(deep_keys) != set(deep_types):
        raise AssertionError("deep schema coverage")
    declarations = []
    for collection in (result_types, nested_types, deep_types):
        stack = [collection]
        while stack:
            item = stack.pop()
            for value in item.values():
                if type(value) is dict:
                    stack.append(value)
                else:
                    declarations.append(value)
    if not declarations or any(type(item) is not str or not valid_declaration(item) or item == "list" for item in declarations):
        raise AssertionError("element type declarations")

    for observed, expected in zip(payload["cases"], cases_spec["cases"]):
        if type(observed) is not dict or set(observed) != set(schema["case_keys"]):
            raise AssertionError("case keys")
        known.add(id(observed))
        kind = expected["kind"]
        if observed["case_id"] != expected["case_id"] or observed["kind"] != kind:
            raise AssertionError("case identity")
        if set(result_types[kind]) != set(result_keys[kind]) or set(result_keys[kind]) != set(observed["result"]):
            raise AssertionError("result keys")
        exact_record(observed["result"], result_types[kind], known)

        if set(nested_keys[kind]) != set(nested_types[kind]):
            raise AssertionError("nested schema")
        nested_records: dict[str, list[dict[str, Any]]] = {}
        for field, keys in nested_keys[kind].items():
            type_map = nested_types[kind][field]
            if keys != list(type_map) or type(observed["result"][field]) is not list:
                raise AssertionError("nested field")
            nested_records[field] = observed["result"][field]
            for record in nested_records[field]:
                exact_record(record, type_map, known)

        for path, keys in deep_keys.get(kind, {}).items():
            outer, inner = path.split(".")
            type_map = deep_types[kind][path]
            if keys != list(type_map) or outer not in nested_records:
                raise AssertionError("deep schema")
            for outer_record in nested_records[outer]:
                if type(outer_record[inner]) is not list:
                    raise AssertionError("deep list")
                for record in outer_record[inner]:
                    exact_record(record, type_map, known)

    runtime_count = runtime_nodes(envelope, set(schema["allowed_scalar_types"]))
    mark_terms(envelope, schema, known)
    reject_untyped_dicts(envelope, known)
    return runtime_count
