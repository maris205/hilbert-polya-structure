#!/usr/bin/env python3
"""Root-only P209 manuscript-B replay pair; existing canonical is read-only.

Disclosed path/role/canonical adaptation of the physically saved B recorder.
No review recorder is imported; the unchanged B verifier is copied as code
only. Original recording and closure machinery remains. Build helpers stay
unchanged but unreachable through this exact pair-only entry point.
Infrastructure preparation is not a manuscript review or replay.
"""
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import signal
import subprocess
import sys
import sysconfig
import time
import traceback

SCRIPT = Path(__file__).resolve()
ROOT = Path("/root/autodl-tmp/symbolic_dynamics")
PAPER = ROOT / "docs/papers204_208_sequence/reviews/p209_b"
OUTPUT_ROOT = ROOT / "docs/papers204_208_sequence/qa/root_replays/p209_b_strict"
ROOT_LAUNCHER = SCRIPT.with_name("root_launch_pair.py")
FIXED_INPUTS = SCRIPT.with_name("FIXED_INPUTS.json")
EXPECTED_FIXED_INPUTS = "09a5033597e9b218296f624c256fe2d370331e08269bf1fcc2928352104fb7c8"
EXPECTED_B_INPUTS = {
    "record_review.py": "01623b42719e6159ae31c0e422079929766de61e4f07459c6d579b7f952fa272",
    "launch_review.py": "f190bf2e91b130428a97025bfd708f9a652e80f31ca41706dd81d0259c15693d",
    "bootstrap.py": "dc2f0ef968f2b451ceaf390ac7a8189005881246624a0f94ab64879efa18a80b",
    "verify.py": "d5fd105ddfc162323f06cd530fbd696b0093643a7a0c24c64747cd9c9be30467",
    "PARAMETERS.json": "3b292d4c771041cd07f82c5da2bf534bfa77e67fc971e78df3d08910e937b8e4",
    "INPUT_PINS.sha256": "eee2b677a37c82bc3e99b209f0d310231f1bd0358752724ce7f9d0f3588f200f",
    "CANONICAL.json": "612e1463162deba868cf7cf81d61c8f017713f9b28c4c38b81b00d376bac992c",
    "SHA256SUMS": "d88b831e60414d47ae0b2afb2583b73d02fc9764877a00952f4a9d90d13488ea",
}
FREEZE = ROOT / "papers/209-ordered-fibre-threading/frozen_round1"
PYTHON = Path(sys.executable).resolve()
STDLIB = Path(sysconfig.get_path("stdlib")).resolve()
ENV = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8", "TZ": "UTC"}
SOURCES = ("main.tex", "math_commands.tex", "references.bib",
           "sections/00_abstract.tex", "sections/01_setup.tex",
           "sections/02_recurrence.tex", "sections/03_inverse.tex", "sections/04_scope.tex")
SCIENCE = ("PAPER_PLAN.md", "NARRATIVE_REPORT.md", "CLAIMS_EVIDENCE.md",
           "PROOF_PACKAGE.md", "SOURCE_AUDIT.md", "README.md", "verify.py",
           "bootstrap.py", "PARAMETERS.json", "collect_context.py", "record_review.py", "launch_author.py",
           "metadata_web_01.json", "metadata_web_02.json") + SOURCES
TOOLS = tuple(Path(p) for p in ("/usr/bin/env", "/usr/bin/cmp", "/usr/bin/ldd", "/bin/bash", "/bin/sh"))
BUILD_TOOLS = tuple(Path("/usr/bin") / name for name in
                    ("pdflatex", "bibtex", "kpsewhich", "pdfinfo", "pdffonts", "pdftotext", "pdftoppm"))
LIB_ROOTS = tuple(Path(p) for p in ("/usr/lib/x86_64-linux-gnu", "/usr/lib64", "/usr/local/lib"))
TEX_ROOTS = tuple(Path(p) for p in ("/usr/share/texlive/texmf-dist", "/usr/share/texmf",
                   "/var/lib/texmf", "/etc/texmf", "/usr/local/share/texmf", "/root/texmf",
                   "/root/.texlive2021/texmf-config", "/root/.texlive2021/texmf-var"))
BUILD_CONFIG_ROOTS = tuple(Path(p) for p in ("/usr/share/fonts", "/usr/local/share/fonts", "/etc/fonts", "/var/cache/fontconfig",
                   "/usr/share/fontconfig", "/usr/share/poppler", "/etc/xdg/fontconfig",
                   "/root/.fonts", "/root/.fontconfig", "/root/.fonts.conf.d",
                   "/root/.config/fontconfig", "/root/.cache/fontconfig", "/root/.local/share/fonts"))
OPENED = set()
VALIDATED_GENERATED_MANIFESTS = set()
UNREAPED_CHILDREN = set()
REGISTERED_INPUTS = {}
COMMAND_RECORDS = []
COMMAND_OBSERVED = set()
HASHING = False


def audit(event, args):
    if not HASHING and event == "open" and isinstance(args[0], (str, bytes)):
        p = Path(os.fsdecode(args[0])).absolute()
        if p.is_file() and not str(p).startswith("/proc/"):
            OPENED.add(str(p.resolve()))


sys.addaudithook(audit)


def info(raw):
    global HASHING
    path = Path(raw)
    previous, HASHING = HASHING, True
    try:
        h = hashlib.sha256()
        with path.open("rb") as stream:
            for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                h.update(chunk)
        return {"sha256": h.hexdigest(), "bytes": path.stat().st_size,
                "resolved": str(path.resolve()),
                "symlink": os.readlink(path) if path.is_symlink() else None}
    finally:
        HASHING = previous


def byteinfo(path):
    data = info(path)
    return {k: data[k] for k in ("sha256", "bytes")}


def save(path, value):
    with Path(path).open("x", encoding="utf-8") as stream:
        json.dump(value, stream, sort_keys=True, indent=2)
        stream.write("\n")


def bytesave(path, value):
    with Path(path).open("xb") as stream:
        stream.write(value)


def pins(paths):
    result = {}
    for raw in sorted(set(map(str, paths))):
        try:
            result[raw] = info(raw)
        except BaseException as error:
            result[raw] = {"error": type(error).__name__ + ": " + str(error)}
    return result


def require(value, label, *witness):
    if not value:
        raise RuntimeError((label, witness))


def inventory(roots):
    names = sorted({str(p) for root in roots if root.is_dir()
                    for p in root.rglob("*") if p.is_file()})
    return {"roots": {str(p): p.exists() for p in roots}, "files": pins(names)}


def manifest(base):
    target = base / "SHA256SUMS"
    require(not UNREAPED_CHILDREN, "REFUSE_SEAL_WITH_UNREAPED_OWNED_CHILD", sorted(UNREAPED_CHILDREN))
    require(not target.exists(), "REFUSE_SEAL_OVERWRITE", target)
    paths = sorted(p for p in base.rglob("*") if p.is_file())
    require(all(not p.is_symlink() for p in paths), "PACKAGE_SYMLINK", base)
    bytesave(target, "".join(info(p)["sha256"] + "  " + p.relative_to(base).as_posix() + "\n"
                              for p in paths).encode())
    check_manifest(base)
    VALIDATED_GENERATED_MANIFESTS.add(str(target.resolve()))
    return {"payloads": len(paths), **byteinfo(target)}


def check_manifest(base):
    target = base / "SHA256SUMS"
    seen = set()
    for line in target.read_text().splitlines():
        digest, name = line.split("  ", 1)
        relative = Path(name)
        require(re.fullmatch(r"[0-9a-f]{64}", digest) and not relative.is_absolute()
                and ".." not in relative.parts and name != "SHA256SUMS" and name not in seen,
                "UNSAFE_OR_SELF_MANIFEST", target, name)
        seen.add(name)
        require(info(base / relative)["sha256"] == digest, "MANIFEST_HASH", target, name)
    require(seen == {p.relative_to(base).as_posix() for p in base.rglob("*")
                     if p.is_file() and p != target}, "INCOMPLETE_NONSELF_MANIFEST", base)


def observation(phase):
    modules = {name: {"file": getattr(module, "__file__", None),
                      "origin": getattr(getattr(module, "__spec__", None), "origin", None)}
               for name, module in sorted(sys.modules.items())}
    maps = Path("/proc/self/maps").read_text()
    mapped = sorted({str(Path(line.split(None, 5)[5]).resolve())
                     for line in maps.splitlines()
                     if len(line.split(None, 5)) == 6 and line.split(None, 5)[5].startswith("/")})
    return {"phase": phase, "modules": modules, "maps": maps, "mapped_files": mapped,
            "opened_existing_files": sorted(OPENED), "argv": sys.argv, "orig_argv": sys.orig_argv,
            "cwd": os.getcwd(), "env": dict(os.environ), "executable": str(PYTHON),
            "version": sys.version, "sys_path": sys.path, "flags": str(sys.flags),
            "optimization": sys.flags.optimize, "pycache_prefix": sys.pycache_prefix,
            "cache_exists": bool(sys.pycache_prefix and Path(sys.pycache_prefix).exists())}


def consumed(obs):
    paths = set(obs.get("mapped_files", [])) | set(obs.get("opened_existing_files", []))
    for value in obs.get("modules", {}).values():
        for key in ("file", "origin"):
            raw = value.get(key)
            if raw and Path(raw).is_file():
                paths.add(str(Path(raw).resolve()))
    return {str(Path(p).resolve()) for p in paths if not str(p).startswith("/proc/")}


def coverage(used, before, out):
    covered = {v["resolved"] for v in before.values() if "resolved" in v}
    generated = {p for p in used - covered if Path(p).is_relative_to(out)
                 and Path(p).is_file() and (Path(p).suffix in {".json", ".stdout", ".stderr", ".log", ".fls", ".aux", ".bbl", ".blg", ".txt", ".pdf", ".png"}
                 or p in VALIDATED_GENERATED_MANIFESTS)}
    return {"observed_files": sorted(used), "generated_receipt_or_build_reads": sorted(generated),
            "exact_validated_generated_manifests": sorted(VALIDATED_GENERATED_MANIFESTS),
            "uncovered": sorted(used - covered - generated),
            "bytecode": sorted(p for p in used if p.endswith((".pyc", ".pyo")))}


def science():
    check_manifest(FREEZE)
    require(info(FREEZE / "SHA256SUMS")["sha256"] == "c93e16cf20d2eb87f3b454fbdb3576e52c6c79fb74c8712a277efeab7e60ce57", "EXACT_ROUND1_SEAL")
    files = [p for p in FREEZE.rglob("*") if p.is_file()]
    files += [PAPER / n for n in ("verify.py", "bootstrap.py", "record_review.py", "launch_review.py", "PARAMETERS.json", "INDEPENDENCE_DESIGN.md", "INDEPENDENCE_COMMITMENT.sha256", "intake.py", "prepare_infrastructure.py", "INFRASTRUCTURE_INPUT_PINS.sha256", "ADAPTATION.diff", "INPUT_PINS.sha256")]
    files += [p for p in (PAPER / "infrastructure_originals").rglob("*") if p.is_file()]
    require((PAPER / "CANONICAL.json").is_file(), "ROOT_CANONICAL_REQUIRED_NO_ADOPTION")
    files += [PAPER / "CANONICAL.json", PAPER / "SHA256SUMS"]
    require(info(FIXED_INPUTS)["sha256"] == EXPECTED_FIXED_INPUTS, "FIXED_INPUT_MANIFEST_CHANGED")
    fixed = json.loads(FIXED_INPUTS.read_bytes())
    require(set(fixed) == set(map(str, files)) and len(fixed) == 2021, "FIXED_ORIGINAL_SCOPE_CHANGED")
    value = pins(files)
    require(value == fixed, "EXACT_PREPARATION_FULL_INPUTS_CHANGED")
    value.update(pins([SCRIPT, ROOT_LAUNCHER, FIXED_INPUTS]))
    REGISTERED_INPUTS.update(value)
    require(all("error" not in p for p in value.values()), "MISSING_SCIENTIFIC_INPUT")
    require(all(value[str(PAPER / name)]["sha256"] == digest
                for name, digest in EXPECTED_B_INPUTS.items()), "EXACT_PREPARATION_B_INPUTS_CHANGED")
    config = json.loads((PAPER / "PARAMETERS.json").read_bytes())
    require(config["n_values"] == list(range(6)) and config["total_states"] == 3414, "ORIGINAL_CUTOFF_CHANGED")
    return value


def runtime(mode):
    std = []
    for directory, folders, files in os.walk(STDLIB):
        folders[:] = [f for f in folders if f not in {"site-packages", "dist-packages", "__pycache__"}]
        std += [Path(directory) / n for n in files if not n.endswith((".pyc", ".pyo"))]
    potential = []
    for root in LIB_ROOTS:
        if root.is_dir():
            # OS multiarch is recursive (providers/gconv included); /usr/local
            # is direct only, avoiding unrelated Python packages below it.
            iterator = root.glob("*") if root == Path("/usr/local/lib") else root.rglob("*")
            potential += [p for p in iterator if p.is_file() and
                          (p.name.endswith(".so") or ".so." in p.name)]
    paths = std + potential + list(TOOLS) + [PYTHON]
    if mode == "build":
        paths += list(BUILD_TOOLS)
    early = observation("runtime_discovery")
    early["opened_existing_files"] = []
    paths += [Path(p) for p in consumed(early) if p != str(SCRIPT)]
    optional = [Path(p) for p in ("/etc/ld.so.cache", "/etc/ld.so.conf", "/etc/ld.so.preload",
             "/etc/nsswitch.conf", "/etc/localtime", "/etc/locale.conf", "/etc/default/locale",
             "/usr/lib/locale/locale-archive", "/etc/bash.bashrc", "/etc/profile",
             "/lib/ld-linux.so.2", "/lib64/ld-linux-x86-64.so.2", "/libx32/ld-linux-x32.so.2")]
    optional += [Path(sysconfig.get_makefile_filename()), Path(sysconfig.get_config_h_filename()),
                 STDLIB.parent / ("python%d%d.zip" % sys.version_info[:2]),
                 PYTHON.parent / "pyvenv.cfg", PYTHON.parent.parent / "pyvenv.cfg"]
    names = {"python._pth", "python3._pth", "python%d%d._pth" % sys.version_info[:2],
             "python%d.%d._pth" % sys.version_info[:2], PYTHON.name + "._pth"}
    for directory in {PYTHON.parent, Path(sys.executable).parent, STDLIB.parent}:
        optional += [directory / name for name in names]
    for name in ("LDLIBRARY", "INSTSONAME"):
        value = sysconfig.get_config_var(name)
        if value:
            optional.append(STDLIB.parent / (value + "._pth"))
    dirs = [Path(p) for p in ("/etc/ld.so.conf.d", "/usr/lib/locale/C.utf8", "/etc/profile.d",
                             "/usr/lib/x86_64-linux-gnu/gconv", "/usr/lib/gconv")]
    if mode == "build":
        dirs += list(BUILD_CONFIG_ROOTS)
        optional += [Path(p) for p in ("/root/.fonts.conf", "/root/.config/fontconfig/fonts.conf",
                     "/etc/fonts/local.conf", "/etc/passwd", "/etc/group")]
    ldd_source = Path("/usr/bin/ldd").read_text()
    match = re.search(r'^RTLDLIST="([^"]+)"', ldd_source, re.M)
    require(ldd_source.splitlines()[0] == "#!/bin/bash" and match is not None, "UNREVIEWED_LDD_LOADER")
    optional += [Path(p) for p in match.group(1).split()]
    paths += [p for p in optional if p.is_file()]
    paths += [p for root in dirs if root.is_dir() for p in root.rglob("*") if p.is_file()]
    return pins(paths), optional, dirs, {"stdlib": str(STDLIB), "potential_library_roots": list(map(str, LIB_ROOTS)),
           "ldd_shebang": ldd_source.splitlines()[0], "ldd_loaders": match.group(1).split(),
           "sysconfig_paths": sysconfig.get_paths(), "sysconfig_vars": sysconfig.get_config_vars(),
           "bash_mode": "noninteractive non-login ldd shell; ENV/BASH_ENV absent"}


def presence(optional, dirs):
    return {"optional": {str(p): {"exists": p.exists(), "is_file": p.is_file(),
                         "resolved": str(p.resolve()), **(byteinfo(p) if p.is_file() else {})}
                          for p in sorted(set(optional))},
            "directories": {str(p): sorted(str(q) for q in p.rglob("*") if q.is_file())
                            if p.is_dir() else None for p in sorted(set(dirs))}}


def is_elf(path):
    global HASHING
    previous, HASHING = HASHING, True
    try:
        with Path(path).open("rb") as stream:
            return stream.read(4) == b"\x7fELF"
    finally:
        HASHING = previous


def command(argv, cwd, folder, tag, env):
    started = time.time()
    row = {"argv": argv, "cwd": str(cwd), "env": env, "started_epoch": started,
           "exit": None, "process_outcome": "NOT_STARTED", "spawn_error": None,
           "stdout": tag + ".stdout", "stderr": tag + ".stderr",
           "start_new_session": True, "cleanup": []}
    save(folder / (tag + ".attempt.json"), {**row, "record_kind": "PRE_SPAWN_ATTEMPT"})
    samples, failures, proc = [], [], None
    try:
        with (folder / row["stdout"]).open("xb") as out, (folder / row["stderr"]).open("xb") as err:
            proc = subprocess.Popen(argv, cwd=cwd, env=env, stdout=out, stderr=err, start_new_session=True)
            UNREAPED_CHILDREN.add(proc.pid)
            row.update(pid=proc.pid, process_outcome="UNKNOWN_UNTIL_WAIT")
            previous = None
            while proc.poll() is None:
                try:
                    raw = Path("/proc") / str(proc.pid) / "maps"
                    maps = raw.read_text()
                    if maps != previous:
                        paths = sorted({str(Path(line.split(None, 5)[5]).resolve())
                                        for line in maps.splitlines() if len(line.split(None, 5)) == 6
                                        and line.split(None, 5)[5].startswith("/")})
                        samples.append({"epoch": time.time(), "maps": maps, "mapped_files": paths})
                        previous = maps
                except OSError as error:
                    failures.append({"epoch": time.time(), "type": type(error).__name__,
                                     "meaning": "sample raced with process exit or map availability"})
                time.sleep(0.01)
            row.update(exit=proc.wait(), process_outcome="COMPLETED")
            UNREAPED_CHILDREN.discard(proc.pid)
    except OSError as error:
        row.update(spawn_error=repr(error), process_outcome="NOT_STARTED" if proc is None else "NO_COMPLETED_RESULT")
    except BaseException as error:
        row.update(spawn_error=repr(error), process_outcome="NO_COMPLETED_RESULT")
    finally:
        if proc is not None and proc.pid in UNREAPED_CHILDREN:
            # A caught interruption never becomes a successful child command.
            # Stop only the process group created by this exact Popen call,
            # then reap its direct child before reading settled output bytes.
            try:
                if proc.poll() is None:
                    try:
                        os.killpg(proc.pid, signal.SIGTERM)
                        row["cleanup"].append({"action": "SIGTERM_OWNED_PROCESS_GROUP", "pgid": proc.pid})
                    except ProcessLookupError:
                        row["cleanup"].append({"action": "OWNED_GROUP_ALREADY_EXITED", "pgid": proc.pid})
                try:
                    cleanup_exit = proc.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    os.killpg(proc.pid, signal.SIGKILL)
                    row["cleanup"].append({"action": "SIGKILL_OWNED_PROCESS_GROUP", "pgid": proc.pid})
                    cleanup_exit = proc.wait(timeout=5)
                # Reap the direct child; any surviving member of its newly
                # created group must also be stopped before artifact sealing.
                try:
                    os.killpg(proc.pid, signal.SIGKILL)
                    row["cleanup"].append({"action": "SIGKILL_REMAINING_OWNED_GROUP", "pgid": proc.pid})
                except ProcessLookupError:
                    pass
                row["cleanup"].append({"action": "DIRECT_CHILD_REAPED", "cleanup_exit": cleanup_exit,
                                       "does_not_replace_original_exit": True})
                UNREAPED_CHILDREN.discard(proc.pid)
            except BaseException:
                row["cleanup"].append({"action": "CLEANUP_FAILED_DO_NOT_SEAL", "traceback": traceback.format_exc()})
        row["finished_epoch"] = time.time()
        for key in ("stdout", "stderr"):
            p = folder / row[key]
            if p.is_file():
                row[key + "_info"] = byteinfo(p)
        save(folder / (tag + ".maps.json"), {"samples": samples, "sample_errors": failures,
             "scope": "Sampled direct-child PID maps only; no continuous tracing or grandchild capture."})
        save(folder / (tag + ".command.json"), row)
        mapped = {p for sample in samples for p in sample["mapped_files"]}
        COMMAND_OBSERVED.update(mapped)
        COMMAND_RECORDS.append({"folder": str(folder), "tag": tag, "command": row,
                                "mapped_files": sorted(mapped)})
    require(row["process_outcome"] == "COMPLETED" and row["exit"] == 0,
            "CHILD_COMMAND_FAILED", tag, row)
    return row, {p for sample in samples for p in sample["mapped_files"]}


def linkage(out, mode, known, env):
    folder = out / "linkage"
    folder.mkdir()
    targets = [PYTHON, *TOOLS]
    targets += [p for p in STDLIB.rglob("*.so") if "site-packages" not in p.parts]
    if mode == "build":
        targets += list(BUILD_TOOLS)
    resolved = {v["resolved"] for v in known.values() if "resolved" in v}
    queue = sorted({p.resolve() for p in targets if p.is_file() and is_elf(p)})
    processed, rows, observed = set(), [], set()
    try:
        while queue:
            target = queue.pop(0)
            if target in processed:
                continue
            processed.add(target)
            tag = "ldd_" + str(len(processed)).zfill(3)
            entry = {"target": str(target), "tag": tag, "status": "ATTEMPTED_NOT_YET_VALIDATED"}
            rows.append(entry)
            row, mapped = command(["/usr/bin/ldd", str(target)], folder, folder, tag, env)
            entry["command"] = row
            raw = (folder / row["stdout"]).read_text(errors="replace")
            require("not found" not in raw, "UNRESOLVED_LINK", target)
            dependencies = {Path(p).resolve() for p in re.findall(r"/[^\s()]+", raw) if Path(p).is_file()}
            entry["dependencies"] = sorted(map(str, dependencies))
            require(all(str(p) in resolved for p in dependencies | {target}),
                    "LINK_DEPENDENCY_NOT_PINNED_BEFORE_FIRST_USE", target,
                    sorted(str(p) for p in dependencies | {target} if str(p) not in resolved))
            require(mapped <= resolved, "LINK_COMMAND_MAPPED_UNPINNED", target, sorted(mapped - resolved))
            observed |= mapped | set(map(str, dependencies))
            entry["status"] = "VALIDATED"
            queue += sorted(p for p in dependencies if p not in processed)
    finally:
        save(out / "LINKAGE.json", {"entries": rows, "pending_targets": list(map(str, queue)),
             "scope": "Attempt index retained even on failure; per-command receipts hold original exits and maps."})
    return rows, observed


def one_producer(out, label, all_before):
    folder = out / label
    folder.mkdir()
    capsule = folder / "source_inputs"
    capsule.mkdir()
    for name in ("bootstrap.py", "verify.py"):
        shutil.copyfile(PAPER / name, capsule / name)
        require(byteinfo(PAPER / name) == byteinfo(capsule / name), "PRODUCER_SOURCE_COPY", name)
    require(sorted(p.name for p in capsule.iterdir()) == ["bootstrap.py", "verify.py"], "NOT_CODE_ONLY")
    capsule_pins = pins(capsule.iterdir())
    REGISTERED_INPUTS.update(capsule_pins)
    before = {**all_before, **capsule_pins}
    save(folder / "INPUTS_BEFORE.json", before)
    cache = folder / "never_created_child_cache"
    argv = [str(PYTHON), "-I", "-S", "-B", "-X", "pycache_prefix=" + str(cache), str(capsule / "bootstrap.py")]
    problem, row, mapped, details = None, None, set(), {}
    try:
        require(not cache.exists(), "CHILD_CACHE_NOT_ABSENT")
        row, mapped = command(argv, folder, folder, "producer", ENV)
        payload = json.loads((folder / "producer.stdout").read_bytes())
        require(payload["schema"] == "p209-b-ports-constructive-carrier-v1"
                and sum(b["states"] for b in payload["boxes"]) == 3414
                and [b["n"] for b in payload["boxes"]] == list(range(6))
                and all(len(b["rows"]) == b["states"] for b in payload["boxes"]), "PRODUCER_PAYLOAD_SCOPE")
        details = {"checks": payload["checks"], "total_states": 3414,
                   "boxes": [{k: b[k] for k in ("n", "states", "recurrent", "image_size", "max_inverse")}
                             for b in payload["boxes"]]}

    except BaseException:
        problem = traceback.format_exc()
    finally:
        # Retain actual observations even when command() raised on nonzero
        # exit before returning its row, or payload parsing subsequently failed.
        for entry in COMMAND_RECORDS:
            if entry["folder"] == str(folder) and entry["tag"] == "producer":
                row = entry["command"]
                mapped.update(entry["mapped_files"])
        for phase in ("before", "after"):
            try:
                obs = json.loads((folder / ("child." + phase + ".json")).read_bytes())
                mapped |= consumed(obs)
                require(obs["orig_argv"] == argv and obs["env"] == ENV and obs["cwd"] == str(folder)
                        and obs["optimize"] == 0 and obs["isolated"] == 1 and obs["no_site"] == 1
                        and obs["dont_write_bytecode"] and obs["pycache_prefix"] == str(cache)
                        and not obs["cache_exists"], "ACTUAL_CHILD_SETTINGS", phase)
            except BaseException:
                problem = (problem or "") + "\nOBSERVATION_" + phase + ":\n" + traceback.format_exc()
        COMMAND_OBSERVED.update(mapped)
        after = pins(before)
        save(folder / "INPUTS_AFTER.json", after)
        closure = coverage(mapped, before, out)
        okay = problem is None and before == after and not closure["uncovered"] and not closure["bytecode"] and not cache.exists()
        value = {"status": "PASS" if okay else "FAIL_PRESERVED", "failure": problem,
                 "inputs_unchanged": before == after, "closure": closure, "command": row,
                 "capsule_pins": capsule_pins, "source_only_initial_names": ["bootstrap.py", "verify.py"], **details}
        save(folder / "RECEIPT.json", value)
        manifest(folder)
    require(okay, "PRODUCER_REPLAY_FAILED", label, value)
    return value, capsule_pins, mapped


def pair(out, all_before):
    results, added, observed = [], {}, set()
    for label in ("replay_01", "replay_02"):
        result, capsule, used = one_producer(out, label, {**all_before, **added})
        results.append(result)
        added.update(capsule)
        observed |= used
    comparison = out / "comparison"
    comparison.mkdir()
    raw1, raw2 = out / "replay_01/producer.stdout", out / "replay_02/producer.stdout"
    canonical = PAPER / "CANONICAL.json"
    adopted = False
    require(str(canonical) in all_before and canonical.is_file(), "ROOT_CANONICAL_MUST_PREEXIST")
    before = pins([raw1, raw2, "/usr/bin/cmp"] + ([canonical] if canonical.exists() else []))
    REGISTERED_INPUTS.update(before)
    save(comparison / "INPUTS_BEFORE.json", before)
    comparisons = []
    row, used = command(["/usr/bin/cmp", "--", str(raw1), str(raw2)], comparison, comparison, "pair", ENV)
    comparisons.append(row)
    observed |= used
    for label, raw in (("canonical_01", raw1), ("canonical_02", raw2)):
        row, used = command(["/usr/bin/cmp", "--", str(raw), str(canonical)], comparison, comparison, label, ENV)
        comparisons.append(row)
        observed |= used
    after = pins(before)
    save(comparison / "INPUTS_AFTER.json", after)
    require(after == before, "RAW_COMPARISON_INPUT_CHANGED")
    require(byteinfo(canonical) == byteinfo(raw1) == byteinfo(raw2), "ADOPTED_CANONICAL_BYTES")
    canonical_pin = info(canonical)
    require(canonical_pin == all_before[str(canonical)], "EXISTING_CANONICAL_INITIAL_PIN_CHANGED")
    REGISTERED_INPUTS.update(added)
    save(comparison / "CANONICAL_PIN.json", canonical_pin)
    manifest(comparison)
    return {"replays": results, "comparisons": comparisons, "canonical_adopted": adopted,
            "canonical": byteinfo(canonical)}, added, observed


def build(out, all_before, tex_before):
    folder = out / "cold_build"
    folder.mkdir()
    for name in SOURCES:
        destination = folder / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(FREEZE / name, destination)
    source_pins = pins(folder / name for name in SOURCES)
    REGISTERED_INPUTS.update(source_pins)
    require({p.relative_to(folder).as_posix() for p in folder.rglob("*") if p.is_file()} == set(SOURCES), "BUILD_NOT_SOURCE_ONLY")
    require(all(byteinfo(folder / n) == byteinfo(FREEZE / n) for n in SOURCES), "BUILD_SOURCE_COPY")
    save(out / "SOURCE_ONLY_INITIAL.json", source_pins)
    env = {**ENV, "SOURCE_DATE_EPOCH": "1788652800", "FORCE_SOURCE_DATE": "1", "openin_any": "p", "openout_any": "p"}
    roots = {key: str(out / ("never_created_" + key.lower())) for key in ("TEXMFHOME", "TEXMFCONFIG", "TEXMFVAR")}
    env.update(roots)
    require(not any(Path(v).exists() for v in roots.values()), "BUILD_USER_ROOT_NOT_ABSENT")
    save(out / "USER_ROOTS_BEFORE.json", {k: {"path": v, "exists": False} for k, v in roots.items()})
    commands, used, consumed_tex, generated_tex = [], set(), {}, {}
    external = {v["resolved"]: {k: v[k] for k in ("sha256", "bytes")}
                for v in tex_before["files"].values()}

    def call(tag, argv):
        row, mapped = command(argv, folder, out, tag, env)
        commands.append(row)
        used.update(mapped)
        return (out / row["stdout"]).read_text(errors="replace")

    for name in ("pdflatex", "bibtex"):
        call(name + "_version", ["/usr/bin/" + name, "--version"])
    call("texmf_roots", ["/usr/bin/kpsewhich", "-var-value=TEXMF"])
    for key, expected in roots.items():
        actual = call("query_" + key, ["/usr/bin/kpsewhich", "-var-value=" + key]).strip()
        require(str(Path(actual).resolve()) == expected, "UNEXPECTED_TEX_USER_ROOT", key, actual)
    for index in (1, 2, 3):
        call("tex_pass_" + str(index), ["/usr/bin/pdflatex", "-no-shell-escape", "-recorder",
             "-interaction=nonstopmode", "-halt-on-error", "main.tex"])
        for suffix in ("log", "fls", "aux"):
            shutil.copyfile(folder / ("main." + suffix), out / ("pass_" + str(index) + "." + suffix))
        for line in (folder / "main.fls").read_text().splitlines():
            if line.startswith("INPUT "):
                p = Path(line[6:])
                p = (p if p.is_absolute() else folder / p).resolve()
                require(p.is_file(), "FLS_MISSING_INPUT", p)
                value = byteinfo(p)
                if p.is_relative_to(folder):
                    local = p.relative_to(folder).as_posix()
                    if local in SOURCES:
                        require(value == byteinfo(FREEZE / local), "FLS_LOCAL_SOURCE_CHANGED", p)
                    else:
                        require(p.suffix in {".aux", ".bbl", ".out", ".toc"}, "UNEXPECTED_LOCAL_BUILD_INPUT", p)
                        generated_tex[str(index) + ":" + local] = value
                else:
                    require(external.get(str(p)) == value, "UNPINNED_EXTERNAL_TEX_INPUT", p)
                    consumed_tex[str(p)] = value
        if index == 1:
            bst = Path(call("bibliography_style", ["/usr/bin/kpsewhich", "plainnat.bst"]).strip()).resolve()
            require(external.get(str(bst)) == byteinfo(bst), "UNPINNED_BIB_STYLE")
            consumed_tex[str(bst)] = byteinfo(bst)
            call("bibtex_pass", ["/usr/bin/bibtex", "main"])
            for suffix in ("bbl", "blg"):
                shutil.copyfile(folder / ("main." + suffix), out / ("generated." + suffix))
    pdfinfo = call("pdfinfo", ["/usr/bin/pdfinfo", "main.pdf"])
    fonts = call("pdffonts", ["/usr/bin/pdffonts", "main.pdf"])
    call("pdftotext", ["/usr/bin/pdftotext", "-layout", "main.pdf", str(out / "main.txt")])
    pages = folder / "pages"
    pages.mkdir()
    call("render", ["/usr/bin/pdftoppm", "-png", "-r", "120", "main.pdf", str(pages / "page")])
    count = int(re.search(r"^Pages:\s+(\d+)$", pdfinfo, re.M).group(1))
    rows = [line.split()[-5:] for line in fonts.splitlines()[2:] if line.strip()]
    require(rows and all(row[0] == "yes" for row in rows), "NONEMBEDDED_FONT")
    require(count >= 1 and len(list(pages.glob("*.png"))) == count, "RENDER_PAGE_COUNT")
    text = (out / "main.txt").read_text()
    require(not any(word in text for word in ("[VERIFY]", "??", "[?]")), "UNRESOLVED_PDF_MARKER")
    log = (folder / "main.log").read_text()
    diagnostics = {key: re.findall(r"^.*" + pattern + r".*$", log, re.M)
                   for key, pattern in (("undefined", "undefined"), ("overfull", "Overfull"),
                       ("underfull", "Underfull"), ("warning", "Warning"),
                       ("rerun", "Rerun to|Please .*rerun|Label\\(s\\) may have changed"))}
    require(not diagnostics["undefined"] and not diagnostics["overfull"] and not diagnostics["rerun"], "FINAL_TEX_DIAGNOSTIC", diagnostics)
    require(source_pins == pins(source_pins), "BUILD_SOURCES_CHANGED")
    require(all(byteinfo(p) == value for p, value in consumed_tex.items()), "CONSUMED_TEX_CHANGED")
    user_after = {k: {"path": v, "exists": Path(v).exists()} for k, v in roots.items()}
    save(out / "USER_ROOTS_AFTER.json", user_after)
    require(not any(v["exists"] for v in user_after.values()), "TEX_USER_ROOT_CREATED")
    save(out / "CONSUMED_TEX.json", consumed_tex)
    save(out / "GENERATED_LOCAL_TEX_INPUTS.json", generated_tex)
    return {"commands": commands, "pdf": byteinfo(folder / "main.pdf"), "pages": count,
            "embedded_fonts": len(rows), "diagnostics": diagnostics,
            "visual_review": "NOT_YET_VIEWED_RENDER_NOT_A_VIEW", "source_names": list(SOURCES),
            "consumed_tex_count": len(consumed_tex)}, source_pins, used


def main():
    require(sys.argv[1:] == ["pair", "root_b_pair_01"], "USAGE", "root_record_pair.py pair root_b_pair_01")
    mode, label = sys.argv[1:]
    require(OUTPUT_ROOT.resolve() == OUTPUT_ROOT, "ROOT_OUTPUT_PATH_ALIAS")
    OUTPUT_ROOT.mkdir(mode=0o700, parents=True, exist_ok=True)
    out = OUTPUT_ROOT / label
    require(not out.exists() and not out.is_symlink(), "REFUSE_EXISTING_OUTPUT")
    out.mkdir(mode=0o700)
    failures, scientific, runtime_before, all_before, added = [], {}, {}, {}, {}
    optional, dirs, observed, link_rows = [], [], set(), []
    initial_presence, tex_before, result = {}, {}, {}
    bytesave(out / "executed_recorder.py", SCRIPT.read_bytes())
    save(out / "ATTEMPT.json", observation("PARENT_ENTRY_BEFORE_CHILDREN"))
    try:
        require(sys.flags.isolated == 1 and sys.flags.no_site == 1 and sys.flags.optimize == 0 and sys.dont_write_bytecode,
                "PARENT_ISOLATION_SETTINGS")
        require(sys.pycache_prefix == str(out / "never_created_parent_cache") and not Path(sys.pycache_prefix).exists(), "PARENT_EXCLUSIVE_CACHE")
        require(dict(os.environ) == ENV and Path.cwd() == ROOT, "PARENT_ENV_OR_CWD")
        require(PYTHON == Path("/usr/bin/python3.10"), "DECLARED_INTERPRETER_CHANGED")
        scientific = science()
        scientific[str(out / "executed_recorder.py")] = info(out / "executed_recorder.py")
        REGISTERED_INPUTS.update(scientific)
        save(out / "SCIENCE_BEFORE.json", scientific)
        early = observation("BEFORE_RUNTIME_AND_CHILDREN")
        save(out / "PARENT_BEFORE.json", early)
        observed |= consumed(early)
        runtime_before, optional, dirs, config = runtime(mode)
        REGISTERED_INPUTS.update(runtime_before)
        require(all("error" not in v for v in runtime_before.values()), "RUNTIME_PIN_FAILURE")
        initial_presence = presence(optional, dirs)
        save(out / "RUNTIME_BEFORE.json", runtime_before)
        save(out / "CONFIGURATION_BEFORE.json", initial_presence)
        save(out / "INTERPRETER_CONFIGURATION.json", config)
        all_before = {**scientific, **runtime_before}
        if mode == "build":
            tex_before = inventory(TEX_ROOTS)
            REGISTERED_INPUTS.update(tex_before["files"])
            require(all("error" not in v for v in tex_before["files"].values()), "TEX_RESOURCE_PIN_FAILURE")
            save(out / "TEX_RESOURCES_BEFORE.json", tex_before)
            all_before.update(tex_before["files"])
        save(out / "ALL_INPUTS_BEFORE_CHILDREN.json", all_before)
        link_rows, link_used = linkage(out, mode, all_before, ENV)
        observed |= link_used
        require(runtime_before == pins(runtime_before), "RUNTIME_CHANGED_DURING_LINKAGE")
        if mode == "pair":
            result, added, used = pair(out, all_before)
        else:
            result, added, used = build(out, all_before, tex_before)
        observed |= used
    except BaseException:
        failures.append({"stage": "execution", "traceback": traceback.format_exc()})
    finally:
        complete_before = {**REGISTERED_INPUTS, **all_before, **added}
        save(out / "ALL_INPUTS_INCLUDING_CAPSULES_BEFORE.json", complete_before)
        save(out / "ALL_COMMAND_RECORDS.json", COMMAND_RECORDS)
        try:
            final = pins(complete_before)
            save(out / "ALL_INPUTS_AFTER.json", final)
            require(complete_before and final == complete_before, "FULL_INPUT_BEFORE_AFTER")
        except BaseException:
            failures.append({"stage": "input_closure", "traceback": traceback.format_exc()})
        try:
            runtime_after, optional_after, dirs_after, config_after = runtime(mode)
            save(out / "RUNTIME_AFTER.json", runtime_after)
            require(runtime_before and runtime_before == runtime_after, "RUNTIME_INVENTORY_RECAPTURE")
            now = presence(optional_after, dirs_after)
            save(out / "CONFIGURATION_AFTER.json", now)
            require(initial_presence and now == initial_presence, "CONFIGURATION_PRESENCE_OR_SET_CHANGED")
        except BaseException:
            failures.append({"stage": "runtime_configuration_closure", "traceback": traceback.format_exc()})
        if mode == "build":
            try:
                now = inventory(TEX_ROOTS)
                save(out / "TEX_RESOURCES_AFTER.json", now)
                require(tex_before and tex_before == now, "TEX_RESOURCE_RECAPTURE")
            except BaseException:
                failures.append({"stage": "tex_closure", "traceback": traceback.format_exc()})
        try:
            late = observation("AFTER_CHILDREN_AND_CLOSURE")
            save(out / "PARENT_AFTER.json", late)
            observed |= consumed(late)
            observed |= COMMAND_OBSERVED
            closed = coverage(observed, complete_before, out)
            save(out / "OBSERVED_CLOSURE.json", closed)
            require(not closed["uncovered"] and not closed["bytecode"] and not late["cache_exists"], "OBSERVED_RUNTIME_CLOSURE", closed)
        except BaseException:
            failures.append({"stage": "observed_closure", "traceback": traceback.format_exc()})
        value = {"status": "PASS_ROOT_REVIEW_B_" + mode.upper() if not failures else "FAIL_PRESERVED",
                 "mode": mode, "failures": failures, "result": result,
                 "science_inputs": len(scientific), "runtime_files": len(runtime_before),
                 "known_all_inputs_including_capsules": len(complete_before),
                 "ldd_commands": sum(r["tag"].startswith("ldd_") for r in COMMAND_RECORDS),
                 "ldd_commands_completed_exit_zero": sum(r["tag"].startswith("ldd_") and r["command"]["exit"] == 0 for r in COMMAND_RECORDS),
                 "linkage_returned_complete": bool(link_rows), "tex_resources": len(tex_before.get("files", {})),
                 "scope": "Root executions of unchanged P209 B verifier; not a new independent review, verdict, delta or terminal acceptance.",
                 "observations": "Early/late parent and scientific-child modules/maps; sampled direct-child maps; conservative stdlib, OS libraries, loader/locale/gconv/config inventories; TeX per-pass .fls. No continuous or grandchild tracing, no OS-hermetic claim.",
                 "external": "HOLD_EXTERNAL"}
        save(out / "RECEIPT.json", value)
        seal = manifest(out)
        print(json.dumps({"status": value["status"], "mode": mode, "failures": failures,
                          "output": str(out), "seal": seal,
                          "summary": {k: v for k, v in result.items() if k not in {"replays", "commands", "comparisons"}}}, sort_keys=True))
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
