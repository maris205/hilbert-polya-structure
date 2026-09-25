#!/usr/bin/env python3
"""User-authorized CS08 fixed-winner completion. No optimizer or reselection."""
import csv
from datetime import datetime, timezone
import gc
import hashlib
import importlib.util
import io
import json
import math
import os
from pathlib import Path
import resource
import sys
import threading
import time

import numpy as np
import scipy


PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[1]
OLD = PACKAGE/"evidence/run-1"
OUT = PACKAGE/"evidence/run-2-fixed"
SOURCE = PACKAGE/"run_search.py"
LOCK_FILE = PACKAGE/"repair-input-locks.json"
OLD_LOCK_FILE = PACKAGE/"input-locks.json"
OLD_INVENTORY = PACKAGE/"evidence/failed-run-inventory.json"
SCOPE, EXECUTION = "ASFS-DISCOVERY-20260919-CS08", "CS08-REPAIR-FIXED-01"
FORMS = ("B", "O", "Q", "U", "D")
MEMBER_IDS = {"B": "CS08-B-BASE-REFIT-0068", "O": "CS08-O-OCTIC-0089",
              "Q": "CS08-Q-QUINTIC-0107", "U": "CS08-U-LOG-ENHANCED-0135",
              "D": "CS08-D-LOG-RETARDED-0158"}
PHYSICAL_KEYS = ("theta", "form_key", "grid_n", "L", "sample_count", "beta", "q", "p",
                 "kinetic_minus_mass", "midpoint_u", "schedule", "W_samples", "mean_W",
                 "minimum_values", "minimizers", "potential_mode")
CANONICAL_KEYS = ("sigma", "energy", "energy_resolved_mask", "predicted_320", "scale",
                  "resolution_valid", "invalid_reasons", "target_100")
GIB = 1024**3
COMMAND = ("OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 "
           "PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 600s python -u "
           "papers/258-shape-dispersion-heat-search/resume_fixed.py")


def utc():
    return datetime.now(timezone.utc).isoformat()


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def make_logger(stream, echo=False):
    lock = threading.Lock()

    def event(event_type, /, **fields):
        if "event" in fields or "utc" in fields:
            raise ValueError("Event metadata must not overwrite event/utc fields")
        with lock:
            line = json.dumps({"utc": utc(), "event": event_type, **fields}, allow_nan=False)
            stream.write(line+"\n")
            stream.flush()
            if echo:
                print(line, flush=True)
    return event


def logger_regression_test():
    """Exercise the four real name= call shapes without scientific numerics."""
    stream = io.StringIO()
    event = make_logger(stream)
    cases = (
        ("winner_state_readout_start", {"name": "winner-B-N511", "not_a_propagation": True}),
        ("winner_state_readout_complete", {"name": "winner-B-N511", "counters": {"completed": 1}}),
        ("propagation_start", {"stage": "postfreeze", "name": "post-Q-N1023", "form": "Q"}),
        ("propagation_complete", {"stage": "postfreeze", "name": "post-Q-N1023", "status": "VALID"}),
    )
    for event_type, fields in cases:
        event(event_type, **fields)
    rows = [json.loads(line) for line in stream.getvalue().splitlines()]
    if len(rows) != len(cases):
        raise AssertionError("Logger dropped a regression event")
    for row, (event_type, fields) in zip(rows, cases):
        if row["event"] != event_type or any(row[key] != value for key, value in fields.items()):
            raise AssertionError("Logger confused event type with name metadata")
    for reserved in ("event", "utc"):
        try:
            event("reserved_field_test", **{reserved: "must not overwrite"})
        except ValueError:
            pass
        else:
            raise AssertionError("Logger allowed reserved-field overwrite")
    if len(stream.getvalue().splitlines()) != len(cases):
        raise AssertionError("Rejected reserved metadata still produced an event")
    return {"passed": True, "case_count": len(cases), "event_and_name_preserved": True,
            "events_tested": [row["event"] for row in rows], "reserved_event_utc_rejected": True,
            "scientific_numerics_performed": False}


def verify_inputs():
    repair_locks = json.loads(LOCK_FILE.read_text())
    old_locks = json.loads(OLD_LOCK_FILE.read_text())
    if len(repair_locks) != 34 or len(old_locks) != 16:
        raise RuntimeError("Frozen input-lock cardinality changed")
    for locks in (repair_locks, old_locks):
        for relative, expected in locks.items():
            if sha(ROOT/relative) != expected:
                raise RuntimeError(f"Input hash mismatch: {relative}")
    inventory = json.loads(OLD_INVENTORY.read_text())["files"]
    actual = {str(path.relative_to(OLD)) for path in OLD.rglob("*") if path.is_file()}
    if len(inventory) != 815 or actual != set(inventory):
        raise RuntimeError("Original run-1 file membership differs from 815-file inventory")
    for relative, row in inventory.items():
        path = OLD/relative
        if path.stat().st_size != row["bytes"] or sha(path) != row["sha256"]:
            raise RuntimeError(f"Original run-1 file size/hash changed: {relative}")
    return {"repair_locks_checked": 34, "original_locks_checked": 16,
            "original_files_checked": 815, "all_sizes_and_sha256_match": True,
            "repair_input_locks_sha256": sha(LOCK_FILE), "old_inventory_sha256": sha(OLD_INVENTORY)}


def import_helper():
    spec = importlib.util.spec_from_file_location("cs08_immutable_helpers", SOURCE)
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    return helper


def equal_array(left, right):
    if left.dtype.kind in "fc" and right.dtype.kind in "fc":
        return np.array_equal(left, right, equal_nan=True)
    return np.array_equal(left, right)


def difference_summary(left, right):
    shared = np.isfinite(left) & np.isfinite(right)
    return {"common_finite_count": int(np.count_nonzero(shared)),
            "finite_masks_equal": bool(np.array_equal(np.isfinite(left), np.isfinite(right))),
            "max_absolute_difference_on_common_finite": float(np.max(np.abs(left[shared]-right[shared]))) if np.any(shared) else None}


class BoundedOutput:
    """Serialize before writing; all new evidence shares one byte-budget lock."""
    def __init__(self, directory, byte_limit):
        self.directory, self.byte_limit = directory, byte_limit
        self.lock = threading.Lock()

    def size(self):
        return sum(path.stat().st_size for path in self.directory.rglob("*") if path.is_file())

    def _guard(self, extra):
        if self.size()+extra > self.byte_limit:
            raise RuntimeError("New-run 1 GiB output budget would be exceeded; no retry")

    def binary(self, name, payload):
        with self.lock:
            self._guard(len(payload))
            with (self.directory/name).open("xb") as handle:
                handle.write(payload)

    def json(self, name, value):
        self.binary(name, (json.dumps(value, indent=2, allow_nan=False)+"\n").encode("utf-8"))

    def npz(self, name, arrays):
        buffer = io.BytesIO()
        np.savez_compressed(buffer, **arrays)
        self.binary(name, buffer.getbuffer())

    def text_stream(self, name):
        owner = self
        handle = (self.directory/name).open("xb")

        class Stream:
            def write(self, text):
                payload = text.encode("utf-8")
                with owner.lock:
                    owner._guard(len(payload))
                    handle.write(payload)
                    handle.flush()
                return len(text)

            def flush(self):
                handle.flush()

            def close(self):
                handle.close()
        return Stream()


def main():
    started = time.perf_counter()
    logging_test = logger_regression_test()
    initial_verification = verify_inputs()
    if OUT.exists():
        raise RuntimeError("New output directory exists; refusing overwrite or retry")
    OUT.mkdir(parents=True)
    output = BoundedOutput(OUT, GIB)
    event_stream = output.text_stream("events.jsonl")
    ledger_stream = output.text_stream("minimum-ledger.jsonl")
    event = make_logger(event_stream, echo=True)
    monitor_stop = threading.Event()
    counters = {"propagations_attempted": 0, "propagations_completed": 0,
                "reconstruction_propagations_attempted": 0, "reconstruction_propagations_completed": 0,
                "postfreeze_propagations_attempted": 0, "postfreeze_propagations_completed": 0,
                "full_svd_attempted": 0, "full_svd_completed": 0,
                "static_readouts_attempted": 0, "static_readouts_completed": 0,
                "optimization_calls": 0, "new_target_generations": 0}
    helper_counters = {"minimum_scalar_solves": 0, "minimum_cache_hits": 0, "brent_calls": 0,
                       "static_eigh_calls": 0}
    final_verification = None

    def resources():
        while not monitor_stop.wait(30):
            rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            event("resource_sample", pid=os.getpid(), seconds=time.perf_counter()-started,
                  maxrss_kib=rss, memory_above_1gib_advisory=bool(rss*1024 > GIB),
                  output_bytes=output.size(), counters=dict(counters), helper_internal_attempts=dict(helper_counters))

    monitor = threading.Thread(target=resources, daemon=True)
    monitor.start()
    try:
        helper = import_helper()
        source = helper.import_source()
        original_winner_bytes = (OLD/"winners-frozen.json").read_bytes()
        frozen = json.loads(original_winner_bytes)
        roles = frozen["roles"]
        if (frozen["scope_id"] != SCOPE or frozen["global_joint_winner"] != "Q" or set(roles) != set(FORMS)
                or any(roles[form]["evaluation_id"] != MEMBER_IDS[form] for form in FORMS)):
            raise RuntimeError("Fixed member identity or primary differs from repair card")
        primary = "Q"
        output.binary("winners-frozen-original.json", original_winner_bytes)
        output.json("logger-regression.json", logging_test)
        manifest = {"scope_id": SCOPE, "execution_id": EXECUTION, "started_utc": utc(), "pid": os.getpid(),
                    "command": COMMAND, "script_sha256": sha(Path(__file__)), "helper_sha256": sha(SOURCE),
                    "repair_input_locks_sha256": sha(LOCK_FILE), "inputs": json.loads(LOCK_FILE.read_text()),
                    "start_verification": initial_verification, "original_winners_sha256": sha(OLD/"winners-frozen.json"),
                    "original_winners_copy_sha256": sha(OUT/"winners-frozen-original.json"),
                    "python": sys.version, "numpy": np.__version__, "scipy": scipy.__version__,
                    "thread_environment": {key: os.environ.get(key) for key in
                                           ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")},
                    "fixed_primary": primary, "fixed_member_ids": MEMBER_IDS,
                    "new_forward_budget": 22, "full_svd_budget": 22, "static_readout_budget": 22,
                    "extra_reconstruction_forwards": 10, "original_pending_post_forwards": 12,
                    "old_run_completed_forwards": 323, "old_control_reruns": 0,
                    "old_main_or_optimizer_called": False, "old_module_globals_mutated": False,
                    "helper_internal_attempts_are_not_completed_readouts": True,
                    "canonical_training_arrays": "run-1 sigma/E/mask/prediction/scale; reconstruction fields are separate",
                    "original_minimum_ids_reference": "../run-1/minimum-ledger.jsonl",
                    "new_minimum_ids_reference": "minimum-ledger.jsonl",
                    "all_targets_previously_observed": True, "run_passport": "UNVERIFIED",
                    "not_an_independent_rerun_of_search": True, "output_hard_limit_bytes": GIB,
                    "memory_advisory_bytes": GIB, "timeout_seconds": 600,
                    "process_exit_code": "recorded externally by launcher", "logging_regression": logging_test}
        output.json("manifest.json", manifest)
        event("started", pid=os.getpid(), execution_id=EXECUTION, fixed_primary=primary)
        with np.load(helper.TARGET_SOURCE, allow_pickle=False) as old_target:
            target = old_target["target_100"].copy()
        if len(target) != 100 or not np.all(np.isfinite(target)) or target[0] <= 0 or not np.all(np.diff(target) > 0):
            raise RuntimeError("Invalid original first-100 target")
        minimum_cache, minimum_ledger = {}, []
        members, member_metadata, reconstructions, static_records, post_records = {}, {}, {}, {}, {}
        frozen_files = []

        def propagate_and_decompose(form, theta, n, length, count, name, reconstruction):
            if counters["propagations_attempted"] >= 22:
                raise RuntimeError("Propagation budget exhausted")
            stage = "reconstruction" if reconstruction else "postfreeze"
            counters["propagations_attempted"] += 1
            counters[stage+"_propagations_attempted"] += 1
            event("propagation_start", stage=stage, name=name, form=form, theta=theta.tolist(),
                  N=n, L=length, B=count, counters=dict(counters))
            tick = time.perf_counter()
            arrays, record = helper.propagate(source, form, theta, n, length, count,
                                              minimum_cache, minimum_ledger, helper_counters, ledger_stream)
            counters["propagations_completed"] += 1
            counters[stage+"_propagations_completed"] += 1
            record["propagation_seconds"] = time.perf_counter()-tick
            event("propagation_complete", stage=stage, name=name, counters=dict(counters))
            if counters["full_svd_attempted"] >= 22:
                raise RuntimeError("Full SVD budget exhausted")
            counters["full_svd_attempted"] += 1
            event("full_svd_start", name=name, counters=dict(counters))
            tick = time.perf_counter()
            left, sigma, right_t = np.linalg.svd(arrays["C_tilde"], full_matrices=True)
            counters["full_svd_completed"] += 1
            record["full_svd_seconds"] = time.perf_counter()-tick
            event("full_svd_complete", name=name, counters=dict(counters))
            return arrays, record, left, sigma, right_t

        def save_heat_and_static(name, arrays, record, stage):
            form = record["form_key"]
            members[name] = helper.compact(arrays, record["resolution_valid"])
            meta = {"kind": "heat", "stage": stage, "form": form, "N": int(arrays["grid_n"]),
                    "L": float(arrays["L"]), "B": int(arrays["sample_count"])}
            member_metadata[name] = meta
            output.npz(name+".npz", arrays)
            output.json(name+".json", record)
            if counters["static_readouts_attempted"] >= 22:
                raise RuntimeError("Static readout budget exhausted")
            counters["static_readouts_attempted"] += 1
            event("static_readout_start", name=name, not_a_propagation=True, counters=dict(counters))
            static_arrays, static_record = helper.static_readout(arrays, target, helper_counters)
            counters["static_readouts_completed"] += 1
            static_name = "static-"+name
            static_arrays["minimum_ledger_path"] = np.array("minimum-ledger.jsonl")
            static_record.update(heat_owner=name, form_key=form, minimum_ledger_path="minimum-ledger.jsonl")
            members[static_name] = helper.compact(static_arrays)
            member_metadata[static_name] = {**meta, "kind": "static"}
            static_records[static_name] = static_record
            output.npz(static_name+".npz", static_arrays)
            output.json(static_name+".json", static_record)
            del static_arrays
            event("static_readout_complete", name=static_name, counters=dict(counters), helper_internal_attempts=dict(helper_counters))
            return [name+".npz", name+".json", static_name+".npz", static_name+".json"]

        for form in FORMS:
            theta = np.array(roles[form]["theta"])
            for n in (511, 639):
                name = f"winner-{form}-N{n}"
                original_path = OLD/"evaluations"/f"{MEMBER_IDS[form]}-N{n}.npz"
                with np.load(original_path, allow_pickle=False) as loaded:
                    original = {key: loaded[key].copy() for key in loaded.files}
                if (not np.array_equal(original["theta"], theta) or not np.array_equal(original["target_100"], target)
                        or str(original["evaluation_id"]) != MEMBER_IDS[form]):
                    raise RuntimeError("Original compact member identity/target mismatch")
                event("winner_state_readout_start", name=name, reconstruction_is_new_propagation=True)
                arrays, record, left, sigma, right_t = propagate_and_decompose(form, theta, n, 8., 64, name, True)
                exact = {key: equal_array(arrays[key], original[key]) for key in PHYSICAL_KEYS}
                if not all(exact.values()):
                    raise RuntimeError("Reconstructed physical inputs differ: "+str([key for key, value in exact.items() if not value]))
                original_derived, original_validity = helper.readout(original["sigma"], float(theta[2]), .02, target)
                original_readout_equal = {key: equal_array(original_derived[key], original[key]) for key in CANONICAL_KEYS}
                if not all(original_readout_equal.values()) or not original_validity["resolution_valid"]:
                    raise RuntimeError("Original canonical readout/mask/validity no longer matches its sigma")
                reconstructed, reconstructed_validity = helper.readout(sigma, float(theta[2]), .02, target)
                sigma_difference = float(np.max(np.abs(sigma-original["sigma"])))
                checks = {"exact_physical_arrays": exact, "original_readout_exact": original_readout_equal,
                          "sigma_max_absolute_difference": sigma_difference, "sigma_tolerance": 1e-12,
                          "reconstructed_validity": reconstructed_validity,
                          "raw_energy_difference": difference_summary(reconstructed["energy"], original["energy"]),
                          "first320_energy_difference": difference_summary(reconstructed["energy"][:320], original["energy"][:320]),
                          "prediction_difference": difference_summary(reconstructed["predicted_320"], original["predicted_320"]),
                          "scale_absolute_difference": abs(float(reconstructed["scale"])-float(original["scale"])),
                          "reconstructed_mask_equals_original": bool(np.array_equal(reconstructed["energy_resolved_mask"], original["energy_resolved_mask"])),
                          "original_validity": original_validity,
                          "no_extra_energy_error_gate": True, "no_sigma_clipping": True}
                if not math.isfinite(sigma_difference) or sigma_difference > 1e-12 or not reconstructed_validity["resolution_valid"]:
                    output.json(name+"-consistency-failure.json", checks)
                    raise RuntimeError("Reconstruction sigma/validity consistency failed; no reselection or retry")
                for key, value in reconstructed.items():
                    arrays["reconstruction_"+key] = value.copy()
                for key in CANONICAL_KEYS:
                    arrays[key] = original[key].copy()
                arrays.update(evaluation_id=original["evaluation_id"].copy(),
                              original_minimum_ids=original["minimum_ids"].copy(),
                              original_minimum_ledger_path=np.array("../run-1/minimum-ledger.jsonl"),
                              minimum_ledger_path=np.array("minimum-ledger.jsonl"),
                              original_compact_sha256=np.array(sha(original_path)))
                record.update(original_validity, evaluation_id=MEMBER_IDS[form], consistency=checks,
                              original_compact_path=str(original_path.relative_to(ROOT)), original_compact_sha256=sha(original_path),
                              original_minimum_ids=original["minimum_ids"].tolist(),
                              original_minimum_ledger_path="../run-1/minimum-ledger.jsonl", minimum_ledger_path="minimum-ledger.jsonl",
                              training_metrics=roles[form]["grids"][str(n)]["training_metrics"],
                              selection_J=roles[form]["joint_score"], canonical_selection_arrays_preserved=True,
                              no_reselection=True, C_saved=True)
                helper.add_states(arrays, left, right_t, record)
                del left, right_t, sigma, reconstructed, original_derived, original
                reconstructions[name] = record
                frozen_files.extend(save_heat_and_static(name, arrays, record, "reconstructed-training-winner"))
                del arrays
                gc.collect()
                event("winner_state_readout_complete", name=name, counters=dict(counters))
        freeze = {"scope_id": SCOPE, "execution_id": EXECUTION, "frozen_utc": utc(),
                  "original_winners_sha256": sha(OLD/"winners-frozen.json"), "fixed_primary": primary,
                  "original_winners_copy_path": "winners-frozen-original.json",
                  "original_winners_copy_sha256": sha(OUT/"winners-frozen-original.json"),
                  "full_heat_arrays": 10, "full_static_arrays": 10,
                  "files_sha256": {name: sha(OUT/name) for name in frozen_files},
                  "development_metrics_evaluated": False, "counters": dict(counters),
                  "canonical_selection_owner": "run-1; unchanged"}
        output.json("training-arrays-frozen.json", freeze)
        event("training_arrays_frozen", sha256=sha(OUT/"training-arrays-frozen.json"), counters=dict(counters))
        event("development_reference_read_start", all_previously_observed=True, no_selection=True)
        portions = []
        for path, count in helper.REFERENCES:
            values = np.array([float(value) for value in json.loads(path.read_text())["ordinates"]])
            if len(values) != count:
                raise RuntimeError("Known reference length mismatch")
            portions.append(values)
        truth = np.concatenate([target, *portions])
        if len(truth) != 320 or not np.all(np.isfinite(truth)) or not np.all(np.diff(truth) > 0):
            raise RuntimeError("Invalid historical reference ledger")
        output.json("known-targets.json", {"first": 1, "last": 320, "ordinates": truth.tolist(),
                                           "all_previously_observed": True, "generated_by_this_run": False})
        with np.load(helper.OLD257/"CS07-A3-N1535.npz", allow_pickle=False) as old:
            if not np.array_equal(old["theta"], helper.BASE) or not np.array_equal(old["target_320"], truth):
                raise RuntimeError("Old S0047 diagnostic comparator identity/target mismatch")
            members["old-S0047-N1535"] = {"prediction": old["predicted"].copy(), "energy": old["energy"][:320].copy(),
                                          "scale": float(old["scale"]), "valid": bool(old["resolution_valid"]),
                                          "invalid_reasons": old["invalid_reasons"].tolist()}
            member_metadata["old-S0047-N1535"] = {"kind": "reused", "stage": "old-fixed-comparator", "form": "S0047", "N": 1535, "L": 8., "B": 64}

        def post(form, n, length, count, name):
            theta = np.array(roles[form]["theta"])
            arrays, record, left, sigma, right_t = propagate_and_decompose(form, theta, n, length, count, name, False)
            readout_arrays, validity = helper.readout(sigma, float(theta[2]), .02, target)
            arrays.update(readout_arrays)
            arrays["minimum_ledger_path"] = np.array("minimum-ledger.jsonl")
            record.update(validity, source_evaluation_id=MEMBER_IDS[form], no_selection=True,
                          minimum_ledger_path="minimum-ledger.jsonl", C_saved=True,
                          training_metrics=helper.metrics(arrays["predicted_320"][:100], target) if validity["resolution_valid"] else None)
            helper.add_states(arrays, left, right_t, record)
            record["sigma_used_for_state_residual"] = "sole full SVD of this fixed postcheck matrix"
            del left, right_t, sigma
            save_heat_and_static(name, arrays, record, "fixed-postfreeze")
            post_records[name] = record
            del arrays
            gc.collect()
            event("fixed_postcheck_saved", name=name, status=record["status"], counters=dict(counters))

        for form in FORMS:
            for n in (1023, 1279):
                post(form, n, 8., 64, f"post-{form}-N{n}")
        post(primary, 1279, 8., 128, "primary-time-N1279-B128")
        post(primary, 1599, 10., 64, "primary-box-N1599-L10")
        fits = {name: ({window: helper.metrics(member["prediction"][start:stop], truth[start:stop])
                        for window, (start, stop) in helper.WINDOWS.items()} if member["valid"] else None)
                for name, member in members.items()}
        comparisons = {}
        for form in FORMS:
            for label, left, right in (("train-grid", f"winner-{form}-N511", f"winner-{form}-N639"),
                                       ("N639-N1023", f"winner-{form}-N639", f"post-{form}-N1023"),
                                       ("N1023-N1279", f"post-{form}-N1023", f"post-{form}-N1279"),
                                       ("old-baseline-N1279", "old-S0047-N1535", f"post-{form}-N1279")):
                comparisons[f"{form}-{label}"] = helper.compare(left, right, members, truth)
        for name in list(members):
            if "static-"+name in members:
                comparisons["static-"+name] = helper.compare(name, "static-"+name, members, truth)
        for name in ("primary-time-N1279-B128", "primary-box-N1599-L10"):
            comparisons[name] = helper.compare(f"post-{primary}-N1279", name, members, truth)
        structure = {form: {"z": roles[form]["theta"][3], "z_nonzero": roles[form]["theta"][3] != 0.,
                            "joint_score": roles[form]["joint_score"], "J_minus_1": roles[form]["joint_score"]-1,
                            "J_below_1": roles[form]["joint_score"] < 1,
                            "B_joint_score": roles["B"]["joint_score"],
                            "J_strictly_better_than_B": roles[form]["joint_score"] < roles["B"]["joint_score"],
                            "selection_owner": "original run-1", "no_structure_gain_if_z_zero": True}
                     for form in ("O", "Q", "U", "D")}
        points = io.StringIO(newline="")
        writer = csv.writer(points)
        writer.writerow(["object_id", "kind", "stage", "form", "N", "L", "B", "resolution_valid", "index",
                         "window", "target", "predicted", "energy", "residual", "percent_error"])
        for name, member in members.items():
            meta = member_metadata[name]
            for index, (actual, predicted, energy) in enumerate(zip(truth, member["prediction"], member["energy"]), 1):
                window = "1-100" if index <= 100 else "101-300" if index <= 300 else "301-320"
                writer.writerow([name, meta["kind"], meta["stage"], meta["form"], meta["N"], meta["L"], meta["B"],
                                 member["valid"], index, window, actual, predicted, energy, predicted-actual, 100*abs(predicted-actual)/actual])
        output.binary("points.csv", points.getvalue().encode("utf-8"))
        output.json("development-fit-metrics.json", fits)
        output.json("comparisons.json", comparisons)
        output.json("minimum-ledger.json", minimum_ledger)
        final_verification = verify_inputs()
        if sha(OUT/"winners-frozen-original.json") != sha(OLD/"winners-frozen.json"):
            raise RuntimeError("Original winner identity copy differs at completion")
        if (counters["propagations_completed"] != 22 or counters["full_svd_completed"] != 22
                or counters["static_readouts_completed"] != 22):
            raise RuntimeError("Fixed completion count invariant failed")
        report = {"scope_id": SCOPE, "execution_id": EXECUTION, "status": "completed", "run_passport": "UNVERIFIED",
                  "global_joint_winner": primary, "roles": roles, "role_status": frozen["role_status"],
                  "original_training_calls": frozen["calls"], "original_unique_members": frozen["unique_members"],
                  "original_selection_unchanged": True, "new_optimization_calls": 0,
                  "reconstructions": reconstructions, "static_readouts": static_records, "postfreeze": post_records,
                  "fit_metrics": fits, "comparisons": comparisons, "structure_vs_B": structure,
                  "counters": dict(counters), "helper_internal_attempts": dict(helper_counters),
                  "old_run_completed_propagations": 323, "combined_completed_propagations": 323+counters["propagations_completed"],
                  "start_verification": initial_verification, "end_verification": final_verification,
                  "seconds_before_final_serialization": time.perf_counter()-started,
                  "maxrss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                  "completed_utc": utc(), "output_bytes_before_result": output.size(),
                  "not_an_independent_rerun_of_search": True, "new_targets_generated": False,
                  "formal_route": "UNASSIGNED; B NOT INVOKED"}
        output.json("result.json", report)
        monitor_stop.set()
        monitor.join(timeout=1)
        event("completed", fixed_primary=primary, seconds=report["seconds_before_final_serialization"],
              counters=dict(counters), output_bytes=output.size())
        inventory = {str(path.relative_to(OUT)): {"bytes": path.stat().st_size, "sha256": sha(path)}
                     for path in sorted(OUT.rglob("*")) if path.is_file()}
        output.json("file-inventory.json", {"scope_id": SCOPE, "execution_id": EXECUTION,
                                            "inventory_excludes_itself": True, "files": inventory})
    except Exception as exc:
        try:
            event("failed", type=type(exc).__name__, message=str(exc), counters=dict(counters),
                  helper_internal_attempts=dict(helper_counters), end_verification=final_verification)
        except Exception as log_exc:
            print(f"Failure evidence could not append: {type(log_exc).__name__}: {log_exc}", file=sys.stderr, flush=True)
        raise
    finally:
        monitor_stop.set()
        monitor.join(timeout=1)
        ledger_stream.close()
        event_stream.close()


if __name__ == "__main__":
    main()
