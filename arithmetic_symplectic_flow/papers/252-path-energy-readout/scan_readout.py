#!/usr/bin/env python3
"""CS02: saved-state path-energy readout construction; no evolution/eigensolve."""
import csv
from datetime import datetime,timezone
import hashlib
import json
import os
from pathlib import Path
import resource
import sys
import time
import numpy as np

PACKAGE=Path(__file__).resolve().parent
ROOT=PACKAGE.parents[1]
SOURCE_DIR=ROOT/"papers/251-constructive-fit-portfolio/evidence/run-1"
OUT=PACKAGE/"evidence/run-1"
L,S,A_END=3.5,300,1.02

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def write_json(p,data):
    with p.open("x",encoding="utf-8") as f:
        json.dump(data,f,indent=2,allow_nan=False);f.write("\n")

def write_npz(p,data):
    with p.open("xb") as f:
        np.savez_compressed(f,**data)

def utc():
    return datetime.now(timezone.utc).isoformat()

def metrics(pred,target):
    delta=pred-target
    rel=np.abs(delta)/target
    return {"count":len(target),"mape_percent":float(np.mean(rel)*100),"mse":float(np.mean(delta**2)),
            "max_absolute_error":float(np.max(np.abs(delta))),"max_percent_error":float(np.max(rel)*100),
            "mean_absolute_spacing_error_in_target_gaps":float(np.mean(np.abs(np.diff(pred)-np.diff(target))/np.diff(target)))}

def derivative(form,q):
    if form in "ABD":
        return q**3/3
    r=L/np.pi
    q3=2*r**3*np.sin(q/r)*(1-np.cos(q/r))
    if form=="C":
        return q3/3
    return ((q3[:,None]+np.sqrt(2)*q3[None,:])/3).reshape(-1)

def load_source(p):
    with np.load(p,allow_pickle=False) as z:
        return {k:z[k].copy() for k in z.files}

def readout(source,gradient,alpha):
    h,a_start,beta=source["theta"]
    slope=(a_start-A_END)*gradient
    ee=source["expectation"]+alpha*slope
    phase=source["phase"]
    branch=np.round((S*ee+h*phase)/(2*np.pi*h))
    raw=(-h*phase+2*np.pi*h*branch)/S
    order=np.argsort(raw)
    energy=raw[order]-raw[order[0]]
    if len(energy)<151 or not np.all(np.isfinite(energy)) or energy[1]<=0:
        raise RuntimeError("Invalid readout; no shortening or retry")
    scale=float(source["target_100"][0]/energy[1])
    predicted=scale*energy[1:151]
    return {"ee_ref":ee,"branch":branch,"energy_unshifted":raw,"order":order,
            "energy":energy,"scale":np.array(scale),"predicted_150":predicted},metrics(predicted[:100],source["target_100"])

def main():
    started=time.perf_counter()
    lock_file=PACKAGE/"input-locks.json"
    locks=json.loads(lock_file.read_text())
    for rel,h in locks.items():
        if sha(ROOT/rel)!=h:
            raise RuntimeError(f"Input lock mismatch {rel}")
    if OUT.exists():
        raise RuntimeError("Output exists; refusing overwrite/repeat")
    OUT.mkdir(parents=True)
    log=(OUT/"events.jsonl").open("x",encoding="utf-8")

    def event(name,**kw):
        line=json.dumps({"utc":utc(),"event":name,**kw},allow_nan=False)
        print(line,flush=True);log.write(line+"\n");log.flush()

    try:
        manifest={"scope_id":"ASFS-DISCOVERY-20260919-CS02","started_utc":utc(),"pid":os.getpid(),
                  "script_sha256":sha(Path(__file__)),"input_locks_sha256":sha(lock_file),"inputs":locks,
                  "python":sys.version,"numpy":np.__version__,"initial_maxrss_kib":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                  "command":"OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 120s python -u papers/252-path-energy-readout/scan_readout.py"}
        write_json(OUT/"manifest.json",manifest)
        event("started",pid=os.getpid())
        origins=json.loads((SOURCE_DIR/"winners-frozen.json").read_text())
        all_best={};controls={};capsules={};sources={};total_calls=0;total_unique=0
        with (OUT/"search.csv").open("x",newline="",encoding="utf-8") as f:
            w=csv.writer(f)
            w.writerow(["form","call","stage","alpha","eligible_for_selection","cached","mape_percent","mse","max_percent_error","scale","first_gap"])
            for form in "ABCDE":
                source=load_source(SOURCE_DIR/f"winner-{form}.npz")
                sources[form]=source
                x=derivative(form,source["q"])
                gradient=np.real(np.sum(np.conj(source["eigenvectors"])*(x[:,None]*source["eigenvectors"]),axis=0))
                cache={};best=None;calls=0;unique=0

                def evaluate(alpha,stage,eligible=True):
                    nonlocal calls,unique,best
                    calls+=1
                    alpha=float(alpha)
                    key=alpha.hex()
                    cached=key in cache
                    if cached:
                        arrays,stat=cache[key]
                    else:
                        arrays,stat=readout(source,gradient,alpha)
                        cache[key]=(arrays,stat);unique+=1
                    w.writerow([form,calls,stage,alpha,eligible,cached,stat["mape_percent"],stat["mse"],stat["max_percent_error"],float(arrays["scale"]),float(arrays["energy"][1])])
                    if eligible and (best is None or (stat["mape_percent"],alpha)<(best[2]["mape_percent"],best[0])):
                        best=(alpha,arrays,stat)
                    return stat["mape_percent"]

                event("form_start",form=form,source_evaluation_id=origins["winners"][form]["evaluation_id"],theta=source["theta"].tolist())
                a0,m0=readout(source,gradient,0.)
                diff=float(np.max(abs(a0["predicted_150"]-source["predicted_150"])))
                if diff>1e-10:
                    raise RuntimeError(f"alpha0 reproduction mismatch {form}: {diff}")
                coarse=np.linspace(0,1,1001)
                scores=[evaluate(a,"coarse") for a in coarse]
                centres=sorted(range(1001),key=lambda i:(scores[i],float(coarse[i])))[:5]
                for centre in centres:
                    left,right=max(0.,coarse[centre]-.001),min(1.,coarse[centre]+.001)
                    for a in np.linspace(left,right,201):
                        evaluate(a,f"refine-{centre}")
                mean_alpha=float((np.mean(source["schedule"])-A_END)/(source["theta"][1]-A_END))
                evaluate(mean_alpha,"diagnostic-time-mean",eligible=False)
                mean_arrays,mean_stat=cache[mean_alpha.hex()]
                controls[form]={"alpha0_prediction_max_difference":diff,"endpoint":m0,
                                "time_mean_alpha":mean_alpha,"time_mean_metrics":mean_stat,
                                "startpoint_metrics":cache[float(1.).hex()][1]}
                alpha,arrays,stat=best
                href=source["H_base"]+np.diag(alpha*(source["theta"][1]-A_END)*x)
                full={**arrays,"H_ref":href,"derivative_diagonal":x,"derivative_expectation":gradient,
                      "alpha":np.array(alpha),"theta":source["theta"],"target_100":source["target_100"]}
                write_npz(OUT/f"winner-{form}.npz",full)
                record={"form_id":f"CS02-{form}-PATH-ENERGY","source_form_id":origins["winners"][form]["form"],
                        "source_evaluation_id":origins["winners"][form]["evaluation_id"],"theta":source["theta"].tolist(),
                        "alpha":alpha,"a_ref":float(A_END+alpha*(source["theta"][1]-A_END)),"scale":float(arrays["scale"]),
                        "first_gap":float(arrays["energy"][1]),"metrics":stat,"calls_including_mean_diagnostic":calls,
                        "unique_alphas_including_mean_diagnostic":unique,"refinement_centres":[float(coarse[i]) for i in centres]}
                all_best[form]=record;capsules[form]=arrays;total_calls+=calls;total_unique+=unique
                event("form_complete",result=record)
                f.flush()
        winner=min(all_best,key=lambda f:(all_best[f]["metrics"]["mape_percent"],f))
        frozen={"scope_id":manifest["scope_id"],"frozen_utc":utc(),"global_training_winner":winner,
                "winners":all_best,"selection":"training MAPE only; one extra alpha per source form",
                "extrapolation_metrics_not_read_or_computed":True}
        write_json(OUT/"winners-frozen.json",frozen)
        event("training_frozen",winner=winner,sha256=sha(OUT/"winners-frozen.json"))
        # Only now read future values. Earlier input hash checks do not parse them.
        event("extrapolation_reference_read",first=101,last=150)
        reference=json.loads((SOURCE_DIR/"reference-101-150.json").read_text())
        future=np.array([float(s) for s in reference["ordinates"]])
        extrap={f:metrics(a["predicted_150"][100:150],future) for f,a in capsules.items()}
        with (OUT/"winner-points.csv").open("x",newline="",encoding="utf-8") as f:
            w=csv.writer(f);w.writerow(["form","index","window","target","predicted","percent_error"])
            for form,arrays in capsules.items():
                truths=np.concatenate([sources[form]["target_100"],future])
                for j,(truth,pred) in enumerate(zip(truths,arrays["predicted_150"]),1):
                    w.writerow([form,j,"train" if j<=100 else "extrapolation",truth,pred,100*abs(pred-truth)/truth])
        resolutions=[]
        if winner==origins["global_winner"]:
            for p in sorted(SOURCE_DIR.glob("resolution-*.npz")):
                source=load_source(p)
                x=derivative(winner,source["q"])
                gradient=np.real(np.sum(np.conj(source["eigenvectors"])*(x[:,None]*source["eigenvectors"]),axis=0))
                arrays,stat=readout(source,gradient,all_best[winner]["alpha"])
                write_npz(OUT/p.name,arrays)
                resolutions.append({"source":str(p.relative_to(ROOT)),"source_sha256":sha(p),"alpha":all_best[winner]["alpha"],
                                    "metrics":stat,"extrapolation":metrics(arrays["predicted_150"][100:150],future),
                                    "scale":float(arrays["scale"]),"first_gap":float(arrays["energy"][1])})
        report={"scope_id":manifest["scope_id"],"status":"completed","global_training_winner":winner,
                "winners":all_best,"controls":controls,"extrapolation":extrap,"resolutions":resolutions,
                "resolution_status":"REUSED SAME SOURCE FORM" if resolutions else "NOT TESTED; DIFFERENT SOURCE FORM",
                "calls_including_mean_diagnostic":total_calls,"unique_alphas_including_mean_diagnostic":total_unique,
                "seconds_before_serialization":time.perf_counter()-started,"maxrss_kib":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                "completed_utc":utc(),"all_inputs_unchanged":all(sha(ROOT/rel)==h for rel,h in locks.items())}
        write_json(OUT/"result.json",report)
        event("completed",winner=winner,training_mape=all_best[winner]["metrics"]["mape_percent"],seconds=report["seconds_before_serialization"])
    except Exception as exc:
        event("failed",type=type(exc).__name__,message=str(exc));raise
    finally:
        log.close()

if __name__=="__main__":
    main()
