#!/usr/bin/env python3
"""Read-only documentary receiver for exactly four sealed desks.

No subprocess, network, source import/compile, archived-command evaluation or
scientific calculation. The only outputs are documentary JSON on stdout.
Historical bodies are not displayed. Only declared snippet byte ranges are
compared. Imported stdlib/interpreter files are not a scientific runtime key.
"""
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import sys

ROOT = Path("/root/autodl-tmp/symbolic_dynamics")
BASE = ROOT / "docs/papers211_215_sequence/qa/four_desk_documentary_audit01"
SCOUT = "docs/papers211_215_sequence/scouting/"
DESKS = [
    ("finite_permutation_gap_desk01", 8, 11, 16, 0,
     "8992ffc1b6aa3b9882903d6b819fe3239cd07b2bbe0ec4e8344d943c0ec84c4f"),
    ("finite_nonlinear_residual_desk01", 7, 8, 11, 0,
     "5a68eba861662d4fba5877df497bb0264e5b95d89de8609e61d37872fad72f07"),
    ("finite_graph_rewiring_desk01", 8, 9, 7, 1,
     "cc4f606be87820ae3a85c98ffc470d470850ca5d0e718c98b2ad098155797daf"),
    ("finite_resource_rewriting_desk02", 5, 6, 2, 1,
     "42cdb2d37868316d460c09654c56573ce749b8a313b572b1de2132548bf1cfba"),
]
CLOSURE_SHA = "6d3680e3b2396e203c45a2ccc168b5082685c04ed8706a66dc048067dbb29a43"
checks = 0
before = {}
cache = {}
allowed = {str(Path(__file__)), str(BASE / "NATIVE_READS.json")}
results = {}
snippets = []
archive_summaries = []


def check(value, message):
    global checks
    checks += 1
    if not value:
        raise AssertionError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=True,
                      separators=(",", ":")).encode("ascii")


def rich(path, data=None):
    p = Path(path)
    st = p.lstat()
    check(stat.S_ISREG(st.st_mode) and not p.is_symlink(),
          "regular nonsymlink input: " + str(p))
    check(str(p.resolve()) == str(p), "literal resolved input identity: " + str(p))
    if data is None:
        data = p.read_bytes()
    check(len(data) == st.st_size, "read size: " + str(p))
    return {"bytes": len(data), "sha256": digest(data),
            "resolved": str(p.resolve()), "symlink": None,
            "mode": st.st_mode, "device": st.st_dev, "inode": st.st_ino,
            "mtime_ns": st.st_mtime_ns, "ctime_ns": st.st_ctime_ns}


def get(path):
    p = str(path)
    check(p in allowed, "explicit documentary allowlist: " + p)
    if p not in cache:
        b = Path(p).read_bytes()
        before[p] = rich(p, b)
        cache[p] = b
    return cache[p]


def pairs(items):
    answer = {}
    for key, value in items:
        check(key not in answer, "duplicate JSON key: " + key)
        answer[key] = value
    return answer


def decode(data):
    return json.loads(data, object_pairs_hook=pairs)


def original_json(path):
    return decode(get(path))


def rows(data, blank_count=0):
    check(data.endswith(b"\n"), "terminal LF")
    split = data.decode("ascii").splitlines()
    check(sum(not line for line in split) == blank_count,
          "exact preserved blank-row count")
    if blank_count:
        check(split[-blank_count:] == [""] * blank_count,
              "extra empty rows are terminal only")
    answer = {}
    for line in split:
        if not line:
            continue
        m = re.fullmatch(r"([a-f0-9]{64})  ([^\r\n]+)", line)
        check(m is not None, "exact SHA256 row form")
        h, name = m.groups()
        check(name not in answer, "unique pin path")
        check(not Path(name).is_absolute() and ".." not in Path(name).parts,
              "bounded relative pin")
        answer[name] = h
    return answer


def pin(path, sha):
    b = get(path)
    check(digest(b) == sha, "pin matches complete bytes: " + str(path))
    return {"bytes": len(b), "sha256": sha}


def excerpt(path, low, high):
    # Only the selected byte range is used as body evidence.
    p = ROOT / path
    check(str(p) in allowed, "snippet is a selected historical pin")
    b = get(p)
    check(1 <= low <= high, "positive exact line range")
    starts = [0]
    starts.extend(i + 1 for i, char in enumerate(b) if char == 10)
    a = starts[low - 1] if low - 1 < len(starts) else len(b)
    z = starts[high] if high < len(starts) else len(b)
    return b[a:z]


def output_of(record):
    return record["result"]["output"] if "result" in record else record["output"]


def cmd_of(record):
    return record["request"]["cmd"] if "request" in record else record["cmd"]


def chunk_of(record):
    return record["result"]["chunk_id"] if "result" in record else record["chunk_id"]


def receive_slice(desk, index, record, command, mode="whole_return"):
    m = re.fullmatch(r"sed -n '(\d+),(\d+)p' (.+)", command)
    check(m is not None, "explicit sed-only documentary snippet")
    low, high, path = int(m[1]), int(m[2]), m[3]
    b = excerpt(path, low, high)
    out = output_of(record).encode("utf-8")
    if mode == "whole_return":
        check(out == b, "exact native entire decoded-return bytes")
        offset = 0
    else:
        check(out.count(b) == 1, "unique complete selected snippet in combined return")
        offset = out.index(b)
    snippets.append({"desk": desk, "record_index": index,
                     "native_chunk_id": chunk_of(record),
                     "path": path, "lines": [low, high],
                     "comparison": mode, "archived_byte_offset": offset,
                     "bytes": len(b), "sha256": digest(b)})
    return b


def native_summary(desk, index, record):
    result = record.get("result", record)
    command = record.get("request", {}).get("cmd", record.get("cmd"))
    check(isinstance(result.get("chunk_id"), str), "native chunk string")
    check(type(result.get("original_token_count")) is int,
          "actual token-count metadata retained")
    check(type(result.get("wall_time_seconds")) in (int, float),
          "actual elapsed metadata retained")
    summary = {"desk": desk, "record_index": index,
               "record_canonical_sha256": digest(canonical(record)),
               "native_chunk_id": result["chunk_id"],
               "exit_code": result.get("exit_code"),
               "session_id": result.get("session_id"),
               "command_present": command is not None,
               "command": command,
               "request_fields": sorted(record["request"]) if "request" in record else None,
               "returned_fields": sorted(result)}
    if command is not None:
        check(isinstance(command, str) and command, "actual command text")
        summary["command_utf8_sha256"] = digest(command.encode("utf-8"))
    if "output" in result:
        check(isinstance(result["output"], str), "complete archived decoded string")
        b = result["output"].encode("utf-8")
        summary.update(output_archived=True, output_utf8_bytes=len(b),
                       output_utf8_sha256=digest(b))
    else:
        check(desk == "finite_nonlinear_residual_desk01" and index in [18, 20],
              "only declared missing source completion bodies")
        check(result["output_not_archived"] is True, "missing body not fabricated")
        summary.update(output_archived=False,
                       output_utf16_length=result["output_utf16_length"])
    archive_summaries.append(summary)


def receive_inventory(base, inventory, expected_names, name_field="name"):
    check({r[name_field] for r in inventory} == set(expected_names),
          "exact archived initial inventory names")
    check(len(inventory) == len(expected_names), "no duplicate inventory rows")
    total = 0
    for item in inventory:
        b = get(base / item[name_field])
        check(item["bytes"] == len(b) and item["sha256"] == digest(b),
              "complete archived initial inventory pin")
        total += len(b)
    return total


def receive_local_links(base, names):
    links = []
    for name in names:
        if not name.endswith(".md"):
            continue
        txt = get(base / name).decode("utf-8")
        check(txt.endswith("\n"), "Markdown terminal LF")
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", txt):
            if target.startswith(("http://", "https://")):
                continue
            p = (base / target.split("#", 1)[0]).resolve()
            check(p.is_file(), "local Markdown target exists")
            # Existence only; a link does not authorize opening another file.
            links.append({"document": name, "target": target})
    return links


def main():
    check(Path(__file__).resolve() == BASE / "receive_four_desks.py",
          "exact owned documentary source")
    check(Path.cwd() == ROOT, "documentary cwd")
    check(sys.flags.isolated == 1 and sys.flags.no_site == 1
          and sys.dont_write_bytecode, "documentary isolation flags")
    get(Path(__file__))
    read_evidence = original_json(BASE / "NATIVE_READS.json")
    check(read_evidence["schema"] == "four-desk-selected-zr-native-reads-v1",
          "owned exact ZR actual-read capture")
    check(len(read_evidence["records"]) == 2, "exactly two new ZR read envelopes")
    all_originals = {}
    directory_names_before = {}
    for desk, initial_count, total_files, historical_count, delta, seal in DESKS:
        base = ROOT / SCOUT / desk
        names = {p.name for p in base.iterdir()}
        directory_names_before[str(base)] = sorted(names)
        check(len(names) == total_files, "exact sealed desk file census")
        for name in names:
            check("/" not in name, "flat selected desk package")
            allowed.add(str(base / name))
        manifest = get(base / "MANIFEST.sha256")
        check(digest(manifest) == seal, "original manifest bytes unchanged")
        initial = rows(manifest)
        check(len(initial) == initial_count, "exact initial payload count")
        for name, h in initial.items():
            pin(base / name, h)
        final = initial
        if desk == "finite_permutation_gap_desk01":
            closure = get(base / "CLOSURE_MANIFEST.sha256")
            check(digest(closure) == CLOSURE_SHA, "additive closure manifest pin")
            final = rows(closure)
            check(len(final) == 10, "permutation final ten payloads")
            check(set(final) == set(initial) |
                  {"MANIFEST.sha256", "POST_SEAL_DOCUMENTARY_CLOSURE.json"},
                  "initial seal preserved additively")
            check(all(final[k] == v for k, v in initial.items()),
                  "all eight initial pins unchanged in closure")
            for name, h in final.items():
                pin(base / name, h)
            check(names == set(final) | {"CLOSURE_MANIFEST.sha256"},
                  "exact additive final package")
        else:
            check(names == set(initial) | {"MANIFEST.sha256"},
                  "exact final nonself package")
        hist_raw = get(base / "INPUT_PINS.sha256")
        blanks = 1 if desk in {"finite_permutation_gap_desk01",
                               "finite_graph_rewiring_desk01"} else 0
        hist = rows(hist_raw, blanks)
        check(len(hist) == historical_count, "exact selected historical pin count")
        for name, h in hist.items():
            p = ROOT / name
            check("stdout" not in name and "/reviews/" not in name,
                  "no saved stdout or reviewer-tree historical input")
            check(not name.endswith("finite_graph_memory_fresh_desk/SOURCES_AND_SUBTRACTION.md")
                  and not name.endswith("finite_local_state_fresh_desk/SOURCES_AND_SUBTRACTION.md"),
                  "no graph exposure original reopened")
            allowed.add(str(p))
            item = pin(p, h)
            if name in all_originals:
                check(item == all_originals[name], "shared historical pin agreement")
            all_originals[name] = item
        local = original_json(base / "LOCAL_NATIVE_RECORDS.json")
        primary = original_json(base / "PRIMARY_SOURCE_RECORDS.json")
        documentary = original_json(base / "DOCUMENTARY_RESULT.json")
        for i, record in enumerate(local["records"]):
            native_summary(desk, i, record)
        results[desk] = {
            "base": str(base), "initial_manifest_sha256": seal,
            "initial_payloads": initial_count, "final_payloads": len(final),
            "total_files": total_files,
            "total_bytes": sum(len(get(base / n)) for n in names),
            "historical_pins": historical_count, "pin_blank_lines": blanks,
            "selected_local_native_records": len(local["records"]),
            "reported_closed_attempt_delta_not_adopted": delta,
            "local_markdown_links": receive_local_links(base, names),
        }
        if desk == "finite_permutation_gap_desk01":
            receive_permutation(base, local, primary, documentary, hist_raw, hist, initial)
        elif desk == "finite_nonlinear_residual_desk01":
            receive_nonlinear(base, local, primary, documentary, hist_raw, hist)
        elif desk == "finite_graph_rewiring_desk01":
            receive_graph(base, local, primary, documentary, hist_raw, hist)
        else:
            receive_resource(base, local, primary, documentary, hist_raw, hist, read_evidence)
    check(len(all_originals) == 36, "36 unique selected historical originals")
    check(sum(x["total_files"] for x in results.values()) == 34,
          "34 complete sealed desk files")
    check(set(before) == allowed, "all and only allowed document files consumed")
    check(len(before) == 72, "34 package + 36 historical + source and actual reads")
    after = {p: rich(p) for p in sorted(before)}
    check(before == after, "complete rich input keys unchanged before and after")
    check(directory_names_before ==
          {p: sorted(f.name for f in Path(p).iterdir()) for p in directory_names_before},
          "exact sealed directory listings unchanged")
    answer = {
        "schema": "four-desk-documentary-reception-result-v1",
        "status": "PASS_SCOPED_DOCUMENTARY_RECEPTION_WITH_PRESERVED_LIMITS",
        "checks": checks, "input_paths": len(before),
        "INPUTS_BEFORE": before, "INPUTS_AFTER": after,
        "desks": results, "selected_historical_originals": all_originals,
        "complete_archived_native_entries": archive_summaries,
        "actual_native_source_byte_bindings": snippets,
        "scientific_imports_or_executions": 0, "archived_commands_evaluated": 0,
        "new_web_requests": 0, "new_literal_orbit_calculations": 0,
        "reported_closed_attempt_deltas": [0, 0, 1, 1],
        "count_or_admission_adoption": False,
        "scope": "All selected package/native JSON bytes received; only declared pin-backed source snippets compared. New rich keys bracket this documentary audit, not earlier discovery or a scientific runtime. No imported interpreter/stdlib runtime certificate is claimed.",
        "excluded_live_source_scopes": {
            "graph_exposure_records": [4, 5],
            "permutation_record1_unpinned_pointer_gate_tail": "archive only",
            "nonlinear_unpinned_discovery_records": [12, 13],
            "resource_mixed_records": "6/7 archive preserved; originals used only for hashes and ZR 24-81/20-33 snippets",
            "P211_B": "not opened",
            "saved_pointer_stdout": "not opened",
        },
        "authority": "Root retains source-context reception, theorem/value decisions and any count/index update.",
        "external_status": "HOLD_EXTERNAL",
    }
    print(json.dumps(answer, sort_keys=True, ensure_ascii=True, separators=(",", ":")))


def receive_permutation(base, local, primary, d, pin_raw, hist, initial):
    desk = base.name
    rec = local["records"]
    check(local["schema"] == "finite-permutation-gap-selected-local-records-v1",
          "permutation local schema")
    check([r["record_name"] for r in rec] ==
          ["pg_old_body01", "pg_current_bodies", "pg_distinctions", "pg_final_body",
           "pg_old_search", "pg_old_search_corrected", "pg_pins_before"],
          "permutation exact seven selected records")
    for r in rec:
        check(r["result"]["exit_code"] == 0, "recorded outer exit")
        check(set(r) == {"record_name", "request", "result"}, "permutation envelope fields")
        check(set(r["request"]) == {"cmd", "max_output_tokens"},
              "recorded actual request fields; inherited cwd not invented")
    check("binary file matches" in output_of(rec[4]), "NUL diagnostic preserved")
    check("COMBINATORIAL_SCOUT.md: No such file or directory" in output_of(rec[3]),
          "missing old scout diagnostic preserved")
    check(output_of(rec[6]).encode() + b"\n" == pin_raw,
          "exact native pin return plus preserved terminal blank line")
    check(d["selected_original_pins_before_and_after"] ==
          {p: {"bytes": len(get(ROOT / p)), "sha256": h} for p, h in hist.items()},
          "full original documented pin set")
    for name, value in {"selected_originals_unchanged": 16, "selected_local_read_records": 7,
                        "primary_source_read_entries": 5, "science_executions": 0,
                        "saved_pointer_output_reads": 0, "new_literal_nominations": 0,
                        "closed_attempt_increment": 0}.items():
        check(type(d[name]) is int and d[name] == value, "permutation count " + name)
    check(d["receiver_source_and_manifest_unchanged"] is True, "receiver integrity-only flag")
    # Only pin-backed sed components. The unpinned pointer-gate tail stays archived.
    sed_parts = {}
    for i in range(4):
        sed_parts[i] = []
        for command in cmd_of(rec[i]).splitlines():
            m = re.fullmatch(r"sed -n '(\d+),(\d+)p' (.+)", command)
            if m and m[3] in hist:
                sed_parts[i].append(receive_slice(desk, i, rec[i], command, "combined_selected_slice"))
    check(len(sed_parts[0]) == 2 and len(sed_parts[1]) == 3
          and len(sed_parts[2]) == 5 and len(sed_parts[3]) == 2,
          "twelve exact permitted sed components")
    check(output_of(rec[2]).encode() == b"".join(sed_parts[2]),
          "complete five-component returned stream binding")
    check(output_of(rec[1]).encode().startswith(b"".join(sed_parts[1])),
          "three permitted components form exact prefix; tail not reopened")
    check(output_of(rec[0]).encode().endswith(b"".join(sed_parts[0])),
          "record0 exact two snippet suffix")
    wc_raw = output_of(rec[0]).encode()[:-sum(map(len, sed_parts[0]))]
    wc_lines = wc_raw.decode("utf-8").splitlines()
    wc_paths = cmd_of(rec[0]).splitlines()[0].split()[2:]
    check(len(wc_lines) == len(wc_paths) + 1 == 6, "recorded wc prefix extent")
    expected_total = 0
    for line, path in zip(wc_lines[:-1], wc_paths):
        m = re.fullmatch(r"\s*(\d+) (.+)", line)
        check(m is not None and m[2] == path, "wc path binding")
        count = get(ROOT / path).count(b"\n")
        check(int(m[1]) == count, "wc actual line count")
        expected_total += count
    check(wc_lines[-1].strip() == str(expected_total) + " total", "wc total")
    # Validate only returned indexed rows, not a fresh broad rg discovery.
    indexed = []
    candidates = [p for p in hist if "/scouting/combinatorial/" in p
                  and "papers204_208_sequence" in p]
    for line in output_of(rec[3]).encode().splitlines(keepends=True):
        for p in candidates:
            prefix = p.encode() + b":"
            if line.startswith(prefix):
                number, body = line[len(prefix):].split(b":", 1)
                check(number.isdigit(), "archived indexed source line number")
                check(body == excerpt(p, int(number), int(number)),
                      "exact returned indexed source row bytes")
                indexed.append({"path": p, "line": int(number),
                                "bytes": len(body), "sha256": digest(body)})
    check(len(indexed) > 0, "actual old definition rows present")
    check(primary["full_provider_or_http_bodies_archived"] is False
          and primary["scientific_execution"] is False, "permutation browser limits")
    check([r["id"] for r in primary["records"]] ==
          ["AKS", "BCF", "DK", "D_TORIC", "DMT"], "five primary read entries")
    check("404" in primary["failures"][0]["provider_failure_return"],
          "version request failure retained")
    close = original_json(base / "POST_SEAL_DOCUMENTARY_CLOSURE.json")
    check(close["initial_manifest_sha256"] ==
          digest(get(base / "MANIFEST.sha256")), "closure initial seal binding")
    failure = close["failure"]
    check(failure["actual_chunk_id"] == "8c16db" and failure["actual_exit_code"] == 1,
          "post-seal actual failure metadata")
    check("excerpt only" in failure["retained_extent"]
          and "full combined return remains outside" in failure["retained_extent"],
          "missing failure body not filled")
    check(failure["actual_diagnostics"] ==
          ["sha256sum: WARNING: 1 line is improperly formatted",
           "sha256sum: MANIFEST.sha256: No such file or directory"],
          "exact preserved failure diagnostics")
    checks4 = close["separate_actual_checks"]
    check([x["result"]["chunk_id"] for x in checks4] ==
          ["de88da", "b01a01", "367fef", "4b8dae"], "four actual closure records")
    check(all(x["result"]["exit_code"] == 0 for x in checks4), "actual closure exits")
    for x in checks4:
        check(set(x) == {"request", "result"}, "actual closure envelope")
        check(set(x["request"]) == {"cmd", "workdir", "max_output_tokens"},
              "actual closure request fields")
    first = decode(checks4[0]["result"]["output"])
    check(first == {"manifest_bytes": len(get(base / "MANIFEST.sha256")),
                    "manifest_sha256": digest(get(base / "MANIFEST.sha256")),
                    "original_pins": 16,
                    "payload_bytes": sum(len(get(base / n)) for n in initial),
                    "payloads": 8, "science_executions": 0,
                    "status": "PASS_DOCUMENTARY_ONLY_ZERO_NEW_LITERAL"},
          "complete initial seal-result projection")
    expected = "".join(n + ": OK\n" for n in initial)
    expected += digest(get(base / "MANIFEST.sha256")) + "  MANIFEST.sha256\n"
    check(checks4[1]["result"]["output"] == expected, "actual 8/8 seal check string")
    expected = "".join(n + ": OK\n" for n in hist)
    expected += "sha256sum: WARNING: 1 line is improperly formatted\n"
    check(checks4[2]["result"]["output"] == expected, "16/16 and warning exact string")
    receiver_manifest_path = next(p for p in hist if p.endswith("/MANIFEST.sha256"))
    old_receiver_names = rows(get(ROOT / receiver_manifest_path))
    check(len(old_receiver_names) == 10, "pinned receiver manifest ten names only")
    check(checks4[3]["result"]["output"] ==
          "".join(n + ": OK\n" for n in old_receiver_names),
          "archived receiver check output; no receiver payload re-audit")
    results[desk].update(
        final_manifest_sha256=CLOSURE_SHA,
        native_sed_snippets=12, indexed_returned_rows=indexed,
        complete_combined_body_return_bound=[2],
        partial_combined_return_binding=[0, 1, 3],
        missing_failure_body_preserved=failure,
        browser_full_bodies_archived=False,
        documentary_closure_native_chunks=[x["result"]["chunk_id"] for x in checks4],
        old_receiver_payloads_newly_audited=0)


def receive_nonlinear(base, local, primary, d, pin_raw, hist):
    desk = base.name
    rec = local["records"]
    check(local["schema"] == "source_only_selected_native_records_v1",
          "nonlinear local schema")
    check(len(rec) == 27 and [r["record_index"] for r in rec] == list(range(27)),
          "all 27 indexed local records")
    check(local["cwd"] == str(ROOT), "recorded nonlinear cwd")
    check(rec[21]["cmd"] == rec[26]["cmd"] and
          rec[21]["output"].encode() == rec[26]["output"].encode() == pin_raw,
          "exact before/after native pin strings")
    check(local["pin_bracket"] == {"before_record": 21, "after_record": 26,
                                  "closing_reads": [22, 23, 24, 25],
                                  "all_eleven_text_hash_rows_identical": True},
          "original bracket only covers four closing reads")
    selected = [0, 1, 2, 3, 6, 7, 14, 15, 16, 22, 23, 24, 25]
    for i in selected:
        receive_slice(desk, i, rec[i], rec[i]["cmd"])
    for i in [12, 13]:
        m = re.fullmatch(r"sed -n '(\d+),(\d+)p' (.+)", rec[i]["cmd"])
        check(m is not None and m[3] not in hist,
              "two unpinned discovery source returns archived without reopening")
    for i, r in enumerate(rec):
        if i not in [17, 19]:
            check(r["exit_code"] == 0, "recorded nonlinear exit")
    stream_pairs = []
    for a, b, session, length in [(17, 18, 10988, 22436), (19, 20, 96299, 12842)]:
        check("exit_code" not in rec[a] and rec[a]["output"] == "",
              "actual yielded launch is not completion")
        check(rec[a]["session_id"] == rec[b]["poll"]["session_id"] == session,
              "source stream session binding")
        check(rec[b]["poll"]["chars"] == "" and rec[b]["exit_code"] == 0,
              "actual empty poll and zero completion")
        check("output" not in rec[b] and rec[b]["output_not_archived"] is True
              and rec[b]["output_utf16_length"] == length,
              "completion body missing, lengths only")
        stream_pairs.append({"launch": a, "completion": b, "session": session,
                             "body_archived": False, "reported_utf16_length": length})
    check("2>/dev/null" in rec[9]["cmd"] and "pipefail" not in rec[9]["cmd"],
          "library discovery suppression/outer exit limitation")
    check(primary["public_full_bodies_archived"] is False
          and len(primary["sources"]) == 2, "two sources, no full article archive")
    browser = primary["browser_requests"]
    check(len(browser) == 6 and [x["record_index"] for x in browser] == list(range(6)),
          "six actual bounded browser request specifications")
    check(len(browser[3]["request"]["find"]) == 5
          and browser[3]["complete_failure_return"].count("No matching text found") == 5,
          "five preserved find failures")
    check("Timeout fetching" in browser[4]["failure_lines"][0], "timeout preserved")
    check(primary["non_native_display_failure"]["complete_numeric_index_dump_archived"] is False,
          "truncated metadata display not supplied as full return")
    native = d["native"]
    check(native["chunk_id"] == "7bad9c" and native["exit_code"] == 0
          and isinstance(native["command"], str), "actual nonlinear documentary original")
    out = decode(native["output"])
    expected_names = {"HANDOFF.md", "INPUT_PINS.sha256", "LOCAL_NATIVE_RECORDS.json",
                      "PRIMARY_SOURCE_RECORDS.json", "PROOF_PACKAGE.md",
                      "SOURCES_AND_SUBTRACTION.md"}
    receive_inventory(base, out["payloads"], expected_names, "path")
    check(out["historical_pins"] == 11 and out["initial_payload_files"] == 6,
          "old nonlinear documentary inventory counts")
    check(out["exact_native_excerpt_byte_comparisons"] == 15,
          "old claimed fifteen read comparisons retained; current scope is thirteen")
    check(out["science_executed"] is False and out["source_full_bodies_archived"] is False
          and out["completed_source_streams"] == 2 and out["browser_request_records"] == 6,
          "old documentary counts and limitations")
    results[desk].update(native_sed_snippets=13,
                        unpinned_discovery_returns_not_reopened=[12, 13],
                        original_documentary_excerpt_count=15,
                        source_stream_pairs=stream_pairs,
                        browser_request_count=6, browser_full_bodies_archived=False,
                        documentary_native_chunk=native["chunk_id"])


def receive_graph(base, local, primary, d, pin_raw, hist):
    desk = base.name
    rec = local["records"]
    check(len(rec) == local["record_count"] == 16
          and [r["record_index"] for r in rec] == list(range(16)),
          "graph sixteen exact indexed records")
    check(local["scope_violation_record_indices"] == [4, 5]
          and local["scope_violation_disclosed_to_root"] is True
          and local["reopen_after_disclosure"] is False
          and local["mathematical_use_of_violation_material"] is False,
          "graph exposure boundary preserved")
    for r in rec:
        check(r["exit_code"] == 0, "graph actual outer native exit")
    selected = [3, 6, 7, 10, 11, 12, 13]
    for i in selected:
        receive_slice(desk, i, rec[i], rec[i]["cmd"])
    check(rec[15]["output"].encode() + b"\n" == pin_raw,
          "graph seven native pins and exact terminal blank")
    exposures = []
    for i, chunk, size, h in [
        (4, "e2d11a", 9040, "53fcee206e73b274b57654cc2d5e04f0c7eb0438eea71e47d53d5c717cdbb643"),
        (5, "ceef66", 8716, "70fe99ee0e1a21070c8131cec5351c359d49db0c2801333c6fd1ca245f56e4fe")]:
        r = rec[i]; b = r["output"].encode("utf-8")
        check(r["classification"] == "DISCLOSED_OUT_OF_SCOPE_POINTER_OVERVIEW_READ"
              and r["chunk_id"] == chunk and len(b) == size and digest(b) == h,
              "whole archived exposure string retained without original reopening")
        exposures.append({"record_index": i, "native_chunk_id": chunk,
                          "archived_decoded_output_bytes": size,
                          "archived_decoded_output_sha256": h,
                          "original_reopened": False})
    check(primary["browser_request_count"] == len(primary["requests"]) == 3
          and [r["request_index"] for r in primary["requests"]] == [0, 1, 2],
          "three graph browser requests")
    check(primary["failed_primary_access"]["body_read"] is False
          and "Internal Error" in primary["failed_primary_access"]["actual_result_excerpt"],
          "unread DOI failure preserved")
    check(primary["source_full_text_redistributed"] is False
          and primary["scientific_runs"] == 0 and primary["global_novelty_claim"] is False,
          "graph browser/science boundaries")
    native = d["native_result"]
    check(native["chunk_id"] == "4e5f01" and native["exit_code"] == 0
          and isinstance(d["command"], str), "actual graph documentary command/result")
    out = decode(native["output"])
    expected = {"HANDOFF.md", "INPUT_PINS.sha256", "INTAKE.md", "LOCAL_NATIVE_RECORDS.json",
                "PRIMARY_SOURCE_RECORDS.json", "PROOF_PACKAGE.md", "SOURCES_AND_SUBTRACTION.md"}
    total = receive_inventory(base, out["first_seven_payloads"], expected)
    check(out["total_first_seven_payload_bytes"] == total, "graph initial byte total")
    check(out["disclosed_scope_violation_archives"] == exposures,
          "complete graph exposure projection")
    check({x["path"]: {"bytes": x["bytes"], "sha256": x["sha256"]}
           for x in out["selected_original_pins_checked"]} ==
          {p: {"bytes": len(get(ROOT / p)), "sha256": h} for p, h in hist.items()},
          "graph all seven documented original pins")
    own = [s for s in snippets if s["desk"] == desk]
    expected_reads = [{"record_index": s["record_index"], "path": s["path"],
                       "bytes": s["bytes"], "sha256": s["sha256"],
                       "native_chunk_id": s["native_chunk_id"]} for s in own]
    check(out["exact_decoded_return_to_current_original_byte_comparisons"] == expected_reads,
          "all seven actual old graph snippet records equal fresh byte bindings")
    results[desk].update(native_sed_snippets=7, exposure_archives=exposures,
                        browser_request_count=3, browser_full_bodies_archived=False,
                        documentary_native_chunk=native["chunk_id"])


def receive_resource(base, local, primary, d, pin_raw, hist, new_reads):
    desk = base.name
    rec = local["records"]
    check(len(rec) == local["record_count"] == 12
          and [r["record_index"] for r in rec] == list(range(12)),
          "resource twelve exact indexed records")
    check(local["mixed_pointer_content_exposure_record_indices"] == [6, 7]
          and local["mixed_pointer_content_disclosed_to_root"] is True,
          "mixed PR exposure retained")
    check(local["mathematical_comparison_record_indices"] == [6, 7, 10, 11]
          and local["scientific_runs"] == 0
          and local["forbidden_current_directories_accessed"] is False,
          "resource source/scope declarations")
    for r in rec:
        check(r["exit_code"] == 0, "resource actual outer exit")
    check(rec[9]["output"].encode() == pin_raw, "two exact native whole-file pin strings")
    comparisons = []
    for j, (first, repeat, lo, hi) in enumerate([(6, 10, 24, 81), (7, 11, 20, 33)]):
        b = receive_slice(desk, repeat, rec[repeat], rec[repeat]["cmd"])
        # The mixed originals are not used outside the permitted ZR byte range.
        archive = rec[first]["output"].encode("utf-8").splitlines(keepends=True)
        check(b"".join(archive[lo - 1:hi]) == b,
              "ZR-only selected bytes equal preserved mixed archived return")
        r = new_reads["records"][j]
        check(r["request"]["cmd"] == rec[repeat]["cmd"]
              and r["request"]["workdir"] == str(ROOT)
              and r["result"]["exit_code"] == 0,
              "actual new exact ZR request/native success")
        check(r["result"]["output"].encode("utf-8") == b,
              "actual new ZR decoded native output equals exact original bytes")
        comparisons.append({"archived_mixed_record": first,
                            "section_only_repeat_record": repeat,
                            "lines": [lo, hi], "bytes": len(b), "sha256": digest(b),
                            "actual_repeat_native_chunk": rec[repeat]["chunk_id"],
                            "new_actual_read_chunk": r["result"]["chunk_id"]})
    failed = local["document_construction_failure"]
    check(failed["actual_return"] ==
          "Script error:\nSyntaxError: Unexpected identifier 'docs'",
          "actual pre-evaluation authoring diagnostic")
    check(failed["filesystem_mutation"] is False
          and failed["full_failed_template_source_archived"] is False,
          "missing failed template not reconstructed")
    check(primary["browser_request_count"] == len(primary["requests"]) == 3
          and len(primary["sources"]) == 3, "resource three primary request records")
    check([r["request_index"] for r in primary["requests"]] == [0, 1, 2],
          "ordered source request metadata")
    check(primary["sources"][1]["header_version_date"] == "2020-09-20"
          and primary["sources"][1]["rendered_body_date"] == "2026-08-24",
          "header/rendered date difference preserved")
    check(primary["sources"][2]["verified_publication_date"] is None
          and primary["sources"][2]["visual_review"] is False,
          "placeholder venue/date and no visual review preserved")
    native = d["native_result"]
    check(native["chunk_id"] == "22e41b" and native["exit_code"] == 0
          and isinstance(d["command"], str), "resource documentary command/result")
    out = decode(native["output"])
    total = receive_inventory(base, out["first_four_payload_inventory"],
                              {"INPUT_PINS.sha256", "LOCAL_NATIVE_RECORDS.json",
                               "PRIMARY_SOURCE_RECORDS.json", "REPORT.md"})
    check(total == out["first_four_payload_bytes"], "resource initial byte total")
    check(out["two_actual_ZR_byte_comparisons"] ==
          [{k: v for k, v in r.items() if k != "new_actual_read_chunk"}
           for r in comparisons], "complete prior ZR check records bound")
    check(out["construction_parse_failure_preserved"] == failed,
          "authoring failure unchanged in documentary result")
    check({r["path"]: {"bytes": r["bytes"], "sha256": r["sha256"]}
           for r in out["selected_original_pins"]} ==
          {p: {"bytes": len(get(ROOT / p)), "sha256": h} for p, h in hist.items()},
          "two documented complete original hashes")
    for exposure, i in zip(out["mixed_read_exposures_preserved"], [6, 7]):
        check(exposure["record_index"] == i
              and exposure["native_chunk"] == rec[i]["chunk_id"]
              and exposure["retained_return_bytes"] == len(rec[i]["output"].encode()),
              "full archived mixed-return metadata")
    results[desk].update(native_sed_snippets=2, actual_new_ZR_reads=comparisons,
                        mixed_archived_records_preserved=[6, 7],
                        browser_request_count=3, browser_full_bodies_archived=False,
                        missing_failed_template_preserved=True,
                        documentary_native_chunk=native["chunk_id"])


if __name__ == "__main__":
    main()
