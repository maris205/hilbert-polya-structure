#!/usr/bin/env python3
"""Produce the deterministic HCS-C207 full-exponent Barenblatt certificate."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path

import mpmath as mp


SOURCE_COMMIT = "d108ef46fea7a8f62490a69071a83fcbda7c113b"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
DEFAULT_OUTPUT = Path(__file__).resolve().parents[1] / "results/c207_barenblatt_evidence.json"
MS = [F(1,4), F(1,3), F(1,2), F(2,3), F(1), F(3,2), F(2), F(3), F(5)]
MASSES = [F(1), F(3,2)]
RS = [F(0), F(1), F(2), F(3), F(4), F(5)]
ZS = [F(0), F(1,2), F(1), F(3,2), F(2)]
WORKING_DECIMAL_DIGITS = 100
SERIALIZED_SIGNIFICANT_DIGITS = 82


def payload_hash(data: dict) -> str:
    body = dict(data); body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def mpq(q: F) -> mp.mpf:
    return mp.mpf(q.numerator) / q.denominator


def fmt(x: mp.mpf) -> str:
    return mp.nstr(x, SERIALIZED_SIGNIFICANT_DIGITS, strip_zeros=False)


def build() -> dict:
    mp.mp.dps = WORKING_DECIMAL_DIGITS
    profiles = []
    for m_q in MS:
        for mass_q in MASSES:
            m, mass = mpq(m_q), mpq(mass_q)
            alpha_q = F(1,1) / (m_q+1)
            alpha = mpq(alpha_q)
            samples = []
            moments = []
            if m_q > 1:
                regime = "porous_compact"
                p_q = F(1,1)/(m_q-1); p=mpq(p_q)
                k_q = (m_q-1)/(2*m_q*(m_q+1)); k=mpq(k_q)
                beta_mass = mp.beta(mp.mpf("0.5"),p+1)
                C = (mass*mp.sqrt(k)/beta_mass)**(1/(p+mp.mpf("0.5")))
                radius = mp.sqrt(C/k)
                mass_reconstructed = C**(p+mp.mpf("0.5"))/mp.sqrt(k)*beta_mass
                chemical_const = m/(m-1)*C
                for z_q in ZS:
                    z=mpq(z_q); xi=z*radius
                    value=C**p*(1-z*z)**p if z<1 else mp.mpf("0")
                    chem=chemical_const if z<=1 else None
                    samples.append({"z":str(z_q),"xi":fmt(xi),"profile":fmt(value),"inside_support":z_q<=1,"chemical_potential":fmt(chem) if chem is not None else None})
                for r_q in RS:
                    r=mpq(r_q)
                    val=C**(p+(r+1)/2)*k**(-(r+1)/2)*mp.beta((r+1)/2,p+1)
                    moments.append({"r":str(r_q),"status":"finite","coefficient":fmt(val)})
                derived={"alpha":str(alpha_q),"shape_exponent":str(p_q),"quadratic_coefficient":str(k_q),"C":fmt(C),"mass_beta":fmt(beta_mass),"mass_reconstructed":fmt(mass_reconstructed),"support_radius_at_t1":fmt(radius),"free_boundary_speed_at_t1":fmt(alpha*radius),"chemical_constant":fmt(chemical_const),"tail_power":None,"moment_threshold":None}
            elif m_q < 1:
                regime = "fast_algebraic"
                q_q = F(1,1)/(1-m_q); q=mpq(q_q)
                b_q = (1-m_q)/(2*m_q*(m_q+1)); b=mpq(b_q)
                beta_mass=mp.beta(mp.mpf("0.5"),q-mp.mpf("0.5"))
                C=(beta_mass/(mass*mp.sqrt(b)))**(1/(q-mp.mpf("0.5")))
                scale=mp.sqrt(C/b)
                mass_reconstructed=C**(mp.mpf("0.5")-q)/mp.sqrt(b)*beta_mass
                chemical_const=m/(m-1)*C
                threshold_q=(1+m_q)/(1-m_q); threshold=mpq(threshold_q)
                for z_q in ZS:
                    z=mpq(z_q); xi=z*scale; value=C**(-q)*(1+z*z)**(-q)
                    samples.append({"z":str(z_q),"xi":fmt(xi),"profile":fmt(value),"inside_support":True,"chemical_potential":fmt(chemical_const)})
                for r_q in RS:
                    r=mpq(r_q)
                    if r_q < threshold_q:
                        val=C**(-q+(r+1)/2)*b**(-(r+1)/2)*mp.beta((r+1)/2,q-(r+1)/2)
                        moments.append({"r":str(r_q),"status":"finite","coefficient":fmt(val)})
                    elif r_q == threshold_q:
                        moments.append({"r":str(r_q),"status":"logarithmic_divergence","coefficient":None})
                    else:
                        moments.append({"r":str(r_q),"status":"power_divergence","coefficient":None})
                derived={"alpha":str(alpha_q),"shape_exponent":str(q_q),"quadratic_coefficient":str(b_q),"C":fmt(C),"mass_beta":fmt(beta_mass),"mass_reconstructed":fmt(mass_reconstructed),"support_radius_at_t1":None,"free_boundary_speed_at_t1":None,"chemical_constant":fmt(chemical_const),"tail_power":str(2*q_q),"moment_threshold":str(threshold_q)}
            else:
                regime = "heat_gaussian"
                C=mass/(2*mp.sqrt(mp.pi)); mass_reconstructed=2*C*mp.sqrt(mp.pi)
                chemical_const=mp.log(C)
                for z_q in ZS:
                    xi=mpq(z_q); value=C*mp.e**(-xi*xi/4)
                    samples.append({"z":str(z_q),"xi":fmt(xi),"profile":fmt(value),"inside_support":True,"chemical_potential":fmt(chemical_const)})
                for r_q in RS:
                    r=mpq(r_q); val=mass*2**r*mp.gamma((r+1)/2)/mp.sqrt(mp.pi)
                    moments.append({"r":str(r_q),"status":"finite","coefficient":fmt(val)})
                derived={"alpha":"1/2","shape_exponent":None,"quadratic_coefficient":"1/4","C":fmt(C),"mass_beta":None,"mass_reconstructed":fmt(mass_reconstructed),"support_radius_at_t1":None,"free_boundary_speed_at_t1":None,"chemical_constant":fmt(chemical_const),"tail_power":"Gaussian","moment_threshold":"all"}
            profiles.append({"case_id":f"m{m_q}_M{mass_q}","m":str(m_q),"mass":str(mass_q),"regime":regime,"derived":derived,"samples":samples,"moments":moments})

    data={
      "schema":"hcs-c207-barenblatt-v1","candidate_id":"HCS-C207","evaluation_date":"2026-08-27","source_commit":SOURCE_COMMIT,"scope_literal":SCOPE,
      "evaluator":{"path":"flow_systems/skills/route-a-evaluator.md","version":"0.2.0","sha256":EVALUATOR_SHA256},
      "headline":"All one-dimensional positive exponents admit a single mass-normalized Barenblatt similarity atlas with exact compact, Gaussian, algebraic-tail, moment, pressure, and rescaled-dissipation boundaries",
      "frozen_object":{"equation":"u_t=(u^m)_xx on R with m>0 and mass M>0","similarity":"u(x,t)=t^(-alpha)F(x t^(-alpha)), alpha=1/(m+1)","profile_class":"centered nonnegative integrable first-kind profiles of mass M with F^m locally absolutely continuous and (F^m)'+alpha*xi*F=0 almost everywhere; uniqueness is up to almost-everywhere equality","clock":"physical diffusion time t>0; tau=log t only for the explicitly declared rescaled flow","normalization":"mass integral equals M; translations are excluded by centered normalization"},
      "theorem":{
        "porous":"for m>1, F=(C-k_m xi^2)_+^(1/(m-1)), k_m=(m-1)/(2m(m+1)), with compact support",
        "heat":"for m=1, F=M exp(-xi^2/4)/(2 sqrt(pi))",
        "fast":"for 0<m<1, F=(C+b_m xi^2)^(-1/(1-m)), b_m=(1-m)/(2m(m+1)), with algebraic tail",
        "mass":"C is uniquely fixed by the exact Beta integrals recorded in the theorem package",
        "moments":"all porous and Gaussian absolute moments are finite; in fast diffusion the r-th absolute moment is finite exactly when r<(1+m)/(1-m), logarithmically divergent at equality",
        "second_moment":"the fast-diffusion second moment is finite exactly for m>1/3; m=1/3 is logarithmically divergent",
        "uniqueness":"uniqueness is only among centered nonnegative integrable zero-flux first-kind similarity profiles of mass M with F^m locally absolutely continuous and the integrated profile law holding almost everywhere, up to almost-everywhere equality; it is not uniqueness among arbitrary Cauchy solutions",
        "pressure":"for m>1, P=m u^(m-1)/(m-1) is parabolic on support, X_+/-=+/-R_M t^alpha, and each one-sided interface satisfies X_+/-'=alpha X_+/-/t=-lim_inside P_x",
        "rescaled":"v_tau=(v^m)_(xi xi)+alpha(xi v)_xi and each mass-M Barenblatt profile is stationary",
        "free_energy":"F_m[v]=integral[v^m/(m-1)+alpha*xi^2*v/2] for m!=1 and F_1[v]=integral[v*log(v)-v+alpha*xi^2*v/2]",
        "dissipation":"for sufficiently regular positive rescaled solutions with finite displayed free energy (no infinity-minus-infinity) and justified boundary decay, dF_m/dtau=-integral v |partial_xi chemical_potential|^2; this is not asserted outside that class, and the unrenormalized Barenblatt free-energy/second-moment boundary is m>1/3 in fast diffusion",
      },
      "regression":{"profiles":profiles},
      "summary":{"m_values":len(MS),"mass_values":len(MASSES),"profiles":len(profiles),"profile_samples":len(profiles)*len(ZS),"moment_cells":len(profiles)*len(RS),"working_decimal_digits":WORKING_DECIMAL_DIGITS,"serialized_significant_digits":SERIALIZED_SIGNIFICANT_DIGITS},
      "route_a":{"tuple":["A0_FAIL","A1_FAIL","A2_FAIL","A3_FAIL","A4_FAIL"],"overall":"ROUTE_A_REJECTED","route_b_invocation_allowed":False,"strongest_positive":"The nonlinear diffusion has a source-native mass-preserving similarity flow and exact gradient-flow dissipation in its stated finite-energy class.","strongest_failure":"The flow is dissipative and supplies no rational-prime primitive owner, periodic ledger, target determinant, or same-clock unitary lift."},
      "scope_flags":{"uses_target_zero_table":False,"uses_prime_table":False,"claims_arithmetic_local_data":False,"claims_euler_factors":False,"claims_root_numbers":False,"claims_automorphy":False,"claims_target_divisor_or_functional_equation":False,"claims_hilbert_polya_operator":False,"invokes_route_b":False},
      "citations":[
        {"key":"Barenblatt1952","claim":"classical source-type porous-medium solution","reference":"G. I. Barenblatt, Prikl. Mat. Mekh. 16 (1952), 67-78"},
        {"key":"Vazquez2007","claim":"porous-medium and fast-diffusion mathematical framework and source ownership","doi":"10.1093/acprof:oso/9780198569039.001.0001"}],
      "nonclaims":[
        "priority for the porous-medium equation, Barenblatt profiles, fast diffusion, or Wasserstein gradient flow",
        "classification of arbitrary Cauchy solutions, signed profiles, non-centered profiles, or higher dimensions",
        "that finite rational-exponent regression proves the all-m theorem",
        "free-energy dissipation without regularity, integrability, and boundary-decay hypotheses",
        "a prime-orbit law, arithmetic local datum, Euler factor, root number, automorphy, target divisor, or Hilbert--Polya operator",
        "external peer review, literature exhaustiveness, novelty certification, or an acceptance score"],
    }
    data["payload_sha256"]=payload_hash(data)
    return data


def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--output",type=Path,default=DEFAULT_OUTPUT); args=parser.parse_args()
    data=build(); args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(json.dumps(data,sort_keys=True,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps({"status":"C207_PRODUCER_PASS","profiles":data["summary"]["profiles"],"moment_cells":data["summary"]["moment_cells"],"working_decimal_digits":data["summary"]["working_decimal_digits"],"serialized_significant_digits":data["summary"]["serialized_significant_digits"],"payload_sha256":data["payload_sha256"]},sort_keys=True))
if __name__=="__main__": main()
