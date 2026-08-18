#!/usr/bin/env python3
"""Independent exact checker for the HCS-C61 resolver component.

This program shares no Python module with the producer.  It reloads immutable
P60 Git objects and frozen C61 target inputs, independently reconstructs the
finite groups, product-form carriers, Fourier carriers, arithmetic tables and
both retained local branches, then rejects any evidence byte outside the
strict schema.  It also runs parser, path/TOCTOU and semantic mutation suites.

Lifecycle: resolver component only / PAPER_PENDING / NOT_RELEASED.
"""

from __future__ import annotations

import argparse
from collections import Counter, deque
import copy
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys
from typing import Any, Callable, Iterable, Sequence

sys.dont_write_bytecode = True

PRIME=692717
NLETTERS=27
E=tuple(range(NLETTERS))
P60="fe1217810b72840619efdf40a2af31b8b80d96f6"
P60_PARENT="f3b3726c40519cdd8ac7832f9f22df16d451b890"
P60_TREE="22b67a5ad27cc0e447bd63ecd2d9ac13ad2a595a"
PROJECT_BASENAME="henon_mu3_yukawa_tensor_fourier_descent"
EVIDENCE_BASENAME="c61_resolvent_evidence.json"
STAGE_PATTERN=re.compile(r"^\.c61-stage-[A-Za-z0-9]{8}$")
C60_BASE=Path("henon_dynamics/henon_mu3_yukawa_biquadratic_envelope")
C59_EVIDENCE=Path("henon_dynamics/henon_mu3_yukawa_gassmann_twins/results/c59_resolvent_evidence.json")
C59_SHA="667e0eeb04e5724b620bf513f9556a321dfd39f9215396ed1840ca83879ec6a6"
ARRAYS_SHA="0fc281590b635eed046cc4a8d38036895e2b1bc56284a0948b1576303de1c2f5"
LAMBDA_SHA="fae69eb91d414d8241bbbee51f4a3fcc91c4f8691090adc5cbb575079d2ea1f5"
C60_PAYLOAD="dca8dbbf269735e78b0435799b0d9c8c9ffad8bdd0470b9262ef64005ff0dead"

C60_INPUTS={
 "certificate":(C60_BASE/"results/c60_certificate.json","d325de1bb0388ccc0c2e81d41fbc6c8fffd692ff777f23647d9e88367d6c2518"),
 "group_evidence":(C60_BASE/"results/c60_group_evidence.json","dcdb9a8be954d4ea5376220d55fcbae9bbb08eb49d03d98d57d790c319ad5fb2"),
 "resolvent_evidence":(C60_BASE/"results/c60_resolvent_evidence.json","f115125725c9160ee3d02f1996147098c234226bdc81eaa670460802a8d827da"),
 "group_module":(C60_BASE/"code/c60_group.py","fd3e75913db3cf5d71f7fd95a3e260edae19bc53a748767f28773d008121536b"),
 "schema":(C60_BASE/"results/c60_schema.json","c7ddb4ff8fa890f9f801d615158c9038299487affa3808f25fe5d73c987791a5"),
 "check_report":(C60_BASE/"results/c60_check_report.json","25bc9c1c656da742359814054b66c05e18a304ca85741776c055152a30a98e44"),
 "scoped_manifest":(C60_BASE/"results/scoped_hash_manifest.json","f8d44a1929b6f873d4f1b4e7317222c0f06e927ba1977f00f493b8fb004cfec7"),
 "full_manifest":(C60_BASE/"FULL_PROJECT_HASHES.sha256","37c1f227aee6c0bfff233ffc1a7f1f8d2a8a27657faad353af711f2e503ed0a4"),
 "route":(C60_BASE/"route_a_evaluation.yaml","8ff624d1fa3d598c4f6aeddea8a9274619f2f21b468054281dda4169480c5872"),
 "route_archive":(C60_BASE/"evaluations/route_a/HCS-C60/20260817T000000Z.yaml","8ff624d1fa3d598c4f6aeddea8a9274619f2f21b468054281dda4169480c5872"),
}
RELEASED_BATCH_SHA="d1a9ebd06f125b1b4236f974e9e4b179f0cf2a57584f1ba180debf3591f2e3f5"
GUARD_REL=Path("henon_dynamics/codex_prompt.md")
GUARD_SHA="24c0978ea1f0d29c06e1eeee33405a416fad626b2dbfb48f30bc103a1503aead"

FORMAL_NAMES=["DERIVATION.md","EXPERIMENT_PLAN.md","EXPERIMENT_TRACKER.md","IMPLEMENTATION_CHECKLIST.md","INTEGRITY_REPORT.md","METHODOLOGY_BLUEPRINT.md","NARRATIVE_REPORT.md","PAPER_PLAN.md","PROOF_PACKAGE.md","README.md","RESEARCH_QUESTION.md","SOURCE_AUDIT.md","THEOREM_PACKAGE.md"]
FORMAL13="c5fc87d395e1e76d602d58bcbdba448e333a987c22d265aae80e1f4107a3dc28"
FORMAL_ROUTE="c773812c949bc4197b4ad5e9e2076ddd5a5d4594d5fb8884ba7109812c3fb40b"
FORMAL_BATCH="13a626b4f43cf560bf194268d503e41ba1bbded16ad59e305c24b9045ee1d814"
FORMAL15="61984f2a06fcd8f57c50ec28e1a557107e551fa0e2b82edc936321507ead37b5"

TOP={"schema_id","schema_sha256","authority","conventions","GAF0_released_authority_rebind","GAF1_fourier_carrier_dag","GAF2_orbit_span_and_nonnormality","GAF3_stabilizers_and_noncollision","GAF4_mixed_type3_exact_bridge","GAF5_fixed_field_diamond","GAF6_global_arithmetic","GAF7_both_local_branches_and_ideal_laws","independence_contract","scope_nonclaims","status","payload_sha256"}
STABLE_SHA={
 "conventions":"73140caa6b132212e8d35b365e9193a637c0d4a473e1a8e613d7a7246195453c",
 "GAF0_released_authority_rebind":"720a56139702a3bf2539f2817eb9076ca66973ef87e50d8efe3870712481b0da",
 "GAF1_fourier_carrier_dag":"b1393c3037f5fe55d12480fa0b4b8f8fdd55a5de6553e2fc37e3c034d7f68724",
 "GAF2_orbit_span_and_nonnormality":"3bb46af87dda77701b917681309bbc4d4969912969cba83a9368ab32e3ee65ea",
 "GAF3_stabilizers_and_noncollision":"81ee15af90e89ad3b0d2f7fe599bad85591846a7b235a76d4ffac21e8c828ad4",
 "GAF4_mixed_type3_exact_bridge":"6aa26ab605acdb14f2432e856ce59cbfdcdf75a33039efc9b25649f84c4b6b72",
 "GAF5_fixed_field_diamond":"3251da9681e27131fd47f67e6748c2586bef07e3281a296b2edf52e4a7d0dc25",
 "GAF6_global_arithmetic":"1da67a1e3f1c3fb605537afa1a5dee20a067148edf4bfb0d238c82686f6dd538",
 "GAF7_both_local_branches_and_ideal_laws":"7b9eba8a1d34e24a4610c2dff0b27727c63411dd7fa8c8b24b8bcf7bd5439b6e",
 "scope_nonclaims":"1ee379636f87fe23656ff5159cf92b9ea4dbd6f74e273d9acb79d786e0b6c18f",
 "status":"e0f16886db12e08477921bef5966df1ec067353ff25c4352937a14fa0d8be704",
}

S_GEN_1=[
 [1,2,3,5,4,6,7,8,10,9,11,12,14,13,15,17,16,18,19,21,20,22,23,24,26,25,27],
 [1,2,3,20,21,19,24,23,10,9,11,22,14,13,15,17,16,18,6,4,5,12,8,7,26,25,27],
 [1,2,6,4,5,3,7,11,9,10,8,15,13,14,12,20,21,18,19,16,17,22,23,27,25,26,24],
 [1,18,12,4,5,15,7,11,26,25,8,3,13,14,6,20,21,2,22,16,17,19,23,27,10,9,24],
 [2,1,3,4,5,6,7,12,13,14,15,8,9,10,11,16,17,18,19,20,21,23,22,24,25,26,27],
 [3,6,4,1,2,5,18,16,8,12,17,20,11,15,21,9,13,19,7,10,14,24,27,25,22,23,26],
]
T_GEN_1=[S_GEN_1[0],S_GEN_1[1],S_GEN_1[2],[1,13,5,3,15,20,11,24,26,9,7,21,18,2,4,22,19,14,16,12,6,17,27,8,10,25,23],S_GEN_1[4],S_GEN_1[5]]
LOCAL_GEN_1={
 "I5":[[16,23,27,8,26,9,7,11,24,10,25,5,13,6,12,20,2,18,19,22,17,1,21,14,4,15,3],[16,2,23,8,18,17,25,4,21,10,11,12,22,27,26,1,6,5,19,20,9,13,3,24,7,15,14]],
 "P5":[[10,7,3,14,4,6,1,12,5,13,15,17,2,19,21,8,27,25,9,11,24,23,26,20,22,18,16]],
 "C3":[[23,25,18,22,17,21,1,14,4,15,12,19,2,20,16,10,24,27,11,8,26,9,7,5,13,6,3]],
 "C2":[[1,2,3,6,5,4,7,8,11,10,9,12,15,14,13,18,17,16,21,20,19,22,23,24,27,26,25]],
 "Cinf":[[6,13,16,12,5,1,18,15,20,22,26,4,2,17,8,3,14,7,19,9,27,10,24,23,25,11,21]],
}
TYPE_BY_SEED={148:1,24:2,178:2,149:3,2:4,3:4,12:5,169:5,0:6,1:6,7:7,4:8}
REP_SEED={1:148,2:24,3:149,4:2,5:12,6:0,7:7,8:4}
CONJ_ORBIT={1:1,2:3,3:3,4:9,5:9,6:27,7:27,8:81}
FOURIER_LOCK={
 "Trace":(2,243,[[2,54],[4,189]],"a7398d36cea0c83ace64466a579e21666731d1e3c8e8641df4ce036c79de2bd7",581739),
 "rplus":(2,54,[[-1,27],[1,27]],"2edfe1e8f952faf2ddbfae3af135da4509f3f40e4175e188e240a5f09b785a96",643771),
 "r3":(2,162,[[-1,81],[1,81]],"b9c21c9fc7060d4e52630a75d6ec0c10305ac33946f78c2c93e33fad68df8c7e",119649),
 "r0":(4,7560,[[-3,54],[-2,324],[-1,3402],[1,3402],[2,324],[3,54]],"a26813d1b2874ee700ececba786af55391dacc2a30a0d4da0390ecb871f63382",582281),
 "delta_plus":(4,1458,[[-2,729],[1,54],[2,648],[4,27]],"1b5927b4d213dfd5af490067a9a551ae0942791a5221e2fb2f9f826440b040c3",None),
 "delta3":(4,10125,[[-4,729],[-2,4131],[1,162],[2,4698],[4,405]],"5f8baf7254f5c27478afce45b5667c62d13a35b205739bbf20ebd36651a144e7",None),
}
ORBIT_LOCK={
 "rplus":(80,"ce3e5dc81b4b902eaaa4cc0edf34daaccea64c94262774bf9c4f5561f80ede31","37042b8b829035a921be14a4360c11073450b025fe3d2af451b412192f84aff4"),
 "delta_plus":(40,"eb3a6df8d4b172f906c8bb968501bd0dad5989b02c160efba75a7739d3791e13","a70e4e7fdad54cd3f5c68f10ee382baa6237b64847e8889129d7d69ee30ff878"),
 "r3":(320,"9eb456211f8841c7968d83140cad9f5103f6ffadabf979184df4bc69c400b725","5e37b4d0f662281feaa5616768b3173d62078a05f69c81b95f29d94415434ec9"),
 "delta3":(160,"d8f1099368ad68c9f3961d2d21f70bd553b5fab9058ce25936a2856c408f77c2","bd98f2356fcc0476dbd44c253343e2851de5121d77f8c852d30017307c24489c"),
 "r0":(320,"6eec729eeb002432f0a36866e041ebeb3cddf9e1a2eb9226922975bb13bacba5","9f7f845af3b92151c004d894bb150ed9db51ac7281ea9f4af32ab8f31ed25118"),
 "delta0":(160,"0fe6b00526627175b2d83621c85da1c4c1c01eb12cf3ddee7b106f4154a02e22","5c7b8802fa76fa3c67d22616369a56d526541ce0d1476f299dd40e00b0321004"),
}
GLOBAL_LOCK={
 "E1":(640,[0,320],1,[1264,992,384,320],[32,0,0,0]),"E2":(960,[16,472],1,[1944,1488,624,480],[312,0,192,0]),
 "E3":(1920,[0,960],1,[3808,2976,1152,960],[208,48,0,240]),"E4":(2880,[16,1432],1,[5872,4464,1872,1440],[5872,4464,1872,1440]),
 "E5":(2880,[48,1416],1,[5856,4464,1872,1440],[5856,4464,1872,1440]),"E6":(8640,[48,4296],1,[17640,13392,5616,4320],[17640,13392,5616,4320]),
 "E7":(17280,[0,8640],1,[35504,26784,11520,8640],[35504,26784,11520,8640]),"E8":(51840,[0,25920],1,[106560,80352,34560,25920],[106560,80352,34560,25920]),
 "C1":(160,[16,72],1,[308,248,96,80],None),"C2":(40,[8,16],1,[68,62,18,20],None),"C3":(40,[6,17],-1,[75,61,24,15],None),"C4":(1,[1,0],1,[0,0,0,0],None),"B80":(80,[4,38],1,[154,122,48,30],None),
}

class Reject(RuntimeError):
    pass

def canon(x:Any)->bytes:
    return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode("ascii")

def H(x:Any)->str:
    return hashlib.sha256(canon(x)).hexdigest()

def raw_sha(raw:bytes)->str:
    return hashlib.sha256(raw).hexdigest()

def load_strict(raw:bytes)->Any:
    def pairs(rows:list[tuple[str,Any]])->dict[str,Any]:
        out={}
        for k,v in rows:
            if type(k) is not str or k in out:
                raise Reject("duplicate/non-string JSON key")
            out[k]=v
        return out
    try:
        return json.loads(raw.decode("utf-8"),object_pairs_hook=pairs,
            parse_float=lambda x:(_ for _ in ()).throw(Reject("float forbidden")),
            parse_constant=lambda x:(_ for _ in ()).throw(Reject("constant forbidden")))
    except (UnicodeDecodeError,json.JSONDecodeError) as exc:
        raise Reject("invalid strict JSON") from exc

def read_guarded(path:Path,limit:int=30_000_000,hook:Callable[[],None]|None=None)->tuple[bytes,dict[str,Any]]:
    path=path.absolute(); before=os.lstat(path)
    if not stat.S_ISREG(before.st_mode) or before.st_nlink!=1 or before.st_size>limit:
        raise Reject("unsafe/nonregular/oversized input")
    if hook is not None: hook()
    fd=os.open(path,os.O_RDONLY|getattr(os,"O_NOFOLLOW",0))
    try:
        first=os.fstat(fd); chunks=[]
        while True:
            part=os.read(fd,1<<20)
            if not part: break
            chunks.append(part)
        last=os.fstat(fd)
    finally: os.close(fd)
    after=os.lstat(path)
    snap=lambda s:(s.st_dev,s.st_ino,s.st_size,s.st_mtime_ns,s.st_ctime_ns,s.st_mode,s.st_nlink)
    if not (snap(before)==snap(first)==snap(last)==snap(after)):
        raise Reject("TOCTOU drift")
    raw=b"".join(chunks)
    return raw,{"sha256":raw_sha(raw),"size_bytes":len(raw),"lines":len(raw.splitlines()),
        "filesystem_identity":{"dev":after.st_dev,"ino":after.st_ino,"mode":after.st_mode,
        "mtime_ns":after.st_mtime_ns,"ctime_ns":after.st_ctime_ns,"nlink":after.st_nlink}}

def canonical_layout()->tuple[Path,Path,Path]:
    invoked=Path(__file__).absolute();source=invoked.resolve(strict=True);project=source.parent.parent;repo=project.parent.parent
    if source.name!="c61_checker_resolvent.py" or source.parent.name!="code" or project.name!=PROJECT_BASENAME or project.parent.name!="henon_dynamics":raise Reject("checker not at canonical installed basename")
    sinfo=os.lstat(source)
    if invoked!=source or project.resolve(strict=True)!=project or repo.resolve(strict=True)!=repo or not stat.S_ISDIR(os.lstat(repo).st_mode) or not stat.S_ISREG(sinfo.st_mode) or sinfo.st_nlink!=1:raise Reject("cannot derive real canonical repository/project/source")
    return repo,project,source

def directory_snapshot(path:Path)->tuple[int,int,int,int]:
    s=os.lstat(path)
    if not stat.S_ISDIR(s.st_mode) or stat.S_ISLNK(s.st_mode) or path.resolve(strict=True)!=path:raise Reject("stage/results is not one real directory")
    return (s.st_dev,s.st_ino,s.st_mode,s.st_mtime_ns)

def staged_evidence_path(value:str,must_exist:bool|None)->tuple[Path,Path,tuple[int,int,int,int]]:
    _repo,project,_source=canonical_layout();results=project/"results";directory_snapshot(results)
    path=Path(value).absolute();stage=path.parent
    if path.name!=EVIDENCE_BASENAME or STAGE_PATTERN.fullmatch(stage.name) is None or stage.parent!=results:raise Reject("noncanonical C61 evidence path")
    identity=directory_snapshot(stage)
    if must_exist is True:
        _raw,record=read_guarded(path,25_000_000)
        if stat.S_IMODE(record["filesystem_identity"]["mode"])!=0o644:raise Reject("existing evidence mode must be 0644")
    elif must_exist is False and os.path.lexists(path):raise Reject("write leaf unexpectedly exists")
    elif must_exist is None and os.path.lexists(path):
        _raw,record=read_guarded(path,25_000_000)
        if stat.S_IMODE(record["filesystem_identity"]["mode"])!=0o644:raise Reject("existing attestation leaf mode must be 0644")
    return path,stage,identity

def runtime_input_snapshot()->dict[str,dict[str,int|str]]:
    repo,project,checker=canonical_layout()
    rels=[Path("henon_dynamics/BATCH_PLAN_C57_C61.md")]
    rels += [Path("henon_dynamics")/PROJECT_BASENAME/name for name in FORMAL_NAMES]
    rels += [Path("henon_dynamics")/PROJECT_BASENAME/"route_a_evaluation.yaml",GUARD_REL]
    paths={rel.as_posix():repo_path(repo,rel) for rel in rels}
    paths["henon_dynamics/"+PROJECT_BASENAME+"/code/c61_resolvent.py"]=checker.with_name("c61_resolvent.py")
    paths["henon_dynamics/"+PROJECT_BASENAME+"/code/c61_checker_resolvent.py"]=checker
    out={}
    for label,path in sorted(paths.items()):
        _raw,record=read_guarded(path,2_000_000)
        out[label]={"sha256":record["sha256"],"size_bytes":record["size_bytes"],**record["filesystem_identity"]}
    out["henon_dynamics/"+PROJECT_BASENAME+"/results"]={
        "sha256":"DIRECTORY_IDENTITY","size_bytes":0,
        **dict(zip(("dev","ino","mode","mtime_ns"),directory_snapshot(project/"results"))),
        "ctime_ns":0,"nlink":0,
    }
    return out

def assert_stage(stage:Path,identity:tuple[int,int,int,int])->None:
    if directory_snapshot(stage)!=identity:raise Reject("C61 stage changed/substituted during checker")

def repo_path(root:Path,rel:Path)->Path:
    if rel.is_absolute() or ".." in rel.parts: raise Reject("unsafe relative path")
    a=root.absolute(); p=(a/rel).absolute()
    if os.path.commonpath([str(a),str(p)])!=str(a): raise Reject("path escape")
    return p

def git(repo:Path,*words:str)->bytes:
    run=subprocess.run(["git",*words],cwd=repo,stdin=subprocess.DEVNULL,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False,env={"PATH":os.environ.get("PATH","")})
    if run.returncode or run.stderr: raise Reject("Git command failed closed")
    return run.stdout

def blob(repo:Path,rel:Path)->bytes:
    repo_path(repo,rel)
    return git(repo,"show",f"{P60}:{rel.as_posix()}")

Perm=tuple[int,...]
Poly=dict[tuple[int,...],int]

def perms(rows:Sequence[Sequence[int]])->list[Perm]:
    ans=[]
    for row in rows:
        if type(row) is not list or len(row)!=27 or sorted(row)!=list(range(1,28)): raise Reject("bad permutation")
        ans.append(tuple(x-1 for x in row))
    return ans

def mul(a:Perm,b:Perm)->Perm:
    return tuple(a[b[i]] for i in range(27))

def pinv(a:Perm)->Perm:
    z=[0]*27
    for i,j in enumerate(a): z[j]=i
    return tuple(z)

def conj(a:Perm,b:Perm)->Perm:
    return mul(a,mul(b,pinv(a)))

def close(gens:Iterable[Perm])->frozenset[Perm]:
    gs=tuple(gens); seen={E}; todo=deque([E])
    while todo:
        x=todo.popleft()
        for s in gs:
            y=mul(x,s)
            if y not in seen: seen.add(y);todo.append(y)
    return frozenset(seen)

def group_hash(g:Iterable[Perm])->str:
    return H([[x+1 for x in p] for p in sorted(g)])

class RightCosets:
    def __init__(self,G:frozenset[Perm],K:frozenset[Perm],identity_first:bool=False):
        unseen=set(G); order=sorted(G)
        if identity_first: order=[E]+[g for g in order if g!=E]
        self.reps=[];self.where={}
        for r in order:
            if r not in unseen: continue
            block={mul(r,h) for h in K}; idx=len(self.reps);self.reps.append(r)
            if not block<=unseen: raise Reject("coset collision")
            for x in block:self.where[x]=idx
            unseen-=block
        if unseen:raise Reject("coset omission")
        self.degree=len(self.reps)
    def image(self,g:Perm,i:int)->int:
        return self.where[mul(g,self.reps[i])]
    def orbits(self,K:frozenset[Perm],domain:Iterable[int]|None=None)->list[list[int]]:
        unseen=set(range(self.degree) if domain is None else domain); out=[]
        for seed in sorted(unseen):
            if seed not in unseen:continue
            block={self.image(g,seed) for g in K}
            if not block<=unseen:raise Reject("orbit collision")
            unseen-=block;out.append(sorted(block))
        if unseen:raise Reject("orbit omission")
        return out

def ledger(raw:bytes)->list[tuple[str,str]]:
    try:text=raw.decode("utf-8")
    except UnicodeDecodeError as exc:raise Reject("non-UTF8 ledger") from exc
    out=[];seen=set()
    for line in text.splitlines():
        if not line:continue
        if len(line)<67 or line[64:66]!="  ":raise Reject("malformed ledger")
        d,name=line[:64],line[66:]
        if name.startswith("./"):name=name[2:]
        rel=Path(name)
        if len(d)!=64 or any(c not in "0123456789abcdef" for c in d) or rel.is_absolute() or ".." in rel.parts or name in seen:raise Reject("unsafe ledger")
        seen.add(name);out.append((d,name))
    if [n for _,n in out]!=sorted(n for _,n in out):raise Reject("unsorted ledger")
    return out

def installed_formal(repo:Path)->dict[str,Any]:
    rels=[Path("BATCH_PLAN_C57_C61.md")]
    rels += [Path("henon_mu3_yukawa_tensor_fourier_descent")/n for n in FORMAL_NAMES]
    rels += [Path("henon_mu3_yukawa_tensor_fourier_descent/route_a_evaluation.yaml")]
    records=[];raws={}
    for rel in sorted(rels,key=lambda p:p.as_posix()):
        raw,rec=read_guarded(repo_path(repo,Path("henon_dynamics")/rel),1_000_000)
        raws[rel.as_posix()]=raw
        records.append({"path":rel.as_posix(),"sha256":rec["sha256"],"size_bytes":rec["size_bytes"],"lines":rec["lines"]})
    root_ledger=b"".join(f"{raw_sha(raws['henon_mu3_yukawa_tensor_fourier_descent/'+n])}  {n}\n".encode("ascii") for n in FORMAL_NAMES)
    exact_ledger=b"".join(f"{r['sha256']}  {r['path']}\n".encode("ascii") for r in records)
    if (raw_sha(root_ledger),raw_sha(raws["henon_mu3_yukawa_tensor_fourier_descent/route_a_evaluation.yaml"]),raw_sha(raws["BATCH_PLAN_C57_C61.md"]),raw_sha(exact_ledger),len(records),sum(r["size_bytes"] for r in records),sum(r["lines"] for r in records))!=(FORMAL13,FORMAL_ROUTE,FORMAL_BATCH,FORMAL15,15,199565,5094):
        raise Reject("installed formal tuple drift")
    return {"installed_root":"henon_dynamics/henon_mu3_yukawa_tensor_fourier_descent","formal_root_count":13,"formal_root_aggregate_sha256":FORMAL13,"route_sha256":FORMAL_ROUTE,"batch_sha256":FORMAL_BATCH,"exact15_ledger_sha256":FORMAL15,"exact15_count":15,"exact15_bytes":199565,"exact15_lines":5094,"entries":records}

def bind_inputs()->tuple[dict[str,Any],dict[str,Any]]:
    if not __debug__:raise Reject("optimized interpreter forbidden")
    repo,_project,checker_path=canonical_layout()
    if not stat.S_ISDIR(os.lstat(repo).st_mode):raise Reject("bad repo root")
    triple=tuple(git(repo,"rev-parse",x).decode("ascii").strip() for x in ("HEAD","HEAD^","HEAD^{tree}"))
    if triple!=(P60,P60_PARENT,P60_TREE):raise Reject("P60 identity drift")
    inputs={};records={}
    for label,(rel,want) in C60_INPUTS.items():
        raw=blob(repo,rel)
        if raw_sha(raw)!=want:raise Reject("released C60 byte drift")
        inputs[label]=raw;records[label]={"git_object":f"{P60}:{rel.as_posix()}","sha256":want,"size_bytes":len(raw)}
    if inputs["route"]!=inputs["route_archive"]:raise Reject("C60 Route mismatch")
    rb=blob(repo,Path("henon_dynamics/BATCH_PLAN_C57_C61.md"))
    if raw_sha(rb)!=RELEASED_BATCH_SHA:raise Reject("released Batch drift")
    records["released_batch"]={"git_object":f"{P60}:henon_dynamics/BATCH_PLAN_C57_C61.md","sha256":RELEASED_BATCH_SHA,"size_bytes":len(rb)}
    rows=ledger(inputs["full_manifest"]);total=0
    if len(rows)!=88:raise Reject("released manifest count")
    for want,name in rows:
        raw=blob(repo,C60_BASE/Path(name));total+=len(raw)
        if raw_sha(raw)!=want:raise Reject("released manifest leaf")
    replay={"entry_count":88,"verified_leaf_total_bytes":total,"all_entries_rebound":True}
    c59raw=blob(repo,C59_EVIDENCE)
    if raw_sha(c59raw)!=C59_SHA:raise Reject("C59 evidence drift")
    c59=load_strict(c59raw);cert=load_strict(inputs["certificate"]);gev=load_strict(inputs["group_evidence"]);rev=load_strict(inputs["resolvent_evidence"])
    if H(cert["payload"])!=cert["payload_sha256"] or cert["payload_sha256"]!=C60_PAYLOAD:raise Reject("C60 payload drift")
    arrays=gev["frozen_permutation_arrays"]["arrays"]
    if H(arrays)!=ARRAYS_SHA or gev["frozen_permutation_arrays"]["canonical_sha256"]!=ARRAYS_SHA:raise Reject("array drift")
    lamrec=cert["payload"]["G2_primitive_integral_carriers"]["carriers"]["L"]
    if H(lamrec["carrier"])!=LAMBDA_SHA or lamrec["carrier_sha256"]!=LAMBDA_SHA or rev["payload"]["carriers"]["L"]["carrier_sha256"]!=LAMBDA_SHA:raise Reject("lambda drift")
    formal=installed_formal(repo)
    guard,ginfo=read_guarded(repo_path(repo,GUARD_REL),1_000_000)
    if ginfo["sha256"]!=GUARD_SHA:raise Reject("guard drift")
    producer_path=checker_path.with_name("c61_resolvent.py")
    producer,prec=read_guarded(producer_path,2_000_000);checker,crec=read_guarded(checker_path,2_000_000)
    if b"c61_resolvent" not in producer or b"c61_checker_resolvent" not in checker:raise Reject("logical source identity")
    authority={
      "release":{"commit":P60,"parent":P60_PARENT,"tree":P60_TREE,"worktree_layer_included":False},
      "released_c60":records,"c60_payload_sha256":C60_PAYLOAD,"c60_full_manifest_replay":replay,
      "c59_resolvent":{"git_object":f"{P60}:{C59_EVIDENCE.as_posix()}","sha256":C59_SHA,"size_bytes":len(c59raw)},
      "frozen_permutation_arrays_sha256":ARRAYS_SHA,"lambda_carrier_sha256":LAMBDA_SHA,
      "formal_target":formal,
      "installed_protected_guard":{"path":GUARD_REL.as_posix(),"sha256":ginfo["sha256"],"size_bytes":len(guard)},
      "whole_project_inventory_owner":"release runner",
      "resolver_replay_contract":{"builder_basename":"c61_resolvent.py","checker_basename":"c61_checker_resolvent.py","evidence_basename":EVIDENCE_BASENAME,"canonical_stage_pattern":".c61-stage-XXXXXXXX","repository_and_project_derived_from_installed_source":True,"write_requires_absent_leaf":True,"existing_bytes_require_check_existing":True},
      "source_files":{"producer":{"sha256":prec["sha256"],"size_bytes":prec["size_bytes"]},"checker":{"sha256":crec["sha256"],"size_bytes":crec["size_bytes"]}},
      "runtime_pilot_dependencies":[],
    }
    alpha=c59["payload"]["line_configuration"]["alpha_by_standard_label"]
    if type(alpha) is not list or len(alpha)!=27 or any(type(x) is not int or not 0<=x<PRIME for x in alpha) or len(set(alpha))!=27:raise Reject("split roots invalid")
    finite=c59["payload"]["finite_field"]
    if c59["payload"]["constants"]["prime"]!=PRIME or finite["prime_proven"] is not True or finite["factor_degrees"]!=[[1,27]] or c59["payload"]["G1_primitive_orbit_resolvents"]["factor_degrees"]!=[[1,27]] or c59["payload"]["line_configuration"]["all_equation_residues_zero"] is not True:raise Reject("C59 completely-split labelled-root certificate")
    authority["released_C59_completely_split_prime_certificate"]={"source_git_object":f"{P60}:{C59_EVIDENCE.as_posix()}","prime_locator":"payload.constants.prime","prime":PRIME,"prime_proven_locator":"payload.finite_field.prime_proven","prime_proven":True,"factor_degrees_locator":"payload.finite_field.factor_degrees","factor_degrees":[[1,27]],"G1_factor_degrees_locator":"payload.G1_primitive_orbit_resolvents.factor_degrees","G1_factor_degrees":[[1,27]],"labelled_roots_locator":"payload.line_configuration.alpha_by_standard_label","labelled_root_count":27,"labelled_roots_sha256":H(alpha),"labelled_roots_pairwise_distinct":True,"all_equation_residues_zero_locator":"payload.line_configuration.all_equation_residues_zero","all_equation_residues_zero":True,"K_completely_split_at_prime":True}
    return authority,{"repo":repo,"arrays":arrays,"lambda":lamrec["carrier"],"alpha":alpha}

def groups_from(arrays:dict[str,Any])->dict[str,Any]:
    gg={k:perms(v) for k,v in arrays.items() if k.endswith("_generators")}
    W=close(gg["W27_generators"]);N=close(gg["N_generators"]);J=close(gg["J_generators"])
    Hp=close(gg["H301_generators"]);H0=close(gg["H302_generators"]);Hm=close(gg["H303_generators"])
    x=perms([arrays["normalizer_conjugator"]])[0];H3=close(conj(x,h) for h in gg["H303_generators"])
    Sg=perms(S_GEN_1);Tg=perms(T_GEN_1);S=close(Sg);T=close(Tg)
    G={"W":W,"N":N,"J":J,"Hplus":Hp,"H0":H0,"Hminus":Hm,"H3":H3,"Splus":S,"Tplus":T}
    if {k:len(v) for k,v in G.items()}!={"W":51840,"N":324,"J":81,"Hplus":162,"H0":162,"Hminus":162,"H3":162,"Splus":648,"Tplus":1296}:raise Reject("group orders")
    if group_hash(S)!="1df969ee447989751850d36d7af50ce219daff3dbc830c56df04d93e9c512871" or group_hash(T)!="55d7f2df8abc6709489e9bf632c45d620b9b570e6a295a82ee6f941c24c2c6bc":raise Reject("S/T group identity")
    q={"1":E,"Hplus":min(Hp-J),"H0":min(H0-J),"H3":min(H3-J)}
    if len({frozenset(mul(r,j) for j in J) for r in q.values()})!=4:raise Reject("V4 quotient")
    return {"G":G,"gens":gg,"Sgens":Sg,"Tgens":Tg,"q":q}

def mixed_rebuild(ctx:dict[str,Any],doc:dict[str,Any])->dict[int,tuple[frozenset[Perm],frozenset[Perm]]]:
    G=ctx["G"];W,Hp,Hm=G["W"],G["Hplus"],G["Hminus"]
    act=RightCosets(W,Hm);unseen=set(range(act.degree));rows=[];types={}
    for seed in range(act.degree):
        if seed not in unseen:continue
        r=act.reps[seed];orb={act.image(h,seed) for h in Hp};unseen-=orb
        moved=frozenset(conj(r,h) for h in Hm)
        inter=frozenset(Hp&moved)
        join=close(tuple(ctx["gens"]["H301_generators"])+tuple(conj(r,h) for h in ctx["gens"]["H303_generators"]))
        if seed not in TYPE_BY_SEED:raise Reject("mixed seed")
        kind=TYPE_BY_SEED[seed]
        row={"seed":seed,"representative_one_based":[x+1 for x in r],"tensor_right_coset_orbit_size":len(orb),"conjugate_position_orbit_size":CONJ_ORBIT[kind],"q_isomorphism_type":kind,"intersection_order":len(inter),"intersection_sha256":group_hash(inter),"simple_factor_degree":len(W)//len(inter),"join_order":len(join),"join_sha256":group_hash(join),"intersection_field_degree":len(W)//len(join)}
        rows.append(row)
        if seed==REP_SEED[kind]:types[kind]=(inter,join)
    rows.sort(key=lambda r:r["seed"])
    advertised=doc["GAF4_mixed_type3_exact_bridge"]
    if rows!=advertised["mixed_rows"] or len(rows)!=12 or len(types)!=8:raise Reject("mixed 12/8 reconstruction")
    if sum(r["simple_factor_degree"] for r in rows)!=102400 or sum(r["tensor_right_coset_orbit_size"] for r in rows)!=320 or sum(CONJ_ORBIT.values())!=160:raise Reject("mixed spectrum totals")
    if [Counter(r["q_isomorphism_type"] for r in rows)[i] for i in range(1,9)]!=[1,2,1,2,2,2,1,1]:raise Reject("mixed multiplicities")
    if types[3][1]!=G["Tplus"] or rows[[r["seed"] for r in rows].index(149)]["simple_factor_degree"]!=1920:raise Reject("mixed type-3 exact bridge")
    return types

def mod_product(a:Sequence[int],b:Sequence[int])->list[int]:
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]=(out[i+j]+x*y)%PRIME
    return out

def int_product(a:Sequence[int],b:Sequence[int])->list[int]:
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out

def lagrange(alpha:Sequence[int])->tuple[list[list[int]],list[int]]:
    basis=[]
    for j,a in enumerate(alpha):
        num=[1];den=1
        for k,b in enumerate(alpha):
            if k==j:continue
            num=mod_product(num,[(-b)%PRIME,1]);den=den*(a-b)%PRIME
        scale=pow(den,-1,PRIME);basis.append([x*scale%PRIME for x in num])
    for j,p in enumerate(basis):
        for k,a in enumerate(alpha):
            value=0
            for c in reversed(p):value=(value*a+c)%PRIME
            if value!=(j==k):raise Reject("Lagrange identity matrix")
    vanish=[1]
    for a in alpha:vanish=int_product(vanish,[-a,1])
    if len(vanish)!=28 or vanish[-1]!=1:raise Reject("vanishing polynomial")
    return basis,vanish

def check_product_carriers(ctx:dict[str,Any],types:dict[int,tuple[frozenset[Perm],frozenset[Perm]]],alpha:list[int],doc:dict[str,Any])->None:
    W=ctx["G"]["W"];basis,vanish=lagrange(alpha)
    advertised=doc["GAF3_stabilizers_and_noncollision"]["product_form_mixed_base_A_B_resolvents"]
    if advertised["univariate_lagrange_basis_sha256"]!=H(basis) or advertised["integer_vanishing_polynomial_sha256"]!=H(vanish):raise Reject("product basis hashes")
    sub={f"E{i}":types[i][0] for i in range(1,9)}
    sub.update({"C1":types[1][1],"C2":types[2][1],"C3":types[3][1],"C4":W,"A40":ctx["G"]["Tplus"],"B80":ctx["G"]["Splus"]})
    carriers=advertised["carriers"]
    if set(carriers)!=set(sub) or len(carriers)!=14:raise Reject("carrier inventory")
    ordered=sorted(W)
    for name,K in sub.items():
        act=RightCosets(W,K,True);labels=[act.where[g]+1 for g in ordered];degree=act.degree
        counts=Counter(labels);values=list(range(1,degree+1));factors=[[(-v)%PRIME,1] for v in values]
        c=carriers[name]
        if c["degree"]!=degree or c["subgroup_order"]!=len(K) or c["subgroup_complete_group_sha256"]!=group_hash(K):raise Reject("carrier subgroup")
        if c["regular_basis_vector_count"]!=51840 or c["right_coset_label_vector_sha256"]!=H(labels) or c["coefficient_range"]!=[1,degree] or c["each_coefficient_multiplicity"]!=len(K) or set(counts.values())!={len(K)}:raise Reject("carrier full label vector")
        if c["sorted_values_sha256"]!=H(values) or c["product_form_orbit_polynomial_sha256"]!=H(factors) or c["product_form_orbit_polynomial_factor_count"]!=degree or not c["complete_noncollision"]:raise Reject("carrier product noncollision")
        indices=sorted({0,len(ordered)//7,len(ordered)//3,len(ordered)//2,len(ordered)-1})
        samples=[{"ambient_index":i,"permutation_one_based":[x+1 for x in ordered[i]],"right_coset_label":labels[i]} for i in indices]
        if c["hostile_label_samples"]!=samples:raise Reject("carrier hostile samples")
        spec=c["carrier_spec"]
        if c["carrier_spec_sha256"]!=H(spec) or spec["basis_sha256"]!=H(basis) or spec["integer_vanishing_polynomial_sha256"]!=H(vanish) or spec["right_coset_label_vector_sha256"]!=H(labels):raise Reject("carrier spec")
        # The tensor Lagrange functions evaluate as the 51,840 identity
        # submatrix.  Z vanishes there.  Its monic marker exponent is
        # (27+g(i))_i; coordinatewise domination by another permutation and
        # equality of coordinate sums forces equality.  Label 1 occurs on H.
        required=(c["exact_monomial_content"]==1 and c["integral"] is True and c["formal_stabilizer_equals_embedded_subgroup"] is True and c["characteristic_zero_expanded_coefficients_claimed"] is False and "Z*M_g" in spec["marker"] and min(labels)==1)
        if not required:raise Reject("marker/content/stabilizer proof")
    if carriers["A40"]["carrier_spec_sha256"]!=carriers["C3"]["carrier_spec_sha256"]:raise Reject("A/C3 carrier identity")

def pserial(p:Poly)->list[list[Any]]:
    return [[list(m),c] for m,c in sorted(p.items()) if c]

def psha(p:Poly)->str:return H(pserial(p))

def pimage(g:Perm,p:Poly)->Poly:
    return {tuple(sorted(g[i] for i in m)):c for m,c in p.items()}

def padd(dst:Poly,src:Poly,k:int)->None:
    for m,c in src.items():
        v=dst.get(m,0)+k*c
        if v:dst[m]=v
        elif m in dst:del dst[m]

def pmul(a:Poly,b:Poly)->Poly:
    out={}
    for m,x in a.items():
        for n,y in b.items():
            key=tuple(sorted(m+n));out[key]=out.get(key,0)+x*y
    return {m:c for m,c in out.items() if c}

def frozen(p:Poly)->tuple[tuple[tuple[int,...],int],...]:return tuple(sorted(p.items()))

def signed_key(x:tuple[tuple[tuple[int,...],int],...])->tuple[tuple[tuple[int,...],int],...]:
    neg=tuple((m,-c) for m,c in x);return min(x,neg)

def porbit(p:Poly,gens:Sequence[Perm],sign:bool=False)->list[tuple[tuple[tuple[int,...],int],...]]:
    first=frozen(p);first=signed_key(first) if sign else first;seen={first};todo=deque([first])
    while todo:
        x=dict(todo.popleft())
        for g in gens:
            y=frozen(pimage(g,x));y=signed_key(y) if sign else y
            if y not in seen:seen.add(y);todo.append(y)
    return sorted(seen)

def peval(p:Poly,alpha:Sequence[int])->int:
    total=0
    for m,c in p.items():
        v=c%PRIME
        for i in m:v=v*alpha[i]%PRIME
        total=(total+v)%PRIME
    return total

def roots_poly(roots:Sequence[int])->list[int]:
    out=[1]
    for r in roots:out=mod_product(out,[(-r)%PRIME,1])
    return out

def orbit_info(p:Poly,gens:Sequence[Perm],alpha:Sequence[int],square:bool=False)->dict[str,Any]:
    orb=porbit(p,gens,square);vals=sorted({pow(peval(dict(x),alpha),2 if square else 1,PRIME) for x in orb});coef=roots_poly(vals)
    return {"formal_orbit_size":len(orb),"modular_distinct_value_count":len(vals),"sorted_values_sha256":H(vals),"modular_minimal_polynomial_coefficient_count":len(coef),"modular_minimal_polynomial_sha256":H(coef),"complete_noncollision":len(vals)==len(orb)}

def check_fourier(ctx:dict[str,Any],docs:dict[str,Any],doc:dict[str,Any])->dict[str,Poly]:
    lam={tuple(m):int(c) for m,c in docs["lambda"]}
    if psha(lam)!=LAMBDA_SHA:raise Reject("lambda parse")
    images={k:pimage(g,lam) for k,g in ctx["q"].items()}
    chars={"Hplus":{"1":1,"Hplus":1,"H0":-1,"H3":-1},"H0":{"1":1,"Hplus":-1,"H0":1,"H3":-1},"H3":{"1":1,"Hplus":-1,"H0":-1,"H3":1}}
    trace={};raw={k:{} for k in chars}
    for label,p in images.items():
        padd(trace,p,1)
        for name,ch in chars.items():padd(raw[name],p,ch[label])
    if raw["H0"]:raise Reject("R0 nonzero")
    if any(c%2 for c in raw["Hplus"].values()) or any(c%4 for c in raw["H3"].values()):raise Reject("Fourier normalization")
    rp={m:c//2 for m,c in raw["Hplus"].items()};r3={m:c//4 for m,c in raw["H3"].items()}
    r0=pmul(rp,r3);dp=pmul(rp,rp);d3=pmul(r3,r3)
    polys={"Trace":trace,"rplus":rp,"r3":r3,"r0":r0,"delta_plus":dp,"delta3":d3}
    records=doc["GAF1_fourier_carrier_dag"]["normalized_carriers"]
    for name,p in polys.items():
        lock=FOURIER_LOCK[name];hist=[[k,v] for k,v in sorted(Counter(p.values()).items())]
        if (len(next(iter(p))),len(p),hist,psha(p))!=lock[:4]:raise Reject("Fourier carrier")
        if lock[4] is not None and peval(p,docs["alpha"])!=lock[4]:raise Reject("Fourier split value")
        if records[name]["carrier_sha256"]!=psha(p) or records[name]["term_count"]!=len(p):raise Reject("Fourier evidence record")
    raw_e=doc["GAF1_fourier_carrier_dag"]["raw_components"]
    if raw_e!={"R0":{"zero":True,"term_count":0,"carrier_sha256":psha(raw["H0"])},"Rplus":{"term_count":len(raw["Hplus"]),"carrier_sha256":psha(raw["Hplus"]),"exact_content_divisor":2},"R3":{"term_count":len(raw["H3"]),"carrier_sha256":psha(raw["H3"]),"exact_content_divisor":4}}:raise Reject("raw Fourier/exact division evidence")
    rebuild=dict(trace);padd(rebuild,rp,2);padd(rebuild,r3,4)
    if rebuild!={m:4*c for m,c in lam.items()}:raise Reject("Fourier reconstruction")
    orbit={"rplus":orbit_info(rp,ctx["gens"]["W27_generators"],docs["alpha"]),"delta_plus":orbit_info(rp,ctx["gens"]["W27_generators"],docs["alpha"],True),"r3":orbit_info(r3,ctx["gens"]["W27_generators"],docs["alpha"]),"delta3":orbit_info(r3,ctx["gens"]["W27_generators"],docs["alpha"],True),"r0":orbit_info(r0,ctx["gens"]["W27_generators"],docs["alpha"]),"delta0":orbit_info(r0,ctx["gens"]["W27_generators"],docs["alpha"],True)}
    advertised=doc["GAF3_stabilizers_and_noncollision"]["fourier_formal_and_evaluated_orbits"]
    if orbit!=advertised:raise Reject("Fourier orbit evidence")
    for name,r in orbit.items():
        lock=ORBIT_LOCK[name]
        if (r["formal_orbit_size"],r["sorted_values_sha256"],r["modular_minimal_polynomial_sha256"])!=lock:raise Reject("Fourier noncollision lock")
    target=frozen(rp);neg=tuple((m,-c) for m,c in target)
    if any(frozen(pimage(s,rp))!=target for s in ctx["G"]["Splus"]):raise Reject("S containment")
    if any(frozen(pimage(t,rp)) not in (target,neg) for t in ctx["G"]["Tplus"]):raise Reject("T containment")
    if len(ctx["G"]["Splus"])*len(porbit(rp,ctx["gens"]["W27_generators"]))!=len(ctx["G"]["W"]) or len(ctx["G"]["Tplus"])*len(porbit(rp,ctx["gens"]["W27_generators"],True))!=len(ctx["G"]["W"]):raise Reject("exact S/T orbit-stabilizer")
    g3=doc["GAF3_stabilizers_and_noncollision"]
    if g3["Splus"]!={"order":648,"complete_group_sha256":group_hash(ctx["G"]["Splus"]),"contained_in_exact_stabilizer_and_equal_by_orbit_stabilizer":True} or g3["Tplus"]!={"order":1296,"complete_group_sha256":group_hash(ctx["G"]["Tplus"]),"contained_in_line_stabilizer_and_equal_by_sign_orbit_stabilizer":True}:raise Reject("advertised exact S/T")
    span=doc["GAF2_orbit_span_and_nonnormality"]
    values=[peval(trace,docs["alpha"]),peval(rp,docs["alpha"]),peval(r3,docs["alpha"])]
    if span["identity_values"]!=values or span["orbit_span_dimension_over_M"]!=3 or not all(values):raise Reject("evaluated rank-three span")
    return {**polys,"lambda":lam}

def normalizer(G:frozenset[Perm],K:frozenset[Perm],kgens:Sequence[Perm])->frozenset[Perm]:
    return frozenset(g for g in G if all(conj(g,h) in K for h in kgens))

def group_core(gens:Sequence[Perm],K:frozenset[Perm])->frozenset[Perm]:
    now=K
    carriers=tuple(gens)+tuple(pinv(g) for g in gens)
    while True:
        old=now
        for g in carriers:now=frozenset(set(now)&{conj(g,h) for h in now})
        if now==old:return now

def check_diamond(ctx:dict[str,Any],types:dict[int,tuple[frozenset[Perm],frozenset[Perm]]],doc:dict[str,Any])->None:
    G=ctx["G"];W,N,Hp,S,T=G["W"],G["N"],G["Hplus"],G["Splus"],G["Tplus"]
    if not (Hp<S<T and N<T and S&N==Hp):raise Reject("diamond lattice")
    if close(tuple(ctx["Sgens"])+tuple(ctx["gens"]["N_generators"]))!=T or {mul(s,n) for s in S for n in N}!=set(T):raise Reject("diamond join/product")
    if normalizer(W,S,ctx["Sgens"])!=T or normalizer(W,T,ctx["Tgens"])!=T:raise Reject("diamond normalizers")
    if len(group_core(ctx["gens"]["W27_generators"],S))!=1 or len(group_core(ctx["gens"]["W27_generators"],T))!=1:raise Reject("diamond cores")
    bridge=doc["GAF4_mixed_type3_exact_bridge"];diamond=doc["GAF5_fixed_field_diamond"]
    p3="263f31237e6f5111f76fd3470b6936a1a314020255c22eab55cece395c2adeb5"
    if types[3][1]!=T or bridge["exact_embedded_element_set_equality_Tmix_Tplus"] is not True or bridge["Tmix_sha256"]!=group_hash(T) or bridge["self_P3_substitute_hash_rejected"]!=p3 or p3==group_hash(T):raise Reject("Tmix equality/P3 correction")
    if diamond["degrees_A40_B80_M160_Fplus320"]!=[40,80,160,320] or diamond["B80_intersection_M160_equals_A40"] is not True or diamond["B80_compositum_M160_equals_Fplus320"] is not True or diamond["generated_Splus_N_equals_Tplus"] is not True or diamond["set_product_Splus_N_equals_Tplus"] is not True:raise Reject("fixed-field diamond")

def locals_from(ctx:dict[str,Any])->dict[str,frozenset[Perm]]:
    gg=ctx["gens"];extra={k:perms(v) for k,v in LOCAL_GEN_1.items()}
    out={
      "I3":close(gg["branch140_D_generators"]),"P3":close(gg["branch140_P_generators"]),"Q3":close(gg["branch140_Q_generators"]),
      "I5":close(extra["I5"]),"P5":close(extra["P5"]),"C3":close(extra["C3"]),"C2":close(extra["C2"]),"Cinf":close(extra["Cinf"]),
      "D140":close(gg["branch140_D_generators"]),"I140":close(gg["branch140_D_generators"]),"P140":close(gg["branch140_P_generators"]),"Q140":close(gg["branch140_Q_generators"]),
      "D206":close(gg["branch206_D_generators"]),"I206":close(gg["branch206_I_generators"]),"P206":close(gg["branch206_P_generators"]),"Q206":close(gg["branch206_Q_generators"]),
    }
    wanted={"I3":18,"P3":9,"Q3":3,"I5":20,"P5":5,"C3":3,"C2":2,"Cinf":2,"D140":18,"I140":18,"P140":9,"Q140":3,"D206":36,"I206":18,"P206":9,"Q206":3}
    if {k:len(v) for k,v in out.items()}!=wanted:raise Reject("local group orders")
    return out

def arithmetic(G:frozenset[Perm],K:frozenset[Perm],L:dict[str,frozenset[Perm]])->dict[str,Any]:
    a=RightCosets(G,K);order=["I3","P3","Q3","I5","P5","C3","C2","Cinf"]
    count=[len(a.orbits(L[k])) for k in order];n=a.degree;i3,p3,q3,i5,p5,c3,c2,ci=count
    u=2*(n-i3)+(n-p3)+2*(n-q3);v=4*(n-i5)+3*(n-p5)
    if u%2 or v%4:raise Reject("conductor integrality")
    ex=[u//2,v//4,n-c3,n-c2];sig=[2*ci-n,n-ci]
    if sig[0]+2*sig[1]!=n or min(sig)<0:raise Reject("signature")
    return {"degree":n,"orbit_vector_I3_P3_Q3_I5_P5_C3_C2_Cinf":count,"signature_r1_r2":sig,"discriminant_sign":-1 if sig[1]%2 else 1,"absolute_exponents_3_5_PiA_PiB":ex}

def prime_rows(a:RightCosets,D:frozenset[Perm],I:frozenset[Perm],Pp:frozenset[Perm],Q:frozenset[Perm])->list[dict[str,Any]]:
    out=[]
    for idx,orb in enumerate(a.orbits(D)):
        n=len(orb);f=len(a.orbits(I,orb));pc=len(a.orbits(Pp,orb));qc=len(a.orbits(Q,orb))
        if n%f:raise Reject("local e")
        e=n//f;num=2*(n-f)+(n-pc)+2*(n-qc)
        if num%(2*f):raise Reject("local d")
        out.append({"prime_index":idx,"coset_seed":min(orb),"row_n_e_f_d":[n,e,f,num//(2*f)]})
    return out

def local_table(a:RightCosets,D:frozenset[Perm],I:frozenset[Perm],Pp:frozenset[Perm],Q:frozenset[Perm])->dict[str,Any]:
    rows=prime_rows(a,D,I,Pp,Q);counts=Counter(tuple(x["row_n_e_f_d"]) for x in rows)
    coll=[{"row_n_e_f_d":list(r),"multiplicity":counts[r]} for r in sorted(counts)]
    degree=sum(x["multiplicity"]*x["row_n_e_f_d"][0] for x in coll);diff=sum(x["multiplicity"]*x["row_n_e_f_d"][2]*x["row_n_e_f_d"][3] for x in coll)
    if degree!=a.degree:raise Reject("local totals")
    return {"degree_total":degree,"different_total":diff,"factor_count":len(rows),"uncollected_prime_rows":rows,"collected_rows_with_multiplicity":coll}

def relative_tower(base:RightCosets,fields:dict[str,RightCosets],D:frozenset[Perm],I:frozenset[Perm],Pp:frozenset[Perm],Q:frozenset[Perm])->dict[str,Any]:
    names=["Fplus","F0","F3","L"];qdeg={"Fplus":2,"F0":2,"F3":2,"L":4}
    borb=base.orbits(D);brows=prime_rows(base,D,I,Pp,Q);lookup={c:i for i,o in enumerate(borb) for c in o}
    aorb={n:fields[n].orbits(D) for n in names};arows={n:prime_rows(fields[n],D,I,Pp,Q) for n in names}
    rows=[];types=Counter();mass=Counter();norm=Counter({n:0 for n in names})
    for bi,(bo,bitem) in enumerate(zip(borb,brows)):
        b=bitem["row_n_e_f_d"];relative={}
        for name in names:
            a=fields[name];selected=[]
            for orb,item in zip(aorb[name],arows[name]):
                images={lookup[base.where[a.reps[c]]] for c in orb}
                if len(images)!=1:raise Reject("tower prime map")
                if next(iter(images))==bi:selected.append(item["row_n_e_f_d"])
            rel=[]
            for z in selected:
                if z[1]%b[1] or z[2]%b[2]:raise Reject("relative e/f")
                rel.append([len(selected),z[1]//b[1],z[2]//b[2],z[3]-(z[1]//b[1])*b[3]])
            if not rel or any(x!=rel[0] for x in rel) or rel[0][0]*rel[0][1]*rel[0][2]!=qdeg[name] or rel[0][3]<0:raise Reject("relative row")
            relative[name]=rel[0]
        exp={n:relative[n][0]*relative[n][2]*relative[n][3] for n in names};ram={n for n in names[:3] if exp[n]>0}
        if not ram:dtype="trivial"
        else:
            if len(ram)!=2:raise Reject("V4 inertia population")
            split=({"Fplus","F0","F3"}-ram).pop();dtype={"Fplus":"Hplus","F0":"H0","F3":"H3"}[split]
        checks={"Fplus_F3_coprime":min(exp["Fplus"],exp["F3"])==0,"F0_product_law":exp["F0"]==exp["Fplus"]+exp["F3"],"L_square_law":exp["L"]==2*exp["F0"],"conductor_discriminant_law":exp["L"]==exp["Fplus"]+exp["F0"]+exp["F3"]}
        if not all(checks.values()):raise Reject("ideal complementarity")
        types[dtype]+=1;mass[dtype]+=b[2]
        for n in names:norm[n]+=b[2]*exp[n]
        rows.append({"base_prime_index":bi,"base_coset_seed":min(bo),"base_row_n_e_f_d":b,"relative_rows_g_e_f_d":relative,"relative_discriminant_exponents":exp,"V4_decomposition_inertia_type":dtype,**checks})
    collected_count=Counter(canon({"base":r["base_row_n_e_f_d"],"relative":r["relative_rows_g_e_f_d"]}).decode("ascii") for r in rows)
    coll=[{"row":load_strict(k.encode("ascii")),"multiplicity":v} for k,v in sorted(collected_count.items())]
    return {"base_prime_count":len(rows),"uncollected_base_prime_rows":rows,"collected_rows_with_multiplicity":coll,"V4_type_counts":{k:types.get(k,0) for k in ["Hplus","H3","trivial","H0"]},"residue_degree_masses":{k:mass.get(k,0) for k in ["Hplus","H3","trivial","H0"]},"relative_norm_exponents_Fplus_F0_F3_L":[norm[n] for n in names],"all_rows_verify_ideal_laws":True}

def check_arithmetic(ctx:dict[str,Any],types:dict[int,tuple[frozenset[Perm],frozenset[Perm]]],doc:dict[str,Any])->None:
    G=ctx["G"];W=G["W"];L=locals_from(ctx)
    sub={f"E{i}":types[i][0] for i in range(1,9)}
    sub.update({"C1":types[1][1],"C2":types[2][1],"C3":types[3][1],"C4":W,"B80":G["Splus"]})
    rows={name:arithmetic(W,K,L) for name,K in sub.items()}
    if rows!=doc["GAF6_global_arithmetic"]["fields"]:raise Reject("full global field table")
    for name,lock in GLOBAL_LOCK.items():
        r=rows[name]
        if (r["degree"],r["signature_r1_r2"],r["discriminant_sign"],r["absolute_exponents_3_5_PiA_PiB"])!=lock[:4]:raise Reject("global arithmetic lock")
    base={1:"C1",2:"C2",3:"C3",4:"C4",5:"C4",6:"C4",7:"C4",8:"C4"};rel={}
    for i in range(1,9):
        u=rows[f"E{i}"];b=rows[base[i]];q=u["degree"]//b["degree"]
        rel[f"E{i}_over_{base[i]}"]=[x-q*y for x,y in zip(u["absolute_exponents_3_5_PiA_PiB"],b["absolute_exponents_3_5_PiA_PiB"])]
    if rel!=doc["GAF6_global_arithmetic"]["mixed_relative_discriminant_norm_vectors"]:raise Reject("mixed relative discriminants")
    A=rows["C3"];B=rows["B80"];M=arithmetic(W,G["N"],L);Fp=arithmetic(W,G["Hplus"],L)
    def rv(u:dict[str,Any],b:dict[str,Any])->list[int]:
        q=u["degree"]//b["degree"];return [x-q*y for x,y in zip(u["absolute_exponents_3_5_PiA_PiB"],b["absolute_exponents_3_5_PiA_PiB"])]
    diamond={"d_B80_over_A40":rv(B,A),"d_M160_over_A40":rv(M,A),"d_Fplus320_over_B80":rv(Fp,B),"d_Fplus320_over_A40":rv(Fp,A),"d_Fplus320_over_M160":rv(Fp,M)}
    if diamond!=doc["GAF6_global_arithmetic"]["diamond_relative_discriminant_norm_vectors"]:raise Reject("diamond discriminants")
    actions={n:RightCosets(W,K) for n,K in sub.items()};branches={"ToM140":(L["D140"],L["I140"],L["P140"],L["Q140"]),"ToM206":(L["D206"],L["I206"],L["P206"],L["Q206"])}
    local={b:{n:local_table(a,*quad) for n,a in actions.items()} for b,quad in branches.items()}
    local_e=doc["GAF7_both_local_branches_and_ideal_laws"]
    if local!=local_e["absolute_local_tables"]:raise Reject("full both-branch local tables")
    if local_e["retained_branches"]!=["ToM140","ToM206"] or local_e["branch_selected"] is not False or local_e["all_primewise_ideal_laws"] is not True or local_e["local_fields_classified_by_nefd_rows"] is not False:raise Reject("branch/firewall flags")
    for b in branches:
        for n,t in local[b].items():
            if t["different_total"]!=rows[n]["absolute_exponents_3_5_PiA_PiB"][0]:raise Reject("local/global p3")
    vg={"Fplus":G["Hplus"],"F0":G["H0"],"F3":G["H3"],"L":G["J"]};baseact=RightCosets(W,G["N"]);fa={n:RightCosets(W,K) for n,K in vg.items()}
    towers={b:relative_tower(baseact,fa,*quad) for b,quad in branches.items()}
    if towers!=doc["GAF7_both_local_branches_and_ideal_laws"]["V4_relative_towers_over_M"]:raise Reject("full V4 tower tables")
    if towers["ToM140"]["V4_type_counts"]!={"Hplus":8,"H3":8,"trivial":6,"H0":0} or towers["ToM206"]["V4_type_counts"]!={"Hplus":4,"H3":4,"trivial":3,"H0":0}:raise Reject("retained D3 branches")

SCHEMA={"schema_id":"hcs-c61-resolvent-evidence-v1","top_level_keys":["schema_id","schema_sha256","authority","conventions","GAF0_released_authority_rebind","GAF1_fourier_carrier_dag","GAF2_orbit_span_and_nonnormality","GAF3_stabilizers_and_noncollision","GAF4_mixed_type3_exact_bridge","GAF5_fixed_field_diamond","GAF6_global_arithmetic","GAF7_both_local_branches_and_ideal_laws","independence_contract","scope_nonclaims","status","payload_sha256"],"strict_json":True,"unknown_or_missing_fields_rejected_by_independent_full_rebuild":True,"duplicate_keys_rejected":True,"floats_rejected":True,"booleans_rejected_in_integer_slots":True,"non_utf8_rejected":True,"noncanonical_json_rejected":True,"max_evidence_bytes":25000000,"scope_false_leaf_count":30}

def payload(doc:dict[str,Any])->str:
    return H({k:v for k,v in doc.items() if k!="payload_sha256"})

def parse_wire(raw:bytes)->dict[str,Any]:
    if len(raw)>25_000_000:raise Reject("oversized evidence")
    obj=load_strict(raw)
    if type(obj) is not dict or raw!=canon(obj)+b"\n":raise Reject("noncanonical evidence wire")
    return obj

def surface(doc:dict[str,Any],authority:dict[str,Any])->None:
    if type(doc) is not dict or set(doc)!=TOP:raise Reject("top schema")
    if doc["schema_id"]!="hcs-c61-resolvent-evidence-v1" or doc["schema_sha256"]!=H(SCHEMA):raise Reject("schema identity")
    if doc["authority"]!=authority:raise Reject("authority reconstruction")
    for key,want in STABLE_SHA.items():
        if H(doc[key])!=want:raise Reject(f"stable section {key}")
    contract=doc["independence_contract"]
    wanted={"producer_source_sha256":authority["source_files"]["producer"]["sha256"],"checker_source_sha256":authority["source_files"]["checker"]["sha256"],"checker_imports_producer":False,"shared_mathematical_helpers":False,"shared_inputs":"released authority and independently duplicated expected literals only","producer_two_run_replay":True,"checker_attestation_two_run_equal":False,"checker_attestation":None}
    if contract!=wanted:raise Reject("candidate independence contract")
    if doc["payload_sha256"]!=payload(doc):raise Reject("candidate payload")

def full_check(doc:dict[str,Any])->tuple[dict[str,Any],dict[str,Any]]:
    authority,docs=bind_inputs();surface(doc,authority)
    ctx=groups_from(docs["arrays"])
    types=mixed_rebuild(ctx,doc)
    check_product_carriers(ctx,types,docs["alpha"],doc)
    check_fourier(ctx,docs,doc)
    check_diamond(ctx,types,doc)
    check_arithmetic(ctx,types,doc)
    return authority,{"docs":docs,"ctx":ctx,"types":types}

def expect_bad(fn:Callable[[],Any])->bool:
    try:fn()
    except (Reject,OSError,ValueError,KeyError,TypeError,IndexError):return True
    return False

def parser_suite()->dict[str,Any]:
    cases={
      "duplicate_key":lambda:load_strict(b'{"x":1,"x":2}'),
      "float":lambda:load_strict(b'{"x":1.5}'),
      "nan":lambda:load_strict(b'{"x":NaN}'),
      "non_utf8":lambda:load_strict(b'\xff'),
      "trailing_junk":lambda:load_strict(b'{}x'),
      "missing_final_newline":lambda:parse_wire(b'{}'),
      "noncanonical_spacing":lambda:parse_wire(b'{ "x":1 }\n'),
      "oversized":lambda:parse_wire(b' '*25_000_001),
    }
    passed=[name for name,fn in cases.items() if expect_bad(fn)]
    if len(passed)!=len(cases):raise Reject("strict parser hostile suite")
    return {"passed":len(passed),"total":len(cases),"families":sorted(passed)}

def path_suite(evidence_path:Path)->dict[str,Any]:
    _repo,project,_source=canonical_layout();results=(project/"results").resolve(strict=True);stage=evidence_path.parent
    cases={
      "direct_results_leaf":results/EVIDENCE_BASENAME,
      "outside_results":project/EVIDENCE_BASENAME,
      "nested_stage_leaf":stage/"nested"/EVIDENCE_BASENAME,
      "wrong_basename":stage/"wrong.json",
      "punctuated_stage":results/".c61-stage-ABCD!234"/EVIDENCE_BASENAME,
      "short_stage":results/".c61-stage-ABC1234"/EVIDENCE_BASENAME,
      "overlong_stage":results/".c61-stage-ABCDEFGHI"/EVIDENCE_BASENAME,
    }
    passed=[]
    for name,path in cases.items():
        if not expect_bad(lambda path=path:staged_evidence_path(str(path),None)):raise Reject("canonical path hostile suite")
        passed.append(name)
    return {"passed":len(passed),"total":len(cases),"families":sorted(passed),"symlink_hardlink_stage_substitution_owned_by_nonpromoted_harness":True}

def mutate(doc:dict[str,Any],name:str)->dict[str,Any]:
    x=copy.deepcopy(doc)
    if name=="marker_removal":x["GAF3_stabilizers_and_noncollision"]["product_form_mixed_base_A_B_resolvents"]["carriers"]["E1"]["carrier_spec"]["marker"]=""
    elif name=="content_two":x["GAF3_stabilizers_and_noncollision"]["product_form_mixed_base_A_B_resolvents"]["carriers"]["B80"]["exact_monomial_content"]=2
    elif name=="coset_side":x["GAF3_stabilizers_and_noncollision"]["product_form_mixed_base_A_B_resolvents"]["carriers"]["A40"]["carrier_spec"]["coefficient_rule"]="left cosets"
    elif name=="label_hash":x["GAF3_stabilizers_and_noncollision"]["product_form_mixed_base_A_B_resolvents"]["carriers"]["E8"]["right_coset_label_vector_sha256"]="0"*64
    elif name=="R0_nonzero":x["GAF1_fourier_carrier_dag"]["raw_components"]["R0"]["zero"]=False
    elif name=="exact_division":x["GAF1_fourier_carrier_dag"]["raw_components"]["R3"]["exact_content_divisor"]=2
    elif name=="rank_drop":x["GAF2_orbit_span_and_nonnormality"]["orbit_span_dimension_over_M"]=2
    elif name=="subgroup_hash":x["GAF3_stabilizers_and_noncollision"]["Splus"]["complete_group_sha256"]="0"*64
    elif name=="mixed_count":x["GAF4_mixed_type3_exact_bridge"]["mixed_rows"][0]["tensor_right_coset_orbit_size"]+=1
    elif name=="Tmix_hash_only":x["GAF4_mixed_type3_exact_bridge"]["exact_embedded_element_set_equality_Tmix_Tplus"]=False
    elif name=="self_P3_substitution":x["GAF4_mixed_type3_exact_bridge"]["Tmix_sha256"]="263f31237e6f5111f76fd3470b6936a1a314020255c22eab55cece395c2adeb5"
    elif name=="three_nonconjugate_joins":x["GAF4_mixed_type3_exact_bridge"]["self_P3_substitute_hash_rejected"]="three-nonconjugate-joins"
    elif name=="noncollision_rebound":
        r=x["GAF3_stabilizers_and_noncollision"]["fourier_formal_and_evaluated_orbits"]["rplus"]
        r["modular_distinct_value_count"]=79;r["sorted_values_sha256"]="1"*64
    elif name=="diamond_degree":x["GAF5_fixed_field_diamond"]["degrees_A40_B80_M160_Fplus320"][0]=41
    elif name=="diamond_join":x["GAF5_fixed_field_diamond"]["generated_Splus_N_equals_Tplus"]=False
    elif name=="relative_discriminant":x["GAF6_global_arithmetic"]["diamond_relative_discriminant_norm_vectors"]["d_B80_over_A40"][0]+=1
    elif name=="global_sign":x["GAF6_global_arithmetic"]["fields"]["C3"]["discriminant_sign"]=1
    elif name=="drop_branch":del x["GAF7_both_local_branches_and_ideal_laws"]["absolute_local_tables"]["ToM206"]
    elif name=="branch_select":x["GAF7_both_local_branches_and_ideal_laws"]["branch_selected"]=True
    elif name=="ideal_law":x["GAF7_both_local_branches_and_ideal_laws"]["all_primewise_ideal_laws"]=False
    elif name=="bad_euler":x["scope_nonclaims"]["bad_artin_euler_claimed"]=True
    elif name=="release_claim":x["status"]["release_status"]="RELEASED"
    elif name=="authority_tree":x["authority"]["release"]["tree"]="0"*40
    elif name=="pilot_authority":x["authority"]["runtime_pilot_dependencies"]=["pilot.json"]
    elif name=="self_consistent_label_rebound":
        c=x["GAF3_stabilizers_and_noncollision"]["product_form_mixed_base_A_B_resolvents"]["carriers"]["E1"]
        c["right_coset_label_vector_sha256"]="2"*64;c["carrier_spec"]["right_coset_label_vector_sha256"]="2"*64;c["carrier_spec_sha256"]=H(c["carrier_spec"])
    elif name=="unknown_top":x["unknown"]=0
    else:raise Reject("unknown mutation")
    x["payload_sha256"]=payload(x)
    return x

def mutation_suite(doc:dict[str,Any],authority:dict[str,Any])->tuple[dict[str,Any],dict[str,Any]]:
    targeted=["marker_removal","content_two","coset_side","label_hash","exact_division","R0_nonzero","rank_drop","subgroup_hash","mixed_count","Tmix_hash_only","self_P3_substitution","three_nonconjugate_joins","noncollision_rebound","diamond_degree","diamond_join","relative_discriminant","global_sign","drop_branch","branch_select","ideal_law","self_consistent_label_rebound"]
    firewall=["bad_euler","release_claim","authority_tree","pilot_authority","unknown_top"]
    def run(names:list[str])->dict[str,Any]:
        passed=[]
        for name in names:
            if not expect_bad(lambda name=name:surface(mutate(doc,name),authority)):raise Reject("semantic mutation survived")
            passed.append(name)
        return {"passed":len(passed),"total":len(names),"families":passed}
    return run(targeted),run(firewall)

def full_recomputation_mutations(doc:dict[str,Any],bundle:dict[str,Any])->dict[str,Any]:
    docs=bundle["docs"];ctx=bundle["ctx"];types=bundle["types"]
    probes=[
      ("family_02_carrier_content_action_division","marker_removal",lambda x:check_product_carriers(ctx,types,docs["alpha"],x)),
      ("family_03_DAG_R0","R0_nonzero",lambda x:check_fourier(ctx,docs,x)),
      ("family_04_subgroups","subgroup_hash",lambda x:check_fourier(ctx,docs,x)),
      ("family_05_mixed_counts_types","mixed_count",lambda x:mixed_rebuild(ctx,x)),
      ("family_06_P3_substitution","self_P3_substitution",lambda x:check_diamond(ctx,types,x)),
      ("family_06_stale_three_nonconjugate_joins","three_nonconjugate_joins",lambda x:check_diamond(ctx,types,x)),
      ("family_07_modular_noncollision","noncollision_rebound",lambda x:check_fourier(ctx,docs,x)),
      ("family_08_diamond","diamond_join",lambda x:check_diamond(ctx,types,x)),
      ("family_09_global_arithmetic","global_sign",lambda x:check_arithmetic(ctx,types,x)),
      ("family_10_both_local_branches","branch_select",lambda x:check_arithmetic(ctx,types,x)),
      ("family_12_self_consistent_label_spec_payload_rebound","self_consistent_label_rebound",lambda x:check_product_carriers(ctx,types,docs["alpha"],x)),
    ]
    passed=[]
    for label,mutation,fn in probes:
        if not expect_bad(lambda mutation=mutation,fn=fn:fn(mutate(doc,mutation))):raise Reject("full semantic mutation recomputation survived")
        passed.append(label)
    return {"passed":len(passed),"total":len(probes),"families":passed,"each_family_2_through_10_covered":True,"each_invoked_independent_semantic_reconstruction":True}

def scope_suite(doc:dict[str,Any],authority:dict[str,Any])->dict[str,Any]:
    leaves=[k for k,v in doc["scope_nonclaims"].items() if type(v) is bool and v is False]
    if len(leaves)!=30:raise Reject("scope leaf count")
    passed=[]
    for leaf in leaves:
        x=copy.deepcopy(doc);x["scope_nonclaims"][leaf]=True;x["payload_sha256"]=payload(x)
        if not expect_bad(lambda x=x:surface(x,authority)):raise Reject("true scope leaf survived")
        passed.append(leaf)
    return {"passed":30,"total":30,"families":sorted(passed)}

def make_attestation(doc:dict[str,Any],evidence_path:Path,stage:Path,stage_identity:tuple[int,int,int,int])->dict[str,Any]:
    evidence_before=read_guarded(evidence_path,25_000_000) if os.path.lexists(evidence_path) else None
    if evidence_before is not None and stat.S_IMODE(evidence_before[1]["filesystem_identity"]["mode"])!=0o644:raise Reject("attestation evidence mode")
    runtime_before=runtime_input_snapshot()
    assert_stage(stage,stage_identity);authority,bundle=full_check(doc);assert_stage(stage,stage_identity)
    parser_result=parser_suite();path_result=path_suite(evidence_path);targeted,hostile=mutation_suite(doc,authority)
    targeted["full_semantic_recomputations"]=full_recomputation_mutations(doc,bundle)
    hostile["all_30_false_scope_leaves_rejected"]=scope_suite(doc,authority)
    source,_=read_guarded(Path(__file__).resolve(strict=True),2_000_000)
    forbidden=b"import"+b" c61_"+b"resolvent"
    if forbidden in source:raise Reject("producer import boundary")
    authority_after,_=bind_inputs();assert_stage(stage,stage_identity)
    if authority_after!=authority:raise Reject("authority/formal/source changed around checker")
    if runtime_input_snapshot()!=runtime_before:raise Reject("installed authority/source/results identity changed around checker")
    if evidence_before is None:
        if os.path.lexists(evidence_path):raise Reject("absent attestation leaf appeared during checker")
    elif read_guarded(evidence_path,25_000_000)!=evidence_before:
        raise Reject("existing attestation evidence changed during checker")
    return {"schema_id":"hcs-c61-resolvent-checker-attestation-v1","candidate_payload_sha256":doc["payload_sha256"],"checker_source_sha256":authority["source_files"]["checker"]["sha256"],"independent_semantic_checks":["immutable_P60_Git_objects","installed_formal_exact15","36-row_source_groups","mixed_12_rows_8_types","14_marker_product_carriers","Fourier_R0_rank3_orbits_S_T","mixed_type3_exact_Tplus","A40_B80_M160_Fplus_diamond","global_signatures_discriminants","both_D3_local_tables","primewise_ideal_complementarity"],"hostile_mutations_rejected":hostile,"targeted_semantic_mutations_rejected":targeted,"strict_parser_cases_rejected":parser_result,"path_toctou_cases_rejected":path_result,"no_producer_import":True,"status":"PASS"}

def final_check(doc:dict[str,Any],evidence_path:Path,stage:Path,stage_identity:tuple[int,int,int,int])->dict[str,Any]:
    if type(doc) is not dict or set(doc)!=TOP:raise Reject("final top schema")
    if doc["payload_sha256"]!=payload(doc):raise Reject("final payload")
    att=doc.get("independence_contract",{}).get("checker_attestation")
    candidate=copy.deepcopy(doc)
    candidate["independence_contract"]["checker_attestation"]=None
    candidate["independence_contract"]["checker_attestation_two_run_equal"]=False
    candidate["status"]["resolver_component_status"]="PRODUCER_PASS_CHECKER_PENDING"
    candidate["payload_sha256"]=payload(candidate)
    expected=make_attestation(candidate,evidence_path,stage,stage_identity)
    if att!=expected or doc["independence_contract"]["checker_attestation_two_run_equal"] is not True or doc["status"]["resolver_component_status"]!="RESOLVER_COMPONENT_PASS":raise Reject("final checker attestation")
    return {"schema_id":"hcs-c61-resolvent-final-check-v1","evidence_payload_sha256":doc["payload_sha256"],"candidate_payload_sha256":candidate["payload_sha256"],"checker_status":"PASS","resolver_component_status":"RESOLVER_COMPONENT_PASS","release_status":"NOT_RELEASED"}

def attest_candidate_document(raw:bytes,evidence_path:str|Path)->dict[str,Any]:
    """Public neutral-I/O API for an integrated producer subprocess lane."""
    path,stage,identity=staged_evidence_path(str(evidence_path),None);doc=parse_wire(raw)
    return make_attestation(doc,path,stage,identity)

def validate_full_document(evidence_path:str|Path)->dict[str,Any]:
    """Public full-document validator; reconstructs all resolver semantics."""
    path,stage,identity=staged_evidence_path(str(evidence_path),True);before=read_guarded(path,25_000_000)
    doc=parse_wire(before[0]);out=final_check(doc,path,stage,identity)
    if read_guarded(path,25_000_000)!=before:raise Reject("evidence changed around public validation")
    assert_stage(stage,identity);return out

def cli()->argparse.ArgumentParser:
    p=argparse.ArgumentParser(description="Independently check the C61 resolver component")
    mode=p.add_mutually_exclusive_group(required=True);mode.add_argument("--attest-for",metavar="EVIDENCE");mode.add_argument("--check-existing",metavar="EVIDENCE")
    return p

def main()->None:
    args=cli().parse_args()
    try:
        if args.attest_for:
            path,stage,identity=staged_evidence_path(args.attest_for,None)
            raw=sys.stdin.buffer.read(25_000_001);doc=parse_wire(raw);out=make_attestation(doc,path,stage,identity)
        else:
            path,stage,identity=staged_evidence_path(args.check_existing,True);before=read_guarded(path,25_000_000)
            doc=parse_wire(before[0]);out=final_check(doc,path,stage,identity)
            if read_guarded(path,25_000_000)!=before:raise Reject("evidence changed during CLI replay")
            assert_stage(stage,identity)
        sys.stdout.buffer.write(canon(out)+b"\n")
    except Exception as exc:
        print(f"C61_RESOLVENT_CHECK_FAIL: {exc}",file=sys.stderr);raise SystemExit(1)

if __name__=="__main__":main()
