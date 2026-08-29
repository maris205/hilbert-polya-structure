#!/usr/bin/env python3
"""Independent checker for the C232 Duffing energy/separatrix certificate."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import re
import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c232_duffing_evidence.json"
SOURCE_COMMIT = "e1dc522e054c2d0ded74b017bc52c7b016a52c59"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
PARAMETERS = [("hardening", F(1), F(1), [F(1, 20), F(1, 5), F(1, 2), F(1)]), ("pure_quartic", F(0), F(1), [F(1, 20), F(1, 5), F(1, 2), F(1)]), ("double_well_unit", F(-1), F(1), [F(-6, 25), F(-1, 10), F(-1, 100), F(1, 10)]), ("double_well_scaled", F(-2), F(3, 2), [F(-13, 20), F(-1, 3), F(-1, 50), F(1, 5)]), ("stiff_hardening", F(3), F(2), [F(1, 20), F(1, 5), F(1, 2), F(1)])]
NUM_RE = re.compile(r"^-?(?:0|[1-9][0-9]*)(?:\.[0-9]+|[eE][+-]?[0-9]+)$")


def payload_hash(data: dict) -> str:
    body = dict(data); body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def mpq(q: F) -> mp.mpf: return mp.mpf(q.numerator) / q.denominator


def potential(x, d, b): return d*x*x/2 + b*x**4/4


def fmt_close(value, expected, label, check, tol=mp.mpf("4e-52")):
    check(isinstance(value, str) and NUM_RE.fullmatch(value) is not None, label + " syntax")
    check(abs(mp.mpf(value)-expected) <= tol*max(1, abs(expected)), label + " value")


def roots_for(d, b, e):
    disc = d*d + 4*b*e
    if disc < 0: raise AssertionError("invalid energy")
    s = mp.sqrt(max(disc, mp.mpf("0"))); ym=(-d-s)/b; yp=(-d+s)/b
    if d >= 0:
        a=mp.sqrt(yp); return "single_center",1,-a,a,[-a,a]
    if e < 0:
        lo,hi=mp.sqrt(ym),mp.sqrt(yp); return "double_inner",2,lo,hi,[-hi,-lo,lo,hi]
    a=mp.sqrt(yp); return "outer",1,-a,a,[-a,a]


def recompute(d,b,e,left,right):
    mid=(left+right)/2; half=(right-left)/2
    def rem(th):
        x=mid+half*mp.sin(th); return max(e-potential(x,d,b),mp.mpf("0"))
    def pfun(th):
        c=mp.cos(th)
        if abs(c)<mp.mpf("1e-34") or rem(th)<=0: return mp.mpf("0")
        return mp.sqrt(2)*half*c/mp.sqrt(rem(th))
    def ifun(th):
        c=mp.cos(th)
        return mp.sqrt(2*rem(th))*half*c/mp.pi
    return (mp.re(mp.quad(pfun,[-mp.pi/2,0,mp.pi/2])), mp.re(mp.quad(ifun,[-mp.pi/2,0,mp.pi/2])))


def quick_preflight(data: dict) -> None:
    """Cheap hostile-mutation preflight; full checker remains authoritative."""
    assert set(data)=={"schema","candidate_id","evaluation_date","source_commit","fixed_epoch","scope_literal","evaluator","headline","frozen_object","theorem","regression","exact_identities","route_a","scope_flags","citations","nonclaims","payload_sha256"}
    assert data.get("schema") == "hcs-c232-duffing-separatrix-v1"
    assert data.get("candidate_id") == "HCS-C232"
    assert data.get("source_commit") == SOURCE_COMMIT
    assert data.get("fixed_epoch") == 1787875200
    assert data.get("scope_literal") == SCOPE
    assert data.get("evaluation_date") == "2026-08-29"
    assert data.get("evaluator") == {"path":"flow_systems/skills/route-a-evaluator.md","version":"0.2.0","sha256":EVALUATOR_SHA256}
    assert data.get("payload_sha256") == payload_hash(data)
    assert data.get("route_a", {}).get("tuple") == ["A0_FAIL","A1_WEAK","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"]
    assert data.get("route_a", {}).get("overall") == "ROUTE_A_REJECTED"
    assert data.get("route_a", {}).get("route_b_invocation_allowed") is False
    assert all(v is False for v in data.get("scope_flags", {}).values())
    assert len(data.get("regression", {}).get("energy_rows", [])) == 20
    by_case={s[0]:s for s in PARAMETERS}
    for r in data["regression"]["energy_rows"]:
        assert set(r)=={"case_id","delta","beta","energy","regime","component_count","selected_interval","all_turning_roots","period","action","turning_residual_left","turning_residual_right","saddle_rate","linear_period","quartic_scaling_invariant"}
        assert r["case_id"] in by_case
        _,dq,bq,energies=by_case[r["case_id"]]; e=F(r["energy"]); assert r["delta"]==str(dq) and r["beta"]==str(bq) and e in energies
        d,b,en=mpq(dq),mpq(bq),mpq(e); reg,comp,left,right,roots=roots_for(d,b,en)
        assert r["regime"]==reg and r["component_count"]==comp
        assert len(r["selected_interval"])==2 and float(r["selected_interval"][0]) < float(r["selected_interval"][1])
        assert abs(float(r["selected_interval"][0])-float(left)) < 1e-10 and abs(float(r["selected_interval"][1])-float(right)) < 1e-10
        assert len(r["all_turning_roots"])==len(roots) and float(r["period"])>0 and float(r["action"])>0
        assert abs(float(r["turning_residual_left"])) < 1e-8 and abs(float(r["turning_residual_right"])) < 1e-8
    for m in data.get("regression",{}).get("parameter_cases",[]): assert set(m)=={"case_id","delta","beta","energy_values","saddle_or_center_rate","well_minimum"}
    for c in data.get("citations",[]): assert set(c)=={"key","claim","title","authors","venue","date","doi"} and c["doi"].startswith("10.")


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--evidence",type=Path,default=DEFAULT_EVIDENCE); ap.add_argument("--quick",action="store_true"); args=ap.parse_args(); data=json.loads(args.evidence.read_text())
    if args.quick:
        quick_preflight(data)
        print("C232 quick hostile preflight: PASS")
        return
    checks=0
    def check(ok,label):
        nonlocal checks; checks+=1
        if not ok: raise AssertionError(label)
    def exact(a,b,label): check(type(a) is type(b),label+" type"); check(a==b,label)
    top={"schema","candidate_id","evaluation_date","source_commit","fixed_epoch","scope_literal","evaluator","headline","frozen_object","theorem","regression","exact_identities","route_a","scope_flags","citations","nonclaims","payload_sha256"}
    check(set(data)==top,"top-level closure"); check(data["payload_sha256"]==payload_hash(data),"payload hash")
    exact(data["schema"],"hcs-c232-duffing-separatrix-v1","schema"); exact(data["candidate_id"],"HCS-C232","candidate"); exact(data["evaluation_date"],"2026-08-29","date"); exact(data["source_commit"],SOURCE_COMMIT,"source commit"); exact(data["fixed_epoch"],1787875200,"epoch"); exact(data["scope_literal"],SCOPE,"scope")
    exact(data["evaluator"],{"path":"flow_systems/skills/route-a-evaluator.md","version":"0.2.0","sha256":EVALUATOR_SHA256},"evaluator")
    check(data["route_a"]["tuple"]==["A0_FAIL","A1_WEAK","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"],"route tuple"); check(data["route_a"]["overall"]=="ROUTE_A_REJECTED" and data["route_a"]["route_b_invocation_allowed"] is False,"route verdict"); check(all(v is False for v in data["scope_flags"].values()),"scope firewall")
    check(data["regression"]["case_count"]==5 and data["regression"]["energy_row_count"]==20,"counts"); check(data["regression"]["working_digits"]==80 and data["regression"]["serialized_digits"]==62,"precision")
    check(len(data["regression"]["parameter_cases"])==5 and len(data["regression"]["energy_rows"])==20,"ledger lengths")
    mp.mp.dps=80
    for i,(meta,spec) in enumerate(zip(data["regression"]["parameter_cases"],PARAMETERS)):
        cid,dq,bq,energies=spec; d,b=mpq(dq),mpq(bq)
        check(set(meta)=={"case_id","delta","beta","energy_values","saddle_or_center_rate","well_minimum"},f"case {i} keys"); exact(meta["case_id"],cid,f"case {i} id"); exact(meta["delta"],str(dq),f"case {i} delta"); exact(meta["beta"],str(bq),f"case {i} beta"); exact(meta["energy_values"],[str(x) for x in energies],f"case {i} energies")
        rate=mp.sqrt(-d) if d<0 else mp.sqrt(d) if d>0 else mp.mpf("0"); vmin=-d*d/(4*b) if d<0 else mp.mpf("0")
        fmt_close(meta["saddle_or_center_rate"],rate,f"case {i} rate",check); fmt_close(meta["well_minimum"],vmin,f"case {i} minimum",check)
    by_case={s[0]:s for s in PARAMETERS}; pure=[]
    for i,r in enumerate(data["regression"]["energy_rows"]):
        check(set(r)=={"case_id","delta","beta","energy","regime","component_count","selected_interval","all_turning_roots","period","action","turning_residual_left","turning_residual_right","saddle_rate","linear_period","quartic_scaling_invariant"},f"row {i} keys")
        cid=r["case_id"]; check(cid in by_case,f"row {i} case"); _,dq,bq,energies=by_case[cid]; e=F(r["energy"]); exact(r["delta"],str(dq),f"row {i} delta"); exact(r["beta"],str(bq),f"row {i} beta"); check(e in energies,f"row {i} energy")
        d,b,en=mpq(dq),mpq(bq),mpq(e); reg,comp,left,right,roots=roots_for(d,b,en); exact(r["regime"],reg,f"row {i} regime"); exact(r["component_count"],comp,f"row {i} components")
        check(len(r["selected_interval"])==2 and len(r["all_turning_roots"])==len(roots),f"row {i} root lengths")
        fmt_close(r["selected_interval"][0],left,f"row {i} left",check); fmt_close(r["selected_interval"][1],right,f"row {i} right",check)
        for j,(v,x) in enumerate(zip(r["all_turning_roots"],roots)): fmt_close(v,x,f"row {i} root {j}",check)
        # Independent endpoint treatment changes the last ~30 digits of the
        # quadrature; the ledger keeps 62 digits, so use a conservative
        # cross-implementation tolerance here.
        period,action=recompute(d,b,en,left,right); fmt_close(r["period"],period,f"row {i} period",check,mp.mpf("2e-30")); fmt_close(r["action"],action,f"row {i} action",check,mp.mpf("2e-30")); fmt_close(r["turning_residual_left"],potential(left,d,b)-en,f"row {i} residual L",check,mp.mpf("2e-35")); fmt_close(r["turning_residual_right"],potential(right,d,b)-en,f"row {i} residual R",check,mp.mpf("2e-35")); fmt_close(r["saddle_rate"],mp.sqrt(-d) if d<0 else mp.mpf("0"),f"row {i} saddle",check)
        if d>0: fmt_close(r["linear_period"],2*mp.pi/mp.sqrt(d),f"row {i} linear period",check)
        else: check(r["linear_period"] is None,f"row {i} linear null")
        if d==0: pure.append(mp.mpf(r["quartic_scaling_invariant"])); check(r["quartic_scaling_invariant"] is not None,f"row {i} quartic scale")
        else: check(r["quartic_scaling_invariant"] is None,f"row {i} quartic null")
        check(period>0 and action>0 and left<right,f"row {i} positivity")
    for x in pure: check(abs(x-pure[0])<mp.mpf("1e-40"),"quartic scaling constancy")
    check(len(data["exact_identities"])==8,"identity count")
    for c in data["citations"]: check(set(c)=={"key","claim","title","authors","venue","date","doi"},"citation closure"); check(c["doi"].startswith("10."),"citation DOI")
    print(f"C232 independent checker: PASS ({checks} assertions; energy topology, period/action quadratures and separatrix ledger)")
    print("turning roots, Hamiltonian boundaries, scaling law and scope firewall: PASS")


if __name__ == "__main__": main()
