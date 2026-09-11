#!/usr/bin/env python3
"""AST/data-only check; never import, invoke or partially execute any inspected program."""
import ast
from datetime import datetime, timezone
import difflib
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import shlex
import sys

ROOT = Path("/root/autodl-tmp/symbolic_dynamics")
QA = ROOT / "docs/papers204_208_sequence/qa"
HERE = QA / "p210_terminal_reception_preparation"
OLD = QA / "batch_four_build_original_revision_01"
OLD_BUILD = QA / "p210_terminal_build_preparation"
NEW_BUILD = QA / "p210_terminal_build_revision_01"
PAPER = ROOT / "papers/210-weakly-increasing-run-aggregation"
KEYS, CHECKS = {}, []


def key(body):
    return dict(sha256=sha256(body).hexdigest(), bytes=len(body))


def ck(value, label):
    assert value, label
    CHECKS.append(label)


def raw(path):
    path = Path(path)
    ck(path.resolve() == path and path.is_file() and not path.is_symlink(), "explicit physical file " + str(path))
    body = path.read_bytes()
    value = key(body)
    ck(str(path) not in KEYS or KEYS[str(path)] == value, "same-read key " + str(path))
    KEYS[str(path)] = value
    return body


def package(base, wanted, count):
    body = raw(base / "SHA256SUMS")
    ck(key(body)["sha256"] == wanted, "actual original preparation seal " + str(base))
    names = set()
    for row in body.decode().splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", row)
        ck(match is not None, "strict original manifest row")
        digest, name = match.groups()
        ck(not Path(name).is_absolute() and ".." not in Path(name).parts and
           name != "SHA256SUMS" and name not in names, "safe distinct original member " + name)
        ck(key(raw(base / name))["sha256"] == digest, "entire original payload " + name)
        names.add(name)
    entries = list(base.rglob("*"))
    ck(not any(p.is_symlink() for p in entries) and len(names) == count and names ==
       {p.relative_to(base).as_posix() for p in entries if p.is_file() and p != base / "SHA256SUMS"},
       "complete unchanged nonself original membership " + str(base))


def main():
    ck(sys.argv[1:] in (["collect-baseline"], ["ast-data-only"]), "explicit static-only mode")
    ck(sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode, "isolated no-site no-bytecode static interpreter")
    package(OLD, "3c7d87dd961c270c5694d198e98caf9c39fcb17e75375dc398c7cedbf084771f", 12)
    package(OLD_BUILD, "beebe9b3db278b65ceb2ae8060c377889b5effab1806c9f7a2ce54b1c803d6a9", 7)
    old = raw(OLD / "inspect_four_builds.py").decode()
    source = raw(HERE / "inspect_p210_terminal.py").decode()
    builder = raw(NEW_BUILD / "build_p210.py").decode()
    raw(NEW_BUILD / "INPUT_CONTRACT.json")
    raw(HERE / "README.md")
    raw(HERE / "static_check.py")
    contract = json.loads(raw(HERE / "INPUT_CONTRACT.json"))
    historical = json.loads(raw(OLD_BUILD / "INPUT_CONTRACT.json"))
    for path, wanted in historical["infrastructure_pins"].items():
        ck(key(raw(path)) == wanted, "actual infrastructure byte pin " + path)
    baseline = historical["historical_round1_source_baseline"]
    for base in (PAPER, PAPER / "frozen_round1"):
        for name, wanted in {**baseline["source_pins"], "main.pdf": baseline["pdf_pin"]}.items():
            ck(key(raw(base / name)) == wanted, "actual historical ten-source/PDF key " + str(base / name))
    report = raw(QA / "BATCH_FOUR_BUILDS_ROOT_INSPECTION.md").decode()
    launch = json.loads(raw(QA / "BATCH_FOUR_BUILDS_ROOT_REVISION01_LAUNCH.actual.json"))
    completion = json.loads(raw(QA / "BATCH_FOUR_BUILDS_ROOT_REVISION01_COMPLETION.actual.json"))
    old_native = json.loads(completion["result"]["output"])
    ck("ROOT_ACCEPTED_FOUR_FRESH_SOURCE_ONLY_BUILDS_AND_ORIGINAL_EVIDENCE" in report and
       launch["result"]["session_id"] == completion["session_id"] == 63799 and completion["result"]["exit_code"] == 0 and
       launch["result"]["output"] == "" and old_native["status"] == "PASS_FOUR_BUILD_ORIGINAL_DOCUMENTS_ONLY" and
       old_native["checks"] == 400754 and old_native["current_path_keys"] == 124177, "actual accepted old receiver native provenance, not a new receiver execution")
    ck(launch["source_sha256"] == KEYS[str(OLD / "inspect_four_builds.py")]["sha256"] and
       launch["preparation_sha256"] == KEYS[str(OLD / "SHA256SUMS")]["sha256"] and
       shlex.split(launch["command"]) == ["/usr/bin/python3.10", "-I", "-S", "-B", str(OLD / "inspect_four_builds.py")],
       "complete old native source/preparation/argv binding")
    ck(len(old.splitlines()) == 495 and len(old.encode()) == 32043, "actual original 495-line 32043-byte source, not read-range upper bound")
    old_tree, tree, builder_tree = ast.parse(old), ast.parse(source), ast.parse(builder)
    functions = lambda t: {n.name: n for n in ast.walk(t) if isinstance(n, ast.FunctionDef)}
    prior, own, writer = functions(old_tree), functions(tree), functions(builder_tree)
    dump = lambda n: ast.dump(n, include_attributes=False)
    changed = sorted(n for n in prior if n in own and dump(prior[n]) != dump(own[n]))
    ck(changed == ["build", "commands", "main", "native_records", "originals"], "only five disclosed original functions change")
    ck(set(own) - set(prior) == {"final_schema_binding"} and not set(prior) - set(own), "one hard-gate function added, no original helper removed")
    reused = {}
    for name in sorted(set(prior) - set(changed)):
        ck(dump(prior[name]) == dump(own[name]), "exact original helper AST " + name)
        reused[name] = key(ast.get_source_segment(source, own[name]).encode())
    imports = lambda t: [dump(n) for n in t.body if isinstance(n, (ast.Import, ast.ImportFrom))]
    ck(imports(old_tree) == imports(tree), "all imports unchanged, no program-import shortcut")
    assignments = lambda t: {target.id: n.value for n in t.body if isinstance(n, ast.Assign) for target in n.targets if isinstance(target, ast.Name)}
    oa, na, ba = assignments(old_tree), assignments(tree), assignments(builder_tree)
    for name in sorted(set(oa) - {"OUT", "PREP", "OUT_SEAL", "PREP_SEAL", "UNDERFULL"}):
        ck(dump(oa[name]) == dump(na[name]), "unchanged module binding " + name)
    ck(ast.literal_eval(na["SOURCE_NAMES"]) == ast.literal_eval(ba["SOURCE_NAMES"]) ==
       tuple(baseline["source_names"]) and len(baseline["source_names"]) == 10, "entire exact ten-source schema agreement")
    env = {kw.arg: ast.literal_eval(kw.value) for kw in na["ENV"].keywords}
    ck(env == ast.literal_eval(ba["ENV"]) == dict(PATH="/usr/bin:/bin", LANG="C", LC_ALL="C", TZ="UTC",
       SOURCE_DATE_EPOCH="1704067200", FORCE_SOURCE_DATE="1", openin_any="p", openout_any="p"), "exact eight-variable original deterministic environment")
    stub = own["final_schema_binding"]
    ck(isinstance(stub.body[-1], ast.Raise) and not any(isinstance(n, ast.Return) for n in ast.walk(stub)),
       "hard unbound gate has no success branch")
    ck(isinstance(own["main"].body[1], ast.Assign) and isinstance(own["main"].body[1].value, ast.Call) and
       isinstance(own["main"].body[1].value.func, ast.Name) and own["main"].body[1].value.func.id == "final_schema_binding",
       "hard gate is second main statement before original/host reads or PASS output")
    ck(contract["schema"] == "p210-terminal-reception-unbound-contract-v1" and
       contract["stage"] == "PRELIMINARY_UNBOUND_NO_EXECUTION" and contract["final_schema_binding"] is None and
       contract["actual_native_builds_observed"] == contract["actual_native_receivers_run"] == contract["actual_new_views"] == 0,
       "actual contract is fully unbound, no prospective evidence asserted")
    forbidden = {"write", "write_bytes", "write_text", "mkdir", "unlink", "remove", "rmdir", "rename", "replace", "system", "popen"}
    ck(not any(isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr in forbidden for n in ast.walk(tree)),
       "receiver has no filesystem mutation or child-process surface")
    ck(not any(isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in {"exec", "eval", "compile", "__import__"} for n in ast.walk(tree)),
       "receiver does not dynamically import/evaluate an old program")
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr == "open":
            ck(n.args and isinstance(n.args[0], ast.Constant) and n.args[0].value == "rb", "only existing accepted binary read open")
    old_native_source = ast.get_source_segment(old, prior["native_records"])
    native_expected = old_native_source.replace("len(expected) == 58", "len(expected) == 33").replace(
        "all 58 native commands, original order", "all 33 native commands, original order including actual Round2 pdfinfo")
    ck(dump(ast.parse(native_expected).body[0]) == dump(own["native_records"]), "native receipt/stream/failure code changes only count and label")
    old_commands = ast.get_source_segment(old, prior["commands"])
    expected_commands_source = old_commands.replace('PREP / "build_four.py"', 'PREP / "build_p210.py"').replace(
        'for ident in ("P205", "P207"):', 'for ident in ("P210",):').replace(
        '        paper = contract["papers"][ident]\n        for number in (1, 2):',
        '        paper = contract["papers"][ident]\n        freeze_pdf = Path(paper["freeze"]) / "main.pdf"\n        add("P210_round2_pdfinfo", ["/usr/bin/pdfinfo", freeze_pdf], OUT, [freeze_pdf])\n        for number in (1, 2):').replace(
        'cold = OUT / label', 'cold = OUT / ("cold_build_" + str(number))').replace(
        'OUT / (ident + "_cold_build_" + str(n)) / "main.pdf"', 'OUT / ("cold_build_" + str(n)) / "main.pdf"')
    ck(dump(ast.parse(expected_commands_source).body[0]) == dump(own["commands"]), "entire expected native argv/direct/mutable/cwd source is exact minimal adaptation")
    labels = ["source_cmp", "ldd_before", "pdflatex_version", "bibtex_version", "texmf_roots", "P210_round2_pdfinfo"]
    suffixes = ["TEXMFHOME", "TEXMFCONFIG", "TEXMFVAR", "pass1", "bst", "bibtex", "pass2", "pass3", "pdfinfo", "pdffonts", "pdftotext", "frozen_cmp"]
    for number in (1, 2):
        stem = "P210_cold_build_" + str(number)
        labels.extend(stem + "_" + suffix for suffix in suffixes)
        if number == 1:
            labels.append(stem + "_render")
    labels += ["P210_pair_cmp", "ldd_after"]
    ck(len(labels) == len(set(labels)) == contract["prospective_native_count"] == 33, "prospective exact ordered 33 labels only, no command executed")
    for token in ('cold = OUT / ("cold_build_" + str(number))', 'cold = OUT / ("cold_build_" + match.group(1))',
                  'OUT / ("cold_build_" + str(n)) / query', '"P210_round2_pdfinfo"', 'round2_pages == pages',
                  'text_pages = extracted.split("\\f")', 'reference_heading_pages=bibliography_pages',
                  'round2_measured_pages=round2_pages', 'venue_page_limit=None', 'bibtex_warnings_or_errors=[]',
                  'sorted(CURRENT) == keys', 'extra = {path: CURRENT[path] for path in keys if path not in known_original_paths}',
                  'known_original_paths[path] == value', '{**known_original_paths, **extra} == CURRENT',
                  'current_key_reconstruction=reconstruction', 'complete_map=digest_bytes(complete_raw)',
                  'stdout=json.dumps(expected_stdout, sort_keys=True) + "\\n", stderr=""'):
        ck(token in source, "required prepared mechanism " + token)
    ck('OUT / label' not in source and not any(n in source for n in ("P205", "P207", "OUT_SEAL", "PREP_SEAL")),
       "no stale multi-paper physical directory or historic success seal")
    new_build = ast.get_source_segment(source, own["build"])
    old_build = ast.get_source_segment(old, prior["build"])
    prefix = old_build.split('    require(not re.search(r"Warning--|error message"')[0].replace(
        '    cold = OUT / label',
        '    match = re.fullmatch(r"P210_cold_build_([12])", label)\n    require(match is not None, "exact P210 command label, separate from physical directory")\n    cold = OUT / ("cold_build_" + match.group(1))')
    ck(new_build.startswith(prefix), "entire original auxiliary/FLS/raw-pair prefix unchanged except physical directory")
    suffix = old_build[old_build.index('    require(read(OUT / (label + "_MEASURED.json"))'):]
    ck(new_build.endswith(suffix), "entire original final measured/cold-product/PNG census suffix unchanged")
    before_metadata = old_build[old_build.index("    bst = "):old_build.index('    require(not any(x in text(OUT / (label + ".txt"))')]
    ck(before_metadata in new_build, "all original bibliography-style/PDF/font/diagnostic metadata code unchanged")
    writer_result = next(n.value for n in ast.walk(writer["main"]) if isinstance(n, ast.Assign) and
                         any(isinstance(t, ast.Name) and t.id == "result" for t in n.targets) and
                         isinstance(n.value, ast.Dict) and any(isinstance(k, ast.Constant) and k.value == "label" for k in n.value.keys))
    measured = next(n.value for n in own["build"].body if isinstance(n, ast.Assign) and
                    any(isinstance(t, ast.Name) and t.id == "expected_measured" for t in n.targets))
    ck({ast.literal_eval(k) for k in writer_result.keys} == {kw.arg for kw in measured.keywords},
       "entire known writer/receiver MEASURED field census")
    raw_fixture = json.dumps({"absent": dict(exists=False, symlink=False, link=None, resolved="/fixture/absent", is_file=False, is_dir=False)},
                            sort_keys=True, separators=(",", ":")).encode("utf-8")
    ck(raw_fixture.endswith(b"}}") and not raw_fixture.endswith(b"\n"), "pure in-memory complete-map canonical encoding fixture, no host reads")
    direct = {path: value for path, value in KEYS.items() if not Path(path).is_relative_to(HERE)}
    delta = "".join(difflib.unified_diff(old.splitlines(keepends=True), source.splitlines(keepends=True),
                   fromfile=str(OLD / "inspect_four_builds.py"), tofile=str(HERE / "inspect_p210_terminal.py")))
    if sys.argv[1] == "ast-data-only":
        pins = json.loads(raw(HERE / "INPUT_PINS.json"))
        ck(pins["pins"] == direct, "entire explicitly bound actual original input key")
        ck(raw(HERE / "SOURCE_DELTA.diff").decode() == delta, "full exact original-to-new source diff, including trailing context spaces")
        provenance = json.loads(raw(HERE / "PROVENANCE.json"))
        ck(provenance["original_source"] == KEYS[str(OLD / "inspect_four_builds.py")] and
           provenance["prepared_source"] == KEYS[str(HERE / "inspect_p210_terminal.py")] and
           provenance["changed_functions"] == changed and provenance["exact_reused_functions"] == reused,
           "complete source/provenance AST binding")
        baseline_native = json.loads(raw(HERE / "BASELINE_NATIVE.actual.json"))
        baseline_actual = raw(HERE / "BASELINE.actual.json")
        ck(baseline_native["result"]["exit_code"] == 0 and baseline_native["result"]["output"].encode() == baseline_actual,
           "complete actual baseline native stdout/data and real zero exit")
    ck(not os.path.lexists(PAPER / "qa_final"), "actual qa_final physically absent")
    for path, wanted in dict(KEYS).items():
        ck(key(Path(path).read_bytes()) == wanted, "final explicit original uncached reread " + path)
    print(json.dumps(dict(schema="p210-terminal-reception-static-v1",
        status="PASS_STATIC_HARD_UNBOUND_NOT_EXECUTED", mode=sys.argv[1], utc=datetime.now(timezone.utc).isoformat(),
        checks=len(CHECKS), check_labels=CHECKS, direct_original_pins=direct, input_keys=KEYS, input_count=len(KEYS),
        original_source=KEYS[str(OLD / "inspect_four_builds.py")], prepared_source=KEYS[str(HERE / "inspect_p210_terminal.py")],
        original_source_lines=len(old.splitlines()), prepared_source_lines=len(source.splitlines()),
        changed_functions=changed, exact_reused_functions=reused, added_functions=["final_schema_binding"],
        source_diff=delta, source_diff_lines=len(delta.splitlines()), prospective_native_labels=labels,
        receiver_executions=0, builder_executions=0, scientific_runs=0, native_build_pdf_font_render_cmp_calls=0,
        page_views=0, host_inventory_collections=0, host_tree_copies=0, qa_final_created=False, root_acceptance=False,
        external="OWNER_AMBER / HOLD_EXTERNAL"), sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
