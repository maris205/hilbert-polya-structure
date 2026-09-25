#!/usr/bin/env python3
"""DS02: two approved forward calls, collecting the unchanged upstream solver."""

import csv
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import resource
import sys
import time
from datetime import datetime, timezone

for env_name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[env_name] = "1"
sys.dont_write_bytecode = True

import numpy as np


PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[1]
SOURCE = ROOT / "docs/upstream_snapshots/20260918/riemann_henon/9-robustness_sensitivity.py"
SOURCE_SHA = "dd154507ab7138b2377b9dd7b5fc38809a62b4b1e9ecbf7d7c9ba702e6f737cb"
PREVIOUS = ROOT / "papers/244-a-minus-one-dynamic-start/evidence/h1-stdout.json"
OUTPUT = PACKAGE / "evidence/run-1"


def utc():
    return datetime.now(timezone.utc).isoformat()


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, data):
    with path.open("x", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2, allow_nan=False)
        handle.write("\n")


def captured_solve(module, kwargs):
    """Only inspect return locals of the existing function; no code replacement."""
    captured = {}
    code = module.solve.__code__

    def collector(frame, event, argument):
        if event == "return" and frame.f_code is code:
            captured.update({
                key: value.copy() if isinstance(value, np.ndarray) else value
                for key, value in frame.f_locals.items()
            })

    previous_profiler = sys.getprofile()
    started = time.perf_counter()
    try:
        sys.setprofile(collector)
        returned = module.solve(**kwargs)
    finally:
        sys.setprofile(previous_profiler)
    elapsed = time.perf_counter() - started
    if not np.all(np.isfinite(returned)):
        raise RuntimeError("Nonfinite upstream return; no retry permitted")
    required = {"U_tot", "H_base", "evals", "evecs", "phases", "ee", "m", "E", "scale", "pred"}
    if not required.issubset(captured):
        raise RuntimeError(f"Missing captured locals: {required - captured.keys()}")
    if len(captured["E"]) < 101 or len(captured["pred"]) != 100:
        raise RuntimeError("Incomplete spectrum or target coverage")
    return returned, captured, elapsed


def error_metrics(prediction, target):
    error = prediction - target
    absolute = np.abs(error)
    percent = absolute / target * 100.0
    return {
        "count": int(len(target)),
        "mse": float(np.mean(error**2)),
        "rmse": float(np.sqrt(np.mean(error**2))),
        "mae": float(np.mean(absolute)),
        "mape_percent": float(np.mean(np.abs(error / target)) * 100.0),
        "max_absolute_error": float(np.max(absolute)),
        "max_absolute_error_index": int(np.argmax(absolute) + 1),
        "max_percent_error": float(np.max(percent)),
        "max_percent_error_index": int(np.argmax(percent) + 1),
        "worst_absolute_indices": (np.argsort(-absolute)[:10] + 1).tolist(),
        "worst_percent_indices": (np.argsort(-percent)[:10] + 1).tolist(),
        "first50_mse": float(np.mean(error[:50]**2)),
        "last50_mse": float(np.mean(error[50:]**2)),
        "first50_mape_percent": float(np.mean(percent[:50])),
        "last50_mape_percent": float(np.mean(percent[50:])),
    }


def save_case(case_id, module, returned, values, elapsed):
    case_dir = OUTPUT / case_id
    case_dir.mkdir()
    hbar = values["hbar"]
    phases = values["phases"]
    branch_variable = (values["ee"] * module.T_STEPS + hbar * phases) / (2 * np.pi * hbar)
    branch_margin = 0.5 - np.abs(branch_variable - values["m"])
    unshifted = (-hbar * phases + 2 * np.pi * hbar * values["m"]) / module.T_STEPS
    order = np.argsort(unshifted)
    if not np.array_equal(unshifted[order] - unshifted[order][0], values["E"]):
        raise RuntimeError("Captured sorted spectrum disagrees with provenance mapping")
    indices = np.arange(1, module.T_STEPS + 1)
    schedule = values["a_dyna"] + values["k_opt"] / np.log(indices + module.C_OFFSET)**2
    target = module.TRUE_ZEROS_100.copy()
    prediction = values["pred"]
    metrics = error_metrics(prediction, target)
    if metrics["mse"] != float(returned[0]) or metrics["mape_percent"] != float(returned[1]):
        raise RuntimeError("Postprocessing disagrees with upstream scalar outputs")
    u, h, v, lam = (values[name] for name in ("U_tot", "H_base", "evecs", "evals"))
    diagnostics = {
        "unitarity_relative_fro": float(np.linalg.norm(u.conj().T @ u - np.eye(len(u))) / np.sqrt(len(u))),
        "eigenpair_relative_fro": float(np.linalg.norm(u @ v - v * lam) / np.linalg.norm(v)),
        "hbase_hermitian_relative_fro": float(np.linalg.norm(h - h.conj().T) / np.linalg.norm(h)),
        "max_eigenvalue_unit_circle_error": float(np.max(np.abs(np.abs(lam) - 1))),
        "minimum_rounding_boundary_distance": float(np.min(branch_margin)),
        "minimum_sorted_energy_gap": float(np.min(np.diff(values["E"]))),
    }
    arrays = {name: values[name] for name in (
        "q", "p", "T_kin", "U_kin", "U_tot", "H_base", "evals", "evecs", "phases", "ee", "m", "E", "pred"
    )}
    arrays.update(target=target, a_schedule=schedule, branch_variable=branch_variable,
                  branch_margin=branch_margin, energy_unshifted=unshifted, sort_order=order)
    with (case_dir / "spectrum.npz").open("xb") as handle:
        np.savez_compressed(handle, **arrays)
    with (case_dir / "points.csv").open("x", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["target_index", "target", "predicted", "residual", "absolute_error", "percent_error", "shifted_energy", "original_eigen_index", "phase", "hbase_expectation", "integer_branch", "branch_margin"])
        for index in range(100):
            eig_index = int(order[index + 1])
            residual = float(prediction[index] - target[index])
            writer.writerow([index + 1, target[index], prediction[index], residual, abs(residual),
                             abs(residual) / target[index] * 100.0, values["E"][index + 1],
                             eig_index, phases[eig_index], values["ee"][eig_index],
                             int(values["m"][eig_index]), branch_margin[eig_index]])
    with (case_dir / "schedule.csv").open("x", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["step", "a"])
        writer.writerows(zip(indices, schedule))
    summary = {
        "experiment_id": case_id,
        "parameters": {name: float(values[name]) for name in ("hbar", "a_start", "quartic", "L")},
        "N": int(values["N"]), "S": module.T_STEPS, "c": module.C_OFFSET, "a_end": module.A_END,
        "schedule_first": float(schedule[0]), "schedule_last": float(schedule[-1]),
        "scale": float(values["scale"]), "first_excited_gap": float(values["E"][1]),
        "forward_including_capture_seconds": elapsed,
        "metrics": metrics, "diagnostics": diagnostics,
        "target_table_sha256_float64_le": hashlib.sha256(target.astype("<f8").tobytes()).hexdigest(),
    }
    write_json(case_dir / "summary.json", summary)
    return summary


def main():
    if sha256(SOURCE) != SOURCE_SHA:
        raise RuntimeError("Source lock mismatch")
    if OUTPUT.exists():
        raise RuntimeError("Output already exists; refusing overwrite or automatic repeat")
    OUTPUT.mkdir()
    started = time.perf_counter()
    log = (OUTPUT / "progress.jsonl").open("x", encoding="utf-8")

    def event(name, **fields):
        line = json.dumps({"utc": utc(), "event": name, **fields}, allow_nan=False)
        print(line, flush=True)
        log.write(line + "\n")
        log.flush()

    try:
        manifest = {
            "scope_id": "ASFS-DISCOVERY-20260918-DS02", "started_utc": utc(), "pid": os.getpid(),
            "source_sha256": sha256(SOURCE), "script_sha256": sha256(Path(__file__)),
            "card_sha256": sha256(PACKAGE / "candidate-card.md"),
            "h1_stdout_sha256": sha256(PREVIOUS), "python": sys.version, "numpy": np.__version__,
            "thread_environment": {key: os.environ[key] for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")},
            "working_directory": str(Path.cwd()), "source_path": str(SOURCE),
            "initial_maxrss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        }
        write_json(OUTPUT / "manifest.json", manifest)
        event("started", pid=os.getpid())
        spec = importlib.util.spec_from_file_location("ds02_unchanged_upstream", SOURCE)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        baseline = json.loads(PREVIOUS.read_text(encoding="utf-8"))
        event("forward_start", experiment_id="DS02-D")
        ret_d, loc_d, time_d = captured_solve(module, {})
        if not (abs(ret_d[0] - baseline["mse"]) <= 1e-10 and
                abs(ret_d[1] - baseline["mape_percent"]) <= 1e-10):
            event("baseline_mismatch", mse=float(ret_d[0]), mape_percent=float(ret_d[1]))
            raise RuntimeError("Dynamic capture differs from H1; static run not started")
        dynamic = save_case("DS02-D", module, ret_d, loc_d, time_d)
        event("forward_complete", experiment_id="DS02-D", seconds=time_d, metrics=dynamic["metrics"])
        event("forward_start", experiment_id="DS02-S")
        ret_s, loc_s, time_s = captured_solve(module, {"a_start": module.A_END})
        static = save_case("DS02-S", module, ret_s, loc_s, time_s)
        event("forward_complete", experiment_id="DS02-S", seconds=time_s, metrics=static["metrics"])
        shared_pred = loc_s["E"][1:101] * dynamic["scale"]
        target = module.TRUE_ZEROS_100
        with (OUTPUT / "static_with_dynamic_scale.csv").open("x", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle)
            writer.writerow(["target_index", "target", "predicted", "residual", "absolute_error", "percent_error"])
            for i, (truth, pred) in enumerate(zip(target, shared_pred), start=1):
                residual = float(pred - truth)
                writer.writerow([i, truth, pred, residual, abs(residual), abs(residual) / truth * 100])
        result = {
            "scope_id": "ASFS-DISCOVERY-20260918-DS02", "status": "completed",
            "dynamic": dynamic, "static": static,
            "static_with_dynamic_scale_DIAGNOSTIC_ONLY": error_metrics(shared_pred, target),
            "static_to_dynamic_mse_ratio": static["metrics"]["mse"] / dynamic["metrics"]["mse"],
            "static_to_dynamic_mape_ratio": static["metrics"]["mape_percent"] / dynamic["metrics"]["mape_percent"],
            "static_to_dynamic_scale_ratio": static["scale"] / dynamic["scale"],
            "total_seconds_before_final_serialization": time.perf_counter() - started,
            "maxrss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "completed_utc": utc(),
            "source_unchanged": sha256(SOURCE) == SOURCE_SHA,
        }
        write_json(OUTPUT / "comparison.json", result)
        event("completed", total_seconds=result["total_seconds_before_final_serialization"],
              static_to_dynamic_mse_ratio=result["static_to_dynamic_mse_ratio"],
              static_to_dynamic_mape_ratio=result["static_to_dynamic_mape_ratio"])
    except Exception as error:
        event("failed", exception_type=type(error).__name__, message=str(error))
        raise
    finally:
        log.close()


if __name__ == "__main__":
    main()
