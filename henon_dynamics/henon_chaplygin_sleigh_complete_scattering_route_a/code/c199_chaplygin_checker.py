#!/usr/bin/env python3
"""Independent exact-schema/high-precision checker for C199."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import mpmath as mp


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c199_chaplygin_evidence.json"
SOURCE_COMMIT = "d1e58971e570b855488009af384995702ddb887b"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
HEADLINE = "The signed-offset Chaplygin sleigh admits a complete all-parameter heteroclinic scattering and reconstruction theorem with singular measure and a sharp zero-offset recurrence boundary"


def payload_hash(data: dict) -> str:
    body = dict(data); body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def qmp(s: str) -> mp.mpf:
    q = F(s); return mp.mpf(q.numerator)/q.denominator


def main() -> None:
    parser = argparse.ArgumentParser(); parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    data = json.loads(parser.parse_args().evidence.read_text())
    mp.mp.dps = 100
    assertions = 0
    def check(c, msg):
        nonlocal assertions; assertions += 1
        if not c: raise AssertionError(msg)
    def keys(obj, expected, where):
        check(isinstance(obj, dict), where+" type"); check(set(obj) == set(expected), where+" keys")

    keys(data, {"schema","candidate_id","evaluation_date","source_commit","scope_literal","evaluator","headline","frozen_object","theorem","regression","summary","route_a","scope_flags","citations","nonclaims","payload_sha256"}, "top")
    keys(data["evaluator"], {"path","version","sha256"}, "evaluator")
    keys(data["frozen_object"], {"configuration","parameters","body_velocities","equations","energy","convention_warning"}, "frozen")
    keys(data["theorem"], {"nonzero_offset_solution","constants","scattering","reconstruction","stability","poisson","measure","reversor","zero_offset"}, "theorem")
    keys(data["regression"], {"heteroclinic_cases","zero_offset_cases"}, "regression")
    keys(data["summary"], {"parameter_families","heteroclinic_cases","sample_states","positive_a_cases","negative_a_cases","zero_offset_cases","precision_decimal_digits"}, "summary")
    keys(data["route_a"], {"tuple","overall","route_b_invocation_allowed","strongest_positive","strongest_failure"}, "route")
    keys(data["scope_flags"], {"uses_target_zero_table","uses_prime_table","claims_arithmetic_local_data","claims_euler_factors","claims_root_numbers","claims_automorphy","claims_target_divisor_or_functional_equation","claims_hilbert_polya_operator","invokes_route_b"}, "flags")
    check(data["payload_sha256"] == payload_hash(data), "payload hash")
    check(data["schema"] == "hcs-c199-chaplygin-v1", "schema")
    check(data["candidate_id"] == "HCS-C199", "candidate")
    check(data["evaluation_date"] == "2026-08-27", "date")
    check(data["source_commit"] == SOURCE_COMMIT, "source lock")
    check(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    check(data["evaluator"]["sha256"] == EVALUATOR_SHA256, "evaluator sha")
    check(data["headline"] == HEADLINE, "headline")
    expected_measure = "du domega/|omega| is invariant on each reduced half-plane and its Haar-configuration lift is an off-line full-flow measure; no positive C1 reduced or configuration-Haar-factor density crosses a nonzero reduced equilibrium"
    if data["theorem"]["measure"] != expected_measure:
        raise AssertionError("reduced/full density scope")
    expected_nonclaim = "an exclusion of every configuration-dependent full-flow C1 density; the proved obstruction is for reduced and configuration-Haar-factor densities"
    if expected_nonclaim not in data["nonclaims"]:
        raise AssertionError("full-flow density nonclaim")
    check(data["route_a"]["tuple"] == ["A0_FAIL","A1_FAIL","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"], "tuple")
    check(data["route_a"]["overall"] == "ROUTE_A_REJECTED", "overall")
    check(data["route_a"]["route_b_invocation_allowed"] is False, "route B")
    check(all(v is False for v in data["scope_flags"].values()), "flags false")
    expected_dois = ["10.1016/S0167-2789(00)00046-4","10.1016/j.jappmathmech.2009.04.005","10.1016/0021-8928(87)90079-7","10.1103/PhysRevLett.101.030402"]
    check(len(data["citations"]) == 4, "citations length")
    for i, row in enumerate(data["citations"]):
        keys(row, {"key","claim","doi"}, f"citation {i}"); check(row["doi"] == expected_dois[i], "citation DOI")

    tol = mp.mpf("2e-78")
    positive = negative = samples = 0
    for i, row in enumerate(data["regression"]["heteroclinic_cases"]):
        keys(row, {"case_id","parameters","sigma","theta0","derived","samples"}, f"case {i}")
        keys(row["parameters"], {"m","J","a","H"}, f"params {i}")
        keys(row["derived"], {"I_c","R","A","eta","u_minus","u_plus","omega_endpoint","blade_angle_deflection","stable_endpoint","transverse_eigenvalue_at_u_plus"}, f"derived {i}")
        m,j,a,h = [qmp(row["parameters"][x]) for x in ("m","J","a","H")]
        check(m>0 and j>0 and h>0 and a != 0, "parameter domain")
        if a>0: positive += 1
        else: negative += 1
        sigma = int(row["sigma"]); check(sigma in (-1,1), "sigma")
        ic=j+m*a*a; radius=mp.sqrt(2*h/m); rate=m*abs(a)*radius/ic; eta=mp.sqrt(ic/m)/abs(a)
        check(F(row["derived"]["I_c"]) == F(row["parameters"]["J"])+F(row["parameters"]["m"])*F(row["parameters"]["a"])**2, "Ic exact")
        for name, got, want in [
            ("R",row["derived"]["R"],radius),("A",row["derived"]["A"],rate),("eta",row["derived"]["eta"],eta),
            ("u_minus",row["derived"]["u_minus"],-mp.sign(a)*radius),("u_plus",row["derived"]["u_plus"],mp.sign(a)*radius),
            ("blade deflection",row["derived"]["blade_angle_deflection"],sigma*mp.pi*eta),
            ("eigenvalue",row["derived"]["transverse_eigenvalue_at_u_plus"],-(m*a/ic)*mp.sign(a)*radius)]:
            check(abs(mp.mpf(got)-want)<tol, name)
        check(row["derived"]["omega_endpoint"] == "0", "omega endpoint")
        check(row["derived"]["stable_endpoint"] == "u_plus", "stable endpoint")
        check(mp.mpf(row["derived"]["transverse_eigenvalue_at_u_plus"]) < 0, "stable sign")
        check(len(row["samples"]) == 3, "sample length")
        for k, srow in enumerate(row["samples"]):
            keys(srow, {"q","time","tanh_s_exact","sech_s_exact","u","omega","theta","energy","du_dt","domega_dt"}, f"sample {i}.{k}")
            q=F(srow["q"]); qv=qmp(srow["q"])
            th_exact=(q*q-1)/(q*q+1); se_exact=2*q/(q*q+1)
            check(F(srow["tanh_s_exact"]) == th_exact, "tanh exact")
            check(F(srow["sech_s_exact"]) == se_exact, "sech exact")
            th=qmp(str(th_exact)); se=qmp(str(se_exact)); t=mp.log(qv)/rate
            u=mp.sign(a)*radius*th; w=sigma*radius*mp.sqrt(m/ic)*se
            theta=qmp(row["theta0"])+sigma*eta*mp.asin(th)
            for name, got, want in [("time",srow["time"],t),("u",srow["u"],u),("omega",srow["omega"],w),("theta",srow["theta"],theta),
                                    ("energy",srow["energy"],h),("du",srow["du_dt"],a*w*w),("domega",srow["domega_dt"],-(m*a/ic)*u*w)]:
                check(abs(mp.mpf(got)-want)<tol, name)
            check(abs(m*u*u/2+ic*w*w/2-h)<mp.mpf("1e-90"), "energy independent")
            samples += 1

    for i,row in enumerate(data["regression"]["zero_offset_cases"]):
        keys(row, {"case_id","m","J","a","u","omega","class","period"}, f"boundary {i}")
        check(F(row["m"])>0 and F(row["J"])>0 and F(row["a"])==0, "boundary params")
        w=qmp(row["omega"])
        if w:
            check(row["class"] == "periodic_SE2_circle", "circle class")
            check(abs(mp.mpf(row["period"])-2*mp.pi/abs(w))<tol, "period")
        else:
            check(row["class"] == "straight_line" and row["period"] is None, "line class")
    summary=data["summary"]
    check(summary["parameter_families"]==6, "families")
    check(summary["heteroclinic_cases"]==len(data["regression"]["heteroclinic_cases"])==12, "cases")
    check(summary["sample_states"]==samples==36, "samples")
    check(summary["positive_a_cases"]==positive==6, "positive a")
    check(summary["negative_a_cases"]==negative==6, "negative a")
    check(summary["zero_offset_cases"]==4, "boundaries")
    print(json.dumps({"status":"C199_CHECKER_PASS","assertions":assertions,"cases":12,"sample_states":samples},sort_keys=True))


if __name__ == "__main__": main()
