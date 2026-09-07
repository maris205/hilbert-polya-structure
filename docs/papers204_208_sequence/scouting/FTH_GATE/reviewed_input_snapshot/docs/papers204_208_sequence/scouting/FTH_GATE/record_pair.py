"""Independent, source-only gate replay recorder; no author code imported.

All JSON/files written by this program are actual execution artifacts.
Runtime coverage is module-origin, mapped-file and child audit-open coverage,
not a claim to have traced every kernel syscall or short-lived ldd child map.
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

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[3]
ENV = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8", "TZ": "UTC"}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save(path, value):
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


def hashes(paths):
    return {str(Path(p).resolve()): sha(p) for p in sorted(set(map(Path, paths)))}


def current_runtime():
    modules = {name: {"file": getattr(module, "__file__", None),
                      "origin": getattr(getattr(module, "__spec__", None), "origin", None)}
               for name, module in sorted(sys.modules.items())}
    maps = Path("/proc/self/maps").read_text()
    mapped = sorted({str(Path(line.split()[-1]).resolve()) for line in maps.splitlines()
                     if "/" in line and Path(line.split()[-1]).is_file()})
    return {"modules": modules, "mapped_files": mapped, "maps": maps,
            "sys_executable": sys.executable, "sys_path": sys.path, "flags": str(sys.flags),
            "optimization": sys.flags.optimize, "pycache_prefix": sys.pycache_prefix,
            "cache_exists": bool(sys.pycache_prefix and Path(sys.pycache_prefix).exists())}


def observed_paths(observation):
    used = set(observation["mapped_files"])
    for item in observation["modules"].values():
        if item["file"] and Path(item["file"]).is_file():
            used.add(str(Path(item["file"]).resolve()))
    used |= {str(Path(p).resolve()) for p in observation.get("opened_existing_files", [])
             if Path(p).is_file() and not p.startswith("/proc/")}
    return used


def command(argv, folder, tag):
    start = time.time()
    with (folder / (tag + ".stdout")).open("xb") as out, (folder / (tag + ".stderr")).open("xb") as err:
        process = subprocess.run(argv, cwd=folder, env=ENV, stdout=out, stderr=err, check=False)
    receipt = {"argv": argv, "cwd": str(folder), "env": ENV, "exit": process.returncode,
               "started_epoch": start, "finished_epoch": time.time(),
               "stdout": tag + ".stdout", "stderr": tag + ".stderr"}
    save(folder / (tag + ".command.json"), receipt)
    return receipt


def inventory_runtime(folder):
    fixed = [sys.executable, "/usr/bin/cmp", "/usr/bin/ldd", "/bin/bash", "/bin/sh"]
    paths = {Path(p).resolve() for p in fixed}
    paths |= {Path(p) for p in observed_paths(current_runtime()) if Path(p).resolve() != Path(__file__).resolve()}
    standard = Path(sysconfig.get_path("stdlib"))
    for directory, folders, files in os.walk(standard):
        folders[:] = [name for name in folders if name not in {"site-packages", "dist-packages", "__pycache__"}]
        for name in files:
            p = Path(directory, name)
            if p.suffix in {".py", ".so"} or name in {"Makefile", "pyconfig.h"}:
                paths.add(p.resolve())
    for p in [sysconfig.get_makefile_filename(), sysconfig.get_config_h_filename(),
              "/etc/ld.so.cache", "/etc/ld.so.conf", "/etc/nsswitch.conf", "/etc/localtime"]:
        if Path(p).is_file():
            paths.add(Path(p).resolve())
    for directory in [Path("/etc/ld.so.conf.d"), Path("/usr/lib/locale/C.utf8")]:
        if directory.exists():
            paths |= {p.resolve() for p in directory.rglob("*") if p.is_file()}
    for p in [standard.parent / ("python" + str(sys.version_info.major) + str(sys.version_info.minor) + ".zip"),
              Path(sys.executable).resolve().parent / "pyvenv.cfg",
              Path(sys.executable).resolve().parent.parent / "pyvenv.cfg"]:
        if p.is_file():
            paths.add(p.resolve())
    # Pin ldd's own script and its exact shebang interpreter before using it.
    # Explicit Bash and sh are included even when sh resolves to dash.
    ldd_text = Path("/usr/bin/ldd").read_text()
    first = ldd_text.splitlines()[0]
    interpreter = first[2:].strip().split()[0] if first.startswith("#!") else None
    if interpreter:
        paths.add(Path(interpreter).resolve())
    save(folder / "ldd.bootstrap.before.json", hashes(["/usr/bin/ldd", "/bin/bash", "/bin/sh", sys.executable]))
    ldd_dir = folder / "ldd"
    ldd_dir.mkdir()
    queue = []
    for p in sorted(paths):
        with p.open("rb") as source:
            if source.read(4) == b"\x7fELF":
                queue.append(p)
    processed, links = set(), []
    while queue:
        p = queue.pop(0)
        if p in processed:
            continue
        processed.add(p)
        tag = "link_" + str(len(processed)).zfill(3)
        receipt = command(["/usr/bin/ldd", str(p)], ldd_dir, tag)
        output = (ldd_dir / (tag + ".stdout")).read_text(errors="replace")
        errors = (ldd_dir / (tag + ".stderr")).read_text(errors="replace")
        if receipt["exit"] != 0 and "statically linked" not in output + errors:
            raise RuntimeError(("LDD_FAILED", str(p), receipt, errors))
        dependencies = set()
        for match in re.findall(r"/[^\s()]+", output):
            candidate = Path(match)
            if candidate.is_file():
                dependencies.add(candidate.resolve())
        links.append({"target": str(p), "dependencies": sorted(map(str, dependencies)), "receipt": tag + ".command.json"})
        paths |= dependencies
        queue.extend(sorted(dependencies - processed))
    save(folder / "ldd.index.json", {"shebang": first, "interpreter": interpreter, "links": links})
    save(folder / "ldd.bootstrap.after.json", hashes(["/usr/bin/ldd", "/bin/bash", "/bin/sh", sys.executable]))
    save(folder / "config.json", {"stdlib": str(standard), "sysconfig_paths": sysconfig.get_paths(),
         "sysconfig_vars": sysconfig.get_config_vars(), "env": ENV,
         "absent_optional_inputs": [str(p) for p in [Path("/etc/ld.so.preload")] if not p.exists()]})
    if Path("/etc/ld.so.preload").exists():
        paths.add(Path("/etc/ld.so.preload").resolve())
    return paths


def one_run(label, original_paths):
    folder = BASE / label
    folder.mkdir(exist_ok=False)
    inputs = folder / "source_inputs"
    inputs.mkdir()
    shutil.copyfile(BASE / "pre_author_code/kernel_v0.py", inputs / "kernel_v0.py")
    shutil.copyfile(BASE / "bootstrap.py", inputs / "bootstrap.py")
    if sorted(p.name for p in inputs.iterdir()) != ["bootstrap.py", "kernel_v0.py"]:
        raise RuntimeError("NOT_SOURCE_ONLY")
    scientific = original_paths + [inputs / "kernel_v0.py", inputs / "bootstrap.py", Path(__file__).resolve()]
    before_science = hashes(scientific)
    save(folder / "science.before.json", before_science)
    parent_before = current_runtime()
    save(folder / "parent.before.json", parent_before)
    runtime_paths = inventory_runtime(folder)
    runtime_before = hashes(runtime_paths)
    save(folder / "runtime.before.json", runtime_before)
    cache = folder / "never_created_child_cache"
    if cache.exists():
        raise RuntimeError("STALE_CACHE")
    argv = [str(Path(sys.executable).resolve()), "-I", "-S", "-B", "-X", "pycache_prefix=" + str(cache), str(inputs / "bootstrap.py")]
    receipt = command(argv, folder, "producer")
    after_science, runtime_after = hashes(scientific), hashes(runtime_paths)
    save(folder / "science.after.json", after_science)
    save(folder / "runtime.after.json", runtime_after)
    parent_after = current_runtime()
    save(folder / "parent.after.json", parent_after)
    child = json.loads((folder / "child.observed.json").read_text())
    used = observed_paths(parent_before) | observed_paths(parent_after) | observed_paths(child)
    covered = set(runtime_before) | set(before_science)
    uncovered = sorted(used - covered)
    intact = before_science == after_science and runtime_before == runtime_after
    settings = not cache.exists() and child["optimization"] == 0 and child["isolated"] and child["no_site"] and child["dont_write_bytecode"]
    bytecode = sorted(p for p in used if p.endswith((".pyc", ".pyo")))
    status = "PASS" if receipt["exit"] == 0 and intact and settings and not uncovered and not bytecode else "FAIL_PRESERVED"
    summary = {"status": status, "producer_exit": receipt["exit"], "before_after_equal": intact,
               "settings_pass": bool(settings), "consumed_bytecode": bytecode,
               "science_files": len(before_science), "runtime_files": len(runtime_before),
               "observed_consumed_file_count": len(used), "observed_consumed_files": sorted(used),
               "uncovered": uncovered, "stdout_sha256": sha(folder / "producer.stdout"),
               "stdout_bytes": (folder / "producer.stdout").stat().st_size,
               "source_only_initial_file_names": ["bootstrap.py", "kernel_v0.py"]}
    save(folder / "RECEIPT.json", summary)
    if status != "PASS":
        raise RuntimeError(summary)
    return summary


def main():
    if not (sys.flags.isolated and sys.flags.no_site and sys.flags.dont_write_bytecode
            and sys.flags.optimize == 0 and sys.pycache_prefix and not Path(sys.pycache_prefix).exists()):
        raise RuntimeError("PARENT_ISOLATION_SETTINGS_FAILURE")
    original_paths = [ROOT / line.split("  ", 1)[1] for line in (BASE / "INPUT_PINS.sha256").read_text().splitlines()]
    for line in (BASE / "INPUT_PINS.sha256").read_text().splitlines():
        expected, rel = line.split("  ", 1)
        if sha(ROOT / rel) != expected:
            raise RuntimeError(("INPUT_PIN_CHANGED", rel))
    first = one_run("replay_01", original_paths)
    second = one_run("replay_02", original_paths)
    comparison = BASE / "comparison"
    comparison.mkdir(exist_ok=False)
    cp = shutil.copyfile(BASE / "replay_01/producer.stdout", BASE / "CANONICAL.json")
    before = hashes([BASE / "CANONICAL.json", BASE / "replay_01/producer.stdout", BASE / "replay_02/producer.stdout", "/usr/bin/cmp"])
    save(comparison / "before.json", before)
    checks = [command(["/usr/bin/cmp", "--", str(BASE / left), str(BASE / right)], comparison, tag)
              for left, right, tag in [("replay_01/producer.stdout", "replay_02/producer.stdout", "pair"),
                                       ("CANONICAL.json", "replay_01/producer.stdout", "canonical_01"),
                                       ("CANONICAL.json", "replay_02/producer.stdout", "canonical_02")]]
    after = hashes(before)
    save(comparison / "after.json", after)
    result = {"status": "PASS" if before == after and all(r["exit"] == 0 for r in checks) else "FAIL_PRESERVED",
              "actual_comparisons": checks, "replays": [first, second], "before_after_equal": before == after,
              "canonical_sha256": sha(BASE / "CANONICAL.json"), "parent_cache_exists_after": Path(sys.pycache_prefix).exists()}
    save(comparison / "RECEIPT.json", result)
    print(json.dumps(result, sort_keys=True))
    if result["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
