#!/usr/bin/env python3
"""CS01: five frozen constructive families, bounded training then extrapolation."""
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
import scipy
from scipy import fft
from scipy.optimize import minimize

PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[1]
OUT = PACKAGE / "evidence/run-1"
BASELINE = ROOT / "papers/245-dynamic-start-ablation/evidence/run-1/DS02-D/spectrum.npz"
SOURCE = ROOT / "docs/upstream_snapshots/20260918/riemann_henon/9-robustness_sensitivity.py"
LOCKS = {
    PACKAGE / "candidate-card.md": "d69b49f376662451d0166ef95eb476736f2d1681471fe841f9ae3a60c7d9408c",
    PACKAGE / "forms.md": "f5287ae55839d238c6893691f102caae35ed44d293cef9ffb65330f2bff18b93",
    PACKAGE / "execution-card.md": "c3a0bcb09f3329736d1d396e362f3913f995246dd7549a707be7afcb6f9737af",
    BASELINE: "e5817dc78833b35f1f4f4b234c2ed41d6f0b2c213f56bebe128b7f0136ef0833",
    SOURCE: "dd154507ab7138b2377b9dd7b5fc38809a62b4b1e9ecbf7d7c9ba702e6f737cb",
}
FORM_IDS = {"A":"CS01-A-POLY-COOL", "B":"CS01-B-SYMMETRIC-KICK", "C":"CS01-C-PERIODIC-JET", "D":"CS01-D-DIRICHLET", "E":"CS01-E-COUPLED-2DOF"}
LOW = np.array([.045,1.10,1.4])
HIGH = np.array([.085,2.10,3.2])
DEFAULT = np.array([.06138739295586476,1.551941486210356,2.])
S,L,A_END = 300,3.5,1.02

def utc():
    return datetime.now(timezone.utc).isoformat()

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def write_json(p,data):
    with p.open("x",encoding="utf-8") as f:
        json.dump(data,f,indent=2,allow_nan=False)
        f.write("\n")

def write_npz(p,data):
    with p.open("xb") as f:
        np.savez_compressed(f,**data)

def metrics(pred,target):
    delta=pred-target
    rel=np.abs(delta)/target
    return {"count":len(target),"mape_percent":float(np.mean(rel)*100),
            "mse":float(np.mean(delta**2)),"max_absolute_error":float(np.max(np.abs(delta))),
            "max_percent_error":float(np.max(rel)*100),
            "mean_absolute_spacing_error_in_target_gaps":float(np.mean(np.abs(np.diff(pred)-np.diff(target))/np.diff(target)))}

def polynomial(q,a):
    return -q+q*q+(a/3.)*q**3+.05*q**4

def periodic(q,a):
    r=L/np.pi
    x=q/r
    q1=r*np.sin(x)
    q2=2*r*r*(1-np.cos(x))
    q3=2*r**3*np.sin(x)*(1-np.cos(x))
    q4=4*r**4*(1-np.cos(x))**2
    return -q1+q2+(a/3-1/(6*r*r))*q3+(.05+1/(12*r*r))*q4

def forward(form,theta,target,n_override=None):
    h,a_start,beta=map(float,theta)
    n=int(n_override if n_override is not None else (16 if form=="E" else 250))
    dimension=n*n if form=="E" else n
    q=(-L+2*L*np.arange(1,n+1)/(n+1)) if form=="D" else np.linspace(-L,L,n,endpoint=False)
    if form=="D":
        p=np.pi*h*np.arange(1,n+1)/(2*L)
    else:
        p=np.fft.fftfreq(n)*n*np.pi*h/L
    kinetic=.5*p*p
    if form=="E":
        kinetic=(kinetic[:,None]+np.sqrt(2)*kinetic[None,:]).reshape(-1)

    def transform(mat,inverse=False):
        if form=="D":
            return fft.dst(mat,type=1,axis=0,norm="ortho",workers=1)
        if form=="E":
            arr=mat.reshape(n,n,-1)
            fun=fft.ifftn if inverse else fft.fftn
            return fun(arr,axes=(0,1),norm="ortho",workers=1).reshape(dimension,-1)
        fun=fft.ifft if inverse else fft.fft
        return fun(mat,axis=0,norm="ortho",workers=1)

    def apply_kinetic(mat,multiplier):
        return transform(multiplier[:,None]*transform(mat),inverse=True)

    def potential(a):
        if form=="E":
            v=periodic(q,a)
            q1=(L/np.pi)*np.sin(np.pi*q/L)
            return (v[:,None]+np.sqrt(2)*v[None,:]+.1*q1[:,None]*q1[None,:]).reshape(-1)
        return periodic(q,a) if form=="C" else polynomial(q,a)

    f=np.log(np.arange(1,S+1)+10.)**(-beta)
    schedule=A_END+(a_start-A_END)*(f-f[-1])/(f[0]-f[-1])
    u=np.eye(dimension,dtype=np.complex128)
    drift=np.exp(-1j*kinetic/h)
    for a in schedule:
        v=potential(a)
        if form=="B":
            half=np.exp(-.5j*v/h)
            u=half[:,None]*apply_kinetic(half[:,None]*u,drift)
        else:
            u=apply_kinetic(np.exp(-1j*v/h)[:,None]*u,drift)
    hbase=apply_kinetic(np.eye(dimension,dtype=np.complex128),kinetic)+np.diag(potential(A_END))
    lam,vec=np.linalg.eig(u)
    phase=np.angle(lam)
    ee=np.real(np.sum(np.conj(vec)*(hbase@vec),axis=0))
    branch=np.round((S*ee+h*phase)/(2*np.pi*h))
    raw=(-h*phase+2*np.pi*h*branch)/S
    order=np.argsort(raw)
    energy=raw[order]-raw[order[0]]
    if len(energy)<151 or not np.all(np.isfinite(energy)) or energy[1]<=0:
        raise RuntimeError("Nonfinite/incomplete spectrum or zero first gap; no retry")
    scale=float(target[0]/energy[1])
    pred=energy[1:151]*scale
    stat=metrics(pred[:100],target)
    arrays={"q":q,"p":p,"kinetic":kinetic,"schedule":schedule,"U":u,"H_base":hbase,
            "eigenvalues":lam,"eigenvectors":vec,"phase":phase,"expectation":ee,"branch":branch,
            "energy_unshifted":raw,"sort_order":order,"energy":energy,"predicted_150":pred,
            "theta":np.asarray(theta),"scale":np.array(scale),"target_100":target}
    diagnostics={"unitarity_relative_fro":float(np.linalg.norm(u.conj().T@u-np.eye(dimension))/np.sqrt(dimension)),
                 "eigenpair_relative_fro":float(np.linalg.norm(u@vec-vec*lam)/np.linalg.norm(vec)),
                 "eigenvector_norm_max_error":float(np.max(np.abs(np.sum(abs(vec)**2,axis=0)-1))),
                 "hbase_hermitian_relative_fro":float(np.linalg.norm(hbase-hbase.conj().T)/np.linalg.norm(hbase))}
    return arrays,{"form":FORM_IDS[form],"theta":list(map(float,theta)),"grid_n":n,
                   "dimension":dimension,"scale":scale,"first_gap":float(energy[1]),
                   "metrics":stat,"diagnostics":diagnostics}

def main():
    started=time.perf_counter()
    for p,h in LOCKS.items():
        if sha(p)!=h:
            raise RuntimeError(f"Input lock mismatch: {p}")
    if OUT.exists():
        raise RuntimeError("Existing output; refusing overwrite/repeat")
    OUT.mkdir(parents=True)
    (OUT/"evaluations").mkdir()
    log=(OUT/"events.jsonl").open("x",encoding="utf-8")

    def event(name,**fields):
        record={"utc":utc(),"event":name,**fields}
        line=json.dumps(record,allow_nan=False)
        log.write(line+"\n");log.flush()
        print(line,flush=True)

    try:
        manifest={"scope_id":"ASFS-DISCOVERY-20260919-CS01","started_utc":utc(),"pid":os.getpid(),
                  "inputs":{str(p.relative_to(ROOT)):h for p,h in LOCKS.items()},
                  "script_sha256":sha(Path(__file__)),"python":sys.version,"numpy":np.__version__,
                  "scipy":scipy.__version__,"initial_maxrss_kib":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                  "command":"OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 600s python -u papers/251-constructive-fit-portfolio/run_search.py"}
        write_json(OUT/"manifest.json",manifest)
        event("started",pid=os.getpid())
        with np.load(BASELINE,allow_pickle=False) as z:
            target=z["target"].copy(); old_pred=z["pred"].copy();old_energy=z["E"].copy()
        if not np.all(np.diff(target)>0) or len(target)!=100:
            raise RuntimeError("Invalid locked training target")
        # Technical transform identity check, not a model fit.
        probe=np.array([[1+2j,3-1j],[-2+.5j,4+7j],[.1-1j,2.]])
        if not np.allclose(fft.dst(fft.dst(probe,type=1,axis=0,norm="ortho"),type=1,axis=0,norm="ortho"),probe,atol=1e-12):
            raise RuntimeError("Complex orthogonal DST-I preflight failed")
        cache={};best={};all_records=[];calls=0;unique=0

        def objective(form,x,stage):
            nonlocal calls,unique
            calls+=1
            theta=LOW+np.asarray(x,dtype=float)*(HIGH-LOW)
            key=(form,*(float(v).hex() for v in theta))
            if key in cache:
                record=cache[key]
                event("cached_call",call=calls,stage=stage,source_id=record["evaluation_id"],form=FORM_IDS[form])
                return record["metrics"]["mape_percent"]
            unique+=1
            eval_id=f"{FORM_IDS[form]}-{unique:04d}"
            event("evaluation_start",call=calls,evaluation_id=eval_id,stage=stage,form=FORM_IDS[form],theta=list(map(float,theta)))
            tick=time.perf_counter()
            arrays,record=forward(form,theta,target)
            record.update(evaluation_id=eval_id,call=calls,stage=stage,seconds=time.perf_counter()-tick)
            if unique==1:
                err=float(np.max(np.abs(arrays["predicted_150"][:100]-old_pred)))
                mdiff=abs(record["metrics"]["mape_percent"]-float(np.mean(np.abs((old_pred-target)/target))*100))
                check={"max_prediction_difference":err,"mape_difference_percent_points":mdiff,
                       "tolerance":1e-6,"passed":bool(err<=1e-6 and mdiff<=1e-6)}
                write_json(OUT/"regression-control.json",check)
                if not check["passed"]:
                    raise RuntimeError("A-default regression mismatch; search stopped before other forms")
            compact={k:v for k,v in arrays.items() if k not in ("U","H_base","eigenvectors")}
            write_npz(OUT/"evaluations"/(eval_id+".npz"),compact)
            write_json(OUT/"evaluations"/(eval_id+".json"),record)
            cache[key]=record;all_records.append(record)
            value=record["metrics"]["mape_percent"]
            if form not in best or value<best[form][1]["metrics"]["mape_percent"]:
                best[form]=(arrays,record)
            event("evaluation_complete",evaluation_id=eval_id,stage=stage,mape_percent=value,best_for_form=best[form][1]["metrics"]["mape_percent"],seconds=record["seconds"])
            return value

        default_x=(DEFAULT-LOW)/(HIGH-LOW)
        rng=np.random.default_rng(20260919)
        seeds=[default_x,(np.array([DEFAULT[0],DEFAULT[1],1.8])-LOW)/(HIGH-LOW),
               (np.array([DEFAULT[0],DEFAULT[1],2.2])-LOW)/(HIGH-LOW)]
        seeds.extend(rng.uniform(0,1,(7,3)))
        seeds.extend(np.clip(default_x+rng.uniform(-.003,.003,(8,3)),0,1))
        write_json(OUT/"seed-design.json",{"normalized_points":[list(map(float,x)) for x in seeds],"seed":20260919,"shared_across_forms":True})
        # Round-robin breadth-first ordering, starting with the regression anchor.
        for i,x in enumerate(seeds):
            for form in FORM_IDS:
                objective(form,x,f"seed-{i:02d}")
        optimizer_records={}
        for form in FORM_IDS:
            x0=(np.array(best[form][1]["theta"])-LOW)/(HIGH-LOW)
            simplex=np.repeat(x0[None,:],4,axis=0)
            for j in range(3):
                simplex[j+1,j]+= .002 if x0[j]<=.998 else -.002
            result=minimize(lambda x:objective(form,x,"refine"),x0,method="Nelder-Mead",bounds=[(0.,1.)]*3,
                            options={"maxfev":40,"initial_simplex":simplex,"xatol":1e-6,"fatol":1e-6,"adaptive":False})
            optimizer_records[form]={"success":bool(result.success),"message":str(result.message),"nfev":int(result.nfev),"nit":int(result.nit),"fun":float(result.fun)}
            event("form_training_complete",form=FORM_IDS[form],best=best[form][1],optimizer=optimizer_records[form])
        winner=min(best,key=lambda f:best[f][1]["metrics"]["mape_percent"])
        frozen={"scope_id":manifest["scope_id"],"frozen_utc":utc(),"selection":"minimum training MAPE only",
                "global_winner":winner,"winners":{f:r for f,(a,r) in best.items()},"calls":calls,"unique_evaluations":unique,
                "optimizer_records":optimizer_records,"future_reference_window":"101-150; not yet computed by this run"}
        write_json(OUT/"winners-frozen.json",frozen)
        for form,(arrays,record) in best.items():
            write_npz(OUT/("winner-"+form+".npz"),arrays)
        event("training_frozen",global_winner=winner,sha256=sha(OUT/"winners-frozen.json"),unique_evaluations=unique,calls=calls)

        event("extrapolation_reference_start",first=101,last=150,no_further_training=True)
        import mpmath as mp
        mp.mp.dps=40
        strings=[str(mp.im(mp.zetazero(j))) for j in range(101,151)]
        future=np.array([float(s) for s in strings])
        write_json(OUT/"reference-101-150.json",{"first":101,"last":150,"decimal_precision":40,"mpmath":mp.__version__,"ordinates":strings,
                                                    "scope":"not used by this run before frozen selection; not historically blind"})
        future_results={form:metrics(arrays["predicted_150"][100:150],future) for form,(arrays,record) in best.items()}
        old_future=old_energy[101:151]*(target[0]/old_energy[1])
        future_results["historical_N250_baseline"]=metrics(old_future,future)
        with (OUT/"winner-points.csv").open("x",newline="",encoding="utf-8") as f:
            w=csv.writer(f);w.writerow(["form","index","window","target","predicted","residual","percent_error"])
            for form,(arrays,record) in best.items():
                truths=np.concatenate([target,future])
                for j,(truth,pred) in enumerate(zip(truths,arrays["predicted_150"]),1):
                    w.writerow([form,j,"train" if j<=100 else "extrapolation",truth,pred,pred-truth,100*abs(pred-truth)/truth])
        event("extrapolation_complete",results=future_results)
        resolutions=[]
        for n in ((17,18) if winner=="E" else (260,280)):
            theta=best[winner][1]["theta"]
            event("resolution_start",form=FORM_IDS[winner],grid_n=n,theta=theta)
            arrays,record=forward(winner,theta,target,n_override=n)
            record["extrapolation_metrics"]=metrics(arrays["predicted_150"][100:150],future)
            write_npz(OUT/f"resolution-{n}.npz",arrays)
            resolutions.append(record)
            event("resolution_complete",result=record)
        report={"scope_id":manifest["scope_id"],"status":"completed","global_training_winner":winner,
                "winners":frozen["winners"],"extrapolation":future_results,"resolutions":resolutions,
                "calls":calls,"unique_training_evaluations":unique,"full_resolution_evaluations":2,
                "seconds_before_final_serialization":time.perf_counter()-started,
                "maxrss_kib":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,"completed_utc":utc(),
                "all_inputs_unchanged":all(sha(p)==h for p,h in LOCKS.items())}
        write_json(OUT/"result.json",report)
        event("completed",winner=winner,training_mape=best[winner][1]["metrics"]["mape_percent"],seconds=report["seconds_before_final_serialization"],maxrss_kib=report["maxrss_kib"])
    except Exception as exc:
        event("failed",type=type(exc).__name__,message=str(exc))
        raise
    finally:
        log.close()

if __name__=="__main__":
    main()
