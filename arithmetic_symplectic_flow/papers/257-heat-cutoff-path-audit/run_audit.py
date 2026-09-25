#!/usr/bin/env python3
"""CS07: one fixed-parameter cutoff/path audit; no fit, new targets or retry."""
import csv
from datetime import datetime, timezone
import gc
import hashlib
import importlib.util
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
from scipy import fft


PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[1]
OUT = PACKAGE / "evidence/run-1"
LOCK_FILE = PACKAGE / "input-locks.json"
SOURCE = ROOT / "papers/256-chronological-heat-spectrum/run_search.py"
OLD = SOURCE.parent / "evidence/run-1"
TARGET_SOURCE = ROOT / "papers/253-structural-homotopy-search/evidence/run-1/evaluations/CS03-Q-QUARTIC-0103.npz"
THETA = np.array([.16576459585764247, 1.6227345662574617, .5825369499577147])
SCOPE = "ASFS-DISCOVERY-20260919-CS07"
G_LIMIT, ORDER_FLOOR = 2., 1e-6
GIB = 1024**3
COMMAND = ("OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 "
           "PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 600s python -u "
           "papers/257-heat-cutoff-path-audit/run_audit.py")
REFERENCES = (
    (ROOT/"papers/251-constructive-fit-portfolio/evidence/run-1/reference-101-150.json", 50),
    (ROOT/"papers/253-structural-homotopy-search/evidence/run-1/reference-151-200.json", 50),
    (ROOT/"papers/254-global-forms-joint-fit/evidence/run-1/reference-201-240.json", 40),
    (ROOT/"papers/255-path-operator-multigrid/evidence/run-1/reference-241-300.json", 60),
    (OLD/"reference-301-320.json", 20),
)
WINDOWS = {"1-100": (0, 100), "101-300": (100, 300),
           "301-320": (300, 320), "1-320": (0, 320)}
ROLE_TUPLES = (
    ("CS07-A1-N1023", 1023, 8., 64, .02, 1, "O"),
    ("CS07-A2-N1279", 1279, 8., 64, .02, 1, "O"),
    ("CS07-A3-N1535", 1535, 8., 64, .02, 1, "O"),
    ("CS07-A4-TIME128", 1535, 8., 128, .02, 1, "O"),
    ("CS07-A5-BOX10", 1919, 10., 64, .02, 1, "O"),
    ("CS07-B1-PERM02", 1023, 8., 64, .02, 1, "P"),
    ("CS07-B2-ORDER20-R10", 1023, 8., 64, .20, 10, "O"),
    ("CS07-B3-PERM20-R10", 1023, 8., 64, .20, 10, "P"),
    ("CS07-B4-ORDER20-R20", 1023, 8., 64, .20, 20, "O"),
    ("CS07-B5-PERM20-R20", 1023, 8., 64, .20, 20, "P"),
)
ROLES = tuple(dict(zip(("id", "N", "L", "B", "beta", "r", "order"), row))
              for row in ROLE_TUPLES)
CONTROL = {"id": "CS07-CONTROL-KINETIC", "N": 63, "L": 8., "B": 64,
           "beta": .20, "r": 20, "order": "P"}


def utc():
    return datetime.now(timezone.utc).isoformat()


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, value):
    with path.open("x", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2, allow_nan=False)
        handle.write("\n")


def write_npz(path, arrays):
    with path.open("xb") as handle:
        np.savez_compressed(handle, **arrays)


def nullable(value):
    value = float(value)
    return value if math.isfinite(value) else None


def metrics(prediction, target):
    difference = prediction - target
    relative = np.abs(difference)/target
    return {"count": len(target), "mape_percent": float(100*np.mean(relative)),
            "max_percent_error": float(100*np.max(relative)),
            "mse": float(np.mean(difference**2)),
            "max_absolute_error": float(np.max(np.abs(difference))),
            "mean_absolute_spacing_error_in_target_gaps":
                float(np.mean(np.abs(np.diff(prediction)-np.diff(target))/np.diff(target)))}


def window_metrics(prediction, target, valid):
    return ({name: metrics(prediction[left:right], target[left:right])
             for name, (left, right) in WINDOWS.items()} if valid else None)


def import_math_source():
    spec = importlib.util.spec_from_file_location("cs07_locked_cs06_math", SOURCE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def prepare_samples(role, source, sample_cache, minimum_cache, counters, zero=False):
    """Keep only small sample/grid arrays in cache, never propagator matrices."""
    n, length, count = role["N"], role["L"], role["B"]
    key = n, length, count, zero
    if key in sample_cache:
        return sample_cache[key]
    h, a_start, mass = THETA
    q = -length + 2*length*np.arange(1, n+1)/(n+1)
    p = np.pi*h*np.arange(1, n+1)/(2*length)
    kinetic = p*p/(np.hypot(mass, p)+mass)
    midpoint, schedule = source.cooling(float(a_start), count)
    samples = np.zeros((count, n), dtype=float)
    ledger, clipped_count, max_clip = [], 0, 0.
    for index, a in enumerate(schedule):
        if zero:
            continue
        minimum = source.global_minimum("S", float(a), minimum_cache, counters)
        ledger.append(minimum)
        raw = source.potential("S", q, float(a))-minimum["minimum"]
        if not np.all(np.isfinite(raw)) or np.min(raw) < -1e-10:
            raise RuntimeError("Nonfinite W or W below frozen -1e-10 tolerance")
        negative = raw < 0
        clipped_count += int(np.count_nonzero(negative))
        if np.any(negative):
            max_clip = max(max_clip, float(np.max(-raw[negative])))
        samples[index] = np.maximum(raw, 0.)
    data = {"q": q, "p": p, "kinetic_minus_mass": kinetic,
            "midpoint_u": midpoint, "schedule": schedule, "W_samples": samples,
            "mean_W": np.mean(samples, axis=0), "minimum_ledger": ledger,
            "clipped_count": clipped_count, "max_clip": max_clip,
            "minimum_values": np.array([row["minimum"] for row in ledger]),
            "minimizers": np.array([row["minimizer"] for row in ledger])}
    sample_cache[key] = data
    return data


def readout(sigma, beta, first_target, count):
    mass = float(THETA[2])
    mask = np.isfinite(sigma) & (sigma > 0.)
    energy = np.full(sigma.shape, np.nan)
    energy[mask] = mass-np.log(sigma[mask])/beta
    mask &= np.isfinite(energy)
    reasons = []
    if len(sigma) < count:
        reasons.append("INSUFFICIENT_DIMENSION")
    if not (len(sigma) and math.isfinite(float(sigma[0])) and 0 < sigma[0] <= 1+1e-10):
        reasons.append("SIGMA0_OUT_OF_CONTRACTION_RANGE")
    if len(sigma) >= count and not np.all(mask[:count]):
        reasons.append("UNRESOLVED_REQUIRED_SINGULAR_VALUES")
    if len(sigma) >= count and not np.all(np.diff(sigma[:count]) <= 0):
        reasons.append("REQUIRED_SINGULAR_VALUES_NOT_ORDERED")
    ratio = float(sigma[count-1]/sigma[0]) if len(sigma) >= count and sigma[0] > 0 else float("nan")
    if not math.isfinite(ratio) or ratio < 1e-10:
        reasons.append("REQUIRED_RELATIVE_SINGULAR_VALUE_BELOW_1E-10")
    if not (len(energy) and math.isfinite(float(energy[0])) and energy[0] > 0):
        reasons.append("NONPOSITIVE_OR_NONFINITE_E0")
    if len(energy) >= count and (not np.all(np.isfinite(energy[:count]))
                                or not np.all(energy[:count] >= mass-1e-8)):
        reasons.append("REQUIRED_ENERGY_BELOW_REST_MASS_TOLERANCE_OR_NONFINITE")
    scale = float(first_target/energy[0]) if len(energy) and np.isfinite(energy[0]) and energy[0] > 0 else float("nan")
    prediction = scale*energy[:count] if math.isfinite(scale) else np.full(count, np.nan)
    arrays = {"sigma": sigma, "energy": energy, "energy_resolved_mask": mask,
              "predicted": prediction, "scale": np.array(scale), "resolution_valid": np.array(not reasons),
              "invalid_reasons": np.array(reasons, dtype=str)}
    record = {"status": "VALID" if not reasons else "INVALID_RESOLUTION",
              "resolution_valid": not reasons, "invalid_reasons": reasons,
              "sigma0": nullable(sigma[0]), "required_count": count,
              "required_last_sigma": nullable(sigma[count-1]), "required_sigma_ratio": nullable(ratio),
              "E0": nullable(energy[0]), "scale": nullable(scale),
              "resolved_energy_count": int(np.count_nonzero(mask))}
    return arrays, record


def state_diagnostics(states, q, length):
    n, count = states.shape
    boundary = np.sum(states[np.abs(q) > .9*length]**2, axis=0)
    transformed = fft.dst(states, type=1, axis=0, norm="ortho", workers=1)
    tail_count = (n+4)//5
    tail = np.sum(transformed[-tail_count:]**2, axis=0)
    summaries = {}
    for wanted in (100, 320):
        if wanted <= count:
            summaries[str(wanted)] = {"boundary_max": float(np.max(boundary[:wanted])),
                                      "boundary_mean": float(np.mean(boundary[:wanted])),
                                      "high_momentum_max": float(np.max(tail[:wanted])),
                                      "high_momentum_mean": float(np.mean(tail[:wanted]))}
    return boundary, tail, {"mode_count": tail_count, "rounding": "ceil(N/5)",
                             "boundary_condition": "abs(q)>0.9L", "summaries": summaries}


def run_role(role, samples, target, counters, zero=False):
    n, count, repeats = role["N"], role["B"], role["r"]
    beta, length = role["beta"], role["L"]
    order = (np.arange(count) if role["order"] == "O" else
             np.concatenate((np.arange(0, count, 2), np.arange(1, count, 2))))
    sequence = np.repeat(order, repeats)
    delta = beta/(count*repeats)
    half = np.exp(-.5*delta*samples["W_samples"])
    decay = np.exp(-delta*samples["kinetic_minus_mass"])
    product = np.eye(n)
    for index in sequence:
        transformed = fft.dst(half[index, :, None]*product, type=1, axis=0, norm="ortho", workers=1)
        drifted = fft.dst(decay[:, None]*transformed, type=1, axis=0, norm="ortho", workers=1)
        product = half[index, :, None]*drifted
    del transformed, drifted, half
    if not np.all(np.isfinite(product)):
        raise RuntimeError("Nonfinite real chronological product")
    counters["full_svd_calls"] += 1
    left_all, sigma, right_t_all = np.linalg.svd(product, full_matrices=True)
    retained = 63 if zero else 320
    left, right = left_all[:, :retained].copy(), right_t_all[:retained].T.copy()
    del left_all, right_t_all
    arrays, record = readout(sigma, beta, float(target[0]), retained)
    forward_residual = np.linalg.norm(product@right-left*sigma[:retained], axis=0)
    transpose_residual = np.linalg.norm(product.T@left-right*sigma[:retained], axis=0)
    matrix_fro_squared = float(np.sum(product*product))
    sigma_squared_sum = float(np.sum(sigma*sigma))
    sigma0_usable = math.isfinite(float(sigma[0])) and sigma[0] > 0
    forward_relative = forward_residual/sigma[0] if sigma0_usable else np.full(retained, np.nan)
    transpose_relative = transpose_residual/sigma[0] if sigma0_usable else np.full(retained, np.nan)
    left_boundary, left_tail, left_occupation = state_diagnostics(left, samples["q"], length)
    right_boundary, right_tail, right_occupation = state_diagnostics(right, samples["q"], length)
    arrays.update({key: samples[key] for key in
                   ("q", "p", "kinetic_minus_mass", "midpoint_u", "schedule", "W_samples",
                    "mean_W", "minimum_values", "minimizers")})
    arrays.update(C_tilde=product, theta=THETA.copy(), grid_n=np.array(n), L=np.array(length),
                  beta=np.array(beta), base_sample_count=np.array(count), repeats=np.array(repeats),
                  delta=np.array(delta), order_name=np.array(role["order"]),
                  sample_order_zero_based=order, sample_order_one_based=order+1,
                  fine_step_sample_indices_zero_based=sequence, singular_left=left, singular_right=right,
                  singular_forward_residual=forward_residual, singular_transpose_residual=transpose_residual,
                  singular_forward_residual_over_sigma0=forward_relative,
                  singular_transpose_residual_over_sigma0=transpose_relative,
                  left_boundary_mass=left_boundary, left_high_momentum_mass=left_tail,
                  right_boundary_mass=right_boundary, right_high_momentum_mass=right_tail,
                  target_320=target.copy(), role_id=np.array(role["id"]),
                  potential_mode=np.array("zero_control" if zero else "global_minimum_shift"))
    record.update(role=role, theta=THETA.tolist(), total_fine_steps=len(sequence), delta=delta,
                  potential_clipped_count=samples["clipped_count"], potential_maximum_clip=samples["max_clip"],
                  minimum_ledger=samples["minimum_ledger"], retained_singular_states=retained,
                  matrix_frobenius_squared=matrix_fro_squared, full_sigma_squared_sum=sigma_squared_sum,
                  frobenius_moment_relative_difference=nullable(abs(matrix_fro_squared-sigma_squared_sum)/matrix_fro_squared) if matrix_fro_squared > 0 else None,
                  moment_is_not_partial_state_reconstruction=True,
                  singular_forward_residual_max=nullable(np.max(forward_residual)),
                  singular_transpose_residual_max=nullable(np.max(transpose_residual)),
                  singular_forward_residual_over_sigma0_max=nullable(np.max(forward_relative)),
                  singular_transpose_residual_over_sigma0_max=nullable(np.max(transpose_relative)),
                  left_orthogonality_fro=float(np.linalg.norm(left.T@left-np.eye(retained))),
                  right_orthogonality_fro=float(np.linalg.norm(right.T@right-np.eye(retained))),
                  left_occupation=left_occupation, right_occupation=right_occupation,
                  spatial_step=2*length/(n+1), p_max=float(samples["p"][-1]),
                  metrics=None if zero else window_metrics(arrays["predicted"], target, record["resolution_valid"]),
                  all_targets_previously_observed=True, no_selection=True)
    if zero:
        expected_sigma = np.exp(-beta*samples["kinetic_minus_mass"])
        expected_energy = np.hypot(THETA[2], samples["p"])
        sigma_error = float(np.max(np.abs(sigma-expected_sigma)))
        energy_error = float(np.max(np.abs(arrays["energy"]-expected_energy)))
        arrays.update(expected_sigma=expected_sigma, expected_energy=expected_energy)
        record["analytic_control"] = {"sigma_max_absolute_difference": sigma_error,
                                      "energy_max_absolute_difference": energy_error,
                                      "sigma_tolerance": 1e-10, "energy_tolerance": 1e-8,
                                      "passed": bool(record["resolution_valid"] and sigma_error <= 1e-10 and energy_error <= 1e-8)}
    return arrays, record


def run_static(role, samples, target, counters):
    n = role["N"]
    modes = fft.dst(np.eye(n), type=1, axis=0, norm="ortho", workers=1)
    matrix = fft.dst(samples["kinetic_minus_mass"][:, None]*modes,
                     type=1, axis=0, norm="ortho", workers=1)
    del modes
    matrix.flat[::n+1] += THETA[2]+samples["mean_W"]
    asymmetry = float(np.linalg.norm(matrix-matrix.T)/np.linalg.norm(matrix))
    counters["static_eigh_calls"] += 1
    values, states_all = np.linalg.eigh(matrix, UPLO="L")
    if not np.all(np.isfinite(values)) or values[0] <= 0:
        raise RuntimeError("Nonfinite or nonpositive static spectrum")
    states = states_all[:, :320].copy()
    del states_all
    residual = np.linalg.norm(matrix@states-states*values[:320], axis=0)
    scale = float(target[0]/values[0])
    prediction = scale*values[:320]
    boundary, tail, occupation = state_diagnostics(states, samples["q"], role["L"])
    arrays = {"H_avg": matrix, "energy": values, "states": states, "equation_residual": residual,
              "predicted": prediction, "scale": np.array(scale), "theta": THETA.copy(),
              "q": samples["q"], "p": samples["p"], "kinetic_minus_mass": samples["kinetic_minus_mass"],
              "mean_W": samples["mean_W"], "schedule": samples["schedule"],
              "base_sample_count": np.array(role["B"]), "grid_n": np.array(n), "L": np.array(role["L"]),
              "target_320": target.copy(), "boundary_mass": boundary, "high_momentum_mass": tail}
    record = {"id": "STATIC-"+role["id"], "owner_role": role["id"], "N": n, "L": role["L"],
              "B": role["B"], "theta": THETA.tolist(), "E0": float(values[0]), "scale": scale,
              "symmetry_relative_fro": asymmetry, "equation_residual_max": float(np.max(residual)),
              "state_orthogonality_fro": float(np.linalg.norm(states.T@states-np.eye(320))),
              "occupation": occupation, "metrics": window_metrics(prediction, target, True),
              "not_separately_optimized": True, "no_selection": True}
    return arrays, record


def compact(arrays, valid=True):
    return {"prediction": arrays["predicted"].copy(), "energy": arrays["energy"][:320].copy(),
            "scale": float(arrays["scale"]), "valid": bool(valid),
            "invalid_reasons": arrays["invalid_reasons"].tolist() if "invalid_reasons" in arrays else []}


def comparison(left_id, right_id, members, target):
    left, right = members[left_id], members[right_id]
    valid = left["valid"] and right["valid"]
    record = {"left": left_id, "right": right_id, "status": "VALID" if valid else "UNASSESSABLE_INVALID_RESOLUTION",
              "left_invalid_reasons": left["invalid_reasons"], "right_invalid_reasons": right["invalid_reasons"],
              "left_E0": nullable(left["energy"][0]), "right_E0": nullable(right["energy"][0]),
              "left_scale": nullable(left["scale"]), "right_scale": nullable(right["scale"]),
              "raw_energy_relative_denominator": "positive raw energy of the first/left object", "windows": None}
    if valid:
        record["windows"] = {}
        for name, (start, stop) in WINDOWS.items():
            g = float(100*np.max(np.abs(left["prediction"][start:stop]-right["prediction"][start:stop])/target[start:stop]))
            raw = float(100*np.max(np.abs(left["energy"][start:stop]-right["energy"][start:stop])/left["energy"][start:stop]))
            record["windows"][name] = {"G_percent": g, "raw_energy_max_relative_percent": raw,
                                        "G_below_2_percent": g < G_LIMIT}
    return record


def main():
    started = time.perf_counter()
    locks = json.loads(LOCK_FILE.read_text())
    for relative, expected in locks.items():
        if sha(ROOT/relative) != expected:
            raise RuntimeError(f"Frozen input hash mismatch: {relative}")
    if OUT.exists():
        raise RuntimeError("Output exists; refusing overwrite or retry")
    OUT.mkdir(parents=True)
    log = (OUT/"events.jsonl").open("x", encoding="utf-8")
    log_lock, monitor_stop = threading.Lock(), threading.Event()
    counters = {"propagations": 0, "science_propagations": 0, "control_propagations": 0,
                "full_svd_calls": 0, "static_eigh_calls": 0,
                "minimum_scalar_solves": 0, "minimum_cache_hits": 0, "brent_calls": 0}

    def event(name, **fields):
        with log_lock:
            line = json.dumps({"utc": utc(), "event": name, **fields}, allow_nan=False)
            log.write(line+"\n")
            log.flush()
            print(line, flush=True)

    def output_size():
        return sum(path.stat().st_size for path in OUT.rglob("*") if path.is_file())

    def resources():
        while not monitor_stop.wait(30):
            rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            size = output_size()
            event("resource_sample", pid=os.getpid(), seconds=time.perf_counter()-started,
                  maxrss_kib=rss, memory_above_1gib_advisory=bool(rss*1024 > GIB),
                  output_bytes=size, output_above_1gib=bool(size > GIB))

    monitor = threading.Thread(target=resources, daemon=True)
    monitor.start()
    try:
        manifest = {"scope_id": SCOPE, "started_utc": utc(), "pid": os.getpid(), "command": COMMAND,
                    "script_sha256": sha(Path(__file__)), "input_locks_sha256": sha(LOCK_FILE), "inputs": locks,
                    "python": sys.version, "numpy": np.__version__, "scipy": scipy.__version__,
                    "thread_environment": {key: os.environ.get(key) for key in
                                           ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")},
                    "theta": THETA.tolist(), "roles_in_execution_order": ROLES, "analytic_control": CONTROL,
                    "source_reused_functions": ["potential", "cooling", "global_minimum"],
                    "source_globals_mutated": False, "retained_states_per_science_role": 320,
                    "high_momentum_mode_count": "ceil(N/5)", "raw_energy_comparison_denominator": "first object",
                    "all_targets_previously_observed": True, "no_optimization_or_reference_generation": True,
                    "root_isolation_certified": False, "run_passport": "UNVERIFIED",
                    "max_propagations": 11, "static_objects": 5, "memory_advisory_bytes": GIB,
                    "output_budget_bytes": GIB, "timeout_seconds": 600, "timeout_kill_grace_seconds": 10,
                    "actual_process_exit_code": "collected externally by launching parent"}
        write_json(OUT/"manifest.json", manifest)
        event("started", pid=os.getpid(), scope_id=SCOPE)
        source = import_math_source()
        frozen = json.loads((OLD/"winners-frozen.json").read_text())
        if frozen["roles"]["S"]["evaluation_id"] != "CS06-S-SEXTIC-HEAT-0047" or not np.array_equal(frozen["roles"]["S"]["theta"], THETA):
            raise RuntimeError("Source S0047 identity/parameter mismatch")
        with np.load(OLD/"winner-S-N511.npz", allow_pickle=False) as old:
            target100 = old["target_100"].copy()
        with np.load(TARGET_SOURCE, allow_pickle=False) as original_target:
            if len(target100) != 100 or not np.array_equal(target100, original_target["target_100"]):
                raise RuntimeError("Original first-100 target differs from source winner target")
        portions = []
        for path, length in REFERENCES:
            values = np.array([float(value) for value in json.loads(path.read_text())["ordinates"]])
            if len(values) != length:
                raise RuntimeError(f"Known reference length mismatch: {path}")
            portions.append(values)
        target = np.concatenate([target100, *portions])
        if len(target) != 320 or not np.all(np.isfinite(target)) or target[0] <= 0 or not np.all(np.diff(target) > 0):
            raise RuntimeError("Invalid known target ledger")
        write_json(OUT/"known-targets.json", {"first": 1, "last": 320, "ordinates": target.tolist(),
                                            "all_previously_observed": True, "generated_by_this_run": False})
        members, old_records = {}, {}
        old_paths = {"CS06-N383": OLD/"winner-S-N383.npz", "CS06-N511": OLD/"winner-S-N511.npz",
                     "CS06-N639": OLD/"post-space-N639.npz", "CS06-N767": OLD/"post-space-N767.npz"}
        for name, path in old_paths.items():
            with np.load(path, allow_pickle=False) as old:
                if not np.array_equal(old["theta"], THETA) or not np.array_equal(old["target_100"], target100):
                    raise RuntimeError("Reused role differs from frozen theta or target")
                members[name] = {"prediction": old["predicted_320"].copy(), "energy": old["energy"][:320].copy(),
                                 "scale": float(old["scale"]), "valid": bool(old["resolution_valid"]),
                                 "invalid_reasons": old["invalid_reasons"].tolist()}
            old_records[name] = {"source": str(path.relative_to(ROOT)), "sha256": sha(path),
                                 "metrics": window_metrics(members[name]["prediction"], target, members[name]["valid"]),
                                 "no_repropagation": True}
        write_json(OUT/"reused-roles.json", old_records)
        minimum_cache, sample_cache = {}, {}
        role_records, static_records = {}, {}
        point_file = (OUT/"points.csv").open("x", newline="", encoding="utf-8")
        writer = csv.writer(point_file)
        writer.writerow(["object_id", "kind", "resolution_valid", "index", "window", "target",
                         "predicted", "energy", "residual", "percent_error"])

        def point_rows(name, kind, member):
            for index, (actual, predicted, energy) in enumerate(zip(target, member["prediction"], member["energy"]), 1):
                window = "1-100" if index <= 100 else "101-300" if index <= 300 else "301-320"
                writer.writerow([name, kind, member["valid"], index, window, actual, predicted, energy,
                                 predicted-actual, 100*abs(predicted-actual)/actual])
            point_file.flush()

        try:
            for name in old_paths:
                point_rows(name, "reused", members[name])
            for role in (CONTROL, *ROLES):
                zero = role["id"] == CONTROL["id"]
                if counters["propagations"] >= 11:
                    raise RuntimeError("Frozen propagation budget exceeded")
                samples = prepare_samples(role, source, sample_cache, minimum_cache, counters, zero=zero)
                counters["propagations"] += 1
                counters["control_propagations" if zero else "science_propagations"] += 1
                tick = time.perf_counter()
                event("propagation_start", role=role, counters=dict(counters))
                arrays, record = run_role(role, samples, target, counters, zero=zero)
                record["compute_seconds_before_save"] = time.perf_counter()-tick
                static_id = None if zero else "STATIC-"+(role["id"] if role["id"].startswith("CS07-A") else ROLES[0]["id"])
                record["static_owner_id"] = static_id
                record["static_source_path"] = None if zero else static_id+".npz"
                if not zero:
                    arrays["static_owner_id"] = np.array(static_id)
                    arrays["static_source_path"] = np.array(static_id+".npz")
                if not zero:
                    members[role["id"]] = compact(arrays, record["resolution_valid"])
                    role_records[role["id"]] = record
                    point_rows(role["id"], "heat", members[role["id"]])
                write_npz(OUT/(role["id"]+".npz"), arrays)
                write_json(OUT/(role["id"]+".json"), record)
                del arrays
                gc.collect()
                event("propagation_complete", id=role["id"], status=record["status"],
                      seconds_including_save=time.perf_counter()-tick, counters=dict(counters))
                if zero:
                    control_record = record
                    if not record["analytic_control"]["passed"]:
                        raise RuntimeError("Analytic pure-kinetic control failed; no retry")
                elif role["id"].startswith("CS07-A"):
                    event("static_readout_start", id=static_id, not_a_propagation=True)
                    static_arrays, static_record = run_static(role, samples, target, counters)
                    members[static_id] = compact(static_arrays)
                    static_records[static_id] = static_record
                    point_rows(static_id, "static", members[static_id])
                    write_npz(OUT/(static_id+".npz"), static_arrays)
                    write_json(OUT/(static_id+".json"), static_record)
                    del static_arrays
                    gc.collect()
                    event("static_readout_complete", id=static_id, counters=dict(counters))
                if output_size() > GIB:
                    raise RuntimeError("Frozen 1 GiB output budget exceeded; no retry")
        finally:
            point_file.close()
        a1, a2, a3, a4, a5, b1, b2, b3, b4, b5 = (role["id"] for role in ROLES)
        pair_ids = {"old-383-511": ("CS06-N383", "CS06-N511"),
                    "old-511-639": ("CS06-N511", "CS06-N639"),
                    "old-639-767": ("CS06-N639", "CS06-N767"),
                    "old767-A1": ("CS06-N767", a1), "A1-A2": (a1, a2), "A2-A3": (a2, a3),
                    "A3-A4-time": (a3, a4), "A3-A5-box": (a3, a5),
                    "order-beta02": (a1, b1), "order-r10": (b2, b3), "order-r20": (b4, b5),
                    "order-refinement": (b2, b4), "permutation-refinement": (b3, b5)}
        pair_ids.update({"static-"+role["id"]: (role["id"], role_records[role["id"]]["static_owner_id"])
                         for role in ROLES})
        comparisons = {name: comparison(left, right, members, target) for name, (left, right) in pair_ids.items()}

        def stability(names):
            if any(comparisons[name]["windows"] is None for name in names):
                return "UNASSESSABLE_INVALID_RESOLUTION"
            return "BELOW_2_PERCENT" if all(comparisons[name]["windows"]["1-320"]["G_percent"] < G_LIMIT for name in names) else "NOT_BELOW_2_PERCENT"

        order_effect = {}
        necessary = ("order-r10", "order-r20", "order-refinement", "permutation-refinement")
        for window in WINDOWS:
            if any(comparisons[name]["windows"] is None for name in necessary):
                order_effect[window] = {"status": "UNASSESSABLE_INVALID_RESOLUTION",
                                        "invalid_dependency_comparisons": [name for name in necessary if comparisons[name]["windows"] is None]}
                continue
            delta10 = comparisons["order-r10"]["windows"][window]["G_percent"]
            delta20 = comparisons["order-r20"]["windows"][window]["G_percent"]
            epsilon = max(comparisons[name]["windows"][window]["G_percent"] for name in necessary[2:])
            threshold = max(ORDER_FLOOR, 10*epsilon)
            order_effect[window] = {"Delta_r10_percent": delta10, "Delta_r20_percent": delta20,
                                    "epsilon_percent": epsilon, "threshold_percent": threshold,
                                    "status": "ORDER EFFECT RESOLVED AT TESTED SPLITTINGS" if delta20 > threshold else "UNRESOLVED"}
        write_json(OUT/"comparisons.json", comparisons)
        write_json(OUT/"minimum-cache.json", list(minimum_cache.values()))
        report = {"scope_id": SCOPE, "status": "completed", "run_passport": "UNVERIFIED",
                  "theta": THETA.tolist(), "predeclared_primary_diagnostic": a3,
                  "roles": role_records, "static_objects": static_records, "reused_roles": old_records,
                  "analytic_control": control_record, "comparisons": comparisons, "order_effect": order_effect,
                  "space_engineering_status": stability(("A1-A2", "A2-A3")),
                  "time_engineering_status": stability(("A3-A4-time",)),
                  "box_engineering_status": stability(("A3-A5-box",)),
                  "counters": dict(counters), "seconds_before_final_serialization": time.perf_counter()-started,
                  "maxrss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                  "completed_utc": utc(), "all_inputs_unchanged": all(sha(ROOT/path) == wanted for path, wanted in locks.items()),
                  "output_bytes_before_result": output_size(), "all_targets_previously_observed": True,
                  "no_fit_or_new_winner": True, "formal_route": "UNASSIGNED; B NOT INVOKED"}
        write_json(OUT/"result.json", report)
        monitor_stop.set()
        monitor.join(timeout=1)
        event("completed", seconds=report["seconds_before_final_serialization"], counters=dict(counters),
              space_engineering_status=report["space_engineering_status"], output_bytes=output_size())
        write_json(OUT/"file-inventory.json", {str(path.relative_to(OUT)): path.stat().st_size
                                              for path in sorted(OUT.rglob("*")) if path.is_file()})
    except Exception as exc:
        event("failed", type=type(exc).__name__, message=str(exc), counters=dict(counters))
        raise
    finally:
        monitor_stop.set()
        monitor.join(timeout=1)
        log.close()


if __name__ == "__main__":
    main()
