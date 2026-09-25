#!/usr/bin/env python3
"""CS06: frozen chronological heat products; run once, no numerical retry."""
import csv
from datetime import datetime, timezone
import hashlib
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
OLD253 = ROOT / "papers/253-structural-homotopy-search/evidence/run-1"
TARGET_SOURCE = OLD253 / "evaluations/CS03-Q-QUARTIC-0103.npz"
MEAN_SOURCE = OLD253 / "winner-S.npz"
DEVELOPMENT_SOURCES = (
    ROOT / "papers/251-constructive-fit-portfolio/evidence/run-1/reference-101-150.json",
    OLD253 / "reference-151-200.json",
    ROOT / "papers/254-global-forms-joint-fit/evidence/run-1/reference-201-240.json",
    ROOT / "papers/255-path-operator-multigrid/evidence/run-1/reference-241-300.json",
)
FORM_IDS = {"Q": "CS06-Q-NONREL-HEAT", "R": "CS06-R-REL-HEAT",
            "S": "CS06-S-SEXTIC-HEAT", "E": "CS06-E-COSH-HEAT"}
LOW = np.array([.03, 1.10, .2])
HIGH = np.array([.20, 1.80, 3.])
DEFAULT = np.array([.1, 1.50, 1.])
TRAIN_GRIDS = (383, 511)
BETA, L, STEPS, A_END = .02, 8., 64, 1.02
M_REF, W_REF, G_REF, PENALTY = 2.2717925657954106, 14.105396903565387, 2., 1e30
POST_VARIANTS = (("space-N639", 639, 8., 64), ("space-N767", 767, 8., 64),
                 ("time-S128", 511, 8., 128), ("box-L10-N639", 639, 10., 64))
ROOT_XTOL, ROOT_RTOL, ROOT_RESIDUAL, ROOT_MERGE = 1e-13, 4 * np.finfo(float).eps, 1e-9, 1e-10
TAYLOR_TERMS = {d: tuple((2 * k - d, 1. / math.factorial(2 * k - d)) for k in range(3, 15))
                for d in range(4)}
COMMAND = ("OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 "
           "PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 600s python -u "
           "papers/256-chronological-heat-spectrum/run_search.py")


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
    relative = np.abs(difference) / target
    return {"count": len(target), "mape_percent": float(100 * np.mean(relative)),
            "mse": float(np.mean(difference**2)),
            "max_absolute_error": float(np.max(np.abs(difference))),
            "max_percent_error": float(100 * np.max(relative)),
            "mean_absolute_spacing_error_in_target_gaps":
                float(np.mean(np.abs(np.diff(prediction) - np.diff(target)) / np.diff(target)))}


def r6(q, derivative=0):
    q = np.asarray(q, dtype=float)
    series = np.zeros_like(q)
    for power, coefficient in TAYLOR_TERMS[derivative]:
        series = series + coefficient * q**power
    if derivative == 0:
        direct = np.cosh(q) - 1 - q*q/2 - q**4/24
    elif derivative == 1:
        direct = np.sinh(q) - q - q**3/6
    elif derivative == 2:
        direct = np.cosh(q) - 1 - q*q/2
    else:
        direct = np.sinh(q) - q
    return np.where(np.abs(q) < .5, series, direct)


def potential(form, q, a, derivative=0):
    q = np.asarray(q, dtype=float)
    if derivative == 0:
        value = -q + q*q + (a/3.)*q**3 + .05*q**4
    elif derivative == 1:
        value = -1 + 2*q + a*q*q + .2*q**3
    elif derivative == 2:
        value = 2 + 2*a*q + .6*q*q
    elif derivative == 3:
        value = 2*a + 1.2*q
    else:
        raise ValueError("Only frozen derivatives 0 through 3 are available")
    if form == "S":
        coefficient = (.002, .012, .06, .24)[derivative]
        value = value + coefficient * q**(6 - derivative)
    elif form == "E":
        value = value + .02*r6(q, derivative)
    return value


def merge_roots(values):
    roots = []
    for value in sorted(map(float, values)):
        if not roots or value - roots[-1] > ROOT_MERGE:
            roots.append(value)
    return roots


def global_minimum(form, a, cache, counters):
    """Frozen scalar isolation on [-8,8], independent of model grid and box."""
    family = "P" if form in ("Q", "R") else form
    key = family, float(a).hex()
    if key in cache:
        counters["minimum_cache_hits"] += 1
        return cache[key]
    counters["minimum_scalar_solves"] += 1
    derivative = lambda order, x: float(potential(family, x, a, order))

    def solve(order, left, right):
        counters["brent_calls"] += 1
        root = float(brentq(lambda x: derivative(order, x), left, right,
                            xtol=ROOT_XTOL, rtol=ROOT_RTOL, maxiter=100))
        residual = abs(derivative(order, root))
        if not math.isfinite(root) or residual > ROOT_RESIDUAL:
            raise RuntimeError("Stationary-root isolation residual exceeded frozen tolerance")
        return root

    endpoint_values = {str(order): [derivative(order, -8.), derivative(order, 8.)]
                       for order in (1, 2, 3)}
    if (not all(math.isfinite(x) for values in endpoint_values.values() for x in values)
            or not endpoint_values["3"][0] < 0 < endpoint_values["3"][1]
            or not endpoint_values["1"][0] < 0 < endpoint_values["1"][1]
            or min(endpoint_values["2"]) <= 0):
        raise RuntimeError("Frozen stationary-root isolation endpoint conditions failed")
    z = solve(3, -8., 8.)
    second_minimum = derivative(2, z)
    if second_minimum < 0:
        second_roots = [solve(2, -8., z), solve(2, z, 8.)]
    elif second_minimum == 0.:
        second_roots = [z]
    else:
        second_roots = []
    divisions = merge_roots([-8., *second_roots, 8.])
    values = [derivative(1, point) for point in divisions]
    candidates = [point for point, value in zip(divisions, values) if value == 0.]
    for left, right, fl, fr in zip(divisions[:-1], divisions[1:], values[:-1], values[1:]):
        if (fl < 0 < fr) or (fr < 0 < fl):
            candidates.append(solve(1, left, right))
    roots = merge_roots(candidates)
    if not roots:
        raise RuntimeError("No stationary point found by frozen global-minimum procedure")
    residuals = [abs(derivative(1, root)) for root in roots]
    energies = [float(potential(family, root, a)) for root in roots]
    if max(residuals) > ROOT_RESIDUAL or not all(math.isfinite(x) for x in energies):
        raise RuntimeError("Invalid stationary-point residual or potential value")
    chosen = min(range(len(roots)), key=lambda index: (energies[index], roots[index]))
    record = {
        "potential_family": family, "a": float(a), "root_interval": [-8., 8.],
        "third_derivative_root": z, "third_derivative_root_residual": abs(derivative(3, z)),
        "second_derivative_minimum": second_minimum, "second_derivative_roots": second_roots,
        "second_derivative_root_residuals": [abs(derivative(2, root)) for root in second_roots],
        "partition_points": divisions, "first_derivative_at_partition": values,
        "endpoint_derivatives": endpoint_values, "roots_before_merge": sorted(candidates),
        "stationary_roots": roots, "root_residuals": residuals, "stationary_values": energies,
        "minimum": energies[chosen], "minimizer": roots[chosen],
        "tie_rule": "lowest potential, then leftmost root; floating arithmetic, not certified",
        "zero_endpoint_rule": "literal floating zero; partition values retained for audit",
    }
    cache[key] = record
    return record


def cooling(a_start, steps):
    u = (np.arange(1, steps + 1) - .5) / steps
    f = np.log(11 + 299*u)**(-2.)
    first, last = np.log(11.)**(-2.), np.log(310.)**(-2.)
    return u, A_END + (a_start - A_END)*(f - last)/(first - last)


def propagate(form, theta, n, length, steps, minimum_cache, counters, zero_potential=False):
    h, a_start, mass = map(float, theta)
    q = -length + 2*length*np.arange(1, n + 1)/(n + 1)
    p = np.pi*h*np.arange(1, n + 1)/(2*length)
    kinetic = p*p/(2*mass) if form == "Q" else p*p/(np.hypot(mass, p) + mass)
    u, schedule = cooling(a_start, steps)
    dt = BETA/steps
    decay = np.exp(-dt*kinetic)
    shifted = np.zeros((steps, n), dtype=float)
    minima, clipping_count, maximum_clip = [], 0, 0.
    for index, a in enumerate(schedule):
        if zero_potential:
            continue
        minimum = global_minimum(form, float(a), minimum_cache, counters)
        minima.append(minimum)
        raw = potential(form, q, a) - minimum["minimum"]
        if not np.all(np.isfinite(raw)) or np.min(raw) < -1e-10:
            raise RuntimeError("Nonfinite shifted potential or W below -1e-10")
        negative = raw < 0.
        clipping_count += int(np.count_nonzero(negative))
        if np.any(negative):
            maximum_clip = max(maximum_clip, float(np.max(-raw[negative])))
        shifted[index] = np.maximum(raw, 0.)
    product = np.eye(n, dtype=float)
    for values in shifted:
        half = np.exp(-.5*dt*values)
        first = half[:, None]*product
        transformed = fft.dst(first, type=1, axis=0, norm="ortho", workers=1)
        drifted = fft.dst(decay[:, None]*transformed, type=1, axis=0, norm="ortho", workers=1)
        product = half[:, None]*drifted
    if not np.all(np.isfinite(product)):
        raise RuntimeError("Nonfinite chronological heat product")
    arrays = {
        "form_key": np.array(form), "theta": np.asarray(theta).copy(),
        "grid_n": np.array(n), "L": np.array(length), "steps": np.array(steps), "beta": np.array(BETA),
        "q": q, "p": p, "kinetic_minus_mass": kinetic, "midpoint_u": u,
        "schedule": schedule, "W_samples": shifted, "mean_W": np.mean(shifted, axis=0),
        "C_tilde": product, "potential_mode": np.array("zero_control" if zero_potential else "global_minimum_shift"),
        "minimum_values": np.array([row["minimum"] for row in minima]),
        "minimizers": np.array([row["minimizer"] for row in minima]),
    }
    diagnostics = {"real_matrix": True, "matrix_frobenius_norm": float(np.linalg.norm(product)),
                   "matrix_max_absolute_entry": float(np.max(np.abs(product))),
                   "potential_clipped_count": clipping_count, "potential_maximum_clip": maximum_clip,
                   "potential_minimum_after_clip": float(np.min(shifted)),
                   "potential_maximum_after_clip": float(np.max(shifted)),
                   "first_midpoint_a": float(schedule[0]), "last_midpoint_a": float(schedule[-1]),
                   "spatial_step": float(2*length/(n + 1))}
    return arrays, diagnostics, minima


def spectrum_readout(sigma, mass, target, count=320):
    sigma = np.asarray(sigma)
    mask = np.isfinite(sigma) & (sigma > 0.)
    energy = np.full(sigma.shape, np.nan, dtype=float)
    energy[mask] = mass - np.log(sigma[mask])/BETA
    mask &= np.isfinite(energy)
    reasons = []
    if len(sigma) < count:
        reasons.append("INSUFFICIENT_DIMENSION")
    if not (len(sigma) and math.isfinite(float(sigma[0])) and 0 < sigma[0] <= 1 + 1e-10):
        reasons.append("SIGMA0_OUT_OF_CONTRACTION_RANGE")
    if len(sigma) >= count and not np.all(mask[:count]):
        reasons.append("UNRESOLVED_REQUIRED_SINGULAR_VALUES")
    if len(sigma) >= count and not np.all(np.diff(sigma[:count]) <= 0):
        reasons.append("REQUIRED_SINGULAR_VALUES_NOT_ORDERED")
    ratio = float(sigma[count - 1]/sigma[0]) if len(sigma) >= count and sigma[0] > 0 else float("nan")
    if not math.isfinite(ratio) or ratio < 1e-10:
        reasons.append("REQUIRED_RELATIVE_SINGULAR_VALUE_BELOW_1E-10")
    if not (len(energy) and math.isfinite(float(energy[0])) and energy[0] > 0):
        reasons.append("NONPOSITIVE_OR_NONFINITE_ABSOLUTE_E0")
    if len(energy) >= count and (not np.all(np.isfinite(energy[:count]))
                                or not np.all(energy[:count] >= mass - 1e-8)):
        reasons.append("REQUIRED_ENERGY_BELOW_REST_MASS_TOLERANCE_OR_NONFINITE")
    scale = float(target[0]/energy[0]) if len(energy) and np.isfinite(energy[0]) and energy[0] > 0 else float("nan")
    prediction = np.full(count, np.nan, dtype=float)
    if len(energy) >= count and math.isfinite(scale):
        prediction = scale*energy[:count]
    valid = not reasons
    arrays = {"sigma": sigma.copy(), "energy": energy, "energy_resolved_mask": mask,
              "scale": np.array(scale), "predicted_320" if count == 320 else "predicted_control": prediction,
              "resolution_valid": np.array(valid), "invalid_reasons": np.array(reasons, dtype=str),
              "target_100": target.copy()}
    metadata = {"status": "VALID" if valid else "INVALID_RESOLUTION", "resolution_valid": valid,
                "invalid_reasons": reasons, "sigma0": nullable(sigma[0]) if len(sigma) else None,
                "required_last_sigma": nullable(sigma[count - 1]) if len(sigma) >= count else None,
                "required_sigma_ratio": nullable(ratio), "required_count": count,
                "E0": nullable(energy[0]) if len(energy) else None, "scale": nullable(scale),
                "resolved_energy_count": int(np.count_nonzero(mask))}
    return arrays, metadata


def heat_forward(form, theta, target, n, length, steps, minimum_cache, counters):
    arrays, diagnostics, minima = propagate(form, theta, n, length, steps, minimum_cache, counters)
    counters["score_svd_calls"] += 1
    sigma = np.linalg.svd(arrays["C_tilde"], compute_uv=False)
    readout, validity = spectrum_readout(sigma, float(theta[2]), target)
    arrays.update(readout)
    prediction = arrays["predicted_320"]
    diagnostic_metrics = metrics(prediction[:100], target) if np.all(np.isfinite(prediction[:100])) else None
    record = {"form": FORM_IDS[form], "form_key": form, "theta": list(map(float, theta)),
              "grid_n": n, "L": length, "steps": steps, "beta": BETA,
              **validity, "metrics": diagnostic_metrics,
              "metrics_used_for_selection": bool(validity["resolution_valid"]),
              "diagnostics": diagnostics, "minimum_ledger": minima}
    return arrays, record


def pair_summary(grids, arrays, target):
    valid = all(grids[str(n)]["resolution_valid"] for n in TRAIN_GRIDS)
    if not valid:
        return {"resolution_valid": False, "status": "INVALID_RESOLUTION", "joint_score": PENALTY,
                "max_mape_percent": None, "max_percent_error": None, "cross_grid_percent": None}
    m = [grids[str(n)]["metrics"]["mape_percent"] for n in TRAIN_GRIDS]
    w = [grids[str(n)]["metrics"]["max_percent_error"] for n in TRAIN_GRIDS]
    gap = float(100*np.max(np.abs(arrays[383]["predicted_320"][:100]
                                  - arrays[511]["predicted_320"][:100])/target))
    return {"resolution_valid": True, "status": "VALID", "max_mape_percent": max(m),
            "max_percent_error": max(w), "cross_grid_percent": gap,
            "joint_score": max(m[0]/M_REF, m[1]/M_REF, w[0]/W_REF, w[1]/W_REF, gap/G_REF)}


def rank(record):
    if not record["resolution_valid"]:
        raise ValueError("An invalid pair cannot enter winner ranking")
    return (record["joint_score"], record["max_mape_percent"], record["max_percent_error"],
            record["cross_grid_percent"], record["evaluation_id"])


def analytic_control(target, minimum_cache, counters, event):
    theta = DEFAULT.copy()
    counters["control_propagations"] += 1
    event("propagation_start", stage="analytic-control", grid_n=63, form=FORM_IDS["R"], theta=theta.tolist())
    arrays, diagnostics, minima = propagate("R", theta, 63, L, STEPS, minimum_cache, counters, zero_potential=True)
    counters["control_svd_calls"] += 1
    sigma = np.linalg.svd(arrays["C_tilde"], compute_uv=False)
    readout, validity = spectrum_readout(sigma, 1., target, count=63)
    arrays.update(readout)
    expected_sigma = np.exp(-BETA*arrays["kinetic_minus_mass"])
    expected_energy = np.hypot(1., arrays["p"])
    check = {"sigma_max_absolute_difference": float(np.max(np.abs(sigma - expected_sigma))),
             "energy_max_absolute_difference": float(np.max(np.abs(arrays["energy"] - expected_energy))),
             "sigma_tolerance": 1e-10, "energy_tolerance": 1e-8, "diagnostics": diagnostics,
             "not_used_for_selection": True, "validity": validity}
    check["passed"] = bool(validity["resolution_valid"] and check["sigma_max_absolute_difference"] <= 1e-10
                           and check["energy_max_absolute_difference"] <= 1e-8)
    arrays.update(expected_sigma=expected_sigma, expected_energy=expected_energy)
    write_npz(OUT/"analytic-control.npz", arrays)
    write_json(OUT/"analytic-control.json", check)
    event("propagation_complete", stage="analytic-control", grid_n=63, result=check)
    if not check["passed"]:
        raise RuntimeError("Pure kinetic analytic control failed; no retry")


def freeze_role_arrays(form, n, arrays, target, counters, event):
    """Additional readouts of saved products; no new propagation or selection."""
    event("role_readouts_start", role=form, grid_n=n, not_a_propagation=True)
    counters["winner_full_svd_calls"] += 1
    left, repeated_sigma, right_t = np.linalg.svd(arrays["C_tilde"], full_matrices=True)
    difference = float(np.max(np.abs(repeated_sigma - arrays["sigma"])))
    if not math.isfinite(difference) or difference > 1e-12:
        raise RuntimeError("Winner full SVD differs from frozen score singular values")
    right = right_t.T
    momentum_states = fft.dst(right, type=1, axis=0, norm="ortho", workers=1)
    boundary = np.sum(right[np.abs(arrays["q"]) > .9*float(arrays["L"])]**2, axis=0)
    tail_count = (n + 4)//5
    tail = np.sum(momentum_states[n-tail_count:]**2, axis=0)
    occupation = {"high_momentum_mode_count": tail_count, "rounding": "ceil(N/5)",
                  "boundary_condition": "abs(q)>0.9L", "summaries": {}}
    for count in (100, 320):
        occupation["summaries"][str(count)] = {
            "boundary_max": float(np.max(boundary[:count])), "boundary_mean": float(np.mean(boundary[:count])),
            "high_momentum_max": float(np.max(tail[:count])), "high_momentum_mean": float(np.mean(tail[:count]))}
    identity = np.eye(n)
    modes = fft.dst(identity, type=1, axis=0, norm="ortho", workers=1)
    kinetic_matrix = fft.dst(arrays["kinetic_minus_mass"][:, None]*modes,
                             type=1, axis=0, norm="ortho", workers=1)
    mass = float(arrays["theta"][2])
    havg = mass*identity + kinetic_matrix + np.diag(arrays["mean_W"])
    counters["static_eigvalsh_calls"] += 1
    static_values = np.linalg.eigvalsh(havg, UPLO="L")
    if not np.all(np.isfinite(static_values)) or static_values[0] <= 0:
        raise RuntimeError("Static same-parameter Hamiltonian has invalid absolute spectrum")
    static_scale = float(target[0]/static_values[0])
    static_prediction = static_values[:320]*static_scale
    arrays.update(svd_left=left, svd_sigma_recomputed=repeated_sigma, svd_right_transpose=right_t,
                  right_boundary_mass=boundary, right_high_momentum_mass=tail,
                  H_avg=havg, static_eigenvalues=static_values,
                  static_scale=np.array(static_scale), static_predicted_320=static_prediction)
    norm = float(np.linalg.norm(arrays["C_tilde"]))
    record = {
        "form_key": form, "grid_n": n, "theta": arrays["theta"].tolist(),
        "repeat_svd_sigma_max_difference": difference,
        "svd_relative_reconstruction_residual": float(np.linalg.norm((left*arrays["sigma"])@right_t - arrays["C_tilde"])/norm),
        "repeat_svd_relative_reconstruction_residual": float(np.linalg.norm((left*repeated_sigma)@right_t - arrays["C_tilde"])/norm),
        "left_orthogonality_relative_fro": float(np.linalg.norm(left.T@left - identity)/np.sqrt(n)),
        "right_orthogonality_relative_fro": float(np.linalg.norm(right_t@right_t.T - identity)/np.sqrt(n)),
        "occupation": occupation, "static_scale": static_scale, "static_E0": float(static_values[0]),
        "static_metrics": metrics(static_prediction[:100], target), "not_used_for_selection": True,
        "original_score_sigma_and_prediction_preserved": True,
    }
    write_npz(OUT/f"winner-{form}-N{n}.npz", arrays)
    event("role_readouts_complete", role=form, grid_n=n, result=record, complete_array_saved=True)
    return record


def main():
    started = time.perf_counter()
    locks = json.loads(LOCK_FILE.read_text())
    for path, wanted in locks.items():
        if sha(ROOT/path) != wanted:
            raise RuntimeError(f"Input hash mismatch: {path}")
    if OUT.exists():
        raise RuntimeError("Output exists; refusing overwrite or repeat")
    OUT.mkdir(parents=True)
    (OUT/"evaluations").mkdir()
    log = (OUT/"events.jsonl").open("x", encoding="utf-8")
    log_lock, monitor_stop = threading.Lock(), threading.Event()
    counters = {"training_propagations": 0, "control_propagations": 0, "postfreeze_propagations": 0,
                "score_svd_calls": 0, "control_svd_calls": 0, "winner_full_svd_calls": 0,
                "static_eigvalsh_calls": 0, "minimum_scalar_solves": 0, "minimum_cache_hits": 0,
                "brent_calls": 0}

    def event(name, **fields):
        with log_lock:
            text = json.dumps({"utc": utc(), "event": name, **fields}, allow_nan=False)
            log.write(text + "\n")
            log.flush()
            print(text, flush=True)

    def resources():
        while not monitor_stop.wait(30):
            paths = [path for path in OUT.rglob("*") if path.is_file()]
            rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            event("resource_sample", pid=os.getpid(), seconds=time.perf_counter()-started,
                  maxrss_kib=rss, memory_above_512mib_advisory=bool(rss > 512*1024),
                  output_files=len(paths), output_bytes=sum(path.stat().st_size for path in paths))

    def finish(report):
        report.update(counters=dict(counters),
                      total_propagations=sum(counters[key] for key in
                                             ("training_propagations", "control_propagations", "postfreeze_propagations")),
                      seconds_before_final_serialization=time.perf_counter()-started,
                      maxrss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, completed_utc=utc(),
                      all_inputs_unchanged=all(sha(ROOT/path) == wanted for path, wanted in locks.items()))
        write_json(OUT/"result.json", report)
        monitor_stop.set()
        monitor.join(timeout=1)
        event("completed" if report["status"] == "completed" else "stopped_no_valid_member",
              status=report["status"], global_joint_winner=report.get("global_joint_winner"),
              seconds=report["seconds_before_final_serialization"], counters=dict(counters))
        write_json(OUT/"file-inventory.json", {str(path.relative_to(OUT)): path.stat().st_size
                                              for path in sorted(OUT.rglob("*")) if path.is_file()})

    monitor = threading.Thread(target=resources, daemon=True)
    monitor.start()
    try:
        manifest = {
            "scope_id": "ASFS-DISCOVERY-20260919-CS06", "started_utc": utc(), "pid": os.getpid(),
            "inputs": locks, "input_locks_sha256": sha(LOCK_FILE), "script_sha256": sha(Path(__file__)),
            "preexecution_notes_sha256": sha(PACKAGE/"evidence/preexecution-notes.md"),
            "python": sys.version, "numpy": np.__version__, "scipy": scipy.__version__, "command": COMMAND,
            "thread_environment": {key: os.environ.get(key) for key in
                                   ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")},
            "training_grids": list(TRAIN_GRIDS), "L": L, "steps": STEPS, "beta": BETA,
            "M_ref": M_REF, "W_ref": W_REF, "G_ref_percent": G_REF,
            "invalid_resolution_penalty": PENALTY, "root_isolation_certified": False,
            "all_invalid_seed_nm_fallback": "common DEFAULT, maxfev unchanged at 8; clarified before execution",
            "high_momentum_occupation_mode_count": "ceil(N/5)",
            "run_passport": "UNVERIFIED; saved-evidence checks are not reproduction reruns",
        }
        write_json(OUT/"manifest.json", manifest)
        event("started", pid=os.getpid())
        with np.load(TARGET_SOURCE, allow_pickle=False) as source:
            target = source["target_100"].copy()
            q_prediction = source["energy"][1:101]*float(source["scale"])
        with np.load(MEAN_SOURCE, allow_pickle=False) as source:
            mean_target = source["target_100"].copy()
            m_prediction = source["energy"][1:101]*float(source["scale"])
        if (len(target) != 100 or not np.array_equal(target, mean_target)
                or not np.all(np.isfinite(target)) or not np.all(np.diff(target) > 0)):
            raise RuntimeError("Frozen target mismatch")
        if abs(metrics(q_prediction, target)["max_percent_error"] - W_REF) > 1e-12:
            raise RuntimeError("Frozen W reference mismatch")
        if abs(metrics(m_prediction, target)["mape_percent"] - M_REF) > 1e-12:
            raise RuntimeError("Frozen M reference mismatch")
        minimum_cache = {}
        analytic_control(target, minimum_cache, counters, event)
        cache, best = {}, {}
        call_rows, cached_rows, unique_rows = [], [], []
        calls, unique = 0, 0

        def objective(form, x, stage, physical=None):
            nonlocal calls, unique
            calls += 1
            default_x = (DEFAULT - LOW)/(HIGH - LOW)
            theta = (np.asarray(physical, dtype=float).copy() if physical is not None else
                     DEFAULT.copy() if np.array_equal(x, default_x) else LOW + np.asarray(x)*(HIGH - LOW))
            if calls > 60 or not np.all(np.isfinite(theta)) or np.any(theta < LOW) or np.any(theta > HIGH):
                raise RuntimeError("Frozen pair budget or parameter bounds violated")
            key = form, *(float(value).hex() for value in theta)
            if key in cache:
                record = dict(cache[key])
                record.update(call=calls, stage=stage, cached=True,
                              source_evaluation_id=record["evaluation_id"])
                call_rows.append(record)
                cached_rows.append(record)
                event("cached_pair_call", call=calls, form=FORM_IDS[form], stage=stage,
                      source_evaluation_id=record["evaluation_id"], status=record["status"],
                      joint_score=record["joint_score"])
                return record["joint_score"]
            unique += 1
            eid = f"{FORM_IDS[form]}-{unique:04d}"
            event("pair_evaluation_start", evaluation_id=eid, call=calls, stage=stage,
                  form=FORM_IDS[form], theta=theta.tolist())
            tick = time.perf_counter()
            pair_arrays, grid_records = {}, {}
            for n in TRAIN_GRIDS:
                if counters["training_propagations"] >= 120:
                    raise RuntimeError("Training propagation budget exceeded")
                counters["training_propagations"] += 1
                event("propagation_start", stage="training", evaluation_id=eid, grid_n=n,
                      form=FORM_IDS[form], theta=theta.tolist(), counters=dict(counters))
                grid_started = time.perf_counter()
                arrays, record = heat_forward(form, theta, target, n, L, STEPS, minimum_cache, counters)
                record["seconds"] = time.perf_counter()-grid_started
                pair_arrays[n], grid_records[str(n)] = arrays, record
                write_npz(OUT/"evaluations"/f"{eid}-N{n}.npz", arrays)
                write_json(OUT/"evaluations"/f"{eid}-N{n}.json", record)
                event("propagation_complete", stage="training", evaluation_id=eid, grid_n=n,
                      status=record["status"], invalid_reasons=record["invalid_reasons"],
                      metrics=record["metrics"], seconds=record["seconds"], counters=dict(counters))
            summary = pair_summary(grid_records, pair_arrays, target)
            record = {"evaluation_id": eid, "form": FORM_IDS[form], "form_key": form,
                      "theta": theta.tolist(), "call": calls, "stage": stage, "cached": False,
                      "grids": grid_records, "seconds": time.perf_counter()-tick, **summary}
            write_json(OUT/"evaluations"/f"{eid}.json", record)
            cache[key] = record
            call_rows.append(record)
            unique_rows.append(record)
            if record["resolution_valid"] and (form not in best or rank(record) < rank(best[form][1])):
                best[form] = (pair_arrays, record)
            event("pair_evaluation_complete", evaluation_id=eid, status=record["status"],
                  joint_score=record["joint_score"], max_mape_percent=record["max_mape_percent"],
                  max_percent_error=record["max_percent_error"], cross_grid_percent=record["cross_grid_percent"])
            return record["joint_score"]

        rng = np.random.default_rng(20260923)
        wide = rng.uniform(0, 1, (4, 3))
        seeds = [DEFAULT.copy(), np.array([DEFAULT[0], DEFAULT[1], .3]),
                 np.array([DEFAULT[0], DEFAULT[1], 2.5])]
        seeds += [LOW + point*(HIGH - LOW) for point in wide]
        write_json(OUT/"seed-design.json", {"seed": 20260923, "wide_normalized": wide.tolist(),
                   "physical_points_shared_by_all_forms": [point.tolist() for point in seeds]})
        for index, theta in enumerate(seeds):
            for form in FORM_IDS:
                objective(form, (theta - LOW)/(HIGH - LOW), f"seed-{index:02d}", physical=theta)
        optimizers = {}
        for form in FORM_IDS:
            fallback = form not in best
            start_theta = DEFAULT if fallback else np.asarray(best[form][1]["theta"])
            x0 = (start_theta - LOW)/(HIGH - LOW)
            simplex = np.repeat(x0[None, :], 4, axis=0)
            for coordinate in range(3):
                simplex[coordinate + 1, coordinate] += .08 if x0[coordinate] <= .92 else -.08
            event("optimizer_start", form=FORM_IDS[form], theta=start_theta.tolist(),
                  no_valid_seed_default_fallback=fallback, maxfev=8)
            result = minimize(lambda x: objective(form, x, "refine"), x0, method="Nelder-Mead",
                              bounds=[(0., 1.)]*3,
                              options={"maxfev": 8, "initial_simplex": simplex, "xatol": 1e-5,
                                       "fatol": 1e-5, "adaptive": False})
            optimizers[form] = {"success": bool(result.success), "message": str(result.message),
                                "nfev": int(result.nfev), "nit": int(result.nit), "fun": float(result.fun),
                                "no_valid_seed_default_fallback": fallback}
            event("form_training_complete", form=FORM_IDS[form], optimizer=optimizers[form],
                  role_status="VALID_MEMBER" if form in best else "NO_VALID_MEMBER")
        winner = min(best, key=lambda form: rank(best[form][1])) if best else None
        role_status = {form: "VALID_MEMBER" if form in best else "NO_VALID_MEMBER" for form in FORM_IDS}
        selected_utc = utc()
        readout_records = {}
        for form, (pair_arrays, record) in best.items():
            readout_records[form] = {str(n): freeze_role_arrays(form, n, pair_arrays[n], target, counters, event)
                                     for n in TRAIN_GRIDS}
        frozen = {"scope_id": manifest["scope_id"], "selection_utc": selected_utc, "frozen_utc": utc(),
                  "global_joint_winner": winner, "role_status": role_status,
                  "roles": {form: record for form, (arrays, record) in best.items()},
                  "role_readouts": readout_records, "calls": calls, "unique_training_members": unique,
                  "optimizers": optimizers, "counters": dict(counters),
                  "selection": "valid paired N383/N511 J only",
                  "evaluation_window": "301-320; not yet generated by this run"}
        write_json(OUT/"winners-frozen.json", frozen)
        write_json(OUT/"calls.json", call_rows)
        write_json(OUT/"cache-calls.json", cached_rows)
        write_json(OUT/"unique-members.json", unique_rows)
        write_json(OUT/"minimum-cache.json", list(minimum_cache.values()))
        event("training_frozen", sha256=sha(OUT/"winners-frozen.json"), global_joint_winner=winner,
              role_status=role_status, full_winner_arrays=2*len(best), calls=calls, counters=dict(counters))
        base_report = {"scope_id": manifest["scope_id"], "global_joint_winner": winner,
                       "roles": frozen["roles"], "role_status": role_status, "role_readouts": readout_records,
                       "calls": calls, "cached_calls": len(cached_rows), "unique_training_members": unique,
                       "invalid_unique_members": sum(not row["resolution_valid"] for row in unique_rows),
                       "optimizers": optimizers}
        if len(best) != len(FORM_IDS):
            finish({**base_report, "status": "NO_VALID_MEMBER", "reference_generated": False,
                    "postfreeze": None, "static_postfreeze": None, "post_variants": []})
            return
        event("postfreeze_reference_start", first=301, last=320, no_further_selection=True)
        import mpmath as mp
        mp.mp.dps = 40
        strings = [str(mp.im(mp.zetazero(index))) for index in range(301, 321)]
        future = np.array([float(value) for value in strings])
        write_json(OUT/"reference-301-320.json", {"first": 301, "last": 320, "decimal_precision": 40,
                   "mpmath": mp.__version__, "ordinates": strings,
                   "scope": "postfreeze; non-certified and not historically blind"})
        event("development_reference_read", sources=[str(path.relative_to(ROOT)) for path in DEVELOPMENT_SOURCES])
        development = np.array([float(value) for path in DEVELOPMENT_SOURCES
                                for value in json.loads(path.read_text())["ordinates"]])
        if len(development) != 200 or len(future) != 20:
            raise RuntimeError("Reference-window length mismatch")
        truth = np.concatenate([target, development, future])

        def windows(prediction, valid=True):
            if not valid:
                return None
            return {"training_1_100": metrics(prediction[:100], target),
                    "development_101_300": metrics(prediction[100:300], development),
                    "evaluation_301_320": metrics(prediction[300:320], future)}

        post = {form: {str(n): windows(arrays[n]["predicted_320"]) for n in TRAIN_GRIDS}
                for form, (arrays, record) in best.items()}
        static_post = {form: {str(n): windows(arrays[n]["static_predicted_320"]) for n in TRAIN_GRIDS}
                       for form, (arrays, record) in best.items()}

        def point_table(path, predictions):
            with path.open("x", newline="", encoding="utf-8") as handle:
                writer = csv.writer(handle)
                writer.writerow(["role", "grid_n", "L", "steps", "resolution_valid", "index", "window",
                                 "target", "predicted", "residual", "percent_error"])
                for role, n, length, steps, valid, prediction in predictions:
                    for index, (actual, estimate) in enumerate(zip(truth, prediction), 1):
                        window = "train" if index <= 100 else "development" if index <= 300 else "postfreeze-evaluation"
                        writer.writerow([role, n, length, steps, valid, index, window, actual, estimate,
                                         estimate-actual, 100*abs(estimate-actual)/actual])

        point_table(OUT/"winner-points.csv", [(form, n, L, STEPS, True, arrays[n]["predicted_320"])
                                             for form, (arrays, record) in best.items() for n in TRAIN_GRIDS])
        point_table(OUT/"static-control-points.csv", [(form, n, L, STEPS, True, arrays[n]["static_predicted_320"])
                                                     for form, (arrays, record) in best.items() for n in TRAIN_GRIDS])
        event("postfreeze_evaluation_complete", results=post, static_controls=static_post)
        primary_arrays, primary_record = best[winner]
        baseline = primary_arrays[511]["predicted_320"][:100]
        post_records, post_points = [], []
        for name, n, length, steps in POST_VARIANTS:
            counters["postfreeze_propagations"] += 1
            event("propagation_start", stage="postfreeze", variant=name, form=FORM_IDS[winner],
                  grid_n=n, L=length, steps=steps, theta=primary_record["theta"], counters=dict(counters))
            arrays, record = heat_forward(winner, primary_record["theta"], target, n, length, steps,
                                         minimum_cache, counters)
            valid = record["resolution_valid"]
            record.update(variant=name, windows=windows(arrays["predicted_320"], valid),
                          cross_grid_to_training_N511_percent=float(100*np.max(abs(arrays["predicted_320"][:100]-baseline)/target)) if valid else None,
                          comparison_line_percent=G_REF, not_used_for_selection=True)
            write_npz(OUT/f"post-{name}.npz", arrays)
            write_json(OUT/f"post-{name}.json", record)
            post_records.append(record)
            post_points.append((name, n, length, steps, valid, arrays["predicted_320"]))
            event("propagation_complete", stage="postfreeze", variant=name, status=record["status"],
                  windows=record["windows"], cross_grid_to_training_N511_percent=record["cross_grid_to_training_N511_percent"],
                  counters=dict(counters))
        point_table(OUT/"post-points.csv", post_points)
        finish({**base_report, "status": "completed", "reference_generated": True,
                "postfreeze": post, "static_postfreeze": static_post, "post_variants": post_records})
    except Exception as exc:
        event("failed", type=type(exc).__name__, message=str(exc), counters=dict(counters))
        raise
    finally:
        monitor_stop.set()
        monitor.join(timeout=1)
        log.close()


if __name__ == "__main__":
    main()
