#!/usr/bin/env python3
"""CS15: fixed-parameter, complete two-parity Hermite cutoff audit.

Import and --preflight do no scientific work. Each parity block is fully
diagonalized once, retained states are copied, and the full vectors released.
The continuous action uses genuine (n+4)-by-n polynomial factors, not a
zero-padded finite matrix. All targets are historically observed.
"""
import csv
from datetime import datetime, timezone
import gc
import hashlib
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
from scipy.linalg import eigh


PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[1]
OUT = PACKAGE/"evidence/run-1"
LOCK_FILE = PACKAGE/"input-locks.json"
OLD = ROOT/"papers/264-henon-pullback-oscillator/evidence/run-1"
SCOPE = "ASFS-DISCOVERY-20260919-CS15"
EXPECTED_ID = "CS14-HENON-PULLBACK-OSCILLATOR-0028"
EXPECTED_THETA = (.02263390483074383, 11.825457423506625)
PRIMARY = "fine-n96"
WINDOWS = {"1-100": (0, 100), "101-300": (100, 300), "301-320": (300, 320), "1-320": (0, 320)}
FULL_M_REF, G_REF, TOL, GIB = 3.5251249515592384, 2., 1e-10, 1024**3
COMMAND = ("OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 "
           "PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 600s python -u "
           "papers/265-pullback-cutoff-audit/run_audit.py")


def utc():
    return datetime.now(timezone.utc).isoformat()


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_inputs():
    locks = json.loads(LOCK_FILE.read_text())
    for relative, expected in locks.items():
        if sha(ROOT/relative) != expected:
            raise RuntimeError("Frozen input hash mismatch: "+relative)
    return locks


def nullable(value):
    value = float(value)
    return value if math.isfinite(value) else None


def validate_checks(checks, label):
    """Pure scalar control validation at the earliest known failure boundary."""
    for check in checks.values():
        check["passed"] = check["error"] < check["tolerance"] if check.get("strict_less") else check["error"] <= check["tolerance"]
    failed = [name for name, check in checks.items() if not check["passed"]]
    if failed:
        raise RuntimeError("Hard control failed at "+label+": "+", ".join(failed))


def make_logger(stream, echo=False):
    lock = threading.Lock()

    def event(event_type, /, **fields):
        if "event" in fields or "utc" in fields:
            raise ValueError("Event metadata must not overwrite event/utc")
        with lock:
            line = json.dumps({"utc": utc(), "event": event_type, **fields}, allow_nan=False)
            stream.write(line+"\n")
            stream.flush()
            if echo:
                print(line, flush=True)
    return event


def logger_regression_test():
    stream = io.StringIO()
    event = make_logger(stream)
    cases = (("object_start", {"name": "fine-n96", "n": 96}),
             ("physical_eigh_start", {"name": "fine-n96-parity0", "kind": "parity"}),
             ("block_saved", {"name": "fine-n96-parity1", "counters": {"physical_eigh_completed": 2}}),
             ("continuous_action_start", {"name": "fine-n96", "extra_eigh": False}),
             ("failed_evidence_saved", {"name": "failed-fine-n96", "exception_type": "RuntimeError"}))
    for kind, fields in cases:
        event(kind, **fields)
    rows = [json.loads(line) for line in stream.getvalue().splitlines()]
    if len(rows) != len(cases) or any(row["event"] != kind or any(row[key] != value for key, value in fields.items())
                                      for row, (kind, fields) in zip(rows, cases)):
        raise AssertionError("Logger name/event regression")
    for reserved in ("event", "utc"):
        try:
            event("reserved_field", **{reserved: "forbidden"})
        except ValueError:
            pass
        else:
            raise AssertionError("Logger accepted reserved metadata")
    if len(stream.getvalue().splitlines()) != len(cases):
        raise AssertionError("Rejected metadata produced an event")
    return {"passed": True, "case_count": len(cases), "name_preserved": True,
            "reserved_event_utc_rejected": True, "scientific_numerics_performed": False}


def metadata_regression_test():
    checks = {"ten_objects": 4+1+3+2 == 10, "physical_eigh_budget": 4*3+6*2 == 24,
              "fullspace_and_parity_counts": 4+20 == 24,
              "fixed_primary": PRIMARY == "fine-n96", "two_fixed_parameters": len(EXPECTED_THETA) == 2,
              "largest_parity_dimension": 96*(96//2) == 4608,
              "small_controls_keep_full_space": 8*(8//2)*2 == 64}
    if not all(checks.values()):
        raise AssertionError("Frozen scalar metadata regression")
    return {"passed": True, "checks": checks, "scientific_numerics_performed": False}


class MonitorHealth:
    """Thread-to-main failure channel; checking is never used in failure logging."""
    def __init__(self):
        self.lock = threading.Lock()
        self.failure = None

    def record_failure(self, exc):
        with self.lock:
            if self.failure is None:
                self.failure = {"type": type(exc).__name__, "message": str(exc), "utc": utc()}

    def snapshot(self):
        with self.lock:
            return dict(self.failure) if self.failure is not None else None

    def check(self):
        failure = self.snapshot()
        if failure is not None:
            raise RuntimeError("Resource monitor failed: "+failure["type"]+": "+failure["message"])

    def require_stopped(self, thread):
        if thread.is_alive():
            self.record_failure(RuntimeError("Resource monitor remained alive after bounded join"))
        self.check()


def monitor_regression_test():
    class BrokenStream(io.StringIO):
        def write(self, text):
            raise OSError("simulated monitor log write failure")

    health = MonitorHealth()
    health.check()
    try:
        make_logger(BrokenStream())("resource_sample", name="pure-monitor-test")
    except Exception as exc:
        health.record_failure(exc)
    try:
        health.check()
    except RuntimeError as exc:
        if "simulated monitor log write failure" not in str(exc):
            raise AssertionError("Monitor cause was lost")
    else:
        raise AssertionError("Monitor failure did not propagate")
    still_alive = type("FakeThread", (), {"is_alive": lambda self: True})()
    unclosed = MonitorHealth()
    try:
        unclosed.require_stopped(still_alive)
    except RuntimeError:
        pass
    else:
        raise AssertionError("Unclosed monitor accepted")
    return {"passed": True, "simulated_logger_failure_propagated": True, "unclosed_monitor_rejected": True,
            "scientific_numerics_performed": False}


class BoundedOutput:
    def __init__(self, directory, byte_limit):
        self.directory, self.byte_limit = directory, byte_limit
        self.lock = threading.Lock()

    def size(self):
        return sum(path.stat().st_size for path in self.directory.rglob("*") if path.is_file())

    def guard(self, extra):
        if self.size()+extra > self.byte_limit:
            raise RuntimeError("New-run 1 GiB output budget would be exceeded; no retry")

    def binary(self, name, payload):
        with self.lock:
            self.guard(len(payload))
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
        with self.lock:
            self.guard(0)
            handle = (self.directory/name).open("xb")

        class Stream:
            def write(self, text):
                payload = text.encode("utf-8")
                with owner.lock:
                    owner.guard(len(payload))
                    handle.write(payload)
                    handle.flush()
                return len(text)

            def flush(self):
                handle.flush()

            def close(self):
                handle.close()
        return Stream()


def hermite_matrices(dimension, width):
    lower = np.diag(np.sqrt(np.arange(1, dimension)), k=1)
    raising = lower.T
    return math.sqrt(width/2)*(lower+raising), (lower-raising)/math.sqrt(2*width)


def gram_factors(h, kappa, n, rho):
    width = rho*h
    x, derivative = hermite_matrices(n+2, width)
    q = x+.5*np.eye(n+2)
    xr, dr, qr = x[:, :n], derivative[:, :n], q[:, :n]
    q_squared = (q@q)[:, :n]
    return {"H0": h*h*(dr.T@dr)+xr.T@xr, "Q2": qr.T@qr, "Y2": xr.T@xr,
            "Q4": q_squared.T@q_squared, "X_rect": xr.copy(), "D_rect": dr.copy(),
            "Q_rect": qr.copy(), "Q_squared_rect": q_squared.copy(),
            "n": np.array(n), "h": np.array(h), "kappa": np.array(kappa), "rho": np.array(rho),
            "theta": np.array([h, kappa]), "hermite_width_b": np.array(width)}


def continuous_factors(h, n, rho):
    """Exact action output degrees 0..n+3, input degrees 0..n-1.

    The polynomial powers are formed on n+4 before selecting input columns;
    four coordinate steps cannot leave this space starting below n.
    """
    dimension = n+4
    x, derivative = hermite_matrices(dimension, rho*h)
    q = x+.5*np.eye(dimension)
    x2, q2 = x@x, q@q
    q4 = q@q@q@q
    return {"E_action": np.eye(dimension)[:, :n],
            "H0_action": (-h*h*(derivative@derivative)+x2)[:, :n],
            "Q2_action": q2[:, :n], "Y2_action": x2[:, :n], "Q4_action": q4[:, :n],
            "action_output_axis_dimension": np.array(dimension)}


def full_matrix(factors, kappa):
    n = len(factors["H0"])
    identity = np.eye(n)
    return (np.kron(factors["H0"], identity)+np.kron(identity, factors["H0"])
            +kappa*(np.kron(factors["Q4"], identity)+4*np.kron(factors["Q2"], factors["Y2"])))


def parity_matrix(factors, kappa, parity):
    n = len(factors["H0"])
    y = np.arange(parity, n, 2)
    h0_y, y2 = factors["H0"][np.ix_(y, y)], factors["Y2"][np.ix_(y, y)]
    # Restrict H0 and Y2 AFTER the coordinate chains, never square a parity Y.
    matrix = (np.kron(factors["H0"], np.eye(len(y)))+np.kron(np.eye(n), h0_y)
              +kappa*(np.kron(factors["Q4"], np.eye(len(y)))+4*np.kron(factors["Q2"], y2)))
    indices = (np.arange(n)[:, None]*n+y[None, :]).ravel()
    return matrix, y, indices


def tensor_action(factors, states, n, kappa):
    """Apply P_(n+4) S P_n without an extended 2D dense matrix."""
    count, dimension = states.shape[1], n+4
    coefficient = states.reshape(n, n, count)
    result = np.zeros((dimension, dimension, count))
    q_action = factors["H0_action"]+kappa*factors["Q4_action"]
    result[:, :n] += np.einsum("ai,ijk->ajk", q_action, coefficient, optimize=True)
    result[:n, :] += np.einsum("bj,ijk->ibk", factors["H0_action"], coefficient, optimize=True)
    intermediate = np.einsum("ai,ijk->ajk", factors["Q2_action"], coefficient, optimize=True)
    result += 4*kappa*np.einsum("bj,ajk->abk", factors["Y2_action"], intermediate, optimize=True)
    return result


def oscillator_spectrum(h, n):
    return np.sort(np.array([2*h*(i+j+1) for i in range(n) for j in range(n)]))


def spectrum_guard(eigenvalues):
    if not np.all(np.isfinite(eigenvalues)) or eigenvalues[0] <= 0 or not np.all(np.diff(eigenvalues) >= 0):
        raise RuntimeError("Raw spectrum must be positive, finite and nondecreasing; no clipping or retry")


def finite_diagnostics(matrix, eigenvalues, states):
    spectrum_guard(eigenvalues)
    count = states.shape[1]
    action = matrix@states
    difference = action-states*eigenvalues[:count]
    residual = np.linalg.norm(difference, axis=0)
    orth_error = states.T@states-np.eye(count)
    trace, moment = float(np.trace(matrix)), float(np.sum(matrix*matrix))
    spectral_trace, spectral_moment = float(np.sum(eigenvalues)), float(np.sum(eigenvalues*eigenvalues))
    matrix_scale = max(1., float(np.max(np.abs(matrix))))
    residual_scale = max(1., float(np.max(np.abs(action))), float(np.max(np.abs(states*eigenvalues[:count]))))
    checks = {
        "symmetry": {"error": float(np.max(np.abs(matrix-matrix.T))), "tolerance": TOL*matrix_scale},
        "retained_state_matrix_equation": {"error": float(np.max(np.abs(difference))), "tolerance": TOL*residual_scale},
        "retained_state_orthogonality": {"error": float(np.max(np.abs(orth_error))), "tolerance": TOL},
        "full_trace": {"error": abs(trace-spectral_trace), "tolerance": TOL*max(1., abs(trace))},
        "full_squared_trace": {"error": abs(moment-spectral_moment), "tolerance": TOL*max(1., abs(moment))},
    }
    for check in checks.values():
        check["passed"] = check["error"] <= check["tolerance"]
    record = {"spectrum_positive_finite_nondecreasing": True, "lambda_min": float(eigenvalues[0]),
              "lambda_max": float(eigenvalues[-1]), "trace_J": trace, "full_lambda_sum": spectral_trace,
              "frobenius_squared_J": moment, "full_lambda_squared_sum": spectral_moment,
              "retained_state_residual_norm_max": float(np.max(residual)), "retained_state_orthogonality_fro": float(np.linalg.norm(orth_error)),
              "retained_states": count, "checks": checks, "passed": all(check["passed"] for check in checks.values())}
    return residual, record


def metrics(prediction, target):
    relative = np.abs(prediction-target)/target
    return {"count": len(target), "mape_percent": float(100*np.mean(relative)),
            "max_percent_error": float(100*np.max(relative)), "rmse": float(np.sqrt(np.mean((prediction-target)**2))),
            "max_absolute_error": float(np.max(np.abs(prediction-target)))}


def residual_summary(values):
    result = {}
    for count in (100, 320):
        if len(values) >= count:
            result[str(count)] = {"mean": float(np.mean(values[:count])), "max": float(np.max(values[:count]))}
    if len(values) < 100:
        result["all_control_states"] = {"count": len(values), "mean": float(np.mean(values)), "max": float(np.max(values))}
    return result


def continuous_residuals(factors, states, eigenvalues, n, kappa, projected_residual):
    action = tensor_action(factors, states, n, kappa)
    count = states.shape[1]
    norms = np.linalg.norm(states, axis=0)
    residual = action.copy()
    residual[:n, :n] -= states.reshape(n, n, count)*eigenvalues[:count]
    total_squared = np.sum(residual*residual, axis=(0, 1))/norms**2
    inside_squared = np.sum(residual[:n, :n]**2, axis=(0, 1))/norms**2
    outside_squared = (np.sum(residual[n:, :]**2, axis=(0, 1))+np.sum(residual[:n, n:]**2, axis=(0, 1)))/norms**2
    total, inside, outside = np.sqrt(total_squared), np.sqrt(inside_squared), np.sqrt(outside_squared)
    relative = total/eigenvalues[:count]
    high = math.ceil(n/5)
    axis = np.arange(n)
    edge_mask = (axis[:, None] >= n-high) | (axis[None, :] >= n-high)
    edge = np.sum(states.reshape(n, n, count)[edge_mask]**2, axis=0)/norms**2
    orthogonality = float(np.max(np.abs(states.T@states-np.eye(count))))
    identity_error = float(np.max(np.abs(total_squared-inside_squared-outside_squared)))
    identity_tolerance = TOL*max(1., float(np.max(total_squared)))
    projection_error = float(np.max(np.abs(inside-projected_residual/norms)))
    projection_tolerance = TOL*max(1., float(np.max(np.abs(eigenvalues[:count]))))
    diagnostics = {"observed_extended_basis_residual": True, "rounding_error_not_enclosed": True,
                   "not_an_index_or_normalized_320_certificate": True, "not_a_K_vector_residual": True,
                   "continuous_residual_not_a_fit_or_rejection_gate": True,
                   "residual": residual_summary(total), "relative_residual": residual_summary(relative),
                   "inside_residual": residual_summary(inside), "outside_leak": residual_summary(outside),
                   "edge_occupation": residual_summary(edge), "edge_top_modes_each_axis": high,
                   "global_orthogonality_max_difference": orthogonality,
                   "pythagorean_max_difference": identity_error, "pythagorean_tolerance": identity_tolerance,
                   "inside_vs_block_residual_max_difference": projection_error, "inside_vs_block_tolerance": projection_tolerance,
                   "algebra_checks_passed": orthogonality <= TOL and identity_error <= identity_tolerance and projection_error <= projection_tolerance}
    arrays = {"states": states, "state_norm": norms, "continuous_residual_tensor": residual,
              "continuous_residual": total, "continuous_relative_residual": relative,
              "inside_residual": inside, "outside_leak": outside, "projected_block_residual": projected_residual,
              "continuous_residual_squared": total_squared, "inside_residual_squared": inside_squared, "outside_leak_squared": outside_squared,
              "truncation_edge_mask": edge_mask, "truncation_edge_occupation": edge}
    return arrays, diagnostics, action


def readout(eigenvalues, truth):
    spectrum_guard(eigenvalues)
    with np.errstate(over="ignore", invalid="ignore"):
        energy = eigenvalues**1.5
        predicted = truth[0]*(eigenvalues[:320]/eigenvalues[0])**1.5
        raw = truth[0]*eigenvalues[:320]/eigenvalues[0]
    mask = np.isfinite(energy)
    if not np.all(mask) or not np.all(energy > 0) or not np.all(np.isfinite(predicted)) or not np.all(np.isfinite(raw)):
        raise RuntimeError("Nonfinite powered spectrum or prediction; no clipping")
    return {"energy_power_3_2": energy, "finite_mask": mask, "raw_J_finite_mask": np.isfinite(eigenvalues),
            "predicted_320": predicted, "raw_J_predicted_320": raw, "scale": np.array(truth[0]/energy[0]),
            "raw_J_scale": np.array(truth[0]/eigenvalues[0])}


def compare(left_name, right_name, members, truth, raw=False):
    left, right = members[left_name], members[right_name]
    prediction, energy = ("raw_J_predicted_320", "lambda_raw") if raw else ("predicted_320", "energy_power_3_2")
    windows = {}
    for window, (start, end) in WINDOWS.items():
        gap = float(100*np.max(np.abs(left[prediction][start:end]-right[prediction][start:end])/truth[start:end]))
        raw_gap = float(100*np.max(np.abs(left[energy][start:end]-right[energy][start:end])/left[energy][start:end]))
        windows[window] = {"G_percent": gap, "G_below_threshold": gap < G_REF,
                           "unscaled_energy_max_relative_percent": raw_gap,
                           "raw_lambda_max_absolute_difference": float(np.max(np.abs(left["lambda_raw"][start:end]-right["lambda_raw"][start:end])))}
    return {"left": left_name, "right": right_name, "readout": "raw_J" if raw else "power_3_2",
            "G_threshold_percent": G_REF, "unscaled_energy_denominator": "left object", "windows": windows}


def main():
    started = time.perf_counter()
    logger_test, metadata_test = logger_regression_test(), metadata_regression_test()
    monitor_test = monitor_regression_test()
    locks, own_hash = verify_inputs(), sha(Path(__file__))
    if OUT.exists():
        raise RuntimeError("Output directory exists; refusing overwrite or retry")
    OUT.mkdir(parents=True)
    output = BoundedOutput(OUT, GIB)
    event_stream = output.text_stream("events.jsonl")
    event = make_logger(event_stream, echo=True)
    stop = threading.Event()
    monitor_health = MonitorHealth()
    counters = {"objects_attempted": 0, "objects_completed": 0, "objects_saved": 0,
                "physical_eigh_attempted": 0, "physical_eigh_completed": 0,
                "fullspace_eigh_attempted": 0, "fullspace_eigh_completed": 0,
                "parity_eigh_attempted": 0, "parity_eigh_completed": 0,
                "fullspace_arrays_saved": 0, "parity_arrays_saved": 0, "factor_arrays_saved": 0,
                "small_padded_reference_assemblies_attempted": 0, "small_padded_reference_assemblies_completed": 0,
                "continuous_actions_attempted": 0, "continuous_actions_completed": 0,
                "svd_calls": 0, "root_calls": 0, "quadrature_calls": 0, "optimization_calls": 0,
                "extra_state_eigh_calls": 0, "new_target_generations": 0}
    end_verification = None

    def resources():
        try:
            while not stop.wait(30):
                rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
                event("resource_sample", pid=os.getpid(), seconds=time.perf_counter()-started, maxrss_kib=rss,
                      memory_above_2gib_advisory=bool(rss*1024 > 2*GIB), output_bytes=output.size(), counters=dict(counters))
        except Exception as exc:
            monitor_health.record_failure(exc)

    monitor = threading.Thread(target=resources, daemon=True)
    monitor.start()
    try:
        old_identity_bytes = (OLD/"winners-frozen.json").read_bytes()
        old_identity = json.loads(old_identity_bytes)
        winner = old_identity["winner"]
        theta = tuple(float(value) for value in winner["theta"])
        if winner["evaluation_id"] != EXPECTED_ID or theta != EXPECTED_THETA or winner["joint_score"] != 1.8560562377080405:
            raise RuntimeError("Fixed CS14 winner identity/parameters/failed joint score mismatch")
        output.binary("source-winners-frozen.json", old_identity_bytes)
        identity = {"scope_id": SCOPE, "frozen_utc": utc(), "source_evaluation_id": EXPECTED_ID, "theta": theta,
                    "source_identity_sha256": sha(OLD/"winners-frozen.json"), "source_identity_copy": "source-winners-frozen.json",
                    "primary": PRIMARY, "primary_n": 96, "primary_rho": 1., "no_search_or_reselection": True,
                    "source_CS14_joint_score": winner["joint_score"], "source_CS14_joint_gate_passed": False,
                    "source_CS14_training_worst_percent": winner["max_percent_error"],
                    "source_CS14_training_by_grid": {key: value["training_metrics"] for key, value in winner["grids"].items()},
                    "inputs": locks, "script_sha256": own_hash, "science_started": False, "target_scoring_started": False}
        output.json("fixed-identity.json", identity)
        identity_hash = sha(OUT/"fixed-identity.json")
        output.json("manifest.json", {"scope_id": SCOPE, "started_utc": utc(), "pid": os.getpid(), "command": COMMAND,
                    "script_sha256": own_hash, "input_locks_sha256": sha(LOCK_FILE), "inputs": locks,
                    "fixed_identity_sha256": identity_hash, "python": sys.version, "numpy": np.__version__, "scipy": scipy.__version__,
                    "thread_environment": {key: os.environ.get(key) for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")},
                    "max_objects": 10, "max_physical_eigh": 24, "max_fullspace_eigh": 4, "max_parity_eigh": 20,
                    "solver": "scipy.linalg.eigh driver=evd, full real spectrum and all vectors once per block",
                    "parity_order": [0, 1], "merge_order": ["lambda", "parity", "local_index"], "all_sectors_and_multiplicities_retained": True,
                    "finite_matrix_owner": "complete Cartesian Hermite compression, not selected symmetry block",
                    "continuous_action_owner": "P_(n+4) S P_n via genuinely extended 1D polynomial factors",
                    "primary_readout": "gamma1*(lambda/lambda1)^1.5", "raw_J_readout": "fixed same-spectrum diagnostic",
                    "finite_power_owner": "(S_n)^1.5, not compression of S^1.5", "kappa_zero_owner": "original closed oscillator form",
                    "continuous_residual_not_an_accuracy_certificate": True, "continuous_residual_not_a_selection_gate": True,
                    "old_scientific_modules_imported": False, "new_targets_generated": False, "all_targets_previously_observed": True,
                    "output_hard_limit_bytes": GIB, "memory_advisory_bytes": 2*GIB, "timeout_seconds": 600,
                    "logger_regression": logger_test, "metadata_regression": metadata_test, "monitor_regression": monitor_test,
                    "monitor_failure_policy": "propagate at scientific boundaries; no asynchronous eigensolver kill; bounded join must close",
                    "actual_exit_code": "recorded by launching parent", "run_passport": "UNVERIFIED"})
        output.json("launch-receipt.json", {"scope_id": SCOPE, "started_utc": utc(), "pid": os.getpid(),
                    "script_sha256": own_hash, "input_locks_sha256": sha(LOCK_FILE), "fixed_identity_sha256": identity_hash,
                    "output_was_absent_before_exclusive_creation": True, "command": COMMAND})
        output.json("pure-interface-tests.json", {"logger": logger_test, "metadata": metadata_test, "monitor": monitor_test})
        event("fixed_identity_frozen", sha256=identity_hash, source_identity_copy_sha256=sha(OUT/"source-winners-frozen.json"),
              source_evaluation_id=EXPECTED_ID, primary=PRIMARY, counters=dict(counters))
        event("known_reference_read_start", all_previously_observed=True, no_selection=True)
        target_bytes = (OLD/"known-targets.json").read_bytes()
        truth = np.array([float(value) for value in json.loads(target_bytes)["ordinates"]])
        if len(truth) != 320 or not np.all(np.isfinite(truth)) or truth[0] <= 0 or not np.all(np.diff(truth) > 0):
            raise RuntimeError("Invalid historical 320-point reference")
        output.binary("known-targets.json", target_bytes)
        external_bytes = (OLD/"external-history-comparator.json").read_bytes()
        external = json.loads(external_bytes)
        if abs(external["fit_metrics"]["1-320"]["mape_percent"]-FULL_M_REF) > 1e-10:
            raise RuntimeError("Historical external comparison threshold mismatch")
        output.binary("external-history-comparator.json", external_bytes)
        output.json("historical-CS14-failure.json", {"source_identity_sha256": sha(OLD/"winners-frozen.json"),
                    "joint_score": winner["joint_score"], "joint_gate_passed": False,
                    "training_metrics_by_grid": identity["source_CS14_training_by_grid"],
                    "old_record_not_revised_by_this_audit": True})

        def preserve_failure(name, arrays, exc, metadata):
            try:
                output.npz("failed-"+name+".npz", arrays)
                output.json("failed-"+name+".json", {"scope_id": SCOPE, "name": name, "exception_type": type(exc).__name__,
                            "exception_message": str(exc), "metadata": metadata, "counters": dict(counters),
                            "saved_existing_evidence_only": True, "no_retry_or_extra_scientific_call": True})
                event("failed_evidence_saved", name="failed-"+name, exception_type=type(exc).__name__, counters=dict(counters))
            except Exception as save_exc:
                print(f"Could not preserve failed evidence: {type(save_exc).__name__}: {save_exc}", file=sys.stderr, flush=True)

        def decompose(matrix, name, kind, metadata):
            monitor_health.check()
            if counters["physical_eigh_attempted"] >= 24 or counters[kind+"_eigh_attempted"] >= (4 if kind == "fullspace" else 20):
                raise RuntimeError("Frozen eigendecomposition budget exceeded")
            counters["physical_eigh_attempted"] += 1
            counters[kind+"_eigh_attempted"] += 1
            event("physical_eigh_start", name=name, kind=kind, dimension=len(matrix), counters=dict(counters))
            tick = time.perf_counter()
            arrays = {"matrix_S": matrix}
            try:
                eigenvalues, vectors = eigh(matrix, eigvals_only=False, driver="evd", overwrite_a=False)
                counters["physical_eigh_completed"] += 1
                counters[kind+"_eigh_completed"] += 1
                retained = vectors[:, :min(320, len(matrix))].copy()
                del vectors
                arrays.update(lambda_raw=eigenvalues, states=retained)
                monitor_health.check()
                residual, diagnostics = finite_diagnostics(matrix, eigenvalues, retained)
                arrays["eigenvector_residual"] = residual
                monitor_health.check()
                record = {"name": name, "kind": kind, "dimension": len(matrix), **metadata, **diagnostics,
                          "seconds": time.perf_counter()-tick, "same_call_states": True, "extra_state_eigh_calls": 0}
                if not diagnostics["passed"]:
                    raise RuntimeError("Finite matrix spectral control failed: "+name)
                event("physical_eigh_complete", name=name, kind=kind, seconds=record["seconds"], counters=dict(counters))
                return arrays, record
            except Exception as exc:
                preserve_failure(name, arrays, exc, metadata)
                raise

        all_records, control_records, members, metadata, object_hashes = {}, {}, {}, {}, {}
        specifications = (("control-sourceoff", 8, .16, 0., 1., True),
                          ("control-winner-rho1", 8, theta[0], theta[1], 1., True),
                          ("control-winner-rho080", 8, theta[0], theta[1], .8, True),
                          ("control-winner-rho125", 8, theta[0], theta[1], 1.25, True),
                          ("bridge-n52", 52, theta[0], theta[1], 1., False),
                          ("fine-n64", 64, theta[0], theta[1], 1., False),
                          ("fine-n80", 80, theta[0], theta[1], 1., False),
                          ("fine-n96", 96, theta[0], theta[1], 1., False),
                          ("width080-n96", 96, theta[0], theta[1], .8, False),
                          ("width125-n96", 96, theta[0], theta[1], 1.25, False))
        output.json("object-plan.json", {"primary": PRIMARY, "objects": [{"name": name, "n": n, "h": h, "kappa": kappa,
                    "rho": rho, "small_control": small} for name, n, h, kappa, rho, small in specifications]})
        for name, n, h, kappa, rho, small in specifications:
            monitor_health.check()
            counters["objects_attempted"] += 1
            event("object_start", name=name, n=n, h=h, kappa=kappa, rho=rho, small_control=small)
            tick = time.perf_counter()
            factors = gram_factors(h, kappa, n, rho)
            monitor_health.check()
            factors.update(continuous_factors(h, n, rho))
            monitor_health.check()
            output.npz(name+"-factors.npz", factors)
            counters["factor_arrays_saved"] += 1
            basic = {"object_name": name, "n": n, "h": h, "kappa": kappa, "theta": [h, kappa], "rho": rho}
            file_names = [name+"-factors.npz"]
            full_arrays, full_record, old_matrix = None, None, None
            checks = {}
            # H0/Y2 are formed first; the exact parity split includes q in full.
            even, odd = np.arange(0, n, 2), np.arange(1, n, 2)
            cross_h0 = float(np.max(np.abs(factors["H0"][np.ix_(even, odd)])))
            cross_y2 = float(np.max(np.abs(factors["Y2"][np.ix_(even, odd)])))
            checks["one_dimensional_parity_cross_zero"] = {"error": max(cross_h0, cross_y2),
                "tolerance": TOL*max(1., float(np.max(np.abs(factors["H0"]))), float(np.max(np.abs(factors["Y2"]))))}
            try:
                validate_checks(checks, name+"-parity-factors")
            except Exception as exc:
                preserve_failure(name+"-parity-factors", factors, exc, {**basic, "checks": checks})
                raise
            if small:
                full_arrays, full_record = decompose(full_matrix(factors, kappa), name+"-full", "fullspace", basic)
                output.npz(name+"-full.npz", full_arrays)
                output.json(name+"-full.json", full_record)
                counters["fullspace_arrays_saved"] += 1
                file_names.extend((name+"-full.npz", name+"-full.json"))
            if name == "bridge-n52":
                with np.load(OLD/"post-n52.npz", allow_pickle=False) as old:
                    if tuple(old["theta"].tolist()) != theta or int(old["n"]) != 52 or float(old["rho"]) != 1.:
                        raise RuntimeError("Old n52 bridge owner mismatch")
                    old_matrix = old["matrix_S"].copy()
                    old_lambda = old["lambda_raw"].copy()
                    old_prediction = old["predicted_320"].copy()
                    if not np.array_equal(old["target_100"], truth[:100]):
                        raise RuntimeError("Old bridge target mismatch")
            reference_matrix = full_arrays["matrix_S"] if small else old_matrix
            if reference_matrix is not None:
                even_indices = (np.arange(n)[:, None]*n+even[None, :]).ravel()
                odd_indices = (np.arange(n)[:, None]*n+odd[None, :]).ravel()
                reference_scale = max(1., float(np.max(np.abs(reference_matrix))))
                checks["reference_cross_block_zero"] = {"error": float(np.max(np.abs(reference_matrix[np.ix_(even_indices, odd_indices)]))),
                                                         "tolerance": TOL*reference_scale}
                try:
                    validate_checks(checks, name+"-reference-cross-block")
                except Exception as exc:
                    preserve_failure(name+"-reference-cross-block", {"matrix_S": reference_matrix}, exc, {**basic, "checks": checks})
                    raise
            block_arrays, block_records = [], []
            block_matrix_difference = 0.
            reference_matrix_scale = 1.
            for parity in (0, 1):
                monitor_health.check()
                block, y_degrees, indices = parity_matrix(factors, kappa, parity)
                if reference_matrix is not None:
                    reference_block = reference_matrix[np.ix_(indices, indices)]
                    block_matrix_difference = max(block_matrix_difference, float(np.max(np.abs(block-reference_block))))
                    reference_matrix_scale = max(reference_matrix_scale, float(np.max(np.abs(reference_matrix))))
                    checks[f"parity{parity}_reference_matrix"] = {"error": float(np.max(np.abs(block-reference_block))),
                                                                 "tolerance": TOL*reference_matrix_scale}
                    try:
                        validate_checks(checks, f"{name}-parity{parity}-reference")
                    except Exception as exc:
                        preserve_failure(f"{name}-parity{parity}-reference", {"matrix_S": block, "reference_block": reference_block},
                                         exc, {**basic, "checks": checks})
                        raise
                part_name = f"{name}-parity{parity}"
                part, part_record = decompose(block, part_name, "parity", {**basic, "parity": parity})
                part.update(y_degrees=y_degrees, global_basis_indices=indices, parity=np.array(parity), n=np.array(n),
                            h=np.array(h), kappa=np.array(kappa), rho=np.array(rho), theta=np.array([h, kappa]))
                output.npz(part_name+".npz", part)
                output.json(part_name+".json", part_record)
                counters["parity_arrays_saved"] += 1
                file_names.extend((part_name+".npz", part_name+".json"))
                event("block_saved", name=part_name, counters=dict(counters))
                del part["matrix_S"]
                del block
                if reference_matrix is not None:
                    del reference_block
                block_arrays.append(part)
                block_records.append(part_record)
                gc.collect()
            if reference_matrix is not None:
                i_even, i_odd = block_arrays[0]["global_basis_indices"], block_arrays[1]["global_basis_indices"]
                cross = float(np.max(np.abs(reference_matrix[np.ix_(i_even, i_odd)])))
                checks["block_reconstruction"] = {"error": max(block_matrix_difference, cross), "block_max_difference": block_matrix_difference,
                                                  "cross_block_max_absolute_value": cross, "tolerance": TOL*reference_matrix_scale}
            if old_matrix is not None:
                del reference_matrix, old_matrix
                old_matrix = None
            eigenvalues = np.concatenate([part["lambda_raw"] for part in block_arrays])
            parity_tags = np.concatenate([np.full(len(part["lambda_raw"]), parity, dtype=int) for parity, part in enumerate(block_arrays)])
            local_indices = np.concatenate([np.arange(len(part["lambda_raw"])) for part in block_arrays])
            order = np.lexsort((local_indices, parity_tags, eigenvalues))
            eigenvalues, parity_tags, local_indices = eigenvalues[order], parity_tags[order], local_indices[order]
            count = min(320, n*n)
            states, projected_residual = np.zeros((n*n, count)), np.empty(count)
            for index in range(count):
                parity, local = int(parity_tags[index]), int(local_indices[index])
                part = block_arrays[parity]
                if local >= part["states"].shape[1]:
                    raise RuntimeError("Merged low state unavailable in same-call retained parity prefix")
                states[part["global_basis_indices"], index] = part["states"][:, local]
                projected_residual[index] = part["eigenvector_residual"][local]
            arrays = {"n": np.array(n), "dimension": np.array(n*n), "theta": np.array([h, kappa]), "h": np.array(h),
                      "kappa": np.array(kappa), "rho": np.array(rho), "lambda_raw": eigenvalues,
                      "global_parity": parity_tags, "global_local_index": local_indices, "global_concat_index": order,
                      "states": states, "projected_block_residual": projected_residual,
                      "block0_lambda_raw": block_arrays[0]["lambda_raw"], "block1_lambda_raw": block_arrays[1]["lambda_raw"]}
            try:
                arrays.update(readout(eigenvalues, truth))
                if small:
                    error = float(np.max(np.abs(eigenvalues-full_arrays["lambda_raw"])))
                    checks["full_vs_merged_spectrum"] = {"error": error, "tolerance": TOL*max(1., float(np.max(np.abs(full_arrays["lambda_raw"]))))}
                if kappa == 0:
                    expected = oscillator_spectrum(h, n)
                    arrays["expected_lambda"] = expected
                    checks["sourceoff_analytic_full_spectrum"] = {"error": float(np.max(np.abs(eigenvalues-expected))),
                        "tolerance": TOL*max(1., float(np.max(np.abs(expected))))}
                if name == "bridge-n52":
                    checks["old_n52_full_spectrum"] = {"error": float(np.max(np.abs(eigenvalues-old_lambda))),
                                                       "tolerance": TOL*max(1., float(np.max(np.abs(old_lambda))))}
                    bridge_gap = float(100*np.max(np.abs(arrays["predicted_320"]-old_prediction)/truth))
                    checks["old_n52_prediction"] = {"error": bridge_gap, "tolerance": 1e-7, "strict_less": True, "units": "percent"}
                previous_name = {"fine-n64": "bridge-n52", "fine-n80": "fine-n64", "fine-n96": "fine-n80"}.get(name)
                if previous_name is not None:
                    previous_values = members[previous_name]["lambda_raw"]
                    checks["same_width_nested_raw_Ritz"] = {
                        "error": float(np.max(eigenvalues[:len(previous_values)]-previous_values)),
                        "tolerance": TOL*max(1., float(np.max(np.abs(previous_values))), float(np.max(np.abs(eigenvalues)))),
                        "previous_object": previous_name, "compared_count": len(previous_values)}
                validate_checks(checks, name+"-merged-spectrum")
                monitor_health.check()
                counters["continuous_actions_attempted"] += 1
                event("continuous_action_start", name=name, extra_eigh=False)
                residual_arrays, diagnostics, action = continuous_residuals(factors, states, eigenvalues, n, kappa, projected_residual)
                counters["continuous_actions_completed"] += 1
                arrays.update(residual_arrays)
                monitor_health.check()
                if not diagnostics["algebra_checks_passed"]:
                    raise RuntimeError("Continuous-action algebra identity failed; residual magnitude is not a gate")
                if small:
                    monitor_health.check()
                    counters["small_padded_reference_assemblies_attempted"] += 1
                    padded_factors = gram_factors(h, kappa, n+4, rho)
                    padded = full_matrix(padded_factors, kappa)
                    counters["small_padded_reference_assemblies_completed"] += 1
                    monitor_health.check()
                    embedding = np.zeros(((n+4)**2, count))
                    embedding_indices = (np.arange(n)[:, None]*(n+4)+np.arange(n)[None, :]).ravel()
                    embedding[embedding_indices] = states
                    reference_action = padded@embedding
                    action_difference = float(np.max(np.abs(action.reshape((n+4)**2, count)-reference_action)))
                    action_tolerance = TOL*max(1., float(np.max(np.abs(reference_action))))
                    checks["true_tensor_action_vs_independent_padded_Gram"] = {"error": action_difference, "tolerance": action_tolerance}
                    if kappa == 0:
                        checks["sourceoff_zero_leak"] = {"error": float(np.max(arrays["outside_leak"])), "tolerance": action_tolerance}
                    output.npz(name+"-padded-reference.npz", {"matrix_S": padded, "embedded_states": embedding,
                                "embedding_indices": embedding_indices, "reference_action": reference_action,
                                "tensor_action": action.reshape((n+4)**2, count), "n": np.array(n), "padded_n": np.array(n+4)})
                    file_names.append(name+"-padded-reference.npz")
                    del padded, padded_factors, embedding, reference_action
                del action
                validate_checks(checks, name+"-tensor-action")
                record = {"name": name, **basic, "dimension": n*n, "small_control": small, "primary": name == PRIMARY,
                          "block_records": block_records, "checks": checks, "continuous_diagnostics": diagnostics,
                          "lambda_min": float(eigenvalues[0]), "lambda_max": float(eigenvalues[-1]),
                          "global_merged_count": len(eigenvalues), "retained_global_states": count,
                          "merge_order": ["lambda", "parity", "local_index"], "all_multiplicities_retained": True,
                          "full_lambda_sum": float(np.sum(eigenvalues)), "block_trace_sum": sum(row["trace_J"] for row in block_records),
                          "full_lambda_squared_sum": float(np.sum(eigenvalues*eigenvalues)),
                          "block_frobenius_squared_sum": sum(row["frobenius_squared_J"] for row in block_records),
                          "passed": all(check["passed"] for check in checks.values()) and diagnostics["algebra_checks_passed"],
                          "seconds": time.perf_counter()-tick, "same_call_states_no_extra_eigh": True,
                          "continuous_residual_not_a_fit_gate": True}
                arrays["target_320"] = truth.copy()
                output.npz(name+".npz", arrays)
                output.json(name+".json", record)
                file_names.extend((name+".npz", name+".json"))
                counters["objects_saved"] += 1
                all_records[name] = record
                if small:
                    control_records[name] = record
                else:
                    members[name] = {key: arrays[key].copy() for key in ("lambda_raw", "energy_power_3_2", "predicted_320", "raw_J_predicted_320")}
                    metadata[name] = {"n": n, "h": h, "kappa": kappa, "rho": rho}
                object_hashes[name] = {file: sha(OUT/file) for file in file_names}
                if not record["passed"]:
                    raise RuntimeError("Fixed object algebra/control failure: "+name)
                counters["objects_completed"] += 1
                event("object_completed", name=name, seconds=record["seconds"], counters=dict(counters))
            except Exception as exc:
                preserve_failure(name, arrays, exc, {**basic, "checks": checks})
                raise
            del arrays, residual_arrays, states, block_arrays, factors
            if full_arrays is not None:
                del full_arrays
            gc.collect()
        output.json("object-files-frozen.json", {"scope_id": SCOPE, "fixed_identity_sha256": identity_hash, "files_by_object": object_hashes,
                                                 "no_selection_or_reselection": True, "counters": dict(counters)})
        fits = {name: {readout_name: {window: metrics(member[key][start:end], truth[start:end]) for window, (start, end) in WINDOWS.items()}
                       for readout_name, key in (("power_3_2", "predicted_320"), ("raw_J", "raw_J_predicted_320"))}
                for name, member in members.items()}
        pairs = (("n52-n64", "bridge-n52", "fine-n64"), ("n64-n80", "fine-n64", "fine-n80"),
                 ("n80-n96", "fine-n80", "fine-n96"), ("width080", PRIMARY, "width080-n96"), ("width125", PRIMARY, "width125-n96"))
        comparisons, nesting_checks = {}, {}
        for label, left, right in pairs:
            comparisons[label] = {"power_3_2": compare(left, right, members, truth), "raw_J": compare(left, right, members, truth, raw=True)}
            for readout_name, comparison in comparisons[label].items():
                comparison["right_minus_left_fit_percentage_points"] = {window: {key: fits[right][readout_name][window][key]-fits[left][readout_name][window][key]
                                                                                 for key in ("mape_percent", "max_percent_error")} for window in WINDOWS}
            if label.startswith("n"):
                old_values, new_values = members[left]["lambda_raw"], members[right]["lambda_raw"]
                difference = new_values[:len(old_values)]-old_values
                tolerance = TOL*max(1., float(np.max(np.abs(old_values))), float(np.max(np.abs(new_values))))
                nesting_checks[label] = {"left": left, "right": right, "compared_count": len(old_values),
                                         "max_raw_lambda_increase": float(np.max(difference)), "tolerance": tolerance,
                                         "passed": bool(np.max(difference) <= tolerance), "normalized_prediction_not_required_monotone": True}
        output.json("nested-Ritz-controls.json", nesting_checks)
        if not all(row["passed"] for row in nesting_checks.values()):
            raise RuntimeError("Same-width nested raw Ritz control failed; no retry")
        stability = {label: all(row["G_below_threshold"] for row in comparisons[label]["power_3_2"]["windows"].values())
                     for label in ("n64-n80", "n80-n96", "width080", "width125")}
        stable = all(stability.values())
        retained_fit = fits[PRIMARY]["power_3_2"]["1-320"]["mape_percent"] < FULL_M_REF
        assessment = {"status": "ADVANCE_FINITE_FIXED_PARAMETER_STABILITY_ONLY" if stable else "STOP_FORK_FINITE_STABILITY_GATE_FAILED",
                      "primary_predeclared": PRIMARY, "primary_rho_not_reselected": True, "stability_checks": stability,
                      "all_four_window_G_below_2_percent": stable,
                      "primary_full320_M_below_external_reference": retained_fit,
                      "primary_full320_M": fits[PRIMARY]["power_3_2"]["1-320"]["mape_percent"], "external_reference_full320_M": FULL_M_REF,
                      "old_CS14_joint_score": winner["joint_score"], "old_CS14_joint_gate_remains_failed": True,
                      "old_CS14_training_worst_percent": winner["max_percent_error"],
                      "current_primary_first100_worst_percent": fits[PRIMARY]["power_3_2"]["1-100"]["max_percent_error"],
                      "continuous_index_accuracy_not_certified": True, "raw_J_does_not_reselect": True,
                      "family_not_globally_excluded_by_finite_failure": True}
        points, fit_rows, comparison_rows, residual_rows = (io.StringIO(newline="") for _ in range(4))
        point_writer, fit_writer, comparison_writer, residual_writer = [csv.writer(stream) for stream in (points, fit_rows, comparison_rows, residual_rows)]
        point_writer.writerow(["object_id", "n", "h", "kappa", "rho", "readout", "index", "window", "target", "predicted", "energy", "lambda_raw", "residual", "percent_error"])
        fit_writer.writerow(["object_id", "readout", "window", "count", "mape_percent", "max_percent_error", "rmse", "max_absolute_error"])
        comparison_writer.writerow(["comparison", "readout", "left", "right", "window", "G_percent", "G_below_2_percent", "unscaled_energy_max_relative_percent", "raw_lambda_max_absolute_difference", "right_minus_left_M", "right_minus_left_W"])
        residual_writer.writerow(["object_id", "prefix", "diagnostic", "mean", "max"])
        for name, member in members.items():
            meta = metadata[name]
            for readout_name, prediction, energy in (("power_3_2", "predicted_320", "energy_power_3_2"), ("raw_J", "raw_J_predicted_320", "lambda_raw")):
                for index in range(320):
                    actual, predicted = truth[index], member[prediction][index]
                    window = "1-100" if index < 100 else "101-300" if index < 300 else "301-320"
                    point_writer.writerow([name, meta["n"], meta["h"], meta["kappa"], meta["rho"], readout_name, index+1, window,
                                           actual, predicted, member[energy][index], member["lambda_raw"][index], predicted-actual, 100*abs(predicted-actual)/actual])
                for window, fit in fits[name][readout_name].items():
                    fit_writer.writerow([name, readout_name, window, *[fit[key] for key in ("count", "mape_percent", "max_percent_error", "rmse", "max_absolute_error")]])
        for label, readouts in comparisons.items():
            for readout_name, comparison in readouts.items():
                for window, row in comparison["windows"].items():
                    shifts = comparison["right_minus_left_fit_percentage_points"][window]
                    comparison_writer.writerow([label, readout_name, comparison["left"], comparison["right"], window,
                                                row["G_percent"], row["G_below_threshold"], row["unscaled_energy_max_relative_percent"],
                                                row["raw_lambda_max_absolute_difference"], shifts["mape_percent"], shifts["max_percent_error"]])
        for name, record in all_records.items():
            for diagnostic in ("residual", "relative_residual", "inside_residual", "outside_leak", "edge_occupation"):
                for prefix, row in record["continuous_diagnostics"][diagnostic].items():
                    residual_writer.writerow([name, prefix, diagnostic, row["mean"], row["max"]])
        for filename, stream in (("points.csv", points), ("fit-rows.csv", fit_rows), ("comparison-rows.csv", comparison_rows), ("continuous-residual-summary.csv", residual_rows)):
            output.binary(filename, stream.getvalue().encode("utf-8"))
        output.json("fit-metrics.json", fits)
        output.json("comparisons.json", comparisons)
        output.json("finite-stability-assessment.json", assessment)
        end_locks = verify_inputs()
        if (end_locks != locks or sha(Path(__file__)) != own_hash or sha(OUT/"fixed-identity.json") != identity_hash
                or sha(OUT/"source-winners-frozen.json") != sha(OLD/"winners-frozen.json")):
            raise RuntimeError("Frozen source/input/identity changed during run")
        if (counters["objects_completed"] != 10 or counters["physical_eigh_completed"] != 24
                or counters["fullspace_eigh_completed"] != 4 or counters["parity_eigh_completed"] != 20):
            raise RuntimeError("Completed physical-call ledger differs from frozen 10-object/24-eigh plan")
        end_verification = {"input_count": len(locks), "all_input_hashes_match": True,
                            "script_sha256_unchanged": True, "fixed_identity_sha256_unchanged": True, "source_identity_copy_byte_identical": True}
        monitor_health.check()
        stop.set()
        monitor.join(timeout=1)
        monitor_health.require_stopped(monitor)
        report = {"scope_id": SCOPE, "status": "completed", "run_passport": "UNVERIFIED", "source_evaluation_id": EXPECTED_ID,
                  "fixed_theta": theta, "primary": PRIMARY, "fixed_identity_sha256": identity_hash,
                  "objects": all_records, "controls": control_records, "fit_metrics": fits, "comparisons": comparisons,
                  "nested_Ritz_controls": nesting_checks, "finite_stability_assessment": assessment,
                  "historical_CS14_joint_score": winner["joint_score"], "historical_CS14_joint_failure_not_revised": True,
                  "counters": dict(counters), "end_verification": end_verification,
                  "seconds_before_final_serialization": time.perf_counter()-started,
                  "maxrss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "completed_utc": utc(),
                  "output_bytes_before_result": output.size(), "continuous_residual_is_observed_not_certified": True,
                  "resource_monitor_closed": True, "resource_monitor_failure": monitor_health.snapshot(),
                  "new_targets_generated": False, "no_parameter_or_width_reselection": True, "formal_route": "UNASSIGNED; B NOT INVOKED"}
        output.json("result.json", report)
        event("completed", primary=PRIMARY, seconds=report["seconds_before_final_serialization"], counters=dict(counters), output_bytes=output.size())
        inventory = {str(path.relative_to(OUT)): {"bytes": path.stat().st_size, "sha256": sha(path)}
                     for path in sorted(OUT.rglob("*")) if path.is_file()}
        output.json("file-inventory.json", {"scope_id": SCOPE, "inventory_excludes_itself": True, "files": inventory})
    except Exception as exc:
        try:
            event("failed", type=type(exc).__name__, message=str(exc), counters=dict(counters), end_verification=end_verification,
                  resource_monitor_failure=monitor_health.snapshot())
        except Exception as logging_exc:
            print(f"Could not append failure evidence: {type(logging_exc).__name__}: {logging_exc}", file=sys.stderr, flush=True)
        raise
    finally:
        stop.set()
        monitor.join(timeout=1)
        if monitor.is_alive():
            print("Resource monitor still alive at failure cleanup; closure not claimed", file=sys.stderr, flush=True)
        event_stream.close()


if __name__ == "__main__":
    if sys.argv[1:] == ["--preflight"]:
        print(json.dumps({"logger": logger_regression_test(), "metadata": metadata_regression_test(), "monitor": monitor_regression_test(),
                          "input_count": len(verify_inputs()), "scientific_numerics_performed": False}, indent=2))
    elif len(sys.argv) == 1:
        main()
    else:
        raise SystemExit("Only --preflight (non-scientific) or the frozen no-argument run is supported")
