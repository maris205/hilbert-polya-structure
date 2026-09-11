"""Source-only prepared, stdout-only documentary workspace receiver.

This is written by the two desks' proof author, not an independent reviewer.
No browser return, PDF snapshot, mathematical acceptance or count authority is
created by matching bytes. No archived command string is ever executed.
"""
import hashlib
import json
import os
import re
import stat
import sys

ROOT = "/root/autodl-tmp/symbolic_dynamics"
HERE = "docs/papers211_215_sequence/qa/exchange_interval_reception_preparation01"
PREP_NAMES = {"inspect.py", "INPUT_SPEC.json", "HANDOFF.md", "SHA256SUMS"}
PAYLOAD_NAMES = ["REPORT.md", "PROOF_PACKAGE.md", "SOURCES_AND_LIMITS.md",
                 "INPUTS.sha256", "NATIVE_READS.json", "CLOSING_CHECKS.json"]
ALLOWED = {HERE + "/" + name for name in PREP_NAMES}
READS = {}
RECEIPTS = {}
CHECKS = 0
ROOT_FD = None


class CheckError(Exception):
    pass


def need(condition, label):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise CheckError(label)


def pin(raw):
    return {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}


def components(relative):
    need(type(relative) is str and bool(relative), "nonempty relative path")
    bits = relative.split("/")
    need(all(bit not in ("", ".", "..") for bit in bits), "lexical workspace path")
    need(not relative.startswith("/") and "\x00" not in relative, "no absolute input access")
    return bits


def open_relative(relative, directory=False):
    """Open each in-workspace component without following symbolic links."""
    bits = components(relative)
    parent = os.dup(ROOT_FD)
    try:
        for part in bits[:-1]:
            child = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW,
                            dir_fd=parent)
            os.close(parent)
            parent = child
        # A changed FIFO must fail the regular-file check, not block at open.
        flags = os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK
        if directory:
            flags |= os.O_DIRECTORY
        return os.open(bits[-1], flags, dir_fd=parent)
    finally:
        os.close(parent)


def read(relative):
    need(relative in ALLOWED, "read within exact allowlist: " + str(relative))
    fd = open_relative(relative)
    try:
        before = os.fstat(fd)
        need(stat.S_ISREG(before.st_mode), "regular input file: " + relative)
        need(0 <= before.st_size <= 2_000_000, "bounded complete input: " + relative)
        pieces = []
        length = 0
        while True:
            piece = os.read(fd, 65536)
            if not piece:
                break
            pieces.append(piece)
            length += len(piece)
            need(length <= 2_000_000, "read size ceiling: " + relative)
        raw = b"".join(pieces)
        after = os.fstat(fd)
        need((before.st_size, before.st_mtime_ns, before.st_ino, before.st_dev) ==
             (after.st_size, after.st_mtime_ns, after.st_ino, after.st_dev),
             "stable open file: " + relative)
        need(len(raw) == after.st_size, "full input bytes: " + relative)
    finally:
        os.close(fd)
    observed = pin(raw)
    need(relative not in READS or READS[relative] == observed, "repeated byte stability: " + relative)
    READS[relative] = observed
    return raw


def exact_directory(relative, names):
    fd = open_relative(relative, directory=True)
    try:
        need(set(os.listdir(fd)) == set(names), "exact flat directory: " + relative)
        for name in names:
            mode = os.stat(name, dir_fd=fd, follow_symlinks=False).st_mode
            need(stat.S_ISREG(mode), "no symlink or nested entry: " + relative + "/" + name)
    finally:
        os.close(fd)


def strict_pairs(pairs):
    result = {}
    for key, value in pairs:
        need(key not in result, "no duplicate JSON key: " + key)
        result[key] = value
    return result


def reject_constant(value):
    raise CheckError("nonfinite JSON constant: " + value)


def obj(raw):
    return json.loads(raw.decode("utf-8"), object_pairs_hook=strict_pairs,
                      parse_constant=reject_constant)


def manifest(raw):
    result = {}
    text = raw.decode("utf-8")
    need(text.endswith("\n"), "terminated exact manifest")
    for line in text.splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        need(match is not None, "manifest line syntax")
        digest, path = match.groups()
        need(path not in result, "unique manifest input")
        result[path] = digest
    return result


def wc_table(output):
    lines = output.splitlines()
    need(bool(lines), "archived nonempty wc output")
    result = {}
    for line in lines[:-1]:
        match = re.fullmatch(r"\s*(\d+) (.+)", line)
        need(match is not None, "archived wc row syntax")
        size, path = match.groups()
        need(path not in result, "unique archived wc input")
        result[path] = int(size)
    last = re.fullmatch(r"\s*(\d+) total", lines[-1])
    need(last is not None and int(last.group(1)) == sum(result.values()), "archived wc total")
    return result


def receipt(request, result, location, expected_chunk=None, expected_exit=0):
    need(type(request) is dict and type(result) is dict, "request/result objects: " + location)
    need(set(request) <= {"cmd", "workdir", "max_output_tokens"}, "bounded archived request schema")
    need(type(request.get("cmd")) is str and type(request.get("max_output_tokens")) is int,
         "complete command request: " + location)
    need(set(result) == {"chunk_id", "wall_time_seconds", "exit_code", "original_token_count", "output"},
         "complete terminal result, no session invented: " + location)
    need(type(result["chunk_id"]) is str and bool(result["chunk_id"]), "archived chunk identifier")
    need(type(result["exit_code"]) is int and result["exit_code"] == expected_exit, "actual archived exit")
    need(type(result["original_token_count"]) is int and result["original_token_count"] >= 0,
         "archived token metadata")
    elapsed = result["wall_time_seconds"]
    need(type(elapsed) in (int, float) and 0 <= elapsed < float("inf"), "finite archived duration")
    need(type(result["output"]) is str, "complete returned output string")
    if expected_chunk is not None:
        need(result["chunk_id"] == expected_chunk, "exact archived chunk binding")
    chunk = result["chunk_id"]
    value = {"request": request, "result": result}
    need(chunk not in RECEIPTS or RECEIPTS[chunk]["value"] == value, "same chunk means same full receipt")
    if chunk not in RECEIPTS:
        RECEIPTS[chunk] = {"value": value, "locations": []}
    RECEIPTS[chunk]["locations"].append(location)
    return result["output"]


def archived(row, location, chunk=None, code=0):
    return receipt(row["request"], row["result"], location, chunk, code)


def lf_excerpt(raw, first, last):
    """Reproduce the selected LF-delimited lines without rerunning sed."""
    parts = raw.split(b"\n")
    lines = [part + b"\n" for part in parts[:-1]]
    if parts[-1]:
        lines.append(parts[-1])
    return b"".join(lines[first - 1:last]).decode("utf-8")


def local_link(base, href):
    path = href.split("#", 1)[0]
    need(path and not path.startswith("/") and ":" not in path and "\\" not in path,
         "relative local link only")
    parts = base.split("/")
    for part in path.split("/"):
        if part in ("", "."):
            continue
        if part == "..":
            need(bool(parts), "link stays under workspace")
            parts.pop()
        else:
            parts.append(part)
    result = "/".join(parts)
    need(result in ALLOWED, "link within exact pinned input scope: " + result)
    read(result)
    return result


def inspect_packet(spec, originals):
    base = spec["path"]
    label = spec["key"]
    exact_directory(base, PAYLOAD_NAMES + ["SHA256SUMS"])
    raw = {name: read(base + "/" + name) for name in PAYLOAD_NAMES + ["SHA256SUMS"]}
    for name, value in spec["files"].items():
        need(pin(raw[name]) == value, "whole sealed file anchor: " + label + ":" + name)
    listed = manifest(raw["SHA256SUMS"])
    need(list(listed) == PAYLOAD_NAMES and "SHA256SUMS" not in listed, "six nonself payloads")
    need(all(listed[name] == pin(raw[name])["sha256"] for name in listed), "all sealed manifest bindings")
    inputs = manifest(raw["INPUTS.sha256"])
    need(list(inputs) == spec["input_order"], "exact original-pin order and scope")
    for path, digest in inputs.items():
        need(originals[path]["sha256"] == digest, "original metadata anchor: " + path)
        if originals[path]["scope"] == "workspace_original":
            need(pin(read(path)) == {"sha256": digest, "bytes": originals[path]["bytes"]},
                 "full workspace original: " + path)
    native, close = obj(raw["NATIVE_READS.json"]), obj(raw["CLOSING_CHECKS.json"])
    need(native["schema"] == spec["native_schema"] and close["schema"] == spec["closing_schema"],
         "exact native and closing schemas")
    need(len(native["commands"]) == len(spec["commands"]), "complete selected native command count")
    commands = {}
    for row, expected in zip(native["commands"], spec["commands"]):
        need(set(row) == {"id", "request", "result"} and row["id"] == expected["id"], "ordered native command identity")
        archived(row, label + ":native:" + row["id"], expected["chunk_id"], expected["exit_code"])
        commands[row["id"]] = row
    web = native["browser_requests"]
    need([row["id"] for row in web] == spec["browser_request_ids"], "all browser requests in order")
    need(all(set(row) == {"id", "request"} and type(row["request"]) is dict for row in web),
         "browser requests only; no raw returns or PDF snapshots claimed")
    for kind in ("sha", "bytes"):
        row = close["input_observations"][kind]
        original = commands[spec["input_receipt_ids"][kind]]
        need(row == {"request": original["request"], "result": original["result"]}, "complete original observation duplicated exactly")
        output = archived(row, label + ":closing:input:" + kind)
        prefix = "sha256sum " if kind == "sha" else "wc -c "
        need(row["request"]["cmd"] == prefix + " ".join(spec["input_order"]), "archived input command spelling, never executed")
        if kind == "sha":
            need(output.encode("utf-8") == raw["INPUTS.sha256"], "full archived SHA text binding")
        else:
            need(wc_table(output) == {path: originals[path]["bytes"] for path in inputs}, "all archived original sizes, host opaque")
    repeats = close["repeat_original_text_bindings"]
    need(len(repeats) == len(spec["source_bindings"]), "complete source-repeat denominator")
    bindings = []
    for row, expected in zip(repeats, spec["source_bindings"]):
        original = commands[expected["id"]]
        need(row["original_id"] == expected["id"] and row["request"] == original["request"], "exact full repeated request")
        command = "sed -n '" + str(expected["first"]) + "," + str(expected["last"]) + "p' " + expected["path"]
        need(original["request"]["cmd"] == command, "explicit source range, no shell evaluation")
        need(original["request"].get("workdir", ROOT) == ROOT, "source observation workspace")
        output = archived(row, label + ":closing:repeat:" + expected["id"], expected["repeat_chunk_id"])
        need(row["passed"] is True and output == original["result"]["output"], "whole original/repeated returned text equality")
        excerpt = lf_excerpt(read(expected["path"]), expected["first"], expected["last"])
        need(output == excerpt, "whole current source excerpt equals both archived strings")
        bindings.append({**expected, "returned_utf8": pin(output.encode("utf-8")),
                         "binding_kind": "full returned-text comparison; not independent raw-pipe provenance"})
    row = close["actual_input_sha_check"]
    output = archived(row, label + ":closing:sha_check", spec["closing_receipt_chunks"]["input_sha_check"])
    need(row["request"]["cmd"] == "sha256sum -c " + base + "/INPUTS.sha256", "archived SHA-check request only")
    need(output == "".join(path + ": OK\n" for path in inputs), "all archived SHA-check output retained, not rerun")
    preseal = close["actual_preseal_payload_observations"]
    for kind, prefix in (("sha", "sha256sum "), ("bytes", "wc -c ")):
        row = preseal[kind]
        output = archived(row, label + ":closing:preseal:" + kind, spec["closing_receipt_chunks"]["preseal_" + kind])
        need(row["request"]["cmd"] == prefix + " ".join(PAYLOAD_NAMES[:5]) and
             row["request"]["workdir"] == ROOT + "/" + base, "exact preseal command and directory metadata")
        if kind == "sha":
            need(manifest(output.encode("utf-8")) == {name: pin(raw[name])["sha256"] for name in PAYLOAD_NAMES[:5]}, "full preseal digest text to current payloads")
        else:
            need(wc_table(output) == {name: len(raw[name]) for name in PAYLOAD_NAMES[:5]}, "full preseal byte table to current payloads")
    structural = close["actual_structural_checks"]
    need(len(structural["reads"]) == 5, "five structural-read metadata records")
    for row, name, chunk in zip(structural["reads"], PAYLOAD_NAMES[:5], spec["structural_metadata_chunks"]):
        need(set(row) == {"request", "result_metadata", "note"}, "metadata-only structural record, no invented output")
        need(row["request"]["cmd"] == "sed -n '1,10000p' " + name and
             row["request"]["workdir"] == ROOT + "/" + base, "exact structural read request")
        meta = row["result_metadata"]
        need(set(meta) == {"chunk_id", "exit_code", "original_token_count", "wall_time_seconds"} and
             meta["chunk_id"] == chunk and type(meta["exit_code"]) is int and meta["exit_code"] == 0,
             "preserved structural completion metadata only")
    need([row["name"] for row in structural["checks"]] == spec["structural_check_names"] and
         all(row["passed"] is True for row in structural["checks"]) and structural["all_passed"] is True,
         "archived structural assertions preserved, not mathematical reevaluation")
    links = []
    for name in PAYLOAD_NAMES[:3]:
        links.extend({"source": name, "href": match.group(1)} for match in
                     re.finditer(r"\]\(([^)\n]+)\)", raw[name].decode("utf-8")))
    need(links == spec["links"], "complete simple inline Markdown link inventory")
    local, external = [], []
    for row in links:
        if row["href"].startswith("https://"):
            external.append(row)
        else:
            local.append({**row, "target": local_link(base, row["href"])})
    if label == "exchange":
        need(commands["15"]["result"]["original_token_count"] == 114393 and
             commands["15"]["result"]["exit_code"] == 2, "retain truncated/missing-library native result")
        failure = native["unarchived_actual_failure"]
        need(failure["observed_chunk_id"] == "419365" and failure["exit_code"] == 2,
             "manual failure transcription remains separate from native receipt ledger")
    else:
        need(commands["22"]["result"]["exit_code"] == 1 and commands["22"]["result"]["output"] == "",
             "normal empty local filename search preserved")
        need(native["provider_search"]["matches"] == [], "historical provider lookup metadata only")
    need(close["disposition"] == "NO_PROMOTION / NO_RESERVE / NO_FRESH_SLATE; root-pending", "archived disposition preserved")
    return {"key": label, "packet_files": len(raw), "manifest": pin(raw["SHA256SUMS"]),
            "original_pins": len(inputs), "native_commands": len(commands),
            "complete_source_text_bindings": bindings, "browser_request_objects": len(web),
            "archived_browser_returns": 0, "archived_external_primary_or_pdf_snapshots": 0,
            "structural_read_records_metadata_only": 5, "local_link_occurrences": local,
            "external_links_not_fetched": external, "archive_disposition_only": close["disposition"],
            "archive_denominator_annotations_only": close["denominator"]}


def main():
    global ROOT_FD
    need(len(sys.argv) == 1 and sys.argv[0] == ROOT + "/" + HERE + "/inspect.py", "fixed absolute source, no extra inputs")
    need(sys.flags.isolated == 1 and sys.flags.no_site == 1 and sys.dont_write_bytecode is True,
         "require caller -I -S -B startup; no runtime provenance inferred")
    ROOT_FD = os.open(ROOT, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    exact_directory(HERE, PREP_NAMES)
    prep_manifest = manifest(read(HERE + "/SHA256SUMS"))
    need(set(prep_manifest) == PREP_NAMES - {"SHA256SUMS"}, "three nonself preparation payloads")
    for name, digest in prep_manifest.items():
        need(pin(read(HERE + "/" + name))["sha256"] == digest, "preparation payload integrity")
    spec = obj(read(HERE + "/INPUT_SPEC.json"))
    need(spec["schema"] == "exchange-interval-workspace-receiver-inputs-v1" and spec["workspace"] == ROOT,
         "fixed prepared input specification")
    need([p["key"] for p in spec["packets"]] == ["exchange", "interval"], "exact two desks")
    originals = {row["path"]: row for row in spec["originals"]}
    need(len(originals) == len(spec["originals"]) == 18, "exact distinct original metadata rows")
    opaque = []
    for path, row in originals.items():
        if row["scope"] == "workspace_original":
            components(path)
            ALLOWED.add(path)
        else:
            need(row["scope"] == "opaque_host_metadata_only" and path.startswith("/root/autodl-tmp/.codex/skills/"),
                 "explicit opaque host metadata, never filesystem input")
            opaque.append(row)
    need(len(opaque) == 3 and len(ALLOWED) == 19, "fifteen workspace originals, three opaque host rows")
    for packet in spec["packets"]:
        components(packet["path"])
        need(set(packet["files"]) == set(PAYLOAD_NAMES + ["SHA256SUMS"]), "exact seven sealed packet files")
        ALLOWED.update(packet["path"] + "/" + name for name in packet["files"])
    need(len(ALLOWED) == 33, "exact 29 workspace evidence files and four preparation files")
    summaries = [inspect_packet(packet, originals) for packet in spec["packets"]]
    need(set(READS) == ALLOWED, "every allowed whole workspace input received")
    for path in sorted(ALLOWED):
        read(path)
    exact_directory(HERE, PREP_NAMES)
    for packet in spec["packets"]:
        exact_directory(packet["path"], PAYLOAD_NAMES + ["SHA256SUMS"])
    ledger = []
    for chunk, record in RECEIPTS.items():
        value = record["value"]
        ledger.append({"chunk_id": chunk, "locations": record["locations"],
                       "request": value["request"], "exit_code": value["result"]["exit_code"],
                       "returned_output_utf8": pin(value["result"]["output"].encode("utf-8")),
                       "session_id_present": False})
    need(len(ledger) == 48, "all 48 distinct complete archived terminal receipts, including closing reads")
    return {"status": "DOCUMENTARY_WORKSPACE_BINDINGS_COMPLETED_WITH_EXPLICIT_LIMITS",
            "scope": "byte/text reception only; no independent mathematical review or adoption",
            "checks": CHECKS, "workspace_inputs": READS, "packets": summaries,
            "complete_terminal_receipt_ledger": ledger, "archived_live_sessions": 0,
            "opaque_host_pins_not_dereferenced": opaque,
            "limitations": ["11 browser request objects are not browser returns or PDF snapshots",
                            "10 structural-read records omit stdout and remain metadata-only",
                            "selected native archives are not a complete discovery-call history",
                            "returned UTF-8 text bindings are not independent raw-pipe provenance",
                            "root primary-body reading and semantic decisions remain separate"],
            "new_scientific_executions": 0, "independent_mathematical_review": False,
            "closed_count_authority": False, "external_state_changes": False,
            "author_role": "original proof author; documentary helper preparation only"}


if __name__ == "__main__":
    try:
        result = main()
    except (CheckError, OSError, ValueError, KeyError, TypeError, IndexError) as error:
        print(json.dumps({"status": "DOCUMENTARY_RECEPTION_INCOMPLETE", "checks": CHECKS,
                          "error_type": type(error).__name__, "error": str(error),
                          "closed_count_authority": False}, sort_keys=True))
        code = 1
    else:
        print(json.dumps(result, sort_keys=True, ensure_ascii=False))
        code = 0
    finally:
        if ROOT_FD is not None:
            os.close(ROOT_FD)
    sys.exit(code)
