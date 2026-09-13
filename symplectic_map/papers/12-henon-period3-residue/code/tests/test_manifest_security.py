"""Adversarial AST/capability and JUnit-evidence tests."""

from __future__ import annotations

import textwrap

import pytest

from bootstrap.manifest import (
    _capability_category_counts,
    _science_capability_findings,
    analyze_python,
    parse_junit,
    static_code_audit,
)
from conftest import PROJECT_ROOT


@pytest.mark.parametrize(
    "source",
    [
        "import os as harmless\nharmless.spawnl(0, 'x')\n",
        "reader = open\nreader('x')\n",
        "box = [open]\nbox[0]('x')\n",
        "__builtins__['open']('x')\n",
        "__loader__.get_data('x')\n",
        "import sys\nsys.modules['x']\n",
        "__import__('os')\n",
        "eval('1')\n",
        "compile('1', 'x', 'exec')\n",
        "getattr({}, 'items')()\n",
        "from pathlib import Path\nPath('x').read_text()\nPath('x').glob('*')\n",
        "import os\nos.open('x', 0)\nos.read(3, 1)\nos.fsync(3)\n",
        "import os\nreader = os.open\nreader('x', 0)\n",
        "import os\nbox = {'reader': os.open}\nbox['reader']('x', 0)\n",
        "len = print\nlen('leak')\n",
        "for _q_choose in [print]:\n    _q_choose('leak')\n",
        "f = lambda: 1\nf()\n",
    ],
)
def test_science_capability_alias_container_and_dunder_attacks_rejected(tmp_path, source):
    root = tmp_path / "code"
    path = root / "candidate_v1/track_q/engine.py"
    path.parent.mkdir(parents=True)
    path.write_text(source)
    findings = _science_capability_findings(root, "candidate_v1/track_q/engine.py")
    assert findings


def test_float_and_network_findings_have_positive_categories(tmp_path):
    root = tmp_path / "code"
    q_path = root / "candidate_v1/track_q/engine.py"
    r_path = root / "candidate_v1/track_r/engine.py"
    q_path.parent.mkdir(parents=True)
    r_path.parent.mkdir(parents=True)
    q_path.write_text("import socket\nvalue = 1.5\nsocket.connect()\n")
    r_path.write_text("\n")
    findings = _science_capability_findings(root, "candidate_v1/track_q/engine.py")
    counters = _capability_category_counts(root, findings)
    assert counters["network"] > 0
    assert counters["floating"] > 0


def test_live_static_audit_is_clean_and_body_digested():
    record = static_code_audit(PROJECT_ROOT / "code")
    assert record["status"] == "CLEAN"
    assert record["science_capability_findings"] == []
    assert record["science_capability_category_counts"] == {
        "dynamic_loader": 0,
        "filesystem": 0,
        "floating": 0,
        "network": 0,
        "process": 0,
    }
    q = analyze_python(
        PROJECT_ROOT / "code/candidate_v1/track_q/engine.py",
        "candidate_v1/track_q/engine.py",
    )
    assert q["imports"] == []
    assert "quartic_quotient_witness" in q["function_body_sha256"]
    assert all(len(digest) == 64 for digest in q["function_body_sha256"].values())


def test_junit_parser_rejects_declaration_content_mismatch(tmp_path):
    path = tmp_path / "junit.xml"
    path.write_text(
        textwrap.dedent(
            """\
            <testsuite tests="1" failures="0" errors="0" skipped="0">
              <testcase classname="x" name="bad"><failure>boom</failure></testcase>
            </testsuite>
            """
        )
    )
    record = parse_junit(path)
    assert record["status"] == "REJECTED"
    assert "JUNIT_DECLARATION_MISMATCH_FAILURES" in record["errors_detail"]


def test_junit_parser_accepts_exact_clean_content(tmp_path):
    path = tmp_path / "junit.xml"
    path.write_text(
        '<testsuite tests="1" failures="0" errors="0" skipped="0">'
        '<testcase classname="x" name="ok"/></testsuite>'
    )
    record = parse_junit(path)
    assert record["status"] == "VALID"
    assert record["tests"] == 1
