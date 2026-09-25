#!/usr/bin/env python3
"""CS13 frozen factorized-drift forms; importing performs no scientific work.

Seven-point cell quadrature constructs the positive Gram before removing the
Dirichlet endpoints. The complete-cell mass is lumped first, leaving d I.
One full STEMR tridiagonal decomposition per forward supplies both the entire
spectrum and the retained states. No old scientific module is imported.
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
from scipy import fft
from scipy.linalg import eigh_tridiagonal
from scipy.optimize import minimize
from scipy.special import roots_legendre


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
SCOPE = "ASFS-DISCOVERY-20260919-CS13"
FORMS = {"M": "CS13-M-MEAN-DRIFT", "V": "CS13-V-MEAN-GRAM"}
BASE = (.1639363246753303, 1.655042492001211, .5881152959703404, -.003369556173000019)
LOWER, UPPER = (.12, 1.4, .3, -.006), (.22, 1.8, .9, .006)
TRAIN_N, POST_N = (1023, 1279), (2047, 3071, 4095)
WINDOWS = {"1-100": (0, 100), "101-300": (100, 300), "301-320": (300, 320), "1-320": (0, 320)}
M_REF, W_REF, FULL_M_REF = 1.695273790061038, 5.234299091683695, 3.5251249515592384
LENGTH, A_END, STEPS = 8., 1.02, 64
G_REF, PENALTY, GIB = 2., 1e30, 1024**3
COMMAND = ("OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 "
           "PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 600s python -u "
           "papers/263-factorized-drift-spectrum/run_search.py")


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
    cases = (
        ("forward_start", {"name": "sample-N1023", "stage": "training", "N": 1023}),
        ("physical_eigh_complete", {"name": "sample-N1023", "status": "VALID"}),
        ("winner_state_readout_start", {"name": "winner-V-N1023", "additional_eigh": False}),
        ("winner_state_readout_complete", {"name": "winner-V-N1023", "counters": {"full_arrays_saved": 1}}),
        ("fixed_postcheck_saved", {"name": "ablation-V-VAROFF-N4095", "stage": "ablation"}),
    )
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


def cache_key(form, theta):
    return (form, *(float(value).hex() for value in theta))


def metadata_regression_test():
    checks = {"same_form_same_theta_matches": cache_key("M", BASE) == cache_key("M", tuple(BASE)),
              "no_cross_form_cache": cache_key("M", BASE) != cache_key("V", BASE),
              "parameter_order_matters": cache_key("M", BASE) != cache_key("M", BASE[::-1]),
              "four_parameters": len(BASE) == len(LOWER) == len(UPPER) == 4,
              "default_inside_box": all(lo <= value <= hi for value, lo, hi in zip(BASE, LOWER, UPPER)),
              "physical_budget": 2*(2*9+2*24)+6+2*3+2+2+1 == 149,
              "box_same_spacing": 16/(4095+1) == 20/(5119+1)}
    if not all(checks.values()):
        raise AssertionError("Frozen scalar metadata regression")
    return {"passed": True, "checks": checks, "scientific_numerics_performed": False}


class BoundedOutput:
    """Every new write is exclusive and shares one hard byte-budget lock."""
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


def cooling(a_start, steps):
    u = (np.arange(steps)+.5)/steps
    start, end = math.log(11.)**-2, math.log(310.)**-2
    weights = (np.log(11+299*u)**-2-end)/(start-end)
    path = A_END+(a_start-A_END)*weights
    mean = float(np.mean(path))
    variance = float(np.mean((path-mean)**2))
    return u, path, mean, variance


def cell_gram(hbar, mean_a, z, N, length, quadrature, variance=0., mode="source", constant=None):
    """Integrate the full-cell two-hat Gram, then impose Dirichlet boundaries.

    No m enters J. The quadrature has already been constructed once by main.
    The consistent q^4 multiplication matrix is integrated, never diagonalized.
    """
    xi, weights = quadrature
    spacing = 2*length/(N+1)
    q_full = -length+spacing*np.arange(N+2)
    points = -length+spacing*(np.arange(N+1)[:, None]+(xi[None, :]+1)/2)
    phi_left, phi_right = (1-xi)/2, (1+xi)/2
    if mode == "constant":
        if constant is None:
            raise ValueError("Constant-drift control missing c")
        drift = np.full_like(points, constant)
    elif mode == "sourceoff":
        drift = points**3*(.2+points*(5*z+.012*points))
    elif mode == "source":
        drift = -1+points*(2+points*(mean_a+points*(.2+points*(5*z+.012*points))))
    else:
        raise ValueError("Unknown drift mode")
    left = -hbar/spacing+drift*phi_left
    right = hbar/spacing+drift*phi_right
    factor = spacing/2
    local00 = factor*np.sum(weights*left*left, axis=1)
    local01 = factor*np.sum(weights*left*right, axis=1)
    local11 = factor*np.sum(weights*right*right, axis=1)
    q4 = points**4
    mul00 = factor*np.sum(weights*q4*phi_left**2, axis=1)
    mul01 = factor*np.sum(weights*q4*phi_left*phi_right, axis=1)
    mul11 = factor*np.sum(weights*q4*phi_right**2, axis=1)
    local00 += variance*mul00
    local01 += variance*mul01
    local11 += variance*mul11
    full_diagonal = np.zeros(N+2)
    full_diagonal[:-1] += local00
    full_diagonal[1:] += local11
    # Row sums of each COMPLETE cell mass are spacing/2 at both endpoints.
    full_mass = np.zeros(N+2)
    full_mass[:-1] += spacing/2
    full_mass[1:] += spacing/2
    mass = full_mass[1:-1].copy()
    if not np.all(mass == spacing):
        raise RuntimeError("Preboundary cell mass-lumping identity failed")
    diagonal, off = full_diagonal[1:-1]/spacing, local01[1:-1]/spacing
    q4_diagonal, q4_off = (mul11[:-1]+mul00[1:])/spacing, mul01[1:-1]/spacing
    arrays = {"q": q_full[1:-1].copy(), "q_full": q_full, "spacing": np.array(spacing),
              "mass_lumped_full": full_mass, "mass_diagonal": mass,
              "J_diagonal": diagonal, "J_off_diagonal": off,
              "q4_diagonal": q4_diagonal, "q4_off_diagonal": q4_off}
    if not all(np.all(np.isfinite(value)) for value in arrays.values()):
        raise RuntimeError("Nonfinite cell Gram or grid; no retry")
    return arrays


def metrics(prediction, target):
    relative = np.abs(prediction-target)/target
    return {"count": len(target), "mape_percent": float(100*np.mean(relative)),
            "max_percent_error": float(100*np.max(relative)),
            "rmse": float(np.sqrt(np.mean((prediction-target)**2))),
            "max_absolute_error": float(np.max(np.abs(prediction-target)))}


def readout(arrays, eigenvalues, states, target, control=False):
    diagonal, off = arrays["J_diagonal"], arrays["J_off_diagonal"]
    rows = np.abs(diagonal).copy()
    rows[:-1] += np.abs(off)
    rows[1:] += np.abs(off)
    row_norm = float(np.max(rows))
    tolerance = 64*np.finfo(float).eps*max(1., row_norm)
    if not np.all(np.isfinite(eigenvalues)):
        raise RuntimeError("Nonfinite raw tridiagonal eigenvalue; no retry")
    if eigenvalues[0] < -tolerance:
        raise RuntimeError(f"PSD hard failure: lambda_min={eigenvalues[0]!r} < {-tolerance!r}")
    mass = float(arrays["theta"][2])
    radicand = mass*mass+eigenvalues
    positive = np.isfinite(radicand) & (radicand > 0)
    energy = np.full(len(eigenvalues), np.nan)
    energy[positive] = np.sqrt(radicand[positive])
    finite = np.isfinite(energy)
    required = len(eigenvalues) if control else 320
    reasons = []
    if len(energy) < required:
        reasons.append("INSUFFICIENT_ENERGY_COUNT")
    if not (radicand[0] > 0):
        reasons.append("NONPOSITIVE_M_SQUARED_PLUS_LAMBDA_MIN")
    if not np.all(finite[:required]) or not np.all(energy[:required] > 0):
        reasons.append("PREFIX_ENERGY_NOT_FINITE_POSITIVE")
    if not np.all(np.diff(energy[:required]) >= 0):
        reasons.append("PREFIX_ENERGY_NOT_NONDECREASING")
    scale = target[0]/energy[0] if finite[0] and energy[0] > 0 else np.nan
    predicted = scale*energy[:min(320, len(energy))]
    valid = not reasons
    trace = float(np.sum(diagonal))
    trace_spectral = float(np.sum(eigenvalues))
    fro2 = float(np.sum(diagonal*diagonal)+2*np.sum(off*off))
    moment2 = float(np.sum(eigenvalues*eigenvalues))
    arrays.update(lambda_raw=eigenvalues, energy=energy, finite_mask=finite, radicand_positive_mask=positive,
                  predicted_320=predicted, scale=np.array(scale), target_100=target.copy(),
                  psd_tolerance=np.array(tolerance), valid=np.array(valid), invalid_reasons=np.array(reasons, dtype=str),
                  _cached_states=states)
    record = {"valid": valid, "status": "VALID" if valid else "INVALID_ENERGY_READOUT", "invalid_reasons": reasons,
              "required_energy_count": required, "E1": nullable(energy[0]), "scale": nullable(scale),
              "lambda_min": float(eigenvalues[0]), "negative_lambda_count": int(np.sum(eigenvalues < 0)),
              "psd_tolerance": tolerance, "J_absolute_row_sum_max": row_norm,
              "raw_lambda_clipped": False, "small_negative_eigenvalues_noncertified": bool(np.any(eigenvalues < 0)),
              "finite_energy_count_all_N": int(np.sum(finite)), "all_tail_precision_certified": False,
              "trace_J": trace, "full_lambda_sum": trace_spectral,
              "trace_relative_difference": abs(trace-trace_spectral)/max(1., abs(trace)),
              "frobenius_squared_J": fro2, "full_lambda_squared_sum": moment2,
              "second_moment_relative_difference": abs(fro2-moment2)/max(1., fro2),
              "training_metrics": metrics(predicted[:100], target) if valid and not control else None}
    return record


def add_states(arrays, record):
    states = arrays.pop("_cached_states")
    retained = states.shape[1]
    diagonal, off, eigenvalues = arrays["J_diagonal"], arrays["J_off_diagonal"], arrays["lambda_raw"]
    action = diagonal[:, None]*states
    action[:-1] += off[:, None]*states[1:]
    action[1:] += off[:, None]*states[:-1]
    residual = np.linalg.norm(action-states*eigenvalues[:retained], axis=0)
    momentum = fft.dst(states, type=1, norm="ortho", axis=0, workers=1)
    high_count = math.ceil(int(arrays["N"])/5)
    high = np.sum(momentum[-high_count:]**2, axis=0)
    edge = np.sum(states[np.abs(arrays["q"]) > .9*float(arrays["L"])]**2, axis=0)
    orthogonality = float(np.linalg.norm(states.T@states-np.eye(retained)))
    summary = {}
    for count in (100, 320):
        if retained >= count:
            summary[str(count)] = {"edge_mean": float(np.mean(edge[:count])), "edge_max": float(np.max(edge[:count])),
                                    "high_DST_mean": float(np.mean(high[:count])), "high_DST_max": float(np.max(high[:count]))}
    if retained < 100:
        summary["all_control_states"] = {"count": retained, "edge_mean": float(np.mean(edge)), "edge_max": float(np.max(edge)),
                                         "high_DST_mean": float(np.mean(high)), "high_DST_max": float(np.max(high))}
    arrays.update(states=states, eigenvector_residual=residual, edge_occupation=edge, high_DST_occupation=high)
    record.update(states_saved=True, retained_states=retained, eigenvector_residual_max=float(np.max(residual)),
                  eigenvector_residual_relative_row_norm_max=float(np.max(residual))/max(1., record["J_absolute_row_sum_max"]),
                  states_orthogonality_fro=orthogonality, state_diagnostics=summary,
                  high_DST_mode_count=high_count, high_DST_normalization="DST-I ortho", state_diagnostics_are_not_selection_gates=True,
                  same_call_eigenvectors=True, extra_state_eigh_calls=0)


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
    return {"prediction": arrays["predicted_320"].copy(), "energy": arrays["energy"][:320].copy(),
            "lambda_raw": arrays["lambda_raw"][:320].copy(), "scale": float(arrays["scale"]),
            "valid": record["valid"], "invalid_reasons": record["invalid_reasons"]}


def compare(left_name, right_name, members, truth):
    left, right = members[left_name], members[right_name]
    valid = left["valid"] and right["valid"]
    record = {"left": left_name, "right": right_name, "status": "VALID" if valid else "UNASSESSABLE_INVALID_MEMBER",
              "left_invalid_reasons": left["invalid_reasons"], "right_invalid_reasons": right["invalid_reasons"],
              "left_E1": nullable(left["energy"][0]), "right_E1": nullable(right["energy"][0]),
              "left_scale": nullable(left["scale"]), "right_scale": nullable(right["scale"]),
              "G_threshold_percent": G_REF, "raw_energy_denominator": "left object", "windows": None}
    if valid:
        record["windows"] = {}
        for window, (start, end) in WINDOWS.items():
            gap = float(100*np.max(np.abs(left["prediction"][start:end]-right["prediction"][start:end])/truth[start:end]))
            raw_gap = float(100*np.max(np.abs(left["energy"][start:end]-right["energy"][start:end])/left["energy"][start:end]))
            record["windows"][window] = {"G_percent": gap, "G_below_threshold": gap < G_REF,
                                            "raw_energy_max_relative_percent": raw_gap,
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
                "ablation_forwards_attempted": 0, "ablation_forwards_completed": 0,
                "physical_eigh_attempted": 0, "physical_eigh_completed": 0,
                "quadrature_constructors_attempted": 0, "quadrature_constructors_completed": 0,
                "cell_gram_assemblies_attempted": 0, "cell_gram_assemblies_completed": 0,
                "control_direct_frame_gram_assemblies": 0, "control_arrays_saved": 0,
                "training_compact_grids_saved": 0, "full_arrays_saved": 0,
                "svd_calls": 0, "extra_state_eigh_calls": 0, "new_target_generations": 0}
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
                    "forms": FORMS, "parameter_order": ["hbar", "a_start", "m", "z"], "default": BASE, "lower": LOWER, "upper": UPPER,
                    "train_N": TRAIN_N, "post_N": POST_N, "L": LENGTH, "midpoint_count": STEPS,
                    "M_ref": M_REF, "W_ref": W_REF, "full320_M_ref": FULL_M_REF,
                    "max_pair_calls": 66, "max_physical_eigh": 149, "max_quadrature_constructors": 1, "svd_budget": 0,
                    "quadrature_constructor": "scipy.special.roots_legendre(7); its internal roots/eigenwork is separate from physical spectra",
                    "physical_solver": "eigh_tridiagonal eigvals_only=False lapack_driver=stemr; all N eigenvectors exactly once per forward",
                    "mass": "complete-cell consistent mass row sums before Dirichlet: interior d I",
                    "potential_multiplication": "exact-degree 7-point positive cell Gram; variance q^4 consistent FE multiplication",
                    "energy": "sqrt(m^2+raw_lambda); no clipping, deletion, ground subtraction or potential minimum",
                    "path_retention": "M: mean only; V: mean and variance only; no chronology",
                    "old_scientific_modules_imported": False, "same_form_exact_parameter_cache_only": True,
                    "nonwinner_states_saved": False, "additional_state_eigh": False,
                    "new_targets_generated": False, "all_development_targets_previously_observed": True,
                    "only_primary_has_time_and_box_checks": True, "reference_is_distinct_old_heat_owner": True,
                    "output_hard_limit_bytes": GIB, "memory_advisory_bytes": GIB, "timeout_seconds": 600,
                    "logger_regression": logger_test, "metadata_regression": metadata_test,
                    "actual_exit_code": "recorded by launching parent", "run_passport": "UNVERIFIED"})
        output.json("pure-interface-tests.json", {"logger": logger_test, "metadata": metadata_test})
        event("started", scope_id=SCOPE, pid=os.getpid())
        with np.load(TARGET_FILE, allow_pickle=False) as source:
            target = source["target_100"].copy()
        if len(target) != 100 or not np.all(np.isfinite(target)) or not np.all(np.diff(target) > 0) or target[0] <= 0:
            raise RuntimeError("Invalid frozen first100 target")
        event("quadrature_constructor_start")
        counters["quadrature_constructors_attempted"] += 1
        xi, weights = roots_legendre(7)
        counters["quadrature_constructors_completed"] += 1
        moments = np.array([np.sum(weights*xi**degree) for degree in range(14)])
        expected_moments = np.array([2/(degree+1) if degree % 2 == 0 else 0. for degree in range(14)])
        quadrature_error = float(np.max(np.abs(moments-expected_moments)))
        quadrature_passed = bool(np.all(weights > 0) and np.all(np.isfinite(xi)) and np.all(np.isfinite(weights)) and quadrature_error <= 1e-13)
        output.npz("quadrature.npz", {"nodes": xi, "weights": weights, "moments_0_to_13": moments,
                                      "expected_moments": expected_moments})
        output.json("quadrature.json", {"constructor": "roots_legendre(7)", "physical_spectral_call": False,
                    "moments_degree_range": [0, 13], "max_absolute_moment_error": quadrature_error,
                    "tolerance": 1e-13, "positive_weights": bool(np.all(weights > 0)), "passed": quadrature_passed})
        event("quadrature_constructor_complete", passed=quadrature_passed, counters=dict(counters))
        if not quadrature_passed:
            raise RuntimeError("Frozen quadrature control failed")
        quadrature = xi, weights

        def assemble(hbar, mean_a, z, N, length, variance=0., mode="source", constant=None):
            counters["cell_gram_assemblies_attempted"] += 1
            arrays = cell_gram(hbar, mean_a, z, N, length, quadrature, variance, mode, constant)
            counters["cell_gram_assemblies_completed"] += 1
            return arrays

        def calculate(form, theta, N, stage, name, length=LENGTH, steps=STEPS, mode="source", constant=None, varoff=False):
            if counters["forwards_attempted"] >= 149:
                raise RuntimeError("Frozen physical-forward budget exceeded")
            counters["forwards_attempted"] += 1
            counters[stage+"_forwards_attempted"] += 1
            event("forward_start", name=name, form_key=form, N=N, stage=stage, theta=list(theta), L=length, steps=steps, mode=mode)
            tick = time.perf_counter()
            hbar, a_start, mass, z = theta
            u, path, mean_a, variance = cooling(a_start, steps)
            effective_variance = variance if form == "V" and not varoff and mode == "source" else 0.
            arrays = assemble(hbar, mean_a, z, N, length, effective_variance, mode, constant)
            arrays.update(N=np.array(N), L=np.array(length), theta=np.array(theta), path_u=u, path_a=path,
                          a_mean=np.array(mean_a), a_variance=np.array(variance), effective_variance=np.array(effective_variance),
                          midpoint_count=np.array(steps), form_key=np.array(form), mode=np.array(mode), varoff=np.array(varoff))
            if constant is not None:
                arrays["constant_drift"] = np.array(constant)
            counters["physical_eigh_attempted"] += 1
            eigenvalues, full_vec = eigh_tridiagonal(arrays["J_diagonal"], arrays["J_off_diagonal"],
                                                     eigvals_only=False, lapack_driver="stemr")
            counters["physical_eigh_completed"] += 1
            retained = full_vec[:, :min(N, 320)].copy()
            del full_vec
            try:
                record = readout(arrays, eigenvalues, retained, target, control=stage == "control")
            except Exception as exc:
                # A completed solve followed by a hard readout failure still
                # owns evidence. Preserve it without clipping or retrying.
                failed = {key: value for key, value in arrays.items() if not key.startswith("_cached_")}
                failed.update(lambda_raw=eigenvalues, states=retained, target_100=target.copy())
                output.npz("failed-"+name+".npz", failed)
                output.json("failed-"+name+".json", {
                    "name": name, "stage": stage, "form_key": form, "N": N,
                    "failure_type": type(exc).__name__, "failure_message": str(exc),
                    "physical_eigh_completed": True, "forward_completed": False,
                    "raw_lambda_clipped": False, "same_call_states_preserved": True,
                    "no_retry": True, "counters": dict(counters)})
                raise
            counters["forwards_completed"] += 1
            counters[stage+"_forwards_completed"] += 1
            record.update(name=name, form=FORMS[form], form_key=form, N=N, L=length, theta=list(theta), stage=stage,
                          midpoint_count=steps, a_mean=mean_a, a_variance=variance, effective_variance=effective_variance,
                          drift_mode=mode, varoff=varoff, constant_drift=constant, states_saved=False,
                          seconds=time.perf_counter()-tick, full_spectrum_count=len(eigenvalues), physical_eigh_calls=1,
                          mass_lumped_before_boundary=True, static_moments_not_chronological=True)
            event("physical_eigh_complete", name=name, status=record["status"], seconds=record["seconds"], counters=dict(counters))
            return arrays, record

        controls, control_arrays = {}, {}
        base, lower, upper = np.array(BASE), np.array(LOWER), np.array(UPPER)
        endpoint = base.copy()
        endpoint[1] = A_END
        control_specs = (("control-1-constant-zero", "M", base, "constant", 0.),
                         ("control-2-constant-point7", "M", base, "constant", .7),
                         ("control-3-M-default", "M", base, "source", None),
                         ("control-4-V-default", "V", base, "source", None),
                         ("control-5-M-end", "M", endpoint, "source", None),
                         ("control-6-V-end", "V", endpoint, "source", None))
        for name, form, theta, mode, constant in control_specs:
            arrays, record = calculate(form, theta, 31, "control", name, length=2., mode=mode, constant=constant)
            checks = {"passed": record["valid"]}
            if constant is not None:
                angle = np.pi*np.arange(1, 32)/32
                expected = 4*theta[0]**2/float(arrays["spacing"])**2*np.sin(angle/2)**2+constant**2*(2/3+np.cos(angle)/3)
                error = float(np.max(np.abs(arrays["lambda_raw"]-expected)))
                tolerance = 1e-10*max(1., float(np.max(np.abs(expected))))
                arrays["expected_lambda"] = expected
                checks.update(lambda_max_absolute_difference=error, lambda_tolerance=tolerance, passed=checks["passed"] and error <= tolerance)
            elif name == "control-4-V-default":
                direct_diagonal = np.zeros(31)
                direct_off = np.zeros(30)
                for value in arrays["path_a"]:
                    frame = assemble(theta[0], value, theta[3], 31, 2.)
                    direct_diagonal += frame["J_diagonal"]
                    direct_off += frame["J_off_diagonal"]
                    counters["control_direct_frame_gram_assemblies"] += 1
                direct_diagonal /= STEPS
                direct_off /= STEPS
                matrix_error = float(max(np.max(np.abs(direct_diagonal-arrays["J_diagonal"])),
                                         np.max(np.abs(direct_off-arrays["J_off_diagonal"]))))
                matrix_scale = max(1., float(np.max(np.abs(arrays["J_diagonal"]))), float(np.max(np.abs(arrays["J_off_diagonal"]))))
                expected_diagonal = control_arrays["control-3-M-default"]["J_diagonal"]+float(arrays["a_variance"])*arrays["q4_diagonal"]
                expected_off = control_arrays["control-3-M-default"]["J_off_diagonal"]+float(arrays["a_variance"])*arrays["q4_off_diagonal"]
                identity_error = float(max(np.max(np.abs(expected_diagonal-arrays["J_diagonal"])), np.max(np.abs(expected_off-arrays["J_off_diagonal"]))))
                arrays.update(direct_frame_mean_J_diagonal=direct_diagonal, direct_frame_mean_J_off_diagonal=direct_off,
                              identity_expected_J_diagonal=expected_diagonal, identity_expected_J_off_diagonal=expected_off)
                checks.update(direct_frames=STEPS, direct_mean_matrix_max_difference=matrix_error,
                              variance_identity_matrix_max_difference=identity_error, matrix_tolerance=1e-11*matrix_scale,
                              passed=checks["passed"] and max(matrix_error, identity_error) <= 1e-11*matrix_scale)
            elif name == "control-6-V-end":
                original = control_arrays["control-5-M-end"]
                matrix_error = float(max(np.max(np.abs(arrays["J_diagonal"]-original["J_diagonal"])),
                                         np.max(np.abs(arrays["J_off_diagonal"]-original["J_off_diagonal"]))))
                spectrum_error = float(np.max(np.abs(arrays["lambda_raw"]-original["lambda_raw"])))
                matrix_tolerance = 1e-11*max(1., float(np.max(np.abs(arrays["J_diagonal"]))), float(np.max(np.abs(arrays["J_off_diagonal"]))))
                spectrum_tolerance = 1e-10*max(1., float(np.max(np.abs(original["lambda_raw"]))))
                checks.update(source="control-5-M-end", matrix_max_difference=matrix_error, spectrum_max_difference=spectrum_error,
                              matrix_tolerance=matrix_tolerance, spectrum_tolerance=spectrum_tolerance,
                              passed=checks["passed"] and matrix_error <= matrix_tolerance and spectrum_error <= spectrum_tolerance)
            record["control_checks"] = checks
            add_states(arrays, record)
            output.npz(name+".npz", arrays)
            output.json(name+".json", record)
            counters["control_arrays_saved"] += 1
            controls[name], control_arrays[name] = record, arrays
            event("control_saved", name=name, checks=checks, counters=dict(counters))
            if not checks["passed"]:
                raise RuntimeError("Frozen small control failed: "+name+"; no retry")
        control_arrays.clear()
        del arrays
        cache, best, seed_physical = {}, {}, {}
        call_rows, unique_rows = [], []
        calls, unique = 0, 0

        def objective(form, normalized, stage, physical=None):
            nonlocal calls, unique
            calls += 1
            normalized = np.asarray(normalized)
            normalized_key = cache_key(form, normalized)
            if physical is not None:
                theta = np.asarray(physical).copy()
                seed_physical[normalized_key] = theta.copy()
            else:
                theta = seed_physical[normalized_key].copy() if normalized_key in seed_physical else lower+normalized*(upper-lower)
            if calls > 66 or not np.all(np.isfinite(theta)) or np.any(theta < lower) or np.any(theta > upper):
                raise RuntimeError("Frozen pair budget/parameter bounds violated")
            key = cache_key(form, theta)
            if key in cache:
                row = dict(cache[key])
                row.update(call=calls, stage=stage, cached=True, source_evaluation_id=row["evaluation_id"])
                call_rows.append(row)
                call_stream.write(json.dumps(row, allow_nan=False)+"\n")
                event("cached_pair_call", call=calls, form_key=form, source_evaluation_id=row["evaluation_id"], joint_score=row["joint_score"])
                return row["joint_score"]
            unique += 1
            eid = f"{FORMS[form]}-{unique:04d}"
            pair_arrays, grids = {}, {}
            event("pair_start", evaluation_id=eid, call=calls, form_key=form, theta=theta.tolist(), stage=stage)
            tick = time.perf_counter()
            for N in TRAIN_N:
                arrays, grid = calculate(form, theta, N, "training", f"{eid}-N{N}")
                arrays["evaluation_id"] = np.array(eid)
                output.npz(f"evaluations/{eid}-N{N}.npz", {name: value for name, value in arrays.items() if not name.startswith("_cached_")})
                output.json(f"evaluations/{eid}-N{N}.json", grid)
                counters["training_compact_grids_saved"] += 1
                pair_arrays[N], grids[str(N)] = arrays, grid
            row = {"evaluation_id": eid, "form": FORMS[form], "form_key": form, "theta": theta.tolist(),
                   "normalized_x": normalized.tolist(), "call": calls, "stage": stage, "cached": False,
                   "grids": grids, "seconds_including_save": time.perf_counter()-tick, **pair_summary(grids, pair_arrays, target)}
            output.json(f"evaluations/{eid}.json", row)
            cache[key] = row
            call_rows.append(row)
            unique_rows.append(row)
            call_stream.write(json.dumps(row, allow_nan=False)+"\n")
            if row["valid"] and (form not in best or rank(row) < rank(best[form][1])):
                best[form] = (pair_arrays, row)
            event("pair_complete", evaluation_id=eid, status=row["status"], joint_score=row["joint_score"],
                  J_minus_1=row["J_minus_1"], max_mape_percent=row["max_mape_percent"], max_percent_error=row["max_percent_error"])
            return row["joint_score"]

        wide = np.random.default_rng(20260930).uniform(0, 1, (2, 4))
        seed_points = [base.copy()]
        for coordinate in (0, 2, 1):
            for value in (lower[coordinate], upper[coordinate]):
                point = base.copy()
                point[coordinate] = value
                seed_points.append(point)
        seed_points.extend(lower+row*(upper-lower) for row in wide)
        output.json("seed-design.json", {"rng_seed": 20260930, "wide_normalized_2x4": wide.tolist(),
                                         "physical_seeds_shared_design": [point.tolist() for point in seed_points]})
        for index, theta in enumerate(seed_points):
            for form in FORMS:
                objective(form, (theta-lower)/(upper-lower), f"seed-{index:02d}", physical=theta)
        optimizers = {}
        for form in FORMS:
            if form not in best:
                optimizers[form] = {"status": "SKIPPED_NO_VALID_SEED", "nfev": 0, "no_budget_transfer": True}
                event("optimizer_skipped", form_key=form, reason="NO_VALID_SEED")
                continue
            x0 = np.array(best[form][1]["normalized_x"])
            simplex = np.repeat(x0[None, :], 5, axis=0)
            for coordinate in range(4):
                simplex[coordinate+1, coordinate] += .06 if x0[coordinate] <= .94 else -.06
            event("optimizer_start", form_key=form, starting_member=best[form][1]["evaluation_id"], maxfev=24)
            optimized = minimize(lambda x: objective(form, x, "refine"), x0, method="Nelder-Mead",
                                 bounds=[(0., 1.)]*4, options={"maxfev": 24, "initial_simplex": simplex,
                                 "xatol": 1e-6, "fatol": 1e-6, "adaptive": False})
            optimizers[form] = {"success": bool(optimized.success), "message": str(optimized.message),
                                "nfev": int(optimized.nfev), "nit": int(optimized.nit), "fun": float(optimized.fun),
                                "budget_exhausted": bool(optimized.nfev >= 24)}
            event("optimizer_complete", form_key=form, optimizer=optimizers[form])
        primary = min(best, key=lambda form: rank(best[form][1])) if best else None
        roles = {form: row for form, (arrays, row) in best.items()}
        role_status = {form: "VALID_MEMBER" if form in roles else "NO_VALID_MEMBER" for form in FORMS}
        output.json("winners-frozen.json", {"scope_id": SCOPE, "frozen_utc": utc(), "global_joint_winner": primary,
                    "roles": roles, "role_status": role_status, "calls": calls, "unique_members": unique,
                    "optimizers": optimizers, "selection": "joint first100 N1023/N1279 only", "development_metrics_evaluated": False})
        identity_hash = sha(OUT/"winners-frozen.json")
        output.json("calls.json", call_rows)
        output.json("unique-members.json", unique_rows)
        event("winner_identities_frozen", sha256=identity_hash, primary=primary, role_status=role_status)
        members, metadata, full_records, frozen_files = {}, {}, {}, []

        def save_full(name, arrays, record, stage):
            event("winner_state_readout_start", name=name, additional_eigh=False)
            add_states(arrays, record)
            members[name] = compact(arrays, record)
            metadata[name] = {"stage": stage, "form_key": record["form_key"], "N": int(arrays["N"]),
                              "L": float(arrays["L"]), "midpoint_count": int(arrays["midpoint_count"]), "drift_mode": record["drift_mode"]}
            output.npz(name+".npz", arrays)
            output.json(name+".json", record)
            counters["full_arrays_saved"] += 1
            full_records[name] = record
            event("winner_state_readout_complete", name=name, counters=dict(counters))
            return [name+".npz", name+".json"]

        for form in FORMS:
            if form not in best:
                continue
            pair_arrays, row = best[form]
            for N in TRAIN_N:
                arrays = pair_arrays.pop(N)
                record = dict(row["grids"][str(N)])
                record.update(evaluation_id=row["evaluation_id"], selection_J=row["joint_score"])
                frozen_files.extend(save_full(f"winner-{form}-N{N}", arrays, record, "training-winner"))
                del arrays
                gc.collect()
        best.clear()
        if len(frozen_files) != 4*len(roles):
            raise RuntimeError("Full training-array freeze file count mismatch")
        output.json("training-arrays-frozen.json", {"scope_id": SCOPE, "frozen_utc": utc(),
                    "winner_identity_file": "winners-frozen.json", "winner_identity_sha256": identity_hash,
                    "role_status": role_status, "full_training_arrays": 2*len(roles), "file_count": len(frozen_files),
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
                    "raw_energy_comparison_permitted": False, "used_for_selection_only_as_frozen_M_W_constants": True})
        output.json("known-targets.json", {"first": 1, "last": 320, "ordinates": truth.tolist(),
                                           "all_previously_observed": True, "generated_by_this_run": False})
        post_records = {}

        def post(form, N, name, stage="postfreeze", length=LENGTH, steps=STEPS, mode="source", varoff=False):
            theta = np.array(roles[form]["theta"])
            arrays, record = calculate(form, theta, N, stage, name, length=length, steps=steps, mode=mode, varoff=varoff)
            record.update(source_evaluation_id=roles[form]["evaluation_id"], no_selection=True)
            save_full(name, arrays, record, "fixed-"+stage)
            post_records[name] = record
            del arrays
            gc.collect()
            event("fixed_postcheck_saved", name=name, status=record["status"], counters=dict(counters))

        for form in FORMS:
            if form in roles:
                for N in POST_N:
                    post(form, N, f"post-{form}-N{N}")
        if primary is not None:
            post(primary, 4095, f"post-{primary}-time128-N4095", steps=128)
            post(primary, 5119, f"post-{primary}-box10-N5119", length=10.)
        if "V" in roles:
            for N in (3071, 4095):
                post("V", N, f"ablation-V-VAROFF-N{N}", stage="ablation", varoff=True)
        if primary is not None:
            post(primary, 4095, f"ablation-{primary}-SOURCEOFF-N4095", stage="ablation", mode="sourceoff", varoff=True)
        fits = {name: ({window: metrics(member["prediction"][start:end], truth[start:end]) for window, (start, end) in WINDOWS.items()}
                      if member["valid"] else None) for name, member in members.items()}
        comparisons = {}
        for form in roles:
            names = [f"winner-{form}-N{N}" for N in TRAIN_N]+[f"post-{form}-N{N}" for N in POST_N]
            sizes = TRAIN_N+POST_N
            for index in range(4):
                comparisons[f"{form}-N{sizes[index]}-N{sizes[index+1]}"] = compare(names[index], names[index+1], members, truth)
        if primary is not None:
            anchor = f"post-{primary}-N4095"
            comparisons[primary+"-time128"] = compare(anchor, f"post-{primary}-time128-N4095", members, truth)
            comparisons[primary+"-box10"] = compare(anchor, f"post-{primary}-box10-N5119", members, truth)
            comparisons[primary+"-SOURCEOFF"] = compare(anchor, f"ablation-{primary}-SOURCEOFF-N4095", members, truth)
        if "V" in roles:
            for N in (3071, 4095):
                comparisons[f"V-VAROFF-N{N}"] = compare(f"post-V-N{N}", f"ablation-V-VAROFF-N{N}", members, truth)
        if len(roles) == 2:
            comparisons["V-M-independent-winners-N4095"] = compare("post-V-N4095", "post-M-N4095", members, truth)
        for comparison in comparisons.values():
            left, right = comparison["left"], comparison["right"]
            comparison["right_minus_left_fit_percentage_points"] = (
                {window: {key: fits[right][window][key]-fits[left][window][key]
                          for key in ("mape_percent", "max_percent_error")} for window in WINDOWS}
                if fits[left] is not None and fits[right] is not None else None)
        assessments = {}
        for form, row in roles.items():
            training = {str(N): row["grids"][str(N)]["training_metrics"] for N in TRAIN_N}
            training_better = all(item["mape_percent"] < M_REF and item["max_percent_error"] < W_REF for item in training.values())
            fine_checks = {}
            for suffix in ("N2047-N3071", "N3071-N4095"):
                windows = comparisons[form+"-"+suffix]["windows"]
                fine_checks[suffix] = all(item["G_below_threshold"] for item in windows.values()) if windows is not None else None
            final_fit = fits[f"post-{form}-N4095"]
            full_better = final_fit is not None and final_fit["1-320"]["mape_percent"] < FULL_M_REF
            partial = bool(row["joint_score"] < 1 and training_better and full_better and all(value is True for value in fine_checks.values()))
            special = {}
            if form == primary:
                for label in ("time128", "box10"):
                    windows = comparisons[form+"-"+label]["windows"]
                    special[label] = all(item["G_below_threshold"] for item in windows.values()) if windows is not None else None
            complete = bool(partial and form == primary and all(value is True for value in special.values()))
            assessments[form] = {"status": ("NECESSARY_FINITE_ADVANCE_CONDITIONS_MET_MAGNITUDE_REVIEW_REQUIRED" if complete else
                                             "PARTIAL_CONDITIONS_MET_PRIMARY_ONLY_DIAGNOSTICS_NOT_RUN" if partial and form != primary else
                                             "NECESSARY_FINITE_ADVANCE_CONDITIONS_NOT_MET"),
                                 "is_primary": form == primary, "joint_score": row["joint_score"], "J_below_1": row["joint_score"] < 1,
                                 "training_by_grid": training, "each_training_M_W_below_external_reference": training_better,
                                 "N4095_full320_M_below_external_reference": bool(full_better), "fine_grid_checks": fine_checks,
                                 "own_time_box_checks": special if form == primary else None,
                                 "training_and_fine_necessary_conditions_met": partial, "full_necessary_conditions_met": complete,
                                 "nonprimary_cannot_borrow_primary_checks": True, "small_gain_requires_actual_shift_review": True,
                                 "engineering_lines_not_accuracy_or_arithmetic_certificates": True}
        variance_assessment = {"status": "MISSING_V_ROLE", "time_order_effect_not_claimed": True}
        if "V" in roles:
            variance_assessment = {"status": "DESCRIPTIVE_SAME_THETA_VAROFF_ONLY", "V_source_evaluation_id": roles["V"]["evaluation_id"],
                                   "same_theta_VAROFF_comparisons": {str(N): comparisons[f"V-VAROFF-N{N}"] for N in (3071, 4095)},
                                   "independently_optimized_M_is_not_VAROFF_control": True, "time_order_effect_not_claimed": True,
                                   "variance_effect_not_automatically_fit_gain": True}
        points = io.StringIO(newline="")
        writer = csv.writer(points)
        writer.writerow(["object_id", "stage", "form_key", "N", "L", "midpoint_count", "valid", "index", "window",
                         "target", "predicted", "energy", "lambda_raw", "residual", "percent_error"])
        for name, member in members.items():
            meta = metadata[name]
            for index, (actual, predicted, energy, eigenvalue) in enumerate(zip(truth, member["prediction"], member["energy"], member["lambda_raw"]), 1):
                window = "1-100" if index <= 100 else "101-300" if index <= 300 else "301-320"
                writer.writerow([name, meta["stage"], meta["form_key"], meta["N"], meta["L"], meta["midpoint_count"], member["valid"],
                                 index, window, actual, predicted, energy, eigenvalue, predicted-actual, 100*abs(predicted-actual)/actual])
        output.binary("points.csv", points.getvalue().encode("utf-8"))
        output.json("development-fit-metrics.json", fits)
        output.json("comparisons.json", comparisons)
        output.json("finite-discovery-assessments.json", assessments)
        output.json("variance-effect-assessment.json", variance_assessment)
        end_locks = verify_inputs()
        if end_locks != locks or sha(Path(__file__)) != own_hash or sha(OUT/"winners-frozen.json") != identity_hash:
            raise RuntimeError("Frozen source/input/identity changed during run")
        end_verification = {"input_count": len(locks), "all_input_hashes_match": True,
                            "script_sha256_unchanged": True, "winner_identity_sha256_unchanged": True}
        report = {"scope_id": SCOPE, "status": "completed" if len(roles) == len(FORMS) else "completed_with_missing_roles",
                  "run_passport": "UNVERIFIED", "global_joint_winner": primary, "roles": roles, "role_status": role_status,
                  "calls": calls, "unique_members": unique, "cached_calls": sum(row["cached"] for row in call_rows),
                  "invalid_unique_members": sum(not row["valid"] for row in unique_rows), "optimizers": optimizers,
                  "controls": controls, "quadrature_control_passed": quadrature_passed, "winner_identity_sha256": identity_hash,
                  "full_readouts": full_records, "postfreeze": post_records, "fit_metrics": fits, "comparisons": comparisons,
                  "finite_discovery_assessments": assessments, "variance_effect_assessment": variance_assessment,
                  "external_history_fit_metrics": external_fits, "counters": dict(counters), "end_verification": end_verification,
                  "seconds_before_final_serialization": time.perf_counter()-started,
                  "maxrss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "completed_utc": utc(),
                  "output_bytes_before_result": output.size(), "new_targets_generated": False,
                  "formal_route": "UNASSIGNED; B NOT INVOKED", "static_forms_no_time_order_effect": True}
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
