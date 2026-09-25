#!/usr/bin/env python3
"""CS04: five frozen global constructions and a joint training objective."""
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
OLD = ROOT / "papers/253-structural-homotopy-search/evidence/run-1"
Q_CONTROL = OLD / "evaluations/CS03-Q-QUARTIC-0103.npz"
S_CONTROL = OLD / "winner-S.npz"
ALPHA_SOURCE = ROOT / "papers/252-path-energy-readout/evidence/run-1/winner-A.npz"
DEV1 = ROOT / "papers/251-constructive-fit-portfolio/evidence/run-1/reference-101-150.json"
DEV2 = OLD / "reference-151-200.json"
S, L, A_END = 300, 3.5, 1.02
BASE_H, BASE_A = .06138741795586476, 1.5519429445436894
DELTA = -3.9583333333315096e-8
M_REF, W_REF = 2.2717925657954106, 14.105396903565387
FORM_IDS = {"F": "CS04-F-SOFT-POWER", "L": "CS04-L-LOG-DISPERSION",
            "W": "CS04-W-POSITION-WARP", "A": "CS04-A-ALTERNATING-DRIVE",
            "H": "CS04-H-HERMITE-DVR"}
Z_BOUNDS = {"F": (.7, 2.3), "L": (0., 3.), "W": (0., 3.), "A": (0., 1.), "H": (-.04, .15)}
STRUCTURAL = {"F": [.7, .9, 1.1, 1.4, 1.7, 1.9, 2.1, 2.3],
              "L": [1e-6, 1e-4, .001, .01, .1, .5, 1.5, 3.],
              "W": [1e-5, .001, .01, .1, .5, 1., 2., 3.],
              "A": [1e-6, 1e-4, .001, .01, .1, .3, .6, 1.],
              "H": [-.04, -.01, -.001, 0., .001, .01, .05, .15]}


def utc():
    return datetime.now(timezone.utc).isoformat()


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def write_json(p, value):
    with p.open("x", encoding="utf-8") as f:
        json.dump(value, f, indent=2, allow_nan=False)
        f.write("\n")


def write_npz(p, value):
    with p.open("xb") as f:
        np.savez_compressed(f, **value)


def bounds(form):
    lo, hi = Z_BOUNDS[form]
    return np.array([.045, 1.10, lo]), np.array([.085, 2.10, hi])


def default(form):
    return np.array([BASE_H, BASE_A, 2. if form == "F" else 0.])


def score(metrics):
    return max(metrics["mape_percent"] / M_REF, metrics["max_percent_error"] / W_REF)


def rank(record, role="joint"):
    m, w = record["metrics"]["mape_percent"], record["metrics"]["max_percent_error"]
    if role == "mean":
        return m, w, record["evaluation_id"]
    if role == "worst":
        return w, m, record["evaluation_id"]
    return record["joint_score"], m, w, record["evaluation_id"]


def hermite_basis(n, cache, event):
    if n in cache:
        return cache[n]
    event("hermite_basis_start", grid_n=n)
    j = np.arange(n)
    q0 = np.diag(np.sqrt(np.arange(1, n) / 2.), 1)
    q0 = q0 + q0.T
    t0 = np.diag((2*j+1)/4.)
    off = -np.sqrt(np.arange(1, n-1)*np.arange(2, n))/4.
    t0 = t0 + np.diag(off, 2) + np.diag(off, -2)
    nodes, o = np.linalg.eigh(q0)
    vals, v = np.linalg.eigh(t0)
    tdvr = o.T @ t0 @ o
    drift = o.T @ ((v * np.exp(-1j*vals)) @ v.T) @ o
    checks = {"q_symmetry": float(np.linalg.norm(q0-q0.T)),
              "t_symmetry": float(np.linalg.norm(t0-t0.T)),
              "orthogonality_relative_fro": float(np.linalg.norm(o.T@o-np.eye(n))/np.sqrt(n)),
              "q_diagonalization_relative_fro": float(np.linalg.norm(q0@o-o*nodes)/np.linalg.norm(q0)),
              "drift_unitarity_relative_fro": float(np.linalg.norm(drift.conj().T@drift-np.eye(n))/np.sqrt(n))}
    if max(checks.values()) > 1e-11:
        raise RuntimeError("Hermite basis preflight failed")
    basis = {"q0": q0, "T_G_h1": t0, "nodes_h1": nodes, "O": o,
             "T_DVR_h1": tdvr, "drift": drift}
    write_npz(OUT/f"hermite-basis-{n}.npz", basis)
    write_json(OUT/f"hermite-basis-{n}-checks.json", checks)
    cache[n] = basis
    event("hermite_basis_complete", grid_n=n, checks=checks)
    return basis


def forward(form, theta, target, alpha, helper, basis_cache, event, n=250):
    h, a_start, z = map(float, theta)
    if form == "H":
        basis = hermite_basis(n, basis_cache, event)
        q = np.sqrt(h)*basis["nodes_h1"]
        p, kinetic = np.array([]), np.array([])
        tmat, drift = h*basis["T_DVR_h1"], basis["drift"]
        def drift_apply(mat):
            return drift @ mat
    else:
        q = np.linspace(-L, L, n, endpoint=False)
        p = np.fft.fftfreq(n)*n*np.pi*h/L
        kinetic = .5*p*p
        if form == "F" and z != 2.:
            kinetic = np.expm1((z/2.)*np.log1p(p*p))/z
        if form == "L" and z != 0.:
            kinetic = np.log1p(z*p*p)/(2*z)
        def apply_kinetic(mat, multiplier):
            return fft.ifft(multiplier[:, None]*fft.fft(mat, axis=0, norm="ortho", workers=1),
                            axis=0, norm="ortho", workers=1)
        drift = np.exp(-1j*kinetic/h)
        tmat = apply_kinetic(np.eye(n, dtype=np.complex128), kinetic)
        def drift_apply(mat):
            return apply_kinetic(mat, drift)
    qpot = L*np.tanh(z*q/L)/np.tanh(z) if form == "W" and z != 0. else q
    def potential(a):
        value = helper.polynomial(qpot, a) + DELTA*qpot**4
        return value + z*q**4 if form == "H" and z != 0. else value
    f = np.log(np.arange(1, S+1)+10.)**(-2.)
    w = (f-f[-1])/(f[0]-f[-1])
    if form == "A" and z != 0.:
        w = w*((1-z)+z*(-1.)**np.arange(S))
    schedule = A_END+(a_start-A_END)*w
    endpoints = max(abs(schedule[0]-a_start), abs(schedule[-1]-A_END))
    if endpoints > 1e-14 or (form != "A" and not np.all(np.diff(schedule) < 0)):
        raise RuntimeError("Schedule invariant failed")
    u = np.eye(n, dtype=np.complex128)
    for a in schedule:
        u = drift_apply(np.exp(-1j*potential(a)/h)[:, None]*u)
    a_ref = A_END+alpha*(a_start-A_END)
    href = tmat+np.diag(potential(a_ref))
    vals, vec = np.linalg.eig(u)
    phase = np.angle(vals)
    ee = np.real(np.sum(np.conj(vec)*(href@vec), axis=0))
    branch = np.round((S*ee+h*phase)/(2*np.pi*h))
    raw = (-h*phase+2*np.pi*h*branch)/S
    order = np.argsort(raw)
    energy = raw[order]-raw[order[0]]
    if len(energy) < 241 or not np.all(np.isfinite(energy)) or energy[1] <= 0:
        raise RuntimeError("Incomplete spectrum or nonpositive first gap")
    scale = float(target[0]/energy[1])
    pred = energy[1:241]*scale
    arrays = {"q": q, "q_potential": qpot, "p": p, "kinetic": kinetic, "schedule": schedule,
              "U": u, "H_ref": href, "T_matrix": tmat, "eigenvalues": vals, "eigenvectors": vec,
              "phase": phase, "expectation": ee, "branch": branch, "energy_unshifted": raw,
              "sort_order": order, "energy": energy, "predicted_240": pred,
              "theta": np.asarray(theta), "alpha": np.array(alpha), "a_ref": np.array(a_ref),
              "scale": np.array(scale), "target_100": target}
    diagnostics = {"unitarity_relative_fro": float(np.linalg.norm(u.conj().T@u-np.eye(n))/np.sqrt(n)),
                   "eigenpair_relative_fro": float(np.linalg.norm(u@vec-vec*vals)/np.linalg.norm(vec)),
                   "eigenvector_norm_max_error": float(np.max(np.abs(np.sum(abs(vec)**2, axis=0)-1))),
                   "href_hermitian_relative_fro": float(np.linalg.norm(href-href.conj().T)/np.linalg.norm(href)),
                   "schedule_endpoint_max_error": float(endpoints)}
    metrics = helper.metrics(pred[:100], target)
    return arrays, {"form": FORM_IDS[form], "form_key": form, "theta": list(map(float, theta)),
                    "alpha_fixed": alpha, "a_ref": float(a_ref), "grid_n": n, "scale": scale,
                    "first_gap": float(energy[1]), "metrics": metrics, "joint_score": score(metrics),
                    "diagnostics": diagnostics}


def main():
    started = time.perf_counter()
    locks = json.loads(LOCK_FILE.read_text())
    for path, want in locks.items():
        if sha(ROOT/path) != want:
            raise RuntimeError(f"Input hash mismatch: {path}")
    if OUT.exists():
        raise RuntimeError("Output exists; refusing overwrite or repeat")
    spec = importlib.util.spec_from_file_location("cs04_locked_helper", HELPER)
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    OUT.mkdir(parents=True)
    (OUT/"evaluations").mkdir()
    log = (OUT/"events.jsonl").open("x", encoding="utf-8")
    log_lock, monitor_stop = threading.Lock(), threading.Event()

    def event(name, **fields):
        line = json.dumps({"utc": utc(), "event": name, **fields}, allow_nan=False)
        with log_lock:
            log.write(line+"\n")
            log.flush()
            print(line, flush=True)

    def resources():
        while not monitor_stop.wait(30):
            paths = [p for p in OUT.rglob("*") if p.is_file()]
            event("resource_sample", pid=os.getpid(), seconds=time.perf_counter()-started,
                  maxrss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                  output_files=len(paths), output_bytes=sum(p.stat().st_size for p in paths))

    monitor = threading.Thread(target=resources, daemon=True)
    monitor.start()
    try:
        manifest = {"scope_id": "ASFS-DISCOVERY-20260919-CS04", "started_utc": utc(), "pid": os.getpid(),
                    "inputs": locks, "input_locks_sha256": sha(LOCK_FILE), "script_sha256": sha(Path(__file__)),
                    "python": sys.version, "numpy": np.__version__, "scipy": scipy.__version__,
                    "thread_environment": {k: os.environ.get(k) for k in
                                           ["OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"]},
                    "command": "OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 600s python -u papers/254-global-forms-joint-fit/run_search.py"}
        write_json(OUT/"manifest.json", manifest)
        event("started", pid=os.getpid())
        with np.load(Q_CONTROL, allow_pickle=False) as z:
            target = z["target_100"].copy()
            q_pred = z["energy"][1:241]*float(z["scale"])
        with np.load(S_CONTROL, allow_pickle=False) as z:
            s_pred = z["energy"][1:241]*float(z["scale"])
        with np.load(ALPHA_SOURCE, allow_pickle=False) as z:
            alpha = float(z["alpha"])
        if len(target) != 100 or not np.all(np.diff(target) > 0) or alpha != .0027300000000000002:
            raise RuntimeError("Frozen target/alpha mismatch")
        if abs(helper.metrics(s_pred[:100], target)["mape_percent"]-M_REF) > 1e-12:
            raise RuntimeError("Mean score reference mismatch")
        if abs(helper.metrics(q_pred[:100], target)["max_percent_error"]-W_REF) > 1e-12:
            raise RuntimeError("Worst score reference mismatch")
        cache, best, champions, basis_cache = {}, {}, {}, {}
        calls, unique, shared_arrays = 0, 0, None
        call_rows, unique_records = [], []

        def consider(form, arrays, record):
            if form not in best or rank(record) < rank(best[form][1]):
                if arrays is None:
                    raise RuntimeError("Cache lacked improving member arrays")
                best[form] = (arrays, record)
            for role in ("mean", "worst"):
                if role not in champions or rank(record, role) < rank(champions[role][1], role):
                    if arrays is None:
                        raise RuntimeError("Cache lacked champion arrays")
                    champions[role] = (arrays, record)

        def objective(form, x, stage, physical=None):
            nonlocal calls, unique, shared_arrays
            calls += 1
            low, high = bounds(form)
            d = default(form)
            dx = (d-low)/(high-low)
            theta = (np.asarray(physical, dtype=float).copy() if physical is not None else
                     d.copy() if np.array_equal(x, dx) else low+np.asarray(x)*(high-low))
            if np.any(theta < low) or np.any(theta > high) or calls > 285:
                raise RuntimeError("Parameter/budget boundary violated")
            common = form != "H" and np.array_equal(theta, d)
            key = ("shared-default",) if common else (form, *(float(v).hex() for v in theta))
            if key in cache:
                source = cache[key]
                record = dict(source)
                record.update(form=FORM_IDS[form], form_key=form, theta=theta.tolist(), call=calls,
                              stage=stage, cached=True, source_evaluation_id=source["evaluation_id"])
                arrays = {**shared_arrays, "theta": theta.copy()} if common else None
                consider(form, arrays, record)
                call_rows.append(record)
                event("cached_call", call=calls, form=FORM_IDS[form], stage=stage,
                      source_id=source["evaluation_id"], joint_score=record["joint_score"])
                return record["joint_score"]
            unique += 1
            eid = f"{FORM_IDS[form]}-{unique:04d}"
            event("evaluation_start", evaluation_id=eid, call=calls, form=FORM_IDS[form],
                  stage=stage, theta=theta.tolist(), alpha_fixed=alpha)
            tick = time.perf_counter()
            arrays, record = forward(form, theta, target, alpha, helper, basis_cache, event)
            record.update(evaluation_id=eid, call=calls, stage=stage, cached=False,
                          seconds=time.perf_counter()-tick)
            if unique == 1:
                old_metrics = helper.metrics(q_pred[:100], target)
                check = {"max_prediction_difference": float(np.max(abs(arrays["predicted_240"][:100]-q_pred[:100]))),
                         "mape_difference_percent_points": abs(record["metrics"]["mape_percent"]-old_metrics["mape_percent"]),
                         "max_percent_difference_points": abs(record["metrics"]["max_percent_error"]-old_metrics["max_percent_error"])}
                check["passed"] = bool(max(check.values()) <= 1e-6)
                check["tolerance"] = 1e-6
                write_json(OUT/"regression-control.json", check)
                if not check["passed"]:
                    raise RuntimeError("Q0103 regression failed; no retry")
                shared_arrays = arrays
            compact = {k: v for k, v in arrays.items() if k not in ("U", "H_ref", "T_matrix", "eigenvectors")}
            write_npz(OUT/"evaluations"/(eid+".npz"), compact)
            write_json(OUT/"evaluations"/(eid+".json"), record)
            cache[key] = record
            unique_records.append(record)
            call_rows.append(record)
            consider(form, arrays, record)
            event("evaluation_complete", evaluation_id=eid, joint_score=record["joint_score"],
                  mape_percent=record["metrics"]["mape_percent"],
                  max_percent_error=record["metrics"]["max_percent_error"], seconds=record["seconds"])
            return record["joint_score"]

        rng = np.random.default_rng(20260921)
        wide = rng.uniform(0, 1, (4, 3))
        local = rng.uniform(-1, 1, (4, 3))*np.array([1e-7, 1e-5, 1e-3, 1e-2])[:, None]
        seeds = {}
        for form in FORM_IDS:
            low, high = bounds(form)
            d = default(form)
            dx = (d-low)/(high-low)
            physical = [d]+[np.array([BASE_H, BASE_A, z]) for z in STRUCTURAL[form]]
            physical += [low+x*(high-low) for x in wide]
            physical += [low+x*(high-low) for x in np.clip(dx+local, 0, 1)]
            seeds[form] = physical
        write_json(OUT/"seed-design.json", {"seed": 20260921, "wide_normalized": wide.tolist(),
                   "local_normalized_delta": local.tolist(),
                   "physical_points": {f: [x.tolist() for x in xs] for f, xs in seeds.items()}})
        for i in range(17):
            for form in FORM_IDS:
                low, high = bounds(form)
                theta = seeds[form][i]
                objective(form, (theta-low)/(high-low), f"seed-{i:02d}", physical=theta)
        optimizers = {}
        for form in FORM_IDS:
            low, high = bounds(form)
            optimizers[form] = []
            for stage, edge in enumerate((.005, 2e-7), 1):
                x0 = (np.array(best[form][1]["theta"])-low)/(high-low)
                simplex = np.repeat(x0[None, :], 4, axis=0)
                for j in range(3):
                    simplex[j+1, j] += edge if x0[j] <= 1-edge else -edge
                result = minimize(lambda x: objective(form, x, f"refine-{stage}"), x0,
                                  method="Nelder-Mead", bounds=[(0., 1.)]*3,
                                  options={"maxfev": 20, "initial_simplex": simplex, "xatol": 1e-6,
                                           "fatol": 1e-6, "adaptive": False})
                rec = {"success": bool(result.success), "message": str(result.message),
                       "nfev": int(result.nfev), "nit": int(result.nit), "fun": float(result.fun), "edge": edge}
                optimizers[form].append(rec)
                event("optimizer_stage_complete", form=FORM_IDS[form], stage=stage, result=rec)
        winner = min(best, key=lambda f: rank(best[f][1]))
        roles = {f"joint-{f}": pair for f, pair in best.items()}
        roles.update({f"secondary-{r}": pair for r, pair in champions.items()})
        pareto = [r for r in unique_records if not any(
            s["metrics"]["mape_percent"] <= r["metrics"]["mape_percent"] and
            s["metrics"]["max_percent_error"] <= r["metrics"]["max_percent_error"] and
            (s["metrics"]["mape_percent"] < r["metrics"]["mape_percent"] or
             s["metrics"]["max_percent_error"] < r["metrics"]["max_percent_error"])
            for s in unique_records)]
        frozen = {"scope_id": manifest["scope_id"], "frozen_utc": utc(), "global_joint_winner": winner,
                  "selection": "training J=max(M/M_ref,W/W_ref); seven predeclared roles",
                  "M_ref": M_REF, "W_ref": W_REF, "roles": {k: r for k, (a, r) in roles.items()},
                  "calls": calls, "unique_training_forwards": unique, "optimizers": optimizers,
                  "evaluation_window": "201-240; reference not yet generated by this run"}
        write_json(OUT/"winners-frozen.json", frozen)
        for role, (arrays, record) in roles.items():
            write_npz(OUT/f"winner-{role}.npz", arrays)
        write_json(OUT/"calls.json", call_rows)
        write_json(OUT/"training-pareto.json", pareto)
        event("training_frozen", global_joint_winner=winner, sha256=sha(OUT/"winners-frozen.json"),
              calls=calls, unique_forwards=unique, distinct_role_members=len({r["evaluation_id"] for a, r in roles.values()}))
        event("postfreeze_reference_start", first=201, last=240, no_further_selection=True)
        import mpmath as mp
        mp.mp.dps = 40
        strings = [str(mp.im(mp.zetazero(j))) for j in range(201, 241)]
        future = np.array([float(v) for v in strings])
        write_json(OUT/"reference-201-240.json", {"first": 201, "last": 240, "decimal_precision": 40,
                   "mpmath": mp.__version__, "ordinates": strings,
                   "scope": "postfreeze numerical reference, not certified and not historically blind"})
        event("development_reference_read", sources=[str(DEV1.relative_to(ROOT)), str(DEV2.relative_to(ROOT))])
        dev = np.array([float(v) for path in (DEV1, DEV2) for v in json.loads(path.read_text())["ordinates"]])
        truth = np.concatenate([target, dev, future])

        def windows(pred):
            return {"training_1_100": helper.metrics(pred[:100], target),
                    "development_101_200": helper.metrics(pred[100:200], dev),
                    "evaluation_201_240": helper.metrics(pred[200:240], future)}

        post = {role: windows(a["predicted_240"]) for role, (a, r) in roles.items()}
        controls = {"CS03-Q0103": windows(q_pred), "CS03-S-winner": windows(s_pred)}
        def point_table(path, predictions):
            with path.open("x", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["role", "index", "window", "target", "predicted", "residual", "percent_error"])
                for role, pred in predictions.items():
                    for j, (t, p) in enumerate(zip(truth, pred), 1):
                        window = "train" if j <= 100 else "development" if j <= 200 else "postfreeze-evaluation"
                        writer.writerow([role, j, window, t, p, p-t, 100*abs(p-t)/t])
        point_table(OUT/"winner-points.csv", {k: a["predicted_240"] for k, (a, r) in roles.items()})
        point_table(OUT/"control-points.csv", {"CS03-Q0103": q_pred, "CS03-S-winner": s_pred})
        event("postfreeze_evaluation_complete", results=post, controls=controls)
        resolutions = []
        for n in (260, 280):
            theta = best[winner][1]["theta"]
            event("resolution_start", form=FORM_IDS[winner], grid_n=n, theta=theta)
            arrays, record = forward(winner, theta, target, alpha, helper, basis_cache, event, n=n)
            record["windows"] = windows(arrays["predicted_240"])
            write_npz(OUT/f"resolution-{n}.npz", arrays)
            resolutions.append(record)
            event("resolution_complete", result=record)
        report = {"scope_id": manifest["scope_id"], "status": "completed", "global_joint_winner": winner,
                  "roles": frozen["roles"], "postfreeze": post, "controls": controls, "resolutions": resolutions,
                  "calls": calls, "unique_training_forwards": unique, "new_resolution_forwards": 2,
                  "optimizers": optimizers, "training_pareto_count": len(pareto),
                  "seconds_before_final_serialization": time.perf_counter()-started,
                  "maxrss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "completed_utc": utc(),
                  "all_inputs_unchanged": all(sha(ROOT/p) == h for p, h in locks.items())}
        write_json(OUT/"result.json", report)
        monitor_stop.set()
        monitor.join(timeout=1)
        event("completed", winner=winner, joint_score=best[winner][1]["joint_score"],
              seconds=report["seconds_before_final_serialization"], maxrss_kib=report["maxrss_kib"])
        write_json(OUT/"file-inventory.json", {str(p.relative_to(OUT)): p.stat().st_size
                                              for p in sorted(OUT.rglob("*")) if p.is_file()})
    except Exception as exc:
        event("failed", type=type(exc).__name__, message=str(exc))
        raise
    finally:
        monitor_stop.set()
        monitor.join(timeout=1)
        log.close()


if __name__ == "__main__":
    main()
