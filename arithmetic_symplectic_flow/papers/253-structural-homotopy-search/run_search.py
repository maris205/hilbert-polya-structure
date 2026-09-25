#!/usr/bin/env python3
"""CS03: frozen structural forks; fixed inherited readout; bounded search."""
import csv
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import resource
import sys
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
BASELINE = ROOT / "papers/252-path-energy-readout/evidence/run-1/winner-A.npz"
DEV_REFERENCE = ROOT / "papers/251-constructive-fit-portfolio/evidence/run-1/reference-101-150.json"
S, L, A_END = 300, 3.5, 1.02
BASE_H, BASE_A = .06138739295586476, 1.551941486210356
FORM_IDS = {"Q": "CS03-Q-QUARTIC", "S": "CS03-S-SEXTIC", "J": "CS03-J-PERIODIC-BRIDGE",
            "K": "CS03-K-QUARTIC-KINETIC", "R": "CS03-R-PATH-CURVATURE"}
LAMBDA_BOUNDS = {"Q": (-.04, .15), "S": (0., .06), "J": (0., 1.), "K": (0., .25), "R": (-1., 1.)}
STRUCTURAL_SEEDS = {
    "Q": [-.04, -.01, -.001, -.00001, .00001, .001, .01, .15],
    "S": [.000001, .00001, .0001, .001, .005, .01, .02, .06],
    "J": [.000001, .00001, .0001, .001, .01, .1, .5, 1.],
    "K": [.000001, .00001, .0001, .001, .01, .05, .1, .25],
    "R": [-1., -.25, -.01, -.001, .001, .01, .25, 1.]}


def utc():
    return datetime.now(timezone.utc).isoformat()


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def write_json(p, data):
    with p.open("x", encoding="utf-8") as f:
        json.dump(data, f, indent=2, allow_nan=False)
        f.write("\n")


def write_npz(p, data):
    with p.open("xb") as f:
        np.savez_compressed(f, **data)


def bounds(form):
    lo, hi = LAMBDA_BOUNDS[form]
    return np.array([.045, 1.10, lo]), np.array([.085, 2.10, hi])


def forward(form, theta, target, alpha, helper, n=250):
    h, a_start, lam = map(float, theta)
    q = np.linspace(-L, L, n, endpoint=False)
    p = np.fft.fftfreq(n)*n*np.pi*h/L
    kinetic = .5*p*p
    if form == "K" and lam != 0.:
        kinetic = kinetic + lam*p**4/4.

    def potential(a):
        base = helper.polynomial(q, a)
        if lam == 0.:
            return base
        if form == "Q":
            return base + lam*q**4
        if form == "S":
            return base + lam*q**6/L**2
        if form == "J":
            return (1-lam)*base + lam*helper.periodic(q, a)
        return base

    def apply_kinetic(mat, multiplier):
        return fft.ifft(multiplier[:, None]*fft.fft(mat, axis=0, norm="ortho", workers=1),
                        axis=0, norm="ortho", workers=1)

    f = np.log(np.arange(1, S+1)+10.)**(-2.)
    w = (f-f[-1])/(f[0]-f[-1])
    if form == "R" and lam != 0.:
        w = w + lam*w*(1-w)
    schedule = A_END + (a_start-A_END)*w
    if not (np.all(np.diff(schedule) < 0) and abs(schedule[0]-a_start) < 1e-14
            and abs(schedule[-1]-A_END) < 1e-14):
        raise RuntimeError("Endpoint/monotone schedule check failed")
    u = np.eye(n, dtype=np.complex128)
    drift = np.exp(-1j*kinetic/h)
    for a in schedule:
        u = apply_kinetic(np.exp(-1j*potential(a)/h)[:, None]*u, drift)
    tmat = apply_kinetic(np.eye(n, dtype=np.complex128), kinetic)
    a_ref = A_END + alpha*(a_start-A_END)
    href = tmat + np.diag(potential(a_ref))
    hend = tmat + np.diag(potential(A_END))
    vals, vec = np.linalg.eig(u)
    phase = np.angle(vals)
    ee = np.real(np.sum(np.conj(vec)*(href@vec), axis=0))
    branch = np.round((S*ee+h*phase)/(2*np.pi*h))
    raw = (-h*phase+2*np.pi*h*branch)/S
    order = np.argsort(raw)
    energy = raw[order]-raw[order[0]]
    if len(energy) < 201 or not np.all(np.isfinite(energy)) or energy[1] <= 0:
        raise RuntimeError("Incomplete/nonfinite spectrum or nonpositive first gap")
    scale = float(target[0]/energy[1])
    pred = energy[1:201]*scale
    arrays = {"q": q, "p": p, "kinetic": kinetic, "schedule": schedule, "U": u,
              "H_ref": href, "H_end": hend, "eigenvalues": vals, "eigenvectors": vec,
              "phase": phase, "expectation": ee, "branch": branch, "energy_unshifted": raw,
              "sort_order": order, "energy": energy, "predicted_200": pred, "theta": np.asarray(theta),
              "alpha": np.array(alpha), "a_ref": np.array(a_ref), "scale": np.array(scale), "target_100": target}
    diagnostics = {
        "unitarity_relative_fro": float(np.linalg.norm(u.conj().T@u-np.eye(n))/np.sqrt(n)),
        "eigenpair_relative_fro": float(np.linalg.norm(u@vec-vec*vals)/np.linalg.norm(vec)),
        "eigenvector_norm_max_error": float(np.max(np.abs(np.sum(abs(vec)**2, axis=0)-1))),
        "href_hermitian_relative_fro": float(np.linalg.norm(href-href.conj().T)/np.linalg.norm(href)),
        "schedule_endpoint_max_error": float(max(abs(schedule[0]-a_start), abs(schedule[-1]-A_END)))}
    record = {"form": FORM_IDS[form], "theta": list(map(float, theta)), "alpha_fixed": alpha,
              "a_ref": float(a_ref), "grid_n": n, "dimension": n, "scale": scale,
              "first_gap": float(energy[1]), "metrics": helper.metrics(pred[:100], target), "diagnostics": diagnostics}
    return arrays, record


def main():
    started = time.perf_counter()
    locks = json.loads(LOCK_FILE.read_text())
    for p, want in locks.items():
        if sha(ROOT/p) != want:
            raise RuntimeError(f"Input hash mismatch: {p}")
    if OUT.exists():
        raise RuntimeError("Output exists; refusing overwrite or repeat")
    spec = importlib.util.spec_from_file_location("cs03_locked_helper", HELPER)
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    OUT.mkdir(parents=True)
    (OUT/"evaluations").mkdir()
    log = (OUT/"events.jsonl").open("x", encoding="utf-8")

    def event(name, **fields):
        line = json.dumps({"utc": utc(), "event": name, **fields}, allow_nan=False)
        log.write(line+"\n"); log.flush()
        print(line, flush=True)

    try:
        manifest = {"scope_id": "ASFS-DISCOVERY-20260919-CS03", "started_utc": utc(), "pid": os.getpid(),
                    "inputs": locks, "input_locks_sha256": sha(LOCK_FILE), "script_sha256": sha(Path(__file__)),
                    "python": sys.version, "numpy": np.__version__, "scipy": scipy.__version__,
                    "initial_maxrss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                    "command": "OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 600s python -u papers/253-structural-homotopy-search/run_search.py"}
        write_json(OUT/"manifest.json", manifest)
        event("started", pid=os.getpid())
        with np.load(BASELINE, allow_pickle=False) as z:
            target = z["target_100"].copy()
            old_pred = z["predicted_150"].copy()
            old_energy = z["energy"].copy()
            old_scale = float(z["scale"])
            alpha = float(z["alpha"])
        if len(target) != 100 or not np.all(np.diff(target) > 0) or alpha != .0027300000000000002:
            raise RuntimeError("Frozen target/alpha mismatch")
        cache, best, calls, unique = {}, {}, 0, 0
        shared_arrays = None
        call_rows = []

        def objective(form, x, stage):
            nonlocal calls, unique, shared_arrays
            calls += 1
            low, high = bounds(form)
            theta = low+np.asarray(x, dtype=float)*(high-low)
            # Share only the frozen common default; other points cache by form.
            is_shared_default = np.array_equal(theta, [BASE_H, BASE_A, 0.])
            key = ("shared-default" if is_shared_default else form, *(float(v).hex() for v in theta))
            if key in cache:
                source = cache[key]
                record = dict(source)
                record.update(form=FORM_IDS[form], call=calls, stage=stage, cached=True,
                              source_evaluation_id=source["evaluation_id"])
                arrays = shared_arrays if is_shared_default else None
                if form not in best:
                    if arrays is None:
                        raise RuntimeError("Missing full arrays for first cached member")
                    best[form] = (arrays, record)
                call_rows.append(record)
                event("cached_call", call=calls, form=FORM_IDS[form], stage=stage,
                      source_id=source["evaluation_id"], mape_percent=record["metrics"]["mape_percent"])
                return record["metrics"]["mape_percent"]
            unique += 1
            eval_id = f"{FORM_IDS[form]}-{unique:04d}"
            event("evaluation_start", evaluation_id=eval_id, call=calls, form=FORM_IDS[form], stage=stage,
                  theta=list(map(float, theta)), alpha_fixed=alpha)
            tick = time.perf_counter()
            arrays, record = forward(form, theta, target, alpha, helper)
            record.update(evaluation_id=eval_id, call=calls, stage=stage, cached=False,
                          seconds=time.perf_counter()-tick)
            if unique == 1:
                err = float(np.max(np.abs(arrays["predicted_200"][:100]-old_pred[:100])))
                mdiff = abs(record["metrics"]["mape_percent"]-helper.metrics(old_pred[:100], target)["mape_percent"])
                regression = {"max_prediction_difference": err, "mape_difference_percent_points": mdiff,
                              "tolerance": 1e-6, "passed": bool(err <= 1e-6 and mdiff <= 1e-6)}
                write_json(OUT/"regression-control.json", regression)
                if not regression["passed"]:
                    raise RuntimeError("CS02 baseline regression failed; no retry")
                shared_arrays = arrays
            compact = {k: v for k, v in arrays.items() if k not in ("U", "H_ref", "H_end", "eigenvectors")}
            write_npz(OUT/"evaluations"/(eval_id+".npz"), compact)
            write_json(OUT/"evaluations"/(eval_id+".json"), record)
            cache[key] = record
            call_rows.append(record)
            value = record["metrics"]["mape_percent"]
            if form not in best or value < best[form][1]["metrics"]["mape_percent"]:
                best[form] = (arrays, record)
            event("evaluation_complete", evaluation_id=eval_id, mape_percent=value,
                  best_for_form=best[form][1]["metrics"]["mape_percent"], seconds=record["seconds"])
            return value

        rng = np.random.default_rng(20260920)
        perturbation = rng.uniform(-1, 1, (8, 3))*np.array([1e-5, 1e-5, 1e-4, 1e-4, 1e-3, 1e-3, 1e-2, 1e-2])[:, None]
        seeds = {}
        for form in FORM_IDS:
            low, high = bounds(form)
            default_x = (np.array([BASE_H, BASE_A, 0.])-low)/(high-low)
            seeds[form] = [default_x]
            seeds[form] += [(np.array([BASE_H, BASE_A, lam])-low)/(high-low) for lam in STRUCTURAL_SEEDS[form]]
            seeds[form] += list(np.clip(default_x+perturbation, 0, 1))
        write_json(OUT/"seed-design.json", {"seed": 20260920, "normalized_points":
                   {f: [x.tolist() for x in points] for f, points in seeds.items()},
                   "shared_normalized_perturbation": perturbation.tolist()})
        for i in range(17):
            for form in FORM_IDS:
                objective(form, seeds[form][i], f"seed-{i:02d}")
        optimizers = {}
        for form in FORM_IDS:
            low, high = bounds(form)
            x0 = (np.array(best[form][1]["theta"])-low)/(high-low)
            simplex = np.repeat(x0[None, :], 4, axis=0)
            for j in range(3):
                simplex[j+1, j] += 2e-5 if x0[j] <= 1-2e-5 else -2e-5
            result = minimize(lambda x: objective(form, x, "refine"), x0, method="Nelder-Mead",
                              bounds=[(0., 1.)]*3,
                              options={"maxfev": 40, "initial_simplex": simplex, "xatol": 1e-6,
                                       "fatol": 1e-6, "adaptive": False})
            optimizers[form] = {"success": bool(result.success), "message": str(result.message),
                                "nfev": int(result.nfev), "nit": int(result.nit), "fun": float(result.fun)}
            event("form_training_complete", form=FORM_IDS[form], best=best[form][1], optimizer=optimizers[form])
        winner = min(best, key=lambda f: best[f][1]["metrics"]["mape_percent"])
        frozen = {"scope_id": manifest["scope_id"], "frozen_utc": utc(), "selection": "minimum first-100 training MAPE only",
                  "global_winner": winner, "winners": {f: r for f, (a, r) in best.items()},
                  "alpha_fixed": alpha, "calls": calls, "unique_training_forwards": unique,
                  "optimizers": optimizers, "evaluation_window": "151-200; not yet generated by this run",
                  "development_window": "101-150; previously observed, not used in this run's objective"}
        write_json(OUT/"winners-frozen.json", frozen)
        for form, (arrays, record) in best.items():
            write_npz(OUT/f"winner-{form}.npz", arrays)
        write_json(OUT/"calls.json", call_rows)
        event("training_frozen", global_winner=winner, sha256=sha(OUT/"winners-frozen.json"), calls=calls, unique_forwards=unique)
        event("postfreeze_reference_start", first=151, last=200, no_further_selection=True)
        import mpmath as mp
        mp.mp.dps = 40
        strings = [str(mp.im(mp.zetazero(j))) for j in range(151, 201)]
        future = np.array([float(v) for v in strings])
        write_json(OUT/"reference-151-200.json", {"first": 151, "last": 200, "decimal_precision": 40,
                   "mpmath": mp.__version__, "ordinates": strings,
                   "scope": "not used for this run's selection; historical blind status not claimed"})
        event("development_reference_read", source=str(DEV_REFERENCE.relative_to(ROOT)))
        dev = np.array([float(v) for v in json.loads(DEV_REFERENCE.read_text())["ordinates"]])
        post = {f: {"development_101_150": helper.metrics(a["predicted_200"][100:150], dev),
                    "evaluation_151_200": helper.metrics(a["predicted_200"][150:200], future)}
                for f, (a, r) in best.items()}
        baseline_pred = old_energy[1:201]*old_scale
        baseline = {"training": helper.metrics(baseline_pred[:100], target),
                    "development_101_150": helper.metrics(baseline_pred[100:150], dev),
                    "evaluation_151_200": helper.metrics(baseline_pred[150:200], future)}
        with (OUT/"winner-points.csv").open("x", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["form", "index", "window", "target", "predicted", "residual", "percent_error"])
            truth = np.concatenate([target, dev, future])
            for form, (arrays, record) in best.items():
                for j, (t, pred) in enumerate(zip(truth, arrays["predicted_200"]), 1):
                    window = "train" if j <= 100 else "development" if j <= 150 else "postfreeze-evaluation"
                    writer.writerow([form, j, window, t, pred, pred-t, 100*abs(pred-t)/t])
        event("postfreeze_evaluation_complete", results=post, baseline=baseline)
        resolutions = []
        resolution_forwards = 0
        for n in (260, 280):
            theta = best[winner][1]["theta"]
            if np.array_equal(theta, [BASE_H, BASE_A, 0.]):
                old_path = ROOT/f"papers/252-path-energy-readout/evidence/run-1/resolution-{n}.npz"
                event("resolution_reuse", source=str(old_path.relative_to(ROOT)), grid_n=n)
                with np.load(old_path, allow_pickle=False) as z:
                    arrays = {k: z[k].copy() for k in z.files}
                pred = arrays["energy"][1:201]*float(arrays["scale"])
                arrays["predicted_200"] = pred
                record = {"form": FORM_IDS[winner], "theta": theta, "alpha_fixed": alpha, "grid_n": n,
                          "source": str(old_path.relative_to(ROOT)), "new_forward": False,
                          "metrics": helper.metrics(pred[:100], target), "scale": float(arrays["scale"])}
            else:
                event("resolution_start", form=FORM_IDS[winner], grid_n=n, theta=theta)
                arrays, record = forward(winner, theta, target, alpha, helper, n=n)
                record["new_forward"] = True
                resolution_forwards += 1
            record["development_metrics"] = helper.metrics(arrays["predicted_200"][100:150], dev)
            record["evaluation_metrics"] = helper.metrics(arrays["predicted_200"][150:200], future)
            write_npz(OUT/f"resolution-{n}.npz", arrays)
            resolutions.append(record)
            event("resolution_complete", result=record)
        report = {"scope_id": manifest["scope_id"], "status": "completed", "global_training_winner": winner,
                  "winners": frozen["winners"], "postfreeze": post, "baseline": baseline, "resolutions": resolutions,
                  "calls": calls, "unique_training_forwards": unique, "new_resolution_forwards": resolution_forwards,
                  "optimizers": optimizers, "seconds_before_final_serialization": time.perf_counter()-started,
                  "maxrss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "completed_utc": utc(),
                  "all_inputs_unchanged": all(sha(ROOT/p) == h for p, h in locks.items())}
        write_json(OUT/"result.json", report)
        event("completed", winner=winner, training_mape=best[winner][1]["metrics"]["mape_percent"],
              seconds=report["seconds_before_final_serialization"], maxrss_kib=report["maxrss_kib"])
    except Exception as exc:
        event("failed", type=type(exc).__name__, message=str(exc))
        raise
    finally:
        log.close()


if __name__ == "__main__":
    main()
