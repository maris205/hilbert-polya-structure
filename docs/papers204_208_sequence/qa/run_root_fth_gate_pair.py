"""Prepared root-only FTH replay adapter; execution creates a NEW evidence directory.

No mathematical implementation is imported here. The sealed original kernel and
bootstrap are copied byte-for-byte; ROOT_ENTRY adds actual child invocation data.
This is observed dependency closure, not an OS-hermetic syscall trace. See the
adjacent root_fth_gate_pair_preparation/PREPARATION.md before root execution.
"""
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import sysconfig
import time
import traceback

SCRIPT = Path(__file__).resolve()
QA = SCRIPT.parent
ROOT = QA.parents[2]
GATE = QA.parent / "scouting/FTH_GATE"
PREPARATION = QA / "root_fth_gate_pair_preparation/PREPARATION.md"
ROOT_INSPECTION = QA / "FTH_GATE_ROOT_ORIGINAL_INSPECTION.actual.json"
ENV = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8", "TZ": "UTC"}
SEAL_SHA = "6989fad02d78655482d50a1eb18e6e099b44e016f1cec4478e7e94e88a483940"
KERNEL_SHA = "d172db91901a2d087ed96cadb8e6a38690330cce414b117f07a0e769910c5107"
BOOTSTRAP_SHA = "c2d418d9b5f6fa4c96795aa42dced529e3a78447c06bfff932fd789f27a269ef"
ROOT_ENTRY = '''"""Invocation-only wrapper; sealed bootstrap executes the sealed kernel."""
import json
import os
from pathlib import Path
import sys
base = Path(__file__).resolve().parent
def record(label):
    value = {"argv": sys.argv, "orig_argv": sys.orig_argv,
             "cwd": os.getcwd(), "env": dict(os.environ),
             "executable": sys.executable, "flags": str(sys.flags),
             "optimize": sys.flags.optimize, "isolated": sys.flags.isolated,
             "no_site": sys.flags.no_site,
             "dont_write_bytecode": sys.flags.dont_write_bytecode,
             "pycache_prefix": sys.pycache_prefix,
             "cache_exists": bool(sys.pycache_prefix and Path(sys.pycache_prefix).exists())}
    with (base.parent / ("child.invocation." + label + ".json")).open("x") as output:
        json.dump(value, output, indent=2, sort_keys=True)
        output.write("\\n")
record("before")
try:
    bootstrap = base / "bootstrap.py"
    exec(compile(bootstrap.read_bytes(), str(bootstrap), "exec"),
         {"__name__": "__main__", "__file__": str(bootstrap)})
finally:
    record("after")
'''
OPENED = set()


def audit(event, args):
    if event == "open" and isinstance(args[0], (str, bytes)):
        path = os.path.abspath(os.fsdecode(args[0]))
        if os.path.isfile(path) and not path.startswith("/proc/"):
            OPENED.add(path)


sys.addaudithook(audit)


def sha(path):
    with Path(path).open("rb") as source:
        return hashlib.file_digest(source, "sha256").hexdigest()


def save(path, value):
    with Path(path).open("x", encoding="utf-8") as output:
        json.dump(value, output, indent=2, sort_keys=True)
        output.write("\n")


def snapshot(paths):
    result = {}
    for raw in sorted(set(map(str, paths))):
        p = Path(raw)
        try:
            result[raw] = {"sha256": sha(p), "bytes": p.stat().st_size,
                           "resolved": str(p.resolve()),
                           "symlink": os.readlink(p) if p.is_symlink() else None}
        except Exception as error:
            result[raw] = {"error": repr(error)}
    return result


def observation():
    modules = {name: {"file": getattr(module, "__file__", None),
                      "origin": getattr(getattr(module, "__spec__", None), "origin", None)}
               for name, module in sorted(sys.modules.items())}
    maps = Path("/proc/self/maps").read_text()
    mapped = sorted({line.split()[-1] for line in maps.splitlines()
                     if "/" in line and Path(line.split()[-1]).is_file()})
    return {"modules": modules, "mapped_files": mapped, "maps": maps,
            "opened_existing_files": sorted(OPENED), "argv": sys.argv,
            "orig_argv": sys.orig_argv, "cwd": os.getcwd(), "env": dict(os.environ),
            "executable": sys.executable, "sys_path": sys.path, "flags": str(sys.flags),
            "optimization": sys.flags.optimize, "pycache_prefix": sys.pycache_prefix}


def consumed(obs):
    paths = set(obs.get("mapped_files", [])) | set(obs.get("opened_existing_files", []))
    for module in obs.get("modules", {}).values():
        for key in ("file", "origin"):
            value = module.get(key)
            if value and Path(value).is_file():
                paths.add(value)
    return {str(Path(p).resolve()) for p in paths if not p.startswith("/proc/")}


def path_closure(used, before, out):
    covered = {item.get("resolved") for item in before.values()}
    produced = sorted(p for p in used - covered if Path(p).is_relative_to(out)
                      and Path(p).suffix in {".json", ".stdout", ".stderr"})
    return {"observed_consumed_files": sorted(used),
            "observed_generated_receipt_reads": produced,
            "uncovered": sorted(used - covered - set(produced)),
            "bytecode": sorted(p for p in used if p.endswith((".pyc", ".pyo")))}


def presence(optional, directories):
    return {"optional": {str(p): p.exists() for p in optional},
            "directories": {str(d): sorted(str(p) for p in d.rglob("*") if p.is_file())
                            if d.is_dir() else None for d in directories}}


def is_elf(path):
    with path.open("rb") as source:
        return source.read(4) == b"\x7fELF"


def command(argv, folder, tag):
    receipt = {"argv": argv, "cwd": str(folder), "env": ENV,
               "started_epoch": time.time(), "exit": None, "spawn_error": None,
               "stdout": tag + ".stdout", "stderr": tag + ".stderr",
               "parent_actual_env": dict(os.environ), "process_outcome": "NOT_STARTED"}
    # An independently preserved physical attempt precedes opening logs or spawn.
    save(folder / (tag + ".attempt.json"), {**receipt, "record_kind": "PRE_SPAWN_ATTEMPT"})
    try:
        with (folder / receipt["stdout"]).open("xb") as out, (folder / receipt["stderr"]).open("xb") as err:
            if dict(os.environ) != ENV or any(name in os.environ for name in ("BASH_ENV", "ENV")):
                raise OSError("ACTUAL_PARENT_MINIMAL_ENV_OR_BASH_STARTUP_ENV_GUARD_FAILED")
            receipt["process_outcome"] = "UNKNOWN_OUTCOME_NO_COMPLETED_CHILD_RESULT"
            receipt["exit"] = subprocess.run(argv, cwd=folder, env=ENV,
                stdout=out, stderr=err, check=False).returncode
            receipt["process_outcome"] = "COMPLETED"
    except OSError as error:
        receipt["process_outcome"] = "NOT_STARTED"
        receipt["spawn_error"] = repr(error)
    except BaseException as error:
        receipt["spawn_error"] = repr(error)
    finally:
        receipt["finished_epoch"] = time.time()
        save(folder / (tag + ".command.json"), receipt)
    return receipt


def manifest(path, base):
    result = {}
    for line in path.read_text().splitlines():
        digest, relative = line.split("  ", 1)
        p = Path(relative)
        if not re.fullmatch(r"[0-9a-f]{64}", digest) or p.is_absolute() or ".." in p.parts:
            raise ValueError(("UNSAFE_MANIFEST", str(path), line))
        key = str(base / p)
        if key in result:
            raise ValueError(("DUPLICATE_MANIFEST_PATH", key))
        result[key] = digest
    return result


def sealed_inputs():
    if sha(GATE / "SHA256SUMS") != SEAL_SHA:
        raise RuntimeError("GATE_SEAL_DIGEST_CHANGED")
    gate = manifest(GATE / "SHA256SUMS", GATE)
    names = sorted(str(p.relative_to(GATE)) for p in GATE.rglob("*")
                   if p.is_file() and p != GATE / "SHA256SUMS")
    if len(gate) != 1053 or names != sorted(str(Path(p).relative_to(GATE)) for p in gate):
        raise RuntimeError("GATE_COMPLETE_NONSELF_COVERAGE_FAILED")
    groups = {"gate_payloads": gate, "gate_seal": {str(GATE / "SHA256SUMS"): SEAL_SHA},
              "reviewed_originals": manifest(GATE / "INPUT_PINS.sha256", ROOT),
              "supplement_originals": manifest(GATE / "SUPPLEMENT_INPUTS.sha256", ROOT)}
    for label in ("before", "after"):
        groups["history_" + label] = json.loads((GATE / ("history_discovery/" + label + ".json")).read_text())
    for run in ("replay_01", "replay_02"):
        for kind in ("science", "runtime"):
            for label in ("before", "after"):
                key = run + "/" + kind + "." + label + ".json"
                groups[key] = json.loads((GATE / key).read_text())
    expected = {}
    for group, pins in groups.items():
        for path, digest in pins.items():
            if path in expected and expected[path] != digest:
                raise RuntimeError(("CONTRADICTORY_SEALED_PINS", group, path))
            expected[path] = digest
    return groups, expected


def runtime_inventory(folder, expected, failures):
    standard = Path(sysconfig.get_path("stdlib"))
    paths = {Path(p) for p in expected if not p.startswith(str(ROOT))
             and (p.startswith("/usr/") or p.startswith("/etc/") or p.startswith("/root/miniconda3/"))}
    paths.update(map(Path, (sys.executable, "/usr/bin/cmp", "/usr/bin/ldd", "/bin/bash", "/bin/sh")))
    parent = observation()
    parent["opened_existing_files"] = []  # Scientific hash reads are not runtime imports.
    paths.update(Path(p) for p in consumed(parent) if p != str(SCRIPT))
    for directory, folders, files in os.walk(standard):
        folders[:] = [n for n in folders if n not in {"site-packages", "dist-packages", "__pycache__"}]
        paths.update(Path(directory, n) for n in files if Path(n).suffix in {".py", ".so"})
    optional = [Path(p) for p in (sysconfig.get_makefile_filename(), sysconfig.get_config_h_filename(),
        "/etc/ld.so.cache", "/etc/ld.so.conf", "/etc/ld.so.preload", "/etc/nsswitch.conf", "/etc/localtime",
        "/usr/lib/locale/locale-archive", "/etc/bash.bashrc", "/etc/profile")]
    optional += [standard.parent / ("python%d%d.zip" % sys.version_info[:2]),
                 Path(sys.executable).resolve().parent / "pyvenv.cfg",
                 Path(sys.executable).resolve().parent.parent / "pyvenv.cfg"]
    executable = Path(sys.executable).resolve()
    pth_names = {"python._pth", "python3._pth", "python%d%d._pth" % sys.version_info[:2],
                 "python%d.%d._pth" % sys.version_info[:2], executable.name + "._pth"}
    for directory in {executable.parent, Path(sys.executable).parent, standard.parent}:
        optional += [directory / name for name in sorted(pth_names)]
    for key in ("LDLIBRARY", "INSTSONAME"):
        library = sysconfig.get_config_var(key)
        if library:
            optional.append(standard.parent / (library + "._pth"))
    directories = list(map(Path, ("/etc/ld.so.conf.d", "/usr/lib/locale/C.utf8", "/etc/profile.d")))
    gconv = sorted(Path("/usr/lib").glob("*/gconv")) + [Path("/usr/lib/gconv")]
    for directory in gconv:
        optional += [directory / "gconv-modules", directory / "gconv-modules.cache"]
        directories.append(directory / "gconv-modules.d")
    paths.update(p for p in optional if p.is_file())
    for directory in directories:
        if directory.is_dir():
            paths.update(p for p in directory.rglob("*") if p.is_file())
    ldd_text = Path("/usr/bin/ldd").read_text()
    shebang = ldd_text.splitlines()[0]
    if shebang != "#!/bin/bash":
        raise RuntimeError(("UNREVIEWED_LDD_INTERPRETER", shebang))
    rtld_match = re.search(r'^RTLDLIST="([^"]+)"', ldd_text, re.MULTILINE)
    if not rtld_match:
        raise RuntimeError("UNREVIEWED_LDD_RTLDLIST")
    optional += list(map(Path, rtld_match.group(1).split()))
    paths.update(p for p in optional if p.is_file())
    before = snapshot(paths)
    save(folder / "runtime.before_ldd.json", before)
    save(folder / "runtime.presence.before.json", presence(optional, directories))
    save(folder / "config.json", {"sysconfig_paths": sysconfig.get_paths(),
        "sysconfig_vars": sysconfig.get_config_vars(), "actual_env": dict(os.environ),
        "ldd_shebang": shebang, "ldd_rtld_candidates": rtld_match.group(1).split(),
        "optional_absent": sorted(str(p) for p in optional if not p.exists()),
        "config_directories": {str(p): p.exists() for p in directories},
        "bash_mode": "ldd uses noninteractive, non-login /bin/bash; ENV/BASH_ENV unset"})
    queue = [p for p in sorted(paths) if is_elf(p)]
    processed, links = set(), []
    ldd_dir = folder / "ldd"
    ldd_dir.mkdir()
    initial_resolved = {value.get("resolved") for value in before.values()}
    while queue:
        p = queue.pop(0).resolve()
        if p in processed:
            continue
        processed.add(p)
        tag = "link_" + str(len(processed)).zfill(3)
        receipt = command(["/usr/bin/ldd", str(p)], ldd_dir, tag)
        output = (ldd_dir / (tag + ".stdout")).read_text(errors="replace")
        errors = (ldd_dir / (tag + ".stderr")).read_text(errors="replace")
        if receipt["spawn_error"] or (receipt["exit"] != 0 and "statically linked" not in output + errors):
            failures.append({"stage": "ldd", "target": str(p), "receipt": receipt})
        if "not found" in output + errors:
            failures.append({"stage": "ldd_unresolved", "target": str(p)})
        dependencies = {Path(match).resolve() for match in re.findall(r"/[^\s()]+", output)
                        if Path(match).is_file()}
        unseen = sorted(str(p) for p in dependencies if str(p) not in initial_resolved)
        if unseen:
            failures.append({"stage": "ldd_dependency_not_pinned_before_first_use", "paths": unseen})
        links.append({"target": str(p), "dependencies": sorted(map(str, dependencies)), "receipt": tag + ".command.json"})
        paths.update(dependencies)
        queue.extend(sorted(dependencies - processed))
    save(folder / "ldd.index.json", links)
    after = snapshot(before)
    save(folder / "runtime.after_ldd.json", after)
    if before != after or any("error" in item for item in before.values()):
        failures.append({"stage": "runtime_ldd_before_after"})
    return paths, optional, directories


def safe(stage, failures, function):
    try:
        return function()
    except BaseException as error:
        failures.append({"stage": stage, "error": repr(error), "traceback": traceback.format_exc()})
        return None


def one_run(folder, pinned_paths, failures):
    folder.mkdir()
    inputs = folder / "source_inputs"
    inputs.mkdir()
    shutil.copyfile(GATE / "pre_author_code/kernel_v0.py", inputs / "kernel_v0.py")
    shutil.copyfile(GATE / "bootstrap.py", inputs / "bootstrap.py")
    with (inputs / "root_entry.py").open("x") as output:
        output.write(ROOT_ENTRY)
    if sha(inputs / "kernel_v0.py") != KERNEL_SHA or sha(inputs / "bootstrap.py") != BOOTSTRAP_SHA:
        raise RuntimeError("SOURCE_COPY_DIGEST_MISMATCH")
    scientific = list(inputs.iterdir())
    if sorted(p.name for p in scientific) != ["bootstrap.py", "kernel_v0.py", "root_entry.py"]:
        raise RuntimeError("NOT_CODE_ONLY")
    pinned_paths.update(map(str, scientific))
    before = snapshot(pinned_paths)
    save(folder / "inputs.before.json", before)
    parent_before = observation()
    save(folder / "parent.before.json", parent_before)
    cache = folder / "never_created_child_cache"
    argv = [str(Path(sys.executable).resolve()), "-I", "-S", "-B", "-X",
            "pycache_prefix=" + str(cache), str(inputs / "root_entry.py")]
    local = []
    try:
        if cache.exists():
            raise RuntimeError("CHILD_CACHE_NOT_FRESH")
        receipt = command(argv, folder, "producer")
        if receipt["exit"] != 0 or receipt["spawn_error"]:
            local.append({"stage": "producer", "receipt": receipt})
    except BaseException as error:
        local.append({"stage": "producer_exception", "error": repr(error)})
    finally:
        after = safe("run_input_closure", local, lambda: snapshot(before))
        safe("write_run_input_closure", local, lambda: save(folder / "inputs.after.json", after))
        if before != after or any("error" in value for value in before.values()):
            local.append({"stage": "run_input_before_after"})
        parent_after = safe("parent_observation", local, observation)
        safe("write_parent_observation", local, lambda: save(folder / "parent.after.json", parent_after))
        child = safe("child_observation", local, lambda: json.loads((folder / "child.observed.json").read_text()))
        for label in ("before", "after"):
            invocation = safe("child_invocation_" + label, local,
                lambda label=label: json.loads((folder / ("child.invocation." + label + ".json")).read_text()))
            if invocation is not None and not (invocation["env"] == ENV and invocation["cwd"] == str(folder)
                and invocation["orig_argv"] == argv and invocation["optimize"] == 0
                and invocation["isolated"] and invocation["no_site"] and invocation["dont_write_bytecode"]
                and invocation["pycache_prefix"] == str(cache) and not invocation["cache_exists"]):
                local.append({"stage": "child_invocation_settings_" + label})
        used = set().union(*(consumed(obs) for obs in (parent_before, parent_after, child) if obs))
        closure = path_closure(used, before, folder.parent)
        if closure["uncovered"] or closure["bytecode"] or cache.exists():
            local.append({"stage": "consumed_path_closure", **closure, "cache_exists": cache.exists()})
        result = {"status": "PASS" if not local else "FAIL_PRESERVED", "failures": local,
            **closure, "source_inputs_before": {str(p): before[str(p)] for p in scientific},
            "input_files": len(before), "source_only_initial_names": sorted(p.name for p in scientific)}
        safe("write_run_receipt", local, lambda: save(folder / "RECEIPT.json", result))
        failures.extend({"run": folder.name, **item} for item in local)
    return result


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: run_root_fth_gate_pair.py ABSOLUTE_NEW_QA_OUTPUT_DIR")
    out = Path(sys.argv[1])
    if not out.is_absolute() or out.parent != QA or out.exists() or out.is_symlink():
        raise SystemExit("Output must be a previously nonexistent direct child of qa; nothing overwritten")
    out.mkdir(mode=0o700, exist_ok=False)
    failures, expected, before, replays, groups, task_inputs = [], {}, {}, [], {}, {}
    optional, directories = [], []
    initial_gate = snapshot([GATE / "SHA256SUMS"])
    save(out / "invocation.json", observation())
    try:
        if not (sys.flags.isolated and sys.flags.no_site and sys.flags.dont_write_bytecode
                and sys.flags.optimize == 0 and sys.pycache_prefix == str(out / "never_created_parent_cache")
                and not Path(sys.pycache_prefix).exists() and dict(os.environ) == ENV
                and Path.cwd() == ROOT):
            raise RuntimeError("PARENT_SETTINGS_ENV_CWD_OR_EXCLUSIVE_CACHE_GUARD_FAILED")
        groups, expected = sealed_inputs()
        save(out / "sealed.groups.json", groups)
        save(out / "sealed.expected.json", expected)
        task_inputs = snapshot([SCRIPT, PREPARATION, ROOT_INSPECTION])
        save(out / "root_task_inputs.before.json", task_inputs)
        before = snapshot(set(expected) | set(task_inputs))
        save(out / "sealed.before.json", {p: before[p] for p in expected})
        mismatch = {p: before.get(p) for p, digest in expected.items()
                    if before.get(p, {}).get("sha256") != digest}
        mismatch.update({p: value for p, value in task_inputs.items() if "error" in value})
        if mismatch:
            save(out / "sealed.initial_mismatches.json", mismatch)
            raise RuntimeError("SEALED_INPUT_DIGEST_MISMATCH")
        runtime, optional, directories = runtime_inventory(out, expected, failures)
        # Any newly discovered, unpinned loader dependency blocks scientific runs.
        if failures:
            raise RuntimeError("RUNTIME_INVENTORY_FAILED_BEFORE_PRODUCER")
        pinned = set(before) | set(map(str, runtime))
        full_before = snapshot(pinned)
        save(out / "all_inputs.before.json", full_before)
        before = full_before
        for label in ("replay_01", "replay_02"):
            result = safe(label, failures, lambda label=label: one_run(out / label, pinned, failures))
            replays.append(result)
            if result is not None:
                before.update(result["source_inputs_before"])
        save(out / "all_inputs.including_capsules.before.json", before)
        comparison = out / "comparison"
        comparison.mkdir()
        targets = [(out / "replay_01/producer.stdout", out / "replay_02/producer.stdout", "pair"),
                   (GATE / "CANONICAL.json", out / "replay_01/producer.stdout", "canonical_01"),
                   (GATE / "CANONICAL.json", out / "replay_02/producer.stdout", "canonical_02")]
        comparison_before = snapshot({str(p) for pair in targets for p in pair[:2]} | {"/usr/bin/cmp"})
        save(comparison / "before.json", comparison_before)
        for left, right, tag in targets:
            receipt = command(["/usr/bin/cmp", "--", str(left), str(right)], comparison, tag)
            if receipt["exit"] != 0 or receipt["spawn_error"]:
                failures.append({"stage": "raw_comparison", "tag": tag, "receipt": receipt})
        comparison_after = snapshot(comparison_before)
        save(comparison / "after.json", comparison_after)
        if comparison_before != comparison_after:
            failures.append({"stage": "comparison_input_closure"})
        shutil.copyfile(out / "replay_01/producer.stdout", out / "CANONICAL.json")
        if sha(out / "CANONICAL.json") != sha(GATE / "CANONICAL.json"):
            failures.append({"stage": "root_canonical_digest"})
    except BaseException as error:
        failures.append({"stage": "main", "error": repr(error), "traceback": traceback.format_exc()})
    finally:
        task_after = safe("root_task_inputs_after", failures, lambda: snapshot(task_inputs))
        safe("write_root_task_inputs_after", failures, lambda: save(out / "root_task_inputs.after.json", task_after))
        if task_inputs != task_after:
            failures.append({"stage": "root_task_inputs_before_after"})
        if (out / "runtime.before_ldd.json").is_file():
            runtime_before = safe("read_runtime_baseline", failures,
                lambda: json.loads((out / "runtime.before_ldd.json").read_text()))
            runtime_after = safe("runtime_global_closure", failures, lambda: snapshot(runtime_before or {}))
            safe("write_runtime_global_closure", failures, lambda: save(out / "runtime.global.after.json", runtime_after))
            if runtime_before != runtime_after:
                failures.append({"stage": "runtime_global_before_after"})
        if optional or directories:
            present_after = safe("runtime_presence_after", failures, lambda: presence(optional, directories))
            safe("write_runtime_presence_after", failures, lambda: save(out / "runtime.presence.after.json", present_after))
            present_before = safe("read_runtime_presence_before", failures,
                lambda: json.loads((out / "runtime.presence.before.json").read_text()))
            if present_after != present_before:
                failures.append({"stage": "runtime_optional_or_config_directory_presence_changed"})
        after = safe("all_inputs_after", failures, lambda: snapshot(before))
        safe("write_all_inputs_after", failures, lambda: save(out / "all_inputs.after.json", after))
        if before != after:
            failures.append({"stage": "global_input_before_after"})
        closed = safe("gate_complete_after", failures, sealed_inputs)
        if closed is not None and groups and closed != (groups, expected):
            failures.append({"stage": "gate_or_external_pin_manifest_changed"})
        if initial_gate != snapshot(initial_gate):
            failures.append({"stage": "gate_seal_changed"})
        parent_final = safe("final_parent_observation", failures, observation)
        safe("write_final_parent_observation", failures, lambda: save(out / "parent.final.json", parent_final))
        final_closure = path_closure(consumed(parent_final or {}), before, out)
        safe("write_final_parent_closure", failures, lambda: save(out / "parent.final.closure.json", final_closure))
        if final_closure["uncovered"] or final_closure["bytecode"]:
            failures.append({"stage": "final_parent_consumed_path_closure", **final_closure})
        if sys.pycache_prefix and Path(sys.pycache_prefix).exists():
            failures.append({"stage": "parent_cache_created"})
        result = {"status": "PASS" if not failures and len(replays) == 2 else "FAIL_PRESERVED",
                  "failures": failures, "replays": replays, "gate_seal_sha256": SEAL_SHA,
                  "scope": "root actual execution of sealed standalone kernel; original n=0..5 only",
                  "external_action": "HOLD_EXTERNAL", "output_directory": str(out),
                  "observation_limit": "module/maps/audit-open plus conservative stdlib/config and actual ldd; not OS hermetic"}
        save(out / "RECEIPT.json", result)
        payloads = sorted((p for p in out.rglob("*") if p.is_file()), key=lambda p: str(p.relative_to(out)))
        with (out / "SHA256SUMS").open("x") as seal:
            for p in payloads:
                seal.write(sha(p) + "  " + str(p.relative_to(out)) + "\n")
        print(json.dumps({"status": result["status"], "output_directory": str(out),
                          "failure_count": len(failures), "payload_count": len(payloads)}, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
