#!/usr/bin/env python3
"""Actual-bound source-only P210 terminal original-evidence receiver revision 01.

Prepared by P210's manuscript/verifier author, not a manuscript reviewer.
No original program is imported or executed. No new build/view is performed.
Binds actual outer02 normal native completion and closed build02 originals.
Root owns inspection, execution, six separate actual page views and acceptance.
"""
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import shlex
import sys
import sysconfig

HERE = Path(__file__).resolve().parent
QA = HERE.parent
ROOT = QA.parents[2]
PAPER = ROOT / "papers/210-weakly-increasing-run-aggregation"
OUT = PAPER / "qa_final"
PREP = QA / "p210_terminal_build_revision_02"
SOURCE_NAMES = ("main.tex", "math_commands.tex", "references.bib",
    "sections/0_abstract.tex", "sections/1_introduction.tex", "sections/2_clock.tex",
    "sections/3_image.tex", "sections/4_coding.tex", "sections/5_fibres.tex", "sections/6_scope.tex")
ENV = dict(PATH="/usr/bin:/bin", LANG="C", LC_ALL="C", TZ="UTC", SOURCE_DATE_EPOCH="1704067200",
           FORCE_SOURCE_DATE="1", openin_any="p", openout_any="p")
TOOLS = {Path("/usr/bin") / n for n in ("pdflatex", "bibtex", "kpsewhich", "pdfinfo", "pdffonts",
         "pdftotext", "pdftoppm", "ldd", "cmp", "env", "python3.10")} | {Path("/bin/bash"), Path("/bin/sh")}
STDLIB = Path("/usr/lib/python3.10")
TEX_ROOTS = tuple(map(Path, ("/usr/share/texlive/texmf-dist", "/usr/share/texmf", "/var/lib/texmf", "/etc/texmf",
    "/usr/local/share/texmf", "/root/texmf", "/root/.texlive2021/texmf-config", "/root/.texlive2021/texmf-var")))
LIB_ROOTS = tuple(map(Path, ("/usr/lib/x86_64-linux-gnu", "/usr/lib64", "/usr/local/lib")))
CONFIG_ROOTS = tuple(map(Path, ("/etc/ld.so.conf.d", "/usr/share/fonts", "/etc/fonts", "/var/cache/fontconfig",
    "/usr/share/fontconfig", "/usr/lib/locale/C.utf8", "/usr/lib/x86_64-linux-gnu/gconv", "/usr/lib/gconv",
    "/usr/share/poppler", "/usr/local/share/fonts", "/etc/xdg/fontconfig", "/etc/profile.d", "/root/.fonts",
    "/root/.fontconfig", "/root/.fonts.conf.d", "/root/.config/fontconfig", "/root/.cache/fontconfig", "/root/.local/share/fonts")))
USER_VARS = ("TEXMFHOME", "TEXMFCONFIG", "TEXMFVAR")
CURRENT = {}
CHECKS = 0
RAW_PAIRS = 0


def require(value, label):
    global CHECKS
    CHECKS += 1
    if not value:
        raise AssertionError(label)


def digest_bytes(data):
    return dict(bytes=len(data), sha256=hashlib.sha256(data).hexdigest())


def fresh_entry(path):
    path = Path(path)
    row = dict(exists=path.exists(), symlink=path.is_symlink(), link=str(path.readlink()) if path.is_symlink() else None,
               resolved=str(path.resolve()), is_file=path.is_file(), is_dir=path.is_dir())
    if row["is_file"]:
        sha = hashlib.sha256()
        with path.open("rb") as stream:
            for block in iter(lambda: stream.read(1 << 20), b""):
                sha.update(block)
        row.update(bytes=path.stat().st_size, sha256=sha.hexdigest())
    return row


def current(path):
    key = str(Path(path))
    if key not in CURRENT:
        CURRENT[key] = fresh_entry(key)
    return CURRENT[key]


def pin(path):
    row = current(path)
    require(row["is_file"], "missing current file: " + str(path))
    return {k: row[k] for k in ("sha256", "bytes")}


def raw(path):
    data = Path(path).read_bytes()
    require(digest_bytes(data) == pin(path), "complete raw read changed: " + str(path))
    return data


def read(path):
    return json.loads(raw(path))


def text(path):
    return raw(path).decode("utf-8")


def exact_pair(left, right):
    global RAW_PAIRS
    require(raw(left) == raw(right), "whole raw byte pair: " + str(left))
    RAW_PAIRS += 1


def physical(base):
    entries = list(base.rglob("*"))
    require(not any(p.is_symlink() for p in entries), "no symlink in physical sealed package")
    return {str(p): pin(p) for p in entries if p.is_file() and p != base / "SHA256SUMS"}


def manifest(base, seal, count):
    require(pin(base / "SHA256SUMS")["sha256"] == seal, "exact original manifest identity")
    rows = {}
    for line in text(base / "SHA256SUMS").splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        require(match is not None, "strict original manifest row")
        sha, name = match.groups()
        path = base / name
        require(not Path(name).is_absolute() and ".." not in Path(name).parts and name != "SHA256SUMS" and
                str(path) not in rows and path.resolve() == path, "exact contained original member")
        value = pin(path)
        require(value["sha256"] == sha, "original manifest digest")
        rows[str(path)] = value
    require(len(rows) == count and rows == physical(base), "complete nonself original membership")
    return {**rows, str(base / "SHA256SUMS"): pin(base / "SHA256SUMS")}


def ledger(name):
    path = OUT / (name + ".json.gz")
    compressed = raw(path)
    body = gzip.decompress(compressed)
    sidecar = read(OUT / (name + ".json.gz.meta.json"))
    data = json.loads(body)
    require(sidecar == dict(encoding="gzip of exact UTF-8 JSON with terminal LF; mtime=0",
            json_bytes=len(body), json_sha256=hashlib.sha256(body).hexdigest(), compressed=pin(path),
            semantic_groups={k: len(v) for k, v in data.items()}), "entire lossless ledger sidecar")
    require(body.endswith(b"\n") and compressed[:4] == b"\x1f\x8b\x08\x00" and compressed[4:8] == b"\x00" * 4,
            "exact gzip header and final JSON newline")
    return data, digest_bytes(body)


def known_membership(snapshot):
    # Match the original bounded selection rules; never copy any host tree.
    std = {STDLIB}
    for directory, folders, files in os.walk(STDLIB):
        folders[:] = [n for n in folders if n not in {"site-packages", "dist-packages", "__pycache__"}]
        std.update(Path(directory) / n for n in files if not n.endswith((".pyc", ".pyo")))
    runtime = std | TOOLS | set(LIB_ROOTS)
    for base in LIB_ROOTS:
        paths = base.glob("*") if base == Path("/usr/local/lib") else base.rglob("*")
        runtime.update(p for p in paths if p.is_file() and (p.name.endswith(".so") or ".so." in p.name))
    groups = {"runtime": {str(p) for p in runtime}}
    for name, roots in (("tex", TEX_ROOTS), ("configuration", CONFIG_ROOTS)):
        selected = set(roots)
        for base in roots:
            if base.is_dir():
                selected.update(base.rglob("*"))
        if name == "configuration":
            # Restore the original explicit selection, including ABSENT fixed
            # children underneath recursive roots; never inherit ledger extras.
            selected.update(map(Path, ("/etc/ld.so.cache", "/etc/ld.so.conf", "/etc/ld.so.preload",
                "/etc/locale.conf", "/etc/default/locale", "/etc/nsswitch.conf", "/etc/localtime",
                "/etc/bash.bashrc", "/etc/profile", "/etc/passwd", "/etc/group", "/etc/fonts/local.conf",
                "/usr/lib/locale/locale-archive", "/root/.fonts.conf", "/root/.config/fontconfig/fonts.conf",
                "/usr/lib/python310.zip", "/usr/bin/pyvenv.cfg", "/usr/pyvenv.cfg")))
            for base in (Path("/usr/bin"), Path("/usr/lib")):
                selected.update(base / n for n in ("python._pth", "python3._pth", "python310._pth", "python3.10._pth"))
            selected.update(map(Path, (sysconfig.get_makefile_filename(), sysconfig.get_config_h_filename())))
            for key in ("LDLIBRARY", "INSTSONAME"):
                value = sysconfig.get_config_var(key)
                if value:
                    selected.add(STDLIB.parent / (value + "._pth"))
            ldd = text("/usr/bin/ldd")
            match = re.search(r'^RTLDLIST="([^"]+)"', ldd, re.M)
            require(ldd.startswith("#!/bin/bash\n") and match is not None, "original ldd interpreter/loader-list rule")
            selected.update(map(Path, match.group(1).split()))
        groups[name] = {str(p) for p in selected}
    differences = {name: dict(missing=sorted(set(snapshot.get(name, {})) - groups.get(name, set())),
                              unexpected=sorted(groups.get(name, set()) - set(snapshot.get(name, {}))))
                   for name in sorted(set(snapshot) | set(groups))}
    require(set(snapshot) == set(groups) and all(not d["missing"] and not d["unexpected"] for d in differences.values()),
            "complete original-scope current directory membership: " + json.dumps(differences, sort_keys=True))


def final_schema_binding():
    """Bind the actual settled outer02/build02 originals, not caller success flags."""
    reception = read(HERE / "INPUT_CONTRACT.json")
    require(reception["schema"] == "p210-terminal-reception-actual-bound-contract-v1" and
            reception["stage"] == "ACTUAL_OUTER02_BUILD02_BOUND_RECEIVER_NOT_EXECUTED" and
            reception["physical_output"] == str(OUT), "actual receiver contract and fixed terminal role")
    actual = reception["final_schema_binding"]
    require(set(actual) == {"launcher_preparation", "launcher_output", "builder_preparation", "build", "root_native"},
            "entire actual terminal binding role set")
    fixed = {
        "launcher_preparation": (QA / "p210_terminal_launch_revision_02", "6adbded08080db7be5ec261c59c18adf298464f6012e3e266b20e51d56b29bc2", 8, 706),
        "launcher_output": (QA / "p210_terminal_launch_02", "42fed5ca10fc44fb36159f955f9193342d0775ec0f2886efd09237293e96e773", 11, 940),
        "builder_preparation": (PREP, "2e99af39ab35bfb9e3fec7c9944927c574fe459b56a1b764a5948dde0266e31a", 9, 793),
        "build": (OUT, "659b493dbc4e84137cf873643c1673b725294455d057c62b41e82572ffd31fd1", 222, 22762)}
    for name, (path, sha, payloads, size) in fixed.items():
        require(actual[name] == dict(path=str(path), sha256=sha, payloads=payloads, bytes=size),
                "exact actually observed fixed package role")
    native_roles = actual["root_native"]
    require(set(native_roles) == {"launch", "completion"}, "exact two actual root native roles")
    for label, name in (("launch", "P210_TERMINAL_OUTER02_ROOT_LAUNCH.actual.json"),
                        ("completion", "P210_TERMINAL_OUTER02_ROOT_COMPLETION.actual.json")):
        row = native_roles[label]
        require(row["path"] == str(QA / name) and set(row) == {"path", "sha256", "bytes"} and
                pin(row["path"]) == {k: row[k] for k in ("sha256", "bytes")}, "actual root native original identity")
    launch, completion = (read(native_roles[k]["path"]) for k in ("launch", "completion"))
    require(launch["cwd"] == str(ROOT) and launch["result"]["session_id"] == 91983 and
            launch["result"]["chunk_id"] == "d356b7" and launch["result"]["output"] == "" and
            "exit_code" not in launch["result"] and completion["session_id"] == 91983 and
            completion["launch_record"] == Path(native_roles["launch"]["path"]).name and
            completion["result"]["chunk_id"] == "81fe42" and completion["result"]["exit_code"] == 0 and
            "session_id" not in completion["result"], "actual root native started-session-to-normal-completion chain")
    root_output = completion["result"]["output"]
    root_report = json.loads(root_output)
    require(root_report["status"] == "PASS_P210_OUTER_CAPTURE_NOT_VIEWED" and
            root_report["builder_exit_code"] == 0 and root_report["output"] == actual["launcher_output"]["path"],
            "actual complete native output reports settled outer success")
    launch_prep = Path(actual["launcher_preparation"]["path"])
    launch_out = Path(actual["launcher_output"]["path"])
    require(launch_prep == QA / "p210_terminal_launch_revision_02" and
            launch_out == QA / "p210_terminal_launch_02", "actual fixed outer preparation/output roles")
    launcher_originals = manifest(launch_prep, actual["launcher_preparation"]["sha256"],
                                 actual["launcher_preparation"]["payloads"])
    builder_originals = manifest(PREP, actual["builder_preparation"]["sha256"], 9)
    require(actual["builder_preparation"]["sha256"] ==
            "2e99af39ab35bfb9e3fec7c9944927c574fe459b56a1b764a5948dde0266e31a",
            "actual final root-read builder preparation")
    launch_receipt = read(launch_out / "RECEIPT.json")
    require(launch_receipt["status"] == "PASS_P210_OUTER_CAPTURE_NOT_VIEWED" and
            launch_receipt["original_wait_outcome"] == "COMPLETED" and
            launch_receipt["original_wait_exit_code"] == 0 and launch_receipt["original_wait_exception"] is None and
            launch_receipt["cleanup_events"] == [] and launch_receipt["cleanup_exit_code"] == 0 and
            launch_receipt["builder_reaped"] is True and launch_receipt["builder_group_absent"] is True and
            launch_receipt["streams_hashed"] is True and launch_receipt["inputs_unchanged"] is True and
            launch_receipt["observed_runtime_closed"] is True and launch_receipt["failures"] == [] and
            launch_receipt["cache_absent"] is True and launch_receipt["visual_review"] == "NOT_VIEWED" and
            launch_receipt["outer_native_exit"] is None,
            "actual successful settled outer receipt; its own native exit is externally bound, not retrofilled")
    require(launch_receipt["env"] == ENV and launch_receipt["cwd"] == str(ROOT) and
            launch_receipt["start_new_session"] is True and launch_receipt["timeout_seconds"] == 21600 and
            isinstance(launch_receipt["pid"], int) and launch_receipt["pid"] > 0 and
            launch_receipt["finished_epoch"] >= launch_receipt["started_epoch"],
            "actual full outer builder command context")
    try:
        os.killpg(launch_receipt["pid"], 0)
    except ProcessLookupError:
        pass
    else:
        raise AssertionError("Actual owned builder group is present at documentary reception")
    require(not os.path.lexists(launch_out / "UNCLOSED.json") and not os.path.lexists(OUT / "UNCLOSED.json"),
            "no unsettled or failed outer/build evidence")
    require(read(launch_out / "SPAWNED.json") == dict(pid=launch_receipt["pid"],
            owned_pgid=launch_receipt["pid"], start_new_session=True), "complete pre-pinned owned builder spawn")
    attempted = read(launch_out / "PRE_SPAWN_ATTEMPT.json")
    require({k: v for k, v in attempted.items() if k not in
            {"original_wait_outcome", "original_wait_exit_code", "original_wait_exception"}} ==
            {k: launch_receipt[k] for k in attempted if k not in
            {"original_wait_outcome", "original_wait_exit_code", "original_wait_exception"}} and
            attempted["original_wait_outcome"] == "NOT_STARTED" and attempted["original_wait_exit_code"] is None and
            attempted["original_wait_exception"] is None, "entire actual pre-spawn attempt-to-receipt chain")
    outer_payloads = manifest(launch_out, actual["launcher_output"]["sha256"],
                              actual["launcher_output"]["payloads"])
    require(set(launch_receipt["streams"]) == {"builder.stdout", "builder.stderr"} and
            all(pin(launch_out / name) == value for name, value in launch_receipt["streams"].items()) and
            raw(launch_out / "builder.stderr") == b"", "two real separately captured builder streams")
    before, after = read(launch_out / "INPUTS_BEFORE.json"), read(launch_out / "INPUTS_AFTER.json")
    require(before == after, "entire actual outer input key equality")
    for name, value in before.items():
        require(pin(name) == value, "every actual outer input current key")
    preflight_dir = QA / "p210_terminal_preflight_02"
    preflight_keys = manifest(preflight_dir, "d6adc396a8562e8683f66df348aa420ce3f97997b4bf73c0c674f621aac7fb1c", 6)
    preflight_result, preflight_data = read(preflight_dir / "RESULT.json"), read(preflight_dir / "stdout")
    require(preflight_result["original_wait_exit_code"] == 0 and preflight_result["inputs_unchanged"] is True and
            preflight_result["inputs_before"] == preflight_result["inputs_after"] and
            preflight_data["status"] == "PASS_P210_FINAL_SCHEMA_PREFLIGHT_ONLY" and
            preflight_data["source"] == pin(PREP / "build_p210.py") and
            preflight_data["preparation_seal"] == pin(PREP / "SHA256SUMS") and
            preflight_data["original_input_count"] == len(preflight_data["original_input_pins"]) == 1619 and
            raw(preflight_dir / "stderr") == b"", "actual complete preflight originals retained by outer")
    expected_before = {}
    extra_paths = [QA / name for name in ("record_p210_terminal_preflight_02.py",
        "P210_TERMINAL_PREFLIGHT02_ROOT_LAUNCH.actual.json", "P210_TERMINAL_PREFLIGHT02_ROOT_COMPLETION.actual.json",
        "P210_TERMINAL_PREFLIGHT02_ROOT_RECEPTION.actual.json")]
    for group in (launcher_originals, builder_originals, preflight_keys, {str(p): pin(p) for p in extra_paths},
                  preflight_result["inputs_before"], preflight_data["original_input_pins"]):
        for name, value in group.items():
            require(name not in expected_before or expected_before[name] == value, "exact consistent outer prerequisite union")
            expected_before[name] = value
    outer_argv = ["/usr/bin/python3.10", "-I", "-S", "-B", "-X",
        "pycache_prefix=" + str(launch_out / "unused_outer_cache"), str(launch_prep / "launch_p210_terminal.py"),
        "--expected-preparation-sha256", actual["launcher_preparation"]["sha256"]]
    require(shlex.split(launch["command"]) == ["/usr/bin/env", "-i",
            *[k + "=" + v for k, v in ENV.items()], *outer_argv],
            "entire actual root launch command is exact clean-environment outer invocation")
    for phase, label in (("BEFORE", "BEFORE_BUILDER_AND_OUTPUT_CREATION"),
                         ("AFTER", "AFTER_CLOSED_BUILDER_AND_INPUT_REREAD")):
        observed_outer = read(launch_out / ("LAUNCHER_RUNTIME_" + phase + ".json"))
        require(observed_outer["phase"] == label and observed_outer["orig_argv"] == outer_argv and
                observed_outer["cwd"] == str(ROOT) and observed_outer["environment"] == ENV and
                observed_outer["executable"] == "/usr/bin/python3.10" and observed_outer["sys_path"] ==
                ["/usr/lib/python310.zip", "/usr/lib/python3.10", "/usr/lib/python3.10/lib-dynload"] and
                observed_outer["cache_prefix"] == str(launch_out / "unused_outer_cache") and
                observed_outer["cache_absent"] is True and not os.path.lexists(observed_outer["cache_prefix"]),
                "entire actual outer runtime context and cache absence")
        current(observed_outer["cache_prefix"])
        for flag in ("dont_write_bytecode", "no_user_site", "no_site", "ignore_environment", "isolated"):
            require(re.search(r"(?:\(|, )" + flag + r"=1(?:,|\))", observed_outer["flags"]),
                    "actual outer isolated source-only flag")
        require("optimize=0" in observed_outer["flags"], "actual outer optimization zero")
        mapped = {str(Path(line.split(None, 5)[5]).resolve()) for line in observed_outer["maps_raw"].splitlines()
                  if len(line.split(None, 5)) == 6 and line.split(None, 5)[5].startswith("/")}
        require(mapped == set(observed_outer["mapped_files"]), "entire raw outer maps correspondence")
        observations = list(observed_outer["mapped_files"].items())
        for value in observed_outer["modules"].values():
            require(Path(value["path"]).suffix not in {".pyc", ".pyo"}, "outer actual source module not bytecode")
            observations.append((value["path"], {k: value[k] for k in ("sha256", "bytes")}))
        for name, value in observations:
            require(pin(name) == value == before.get(name), "complete actual outer observed current file")
            if phase == "BEFORE":
                require(name not in expected_before or expected_before[name] == value, "consistent early outer observation")
                expected_before[name] = value
    expected_before["/usr/bin/python3.10"] = pin("/usr/bin/python3.10")
    require(before == expected_before, "entire actual outer preflight/preparation/early-runtime input union")
    exact_pair(launch_out / "executed_launcher.py", launch_prep / "launch_p210_terminal.py")
    exact_pair(launch_out / "executed_builder.py", PREP / "build_p210.py")
    exact_pair(OUT / "executed_source.py", PREP / "build_p210.py")
    # The actual native outer has already succeeded and attested owned-group
    # closure before these immutable builder payload hashes are inspected.
    build_members = manifest(OUT, actual["build"]["sha256"], actual["build"]["payloads"])
    result = read(OUT / "RESULT.json")
    require(launch_receipt["builder_closure"] == {
            "manifest": pin(OUT / "SHA256SUMS"), "payloads": actual["build"]["payloads"],
            "result": pin(OUT / "RESULT.json"), "status": "PASS_P210_SOURCE_ONLY_BUILD_PAIR_NOT_VIEWED"},
            "actual outer closure binds complete physical builder result and seal")
    expected_root_report = dict(status=launch_receipt["status"], output=str(launch_out), builder_exit_code=0,
        launcher_seal=pin(launch_out / "SHA256SUMS"), builder_closure=launch_receipt["builder_closure"])
    require(root_report == expected_root_report and root_output == json.dumps(expected_root_report, sort_keys=True) + "\n",
            "entire actual root native output binds this exact closed outer/build pair; outer stderr not separately claimed")
    recipe = read(PREP / "INPUT_CONTRACT.json")
    require(recipe["schema"] == "p210-terminal-build-actual-bound-contract-v1" and
            recipe["stage"] == "ACTUAL_B_ROOT_DELTA_PHYSICAL_ROUND2_BOUND_NOT_EXECUTED",
            "actual final builder contract schema")
    actual_final = read(OUT / "FINAL_SCHEMA_BINDING_RETURN.json")
    bound = recipe["final_schema_binding"]
    require(actual_final == preflight_data["final_schema_binding_return"] and
            read(OUT / "ORIGINALS_BEFORE.json") == read(OUT / "ORIGINALS_AFTER.json") ==
            preflight_data["original_input_pins"], "entire actual successful preflight/build original identity")
    expected_prerequisites = {}
    require(len(bound["manifests"]) == 8 and len(bound["roles"]) == 41, "complete actual builder role census")
    for row in bound["manifests"].values():
        expected_prerequisites.update(manifest(Path(row["path"]), row["seal"]["sha256"], row["payloads"]))
    for row in bound["roles"].values():
        value = {k: row[k] for k in ("sha256", "bytes")}
        require(pin(row["path"]) == value and
                (row["path"] not in expected_prerequisites or expected_prerequisites[row["path"]] == value),
                "all actual named prerequisite keys and duplicate consistency")
        expected_prerequisites[row["path"]] = value
    require(len(expected_prerequisites) == 1594 and actual_final["required_input_pins"] == expected_prerequisites and
            actual_final["papers"] == bound["papers"] and
            actual_final["status"] == "BOUND_ACTUAL_P210_B_ROOT_ROUND2_PRETERMINAL_ORIGINALS",
            "complete actually executed final schema return; no omitted dependency roles")
    root_b = read(bound["roles"]["root_b"]["path"])
    current_b = read(bound["roles"]["b_current"]["path"])
    round2 = read(bound["roles"]["round2_reception"]["path"])
    require(root_b["schema"] == "p210-b-root-delta-closure-v1" and
            root_b["status"] == "ROOT_ACCEPTED_B_DELTA_ORIGINAL_CLOSURE_PASS" and
            root_b["reviewer_delta_accepted"] is True and root_b["root_original_inspection_complete"] is True and
            root_b["root_replay_closure_complete"] is True and root_b["current_open_findings"] == 0 and
            current_b["accepted_delta"] is True and current_b["reviewer"] == root_b["reviewer"] == "/root/p210_b_reviewer" and
            current_b["current_open_counts"] == dict(Critical=0, Major=0, Minor=0) and
            round2["status"] == "PASS_ROOT_PHYSICAL_P210_ROUND2_RECEPTION" and round2["payloads"] == 524 and
            round2["round2_manifest_sha256"] == actual_final["papers"]["P210"]["freeze_manifest"]["sha256"],
            "actual same-B/root/physical-Round2 prerequisites; not a new manuscript verdict")
    argv = ["/usr/bin/python3.10", "-I", "-S", "-B", "-X", "pycache_prefix=" + str(OUT / "unused_parent_cache"),
            str(PREP / "build_p210.py"), "--output", str(OUT), "--expected-preparation-sha256",
            actual["builder_preparation"]["sha256"]]
    require(launch_receipt["argv"] == argv and launch_receipt["stdout"] == "builder.stdout" and
            launch_receipt["stderr"] == "builder.stderr", "actual argv and physical separate stream roles")
    builder_stdout = text(launch_out / "builder.stdout")
    reported = json.loads(builder_stdout)
    require(reported == dict(status=result["status"], output=str(OUT), commands=len(result["commands"]),
            builds=result["builds"], failures=result["failures"], seal=pin(OUT / "SHA256SUMS"),
            payloads=actual["build"]["payloads"]) and len(result["commands"]) == 33,
            "complete actual builder raw stdout matches its immutable RESULT")
    return dict(preparation_sha256=actual["builder_preparation"]["sha256"], preparation_payloads=9,
        build_sha256=actual["build"]["sha256"], build_payloads=actual["build"]["payloads"],
        final_schema_binding_return=actual_final,
        actual_native=dict(argv=["/usr/bin/env", "-i", *[k + "=" + v for k, v in ENV.items()], *argv],
                           cwd=str(ROOT), exit_code=launch_receipt["original_wait_exit_code"],
                           stdout=builder_stdout, stderr=text(launch_out / "builder.stderr")))



def originals(recipe, binding):
    expected = manifest(PREP, binding["preparation_sha256"], binding["preparation_payloads"])
    final = read(OUT / "FINAL_SCHEMA_BINDING_RETURN.json")
    require(final == binding["final_schema_binding_return"] and set(final["papers"]) == {"P210"},
            "entire actually bound final return and one-paper scope")
    require(all(path not in recipe["infrastructure_pins"] or recipe["infrastructure_pins"][path] == value
                for path, value in final["required_input_pins"].items()), "no conflicting original roles")
    for path, value in {**recipe["infrastructure_pins"], **final["required_input_pins"]}.items():
        require(pin(path) == value, "actual complete prerequisite original")
        expected[path] = value
    paper = final["papers"]["P210"]
    freeze, live = Path(paper["freeze"]), Path(paper["paper"])
    require(live == PAPER and freeze == PAPER / "frozen_round2" and paper["round"] == 2,
            "actual physical P210 Round2, not Round1 or a proposed freezer")
    expected.update(manifest(freeze, paper["freeze_manifest"]["sha256"], paper["freeze_payloads"]))
    names = paper["source_names"]
    require(tuple(names) == SOURCE_NAMES and set(names) == set(paper["source_pins"]), "exact ten-source contract")
    require(paper["underfull"] == [] and paper["pages"] == 6, "exact six-page zero-Underfull baseline")
    for base in (freeze, live):
        require({str(p.relative_to(base)) for p in (base / "sections").rglob("*") if p.is_file()} ==
                {n for n in names if n.startswith("sections/")}, "exact accepted source membership")
        for name, value in {**paper["source_pins"], "main.pdf": paper["pdf_pin"]}.items():
            require(pin(base / name) == value, "actual live/frozen scientific source and PDF")
            expected[str(base / name)] = value
        main_tex = text(base / "main.tex")
        inputs = {n if n.endswith(".tex") else n + ".tex" for n in re.findall(r"\\input\{([^}]+)\}", main_tex)}
        require(inputs == set(names) - {"main.tex", "references.bib"}, "entire main input graph")
        require("\\bibliography{references}" in main_tex and "\\bibliographystyle{plainnat}" in main_tex and
                "\\author{Anonymous}" in main_tex and "pdfauthor={}" in main_tex, "exact bibliography and anonymity")
    require(read(OUT / "ORIGINALS_BEFORE.json") == read(OUT / "ORIGINALS_AFTER.json") == expected,
            "entire original pre/post key and all actual current original pins")
    return expected, final


def commands(contract):
    # Expected native sequence/argv/direct inputs; none of these commands run here.
    result = {}
    def add(label, argv, cwd, direct=(), mutable=()):
        result[label] = (list(map(str, argv)), str(cwd), {str(argv[0]), *map(str, direct)}, {str(p) for p in mutable})
    add("source_cmp", ["/usr/bin/cmp", "--", PREP / "build_p210.py", OUT / "executed_source.py"], OUT,
        [PREP / "build_p210.py", OUT / "executed_source.py"])
    elf = sorted(str(p) for p in TOOLS | set((STDLIB / "lib-dynload").glob("*.so")) if raw(p)[:4] == b"\x7fELF")
    add("ldd_before", ["/usr/bin/ldd", *elf], OUT, elf)
    for tool in ("pdflatex", "bibtex"):
        add(tool + "_version", ["/usr/bin/" + tool, "--version"], OUT)
    add("texmf_roots", ["/usr/bin/kpsewhich", "-var-value=TEXMF"], OUT)
    for ident in ("P210",):
        paper = contract["papers"][ident]
        freeze_pdf = Path(paper["freeze"]) / "main.pdf"
        add("P210_round2_pdfinfo", ["/usr/bin/pdfinfo", freeze_pdf], OUT, [freeze_pdf])
        for number in (1, 2):
            label = ident + "_cold_build_" + str(number)
            cold = OUT / ("cold_build_" + str(number))
            pdf = cold / "main.pdf"
            for variable in USER_VARS:
                add(label + "_" + variable, ["/usr/bin/kpsewhich", "-var-value=" + variable], cold)
            for n in (1, 2, 3):
                add(label + "_pass" + str(n), ["/usr/bin/pdflatex", "-no-shell-escape", "-recorder",
                    "-interaction=nonstopmode", "-halt-on-error", "main.tex"], cold,
                    [cold / name for name in paper["source_names"]], [cold / ("main." + s) for s in ("aux", "bbl", "out", "toc")])
                if n == 1:
                    add(label + "_bst", ["/usr/bin/kpsewhich", "plainnat.bst"], cold)
                    bst = Path(text(OUT / "commands" / (label + "_bst") / "stdout").strip()).resolve()
                    add(label + "_bibtex", ["/usr/bin/bibtex", "main"], cold, [cold / "main.aux", cold / "references.bib", bst])
            for tool in ("pdfinfo", "pdffonts"):
                add(label + "_" + tool, ["/usr/bin/" + tool, "main.pdf"], cold, [pdf])
            add(label + "_pdftotext", ["/usr/bin/pdftotext", "-layout", "main.pdf", OUT / (label + ".txt")], cold, [pdf])
            add(label + "_frozen_cmp", ["/usr/bin/cmp", "--", pdf, Path(paper["freeze"]) / "main.pdf"], cold,
                [pdf, Path(paper["freeze"]) / "main.pdf"])
            if number == 1:
                add(label + "_render", ["/usr/bin/pdftoppm", "-png", "-r", "105", "main.pdf", cold / "pages/page"], cold, [pdf])
        pair = [OUT / ("cold_build_" + str(n)) / "main.pdf" for n in (1, 2)]
        add(ident + "_pair_cmp", ["/usr/bin/cmp", "--", *pair], OUT, pair)
    add("ldd_after", ["/usr/bin/ldd", *elf], OUT, elf)
    return result


def native_records(result, expected):
    require(result["expected_command_count"] == len(expected) == 33 and result["expected_command_labels"] == list(expected) and
            [r["label"] for r in result["commands"]] == list(expected), "all 33 native commands, original order including actual Round2 pdfinfo")
    require({p.name for p in (OUT / "commands").iterdir()} == set(expected), "entire native command directory census")
    rows = {}
    attempt_keys = {"label", "argv", "cwd", "env", "started_epoch", "timeout_seconds", "start_new_session",
                    "exit_code", "status", "inputs_before", "generated_inputs_before"}
    for row in result["commands"]:
        label = row["label"]
        directory = OUT / "commands" / label
        attempt, receipt = read(directory / "ATTEMPT.json"), read(directory / "RECEIPT.json")
        argv, cwd, direct, mutable = expected[label]
        require(receipt == row and set(attempt) == attempt_keys, "entire original receipt/result row and attempt schema")
        require({k: v for k, v in attempt.items() if k not in {"status", "exit_code"}} ==
                {k: row[k] for k in attempt if k not in {"status", "exit_code"}}, "complete pre-spawn attempt binding")
        require(attempt["status"] == "ATTEMPTED" and attempt["exit_code"] is None and row["status"] == "COMPLETED" and
                row["exit_code"] == 0 and row["error"] is None and row["streams_settled"] is True and "cleanup" not in row,
                "real settled native success, no cleanup/failure hidden")
        require(row["argv"] == argv and row["cwd"] == cwd and row["env"] == ENV and row["timeout_seconds"] == 600 and
                row["start_new_session"] is True and isinstance(row["pid"], int) and row["pid"] > 0 and
                row["ended_epoch"] >= row["started_epoch"], "complete argv/env/cwd/process/time metadata")
        require(set(row["inputs_before"]) == direct and row["inputs_before"] == row["inputs_after"] and
                set(row["generated_inputs_before"]) == set(row["generated_inputs_after"]) == mutable, "complete direct and generated input keys")
        for path, value in row["inputs_before"].items():
            # Only the exact BibTeX .aux input role was later overwritten.
            archived = OUT / (label[:-7] + "_pass1.aux") if label.endswith("_bibtex") and path == str(Path(cwd) / "main.aux") else Path(path)
            require(pin(archived) == value, "exact immutable native input or saved BibTeX-aux role")
        require(set(row["streams"]) == {"stdout", "stderr"}, "both complete native stream pins")
        for stream in ("stdout", "stderr"):
            require(digest_bytes(raw(directory / stream)) == row["streams"][stream], "entire raw native stream")
        if argv[0] == "/usr/bin/cmp":
            require(raw(directory / "stdout") == raw(directory / "stderr") == b"", "original cmp empty success streams")
            exact_pair(argv[2], argv[3])
        require({p.name for p in directory.iterdir()} == {"ATTEMPT.json", "RECEIPT.json", "stdout", "stderr"}, "closed native record directory")
        rows[label] = row
    return rows


def build(label, paper, rows, known):
    match = re.fullmatch(r"P210_cold_build_([12])", label)
    require(match is not None, "exact P210 command label, separate from physical directory")
    cold = OUT / ("cold_build_" + match.group(1))
    initial = read(OUT / (label + "_SOURCE_ONLY_INITIAL.json"))
    require(initial == paper["source_pins"], "exact source-only initial ledger; no PDF/aux/bbl input")
    for name, value in initial.items():
        require(pin(cold / name) == value, "all final copied scientific sources unchanged")
    consumed = {}
    previous = None
    historical_out = []
    for n in (1, 2, 3):
        stem = label + "_pass" + str(n)
        row = rows[stem]
        before, after = row["generated_inputs_before"], row["generated_inputs_after"]
        for path in before:
            suffix = Path(path).suffix
            for moment, record in (("before", before[path]), ("after", after[path])):
                base = dict(exists=record["is_file"], symlink=False, link=None, resolved=path, is_file=record["is_file"], is_dir=False)
                require(record == {**base, **({k: record[k] for k in ("sha256", "bytes")} if record["is_file"] else {})}, "entire original auxiliary state schema")
                if record["is_file"]:
                    value = {k: record[k] for k in ("sha256", "bytes")}
                    if suffix == ".aux":
                        saved_pass = n if moment == "after" else n - 1
                        require(saved_pass >= 1 and pin(OUT / (label + "_pass%d.aux" % saved_pass)) == value, "physical exact per-pass auxiliary input/output")
                    elif suffix == ".bbl":
                        require(pin(OUT / (label + ".bbl")) == value, "physical bibliography product")
                    elif suffix == ".out" and value != pin(cold / "main.out"):
                        require((n, moment) in {(1, "after"), (2, "before")}, "only exact first-pass historical bookmark role")
                        historical_out.append(dict(command=stem, moment=moment, path=path, **value))
                    else:
                        require(pin(path) == value, "unchanged or final auxiliary product")
            if n == 1:
                require(before[path]["exists"] is False, "no generated input in cold first pass")
            elif suffix == ".bbl" and n == 2:
                require(before[path]["is_file"] and before[path] == after[path], "BibTeX inserts unchanged bbl between passes")
            else:
                require(before[path] == previous[path], "complete successive auxiliary state chain")
        previous = after
        observed = read(OUT / (stem + "_INPUTS.json"))
        require(set(observed) == {"local", "external"}, "entire per-pass recorder ledger")
        expected = {"local": {}, "external": {}}
        # Original recorder ledger stores unique resolved INPUT paths at the end
        # of this pass; duplicate raw lines remain physically bound in the .fls.
        for line in text(OUT / (stem + ".fls")).splitlines():
            if not line.startswith("INPUT "):
                continue
            path = Path(line[6:])
            path = (path if path.is_absolute() else cold / path).resolve()
            if path.is_relative_to(cold):
                name = str(path.relative_to(cold))
                if name in initial:
                    value = initial[name]
                else:
                    require(path.suffix in {".aux", ".bbl", ".out", ".toc"} and str(path) in after and after[str(path)]["is_file"], "exact local generated FLS role")
                    value = {k: after[str(path)][k] for k in ("sha256", "bytes")}
                expected["local"][str(path)] = value
            else:
                require(str(path) in known, "every observed external TeX input already known")
                value = pin(path)
                require(value == known[str(path)], "exact external TeX input")
                expected["external"][str(path)] = value
                consumed[str(path)] = value
        require(expected == observed, "complete raw FLS-to-ledger correspondence")
        require("Output written on main.pdf" in text(OUT / (stem + ".log")), "physical complete engine pass log")
    for suffix in ("aux", "fls", "log"):
        exact_pair(cold / ("main." + suffix), OUT / (label + "_pass3." + suffix))
    for suffix in ("bbl", "blg"):
        exact_pair(cold / ("main." + suffix), OUT / (label + "." + suffix))
    require(re.search(r"(?im)Warning--|I couldn't open|There (?:was|were) [1-9][0-9]* error messages?",
                      text(OUT / (label + ".blg"))) is None, "complete bibliography log without warnings/errors")
    bst = str(Path(text(OUT / "commands" / (label + "_bst") / "stdout").strip()).resolve())
    require(pin(bst) == known[bst], "exact recorded bibliography-style input")
    consumed[bst] = pin(bst)
    metadata = text(OUT / "commands" / (label + "_pdfinfo") / "stdout")
    fonts = text(OUT / "commands" / (label + "_pdffonts") / "stdout")
    font_rows = [line.split()[-5:] for line in fonts.splitlines()[2:] if line.strip()]
    require(font_rows and all(len(row) == 5 and row[0] == "yes" for row in font_rows), "all complete font records embedded")
    pages = int(re.search(r"^Pages:\s+(\d+)$", metadata, re.M)[1])
    require(pages == paper["pages"] and pin(cold / "main.pdf") == paper["pdf_pin"] and
            int(re.search(r"^File size:\s+(\d+) bytes$", metadata, re.M)[1]) == paper["pdf_pin"]["bytes"] and
            re.search(r"^Author:[ \t]*$", metadata, re.M), "full metadata/PDF bytes/anonymous author")
    log = text(cold / "main.log")
    diagnostics = {name: re.findall(pattern, log, re.M) for name, pattern in dict(undefined=r"^.*undefined.*$",
        overfull=r"^.*Overfull.*$", underfull=r"^.*Underfull.*$", warnings=r"^.*Warning.*$",
        rerun=r"^.*(?:Rerun to|Please .*rerun|Label\(s\) may have changed).*$").items()}
    require(diagnostics["underfull"] == paper["underfull"] and all(not v for k, v in diagnostics.items() if k != "underfull"), "exact allowed final diagnostics")
    extracted = text(OUT / (label + ".txt"))
    require(not any(x in extracted for x in ("[VERIFY]", "??", "[?]")), "complete extracted text")
    text_pages = extracted.split("\f")
    if text_pages and not text_pages[-1].strip():
        text_pages.pop()
    require(len(text_pages) == pages == 6, "actual complete PDF/text six-page agreement")
    bibliography_pages = [i + 1 for i, page_text in enumerate(text_pages)
                          if re.search(r"^\s*(?:References|Bibliography)\s*$", page_text, re.M)]
    require(bibliography_pages, "actual reference heading pages, not inferred venue compliance")
    frozen_metadata = text(OUT / "commands/P210_round2_pdfinfo/stdout")
    round2_pages = int(re.search(r"^Pages:\s+(\d+)$", frozen_metadata, re.M)[1])
    require(round2_pages == pages and int(re.search(r"^File size:\s+(\d+) bytes$", frozen_metadata, re.M)[1]) ==
            paper["pdf_pin"]["bytes"], "actual native Round2 six-page and file-byte baseline")
    expected_measured = dict(label=label, pages=pages, pdf=pin(cold / "main.pdf"), fonts=len(font_rows),
                            diagnostics=diagnostics, source_count=len(initial), visual_review="NOT_VIEWED",
                            reference_heading_pages=bibliography_pages, round2_measured_pages=round2_pages,
                            venue_page_limit=None, bibtex_warnings_or_errors=[])
    require(read(OUT / (label + "_MEASURED.json")) == expected_measured, "exact measured build result")
    products = {"main." + s for s in ("aux", "bbl", "blg", "fls", "log", "out", "pdf")}
    rendered = {"pages/page-%d.png" % n for n in range(1, pages + 1)} if label.endswith("_1") else set()
    require({str(p.relative_to(cold)) for p in cold.rglob("*") if p.is_file()} == set(initial) | products | rendered, "complete final cold directory, no unexpected inputs/products")
    for name in rendered:
        require(raw(cold / name).startswith(b"\x89PNG\r\n\x1a\n"), "rendered PNG binding, not new viewing")
    return expected_measured, consumed, historical_out


def runtime(phase, known, original, argv):
    row = read(OUT / ("PARENT_RUNTIME_" + phase + ".json"))
    require(row["argv"] == argv and row["cwd"] == str(ROOT) and row["env"] == ENV and row["sys_path"] ==
            ["/usr/lib/python310.zip", "/usr/lib/python3.10", "/usr/lib/python3.10/lib-dynload"], "entire recorded isolated parent context")
    require(row["phase"] == ("before_first_child" if phase == "BEFORE" else "after_last_child_and_inventory"), "actual runtime sample phase")
    for flag in ("dont_write_bytecode", "no_user_site", "no_site", "ignore_environment", "isolated"):
        require(re.search(r"(?:\(|, )" + flag + r"=1(?:,|\))", row["flags"]), "isolated recorded parent flags")
    require("optimize=0" in row["flags"] and row["cache_absent"] is True and row["cache_prefix"] == str(OUT / "unused_parent_cache") and
            not os.path.lexists(row["cache_prefix"]), "absent exact parent bytecode prefix")
    body = row["maps_raw"].encode()
    require(digest_bytes(body) == dict(bytes=row["maps_bytes"], sha256=row["maps_sha256"]), "entire raw original maps")
    mapped = {str(Path(line.split(None, 5)[5]).resolve()) for line in row["maps_raw"].splitlines()
              if len(line.split(None, 5)) == 6 and line.split(None, 5)[5].startswith("/")}
    require(mapped == set(row["mapped_files"]), "complete raw-map-to-file key")
    allowed = {**known, **original}
    for path, value in row["mapped_files"].items():
        require(pin(path) == value == allowed[path], "all observed mapped parent files")
    for name, value in row["modules"].items():
        path = value["path"]
        require(Path(path).suffix not in {".pyc", ".pyo"} and not {"site-packages", "dist-packages"}.intersection(Path(path).parts), "observed source-only modules")
        require({k: value[k] for k in ("sha256", "bytes")} == pin(path) == allowed[path], "every observed parent module")
    return dict(phase=phase, modules=len(row["modules"]), mapped=len(mapped))


def main():
    require(len(sys.argv) == 1 and sys.flags.isolated and sys.flags.no_site and sys.flags.dont_write_bytecode, "read-only isolated invocation with no arguments")
    binding = final_schema_binding()
    for path, expected in read(HERE / "INPUT_PINS.json")["pins"].items():
        require(pin(path) == expected, "preparation direct input binding")
    manifest(OUT, binding["build_sha256"], binding["build_payloads"])
    recipe = read(PREP / "INPUT_CONTRACT.json")
    original, contract = originals(recipe, binding)
    result = read(OUT / "RESULT.json")
    require(result["status"] == "PASS_P210_SOURCE_ONLY_BUILD_PAIR_NOT_VIEWED" and result["failures"] == [] and
            result["new_mathematical_executions"] == 0 and result["external"] == "OWNER_AMBER / HOLD_EXTERNAL" and
            result["visual_review"] == "NOT_VIEWED_ROOT_ACTUAL_PAGE_INSPECTION_REQUIRED" and
            result["paper_completion"] is False and result["five_paper_completion"] is False, "exact original completion scope")
    before, before_raw = ledger("KNOWN_INPUTS_BEFORE")
    after, after_raw = ledger("KNOWN_INPUTS_AFTER")
    require(before == after and before_raw == after_raw and set(before) == {"configuration", "runtime", "tex"},
            "entire original lossless pre/post ledger; counts derived from exact current bounded membership")
    known_membership(before)
    known = {}
    for group in before.values():
        for path, value in group.items():
            require(current(path) == value, "exact current original path/presence/link/bytes")
            if value["is_file"]:
                simple = {k: value[k] for k in ("sha256", "bytes")}
                require(value["resolved"] not in known or known[value["resolved"]] == simple, "consistent aliased known coverage")
                known[value["resolved"]] = simple
    rows = native_records(result, commands(contract))
    measured, consumed, bookmark_roles = [], {}, []
    user_roots = read(OUT / "USER_ROOTS.json")
    require(len(user_roots) == 6, "all six user TeX root queries")
    for ident in ("P210",):
        for n in (1, 2):
            label = ident + "_cold_build_" + str(n)
            value, external, historical = build(label, contract["papers"][ident], rows, known)
            measured.append(value); consumed.update(external); bookmark_roles.extend(historical)
            for variable in USER_VARS:
                raw_query = text(OUT / "commands" / (label + "_" + variable) / "stdout").strip()
                query = Path(raw_query)
                resolved = (query if query.is_absolute() else OUT / ("cold_build_" + str(n)) / query).resolve()
                require(user_roots[label + ":" + variable] == dict(query=raw_query, resolved=str(resolved), absent=True) and
                        not os.path.lexists(resolved), "every original user-root absence and query binding")
                current(resolved)
    require(measured == result["builds"] and read(OUT / "CONSUMED_TEX_BEFORE.json") ==
            read(OUT / "CONSUMED_TEX_AFTER.json") == consumed, "all measured results and complete actual consumed-TeX union")
    libraries = []
    for phase in ("BEFORE", "AFTER"):
        body = text(OUT / "commands" / ("ldd_" + phase.lower()) / "stdout")
        require("not found" not in body, "full ldd output has no unresolved dependency")
        paths = {str(Path(p).resolve()) for p in re.findall(r"(/[^\s():]+)", body)}
        record = read(OUT / ("LIBRARIES_" + phase + ".json"))
        require(paths == set(record), "all ldd headers/resolved-library paths")
        for path, value in record.items():
            require(pin(path) == value == known[path], "entire original linked-library closure")
        libraries.append(record)
    require(libraries[0] == libraries[1], "complete original link-time pre/post closure")
    argv = ["/usr/bin/python3.10", "-I", "-S", "-B", "-X", "pycache_prefix=" + str(OUT / "unused_parent_cache"),
            str(PREP / "build_p210.py"), "--output", str(OUT), "--expected-preparation-sha256", binding["preparation_sha256"]]
    observed = [runtime(phase, known, original, argv) for phase in ("BEFORE", "AFTER")]
    expected_stdout = dict(status=result["status"], output=str(OUT), commands=33, builds=measured, failures=[],
                           seal=pin(OUT / "SHA256SUMS"), payloads=binding["build_payloads"])
    expected_native = dict(argv=["/usr/bin/env", "-i", *[k + "=" + v for k, v in ENV.items()], *argv],
                           cwd=str(ROOT), exit_code=0, stdout=json.dumps(expected_stdout, sort_keys=True) + "\n", stderr="")
    require(binding["actual_native"] == expected_native,
            "entire actual outer native normalized context/exit/raw streams, derived by exact-schema gate")
    require(text(OUT / "commands/texmf_roots/stdout") == "{{}./.texlive2021/texmf-config,./.texlive2021/texmf-var,./texmf,!!/usr/local/share/texmf,/etc/texmf,!!/var/lib/texmf,!!/usr/share/texmf,!!/usr/share/texlive/texmf-dist}\n", "exact native TeX search-root configuration")
    # No generated broad ledger is written: the original ledgers remain controlling.
    keys = sorted(CURRENT)
    for path in keys:
        require(fresh_entry(path) == CURRENT[path], "final uncached current path/presence/link/bytes reread")
    known_membership(before)
    require(len(physical(OUT)) == binding["build_payloads"], "original output membership unchanged")
    require(sorted(CURRENT) == keys, "no unreported current key added after final uncached rereads")
    known_original_paths = {}
    for group in before.values():
        for path, value in group.items():
            require(path not in known_original_paths or known_original_paths[path] == value,
                    "consistent duplicate original spelling across known ledger groups")
            known_original_paths[path] = value
    extra = {path: CURRENT[path] for path in keys if path not in known_original_paths}
    require({**known_original_paths, **extra} == CURRENT and not set(known_original_paths).intersection(extra),
            "complete disjoint original-spelling known union plus rich current extras")
    complete_raw = json.dumps(CURRENT, sort_keys=True, separators=(",", ":")).encode("utf-8")
    reconstruction = dict(known_ledger=str(OUT / "KNOWN_INPUTS_BEFORE.json.gz"),
        known_ledger_pin=pin(OUT / "KNOWN_INPUTS_BEFORE.json.gz"), known_original_paths=len(known_original_paths),
        merge_rule="Union all three original ledger groups by original path spelling with exact duplicate equality, then disjoint extra_entries; no resolved-path substitution.",
        canonical_encoding="json.dumps(complete_map, sort_keys=True, separators=(',', ':')).encode('utf-8'); ensure_ascii=True; no terminal LF",
        extra_entries=extra, extra_count=len(extra), complete_entries=len(CURRENT), complete_map=digest_bytes(complete_raw))
    print(json.dumps(dict(status="PASS_P210_TERMINAL_BUILD_ORIGINAL_DOCUMENTS_ONLY", preparer="/root/p210_checkpoint_planner; author, not reviewer",
        checks=CHECKS, original_payloads=binding["build_payloads"], original_commands=33, original_builds=measured,
        current_path_keys=len(keys), current_path_keys_sha256=hashlib.sha256(json.dumps(keys, separators=(",", ":")).encode()).hexdigest(),
        current_key_reconstruction=reconstruction,
        gzip_groups={k: len(v) for k, v in before.items()}, original_inputs=len(original), consumed_tex=len(consumed),
        linked_files=len(libraries[0]), parent_runtime_samples=observed, raw_documentary_pairs=RAW_PAIRS,
        historical_first_pass_bookmark_hash_roles=bookmark_roles, build_seal=binding["build_sha256"],
        new_science_executions=0, new_builds=0, new_views=0, manuscript_reviews=0, root_acceptance=False,
        limitations=["Author-prepared documentary adapter; root owns source inspection, execution and acceptance.",
            "Six root page views are explicitly outside this inspector; rendered PNGs are not visual review.",
            "Historical first-pass .out files have complete native before/after chain roles, not separate physical old-byte snapshots.",
            "Original bounded known-path/FLS/link-time/parent-map scope is not child-map, transient dlopen, non-FLS or continuous OS/startup tracing.",
            "The actual outer02 native command/completion and separate builder streams are bound; the root tool envelope does not supply a separate outer-stderr file."]
    ), sort_keys=True))


if __name__ == "__main__":
    main()
