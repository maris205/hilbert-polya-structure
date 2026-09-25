#!/usr/bin/env python3
"""CS11 frozen position-mobility search. Import does not execute scientific work."""
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
from scipy.optimize import minimize


PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[1]
OUT = PACKAGE/"evidence/run-1"
LOCK_FILE = PACKAGE/"input-locks.json"
HELPER_FILE = ROOT/"papers/258-shape-dispersion-heat-search/run_search.py"
UTILITY_FILE = ROOT/"papers/258-shape-dispersion-heat-search/resume_fixed.py"
STATE_FILE = ROOT/"papers/260-phase-shear-heat-search/run_search.py"
POTENTIAL_FILE = ROOT/"papers/259-hyperbolic-tail-heat-search/run_search.py"
OLD = POTENTIAL_FILE.parent/"evidence/run-1"
SCOPE = "ASFS-DISCOVERY-20260919-CS11"
FORMS = {"B": "CS11-B-QUINTIC-REFIT", "M": "CS11-M-POSITION-MOBILITY"}
BASE = np.array([.1639363246753303, 1.655042492001211, .5881152959703404, -.003369556173000019])
LOW4, HIGH4 = np.array([.12, 1.40, .30, -.006]), np.array([.22, 1.80, .90, .006])
TRAIN_N, POST_N = (511, 639), (1023, 1279)
BETA, LENGTH, SAMPLES, A_END = .02, 8., 64, 1.02
M_REF, W_REF, G_REF, PENALTY = 1.695273790061038, 5.234299091683695, 2., 1e30
GIB = 1024**3
COMMAND = ("OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 "
           "PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 600s python -u "
           "papers/261-position-mobility-heat-search/run_search.py")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def import_file(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def verify_inputs():
    locks = json.loads(LOCK_FILE.read_text())
    for path, wanted in locks.items():
        if sha(ROOT/path) != wanted:
            raise RuntimeError("Frozen input hash mismatch: "+path)
    return locks


def bounds(form):
    return (LOW4.copy(), HIGH4.copy()) if form == "B" else (np.append(LOW4, -.75), np.append(HIGH4, 1.5))


def default_theta(form):
    return BASE.copy() if form == "B" else np.append(BASE, 0.)


def dst(values):
    return fft.dst(values, type=1, axis=0, norm="ortho", workers=1)


def rank(row):
    if not row["resolution_valid"]:
        raise ValueError("Invalid member cannot enter winner ranking")
    return (row["joint_score"], row["max_mape_percent"], row["max_percent_error"], row["cross_grid_percent"], row["evaluation_id"])


def pair_summary(grids, arrays, target):
    if not all(grids[str(n)]["resolution_valid"] for n in TRAIN_N):
        return {"status": "INVALID_RESOLUTION", "resolution_valid": False, "joint_score": PENALTY,
                "J_minus_1": None, "max_mape_percent": None, "max_percent_error": None,
                "cross_grid_percent": None, "benchmark_differences": None}
    means = [grids[str(n)]["training_metrics"]["mape_percent"] for n in TRAIN_N]
    worst = [grids[str(n)]["training_metrics"]["max_percent_error"] for n in TRAIN_N]
    gap = float(100*np.max(np.abs(arrays[511]["predicted_320"][:100]-arrays[639]["predicted_320"][:100])/target))
    score = max(means[0]/M_REF, means[1]/M_REF, worst[0]/W_REF, worst[1]/W_REF, gap/G_REF)
    return {"status": "VALID", "resolution_valid": True, "joint_score": score, "J_minus_1": score-1,
            "max_mape_percent": max(means), "max_percent_error": max(worst), "cross_grid_percent": gap,
            "benchmark_differences": {str(n): {"M_minus_M_ref_percentage_points": means[i]-M_REF,
                                                "W_minus_W_ref_percentage_points": worst[i]-W_REF}
                                      for i, n in enumerate(TRAIN_N)}}


def materialize_base_kinetic(arrays, record):
    """Analytic DST eigenbasis, not an eigensolver or another propagation."""
    if "K" in arrays:
        return
    if str(arrays["form_key"]) != "B":
        raise RuntimeError("Only B may materialize its analytic kinetic basis here")
    n = int(arrays["grid_n"])
    basis = dst(np.eye(n))
    values = arrays["kinetic_minus_mass"].copy()
    matrix = dst(values[:, None]*basis)
    drift = dst(np.exp(-float(arrays["delta"])*values)[:, None]*basis)
    arrays.update(K=matrix, kinetic_Q=basis, kinetic_nu=values, P_delta=drift)
    record.update(kinetic_basis="analytic orthonormal DST-I; no kinetic eigh", kinetic_full_arrays_materialized=True,
                  kinetic_trace=float(np.trace(matrix)), kinetic_trace_identity_rhs=float(np.sum(values)),
                  kinetic_trace_identity_absolute_difference=float(abs(np.trace(matrix)-np.sum(values))),
                  kinetic_symmetry_relative_fro=float(np.linalg.norm(matrix-matrix.T)/np.linalg.norm(matrix)))


def propagate(potential_source, cooling_source, form, theta, n, length, count, minimum_cache,
              ledger, root_counts, ledger_stream, counters, event, name, order="O", zero=False, profile="henon"):
    h, a_start, mass, z = map(float, theta[:4])
    kappa = float(theta[4]) if form == "M" else 0.
    q = -length+2*length*np.arange(1, n+1)/(n+1)
    p = np.pi*h*np.arange(1, n+1)/(2*length)
    kinetic = p*p/(np.hypot(mass, p)+mass)
    x = (2*A_END*q)**2
    natural_profile = x/(1+x)
    if profile not in ("henon", "constant_one") or (form == "B" and profile != "henon"):
        raise ValueError("Unsupported profile owner")
    g = natural_profile if profile == "henon" else np.ones(n)
    multiplier = np.sqrt(1+kappa*g)
    if not np.all(np.isfinite(multiplier)) or np.min(multiplier) <= 0:
        raise RuntimeError("Invalid positive mobility multiplier")
    midpoint, schedule = cooling_source.cooling(a_start, count)
    shifted = np.zeros((count, n))
    ids, minima, minimizers = [], [], []
    clipped_count, maximum_clip = 0, 0.
    for j, a in enumerate(schedule):
        if zero:
            continue
        row = potential_source.global_minimum("B", float(a), z, 0., minimum_cache, ledger, root_counts, ledger_stream)
        raw = potential_source.potential("B", q, float(a), z, 0.)-row["minimum"]
        if not np.all(np.isfinite(raw)) or np.min(raw) < -1e-10:
            raise RuntimeError("Nonfinite shifted potential or W below -1e-10")
        negative = raw < 0
        clipped_count += int(np.count_nonzero(negative))
        if np.any(negative):
            maximum_clip = max(maximum_clip, float(np.max(-raw[negative])))
        shifted[j] = np.maximum(raw, 0.)
        ids.append(row["minimum_id"])
        minima.append(row["minimum"])
        minimizers.append(row["minimizer"])
    if order not in ("O", "reverse"):
        raise ValueError("Unsupported frozen order")
    indices = np.arange(count) if order == "O" else np.arange(count-1, -1, -1)
    delta = BETA/count
    half = np.exp(-.5*delta*shifted)
    decay = np.exp(-delta*kinetic)
    arrays = {"theta": np.asarray(theta).copy(), "form_key": np.array(form), "grid_n": np.array(n),
              "L": np.array(length), "sample_count": np.array(count), "beta": np.array(BETA), "delta": np.array(delta),
              "q": q, "p": p, "kinetic_minus_mass": kinetic, "g": g, "g_henon_reference": natural_profile,
              "R_diagonal": multiplier, "profile": np.array(profile), "a_end_profile": np.array(A_END),
              "midpoint_u": midpoint, "schedule": schedule, "W_samples": shifted, "mean_W": np.mean(shifted, axis=0),
              "minimum_ids": np.array(ids, dtype=np.int64), "minimum_values": np.array(minima),
              "minimizers": np.array(minimizers), "minimum_ledger_path": np.array("minimum-ledger.jsonl"),
              "sample_order_zero_based": indices, "sample_order_one_based": indices+1,
              "order_name": np.array(order), "potential_mode": np.array("zero_control" if zero else "global_minimum_shift")}
    record = {"form_key": form, "form": FORMS[form], "theta": list(map(float, theta)), "N": n,
              "L": length, "B": count, "beta": BETA, "delta": delta, "order": order, "profile": profile,
              "kappa": kappa, "minimum_ids": ids, "potential_clipped_count": clipped_count,
              "potential_maximum_clip": maximum_clip, "first_midpoint_a": float(schedule[0]),
              "last_midpoint_a": float(schedule[-1]), "spatial_step": 2*length/(n+1), "p_max": float(p[-1]),
              "multiplier_min": float(np.min(multiplier)), "multiplier_max": float(np.max(multiplier)),
              "rest_mass_outside_congruence": True, "kinetic_full_arrays_materialized": form == "M"}
    drift = None
    if form == "M":
        if counters["kinetic_eigh_attempted"] >= 54:
            raise RuntimeError("Frozen kinetic eigh budget exceeded")
        basis = dst(np.eye(n))
        base_matrix = dst(kinetic[:, None]*basis)
        del basis
        trace_rhs = float(np.sum(np.diag(base_matrix)*multiplier**2))
        matrix = multiplier[:, None]*base_matrix*multiplier[None, :]
        del base_matrix
        if not np.all(np.isfinite(matrix)):
            raise RuntimeError("Nonfinite mobility kinetic matrix")
        counters["kinetic_eigh_attempted"] += 1
        event("kinetic_eigh_start", name=name, kappa=kappa, profile=profile, counters=dict(counters))
        tick = time.perf_counter()
        values, basis = np.linalg.eigh(matrix, UPLO="L")
        counters["kinetic_eigh_completed"] += 1
        elapsed = time.perf_counter()-tick
        if not np.all(np.isfinite(values)) or np.min(values) <= 0:
            raise RuntimeError("Mobility kinetic eigenvalues not strictly positive; no clipping")
        residual = np.linalg.norm(matrix@basis-basis*values, axis=0)
        drift = (basis*np.exp(-delta*values))@basis.T
        if not np.all(np.isfinite(drift)):
            raise RuntimeError("Nonfinite reused kinetic exponential")
        arrays.update(K=matrix, kinetic_Q=basis, kinetic_nu=values, P_delta=drift,
                      kinetic_eigen_equation_residual=residual, kinetic_trace_identity_rhs=np.array(trace_rhs))
        record.update(kinetic_basis="one full real eigh per M propagation, including kappa=0", kinetic_eigh_seconds=elapsed,
                      kinetic_min_eigenvalue=float(values[0]), kinetic_max_eigenvalue=float(values[-1]),
                      kinetic_symmetry_relative_fro=float(np.linalg.norm(matrix-matrix.T)/np.linalg.norm(matrix)),
                      kinetic_equation_residual_max=float(np.max(residual)),
                      kinetic_eigh_triangle="L; residual against original full saved matrix, no explicit symmetrization",
                      kinetic_orthogonality_fro=float(np.linalg.norm(basis.T@basis-np.eye(n))),
                      kinetic_trace=float(np.trace(matrix)), kinetic_trace_identity_rhs=trace_rhs,
                      kinetic_trace_identity_absolute_difference=float(abs(np.trace(matrix)-trace_rhs)),
                      kinetic_trace_spectrum_absolute_difference=float(abs(np.trace(matrix)-np.sum(values))))
        event("kinetic_eigh_complete", name=name, counters=dict(counters))
    else:
        arrays["kinetic_nu"] = kinetic.copy()
        record["kinetic_basis"] = "analytic DST-I action; no kinetic eigh"
    product = np.eye(n)
    for j in indices:
        entered = half[j, :, None]*product
        evolved = dst(decay[:, None]*dst(entered)) if form == "B" else drift@entered
        product = half[j, :, None]*evolved
    if not np.all(np.isfinite(product)):
        raise RuntimeError("Nonfinite heat product")
    arrays["C_tilde"] = product
    return arrays, record


def static_readout(arrays, target, helper, state_source):
    n = int(arrays["grid_n"])
    matrix = arrays["K"].copy()
    matrix.flat[::n+1] += float(arrays["theta"][2])+arrays["mean_W"]
    values, states_all = np.linalg.eigh(matrix, UPLO="L")
    if not np.all(np.isfinite(values)) or values[0] <= 0:
        raise RuntimeError("Invalid same-owner static spectrum")
    states = states_all[:, :320].copy()
    del states_all
    residual = np.linalg.norm(matrix@states-states*values[:320], axis=0)
    scale = float(target[0]/values[0])
    prediction = scale*values[:320]
    boundary, tail, occupation = state_source.occupation(states, arrays["q"], float(arrays["L"]))
    result = {key: arrays[key] for key in ("theta", "form_key", "grid_n", "L", "sample_count", "q", "p",
                                          "kinetic_minus_mass", "g", "R_diagonal", "profile", "mean_W", "schedule",
                                          "minimum_ids", "minimum_ledger_path", "target_100")}
    result.update(H_avg=matrix, energy=values, states=states, equation_residual=residual,
                  scale=np.array(scale), predicted_320=prediction, boundary_mass=boundary, high_momentum_mass=tail)
    record = {"N": n, "L": float(arrays["L"]), "B": int(arrays["sample_count"]), "theta": arrays["theta"].tolist(),
              "profile": str(arrays["profile"]), "E0": float(values[0]), "scale": scale,
              "equation_residual_max": float(np.max(residual)),
              "symmetry_relative_fro": float(np.linalg.norm(matrix-matrix.T)/np.linalg.norm(matrix)),
              "orthogonality_fro": float(np.linalg.norm(states.T@states-np.eye(320))),
              "eigh_triangle": "L; residual against full saved formula matrix, no explicit symmetrization",
              "occupation": occupation, "training_metrics": helper.metrics(prediction[:100], target),
              "not_separately_optimized": True, "no_selection": True,
              "static_owner": "mI + own R K0 R + diag(mean W)"}
    return result, record


def main():
    started = time.perf_counter()
    utilities = import_file("cs11_immutable_utilities", UTILITY_FILE)
    logging_test = utilities.logger_regression_test()
    locks, own_hash = verify_inputs(), sha(Path(__file__))
    if OUT.exists():
        raise RuntimeError("Output exists; refusing overwrite or retry")
    OUT.mkdir(parents=True)
    (OUT/"evaluations").mkdir()
    output = utilities.BoundedOutput(OUT, GIB)
    event_stream = output.text_stream("events.jsonl")
    ledger_stream = output.text_stream("minimum-ledger.jsonl")
    call_stream = output.text_stream("calls.jsonl")
    event = utilities.make_logger(event_stream, echo=True)
    stop = threading.Event()
    counters = {"propagations_attempted": 0, "propagations_completed": 0,
                "control_propagations_attempted": 0, "control_propagations_completed": 0,
                "training_propagations_attempted": 0, "training_propagations_completed": 0,
                "postfreeze_propagations_attempted": 0, "postfreeze_propagations_completed": 0,
                "full_svd_attempted": 0, "full_svd_completed": 0,
                "kinetic_eigh_attempted": 0, "kinetic_eigh_completed": 0,
                "control_arrays_saved": 0, "training_compact_grids_saved": 0, "full_heat_grids_saved": 0,
                "kinetic_full_grids_saved": 0, "static_readouts_attempted": 0,
                "static_readouts_completed": 0, "static_grids_saved": 0, "aliased_ablation_roles": 0}
    root_counts = {"minimum_cache_hits": 0, "minimum_solves_attempted": 0, "minimum_solves_completed": 0,
                   "brent_attempted": 0, "brent_returned": 0}
    end_verification = None

    def resources():
        while not stop.wait(30):
            rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            event("resource_sample", pid=os.getpid(), seconds=time.perf_counter()-started, maxrss_kib=rss,
                  memory_above_1gib_advisory=bool(rss*1024 > GIB), output_bytes=output.size(), counters=dict(counters))

    monitor = threading.Thread(target=resources, daemon=True)
    monitor.start()
    try:
        helper = import_file("cs11_immutable_readouts", HELPER_FILE)
        state_source = import_file("cs11_immutable_state_diagnostics", STATE_FILE)
        potential_source = import_file("cs11_immutable_polynomial_roots", POTENTIAL_FILE)
        cooling_source = helper.import_source()
        output.json("manifest.json", {"scope_id": SCOPE, "started_utc": utilities.utc(), "pid": os.getpid(),
                    "command": COMMAND, "script_sha256": own_hash, "input_locks_sha256": sha(LOCK_FILE), "inputs": locks,
                    "python": sys.version, "numpy": np.__version__, "scipy": scipy.__version__,
                    "thread_environment": {key: os.environ.get(key) for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")},
                    "forms": FORMS, "train_N": TRAIN_N, "post_N": POST_N, "beta": BETA, "L": LENGTH, "B": SAMPLES,
                    "M_ref": M_REF, "W_ref": W_REF, "G_ref_percent": G_REF, "max_pair_calls": 44,
                    "max_propagations": 102, "max_full_svd": 102, "max_kinetic_eigh": 54, "max_static_eigh": 12,
                    "M_kappa_zero_still_dense": True, "kinetic_eigh_cached_across_forwards": False,
                    "full_svd_type": "real, exactly one per propagation", "same_form_exact_cache_only": True,
                    "rest_mass_outside_congruence": True, "old_module_globals_mutated": False,
                    "old_main_or_optimizer_called": False, "nonwinner_C_K_P_Q_states_saved": False,
                    "static_owner": "mI + own R K0 R + diag(mean W)", "control_readout_count": 63,
                    "control_relative_sigma_ratio_diagnostic_only": True, "root_isolation_certified": False,
                    "kappa_zero_Z_F_policy": "explicit aliases of post-M-N1279, no new propagation/static or budget transfer",
                    "output_hard_limit_bytes": GIB, "memory_advisory_bytes": GIB, "timeout_seconds": 600,
                    "actual_exit_code": "recorded by launching parent", "logging_regression": logging_test,
                    "run_passport": "UNVERIFIED", "all_development_targets_previously_observed": True})
        output.json("logger-regression.json", logging_test)
        event("started", scope_id=SCOPE, pid=os.getpid())
        with np.load(helper.TARGET_SOURCE, allow_pickle=False) as old:
            target = old["target_100"].copy()
        if len(target) != 100 or not np.all(np.isfinite(target)) or target[0] <= 0 or not np.all(np.diff(target) > 0):
            raise RuntimeError("Invalid frozen target100")
        old_identity = json.loads((OLD/"winners-frozen.json").read_text())
        old_role = old_identity["roles"]["B"]
        if old_role["evaluation_id"] != "CS09-B-QUINTIC-REFIT-0055" or not np.array_equal(old_role["theta"], BASE):
            raise RuntimeError("Old B0055 identity/default mismatch")
        if abs(old_role["max_mape_percent"]-M_REF) > 1e-12 or abs(old_role["max_percent_error"]-W_REF) > 1e-12:
            raise RuntimeError("Same-owner benchmark constants mismatch")
        old_regression = {}
        for n in TRAIN_N:
            with np.load(OLD/"evaluations"/f"CS09-B-QUINTIC-REFIT-0055-N{n}.npz", allow_pickle=False) as old:
                if not np.array_equal(old["theta"], BASE) or not np.array_equal(old["target_100"], target):
                    raise RuntimeError("Old training grid identity/target mismatch")
                old_regression[n] = old["predicted_320"].copy()
        minimum_cache, minimum_ledger = {}, []

        def calculate(form, theta, n, length, count, stage, name, order="O", zero=False, profile="henon"):
            limits = {"control": 6, "training": 88, "postfreeze": 8}
            if counters["propagations_attempted"] >= 102 or counters[stage+"_propagations_attempted"] >= limits[stage]:
                raise RuntimeError("Frozen propagation budget exceeded")
            counters["propagations_attempted"] += 1
            counters[stage+"_propagations_attempted"] += 1
            event("propagation_start", name=name, stage=stage, form=form, theta=theta.tolist(), N=n, L=length,
                  B=count, order=order, profile=profile, counters=dict(counters))
            tick = time.perf_counter()
            arrays, record = propagate(potential_source, cooling_source, form, theta, n, length, count,
                                       minimum_cache, minimum_ledger, root_counts, ledger_stream, counters, event,
                                       name, order=order, zero=zero, profile=profile)
            counters["propagations_completed"] += 1
            counters[stage+"_propagations_completed"] += 1
            record["propagation_seconds_including_kinetic"] = time.perf_counter()-tick
            event("propagation_complete", name=name, stage=stage, counters=dict(counters))
            if counters["full_svd_attempted"] >= 102:
                raise RuntimeError("Frozen full SVD budget exceeded")
            counters["full_svd_attempted"] += 1
            tick = time.perf_counter()
            left, sigma, right_t = np.linalg.svd(arrays["C_tilde"], full_matrices=True)
            counters["full_svd_completed"] += 1
            record["full_svd_seconds"] = time.perf_counter()-tick
            retained = 63 if stage == "control" else 320
            arrays["_cached_left"], arrays["_cached_right"] = left[:, :retained].copy(), right_t[:retained].T.copy()
            del left, right_t
            readout, validity = helper.readout(sigma, float(theta[2]), BETA, target, retained)
            if stage == "control":
                reasons = [reason for reason in validity["invalid_reasons"]
                           if reason != "REQUIRED_RELATIVE_SINGULAR_VALUE_BELOW_1E-10"]
                readout.update(resolution_valid=np.array(not reasons), invalid_reasons=np.array(reasons, dtype=str))
                validity.update(status="VALID" if not reasons else "INVALID_RESOLUTION", resolution_valid=not reasons,
                                invalid_reasons=reasons, required_sigma_ratio_diagnostic_only=True)
            arrays.update(readout)
            record.update(validity)
            if stage != "control":
                record["training_metrics"] = helper.metrics(arrays["predicted_320"][:100], target) if validity["resolution_valid"] else None
            event("full_svd_complete", name=name, status=record["status"], counters=dict(counters))
            return arrays, record

        controls, control_arrays = {}, {}
        specifications = (("control-1-free-B", "B", 0., True, "O"), ("control-2-base", "B", 0., False, "O"),
                          ("control-3-M-zero", "M", 0., False, "O"), ("control-4-M-one", "M", 1., False, "O"),
                          ("control-5-M-reverse", "M", 1., False, "reverse"), ("control-6-free-M", "M", 1., True, "O"))
        for name, form, kappa, zero, order in specifications:
            theta = BASE.copy() if form == "B" else np.append(BASE, kappa)
            arrays, record = calculate(form, theta, 63, LENGTH, SAMPLES, "control", name, order=order, zero=zero)
            materialize_base_kinetic(arrays, record)
            state_source.add_states(arrays, record)
            checks = {"required_count": 63, "no_320_rejection": True, "relative_sigma_ratio_diagnostic_only": True,
                      "passed": bool(record["resolution_valid"])}
            if zero:
                expected_sigma = np.sort(np.exp(-BETA*arrays["kinetic_nu"]))[::-1]
                expected_energy = np.sort(BASE[2]+arrays["kinetic_nu"])
                sigma_error = float(np.max(np.abs(arrays["sigma"]-expected_sigma)))
                energy_error = float(np.max(np.abs(arrays["energy"]-expected_energy)))
                arrays.update(expected_sigma=expected_sigma, expected_energy=expected_energy)
                checks.update(sigma_max_absolute_difference=sigma_error, energy_max_absolute_difference=energy_error,
                              sigma_tolerance=1e-10, energy_tolerance=1e-8,
                              reference="analytic DST k" if form == "B" else "same single-eigh stored mobility nu",
                              passed=bool(record["resolution_valid"] and sigma_error <= 1e-10 and energy_error <= 1e-8))
            elif name in ("control-3-M-zero", "control-5-M-reverse"):
                reference = "control-2-base" if name == "control-3-M-zero" else "control-4-M-one"
                original = control_arrays[reference]
                expected = original["C_tilde"] if name == "control-3-M-zero" else original["C_tilde"].T
                sigma_error = float(np.max(np.abs(arrays["sigma"]-original["sigma"])))
                matrix_error = float(np.linalg.norm(arrays["C_tilde"]-expected))
                tolerance = 1e-10*max(1., float(np.linalg.norm(original["C_tilde"])))
                checks.update(reference=reference, sigma_max_absolute_difference=sigma_error,
                              matrix_frobenius_difference=matrix_error, sigma_tolerance=1e-10, matrix_tolerance=tolerance,
                              passed=bool(record["resolution_valid"] and sigma_error <= 1e-10 and matrix_error <= tolerance))
            else:
                checks["no_required_fit_or_order_gain"] = True
            record["control_checks"] = checks
            output.npz(name+".npz", arrays)
            output.json(name+".json", record)
            counters["control_arrays_saved"] += 1
            counters["kinetic_full_grids_saved"] += 1
            controls[name], control_arrays[name] = record, arrays
            event("control_saved", name=name, checks=checks, counters=dict(counters))
            if not checks["passed"]:
                raise RuntimeError("Frozen N63 control failed: "+name+"; no retry")
        control_arrays.clear()
        del arrays
        cache, best, seed_physical = {}, {}, {}
        call_rows, unique_rows = [], []
        calls, unique, regression = 0, 0, None

        def objective(form, normalized, stage, physical=None):
            nonlocal calls, unique, regression
            calls += 1
            lower, upper = bounds(form)
            normalized = np.asarray(normalized)
            normalized_key = form, *(float(value).hex() for value in normalized)
            if physical is not None:
                theta = np.asarray(physical).copy()
                seed_physical[normalized_key] = theta.copy()
            else:
                theta = seed_physical[normalized_key].copy() if normalized_key in seed_physical else lower+normalized*(upper-lower)
            if calls > 44 or not np.all(np.isfinite(theta)) or np.any(theta < lower) or np.any(theta > upper):
                raise RuntimeError("Frozen pair budget/parameter bounds violated")
            key = form, *(float(value).hex() for value in theta)
            if key in cache:
                row = dict(cache[key])
                row.update(call=calls, stage=stage, cached=True, source_evaluation_id=row["evaluation_id"])
                call_rows.append(row)
                call_stream.write(json.dumps(row, allow_nan=False)+"\n")
                event("cached_pair_call", call=calls, form=form, source_evaluation_id=row["evaluation_id"], joint_score=row["joint_score"])
                return row["joint_score"]
            unique += 1
            eid = f"{FORMS[form]}-{unique:04d}"
            pair_arrays, grids = {}, {}
            event("pair_start", evaluation_id=eid, call=calls, form=form, theta=theta.tolist(), stage=stage)
            tick = time.perf_counter()
            for n in TRAIN_N:
                arrays, grid = calculate(form, theta, n, LENGTH, SAMPLES, "training", f"{eid}-N{n}")
                arrays["evaluation_id"] = np.array(eid)
                compact_arrays = {name: value for name, value in arrays.items()
                                  if name not in ("C_tilde", "K", "P_delta", "kinetic_Q") and not name.startswith("_cached_")}
                output.npz(f"evaluations/{eid}-N{n}.npz", compact_arrays)
                grid.update(C_K_P_Q_states_saved=False, full_arrays_reconstruction="frozen code/theta/grid/own profile; not a stored full matrix")
                output.json(f"evaluations/{eid}-N{n}.json", grid)
                counters["training_compact_grids_saved"] += 1
                pair_arrays[n], grids[str(n)] = arrays, grid
            row = {"evaluation_id": eid, "form": FORMS[form], "form_key": form, "theta": theta.tolist(),
                   "normalized_x": normalized.tolist(), "call": calls, "stage": stage, "cached": False,
                   "grids": grids, "seconds_including_save": time.perf_counter()-tick, **pair_summary(grids, pair_arrays, target)}
            output.json(f"evaluations/{eid}.json", row)
            cache[key] = row
            call_rows.append(row)
            unique_rows.append(row)
            call_stream.write(json.dumps(row, allow_nan=False)+"\n")
            if row["resolution_valid"] and (form not in best or rank(row) < rank(best[form][1])):
                best[form] = (pair_arrays, row)
            if calls == 1:
                if form != "B" or not np.array_equal(theta, BASE):
                    raise RuntimeError("First member is not frozen B default")
                regression = {}
                for n in TRAIN_N:
                    prediction = pair_arrays[n]["predicted_320"]
                    old_metrics = helper.metrics(old_regression[n][:100], target)
                    new_metrics = helper.metrics(prediction[:100], target)
                    error = float(np.max(np.abs(prediction-old_regression[n])))
                    metric_error = max(abs(old_metrics[key]-new_metrics[key]) for key in ("mape_percent", "max_percent_error"))
                    regression[str(n)] = {"prediction320_max_absolute_difference": error,
                                           "first100_MW_max_absolute_difference": metric_error, "tolerance": 1e-6,
                                           "passed": bool(row["resolution_valid"] and error <= 1e-6 and metric_error <= 1e-6)}
                output.json("default-regression.json", regression)
                if not all(value["passed"] for value in regression.values()):
                    raise RuntimeError("Default B paired-grid regression failed; no retry")
            event("pair_complete", evaluation_id=eid, status=row["status"], joint_score=row["joint_score"],
                  J_minus_1=row["J_minus_1"], max_mape_percent=row["max_mape_percent"], max_percent_error=row["max_percent_error"])
            return row["joint_score"]

        wide = np.random.default_rng(20260928).uniform(0, 1, (2, 5))
        seeds = {}
        for form in FORMS:
            lower, upper = bounds(form)
            points = [default_theta(form)]
            if form == "B":
                for coordinate, value in ((0, .12), (0, .22), (2, .90)):
                    point = BASE.copy()
                    point[coordinate] = value
                    points.append(point)
            else:
                points.extend(np.append(BASE, value) for value in (-.6, .6, 1.5))
            points.extend(lower+row[:len(lower)]*(upper-lower) for row in wide)
            seeds[form] = points
        output.json("seed-design.json", {"rng_seed": 20260928, "wide_normalized_2x5": wide.tolist(),
                                         "physical_seeds": {form: [point.tolist() for point in points] for form, points in seeds.items()}})
        for index in range(6):
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
            event("optimizer_start", form=form, starting_member=best[form][1]["evaluation_id"], maxfev=16)
            optimized = minimize(lambda x: objective(form, x, "refine"), x0, method="Nelder-Mead",
                                 bounds=[(0., 1.)]*len(x0), options={"maxfev": 16, "initial_simplex": simplex,
                                 "xatol": 1e-6, "fatol": 1e-6, "adaptive": False})
            optimizers[form] = {"success": bool(optimized.success), "message": str(optimized.message),
                                "nfev": int(optimized.nfev), "nit": int(optimized.nit), "fun": float(optimized.fun)}
            event("optimizer_complete", form=form, optimizer=optimizers[form])
        primary = min(best, key=lambda form: rank(best[form][1])) if best else None
        roles = {form: row for form, (arrays, row) in best.items()}
        role_status = {form: "VALID_MEMBER" if form in roles else "NO_VALID_MEMBER" for form in FORMS}
        output.json("winners-frozen.json", {"scope_id": SCOPE, "frozen_utc": utilities.utc(), "global_joint_winner": primary,
                    "roles": roles, "role_status": role_status, "calls": calls, "unique_members": unique,
                    "optimizers": optimizers, "selection": "joint first100 N511/N639 only", "development_metrics_evaluated": False})
        identity_hash = sha(OUT/"winners-frozen.json")
        output.json("calls.json", call_rows)
        output.json("unique-members.json", unique_rows)
        event("winner_identities_frozen", sha256=identity_hash, primary=primary, role_status=role_status)
        members, metadata, heat_records, static_records, frozen_files = {}, {}, {}, {}, []

        def save_full(name, arrays, record, stage):
            event("winner_state_readout_start", name=name, not_a_propagation=True, no_additional_svd=True)
            materialize_base_kinetic(arrays, record)
            state_source.add_states(arrays, record)
            static_name = "static-"+name
            record.update(C_K_P_Q_states_saved=True, no_selection=True, static_owner_id=static_name,
                          static_source_path=static_name+".npz", sole_svd_spectrum_preserved=True)
            arrays["static_owner_id"], arrays["static_source_path"] = np.array(static_name), np.array(static_name+".npz")
            members[name] = helper.compact(arrays, record["resolution_valid"])
            metadata[name] = {"kind": "heat", "stage": stage, "form": record["form_key"], "N": int(arrays["grid_n"]),
                              "L": float(arrays["L"]), "B": int(arrays["sample_count"]), "profile": str(arrays["profile"])}
            output.npz(name+".npz", arrays)
            output.json(name+".json", record)
            counters["full_heat_grids_saved"] += 1
            counters["kinetic_full_grids_saved"] += 1
            heat_records[name] = record
            if counters["static_readouts_attempted"] >= 12:
                raise RuntimeError("Frozen static readout budget exceeded")
            counters["static_readouts_attempted"] += 1
            event("static_readout_start", name=name, counters=dict(counters))
            static_arrays, static_record = static_readout(arrays, target, helper, state_source)
            counters["static_readouts_completed"] += 1
            static_record.update(heat_owner=name, form_key=record["form_key"])
            static_arrays["kinetic_owner_source"] = np.array(name+".npz")
            members[static_name] = helper.compact(static_arrays)
            metadata[static_name] = {**metadata[name], "kind": "static"}
            output.npz(static_name+".npz", static_arrays)
            output.json(static_name+".json", static_record)
            counters["static_grids_saved"] += 1
            static_records[static_name] = static_record
            del static_arrays
            event("winner_state_readout_complete", name=name, counters=dict(counters))
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
            raise RuntimeError("Training array freeze file count mismatch")
        output.json("training-arrays-frozen.json", {"scope_id": SCOPE, "frozen_utc": utilities.utc(),
                    "winner_identity_file": "winners-frozen.json", "winner_identity_sha256": identity_hash,
                    "role_status": role_status, "full_heat_arrays": 2*len(roles), "full_static_arrays": 2*len(roles),
                    "file_count": len(frozen_files), "files_sha256": {name: sha(OUT/name) for name in frozen_files},
                    "development_metrics_evaluated": False, "counters": dict(counters)})
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
        with np.load(OLD/"post-B-N1279.npz", allow_pickle=False) as old:
            if not np.array_equal(old["theta"], BASE) or not np.array_equal(old["target_100"], target):
                raise RuntimeError("Old B0055 comparator identity mismatch")
            members["old-B0055-N1279"] = helper.compact(old, bool(old["resolution_valid"]))
            metadata["old-B0055-N1279"] = {"kind": "reused", "stage": "old-fixed-comparator", "form": "B0055", "N": 1279,
                                           "L": 8., "B": 64, "profile": "old-flat"}
        output.json("known-targets.json", {"first": 1, "last": 320, "ordinates": truth.tolist(),
                                           "all_previously_observed": True, "generated_by_this_run": False})
        post_records, aliases = {}, {}

        def post(form, n, length, count, name, theta_override=None, profile="henon", stage="fixed-postfreeze"):
            theta = np.array(roles[form]["theta"]) if theta_override is None else theta_override.copy()
            arrays, record = calculate(form, theta, n, length, count, "postfreeze", name, profile=profile)
            record.update(source_evaluation_id=roles[form]["evaluation_id"], no_selection=True)
            save_full(name, arrays, record, stage)
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
        if "M" in roles:
            theta = np.array(roles["M"]["theta"])
            if theta[4] == 0.:
                for label, profile in (("Z", "henon"), ("F", "constant_one")):
                    name, owner = f"ablation-M-{label}-N1279", "post-M-N1279"
                    static_name, static_owner = "static-"+name, "static-"+owner
                    aliases[name] = {"status": "ALIASED_EXACT_KAPPA_ZERO", "source_object": owner,
                                     "requested_profile": profile, "requested_theta": theta.tolist(),
                                     "source_npz": owner+".npz", "source_sha256": sha(OUT/(owner+".npz")),
                                     "static_source_object": static_owner, "static_source_npz": static_owner+".npz",
                                     "static_source_sha256": sha(OUT/(static_owner+".npz")),
                                     "reason": "kappa is exactly zero, so both requested multipliers are I",
                                     "additional_propagation": False, "additional_eigh": False, "budget_not_transferred": True}
                    members[name], members[static_name] = members[owner], members[static_owner]
                    metadata[name] = {**metadata[owner], "kind": "heat-alias", "stage": "fixed-ablation-alias", "profile": profile}
                    metadata[static_name] = {**metadata[static_owner], "kind": "static-alias", "stage": "fixed-ablation-alias", "profile": profile}
                    output.json(name+"-alias.json", aliases[name])
                    counters["aliased_ablation_roles"] += 1
                    event("ablation_alias_saved", name=name, source=owner, counters=dict(counters))
            else:
                zero_theta = theta.copy()
                zero_theta[4] = 0.
                post("M", 1279, 8., 64, "ablation-M-Z-N1279", theta_override=zero_theta, stage="fixed-zero-mobility-ablation")
                post("M", 1279, 8., 64, "ablation-M-F-N1279", theta_override=theta, profile="constant_one", stage="fixed-flat-profile-ablation")
        output.json("ablation-aliases.json", aliases)
        fits = {name: ({window: helper.metrics(member["prediction"][start:end], truth[start:end])
                        for window, (start, end) in helper.WINDOWS.items()} if member["valid"] else None)
                for name, member in members.items()}
        comparisons = {}
        for form in roles:
            for label, left, right in (("train-grid", f"winner-{form}-N511", f"winner-{form}-N639"),
                                       ("N639-N1023", f"winner-{form}-N639", f"post-{form}-N1023"),
                                       ("N1023-N1279", f"post-{form}-N1023", f"post-{form}-N1279"),
                                       ("old-baseline-N1279", "old-B0055-N1279", f"post-{form}-N1279")):
                comparisons[f"{form}-{label}"] = helper.compare(left, right, members, truth)
        for name, row in heat_records.items():
            comparisons["static-"+name] = helper.compare(name, row["static_owner_id"], members, truth)
        for name, alias in aliases.items():
            comparisons["static-"+name] = helper.compare(name, "static-"+name, members, truth)
        if primary is not None:
            for name in ("primary-time-N1279-B128", "primary-box-N1599-L10"):
                comparisons[name] = helper.compare(f"post-{primary}-N1279", name, members, truth)
        if "M" in roles:
            for label in ("Z", "F"):
                comparisons["M-versus-"+label] = helper.compare("post-M-N1279", f"ablation-M-{label}-N1279", members, truth)
        if all(form in roles for form in FORMS):
            comparisons["M-versus-refitted-B"] = helper.compare("post-M-N1279", "post-B-N1279", members, truth)
        structure = {"status": "NO_VALID_MEMBER"}
        if "M" in roles:
            kappa = roles["M"]["theta"][4]
            both = "B" in roles
            training_components = ({str(n): {key: {"M_value": roles["M"]["grids"][str(n)]["training_metrics"][key],
                                                  "B_value": roles["B"]["grids"][str(n)]["training_metrics"][key],
                                                  "M_minus_B": roles["M"]["grids"][str(n)]["training_metrics"][key]-roles["B"]["grids"][str(n)]["training_metrics"][key]}
                                             for key in ("mape_percent", "max_percent_error")} for n in TRAIN_N} if both else None)
            below = bool(both and all(item["M_value"] < item["B_value"] and item["M_value"] < (M_REF if key == "mape_percent" else W_REF)
                                     for row in training_components.values() for key, item in row.items()))
            full_valid = bool(both and fits["post-M-N1279"] is not None and fits["post-B-N1279"] is not None)
            development_better = bool(full_valid and fits["post-M-N1279"]["1-320"]["mape_percent"] < fits["post-B-N1279"]["1-320"]["mape_percent"])
            engineering_names = ["M-N1023-N1279"]+(["primary-time-N1279-B128", "primary-box-N1599-L10"] if primary == "M" else [])
            engineering = {name: (all(row["G_below_2_percent"] for row in comparisons[name]["windows"].values())
                                  if comparisons[name]["windows"] is not None else None) for name in engineering_names}
            necessary = bool(kappa != 0 and primary == "M" and below and development_better and all(value is True for value in engineering.values()))
            discretization = {}
            for name in ("post-M-N1023", "primary-time-N1279-B128", "primary-box-N1599-L10"):
                if name not in fits or (name.startswith("primary-") and primary != "M"):
                    continue
                discretization[name] = ({window: {key: fits[name][window][key]-fits["post-M-N1279"][window][key]
                                                  for key in ("mape_percent", "max_percent_error")}
                                         for window in helper.WINDOWS}
                                        if fits[name] is not None and fits["post-M-N1279"] is not None else None)
            structure = {"status": "NECESSARY_FINITE_CRITERIA_MET_MAGNITUDE_REVIEW_REQUIRED" if necessary else "NECESSARY_FINITE_CRITERIA_NOT_MET",
                         "kappa": kappa, "kappa_nonzero": kappa != 0., "M_is_global_primary": primary == "M",
                         "joint_score": roles["M"]["joint_score"], "J_minus_1": roles["M"]["joint_score"]-1,
                         "training_components": training_components, "both_training_M_W_below_refitted_B_and_old_reference": below,
                         "N1279_full320_M_below_refitted_B": development_better,
                         "engineering_all_windows": engineering, "necessary_finite_criteria_met": necessary,
                         "actual_discretization_metric_changes_percentage_points": discretization,
                         "micro_gain_not_certified_by_2_percent_line": True, "robust_structure_label_not_automatically_awarded": True,
                         "chronology_benefit_not_inferred": True, "F_not_optimized_uniform_kinetic_competitor": True}
        points = io.StringIO(newline="")
        writer = csv.writer(points)
        writer.writerow(["object_id", "kind", "stage", "form", "N", "L", "B", "profile", "resolution_valid", "index", "window",
                         "target", "predicted", "energy", "residual", "percent_error"])
        for name, member in members.items():
            meta = metadata[name]
            for index, (actual, prediction, energy) in enumerate(zip(truth, member["prediction"], member["energy"]), 1):
                window = "1-100" if index <= 100 else "101-300" if index <= 300 else "301-320"
                writer.writerow([name, meta["kind"], meta["stage"], meta["form"], meta["N"], meta["L"], meta["B"], meta["profile"],
                                 member["valid"], index, window, actual, prediction, energy, prediction-actual, 100*abs(prediction-actual)/actual])
        output.binary("points.csv", points.getvalue().encode("utf-8"))
        output.json("development-fit-metrics.json", fits)
        output.json("comparisons.json", comparisons)
        output.json("structure-assessment.json", structure)
        output.json("minimum-ledger.json", minimum_ledger)
        end_locks = verify_inputs()
        if end_locks != locks or sha(Path(__file__)) != own_hash or sha(OUT/"winners-frozen.json") != identity_hash:
            raise RuntimeError("Frozen input/source/identity changed during run")
        end_verification = {"input_count": len(locks), "all_input_hashes_match": True,
                            "script_sha256_unchanged": True, "winner_identity_sha256_unchanged": True}
        report = {"scope_id": SCOPE, "status": "completed" if len(roles) == len(FORMS) else "completed_with_missing_roles",
                  "run_passport": "UNVERIFIED", "global_joint_winner": primary, "roles": roles, "role_status": role_status,
                  "calls": calls, "unique_members": unique, "cached_calls": sum(row["cached"] for row in call_rows),
                  "invalid_unique_members": sum(not row["resolution_valid"] for row in unique_rows), "optimizers": optimizers,
                  "controls": controls, "default_regression": regression, "winner_identity_sha256": identity_hash,
                  "heat_readouts": heat_records, "static_readouts": static_records, "postfreeze": post_records,
                  "ablation_aliases": aliases, "fit_metrics": fits, "comparisons": comparisons, "structure_assessment": structure,
                  "counters": dict(counters), "root_counters": dict(root_counts), "end_verification": end_verification,
                  "seconds_before_final_serialization": time.perf_counter()-started,
                  "maxrss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "completed_utc": utilities.utc(),
                  "output_bytes_before_result": output.size(), "new_targets_generated": False,
                  "formal_route": "UNASSIGNED; B NOT INVOKED", "order_effect_not_claimed": True}
        output.json("result.json", report)
        stop.set()
        monitor.join(timeout=1)
        event("completed", primary=primary, seconds=report["seconds_before_final_serialization"], calls=calls,
              counters=dict(counters), output_bytes=output.size())
        inventory = {str(path.relative_to(OUT)): {"bytes": path.stat().st_size, "sha256": sha(path)}
                     for path in sorted(OUT.rglob("*")) if path.is_file()}
        output.json("file-inventory.json", {"scope_id": SCOPE, "inventory_excludes_itself": True, "files": inventory})
    except Exception as exc:
        try:
            event("failed", type=type(exc).__name__, message=str(exc), counters=dict(counters),
                  root_counters=dict(root_counts), end_verification=end_verification)
        except Exception as logging_exc:
            print(f"Could not append failure evidence: {type(logging_exc).__name__}: {logging_exc}", file=sys.stderr, flush=True)
        raise
    finally:
        stop.set()
        monitor.join(timeout=1)
        ledger_stream.close()
        call_stream.close()
        event_stream.close()


if __name__ == "__main__":
    main()
