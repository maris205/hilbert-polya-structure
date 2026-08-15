import ast
import json
from pathlib import Path

import pytest
import sympy as sp

from base2_clock.algebra import candidate_field, serialize_element, serialize_polynomial
from base2_clock.dynatomic import target_certificate
from base2_clock.lifecycle import (
    claim_registered_run,
    validate_registered_claim,
    write_terminal_ledger,
)
from base2_clock.manifest import (
    _validate_field_element,
    _validate_polynomial,
    parse_passing_junit,
    validate_official_preflight,
    validate_period_records,
)
from base2_clock.protocol import (
    CANDIDATE_ID,
    EXPECTED_CODE_FILES,
    EXPECTED_LOCK_SHA256,
    _IsolationVisitor,
    executable_isolation_scan,
    load_strict_json,
    stable_file_bytes,
    write_json,
)


PROJECT_ROOT = Path(__file__).absolute().parents[2]


def _scan_fixture(source: str) -> set[str]:
    visitor = _IsolationVisitor("fixture.py")
    visitor.visit(ast.parse(source))
    return {item["kind"] for item in visitor.findings}


def _closed_world_scan(tmp_path: Path, fixture_name: str, replacement: str):
    fixture_root = tmp_path / fixture_name
    code_root = fixture_root / "code"
    code_root.mkdir(parents=True)
    for relative in sorted(EXPECTED_CODE_FILES):
        target = code_root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        content = (
            replacement.encode("utf-8")
            if relative == "tests/test_algebra.py"
            else stable_file_bytes(PROJECT_ROOT / "code" / relative)
        )
        target.write_bytes(content)
    (fixture_root / "pyproject.toml").write_bytes(
        stable_file_bytes(PROJECT_ROOT / "pyproject.toml")
    )
    return executable_isolation_scan(code_root)


def test_scanner_blocks_round1_alias_and_path_bypasses():
    fixtures = {
        'import os as x\nx.system("true")': "forbidden_os_capability",
        'from os import system as x\nx("true")': "forbidden_call",
        'import builtins\ngetattr(builtins, "__import__")("socket")': (
            "dynamic_callable_invocation"
        ),
        'from pathlib import Path\nPath("prime_" + "table").read_text()': (
            "forbidden_path_capability"
        ),
        'convert = float\nconvert("0.125")': "forbidden_call",
        'import os\nos.execv("/bin/true", ["true"])': "forbidden_os_capability",
        'open("artifact.txt")': "forbidden_call",
    }
    for source, required_kind in fixtures.items():
        assert required_kind in _scan_fixture(source)


def test_scanner_blocks_named_container_callable_laundering_in_closed_tree(tmp_path):
    assert _scan_fixture("assert type(value) is float") == set()
    replacements = [
        'import os\nfuncs = (os.system,)\nrun = funcs[0]\nrun("true")\n',
        'funcs = {"x": open}\nrun = funcs["x"]\nrun("artifact.txt")\n',
        (
            'from pathlib import Path\n'
            'funcs = (Path("prime_" + "table").read_text,)\n'
            'reader = funcs[0]\nreader()\n'
        ),
    ]
    for index, replacement in enumerate(replacements):
        record = _closed_world_scan(tmp_path, f"container-{index}", replacement)
        assert record["inventory"]["pass"] is True
        assert record["pass"] is False
        assert any(
            item["kind"] == "forbidden_callable_storage"
            for item in record["findings"]
        )


def test_scanner_blocks_ifexp_lambda_and_default_callable_flow_in_closed_tree(tmp_path):
    replacements = [
        (
            'import os\nrun = os.system if True else len\n'
            'run("true")\n'
        ),
        (
            'import os\nfactory = lambda: os.system\n'
            'run = factory()\nrun("true")\n'
        ),
        (
            'import os\ndef invoke(run=os.system):\n'
            '    run("true")\ninvoke()\n'
        ),
    ]
    for index, replacement in enumerate(replacements):
        record = _closed_world_scan(tmp_path, f"flow-{index}", replacement)
        assert record["inventory"]["pass"] is True
        assert record["pass"] is False
        assert any(
            item["kind"] == "forbidden_callable_storage"
            for item in record["findings"]
        )

    positive = _closed_world_scan(
        tmp_path,
        "type-positive",
        "def exact_type(value):\n    return type(value) is float\n",
    )
    assert positive["inventory"]["pass"] is True
    assert positive["pass"] is True
    assert positive["findings"] == []


def test_field_target_hit_and_miss_agree():
    field = candidate_field()
    z = sp.Symbol("z")
    u = field.generator
    exact = sp.Poly((z - 1) * (z + u), z, domain=field.domain)
    normalized = sp.Poly(z, z, domain=field.domain)
    assert _validate_polynomial(serialize_polynomial(exact, field), expected_degree=2) == []
    assert _validate_field_element(
        serialize_element(field.domain.convert(2 + u), field)
    )[0] == []

    hit = target_certificate(exact, normalized, sp.Rational(1), field=field)
    assert hit.gcd.degree() == 1
    assert hit.resultant == field.domain.zero
    assert hit.rational_field_norm == 0
    assert hit.hit is True
    assert hit.engines_agree is True

    miss = target_certificate(exact, normalized, sp.Rational(2), field=field)
    assert miss.gcd.degree() == 0
    assert miss.resultant != field.domain.zero
    assert miss.rational_field_norm == 22
    assert miss.hit is False
    assert miss.engines_agree is True


def _prepare_claim_fixture(project_root: Path, code_digest: str) -> None:
    results = project_root / "results"
    results.mkdir()
    (results / "CODE_REVIEW.md").write_text("independent fixture\n", encoding="utf-8")
    write_json(results / "PRE_EXECUTION_AUDIT.json", {"fixture": True})
    claim_registered_run(project_root, code_digest)


def test_lifecycle_claim_is_one_shot_and_target_halt_is_terminal(tmp_path):
    code_digest = "a" * 64
    _prepare_claim_fixture(tmp_path, code_digest)
    with pytest.raises(FileExistsError):
        claim_registered_run(tmp_path, code_digest)

    halt_path = tmp_path / "results" / "TARGET_HIT_HALT.json"
    write_json(halt_path, {"stopped_on_target_hit": True}, exclusive=True)
    terminal_path = write_terminal_ledger(
        tmp_path,
        reviewed_code_sha256=code_digest,
        state="HALTED_TARGET_HIT",
        periods_started=[2],
        periods_completed=[2],
        stopped_period=2,
        artifact_path="results/TARGET_HIT_HALT.json",
        failure_code="TARGET_HIT",
    )
    terminal = load_strict_json(terminal_path)
    assert terminal["state"] == "HALTED_TARGET_HIT"
    assert terminal["stopped_period"] == 2
    assert validate_registered_claim(tmp_path, code_digest)["pass"] is True
    assert validate_registered_claim(
        tmp_path, code_digest, require_clean_started=True
    )["pass"] is False


def test_interrupted_claim_is_terminal_and_never_reusable(tmp_path):
    code_digest = "b" * 64
    _prepare_claim_fixture(tmp_path, code_digest)
    terminal_path = write_terminal_ledger(
        tmp_path,
        reviewed_code_sha256=code_digest,
        state="FAILED_CLOSED",
        periods_started=[],
        periods_completed=[],
        stopped_period=None,
        artifact_path=None,
        failure_code="INTERRUPTED",
    )
    assert load_strict_json(terminal_path)["state"] == "FAILED_CLOSED"
    with pytest.raises(FileExistsError):
        claim_registered_run(tmp_path, code_digest)


def test_manifest_rejects_forged_nested_evidence(tmp_path):
    assert validate_period_records([{"targets": []} for _ in range(6)])

    live = {
        "schema": "BASE2_PRE_EXECUTION_AUDIT_V1",
        "candidate_id": CANDIDATE_ID,
        "source_lock_sha256": EXPECTED_LOCK_SHA256,
        "reviewed_code_sha256": "c" * 64,
        "gates": {},
        "independent_review": {"pass": True},
        "registered_candidate_runs": 0,
        "registered_candidate_periods_executed": [],
        "external_prime_tables_accessed": False,
        "riemann_zero_data_accessed": False,
        "floating_or_approximate_matching_used": False,
        "status": "AUTHORIZED_FOR_REGISTERED_EXECUTION",
        "pass": True,
    }
    errors = validate_official_preflight(dict(live), live)
    assert "PREFLIGHT_GATE_KEYS_NOT_EXACT" in errors

    junit = tmp_path / "forged.xml"
    junit.write_text(
        '<testsuite tests="1" errors="0" failures="99" skipped="0">'
        '<testcase name="forged"/></testsuite>',
        encoding="utf-8",
    )
    parsed = parse_passing_junit(junit)
    assert parsed["pass"] is False
    assert "JUNIT_NONPASSING_COUNTS" in parsed["errors"]

    forged_element = {
        "domain": "QQ<u>",
        "basis": "1,u,u^2",
        "coefficients_ascending": ["1", "0", "0"],
        "expression": "0",
    }
    assert "FIELD_ELEMENT_EXPRESSION_BASIS_MISMATCH" in _validate_field_element(
        forged_element
    )[0]
    forged_polynomial = {
        "variable": "garbage",
        "domain": "QQ<u>",
        "degree": 2,
        "coefficients_descending": ["not algebra", "0", "0"],
        "coefficient_basis": "1,u,u^2",
        "coefficients_basis_descending": [
            ["0", "0", "0"],
            ["0", "0", "0"],
            ["0", "0", "0"],
        ],
    }
    assert _validate_polynomial(forged_polynomial, expected_degree=2)
