#!/usr/bin/env python3
"""DS06 sampled single-kick diagnostic, not 300-step spectral simulation."""
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
SOURCE = ROOT / "docs/upstream_snapshots/20260918/riemann_henon/9-robustness_sensitivity.py"
SOURCE_SHA = "dd154507ab7138b2377b9dd7b5fc38809a62b4b1e9ecbf7d7c9ba702e6f737cb"
CARD_SHA = "f8a0a03ba77dc724f8dff268008a33185c129d92a7b40cb81947e0a3fc493670"
HBAR, L = .06138739295586476, 3.5

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def write_json(p, data):
    with p.open("x", encoding="utf-8") as f:
        json.dump(data, f, indent=2, allow_nan=False)
        f.write("\n")

def potential(q, a):
    return -q+q*q+a*q**3/3+.05*q**4

def main():
    started = time.perf_counter()
    if sha(SOURCE) != SOURCE_SHA or sha(PACKAGE / "candidate-card.md") != CARD_SHA:
        raise RuntimeError("Input lock mismatch")
    if OUT.exists():
        raise RuntimeError("Existing output; no overwrite/retry")
    OUT.mkdir(parents=True)
    manifest = {"scope_id": "ASFS-DISCOVERY-20260919-DS06", "pid": os.getpid(),
                "started_utc": datetime.now(timezone.utc).isoformat(),
                "source_sha256": SOURCE_SHA, "card_sha256": CARD_SHA,
                "script_sha256": sha(Path(__file__)), "python": sys.version, "numpy": np.__version__,
                "initial_maxrss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                "command": "OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 120s python -u papers/249-periodic-kick-domain/one_kick.py"}
    write_json(OUT / "manifest.json", manifest)
    print(json.dumps({"event": "started", "pid": os.getpid()}), flush=True)
    cases, arrays = [], {}
    for name, a in (("start",1.551941486210356),("end",1.02)):
        jump = np.exp(-1j*potential(L,a)/HBAR)-np.exp(-1j*potential(-L,a)/HBAR)
        delta = float(potential(L,a)-potential(-L,a))
        rows = []
        for n in (250,500,1000,2000,4000,8000):
            q = np.linspace(-L,L,n,endpoint=False)
            p = 2*np.pi*HBAR*np.fft.fftfreq(n,d=2*L/n)
            kinetic = .5*p*p
            row = {"N": n}
            arrays[f"{name}_{n}_p"] = p
            for kind,v in (("original",potential(q,a)),("smooth_control",a*np.cos(np.pi*q/L))):
                coefficient = np.fft.fft(np.exp(-1j*v/HBAR))/n
                weight = np.abs(coefficient)**2
                mean_kinetic = float(np.sum(kinetic*weight))
                if not (np.isfinite(mean_kinetic) and abs(float(weight.sum())-1)<1e-12):
                    raise RuntimeError("Invalid norm/energy")
                row[kind] = {"kinetic_expectation": mean_kinetic, "norm_error": abs(float(weight.sum())-1),
                             "highest_quarter_abs_mode_weight": float(weight[np.abs(np.fft.fftfreq(n))>=.375].sum())}
                arrays[f"{name}_{n}_{kind}_weight"] = weight
            rows.append(row)
        cases.append({"a_label": name, "a": a, "delta_V": delta,
                      "delta_V_over_2pi_hbar": float(delta/(2*np.pi*HBAR)),
                      "endpoint_multiplier_jump_abs": float(abs(jump)),
                      "exact_Fourier_symmetric_cutoff_energy_slope": float(HBAR**2*abs(jump)**2/(4*L**2)),
                      "smooth_control_exact_kinetic": float(a*a*np.pi**2/(4*L**2)), "grids": rows})
    with (OUT / "mode-weights.npz").open("xb") as f:
        np.savez_compressed(f,**arrays)
    report = {"scope_id": manifest["scope_id"], "status": "completed", "cases": cases,
              "seconds_before_serialization": time.perf_counter()-started,
              "maxrss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
              "completed_utc": datetime.now(timezone.utc).isoformat(), "source_unchanged": sha(SOURCE)==SOURCE_SHA}
    write_json(OUT / "result.json",report)
    print(json.dumps(report,allow_nan=False),flush=True)

if __name__ == "__main__":
    main()
