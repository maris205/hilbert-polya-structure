#!/usr/bin/env python3
"""Static-only preparation checks: parse/read/hash; NEVER import/run inspector."""
import ast
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
A = ROOT / "docs/papers204_208_sequence/reviews/p210_a"
OLD = ROOT / "docs/papers204_208_sequence/qa/p210_round0_original_preparation/inspect_originals.py"
records = []


def check(value, role):
    if not value:
        raise AssertionError(role)
    records.append(role)


def signature(node):
    return ast.dump(node, include_attributes=False)


check(sys.flags.isolated and sys.flags.no_site and sys.flags.dont_write_bytecode, "static tool invoked isolated/no-site/no-bytecode")
source = (HERE / "inspect_originals.py").read_text()
tree = ast.parse(source, filename=str(HERE / "inspect_originals.py"))
check(bool(tree.body), "entire inspector parsed without execution")
imports = {alias.name for node in ast.walk(tree) if isinstance(node, ast.Import) for alias in node.names}
froms = {(node.module, tuple(alias.name for alias in node.names)) for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)}
check(imports == {"ast", "collections", "gzip", "hashlib", "json", "re", "sys"} and froms == {("pathlib", ("Path",))},
      "inspector imports only explicit standard-library read/data/AST helpers")
calls = [node for node in ast.walk(tree) if isinstance(node, ast.Call)]
check(not any(isinstance(node.func, ast.Name) and node.func.id in {"exec", "eval", "__import__", "compile", "open"} for node in calls),
      "no dynamic execution/import/compiler or unscoped builtin open in inspector")
for node in calls:
    if isinstance(node.func, ast.Attribute):
        check(node.func.attr not in {"write", "write_text", "write_bytes", "mkdir", "unlink", "rename", "rmdir", "touch",
                                    "run", "Popen", "system", "spawn", "execve", "copy", "copy2", "copytree", "run_path", "run_module"},
              "no mutation/launch call at inspector line%d" % node.lineno)
        if node.func.attr == "replace":
            check(len(node.args) == 2 and all(isinstance(value, ast.Constant) and isinstance(value.value, str) for value in node.args),
                  "only literal string replacement, not Path.replace, at inspector line%d" % node.lineno)
        if node.func.attr == "open":
            check(len(node.args) == 1 and isinstance(node.args[0], ast.Constant) and node.args[0].value == "rb" and not node.keywords,
                  "only read-binary stream open at inspector line%d" % node.lineno)
check(isinstance(tree.body[-1], ast.If) and signature(tree.body[-1].test) == signature(ast.parse('__name__ == "__main__"', mode="eval").body),
      "inspector main is guarded; static tool does not import it")
old = ast.parse(OLD.read_text())
old_funcs = {node.name: node for node in old.body if isinstance(node, ast.FunctionDef)}
new_funcs = {node.name: node for node in tree.body if isinstance(node, ast.FunctionDef)}
unchanged = ["require", "fresh_pin", "memo", "raw", "document", "text", "pin", "physical", "expected_environment", "child_commands", "map_paths"]
for name in unchanged:
    check(signature(old_funcs[name]) == signature(new_funcs[name]), "unchanged proven original helper AST: " + name)
original_comparison = ast.parse((A / "compare_author.py").read_text())
adapted = new_funcs["semantic_compare"]
old_parts = {node.name: node for node in original_comparison.body if isinstance(node, ast.FunctionDef)}
new_parts = {node.name: node for node in adapted.body if isinstance(node, ast.FunctionDef)}
for name in ["parts", "mask", "intervals", "keys"]:
    check(signature(old_parts[name]) == signature(new_parts[name]), "unchanged full transcript helper AST: " + name)
original_loop = [node for node in original_comparison.body if isinstance(node, ast.For)]
adapted_loop = [node for node in adapted.body if isinstance(node, ast.For)]
check([signature(node) for node in original_loop] == [signature(node) for node in adapted_loop] and len(original_loop) == 1,
      "entire whole-author-transcript loop unchanged, not abbreviated to summary fields")
def comparison_calls(node):
    return [signature(value) for value in ast.walk(node) if isinstance(value, ast.Call) and
            isinstance(value.func, ast.Name) and value.func.id in {"eq", "keys"}]
check(comparison_calls(original_comparison) == comparison_calls(adapted), "all original eq/keys data predicates unchanged")
original_return = original_comparison.body[-1].value.args[0].args[0]
adapted_return = adapted.body[-1].value
check(signature(original_return) == signature(adapted_return), "entire original comparison result structure preserved")
bindings = json.loads((HERE / "INPUT_PINS.json").read_text())
for name, expected in bindings["pins"].items():
    path = Path(name)
    actual = dict(sha256=hashlib.sha256(path.read_bytes()).hexdigest(), size=path.stat().st_size,
                  real=str(path.resolve()), symlink=str(path.readlink()) if path.is_symlink() else None)
    check(actual == expected, "exact direct preparation input key: " + name)
check(hashlib.sha256((A / "SHA256SUMS").read_bytes()).hexdigest() == bindings["initial_review_seal_sha256"],
      "direct initial A seal still exact; full484-member inspector was NOT run")
print(json.dumps(dict(status="PASS_STATIC_PREPARATION_ONLY", checks=len(records), checks_performed=records,
    inspector_sha256=hashlib.sha256(source.encode()).hexdigest(), inspector_lines=len(source.splitlines()),
    static_source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), unchanged_original_helpers=unchanged,
    direct_input_pins=len(bindings["pins"]), full_inspector_executed=False, original_code_imported_or_executed=False,
    scientific_runs=0, builds=0, new_views=0, root_acceptance=False), sort_keys=True, indent=2))
