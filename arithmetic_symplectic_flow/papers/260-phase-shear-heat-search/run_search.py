#!/usr/bin/env python3
"""CS10: frozen complex phase-shear heat search; no numerical work on import."""
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
POTENTIAL_FILE = ROOT/"papers/259-hyperbolic-tail-heat-search/run_search.py"
OLD = POTENTIAL_FILE.parent/"evidence/run-1"
SCOPE = "ASFS-DISCOVERY-20260919-CS10"
FORMS = {"B": "CS10-B-QUINTIC-REFIT", "S": "CS10-S-PHASE-SHEAR"}
BASE = np.array([.1639363246753303, 1.655042492001211, .5881152959703404, -.003369556173000019])
LOW4, HIGH4 = np.array([.12, 1.40, .30, -.006]), np.array([.22, 1.80, .90, .006])
TRAIN_N, POST_N = (511, 639), (1023, 1279)
BETA, LENGTH, SAMPLES = .02, 8., 64
M_REF, W_REF, G_REF, PENALTY = 1.695273790061038, 5.234299091683695, 2., 1e30
GIB = 1024**3
COMMAND = ("OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 "
           "PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 600s python -u "
           "papers/260-phase-shear-heat-search/run_search.py")


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
    return (LOW4.copy(), HIGH4.copy()) if form == "B" else (np.append(LOW4, 0.), np.append(HIGH4, .6))


def default_theta(form):
    return BASE.copy() if form == "B" else np.append(BASE, 0.)


def dst_columns(values):
    """The complex-linear extension of the real orthonormal DST-I."""
    real = fft.dst(values.real, type=1, axis=0, norm="ortho", workers=1)
    if np.iscomplexobj(values):
        imaginary = fft.dst(values.imag, type=1, axis=0, norm="ortho", workers=1)
        return real+1j*imaginary
    return real


def propagate(potential_source, cooling_source, form, theta, n, length, count,
              minimum_cache, ledger, roots, ledger_stream, order="O", repeats=1,
              mode="conjugated", zero=False):
    h, a_start, mass, z = map(float, theta[:4])
    amplitude = float(theta[4]) if form == "S" else 0.
    q = -length+2*length*np.arange(1, n+1)/(n+1)
    p = np.pi*h*np.arange(1, n+1)/(2*length)
    kinetic = p*p/(np.hypot(mass, p)+mass)
    midpoint, schedule = cooling_source.cooling(a_start, count)
    chi = np.full(count, amplitude) if mode == "constant" else amplitude*np.sin(2*np.pi*midpoint)
    phases = np.exp(1j*chi[:, None]*q[None, :]**2/(2*h))
    shifted = np.zeros((count, n))
    ids, minimum_values, minimizers = [], [], []
    clipped_count, maximum_clip = 0, 0.
    for index, a in enumerate(schedule):
        if zero:
            continue
        row = potential_source.global_minimum("B", float(a), z, 0., minimum_cache, ledger, roots, ledger_stream)
        raw = potential_source.potential("B", q, float(a), z, 0.)-row["minimum"]
        if not np.all(np.isfinite(raw)) or np.min(raw) < -1e-10:
            raise RuntimeError("Nonfinite shifted potential or W below -1e-10")
        negative = raw < 0.
        clipped_count += int(np.count_nonzero(negative))
        if np.any(negative):
            maximum_clip = max(maximum_clip, float(np.max(-raw[negative])))
        shifted[index] = np.maximum(raw, 0.)
        ids.append(row["minimum_id"])
        minimum_values.append(row["minimum"])
        minimizers.append(row["minimizer"])
    if order == "O":
        indices = np.arange(count)
    elif order == "P":
        indices = np.concatenate((np.arange(0, count, 2), np.arange(1, count, 2)))
    elif order == "reverse":
        indices = np.arange(count-1, -1, -1)
    else:
        raise ValueError("Unknown frozen sample order")
    if repeats not in (1, 2) or (mode == "transport" and repeats != 1):
        raise ValueError("Unsupported frozen repeat/transport combination")
    if mode not in ("conjugated", "constant", "transport"):
        raise ValueError("Unknown phase mode")
    sequence = np.repeat(indices, repeats)
    delta = BETA/(count*repeats)
    half_kicks = np.exp(-.5*delta*shifted)
    decay = np.exp(-delta*kinetic)
    product = np.eye(n, dtype=np.complex128)
    previous_phase = np.ones(n, dtype=np.complex128)
    for index in sequence:
        g = phases[index]
        right_phase = previous_phase.conj() if mode == "transport" else g.conj()
        entered = half_kicks[index, :, None]*(right_phase[:, None]*product)
        modes = dst_columns(entered)
        drifted = dst_columns(decay[:, None]*modes)
        product = g[:, None]*(half_kicks[index, :, None]*drifted)
        previous_phase = g
    if not np.all(np.isfinite(product)):
        raise RuntimeError("Nonfinite complex heat product")
    arrays = {"theta": np.asarray(theta).copy(), "form_key": np.array(form), "grid_n": np.array(n),
              "L": np.array(length), "sample_count": np.array(count), "beta": np.array(BETA),
              "q": q, "p": p, "kinetic_minus_mass": kinetic, "midpoint_u": midpoint, "schedule": schedule,
              "chi": chi, "phase_diagonal_samples": phases, "W_samples": shifted, "mean_W": np.mean(shifted, axis=0),
              "C_tilde": product, "minimum_ids": np.array(ids, dtype=np.int64),
              "minimum_values": np.array(minimum_values), "minimizers": np.array(minimizers),
              "minimum_ledger_path": np.array("minimum-ledger.jsonl"), "sample_order_zero_based": indices,
              "sample_order_one_based": indices+1, "fine_step_sample_indices_zero_based": sequence,
              "repeats": np.array(repeats), "delta": np.array(delta), "order_name": np.array(order),
              "phase_mode": np.array(mode), "potential_mode": np.array("zero_control" if zero else "global_minimum_shift")}
    record = {"form_key": form, "form": FORMS[form], "theta": list(map(float, theta)), "N": n, "L": length,
              "B": count, "beta": BETA, "order": order, "repeats": repeats, "fine_steps": len(sequence),
              "phase_mode": mode, "delta": delta, "minimum_ids": ids,
              "potential_clipped_count": clipped_count, "potential_maximum_clip": maximum_clip,
              "first_midpoint_a": float(schedule[0]), "last_midpoint_a": float(schedule[-1]),
              "spatial_step": 2*length/(n+1), "p_max": float(p[-1]),
              "max_phase_unit_modulus_error": float(np.max(np.abs(np.abs(phases)-1))),
              "phase_grid_upper_bound": float(np.max(np.abs(chi))*length*(2*length/(n+1))/h),
              "phase_grid_bound_is_diagnostic_only": True,
              "paired_samples_permutation_check": bool(np.array_equal(np.sort(indices), np.arange(count))),
              "normalized_fine_step_multiplicities_equal": bool(np.array_equal(np.bincount(sequence, minlength=count), np.full(count, repeats)))}
    return arrays, record


def occupation(states, q, length):
    n, retained = states.shape
    boundary = np.sum(np.abs(states[np.abs(q) > .9*length])**2, axis=0)
    modes = dst_columns(states)
    tail_count = (n+4)//5
    tail = np.sum(np.abs(modes[-tail_count:])**2, axis=0)
    summary = {"highest_mode_count": tail_count, "rounding": "ceil(N/5)", "boundary": "abs(q)>0.9L",
               "momentum_basis": "fixed laboratory Dirichlet DST basis; not a gauge-invariant cutoff bound", "windows": {}}
    for count in (100, 320):
        if count <= retained:
            summary["windows"][str(count)] = {"boundary_max": float(np.max(boundary[:count])),
                                              "boundary_mean": float(np.mean(boundary[:count])),
                                              "momentum_max": float(np.max(tail[:count])),
                                              "momentum_mean": float(np.mean(tail[:count]))}
    return boundary, tail, summary


def nullable(value):
    value = float(value)
    return value if math.isfinite(value) else None


def add_states(arrays, record):
    left, right = arrays.pop("_cached_left"), arrays.pop("_cached_right")
    product, sigma = arrays["C_tilde"], arrays["sigma"]
    retained = left.shape[1]
    forward = np.linalg.norm(product@right-left*sigma[:retained], axis=0)
    adjoint = np.linalg.norm(product.conj().T@left-right*sigma[:retained], axis=0)
    denominator = float(sigma[0])
    forward_relative = forward/denominator if denominator > 0 and math.isfinite(denominator) else np.full(retained, np.nan)
    adjoint_relative = adjoint/denominator if denominator > 0 and math.isfinite(denominator) else np.full(retained, np.nan)
    lb, lt, ls = occupation(left, arrays["q"], float(arrays["L"]))
    rb, rt, rs = occupation(right, arrays["q"], float(arrays["L"]))
    fro = float(np.sum(np.abs(product)**2))
    moment = float(np.sum(sigma*sigma))
    arrays.update(singular_left=left, singular_right=right, singular_forward_residual=forward,
                  singular_adjoint_residual=adjoint, singular_forward_residual_over_sigma0=forward_relative,
                  singular_adjoint_residual_over_sigma0=adjoint_relative,
                  left_boundary_mass=lb, left_high_momentum_mass=lt, right_boundary_mass=rb, right_high_momentum_mass=rt)
    record.update(retained_singular_states=retained, sole_svd_spectrum_preserved=True, no_additional_svd=True,
                  singular_forward_residual_max=nullable(np.max(forward)), singular_adjoint_residual_max=nullable(np.max(adjoint)),
                  singular_forward_relative_max=nullable(np.max(forward_relative)), singular_adjoint_relative_max=nullable(np.max(adjoint_relative)),
                  left_orthogonality_fro=float(np.linalg.norm(left.conj().T@left-np.eye(retained))),
                  right_orthogonality_fro=float(np.linalg.norm(right.conj().T@right-np.eye(retained))),
                  left_occupation=ls, right_occupation=rs, matrix_frobenius_squared=fro, full_sigma_squared_sum=moment,
                  frobenius_moment_relative_difference=nullable(abs(fro-moment)/fro) if fro > 0 else None,
                  partial_states_are_not_full_reconstruction=True)


def static_readout(arrays, target, metrics):
    n = int(arrays["grid_n"])
    modes = dst_columns(np.eye(n))
    kinetic_matrix = dst_columns(arrays["kinetic_minus_mass"][:, None]*modes)
    del modes
    phases = arrays["phase_diagonal_samples"]
    phase_correlation = phases.T@phases.conj()/len(phases)
    matrix = kinetic_matrix*phase_correlation
    del kinetic_matrix, phase_correlation
    matrix.flat[::n+1] += float(arrays["theta"][2])+arrays["mean_W"]
    if not np.all(np.isfinite(matrix)):
        raise RuntimeError("Nonfinite same-parameter averaged Hermitian matrix")
    values, states_all = np.linalg.eigh(matrix, UPLO="L")
    if not np.all(np.isfinite(values)) or values[0] <= 0:
        raise RuntimeError("Invalid static spectrum")
    states = states_all[:, :320].copy()
    del states_all
    residual = np.linalg.norm(matrix@states-states*values[:320], axis=0)
    scale = float(target[0]/values[0])
    prediction = scale*values[:320]
    boundary, tail, summary = occupation(states, arrays["q"], float(arrays["L"]))
    result = {key: arrays[key] for key in ("theta", "form_key", "grid_n", "L", "sample_count", "q", "p",
                                          "kinetic_minus_mass", "mean_W", "schedule", "chi", "phase_diagonal_samples",
                                          "minimum_ids", "minimum_ledger_path", "target_100")}
    result.update(H_avg=matrix, energy=values, states=states, equation_residual=residual, scale=np.array(scale),
                  predicted_320=prediction, boundary_mass=boundary, high_momentum_mass=tail)
    record = {"N": n, "L": float(arrays["L"]), "B": int(arrays["sample_count"]), "theta": arrays["theta"].tolist(),
              "E0": float(values[0]), "scale": scale, "equation_residual_max": float(np.max(residual)),
              "hermiticity_relative_fro": float(np.linalg.norm(matrix-matrix.conj().T)/np.linalg.norm(matrix)),
              "eigh_triangle": "L; residual evaluated against full saved formula matrix, no explicit symmetrization",
              "orthogonality_fro": float(np.linalg.norm(states.conj().T@states-np.eye(320))),
              "occupation": summary, "training_metrics": metrics(prediction[:100], target),
              "not_separately_optimized": True, "no_selection": True,
              "static_owner": "mI + K elementwise mean(G_r conjugate(G_t)) + diag(mean W)"}
    return result, record


def rank(row):
    if not row["resolution_valid"]:
        raise ValueError("Invalid pair cannot enter winner ranking")
    return (row["joint_score"], row["max_mape_percent"], row["max_percent_error"], row["cross_grid_percent"], row["evaluation_id"])


def pair_summary(grids, arrays, target):
    if not all(grids[str(n)]["resolution_valid"] for n in TRAIN_N):
        return {"status": "INVALID_RESOLUTION", "resolution_valid": False, "joint_score": PENALTY, "J_minus_1": None,
                "max_mape_percent": None, "max_percent_error": None, "cross_grid_percent": None, "benchmark_differences": None}
    m = [grids[str(n)]["training_metrics"]["mape_percent"] for n in TRAIN_N]
    w = [grids[str(n)]["training_metrics"]["max_percent_error"] for n in TRAIN_N]
    gap = float(100*np.max(np.abs(arrays[511]["predicted_320"][:100]-arrays[639]["predicted_320"][:100])/target))
    joint = max(m[0]/M_REF, m[1]/M_REF, w[0]/W_REF, w[1]/W_REF, gap/G_REF)
    return {"status": "VALID", "resolution_valid": True, "joint_score": joint, "J_minus_1": joint-1,
            "max_mape_percent": max(m), "max_percent_error": max(w), "cross_grid_percent": gap,
            "benchmark_differences": {str(n): {"M_minus_M_ref_percentage_points": m[index]-M_REF,
                                                 "W_minus_W_ref_percentage_points": w[index]-W_REF}
                                      for index, n in enumerate(TRAIN_N)}}


def raw_energy_comparison(left_name, right_name, members, windows):
    left, right = members[left_name], members[right_name]
    valid = left["valid"] and right["valid"]
    row = {"left": left_name, "right": right_name, "status": "VALID" if valid else "UNASSESSABLE_INVALID_RESOLUTION",
           "quantity": "100 max abs(E_left-E_right)/E_left", "uses_target_or_scale": False,
           "left_invalid_reasons": left["invalid_reasons"], "right_invalid_reasons": right["invalid_reasons"], "windows": None}
    if valid:
        row["windows"] = {name: float(100*np.max(np.abs(left["energy"][start:stop]-right["energy"][start:stop])/left["energy"][start:stop]))
                          for name, (start, stop) in windows.items()}
    return row


def main():
    started = time.perf_counter()
    utilities = import_file("cs10_immutable_utilities", UTILITY_FILE)
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
                "probe_propagations_attempted": 0, "probe_propagations_completed": 0,
                "full_svd_attempted": 0, "full_svd_completed": 0, "control_arrays_saved": 0,
                "training_compact_grids_saved": 0, "full_heat_grids_saved": 0,
                "static_readouts_attempted": 0, "static_readouts_completed": 0, "static_grids_saved": 0}
    root_counts = {"minimum_cache_hits": 0, "minimum_solves_attempted": 0, "minimum_solves_completed": 0,
                   "brent_attempted": 0, "brent_returned": 0}
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
        helper = import_file("cs10_immutable_readouts", HELPER_FILE)
        potential_source = import_file("cs10_immutable_polynomial_roots", POTENTIAL_FILE)
        cooling_source = helper.import_source()
        manifest = {"scope_id": SCOPE, "started_utc": utilities.utc(), "pid": os.getpid(), "command": COMMAND,
                    "script_sha256": own_hash, "input_locks_sha256": sha(LOCK_FILE), "inputs": locks,
                    "python": sys.version, "numpy": np.__version__, "scipy": scipy.__version__,
                    "thread_environment": {key: os.environ.get(key) for key in
                                           ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")},
                    "forms": FORMS, "train_N": TRAIN_N, "post_N": POST_N, "beta": BETA, "L": LENGTH, "B": SAMPLES,
                    "M_ref": M_REF, "W_ref": W_REF, "G_ref_percent": G_REF,
                    "max_pair_calls": 54, "max_propagations": 124, "max_full_svd": 124, "max_static": 11,
                    "full_svd_type": "complex128, exactly one per propagation",
                    "complex_DST": "orthonormal DST-I applied separately to real/imaginary parts",
                    "same_form_exact_spectrum_cache_only": True, "new_complex_state_and_static_helpers": True,
                    "old_module_globals_mutated": False, "old_main_or_optimizer_called": False,
                    "nonwinner_C_states_G_table_saved": False,
                    "nonwinner_reconstruction": "frozen code/theta/grid/schedule/chi/W; no reconstruction rerun here",
                    "static_owner": "mean G_j K G_j* + mI + mean W; not old untransformed K",
                    "probe": "fixed CS10-PROBE-S06; independent of selected shear amplitude",
                    "probe_static_readouts": 1, "probe_permutation_moves_whole_a_chi_pairs": True,
                    "control_readout_count": 63, "root_isolation_certified": False,
                    "output_hard_limit_bytes": GIB, "memory_advisory_bytes": GIB, "timeout_seconds": 600,
                    "actual_exit_code": "recorded by launching parent", "logging_regression": logging_test,
                    "run_passport": "UNVERIFIED", "all_development_targets_previously_observed": True}
        output.json("manifest.json", manifest)
        output.json("logger-regression.json", logging_test)
        event("started", scope_id=SCOPE, pid=os.getpid())
        with np.load(helper.TARGET_SOURCE, allow_pickle=False) as old:
            target = old["target_100"].copy()
        if len(target) != 100 or target[0] <= 0 or not np.all(np.isfinite(target)) or not np.all(np.diff(target) > 0):
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

        def calculate(form, theta, n, length, count, stage, name, order="O", repeats=1, mode="conjugated", zero=False):
            limits = {"control": 6, "training": 108, "postfreeze": 6, "probe": 4}
            if counters["propagations_attempted"] >= 124 or counters[stage+"_propagations_attempted"] >= limits[stage]:
                raise RuntimeError("Frozen propagation budget exceeded")
            counters["propagations_attempted"] += 1
            counters[stage+"_propagations_attempted"] += 1
            event("propagation_start", name=name, stage=stage, form=form, theta=theta.tolist(), N=n, L=length,
                  B=count, order=order, repeats=repeats, phase_mode=mode, counters=dict(counters))
            tick = time.perf_counter()
            arrays, record = propagate(potential_source, cooling_source, form, theta, n, length, count,
                                       minimum_cache, minimum_ledger, root_counts, ledger_stream, order, repeats, mode, zero)
            counters["propagations_completed"] += 1
            counters[stage+"_propagations_completed"] += 1
            record["propagation_seconds"] = time.perf_counter()-tick
            event("propagation_complete", name=name, stage=stage, counters=dict(counters))
            if counters["full_svd_attempted"] >= 124:
                raise RuntimeError("Frozen full SVD budget exceeded")
            counters["full_svd_attempted"] += 1
            tick = time.perf_counter()
            left_all, sigma, right_h_all = np.linalg.svd(arrays["C_tilde"], full_matrices=True)
            counters["full_svd_completed"] += 1
            record["full_svd_seconds"] = time.perf_counter()-tick
            retained = 63 if stage == "control" else 320
            arrays["_cached_left"] = left_all[:, :retained].copy()
            arrays["_cached_right"] = right_h_all[:retained].conj().T.copy()
            del left_all, right_h_all
            readout, validity = helper.readout(sigma, float(theta[2]), BETA, target, retained)
            if stage == "control":
                # The frozen relative-resolution threshold is a 320-state gate,
                # not an additional rejection rule for the N63 algebraic nulls.
                reasons = [reason for reason in validity["invalid_reasons"]
                           if reason != "REQUIRED_RELATIVE_SINGULAR_VALUE_BELOW_1E-10"]
                readout.update(resolution_valid=np.array(not reasons), invalid_reasons=np.array(reasons, dtype=str))
                validity.update(status="VALID" if not reasons else "INVALID_RESOLUTION",
                                resolution_valid=not reasons, invalid_reasons=reasons,
                                required_sigma_ratio_diagnostic_only=True)
            arrays.update(readout)
            record.update(validity)
            if stage != "control":
                record["training_metrics"] = helper.metrics(arrays["predicted_320"][:100], target) if validity["resolution_valid"] else None
            event("full_svd_complete", name=name, status=record["status"], counters=dict(counters))
            return arrays, record

        controls, control_arrays = {}, {}
        control_specs = (
            ("control-1-free", "B", True, "conjugated", "O"),
            ("control-2-base", "B", False, "conjugated", "O"),
            ("control-3-shear", "S", False, "conjugated", "O"),
            ("control-4-constant", "S", False, "constant", "O"),
            ("control-5-transport", "S", False, "transport", "O"),
            ("control-6-reverse", "S", False, "conjugated", "reverse"),
        )
        for name, form, zero, mode, order in control_specs:
            theta = BASE.copy() if form == "B" else np.append(BASE, .6)
            arrays, record = calculate(form, theta, 63, LENGTH, SAMPLES, "control", name, order=order, mode=mode, zero=zero)
            add_states(arrays, record)
            checks = {"readout_uses_only_63_states": True, "resolution63_valid": record["resolution_valid"]}
            if name == "control-1-free":
                expected_sigma = np.sort(np.exp(-BETA*arrays["kinetic_minus_mass"]))[::-1]
                expected_energy = np.sort(BASE[2]+arrays["kinetic_minus_mass"])
                sigma_error = float(np.max(np.abs(arrays["sigma"]-expected_sigma)))
                energy_error = float(np.max(np.abs(arrays["energy"]-expected_energy)))
                arrays.update(expected_sigma=expected_sigma, expected_energy=expected_energy)
                checks.update(sigma_max_absolute_difference=sigma_error, energy_max_absolute_difference=energy_error,
                              sigma_tolerance=1e-10, energy_tolerance=1e-8,
                              passed=bool(record["resolution_valid"] and sigma_error <= 1e-10 and energy_error <= 1e-8))
            elif name == "control-4-constant":
                error = float(np.max(np.abs(arrays["sigma"]-control_arrays["control-2-base"]["sigma"])))
                checks.update(sigma_max_absolute_difference=error, sigma_tolerance=1e-10,
                              passed=bool(record["resolution_valid"] and error <= 1e-10))
            elif name == "control-5-transport":
                original = control_arrays["control-2-base"]
                expected = arrays["phase_diagonal_samples"][-1, :, None]*original["C_tilde"]
                sigma_error = float(np.max(np.abs(arrays["sigma"]-original["sigma"])))
                matrix_error = float(np.linalg.norm(arrays["C_tilde"]-expected))
                tolerance = 1e-10*max(1., float(np.linalg.norm(original["C_tilde"])))
                arrays["expected_transport_matrix"] = expected
                checks.update(sigma_max_absolute_difference=sigma_error, matrix_frobenius_difference=matrix_error,
                              sigma_tolerance=1e-10, matrix_tolerance=tolerance,
                              passed=bool(record["resolution_valid"] and sigma_error <= 1e-10 and matrix_error <= tolerance))
            elif name == "control-6-reverse":
                original = control_arrays["control-3-shear"]
                expected = original["C_tilde"].conj().T
                sigma_error = float(np.max(np.abs(arrays["sigma"]-original["sigma"])))
                matrix_error = float(np.linalg.norm(arrays["C_tilde"]-expected))
                tolerance = 1e-10*max(1., float(np.linalg.norm(original["C_tilde"])))
                arrays["expected_reverse_matrix"] = expected.copy()
                checks.update(sigma_max_absolute_difference=sigma_error, matrix_frobenius_difference=matrix_error,
                              sigma_tolerance=1e-10, matrix_tolerance=tolerance,
                              passed=bool(record["resolution_valid"] and sigma_error <= 1e-10 and matrix_error <= tolerance))
            else:
                checks["passed"] = bool(record["resolution_valid"])
                checks["no_required_shear_spectral_difference"] = True
            record["control_checks"] = checks
            output.npz(name+".npz", arrays)
            output.json(name+".json", record)
            counters["control_arrays_saved"] += 1
            controls[name] = record
            control_arrays[name] = arrays
            event("control_saved", name=name, checks=checks, counters=dict(counters))
            if not checks["passed"]:
                raise RuntimeError("Frozen N63 control failed: "+name+"; no retry")
        control_arrays.clear()
        del arrays
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
            if calls > 54 or not np.all(np.isfinite(theta)) or np.any(theta < lower) or np.any(theta > upper):
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
                                  if name not in ("C_tilde", "phase_diagonal_samples") and not name.startswith("_cached_")}
                output.npz(f"evaluations/{eid}-N{n}.npz", compact_arrays)
                grid.update(C_and_states_saved=False, G_table_reconstruction="exp(i chi_j q_r^2/(2 h)); no grid-fitted phases")
                output.json(f"evaluations/{eid}-N{n}.json", grid)
                counters["training_compact_grids_saved"] += 1
                pair_arrays[n], grids[str(n)] = arrays, grid
            row = {"evaluation_id": eid, "form": FORMS[form], "form_key": form, "theta": theta.tolist(),
                   "normalized_x": x.tolist(), "call": calls, "stage": stage, "cached": False, "grids": grids,
                   "seconds_including_save": time.perf_counter()-tick, **pair_summary(grids, pair_arrays, target)}
            output.json(f"evaluations/{eid}.json", row)
            cache[key] = row
            call_rows.append(row)
            unique_rows.append(row)
            call_stream.write(json.dumps(row, allow_nan=False)+"\n")
            if row["resolution_valid"] and (form not in best or rank(row) < rank(best[form][1])):
                best[form] = (pair_arrays, row)
            if calls == 1:
                if form != "B" or not np.array_equal(theta, BASE):
                    raise RuntimeError("First member is not the frozen B default")
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
                if not all(value["passed"] for value in regression.values()):
                    raise RuntimeError("Default B paired-grid regression failed; no retry")
            event("pair_complete", evaluation_id=eid, status=row["status"], joint_score=row["joint_score"],
                  J_minus_1=row["J_minus_1"], max_mape_percent=row["max_mape_percent"], max_percent_error=row["max_percent_error"])
            return row["joint_score"]

        wide = np.random.default_rng(20260927).uniform(0, 1, (3, 5))
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
                points.extend(np.append(BASE, amplitude) for amplitude in (.15, .35, .6))
            points.extend(lower+row[:len(lower)]*(upper-lower) for row in wide)
            seeds[form] = points
        output.json("seed-design.json", {"rng_seed": 20260927, "wide_normalized_3x5": wide.tolist(),
                                         "physical_seeds": {form: [point.tolist() for point in points] for form, points in seeds.items()}})
        for index in range(7):
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
            event("optimizer_start", form=form, starting_member=best[form][1]["evaluation_id"], maxfev=20)
            optimized = minimize(lambda x: objective(form, x, "refine"), x0, method="Nelder-Mead",
                                 bounds=[(0., 1.)]*len(x0), options={"maxfev": 20, "initial_simplex": simplex,
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
                  "development_metrics_evaluated": False, "probe_cannot_replace_winner": True}
        output.json("winners-frozen.json", frozen)
        identity_hash = sha(OUT/"winners-frozen.json")
        output.json("calls.json", call_rows)
        output.json("unique-members.json", unique_rows)
        event("winner_identities_frozen", sha256=identity_hash, primary=primary, role_status=role_status)
        members, metadata, heat_records, static_records, frozen_files = {}, {}, {}, {}, []

        def save_full(name, arrays, record, stage, make_static=True, static_owner=None):
            event("winner_state_readout_start", name=name, not_a_propagation=True, no_additional_svd=True)
            add_states(arrays, record)
            record.update(C_and_states_saved=True, sole_svd_spectrum_preserved=True, no_selection=True)
            static_name = "static-"+name if make_static else static_owner
            record.update(static_owner_id=static_name, static_source_path=static_name+".npz")
            arrays["static_owner_id"] = np.array(static_name)
            arrays["static_source_path"] = np.array(static_name+".npz")
            members[name] = helper.compact(arrays, record["resolution_valid"])
            metadata[name] = {"kind": "heat", "stage": stage, "form": record["form_key"], "N": int(arrays["grid_n"]),
                              "L": float(arrays["L"]), "B": int(arrays["sample_count"]), "repeats": int(arrays["repeats"])}
            output.npz(name+".npz", arrays)
            output.json(name+".json", record)
            counters["full_heat_grids_saved"] += 1
            heat_records[name] = record
            files = [name+".npz", name+".json"]
            if make_static:
                if counters["static_readouts_attempted"] >= 11:
                    raise RuntimeError("Frozen static readout budget exceeded")
                counters["static_readouts_attempted"] += 1
                event("static_readout_start", name=name, counters=dict(counters))
                static_arrays, static_record = static_readout(arrays, target, helper.metrics)
                counters["static_readouts_completed"] += 1
                static_record.update(heat_owner=name, form_key=record["form_key"], phase_grid_upper_bound=record["phase_grid_upper_bound"])
                members[static_name] = helper.compact(static_arrays)
                metadata[static_name] = {**metadata[name], "kind": "static"}
                output.npz(static_name+".npz", static_arrays)
                output.json(static_name+".json", static_record)
                counters["static_grids_saved"] += 1
                static_records[static_name] = static_record
                del static_arrays
                files.extend([static_name+".npz", static_name+".json"])
            event("winner_state_readout_complete", name=name, counters=dict(counters))
            return files

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
        with np.load(OLD/"post-B-N1279.npz", allow_pickle=False) as old:
            if not np.array_equal(old["theta"], BASE) or not np.array_equal(old["target_100"], target):
                raise RuntimeError("Old fixed B0055 comparator identity mismatch")
            members["old-B0055-N1279"] = helper.compact(old, bool(old["resolution_valid"]))
            metadata["old-B0055-N1279"] = {"kind": "reused", "stage": "old-fixed-comparator", "form": "B0055", "N": 1279, "L": 8., "B": 64, "repeats": 1}
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
        probe_records = {}
        probe_reference = None
        probe_keys = ("theta", "q", "p", "kinetic_minus_mass", "midpoint_u", "schedule", "chi",
                      "W_samples", "mean_W", "minimum_values", "minimizers", "phase_diagonal_samples")
        for order, repeats in (("O", 1), ("P", 1), ("O", 2), ("P", 2)):
            name = f"probe-{order}-r{repeats}"
            arrays, record = calculate("S", np.append(BASE, .6), 1023, 8., 64, "probe", name, order=order, repeats=repeats)
            if probe_reference is None:
                probe_reference = {key: arrays[key].copy() for key in probe_keys}
            sample_checks = {key: bool(np.array_equal(arrays[key], probe_reference[key])) for key in probe_keys}
            if not all(sample_checks.values()) or not record["paired_samples_permutation_check"] or not record["normalized_fine_step_multiplicities_equal"]:
                raise RuntimeError("Probe pair multiset/repetition contract failed")
            record.update(probe_id="CS10-PROBE-S06", no_selection=True, exact_base_sample_checks=sample_checks,
                          same_static_owner_reason="same base samples and equal normalized multiplicity; whole (a,chi) pairs permuted; repeats only split each pair")
            save_full(name, arrays, record, "fixed-nonzero-mechanism-probe", make_static=(order == "O" and repeats == 1),
                      static_owner="static-probe-O-r1")
            probe_records[name] = record
            del arrays
            gc.collect()
        del probe_reference
        fits = {name: ({window: helper.metrics(member["prediction"][start:stop], truth[start:stop])
                        for window, (start, stop) in helper.WINDOWS.items()} if member["valid"] else None)
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
        if primary is not None:
            for name in ("primary-time-N1279-B128", "primary-box-N1599-L10"):
                comparisons[name] = helper.compare(f"post-{primary}-N1279", name, members, truth)
        mechanism_pairs = {"order_r1": ("probe-O-r1", "probe-P-r1"), "order_r2": ("probe-O-r2", "probe-P-r2"),
                           "O_refinement": ("probe-O-r1", "probe-O-r2"), "P_refinement": ("probe-P-r1", "probe-P-r2")}
        mechanism_comparisons = {name: raw_energy_comparison(left, right, members, helper.WINDOWS)
                                for name, (left, right) in mechanism_pairs.items()}
        mechanism = {}
        for window in helper.WINDOWS:
            invalid = [name for name, row in mechanism_comparisons.items() if row["windows"] is None]
            if invalid:
                mechanism[window] = {"status": "UNASSESSABLE_INVALID_RESOLUTION", "invalid_dependency_comparisons": invalid}
                continue
            delta = mechanism_comparisons["order_r2"]["windows"][window]
            epsilon = max(mechanism_comparisons[name]["windows"][window] for name in ("O_refinement", "P_refinement"))
            threshold = max(1e-6, 10*epsilon)
            mechanism[window] = {"Delta_percent": delta, "epsilon_percent": epsilon, "threshold_percent": threshold,
                                  "status": "RESOLVED_ORDER_EFFECT" if delta > threshold else "UNRESOLVED",
                                  "target_or_scale_used": False, "finite_N_fixed_path_only": True}
        structure = ({"status": "NO_VALID_MEMBER"} if "S" not in roles else
                     {"lambda": roles["S"]["theta"][4], "lambda_nonzero": roles["S"]["theta"][4] != 0.,
                      "joint_score": roles["S"]["joint_score"], "J_minus_1": roles["S"]["joint_score"]-1,
                      "J_below_1": roles["S"]["joint_score"] < 1,
                      "B_joint_score": roles["B"]["joint_score"] if "B" in roles else None,
                      "J_strictly_better_than_B": roles["S"]["joint_score"] < roles["B"]["joint_score"] if "B" in roles else None,
                      "no_shear_gain_if_lambda_zero": True, "separate_from_fixed_probe_order_effect": True})
        points = io.StringIO(newline="")
        writer = csv.writer(points)
        writer.writerow(["object_id", "kind", "stage", "form", "N", "L", "B", "repeats", "resolution_valid", "index", "window",
                         "target", "predicted", "energy", "residual", "percent_error"])
        for name, member in members.items():
            meta = metadata[name]
            for index, (actual, predicted, energy) in enumerate(zip(truth, member["prediction"], member["energy"]), 1):
                window = "1-100" if index <= 100 else "101-300" if index <= 300 else "301-320"
                writer.writerow([name, meta["kind"], meta["stage"], meta["form"], meta["N"], meta["L"], meta["B"], meta["repeats"],
                                 member["valid"], index, window, actual, predicted, energy, predicted-actual, 100*abs(predicted-actual)/actual])
        output.binary("points.csv", points.getvalue().encode("utf-8"))
        output.json("development-fit-metrics.json", fits)
        output.json("comparisons.json", comparisons)
        output.json("mechanism-comparisons.json", mechanism_comparisons)
        output.json("mechanism-verdict.json", mechanism)
        output.json("minimum-ledger.json", minimum_ledger)
        end_locks = verify_inputs()
        if end_locks != locks or sha(Path(__file__)) != own_hash or sha(OUT/"winners-frozen.json") != identity_hash:
            raise RuntimeError("Frozen input/source/identity changed during run")
        end_verification = {"input_count": len(locks), "all_input_hashes_match": True,
                            "script_sha256_unchanged": True, "winner_identity_sha256_unchanged": True}
        report = {"scope_id": SCOPE, "status": "completed" if len(roles) == len(FORMS) else "completed_with_missing_roles",
                  "run_passport": "UNVERIFIED", "global_joint_winner": primary, "roles": roles, "role_status": role_status,
                  "calls": calls, "unique_members": unique, "cached_calls": sum(row["cached"] for row in call_rows),
                  "invalid_unique_members": sum(not row["resolution_valid"] for row in unique_rows),
                  "optimizers": optimizers, "controls": controls, "default_regression": regression,
                  "winner_identity_sha256": identity_hash, "heat_readouts": heat_records, "static_readouts": static_records,
                  "postfreeze": post_records, "fixed_probe": probe_records, "mechanism_comparisons": mechanism_comparisons,
                  "order_mechanism": mechanism, "fit_metrics": fits, "comparisons": comparisons, "shear_vs_B": structure,
                  "counters": dict(counters), "root_counters": dict(root_counts), "end_verification": end_verification,
                  "seconds_before_final_serialization": time.perf_counter()-started,
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
                  root_counters=dict(root_counts), end_verification=end_verification)
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
