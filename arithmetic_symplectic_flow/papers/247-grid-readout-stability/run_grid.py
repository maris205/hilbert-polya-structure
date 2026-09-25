#!/usr/bin/env python3
"""DS04: exactly three approved grid forwards; reuse the frozen DS02 capture."""

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

sys.dont_write_bytecode = True
for env_name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[env_name] = "1"

import numpy as np

PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[1]
SOURCE = ROOT / "docs/upstream_snapshots/20260918/riemann_henon/9-robustness_sensitivity.py"
HELPER = PACKAGE.parent / "245-dynamic-start-ablation/run_comparison.py"
BASE = PACKAGE.parent / "245-dynamic-start-ablation/evidence/run-1"
BASE_NPZ = BASE / "DS02-D/spectrum.npz"
BASE_JSON = BASE / "comparison.json"
OUTPUT = PACKAGE / "evidence/run-1"
GRIDS = (260, 280, 300)
LOCKS = {
    SOURCE: "dd154507ab7138b2377b9dd7b5fc38809a62b4b1e9ecbf7d7c9ba702e6f737cb",
    HELPER: "734dfd7883cf9abc7e13b9b31205aa80077b0e77a9b2b057cb63b23d4cdb22eb",
    BASE_NPZ: "e5817dc78833b35f1f4f4b234c2ed41d6f0b2c213f56bebe128b7f0136ef0833",
    BASE_JSON: "378d861f7d86fb1afdb400f512b21f86d34b5753d956bd0ada76395f56acf982",
    PACKAGE / "candidate-card-frozen-v1.md": "90d4c96ac7b2eccbf6dfb6f3d95d4ad33298a7e5f88614a118202404fe4fce64",
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def utc():
    return datetime.now(timezone.utc).isoformat()


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def extra_diagnostics(arrays, helper):
    n = len(arrays["q"])
    for key in arrays.files:
        if not np.all(np.isfinite(arrays[key])):
            raise RuntimeError(f"Nonfinite saved array: {key}")
    if arrays["U_tot"].shape != (n, n) or len(arrays["pred"]) != 100:
        raise RuntimeError("Unexpected array shape or target coverage")
    ee = arrays["ee"]
    energy = arrays["energy_unshifted"]
    order = arrays["sort_order"]
    target = arrays["target"]
    pure = np.sort(ee) - np.min(ee)
    if pure[1] <= 0:
        raise RuntimeError("Pure-expectation anchor is not positive")
    pure_scale = target[0] / pure[1]
    pure_prediction = pure[1:101] * pure_scale
    norms = np.sum(abs(arrays["evecs"])**2, axis=0)
    return {
        "dq_actual": float(arrays["q"][1] - arrays["q"][0]),
        "dp_actual": float(arrays["p"][1] - arrays["p"][0]),
        "momentum_min": float(arrays["p"].min()),
        "momentum_max": float(arrays["p"].max()),
        "maximum_kinetic_energy": float(arrays["T_kin"].max()),
        "maximum_eigenvector_norm_error": float(np.max(abs(norms - 1))),
        "lowest_three": [{
            "rank0": int(rank), "original_eigen_index0": int(j),
            "ee": float(ee[j]), "energy_unshifted": float(energy[j]),
            "shifted_energy": float(arrays["E"][rank]),
        } for rank, j in enumerate(order[:3])],
        "ee_range": [float(ee.min()), float(ee.max())],
        "pure_expectation_DIAGNOSTIC_ONLY": {
            "first_gap": float(pure[1]), "scale": float(pure_scale),
            "metrics": helper.error_metrics(pure_prediction, target),
        },
    }, pure_prediction


def output_difference(prediction, reference, scale, reference_scale):
    delta = prediction - reference
    return {
        "rms_prediction_difference": float(np.sqrt(np.mean(delta**2))),
        "mean_absolute_prediction_difference": float(np.mean(abs(delta))),
        "maximum_absolute_prediction_difference": float(np.max(abs(delta))),
        "maximum_difference_target_index1": int(np.argmax(abs(delta)) + 1),
        "mean_absolute_relative_difference_percent": float(np.mean(abs(delta / reference)) * 100),
        "scale_ratio": float(scale / reference_scale),
    }


def main():
    for path, expected in LOCKS.items():
        if sha(path) != expected:
            raise RuntimeError(f"Input lock mismatch: {path.name}")
    if OUTPUT.exists():
        raise RuntimeError("Output exists; no overwrite or automatic repeat permitted")
    OUTPUT.mkdir()
    started = time.perf_counter()
    log = (OUTPUT / "progress.jsonl").open("x", encoding="utf-8")

    def event(name, **fields):
        line = json.dumps({"utc": utc(), "event": name, **fields}, allow_nan=False)
        print(line, flush=True)
        log.write(line + "\n")
        log.flush()

    try:
        helper = load_module("ds04_locked_capture", HELPER)
        helper.OUTPUT = OUTPUT  # Process-local output routing; no source edit.
        helper.write_json(OUTPUT / "manifest.json", {
            "scope_id": "ASFS-DISCOVERY-20260919-DS04", "started_utc": utc(),
            "pid": os.getpid(), "working_directory": str(Path.cwd()),
            "python": sys.version, "numpy": np.__version__,
            "thread_environment": {k: os.environ[k] for k in (
                "OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")},
            "input_sha256": {str(p.relative_to(ROOT)): sha(p) for p in LOCKS},
            "script_sha256": sha(Path(__file__)),
            "execution_card_sha256": sha(PACKAGE / "execution-card.md"),
            "candidate_card_sha256": sha(PACKAGE / "candidate-card.md"),
            "new_grids": list(GRIDS), "reference_grid_reused": 250,
            "initial_maxrss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        })
        event("started", pid=os.getpid(), new_grids=list(GRIDS))
        baseline = json.loads(BASE_JSON.read_text(encoding="utf-8"))["dynamic"]
        with np.load(BASE_NPZ, allow_pickle=False) as arrays:
            target = arrays["target"].copy()
            schedule = arrays["a_schedule"].copy()
            predictions = {250: arrays["pred"].copy()}
            base_extra, _ = extra_diagnostics(arrays, helper)
        base_metrics = helper.error_metrics(predictions[250], target)
        if base_metrics != baseline["metrics"]:
            raise RuntimeError("Stored N250 metrics disagree with baseline manifest")
        cases = {250: dict(baseline, experiment_id="DS04-N250-reference",
                           reused_without_forward=True, grid_diagnostics=base_extra)}
        helper.write_json(OUTPUT / "reference-250.json", cases[250])
        source = load_module("ds04_locked_solver", SOURCE)
        if not np.array_equal(target, source.TRUE_ZEROS_100):
            raise RuntimeError("Target identity mismatch")
        for n in GRIDS:
            case_id = f"DS04-N{n}"
            event("forward_start", experiment_id=case_id, N=n)
            returned, values, elapsed = helper.captured_solve(source, {"N": n})
            summary = helper.save_case(case_id, source, returned, values, elapsed)
            with np.load(OUTPUT / case_id / "spectrum.npz", allow_pickle=False) as arrays:
                if not np.array_equal(schedule, arrays["a_schedule"]):
                    raise RuntimeError("The non-autonomous schedule changed")
                extra, pure_prediction = extra_diagnostics(arrays, helper)
                predictions[n] = arrays["pred"].copy()
            summary.update(reused_without_forward=False, grid_diagnostics=extra)
            cases[n] = summary
            helper.write_json(OUTPUT / case_id / "grid-diagnostics.json", extra)
            with (OUTPUT / case_id / "pure-expectation.csv").open("x", newline="", encoding="utf-8") as handle:
                writer = csv.writer(handle)
                writer.writerow(["target_index", "target", "predicted", "residual"])
                writer.writerows((i + 1, target[i], pure_prediction[i], pure_prediction[i] - target[i]) for i in range(100))
            event("forward_complete", experiment_id=case_id, seconds=elapsed,
                  metrics=summary["metrics"], scale=summary["scale"],
                  first_gap=summary["first_excited_gap"])
            del values
        grids = (250,) + GRIDS
        differences = {}
        for i, n in enumerate(GRIDS, start=1):
            for ref in sorted({250, grids[i - 1]}):
                differences[f"N{n}_minus_N{ref}"] = output_difference(
                    predictions[n], predictions[ref], cases[n]["scale"], cases[ref]["scale"])
        with (OUTPUT / "prediction-comparison.csv").open("x", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle)
            writer.writerow(["target_index", "target"] + [f"prediction_N{n}" for n in grids]
                            + [f"N{n}_minus_N250" for n in GRIDS])
            for i in range(100):
                writer.writerow([i + 1, target[i]] + [predictions[n][i] for n in grids]
                                + [predictions[n][i] - predictions[250][i] for n in GRIDS])
        if any(sha(p) != expected for p, expected in LOCKS.items()):
            raise RuntimeError("A frozen input changed during execution")
        result = {
            "scope_id": "ASFS-DISCOVERY-20260919-DS04", "status": "completed",
            "new_forward_count": 3, "baseline_reused_not_rerun": True,
            "cases": cases, "sorted_output_differences_NOT_STATE_TRACKING": differences,
            "total_seconds_before_final_serialization": time.perf_counter() - started,
            "maxrss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            "completed_utc": utc(), "frozen_inputs_unchanged": True,
        }
        helper.write_json(OUTPUT / "comparison.json", result)
        event("completed", total_seconds=result["total_seconds_before_final_serialization"],
              new_forward_count=3)
    except Exception as error:
        event("failed", exception_type=type(error).__name__, message=str(error))
        raise
    finally:
        log.close()


if __name__ == "__main__":
    main()
