import shutil
from pathlib import Path

from centralizer_q.protocol import (
    code_inventory,
    executable_isolation_scan,
    strict_json_loads,
)


CODE_ROOT = Path(__file__).parents[1]


def test_strict_json_and_closed_inventory() -> None:
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
    path = target / "centralizer_q" / "candidate.py"
    path.write_text(path.read_text(encoding="utf-8") + "\n" + snippet + "\n", encoding="utf-8")
    return target


def test_scanner_rejects_dynamic_alias_loader_process_network_and_float_bypasses(tmp_path: Path) -> None:
    snippets = (
        "import importlib as bridge\nlatent = bridge.import_module('requests')",
        "import pickle\nlatent = pickle.loads(b'x')",
        "import os\nlatent = os.system('true')",
        "import requests\nlatent = requests.get('https://example.invalid')",
        "latent = 1.25",
        "latent = getattr(__builtins__, '__import__')('socket')",
        "from pathlib import Path\nlatent = Path('/tmp/prime-table').read_bytes()",
        "import os\nlatent = os.read(os.open('/tmp/zero-table', os.O_RDONLY), 16)",
        "latent = __loader__.load_module('socket')",
    )
    for index, snippet in enumerate(snippets):
        target = _attacked_copy(tmp_path, snippet, "attack_" + str(index))
        assert executable_isolation_scan(target)["pass"] is False


def test_scanner_rejects_unreviewed_tree_and_hidden_modulus_literal(tmp_path: Path) -> None:
    hidden = _attacked_copy(tmp_path, "HIDDEN_MODULI = (13, 17)", "hidden")
    assert executable_isolation_scan(hidden)["pass"] is False
    extra = tmp_path / "extra"
    shutil.copytree(CODE_ROOT, extra)
    (extra / "centralizer_q" / "latent.py").write_text("TARGETS=(19,23)\n", encoding="utf-8")
    assert code_inventory(extra)["pass"] is False
