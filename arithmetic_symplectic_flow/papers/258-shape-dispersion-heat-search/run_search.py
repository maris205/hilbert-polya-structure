#!/usr/bin/env python3
"""CS08 frozen five-form heat search. Main is the sole numerical entry point."""
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
from scipy.optimize import brentq, minimize


PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[1]
OUT = PACKAGE / "evidence/run-1"
LOCK_FILE = PACKAGE / "input-locks.json"
SOURCE = ROOT / "papers/256-chronological-heat-spectrum/run_search.py"
OLD256 = SOURCE.parent / "evidence/run-1"
OLD257 = ROOT / "papers/257-heat-cutoff-path-audit/evidence/run-1"
TARGET_SOURCE = ROOT / "papers/253-structural-homotopy-search/evidence/run-1/evaluations/CS03-Q-QUARTIC-0103.npz"
REFERENCES = (
    (ROOT/"papers/251-constructive-fit-portfolio/evidence/run-1/reference-101-150.json", 50),
    (ROOT/"papers/253-structural-homotopy-search/evidence/run-1/reference-151-200.json", 50),
    (ROOT/"papers/254-global-forms-joint-fit/evidence/run-1/reference-201-240.json", 40),
    (ROOT/"papers/255-path-operator-multigrid/evidence/run-1/reference-241-300.json", 60),
    (OLD256/"reference-301-320.json", 20),
)
SCOPE = "ASFS-DISCOVERY-20260919-CS08"
FORMS = {"B": "CS08-B-BASE-REFIT", "O": "CS08-O-OCTIC", "Q": "CS08-Q-QUINTIC",
         "U": "CS08-U-LOG-ENHANCED", "D": "CS08-D-LOG-RETARDED"}
BASE = np.array([.16576459585764247, 1.6227345662574617, .5825369499577147])
LOW3, HIGH3 = np.array([.12, 1.40, .30]), np.array([.22, 1.80, .90])
Z_BOUNDS = {"O": (0., .0002), "Q": (-.006, .006), "U": (0., .25), "D": (0., .25)}
STRUCTURE_SEEDS = {"O": [1e-6, 1e-5, 5e-5, 2e-4], "Q": [-.006, -.003, .003, .006],
                   "U": [.01, .03, .10, .25], "D": [.01, .03, .10, .25]}
TRAIN_N = (511, 639)
POST_N = (1023, 1279)
BETA, LENGTH, SAMPLE_COUNT = .02, 8., 64
M_REF, W_REF, G_REF, PENALTY = 2.050747149089365, 6.351622303308553, 2., 1e30
WINDOWS = {"1-100": (0, 100), "101-300": (100, 300), "301-320": (300, 320), "1-320": (0, 320)}
ROOT_XTOL, ROOT_RTOL, ROOT_TOL, ROOT_MERGE = 1e-13, 4*np.finfo(float).eps, 1e-9, 1e-10
GIB = 1024**3
COMMAND = ("OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 "
           "PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 600s python -u "
           "papers/258-shape-dispersion-heat-search/run_search.py")


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
    difference = prediction-target
    relative = np.abs(difference)/target
    return {"count": len(target), "mape_percent": float(100*np.mean(relative)),
            "max_percent_error": float(100*np.max(relative)), "mse": float(np.mean(difference**2)),
            "max_absolute_error": float(np.max(np.abs(difference))),
            "mean_absolute_spacing_error_in_target_gaps":
                float(np.mean(np.abs(np.diff(prediction)-np.diff(target))/np.diff(target)))}


def bounds(form):
    if form == "B":
        return LOW3.copy(), HIGH3.copy()
    return np.append(LOW3, Z_BOUNDS[form][0]), np.append(HIGH3, Z_BOUNDS[form][1])


def default_theta(form):
    return BASE.copy() if form == "B" else np.append(BASE, 0.)


def import_source():
    spec = importlib.util.spec_from_file_location("cs08_locked_cs06_math", SOURCE)
    source = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(source)
    return source


def potential(source, form, q, a, z, derivative=0):
    value = source.potential("S", q, a, derivative)
    if form in ("O", "Q") and z != 0.:
        power = 8 if form == "O" else 5
        coefficient = math.factorial(power)/math.factorial(power-derivative)
        value = value+z*coefficient*np.asarray(q)**(power-derivative)
    return value


def merge_roots(values):
    merged = []
    for value in sorted(map(float, values)):
        if not merged or value-merged[-1] > ROOT_MERGE:
            merged.append(value)
    return merged


def minimum(source, form, a, z, cache, ledger, counters, ledger_log):
    # Identity is the potential, not the kinetic form, hbar, mass, or grid.
    family = form if form in ("O", "Q") and z != 0. else "V0"
    potential_z = z if family != "V0" else 0.
    key = family, float(potential_z).hex(), float(a).hex()
    if key in cache:
        counters["minimum_cache_hits"] += 1
        return cache[key]
    counters["minimum_scalar_solves"] += 1
    derivative = lambda order, x: float(potential(source, family, x, a, potential_z, order))

    def solve(order, left, right):
        counters["brent_calls"] += 1
        root = float(brentq(lambda x: derivative(order, x), left, right,
                            xtol=ROOT_XTOL, rtol=ROOT_RTOL, maxiter=100))
        if not math.isfinite(root) or abs(derivative(order, root)) > ROOT_TOL:
            raise RuntimeError("Global-minimum root residual exceeded 1e-9")
        return root

    endpoints = {str(order): [derivative(order, -8.), derivative(order, 8.)] for order in (1, 2, 3)}
    if (not all(math.isfinite(x) for values in endpoints.values() for x in values)
            or not endpoints["1"][0] < 0 < endpoints["1"][1]
            or not endpoints["3"][0] < 0 < endpoints["3"][1] or min(endpoints["2"]) <= 0):
        raise RuntimeError("Frozen global-minimum endpoint conditions failed")
    third_root = solve(3, -8., 8.)
    second_minimum = derivative(2, third_root)
    second_roots = ([solve(2, -8., third_root), solve(2, third_root, 8.)] if second_minimum < 0
                    else [third_root] if second_minimum == 0. else [])
    divisions = merge_roots([-8., *second_roots, 8.])
    values = [derivative(1, point) for point in divisions]
    candidates = [point for point, value in zip(divisions, values) if value == 0.]
    for left, right, fl, fr in zip(divisions[:-1], divisions[1:], values[:-1], values[1:]):
        if (fl < 0 < fr) or (fr < 0 < fl):
            candidates.append(solve(1, left, right))
    roots = merge_roots(candidates)
    if not roots:
        raise RuntimeError("No stationary point in frozen isolation procedure")
    residuals = [abs(derivative(1, root)) for root in roots]
    energies = [float(potential(source, family, root, a, potential_z)) for root in roots]
    if max(residuals) > ROOT_TOL or not all(math.isfinite(x) for x in energies):
        raise RuntimeError("Invalid stationary values/residuals")
    chosen = min(range(len(roots)), key=lambda index: (energies[index], roots[index]))
    row = {"minimum_id": len(ledger), "potential_family": family, "z": float(potential_z), "a": float(a),
           "exact_key": list(key), "root_interval": [-8., 8.], "endpoint_derivatives": endpoints,
           "third_derivative_root": third_root, "third_derivative_root_residual": abs(derivative(3, third_root)),
           "second_derivative_minimum": second_minimum, "second_derivative_roots": second_roots,
           "second_derivative_root_residuals": [abs(derivative(2, root)) for root in second_roots],
           "partition_points": divisions, "first_derivative_at_partition": values,
           "roots_before_merge": sorted(candidates), "stationary_roots": roots,
           "root_residuals": residuals, "stationary_values": energies,
           "minimum": energies[chosen], "minimizer": roots[chosen],
           "tie_rule": "lowest value, then leftmost root",
           "zero_endpoint_rule": "literal floating zero; non-certified"}
    ledger.append(row)
    cache[key] = row
    ledger_log.write(json.dumps(row, allow_nan=False)+"\n")
    ledger_log.flush()
    return row


def kinetic(form, p, mass, z):
    base = p*p/(np.hypot(mass, p)+mass)
    if form in ("U", "D"):
        factor = 1+z*np.log1p((p/mass)**2)
        return base*factor if form == "U" else base/factor
    return base


def propagate(source, form, theta, n, length, count, minimum_cache, ledger, counters, ledger_log, zero=False):
    h, a_start, mass = map(float, theta[:3])
    z = float(theta[3]) if len(theta) == 4 else 0.
    q = -length+2*length*np.arange(1, n+1)/(n+1)
    p = np.pi*h*np.arange(1, n+1)/(2*length)
    k = kinetic(form, p, mass, z)
    if not np.all(np.isfinite(k)) or np.min(k) < 0:
        raise RuntimeError("Invalid kinetic dispersion")
    midpoint, schedule = source.cooling(a_start, count)
    shifted = np.zeros((count, n))
    ids, min_values, minimizers = [], [], []
    clipping_count, maximum_clip = 0, 0.
    for index, a in enumerate(schedule):
        if zero:
            continue
        row = minimum(source, form, float(a), z, minimum_cache, ledger, counters, ledger_log)
        raw = potential(source, form, q, float(a), z)-row["minimum"]
        if not np.all(np.isfinite(raw)) or np.min(raw) < -1e-10:
            raise RuntimeError("Nonfinite W or W below -1e-10")
        negative = raw < 0.
        clipping_count += int(np.count_nonzero(negative))
        if np.any(negative):
            maximum_clip = max(maximum_clip, float(np.max(-raw[negative])))
        shifted[index] = np.maximum(raw, 0.)
        ids.append(row["minimum_id"])
        min_values.append(row["minimum"])
        minimizers.append(row["minimizer"])
    delta = BETA/count
    decay = np.exp(-delta*k)
    product = np.eye(n)
    for values in shifted:
        half = np.exp(-.5*delta*values)
        transformed = fft.dst(half[:, None]*product, type=1, axis=0, norm="ortho", workers=1)
        drifted = fft.dst(decay[:, None]*transformed, type=1, axis=0, norm="ortho", workers=1)
        product = half[:, None]*drifted
    if not np.all(np.isfinite(product)):
        raise RuntimeError("Nonfinite chronological heat matrix")
    arrays = {"theta": np.asarray(theta).copy(), "form_key": np.array(form), "grid_n": np.array(n),
              "L": np.array(length), "sample_count": np.array(count), "beta": np.array(BETA),
              "q": q, "p": p, "kinetic_minus_mass": k, "midpoint_u": midpoint, "schedule": schedule,
              "W_samples": shifted, "mean_W": np.mean(shifted, axis=0), "C_tilde": product,
              "minimum_ids": np.array(ids, dtype=np.int64), "minimum_values": np.array(min_values),
              "minimizers": np.array(minimizers), "potential_mode": np.array("zero_control" if zero else "global_minimum_shift")}
    record = {"form": FORMS[form], "form_key": form, "theta": list(map(float, theta)),
              "N": n, "L": length, "B": count, "beta": BETA, "delta": delta,
              "potential_clipped_count": clipping_count, "potential_maximum_clip": maximum_clip,
              "minimum_ids": ids, "first_midpoint_a": float(schedule[0]), "last_midpoint_a": float(schedule[-1]),
              "spatial_step": 2*length/(n+1), "p_max": float(p[-1])}
    return arrays, record


def readout(sigma, mass, beta, target, count=320):
    mask = np.isfinite(sigma) & (sigma > 0)
    energy = np.full(sigma.shape, np.nan)
    energy[mask] = mass-np.log(sigma[mask])/beta
    mask &= np.isfinite(energy)
    reasons = []
    if not (math.isfinite(float(sigma[0])) and 0 < sigma[0] <= 1+1e-10):
        reasons.append("SIGMA0_OUT_OF_CONTRACTION_RANGE")
    if len(sigma) < count or not np.all(mask[:count]):
        reasons.append("UNRESOLVED_REQUIRED_SINGULAR_VALUES")
    if not np.all(np.diff(sigma[:count]) <= 0):
        reasons.append("REQUIRED_SINGULAR_VALUES_NOT_ORDERED")
    ratio = float(sigma[count-1]/sigma[0]) if len(sigma) >= count and sigma[0] > 0 else float("nan")
    if not math.isfinite(ratio) or ratio < 1e-10:
        reasons.append("REQUIRED_RELATIVE_SINGULAR_VALUE_BELOW_1E-10")
    if not (math.isfinite(float(energy[0])) and energy[0] > 0):
        reasons.append("NONPOSITIVE_OR_NONFINITE_E0")
    if not np.all(np.isfinite(energy[:count])) or not np.all(energy[:count] >= mass-1e-8):
        reasons.append("REQUIRED_ENERGY_BELOW_REST_MASS_TOLERANCE_OR_NONFINITE")
    scale = float(target[0]/energy[0]) if np.isfinite(energy[0]) and energy[0] > 0 else float("nan")
    prediction = scale*energy[:count] if math.isfinite(scale) else np.full(count, np.nan)
    arrays = {"sigma": sigma.copy(), "energy": energy, "energy_resolved_mask": mask,
              "scale": np.array(scale), "predicted_320" if count == 320 else "predicted_control": prediction,
              "target_100": target.copy(), "resolution_valid": np.array(not reasons),
              "invalid_reasons": np.array(reasons, dtype=str)}
    record = {"status": "VALID" if not reasons else "INVALID_RESOLUTION", "resolution_valid": not reasons,
              "invalid_reasons": reasons, "required_count": count, "sigma0": nullable(sigma[0]),
              "required_last_sigma": nullable(sigma[count-1]), "required_sigma_ratio": nullable(ratio),
              "E0": nullable(energy[0]), "scale": nullable(scale),
              "resolved_energy_count": int(np.count_nonzero(mask))}
    return arrays, record


def occupation(states, q, length):
    n, retained = states.shape
    boundary = np.sum(states[np.abs(q) > .9*length]**2, axis=0)
    transformed = fft.dst(states, type=1, axis=0, norm="ortho", workers=1)
    tail_count = (n+4)//5
    tail = np.sum(transformed[-tail_count:]**2, axis=0)
    summary = {"highest_mode_count": tail_count, "rounding": "ceil(N/5)", "boundary": "abs(q)>0.9L", "windows": {}}
    for count in (100, 320):
        if count <= retained:
            summary["windows"][str(count)] = {"boundary_max": float(np.max(boundary[:count])),
                                              "boundary_mean": float(np.mean(boundary[:count])),
                                              "momentum_max": float(np.max(tail[:count])),
                                              "momentum_mean": float(np.mean(tail[:count]))}
    return boundary, tail, summary


def add_states(arrays, left_all, right_t_all, record):
    left, right = left_all[:, :320].copy(), right_t_all[:320].T.copy()
    product, sigma = arrays["C_tilde"], arrays["sigma"]
    forward = np.linalg.norm(product@right-left*sigma[:320], axis=0)
    transpose = np.linalg.norm(product.T@left-right*sigma[:320], axis=0)
    denominator = float(sigma[0])
    forward_relative = forward/denominator if denominator > 0 and math.isfinite(denominator) else np.full(320, np.nan)
    transpose_relative = transpose/denominator if denominator > 0 and math.isfinite(denominator) else np.full(320, np.nan)
    lb, lt, ls = occupation(left, arrays["q"], float(arrays["L"]))
    rb, rt, rs = occupation(right, arrays["q"], float(arrays["L"]))
    fro = float(np.sum(product*product))
    moment = float(np.sum(sigma*sigma))
    arrays.update(singular_left=left, singular_right=right, singular_forward_residual=forward,
                  singular_transpose_residual=transpose, singular_forward_residual_over_sigma0=forward_relative,
                  singular_transpose_residual_over_sigma0=transpose_relative,
                  left_boundary_mass=lb, left_high_momentum_mass=lt, right_boundary_mass=rb, right_high_momentum_mass=rt)
    record.update(retained_singular_states=320, sigma_used_for_state_residual="original score sigma",
                  singular_forward_residual_max=nullable(np.max(forward)),
                  singular_transpose_residual_max=nullable(np.max(transpose)),
                  singular_forward_relative_max=nullable(np.max(forward_relative)),
                  singular_transpose_relative_max=nullable(np.max(transpose_relative)),
                  left_orthogonality_fro=float(np.linalg.norm(left.T@left-np.eye(320))),
                  right_orthogonality_fro=float(np.linalg.norm(right.T@right-np.eye(320))),
                  left_occupation=ls, right_occupation=rs, matrix_frobenius_squared=fro,
                  full_sigma_squared_sum=moment, frobenius_moment_relative_difference=nullable(abs(fro-moment)/fro) if fro > 0 else None,
                  partial_states_are_not_full_reconstruction=True)


def forward(source, form, theta, target, n, length, count, minimum_cache, ledger, counters, ledger_log, states=False, zero=False):
    arrays, record = propagate(source, form, theta, n, length, count, minimum_cache, ledger, counters, ledger_log, zero)
    if states:
        counters["post_full_svd_calls"] += 1
        left, sigma, right_t = np.linalg.svd(arrays["C_tilde"], full_matrices=True)
    else:
        counters["control_svd_calls" if zero else "training_score_svd_calls"] += 1
        sigma = np.linalg.svd(arrays["C_tilde"], compute_uv=False)
    readout_arrays, validity = readout(sigma, float(theta[2]), BETA, target, 63 if zero else 320)
    arrays.update(readout_arrays)
    record.update(validity)
    if not zero:
        record["training_metrics"] = metrics(arrays["predicted_320"][:100], target) if validity["resolution_valid"] else None
    if states:
        add_states(arrays, left, right_t, record)
    return arrays, record


def rank(record):
    if not record["resolution_valid"]:
        raise ValueError("Invalid member cannot enter winner ranking")
    return (record["joint_score"], record["max_mape_percent"], record["max_percent_error"],
            record["cross_grid_percent"], record["evaluation_id"])


def pair_summary(grids, arrays, target):
    if not all(grids[str(n)]["resolution_valid"] for n in TRAIN_N):
        return {"status": "INVALID_RESOLUTION", "resolution_valid": False, "joint_score": PENALTY,
                "max_mape_percent": None, "max_percent_error": None, "cross_grid_percent": None}
    m = [grids[str(n)]["training_metrics"]["mape_percent"] for n in TRAIN_N]
    w = [grids[str(n)]["training_metrics"]["max_percent_error"] for n in TRAIN_N]
    gap = float(100*np.max(np.abs(arrays[511]["predicted_320"][:100]-arrays[639]["predicted_320"][:100])/target))
    return {"status": "VALID", "resolution_valid": True, "joint_score": max(m[0]/M_REF, m[1]/M_REF, w[0]/W_REF, w[1]/W_REF, gap/G_REF),
            "max_mape_percent": max(m), "max_percent_error": max(w), "cross_grid_percent": gap}


def static_readout(arrays, target, counters):
    n = int(arrays["grid_n"])
    modes = fft.dst(np.eye(n), type=1, axis=0, norm="ortho", workers=1)
    matrix = fft.dst(arrays["kinetic_minus_mass"][:, None]*modes, type=1, axis=0, norm="ortho", workers=1)
    del modes
    matrix.flat[::n+1] += float(arrays["theta"][2])+arrays["mean_W"]
    counters["static_eigh_calls"] += 1
    if counters["static_eigh_calls"] > 22:
        raise RuntimeError("Static readout budget exceeded")
    values, states_all = np.linalg.eigh(matrix, UPLO="L")
    if not np.all(np.isfinite(values)) or values[0] <= 0:
        raise RuntimeError("Invalid same-parameter static spectrum")
    states = states_all[:, :320].copy()
    del states_all
    residual = np.linalg.norm(matrix@states-states*values[:320], axis=0)
    scale = float(target[0]/values[0])
    prediction = scale*values[:320]
    boundary, tail, summary = occupation(states, arrays["q"], float(arrays["L"]))
    result = {key: arrays[key] for key in ("theta", "form_key", "grid_n", "L", "sample_count", "q", "p",
                                          "kinetic_minus_mass", "mean_W", "schedule", "minimum_ids", "target_100")}
    result.update(H_avg=matrix, energy=values, states=states, equation_residual=residual,
                  scale=np.array(scale), predicted_320=prediction, boundary_mass=boundary, high_momentum_mass=tail)
    record = {"N": n, "L": float(arrays["L"]), "B": int(arrays["sample_count"]),
              "theta": arrays["theta"].tolist(), "E0": float(values[0]), "scale": scale,
              "equation_residual_max": float(np.max(residual)),
              "symmetry_relative_fro": float(np.linalg.norm(matrix-matrix.T)/np.linalg.norm(matrix)),
              "orthogonality_fro": float(np.linalg.norm(states.T@states-np.eye(320))),
              "occupation": summary, "training_metrics": metrics(prediction[:100], target),
              "not_separately_optimized": True, "no_selection": True}
    return result, record


def compact(arrays, valid=True):
    return {"prediction": arrays["predicted_320"].copy(), "energy": arrays["energy"][:320].copy(),
            "scale": float(arrays["scale"]), "valid": bool(valid),
            "invalid_reasons": arrays["invalid_reasons"].tolist() if "invalid_reasons" in arrays else []}


def compare(left_id, right_id, members, truth):
    left, right = members[left_id], members[right_id]
    valid = left["valid"] and right["valid"]
    result = {"left": left_id, "right": right_id, "status": "VALID" if valid else "UNASSESSABLE_INVALID_RESOLUTION",
              "left_invalid_reasons": left["invalid_reasons"], "right_invalid_reasons": right["invalid_reasons"],
              "left_E0": nullable(left["energy"][0]), "right_E0": nullable(right["energy"][0]),
              "left_scale": nullable(left["scale"]), "right_scale": nullable(right["scale"]),
              "raw_energy_denominator": "first/left object", "windows": None}
    if valid:
        result["windows"] = {}
        for name, (start, stop) in WINDOWS.items():
            g = float(100*np.max(np.abs(left["prediction"][start:stop]-right["prediction"][start:stop])/truth[start:stop]))
            raw = float(100*np.max(np.abs(left["energy"][start:stop]-right["energy"][start:stop])/left["energy"][start:stop]))
            result["windows"][name] = {"G_percent": g, "G_below_2_percent": g < G_REF,
                                        "raw_energy_max_relative_percent": raw}
    return result


def main():
    started = time.perf_counter()
    locks = json.loads(LOCK_FILE.read_text())
    for path, wanted in locks.items():
        if sha(ROOT/path) != wanted:
            raise RuntimeError(f"Input hash mismatch: {path}")
    if OUT.exists():
        raise RuntimeError("Output exists; refusing overwrite or retry")
    OUT.mkdir(parents=True)
    (OUT/"evaluations").mkdir()
    event_log = (OUT/"events.jsonl").open("x", encoding="utf-8")
    ledger_log = (OUT/"minimum-ledger.jsonl").open("x", encoding="utf-8")
    call_log = (OUT/"calls.jsonl").open("x", encoding="utf-8")
    log_lock, monitor_stop = threading.Lock(), threading.Event()
    counters = {"training_propagations": 0, "control_propagations": 0, "postfreeze_propagations": 0,
                "training_score_svd_calls": 0, "control_svd_calls": 0, "post_full_svd_calls": 0,
                "winner_extra_svd_calls": 0, "static_eigh_calls": 0,
                "minimum_scalar_solves": 0, "minimum_cache_hits": 0, "brent_calls": 0}

    def event(name, **fields):
        with log_lock:
            line = json.dumps({"utc": utc(), "event": name, **fields}, allow_nan=False)
            event_log.write(line+"\n")
            event_log.flush()
            print(line, flush=True)

    def output_size():
        return sum(path.stat().st_size for path in OUT.rglob("*") if path.is_file())

    def output_guard():
        if output_size() > GIB:
            raise RuntimeError("Frozen 1 GiB output budget exceeded; no retry")

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
                    "forms": FORMS, "train_N": TRAIN_N, "post_N": POST_N, "beta": BETA,
                    "L": LENGTH, "B": SAMPLE_COUNT, "M_ref": M_REF, "W_ref": W_REF, "G_ref_percent": G_REF,
                    "source_functions_reused": ["potential('S', derivative)", "cooling"],
                    "source_globals_mutated": False, "root_isolation_certified": False,
                    "seed_rng": 20260925, "seed_calls_per_form": 9, "nm_maxfev_per_form": 24,
                    "max_pair_calls": 165, "max_propagations": 345, "max_extra_svd": 10, "max_static_eigh": 22,
                    "training_cache": "same form and exact physical theta only; no cross-form spectra",
                    "nonwinner_training_C_saved": False,
                    "reconstruction_limit": "Nonwinner C must be reconstructed from frozen code/inputs; saved compact spectra are not a rerun.",
                    "no_valid_seed_policy": "skip this form's NM; no fallback or budget redistribution",
                    "development_policy": "all 101-320 previously observed; evaluate only after full training-winner arrays frozen",
                    "high_momentum_mode_count": "ceil(N/5)", "run_passport": "UNVERIFIED",
                    "output_budget_bytes": GIB, "memory_advisory_bytes": GIB,
                    "timeout_seconds": 600, "actual_process_exit_code": "collected by launching parent"}
        write_json(OUT/"manifest.json", manifest)
        event("started", pid=os.getpid(), scope_id=SCOPE)
        source = import_source()
        with np.load(TARGET_SOURCE, allow_pickle=False) as old:
            target = old["target_100"].copy()
        if len(target) != 100 or not np.all(np.isfinite(target)) or target[0] <= 0 or not np.all(np.diff(target) > 0):
            raise RuntimeError("Invalid frozen training target")
        reference_metrics = json.loads((OLD257/"CS07-A1-N1023.json").read_text())["metrics"]["1-100"]
        if (abs(reference_metrics["mape_percent"]-M_REF) > 1e-12
                or abs(reference_metrics["max_percent_error"]-W_REF) > 1e-12):
            raise RuntimeError("Same-object benchmark constants mismatch")
        old_regression = {}
        for n, path in ((511, OLD256/"winner-S-N511.npz"), (639, OLD256/"post-space-N639.npz")):
            with np.load(path, allow_pickle=False) as old:
                if not np.array_equal(old["theta"], BASE) or not np.array_equal(old["target_100"], target):
                    raise RuntimeError("Regression theta/target mismatch")
                old_regression[n] = old["predicted_320"].copy()
        minimum_cache, minimum_ledger = {}, []
        controls = {}
        for form in ("B", "U", "D"):
            theta = BASE.copy() if form == "B" else np.append(BASE, .25)
            counters["control_propagations"] += 1
            event("propagation_start", stage="control", form=form, N=63, counters=dict(counters))
            arrays, record = forward(source, form, theta, target, 63, LENGTH, SAMPLE_COUNT,
                                     minimum_cache, minimum_ledger, counters, ledger_log, zero=True)
            expected_sigma = np.sort(np.exp(-BETA*arrays["kinetic_minus_mass"]))[::-1]
            expected_energy = np.sort(theta[2]+arrays["kinetic_minus_mass"])
            sigma_error = float(np.max(np.abs(arrays["sigma"]-expected_sigma)))
            energy_error = float(np.max(np.abs(arrays["energy"]-expected_energy)))
            record["analytic_control"] = {"sigma_max_absolute_difference": sigma_error,
                                           "energy_max_absolute_difference": energy_error,
                                           "passed": bool(record["resolution_valid"] and sigma_error <= 1e-10 and energy_error <= 1e-8),
                                           "sigma_tolerance": 1e-10, "energy_tolerance": 1e-8,
                                           "analytic_sorting": "sigma descending; absolute energy ascending"}
            arrays.update(expected_sigma=expected_sigma, expected_energy=expected_energy)
            write_npz(OUT/f"control-{form}.npz", arrays)
            write_json(OUT/f"control-{form}.json", record)
            controls[form] = record
            del arrays
            event("propagation_complete", stage="control", form=form, result=record["analytic_control"], counters=dict(counters))
            if not record["analytic_control"]["passed"]:
                raise RuntimeError("Analytic control failed; no retry")
        cache, best, seed_physical = {}, {}, {}
        call_rows, unique_rows = [], []
        calls, unique, regression = 0, 0, None

        def objective(form, x, stage, physical=None):
            nonlocal calls, unique, regression
            calls += 1
            lower, upper = bounds(form)
            x = np.asarray(x)
            seed_key = form, *(float(value).hex() for value in x)
            if physical is not None:
                theta = np.asarray(physical).copy()
                seed_physical[seed_key] = theta.copy()
            else:
                theta = seed_physical[seed_key].copy() if seed_key in seed_physical else lower+x*(upper-lower)
            if calls > 165 or not np.all(np.isfinite(theta)) or np.any(theta < lower) or np.any(theta > upper):
                raise RuntimeError("Frozen objective budget or bounds violated")
            key = form, *(float(value).hex() for value in theta)
            if key in cache:
                record = dict(cache[key])
                record.update(call=calls, stage=stage, cached=True, source_evaluation_id=record["evaluation_id"])
                call_rows.append(record)
                call_log.write(json.dumps(record, allow_nan=False)+"\n")
                call_log.flush()
                event("cached_pair_call", call=calls, form=form, source_evaluation_id=record["evaluation_id"], joint_score=record["joint_score"])
                return record["joint_score"]
            unique += 1
            eid = f"{FORMS[form]}-{unique:04d}"
            pair_arrays, grids = {}, {}
            tick = time.perf_counter()
            event("pair_start", evaluation_id=eid, call=calls, form=form, theta=theta.tolist(), stage=stage)
            for n in TRAIN_N:
                if counters["training_propagations"] >= 330:
                    raise RuntimeError("Training propagation budget exceeded")
                counters["training_propagations"] += 1
                grid_tick = time.perf_counter()
                arrays, grid = forward(source, form, theta, target, n, LENGTH, SAMPLE_COUNT,
                                       minimum_cache, minimum_ledger, counters, ledger_log)
                grid["seconds_before_save"] = time.perf_counter()-grid_tick
                arrays["evaluation_id"] = np.array(eid)
                write_npz(OUT/"evaluations"/f"{eid}-N{n}.npz", {name: value for name, value in arrays.items() if name != "C_tilde"})
                grid.update(C_saved=False, reconstruction_source="frozen script, theta, grid and minimum ledger")
                write_json(OUT/"evaluations"/f"{eid}-N{n}.json", grid)
                pair_arrays[n], grids[str(n)] = arrays, grid
                event("training_grid_complete", evaluation_id=eid, N=n, status=grid["status"],
                      metrics=grid["training_metrics"], counters=dict(counters))
            record = {"evaluation_id": eid, "form_key": form, "form": FORMS[form], "theta": theta.tolist(),
                      "normalized_x": x.tolist(), "call": calls, "stage": stage, "cached": False,
                      "grids": grids, "seconds_including_save": time.perf_counter()-tick,
                      **pair_summary(grids, pair_arrays, target)}
            record["J_minus_1"] = record["joint_score"]-1 if record["resolution_valid"] else None
            record["benchmark_differences"] = ({str(n): {
                "M_minus_M_ref_percentage_points": grids[str(n)]["training_metrics"]["mape_percent"]-M_REF,
                "W_minus_W_ref_percentage_points": grids[str(n)]["training_metrics"]["max_percent_error"]-W_REF}
                for n in TRAIN_N} if record["resolution_valid"] else None)
            write_json(OUT/"evaluations"/f"{eid}.json", record)
            cache[key] = record
            call_rows.append(record)
            unique_rows.append(record)
            call_log.write(json.dumps(record, allow_nan=False)+"\n")
            call_log.flush()
            if record["resolution_valid"] and (form not in best or rank(record) < rank(best[form][1])):
                best[form] = (pair_arrays, record)
            if calls == 1:
                if form != "B" or not np.array_equal(theta, BASE):
                    raise RuntimeError("First objective is not the frozen common B default")
                regression = {}
                for n in TRAIN_N:
                    predicted = pair_arrays[n]["predicted_320"]
                    old_metrics = metrics(old_regression[n][:100], target)
                    new_metrics = metrics(predicted[:100], target)
                    prediction_error = float(np.max(np.abs(predicted-old_regression[n])))
                    metric_error = max(abs(new_metrics[name]-old_metrics[name]) for name in ("mape_percent", "max_percent_error"))
                    regression[str(n)] = {"prediction_320_max_absolute_difference": prediction_error,
                                           "first100_MW_max_absolute_difference": metric_error,
                                           "tolerance": 1e-6, "passed": bool(record["resolution_valid"] and prediction_error <= 1e-6 and metric_error <= 1e-6)}
                write_json(OUT/"default-regression.json", regression)
                if not all(row["passed"] for row in regression.values()):
                    raise RuntimeError("Common-default double-grid regression failed; no retry")
            event("pair_complete", evaluation_id=eid, status=record["status"], joint_score=record["joint_score"],
                  max_mape_percent=record["max_mape_percent"], max_percent_error=record["max_percent_error"], cross_grid_percent=record["cross_grid_percent"])
            output_guard()
            return record["joint_score"]

        wide = np.random.default_rng(20260925).uniform(0, 1, (4, 4))
        seeds = {}
        for form in FORMS:
            lower, upper = bounds(form)
            points = [default_theta(form)]
            if form == "B":
                for coordinate, value in ((0, .12), (0, .22), (2, .30), (2, .90)):
                    point = BASE.copy()
                    point[coordinate] = value
                    points.append(point)
            else:
                points.extend(np.append(BASE, value) for value in STRUCTURE_SEEDS[form])
            points.extend(lower+row[:len(lower)]*(upper-lower) for row in wide)
            seeds[form] = points
        write_json(OUT/"seed-design.json", {"rng_seed": 20260925, "wide_normalized_4x4": wide.tolist(),
                                          "physical_points": {form: [point.tolist() for point in points] for form, points in seeds.items()}})
        for index in range(9):
            for form in FORMS:
                lower, upper = bounds(form)
                theta = seeds[form][index]
                objective(form, (theta-lower)/(upper-lower), f"seed-{index:02d}", physical=theta)
        optimizers = {}
        for form in FORMS:
            if form not in best:
                optimizers[form] = {"status": "SKIPPED_NO_VALID_SEED", "nfev": 0, "no_budget_transfer": True}
                event("optimizer_skipped", form=form, reason="NO_VALID_SEED")
                continue
            x0 = np.array(best[form][1]["normalized_x"])
            simplex = np.repeat(x0[None, :], len(x0)+1, axis=0)
            for coordinate in range(len(x0)):
                simplex[coordinate+1, coordinate] += .06 if x0[coordinate] <= .94 else -.06
            event("optimizer_start", form=form, seed_evaluation_id=best[form][1]["evaluation_id"], maxfev=24)
            optimized = minimize(lambda x: objective(form, x, "refine"), x0, method="Nelder-Mead",
                                 bounds=[(0., 1.)]*len(x0), options={"maxfev": 24, "initial_simplex": simplex,
                                 "xatol": 1e-6, "fatol": 1e-6, "adaptive": False})
            optimizers[form] = {"success": bool(optimized.success), "message": str(optimized.message),
                                "nfev": int(optimized.nfev), "nit": int(optimized.nit), "fun": float(optimized.fun)}
            event("optimizer_complete", form=form, optimizer=optimizers[form])
        primary = min(best, key=lambda form: rank(best[form][1])) if best else None
        roles = {form: record for form, (arrays, record) in best.items()}
        role_status = {form: "VALID_MEMBER" if form in best else "NO_VALID_MEMBER" for form in FORMS}
        frozen = {"scope_id": SCOPE, "frozen_utc": utc(), "roles": roles, "role_status": role_status,
                  "global_joint_winner": primary, "calls": calls, "unique_members": unique,
                  "optimizers": optimizers, "selection": "joint first100 paired N511/N639 only",
                  "development_metrics_evaluated": False, "full_array_freeze_follows": True}
        write_json(OUT/"winners-frozen.json", frozen)
        write_json(OUT/"calls.json", call_rows)
        write_json(OUT/"unique-members.json", unique_rows)
        event("winner_identities_frozen", sha256=sha(OUT/"winners-frozen.json"), primary=primary, role_status=role_status)
        members, member_metadata, state_records, static_records, frozen_files = {}, {}, {}, {}, []

        def save_full(name, arrays, record, stage):
            members[name] = compact(arrays, record["resolution_valid"])
            member_metadata[name] = {"kind": "heat", "stage": stage, "form": record["form_key"],
                                      "N": int(arrays["grid_n"]), "L": float(arrays["L"]), "B": int(arrays["sample_count"])}
            write_npz(OUT/f"{name}.npz", arrays)
            write_json(OUT/f"{name}.json", record)
            static_arrays, static_record = static_readout(arrays, target, counters)
            static_name = "static-"+name
            static_record.update(heat_owner=name, form_key=record["form_key"])
            members[static_name] = compact(static_arrays)
            member_metadata[static_name] = {**member_metadata[name], "kind": "static"}
            static_records[static_name] = static_record
            write_npz(OUT/f"{static_name}.npz", static_arrays)
            write_json(OUT/f"{static_name}.json", static_record)
            del static_arrays
            output_guard()
            return [f"{name}.npz", f"{name}.json", f"{static_name}.npz", f"{static_name}.json"]

        for form in FORMS:
            if form not in best:
                continue
            pair_arrays, record = best[form]
            for n in TRAIN_N:
                arrays = pair_arrays.pop(n)
                name = f"winner-{form}-N{n}"
                state_record = dict(record["grids"][str(n)])
                state_record.update(evaluation_id=record["evaluation_id"], C_saved=True, original_ranking_arrays_preserved=True)
                counters["winner_extra_svd_calls"] += 1
                if counters["winner_extra_svd_calls"] > 10:
                    raise RuntimeError("Extra winner SVD budget exceeded")
                event("winner_state_readout_start", name=name, not_a_propagation=True)
                left, repeated_sigma, right_t = np.linalg.svd(arrays["C_tilde"], full_matrices=True)
                difference = float(np.max(np.abs(repeated_sigma-arrays["sigma"])))
                if not math.isfinite(difference) or difference > 1e-12:
                    raise RuntimeError("Winner full SVD differs from original ranking spectrum")
                arrays["svd_sigma_recomputed"] = repeated_sigma
                add_states(arrays, left, right_t, state_record)
                del left, right_t
                state_record["repeat_svd_sigma_max_difference"] = difference
                state_records[name] = state_record
                frozen_files.extend(save_full(name, arrays, state_record, "training-winner"))
                del arrays
                gc.collect()
                event("winner_state_readout_complete", name=name, counters=dict(counters))
        best.clear()
        full_freeze = {"scope_id": SCOPE, "frozen_utc": utc(), "role_status": role_status,
                       "full_heat_arrays": 2*len(roles), "static_arrays": 2*len(roles),
                       "files_sha256": {name: sha(OUT/name) for name in frozen_files},
                       "development_metrics_evaluated": False, "counters": dict(counters)}
        write_json(OUT/"training-arrays-frozen.json", full_freeze)
        event("training_arrays_frozen", sha256=sha(OUT/"training-arrays-frozen.json"), counters=dict(counters))
        event("development_reference_read_start", no_further_selection=True, all_previously_observed=True)
        portions = []
        for path, count in REFERENCES:
            values = np.array([float(value) for value in json.loads(path.read_text())["ordinates"]])
            if len(values) != count:
                raise RuntimeError("Known development reference length mismatch")
            portions.append(values)
        truth = np.concatenate([target, *portions])
        if len(truth) != 320 or not np.all(np.isfinite(truth)) or not np.all(np.diff(truth) > 0):
            raise RuntimeError("Invalid known development target ledger")
        with np.load(OLD257/"CS07-A3-N1535.npz", allow_pickle=False) as old:
            if not np.array_equal(old["theta"], BASE) or not np.array_equal(old["target_320"], truth):
                raise RuntimeError("Old stable diagnostic benchmark identity/target mismatch")
            members["old-S0047-N1535"] = {"prediction": old["predicted"].copy(), "energy": old["energy"][:320].copy(),
                                          "scale": float(old["scale"]), "valid": bool(old["resolution_valid"]),
                                          "invalid_reasons": old["invalid_reasons"].tolist()}
            member_metadata["old-S0047-N1535"] = {"kind": "reused", "stage": "old-fixed-benchmark", "form": "S0047", "N": 1535, "L": 8., "B": 64}
        write_json(OUT/"known-targets.json", {"first": 1, "last": 320, "ordinates": truth.tolist(),
                                            "previously_observed": True, "generated_by_this_run": False})
        post_records = {}

        def post(form, n, length, count, name):
            counters["postfreeze_propagations"] += 1
            if counters["postfreeze_propagations"] > 12:
                raise RuntimeError("Postfreeze propagation budget exceeded")
            theta = np.array(roles[form]["theta"])
            event("propagation_start", stage="postfreeze", name=name, form=form, theta=theta.tolist(), N=n, L=length, B=count, counters=dict(counters))
            tick = time.perf_counter()
            arrays, record = forward(source, form, theta, target, n, length, count,
                                     minimum_cache, minimum_ledger, counters, ledger_log, states=True)
            record.update(no_selection=True, source_evaluation_id=roles[form]["evaluation_id"], seconds_before_save=time.perf_counter()-tick)
            save_full(name, arrays, record, "postfreeze")
            post_records[name] = record
            del arrays
            gc.collect()
            event("propagation_complete", stage="postfreeze", name=name, status=record["status"], counters=dict(counters))

        for form in FORMS:
            if form in roles:
                for n in POST_N:
                    post(form, n, LENGTH, SAMPLE_COUNT, f"post-{form}-N{n}")
        if primary is not None:
            post(primary, 1279, LENGTH, 128, "primary-time-N1279-B128")
            post(primary, 1599, 10., SAMPLE_COUNT, "primary-box-N1599-L10")
        fits = {name: ({window: metrics(member["prediction"][start:stop], truth[start:stop])
                        for window, (start, stop) in WINDOWS.items()} if member["valid"] else None)
                for name, member in members.items()}
        comparisons = {}
        for form in roles:
            for label, left, right in (("train-grid", f"winner-{form}-N511", f"winner-{form}-N639"),
                                       ("N639-N1023", f"winner-{form}-N639", f"post-{form}-N1023"),
                                       ("N1023-N1279", f"post-{form}-N1023", f"post-{form}-N1279"),
                                       ("old-baseline-N1279", "old-S0047-N1535", f"post-{form}-N1279")):
                comparisons[f"{form}-{label}"] = compare(left, right, members, truth)
        for name in list(members):
            if "static-"+name in members:
                comparisons["static-"+name] = compare(name, "static-"+name, members, truth)
        if primary is not None:
            for label in ("primary-time-N1279-B128", "primary-box-N1599-L10"):
                comparisons[label] = compare(f"post-{primary}-N1279", label, members, truth)
        structure_comparisons = {}
        for form in ("O", "Q", "U", "D"):
            if form not in roles:
                structure_comparisons[form] = {"status": "NO_VALID_MEMBER"}
                continue
            row = roles[form]
            structure_comparisons[form] = {"z": row["theta"][3], "z_nonzero": row["theta"][3] != 0.,
                "joint_score": row["joint_score"], "J_below_1": row["joint_score"] < 1,
                "B_joint_score": roles["B"]["joint_score"] if "B" in roles else None,
                "J_strictly_better_than_B": row["joint_score"] < roles["B"]["joint_score"] if "B" in roles else None,
                "not_a_structure_gain_if_z_zero": True}
        with (OUT/"points.csv").open("x", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle)
            writer.writerow(["object_id", "kind", "stage", "form", "N", "L", "B", "resolution_valid",
                             "index", "window", "target", "predicted", "energy", "residual", "percent_error"])
            for name, member in members.items():
                meta = member_metadata[name]
                for index, (actual, predicted, energy) in enumerate(zip(truth, member["prediction"], member["energy"]), 1):
                    window = "1-100" if index <= 100 else "101-300" if index <= 300 else "301-320"
                    writer.writerow([name, meta["kind"], meta["stage"], meta["form"], meta["N"], meta["L"], meta["B"],
                                     member["valid"], index, window, actual, predicted, energy, predicted-actual, 100*abs(predicted-actual)/actual])
        write_json(OUT/"development-fit-metrics.json", fits)
        write_json(OUT/"comparisons.json", comparisons)
        write_json(OUT/"minimum-ledger.json", minimum_ledger)
        report = {"scope_id": SCOPE, "status": "completed" if len(roles) == len(FORMS) else "completed_with_missing_roles",
                  "run_passport": "UNVERIFIED", "global_joint_winner": primary, "roles": roles, "role_status": role_status,
                  "controls": controls, "default_regression": regression, "optimizers": optimizers,
                  "calls": calls, "cached_calls": sum(row["cached"] for row in call_rows), "unique_members": unique,
                  "invalid_unique_members": sum(not row["resolution_valid"] for row in unique_rows),
                  "winner_state_readouts": state_records, "static_readouts": static_records, "postfreeze": post_records,
                  "fit_metrics": fits, "comparisons": comparisons, "structure_vs_B": structure_comparisons,
                  "counters": dict(counters), "total_propagations": sum(counters[key] for key in
                      ("training_propagations", "control_propagations", "postfreeze_propagations")),
                  "seconds_before_final_serialization": time.perf_counter()-started,
                  "maxrss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                  "completed_utc": utc(), "all_inputs_unchanged": all(sha(ROOT/path) == wanted for path, wanted in locks.items()),
                  "output_bytes_before_result": output_size(), "new_targets_generated": False,
                  "formal_route": "UNASSIGNED; B NOT INVOKED"}
        write_json(OUT/"result.json", report)
        output_guard()
        monitor_stop.set()
        monitor.join(timeout=1)
        event("completed", primary=primary, seconds=report["seconds_before_final_serialization"],
              calls=calls, counters=dict(counters), output_bytes=output_size())
        write_json(OUT/"file-inventory.json", {str(path.relative_to(OUT)): path.stat().st_size
                                              for path in sorted(OUT.rglob("*")) if path.is_file()})
    except Exception as exc:
        event("failed", type=type(exc).__name__, message=str(exc), counters=dict(counters))
        raise
    finally:
        monitor_stop.set()
        monitor.join(timeout=1)
        ledger_log.close()
        call_log.close()
        event_log.close()


if __name__ == "__main__":
    main()
