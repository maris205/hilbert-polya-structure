#!/usr/bin/env python3
"""Independent analytic receipt reconstruction: no producer import."""
if not __debug__:
    raise RuntimeError("c383 checker refuses optimized Python")
import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
import mpmath as mp
import yaml

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"results/c383_ab_evidence.json"
YAML=ROOT/"evaluations/route_a/HCS-C383/2026-09-05.yaml"
YAML_SHA="bd53ae47f47fa2abf37302c5350d706e1a24153a7da44d9193bb9aad9aeecb14"
EXPECTED_FLAGS={"claims_target_arithmetic_local_data","claims_target_euler_factors","claims_root_number","claims_automorphy","claims_target_divisor_or_counting_law","claims_target_functional_equation","claims_target_zero_match","claims_hilbert_polya_operator","invokes_route_b"}

def canon(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False).encode()
def pairs(rows):
    result={}
    for k,v in rows:
        if k in result:raise ValueError("duplicate JSON key")
        result[k]=v
    return result
def reject(x):raise ValueError("nonfinite JSON")
def strict_json(path):return json.loads(path.read_text(),object_pairs_hook=pairs,parse_constant=reject)
def rational(x):
    assert type(x) is list and len(x)==2 and all(type(y) is int for y in x) and x[1]>0
    value=Fraction(*x)
    assert [value.numerator,value.denominator]==x
    return value

class StrictYAML(yaml.SafeLoader):pass
StrictYAML.yaml_implicit_resolvers={k:[(t,r) for t,r in v if t!="tag:yaml.org,2002:timestamp"] for k,v in yaml.SafeLoader.yaml_implicit_resolvers.items()}
def yamlmap(loader,node,deep=False):
    d={}
    for k,v in node.value:
        if k.tag=="tag:yaml.org,2002:merge":raise ValueError("YAML merge")
        key=loader.construct_object(k,deep=deep)
        if type(key)is not str or key in d:raise ValueError("YAML duplicate/nonstring key")
        d[key]=loader.construct_object(v,deep=deep)
    return d
StrictYAML.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,yamlmap)
def strict_yaml(path):
    raw=path.read_bytes()
    for token in yaml.scan(raw):
        if isinstance(token,(yaml.tokens.AnchorToken,yaml.tokens.AliasToken)):raise ValueError("YAML alias/anchor")
    return yaml.load(raw,Loader=StrictYAML)

def check_yaml_lock():
    raw=YAML.read_bytes();evaluation=strict_yaml(YAML)
    assert hashlib.sha256(raw).hexdigest()==YAML_SHA,"evaluation changed"
    assert type(evaluation)is dict
    assert type(evaluation["evaluation_date"])is str and evaluation["evaluation_date"]=="2026-09-05"
    assert set(evaluation["scope_flags"])==EXPECTED_FLAGS
    assert all(v is False for v in evaluation["scope_flags"].values())
    assert evaluation["route_b_invocation_allowed"] is False
    return raw,evaluation

def check(path):
    data=strict_json(path)
    assert set(data)=={"schema","candidate_id","obstruction_id","source_commit","fixed_epoch","scope_literal","scope_flags","evaluator","route_a_yaml","route_a","channels","gauge_rows","time_reversal_rows","cutoff_rows","heat_rows","cross_section_rows","counts","theorem_boundary","payload_sha256"}
    payload=data.pop("payload_sha256");assert payload==hashlib.sha256(canon(data)).hexdigest()
    assert data["schema"]=="hcs-c383-ab-v1" and data["candidate_id"]=="HCS-C383" and data["obstruction_id"]=="HEN-O367"
    assert data["source_commit"]=="0596f9d680277288225062a6fdd7ad7ce116e01d" and type(data["fixed_epoch"])is int and data["fixed_epoch"]==1788566400
    assert data["scope_literal"]=="NO_BAD_EULER_OR_ROOT_NUMBER"
    assert set(data["scope_flags"])==EXPECTED_FLAGS and all(v is False for v in data["scope_flags"].values())
    assert data["evaluator"]=={"authority":"flow_systems/skills/route-a-evaluator.md","version":"0.2.0","sha256":"6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"}
    raw,evaluation=check_yaml_lock()
    assert data["route_a_yaml"]=={"path":"evaluations/route_a/HCS-C383/2026-09-05.yaml","raw_sha256":YAML_SHA,"semantic_sha256":hashlib.sha256(canon(evaluation)).hexdigest()}
    assert data["route_a"]=={"tuple":["A0_FAIL","A1_FAIL","A2_FAIL","A3_FAIL","A4_UNITARY_OR_SCATTERING_CANDIDATE"],"overall_verdict":"ROUTE_A_REJECTED","route_b_invocation_allowed":False}
    assert data["route_a"]["route_b_invocation_allowed"] is False
    assert evaluation["tuple"]==data["route_a"]["tuple"] and evaluation["route_b_invocation_allowed"] is False
    assert evaluation["scope_flags"]==data["scope_flags"]
    betas=[Fraction(0),Fraction(1,7),Fraction(1,4),Fraction(1,3),Fraction(1,2),Fraction(2,3),Fraction(3,4),Fraction(6,7)]
    assert data["counts"]=={"channels":520,"gauges":680,"time_reversal":8,"cutoffs":520,"heat":6,"cross_section":12}
    assert all(type(v)is int for v in data["counts"].values())
    assert len(data["channels"])==520
    for row,(b,m) in zip(data["channels"],((b,m) for b in betas for m in range(-32,33))):
        assert set(row)=={"beta","m","nu","phase_over_pi","limit_circle"}
        assert rational(row["beta"])==b and type(row["m"])is int and row["m"]==m
        # Piecewise channel reconstruction avoids producer's absolute-difference phase formula.
        order=Fraction(m)-b if m>=1 else b-m
        assert rational(row["nu"])==order
        assert rational(row["phase_over_pi"])==(b if m>=1 else -b)
        assert row["limit_circle"] is (m==0 or (m==1 and b>0))
    assert len(data["gauge_rows"])==680
    for row,(b,n,m) in zip(data["gauge_rows"],((b,n,m) for b in betas for n in range(-2,3) for m in range(-8,9))):
        assert set(row)=={"beta","shift","m","shifted_m","shifted_beta","order"}
        assert all(type(row[k])is int for k in ("shift","m","shifted_m"))
        assert rational(row["beta"])==b and row["shift"]==n and row["m"]==m and row["shifted_m"]==m+n
        assert rational(row["shifted_beta"])==b+n and rational(row["order"])**2==(m+n-rational(row["shifted_beta"]))**2
    assert len(data["time_reversal_rows"])==8
    for row,b in zip(data["time_reversal_rows"],betas):
        assert set(row)=={"beta","position_preserving_TR","required_winding","reflection_K_symmetry"}
        assert rational(row["beta"])==b and rational(row["required_winding"])==2*b
        assert row["position_preserving_TR"] is (b in (0,Fraction(1,2))) and row["reflection_K_symmetry"] is True
    assert len(data["cutoff_rows"])==520
    for row,(b,m) in zip(data["cutoff_rows"],((b,m) for b in betas for m in range(65))):
        assert set(row)=={"beta","M","symmetric_phase_over_pi","shifted_phase_over_pi"}
        assert type(row["M"])is int
        assert rational(row["beta"])==b and row["M"]==m
        assert rational(row["symmetric_phase_over_pi"])==-b and rational(row["shifted_phase_over_pi"])==0
    expected_heat=[(0,1,1,1),(Fraction(1,7),1,2,1),(Fraction(1,2),2,1,Fraction(1,2)),(Fraction(2,3),Fraction(1,2),Fraction(3,2),2),(3,1,2,Fraction(3,2)),(Fraction(7,2),2,2,1)]
    assert len(data["heat_rows"])==6
    with mp.workdps(65):
        for row,expected in zip(data["heat_rows"],expected_heat):
            assert set(row)=={"nu","r","rp","t","radial_heat_kernel"}
            params=[rational(row[k]) for k in ("nu","r","rp","t")];assert tuple(params)==expected
            nu,r,rp,t=[mp.mpf(x.numerator)/x.denominator for x in params]
            spectral=mp.quad(lambda k:mp.exp(-t*k*k)*mp.besselj(nu,k*r)*mp.besselj(nu,k*rp)*k,[0,1,3,8,mp.inf])
            assert type(row["radial_heat_kernel"])is str
            assert abs(spectral-mp.mpf(row["radial_heat_kernel"]))<mp.mpf("1e-39")
        assert len(data["cross_section_rows"])==12
        expected_angles=[Fraction(1,4),Fraction(1,2),Fraction(1),Fraction(3,2)]
        for row,(b,theta) in zip(data["cross_section_rows"],((b,t) for b in (Fraction(1,7),Fraction(1,2),Fraction(6,7)) for t in expected_angles)):
            assert set(row)=={"beta","theta_over_pi","k","cross_section"}
            assert rational(row["beta"])==b and rational(row["theta_over_pi"])==theta and rational(row["k"])==1
            flux=mp.mpf(b.numerator)/b.denominator;angle=mp.pi*theta.numerator/theta.denominator
            amplitude=-mp.sin(mp.pi*flux)*(mp.cot(angle/2)+1j)/mp.sqrt(2j*mp.pi)
            assert type(row["cross_section"])is str and abs(abs(amplitude)**2-mp.mpf(row["cross_section"]))<mp.mpf("1e-38")
    assert data["theorem_boundary"]=="Friedrichs extension only; all-channel completeness is analytic; finite decimal checks are numerical regression, not interval certification; no ordinary global heat trace or ordinary Fredholm scattering determinant; no Hilbert-Polya operator and no Route B"
    return payload

def main():
    p=argparse.ArgumentParser();p.add_argument("path",type=Path,nargs="?",default=OUT);p.add_argument("--yaml-only",action="store_true");a=p.parse_args()
    if a.yaml_only:
        check_yaml_lock();print("C383 locked strict YAML PASS");return
    print("C383 independent checker PASS",check(a.path))
if __name__=="__main__":main()
