import shutil
from pathlib import Path

from equivariant_clock.protocol import code_inventory, executable_isolation_scan, strict_json_loads


CODE_ROOT = Path(__file__).parents[1]


def test_strict_json_closed_inventory_and_scanner() -> None:
    assert strict_json_loads('{"a":1}') == {"a": 1}
    for text in ('{"a":1,"a":2}', '{"x":NaN}', '{"x":1.5}'):
        try:
            strict_json_loads(text)
        except ValueError:
            pass
        else:
            raise AssertionError("inexact JSON accepted")
    assert code_inventory(CODE_ROOT)["pass"] is True
    assert executable_isolation_scan(CODE_ROOT)["pass"] is True


def _attacked_copy(tmp_path: Path, snippet: str, name: str) -> Path:
    target = tmp_path / name
    shutil.copytree(CODE_ROOT, target)
    path = target / "equivariant_clock" / "candidate.py"
    path.write_text(path.read_text(encoding="utf-8") + "\n" + snippet + "\n", encoding="utf-8")
    return target


def test_scanner_rejects_capability_float_and_hidden_modulus_attacks(tmp_path: Path) -> None:
    snippets = (
        "import importlib as bridge\nlatent = bridge.import_module('requests')",
        "import os\nlatent = os.system('true')",
        "import requests\nlatent = requests.get('https://example.invalid')",
        "latent = 1.25",
        "latent = getattr(__builtins__, '__import__')('socket')",
        "from pathlib import Path\nlatent = Path('/tmp/prime-table').read_bytes()",
        "HIDDEN_MODULI = (13, 17)",
    )
    for index, snippet in enumerate(snippets):
        target = _attacked_copy(tmp_path, snippet, "attack_" + str(index))
        assert executable_isolation_scan(target)["pass"] is False
    extra = tmp_path / "extra"
    shutil.copytree(CODE_ROOT, extra)
    (extra / "equivariant_clock" / "latent.py").write_text("TARGETS=(19,23)\n", encoding="utf-8")
    assert code_inventory(extra)["pass"] is False
