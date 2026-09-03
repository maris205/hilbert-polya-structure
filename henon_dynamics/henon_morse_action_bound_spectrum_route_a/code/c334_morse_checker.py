#!/usr/bin/env python3
"""Producer-independent structural and mathematical checker for HCS-C334."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from fractions import Fraction
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c334_morse_evidence.json"
DEFAULT_EVAL = ROOT / "evaluations/route_a/HCS-C334/2026-09-03.yaml"
SOURCE = "db2c816b7b6bd450f51f79b91842cb882b0bd773"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EVAL_RAW = "d6bdbb263f89e478bad3b0fb760ae59c400c51df399cf02b28dcea573d04d8c5"
EVAL_SEMANTIC = "243b294744a8fd0ef9ac65480e7fc93dd257b23e238a8d93ded6e1cc07be1e3e"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
PYTHAGOREAN = ((0, 1), (3, 5), (4, 5), (5, 13), (12, 13), (7, 25), (24, 25), (20, 29), (21, 29), (9, 41), (40, 41))


def pairs(items):
    out = {}
    for key, value in items:
        if key in out:
            raise ValueError("duplicate JSON key")
        out[key] = value
    return out


def strict_json(path: Path):
    return json.loads(path.read_text(), object_pairs_hook=pairs,
                      parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))


class UniqueLoader(yaml.SafeLoader):
    pass


UniqueLoader.yaml_implicit_resolvers = {
    key: [(tag, rx) for tag, rx in values if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def yaml_mapping(loader, node, deep=False):
    out = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("merge forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in out:
            raise ValueError("duplicate or non-string YAML key")
        out[key] = loader.construct_object(value_node, deep=deep)
    return out


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, yaml_mapping)


def strict_yaml(path: Path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML aliases forbidden")
    return yaml.load(raw, Loader=UniqueLoader)


def semantic_hash(value) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def payload_hash(data: dict) -> str:
    body = dict(data); body.pop("payload_sha256", None)
    return semantic_hash(body)


def leaves(value) -> int:
    if type(value) is dict:
        return sum(leaves(item) for item in value.values())
    if type(value) is list:
        return sum(leaves(item) for item in value)
    return 1


def q(text: str) -> Fraction:
    if type(text) is not str or not re.fullmatch(r"-?(?:0|[1-9][0-9]*)(?:/[1-9][0-9]*)?", text):
        raise AssertionError("noncanonical rational syntax")
    value = Fraction(text)
    rendered = str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"
    if rendered != text:
        raise AssertionError("nonreduced rational")
    return value


def choose(top: Fraction, count: int) -> Fraction:
    value = Fraction(1)
    for j in range(1, count+1):
        value = value*(top-j+1)/j
    return value


def expected_laguerre(n: int, alpha: Fraction) -> list[Fraction]:
    factorial = 1
    out = []
    for power in range(n+1):
        if power:
            factorial *= power
        out.append(((-1)**power)*choose(n+alpha, n-power)/factorial)
    return out


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C334 checker refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_EVAL)
    args = parser.parse_args()
    data = strict_json(args.evidence); evaluation = strict_yaml(args.evaluation); checks = 0
    if hashlib.sha256(args.evaluation.read_bytes()).hexdigest() != EVAL_RAW or semantic_hash(evaluation) != EVAL_SEMANTIC:
        raise AssertionError("evaluation digest")
    if payload_hash(data) != data.get("payload_sha256"):
        raise AssertionError("payload digest")
    checks += 3

    top = {"schema","candidate_id","obstruction_id","evaluation_date","fixed_epoch","source_commit","scope_literal","evaluator","evaluation_lock","model","theorem_contract","classical_rows","bound_count_rows","bound_level_rows","threshold_rows","boundary_atlas","collision_boundary","route_a","scope_flags","nonclaims","references","enumeration","payload_sha256"}
    if type(data) is not dict or set(data) != top:
        raise AssertionError("evidence schema")
    if tuple(data[k] for k in ("schema","candidate_id","obstruction_id","evaluation_date","fixed_epoch","source_commit","scope_literal")) != ("hcs-c334-morse-action-spectrum-v1","HCS-C334","HEN-O318","2026-09-03",1788393600,SOURCE,SCOPE):
        raise AssertionError("identity")
    if data["evaluator"] != {"authority":"flow_systems/skills/route-a-evaluator.md","version":"0.2.0","sha256":EVALUATOR}:
        raise AssertionError("evaluator")
    if data["evaluation_lock"] != {"relative_path":"evaluations/route_a/HCS-C334/2026-09-03.yaml","raw_sha256":EVAL_RAW,"semantic_sha256":EVAL_SEMANTIC}:
        raise AssertionError("evaluation lock")
    expected_model = {
        "classical":"H=p^2/(2m)+D(exp(-2ax)-2exp(-ax)), with m,D,a>0",
        "quantum":"the Friedrichs Schrödinger realization on L2(R), with hbar>0",
        "dimensionless_coupling":"lambda=sqrt(2mD)/(a hbar)",
        "action_normalization":"J(E)=(1/(2pi)) integral over the closed energy orbit of p dx",
    }
    expected_theorem = {
        "classical_action":"for -D<E<0, J=sqrt(2mD)/a times (1-sqrt(-E/D))",
        "classical_period":"for -D<E<0, T=2pi/(a sqrt(-2E/m)) and dJ/dE=T/(2pi)",
        "bound_spectrum":"E_n=-(a^2 hbar^2/(2m))(lambda-n-1/2)^2 exactly for integers n>=0 with n<lambda-1/2",
        "eigenfunctions":"z^(lambda-n-1/2) exp(-z/2) L_n^(2lambda-2n-1)(z), z=2lambda exp(-ax), up to normalization",
        "spectral_boundary":"the essential spectrum is [0,infinity), there are no nonnegative L2 eigenfunctions, and equality at n=lambda-1/2 is a non-L2 zero-energy threshold state",
        "completeness":"the displayed negative levels are all and only the L2 point spectrum",
    }
    if data["model"] != expected_model or data["theorem_contract"] != expected_theorem:
        raise AssertionError("model/theorem literal")
    static_hashes={"boundary_atlas":"fe46dca50af9dd886609f66e978e56dd3dbcba369c48025f6df476b52175aea9","collision_boundary":"34d03198a7f1036925d9acbdfb92b722c562ea2226edcc3148993769c8e86cd0","nonclaims":"84b9a00d608b633629ce5118d709c97ede5ad870141c2ded5998e28016b11c53","references":"490936793a60adcf8d1910aafbf82a3ed837d266214c8477154f98ee4a06bd4a"}
    if any(semantic_hash(data[k])!=v for k,v in static_hashes.items()):
        raise AssertionError("static boundary/source lock")
    route = {"tuple":["A0_FAIL","A1_PASS_ANALYTIC","A2_FAIL","A3_FAIL","A4_NATURAL_QUANTIZATION"],"overall":"ROUTE_A_REJECTED","route_b_invocation_allowed":False}
    flag_keys={"claims_target_arithmetic_local_data","claims_target_euler_factors","claims_root_number","claims_automorphy","claims_target_divisor_or_counting_law","claims_target_functional_equation","claims_target_zero_match","claims_hilbert_polya_operator","invokes_route_b"}
    if data["route_a"] != route or set(data["scope_flags"])!=flag_keys or any(type(v) is not bool or v for v in data["scope_flags"].values()):
        raise AssertionError("route firewall")
    checks += 10

    eval_top = {"schema","candidate_id","title","evaluation_date","source_commit","fixed_epoch","scope_literal","evaluator_authority","evaluator_version","evaluator_authority_sha256","obstruction_id","candidate_definition","family","phase_space","dynamics","parameters","parameter_provenance","arithmetic_origin","clock","normalization","determinant_convention","orbit_cutoff","precision","training_data","forbidden_data","artifact_paths","a0","a1","a2","a3","a4","tuple","overall_verdict","route_b_invocation_allowed","route_b_lock_reason","scope_flags","theorem_status","finite_evidence_role","source_owner_tokens"}
    if type(evaluation) is not dict or set(evaluation) != eval_top:
        raise AssertionError("evaluation schema")
    layer_keys = {"verdict","evidence_status","strongest_evidence","strongest_failure"}
    if any(type(evaluation[k]) is not dict or set(evaluation[k]) != layer_keys for k in ("a0","a1","a2","a3","a4")):
        raise AssertionError("evaluation layers")
    if (evaluation["candidate_id"],evaluation["obstruction_id"],evaluation["evaluation_date"],evaluation["source_commit"],evaluation["fixed_epoch"],evaluation["scope_literal"],evaluation["evaluator_authority"],evaluation["evaluator_version"],evaluation["evaluator_authority_sha256"],evaluation["artifact_paths"],evaluation["tuple"],evaluation["overall_verdict"],evaluation["route_b_invocation_allowed"],evaluation["scope_flags"],evaluation["theorem_status"],evaluation["finite_evidence_role"],evaluation["source_owner_tokens"]) != ("HCS-C334","HEN-O318","2026-09-03",SOURCE,1788393600,SCOPE,"flow_systems/skills/route-a-evaluator.md","0.2.0",EVALUATOR,["results/c334_morse_evidence.json","THEOREM_PACKAGE.md","paper/main.pdf"],route["tuple"],"ROUTE_A_REJECTED",False,data["scope_flags"],"PROVABLE_AS_STATED","convention and implementation receipt, not proof",["10.1103/PhysRev.34.57","https://dlmf.nist.gov/18.5","https://dlmf.nist.gov/13.14"]):
        raise AssertionError("evaluation semantics")
    if [evaluation[k]["verdict"] for k in ("a0","a1","a2","a3","a4")] != route["tuple"]:
        raise AssertionError("evaluation verdicts")
    if [evaluation[k]["evidence_status"] for k in ("a0","a1","a2","a3","a4")] != ["STOP_SCOPED","PROVED","STOP_SCOPED","STOP_SCOPED","PROVED"]:
        raise AssertionError("evaluation statuses")
    checks += 40

    rows = data["classical_rows"]
    keys = {"row_id","delta","sigma","energy_over_D","left_y_turn","right_y_turn","action_over_sqrt_2mD_over_a","period_times_a_sqrt_D_over_2m_over_pi"}
    if len(rows) != len(PYTHAGOREAN): raise AssertionError("classical count")
    for index, (row, (dn,h)) in enumerate(zip(rows,PYTHAGOREAN),1):
        if type(row) is not dict or set(row) != keys: raise AssertionError("classical schema")
        delta=Fraction(dn,h); sigma=Fraction(int((h*h-dn*dn)**0.5),h)
        expected=(f"classical-{index:02d}",delta,sigma,-sigma*sigma,1+delta,1-delta,1-sigma,1/sigma)
        actual=(row["row_id"],q(row["delta"]),q(row["sigma"]),q(row["energy_over_D"]),q(row["left_y_turn"]),q(row["right_y_turn"]),q(row["action_over_sqrt_2mD_over_a"]),q(row["period_times_a_sqrt_D_over_2m_over_pi"]))
        if actual != expected or delta*delta+sigma*sigma != 1: raise AssertionError("classical identity")
        checks += 10

    lambdas=[Fraction(k,4) for k in range(1,33)]
    counts=data["bound_count_rows"]
    if len(counts)!=len(lambdas): raise AssertionError("count rows")
    expected_level_coords=[]; expected_threshold=[]
    for row,lam in zip(counts,lambdas):
        if type(row) is not dict or set(row)!={"lambda","bound_state_count"}: raise AssertionError("count schema")
        allowed=[n for n in range(16) if n<lam-Fraction(1,2)]
        if (q(row["lambda"]),row["bound_state_count"])!=(lam,len(allowed)): raise AssertionError("bound count")
        expected_level_coords.extend((lam,n) for n in allowed)
        if (lam-Fraction(1,2)).denominator==1 and lam>=Fraction(1,2): expected_threshold.append(lam)
        checks+=3
    levels=data["bound_level_rows"]
    level_keys={"lambda","n","decay_exponent","energy_over_scale","laguerre_alpha","laguerre_coefficients_low_to_high","node_count"}
    if len(levels)!=len(expected_level_coords): raise AssertionError("level count")
    for row,(lam,n) in zip(levels,expected_level_coords):
        if type(row) is not dict or set(row)!=level_keys: raise AssertionError("level schema")
        exponent=lam-n-Fraction(1,2); alpha=2*exponent
        coeffs=[q(x) for x in row["laguerre_coefficients_low_to_high"]]
        if (q(row["lambda"]),row["n"],q(row["decay_exponent"]),q(row["energy_over_scale"]),q(row["laguerre_alpha"]),row["node_count"],coeffs)!=(lam,n,exponent,-exponent*exponent,alpha,n,expected_laguerre(n,alpha)):
            raise AssertionError("level identity")
        if exponent<=0 or len(coeffs)!=n+1: raise AssertionError("L2/degree")
        checks += 8+len(coeffs)
    thresholds=data["threshold_rows"]
    if len(thresholds)!=len(expected_threshold): raise AssertionError("threshold count")
    for row,lam in zip(thresholds,expected_threshold):
        if type(row) is not dict or set(row)!={"lambda","formal_n","decay_exponent","energy_over_scale","l2_status"}: raise AssertionError("threshold schema")
        if (q(row["lambda"]),row["formal_n"],q(row["decay_exponent"]),q(row["energy_over_scale"]),row["l2_status"])!=(lam,int(lam-Fraction(1,2)),Fraction(0),Fraction(0),"excluded_nonintegrable_constant_tail"):
            raise AssertionError("threshold")
        checks+=6

    expected_enum={"classical_rows":len(rows),"bound_count_rows":len(counts),"bound_level_rows":len(levels),"threshold_rows":len(thresholds),"laguerre_coefficients":sum(len(r["laguerre_coefficients_low_to_high"]) for r in levels)}
    if type(data["enumeration"]) is not dict or set(data["enumeration"])!=set(expected_enum)|{"audited_leaf_count"}:
        raise AssertionError("enumeration schema")
    if any(data["enumeration"][k]!=v for k,v in expected_enum.items()) or data["enumeration"]["audited_leaf_count"]!=leaves({k:v for k,v in data.items() if k not in ("enumeration","payload_sha256")})+leaves(data["enumeration"]):
        raise AssertionError("enumeration")
    checks+=10
    print(f"C334 independent checker: PASS ({checks} checks)")


if __name__ == "__main__":
    main()
