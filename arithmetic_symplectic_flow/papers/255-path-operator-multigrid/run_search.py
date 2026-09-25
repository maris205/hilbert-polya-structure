#!/usr/bin/env python3
"""CS05: frozen prefix-energy operators, paired-grid selection, one run only."""
import csv
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
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
OUT = PACKAGE / "evidence/run-1"
LOCK_FILE = PACKAGE / "input-locks.json"
HELPER = ROOT / "papers/251-constructive-fit-portfolio/run_search.py"
OLD253 = ROOT / "papers/253-structural-homotopy-search/evidence/run-1"
Q_SOURCE = OLD253 / "evaluations/CS03-Q-QUARTIC-0103.npz"
M_SOURCE = OLD253 / "winner-S.npz"
ALPHA_SOURCE = ROOT / "papers/252-path-energy-readout/evidence/run-1/winner-A.npz"
DEVELOPMENT_SOURCES = (
    ROOT / "papers/251-constructive-fit-portfolio/evidence/run-1/reference-101-150.json",
    OLD253 / "reference-151-200.json",
    ROOT / "papers/254-global-forms-joint-fit/evidence/run-1/reference-201-240.json",
)
S, L, A_END = 300, 3.5, 1.02
DELTA = -3.9583333333315096e-8
ALPHA = .0027300000000000002
DEFAULT = np.array([.06138741795586476, 1.5519429445436894, 1.])
LOW = np.array([.025, 1.10, .35])
HIGH = np.array([.150, 2.10, 2.20])
SNAPSHOTS = np.array([0, 43, 86, 129, 171, 214, 257, 300], dtype=int)
TRAIN_GRIDS = (320, 352)
POST_GRIDS = (384, 416)
M_REF, W_REF, G_REF = 2.2717925657954106, 14.105396903565387, 2.
FORM_IDS = {
    "P": "CS05-P-POLY-PATH", "J": "CS05-J-PERIODIC-PATH",
    "D": "CS05-D-DIRICHLET-PATH", "H": "CS05-H-HERMITE-PATH",
    "B": "CS05-B-BALANCED-PATH",
}
FULL_MATRIX_KEYS = {"U", "prefixes", "T_matrix", "H_ref", "K_raw", "K", "eigenvectors"}
COMMAND = (
    "OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 "
    "PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 600s python -u "
    "papers/255-path-operator-multigrid/run_search.py"
)


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


def relative_fro(matrix, denominator):
    return float(np.linalg.norm(matrix) / max(float(denominator), np.finfo(float).tiny))


def spectral_function(t, nu):
    if nu == 2.:
        return np.asarray(t).copy()
    return np.expm1((nu / 2.) * np.log1p(2. * t)) / nu


def hermite_basis(n, cache, event, counters):
    """Only the h=1 basis and T0 eigendecomposition are cached by N."""
    if n in cache:
        return cache[n]
    event("hermite_basis_start", grid_n=n)
    j = np.arange(n)
    q0 = np.diag(np.sqrt(np.arange(1, n) / 2.), 1)
    q0 = q0 + q0.T
    t0 = np.diag((2 * j + 1) / 4.)
    off = -np.sqrt(np.arange(1, n - 1) * np.arange(2, n)) / 4.
    t0 = t0 + np.diag(off, 2) + np.diag(off, -2)
    counters["hermite_basis_eigh"] += 1
    nodes, o = np.linalg.eigh(q0)
    counters["hermite_basis_eigh"] += 1
    raw_values, vectors = np.linalg.eigh(t0)
    minimum = float(np.min(raw_values))
    negative = raw_values < 0.
    checks = {
        "q_symmetry_fro": float(np.linalg.norm(q0 - q0.T)),
        "t_symmetry_fro": float(np.linalg.norm(t0 - t0.T)),
        "q_orthogonality_relative_fro": relative_fro(o.T @ o - np.eye(n), np.sqrt(n)),
        "t_orthogonality_relative_fro": relative_fro(vectors.T @ vectors - np.eye(n), np.sqrt(n)),
        "q_diagonalization_relative_fro": relative_fro(q0 @ o - o * nodes, np.linalg.norm(q0)),
        "t_diagonalization_relative_fro": relative_fro(t0 @ vectors - vectors * raw_values, np.linalg.norm(t0)),
        "t0_minimum_raw_eigenvalue": minimum,
        "negative_eigenvalue_count": int(np.count_nonzero(negative)),
        "negative_clip_tolerance": 1e-12,
        "maximum_clipping": max(0., -minimum),
    }
    write_json(OUT / f"hermite-basis-{n}-checks.json", checks)
    if not np.all(np.isfinite(raw_values)) or minimum < -1e-12:
        raise RuntimeError("Hermite T0 spectrum is nonfinite or below negative tolerance")
    values = np.maximum(raw_values, 0.)
    basis = {
        "Q0": q0, "T0": t0, "nodes_h1": nodes, "O": o,
        "T0_eigenvalues_raw": raw_values, "T0_eigenvalues": values,
        "T0_eigenvectors": vectors, "T_DVR_h1": o.T @ t0 @ o,
        "T0_eigenvectors_DVR": o.T @ vectors,
    }
    write_npz(OUT / f"hermite-basis-{n}.npz", basis)
    cache[n] = basis
    event("hermite_basis_complete", grid_n=n, checks=checks)
    return basis


def evolution(form, theta, alpha, helper, basis_cache, event, counters, n,
              collect_path=True):
    """One full 300-step propagation; no eigenvalue readout is done here."""
    h, a_start, nu = map(float, theta)
    if form == "H":
        basis = hermite_basis(n, basis_cache, event, counters)
        q = np.sqrt(h) * basis["nodes_h1"]
        p = np.array([], dtype=float)
        quadratic = h * basis["T0_eigenvalues"]
        kinetic = spectral_function(quadratic, nu)
        modes = basis["T0_eigenvectors_DVR"]
        if nu == 2.:
            tmat = h * basis["T_DVR_h1"]
            phase_multiplier = np.exp(-1j * basis["T0_eigenvalues"])
        else:
            tmat = (modes * kinetic) @ modes.T
            phase_multiplier = np.exp(-1j * kinetic / h)
        drift = (modes * phase_multiplier) @ modes.T

        def apply_t(matrix):
            return tmat @ matrix

        def apply_drift(matrix):
            return drift @ matrix
    else:
        if form == "D":
            q = -L + 2 * L * np.arange(1, n + 1) / (n + 1)
            p = np.pi * h * np.arange(1, n + 1) / (2 * L)
        else:
            q = np.linspace(-L, L, n, endpoint=False)
            p = np.fft.fftfreq(n) * n * np.pi * h / L
        quadratic = .5 * p * p
        kinetic = spectral_function(quadratic, nu)

        def transform(matrix, inverse=False):
            if form == "D":
                return fft.dst(matrix, type=1, axis=0, norm="ortho", workers=1)
            function = fft.ifft if inverse else fft.fft
            return function(matrix, axis=0, norm="ortho", workers=1)

        def apply_spectral(matrix, multiplier):
            return transform(multiplier[:, None] * transform(matrix), inverse=True)

        def apply_t(matrix):
            return apply_spectral(matrix, kinetic)

        drift_multiplier = np.exp(-1j * kinetic / h)

        def apply_drift(matrix):
            return apply_spectral(matrix, drift_multiplier)

        tmat = apply_t(np.eye(n, dtype=np.complex128))

    def potential(a):
        if form in ("J", "B"):
            radius = L / np.pi
            q4 = 4 * radius**4 * (1 - np.cos(q / radius))**2
            return helper.periodic(q, a) + DELTA * q4
        return helper.polynomial(q, a) + DELTA * q**4

    f = np.log(np.arange(1, S + 1) + 10.)**(-2.)
    w = (f - f[-1]) / (f[0] - f[-1])
    schedule = A_END + (a_start - A_END) * w
    endpoint_error = float(max(abs(schedule[0] - a_start), abs(schedule[-1] - A_END)))
    if endpoint_error > 1e-14 or not np.all(np.diff(schedule) < 0):
        raise RuntimeError("Frozen cooling endpoint/monotonicity check failed")
    a_ref = A_END + alpha * (a_start - A_END)
    vref = potential(a_ref)
    href = tmat + np.diag(vref)
    u = np.eye(n, dtype=np.complex128)
    prefixes = [u.copy()] if collect_path else []
    ksum = np.asarray(href, dtype=np.complex128).copy() if collect_path else None
    requested = set(map(int, SNAPSHOTS[1:]))
    for step, a in enumerate(schedule, 1):
        values = potential(a)
        if form == "B":
            half = np.exp(-.5j * values / h)
            u = half[:, None] * apply_drift(half[:, None] * u)
        else:
            u = apply_drift(np.exp(-1j * values / h)[:, None] * u)
        if collect_path and step in requested:
            prefixes.append(u.copy())
            # Same H_ref action; FFT/DST avoids one dense matrix product.
            h_u = apply_t(u) + vref[:, None] * u
            ksum += u.conj().T @ h_u
    if not np.all(np.isfinite(u)) or not np.all(np.isfinite(href)):
        raise RuntimeError("Nonfinite propagator or reference Hamiltonian")
    arrays = {
        "form_key": np.array(form), "theta": np.asarray(theta).copy(),
        "alpha": np.array(alpha), "a_ref": np.array(a_ref), "grid_n": np.array(n),
        "q": q, "p": p, "quadratic_spectrum": quadratic,
        "kinetic_spectrum": kinetic, "schedule": schedule, "V_ref": vref,
        "U": u, "T_matrix": tmat, "H_ref": href,
    }
    diagnostics = {
        "unitarity_relative_fro": relative_fro(u.conj().T @ u - np.eye(n), np.sqrt(n)),
        "t_hermitian_relative_fro": relative_fro(tmat - tmat.conj().T, np.linalg.norm(tmat)),
        "href_hermitian_relative_fro": relative_fro(href - href.conj().T, np.linalg.norm(href)),
        "schedule_endpoint_max_error": endpoint_error,
    }
    if collect_path:
        if len(prefixes) != len(SNAPSHOTS):
            raise RuntimeError("Missing frozen cumulative prefix")
        kraw = ksum / len(SNAPSHOTS)
        kval = .5 * (kraw + kraw.conj().T)
        if not np.all(np.isfinite(kval)):
            raise RuntimeError("Nonfinite path-energy matrix")
        arrays.update(snapshot_steps=SNAPSHOTS.copy(), prefixes=np.stack(prefixes),
                      K_raw=kraw, K=kval)
        trace_delta = np.trace(kraw) - np.trace(href)
        diagnostics.update(
            kraw_antihermitian_relative_fro=relative_fro(kraw - kraw.conj().T, np.linalg.norm(kraw)),
            k_hermitian_relative_fro=relative_fro(kval - kval.conj().T, np.linalg.norm(kval)),
            trace_difference_real=float(np.real(trace_delta)),
            trace_difference_imag=float(np.imag(trace_delta)),
            trace_relative_difference=float(abs(trace_delta) / max(1., abs(np.trace(href)))),
        )
    return arrays, diagnostics


def anchored_spectrum(values, target, count):
    if len(values) < count + 1 or not np.all(np.isfinite(values)):
        raise RuntimeError("Incomplete or nonfinite spectrum")
    energy = values - values[0]
    if energy[1] <= 0 or not np.all(np.diff(values) >= 0):
        raise RuntimeError("Nonpositive first gap or unordered Hermitian spectrum")
    scale = float(target[0] / energy[1])
    predicted = energy[1:count + 1] * scale
    if not np.all(np.isfinite(predicted)):
        raise RuntimeError("Nonfinite anchored prediction")
    return energy, scale, predicted


def path_forward(form, theta, target, alpha, helper, basis_cache, event, counters, n):
    arrays, diagnostics = evolution(form, theta, alpha, helper, basis_cache, event,
                                   counters, n, collect_path=True)
    counters["path_readout_eigh"] += 1
    values, vectors = np.linalg.eigh(arrays["K"])
    energy, scale, predicted = anchored_spectrum(values, target, 300)
    diagnostics.update(
        k_eigenpair_relative_fro=relative_fro(arrays["K"] @ vectors - vectors * values,
                                             np.linalg.norm(arrays["K"])),
        eigenvector_orthogonality_relative_fro=relative_fro(vectors.conj().T @ vectors - np.eye(n), np.sqrt(n)),
    )
    arrays.update(eigenvalues=values, eigenvectors=vectors, energy=energy,
                  scale=np.array(scale), predicted_300=predicted, target_100=target.copy(),
                  readout=np.array("direct_K_path_spectrum"))
    record = {
        "form": FORM_IDS[form], "form_key": form, "theta": list(map(float, theta)),
        "grid_n": n, "alpha_fixed": alpha, "a_ref": float(arrays["a_ref"]),
        "scale": scale, "first_gap": float(energy[1]),
        "metrics": helper.metrics(predicted[:100], target), "diagnostics": diagnostics,
    }
    return arrays, record


def pair_score(grid_records, grid_arrays, target):
    m = [grid_records[str(n)]["metrics"]["mape_percent"] for n in TRAIN_GRIDS]
    w = [grid_records[str(n)]["metrics"]["max_percent_error"] for n in TRAIN_GRIDS]
    cross = float(100 * np.max(abs(grid_arrays[320]["predicted_300"][:100]
                                   - grid_arrays[352]["predicted_300"][:100]) / target))
    return {"max_mape_percent": max(m), "max_percent_error": max(w),
            "cross_grid_percent": cross,
            "joint_score": max(m[0] / M_REF, m[1] / M_REF, w[0] / W_REF,
                               w[1] / W_REF, cross / G_REF)}


def rank(record):
    return (record["joint_score"], record["max_mape_percent"], record["max_percent_error"],
            record["cross_grid_percent"], record["evaluation_id"])


def legacy_regression(target, old_prediction, alpha, helper, basis_cache, event, counters):
    theta = DEFAULT.copy()
    theta[2] = 2.
    counters["regression_forwards"] += 1
    event("forward_start", stage="legacy-regression", form=FORM_IDS["P"], grid_n=250,
          theta=theta.tolist(), forward_counts=dict(counters))
    arrays, diagnostics = evolution("P", theta, alpha, helper, basis_cache, event,
                                   counters, 250, collect_path=False)
    counters["legacy_readout_eig"] += 1
    values, vectors = np.linalg.eig(arrays["U"])
    phase = np.angle(values)
    expectation = np.real(np.sum(np.conj(vectors) * (arrays["H_ref"] @ vectors), axis=0))
    h = float(theta[0])
    branch = np.round((S * expectation + h * phase) / (2 * np.pi * h))
    raw = (-h * phase + 2 * np.pi * h * branch) / S
    order = np.argsort(raw)
    energy, scale, prediction = anchored_spectrum(raw[order], target, 100)
    old_metrics = helper.metrics(old_prediction, target)
    metrics = helper.metrics(prediction, target)
    check = {
        "max_prediction_difference": float(np.max(abs(prediction - old_prediction))),
        "mape_difference_percent_points": abs(metrics["mape_percent"] - old_metrics["mape_percent"]),
        "max_percent_difference_points": abs(metrics["max_percent_error"] - old_metrics["max_percent_error"]),
    }
    check["passed"] = bool(max(check.values()) <= 1e-6)
    check.update(tolerance=1e-6, metrics=metrics, diagnostics=diagnostics,
                 theta=theta.tolist(), grid_n=250, not_used_for_selection=True)
    arrays.update(eigenvalues=values, eigenvectors=vectors, phase=phase,
                  expectation=expectation, branch=branch, raw_energy=raw, sort_order=order,
                  energy=energy, scale=np.array(scale), predicted_100=prediction,
                  target_100=target.copy(), readout=np.array("legacy_integer_branch_control"))
    write_npz(OUT / "regression-control.npz", arrays)
    write_json(OUT / "regression-control.json", check)
    event("forward_complete", stage="legacy-regression", grid_n=250, result=check,
          forward_counts=dict(counters))
    if not check["passed"]:
        raise RuntimeError("N250 legacy regression failed; no retry")


def main():
    started = time.perf_counter()
    locks = json.loads(LOCK_FILE.read_text())
    for path, wanted in locks.items():
        if sha(ROOT / path) != wanted:
            raise RuntimeError(f"Input hash mismatch: {path}")
    if OUT.exists():
        raise RuntimeError("Output exists; refusing overwrite or repeat")
    spec = importlib.util.spec_from_file_location("cs05_locked_helper", HELPER)
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    OUT.mkdir(parents=True)
    (OUT / "evaluations").mkdir()
    log = (OUT / "events.jsonl").open("x", encoding="utf-8")
    log_lock, monitor_stop = threading.Lock(), threading.Event()
    counters = {"training_forwards": 0, "regression_forwards": 0, "postfreeze_forwards": 0,
                "path_readout_eigh": 0, "static_readout_eigvalsh": 0,
                "legacy_readout_eig": 0, "hermite_basis_eigh": 0}

    def event(name, **fields):
        with log_lock:
            line = json.dumps({"utc": utc(), "event": name, **fields}, allow_nan=False)
            log.write(line + "\n")
            log.flush()
            print(line, flush=True)

    def resources():
        while not monitor_stop.wait(30):
            paths = [p for p in OUT.rglob("*") if p.is_file()]
            memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            event("resource_sample", pid=os.getpid(), seconds=time.perf_counter() - started,
                  maxrss_kib=memory, memory_advisory_above_512mib=bool(memory > 512 * 1024),
                  output_files=len(paths), output_bytes=sum(p.stat().st_size for p in paths))

    monitor = threading.Thread(target=resources, daemon=True)
    monitor.start()
    try:
        manifest = {
            "scope_id": "ASFS-DISCOVERY-20260919-CS05", "started_utc": utc(), "pid": os.getpid(),
            "inputs": locks, "input_locks_sha256": sha(LOCK_FILE), "script_sha256": sha(Path(__file__)),
            "python": sys.version, "numpy": np.__version__, "scipy": scipy.__version__,
            "thread_environment": {key: os.environ.get(key) for key in
                                   ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")},
            "command": COMMAND, "snapshot_steps": SNAPSHOTS.tolist(),
            "training_grids": list(TRAIN_GRIDS), "postfreeze_grids": list(POST_GRIDS),
            "M_ref": M_REF, "W_ref": W_REF, "G_ref_percent": G_REF,
            "run_passport": "UNVERIFIED; no independent reproduction rerun",
            "evaluation_storage": "one pair JSON plus two N-labelled compact NPZ/grid-JSON pairs per unique member",
        }
        write_json(OUT / "manifest.json", manifest)
        event("started", pid=os.getpid())
        with np.load(Q_SOURCE, allow_pickle=False) as source:
            target = source["target_100"].copy()
            old_prediction = source["energy"][1:101] * float(source["scale"])
        with np.load(M_SOURCE, allow_pickle=False) as source:
            mean_prediction = source["energy"][1:101] * float(source["scale"])
            mean_target = source["target_100"].copy()
        with np.load(ALPHA_SOURCE, allow_pickle=False) as source:
            alpha = float(source["alpha"])
        if (len(target) != 100 or not np.all(np.diff(target) > 0)
                or not np.array_equal(target, mean_target) or alpha != ALPHA):
            raise RuntimeError("Frozen target/alpha mismatch")
        if abs(helper.metrics(old_prediction, target)["max_percent_error"] - W_REF) > 1e-12:
            raise RuntimeError("Frozen worst-error reference mismatch")
        if abs(helper.metrics(mean_prediction, target)["mape_percent"] - M_REF) > 1e-12:
            raise RuntimeError("Frozen mean-error reference mismatch")
        basis_cache = {}
        legacy_regression(target, old_prediction, alpha, helper, basis_cache, event, counters)
        cache, best = {}, {}
        call_rows, unique_records, cached_rows = [], [], []
        calls, unique = 0, 0

        def objective(form, x, stage, physical=None):
            nonlocal calls, unique
            calls += 1
            default_x = (DEFAULT - LOW) / (HIGH - LOW)
            theta = (np.asarray(physical, dtype=float).copy() if physical is not None else
                     DEFAULT.copy() if np.array_equal(x, default_x) else
                     LOW + np.asarray(x, dtype=float) * (HIGH - LOW))
            if (calls > 125 or not np.all(np.isfinite(theta))
                    or np.any(theta < LOW) or np.any(theta > HIGH)):
                raise RuntimeError("Pair call or parameter boundary violated")
            key = (form, *(float(v).hex() for v in theta))
            if key in cache:
                source = cache[key]
                record = dict(source)
                record.update(call=calls, stage=stage, cached=True,
                              source_evaluation_id=source["evaluation_id"])
                call_rows.append(record)
                cached_rows.append(record)
                event("cached_pair_call", call=calls, form=FORM_IDS[form], stage=stage,
                      source_evaluation_id=source["evaluation_id"], joint_score=record["joint_score"])
                return record["joint_score"]
            unique += 1
            eid = f"{FORM_IDS[form]}-{unique:04d}"
            event("pair_evaluation_start", evaluation_id=eid, call=calls, form=FORM_IDS[form],
                  stage=stage, theta=theta.tolist())
            tick = time.perf_counter()
            pair_arrays, grids = {}, {}
            for n in TRAIN_GRIDS:
                if counters["training_forwards"] >= 250:
                    raise RuntimeError("Training forward budget exceeded")
                counters["training_forwards"] += 1
                event("forward_start", stage="training", evaluation_id=eid, grid_n=n,
                      form=FORM_IDS[form], theta=theta.tolist(), forward_counts=dict(counters))
                grid_started = time.perf_counter()
                arrays, grid = path_forward(form, theta, target, alpha, helper,
                                            basis_cache, event, counters, n)
                grid["seconds"] = time.perf_counter() - grid_started
                pair_arrays[n], grids[str(n)] = arrays, grid
                # Persist each completed dimension immediately, including a partial failed pair.
                compact = {key: value for key, value in arrays.items() if key not in FULL_MATRIX_KEYS}
                write_npz(OUT / "evaluations" / f"{eid}-N{n}.npz", compact)
                write_json(OUT / "evaluations" / f"{eid}-N{n}.json", grid)
                event("forward_complete", stage="training", evaluation_id=eid, grid_n=n,
                      metrics=grid["metrics"], seconds=grid["seconds"], forward_counts=dict(counters))
            record = {
                "evaluation_id": eid, "form": FORM_IDS[form], "form_key": form,
                "theta": theta.tolist(), "alpha_fixed": alpha, "call": calls,
                "stage": stage, "cached": False, "grids": grids,
                "seconds": time.perf_counter() - tick,
                **pair_score(grids, pair_arrays, target),
            }
            write_json(OUT / "evaluations" / f"{eid}.json", record)
            cache[key] = record
            call_rows.append(record)
            unique_records.append(record)
            if form not in best or rank(record) < rank(best[form][1]):
                best[form] = (pair_arrays, record)
            event("pair_evaluation_complete", evaluation_id=eid, joint_score=record["joint_score"],
                  cross_grid_percent=record["cross_grid_percent"],
                  max_mape_percent=record["max_mape_percent"], max_percent_error=record["max_percent_error"],
                  seconds=record["seconds"])
            return record["joint_score"]

        rng = np.random.default_rng(20260922)
        wide = rng.uniform(0, 1, (4, 3))
        seeds = [DEFAULT.copy()]
        seeds += [np.array([DEFAULT[0], DEFAULT[1], nu]) for nu in (.35, .65, 1.4, 2.2)]
        seeds += [LOW + x * (HIGH - LOW) for x in wide]
        write_json(OUT / "seed-design.json", {"seed": 20260922, "wide_normalized": wide.tolist(),
                   "physical_points_shared_by_all_forms": [point.tolist() for point in seeds]})
        for index, theta in enumerate(seeds):
            for form in FORM_IDS:
                objective(form, (theta - LOW) / (HIGH - LOW), f"seed-{index:02d}", physical=theta)
        optimizers = {}
        for form in FORM_IDS:
            x0 = (np.asarray(best[form][1]["theta"]) - LOW) / (HIGH - LOW)
            simplex = np.repeat(x0[None, :], 4, axis=0)
            for coordinate in range(3):
                simplex[coordinate + 1, coordinate] += .06 if x0[coordinate] <= .94 else -.06
            result = minimize(lambda x: objective(form, x, "refine"), x0, method="Nelder-Mead",
                              bounds=[(0., 1.)] * 3,
                              options={"maxfev": 16, "initial_simplex": simplex, "xatol": 1e-5,
                                       "fatol": 1e-5, "adaptive": False})
            optimizers[form] = {"success": bool(result.success), "message": str(result.message),
                                "nfev": int(result.nfev), "nit": int(result.nit), "fun": float(result.fun)}
            event("form_training_complete", form=FORM_IDS[form], best=best[form][1],
                  optimizer=optimizers[form])
        winner = min(best, key=lambda form: rank(best[form][1]))
        selection_time = utc()
        static_records = {}
        for form, (pair_arrays, record) in best.items():
            static_records[form] = {}
            for n in TRAIN_GRIDS:
                arrays = pair_arrays[n]
                event("static_readout_start", role=form, grid_n=n, evaluation_id=record["evaluation_id"],
                      not_a_forward=True, not_used_for_selection=True)
                counters["static_readout_eigvalsh"] += 1
                static_values = np.linalg.eigvalsh(arrays["H_ref"], UPLO="L")
                static_energy, static_scale, static_prediction = anchored_spectrum(static_values, target, 300)
                arrays.update(static_eigenvalues=static_values, static_energy=static_energy,
                              static_scale=np.array(static_scale), static_predicted_300=static_prediction,
                              static_readout=np.array("same_parameter_H_ref_eigvalsh_UPLO_L"))
                static_record = {
                    "evaluation_id": record["evaluation_id"], "form_key": form, "grid_n": n,
                    "theta": record["theta"], "scale": static_scale, "first_gap": float(static_energy[1]),
                    "metrics": helper.metrics(static_prediction[:100], target),
                    "not_used_for_selection": True,
                }
                static_records[form][str(n)] = static_record
                write_npz(OUT / f"winner-{form}-N{n}.npz", arrays)
                event("static_readout_complete", role=form, grid_n=n, result=static_record,
                      winner_array_saved=True, not_a_forward=True)
        frozen = {
            "scope_id": manifest["scope_id"], "selection_utc": selection_time, "frozen_utc": utc(),
            "global_joint_winner": winner, "roles": {form: record for form, (a, record) in best.items()},
            "static_controls": static_records, "selection": "paired N320/N352 training J_multi only",
            "calls": calls, "unique_training_members": unique, "forward_counts": dict(counters),
            "optimizers": optimizers, "evaluation_window": "241-300; not yet generated by this run",
            "development_window": "101-240; already observed and not used in objective",
        }
        write_json(OUT / "winners-frozen.json", frozen)
        write_json(OUT / "calls.json", call_rows)
        write_json(OUT / "cache-calls.json", cached_rows)
        write_json(OUT / "unique-members.json", unique_records)
        write_json(OUT / "static-controls.json", static_records)
        event("training_frozen", global_joint_winner=winner, sha256=sha(OUT / "winners-frozen.json"),
              role_count=len(best), full_winner_arrays=2 * len(best), calls=calls,
              unique_training_members=unique, forward_counts=dict(counters))
        event("postfreeze_reference_start", first=241, last=300, no_further_selection=True)
        import mpmath as mp
        mp.mp.dps = 40
        strings = [str(mp.im(mp.zetazero(index))) for index in range(241, 301)]
        future = np.array([float(value) for value in strings])
        write_json(OUT / "reference-241-300.json", {
            "first": 241, "last": 300, "decimal_precision": 40, "mpmath": mp.__version__,
            "ordinates": strings, "scope": "postfreeze reference; not certified or historically blind",
        })
        event("development_reference_read", sources=[str(path.relative_to(ROOT)) for path in DEVELOPMENT_SOURCES])
        development = np.array([float(value) for path in DEVELOPMENT_SOURCES
                                for value in json.loads(path.read_text())["ordinates"]])
        if len(development) != 140 or len(future) != 60:
            raise RuntimeError("Unexpected development/evaluation reference length")
        truth = np.concatenate([target, development, future])

        def windows(prediction):
            return {"training_1_100": helper.metrics(prediction[:100], target),
                    "development_101_240": helper.metrics(prediction[100:240], development),
                    "evaluation_241_300": helper.metrics(prediction[240:300], future)}

        post, static_post = {}, {}
        for form, (pair_arrays, record) in best.items():
            post[form] = {str(n): windows(pair_arrays[n]["predicted_300"]) for n in TRAIN_GRIDS}
            static_post[form] = {str(n): windows(pair_arrays[n]["static_predicted_300"]) for n in TRAIN_GRIDS}

        def point_table(path, field):
            with path.open("x", newline="", encoding="utf-8") as handle:
                writer = csv.writer(handle)
                writer.writerow(["role", "grid_n", "index", "window", "target", "predicted", "residual", "percent_error"])
                for form, (pair_arrays, record) in best.items():
                    for n in TRAIN_GRIDS:
                        for index, (actual, prediction) in enumerate(zip(truth, pair_arrays[n][field]), 1):
                            window = "train" if index <= 100 else "development" if index <= 240 else "postfreeze-evaluation"
                            writer.writerow([form, n, index, window, actual, prediction,
                                             prediction - actual, 100 * abs(prediction - actual) / actual])

        point_table(OUT / "winner-points.csv", "predicted_300")
        point_table(OUT / "static-control-points.csv", "static_predicted_300")
        event("postfreeze_evaluation_complete", roles=post, static_controls=static_post)
        resolutions = []
        primary_arrays, primary_record = best[winner]
        primary_320 = primary_arrays[320]["predicted_300"][:100]
        for n in POST_GRIDS:
            counters["postfreeze_forwards"] += 1
            event("forward_start", stage="postfreeze-grid", form=FORM_IDS[winner], grid_n=n,
                  theta=primary_record["theta"], forward_counts=dict(counters))
            arrays, record = path_forward(winner, primary_record["theta"], target, alpha,
                                         helper, basis_cache, event, counters, n)
            record.update(windows=windows(arrays["predicted_300"]),
                          cross_grid_to_320_percent=float(100 * np.max(abs(arrays["predicted_300"][:100] - primary_320) / target)),
                          comparison_line_percent=G_REF, new_forward=True,
                          not_used_for_selection=True)
            write_npz(OUT / f"resolution-{n}.npz", arrays)
            resolutions.append(record)
            event("forward_complete", stage="postfreeze-grid", grid_n=n, result=record,
                  forward_counts=dict(counters))
        report = {
            "scope_id": manifest["scope_id"], "status": "completed", "global_joint_winner": winner,
            "roles": frozen["roles"], "static_controls": static_records,
            "postfreeze": post, "static_postfreeze": static_post, "resolutions": resolutions,
            "calls": calls, "cached_calls": len(cached_rows), "unique_training_members": unique,
            "forward_counts": dict(counters),
            "total_forwards": sum(counters[key] for key in ("training_forwards", "regression_forwards", "postfreeze_forwards")),
            "optimizers": optimizers, "seconds_before_final_serialization": time.perf_counter() - started,
            "maxrss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "completed_utc": utc(),
            "all_inputs_unchanged": all(sha(ROOT / path) == wanted for path, wanted in locks.items()),
        }
        write_json(OUT / "result.json", report)
        monitor_stop.set()
        monitor.join(timeout=1)
        event("completed", global_joint_winner=winner, joint_score=primary_record["joint_score"],
              seconds=report["seconds_before_final_serialization"], forward_counts=dict(counters),
              maxrss_kib=report["maxrss_kib"])
        write_json(OUT / "file-inventory.json", {str(path.relative_to(OUT)): path.stat().st_size
                                                for path in sorted(OUT.rglob("*")) if path.is_file()})
    except Exception as exc:
        event("failed", type=type(exc).__name__, message=str(exc), forward_counts=dict(counters))
        raise
    finally:
        monitor_stop.set()
        monitor.join(timeout=1)
        log.close()


if __name__ == "__main__":
    main()
