#!/usr/bin/env python3
"""DS05: fixed diagnostics of saved spectra; no evolution or eigensolve."""
import csv
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import resource
import sys
import time
import numpy as np

PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[1]
OUT = PACKAGE / "evidence/run-1"
LOCKS = {
    250: ("papers/245-dynamic-start-ablation/evidence/run-1/DS02-D/spectrum.npz", "e5817dc78833b35f1f4f4b234c2ed41d6f0b2c213f56bebe128b7f0136ef0833"),
    260: ("papers/247-grid-readout-stability/evidence/run-1/DS04-N260/spectrum.npz", "ef514016e2ff64eda1c6430b407d43d16bb195060f2b1180b4099c651547054d"),
    280: ("papers/247-grid-readout-stability/evidence/run-1/DS04-N280/spectrum.npz", "9ca78309a6ad37848518193fded8ddc90b16d59b519814edca1d82095472dbb4"),
    300: ("papers/247-grid-readout-stability/evidence/run-1/DS04-N300/spectrum.npz", "04fe90f80958e5caf71faa4548c60db02ac340f2032bbb874c709680981c4638"),
}
CARD_SHA = "63ec481460f32e1a6ac2167cc189c5d2749628dfa21ebba2d9110e3092ef4e0c"

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def write_json(p, data):
    with p.open("x", encoding="utf-8") as f:
        json.dump(data, f, indent=2, allow_nan=False)
        f.write("\n")

def main():
    started = time.perf_counter()
    if sha(PACKAGE / "candidate-card.md") != CARD_SHA:
        raise RuntimeError("Card mismatch")
    if OUT.exists():
        raise RuntimeError("Existing output; no overwrite/retry")
    data = {}
    for n, (rel, expected) in LOCKS.items():
        if sha(ROOT / rel) != expected:
            raise RuntimeError(f"Input mismatch N{n}")
        with np.load(ROOT / rel, allow_pickle=False) as z:
            data[n] = {k: z[k].copy() for k in ("E", "target", "a_schedule", "pred")}
    ref = data[250]
    base = ref["E"][1:101]
    OUT.mkdir(parents=True)
    manifest = {
        "scope_id": "ASFS-DISCOVERY-20260919-DS05", "pid": os.getpid(),
        "started_utc": datetime.now(timezone.utc).isoformat(), "inputs": LOCKS,
        "script_sha256": sha(Path(__file__)), "card_sha256": CARD_SHA,
        "python": sys.version, "numpy": np.__version__,
        "initial_maxrss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "command": "OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 120s python -u papers/248-anchor-shape-decomposition/analyze_saved.py",
    }
    write_json(OUT / "manifest.json", manifest)
    print(json.dumps({"event": "started", "pid": os.getpid()}), flush=True)
    results = []
    with (OUT / "all-points.csv").open("x", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["N", "anchor", "index", "gap", "target", "diagnostic_prediction", "relative_error_percent", "shape_ratio_to_N250", "log_raw_gap_ratio", "log_first_gap_ratio", "log_original_prediction_ratio"])
        for n, z in data.items():
            d, target = z["E"][1:101], z["target"]
            if not (np.all(np.isfinite(d)) and np.all(d > 0) and
                    np.array_equal(target, ref["target"]) and
                    np.array_equal(z["a_schedule"], ref["a_schedule"])):
                raise RuntimeError(f"Invalid input N{n}")
            log_raw, log_first = np.log(d / base), float(np.log(d[0] / base[0]))
            log_prediction = np.log(z["pred"] / ref["pred"])
            residual = float(np.max(np.abs(log_prediction - (log_raw - log_first))))
            anchors = []
            for r in (1, 10, 50, 100):
                pred = target[r-1] * d / d[r-1]
                shape_ratio = (d / d[r-1]) / (base / base[r-1])
                error = 100 * (pred - target) / target
                anchors.append({
                    "anchor": r, "scale": float(target[r-1] / d[r-1]),
                    "mape_percent": float(np.mean(np.abs(error))),
                    "mse": float(np.mean((pred-target)**2)),
                    "shape_mean_absolute_percent_to_N250": float(100*np.mean(np.abs(shape_ratio-1))),
                    "shape_max_absolute_percent_to_N250": float(100*np.max(np.abs(shape_ratio-1))),
                })
                for j in range(100):
                    w.writerow([n,r,j+1,d[j],target[j],pred[j],error[j],shape_ratio[j],log_raw[j],log_first,log_prediction[j]])
            results.append({"N": n, "gap_ratios_at_1_10_50_100": [float(d[r-1]/base[r-1]) for r in (1,10,50,100)],
                            "log_identity_max_residual": residual, "anchors": anchors})
    report = {"scope_id": manifest["scope_id"], "status": "completed", "cases": results,
              "seconds_before_serialization": time.perf_counter()-started,
              "maxrss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
              "completed_utc": datetime.now(timezone.utc).isoformat(),
              "all_inputs_unchanged": all(sha(ROOT / rel)==expected for rel,expected in LOCKS.values())}
    write_json(OUT / "result.json", report)
    print(json.dumps(report, allow_nan=False), flush=True)

if __name__ == "__main__":
    main()
