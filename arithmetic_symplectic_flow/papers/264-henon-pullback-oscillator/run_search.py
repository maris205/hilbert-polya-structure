#!/usr/bin/env python3
"""CS14 frozen Hermite pullback-oscillator search; no science on import.

Every physical call assembles the full n^2 real symmetric compression and
performs one all-vector eigh. One-dimensional rectangular polynomial chains
are padded before multiplication, not powered after truncation. The primary
3/2 power is fixed; raw J is a same-spectrum diagnostic, never a selector.
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
from scipy.optimize import minimize


PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[1]
OUT = PACKAGE/"evidence/run-1"
LOCK_FILE = PACKAGE/"input-locks.json"
TARGET_FILE = ROOT/"papers/253-structural-homotopy-search/evidence/run-1/evaluations/CS03-Q-QUARTIC-0103.npz"
REFERENCES = (
    (ROOT/"papers/251-constructive-fit-portfolio/evidence/run-1/reference-101-150.json", 50),
    (ROOT/"papers/253-structural-homotopy-search/evidence/run-1/reference-151-200.json", 50),
    (ROOT/"papers/254-global-forms-joint-fit/evidence/run-1/reference-201-240.json", 40),
    (ROOT/"papers/255-path-operator-multigrid/evidence/run-1/reference-241-300.json", 60),
    (ROOT/"papers/256-chronological-heat-spectrum/evidence/run-1/reference-301-320.json", 20),
)
OLD_DIRECTORY = ROOT/"papers/259-hyperbolic-tail-heat-search/evidence/run-1"
SCOPE = "ASFS-DISCOVERY-20260919-CS14"
FORM = "CS14-HENON-PULLBACK-OSCILLATOR"
LOWER, UPPER = (.015, .05), (.6, 30.)
TRAIN_N, POST_N = (24, 28), (36, 44, 52)
WINDOWS = {"1-100": (0, 100), "101-300": (100, 300), "301-320": (300, 320), "1-320": (0, 320)}
M_REF, W_REF, FULL_M_REF = 1.695273790061038, 5.234299091683695, 3.5251249515592384
G_REF, PENALTY, GIB = 2., 1e30, 1024**3
COMMAND = ("OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 "
           "PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 600s python -u "
           "papers/264-henon-pullback-oscillator/run_search.py")


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
    stream = io.StringIO()
    event = make_logger(stream)
    cases = (("forward_start", {"name": "sample-n24", "stage": "training", "n": 24}),
             ("physical_eigh_complete", {"name": "sample-n24", "status": "VALID"}),
             ("winner_arrays_save_start", {"name": "winner-n24", "additional_eigh": False}),
             ("winner_arrays_saved", {"name": "winner-n24", "counters": {"full_arrays_saved": 1}}),
             ("fixed_postcheck_saved", {"name": "sourceoff-n52", "stage": "sourceoff"}))
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
    return {"passed": True, "case_count": len(cases), "event_and_name_preserved": True,
            "reserved_event_utc_rejected": True, "scientific_numerics_performed": False}


def cache_key(theta):
    return tuple(float(value).hex() for value in theta)


def metadata_regression_test():
    point = (.08, 1.)
    checks = {"same_theta_matches": cache_key(point) == cache_key(tuple(point)),
              "parameter_order_matters": cache_key(point) != cache_key(point[::-1]),
              "two_parameters": len(LOWER) == len(UPPER) == 2,
              "positive_log_box": all(0 < lo < hi for lo, hi in zip(LOWER, UPPER)),
              "physical_budget": 2*(12+18)+3+3+1+1 == 68,
              "both_training_dimensions_above_320": all(n*n >= 320 for n in TRAIN_N),
              "full_cartesian_seeds": len([(h, kappa) for h in (.025, .08, .25, .6) for kappa in (.1, 1., 10.)]) == 12}
    if not all(checks.values()):
        raise AssertionError("Frozen scalar metadata regression")
    return {"passed": True, "checks": checks, "scientific_numerics_performed": False}


class BoundedOutput:
    """Every write is exclusive and guarded by the shared hard byte budget."""
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
    coordinate = math.sqrt(width/2)*(lower+raising)
    derivative = (lower-raising)/math.sqrt(2*width)
    return coordinate, derivative


def assemble(h, kappa, n, rho):
    """Exact polynomial compression via one-dimensional rectangular chains."""
    width = rho*h
    x_pad, d_pad = hermite_matrices(n+2, width)
    q_pad = x_pad+.5*np.eye(n+2)
    # Input degrees 0..n-1; one step reaches n, two steps reach n+1.
    x_rect, d_rect, q_rect = x_pad[:, :n], d_pad[:, :n], q_pad[:, :n]
    q_squared_rect = (q_pad@q_pad)[:, :n]
    h0 = h*h*(d_rect.T@d_rect)+x_rect.T@x_rect
    q2, y2 = q_rect.T@q_rect, x_rect.T@x_rect
    q4 = q_squared_rect.T@q_squared_rect
    identity = np.eye(n)
    matrix = np.kron(h0, identity)+np.kron(identity, h0)+kappa*(np.kron(q4, identity)+4*np.kron(q2, y2))
    if not np.all(np.isfinite(matrix)):
        raise RuntimeError("Nonfinite Hermite compression; no clipping or retry")
    return {"matrix_S": matrix, "H0": h0, "Q2": q2, "Y2": y2, "Q4": q4,
            "X_rect": x_rect.copy(), "D_rect": d_rect.copy(), "Q_rect": q_rect.copy(),
            "Q_squared_rect": q_squared_rect.copy(), "hermite_width_b": np.array(width),
            "basis_q_degree": np.repeat(np.arange(n), n), "basis_y_degree": np.tile(np.arange(n), n)}


def independent_padded_reference(h, kappa, n, rho):
    """Independent +4 square polynomial expansion, final tensor compression."""
    dimension = n+4
    x, derivative = hermite_matrices(dimension, rho*h)
    q = x+.5*np.eye(dimension)
    h0 = -h*h*(derivative@derivative)+x@x
    q2, y2 = q@q, x@x
    q4 = q@q@q@q
    identity = np.eye(dimension)
    padded = np.kron(h0, identity)+np.kron(identity, h0)+kappa*(np.kron(q4, identity)+4*np.kron(q2, y2))
    selected = np.array([i*dimension+j for i in range(n) for j in range(n)])
    return padded[np.ix_(selected, selected)]


def oscillator_spectrum(h, n):
    return np.sort(np.array([2*h*(i+j+1) for i in range(n) for j in range(n)]))


def metrics(prediction, target):
    relative = np.abs(prediction-target)/target
    return {"count": len(target), "mape_percent": float(100*np.mean(relative)),
            "max_percent_error": float(100*np.max(relative)),
            "rmse": float(np.sqrt(np.mean((prediction-target)**2))),
            "max_absolute_error": float(np.max(np.abs(prediction-target)))}


def readout(arrays, eigenvalues, states, target, control=False):
    if not np.all(np.isfinite(eigenvalues)) or eigenvalues[0] <= 0 or not np.all(np.diff(eigenvalues) >= 0):
        raise RuntimeError("Raw spectrum must be positive, finite and nondecreasing; no clipping or retry")
    with np.errstate(over="ignore", invalid="ignore"):
        energy = eigenvalues**1.5
        predicted = target[0]*(eigenvalues[:320]/eigenvalues[0])**1.5
        raw_predicted = target[0]*eigenvalues[:320]/eigenvalues[0]
    finite = np.isfinite(energy)
    required = len(eigenvalues) if control else 320
    reasons = []
    if len(eigenvalues) < required:
        reasons.append("INSUFFICIENT_SPECTRAL_COUNT")
    if not np.all(finite[:required]) or not np.all(np.isfinite(predicted[:required])) or not np.all(energy[:required] > 0):
        reasons.append("PRIMARY_PREFIX_ENERGY_OR_PREDICTION_INVALID")
    if not np.all(np.diff(energy[:required]) >= 0):
        reasons.append("PRIMARY_PREFIX_ENERGY_NOT_NONDECREASING")
    if not np.all(np.isfinite(raw_predicted[:required])):
        reasons.append("RAW_J_PREFIX_PREDICTION_INVALID")
    valid = not reasons
    matrix = arrays["matrix_S"]
    trace, fro2 = float(np.trace(matrix)), float(np.sum(matrix*matrix))
    sum_lambda, sum_lambda2 = float(np.sum(eigenvalues)), float(np.sum(eigenvalues*eigenvalues))
    retained = states.shape[1]
    residual = np.linalg.norm(matrix@states-states*eigenvalues[:retained], axis=0)
    orthogonality = float(np.linalg.norm(states.T@states-np.eye(retained)))
    n = int(arrays["n"])
    high_count = math.ceil(n/5)
    boundary = (arrays["basis_q_degree"] >= n-high_count) | (arrays["basis_y_degree"] >= n-high_count)
    occupation = np.sum(states[boundary]**2, axis=0)
    edge_summary = {}
    for count in (100, 320):
        if retained >= count:
            edge_summary[str(count)] = {"mean": float(np.mean(occupation[:count])), "max": float(np.max(occupation[:count]))}
    if retained < 100:
        edge_summary["all_control_states"] = {"count": retained, "mean": float(np.mean(occupation)), "max": float(np.max(occupation))}
    row_norm = float(np.max(np.sum(np.abs(matrix), axis=1)))
    arrays.update(lambda_raw=eigenvalues, energy_power_3_2=energy, finite_mask=finite,
                  raw_J_finite_mask=np.isfinite(eigenvalues), predicted_320=predicted, raw_J_predicted_320=raw_predicted,
                  scale=np.array(target[0]/energy[0]), raw_J_scale=np.array(target[0]/eigenvalues[0]), target_100=target.copy(),
                  valid=np.array(valid), invalid_reasons=np.array(reasons, dtype=str),
                  eigenvector_residual=residual, truncation_edge_occupation=occupation, truncation_edge_mask=boundary,
                  _cached_states=states)
    return {"valid": valid, "status": "VALID" if valid else "INVALID_READOUT", "invalid_reasons": reasons,
            "required_energy_count": required, "lambda_min": float(eigenvalues[0]), "lambda_max": float(eigenvalues[-1]),
            "energy_power_3_2_min": nullable(energy[0]), "scale": nullable(target[0]/energy[0]),
            "raw_J_scale": float(target[0]/eigenvalues[0]), "no_clipping_or_deleted_modes": True,
            "finite_energy_count_all_N": int(np.sum(finite)), "matrix_symmetry_max_difference": float(np.max(np.abs(matrix-matrix.T))),
            "J_absolute_row_sum_max": row_norm, "trace_J": trace, "full_lambda_sum": sum_lambda,
            "trace_relative_difference": abs(trace-sum_lambda)/max(1., abs(trace)),
            "frobenius_squared_J": fro2, "full_lambda_squared_sum": sum_lambda2,
            "second_moment_relative_difference": abs(fro2-sum_lambda2)/max(1., fro2),
            "retained_states": retained, "eigenvector_residual_max": float(np.max(residual)),
            "eigenvector_residual_relative_row_norm_max": float(np.max(residual))/max(1., row_norm),
            "states_orthogonality_fro": orthogonality, "edge_top_modes_each_axis": high_count,
            "edge_definition": "union of highest ceil(n/5) q or y Hermite degrees", "edge_occupation_summary": edge_summary,
            "degenerate_state_diagnostics_basis_dependent": True, "diagnostics_are_not_selection_gates": True,
            "same_call_eigenvectors": True, "states_saved": False, "extra_state_eigh_calls": 0,
            "training_metrics": metrics(predicted[:100], target) if valid and not control else None,
            "raw_J_training_metrics": metrics(raw_predicted[:100], target) if valid and not control else None}


def pair_summary(grids, arrays, target):
    valid = all(row["valid"] for row in grids.values())
    if not valid:
        return {"valid": False, "status": "INVALID_MEMBER", "joint_score": PENALTY, "J_minus_1": PENALTY-1,
                "max_mape_percent": None, "max_percent_error": None, "G100_percent": None}
    maximum_m = max(row["training_metrics"]["mape_percent"] for row in grids.values())
    maximum_w = max(row["training_metrics"]["max_percent_error"] for row in grids.values())
    gap = float(100*np.max(np.abs(arrays[TRAIN_N[0]]["predicted_320"][:100]-arrays[TRAIN_N[1]]["predicted_320"][:100])/target))
    score = max(maximum_m/M_REF, maximum_w/W_REF, gap/G_REF)
    return {"valid": True, "status": "VALID", "joint_score": score, "J_minus_1": score-1,
            "max_mape_percent": maximum_m, "max_percent_error": maximum_w, "G100_percent": gap}


def rank(row):
    return (row["joint_score"], row["max_mape_percent"], row["max_percent_error"], row["G100_percent"], row["evaluation_id"])


def compact(arrays, record):
    return {"prediction": arrays["predicted_320"].copy(), "raw_prediction": arrays["raw_J_predicted_320"].copy(),
            "energy": arrays["energy_power_3_2"][:320].copy(), "lambda_raw": arrays["lambda_raw"][:320].copy(),
            "scale": float(arrays["scale"]), "raw_scale": float(arrays["raw_J_scale"]),
            "valid": record["valid"], "invalid_reasons": record["invalid_reasons"]}


def compare(left_name, right_name, members, truth, raw=False):
    left, right = members[left_name], members[right_name]
    valid = left["valid"] and right["valid"]
    prediction_key, energy_key = ("raw_prediction", "lambda_raw") if raw else ("prediction", "energy")
    record = {"left": left_name, "right": right_name, "readout": "raw_J" if raw else "power_3_2",
              "status": "VALID" if valid else "UNASSESSABLE_INVALID_MEMBER", "G_threshold_percent": G_REF,
              "left_invalid_reasons": left["invalid_reasons"], "right_invalid_reasons": right["invalid_reasons"],
              "raw_energy_denominator": "left object", "windows": None}
    if valid:
        record["windows"] = {}
        for window, (start, end) in WINDOWS.items():
            gap = float(100*np.max(np.abs(left[prediction_key][start:end]-right[prediction_key][start:end])/truth[start:end]))
            raw_gap = float(100*np.max(np.abs(left[energy_key][start:end]-right[energy_key][start:end])/left[energy_key][start:end]))
            record["windows"][window] = {"G_percent": gap, "G_below_threshold": gap < G_REF,
                                            "unscaled_energy_max_relative_percent": raw_gap,
                                            "raw_lambda_max_absolute_difference": float(np.max(np.abs(left["lambda_raw"][start:end]-right["lambda_raw"][start:end])))}
    return record


def main():
    started = time.perf_counter()
    logger_test, metadata_test = logger_regression_test(), metadata_regression_test()
    locks, own_hash = verify_inputs(), sha(Path(__file__))
    if OUT.exists():
        raise RuntimeError("Output directory exists; refusing overwrite or retry")
    OUT.mkdir(parents=True)
    (OUT/"evaluations").mkdir()
    output = BoundedOutput(OUT, GIB)
    event_stream, call_stream = output.text_stream("events.jsonl"), output.text_stream("calls.jsonl")
    event = make_logger(event_stream, echo=True)
    stop = threading.Event()
    counters = {"forwards_attempted": 0, "forwards_completed": 0,
                "control_forwards_attempted": 0, "control_forwards_completed": 0,
                "training_forwards_attempted": 0, "training_forwards_completed": 0,
                "postfreeze_forwards_attempted": 0, "postfreeze_forwards_completed": 0,
                "sourceoff_forwards_attempted": 0, "sourceoff_forwards_completed": 0,
                "physical_eigh_attempted": 0, "physical_eigh_completed": 0,
                "matrix_assemblies_attempted": 0, "matrix_assemblies_completed": 0,
                "independent_control_matrix_assemblies_attempted": 0, "independent_control_matrix_assemblies_completed": 0,
                "control_arrays_saved": 0, "training_compact_grids_saved": 0, "full_arrays_saved": 0,
                "svd_calls": 0, "root_calls": 0, "quadrature_calls": 0, "extra_state_eigh_calls": 0, "new_target_generations": 0}
    end_verification = None

    def resources():
        while not stop.wait(30):
            rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            event("resource_sample", pid=os.getpid(), seconds=time.perf_counter()-started, maxrss_kib=rss,
                  memory_above_1gib_advisory=bool(rss*1024 > GIB), output_bytes=output.size(), counters=dict(counters))

    monitor = threading.Thread(target=resources, daemon=True)
    monitor.start()
    try:
        output.json("manifest.json", {"scope_id": SCOPE, "started_utc": utc(), "pid": os.getpid(), "command": COMMAND,
                    "script_sha256": own_hash, "input_locks_sha256": sha(LOCK_FILE), "inputs": locks,
                    "python": sys.version, "numpy": np.__version__, "scipy": scipy.__version__,
                    "thread_environment": {key: os.environ.get(key) for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")},
                    "form": FORM, "parameter_order": ["h", "kappa"], "lower": LOWER, "upper": UPPER,
                    "parameterization": "affine normalized natural logarithms", "eta_fixed": .5, "a_representative": "2 sqrt(kappa)",
                    "train_n": TRAIN_N, "post_n": POST_N, "normal_rho": 1., "width_check_rho": 1.25,
                    "M_ref": M_REF, "W_ref": W_REF, "full320_M_ref": FULL_M_REF,
                    "max_pair_calls": 30, "max_physical_eigh": 68, "svd_root_quadrature_budget": 0,
                    "physical_solver": "scipy.linalg.eigh real symmetric full spectrum/all vectors, driver=evd, exactly once per forward",
                    "basis": "complete Cartesian Hermite degrees 0..n-1 each axis, centers (.5,0), width b=rho*h",
                    "assembly": "rectangular +2 one-dimensional Gram chains; independent controls use square +4 final compression",
                    "flattening": "q degree outer, y degree inner: i*n+j", "parity_blocks_selected": False,
                    "primary_readout": "gamma1*(lambda/lambda1)^1.5; fixed density-motivated engineering exponent",
                    "finite_power_owner": "(S_n)^1.5, not compression P_n S^1.5 P_n",
                    "kappa_zero_continuous_owner": "original oscillator closed form, without the deleted weighted-domain conditions",
                    "diagnostic_readout": "gamma1*lambda/lambda1; never used to select or reselect",
                    "old_scientific_modules_imported": False, "exact_physical_parameter_cache_only": True,
                    "all_trial_full_matrices_and_spectra_saved": True, "nonwinner_states_saved": False,
                    "new_targets_generated": False, "all_development_targets_previously_observed": True,
                    "reference_is_distinct_old_heat_owner": True, "output_hard_limit_bytes": GIB,
                    "memory_advisory_bytes": GIB, "timeout_seconds": 600,
                    "logger_regression": logger_test, "metadata_regression": metadata_test,
                    "actual_exit_code": "recorded by launching parent", "run_passport": "UNVERIFIED"})
        output.json("launch-receipt.json", {"scope_id": SCOPE, "started_utc": utc(), "pid": os.getpid(),
                    "script_sha256": own_hash, "input_locks_sha256": sha(LOCK_FILE), "input_count": len(locks),
                    "output_was_absent_before_exclusive_creation": True, "command": COMMAND})
        output.json("pure-interface-tests.json", {"logger": logger_test, "metadata": metadata_test})
        event("started", scope_id=SCOPE, pid=os.getpid())
        with np.load(TARGET_FILE, allow_pickle=False) as source:
            target = source["target_100"].copy()
        if len(target) != 100 or not np.all(np.isfinite(target)) or not np.all(np.diff(target) > 0) or target[0] <= 0:
            raise RuntimeError("Invalid frozen first100 target")

        def calculate(theta, n, stage, name, rho=1.):
            if counters["forwards_attempted"] >= 68:
                raise RuntimeError("Frozen physical-forward budget exceeded")
            counters["forwards_attempted"] += 1
            counters[stage+"_forwards_attempted"] += 1
            event("forward_start", name=name, n=n, dimension=n*n, stage=stage, theta=list(theta), rho=rho)
            tick = time.perf_counter()
            h, kappa = theta
            counters["matrix_assemblies_attempted"] += 1
            arrays = assemble(h, kappa, n, rho)
            counters["matrix_assemblies_completed"] += 1
            arrays.update(n=np.array(n), dimension=np.array(n*n), theta=np.array(theta), h=np.array(h), kappa=np.array(kappa),
                          rho=np.array(rho), eta=np.array(.5), a_representative=np.array(2*math.sqrt(kappa)))
            counters["physical_eigh_attempted"] += 1
            eigenvalues, full_vec = eigh(arrays["matrix_S"], eigvals_only=False, driver="evd", overwrite_a=False)
            counters["physical_eigh_completed"] += 1
            retained = full_vec[:, :min(n*n, 320)].copy()
            del full_vec
            try:
                record = readout(arrays, eigenvalues, retained, target, control=stage == "control")
            except Exception as readout_exc:
                # Preserve already-computed evidence, without constructing a
                # replacement power readout or invoking any scientific solver.
                failed_name = "failed-"+name
                try:
                    failed_arrays = {key: value for key, value in arrays.items() if not key.startswith("_cached_")}
                    failed_arrays.update(lambda_raw=eigenvalues, states=retained)
                    output.npz(failed_name+".npz", failed_arrays)
                    output.json(failed_name+".json", {
                        "scope_id": SCOPE, "name": name, "status": "HARD_READOUT_FAILURE",
                        "n": n, "dimension": n*n, "theta": list(theta), "rho": rho, "stage": stage,
                        "exception_type": type(readout_exc).__name__, "exception_message": str(readout_exc),
                        "first_raw_lambda": nullable(eigenvalues[0]), "last_raw_lambda": nullable(eigenvalues[-1]),
                        "raw_spectrum_and_same_call_states_preserved": True, "no_replacement_power_computed": True,
                        "additional_scientific_calls": 0, "counters": dict(counters)})
                    event("failed_forward_evidence_saved", name=failed_name, counters=dict(counters))
                except Exception as save_exc:
                    print(f"Could not preserve failed forward: {type(save_exc).__name__}: {save_exc}", file=sys.stderr, flush=True)
                raise
            counters["forwards_completed"] += 1
            counters[stage+"_forwards_completed"] += 1
            record.update(name=name, form=FORM, n=n, dimension=n*n, theta=list(theta), rho=rho,
                          h=h, kappa=kappa, eta=.5, a_representative=2*math.sqrt(kappa), stage=stage,
                          seconds=time.perf_counter()-tick, full_spectrum_count=len(eigenvalues), physical_eigh_calls=1,
                          no_selected_parity_sector=True, padded_chain_extra_degrees=2)
            event("physical_eigh_complete", name=name, status=record["status"], seconds=record["seconds"], counters=dict(counters))
            return arrays, record

        controls = {}
        for name, kappa, rho in (("control-1-sourceoff", 0., 1.), ("control-2-padding", .7, 1.), ("control-3-width-padding", .7, 1.25)):
            arrays, record = calculate((.16, kappa), 8, "control", name, rho=rho)
            checks = {"passed": record["valid"]}
            if kappa == 0:
                expected = oscillator_spectrum(.16, 8)
                difference = float(np.max(np.abs(arrays["lambda_raw"]-expected)))
                tolerance = 1e-10*max(1., float(np.max(np.abs(expected))))
                arrays["expected_lambda"] = expected
                checks.update(lambda_max_absolute_difference=difference, lambda_tolerance=tolerance,
                              passed=checks["passed"] and difference <= tolerance)
            else:
                counters["independent_control_matrix_assemblies_attempted"] += 1
                reference = independent_padded_reference(.16, kappa, 8, rho)
                counters["independent_control_matrix_assemblies_completed"] += 1
                difference = float(np.max(np.abs(arrays["matrix_S"]-reference)))
                tolerance = 1e-10*max(1., float(np.max(np.abs(reference))))
                arrays["independent_padding4_matrix_S"] = reference
                checks.update(matrix_max_absolute_difference=difference, matrix_tolerance=tolerance,
                              reference_method="padding+4 square operators, polynomial products then final tensor compression",
                              passed=checks["passed"] and difference <= tolerance)
            if rho == 1.:
                expected_h0 = np.diag(.16*(2*np.arange(8)+1))
                h0_difference = float(np.max(np.abs(arrays["H0"]-expected_h0)))
                h0_tolerance = 1e-10*max(1., float(np.max(np.abs(expected_h0))))
                arrays["expected_H0"] = expected_h0
                checks.update(H0_max_absolute_difference=h0_difference, H0_tolerance=h0_tolerance,
                              passed=checks["passed"] and h0_difference <= h0_tolerance)
            arrays["states"] = arrays.pop("_cached_states")
            record.update(control_checks=checks, states_saved=True)
            output.npz(name+".npz", arrays)
            output.json(name+".json", record)
            counters["control_arrays_saved"] += 1
            controls[name] = record
            event("control_saved", name=name, checks=checks, counters=dict(counters))
            if not checks["passed"]:
                raise RuntimeError("Frozen small control failed: "+name+"; no retry")
        del arrays
        cache, seed_physical = {}, {}
        call_rows, unique_rows = [], []
        best = None
        calls, unique = 0, 0
        log_lower, log_upper = np.log(LOWER), np.log(UPPER)

        def objective(normalized, stage, physical=None):
            nonlocal calls, unique, best
            calls += 1
            normalized = np.asarray(normalized)
            normalized_key = cache_key(normalized)
            if physical is not None:
                theta = np.asarray(physical).copy()
                seed_physical[normalized_key] = theta.copy()
            else:
                theta = seed_physical[normalized_key].copy() if normalized_key in seed_physical else np.exp(log_lower+normalized*(log_upper-log_lower))
                # Exact box endpoints avoid exp(log(bound)) rounding outside the frozen box.
                theta = np.where(normalized == 0., np.array(LOWER), np.where(normalized == 1., np.array(UPPER), theta))
            if (calls > 30 or not np.all(np.isfinite(theta)) or np.any(theta < LOWER) or np.any(theta > UPPER)
                    or not np.all(np.isfinite(normalized)) or np.any(normalized < 0) or np.any(normalized > 1)):
                raise RuntimeError("Frozen pair budget/log-parameter bounds violated")
            key = cache_key(theta)
            if key in cache:
                row = dict(cache[key])
                row.update(call=calls, stage=stage, cached=True, source_evaluation_id=row["evaluation_id"])
                call_rows.append(row)
                call_stream.write(json.dumps(row, allow_nan=False)+"\n")
                event("cached_pair_call", call=calls, source_evaluation_id=row["evaluation_id"], joint_score=row["joint_score"])
                return row["joint_score"]
            unique += 1
            eid = f"{FORM}-{unique:04d}"
            pair_arrays, grids = {}, {}
            event("pair_start", evaluation_id=eid, call=calls, theta=theta.tolist(), stage=stage)
            tick = time.perf_counter()
            for n in TRAIN_N:
                arrays, grid = calculate(theta, n, "training", f"{eid}-n{n}")
                arrays["evaluation_id"] = np.array(eid)
                output.npz(f"evaluations/{eid}-n{n}.npz", {name: value for name, value in arrays.items() if not name.startswith("_cached_")})
                output.json(f"evaluations/{eid}-n{n}.json", grid)
                counters["training_compact_grids_saved"] += 1
                pair_arrays[n], grids[str(n)] = arrays, grid
            row = {"evaluation_id": eid, "form": FORM, "theta": theta.tolist(), "normalized_log_x": normalized.tolist(),
                   "call": calls, "stage": stage, "cached": False, "grids": grids,
                   "seconds_including_save": time.perf_counter()-tick, **pair_summary(grids, pair_arrays, target)}
            output.json(f"evaluations/{eid}.json", row)
            cache[key] = row
            call_rows.append(row)
            unique_rows.append(row)
            call_stream.write(json.dumps(row, allow_nan=False)+"\n")
            if row["valid"] and (best is None or rank(row) < rank(best[1])):
                best = pair_arrays, row
            event("pair_complete", evaluation_id=eid, status=row["status"], joint_score=row["joint_score"],
                  J_minus_1=row["J_minus_1"], max_mape_percent=row["max_mape_percent"], max_percent_error=row["max_percent_error"])
            return row["joint_score"]

        seed_points = [np.array([h, kappa]) for h in (.025, .08, .25, .6) for kappa in (.1, 1., 10.)]
        output.json("seed-design.json", {"physical_seeds": [point.tolist() for point in seed_points],
                    "order": "h outer ascending; kappa inner ascending", "parameterization": "normalized natural logs"})
        for index, theta in enumerate(seed_points):
            normalized = (np.log(theta)-log_lower)/(log_upper-log_lower)
            objective(normalized, f"seed-{index:02d}", physical=theta)
        optimizer = {"status": "SKIPPED_NO_VALID_SEED", "nfev": 0, "no_budget_transfer": True}
        if best is not None:
            x0 = np.array(best[1]["normalized_log_x"])
            simplex = np.repeat(x0[None, :], 3, axis=0)
            for coordinate in range(2):
                simplex[coordinate+1, coordinate] += .08 if x0[coordinate] <= .92 else -.08
            event("optimizer_start", starting_member=best[1]["evaluation_id"], maxfev=18)
            optimized = minimize(lambda x: objective(x, "refine"), x0, method="Nelder-Mead", bounds=[(0., 1.)]*2,
                                 options={"maxfev": 18, "initial_simplex": simplex, "xatol": 1e-6, "fatol": 1e-6, "adaptive": False})
            optimizer = {"success": bool(optimized.success), "message": str(optimized.message), "nfev": int(optimized.nfev),
                         "nit": int(optimized.nit), "fun": float(optimized.fun), "budget_exhausted": bool(optimized.nfev >= 18)}
            event("optimizer_complete", optimizer=optimizer)
        else:
            event("optimizer_skipped", reason="NO_VALID_SEED")
        winner = best[1] if best is not None else None
        output.json("winners-frozen.json", {"scope_id": SCOPE, "frozen_utc": utc(), "winner": winner,
                    "status": "VALID_MEMBER" if winner is not None else "NO_VALID_MEMBER", "calls": calls, "unique_members": unique,
                    "optimizer": optimizer, "selection": "power_3_2 first100 n24/n28 only", "development_metrics_evaluated": False})
        identity_hash = sha(OUT/"winners-frozen.json")
        output.json("calls.json", call_rows)
        output.json("unique-members.json", unique_rows)
        event("winner_identity_frozen", sha256=identity_hash, evaluation_id=winner["evaluation_id"] if winner else None)
        members, metadata, full_records, frozen_files = {}, {}, {}, []

        def save_full(name, arrays, record, stage):
            event("winner_arrays_save_start", name=name, additional_eigh=False)
            arrays["states"] = arrays.pop("_cached_states")
            record["states_saved"] = True
            members[name] = compact(arrays, record)
            metadata[name] = {"stage": stage, "n": int(arrays["n"]), "dimension": int(arrays["dimension"]),
                              "theta": arrays["theta"].tolist(), "rho": float(arrays["rho"])}
            output.npz(name+".npz", arrays)
            output.json(name+".json", record)
            counters["full_arrays_saved"] += 1
            full_records[name] = record
            event("winner_arrays_saved", name=name, counters=dict(counters))
            return [name+".npz", name+".json"]

        if best is not None:
            pair_arrays, row = best
            for n in TRAIN_N:
                arrays = pair_arrays.pop(n)
                record = dict(row["grids"][str(n)])
                record.update(evaluation_id=row["evaluation_id"], selection_J=row["joint_score"])
                frozen_files.extend(save_full(f"winner-n{n}", arrays, record, "training-winner"))
                del arrays
                gc.collect()
        best = None
        if len(frozen_files) != (4 if winner is not None else 0):
            raise RuntimeError("Full training-array freeze file count mismatch")
        output.json("training-arrays-frozen.json", {"scope_id": SCOPE, "frozen_utc": utc(),
                    "winner_identity_file": "winners-frozen.json", "winner_identity_sha256": identity_hash,
                    "full_training_arrays": 2 if winner is not None else 0, "file_count": len(frozen_files),
                    "files_sha256": {name: sha(OUT/name) for name in frozen_files},
                    "development_metrics_evaluated": False, "counters": dict(counters)})
        event("training_arrays_frozen", sha256=sha(OUT/"training-arrays-frozen.json"), counters=dict(counters))
        event("development_reference_read_start", all_previously_observed=True, no_further_selection=True)
        portions = []
        for path, count in REFERENCES:
            values = np.array([float(value) for value in json.loads(path.read_text())["ordinates"]])
            if len(values) != count:
                raise RuntimeError("Known reference window length mismatch")
            portions.append(values)
        truth = np.concatenate([target, *portions])
        if len(truth) != 320 or not np.all(np.isfinite(truth)) or not np.all(np.diff(truth) > 0):
            raise RuntimeError("Invalid complete known reference ledger")
        old_result = json.loads((OLD_DIRECTORY/"result.json").read_text())
        old_role = old_result["roles"]["B"]
        if (old_role["evaluation_id"] != "CS09-B-QUINTIC-REFIT-0055"
                or abs(old_role["max_mape_percent"]-M_REF) > 1e-12 or abs(old_role["max_percent_error"]-W_REF) > 1e-12):
            raise RuntimeError("External historical benchmark identity/constants mismatch")
        with np.load(OLD_DIRECTORY/"post-B-N1279.npz", allow_pickle=False) as old:
            if not np.array_equal(old["target_100"], target):
                raise RuntimeError("External comparator target100 mismatch")
            external_prediction = old["predicted_320"].copy()
        external_fits = {window: metrics(external_prediction[start:end], truth[start:end]) for window, (start, end) in WINDOWS.items()}
        if abs(external_fits["1-320"]["mape_percent"]-FULL_M_REF) > 1e-10:
            raise RuntimeError("External full320 benchmark mismatch")
        output.json("external-history-comparator.json", {"source": str((OLD_DIRECTORY/"post-B-N1279.npz").relative_to(ROOT)),
                    "source_sha256": sha(OLD_DIRECTORY/"post-B-N1279.npz"), "model": "old B0055 heat model, distinct owner",
                    "predicted_320": external_prediction.tolist(), "fit_metrics": external_fits,
                    "raw_spectrum_comparison_permitted": False, "used_for_selection_only_as_frozen_M_W_constants": True})
        output.json("known-targets.json", {"first": 1, "last": 320, "ordinates": truth.tolist(),
                                           "all_previously_observed": True, "generated_by_this_run": False})
        post_records = {}

        def post(n, name, rho=1., sourceoff=False):
            theta = np.array(winner["theta"])
            if sourceoff:
                theta[1] = 0.
            stage = "sourceoff" if sourceoff else "postfreeze"
            arrays, record = calculate(theta, n, stage, name, rho=rho)
            record.update(source_evaluation_id=winner["evaluation_id"], no_selection=True,
                          sourceoff=sourceoff, sourceoff_is_not_prime_coding_ablation=sourceoff)
            if sourceoff:
                expected = oscillator_spectrum(float(theta[0]), n)
                error = float(np.max(np.abs(arrays["lambda_raw"]-expected)))
                tolerance = 1e-10*max(1., float(np.max(np.abs(expected))))
                arrays["expected_lambda"] = expected
                record["sourceoff_control"] = {"lambda_max_absolute_difference": error, "lambda_tolerance": tolerance,
                                                 "passed": error <= tolerance, "all_multiplicities_retained": True}
            save_full(name, arrays, record, "fixed-"+stage)
            post_records[name] = record
            del arrays
            gc.collect()
            event("fixed_postcheck_saved", name=name, status=record["status"], counters=dict(counters))
            if sourceoff and not record["sourceoff_control"]["passed"]:
                raise RuntimeError("Fixed sourceoff analytic full-spectrum control failed; no retry")

        if winner is not None:
            for n in POST_N:
                post(n, f"post-n{n}")
            post(52, "post-width125-n52", rho=1.25)
            post(52, "sourceoff-n52", sourceoff=True)
        else:
            event("postfreeze_skipped", reason="NO_VALID_MEMBER")
        fits = {}
        for name, member in members.items():
            fits[name] = {"power_3_2": None, "raw_J": None}
            if member["valid"]:
                for readout_name, key in (("power_3_2", "prediction"), ("raw_J", "raw_prediction")):
                    fits[name][readout_name] = {window: metrics(member[key][start:end], truth[start:end]) for window, (start, end) in WINDOWS.items()}
        comparisons = {}
        if winner is not None:
            names = [f"winner-n{n}" for n in TRAIN_N]+[f"post-n{n}" for n in POST_N]
            sizes = TRAIN_N+POST_N
            pairs = [(f"n{sizes[index]}-n{sizes[index+1]}", names[index], names[index+1]) for index in range(4)]
            pairs.extend((("width125", "post-n52", "post-width125-n52"), ("SOURCEOFF", "post-n52", "sourceoff-n52")))
            for label, left, right in pairs:
                comparisons[label] = {"power_3_2": compare(left, right, members, truth), "raw_J": compare(left, right, members, truth, raw=True)}
                for readout_name, comparison in comparisons[label].items():
                    comparison["right_minus_left_fit_percentage_points"] = (
                        {window: {key: fits[right][readout_name][window][key]-fits[left][readout_name][window][key]
                                  for key in ("mape_percent", "max_percent_error")} for window in WINDOWS}
                        if fits[left][readout_name] is not None and fits[right][readout_name] is not None else None)
        assessment = {"status": "NO_VALID_MEMBER", "full_necessary_conditions_met": False}
        if winner is not None:
            training = {str(n): winner["grids"][str(n)]["training_metrics"] for n in TRAIN_N}
            training_better = all(row["mape_percent"] < M_REF and row["max_percent_error"] < W_REF for row in training.values())
            resolution_checks = {}
            for label in ("n36-n44", "n44-n52", "width125"):
                windows = comparisons[label]["power_3_2"]["windows"]
                resolution_checks[label] = all(row["G_below_threshold"] for row in windows.values()) if windows is not None else None
            final_fit = fits["post-n52"]["power_3_2"]
            full_better = final_fit is not None and final_fit["1-320"]["mape_percent"] < FULL_M_REF
            complete = bool(winner["joint_score"] < 1 and training_better and full_better and all(value is True for value in resolution_checks.values()))
            assessment = {"status": "NECESSARY_FINITE_ADVANCE_CONDITIONS_MET_MAGNITUDE_REVIEW_REQUIRED" if complete else "NECESSARY_FINITE_ADVANCE_CONDITIONS_NOT_MET",
                          "joint_score": winner["joint_score"], "J_below_1": winner["joint_score"] < 1,
                          "training_by_grid": training, "each_training_M_W_below_external_reference": training_better,
                          "n52_full320_M_below_external_reference": bool(full_better), "fine_and_width_checks": resolution_checks,
                          "full_necessary_conditions_met": complete, "small_gain_requires_actual_shift_review": True,
                          "engineering_lines_and_Ritz_bounds_not_accuracy_certificates": True, "raw_J_never_reselects": True}
        points, fit_rows, comparison_rows = io.StringIO(newline=""), io.StringIO(newline=""), io.StringIO(newline="")
        writer, fit_writer, comparison_writer = csv.writer(points), csv.writer(fit_rows), csv.writer(comparison_rows)
        writer.writerow(["object_id", "stage", "n", "dimension", "h", "kappa", "rho", "readout", "valid", "index", "window",
                         "target", "predicted", "energy", "lambda_raw", "residual", "percent_error"])
        fit_writer.writerow(["object_id", "readout", "window", "valid", "count", "mape_percent", "max_percent_error", "rmse", "max_absolute_error"])
        comparison_writer.writerow(["comparison", "readout", "left", "right", "window", "status", "G_percent", "G_below_2_percent",
                                    "unscaled_energy_max_relative_percent", "raw_lambda_max_absolute_difference", "right_minus_left_M", "right_minus_left_W"])
        for name, member in members.items():
            meta = metadata[name]
            for readout_name, prediction_key, energy_key in (("power_3_2", "prediction", "energy"), ("raw_J", "raw_prediction", "lambda_raw")):
                for index, (actual, predicted, energy, eigenvalue) in enumerate(zip(truth, member[prediction_key], member[energy_key], member["lambda_raw"]), 1):
                    window = "1-100" if index <= 100 else "101-300" if index <= 300 else "301-320"
                    writer.writerow([name, meta["stage"], meta["n"], meta["dimension"], *meta["theta"], meta["rho"], readout_name, member["valid"],
                                     index, window, actual, predicted, energy, eigenvalue, predicted-actual, 100*abs(predicted-actual)/actual])
                for window in WINDOWS:
                    fit = fits[name][readout_name][window] if fits[name][readout_name] is not None else None
                    fit_writer.writerow([name, readout_name, window, member["valid"],
                                         *([fit[key] for key in ("count", "mape_percent", "max_percent_error", "rmse", "max_absolute_error")] if fit else [None]*5)])
        for label, readouts in comparisons.items():
            for readout_name, comparison in readouts.items():
                for window in WINDOWS:
                    row = comparison["windows"][window] if comparison["windows"] is not None else None
                    shifts = comparison["right_minus_left_fit_percentage_points"][window] if row is not None else None
                    comparison_writer.writerow([label, readout_name, comparison["left"], comparison["right"], window, comparison["status"],
                                                *([row[key] for key in ("G_percent", "G_below_threshold", "unscaled_energy_max_relative_percent", "raw_lambda_max_absolute_difference")]
                                                  +[shifts["mape_percent"], shifts["max_percent_error"]] if row else [None]*6)])
        output.binary("points.csv", points.getvalue().encode("utf-8"))
        output.binary("fit-rows.csv", fit_rows.getvalue().encode("utf-8"))
        output.binary("comparison-rows.csv", comparison_rows.getvalue().encode("utf-8"))
        output.json("development-fit-metrics.json", fits)
        output.json("comparisons.json", comparisons)
        output.json("finite-discovery-assessment.json", assessment)
        end_locks = verify_inputs()
        if end_locks != locks or sha(Path(__file__)) != own_hash or sha(OUT/"winners-frozen.json") != identity_hash:
            raise RuntimeError("Frozen source/input/identity changed during run")
        end_verification = {"input_count": len(locks), "all_input_hashes_match": True,
                            "script_sha256_unchanged": True, "winner_identity_sha256_unchanged": True}
        report = {"scope_id": SCOPE, "status": "completed" if winner is not None else "completed_no_valid_member",
                  "run_passport": "UNVERIFIED", "winner": winner, "calls": calls, "unique_members": unique,
                  "cached_calls": sum(row["cached"] for row in call_rows), "invalid_unique_members": sum(not row["valid"] for row in unique_rows),
                  "optimizer": optimizer, "controls": controls, "winner_identity_sha256": identity_hash,
                  "full_readouts": full_records, "postfreeze": post_records, "fit_metrics": fits, "comparisons": comparisons,
                  "finite_discovery_assessment": assessment, "external_history_fit_metrics": external_fits,
                  "counters": dict(counters), "end_verification": end_verification,
                  "seconds_before_final_serialization": time.perf_counter()-started,
                  "maxrss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "completed_utc": utc(),
                  "output_bytes_before_result": output.size(), "new_targets_generated": False,
                  "primary_readout_fixed_power": 1.5, "raw_J_never_reselected": True,
                  "formal_route": "UNASSIGNED; B NOT INVOKED"}
        output.json("result.json", report)
        stop.set()
        monitor.join(timeout=1)
        event("completed", evaluation_id=winner["evaluation_id"] if winner else None,
              seconds=report["seconds_before_final_serialization"], calls=calls, counters=dict(counters), output_bytes=output.size())
        inventory = {str(path.relative_to(OUT)): {"bytes": path.stat().st_size, "sha256": sha(path)}
                     for path in sorted(OUT.rglob("*")) if path.is_file()}
        output.json("file-inventory.json", {"scope_id": SCOPE, "inventory_excludes_itself": True, "files": inventory})
    except Exception as exc:
        try:
            event("failed", type=type(exc).__name__, message=str(exc), counters=dict(counters), end_verification=end_verification)
        except Exception as logging_exc:
            print(f"Could not append failure evidence: {type(logging_exc).__name__}: {logging_exc}", file=sys.stderr, flush=True)
        raise
    finally:
        stop.set()
        monitor.join(timeout=1)
        call_stream.close()
        event_stream.close()


if __name__ == "__main__":
    main()
