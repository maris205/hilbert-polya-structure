#!/usr/bin/python3.10
"""Read-only artifact audit of three named negative desks; never imports science.

Only subprocesses: two inspected documentary verify entry points and four
local pdftotext extractions. No writes, network, shell, or science execution.
The result is JSON on stdout; exit 1 denotes a new integrity/check failure.
"""
import base64
import datetime
import hashlib
import json
import os
import pathlib
import re
import shlex
import subprocess
import sys
import time
import traceback

ROOT = pathlib.Path("/root/autodl-tmp/symbolic_dynamics")
SCOUT = ROOT / "docs/papers211_215_sequence/scouting"
OWN = ROOT / "docs/papers211_215_sequence/qa/transport_network_nonlinear_artifact_audit"
C = SCOUT / "circular_interval_transport_desk"
N = SCOUT / "finite_network_rewrite_desk"
F = SCOUT / "finite_nonlinear_feedback_fresh_desk"
INTAKE = SCOUT / "root_reception/transport_network_nonlinear"
ENV = {"LANG": "C", "LC_ALL": "C", "PATH": "/usr/bin:/bin", "TZ": "UTC"}
PYTHON = "/usr/bin/python3.10"
C_INPUTS = [
    ("p198", "papers/198-cyclic-monomer-matching/main.tex", [[73, 205]]),
    ("mrt", "docs/papers204_208_sequence/scouting/finite_systems_thirtieth/PROOF_PACKAGE.md", [[1, 160]]),
    ("omd_hur", "docs/papers162_166_sequence/scouting/replacement_matchings_incidence/SCOUT.md", [[17, 45], [82, 89]]),
    ("uuc_intake", "docs/papers211_215_sequence/scouting/transport_lane/INTAKE.md", [[1, 200]]),
    ("uuc_proof", "docs/papers211_215_sequence/scouting/transport_lane/PROOF_PACKAGE.md", [[1, 220]]),
    ("planar_handoff", "docs/papers211_215_sequence/scouting/planar_matching_lane/HANDOFF.md", [[1, 180]]),
    ("planar_proof", "docs/papers211_215_sequence/scouting/planar_matching_lane/PROOF_PACKAGE.md", [[1, 180]]),
]
N_INPUTS = [
    ("docs/papers117_121_sequence/scouting/COMBINATORIAL_SCOUT.md", [[36, 74], [297, 311]]),
    ("docs/papers204_208_sequence/scouting/finite_systems_sixteenth/PROOF_AND_DISPOSITION.md", [[85, 250], [310, 331]]),
    ("papers/205-conflict-triggered-cyclic-increments/PROOF_PACKAGE.md", [[1, 140]]),
]
F_PINS = [
    "docs/papers204_208_sequence/scouting/algebra_third/PROOF_AND_ADAPTER_NOTES.md",
    "docs/papers204_208_sequence/scouting/algebra_third/SOURCE_AND_COLLISION_NOTES.md",
    "docs/papers204_208_sequence/scouting/finite_systems_thirty_seventh/INTAKE.md",
    "docs/papers204_208_sequence/scouting/finite_systems_thirty_seventh/SCOUT_REPORT.md",
    "papers/125-quadratic-state-shear/main.pdf",
    "papers/205-conflict-triggered-cyclic-increments/main.pdf",
    "docs/papers211_215_sequence/scouting/finite_allocation_lane/INTAKE.md",
    "docs/papers211_215_sequence/scouting/nonlinear_lane/INTAKE.md",
]
F_EARLY_ONLY = "docs/papers204_208_sequence/scouting/algebra_third/SCOUT_REPORT.md"
F_MISSING = "docs/papers211_215_sequence/scouting/resource_allocation_lane/INTAKE.md"
EXTERNAL = sorted(set([p for _, p, _ in C_INPUTS] + [p for p, _ in N_INPUTS] + F_PINS + [F_EARLY_ONLY]))
EXECUTABLES = [PYTHON, "/usr/bin/pdftotext", "/usr/bin/sha256sum", "/usr/bin/sed", "/usr/bin/cmp"]
N_V1 = {"HANDOFF.md", "BOUNDARIES.md", "capture.py", "SOURCE_RETURNS.json",
        "NATIVE_EVIDENCE.json", "METADATA_CORRECTION.md",
        "initial_draft/BOUNDARIES.md", "initial_draft/capture.py"}
N_V2 = N_V1 | {"MANIFEST.json", "FINAL_HANDOFF.md", "capture_v2.py"}

RESULT = {
    "schema": "transport-network-nonlinear-artifact-audit-v1",
    "audit_kind": "read_only_artifact_integrity_not_scientific_review",
    "science_executions": 0, "science_imports": 0, "network_requests": 0,
    "authorship": {
        "auditor": "/root/round211_rational_scout/relation_primary_sources",
        "authored_these_packages_or_checkers": False,
        "prior_read": "Nonlinear HANDOFF.md read during an earlier algebraic subtraction desk.",
        "relationship": "Nonlinear desk author is auditor's parent agent /root/round211_rational_scout; circular/network author is /root/round211_queue_scout.",
        "not_claimed": "Blind independence, a science review, or certification of own mathematics.",
        "p211_boundary": "No A package access or P211 mathematical contribution in this audit.",
    },
    "checks": [], "new_failures": [], "preserved_failures_and_limits": [],
    "source_return_shapes": [], "nonlinear_command_records": [],
    "new_documentary_processes": [],
}
CHECK_COUNT = 0


def sha(data):
    return hashlib.sha256(data).hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def need(condition, label):
    global CHECK_COUNT
    CHECK_COUNT += 1
    if not condition:
        raise AssertionError(label)


def file_pin(path):
    path = pathlib.Path(path)
    raw = path.read_bytes()
    return {"path": str(path), "resolved_path": str(path.resolve()),
            "bytes": len(raw), "sha256": sha(raw),
            "mode": oct(path.stat().st_mode & 0o777)}


def simple_pin(path):
    raw = pathlib.Path(path).read_bytes()
    return {"bytes": len(raw), "sha256": sha(raw)}


def load(path):
    return json.loads(pathlib.Path(path).read_bytes())


def inventory(base, excluded=()):
    rows = []
    for path in sorted(base.rglob("*")):
        need(not path.is_symlink(), "symlink not allowed: " + str(path))
        if path.is_file() and path.relative_to(base).as_posix() not in excluded:
            rows.append({"path": path.relative_to(base).as_posix(), **simple_pin(path)})
    return rows


def safe_relative(base, name):
    need(isinstance(name, str) and name and not pathlib.PurePath(name).is_absolute(), "relative path required")
    need(".." not in pathlib.PurePath(name).parts, "parent traversal forbidden")
    return base / name


def runtime_modules():
    paths = set()
    for module in list(sys.modules.values()):
        value = getattr(module, "__file__", None)
        if value:
            path = pathlib.Path(value)
            if path.is_file():
                if path.resolve() == pathlib.Path(__file__).resolve():
                    continue  # The entry script is already a separate keyed input.
                need(not str(path).startswith(str(ROOT)), "unexpected workspace module import")
                paths.add(str(path))
    return sorted(paths)


def input_key():
    rows = []
    for base in (C, N, F):
        for row in inventory(base):
            rows.append({"role": "complete_desk_file", **file_pin(base / row["path"])})
    for relative in EXTERNAL:
        rows.append({"role": "referenced_original", **file_pin(ROOT / relative)})
    for name in ("INTAKE.md", "CIRCULAR_VERIFY_NATIVE01.json", "NETWORK_VERIFY_NATIVE01.json"):
        rows.append({"role": "root_pending_intake", **file_pin(INTAKE / name)})
    rows.append({"role": "auditor_entry", **file_pin(pathlib.Path(__file__).resolve())})
    for path in EXECUTABLES:
        rows.append({"role": "documentary_runtime_executable", **file_pin(path)})
    for path in runtime_modules():
        rows.append({"role": "loaded_auditor_python_module", **file_pin(path)})
    rows.sort(key=lambda r: (r["role"], r["path"]))
    missing = ROOT / F_MISSING
    value = {
        "scope": [str(C), str(N), str(F)],
        "input_files": rows,
        "recorded_missing_path_currently_exists": missing.exists(),
        "current_missing_path": str(missing),
        "environment": ENV, "python_version": sys.version,
        "python_flags": {"isolated": sys.flags.isolated, "no_site": sys.flags.no_site,
                         "dont_write_bytecode": sys.dont_write_bytecode},
        "entry_argv": [PYTHON, "-I", "-S", "-B", str(pathlib.Path(__file__).resolve())],
        "limits": "Complete declared artifact/original/entry-point key plus observed loaded Python modules; not a hermetic OS/shared-library or historical environment certificate.",
    }
    return value, sha(canonical(value))


def stream(raw):
    return {"encoding": "base64", "base64": base64.b64encode(raw).decode("ascii"),
            "bytes": len(raw), "sha256": sha(raw)}


def run_documentary(argv, purpose):
    allowed_verify = [
        [PYTHON, "-I", "-S", "-B", str(C / "capture.py"), "verify"],
        [PYTHON, "-I", "-S", "-B", str(N / "capture_v2.py"), "verify"],
    ]
    allowed_pdf = [
        ["/usr/bin/pdftotext", "-f", "1", "-l", str(last), path, "-"]
        for path in F_PINS[4:6] for last in (1, 3)
    ]
    need(argv in allowed_verify + allowed_pdf, "subprocess outside explicit documentary allowlist")
    started = time.time_ns()
    child = subprocess.run(argv, cwd=ROOT, env=ENV, stdin=subprocess.DEVNULL,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                           timeout=30, check=False)
    row = {"purpose": purpose, "argv": argv, "cwd": str(ROOT), "environment": ENV,
           "started_unix_ns": started, "finished_unix_ns": time.time_ns(),
           "returncode": child.returncode, "executable": file_pin(argv[0]),
           "stdout": stream(child.stdout), "stderr": stream(child.stderr)}
    RESULT["new_documentary_processes"].append(row)
    need(child.returncode == 0, purpose + ": nonzero return retained")
    need(not child.stderr, purpose + ": nonempty stderr retained")
    return child.stdout


def excerpt(raw, ranges):
    lines = raw.splitlines(keepends=True)
    return b"".join(b"".join(lines[first - 1:last]) for first, last in ranges)


def sed_argv(path, ranges):
    argv = ["/usr/bin/sed", "-n"]
    for first, last in ranges:
        argv.extend(["-e", str(first) + "," + str(last) + "p"])
    return argv + [path]


def decode_native(row):
    need(row["encoding"] == "utf-8", "native encoding")
    raw = row["text"].encode("utf-8")
    need(len(raw) == row["bytes"] and sha(raw) == row["sha256"], "native stream byte/hash")
    return raw


def source_shape(label, request, body, kind):
    need(isinstance(body, str) and bool(body), label + ": nonempty tool-return string")
    if request is not None:
        need(isinstance(request, dict) and bool(request), label + ": request object")
    RESULT["source_return_shapes"].append({
        "record": label, "kind": kind, "request_present": request is not None,
        "request_keys": sorted(request) if isinstance(request, dict) else None,
        "returned_utf8": {"bytes": len(body.encode("utf-8")), "sha256": sha(body.encode("utf-8"))},
        "known_access_failure_markers": [
            word for word in ("404", "Internal Error", "Failed to fetch", "Unable to resolve",
                              "No matching text", "No match found", "SSL_ERROR_SYSCALL")
            if word.lower() in body.lower()
        ],
        "not_claimed": "Raw HTTP, whole-source acquisition, authenticity beyond the pinned archive, or actual full/visual reading.",
    })


def check_circular():
    manifest = load(C / "MANIFEST.json")
    actual = inventory(C, ["MANIFEST.json"])
    need(manifest["excluded_only"] == ["MANIFEST.json"], "circular manifest exclusion")
    need(manifest["rows"] == actual and len(actual) == manifest["payload_count"] == 40, "circular complete inventory")
    need(manifest["payload_bytes"] == sum(r["bytes"] for r in actual) == 322468, "circular byte count")
    inputs = load(C / "HISTORICAL_INPUTS.json")
    need(inputs["origin_base"] == str(ROOT), "circular original base")
    pins = inputs["rows"]
    need([(p["key"], p["original"], p["read_line_ranges"]) for p in pins] == C_INPUTS, "circular literal original/range bindings")
    for pin in pins:
        snapshot = "snapshots/" + pin["original"]
        need(pin["snapshot"] == snapshot, "circular exact snapshot path")
        original = (ROOT / pin["original"]).read_bytes()
        need((C / snapshot).read_bytes() == original, "circular original/copy raw equality")
        need({"bytes": len(original), "sha256": sha(original)} == {k: pin[k] for k in ("bytes", "sha256")}, "circular original pin")
    receipt = load(C / "native/RECEIPT.json")
    need(receipt["kind"] == "read_only_documentary_no_scientific_execution", "circular capture kind")
    for role in ("driver", "interpreter"):
        pin = receipt[role]
        expected_path = str(C / "capture.py") if role == "driver" else PYTHON
        need(pin["path"] == expected_path, "circular driver/interpreter path")
        need(simple_pin(expected_path) == {k: pin[k] for k in ("bytes", "sha256")}, "circular driver/interpreter pin")
    paths = [p for _, p, _ in C_INPUTS]
    expected_hashes = "".join(p["sha256"] + "  " + p["original"] + "\n" for p in pins).encode("ascii")
    expected_commands = [("01_before", ["/usr/bin/sha256sum", *paths], expected_hashes, None)]
    for index, (name, path, ranges) in enumerate(C_INPUTS, 2):
        binding = {"original": path, "snapshot": "snapshots/" + path, "line_ranges": ranges}
        expected_commands.append((str(index).zfill(2) + "_" + name, sed_argv(path, ranges),
                                  excerpt((ROOT / path).read_bytes(), ranges), binding))
    expected_commands += [
        ("09_after", ["/usr/bin/sha256sum", *paths], expected_hashes, None),
        ("10_compare", ["/usr/bin/cmp", "-s", str(C / "native/01_before.stdout"),
                        str(C / "native/09_after.stdout")], b"", None),
    ]
    need(len(receipt["commands"]) == 10, "circular native census")
    for record, (key, argv, raw, binding) in zip(receipt["commands"], expected_commands):
        need(record["key"] == key and record["argv"] == argv, "circular exact native argv " + key)
        need(record["cwd"] == str(ROOT) and record["environment"] == ENV, "circular cwd/env " + key)
        need(record["returncode"] == 0, "circular archived returncode " + key)
        need(isinstance(record["started_unix_ns"], int) and record["started_unix_ns"] <= record["finished_unix_ns"], "circular chronology")
        need(record["executable"]["path"] == argv[0], "circular executable path")
        need(simple_pin(argv[0]) == {k: record["executable"][k] for k in ("bytes", "sha256")}, "circular executable pin")
        for which in ("stdout", "stderr"):
            pin = record[which]
            need(pin["path"] == "native/" + key + "." + which, "circular native path")
            data = (C / pin["path"]).read_bytes()
            need(simple_pin(C / pin["path"]) == {k: pin[k] for k in ("bytes", "sha256")}, "circular stream pin")
            need(data == (raw if which == "stdout" else b""), "circular exact raw stream")
        need(record.get("excerpt_binding") == binding, "circular range metadata")
    for index in range(1, 8):
        name = "sources/web_" + str(index).zfill(2) + ".json"
        row = load(C / name)
        need(row["record_kind"] == "actual_web_tool_response_not_raw_http", "circular source kind")
        source_shape("circular/" + name, row["request"], row["tool_result"], row["record_kind"])
    output = run_documentary([PYTHON, "-I", "-S", "-B", str(C / "capture.py"), "verify"], "reused circular documentary verify")
    prior = load(INTAKE / "CIRCULAR_VERIFY_NATIVE01.json")
    need(prior["request"]["cmd"] == PYTHON + " -I -S -B " + str((C / "capture.py").relative_to(ROOT)) + " verify", "root circular prior command")
    need(prior["request"]["workdir"] == str(ROOT) and prior["result"]["exit_code"] == 0, "root circular prior envelope")
    need(output == prior["result"]["output"].encode("utf-8"), "circular current raw stdout / prior tool-decoded UTF-8 equality")
    RESULT["checks"].append({"desk": C.name, "payloads": 40, "payload_bytes": 322468,
                             "original_pins_and_copies": 7, "exact_native_records": 10,
                             "raw_excerpt_checks": 7, "source_returns": 7,
                             "existing_checker": "capture.py verify", "status": "PASS"})


def check_network():
    actual = inventory(N, ["MANIFEST_V2.json"])
    manifest = load(N / "MANIFEST_V2.json")
    need({p["path"] for p in actual} == N_V2, "network current explicit file universe")
    need(manifest["excluded_exactly"] == ["MANIFEST_V2.json"], "network v2 exclusion")
    need(manifest["payloads"] == actual and manifest["payload_count"] == 11, "network v2 complete inventory")
    need(manifest["payload_bytes"] == sum(r["bytes"] for r in actual) == 243501, "network v2 bytes")
    first = load(N / "MANIFEST.json")
    need(first["excluded_exactly"] == ["MANIFEST.json"], "network v1 exclusion")
    need({p["path"] for p in first["payloads"]} == N_V1 and first["payload_count"] == 8, "network v1 exact subset")
    need(first["payload_bytes"] == 233267, "network v1 bytes")
    for row in first["payloads"]:
        need(simple_pin(safe_relative(N, row["path"])) == {k: row[k] for k in ("bytes", "sha256")}, "network initial seal unchanged")
    receipt = load(N / "NATIVE_EVIDENCE.json")
    need(receipt["scientific_runs"] == receipt["fresh_literals"] == 0 and receipt["runtime_reuse_certificate"] is False, "network declared scope")
    pins = receipt["original_pins"]
    need([p["path"] for p in pins] == [p for p, _ in N_INPUTS], "network exact original list")
    for pin in pins:
        need(simple_pin(ROOT / pin["path"]) == {k: pin[k] for k in ("bytes", "sha256")}, "network original pin")
    names = ["capture.py", "HANDOFF.md", "BOUNDARIES.md", "SOURCE_RETURNS.json"]
    need([p["path"] for p in receipt["collector_inputs"]] == [str((N / n).relative_to(ROOT)) for n in names], "network collector paths")
    for pin, name in zip(receipt["collector_inputs"], names):
        actual_path = N / "initial_draft" / name if name in ("capture.py", "BOUNDARIES.md") else N / name
        need(simple_pin(actual_path) == {k: pin[k] for k in ("bytes", "sha256")}, "network historical collector mapping")
    native = receipt["native_commands"]
    need(len(native) == 4, "network native census")
    hashes = "".join(p["sha256"] + "  " + p["path"] + "\n" for p in pins).encode("ascii")
    for index, record in enumerate(native):
        need(record["cwd"] == str(ROOT) and record["environment"] == ENV, "network cwd/env")
        need(record["exit_code"] == 0 and decode_native(record["stderr"]) == b"", "network archived success/empty stderr")
        need(record["started_utc"] <= record["ended_utc"], "network chronology")
        if index == 0:
            need(record["argv"] == ["/usr/bin/sha256sum"] + [p for p, _ in N_INPUTS], "network hash argv")
            need(decode_native(record["stdout"]) == hashes, "network hash raw stdout")
        else:
            path, ranges = N_INPUTS[index - 1]
            need(record["argv"] == sed_argv(path, ranges), "network exact excerpt argv")
            need(record["selection"] == {"original": path, "inclusive_line_ranges": ranges, "exact_raw_bytes_equal": True}, "network selection metadata")
            need(decode_native(record["stdout"]) == excerpt((ROOT / path).read_bytes(), ranges), "network raw excerpt equality")
    sources = load(N / "SOURCE_RETURNS.json")
    need(sources["kind"] == "actual_tool_responses_not_raw_http", "network source kind")
    need([r["id"] for r in sources["records"]] == list(range(1, 7)), "network source census")
    for row in sources["records"]:
        source_shape("network/source_" + str(row["id"]), row["request"], row["tool_result"], sources["kind"])
    metadata = sources["records"][3]["tool_result"]
    need("Phase transition in firefly cellular automata on finite trees" in metadata, "network first erratum source binding")
    need("completeness of Graph Local Complementation" in metadata and "Pablo Concha-Vega" in metadata, "network second erratum source binding")
    need("Synchronization of finite-state pulse-coupled oscillators" in (N / "initial_draft/BOUNDARIES.md").read_text(), "network original first metadata error preserved")
    need("P-completeness of Graph Local" in (N / "FINAL_HANDOFF.md").read_text(), "network additive final correction")
    output = run_documentary([PYTHON, "-I", "-S", "-B", str(N / "capture_v2.py"), "verify"], "reused network v2 documentary verify")
    prior = load(INTAKE / "NETWORK_VERIFY_NATIVE01.json")
    need(prior["request"]["cmd"] == PYTHON + " -I -S -B " + str((N / "capture_v2.py").relative_to(ROOT)) + " verify", "root network prior command")
    need(prior["request"]["workdir"] == str(ROOT) and prior["result"]["exit_code"] == 0, "root network prior envelope")
    need(output == prior["result"]["output"].encode("utf-8"), "network current raw stdout / prior tool-decoded UTF-8 equality")
    RESULT["preserved_failures_and_limits"].append({
        "id": "TNN-L01", "scope": "network", "kind": "preserved_author_metadata_errors",
        "detail": "Both citation errata and original first seal survive. Original capture.py verify targets the historical eight-payload directory and was not executed against the enlarged directory. V2 is controlling.",
    })
    RESULT["checks"].append({"desk": N.name, "payloads": 11, "payload_bytes": 243501,
                             "historical_first_seal_payloads": 8, "original_pins": 3,
                             "exact_native_records": 4, "raw_excerpt_checks": 3,
                             "source_returns": 6, "existing_checker": "capture_v2.py verify", "status": "PASS"})


def parse_sha_file(path):
    rows = []
    for line in pathlib.Path(path).read_text(encoding="utf-8").splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        need(match is not None, "strict SHA-256 line syntax: " + str(path))
        rows.append({"path": match.group(2), "sha256": match.group(1)})
    need(len({r["path"] for r in rows}) == len(rows), "duplicate manifest/pin path")
    return rows


def check_nonlinear():
    manifest = parse_sha_file(F / "MANIFEST.sha256")
    actual = inventory(F, ["MANIFEST.sha256"])
    need({r["path"] for r in manifest} == {r["path"] for r in actual}
         == {"HANDOFF.md", "INPUTPINS.sha256", "OLD_NATIVE_RETURNS.json", "PRIMARY_RETURNS.json"},
         "nonlinear complete nonself inventory")
    for row in manifest:
        need(sha(safe_relative(F, row["path"]).read_bytes()) == row["sha256"], "nonlinear payload pin")
    pins = parse_sha_file(F / "INPUTPINS.sha256")
    need([p["path"] for p in pins] == F_PINS, "nonlinear exact original pin list")
    for pin in pins:
        need(sha((ROOT / pin["path"]).read_bytes()) == pin["sha256"], "nonlinear original pin")
    old = load(F / "OLD_NATIVE_RETURNS.json")
    need(old["cwd"] == str(ROOT), "nonlinear requested cwd")
    need("combined stdout/stderr" in old["scope"] and "not independent raw stream" in old["scope"], "nonlinear stream limit disclosed")
    need(len(old["earlier_selected"]) == 12 and len(old["closing_excerpts"]) == 8, "nonlinear command census")
    hashes = (F / "INPUTPINS.sha256").read_bytes()
    hash_command = "/usr/bin/sha256sum " + " ".join(F_PINS)
    for name in ("closing_before", "closing_after"):
        row = old[name]
        need(row["cmd"] == hash_command and row["result"]["exit_code"] == 0, "nonlinear closing hash command")
        need(row["result"]["output"].encode("utf-8") == hashes, "nonlinear closing hash decoded bytes")
    need(old["closing_before"]["result"]["output"] == old["closing_after"]["result"]["output"]
         and old["closing_hash_outputs_identical"] is True, "nonlinear recorded closing hashes identical")
    pdf_cache = {}
    counts = {"sed_current_byte_comparisons": 0, "pdf_current_byte_comparisons": 0,
              "preserved_missing_path_records": 0}
    rows = [("earlier_" + str(i), r) for i, r in enumerate(old["earlier_selected"], 1)]
    rows += [("closing_" + str(i), r) for i, r in enumerate(old["closing_excerpts"], 1)]
    for label, row in rows:
        need(isinstance(row["cmd"], str) and isinstance(row["result"]["output"], str), "nonlinear native shape")
        interpreted = shlex.split(row["cmd"])
        archived = row["result"]["output"].encode("utf-8")
        rc = row["result"]["exit_code"]
        record = {"label": label, "recorded_cmd": row["cmd"],
                  "requested_cwd_from_archive": old["cwd"],
                  "parsed_argv_interpretation_not_recorded_native_argv": interpreted,
                  "recorded_exit_code": rc,
                  "tool_decoded_output_utf8": {"bytes": len(archived), "sha256": sha(archived)}}
        if interpreted[0] == "sed":
            need(len(interpreted) == 4 and interpreted[1] == "-n", "nonlinear sed shape")
            path = interpreted[-1]
            need(path in F_PINS + [F_EARLY_ONLY, F_MISSING], "nonlinear sed reference outside explicit scope")
            if path == F_MISSING:
                need(label.startswith("earlier_") and rc == 2, "preserved missing-file return")
                need(b"No such file or directory" in archived and path.encode() in archived, "preserved missing-file message")
                record["comparison"] = "PRESERVED_FAILURE_NOT_REEXECUTED"
                counts["preserved_missing_path_records"] += 1
            else:
                ranges = []
                for part in interpreted[2].split(";"):
                    match = re.fullmatch(r"(\d+),(\d+)p", part)
                    need(match is not None, "nonlinear sed range grammar")
                    first, last = map(int, match.groups())
                    need(1 <= first <= last, "nonlinear sed range bounds")
                    ranges.append([first, last])
                need(rc == 0, "nonlinear archived sed status")
                expected = excerpt((ROOT / path).read_bytes(), ranges)
                need(archived == expected, "nonlinear decoded output / current raw text excerpt equality " + label)
                record["comparison"] = "CURRENT_RAW_EXCERPT_EQUALS_ARCHIVED_TOOL_OUTPUT_UTF8"
                record["original_had_closing_full_file_pin"] = path in F_PINS
                counts["sed_current_byte_comparisons"] += 1
        else:
            need(interpreted[0] == "pdftotext" and len(interpreted) == 7, "nonlinear PDF command grammar")
            need(interpreted[1:4] == ["-f", "1", "-l"] and interpreted[4] in ("1", "3")
                 and interpreted[5] in F_PINS[4:6] and interpreted[6] == "-", "nonlinear PDF command binding")
            need(rc == 0, "nonlinear archived PDF exit")
            argv = ["/usr/bin/pdftotext"] + interpreted[1:]
            key = tuple(argv)
            if key not in pdf_cache:
                pdf_cache[key] = run_documentary(argv, "new local PDF text comparison " + label)
            need(pdf_cache[key] == archived, "nonlinear current PDF raw stdout / archived decoded output equality " + label)
            record["comparison"] = "CURRENT_PDF_RAW_STDOUT_EQUALS_ARCHIVED_TOOL_OUTPUT_UTF8"
            counts["pdf_current_byte_comparisons"] += 1
        RESULT["nonlinear_command_records"].append(record)
    need(counts == {"sed_current_byte_comparisons": 15, "pdf_current_byte_comparisons": 4,
                    "preserved_missing_path_records": 1}, "nonlinear comparison census")
    for name in ("closing_before", "closing_after"):
        row = old[name]
        RESULT["nonlinear_command_records"].append({
            "label": name, "recorded_cmd": row["cmd"], "requested_cwd_from_archive": old["cwd"],
            "parsed_argv_interpretation_not_recorded_native_argv": shlex.split(row["cmd"]),
            "recorded_exit_code": row["result"]["exit_code"],
            "tool_decoded_output_utf8": {"bytes": len(hashes), "sha256": sha(hashes)},
            "comparison": "ARCHIVED_TOOL_OUTPUT_UTF8_EQUALS_CLOSING_INPUTPIN_BYTES",
        })
    need(old["assembly_failure"]["observed"] == "ReferenceError: TextEncoder is not defined", "nonlinear assembly failure preserved")
    sources = load(F / "PRIMARY_RETURNS.json")
    need(len(sources["browser"]) == 3 and len(sources["native_source"]) == 2, "nonlinear source record census")
    for row in sources["browser"]:
        need(row["tool"] == "web.run" and set(row) == {"label", "tool", "return"}, "nonlinear browser record shape")
        source_shape("nonlinear/" + row["label"], None, row["return"], "browser_return_without_request_object")
    for index, row in enumerate(sources["native_source"]):
        launch, completion = row["launch"], row["completion"]
        end = " -f 1 -l 5 - -" if index == 0 else " -f 6 -l 7 - -"
        expected = "set -o pipefail\n/root/miniconda3/bin/curl --fail --location --max-time 20 https://maths.qmul.ac.uk/~fvivaldi/research/Symmetry.pdf | /usr/bin/pdftotext" + end
        need(launch["cmd"] == expected, "nonlinear archived source pipeline command")
        need(isinstance(launch["result"]["session_id"], int), "nonlinear source launch session")
        need("exit_code" not in launch["result"], "nonlinear launch is not a completed process")
        need(completion["exit_code"] == (0 if index == 0 else 1), "nonlinear completed pipeline aggregate exit")
        need(isinstance(launch["result"]["output"], str) and isinstance(completion["output"], str), "nonlinear pipeline decoded chunks")
        if index == 1:
            need("curl: (56)" in completion["output"] and "Document stream is empty" in completion["output"], "nonlinear failed source output preserved")
    RESULT["preserved_failures_and_limits"].extend([
        {"id": "TNN-L02", "scope": "nonlinear", "kind": "incomplete_historical_provenance",
         "detail": "22 command strings plus requested cwd and decoded combined tool outputs; no actual native argv arrays, separated raw streams, executable/environment closure, or historical before/after bracket for earlier reads. Current byte comparisons do not retroactively supply those fields."},
        {"id": "TNN-L03", "scope": "nonlinear", "kind": "missing_browser_request_objects",
         "detail": "All three browser rows contain label/tool/return only. Search query objects and complete request bodies are absent; not reconstructed from source snippets."},
        {"id": "TNN-L04", "scope": "nonlinear", "kind": "preserved_source_and_assembly_failures",
         "detail": "Earlier wrong-path exit 2, failed pp.6–7 source pipeline aggregate exit 1, curl-reported 56 and empty extractor message, plus transcribed TextEncoder assembly error remain intact. Pipeline member exits and a raw assembly traceback are not established."},
    ])
    RESULT["checks"].append({"desk": F.name, "payloads": 4,
                             "payload_bytes": sum(r["bytes"] for r in actual),
                             "original_pins": 8, "earlier_unpinned_original_checked_now": F_EARLY_ONLY,
                             "local_cmd_string_records": 22, **counts,
                             "closing_hash_stream_comparisons": 2,
                             "browser_returns": 3, "native_source_pipelines": 2,
                             "status": "PASS_WITH_RECORDED_PROVENANCE_LIMITS"})


def main():
    need(pathlib.Path(__file__).resolve() == OWN / "audit.py", "auditor path binding")
    need(pathlib.Path.cwd() == ROOT, "auditor cwd binding")
    need(sys.flags.isolated == 1 and sys.flags.no_site == 1 and sys.dont_write_bytecode, "isolated no-site no-bytecode flags")
    before, key = input_key()
    RESULT["input_key"] = {"sha256": key, "definition": "SHA-256 of canonical JSON: sort_keys=True, ensure_ascii=False, separators=(',', ':')", **before}
    for name, action in (("circular", check_circular), ("network", check_network), ("nonlinear", check_nonlinear)):
        try:
            action()
        except Exception as exc:
            RESULT["new_failures"].append({"scope": name, "type": type(exc).__name__,
                                           "message": str(exc), "traceback": traceback.format_exc()})
    after, after_key = input_key()
    RESULT["inputs_unchanged_after"] = after == before
    RESULT["after_input_key_sha256"] = after_key
    if before != after:
        RESULT["new_failures"].append({"scope": "input_key", "type": "InputChanged", "message": "Before/after declared input key mismatch"})
    RESULT["assertions_checked"] = CHECK_COUNT
    RESULT["status"] = "ARTIFACT_INTEGRITY_PASS_WITH_DISCLOSED_LIMITS" if not RESULT["new_failures"] else "ARTIFACT_AUDIT_FAILURE"
    RESULT["not_claimed"] = [
        "science replay", "independent mathematical or source-owner certification",
        "candidate admission", "root acceptance", "full primary PDF retrieval",
        "historically separated raw streams where only decoded tool output exists",
        "hermetic runtime closure",
    ]
    print(json.dumps(RESULT, sort_keys=True, ensure_ascii=False, indent=2))
    return 1 if RESULT["new_failures"] else 0


if __name__ == "__main__":
    try:
        code = main()
    except Exception as exc:
        RESULT["status"] = "AUDITOR_SETUP_FAILURE"
        RESULT["new_failures"].append({"scope": "setup", "type": type(exc).__name__,
                                       "message": str(exc), "traceback": traceback.format_exc()})
        print(json.dumps(RESULT, sort_keys=True, ensure_ascii=False, indent=2))
        code = 1
    raise SystemExit(code)
