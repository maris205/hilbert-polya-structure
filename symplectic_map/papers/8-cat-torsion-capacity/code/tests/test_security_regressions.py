from __future__ import annotations

from pathlib import Path

from cat_torsion.protocol import (
    EXPECTED_CODE_FILES,
    executable_isolation_scan,
    stable_file_bytes,
)


PROJECT_ROOT = Path(__file__).absolute().parents[2]


def _closed_tree(tmp_path: Path) -> tuple[Path, Path, bytes]:
    project = tmp_path / "paper"
    code = project / "code"
    for relative in EXPECTED_CODE_FILES:
        source = PROJECT_ROOT / "code" / relative
        target = code / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(stable_file_bytes(source))
    (project / "pyproject.toml").write_bytes(stable_file_bytes(PROJECT_ROOT / "pyproject.toml"))
    candidate = code / "cat_torsion" / "candidate.py"
    return code, candidate, stable_file_bytes(candidate)


def test_scanner_blocks_alias_named_container_and_path_laundering(tmp_path):
    code, candidate, original = _closed_tree(tmp_path)
    attacks = [
        "import os as x\nx.system('true')\n",
        "from os import system as run\nrun('true')\n",
        "import os\nfuncs=(os.system,)\nrun=funcs[0]\nrun('true')\n",
        "funcs={'x':open}\nrun=funcs['x']\nrun('x')\n",
        "from pathlib import Path\nfuncs=(Path('prime_'+'table').read_text,)\nreader=funcs[0]\nreader()\n",
        "from pathlib import Path\nreader=Path('target_'+'zero').read_text\nreader()\n",
        "import os\ndef f(run=os.system):\n    return run('true')\n",
        "import os\nrun=(lambda value=os.system: value)()\nrun('true')\n",
        "import sys\nmod=sys.modules['os']\nrun=mod.system\nrun('true')\n",
        "import sys\nsys.modules['os'].system('true')\n",
    ]
    for source in attacks:
        candidate.write_text(source, encoding="utf-8")
        report = executable_isolation_scan(code)
        assert report["pass"] is False
        assert report["findings"]
    candidate.write_text("def legal(value):\n    return type(value) is float\n", encoding="utf-8")
    assert executable_isolation_scan(code)["pass"] is True
    candidate.write_bytes(original)


def test_scanner_rejects_symlink_hardlink_and_extra_file(tmp_path):
    code, candidate, original = _closed_tree(tmp_path)
    external = tmp_path / "external.py"
    external.write_bytes(original)
    candidate.unlink()
    candidate.symlink_to(external)
    assert executable_isolation_scan(code)["pass"] is False
    candidate.unlink()
    candidate.hardlink_to(external)
    assert executable_isolation_scan(code)["pass"] is False
    candidate.unlink()
    candidate.write_bytes(original)
    extra = code / "cat_torsion" / "extra.py"
    extra.write_text("value = 1\n", encoding="utf-8")
    assert executable_isolation_scan(code)["pass"] is False
