"""Isolated Track-R capability runner with no project imports."""

import builtins
import ctypes
import hashlib
import json
import os
from pathlib import Path
import socket
import sys

from fractions import Fraction
from math import gcd


_CANDIDATE = "henon_primitive_cycle_cover_v1"
_CAPABILITY_KEYS = {
    "candidate_id",
    "claim_sha256",
    "definitions_sha256",
    "engine_sha256",
    "fixture_sha256",
    "nonce",
    "purpose",
    "runner_sha256",
    "schema",
    "track",
}
_COUNTER_KEYS = {
    "denied_cross_track_read_count",
    "denied_dynamic_loader_count",
    "denied_ledger_read_count",
    "denied_network_count",
    "denied_outside_read_count",
    "denied_outside_write_count",
    "denied_process_count",
    "denied_review_read_count",
    "denied_source_read_count",
    "run_science_call_count",
    "successful_outside_read_count",
    "successful_outside_write_count",
}
_SCIENCE_BUILTIN_NAMES = (
    "ArithmeticError",
    "TypeError",
    "ValueError",
    "ZeroDivisionError",
    "all",
    "any",
    "dict",
    "enumerate",
    "int",
    "len",
    "list",
    "max",
    "min",
    "range",
    "reversed",
    "set",
    "sorted",
    "str",
    "sum",
    "tuple",
    "type",
)
_SCIENCE_BUILTIN_OBJECTS = {
    name: vars(builtins)[name] for name in _SCIENCE_BUILTIN_NAMES
}


def _rj_pairs(pairs):
    output = {}
    for key, value in pairs:
        if key in output:
            raise ValueError("R duplicate JSON key")
        output[key] = value
    return output


def _rj_reject_constant(value):
    raise ValueError("R nonfinite JSON constant: " + value)


def _rj_reject_float(value):
    raise ValueError("R floating JSON number: " + value)


def _rj_load(payload):
    if type(payload) is not bytes:
        raise TypeError("R JSON bytes required")
    return json.loads(
        payload.decode("utf-8"),
        object_pairs_hook=_rj_pairs,
        parse_constant=_rj_reject_constant,
        parse_float=_rj_reject_float,
    )


def _rj_canonical(value):
    pending = [value]
    while pending:
        item = pending.pop()
        if type(item) not in (dict, list, str, int, bool, type(None)):
            raise TypeError("R non-JSON canonical value")
        if type(item) is dict:
            if any(type(key) is not str for key in item):
                raise TypeError("R non-string JSON key")
            pending.extend(item.keys())
            pending.extend(item.values())
        elif type(item) is list:
            pending.extend(item)
    return (
        json.dumps(value, allow_nan=False, ensure_ascii=True, sort_keys=True, separators=(",", ":"))
        + "\n"
    ).encode("ascii")


def _rj_sha(payload):
    return hashlib.sha256(payload).hexdigest()


def _rj_is_hex(value, width):
    return (
        type(value) is str
        and len(value) == width
        and all(character in "0123456789abcdef" for character in value)
    )


def _rj_read_capability():
    chunks = []
    size = 0
    try:
        while True:
            block = os.read(3, 4096)
            if not block:
                break
            chunks.append(block)
            size += len(block)
            if size > 16384:
                raise ValueError("R capability too large")
    except OSError as exc:
        raise RuntimeError("R capability descriptor unavailable") from exc
    finally:
        try:
            os.close(3)
        except OSError:
            pass
    payload = b"".join(chunks)
    token = _rj_load(payload)
    if _rj_canonical(token) != payload:
        raise ValueError("R capability not canonical")
    if type(token) is not dict or set(token) != _CAPABILITY_KEYS:
        raise ValueError("R capability keys")
    if token["schema"] != "P13_TRACK_CAPABILITY_V1" or token["track"] != "R":
        raise ValueError("R capability identity")
    if token["candidate_id"] != _CANDIDATE:
        raise ValueError("R capability candidate")
    if token["purpose"] not in ("SAFE_RUNTIME_PROBE", "REGISTERED_R100"):
        raise ValueError("R capability purpose")
    if not _rj_is_hex(token["nonce"], 32):
        raise ValueError("R capability nonce")
    if not _rj_is_hex(token["definitions_sha256"], 64) or not _rj_is_hex(token["runner_sha256"], 64):
        raise ValueError("R capability base hashes")
    optional = ("claim_sha256", "engine_sha256", "fixture_sha256")
    if token["purpose"] == "SAFE_RUNTIME_PROBE":
        if any(token[key] is not None for key in optional):
            raise ValueError("R safe capability contains science binding")
    elif any(not _rj_is_hex(token[key], 64) for key in optional):
        raise ValueError("R registered capability hashes")
    return token, payload


def _rj_read_regular(path):
    if path.is_symlink() or not path.is_file():
        raise ValueError("R regular file required")
    return path.read_bytes()


def _rj_install_guard(project_root, allowed_reads, engine_path):
    state = {key: 0 for key in _COUNTER_KEYS}
    project_resolved = project_root.resolve()
    allowed = {path.resolve() for path in allowed_reads}
    labels = {path: path.relative_to(project_resolved).as_posix() for path in allowed}
    observed_reads = {label: 0 for label in sorted(labels.values())}
    control = {"science_active": False}
    other_track = project_root / "code/candidate_v1/track_q"
    notes = project_root / "notes"
    experiments = project_root / "experiments"
    refine = project_root / "refine-logs"
    adjudicator = project_root / "code/candidate_v1/adjudicator"
    engine_resolved = engine_path.resolve()

    def category(path):
        resolved = path.resolve()
        if resolved == other_track or other_track in resolved.parents:
            return "denied_cross_track_read_count"
        if resolved == adjudicator or adjudicator in resolved.parents:
            return "denied_ledger_read_count"
        if resolved == notes or notes in resolved.parents:
            return (
                "denied_review_read_count"
                if "REVIEW" in resolved.name.upper()
                else "denied_source_read_count"
            )
        if resolved == experiments or experiments in resolved.parents:
            return "denied_source_read_count"
        if resolved == refine or refine in resolved.parents:
            return "denied_source_read_count"
        return None

    def audit(event, arguments):
        if event == "open":
            raw_path = arguments[0]
            if type(raw_path) is int:
                return
            path = Path(os.fspath(raw_path)).resolve()
            mode = arguments[1] if len(arguments) > 1 else "r"
            flags = arguments[2] if len(arguments) > 2 else 0
            writing = type(mode) is str and any(marker in mode for marker in ("w", "a", "x", "+"))
            if type(flags) is int:
                writing = writing or bool(
                    flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND)
                )
            path_category = category(path)
            if path_category is not None:
                state[path_category] += 1
                raise PermissionError("R protected path denied")
            if writing:
                state["denied_outside_write_count"] += 1
                raise PermissionError("R write denied")
            if control["science_active"] or path not in allowed:
                state["denied_outside_read_count"] += 1
                raise PermissionError("R read outside allowlist")
            observed_reads[labels[path]] += 1
        elif event in {"os.listdir", "os.scandir"}:
            state["denied_outside_read_count"] += 1
            raise PermissionError("R directory enumeration denied")
        elif event in {
            "os.remove",
            "os.unlink",
            "os.rename",
            "os.replace",
            "os.mkdir",
            "os.rmdir",
            "os.chmod",
            "os.chown",
            "os.link",
            "os.symlink",
            "os.truncate",
            "os.utime",
        }:
            state["denied_outside_write_count"] += 1
            raise PermissionError("R filesystem mutation denied")
        elif event == "os.chdir":
            state["denied_process_count"] += 1
            raise PermissionError("R working-directory change denied")
        elif event.startswith("socket."):
            state["denied_network_count"] += 1
            raise PermissionError("R network denied")
        elif event in {
            "os.fork",
            "os.forkpty",
            "os.system",
            "os.exec",
            "os.posix_spawn",
            "os.posix_spawnp",
            "os.spawn",
            "subprocess.Popen",
            "pty.spawn",
        } or event.startswith(("subprocess.", "os.exec", "os.spawn", "os.posix_spawn", "os.fork")):
            state["denied_process_count"] += 1
            raise PermissionError("R process denied")
        elif event.startswith("ctypes.dlopen") or event.startswith("ctypes.dlsym"):
            state["denied_dynamic_loader_count"] += 1
            raise PermissionError("R dynamic loader denied")
        elif event == "import":
            if arguments[0] != "fractions":
                state["denied_dynamic_loader_count"] += 1
                raise PermissionError("R post-capability import denied")
        elif event == "compile":
            if Path(arguments[1]).resolve() != engine_resolved:
                state["denied_dynamic_loader_count"] += 1
                raise PermissionError("R compile denied")
        elif event == "exec":
            if Path(arguments[0].co_filename).resolve() != engine_resolved:
                state["denied_dynamic_loader_count"] += 1
                raise PermissionError("R exec denied")

    sys.addaudithook(audit)
    original_import = builtins.__import__

    def guarded_import(name, globals_value=None, locals_value=None, fromlist=(), level=0):
        if name == "fractions" and level == 0:
            return original_import(name, globals_value, locals_value, fromlist, level)
        state["denied_dynamic_loader_count"] += 1
        raise PermissionError("R cached or dynamic import denied")

    builtins.__import__ = guarded_import
    return state, observed_reads, control


def _rj_expect_denied(callable_object, counter_name, state):
    before = state[counter_name]
    try:
        callable_object()
    except PermissionError:
        pass
    else:
        raise RuntimeError("R denial probe succeeded")
    if state[counter_name] != before + 1:
        raise RuntimeError("R denial counter")


def _rj_probe_write(path):
    descriptor = os.open(path, os.O_WRONLY)
    os.close(descriptor)


def _rj_probe_scandir(path):
    handle = os.scandir(path)
    handle.close()


def _rj_probe_rename(source, target):
    os.rename(source, target)


def _rj_probe_unlink(path):
    os.unlink(path)


def _rj_safe_probes(project_root, state):
    _rj_expect_denied(lambda: open(project_root / "notes/PROOF_PACKAGE.md", "rb"), "denied_source_read_count", state)
    _rj_expect_denied(lambda: open(project_root / "notes/INDEPENDENT_SOURCE_LOCK_REVIEW_R2.md", "rb"), "denied_review_read_count", state)
    _rj_expect_denied(lambda: open(project_root / "code/candidate_v1/adjudicator/acceptance_ledger.json", "rb"), "denied_ledger_read_count", state)
    _rj_expect_denied(lambda: open(project_root / "code/candidate_v1/track_q/engine.py", "rb"), "denied_cross_track_read_count", state)
    _rj_expect_denied(lambda: open("/etc/hosts", "rb"), "denied_outside_read_count", state)
    _rj_expect_denied(lambda: os.listdir(project_root), "denied_outside_read_count", state)
    _rj_expect_denied(lambda: _rj_probe_scandir(project_root), "denied_outside_read_count", state)
    _rj_expect_denied(lambda: _rj_probe_write(project_root / "code/candidate_v1/shared/definitions.json"), "denied_outside_write_count", state)
    _rj_expect_denied(lambda: _rj_probe_rename(project_root / "never_source", project_root / "never_target"), "denied_outside_write_count", state)
    _rj_expect_denied(lambda: _rj_probe_unlink(project_root / "never_unlink"), "denied_outside_write_count", state)
    _rj_expect_denied(lambda: socket.socket(), "denied_network_count", state)
    _rj_expect_denied(lambda: os.system(":"), "denied_process_count", state)
    _rj_expect_denied(lambda: os.fork(), "denied_process_count", state)
    _rj_expect_denied(lambda: ctypes.CDLL(None), "denied_dynamic_loader_count", state)
    _rj_expect_denied(lambda: __import__("os"), "denied_dynamic_loader_count", state)
    probe_builtins = _rj_build_science_builtins(lambda *arguments, **keywords: None)
    for forbidden_name in ("open", "compile", "exec", "eval", "globals", "getattr"):
        if forbidden_name in probe_builtins:
            raise RuntimeError("R dangerous science builtin exposed")


def _rj_build_science_builtins(restricted_import):
    if any(
        vars(builtins).get(name) is not _SCIENCE_BUILTIN_OBJECTS[name]
        for name in _SCIENCE_BUILTIN_NAMES
    ):
        raise RuntimeError("R builtin identity drift")
    output = dict(_SCIENCE_BUILTIN_OBJECTS)
    output["__import__"] = restricted_import
    return output


def _rj_keys(value, keys, label):
    if type(value) is not dict or set(value) != set(keys):
        raise ValueError("R output keys: " + label)


def _rj_rational(value):
    if type(value) is not list or len(value) != 2:
        raise TypeError("R rational pair wire")
    if type(value[0]) is not int or type(value[1]) is not int or value[1] <= 0:
        raise TypeError("R rational pair entries")
    if gcd(abs(value[0]), value[1]) != 1 or (value[0] == 0 and value[1] != 1):
        raise ValueError("R rational pair not canonical")


def _rj_poly(value):
    if type(value) is not list:
        raise TypeError("R polynomial list")
    previous = None
    for term in value:
        _rj_keys(term, {"coefficient", "exponents_acxy"}, "polynomial term")
        _rj_rational(term["coefficient"])
        if term["coefficient"][0] == 0:
            raise ValueError("R zero polynomial term")
        exponents = term["exponents_acxy"]
        if type(exponents) is not list or len(exponents) != 4 or any(type(item) is not int or item < 0 for item in exponents):
            raise TypeError("R exponent wire")
        key = tuple(exponents)
        if previous is not None and key <= previous:
            raise ValueError("R polynomial terms not sorted")
        previous = key


def _rj_matrix2(value):
    if type(value) is not list or len(value) != 2:
        raise TypeError("R matrix wire")
    for row in value:
        if type(row) is not list or len(row) != 2:
            raise TypeError("R matrix row")
        for item in row:
            _rj_rational(item)


def _rj_rejections(value, key_name, expected_disposition):
    if type(value) is not list or len(value) != 2:
        raise ValueError("R rejection count")
    seen = set()
    for item in value:
        _rj_keys(item, {"disposition", key_name}, "rejection")
        if type(item[key_name]) is not str or item["disposition"] != expected_disposition:
            raise ValueError("R rejection leaf")
        seen.add(item[key_name])
    if len(seen) != 2:
        raise ValueError("R duplicate rejection")


def _rj_validate_certificate(certificate):
    _rj_keys(certificate, {"candidate", "certificate_class", "records", "route", "schema", "track"}, "certificate")
    if certificate != {**certificate, "candidate": _CANDIDATE} or certificate["track"] != "R":
        raise ValueError("R certificate identity")
    if certificate["schema"] != "P13_R_EXACT_CERTIFICATE_V1" or certificate["route"] != "SYLVESTER_FITTING_EXTERIOR" or certificate["certificate_class"] != "BOUNDED_EXACT_CONSISTENCY_RECORD":
        raise ValueError("R certificate constants")
    records = certificate["records"]
    _rj_keys(records, {"N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8"}, "records")
    _rj_keys(records["N1"], {"formal_dynatomic_value", "map_value", "point_multiplier", "unsafe_step"}, "N1")
    for key in ("formal_dynatomic_value", "map_value", "point_multiplier"):
        _rj_rational(records["N1"][key])
    if records["N1"]["unsafe_step"] != "REJECTED_FORMAL_TO_ACTUAL":
        raise ValueError("R N1 disposition")
    _rj_keys(records["N2"], {"fitting_matrix", "fitting_square", "generic_discriminant", "unsafe_step"}, "N2")
    _rj_matrix2(records["N2"]["fitting_matrix"])
    _rj_matrix2(records["N2"]["fitting_square"])
    _rj_poly(records["N2"]["generic_discriminant"])
    if records["N2"]["unsafe_step"] != "REJECTED_GENERIC_TO_ALL_FIBERS":
        raise ValueError("R N2 disposition")
    _rj_keys(records["N3"], {"finite_module_exponents", "fraction_exponent_identity", "fraction_power", "normalizer_in_semigroup", "presentation_t_power", "unsafe_step"}, "N3")
    if type(records["N3"]["finite_module_exponents"]) is not list or any(type(item) is not int or item < 0 for item in records["N3"]["finite_module_exponents"]):
        raise TypeError("R N3 module exponents")
    if any(type(records["N3"][key]) is not int or records["N3"][key] < 0 for key in ("fraction_power", "presentation_t_power")):
        raise TypeError("R N3 integer")
    if type(records["N3"]["fraction_exponent_identity"]) is not list or len(records["N3"]["fraction_exponent_identity"]) != 3 or any(type(item) is not int or item < 0 for item in records["N3"]["fraction_exponent_identity"]):
        raise TypeError("R N3 fraction identity")
    if type(records["N3"]["normalizer_in_semigroup"]) is not bool:
        raise TypeError("R N3 flag")
    if records["N3"]["unsafe_step"] != "REJECTED_BIRATIONAL_TO_NORMAL_EQUALITY":
        raise ValueError("R N3 disposition")
    n4_keys = {"characteristic_rho", "characteristic_tau", "cycle_product", "cycle_sum", "degree_one_boundary", "difference_product", "fitting_rho_pivot_count", "fitting_tau_pivot_count", "nontrivial_monodromy_evidence", "nu", "primitive_factor", "rank", "return_trace", "sylvester_pivot_count"}
    _rj_keys(records["N4"], n4_keys, "N4")
    for key in ("cycle_product", "cycle_sum", "difference_product", "primitive_factor", "return_trace"):
        _rj_poly(records["N4"][key])
    for key in ("characteristic_rho", "characteristic_tau"):
        if type(records["N4"][key]) is not list or len(records["N4"][key]) != 2:
            raise TypeError("R characteristic pair")
        for polynomial in records["N4"][key]:
            _rj_poly(polynomial)
    for key in ("fitting_rho_pivot_count", "fitting_tau_pivot_count", "nu", "rank", "sylvester_pivot_count"):
        if type(records["N4"][key]) is not int or records["N4"][key] < 0:
            raise TypeError("R N4 count")
    for key in ("degree_one_boundary", "nontrivial_monodromy_evidence"):
        if type(records["N4"][key]) is not bool:
            raise TypeError("R N4 flag")
    _rj_rejections(records["N5"], "statement", "REJECTED_SCOPE_ERROR")
    _rj_rejections(records["N6"], "statement", "REJECTED_SCOPE_ERROR")
    _rj_keys(records["N7"], {"disposition", "proposed"}, "N7")
    if records["N7"]["disposition"] != "REJECTED_DIRECTION" or records["N7"]["proposed"] != "G_global -> subgroup_of -> G_special":
        raise ValueError("R N7 disposition")
    _rj_rejections(records["N8"], "kind", "REJECTED_CATEGORY_SUBSTITUTION")
    payload = _rj_canonical(certificate)
    if b"PROVED" in payload or (b"SOURCE" + b"_LOCK_PASS") in payload:
        raise ValueError("R authority language")


def _rj_registered(token, paths, state, control, definitions_bytes):
    fixture_bytes = _rj_read_regular(paths["fixture"])
    engine_bytes = _rj_read_regular(paths["engine"])
    if _rj_sha(definitions_bytes) != token["definitions_sha256"] or _rj_sha(fixture_bytes) != token["fixture_sha256"] or _rj_sha(engine_bytes) != token["engine_sha256"]:
        raise RuntimeError("R registered input hash")
    definitions = _rj_load(definitions_bytes)
    fixture = _rj_load(fixture_bytes)

    def restricted_import(name, globals_value=None, locals_value=None, fromlist=(), level=0):
        if name != "fractions" or level != 0:
            raise ImportError("R engine import denied")
        return sys.modules["fractions"]

    safe_builtins = _rj_build_science_builtins(restricted_import)
    namespace = {
        "__builtins__": safe_builtins,
        "__file__": str(paths["engine"]),
        "__name__": "p13_track_r_engine",
        "Fraction": Fraction,
    }
    control["science_active"] = True
    code = compile(engine_bytes, str(paths["engine"]), "exec", dont_inherit=True, optimize=0)
    exec(code, namespace, namespace)
    run_science = namespace.get("run_science")
    if not callable(run_science) or state["run_science_call_count"] != 0:
        raise RuntimeError("R pre-science boundary")
    phase = "SCIENCE_ENTERED"
    state["run_science_call_count"] = 1
    try:
        certificate = run_science(definitions, fixture)
    except BaseException:
        phase = "SCIENCE_FAILED"
        raise
    phase = "SCIENCE_RETURNED"
    if phase != "SCIENCE_RETURNED" or state["run_science_call_count"] != 1:
        raise RuntimeError("R post-science boundary")
    _rj_validate_certificate(certificate)
    phase = "OUTPUT_VALIDATED"
    if phase != "OUTPUT_VALIDATED":
        raise RuntimeError("R output boundary")
    return certificate, fixture_bytes


def main():
    if len(sys.argv) != 1:
        raise RuntimeError("R runner takes no arguments")
    token, capability_bytes = _rj_read_capability()
    runner_path = Path(__file__).resolve()
    project_root = runner_path.parents[3]
    paths = {
        "definitions": project_root / "code/candidate_v1/shared/definitions.json",
        "engine": runner_path.parent / "engine.py",
        "fixture": runner_path.parent / "private_fixture.json",
        "runner": runner_path,
    }
    runner_bytes = _rj_read_regular(runner_path)
    if _rj_sha(runner_bytes) != token["runner_sha256"]:
        raise RuntimeError("R runner hash")
    allowed_reads = {paths["definitions"], paths["runner"]}
    if token["purpose"] == "REGISTERED_R100":
        allowed_reads.update({paths["engine"], paths["fixture"]})
    state, observed_reads, control = _rj_install_guard(project_root, allowed_reads, paths["engine"])
    definitions_bytes = _rj_read_regular(paths["definitions"])
    if _rj_sha(definitions_bytes) != token["definitions_sha256"]:
        raise RuntimeError("R definitions hash")
    if token["purpose"] == "SAFE_RUNTIME_PROBE":
        _rj_safe_probes(project_root, state)
        response = {
            "access_counters": state,
            "access_log": {
                "allowed_read_counts": observed_reads,
                "purpose": "SAFE_RUNTIME_PROBE",
                "schema": "P13_TRACK_ACCESS_LOG_V1",
                "track": "R",
            },
            "candidate_id": _CANDIDATE,
            "capability_sha256": _rj_sha(capability_bytes),
            "definitions_sha256": _rj_sha(definitions_bytes),
            "purpose": "SAFE_RUNTIME_PROBE",
            "runner_sha256": _rj_sha(runner_bytes),
            "schema": "P13_SAFE_RUNTIME_PROBE_V1",
            "track": "R",
        }
    else:
        certificate, fixture_bytes = _rj_registered(token, paths, state, control, definitions_bytes)
        certificate_bytes = _rj_canonical(certificate)
        access_log = {
            "allowed_read_counts": observed_reads,
            "purpose": "REGISTERED_R100",
            "schema": "P13_TRACK_ACCESS_LOG_V1",
            "track": "R",
        }
        access_log_bytes = _rj_canonical(access_log)
        response = {
            "access_counters": state,
            "access_log_canonical_json": access_log_bytes.decode("ascii"),
            "access_log_sha256": _rj_sha(access_log_bytes),
            "candidate_id": _CANDIDATE,
            "capability_sha256": _rj_sha(capability_bytes),
            "certificate_canonical_json": certificate_bytes.decode("ascii"),
            "certificate_sha256": _rj_sha(certificate_bytes),
            "claim_sha256": token["claim_sha256"],
            "definitions_sha256": _rj_sha(definitions_bytes),
            "engine_sha256": token["engine_sha256"],
            "fixture_sha256": _rj_sha(fixture_bytes),
            "runner_sha256": token["runner_sha256"],
            "schema": "P13_BOUNDED_EXACT_TRACK_ENVELOPE_V1",
            "track": "R",
        }
    if set(state) != _COUNTER_KEYS:
        raise RuntimeError("R access-counter shape")
    os.write(1, _rj_canonical(response))


if __name__ == "__main__":
    main()
