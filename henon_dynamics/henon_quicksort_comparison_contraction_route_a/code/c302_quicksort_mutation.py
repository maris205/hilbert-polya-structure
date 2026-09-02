#!/usr/bin/env python3
"""Hostile semantic/parser mutation suite for HCS-C302."""
from __future__ import annotations

import copy
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

ROOT=Path(__file__).resolve().parents[1]
CHECKER=ROOT/"code/c302_quicksort_checker.py"
EVIDENCE=ROOT/"results/c302_quicksort_evidence.json"
EVALUATION=ROOT/"evaluations/route_a/HCS-C302/2026-09-02.yaml"


def payload_hash(data: dict) -> str:
    body=dict(data); body.pop("payload_sha256",None)
    return hashlib.sha256(json.dumps(body,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()


def canonical(data: dict) -> bytes:
    data["payload_sha256"]=payload_hash(data)
    return (json.dumps(data,sort_keys=True,indent=2,ensure_ascii=False)+"\n").encode()


def run(evidence: Path,evaluation: Path,fast: bool=False):
    command=[sys.executable,str(CHECKER),"--evidence",str(evidence),"--yaml",str(evaluation)]
    if fast: command.append("--skip-exhaustive")
    return subprocess.run(command,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)


def main() -> None:
    baseline=run(EVIDENCE,EVALUATION)
    if baseline.returncode:
        raise AssertionError("baseline checker failed:\n"+baseline.stdout)
    original=json.loads(EVIDENCE.read_text())
    raw=EVIDENCE.read_bytes(); yaml_raw=EVALUATION.read_bytes()
    killed=[]; survived=[]

    semantic=[
        ("candidate",lambda d:d.__setitem__("candidate_id","HCS-C301")),
        ("obstruction",lambda d:d.__setitem__("obstruction_id","HEN-O000")),
        ("source",lambda d:d.__setitem__("source_commit","0"*40)),
        ("epoch-bool",lambda d:d.__setitem__("fixed_epoch",True)),
        ("scope",lambda d:d.__setitem__("scope_literal","OPEN")),
        ("model-input",lambda d:d["model"].__setitem__("input","repeated keys")),
        ("model-cost",lambda d:d["model"].__setitem__("partition_cost","n comparisons")),
        ("pgf-theorem",lambda d:d["theorem"].__setitem__("pgf","wrong")),
        ("mean-theorem",lambda d:d["theorem"].__setitem__("mean","wrong")),
        ("variance-theorem",lambda d:d["theorem"].__setitem__("variance","wrong")),
        ("normalization-theorem",lambda d:d["theorem"].__setitem__("normalization","divide by n")),
        ("m3-theorem",lambda d:d["theorem"].__setitem__("limit_third_moment","0")),
        ("contraction-proof",lambda d:d["proof_certificates"].__setitem__("contraction","factor one")),
        ("positivity-proof",lambda d:d["proof_certificates"].__setitem__("positivity","assumed")),
        ("pgf-cost",lambda d:d["finite_pgf_regression"]["rows"][8]["coefficients"][2].__setitem__("comparisons",999)),
        ("pgf-numerator",lambda d:d["finite_pgf_regression"]["rows"][10]["coefficients"][3].__setitem__("numerator",0)),
        ("pgf-denominator",lambda d:d["finite_pgf_regression"]["rows"][9]["coefficients"][1].__setitem__("denominator",7)),
        ("permutation-count",lambda d:d["finite_pgf_regression"]["rows"][7]["coefficients"][0].__setitem__("permutation_count",0)),
        ("coefficient-count",lambda d:d["finite_pgf_regression"]["rows"][12].__setitem__("coefficient_count",0)),
        ("finite-row-n-bool",lambda d:d["finite_pgf_regression"]["rows"][0].__setitem__("n",False)),
        ("coefficient-count-bool",lambda d:d["finite_pgf_regression"]["rows"][12].__setitem__("coefficient_count",True)),
        ("coefficient-cells-float",lambda d:d["finite_pgf_regression"].__setitem__("coefficient_cells",173.0)),
        ("support",lambda d:d["finite_pgf_regression"]["rows"][11].__setitem__("support_max",1)),
        ("probability-sum",lambda d:d["finite_pgf_regression"]["rows"][6].__setitem__("probability_sum","2")),
        ("raw-mean",lambda d:d["finite_pgf_regression"]["rows"][5].__setitem__("raw_moment_1","0")),
        ("raw-third",lambda d:d["finite_pgf_regression"]["rows"][12].__setitem__("raw_moment_3","1")),
        ("variance",lambda d:d["finite_pgf_regression"]["rows"][9].__setitem__("variance_formula","0")),
        ("third-centered",lambda d:d["finite_pgf_regression"]["rows"][10].__setitem__("third_centered_moment","0")),
        ("normalized-variance",lambda d:d["finite_pgf_regression"]["rows"][8].__setitem__("normalized_variance_n_plus_1","0")),
        ("normalized-third",lambda d:d["finite_pgf_regression"]["rows"][8].__setitem__("normalized_third_centered_n_plus_1","0")),
        ("center-left",lambda d:d["centered_recursion_regression"]["groups"][15]["rows"][4].__setitem__("left_coefficient","1/2")),
        ("center-right",lambda d:d["centered_recursion_regression"]["groups"][16]["rows"][5].__setitem__("right_coefficient","1/2")),
        ("center-toll",lambda d:d["centered_recursion_regression"]["groups"][20]["rows"][0].__setitem__("centered_toll","0")),
        ("center-count",lambda d:d["centered_recursion_regression"].__setitem__("pivot_rows",0)),
        ("center-extra-group",lambda d:d["centered_recursion_regression"]["groups"].append(copy.deepcopy(d["centered_recursion_regression"]["groups"][-1]))),
        ("pivot-size-bool",lambda d:d["centered_recursion_regression"]["groups"][0]["rows"][0].__setitem__("pivot_left_size",False)),
        ("integral-C2",lambda d:d["limit_integrals"].__setitem__("integral_C_squared","0")),
        ("integral-C3",lambda d:d["limit_integrals"].__setitem__("integral_C_cubed","0")),
        ("integral-m3",lambda d:d["limit_integrals"].__setitem__("fixed_point_third_moment","0")),
        ("lower-bound",lambda d:d["limit_integrals"].__setitem__("strict_positive_lower_bound","-1")),
        ("diagnostic",lambda d:d["variance_limit_diagnostics"][3].__setitem__("normalized_variance_decimal_12","0.000000000000")),
        ("route-tuple",lambda d:d["route_a"]["tuple"].__setitem__(4,"A4_FORMAL_HINT")),
        ("route-verdict",lambda d:d["route_a"].__setitem__("overall_verdict","ROUTE_A_ACCEPTED")),
        ("route-b",lambda d:d["route_a"].__setitem__("route_b_invocation_allowed",True)),
        ("scope-flag",lambda d:d["scope_flags"].__setitem__("claims_hilbert_polya_operator",True)),
        ("collision",lambda d:d["collision_boundary"].__setitem__("C291","same")),
        ("source-token",lambda d:d["source_owner_tokens"].__setitem__(0,"fake")),
        ("summary-normalization",lambda d:d["regression_summary"].__setitem__("normalization_denominator","n")),
        ("unknown-key",lambda d:d.__setitem__("unknown",1)),
        ("drop-key",lambda d:d.pop("nonclaims")),
    ]
    json_parser=[
        ("json-duplicate",lambda b:b.replace(b'{\n  "candidate_id"',b'{\n  "candidate_id": "HCS-C302",\n  "candidate_id"',1)),
        ("json-trailing",lambda b:b+b"{}\n"),
        ("json-compact",lambda b:json.dumps(json.loads(b)).encode()),
        ("json-nan",lambda b:b.replace(b'"fixed_epoch": 1788307200',b'"fixed_epoch": NaN',1)),
        ("json-invalid-utf8",lambda b:b+b"\xff"),
        ("json-top-list",lambda b:b"[]\n"),
    ]
    yaml_semantic=[
        ("yaml-candidate",lambda d:d.__setitem__("candidate_id","HCS-C301")),
        ("yaml-source",lambda d:d.__setitem__("source_commit","0"*40)),
        ("yaml-epoch-bool",lambda d:d.__setitem__("fixed_epoch",True)),
        ("yaml-obstruction",lambda d:d.__setitem__("obstruction_id","HEN-O000")),
        ("yaml-normalization",lambda d:d.__setitem__("normalization","divide by n")),
        ("yaml-a1",lambda d:d["a1"].__setitem__("verdict","A1_PASS")),
        ("yaml-a4",lambda d:d["a4"].__setitem__("verdict","A4_FORMAL_HINT")),
        ("yaml-tuple",lambda d:d["tuple"].__setitem__(2,"A2_PASS")),
        ("yaml-route-b",lambda d:d.__setitem__("route_b_invocation_allowed",True)),
        ("yaml-flag",lambda d:d["scope_flags"].__setitem__("claims_root_number",True)),
        ("yaml-source-token",lambda d:d["source_owner_tokens"].__setitem__(1,"fake")),
        ("yaml-unknown",lambda d:d.__setitem__("unknown","x")),
    ]
    yaml_parser=[
        ("yaml-duplicate",lambda b:b+b"candidate_id: HCS-C302\n"),
        ("yaml-anchor",lambda b:b"a: &x y\nb: *x\n"+b),
        ("yaml-merge",lambda b:b"a: &x {v: 1}\nb: {<<: *x}\n"+b),
        ("yaml-nonstring",lambda b:b"1: bad\n"+b),
    ]

    with tempfile.TemporaryDirectory(prefix="c302-mutation-") as folder:
        folder=Path(folder)
        for name,mutate in semantic:
            data=copy.deepcopy(original); mutate(data)
            path=folder/(name+".json"); path.write_bytes(canonical(data))
            result=run(path,EVALUATION,fast=True)
            (killed if result.returncode else survived).append(name if result.returncode else (name,result.stdout))
        for name,mutate in json_parser:
            path=folder/(name+".json"); path.write_bytes(mutate(raw))
            result=run(path,EVALUATION,fast=True)
            (killed if result.returncode else survived).append(name if result.returncode else (name,result.stdout))

        base=yaml.load(EVALUATION.read_text(),Loader=yaml.BaseLoader)
        base["fixed_epoch"]=1788307200; base["route_b_invocation_allowed"]=False
        for key in base["scope_flags"]: base["scope_flags"][key]=False
        for name,mutate in yaml_semantic:
            data=copy.deepcopy(base); mutate(data)
            path=folder/(name+".yaml"); path.write_text(yaml.safe_dump(data,sort_keys=False,allow_unicode=True))
            result=run(EVIDENCE,path,fast=True)
            (killed if result.returncode else survived).append(name if result.returncode else (name,result.stdout))
        for name,mutate in yaml_parser:
            path=folder/(name+".yaml"); path.write_bytes(mutate(yaml_raw))
            result=run(EVIDENCE,path,fast=True)
            (killed if result.returncode else survived).append(name if result.returncode else (name,result.stdout))

    if survived: raise AssertionError(f"surviving mutations: {survived}")
    expected=len(semantic)+len(json_parser)+len(yaml_semantic)+len(yaml_parser)
    if len(killed)!=expected: raise AssertionError("mutation accounting")
    print(f"C302 mutation suite PASS ({len(killed)}/{expected} semantic/parser mutations killed)")
    print("classes=model,PGF,moments,n+1-centering,contraction,m3,route,scope,JSON,YAML")


if __name__=="__main__":
    main()
