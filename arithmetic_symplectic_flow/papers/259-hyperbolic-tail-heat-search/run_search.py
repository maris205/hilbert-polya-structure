#!/usr/bin/env python3
"""CS09 frozen hyperbolic-tail search; scientific controls run only in main."""
from decimal import Decimal, localcontext
import csv
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
from scipy import fft
from scipy.optimize import brentq, minimize


PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[1]
OUT = PACKAGE/"evidence/run-1"
LOCK_FILE = PACKAGE/"input-locks.json"
PREVIOUS = ROOT/"papers/258-shape-dispersion-heat-search"
HELPER_FILE = PREVIOUS/"run_search.py"
UTILITY_FILE = PREVIOUS/"resume_fixed.py"
OLD_TRAIN = PREVIOUS/"evidence/run-1"
OLD_FIXED = PREVIOUS/"evidence/run-2-fixed"
SCOPE = "ASFS-DISCOVERY-20260919-CS09"
FORMS = {"B": "CS09-B-QUINTIC-REFIT", "E": "CS09-E-EVEN-HYPERBOLIC",
         "X": "CS09-X-ASYMMETRIC-HYPERBOLIC"}
BASE = np.array([.16368442617990808, 1.640269295261368, .5874437187565427, -.003159505004882813])
LOW4, HIGH4 = np.array([.12, 1.40, .30, -.006]), np.array([.22, 1.80, .90, .006])
TRAIN_N, POST_N = (511, 639), (1023, 1279)
BETA, LENGTH, SAMPLES = .02, 8., 64
M_REF, W_REF, G_REF, PENALTY = 1.7092315698742464, 5.249433263238935, 2., 1e30
ROOT_XTOL, ROOT_RTOL, ROOT_TOL, ROOT_MERGE = 1e-13, 4*np.finfo(float).eps, 1e-9, 1e-10
GIB = 1024**3
TAIL_COEFFICIENTS = {(degree, derivative): tuple(math.factorial(degree)/math.factorial(degree+2*r-derivative)
                      for r in range(33)) for degree in (5, 6) for derivative in range(5)}
COMMAND = ("OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 "
           "PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 600s python -u "
           "papers/259-hyperbolic-tail-heat-search/run_search.py")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def import_file(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def verify_inputs():
    locks = json.loads(LOCK_FILE.read_text())
    for path, expected in locks.items():
        if sha(ROOT/path) != expected:
            raise RuntimeError(f"Frozen input hash mismatch: {path}")
    return locks


def bounds(form):
    return (LOW4.copy(), HIGH4.copy()) if form == "B" else (np.append(LOW4, 0.), np.append(HIGH4, 1.2))


def default_theta(form):
    return BASE.copy() if form == "B" else np.append(BASE, 0.)


def monomial_derivative(degree, q, derivative):
    return (math.factorial(degree)/math.factorial(degree-derivative))*np.asarray(q, dtype=float)**(degree-derivative)


def normalized_tail(degree, kappa, q, derivative=0):
    """Analytic S5/S6 derivatives, with the frozen stable series switch."""
    if degree not in (5, 6) or derivative not in range(5) or kappa < 0:
        raise ValueError("Tail degree/derivative/kappa outside frozen definition")
    q = np.asarray(q, dtype=float)
    if kappa == 0.:
        return monomial_derivative(degree, q, derivative)
    x = kappa*q
    small = np.abs(x) <= 4.
    result = np.empty_like(q)
    xs = x[small]
    horner = np.zeros_like(xs)
    for coefficient in reversed(TAIL_COEFFICIENTS[(degree, derivative)]):
        horner = horner*xs*xs+coefficient
    result[small] = q[small]**(degree-derivative)*horner
    if np.any(~small):
        xb = x[~small]
        remainder = np.cosh(xb) if (degree-derivative) % 2 == 0 else np.sinh(xb)
        for power in range(degree % 2, degree, 2):
            if power >= derivative:
                remainder = remainder-xb**(power-derivative)/math.factorial(power-derivative)
        result[~small] = math.factorial(degree)*kappa**(derivative-degree)*remainder
    return result


def potential(form, q, a, z, kappa, derivative=0):
    q = np.asarray(q, dtype=float)
    if derivative == 0:
        base = -q+q*q+(a/3.)*q**3+.05*q**4
    elif derivative == 1:
        base = -1+2*q+a*q*q+.2*q**3
    elif derivative == 2:
        base = 2+2*a*q+.6*q*q
    elif derivative == 3:
        base = 2*a+1.2*q
    elif derivative == 4:
        base = np.full_like(q, 1.2)
    else:
        raise ValueError("Only derivatives 0 through 4 are frozen")
    if form == "B" or kappa == 0.:
        return base+.002*monomial_derivative(6, q, derivative)+z*monomial_derivative(5, q, derivative)
    fifth = normalized_tail(5, kappa, q, derivative) if form == "X" else monomial_derivative(5, q, derivative)
    return base+.002*normalized_tail(6, kappa, q, derivative)+z*fifth


def evaluation_controls():
    """Finite numerical controls, deliberately called only by main."""
    polynomial_rows = []
    q_grid = np.linspace(-12., 12., 49)
    for a in (1.02, 1.4, 1.8):
        for z in (-.006, 0., .006):
            for derivative in range(5):
                base = potential("B", q_grid, a, z, 0., derivative)
                exact = {form: bool(np.array_equal(base, potential(form, q_grid, a, z, 0., derivative))) for form in ("E", "X")}
                polynomial_rows.append({"a": a, "z": z, "derivative": derivative, "exact_equal": exact})
    decimal_rows = []
    with localcontext() as context:
        context.prec = 60
        for degree in (5, 6):
            for derivative in range(5):
                for q in (-12., -4., -.1, 0., .1, 4., 12.):
                    for kappa in (1e-6, .2, 1.2):
                        dq, dk = Decimal(str(q)), Decimal(str(kappa))
                        reference = Decimal(0)
                        for r in range(100):
                            power = degree+2*r-derivative
                            reference += (Decimal(math.factorial(degree))/Decimal(math.factorial(power))
                                          *dk**(2*r)*dq**power)
                        actual = float(normalized_tail(degree, kappa, q, derivative))
                        difference = abs(actual-float(reference))
                        tolerance = 1e-11*max(1., abs(float(reference)))
                        decimal_rows.append({"degree": degree, "derivative": derivative, "q": q, "kappa": kappa,
                                             "reference_decimal60": str(reference), "actual_float64": actual,
                                             "absolute_difference": difference, "allowed_absolute_difference": tolerance,
                                             "passed": bool(math.isfinite(actual) and difference <= tolerance)})
    passed = all(all(row["exact_equal"].values()) for row in polynomial_rows) and all(row["passed"] for row in decimal_rows)
    return {"passed": passed, "kappa_zero_q_grid": q_grid.tolist(), "kappa_zero_checks": polynomial_rows,
            "decimal_precision": 60, "decimal_series_r": [0, 99], "float_series_r": [0, 32],
            "decimal_comparisons": decimal_rows, "not_a_global_parameter_box_proof": True}


def merge_roots(values):
    merged = []
    for value in sorted(map(float, values)):
        if not merged or value-merged[-1] > ROOT_MERGE:
            merged.append(value)
    return merged


def global_minimum(form, a, z, kappa, cache, ledger, root_counts, ledger_stream):
    family = "B" if form == "B" or kappa == 0. else "E" if form == "X" and z == 0. else form
    potential_kappa = 0. if family == "B" else kappa
    key = family, float(a).hex(), float(z).hex(), float(potential_kappa).hex()
    if key in cache:
        root_counts["minimum_cache_hits"] += 1
        return cache[key]
    root_counts["minimum_solves_attempted"] += 1
    derivative = lambda order, x: float(potential(family, x, a, z, potential_kappa, order))

    def solve(order, left, right):
        root_counts["brent_attempted"] += 1
        root = float(brentq(lambda x: derivative(order, x), left, right,
                            xtol=ROOT_XTOL, rtol=ROOT_RTOL, maxiter=100))
        root_counts["brent_returned"] += 1
        if not math.isfinite(root) or abs(derivative(order, root)) > ROOT_TOL:
            raise RuntimeError("Derivative root residual exceeds frozen 1e-9 tolerance")
        return root

    endpoints = {str(order): [derivative(order, -12.), derivative(order, 12.)] for order in (1, 2, 3)}
    if (not all(math.isfinite(value) for pair in endpoints.values() for value in pair)
            or not endpoints["1"][0] < 0 < endpoints["1"][1]
            or not endpoints["3"][0] < 0 < endpoints["3"][1] or min(endpoints["2"]) <= 0):
        raise RuntimeError("Frozen [-12,12] derivative endpoint conditions failed")
    third_root = solve(3, -12., 12.)
    second_minimum = derivative(2, third_root)
    second_roots = ([solve(2, -12., third_root), solve(2, third_root, 12.)] if second_minimum < 0
                    else [third_root] if second_minimum == 0. else [])
    divisions = merge_roots([-12., *second_roots, 12.])
    values = [derivative(1, point) for point in divisions]
    candidates = [point for point, value in zip(divisions, values) if value == 0.]
    for left, right, fl, fr in zip(divisions[:-1], divisions[1:], values[:-1], values[1:]):
        if (fl < 0 < fr) or (fr < 0 < fl):
            candidates.append(solve(1, left, right))
    roots = merge_roots(candidates)
    if not roots:
        raise RuntimeError("No stationary point in frozen root partition")
    residuals = [abs(derivative(1, root)) for root in roots]
    energies = [float(potential(family, root, a, z, potential_kappa)) for root in roots]
    if max(residuals) > ROOT_TOL or not all(math.isfinite(value) for value in energies):
        raise RuntimeError("Invalid stationary values/residuals")
    index = min(range(len(roots)), key=lambda j: (energies[j], roots[j]))
    row = {"minimum_id": len(ledger), "family": family, "a": float(a), "z": float(z), "kappa": float(potential_kappa),
           "exact_key": list(key), "interval": [-12., 12.], "endpoint_derivatives": endpoints,
           "third_derivative_root": third_root, "third_derivative_residual": abs(derivative(3, third_root)),
           "fourth_derivative_at_third_root": derivative(4, third_root),
           "second_derivative_minimum": second_minimum, "second_derivative_roots": second_roots,
           "second_derivative_residuals": [abs(derivative(2, root)) for root in second_roots],
           "partition_points": divisions, "first_derivative_at_partition": values,
           "roots_before_merge": sorted(candidates), "stationary_roots": roots, "root_residuals": residuals,
           "stationary_values": energies, "minimum": energies[index], "minimizer": roots[index],
           "tie_rule": "lowest value then leftmost root", "noncertified_literal_float_zero_rule": True}
    ledger_stream.write(json.dumps(row, allow_nan=False)+"\n")
    ledger_stream.flush()
    ledger.append(row)
    cache[key] = row
    root_counts["minimum_solves_completed"] += 1
    return row


def propagate(cooling_source, form, theta, n, length, count, cache, ledger, root_counts, ledger_stream, zero=False):
    h, a_start, mass, z = map(float, theta[:4])
    kappa = float(theta[4]) if len(theta) == 5 else 0.
    q = -length+2*length*np.arange(1, n+1)/(n+1)
    p = np.pi*h*np.arange(1, n+1)/(2*length)
    kinetic = p*p/(np.hypot(mass, p)+mass)
    midpoint, schedule = cooling_source.cooling(a_start, count)
    shifted = np.zeros((count, n))
    ids, minima, minimizers = [], [], []
    clipped_count, maximum_clip = 0, 0.
    for index, a in enumerate(schedule):
        if zero:
            continue
        row = global_minimum(form, float(a), z, kappa, cache, ledger, root_counts, ledger_stream)
        raw = potential(form, q, float(a), z, kappa)-row["minimum"]
        if not np.all(np.isfinite(raw)) or np.min(raw) < -1e-10:
            raise RuntimeError("Nonfinite shifted potential or W below -1e-10")
        negative = raw < 0.
        clipped_count += int(np.count_nonzero(negative))
        if np.any(negative):
            maximum_clip = max(maximum_clip, float(np.max(-raw[negative])))
        shifted[index] = np.maximum(raw, 0.)
        ids.append(row["minimum_id"])
        minima.append(row["minimum"])
        minimizers.append(row["minimizer"])
    decay = np.exp(-(BETA/count)*kinetic)
    product = np.eye(n)
    for values in shifted:
        half = np.exp(-.5*(BETA/count)*values)
        transformed = fft.dst(half[:, None]*product, type=1, axis=0, norm="ortho", workers=1)
        drifted = fft.dst(decay[:, None]*transformed, type=1, axis=0, norm="ortho", workers=1)
        product = half[:, None]*drifted
    if not np.all(np.isfinite(product)):
        raise RuntimeError("Nonfinite chronological heat matrix")
    arrays = {"theta": np.asarray(theta).copy(), "form_key": np.array(form), "grid_n": np.array(n),
              "L": np.array(length), "sample_count": np.array(count), "beta": np.array(BETA),
              "q": q, "p": p, "kinetic_minus_mass": kinetic, "midpoint_u": midpoint, "schedule": schedule,
              "W_samples": shifted, "mean_W": np.mean(shifted, axis=0), "C_tilde": product,
              "minimum_ids": np.array(ids, dtype=np.int64), "minimum_values": np.array(minima),
              "minimizers": np.array(minimizers), "minimum_ledger_path": np.array("minimum-ledger.jsonl"),
              "potential_mode": np.array("zero_control" if zero else "global_minimum_shift")}
    record = {"form": FORMS[form], "form_key": form, "theta": list(map(float, theta)), "N": n,
              "L": length, "B": count, "beta": BETA, "minimum_ids": ids,
              "potential_clipped_count": clipped_count, "potential_maximum_clip": maximum_clip,
              "first_midpoint_a": float(schedule[0]), "last_midpoint_a": float(schedule[-1]),
              "spatial_step": 2*length/(n+1), "p_max": float(p[-1])}
    return arrays, record


def rank(row):
    if not row["resolution_valid"]:
        raise ValueError("Invalid pair cannot enter ranking")
    return (row["joint_score"], row["max_mape_percent"], row["max_percent_error"],
            row["cross_grid_percent"], row["evaluation_id"])


def pair_summary(grids, arrays, target):
    if not all(grids[str(n)]["resolution_valid"] for n in TRAIN_N):
        return {"status": "INVALID_RESOLUTION", "resolution_valid": False, "joint_score": PENALTY,
                "max_mape_percent": None, "max_percent_error": None, "cross_grid_percent": None,
                "J_minus_1": None, "benchmark_differences": None}
    m = [grids[str(n)]["training_metrics"]["mape_percent"] for n in TRAIN_N]
    w = [grids[str(n)]["training_metrics"]["max_percent_error"] for n in TRAIN_N]
    gap = float(100*np.max(np.abs(arrays[511]["predicted_320"][:100]-arrays[639]["predicted_320"][:100])/target))
    joint = max(m[0]/M_REF, m[1]/M_REF, w[0]/W_REF, w[1]/W_REF, gap/G_REF)
    return {"status": "VALID", "resolution_valid": True, "joint_score": joint, "J_minus_1": joint-1,
            "max_mape_percent": max(m), "max_percent_error": max(w), "cross_grid_percent": gap,
            "benchmark_differences": {str(n): {"M_minus_M_ref_percentage_points": m[index]-M_REF,
                                                 "W_minus_W_ref_percentage_points": w[index]-W_REF}
                                      for index, n in enumerate(TRAIN_N)}}


def main():
    started = time.perf_counter()
    utilities = import_file("cs09_immutable_utilities", UTILITY_FILE)
    logging_test = utilities.logger_regression_test()
    locks = verify_inputs()
    own_hash = sha(Path(__file__))
    if OUT.exists():
        raise RuntimeError("Output exists; refusing overwrite or retry")
    OUT.mkdir(parents=True)
    (OUT/"evaluations").mkdir()
    output = utilities.BoundedOutput(OUT, GIB)
    event_stream = output.text_stream("events.jsonl")
    ledger_stream = output.text_stream("minimum-ledger.jsonl")
    call_stream = output.text_stream("calls.jsonl")
    event = utilities.make_logger(event_stream, echo=True)
    monitor_stop = threading.Event()
    counters = {"propagations_attempted": 0, "propagations_completed": 0,
                "control_propagations_attempted": 0, "control_propagations_completed": 0,
                "training_propagations_attempted": 0, "training_propagations_completed": 0,
                "postfreeze_propagations_attempted": 0, "postfreeze_propagations_completed": 0,
                "full_svd_attempted": 0, "full_svd_completed": 0, "control_arrays_saved": 0,
                "training_compact_grids_saved": 0, "full_heat_grids_saved": 0,
                "static_readouts_attempted": 0, "static_readouts_completed": 0, "static_grids_saved": 0}
    roots = {"minimum_cache_hits": 0, "minimum_solves_attempted": 0, "minimum_solves_completed": 0,
             "brent_attempted": 0, "brent_returned": 0}
    helper_counts = {"static_eigh_calls": 0}
    end_verification = None

    def resources():
        while not monitor_stop.wait(30):
            rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            event("resource_sample", pid=os.getpid(), seconds=time.perf_counter()-started,
                  maxrss_kib=rss, memory_above_1gib_advisory=bool(rss*1024 > GIB),
                  output_bytes=output.size(), counters=dict(counters))

    monitor = threading.Thread(target=resources, daemon=True)
    monitor.start()
    try:
        helper = import_file("cs09_immutable_readouts", HELPER_FILE)
        cooling_source = helper.import_source()
        manifest = {"scope_id": SCOPE, "started_utc": utilities.utc(), "pid": os.getpid(), "command": COMMAND,
                    "script_sha256": own_hash, "input_locks_sha256": sha(LOCK_FILE), "inputs": locks,
                    "python": sys.version, "numpy": np.__version__, "scipy": scipy.__version__,
                    "thread_environment": {key: os.environ.get(key) for key in
                                           ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")},
                    "forms": FORMS, "train_N": TRAIN_N, "post_N": POST_N,
                    "M_ref": M_REF, "W_ref": W_REF, "G_ref_percent": G_REF,
                    "max_pair_calls": 123, "max_propagations": 255, "max_full_svd": 255, "max_static": 14,
                    "beta": BETA, "L": LENGTH, "B": SAMPLES, "cache": "same form/exact physical theta; no cross-form spectra",
                    "root_interval": [-12., 12.], "root_isolation_certified": False,
                    "only_scalar_minima_share_identical_potential_identity": True,
                    "E_X_are_identical_when_z_zero": True,
                    "training_nonwinner_C_and_states_saved": False,
                    "reconstruction_limit": "Nonwinner C/states require reconstruction from frozen code and inputs; no such rerun in this run.",
                    "per_forward_svd": "exactly one full SVD; no final repeated winner SVD",
                    "old_module_globals_mutated": False, "old_main_or_optimizer_called": False,
                    "source_functions": ["256.cooling", "258.readout/add_states/static_readout/metrics/compare/compact",
                                         "258.resume_fixed.BoundedOutput/make_logger/logger_regression_test"],
                    "output_limit_bytes": GIB, "memory_advisory_bytes": GIB, "timeout_seconds": 600,
                    "actual_exit_code": "recorded by launching parent", "run_passport": "UNVERIFIED",
                    "logging_regression": logging_test, "all_development_targets_previously_observed": True}
        output.json("manifest.json", manifest)
        output.json("logger-regression.json", logging_test)
        event("started", scope_id=SCOPE, pid=os.getpid())
        event("evaluation_controls_start", no_propagation=True)
        control_math = evaluation_controls()
        output.json("evaluation-controls.json", control_math)
        event("evaluation_controls_complete", passed=control_math["passed"], no_propagation=True)
        if not control_math["passed"]:
            raise RuntimeError("Frozen kappa-zero/Decimal60 evaluation control failed; no retry")
        with np.load(helper.TARGET_SOURCE, allow_pickle=False) as old:
            target = old["target_100"].copy()
        if len(target) != 100 or target[0] <= 0 or not np.all(np.isfinite(target)) or not np.all(np.diff(target) > 0):
            raise RuntimeError("Invalid frozen target100")
        old_identity = json.loads((OLD_TRAIN/"winners-frozen.json").read_text())
        if old_identity["roles"]["Q"]["evaluation_id"] != "CS08-Q-QUINTIC-0107" or not np.array_equal(old_identity["roles"]["Q"]["theta"], BASE):
            raise RuntimeError("Old Q0107 identity mismatch")
        if (abs(old_identity["roles"]["Q"]["max_mape_percent"]-M_REF) > 1e-12
                or abs(old_identity["roles"]["Q"]["max_percent_error"]-W_REF) > 1e-12):
            raise RuntimeError("Same-member training benchmark mismatch")
        old_regression = {}
        for n in TRAIN_N:
            with np.load(OLD_TRAIN/"evaluations"/f"CS08-Q-QUINTIC-0107-N{n}.npz", allow_pickle=False) as old:
                if not np.array_equal(old["theta"], BASE) or not np.array_equal(old["target_100"], target):
                    raise RuntimeError("Old default grid theta/target mismatch")
                old_regression[n] = old["predicted_320"].copy()
        minimum_cache, minimum_ledger = {}, []

        def calculate(form, theta, n, length, count, stage, name, zero=False):
            limits = {"control": 1, "training": 246, "postfreeze": 8}
            if counters["propagations_attempted"] >= 255 or counters[stage+"_propagations_attempted"] >= limits[stage]:
                raise RuntimeError("Frozen propagation budget exceeded")
            counters["propagations_attempted"] += 1
            counters[stage+"_propagations_attempted"] += 1
            tick = time.perf_counter()
            event("propagation_start", name=name, stage=stage, form=form, N=n, L=length, B=count,
                  theta=theta.tolist(), counters=dict(counters))
            arrays, record = propagate(cooling_source, form, theta, n, length, count,
                                       minimum_cache, minimum_ledger, roots, ledger_stream, zero)
            counters["propagations_completed"] += 1
            counters[stage+"_propagations_completed"] += 1
            record["propagation_seconds"] = time.perf_counter()-tick
            event("propagation_complete", name=name, stage=stage, counters=dict(counters))
            if counters["full_svd_attempted"] >= 255:
                raise RuntimeError("Full SVD budget exceeded")
            counters["full_svd_attempted"] += 1
            tick = time.perf_counter()
            left_all, sigma, right_t_all = np.linalg.svd(arrays["C_tilde"], full_matrices=True)
            counters["full_svd_completed"] += 1
            record["full_svd_seconds"] = time.perf_counter()-tick
            retained = 63 if zero else 320
            arrays["_cached_left"] = left_all[:, :retained].copy()
            arrays["_cached_right_transpose"] = right_t_all[:retained].copy()
            del left_all, right_t_all
            readout, validity = helper.readout(sigma, float(theta[2]), BETA, target, retained)
            arrays.update(readout)
            record.update(validity)
            if not zero:
                record["training_metrics"] = helper.metrics(arrays["predicted_320"][:100], target) if validity["resolution_valid"] else None
            event("full_svd_complete", name=name, status=record["status"], counters=dict(counters))
            return arrays, record

        arrays, free_control = calculate("B", BASE.copy(), 63, LENGTH, SAMPLES, "control", "free-kinetic-control", zero=True)
        expected_sigma = np.sort(np.exp(-BETA*arrays["kinetic_minus_mass"]))[::-1]
        expected_energy = np.sort(BASE[2]+arrays["kinetic_minus_mass"])
        sigma_error = float(np.max(np.abs(arrays["sigma"]-expected_sigma)))
        energy_error = float(np.max(np.abs(arrays["energy"]-expected_energy)))
        free_control["analytic"] = {"sigma_max_absolute_difference": sigma_error, "energy_max_absolute_difference": energy_error,
                                     "sigma_tolerance": 1e-10, "energy_tolerance": 1e-8,
                                     "passed": bool(free_control["resolution_valid"] and sigma_error <= 1e-10 and energy_error <= 1e-8)}
        arrays.update(expected_sigma=expected_sigma, expected_energy=expected_energy)
        output.npz("free-kinetic-control.npz", {key: value for key, value in arrays.items() if not key.startswith("_cached_")})
        output.json("free-kinetic-control.json", free_control)
        counters["control_arrays_saved"] += 1
        del arrays
        if not free_control["analytic"]["passed"]:
            raise RuntimeError("Frozen free-kinetic control failed; no retry")
        cache, best, seed_physical = {}, {}, {}
        call_rows, unique_rows = [], []
        calls, unique, regression = 0, 0, None

        def objective(form, x, stage, physical=None):
            nonlocal calls, unique, regression
            calls += 1
            lower, upper = bounds(form)
            x = np.asarray(x)
            normalized_key = form, *(float(value).hex() for value in x)
            if physical is not None:
                theta = np.asarray(physical).copy()
                seed_physical[normalized_key] = theta.copy()
            else:
                theta = seed_physical[normalized_key].copy() if normalized_key in seed_physical else lower+x*(upper-lower)
            if calls > 123 or not np.all(np.isfinite(theta)) or np.any(theta < lower) or np.any(theta > upper):
                raise RuntimeError("Frozen objective call budget/bounds violated")
            key = form, *(float(value).hex() for value in theta)
            if key in cache:
                row = dict(cache[key])
                row.update(call=calls, stage=stage, cached=True, source_evaluation_id=row["evaluation_id"])
                call_rows.append(row)
                call_stream.write(json.dumps(row, allow_nan=False)+"\n")
                event("cached_pair_call", form=form, call=calls, source_evaluation_id=row["evaluation_id"], joint_score=row["joint_score"])
                return row["joint_score"]
            unique += 1
            eid = f"{FORMS[form]}-{unique:04d}"
            pair_arrays, grids = {}, {}
            tick = time.perf_counter()
            event("pair_start", evaluation_id=eid, call=calls, form=form, stage=stage, theta=theta.tolist())
            for n in TRAIN_N:
                arrays, grid = calculate(form, theta, n, LENGTH, SAMPLES, "training", f"{eid}-N{n}")
                arrays["evaluation_id"] = np.array(eid)
                compact_arrays = {name: value for name, value in arrays.items() if name != "C_tilde" and not name.startswith("_cached_")}
                output.npz(f"evaluations/{eid}-N{n}.npz", compact_arrays)
                grid.update(C_and_states_saved=False, reconstruction_source="frozen code/inputs; no rerun here")
                output.json(f"evaluations/{eid}-N{n}.json", grid)
                counters["training_compact_grids_saved"] += 1
                pair_arrays[n], grids[str(n)] = arrays, grid
            row = {"evaluation_id": eid, "form": FORMS[form], "form_key": form, "theta": theta.tolist(),
                   "normalized_x": x.tolist(), "call": calls, "stage": stage, "cached": False,
                   "seconds_including_save": time.perf_counter()-tick, "grids": grids,
                   **pair_summary(grids, pair_arrays, target)}
            output.json(f"evaluations/{eid}.json", row)
            cache[key] = row
            call_rows.append(row)
            unique_rows.append(row)
            call_stream.write(json.dumps(row, allow_nan=False)+"\n")
            if row["resolution_valid"] and (form not in best or rank(row) < rank(best[form][1])):
                best[form] = (pair_arrays, row)
            if calls == 1:
                if form != "B" or not np.array_equal(theta, BASE):
                    raise RuntimeError("First member differs from the default B regression owner")
                regression = {}
                for n in TRAIN_N:
                    prediction = pair_arrays[n]["predicted_320"]
                    old_metrics = helper.metrics(old_regression[n][:100], target)
                    new_metrics = helper.metrics(prediction[:100], target)
                    pred_error = float(np.max(np.abs(prediction-old_regression[n])))
                    metric_error = max(abs(old_metrics[key]-new_metrics[key]) for key in ("mape_percent", "max_percent_error"))
                    regression[str(n)] = {"prediction320_max_absolute_difference": pred_error,
                                           "first100_MW_max_absolute_difference": metric_error, "tolerance": 1e-6,
                                           "passed": bool(row["resolution_valid"] and pred_error <= 1e-6 and metric_error <= 1e-6)}
                output.json("default-regression.json", regression)
                if not all(record["passed"] for record in regression.values()):
                    raise RuntimeError("Default double-grid regression failed; no retry")
            event("pair_complete", evaluation_id=eid, joint_score=row["joint_score"], J_minus_1=row["J_minus_1"],
                  status=row["status"], max_mape_percent=row["max_mape_percent"], max_percent_error=row["max_percent_error"])
            return row["joint_score"]

        wide = np.random.default_rng(20260926).uniform(0, 1, (4, 5))
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
                points.extend(np.append(BASE, kappa) for kappa in (.2, .4, .8, 1.2))
            points.extend(lower+row[:len(lower)]*(upper-lower) for row in wide)
            seeds[form] = points
        output.json("seed-design.json", {"rng_seed": 20260926, "wide_normalized_4x5": wide.tolist(),
                                         "physical_seeds": {form: [point.tolist() for point in points] for form, points in seeds.items()}})
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
            event("optimizer_start", form=form, starting_member=best[form][1]["evaluation_id"], maxfev=32)
            optimized = minimize(lambda x: objective(form, x, "refine"), x0, method="Nelder-Mead",
                                 bounds=[(0., 1.)]*len(x0), options={"maxfev": 32, "initial_simplex": simplex,
                                 "xatol": 1e-6, "fatol": 1e-6, "adaptive": False})
            optimizers[form] = {"success": bool(optimized.success), "message": str(optimized.message),
                                "nfev": int(optimized.nfev), "nit": int(optimized.nit), "fun": float(optimized.fun)}
            event("optimizer_complete", form=form, optimizer=optimizers[form])
        primary = min(best, key=lambda form: rank(best[form][1])) if best else None
        roles = {form: row for form, (arrays, row) in best.items()}
        role_status = {form: "VALID_MEMBER" if form in roles else "NO_VALID_MEMBER" for form in FORMS}
        frozen = {"scope_id": SCOPE, "frozen_utc": utilities.utc(), "global_joint_winner": primary,
                  "roles": roles, "role_status": role_status, "calls": calls, "unique_members": unique,
                  "optimizers": optimizers, "selection": "joint first100 N511/N639 only",
                  "development_metrics_evaluated": False, "cached_states_from_original_single_svd": True}
        output.json("winners-frozen.json", frozen)
        identity_hash = sha(OUT/"winners-frozen.json")
        output.json("calls.json", call_rows)
        output.json("unique-members.json", unique_rows)
        event("winner_identities_frozen", sha256=identity_hash, primary=primary, role_status=role_status)
        members, metadata, heat_records, static_records, frozen_files = {}, {}, {}, {}, []

        def save_full(name, arrays, record, stage):
            event("winner_state_readout_start", name=name, not_a_propagation=True, no_additional_svd=True)
            left, right_t = arrays.pop("_cached_left"), arrays.pop("_cached_right_transpose")
            helper.add_states(arrays, left, right_t, record)
            del left, right_t
            record.update(C_and_states_saved=True, sole_svd_spectrum_preserved=True, no_additional_svd=True)
            members[name] = helper.compact(arrays, record["resolution_valid"])
            metadata[name] = {"kind": "heat", "stage": stage, "form": record["form_key"],
                              "N": int(arrays["grid_n"]), "L": float(arrays["L"]), "B": int(arrays["sample_count"])}
            output.npz(name+".npz", arrays)
            output.json(name+".json", record)
            counters["full_heat_grids_saved"] += 1
            heat_records[name] = record
            if counters["static_readouts_attempted"] >= 14:
                raise RuntimeError("New-scope static readout budget exceeded")
            counters["static_readouts_attempted"] += 1
            event("static_readout_start", name=name, not_a_propagation=True, counters=dict(counters))
            static_arrays, static_record = helper.static_readout(arrays, target, helper_counts)
            counters["static_readouts_completed"] += 1
            static_name = "static-"+name
            static_arrays["minimum_ledger_path"] = np.array("minimum-ledger.jsonl")
            static_record.update(heat_owner=name, form_key=record["form_key"], minimum_ledger_path="minimum-ledger.jsonl")
            members[static_name] = helper.compact(static_arrays)
            metadata[static_name] = {**metadata[name], "kind": "static"}
            output.npz(static_name+".npz", static_arrays)
            output.json(static_name+".json", static_record)
            counters["static_grids_saved"] += 1
            static_records[static_name] = static_record
            del static_arrays
            event("winner_state_readout_complete", name=name, counters=dict(counters), helper_internal_attempts=dict(helper_counts))
            return [name+".npz", name+".json", static_name+".npz", static_name+".json"]

        for form in FORMS:
            if form not in best:
                continue
            pair_arrays, row = best[form]
            for n in TRAIN_N:
                arrays = pair_arrays.pop(n)
                record = dict(row["grids"][str(n)])
                record.update(evaluation_id=row["evaluation_id"], selection_J=row["joint_score"], original_ranking_arrays_preserved=True)
                frozen_files.extend(save_full(f"winner-{form}-N{n}", arrays, record, "training-winner"))
                del arrays
                gc.collect()
        best.clear()
        if len(frozen_files) != 8*len(roles):
            raise RuntimeError("Training full-array freeze file count mismatch")
        full_freeze = {"scope_id": SCOPE, "frozen_utc": utilities.utc(), "winner_identity_file": "winners-frozen.json",
                       "winner_identity_sha256": identity_hash, "role_status": role_status,
                       "full_heat_arrays": 2*len(roles), "full_static_arrays": 2*len(roles),
                       "file_count": len(frozen_files), "files_sha256": {name: sha(OUT/name) for name in frozen_files},
                       "development_metrics_evaluated": False, "counters": dict(counters)}
        output.json("training-arrays-frozen.json", full_freeze)
        event("training_arrays_frozen", sha256=sha(OUT/"training-arrays-frozen.json"), counters=dict(counters))
        event("development_reference_read_start", all_previously_observed=True, no_further_selection=True)
        portions = []
        for path, count in helper.REFERENCES:
            values = np.array([float(value) for value in json.loads(path.read_text())["ordinates"]])
            if len(values) != count:
                raise RuntimeError("Known reference window length mismatch")
            portions.append(values)
        truth = np.concatenate([target, *portions])
        if len(truth) != 320 or not np.all(np.isfinite(truth)) or not np.all(np.diff(truth) > 0):
            raise RuntimeError("Invalid complete known reference ledger")
        with np.load(OLD_FIXED/"post-Q-N1279.npz", allow_pickle=False) as old:
            if not np.array_equal(old["theta"], BASE) or not np.array_equal(old["target_100"], target):
                raise RuntimeError("Old fixed Q0107 comparator identity mismatch")
            members["old-Q0107-N1279"] = helper.compact(old, bool(old["resolution_valid"]))
            metadata["old-Q0107-N1279"] = {"kind": "reused", "stage": "old-fixed-comparator", "form": "Q0107", "N": 1279, "L": 8., "B": 64}
        output.json("known-targets.json", {"first": 1, "last": 320, "ordinates": truth.tolist(),
                                           "all_previously_observed": True, "generated_by_this_run": False})
        post_records = {}

        def post(form, n, length, count, name):
            theta = np.array(roles[form]["theta"])
            arrays, record = calculate(form, theta, n, length, count, "postfreeze", name)
            record.update(source_evaluation_id=roles[form]["evaluation_id"], no_selection=True)
            save_full(name, arrays, record, "fixed-postfreeze")
            post_records[name] = record
            del arrays
            gc.collect()
            event("fixed_postcheck_saved", name=name, status=record["status"], counters=dict(counters))

        for form in FORMS:
            if form in roles:
                for n in POST_N:
                    post(form, n, LENGTH, SAMPLES, f"post-{form}-N{n}")
        if primary is not None:
            post(primary, 1279, 8., 128, "primary-time-N1279-B128")
            post(primary, 1599, 10., 64, "primary-box-N1599-L10")
        fits = {name: ({window: helper.metrics(member["prediction"][start:stop], truth[start:stop])
                        for window, (start, stop) in helper.WINDOWS.items()} if member["valid"] else None)
                for name, member in members.items()}
        comparisons = {}
        for form in roles:
            for label, left, right in (("train-grid", f"winner-{form}-N511", f"winner-{form}-N639"),
                                       ("N639-N1023", f"winner-{form}-N639", f"post-{form}-N1023"),
                                       ("N1023-N1279", f"post-{form}-N1023", f"post-{form}-N1279"),
                                       ("old-baseline-N1279", "old-Q0107-N1279", f"post-{form}-N1279")):
                comparisons[f"{form}-{label}"] = helper.compare(left, right, members, truth)
        for name in list(members):
            if "static-"+name in members:
                comparisons["static-"+name] = helper.compare(name, "static-"+name, members, truth)
        if primary is not None:
            for name in ("primary-time-N1279-B128", "primary-box-N1599-L10"):
                comparisons[name] = helper.compare(f"post-{primary}-N1279", name, members, truth)
        structure = {}
        for form in ("E", "X"):
            if form not in roles:
                structure[form] = {"status": "NO_VALID_MEMBER"}
                continue
            row = roles[form]
            structure[form] = {"kappa": row["theta"][4], "kappa_nonzero": row["theta"][4] != 0.,
                               "z": row["theta"][3], "joint_score": row["joint_score"], "J_minus_1": row["joint_score"]-1,
                               "J_below_1": row["joint_score"] < 1,
                               "B_joint_score": roles["B"]["joint_score"] if "B" in roles else None,
                               "J_strictly_better_than_B": row["joint_score"] < roles["B"]["joint_score"] if "B" in roles else None,
                               "no_hyperbolic_structure_gain_if_kappa_zero": True,
                               "E_X_same_potential_when_z_zero": row["theta"][3] == 0.}
        points = io.StringIO(newline="")
        writer = csv.writer(points)
        writer.writerow(["object_id", "kind", "stage", "form", "N", "L", "B", "resolution_valid", "index", "window",
                         "target", "predicted", "energy", "residual", "percent_error"])
        for name, member in members.items():
            meta = metadata[name]
            for index, (actual, predicted, energy) in enumerate(zip(truth, member["prediction"], member["energy"]), 1):
                window = "1-100" if index <= 100 else "101-300" if index <= 300 else "301-320"
                writer.writerow([name, meta["kind"], meta["stage"], meta["form"], meta["N"], meta["L"], meta["B"],
                                 member["valid"], index, window, actual, predicted, energy, predicted-actual, 100*abs(predicted-actual)/actual])
        output.binary("points.csv", points.getvalue().encode("utf-8"))
        output.json("development-fit-metrics.json", fits)
        output.json("comparisons.json", comparisons)
        output.json("minimum-ledger.json", minimum_ledger)
        end_locks = verify_inputs()
        if end_locks != locks or sha(Path(__file__)) != own_hash or sha(OUT/"winners-frozen.json") != identity_hash:
            raise RuntimeError("Frozen inputs/script/winner identity changed during execution")
        end_verification = {"all_input_hashes_match": True, "input_count": len(locks),
                            "script_sha256_unchanged": True, "winner_identity_sha256_unchanged": True}
        report = {"scope_id": SCOPE, "status": "completed" if len(roles) == len(FORMS) else "completed_with_missing_roles",
                  "run_passport": "UNVERIFIED", "global_joint_winner": primary, "roles": roles, "role_status": role_status,
                  "calls": calls, "unique_members": unique, "cached_calls": sum(row["cached"] for row in call_rows),
                  "invalid_unique_members": sum(not row["resolution_valid"] for row in unique_rows),
                  "optimizers": optimizers, "default_regression": regression, "free_control": free_control,
                  "evaluation_control_passed": control_math["passed"], "winner_identity_sha256": identity_hash,
                  "heat_readouts": heat_records, "static_readouts": static_records, "postfreeze": post_records,
                  "fit_metrics": fits, "comparisons": comparisons, "structure_vs_B": structure,
                  "counters": dict(counters), "root_counters": dict(roots), "helper_internal_attempts": dict(helper_counts),
                  "end_verification": end_verification, "seconds_before_final_serialization": time.perf_counter()-started,
                  "maxrss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                  "completed_utc": utilities.utc(), "output_bytes_before_result": output.size(),
                  "new_targets_generated": False, "formal_route": "UNASSIGNED; B NOT INVOKED"}
        output.json("result.json", report)
        monitor_stop.set()
        monitor.join(timeout=1)
        event("completed", primary=primary, seconds=report["seconds_before_final_serialization"], calls=calls,
              counters=dict(counters), output_bytes=output.size())
        inventory = {str(path.relative_to(OUT)): {"bytes": path.stat().st_size, "sha256": sha(path)}
                     for path in sorted(OUT.rglob("*")) if path.is_file()}
        output.json("file-inventory.json", {"scope_id": SCOPE, "inventory_excludes_itself": True, "files": inventory})
    except Exception as exc:
        try:
            event("failed", type=type(exc).__name__, message=str(exc), counters=dict(counters),
                  root_counters=dict(roots), helper_internal_attempts=dict(helper_counts), end_verification=end_verification)
        except Exception as logging_exc:
            print(f"Could not append failure evidence: {type(logging_exc).__name__}: {logging_exc}", file=sys.stderr, flush=True)
        raise
    finally:
        monitor_stop.set()
        monitor.join(timeout=1)
        ledger_stream.close()
        call_stream.close()
        event_stream.close()


if __name__ == "__main__":
    main()
