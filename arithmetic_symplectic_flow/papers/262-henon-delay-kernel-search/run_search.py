#!/usr/bin/env python3
"""CS12 frozen finite delay kernels; no scientific work or file output on import.

For each middle coordinate, evaluate the first column once and use (i+k) mod n
to form the circular Hankel block. Period 4 and the uniform endpoint grid make
this exactly equivalent to the frozen residual formula; equivalent floating
angles are not independently reevaluated. No old scientific module is imported.
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
SCOPE = "ASFS-DISCOVERY-20260919-CS12"
FORMS = {"A": "CS12-A-AUTONOMOUS-DELAY", "D": "CS12-D-COOLING-DELAY"}
BASE = np.array([.12, 1.655042492001211])
LOWER, UPPER = np.array([.04, 1.02]), np.array([.32, 2.10])
LENGTH, A_END = 2., 1.02
TIMES = (0., 1/3, 2/3, 1.)
TRAIN_N, POST_N = (23, 27), (31, 39, 47)
WINDOWS = {"1-100": (0, 100), "101-300": (100, 300), "301-320": (300, 320), "1-320": (0, 320)}
M_REF, W_REF, FULL_M_REF = 1.695273790061038, 5.234299091683695, 3.5251249515592384
G_REF, END_REF, PENALTY, GIB = 2., .1, 1e30, 1024**3
COMMAND = ("OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 "
           "PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 600s python -u "
           "papers/262-henon-delay-kernel-search/run_search.py")


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
        ("forward_start", {"name": "sample-n23", "stage": "training", "n": 23, "d": 529}),
        ("full_svd_complete", {"name": "sample-n23", "status": "VALID", "counters": {"full_svd_completed": 1}}),
        ("winner_state_readout_start", {"name": "winner-D-n23", "no_additional_svd": True}),
        ("winner_state_readout_complete", {"name": "winner-D-n23", "counters": {"full_arrays_saved": 1}}),
        ("ablation_alias_saved", {"name": "ablation-D-END-n39", "source": "post-D-n39"}),
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


def owner_key(n, epsilon, coefficients, length=LENGTH, times=TIMES):
    """Exact scalar metadata only; used solely for fixed-output alias detection."""
    return (int(n), float(epsilon).hex(), float(length).hex(), "endpoint-periodic-i*n+j",
            "column-forward-circular-Hankel-own-Z", tuple(float(value).hex() for value in times),
            tuple(float(value).hex() for value in coefficients))


def metadata_regression_test():
    coefficients = (1.7, 1.4, 1.2, 1.02)
    key = owner_key(39, .12, coefficients)
    checks = {
        "exact_same_owner_matches": key == owner_key(39, .12, tuple(coefficients)),
        "epsilon_distinguishes": key != owner_key(39, .13, coefficients),
        "n_distinguishes": key != owner_key(47, .12, coefficients),
        "L_distinguishes": key != owner_key(39, .12, coefficients, length=3.),
        "coefficient_order_distinguishes": key != owner_key(39, .12, coefficients[::-1]),
        "time_grid_distinguishes": key != owner_key(39, .12, coefficients, times=(0., .2, .8, 1.)),
        "step_count_distinguishes": key != owner_key(39, .12, coefficients[:1], times=(0.,)),
    }
    if not all(checks.values()):
        raise AssertionError("Alias-owner metadata regression")
    return {"passed": True, "checks": checks, "scientific_numerics_performed": False}


class BoundedOutput:
    """All writes share one byte-budget lock; targets are exclusive new files."""
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


def coefficients_for(form, parameter):
    if form == "A":
        return np.full(4, parameter, dtype=float)
    if form != "D":
        raise ValueError("Unknown form")
    u = np.array(TIMES)
    start, end = math.log(11.)**-2, math.log(310.)**-2
    weight = (np.log(11+299*u)**-2-end)/(start-end)
    weight[0], weight[-1] = 1., 0.
    coefficients = A_END+(parameter-A_END)*weight
    coefficients[0], coefficients[-1] = parameter, A_END
    return coefficients


def build_blocks(epsilon, coefficients, n):
    q = -LENGTH+2*LENGTH*np.arange(n)/n
    residual_first_column = q[None, None, :]+q[0]-1+coefficients[:, None, None]*q[None, :, None]**2
    raw_first = np.exp(-(2*LENGTH/np.pi)**2*np.sin(np.pi*residual_first_column/(2*LENGTH))**2/(2*epsilon**2))
    if not np.all(np.isfinite(raw_first)) or np.min(raw_first) <= 0:
        raise RuntimeError("Nonpositive/nonfinite raw kernel weight; no clipping or floor")
    normalizers = np.sum(raw_first, axis=2)
    if not np.all(np.isfinite(normalizers)) or np.min(normalizers) <= 0:
        raise RuntimeError("Invalid kernel normalizer")
    first = raw_first/normalizers[:, :, None]
    circular = (np.arange(n)[:, None]+np.arange(n)[None, :]) % n
    blocks = first[:, :, circular]
    row_error = np.max(np.abs(np.sum(blocks, axis=3)-1), axis=(1, 2))
    column_error = np.max(np.abs(np.sum(blocks, axis=2)-1), axis=(1, 2))
    symmetry = np.max(np.abs(blocks-blocks.swapaxes(2, 3)), axis=(1, 2, 3))
    if (not np.all(np.isfinite(blocks)) or np.min(blocks) <= 0
            or np.max(row_error) > 1e-12 or np.max(column_error) > 1e-12):
        raise RuntimeError("Block positivity/double-stochasticity contract failed")
    arrays = {"q": q, "K_blocks": blocks, "Z": normalizers, "raw_first_column": raw_first,
              "block_row_sum_errors": row_error, "block_column_sum_errors": column_error,
              "block_symmetry_errors": symmetry}
    record = {"block_row_sum_error_max": float(np.max(row_error)), "block_column_sum_error_max": float(np.max(column_error)),
              "block_symmetry_error_max": float(np.max(symmetry)), "raw_kernel_weight_min": float(np.min(raw_first)),
              "normalized_block_weight_min": float(np.min(blocks)), "normalizer_min": float(np.min(normalizers)),
              "normalizer_max": float(np.max(normalizers)), "block_tolerance": 1e-12,
              "kernel_evaluation": "first column; exact periodic (i+k) mod n circular Hankel indexing"}
    return arrays, record


def forward(form, theta, n, coefficients, times):
    if n % 2 != 1 or len(coefficients) != len(times) or len(coefficients) not in (1, 4):
        raise ValueError("Frozen grid/path shape violation")
    dimension = n*n
    arrays, record = build_blocks(float(theta[0]), coefficients, n)
    product = np.eye(dimension)
    for blocks in arrays["K_blocks"]:
        # Source axes: previous i, current j, initial-column c.
        # Batched matmul maps [j,k,i] times [j,i,c] to [j,k,c].
        incoming = product.reshape(n, n, dimension).transpose(1, 0, 2)
        product = np.matmul(blocks, incoming).reshape(dimension, dimension)
    if not np.all(np.isfinite(product)):
        raise RuntimeError("Nonfinite full kernel product")
    constant = np.ones(dimension)/math.sqrt(dimension)
    row_error = float(np.max(np.abs(np.sum(product, axis=1)-1)))
    column_error = float(np.max(np.abs(np.sum(product, axis=0)-1)))
    right_error = float(np.linalg.norm(product@constant-constant))
    left_error = float(np.linalg.norm(product.T@constant-constant))
    if max(row_error, column_error, right_error, left_error) > 1e-10:
        raise RuntimeError("Product double-stochasticity/conservation contract failed")
    arrays.update(theta=np.asarray(theta).copy(), form_key=np.array(form), n=np.array(n), dimension=np.array(dimension),
                  L=np.array(LENGTH), times=np.asarray(times).copy(), coefficients=np.asarray(coefficients).copy(),
                  step_count=np.array(len(coefficients)), epsilon=np.array(theta[0]), C=product,
                  constant_vector=constant, grid_convention=np.array("endpoint-periodic-i*n+j"))
    record.update(form_key=form, form=FORMS[form], theta=list(map(float, theta)), epsilon=float(theta[0]), n=n,
                  dimension=dimension, L=LENGTH, times=list(map(float, times)), coefficients=list(map(float, coefficients)),
                  step_count=len(coefficients), product_row_sum_error=row_error, product_column_sum_error=column_error,
                  right_constant_residual=right_error, left_constant_residual=left_error, product_tolerance=1e-10,
                  product_min=float(np.min(product)), product_zero_count=int(np.count_nonzero(product == 0.)),
                  propagation_convention="column; C=T_last ... T_first; state i*n+j",
                  product_zero_entries_not_repaired=True)
    return arrays, record


def readout(sigma, left0, right0, target, step_count, formal):
    dimension = len(sigma)
    constant = np.ones(dimension)/math.sqrt(dimension)
    left_dot, right_dot = float(constant@left0), float(constant@right0)
    left_distance = float(min(np.linalg.norm(left0-constant), np.linalg.norm(left0+constant)))
    right_distance = float(min(np.linalg.norm(right0-constant), np.linalg.norm(right0+constant)))
    nontrivial = sigma[1:]
    energy = np.full(dimension-1, np.nan)
    positive = np.isfinite(nontrivial) & (nontrivial > 0)
    energy[positive] = -np.log(nontrivial[positive])/step_count
    mask = positive & np.isfinite(energy) & (energy > 0)
    diagnostic = {"sigma0": nullable(sigma[0]), "sigma1": nullable(sigma[1]), "nontrivial_gap": nullable(1-sigma[1]),
                  "constant_left_inner_product": left_dot, "constant_right_inner_product": right_dot,
                  "constant_left_sign_distance": left_distance, "constant_right_sign_distance": right_distance,
                  "constant_signs_consistent": bool(left_dot*right_dot > 0),
                  "formal_unique_constant_gate_applied": formal, "resolved_nontrivial_energy_count": int(np.count_nonzero(mask))}
    arrays = {"sigma": sigma.copy(), "energy": energy, "energy_resolved_mask": mask,
              "energy_sigma_indices": np.arange(1, dimension), "target_100": target.copy()}
    if not formal:
        arrays["control_only"] = np.array(True)
        diagnostic.update(status="CONTROL_ONLY", resolution_valid=None,
                          no_unique_constant_or_321_state_gate=True, energy_is_diagnostic_only=True)
        return arrays, diagnostic
    reasons = []
    if not math.isfinite(float(sigma[0])) or abs(sigma[0]-1) > 1e-10:
        reasons.append("CONSERVATIVE_SIGMA0_NOT_ONE")
    if dimension < 321 or not np.all(np.isfinite(sigma[:321])) or not np.all(sigma[:321] > 0):
        reasons.append("REQUIRED_321_SINGULAR_VALUES_NOT_POSITIVE_FINITE")
    if not np.all(np.diff(sigma[:321]) <= 0):
        reasons.append("REQUIRED_SINGULAR_VALUES_NOT_DESCENDING")
    ratio = float(sigma[320]/sigma[0]) if dimension >= 321 and sigma[0] > 0 else float("nan")
    if not math.isfinite(ratio) or ratio < 1e-10:
        reasons.append("SIGMA320_RELATIVE_RESOLUTION_BELOW_1E-10")
    if not (math.isfinite(float(sigma[1])) and sigma[1] < 1 and 1-sigma[1] >= 1e-8):
        reasons.append("NONTRIVIAL_GAP_BELOW_1E-8")
    if left_distance > 1e-6 or right_distance > 1e-6:
        reasons.append("TOP_SINGULAR_STATES_NOT_CONSTANT")
    if not left_dot*right_dot > 0:
        reasons.append("TOP_CONSTANT_STATE_SIGNS_INCONSISTENT")
    if len(energy) < 320 or not np.all(mask[:320]):
        reasons.append("REQUIRED_NONTRIVIAL_ENERGIES_NOT_POSITIVE_FINITE")
    scale = float(target[0]/energy[0]) if math.isfinite(float(energy[0])) and energy[0] > 0 else float("nan")
    prediction = scale*energy[:320] if math.isfinite(scale) else np.full(320, np.nan)
    arrays.update(scale=np.array(scale), predicted_320=prediction, resolution_valid=np.array(not reasons),
                  invalid_reasons=np.array(reasons, dtype=str), excluded_conservation_modes=np.array(1))
    diagnostic.update(status="VALID" if not reasons else "INVALID_RESOLUTION", resolution_valid=not reasons,
                      invalid_reasons=reasons, required_count=320, required_sigma_count=321,
                      required_last_sigma=nullable(sigma[320]), required_sigma_ratio=nullable(ratio),
                      E1=nullable(energy[0]), scale=nullable(scale), excluded_conservation_modes=1,
                      sigma_not_divided_by_measured_sigma0=True, no_rest_mass_or_offset=True)
    return arrays, diagnostic


def metrics(prediction, target):
    error = np.abs(prediction-target)
    return {"mape_percent": float(100*np.mean(error/target)), "max_percent_error": float(100*np.max(error/target)),
            "mae": float(np.mean(error)), "mse": float(np.mean(error**2)), "rmse": float(np.sqrt(np.mean(error**2)))}


def rank(row):
    if not row["resolution_valid"]:
        raise ValueError("Invalid member cannot enter winner ranking")
    return (row["joint_score"], row["max_mape_percent"], row["max_percent_error"], row["cross_grid_percent"], row["evaluation_id"])


def pair_summary(grids, arrays, target):
    if not all(grids[str(n)]["resolution_valid"] for n in TRAIN_N):
        return {"status": "INVALID_RESOLUTION", "resolution_valid": False, "joint_score": PENALTY,
                "J_minus_1": None, "max_mape_percent": None, "max_percent_error": None, "cross_grid_percent": None}
    means = [grids[str(n)]["training_metrics"]["mape_percent"] for n in TRAIN_N]
    worst = [grids[str(n)]["training_metrics"]["max_percent_error"] for n in TRAIN_N]
    gap = float(100*np.max(np.abs(arrays[23]["predicted_320"][:100]-arrays[27]["predicted_320"][:100])/target))
    score = max(means[0]/M_REF, means[1]/M_REF, worst[0]/W_REF, worst[1]/W_REF, gap/G_REF)
    return {"status": "VALID", "resolution_valid": True, "joint_score": score, "J_minus_1": score-1,
            "max_mape_percent": max(means), "max_percent_error": max(worst), "cross_grid_percent": gap}


def state_diagnostics(states, n):
    dimension, retained = states.shape
    constant = np.ones(dimension)/math.sqrt(dimension)
    projections = constant@states
    transformed = fft.fftn(states.reshape(n, n, retained), axes=(0, 1), norm="ortho", workers=1)
    modes = np.arange(n)
    modes[modes > n//2] -= n
    cutoff = math.floor(.4*n)
    high = np.maximum(np.abs(modes[:, None]), np.abs(modes[None, :])) >= cutoff
    occupation = np.sum(np.abs(transformed[high, :])**2, axis=0)
    summary = {"frequency_threshold": cutoff, "rule": "max(abs(k_i),abs(k_j)) >= floor(.4*n)",
               "transform": "two-dimensional unitary FFT on endpoint grid", "windows": {}}
    for count in (100, 320):
        if retained >= count+1:
            summary["windows"][str(count)] = {"high_frequency_max": float(np.max(occupation[1:count+1])),
                                              "high_frequency_mean": float(np.mean(occupation[1:count+1])),
                                              "constant_projection_abs_max": float(np.max(np.abs(projections[1:count+1])))}
    return projections, occupation, summary


def add_states(arrays, record):
    left, right = arrays.pop("_cached_left"), arrays.pop("_cached_right")
    product, sigma = arrays["C"], arrays["sigma"]
    retained = left.shape[1]
    forward_error = np.linalg.norm(product@right-left*sigma[:retained], axis=0)
    adjoint_error = np.linalg.norm(product.T@left-right*sigma[:retained], axis=0)
    lp, lh, ls = state_diagnostics(left, int(arrays["n"]))
    rp, rh, rs = state_diagnostics(right, int(arrays["n"]))
    fro, moment = float(np.sum(product*product)), float(np.sum(sigma*sigma))
    arrays.update(singular_left=left, singular_right=right, singular_forward_residual=forward_error,
                  singular_transpose_residual=adjoint_error, left_constant_projections=lp, right_constant_projections=rp,
                  left_nontrivial_constant_projections=lp[1:], right_nontrivial_constant_projections=rp[1:],
                  left_high_frequency_occupation=lh, right_high_frequency_occupation=rh)
    record.update(retained_singular_states=retained, retained_state_zero_is_conservative_candidate=True,
                  singular_forward_residual_max=float(np.max(forward_error)), singular_transpose_residual_max=float(np.max(adjoint_error)),
                  left_orthogonality_fro=float(np.linalg.norm(left.T@left-np.eye(retained))),
                  right_orthogonality_fro=float(np.linalg.norm(right.T@right-np.eye(retained))),
                  left_state_diagnostics=ls, right_state_diagnostics=rs,
                  frobenius_squared=fro, full_sigma_squared_sum=moment,
                  frobenius_moment_relative_difference=abs(fro-moment)/fro if fro > 0 else None,
                  single_step_control_remaining_states_not_all_nonconstant=(int(arrays["step_count"]) == 1),
                  original_svd_spectrum_preserved=True, no_additional_svd=True,
                  partial_states_are_not_full_reconstruction=(retained < len(sigma)))


def compact(arrays, valid):
    return {"prediction": arrays["predicted_320"].copy(), "energy": arrays["energy"][:320].copy(),
            "sigma": arrays["sigma"].copy(), "valid": bool(valid), "scale": float(arrays["scale"]),
            "invalid_reasons": arrays["invalid_reasons"].tolist(), "n": int(arrays["n"])}


def compare(left_name, right_name, members, truth, threshold=G_REF):
    left, right = members[left_name], members[right_name]
    valid = left["valid"] and right["valid"]
    same_dimension = len(left["sigma"]) == len(right["sigma"])
    result = {"left": left_name, "right": right_name, "status": "VALID" if valid else "UNASSESSABLE_INVALID_RESOLUTION",
              "left_invalid_reasons": left["invalid_reasons"], "right_invalid_reasons": right["invalid_reasons"],
              "left_E1": nullable(left["energy"][0]), "right_E1": nullable(right["energy"][0]),
              "left_scale": nullable(left["scale"]), "right_scale": nullable(right["scale"]),
              "raw_energy_denominator": "left object", "G_threshold_percent": threshold, "windows": None,
              "full_sigma_max_absolute_difference": float(np.max(np.abs(left["sigma"]-right["sigma"]))) if same_dimension else None,
              "full_sigma_comparable_dimension": same_dimension,
              "first321_sigma_max_absolute_difference": float(np.max(np.abs(left["sigma"][:321]-right["sigma"][:321])))}
    if valid:
        result["windows"] = {window: {"G_percent": float(100*np.max(np.abs(left["prediction"][start:end]-right["prediction"][start:end])/truth[start:end])),
                                      "raw_energy_max_relative_percent": float(100*np.max(np.abs(left["energy"][start:end]-right["energy"][start:end])/left["energy"][start:end]))}
                             for window, (start, end) in WINDOWS.items()}
        for row in result["windows"].values():
            row["G_below_threshold"] = row["G_percent"] < threshold
    return result


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
                "full_svd_attempted": 0, "full_svd_completed": 0, "control_arrays_saved": 0,
                "training_compact_grids_saved": 0, "full_arrays_saved": 0, "ablation_aliases_saved": 0,
                "eigh_calls": 0, "root_calls": 0, "extra_state_svd_calls": 0, "new_target_generations": 0}
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
                    "forms": FORMS, "train_n": TRAIN_N, "post_n": POST_N, "L": LENGTH, "times": TIMES,
                    "M_ref": M_REF, "W_ref": W_REF, "full320_M_ref": FULL_M_REF, "reference_is_external_old_heat_model": True,
                    "max_pair_calls": 56, "max_forwards_and_full_svd": 128, "eigh_root_extra_state_svd_budget": 0,
                    "kernel_evaluation": "first columns only: per frame n^2 positive raw weights, then (i+k) mod n circular indexing",
                    "kernel_equivalence": "exact period-4 frozen residual; equivalent angles not separately reevaluated",
                    "normalizer": "own first-column sum for each frame and middle coordinate; no row renormalization",
                    "propagation": "batched n by n block matrix products; column convention C=T3 T2 T1 T0",
                    "old_scientific_modules_imported": False, "same_form_exact_parameter_cache_only": True,
                    "alias_owner_fields": "n,epsilon,L,grid/flattening,normalization/column convention,times,ordered coefficients",
                    "nonwinner_C_or_states_saved": False, "full_svd": "one full real SVD per forward",
                    "nontrivial_energy": "-log(sigma[1:])/4; exactly one conserved mode excluded",
                    "single_step_control_unique_mode_gate": False, "new_targets_generated": False,
                    "all_development_targets_previously_observed": True, "old_mass_or_potential_inherited": False,
                    "output_hard_limit_bytes": GIB, "memory_advisory_bytes": GIB, "timeout_seconds": 600,
                    "logger_regression": logger_test, "metadata_regression": metadata_test,
                    "actual_exit_code": "recorded by launching parent", "run_passport": "UNVERIFIED"})
        output.json("pure-interface-tests.json", {"logger": logger_test, "metadata": metadata_test})
        event("started", scope_id=SCOPE, pid=os.getpid())
        with np.load(TARGET_FILE, allow_pickle=False) as source:
            target = source["target_100"].copy()
        if len(target) != 100 or not np.all(np.isfinite(target)) or target[0] <= 0 or not np.all(np.diff(target) > 0):
            raise RuntimeError("Invalid locked target100")

        def calculate(form, theta, n, stage, name, coefficients_override=None, times_override=None):
            limits = {"control": 6, "training": 112, "postfreeze": 6, "ablation": 4}
            if counters["forwards_attempted"] >= 128 or counters[stage+"_forwards_attempted"] >= limits[stage]:
                raise RuntimeError("Frozen forward budget exceeded")
            coefficients = coefficients_for(form, float(theta[1])) if coefficients_override is None else np.array(coefficients_override, dtype=float)
            times = np.array(TIMES if times_override is None else times_override, dtype=float)
            counters["forwards_attempted"] += 1
            counters[stage+"_forwards_attempted"] += 1
            event("forward_start", name=name, stage=stage, form=form, theta=theta.tolist(), n=n, d=n*n,
                  coefficients=coefficients.tolist(), times=times.tolist(), counters=dict(counters))
            tick = time.perf_counter()
            arrays, record = forward(form, theta, n, coefficients, times)
            counters["forwards_completed"] += 1
            counters[stage+"_forwards_completed"] += 1
            record["forward_seconds"] = time.perf_counter()-tick
            event("forward_complete", name=name, stage=stage, counters=dict(counters))
            if counters["full_svd_attempted"] >= 128:
                raise RuntimeError("Frozen SVD budget exceeded")
            counters["full_svd_attempted"] += 1
            tick = time.perf_counter()
            left, sigma, right_t = np.linalg.svd(arrays["C"], full_matrices=True)
            counters["full_svd_completed"] += 1
            record["full_svd_seconds"] = time.perf_counter()-tick
            formal = stage != "control"
            retained = 321 if formal else n*n
            arrays["_cached_left"], arrays["_cached_right"] = left[:, :retained].copy(), right_t[:retained].T.copy()
            values, validity = readout(sigma, left[:, 0], right_t[0], target, len(coefficients), formal)
            del left, right_t
            arrays.update(values)
            record.update(validity)
            if formal:
                record["training_metrics"] = metrics(arrays["predicted_320"][:100], target) if validity["resolution_valid"] else None
            event("full_svd_complete", name=name, status=record["status"], counters=dict(counters))
            return arrays, record

        controls, control_arrays = {}, {}
        default_path = coefficients_for("D", float(BASE[1]))
        specifications = (
            ("control-1-one-step", "A", 1.30, [1.30], [0.]),
            ("control-2-zero-source", "A", 0., [0., 0., 0., 0.], TIMES),
            ("control-3-D-default", "D", float(BASE[1]), default_path, TIMES),
            ("control-4-D-reverse", "D", float(BASE[1]), default_path[::-1], TIMES),
            ("control-5-A-end", "A", A_END, [A_END]*4, TIMES),
            ("control-6-D-end", "D", A_END, coefficients_for("D", A_END), TIMES),
        )
        for name, form, parameter, coefficients, times in specifications:
            arrays, record = calculate(form, np.array([.30, parameter]), 7, "control", name,
                                       coefficients_override=coefficients, times_override=times)
            add_states(arrays, record)
            checks = {"no_321_or_unique_constant_gate": True, "passed": True}
            if name == "control-1-one-step":
                expected_sigma = np.sort(np.abs(fft.fft(arrays["K_blocks"][0, :, 0, :], axis=1)).ravel())[::-1]
                error = float(np.max(np.abs(arrays["sigma"]-expected_sigma)))
                arrays["expected_sigma"] = expected_sigma
                checks.update(sigma_max_absolute_difference=error, sigma_tolerance=1e-10,
                              DFT_normalization="unnormalized forward DFT, not occupation FFT", passed=error <= 1e-10)
            elif name == "control-2-zero-source":
                block = arrays["K_blocks"][0, 0]
                squared = block@block
                expected_matrix = np.kron(squared, squared)
                factors = np.abs(fft.fft(block[0]))**2
                expected_sigma = np.sort((factors[:, None]*factors[None, :]).ravel())[::-1]
                sigma_error = float(np.max(np.abs(arrays["sigma"]-expected_sigma)))
                matrix_error = float(np.linalg.norm(arrays["C"]-expected_matrix))
                tolerance = 1e-10*max(1., float(np.linalg.norm(arrays["C"])))
                arrays.update(expected_sigma=expected_sigma, expected_matrix=expected_matrix)
                checks.update(sigma_max_absolute_difference=sigma_error, matrix_frobenius_difference=matrix_error,
                              sigma_tolerance=1e-10, matrix_tolerance=tolerance,
                              passed=sigma_error <= 1e-10 and matrix_error <= tolerance)
            elif name in ("control-4-D-reverse", "control-6-D-end"):
                source_name = "control-3-D-default" if name == "control-4-D-reverse" else "control-5-A-end"
                original = control_arrays[source_name]
                if name == "control-4-D-reverse":
                    swap = np.arange(49).reshape(7, 7).T.ravel()
                    expected_matrix = original["C"].T[np.ix_(swap, swap)]
                else:
                    expected_matrix = original["C"]
                sigma_error = float(np.max(np.abs(arrays["sigma"]-original["sigma"])))
                matrix_error = float(np.linalg.norm(arrays["C"]-expected_matrix))
                tolerance = 1e-10*max(1., float(np.linalg.norm(original["C"])))
                arrays["expected_matrix"] = expected_matrix.copy()
                checks.update(source=source_name, sigma_max_absolute_difference=sigma_error,
                              matrix_frobenius_difference=matrix_error, sigma_tolerance=1e-10,
                              matrix_tolerance=tolerance, passed=sigma_error <= 1e-10 and matrix_error <= tolerance)
            record["control_checks"] = checks
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
            normalized_key = form, *(float(value).hex() for value in normalized)
            if physical is not None:
                theta = np.asarray(physical).copy()
                seed_physical[normalized_key] = theta.copy()
            else:
                theta = seed_physical[normalized_key].copy() if normalized_key in seed_physical else LOWER+normalized*(UPPER-LOWER)
            if calls > 56 or not np.all(np.isfinite(theta)) or np.any(theta < LOWER) or np.any(theta > UPPER):
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
                arrays, grid = calculate(form, theta, n, "training", f"{eid}-n{n}")
                arrays["evaluation_id"] = np.array(eid)
                compact_arrays = {name: value for name, value in arrays.items() if name != "C" and not name.startswith("_cached_")}
                output.npz(f"evaluations/{eid}-n{n}.npz", compact_arrays)
                grid["C_and_states_saved"] = False
                output.json(f"evaluations/{eid}-n{n}.json", grid)
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
            event("pair_complete", evaluation_id=eid, status=row["status"], joint_score=row["joint_score"],
                  J_minus_1=row["J_minus_1"], max_mape_percent=row["max_mape_percent"], max_percent_error=row["max_percent_error"])
            return row["joint_score"]

        wide = np.random.default_rng(20260929).uniform(0, 1, (2, 2))
        seed_points = [BASE.copy(), *[np.array([epsilon, BASE[1]]) for epsilon in (.06, .20, .30)],
                       np.array([.12, 1.02]), np.array([.12, 2.10]), *[LOWER+row*(UPPER-LOWER) for row in wide]]
        output.json("seed-design.json", {"rng_seed": 20260929, "wide_normalized_2x2": wide.tolist(),
                                         "physical_seeds_shared_design": [point.tolist() for point in seed_points]})
        for index, theta in enumerate(seed_points):
            for form in FORMS:
                objective(form, (theta-LOWER)/(UPPER-LOWER), f"seed-{index:02d}", physical=theta)
        optimizers = {}
        for form in FORMS:
            if form not in best:
                optimizers[form] = {"status": "SKIPPED_NO_VALID_SEED", "nfev": 0, "no_budget_transfer": True}
                event("optimizer_skipped", form=form, reason="NO_VALID_SEED")
                continue
            x0 = np.array(best[form][1]["normalized_x"])
            simplex = np.repeat(x0[None, :], 3, axis=0)
            for coordinate in range(2):
                simplex[coordinate+1, coordinate] += .06 if x0[coordinate] <= .94 else -.06
            event("optimizer_start", form=form, starting_member=best[form][1]["evaluation_id"], maxfev=20)
            optimized = minimize(lambda x: objective(form, x, "refine"), x0, method="Nelder-Mead",
                                 bounds=[(0., 1.)]*2, options={"maxfev": 20, "initial_simplex": simplex,
                                 "xatol": 1e-6, "fatol": 1e-6, "adaptive": False})
            optimizers[form] = {"success": bool(optimized.success), "message": str(optimized.message),
                                "nfev": int(optimized.nfev), "nit": int(optimized.nit), "fun": float(optimized.fun)}
            event("optimizer_complete", form=form, optimizer=optimizers[form])
        primary = min(best, key=lambda form: rank(best[form][1])) if best else None
        roles = {form: row for form, (arrays, row) in best.items()}
        role_status = {form: "VALID_MEMBER" if form in roles else "NO_VALID_MEMBER" for form in FORMS}
        output.json("winners-frozen.json", {"scope_id": SCOPE, "frozen_utc": utc(), "global_joint_winner": primary,
                    "roles": roles, "role_status": role_status, "calls": calls, "unique_members": unique,
                    "optimizers": optimizers, "selection": "joint first100 n23/n27 only", "development_metrics_evaluated": False})
        identity_hash = sha(OUT/"winners-frozen.json")
        output.json("calls.json", call_rows)
        output.json("unique-members.json", unique_rows)
        event("winner_identities_frozen", sha256=identity_hash, primary=primary, role_status=role_status)
        members, metadata, full_records, frozen_files, saved_owners = {}, {}, {}, [], {}

        def save_full(name, arrays, record, stage):
            event("winner_state_readout_start", name=name, no_additional_svd=True)
            add_states(arrays, record)
            record.update(C_and_states_saved=True, no_selection=True, original_ranking_spectrum_preserved=True)
            members[name] = compact(arrays, record["resolution_valid"])
            metadata[name] = {"kind": "kernel", "stage": stage, "form": record["form_key"], "n": int(arrays["n"]),
                              "dimension": int(arrays["dimension"]), "epsilon": float(arrays["epsilon"]),
                              "coefficients": arrays["coefficients"].tolist()}
            output.npz(name+".npz", arrays)
            output.json(name+".json", record)
            counters["full_arrays_saved"] += 1
            full_records[name] = record
            key = owner_key(int(arrays["n"]), float(arrays["epsilon"]), arrays["coefficients"], float(arrays["L"]), arrays["times"])
            saved_owners.setdefault(key, name)
            event("winner_state_readout_complete", name=name, counters=dict(counters))
            return [name+".npz", name+".json"]

        for form in FORMS:
            if form not in best:
                continue
            pair_arrays, row = best[form]
            for n in TRAIN_N:
                arrays = pair_arrays.pop(n)
                record = dict(row["grids"][str(n)])
                record.update(evaluation_id=row["evaluation_id"], selection_J=row["joint_score"])
                frozen_files.extend(save_full(f"winner-{form}-n{n}", arrays, record, "training-winner"))
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
                    "raw_energy_or_sigma_comparison_permitted": False, "used_for_selection_only_as_frozen_M_W_constants": True})
        output.json("known-targets.json", {"first": 1, "last": 320, "ordinates": truth.tolist(),
                                           "all_previously_observed": True, "generated_by_this_run": False})
        post_records, aliases = {}, {}

        def post(form, n, name, stage="postfreeze", coefficients_override=None):
            theta = np.array(roles[form]["theta"])
            coefficients = coefficients_for(form, float(theta[1])) if coefficients_override is None else np.array(coefficients_override)
            if stage == "ablation":
                key = owner_key(n, float(theta[0]), coefficients)
                if key in saved_owners:
                    source_name = saved_owners[key]
                    alias = {"status": "EXACT_OWNER_ALIAS", "source_object": source_name,
                             "source_npz": source_name+".npz", "source_sha256": sha(OUT/(source_name+".npz")),
                             "source_json_sha256": sha(OUT/(source_name+".json")), "n": n, "L": LENGTH,
                             "requested_form": form, "requested_theta": theta.tolist(), "requested_times": TIMES,
                             "requested_coefficients": coefficients.tolist(), "exact_owner_key": key,
                             "additional_forward_or_svd": False, "budget_not_transferred": True}
                    aliases[name] = alias
                    members[name] = members[source_name]
                    metadata[name] = {**metadata[source_name], "kind": "kernel-alias", "stage": "fixed-ablation-alias", "form": form,
                                      "coefficients": coefficients.tolist()}
                    output.json(name+"-alias.json", alias)
                    counters["ablation_aliases_saved"] += 1
                    event("ablation_alias_saved", name=name, source=source_name, counters=dict(counters))
                    return
            arrays, record = calculate(form, theta, n, stage, name, coefficients_override=coefficients)
            record.update(source_evaluation_id=roles[form]["evaluation_id"], no_selection=True)
            save_full(name, arrays, record, "fixed-"+stage)
            post_records[name] = record
            del arrays
            gc.collect()
            event("fixed_postcheck_saved", name=name, status=record["status"], counters=dict(counters))

        for form in FORMS:
            if form in roles:
                for n in POST_N:
                    post(form, n, f"post-{form}-n{n}")
        if "D" in roles:
            original_coefficients = coefficients_for("D", float(roles["D"]["theta"][1]))
            endpoints_zero = original_coefficients.copy()
            endpoints_zero[0], endpoints_zero[-1] = 0., 0.
            for n in (39, 47):
                post("D", n, f"ablation-D-END-n{n}", stage="ablation", coefficients_override=endpoints_zero)
                post("D", n, f"ablation-D-ZERO-n{n}", stage="ablation", coefficients_override=np.zeros(4))
        output.json("ablation-aliases.json", aliases)
        fits = {name: ({window: metrics(member["prediction"][start:end], truth[start:end]) for window, (start, end) in WINDOWS.items()}
                      if member["valid"] else None) for name, member in members.items()}
        comparisons = {}
        for form in roles:
            chain = (("n23-n27", f"winner-{form}-n23", f"winner-{form}-n27"),
                     ("n27-n31", f"winner-{form}-n27", f"post-{form}-n31"),
                     ("n31-n39", f"post-{form}-n31", f"post-{form}-n39"),
                     ("n39-n47", f"post-{form}-n39", f"post-{form}-n47"))
            for label, left, right in chain:
                comparisons[form+"-"+label] = compare(left, right, members, truth)
        if "D" in roles:
            for n in (39, 47):
                for label in ("END", "ZERO"):
                    comparisons[f"D-{label}-n{n}"] = compare(f"post-D-n{n}", f"ablation-D-{label}-n{n}", members, truth,
                                                           threshold=END_REF if label == "END" else G_REF)
                if "A" in roles:
                    comparisons[f"D-A-n{n}"] = compare(f"post-D-n{n}", f"post-A-n{n}", members, truth)
        assessments = {}
        for form in roles:
            grid_names = [form+"-n31-n39", form+"-n39-n47"]
            grid_checks = {name: (all(item["G_below_threshold"] for item in comparisons[name]["windows"].values())
                                  if comparisons[name]["windows"] is not None else None) for name in grid_names}
            training = {str(n): {"M": roles[form]["grids"][str(n)]["training_metrics"]["mape_percent"],
                                 "W": roles[form]["grids"][str(n)]["training_metrics"]["max_percent_error"]} for n in TRAIN_N}
            training_better = all(row["M"] < M_REF and row["W"] < W_REF for row in training.values())
            final_fit = fits[f"post-{form}-n47"]
            full_better = final_fit is not None and final_fit["1-320"]["mape_percent"] < FULL_M_REF
            necessary = bool(roles[form]["joint_score"] < 1 and training_better and full_better and all(value is True for value in grid_checks.values()))
            assessments[form] = {"status": "NECESSARY_FINITE_DISCOVERY_CRITERIA_MET_MAGNITUDE_REVIEW_REQUIRED" if necessary else "NECESSARY_FINITE_DISCOVERY_CRITERIA_NOT_MET",
                                 "joint_score": roles[form]["joint_score"], "J_below_1": roles[form]["joint_score"] < 1,
                                 "training_by_grid": training, "each_training_M_W_below_external_reference": training_better,
                                 "n47_full320_M_below_external_reference": bool(full_better), "fine_grid_checks": grid_checks,
                                 "necessary_finite_discovery_criteria_met": necessary, "not_a_continuous_or_arithmetic_claim": True}
        cooling_assessment = {"status": "MISSING_D_OR_A_ROLE"}
        if all(form in roles for form in FORMS):
            training_differences = {str(n): {key: roles["D"]["grids"][str(n)]["training_metrics"][key]-roles["A"]["grids"][str(n)]["training_metrics"][key]
                                             for key in ("mape_percent", "max_percent_error")} for n in TRAIN_N}
            training_better = all(value < 0 for row in training_differences.values() for value in row.values())
            final_valid = fits["post-D-n47"] is not None and fits["post-A-n47"] is not None
            development_difference = (fits["post-D-n47"]["1-320"]["mape_percent"]-fits["post-A-n47"]["1-320"]["mape_percent"]
                                      if final_valid else None)
            end_checks = {str(n): (all(row["G_below_threshold"] for row in comparisons[f"D-END-n{n}"]["windows"].values())
                                  if comparisons[f"D-END-n{n}"]["windows"] is not None else None) for n in (39, 47)}
            changes = {}
            for left, right in (("post-D-n31", "post-D-n39"), ("post-D-n39", "post-D-n47"),
                                ("post-D-n39", "ablation-D-END-n39"), ("post-D-n47", "ablation-D-END-n47")):
                changes[left+"__"+right] = ({window: {key: fits[right][window][key]-fits[left][window][key]
                                                     for key in ("mape_percent", "max_percent_error")} for window in WINDOWS}
                                          if fits[left] is not None and fits[right] is not None else None)
            comparative = bool(primary == "D" and training_better and development_difference is not None and development_difference < 0
                               and all(value is True for value in end_checks.values()))
            necessary = bool(comparative and assessments["D"]["necessary_finite_discovery_criteria_met"])
            cooling_assessment = {"status": "NECESSARY_D_OVER_A_CRITERIA_MET_MAGNITUDE_REVIEW_REQUIRED" if necessary else "NECESSARY_D_OVER_A_CRITERIA_NOT_MET",
                                  "D_is_primary": primary == "D", "training_D_minus_A_percentage_points": training_differences,
                                  "all_training_M_W_better": training_better, "n47_full320_M_D_minus_A": development_difference,
                                  "END_four_window_G_below_point1_percent": end_checks,
                                  "actual_grid_END_metric_changes_percentage_points": changes,
                                  "relative_D_A_conditions_met": comparative,
                                  "D_finite_discovery_necessary_criteria_met": assessments["D"]["necessary_finite_discovery_criteria_met"],
                                  "all_necessary_cooling_advantage_criteria_met": necessary,
                                  "small_gain_not_certified_by_engineering_lines": True,
                                  "four_step_endpoints_not_all_spectrally_identified": True, "time_order_benefit_not_claimed": True}
        points = io.StringIO(newline="")
        writer = csv.writer(points)
        writer.writerow(["object_id", "kind", "stage", "form", "n", "dimension", "epsilon", "resolution_valid", "index", "window",
                         "target", "predicted", "nontrivial_energy", "residual", "percent_error"])
        for name, member in members.items():
            meta = metadata[name]
            for index, (actual, predicted, energy) in enumerate(zip(truth, member["prediction"], member["energy"]), 1):
                window = "1-100" if index <= 100 else "101-300" if index <= 300 else "301-320"
                writer.writerow([name, meta["kind"], meta["stage"], meta["form"], meta["n"], meta["dimension"], meta["epsilon"],
                                 member["valid"], index, window, actual, predicted, energy, predicted-actual, 100*abs(predicted-actual)/actual])
        output.binary("points.csv", points.getvalue().encode("utf-8"))
        output.json("development-fit-metrics.json", fits)
        output.json("comparisons.json", comparisons)
        output.json("finite-discovery-assessments.json", assessments)
        output.json("cooling-versus-autonomous.json", cooling_assessment)
        end_locks = verify_inputs()
        if end_locks != locks or sha(Path(__file__)) != own_hash or sha(OUT/"winners-frozen.json") != identity_hash:
            raise RuntimeError("Frozen source/input/identity changed during run")
        end_verification = {"input_count": len(locks), "all_input_hashes_match": True,
                            "script_sha256_unchanged": True, "winner_identity_sha256_unchanged": True}
        report = {"scope_id": SCOPE, "status": "completed" if len(roles) == len(FORMS) else "completed_with_missing_roles",
                  "run_passport": "UNVERIFIED", "global_joint_winner": primary, "roles": roles, "role_status": role_status,
                  "calls": calls, "unique_members": unique, "cached_calls": sum(row["cached"] for row in call_rows),
                  "invalid_unique_members": sum(not row["resolution_valid"] for row in unique_rows), "optimizers": optimizers,
                  "controls": controls, "winner_identity_sha256": identity_hash, "full_readouts": full_records,
                  "postfreeze": post_records, "ablation_aliases": aliases, "fit_metrics": fits,
                  "comparisons": comparisons, "finite_discovery_assessments": assessments,
                  "cooling_versus_autonomous": cooling_assessment, "external_history_fit_metrics": external_fits,
                  "counters": dict(counters), "end_verification": end_verification,
                  "seconds_before_final_serialization": time.perf_counter()-started,
                  "maxrss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                  "completed_utc": utc(), "output_bytes_before_result": output.size(), "new_targets_generated": False,
                  "formal_route": "UNASSIGNED; B NOT INVOKED", "time_order_effect_not_claimed": True}
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
