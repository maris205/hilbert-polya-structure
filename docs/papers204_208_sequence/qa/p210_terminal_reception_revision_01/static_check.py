#!/usr/bin/python3.10
"""Preparation-only AST/bytes/schema check; never imports or invokes a task program."""
import ast
import hashlib
import json
import os
from pathlib import Path
import re
import shlex
HERE = Path(__file__).resolve().parent
QA = HERE.parent
ROOT = QA.parents[2]
OLD = QA / "p210_terminal_reception_preparation"
PINS = {}
CHECKS = 0
def need(value, label):
    global CHECKS
    CHECKS += 1
    if not value:
        raise AssertionError(label)
def pin(path):
    p = Path(path)
    data = p.read_bytes()
    value = dict(bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
    need(str(p) not in PINS or PINS[str(p)] == value, "unchanged repeated direct original")
    PINS[str(p)] = value
    return value
def read(path):
    pin(path)
    return json.loads(Path(path).read_bytes())
def package(path, sha=None, count=None):
    p = Path(path)
    seal = pin(p / "SHA256SUMS")
    need(sha is None or seal["sha256"] == sha, "actual package seal")
    rows = {}
    for line in (p / "SHA256SUMS").read_text().splitlines():
        m = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        need(m is not None, "strict row")
        h, n = m.groups()
        f = p / n
        need(not Path(n).is_absolute() and ".." not in Path(n).parts and n != "SHA256SUMS" and
             f.resolve() == f and str(f) not in rows and pin(f)["sha256"] == h, "whole contained member")
        rows[str(f)] = pin(f)
    physical = {str(f) for f in p.rglob("*") if f.is_file() and f != p / "SHA256SUMS"}
    need(not any(f.is_symlink() for f in p.rglob("*")) and set(rows) == physical and
         (count is None or len(rows) == count), "complete nonself membership")
    return {**rows, str(p / "SHA256SUMS"): seal}
def merge(target, group):
    for name, value in group.items():
        need(name not in target or target[name] == value, "duplicate original exact equality")
        target[name] = value
def equal(left, right):
    pin(left); pin(right)
    need(Path(left).read_bytes() == Path(right).read_bytes(), "complete raw byte pair")
old = (OLD / "inspect_p210_terminal.py").read_text()
new = (HERE / "inspect_p210_terminal.py").read_text()
old_ast, new_ast = ast.parse(old), ast.parse(new)
old_funcs = {n.name: n for n in old_ast.body if isinstance(n, ast.FunctionDef)}
new_funcs = {n.name: n for n in new_ast.body if isinstance(n, ast.FunctionDef)}
need(set(old_funcs) == set(new_funcs), "same function set")
same = []
for name in old_funcs:
    if name in {"final_schema_binding", "main"}:
        continue
    need(ast.dump(old_funcs[name]) == ast.dump(new_funcs[name]), "whole unchanged helper AST: " + name)
    same.append(name)
old_limit = "The actual outer native schema and raw-stream provenance must be bound in a later sealed exact-schema revision; this preparation is unbound."
new_limit = "The actual outer02 native command/completion and separate builder streams are bound; the root tool envelope does not supply a separate outer-stderr file."
need(old.count(old_limit) == new.count(new_limit) == 1, "one disclosed main limitation change")
old_main = ast.get_source_segment(old, old_funcs["main"]).replace(old_limit, new_limit)
need(ast.dump(ast.parse(old_main)) == ast.dump(ast.parse(ast.get_source_segment(new, new_funcs["main"]))),
     "entire main AST unchanged apart from limitation string")
old_ast.body[0] = new_ast.body[0]
for n in old_ast.body:
    if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "PREP" for t in n.targets):
        n.value = ast.parse('QA / "p210_terminal_build_revision_02"', mode="eval").body
old_ast.body = [n for n in old_ast.body if not isinstance(n, ast.FunctionDef)]
new_ast.body = [n for n in new_ast.body if not isinstance(n, ast.FunctionDef)]
need(ast.dump(old_ast) == ast.dump(new_ast), "all nonfunction AST unchanged except module doc/PREP")
need(not any(isinstance(n, (ast.Import, ast.ImportFrom)) for n in ast.walk(new_funcs["final_schema_binding"])),
     "no new imported execution surface")
package(OLD, "90d89da705137fa7a8b6631f8dde00aadcdfbae6456b50e4593ec1db34d1ee1e", 11)
contract = read(HERE / "INPUT_CONTRACT.json")
actual = contract["final_schema_binding"]
groups = {}
for role, row in actual.items():
    if role == "root_native":
        continue
    groups[role] = package(row["path"], row["sha256"], row["payloads"])
    need(pin(Path(row["path"]) / "SHA256SUMS")["bytes"] == row["bytes"], "entire package seal size")
native = {}
for role, row in actual["root_native"].items():
    need(pin(row["path"]) == {k: row[k] for k in ("bytes", "sha256")}, "actual native pin")
    native[role] = read(row["path"])
launch, completion = native["launch"], native["completion"]
need(launch["result"]["session_id"] == completion["session_id"] == 91983 and launch["result"]["chunk_id"] == "d356b7" and
     launch["result"]["output"] == "" and completion["result"]["exit_code"] == 0 and
     completion["result"]["chunk_id"] == "81fe42" and "session_id" not in completion["result"], "actual root native end")
outer = Path(actual["launcher_output"]["path"])
builder = Path(actual["builder_preparation"]["path"])
build = Path(actual["build"]["path"])
lp = Path(actual["launcher_preparation"]["path"])
receipt = read(outer / "RECEIPT.json")
need(receipt["status"] == "PASS_P210_OUTER_CAPTURE_NOT_VIEWED" and receipt["original_wait_outcome"] == "COMPLETED" and
     receipt["original_wait_exit_code"] == 0 and receipt["original_wait_exception"] is None and
     receipt["cleanup_events"] == [] and receipt["cleanup_exit_code"] == 0 and receipt["builder_reaped"] is True and
     receipt["builder_group_absent"] is True and receipt["streams_hashed"] is True and receipt["inputs_unchanged"] is True and
     receipt["observed_runtime_closed"] is True and receipt["failures"] == [] and receipt["cache_absent"] is True and
     receipt["visual_review"] == "NOT_VIEWED" and receipt["outer_native_exit"] is None, "all actual receipt outcome types")
try:
    os.killpg(receipt["pid"], 0)
except ProcessLookupError:
    pass
else:
    raise AssertionError("owned builder group present")
need(read(outer / "SPAWNED.json") == dict(pid=receipt["pid"], owned_pgid=receipt["pid"], start_new_session=True),
     "actual spawn identity")
attempt = read(outer / "PRE_SPAWN_ATTEMPT.json")
excluded = {"original_wait_outcome", "original_wait_exit_code", "original_wait_exception"}
need({k: v for k, v in attempt.items() if k not in excluded} == {k: receipt[k] for k in attempt if k not in excluded}
     and attempt["original_wait_outcome"] == "NOT_STARTED" and attempt["original_wait_exit_code"] is None and
     attempt["original_wait_exception"] is None, "complete pre-spawn chain")
before, after = read(outer / "INPUTS_BEFORE.json"), read(outer / "INPUTS_AFTER.json")
need(before == after, "full outer pre/post inputs")
for name, value in before.items():
    need(pin(name) == value, "current actual outer input")
pf = QA / "p210_terminal_preflight_02"
pfkeys = package(pf, "d6adc396a8562e8683f66df348aa420ce3f97997b4bf73c0c674f621aac7fb1c", 6)
pfr, pfd = read(pf / "RESULT.json"), read(pf / "stdout")
need(pfr["original_wait_exit_code"] == 0 and pfr["inputs_unchanged"] is True and pfr["inputs_before"] == pfr["inputs_after"] and
     pfd["status"] == "PASS_P210_FINAL_SCHEMA_PREFLIGHT_ONLY" and pfd["source"] == pin(builder / "build_p210.py") and
     pfd["preparation_seal"] == pin(builder / "SHA256SUMS") and
     pfd["original_input_count"] == len(pfd["original_input_pins"]) == 1619, "actual full preflight types and source")
expected = {}
for group in (groups["launcher_preparation"], groups["builder_preparation"], pfkeys, pfr["inputs_before"], pfd["original_input_pins"]):
    merge(expected, group)
for name in ("record_p210_terminal_preflight_02.py", "P210_TERMINAL_PREFLIGHT02_ROOT_LAUNCH.actual.json",
             "P210_TERMINAL_PREFLIGHT02_ROOT_COMPLETION.actual.json", "P210_TERMINAL_PREFLIGHT02_ROOT_RECEPTION.actual.json"):
    merge(expected, {str(QA / name): pin(QA / name)})
env = dict(PATH="/usr/bin:/bin", LANG="C", LC_ALL="C", TZ="UTC", SOURCE_DATE_EPOCH="1704067200",
           FORCE_SOURCE_DATE="1", openin_any="p", openout_any="p")
oa = ["/usr/bin/python3.10", "-I", "-S", "-B", "-X", "pycache_prefix=" + str(outer / "unused_outer_cache"),
      str(lp / "launch_p210_terminal.py"), "--expected-preparation-sha256", actual["launcher_preparation"]["sha256"]]
need(shlex.split(launch["command"]) == ["/usr/bin/env", "-i", *[k + "=" + v for k, v in env.items()], *oa], "full native command")
for phase, label in (("BEFORE", "BEFORE_BUILDER_AND_OUTPUT_CREATION"), ("AFTER", "AFTER_CLOSED_BUILDER_AND_INPUT_REREAD")):
    r = read(outer / ("LAUNCHER_RUNTIME_" + phase + ".json"))
    need(r["phase"] == label and r["orig_argv"] == oa and r["environment"] == env and r["cwd"] == str(ROOT) and
         r["executable"] == "/usr/bin/python3.10" and r["sys_path"] ==
         ["/usr/lib/python310.zip", "/usr/lib/python3.10", "/usr/lib/python3.10/lib-dynload"] and
         r["cache_prefix"] == str(outer / "unused_outer_cache") and r["cache_absent"] is True and
         not os.path.lexists(r["cache_prefix"]), "full actual outer runtime context")
    need(all(re.search(r"(?:\(|, )" + f + r"=1(?:,|\))", r["flags"]) for f in
         ("dont_write_bytecode", "no_user_site", "no_site", "ignore_environment", "isolated")) and
         "optimize=0" in r["flags"], "all actual flags")
    mapped = {str(Path(s.split(None, 5)[5]).resolve()) for s in r["maps_raw"].splitlines()
              if len(s.split(None, 5)) == 6 and s.split(None, 5)[5].startswith("/")}
    need(mapped == set(r["mapped_files"]), "complete raw mapped correspondence")
    observations = dict(r["mapped_files"])
    for value in r["modules"].values():
        need(Path(value["path"]).suffix not in {".pyc", ".pyo"}, "source-only actual modules")
        merge(observations, {value["path"]: {k: value[k] for k in ("sha256", "bytes")}})
    for name, value in observations.items():
        need(pin(name) == value == before[name], "complete current observed key")
    if phase == "BEFORE":
        merge(expected, observations)
expected["/usr/bin/python3.10"] = pin("/usr/bin/python3.10")
need(expected == before, "entire independently reconstructed outer input union")
for left, right in ((outer / "executed_launcher.py", lp / "launch_p210_terminal.py"),
                    (outer / "executed_builder.py", builder / "build_p210.py"),
                    (build / "executed_source.py", builder / "build_p210.py")):
    equal(left, right)
result = read(build / "RESULT.json")
need(len(result["commands"]) == 33 and len(result["builds"]) == 2 and result["failures"] == [], "actual 33 commands/two builds")
for row in result["commands"]:
    need(row["status"] == "COMPLETED" and row["exit_code"] == 0 and row["error"] is None and
         row["start_new_session"] is True and row["streams_settled"] is True, "all actual native normal ends")
closure = dict(manifest=pin(build / "SHA256SUMS"), payloads=222, result=pin(build / "RESULT.json"),
               status="PASS_P210_SOURCE_ONLY_BUILD_PAIR_NOT_VIEWED")
report = dict(status=receipt["status"], output=str(outer), builder_exit_code=0,
              launcher_seal=pin(outer / "SHA256SUMS"), builder_closure=closure)
need(receipt["builder_closure"] == closure and completion["result"]["output"] == json.dumps(report, sort_keys=True) + "\n",
     "complete exact raw root native output including LF")
bstdout = dict(status=result["status"], output=str(build), commands=33, builds=result["builds"], failures=[],
               seal=pin(build / "SHA256SUMS"), payloads=222)
need((outer / "builder.stdout").read_text() == json.dumps(bstdout, sort_keys=True) + "\n" and
     (outer / "builder.stderr").read_bytes() == (pf / "stderr").read_bytes() == b"", "actual separate full builder raw streams")
for name, value in receipt["streams"].items():
    need(pin(outer / name) == value, "actual separate stream keys")
recipe = read(builder / "INPUT_CONTRACT.json")
binding = read(build / "FINAL_SCHEMA_BINDING_RETURN.json")
need(binding == pfd["final_schema_binding_return"] and read(build / "ORIGINALS_BEFORE.json") ==
     read(build / "ORIGINALS_AFTER.json") == pfd["original_input_pins"], "entire preflight/build map equality")
prereq = {}
bound = recipe["final_schema_binding"]
need(len(bound["manifests"]) == 8 and len(bound["roles"]) == 41, "full actual prerequisite role census")
for row in bound["manifests"].values():
    merge(prereq, package(row["path"], row["seal"]["sha256"], row["payloads"]))
for row in bound["roles"].values():
    value = {k: row[k] for k in ("sha256", "bytes")}
    need(pin(row["path"]) == value, "actual named prerequisite original")
    merge(prereq, {row["path"]: value})
need(len(prereq) == 1594 and binding["required_input_pins"] == prereq and binding["papers"] == bound["papers"] and
     binding["status"] == "BOUND_ACTUAL_P210_B_ROOT_ROUND2_PRETERMINAL_ORIGINALS", "complete 1594 actual subset")
rb, cb, r2 = (read(bound["roles"][n]["path"]) for n in ("root_b", "b_current", "round2_reception"))
need(rb["schema"] == "p210-b-root-delta-closure-v1" and rb["status"] == "ROOT_ACCEPTED_B_DELTA_ORIGINAL_CLOSURE_PASS" and
     all(rb[k] is True for k in ("reviewer_delta_accepted", "root_original_inspection_complete", "root_replay_closure_complete")) and
     rb["current_open_findings"] == 0 and cb["accepted_delta"] is True and cb["reviewer"] == rb["reviewer"] == "/root/p210_b_reviewer" and
     cb["current_open_counts"] == dict(Critical=0, Major=0, Minor=0) and r2["status"] == "PASS_ROOT_PHYSICAL_P210_ROUND2_RECEPTION" and
     r2["payloads"] == 524 and r2["round2_manifest_sha256"] == binding["papers"]["P210"]["freeze_manifest"]["sha256"],
     "every actual B/root/Round2 composite field and type")
for name in ("inspect_p210_terminal.py", "INPUT_CONTRACT.json", "README.md", "static_check.py"):
    pin(HERE / name)
print(json.dumps(dict(status="PASS_PREPARATION_AST_BYTES_ACTUAL_SCHEMA_ONLY_NOT_RECEIVER_EXECUTION", checks=CHECKS,
    unchanged_helper_functions=same, complete_main_ast="unchanged except one limitation string", source=pin(HERE / "inspect_p210_terminal.py"),
    old_source=pin(OLD / "inspect_p210_terminal.py"), outer_input_union=len(before), actual_originals=1619,
    actual_semantic_prerequisites=1594, terminal_payloads=222, actual_native_commands=33,
    bounded_existing_path_pins=len(PINS), new_host_inventory_collections=0, new_science_build_view_or_receiver_executions=0,
    pins=PINS), sort_keys=True))
