"""Isolated Track-Q capability runner; no project import is permitted."""

import ctypes
import builtins
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
    "bool",
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


def _pairs(pairs):
    output = {}
    for key, value in pairs:
        if key in output:
            raise ValueError("Q duplicate JSON key")
        output[key] = value
    return output


def _reject_constant(value):
    raise ValueError("Q nonfinite JSON constant: " + value)


def _reject_float(value):
    raise ValueError("Q floating JSON number: " + value)


def _strict_load(payload):
    if type(payload) is not bytes:
        raise TypeError("Q JSON bytes required")
    return json.loads(
        payload.decode("utf-8"),
        object_pairs_hook=_pairs,
        parse_constant=_reject_constant,
        parse_float=_reject_float,
    )


def _canonical(value):
    pending = [value]
    while pending:
        item = pending.pop()
        if type(item) not in (dict, list, str, int, bool, type(None)):
            raise TypeError("Q non-JSON canonical value")
        if type(item) is dict:
            if any(type(key) is not str for key in item):
                raise TypeError("Q non-string JSON key")
            pending.extend(item.keys())
            pending.extend(item.values())
        elif type(item) is list:
            pending.extend(item)
    return (
        json.dumps(value, allow_nan=False, ensure_ascii=True, sort_keys=True, separators=(",", ":"))
        + "\n"
    ).encode("ascii")


def _sha(payload):
    return hashlib.sha256(payload).hexdigest()


def _is_hex(value, width):
    return (
        type(value) is str
        and len(value) == width
        and all(character in "0123456789abcdef" for character in value)
    )


def _read_capability():
    chunks = []
    total = 0
    try:
        while True:
            block = os.read(3, 4096)
            if not block:
                break
            chunks.append(block)
            total += len(block)
            if total > 16384:
                raise ValueError("Q capability too large")
    except OSError as exc:
        raise RuntimeError("Q capability descriptor unavailable") from exc
    finally:
        try:
            os.close(3)
        except OSError:
            pass
    payload = b"".join(chunks)
    token = _strict_load(payload)
    if _canonical(token) != payload:
        raise ValueError("Q capability is not canonical")
    if type(token) is not dict or set(token) != _CAPABILITY_KEYS:
        raise ValueError("Q capability keys")
    if token["schema"] != "P13_TRACK_CAPABILITY_V1" or token["track"] != "Q":
        raise ValueError("Q capability identity")
    if token["candidate_id"] != _CANDIDATE:
        raise ValueError("Q capability candidate")
    if token["purpose"] not in ("SAFE_RUNTIME_PROBE", "REGISTERED_R100"):
        raise ValueError("Q capability purpose")
    if not _is_hex(token["nonce"], 32):
        raise ValueError("Q capability nonce")
    for key in ("definitions_sha256", "runner_sha256"):
        if not _is_hex(token[key], 64):
            raise ValueError("Q capability hash")
    if token["purpose"] == "SAFE_RUNTIME_PROBE":
        if any(token[key] is not None for key in ("claim_sha256", "engine_sha256", "fixture_sha256")):
            raise ValueError("Q safe capability contains science binding")
    else:
        if any(
            not _is_hex(token[key], 64)
            for key in ("claim_sha256", "engine_sha256", "fixture_sha256")
        ):
            raise ValueError("Q registered capability hashes")
    return token, payload


def _read_regular(path):
    if path.is_symlink() or not path.is_file():
        raise ValueError("Q regular file required")
    return path.read_bytes()


def _install_guard(project_root, allowed_reads, engine_path):
    state = {key: 0 for key in _COUNTER_KEYS}
    other_track = project_root / "code/candidate_v1/track_r"
    notes = project_root / "notes"
    experiments = project_root / "experiments"
    refine = project_root / "refine-logs"
    adjudicator = project_root / "code/candidate_v1/adjudicator"
    allowed = {path.resolve() for path in allowed_reads}
    engine_resolved = engine_path.resolve()
    labels = {
        path: path.relative_to(project_root.resolve()).as_posix()
        for path in allowed
    }
    observed_reads = {label: 0 for label in sorted(labels.values())}
    control = {"science_active": False}

    def classify(path):
        resolved = path.resolve()
        if resolved == other_track or other_track in resolved.parents:
            return "denied_cross_track_read_count"
        if resolved == adjudicator or adjudicator in resolved.parents:
            return "denied_ledger_read_count"
        if resolved == notes or notes in resolved.parents:
            if "REVIEW" in resolved.name.upper():
                return "denied_review_read_count"
            return "denied_source_read_count"
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
            writing = False
            if type(mode) is str:
                writing = any(marker in mode for marker in ("w", "a", "x", "+"))
            if type(flags) is int:
                writing = writing or bool(
                    flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND)
                )
            category = classify(path)
            if category is not None:
                state[category] += 1
                raise PermissionError("Q denied protected path")
            if writing:
                state["denied_outside_write_count"] += 1
                raise PermissionError("Q writes are denied")
            if control["science_active"] or path not in allowed:
                state["denied_outside_read_count"] += 1
                raise PermissionError("Q read outside allowlist")
            observed_reads[labels[path]] += 1
        elif event in {"os.listdir", "os.scandir"}:
            state["denied_outside_read_count"] += 1
            raise PermissionError("Q directory enumeration denied")
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
            raise PermissionError("Q filesystem mutation denied")
        elif event == "os.chdir":
            state["denied_process_count"] += 1
            raise PermissionError("Q working-directory change denied")
        elif event.startswith("socket."):
            state["denied_network_count"] += 1
            raise PermissionError("Q network denied")
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
            raise PermissionError("Q process denied")
        elif event.startswith("ctypes.dlopen") or event.startswith("ctypes.dlsym"):
            state["denied_dynamic_loader_count"] += 1
            raise PermissionError("Q dynamic loader denied")
        elif event == "import":
            module_name = arguments[0]
            if module_name != "fractions":
                state["denied_dynamic_loader_count"] += 1
                raise PermissionError("Q post-capability import denied")
        elif event == "compile":
            filename = Path(arguments[1]).resolve()
            if filename != engine_resolved:
                state["denied_dynamic_loader_count"] += 1
                raise PermissionError("Q compile denied")
        elif event == "exec":
            code_object = arguments[0]
            if Path(code_object.co_filename).resolve() != engine_resolved:
                state["denied_dynamic_loader_count"] += 1
                raise PermissionError("Q exec denied")

    sys.addaudithook(audit)
    original_import = builtins.__import__

    def guarded_import(name, globals_value=None, locals_value=None, fromlist=(), level=0):
        if name == "fractions" and level == 0:
            return original_import(name, globals_value, locals_value, fromlist, level)
        state["denied_dynamic_loader_count"] += 1
        raise PermissionError("Q cached or dynamic import denied")

    builtins.__import__ = guarded_import
    return state, observed_reads, control


def _expect_denied(callable_object, counter_name, state):
    before = state[counter_name]
    try:
        callable_object()
    except PermissionError:
        pass
    else:
        raise RuntimeError("Q denial probe unexpectedly succeeded")
    if state[counter_name] != before + 1:
        raise RuntimeError("Q denial probe counter")


def _probe_write_open(path):
    descriptor = os.open(path, os.O_WRONLY)
    os.close(descriptor)


def _probe_scandir(path):
    handle = os.scandir(path)
    handle.close()


def _probe_rename(source, target):
    os.rename(source, target)


def _probe_unlink(path):
    os.unlink(path)


def _run_safe_probes(project_root, state):
    _expect_denied(
        lambda: open(project_root / "notes/PROOF_PACKAGE.md", "rb"),
        "denied_source_read_count",
        state,
    )
    _expect_denied(
        lambda: open(project_root / "notes/INDEPENDENT_SOURCE_LOCK_REVIEW_R2.md", "rb"),
        "denied_review_read_count",
        state,
    )
    _expect_denied(
        lambda: open(project_root / "code/candidate_v1/adjudicator/acceptance_ledger.json", "rb"),
        "denied_ledger_read_count",
        state,
    )
    _expect_denied(
        lambda: open(project_root / "code/candidate_v1/track_r/engine.py", "rb"),
        "denied_cross_track_read_count",
        state,
    )
    _expect_denied(lambda: open("/etc/hosts", "rb"), "denied_outside_read_count", state)
    _expect_denied(lambda: os.listdir(project_root), "denied_outside_read_count", state)
    _expect_denied(lambda: _probe_scandir(project_root), "denied_outside_read_count", state)
    _expect_denied(
        lambda: _probe_write_open(project_root / "code/candidate_v1/shared/definitions.json"),
        "denied_outside_write_count",
        state,
    )
    _expect_denied(
        lambda: _probe_rename(project_root / "never_source", project_root / "never_target"),
        "denied_outside_write_count",
        state,
    )
    _expect_denied(
        lambda: _probe_unlink(project_root / "never_unlink"),
        "denied_outside_write_count",
        state,
    )
    _expect_denied(lambda: socket.socket(), "denied_network_count", state)
    _expect_denied(lambda: os.system(":"), "denied_process_count", state)
    _expect_denied(lambda: os.fork(), "denied_process_count", state)
    _expect_denied(lambda: ctypes.CDLL(None), "denied_dynamic_loader_count", state)
    _expect_denied(lambda: __import__("os"), "denied_dynamic_loader_count", state)
    probe_builtins = _build_science_builtins(lambda *arguments, **keywords: None)
    for forbidden_name in ("open", "compile", "exec", "eval", "globals", "getattr"):
        if forbidden_name in probe_builtins:
            raise RuntimeError("Q dangerous science builtin exposed")


def _build_science_builtins(restricted_import):
    if any(
        vars(builtins).get(name) is not _SCIENCE_BUILTIN_OBJECTS[name]
        for name in _SCIENCE_BUILTIN_NAMES
    ):
        raise RuntimeError("Q builtin identity drift")
    output = dict(_SCIENCE_BUILTIN_OBJECTS)
    output["__import__"] = restricted_import
    return output


def _exact_keys(value, keys, label):
    if type(value) is not dict or set(value) != set(keys):
        raise ValueError("Q output keys: " + label)


def _validate_rational_wire(value):
    _exact_keys(value, {"denominator", "numerator"}, "rational")
    if type(value["numerator"]) is not int or type(value["denominator"]) is not int:
        raise TypeError("Q rational wire integers")
    if value["denominator"] <= 0:
        raise ValueError("Q rational wire denominator")
    if gcd(abs(value["numerator"]), value["denominator"]) != 1:
        raise ValueError("Q rational wire not reduced")
    if value["numerator"] == 0 and value["denominator"] != 1:
        raise ValueError("Q zero rational is not canonical")


def _validate_poly_wire(value):
    if type(value) is not list:
        raise TypeError("Q polynomial wire list")
    previous = None
    for term in value:
        _exact_keys(term, {"coefficient", "exponents_acz0z1"}, "polynomial term")
        _validate_rational_wire(term["coefficient"])
        if term["coefficient"]["numerator"] == 0:
            raise ValueError("Q zero polynomial term")
        exponents = term["exponents_acz0z1"]
        if (
            type(exponents) is not list
            or len(exponents) != 4
            or any(type(item) is not int or item < 0 for item in exponents)
        ):
            raise TypeError("Q exponent wire")
        key = tuple(exponents)
        if previous is not None and key <= previous:
            raise ValueError("Q polynomial terms not strictly sorted")
        previous = key


def _validate_rejection_list(value, value_key):
    if type(value) is not list or len(value) != 2:
        raise ValueError("Q rejection list length")
    seen = set()
    for item in value:
        _exact_keys(item, {"disposition", value_key}, "rejection")
        if type(item["disposition"]) is not str or type(item[value_key]) is not str:
            raise TypeError("Q rejection strings")
        seen.add(item[value_key])
    if len(seen) != 2:
        raise ValueError("Q duplicate rejection")


def _validate_certificate(certificate):
    _exact_keys(
        certificate,
        {"candidate_id", "certificate_kind", "controls", "route", "schema", "track"},
        "certificate",
    )
    if certificate["candidate_id"] != _CANDIDATE or certificate["track"] != "Q":
        raise ValueError("Q certificate identity")
    if (
        certificate["schema"] != "P13_Q_EXACT_CERTIFICATE_V1"
        or certificate["route"] != "CYCLIC_QUOTIENT_REDUCTION"
        or certificate["certificate_kind"] != "BOUNDED_EXACT_CONSISTENCY_RECORD"
    ):
        raise ValueError("Q certificate constants")
    controls = certificate["controls"]
    _exact_keys(controls, {"N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8"}, "controls")
    _exact_keys(controls["N1"], {"dynatomic_at_point", "first_iterate_at_point", "multiplier", "unsafe_inference"}, "N1")
    for key in ("dynatomic_at_point", "first_iterate_at_point", "multiplier"):
        _validate_rational_wire(controls["N1"][key])
    if controls["N1"]["unsafe_inference"] != "REJECTED_FORMAL_TO_ACTUAL":
        raise ValueError("Q N1 disposition")
    _exact_keys(controls["N2"], {"generic_discriminant", "generic_separable", "special_basis_exponents", "special_generator_nonzero", "special_nilpotent_square", "unsafe_inference"}, "N2")
    _validate_poly_wire(controls["N2"]["generic_discriminant"])
    if type(controls["N2"]["generic_separable"]) is not bool or type(controls["N2"]["special_generator_nonzero"]) is not bool:
        raise TypeError("Q N2 booleans")
    if type(controls["N2"]["special_basis_exponents"]) is not list or any(type(item) is not int for item in controls["N2"]["special_basis_exponents"]):
        raise TypeError("Q N2 basis")
    if type(controls["N2"]["special_nilpotent_square"]) is not list:
        raise TypeError("Q N2 nilpotent wire")
    for item in controls["N2"]["special_nilpotent_square"]:
        _validate_rational_wire(item)
    if controls["N2"]["unsafe_inference"] != "REJECTED_GENERIC_TO_ALL_FIBERS":
        raise ValueError("Q N2 disposition")
    _exact_keys(controls["N3"], {"finite_module_generator_exponents", "fraction_exponent_identity", "normalizer_exponent_in_subring_semigroup", "unsafe_inference"}, "N3")
    if type(controls["N3"]["finite_module_generator_exponents"]) is not list or any(type(item) is not int for item in controls["N3"]["finite_module_generator_exponents"]):
        raise TypeError("Q N3 module exponents")
    if type(controls["N3"]["fraction_exponent_identity"]) is not list or len(controls["N3"]["fraction_exponent_identity"]) != 3 or any(type(item) is not int for item in controls["N3"]["fraction_exponent_identity"]):
        raise TypeError("Q N3 fraction exponents")
    if type(controls["N3"]["normalizer_exponent_in_subring_semigroup"]) is not bool:
        raise TypeError("Q N3 semigroup flag")
    if controls["N3"]["unsafe_inference"] != "REJECTED_BIRATIONAL_TO_NORMAL_EQUALITY":
        raise ValueError("Q N3 disposition")
    _exact_keys(controls["N4"], {"characteristic_polynomial_rho", "characteristic_polynomial_tau", "cycle_product", "cycle_sum", "degree_one_boundary", "derivative_trace", "nontrivial_monodromy_evidence", "nu", "rank", "reduction_probe", "reduction_step_count", "reynolds_z0", "standard_cycle_exponents"}, "N4")
    for key in ("cycle_product", "cycle_sum", "derivative_trace", "reduction_probe", "reynolds_z0"):
        _validate_poly_wire(controls["N4"][key])
    for key in ("characteristic_polynomial_rho", "characteristic_polynomial_tau"):
        if type(controls["N4"][key]) is not list or len(controls["N4"][key]) != 2:
            raise TypeError("Q characteristic wire")
        for polynomial in controls["N4"][key]:
            _validate_poly_wire(polynomial)
    if any(type(controls["N4"][key]) is not int for key in ("nu", "rank", "reduction_step_count")):
        raise TypeError("Q N4 integer")
    if any(type(controls["N4"][key]) is not bool for key in ("degree_one_boundary", "nontrivial_monodromy_evidence")):
        raise TypeError("Q N4 boolean")
    standard = controls["N4"]["standard_cycle_exponents"]
    if type(standard) is not list or any(type(item) is not list or len(item) != 2 or any(type(exponent) is not int for exponent in item) for item in standard):
        raise TypeError("Q standard exponent wire")
    if len({tuple(item) for item in standard}) != len(standard) or standard != sorted(standard):
        raise ValueError("Q standard exponents not unique and sorted")
    _validate_rejection_list(controls["N5"], "assertion")
    _validate_rejection_list(controls["N6"], "assertion")
    _exact_keys(controls["N7"], {"disposition", "proposed"}, "N7")
    if controls["N7"] != {"disposition": "REJECTED_DIRECTION", "proposed": "global_to_special"}:
        raise ValueError("Q N7 disposition")
    _validate_rejection_list(controls["N8"], "replacement")
    for identifier in ("N5", "N6"):
        if any(item["disposition"] != "REJECTED_SCOPE_ERROR" for item in controls[identifier]):
            raise ValueError("Q scope disposition")
    if any(item["disposition"] != "REJECTED_CATEGORY_SUBSTITUTION" for item in controls["N8"]):
        raise ValueError("Q N8 disposition")
    payload = _canonical(certificate)
    if b"PROVED" in payload or (b"SOURCE" + b"_LOCK_PASS") in payload:
        raise ValueError("Q forbidden authority language")


def _registered_science(token, project_root, paths, state, control, definitions_bytes):
    fixture_bytes = _read_regular(paths["fixture"])
    engine_bytes = _read_regular(paths["engine"])
    if _sha(definitions_bytes) != token["definitions_sha256"]:
        raise RuntimeError("Q definitions hash mismatch")
    if _sha(fixture_bytes) != token["fixture_sha256"]:
        raise RuntimeError("Q fixture hash mismatch")
    if _sha(engine_bytes) != token["engine_sha256"]:
        raise RuntimeError("Q engine hash mismatch")
    definitions = _strict_load(definitions_bytes)
    fixture = _strict_load(fixture_bytes)
    def restricted_import(name, globals_value=None, locals_value=None, fromlist=(), level=0):
        if name != "fractions" or level != 0:
            raise ImportError("Q engine import denied")
        return sys.modules["fractions"]

    safe_builtins = _build_science_builtins(restricted_import)
    namespace = {
        "__builtins__": safe_builtins,
        "__name__": "p13_track_q_engine",
        "__file__": str(paths["engine"]),
        "Fraction": Fraction,
    }
    control["science_active"] = True
    code = compile(engine_bytes, str(paths["engine"]), "exec", dont_inherit=True, optimize=0)
    exec(code, namespace, namespace)
    run_science = namespace.get("run_science")
    if not callable(run_science):
        raise RuntimeError("Q run_science missing")
    phase = "CAPABILITY_VERIFIED"
    if state["run_science_call_count"] != 0 or phase != "CAPABILITY_VERIFIED":
        raise RuntimeError("Q pre-science phase")
    phase = "SCIENCE_ENTERED"
    state["run_science_call_count"] = 1
    try:
        certificate = run_science(definitions, fixture)
    except BaseException:
        phase = "SCIENCE_FAILED"
        raise
    phase = "SCIENCE_RETURNED"
    if phase != "SCIENCE_RETURNED" or state["run_science_call_count"] != 1:
        raise RuntimeError("Q post-science phase")
    _validate_certificate(certificate)
    phase = "OUTPUT_VALIDATED"
    if phase != "OUTPUT_VALIDATED":
        raise RuntimeError("Q output phase")
    return certificate, definitions_bytes, fixture_bytes


def main():
    if len(sys.argv) != 1:
        raise RuntimeError("Q runner takes no arguments")
    token, capability_bytes = _read_capability()
    runner_path = Path(__file__).resolve()
    project_root = runner_path.parents[3]
    paths = {
        "definitions": project_root / "code/candidate_v1/shared/definitions.json",
        "engine": runner_path.parent / "engine.py",
        "fixture": runner_path.parent / "private_fixture.json",
        "runner": runner_path,
    }
    runner_bytes = _read_regular(runner_path)
    if _sha(runner_bytes) != token["runner_sha256"]:
        raise RuntimeError("Q runner hash mismatch")
    allowed_reads = {paths["definitions"], paths["runner"]}
    if token["purpose"] == "REGISTERED_R100":
        allowed_reads.update({paths["engine"], paths["fixture"]})
    state, observed_reads, control = _install_guard(project_root, allowed_reads, paths["engine"])
    definitions_bytes = _read_regular(paths["definitions"])
    if _sha(definitions_bytes) != token["definitions_sha256"]:
        raise RuntimeError("Q definitions hash mismatch")
    if token["purpose"] == "SAFE_RUNTIME_PROBE":
        _run_safe_probes(project_root, state)
        response = {
            "access_counters": state,
            "access_log": {
                "allowed_read_counts": observed_reads,
                "purpose": "SAFE_RUNTIME_PROBE",
                "schema": "P13_TRACK_ACCESS_LOG_V1",
                "track": "Q",
            },
            "candidate_id": _CANDIDATE,
            "capability_sha256": _sha(capability_bytes),
            "definitions_sha256": _sha(definitions_bytes),
            "purpose": "SAFE_RUNTIME_PROBE",
            "runner_sha256": _sha(runner_bytes),
            "schema": "P13_SAFE_RUNTIME_PROBE_V1",
            "track": "Q",
        }
    else:
        certificate, definitions_bytes, fixture_bytes = _registered_science(
            token, project_root, paths, state, control, definitions_bytes
        )
        certificate_bytes = _canonical(certificate)
        access_log = {
            "allowed_read_counts": observed_reads,
            "purpose": "REGISTERED_R100",
            "schema": "P13_TRACK_ACCESS_LOG_V1",
            "track": "Q",
        }
        access_log_bytes = _canonical(access_log)
        response = {
            "access_counters": state,
            "access_log_canonical_json": access_log_bytes.decode("ascii"),
            "access_log_sha256": _sha(access_log_bytes),
            "candidate_id": _CANDIDATE,
            "capability_sha256": _sha(capability_bytes),
            "certificate_canonical_json": certificate_bytes.decode("ascii"),
            "certificate_sha256": _sha(certificate_bytes),
            "claim_sha256": token["claim_sha256"],
            "definitions_sha256": _sha(definitions_bytes),
            "engine_sha256": token["engine_sha256"],
            "fixture_sha256": _sha(fixture_bytes),
            "runner_sha256": token["runner_sha256"],
            "schema": "P13_BOUNDED_EXACT_TRACK_ENVELOPE_V1",
            "track": "Q",
        }
    if set(state) != _COUNTER_KEYS:
        raise RuntimeError("Q access-counter shape")
    os.write(1, _canonical(response))


if __name__ == "__main__":
    main()
