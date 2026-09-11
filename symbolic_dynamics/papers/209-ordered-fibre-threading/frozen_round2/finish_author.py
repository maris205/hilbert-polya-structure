#!/usr/bin/env python3
"""P209 documentary closure and raw comparisons only; no math/build imports.

Rechecks already-passing evidence and its current full input key, adopts the
actual PDF, verifies recorded views and logical Markdown destination paths,
and seals the author package. Does not execute a scientific verifier, TeX,
renderer, independent review or freeze. An unclosed comparison never seals.
"""
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import time
import traceback
from urllib.parse import unquote, urlsplit

SCRIPT = Path(__file__).resolve()
PAPER = SCRIPT.parent
ROOT = PAPER.parents[1]
OUT = PAPER / "author_finalization_01"
ENV = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8", "TZ": "UTC"}
READS = {}
CHECKS = 0
COMMANDS = []


def require(test, label, *witness):
    global CHECKS
    CHECKS += 1
    if not test:
        raise RuntimeError((label, witness))


def info(raw):
    path = Path(raw)
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return {"sha256": digest.hexdigest(), "bytes": path.stat().st_size,
            "resolved": str(path.resolve()),
            "symlink": os.readlink(path) if path.is_symlink() else None}


def remember(path):
    path = Path(path).absolute()
    value = info(path)
    if str(path) in READS:
        require(READS[str(path)] == value, "READ_INPUT_CHANGED", path)
    READS[str(path)] = value
    return value


def read_json(path):
    remember(path)
    return json.loads(Path(path).read_bytes())


def save(path, value):
    with Path(path).open("x") as stream:
        json.dump(value, stream, sort_keys=True, indent=2)
        stream.write("\n")


def check_manifest(base):
    target = base / "SHA256SUMS"
    remember(target)
    seen = set()
    for line in target.read_text().splitlines():
        digest, name = line.split("  ", 1)
        relative = Path(name)
        require(re.fullmatch(r"[0-9a-f]{64}", digest) and not relative.is_absolute()
                and ".." not in relative.parts and name != "SHA256SUMS" and name not in seen,
                "UNSAFE_OR_SELF_MANIFEST", target, name)
        seen.add(name)
        require(not (base / name).is_symlink() and remember(base / name)["sha256"] == digest,
                "MANIFEST_HASH", target, name)
    require(seen == {p.relative_to(base).as_posix() for p in base.rglob("*")
                     if p.is_file() and p != target}, "INCOMPLETE_MANIFEST", target)
    return {"manifest": str(target), "payloads": len(seen), "pin": info(target)}


def observation():
    modules = {name: {"file": getattr(module, "__file__", None),
                      "origin": getattr(getattr(module, "__spec__", None), "origin", None)}
               for name, module in sorted(sys.modules.items())}
    maps = Path("/proc/self/maps").read_text()
    files = {str(Path(line.split(None, 5)[5]).resolve()) for line in maps.splitlines()
             if len(line.split(None, 5)) == 6 and line.split(None, 5)[5].startswith("/")}
    for value in modules.values():
        for raw in value.values():
            if raw and Path(raw).is_file():
                files.add(str(Path(raw).resolve()))
    return {"modules": modules, "maps": maps, "consumed_files": sorted(files),
            "orig_argv": sys.orig_argv, "env": dict(os.environ), "cwd": os.getcwd(),
            "flags": str(sys.flags), "pycache_prefix": sys.pycache_prefix,
            "cache_exists": bool(sys.pycache_prefix and Path(sys.pycache_prefix).exists())}


def cmp(tag, left, right, known):
    inputs = {str(p): remember(p) for p in (Path("/usr/bin/cmp"), left, right)}
    require(inputs["/usr/bin/cmp"] == known["/usr/bin/cmp"], "CMP_RUNTIME_KEY_CHANGED")
    row = {"argv": ["/usr/bin/cmp", "--", str(left), str(right)], "cwd": str(OUT),
           "env": ENV, "started_epoch": time.time(), "exit": None,
           "stdout": tag + ".stdout", "stderr": tag + ".stderr", "inputs_before": inputs}
    save(OUT / (tag + ".attempt.json"), {**row, "stage": "PRE_SPAWN_ATTEMPT"})
    try:
        with (OUT / row["stdout"]).open("xb") as stdout, (OUT / row["stderr"]).open("xb") as stderr:
            process = subprocess.Popen(row["argv"], cwd=OUT, env=ENV, stdout=stdout, stderr=stderr)
            row["pid"] = process.pid
            row["exit"] = process.wait()
    except BaseException:
        row.update(status="UNCLOSED_NO_SEAL", failure=traceback.format_exc())
        save(OUT / (tag + ".UNCLOSED.json"), row)
        raise
    row.update(finished_epoch=time.time(), stdout_pin=info(OUT / row["stdout"]),
               stderr_pin=info(OUT / row["stderr"]))
    row["inputs_after"] = {p: info(p) for p in inputs}
    row["status"] = "PASS" if row["exit"] == 0 and row["inputs_after"] == inputs else "FAIL_PRESERVED"
    save(OUT / (tag + ".command.json"), row)
    COMMANDS.append(row)
    require(row["status"] == "PASS", "RAW_COMPARISON_FAILED", tag)


def configuration(base):
    before = read_json(base / "CONFIGURATION_BEFORE.json")
    require(before == read_json(base / "CONFIGURATION_AFTER.json"), "RECORDED_CONFIG_CHANGED", base)
    for raw, expected in before["optional"].items():
        path = Path(raw)
        value = {"exists": path.exists(), "is_file": path.is_file(), "resolved": str(path.resolve())}
        if path.is_file():
            value.update({k: info(path)[k] for k in ("sha256", "bytes")})
        require(value == expected, "CURRENT_CONFIG_PRESENCE_CHANGED", path)
    for raw, expected in before["directories"].items():
        path = Path(raw)
        names = sorted(str(p) for p in path.rglob("*") if p.is_file()) if path.is_dir() else None
        require(names == expected, "CURRENT_CONFIG_SET_CHANGED", path)
    return {"optional": len(before["optional"]), "directories": len(before["directories"])}


def links():
    mapping = read_json(PAPER / "source_context/MAPPING.json")
    origin_for = {str((PAPER / row["snapshot"]).resolve()): Path(origin)
                  for origin, row in mapping.items()}
    snapshot_for = {str(Path(origin).resolve()): (PAPER / row["snapshot"]).resolve()
                    for origin, row in mapping.items()}
    result = []
    for path in sorted(PAPER.rglob("*.md")):
        remember(path)
        text = path.read_text()
        text = re.sub(r"(?ms)^\s*```[^\n]*\n.*?^\s*```[^\n]*$", "", text)
        text = re.sub(r"`[^`]*`", "", text)
        semantic = origin_for.get(str(path.resolve()), path)
        for match in re.finditer(r"!?\[[^\]\n]*\]\((<[^>\n]+>|[^\s)]+)(?:\s+\"[^\"]*\")?\)", text):
            href = match.group(1).strip("<>")
            parsed = urlsplit(href)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            target = (semantic.parent / unquote(parsed.path)).resolve()
            actual = snapshot_for.get(str(target), target)
            require(actual.exists(), "MARKDOWN_DESTINATION_MISSING", path, href, actual)
            result.append({"document": str(path), "literal": href, "semantic_origin": str(semantic),
                           "resolved_destination": str(actual),
                           "scope": "Destination existence only; copied contexts resolve at their exact recorded origin, preferring pinned snapshots."})
    return result


def main():
    require(not OUT.exists() and not OUT.is_symlink() and not (PAPER / "SHA256SUMS").exists(), "REFUSE_EXISTING_FINALIZATION")
    require(not (PAPER / "main.pdf").exists() and not any(PAPER.glob("frozen_round*")), "REFUSE_PDF_OVERWRITE_OR_AUTHOR_FREEZE")
    require(dict(os.environ) == ENV and Path.cwd() == ROOT and Path(sys.executable).resolve() == Path("/usr/bin/python3.10"), "FINALIZER_ENV")
    require(sys.flags.isolated == 1 and sys.flags.no_site == 1 and sys.flags.optimize == 0 and sys.dont_write_bytecode
            and sys.pycache_prefix == str(OUT / "never_created_cache") and not Path(sys.pycache_prefix).exists(), "FINALIZER_FLAGS")
    OUT.mkdir(mode=0o700)
    shutil.copyfile(SCRIPT, OUT / "executed_source.py")
    save(OUT / "ATTEMPT.json", {"stage": "DOCUMENTARY_CLOSURE_STARTED", "observation": observation(),
                               "source": remember(SCRIPT), "copied_source": remember(OUT / "executed_source.py")})
    known, summaries, manifests = {}, {}, []
    try:
        for base in sorted(p.parent for p in PAPER.rglob("SHA256SUMS")):
            manifests.append(check_manifest(base))
        for label in ("author_pair_01", "author_build_01", "author_build_02"):
            base = PAPER / label
            receipt = read_json(base / "RECEIPT.json")
            require(receipt["status"] in {"PASS_AUTHOR_PAIR", "PASS_AUTHOR_BUILD"} and not receipt["failures"], "PRIOR_GATE_NOT_PASS", label)
            before = read_json(base / "ALL_INPUTS_INCLUDING_CAPSULES_BEFORE.json")
            require(before == read_json(base / "ALL_INPUTS_AFTER.json"), "RECORDED_FULL_KEY_CHANGED", label)
            for path, value in before.items():
                require(path not in known or known[path] == value, "INCONSISTENT_INITIAL_KEYS", path)
                known[path] = value
            require(read_json(base / "RUNTIME_BEFORE.json") == read_json(base / "RUNTIME_AFTER.json"), "RECORDED_RUNTIME_CHANGED", label)
            closed = read_json(base / "OBSERVED_CLOSURE.json")
            require(not closed["uncovered"] and not closed["bytecode"], "PRIOR_OBSERVATION_GAP", label)
            commands = read_json(base / "ALL_COMMAND_RECORDS.json")
            for entry in commands:
                row, folder = entry["command"], Path(entry["folder"])
                require(row["exit"] == 0 and row["process_outcome"] == "COMPLETED" and not row["cleanup"], "ORIGINAL_COMMAND_NOT_ZERO", entry["tag"])
                for kind in ("stdout", "stderr"):
                    got = info(folder / row[kind])
                    require({k: got[k] for k in ("sha256", "bytes")} == row[kind + "_info"], "ORIGINAL_STREAM_CHANGED", entry["tag"], kind)
            summaries[label] = {"status": receipt["status"], "commands": len(commands),
                                "known_inputs": len(before), "configuration": configuration(base)}
            if label.startswith("author_build"):
                tex = read_json(base / "TEX_RESOURCES_BEFORE.json")
                require(tex == read_json(base / "TEX_RESOURCES_AFTER.json"), "RECORDED_TEX_CHANGED", label)
                require(all(Path(p).exists() == v for p, v in tex["roots"].items()), "CURRENT_TEX_ROOT_PRESENCE", label)
                names = {str(p) for raw in tex["roots"] if Path(raw).is_dir()
                         for p in Path(raw).rglob("*") if p.is_file()}
                require(names == set(tex["files"]), "CURRENT_TEX_RESOURCE_SET", label)
        known[str(SCRIPT)] = info(SCRIPT)
        known[str(OUT / "executed_source.py")] = info(OUT / "executed_source.py")
        for path, expected in known.items():
            require(info(path) == expected, "CURRENT_FULL_INPUT_CHANGED", path)
        save(OUT / "KNOWN_INPUTS_BEFORE_COMPARISONS.json", known)
        early = observation()
        covered = {p["resolved"] for p in known.values()}
        require(set(early["consumed_files"]) <= covered, "FINALIZER_RUNTIME_UNCOVERED", sorted(set(early["consumed_files"]) - covered))
        save(OUT / "RUNTIME_BEFORE.json", early)
        one = PAPER / "author_pair_01/replay_01/producer.stdout"
        two = PAPER / "author_pair_01/replay_02/producer.stdout"
        canonical = PAPER / "CANONICAL.json"
        cmp("canonical_pair", one, two, known)
        cmp("canonical_01", one, canonical, known)
        cmp("canonical_02", two, canonical, known)
        pdf1 = PAPER / "author_build_01/cold_build/main.pdf"
        pdf2 = PAPER / "author_build_02/cold_build/main.pdf"
        cmp("pdf_pair", pdf1, pdf2, known)
        with pdf2.open("rb") as source, (PAPER / "main.pdf").open("xb") as destination:
            shutil.copyfileobj(source, destination)
        save(OUT / "PDF_ADOPTION.json", {"action": "COPY_ACTUAL_BUILD_02_PDF_AFTER_RAW_PAIR_CMP",
             "source": str(pdf2), "source_pin": remember(pdf2), "destination": str(PAPER / "main.pdf"),
             "destination_pin": remember(PAPER / "main.pdf")})
        cmp("pdf_live_01", pdf1, PAPER / "main.pdf", known)
        cmp("pdf_live_02", pdf2, PAPER / "main.pdf", known)
        views = read_json(PAPER / "PAGE_VIEWS.json")
        require(views["status"] == "PASS_ACTUAL_AUTHOR_PAGE_VIEWS" and len(views["records"]) == 8
                and views["actual_individual_image_views"] == 8, "VIEW_RECEIPT_CENSUS")
        for row in views["records"]:
            require(row["actual_individual_view"] and remember(PAPER / row["image"])["sha256"] == row["image_sha256"]
                    and remember(PAPER / row["pdf"])["sha256"] == row["pdf_sha256"], "VIEW_PIN_MISMATCH", row)
        for page in range(1, 5):
            cmp("png_" + str(page), PAPER / ("author_build_01/cold_build/pages/page-%d.png" % page),
                PAPER / ("author_build_02/cold_build/pages/page-%d.png" % page), known)
        destinations = links()
        save(OUT / "LINK_DESTINATIONS.json", destinations)
        after = {path: info(path) for path in known}
        save(OUT / "KNOWN_INPUTS_AFTER_COMPARISONS.json", after)
        require(after == known, "FINAL_FULL_KEY_CHANGED")
        late = observation()
        save(OUT / "RUNTIME_AFTER.json", late)
        require(set(late["consumed_files"]) <= covered and not late["cache_exists"], "FINAL_RUNTIME_OR_CACHE")
        for path, expected in READS.items():
            require(info(path) == expected, "FINAL_READ_INPUT_CHANGED", path)
        save(OUT / "READ_INPUT_PINS.json", READS)
        save(OUT / "RECEIPT.json", {"status": "PASS_DOCUMENTARY_RAW_COMPARISON_AND_PDF_ADOPTION", "checks": CHECKS,
             "original_submanifests": manifests, "original_packages": summaries, "current_known_inputs": len(known),
             "new_raw_comparisons": COMMANDS, "actual_author_view_records_checked": 8,
             "markdown_destinations_checked": len(destinations), "read_inputs_rechecked": len(READS),
             "scope": "No scientific verifier, build, renderer, new view, review or freeze executed here; this checks original passing evidence and the actual author viewing report.",
             "runtime_scope": "Finalizer early/late modules/maps are covered by the revalidated original runtime inventory; no continuous trace or OS-hermetic claim.",
             "external": "HOLD_EXTERNAL"})
        paths = sorted(p for p in PAPER.rglob("*") if p.is_file())
        require(all(not p.is_symlink() for p in paths), "FINAL_PACKAGE_SYMLINK")
        with (PAPER / "SHA256SUMS").open("x") as stream:
            for path in paths:
                stream.write(info(path)["sha256"] + "  " + path.relative_to(PAPER).as_posix() + "\n")
        seal = check_manifest(PAPER)
        print(json.dumps({"status": "PASS_AUTHOR_PACKAGE_SEALED", "seal": seal,
                          "current_known_inputs": len(known), "raw_comparisons": len(COMMANDS),
                          "markdown_destinations": len(destinations), "checks": CHECKS}, sort_keys=True))
        return 0
    except BaseException:
        save(OUT / "FAILURE_UNSEALED.json", {"status": "FAILURE_OR_UNCLOSED_NO_FINAL_SEAL", "traceback": traceback.format_exc(),
             "known_inputs_collected": len(known), "completed_comparisons": COMMANDS,
             "scope": "Preserved failure; no retrospective PASS or silent replacement."})
        raise


if __name__ == "__main__":
    raise SystemExit(main())
