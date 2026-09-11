"""P213 finite observer SOURCE ONLY. No binding or operation is authorized."""

# A later, separately reviewed new source must embed the entire literal binding.
# No JSON/config/source file is loaded to obtain it. Do not edit this frozen copy.
BINDING = None
if BINDING is None:
    raise SystemExit("P213_OBSERVER_DISABLED_UNRESOLVED_BINDING")

import sys

MISSING = object()
FIELDS = ("st_dev", "st_ino", "st_mode", "st_nlink", "st_uid", "st_gid",
          "st_rdev", "st_size", "st_mtime_ns", "st_ctime_ns")
EARLY = []
SNAPSHOTS = []
FILES = []
USED_BYTES = 0


def need(condition, code):
    if not condition:
        raise RuntimeError(code)


def frozen(value):
    if value is MISSING:
        return ("missing",)
    if value is None:
        return ("null",)
    if type(value) in (str, int, bool):
        if type(value) is str:
            need(len(value) <= BINDING["bounds"]["scalar_chars"], "scalar_bound")
        return ("value", value)
    if isinstance(value, tuple) or type(value) is list:
        need(len(value) <= BINDING["bounds"]["sequence_items"], "sequence_bound")
        return ("sequence", tuple(frozen(x) for x in value))
    raise RuntimeError("unsupported_scalar_type:" + type(value).__module__ + "." + type(value).__qualname__)


def attribute(obj, name):
    return frozen(getattr(obj, name, MISSING))


def loader_id(loader):
    if loader is MISSING or loader is None:
        return frozen(loader)
    is_class = isinstance(loader, type)
    kind = loader if is_class else type(loader)
    return ("class" if is_class else "instance",
            attribute(kind, "__module__"), attribute(kind, "__qualname__"))


def module_snapshot(phase):
    record = {"phase": phase, "rows": [], "complete": False}
    SNAPSHOTS.append(record)
    registry = tuple(sys.modules.copy().items())
    need(len(registry) <= BINDING["bounds"]["modules"], "module_bound")
    result = []
    for name, module in sorted(registry):
        need(type(name) is str and module is not None, "invalid_module_entry")
        spec = getattr(module, "__spec__", MISSING)
        spec_data = frozen(spec) if spec is MISSING or spec is None else (
            "spec", attribute(spec, "origin"),
            loader_id(getattr(spec, "loader", MISSING)),
            attribute(spec, "has_location"),
            attribute(spec, "submodule_search_locations"))
        result.append((name, True, name in sys.builtin_module_names, spec_data,
                       loader_id(getattr(module, "__loader__", MISSING)),
                       attribute(module, "__file__"), attribute(module, "__cached__"),
                       attribute(module, "__path__")))
        record["rows"] = tuple(result)
    record["complete"] = True
    return tuple(result)


def launch_snapshot():
    names = ("executable", "orig_argv", "argv", "version", "version_info",
             "path", "prefix", "base_prefix", "exec_prefix", "base_exec_prefix",
             "dont_write_bytecode", "pycache_prefix", "platform", "byteorder",
             "abiflags", "hexversion", "maxsize", "builtin_module_names")
    flags = tuple((n, attribute(sys.flags, n)) for n in BINDING["flag_names"])
    implementation = tuple((n, frozen(v)) for n, v in sorted(vars(sys.implementation).items()))
    streams = tuple((n, attribute(getattr(sys, n), "encoding"),
                     attribute(getattr(sys, n), "errors")) for n in ("stdout", "stderr"))
    return (tuple((n, attribute(sys, n)) for n in names), flags, str(sys.flags),
            implementation, streams, sys.getfilesystemencoding(), sys.getfilesystemencodeerrors())


def raw_maps(phase):
    record = {"phase": phase, "raw_hex": "", "byte_count": 0, "eof": False}
    EARLY.append(record)
    chunks = []
    limit = BINDING["bounds"]["maps_bytes"]
    try:
        with open("/proc/self/maps", "rb", buffering=0) as stream:
            while True:
                block = stream.read(min(65536, limit + 1 - record["byte_count"]))
                if not block:
                    record["eof"] = True
                    break
                chunks.append(block)
                record["byte_count"] += len(block)
                need(record["byte_count"] <= limit, "maps_bound")
    finally:
        record["raw_hex"] = b"".join(chunks).hex()
    return record


def failure(exc):
    # No arbitrary exception text: in particular no environment names/values.
    return {"class": type(exc).__module__ + "." + type(exc).__qualname__,
            "errno": getattr(exc, "errno", None),
            "code": exc.args[0] if type(exc) is RuntimeError else "operation_failed"}


try:
    EARLY_MODULES = module_snapshot("early")
    EARLY_LAUNCH = launch_snapshot()
    EARLY_MAPS = raw_maps("early_pre_helpers")
    SECOND_MODULES = module_snapshot("second_prehelper")
    SECOND_LAUNCH = launch_snapshot()
except BaseException as exc:
    # Before helper imports, ASCII repr is a failed-evidence envelope, not JSON PASS.
    sys.stdout.write(ascii({"status": "HOLD_PREHELPER", "failure": failure(exc),
                           "early_modules": globals().get("EARLY_MODULES"),
                           "early_launch": globals().get("EARLY_LAUNCH"),
                           "module_snapshots": SNAPSHOTS, "maps": EARLY}) + "\n")
    raise SystemExit(78)

try:
    import os
    import hashlib
    import json
except BaseException as exc:
    sys.stdout.write(ascii({"status": "HOLD_HELPER_IMPORT", "failure": failure(exc),
                           "early_modules": EARLY_MODULES, "early_launch": EARLY_LAUNCH,
                           "second_modules": SECOND_MODULES, "second_launch": SECOND_LAUNCH,
                           "module_snapshots": SNAPSHOTS, "maps": EARLY}) + "\n")
    raise SystemExit(78)


def canonical(value):
    return json.dumps(value, ensure_ascii=True, sort_keys=True, separators=(",", ":"))


def path_ok(path):
    need(type(path) is str and path.startswith("/") and path != "/", "absolute_path")
    need(len(path) <= BINDING["bounds"]["scalar_chars"], "path_bound")
    need(all(32 <= ord(c) <= 126 and c != "\\" for c in path), "unsupported_path_encoding")
    need(os.path.normpath(path) == path and "//" not in path, "lexical_path_form")


def full_stat(value):
    result = {name: getattr(value, name) for name in FIELDS}
    need(all(type(v) is int for v in result.values()), "noninteger_stat")
    return result


def points(entry, result):
    result.update({"lexical": entry["lexical"], "links": [], "absence": None})
    first = entry["lexical"]
    for index, link in enumerate(entry["links"]):
        need(link["path"] == first, "link_chain_binding")
        value = full_stat(os.lstat(first))
        need(value["st_mode"] & 0o170000 == 0o120000, "expected_symlink")
        target = os.readlink(first)
        result["links"].append({"path": first, "lstat": value, "readlink": target})
        need(target == link["target"], "unexpected_link_target")
        first = os.path.normpath(os.path.join(os.path.dirname(first), target))
        need(first == link["next"], "link_next_binding")
    need(first == entry["final"], "final_path_binding")
    try:
        result["final_lstat"] = full_stat(os.lstat(first))
    except OSError as exc:
        # Linux ENOENT is 2. ENOTDIR and dangling approved links are never absence.
        if exc.errno == 2 and not entry["links"] and entry["optional"]:
            result["absence"] = {"operation": "lstat", "path": first, "errno": 2}
            return result
        raise
    need(result["final_lstat"]["st_mode"] & 0o170000 == 0o100000, "nonregular_path")
    return result


def key_file(entry):
    global USED_BYTES
    record = {"lexical": entry["lexical"], "roles": entry["roles"],
              "byte_count": 0, "eof": False, "complete": False}
    FILES.append(record)
    fd = None
    digest = hashlib.sha256()
    try:
        record["begin"] = {}
        points(entry, record["begin"])
        if record["begin"]["absence"] is not None:
            record["absent"] = True
            return record
        fd = os.open(entry["final"], os.O_RDONLY | os.O_NONBLOCK | os.O_NOFOLLOW | os.O_CLOEXEC)
        record["fd_before"] = full_stat(os.fstat(fd))
        need(record["fd_before"]["st_mode"] & 0o170000 == 0o100000, "nonregular_fd")
        need(record["fd_before"] == record["begin"]["final_lstat"], "path_fd_before")
        limit = BINDING["bounds"]["file_bytes"]
        need(0 <= record["fd_before"]["st_size"] <= limit, "file_size_bound")
        while True:
            block = os.read(fd, min(65536, limit + 1 - record["byte_count"],
                                   BINDING["bounds"]["total_bytes"] + 1 - USED_BYTES))
            if not block:
                record["eof"] = True
                break
            digest.update(block)
            record["byte_count"] += len(block)
            USED_BYTES += len(block)
            need(record["byte_count"] <= limit, "file_read_bound")
            need(USED_BYTES <= BINDING["bounds"]["total_bytes"], "total_read_bound")
        record["fd_after"] = full_stat(os.fstat(fd))
        record["after_read"] = {}
        points(entry, record["after_read"])
        need(record["fd_before"] == record["fd_after"], "same_fd_changed")
        need(record["begin"] == record["after_read"], "path_changed_during_read")
        need(record["byte_count"] == record["fd_before"]["st_size"], "incomplete_file")
        record["complete"] = True
        return record
    except BaseException as exc:
        record["failure"] = failure(exc)
        raise
    finally:
        record["sha256_of_read_bytes"] = digest.hexdigest()
        if fd is not None:
            try:
                os.close(fd)
            except BaseException as exc:
                record["complete"] = False
                record["close_failure"] = failure(exc)
                raise


def actual_value(marker):
    return marker[1] if len(marker) == 2 and marker[0] == "value" else None


def module_delta(before, after):
    left = {row[0]: row for row in before}
    right = {row[0]: row for row in after}
    return {"added": sorted(right.keys() - left.keys()), "removed": sorted(left.keys() - right.keys()),
            "changed": sorted(name for name in left.keys() & right.keys() if left[name] != right[name])}


def mapped_paths(record):
    return {row["path"] for row in record["parsed"] if row["path"].startswith("/")}


def module_roles(snapshot, phase, entries, keyed=None):
    roles = []
    need(tuple(x[0] for x in snapshot) == tuple(BINDING["module_names"][phase]), "module_set_" + phase)
    for row in snapshot:
        name, present, builtin, spec, loader, filename, cached, search = row
        policy = BINDING["modules"][name]
        need(canonical(row) == canonical(policy["record"]), "module_facts_" + phase)
        mechanism = policy["mechanism"]
        if mechanism == "direct_script":
            need(name == "__main__" and spec == ("null",), "direct_script_spec")
            need(actual_value(filename) == BINDING["observer"], "direct_script_file")
        else:
            need(spec[0] == "spec", "unknown_module_spec")
            origin = actual_value(spec[1])
            if mechanism == "builtin":
                need(builtin and origin == "built-in", "builtin_origin")
            elif mechanism == "frozen":
                need(origin == "frozen", "frozen_origin")
            elif mechanism == "ordinary_file":
                need(origin == actual_value(filename), "ordinary_origin_file")
                path_ok(origin)
            else:
                raise RuntimeError("unsupported_module_mechanism")
            need(canonical(spec[2]) in BINDING["loader_ids"][mechanism], "unsupported_spec_loader")
        need(canonical(loader) in BINDING["loader_ids"][mechanism], "unsupported_module_loader")
        declared = policy["file_roles"]
        if mechanism in ("ordinary_file", "direct_script"):
            for value in (actual_value(filename), actual_value(cached)):
                if value is not None:
                    need(any(x["path"] == value for x in declared), "unkeyed_module_path")
            need(any(x["path"] == actual_value(filename) and x["content_required"]
                     for x in declared), "executed_origin_requires_content_key")
        for role in declared:
            path = role["path"]
            need(path in entries and role["role"] in entries[path]["roles"], "module_role_allowlist")
            if keyed is not None:
                need(keyed[path]["complete"] or (not role["content_required"]
                     and entries[path]["optional"] and keyed[path].get("absent") is True),
                     "late_unkeyed_module")
            roles.append({"phase": phase, "module": name, "mechanism": mechanism,
                          "path": path, "role": role["role"]})
    return roles


def map_roles(record, phase, entries, keyed=None):
    raw = bytes.fromhex(record["raw_hex"])
    need(record["eof"] and len(raw) == record["byte_count"] and raw.endswith(b"\n"), "maps_incomplete")
    parsed = []
    record["parsed"] = parsed
    for line in raw.splitlines():
        fields = line.split(None, 5)
        need(len(fields) in (5, 6), "map_field_count")
        interval, permissions, offset, device, inode = (x.decode("ascii") for x in fields[:5])
        addresses = interval.split("-")
        dev = device.split(":")
        need(len(addresses) == 2 and len(dev) == 2, "map_numeric_shape")
        need(all(x and all(c in "0123456789abcdefABCDEF" for c in x)
                 for x in addresses + dev + [offset]), "map_hex")
        need(inode.isascii() and inode.isdecimal(), "map_inode_decimal")
        need(len(permissions) == 4 and permissions[0] in "r-" and permissions[1] in "w-"
             and permissions[2] in "x-" and permissions[3] in "ps", "map_permissions")
        path = fields[5].decode("ascii") if len(fields) == 6 else ""
        item = {"start": int(addresses[0], 16), "end": int(addresses[1], 16),
                "perms": permissions, "offset": int(offset, 16),
                "device": [int(x, 16) for x in dev], "inode": int(inode), "path": path,
                "phase": phase}
        parsed.append(item)
        need(item["start"] < item["end"], "map_address_order")
        need(not path.endswith(" (deleted)"), "deleted_mapping")
        if path.startswith("/"):
            path_ok(path)
            need(path in entries and "mapped_file" in entries[path]["roles"], "new_map_path")
            need(item["inode"] > 0, "file_map_inode")
            if keyed is not None:
                need(keyed[path]["complete"], "late_unkeyed_map")
                stat = keyed[path]["fd_before"]
                need([os.major(stat["st_dev"]), os.minor(stat["st_dev"])] == item["device"]
                     and stat["st_ino"] == item["inode"], "map_file_identity")
        else:
            need(path in BINDING["special_maps"] and item["inode"] == 0
                 and item["device"] == [0, 0], "unsupported_special_map")
    return parsed


def process_points(keyed, record):
    record["cwd"] = os.getcwd()
    record["proc_cwd"] = os.readlink("/proc/self/cwd")
    record["proc_exe"] = os.readlink("/proc/self/exe")
    record["exe_stat"] = full_stat(os.stat("/proc/self/exe"))
    need(record["cwd"] == record["proc_cwd"] == BINDING["cwd"], "cwd_binding")
    entry = BINDING["interpreter"]
    need(record["proc_exe"] == entry["final"], "exe_binding")
    if keyed is not None:
        need(keyed[entry["lexical"]]["complete"], "exe_key_required")
        need(record["exe_stat"] == keyed[entry["lexical"]]["fd_before"], "exe_file_identity")
    return record


RESULT = {"schema": "P213_FINITE_OBSERVER_V1", "status": "HOLD", "binding_id": BINDING["id"],
          "early_modules": EARLY_MODULES, "early_launch": EARLY_LAUNCH,
          "second_modules": SECOND_MODULES, "second_launch": SECOND_LAUNCH,
          "module_snapshots": SNAPSHOTS, "maps": EARLY, "files": FILES, "runtime_accepted": False}
try:
    helper_modules = module_snapshot("helper")
    RESULT["helper_modules"] = helper_modules
    RESULT["helper_launch"] = launch_snapshot()
    helper_maps = raw_maps("helper")
    RESULT["helper_module_delta"] = module_delta(EARLY_MODULES, helper_modules)
    need(not RESULT["helper_module_delta"]["removed"] and not RESULT["helper_module_delta"]["changed"], "helper_removed_or_changed_module")
    need(EARLY_MODULES == SECOND_MODULES and EARLY_LAUNCH == SECOND_LAUNCH, "prehelper_change")
    need(canonical(EARLY_LAUNCH) == canonical(BINDING["launch_record"]), "launch_binding")
    need(sys.orig_argv == [BINDING["interpreter"]["lexical"], "-I", "-S", "-B", BINDING["observer"]]
         and sys.argv == [BINDING["observer"]], "literal_argv_binding")
    need(sys.flags.isolated == sys.flags.no_site == sys.flags.dont_write_bytecode == 1
         and sys.flags.ignore_environment == sys.flags.no_user_site == 1
         and sys.flags.optimize == 0 and sys.implementation.name == "cpython"
         and sys.platform == "linux", "required_cpython_flags")
    need(sys.executable in (BINDING["interpreter"]["lexical"], BINDING["interpreter"]["final"]), "sys_executable_binding")
    need(RESULT["helper_launch"] == EARLY_LAUNCH, "helper_launch_change")
    # This is only os.environ's Python-level cached mapping; never reload or dump it.
    RESULT["environment"] = {"scope": "os.environ_cached_mapping", "expected": {"LANG": "C", "LC_ALL": "C"}}
    RESULT["environment"]["matches"] = dict(os.environ) == {"LANG": "C", "LC_ALL": "C"}
    need(RESULT["environment"]["matches"], "child_environment_mismatch")
    entries = {}
    need(len(BINDING["files"]) <= BINDING["bounds"]["files"], "file_count_bound")
    for entry in BINDING["files"]:
        path_ok(entry["lexical"])
        path_ok(entry["final"])
        need(entry["lexical"] not in entries and type(entry["optional"]) is bool, "file_binding_unique")
        need(len(entry["links"]) <= BINDING["bounds"]["link_hops"], "link_bound")
        for link in entry["links"]:
            path_ok(link["path"])
            path_ok(link["next"])
        entries[entry["lexical"]] = entry
    need(BINDING["observer"] in entries and not entries[BINDING["observer"]]["optional"], "observer_key_required")
    need(BINDING["interpreter"]["lexical"] in entries
         and not entries[BINDING["interpreter"]["lexical"]]["optional"], "interpreter_key_required")
    RESULT["early_roles"] = module_roles(EARLY_MODULES, "early", entries)
    RESULT["helper_roles"] = module_roles(helper_modules, "helper", entries)
    map_roles(EARLY_MAPS, "early", entries)
    map_roles(helper_maps, "helper", entries)
    RESULT["helper_observed_map_additions"] = sorted(mapped_paths(helper_maps) - mapped_paths(EARLY_MAPS))
    RESULT["process_begin"] = {}
    process_points(None, RESULT["process_begin"])
    keyed = {entry["lexical"]: key_file(entry) for entry in BINDING["files"]}
    RESULT["process_after_keys"] = {}
    process_points(keyed, RESULT["process_after_keys"])
    need(RESULT["process_begin"] == RESULT["process_after_keys"], "process_changed_during_keys")
    map_roles(EARLY_MAPS, "early", entries, keyed)
    map_roles(helper_maps, "helper", entries, keyed)
    module_roles(EARLY_MODULES, "early", entries, keyed)
    module_roles(helper_modules, "helper", entries, keyed)
    closing_modules = module_snapshot("closing")
    RESULT["closing_modules"] = closing_modules
    RESULT["closing_launch"] = launch_snapshot()
    closing_maps = raw_maps("closing")
    RESULT["closing_module_delta"] = module_delta(helper_modules, closing_modules)
    need(not RESULT["closing_module_delta"]["removed"] and not RESULT["closing_module_delta"]["changed"], "closing_removed_or_changed_module")
    RESULT["closing_roles"] = module_roles(closing_modules, "closing", entries, keyed)
    map_roles(closing_maps, "closing", entries, keyed)
    RESULT["closing_observed_map_additions"] = sorted(mapped_paths(closing_maps) - mapped_paths(helper_maps))
    need(RESULT["closing_launch"] == EARLY_LAUNCH, "closing_launch_change")
    RESULT["process_closing"] = {}
    process_points(keyed, RESULT["process_closing"])
    need(RESULT["process_after_keys"] == RESULT["process_closing"], "process_points_changed")
    for entry in BINDING["files"]:
        record = keyed[entry["lexical"]]
        record["closing"] = {}
        points(entry, record["closing"])
        need(record["closing"] == record["begin"], "closing_file_or_absence_changed")
    RESULT["environment"]["closing_matches"] = dict(os.environ) == {"LANG": "C", "LC_ALL": "C"}
    need(RESULT["environment"]["closing_matches"], "closing_environment_mismatch")
    need(module_snapshot("postclosing_check") == closing_modules, "postclosing_module_change")
    RESULT["total_file_read_bytes"] = USED_BYTES
    RESULT["status"] = "OBSERVED_PENDING_INDEPENDENT_RECEPTION"
except BaseException as exc:
    RESULT["failure"] = failure(exc)

try:
    output = (canonical(RESULT) + "\n").encode("ascii")
    need(len(output) <= BINDING["bounds"]["stdout_bytes"], "stdout_bound")
    written = sys.stdout.buffer.write(output)
    need(written == len(output), "short_stdout_write")
    sys.stdout.buffer.flush()
except BaseException:
    # No fabricated complete receipt if serialization/transport fails.
    raise SystemExit(79)
raise SystemExit(0 if RESULT["status"] == "OBSERVED_PENDING_INDEPENDENT_RECEPTION" else 78)
