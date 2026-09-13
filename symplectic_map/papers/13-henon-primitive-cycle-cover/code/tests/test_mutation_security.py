from copy import deepcopy
import builtins

import pytest

from candidate_v1.bootstrap.canonical import canonical_bytes
from candidate_v1.bootstrap.static_audit import _audit_engine, _audit_schema
from candidate_v1.track_q import runner as q_runner
from candidate_v1.track_r import runner as r_runner


BASE_ENGINE = '''"""mutation-audit fixture"""
from fractions import Fraction
def helper(value):
    return value
def run_science(definitions, fixture):
    return helper(Fraction(1, 1))
'''


def _engine_file(tmp_path, source, name="engine.py"):
    path = tmp_path / name
    path.write_text(source, encoding="utf-8")
    return path


def _schema_file(tmp_path, value, name="schema.json"):
    path = tmp_path / name
    path.write_bytes(canonical_bytes(value))
    return path


def test_engine_ast_alias_dunder_pattern_top_level_and_scan_mutations_fail(tmp_path):
    _audit_engine(_engine_file(tmp_path, BASE_ENGINE, "baseline.py"), "Q")
    mutations = {
        "top_level.py": BASE_ENGINE.replace("def helper(value):", "sentinel = 1\ndef helper(value):"),
        "alias_compile.py": BASE_ENGINE.replace("return helper(Fraction(1, 1))", "f = compile\n    return f"),
        "moved_import.py": '''"""x"""\n\ndef helper(value):\n    return value\ndef run_science(definitions, fixture):\n    from fractions import Fraction\n    return Fraction(1,1)\n''',
        "pattern_mro.py": BASE_ENGINE.replace(
            "return helper(Fraction(1, 1))",
            "match int:\n        case type(__mro__=captured):\n            return captured",
        ),
        "pattern_dict.py": BASE_ENGINE.replace(
            "return helper(Fraction(1, 1))",
            "match int:\n        case type(__dict__=captured):\n            return captured",
        ),
        "dunder_string.py": BASE_ENGINE.replace("return helper(Fraction(1, 1))", "return '__getattribute__'"),
        "scan.py": BASE_ENGINE.replace("return helper(Fraction(1, 1))", "for d in (2,):\n        return d"),
        "for_k.py": BASE_ENGINE.replace("return helper(Fraction(1, 1))", "for k in (2,):\n        return k"),
        "while.py": BASE_ENGINE.replace("return helper(Fraction(1, 1))", "while fixture:\n        return fixture"),
        "comprehension.py": BASE_ENGINE.replace("return helper(Fraction(1, 1))", "return [k for k in (1,)]"),
        "nested_default.py": BASE_ENGINE.replace(
            "return helper(Fraction(1, 1))",
            "def nested(value=Fraction(1,1)):\n        return value\n    return nested()",
        ),
        "true_division.py": BASE_ENGINE.replace("return helper(Fraction(1, 1))", "probe = 1 / 2\n    return Fraction(probe)"),
        "negative_power.py": BASE_ENGINE.replace("return helper(Fraction(1, 1))", "return 2 ** -1"),
        "positive_power.py": BASE_ENGINE.replace("return helper(Fraction(1, 1))", "return 2 ** 2"),
        "bytes_literal.py": BASE_ENGINE.replace("return helper(Fraction(1, 1))", "return b'x'"),
        "f_string.py": BASE_ENGINE.replace("return helper(Fraction(1, 1))", "return f'{fixture}'"),
        "str_wrapper.py": BASE_ENGINE.replace("return helper(Fraction(1, 1))", "return str(fixture)"),
        "folded_dunder.py": BASE_ENGINE.replace("return helper(Fraction(1, 1))", "return '_' + '_class__'"),
        "format_attribute.py": BASE_ENGINE.replace("return helper(Fraction(1, 1))", "return '{}'.format(1)"),
        "decode_attribute.py": BASE_ENGINE.replace("return helper(Fraction(1, 1))", "return b'x'.decode()"),
    }
    for name, source in mutations.items():
        with pytest.raises((RuntimeError, SyntaxError)):
            _audit_engine(_engine_file(tmp_path, source, name), "Q")


def test_schema_open_empty_items_type_ref_and_unknown_keyword_mutations_fail(tmp_path):
    metaschema = "https://json-schema.org/draft/2020-12/schema"
    baseline = {
        "$defs": {"leaf": {"type": "integer"}},
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "additionalProperties": False,
        "properties": {"x": {"$ref": "#/$defs/leaf"}},
        "required": ["x"],
        "type": "object",
    }
    _audit_schema(_schema_file(tmp_path, baseline, "baseline.json"))
    mutations = [
        ({**baseline, "additionalProperties": True}, "additionalProperties"),
        ({"$schema": metaschema, "items": {}, "type": "array"}, "items must"),
        ({"$schema": metaschema, "items": True, "type": "array"}, "items must"),
        ({"$schema": metaschema, "items": {"type": "integer"}, "type": []}, "invalid type"),
        ({"$schema": metaschema, "if": 7, "then": {"const": 1}}, "malformed if"),
        ({"$schema": metaschema, "const": 1, "required": ["x", "x"]}, "required is not unique"),
        ({"$schema": metaschema, "$defs": {"leaf": {"type": "integer"}}, "$ref": "#/$defs/leaf/ghost"}, "malformed $ref"),
        ({"$schema": metaschema, "$defs": {"leaf": {"$ref": "#/$defs/leaf"}}, "$ref": "#/$defs/leaf"}, "cyclic local $ref"),
        ({"$schema": metaschema, "then": {"const": 1}}, "orphan conditional"),
        ({"$schema": metaschema, "prefixItems": [{"type": "integer"}], "type": "array"}, "items:false"),
        ({"$schema": metaschema, "typoProperties": {}, "type": "object"}, "unknown schema keywords"),
        ({"$schema": metaschema, "properties": {"x": {"type": "integer"}}, "required": ["x"]}, "object keywords require"),
        ({"$schema": metaschema, "maximum": 0, "minimum": 1, "type": "integer"}, "minimum exceeds maximum"),
        ({"$schema": metaschema, "const": True, "type": "integer"}, "const/type mismatch"),
        ({"$schema": metaschema, "oneOf": [{"const": 1}, {"const": 1}]}, "duplicate oneOf"),
        ({"$schema": metaschema, "oneOf": [{"type": "integer"}, {"minimum": 0, "type": "integer"}]}, "not demonstrably disjoint"),
        ({"$schema": metaschema, "$defs": {"bad/key": {"type": "integer"}}, "$ref": "#/$defs/bad~1key"}, "malformed $defs key"),
    ]
    for index, (mutation, message) in enumerate(mutations):
        with pytest.raises(RuntimeError, match=message.replace("$", r"\$")):
            _audit_schema(_schema_file(tmp_path, mutation, "mutation-" + str(index) + ".json"))


def test_runner_minimal_builtins_fork_hook_and_rejection_category_mutations_fail(paper_root):
    forbidden = {"open", "compile", "exec", "eval", "globals", "getattr", "vars", "locals"}
    q_builtins = q_runner._build_science_builtins(lambda *args, **kwargs: None)
    r_builtins = r_runner._rj_build_science_builtins(lambda *args, **kwargs: None)
    assert forbidden.isdisjoint(q_builtins)
    assert forbidden.isdisjoint(r_builtins)
    assert set(q_builtins) == set(q_runner._SCIENCE_BUILTIN_NAMES) | {"__import__"}
    assert set(r_builtins) == set(r_runner._SCIENCE_BUILTIN_NAMES) | {"__import__"}
    with pytest.raises(RuntimeError, match="Q builtin identity drift"):
        with pytest.MonkeyPatch.context() as local_patch:
            local_patch.setattr(builtins, "len", builtins.open)
            q_runner._build_science_builtins(lambda *args, **kwargs: None)
    with pytest.raises(RuntimeError, match="R builtin identity drift"):
        with pytest.MonkeyPatch.context() as local_patch:
            local_patch.setattr(builtins, "len", builtins.open)
            r_runner._rj_build_science_builtins(lambda *args, **kwargs: None)
    q_source = (paper_root / "code/candidate_v1/track_q/runner.py").read_text(encoding="utf-8")
    r_source = (paper_root / "code/candidate_v1/track_r/runner.py").read_text(encoding="utf-8")
    assert '"os.fork"' in q_source and "lambda: os.fork()" in q_source
    assert '"os.fork"' in r_source and "lambda: os.fork()" in r_source

    n5 = [
        {"disposition": "REJECTED_SCOPE_ERROR", "statement": "left"},
        {"disposition": "REJECTED_SCOPE_ERROR", "statement": "right"},
    ]
    r_runner._rj_rejections(n5, "statement", "REJECTED_SCOPE_ERROR")
    changed = deepcopy(n5)
    changed[0]["disposition"] = "REJECTED_CATEGORY_SUBSTITUTION"
    with pytest.raises(ValueError):
        r_runner._rj_rejections(changed, "statement", "REJECTED_SCOPE_ERROR")
    n8 = [
        {"disposition": "REJECTED_CATEGORY_SUBSTITUTION", "kind": "left"},
        {"disposition": "REJECTED_CATEGORY_SUBSTITUTION", "kind": "right"},
    ]
    r_runner._rj_rejections(n8, "kind", "REJECTED_CATEGORY_SUBSTITUTION")
    changed = deepcopy(n8)
    changed[1]["disposition"] = "REJECTED_SCOPE_ERROR"
    with pytest.raises(ValueError):
        r_runner._rj_rejections(changed, "kind", "REJECTED_CATEGORY_SUBSTITUTION")
