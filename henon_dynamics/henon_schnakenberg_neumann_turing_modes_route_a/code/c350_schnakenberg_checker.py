#!/usr/bin/env python3
"""Producer-independent exact and semantic checker for HCS-C350."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c350_schnakenberg_evidence.json"
DEFAULT_YAML = ROOT / "evaluations/route_a/HCS-C350/2026-09-03.yaml"
SOURCE = "327fc1172cebcdeb17adfd2d8ad12636fbb94f52"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
YAML_RAW = "392e9d205af7e0e7f765bc34889f23cd094434335d68e9ab1cf4853bf32e0d21"
YAML_SEMANTIC = "ed762fcd6f342b51d83c2445e5d862407317fec49d961a73bc1cf20830cc7cda"
AUTHORITY = "flow_systems/skills/route-a-evaluator.md"
VERDICTS = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"]
FLAGS = {
    "claims_target_arithmetic_local_data": False,
    "claims_target_euler_factors": False, "claims_root_number": False,
    "claims_automorphy": False, "claims_target_divisor_or_counting_law": False,
    "claims_target_functional_equation": False, "claims_target_zero_match": False,
    "claims_hilbert_polya_operator": False, "invokes_route_b": False,
}
PARAMETERS = (
    ("kinetic_unstable", "1/100", "9/100", "1", "20", "16"),
    ("kinetic_neutral", "3/16", "5/16", "1", "10", "4"),
    ("equal_diffusion", "1/10", "9/10", "1", "1", "16"),
    ("window_no_mode", "1/10", "9/10", "1", "20", "1"),
    ("one_unstable_mode", "1/10", "9/10", "1", "20", "4"),
    ("two_unstable_modes", "1/10", "9/10", "1", "20", "16"),
    ("lower_endpoint_neutral", "1/10", "9/10", "1", "100/11", "4"),
    ("upper_endpoint_neutral", "1/10", "9/10", "1", "100/11", "25/11"),
    ("double_wall_neutral", "1/9", "8/9", "1", "9", "3"),
)
CHECKS = 0


def pairs(items):
    result = {}
    for key, value in items:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def strict_json(path):
    value = json.loads(path.read_text(), object_pairs_hook=pairs,
        parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)))
    if type(value) is not dict:
        raise TypeError("JSON root")
    return value


class StrictLoader(yaml.SafeLoader):
    pass


StrictLoader.yaml_implicit_resolvers = {
    key: [(tag, rx) for tag, rx in values if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def strict_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in result:
            raise ValueError("duplicate/non-string YAML key")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, strict_mapping)


def strict_yaml(path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchors/aliases forbidden")
    value = yaml.load(raw, Loader=StrictLoader)
    if type(value) is not dict:
        raise TypeError("YAML root")
    return value


def need(condition, label):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)


def exact_keys(value, keys, label):
    need(type(value) is dict and set(value) == set(keys), f"{label} keys")


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def fs(value):
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def algebra(a, b, du, dv):
    s = a + b
    fu = (b-a)/s
    fv = s**2
    gu = -2*b/s
    gv = -s**2
    tau = fu + gv
    detj = fu*gv-fv*gu
    coefficient = dv*fu+du*gv
    discriminant = coefficient**2-4*du*dv*detj
    return s,fu,fv,gu,gv,tau,detj,coefficient,discriminant


def state(trace, det):
    if det < 0: return "saddle_unstable"
    if det == 0: return "neutral_zero"
    if trace < 0: return "stable"
    if trace == 0: return "neutral_imaginary"
    return "positive_spectral_abscissa"


def independent_count_formula(detj, B, Q, du, dv, ell2):
    """Recover the strict floor/ceiling count by independent exact tests."""
    if B <= 0 or Q <= 0:
        return None
    midpoint = B / (2 * du * dv)
    below = 0
    while True:
        trial = below + 1
        mu = Fraction(trial * trial, 1) / ell2
        value = du * dv * mu * mu - B * mu + detj
        if mu <= midpoint and value >= 0:
            below = trial
            continue
        break
    above = 0
    while True:
        mu = Fraction(above * above, 1) / ell2
        value = du * dv * mu * mu - B * mu + detj
        if mu >= midpoint and value >= 0:
            return max(0, above - below - 1)
        above += 1


def independent_rows():
    summaries, modes, walls = [], [], []
    for label, aa, bb, uu, vv, ll in PARAMETERS:
        a,b,du,dv,ell2=map(Fraction,(aa,bb,uu,vv,ll))
        s,fu,fv,gu,gv,tau,detj,B,Q=algebra(a,b,du,dv)
        cutoff=6
        if B>0:
            while Fraction(cutoff**2,1)/ell2 <= B/(du*dv): cutoff+=1
        unstable=[]; neutral=[]
        for n in range(cutoff+1):
            mu=Fraction(n*n,1)/ell2
            tr=tau-(du+dv)*mu
            det=du*dv*mu**2-B*mu+detj
            if tau<0 and n and det<0: unstable.append(n)
            if tau<0 and n and det==0: neutral.append(n)
            modes.append({"case":label,"n":n,"mu":fs(mu),"trace":fs(tr),
                "determinant":fs(det),"state":state(tr,det)})
        window=tau<0 and B>0 and Q>0
        count_formula_value=(
            independent_count_formula(detj,B,Q,du,dv,ell2) if window else None)
        summaries.append({"case":label,"a":fs(a),"b":fs(b),"d_u":fs(du),
            "d_v":fs(dv),"ell_squared":fs(ell2),"s":fs(s),"f_u":fs(fu),
            "f_v":fs(fv),"g_u":fs(gu),"g_v":fs(gv),"tau":fs(tau),
            "det_J":fs(detj),"B":fs(B),"Q":fs(Q),
            "kinetic_state":"stable" if tau<0 else ("neutral" if tau==0 else "unstable"),
            "continuous_window":window,"double_wall":tau<0 and B>0 and Q==0,
            "complete_mode_cutoff":cutoff,"unstable_indices":unstable,
            "neutral_indices":neutral,"finite_domain_turing":bool(unstable),
            "count_formula_value":count_formula_value})
        if window:
            for n in range(1,5):
                walls.append({"case":label,"n":n,
                    "ell2_polynomial":[fs(detj),fs(-B*n*n),fs(du*dv*n**4)],
                    "discriminant":fs(n**4*Q),
                    "strict_between_roots_is_unstable":True})
    return summaries,modes,walls


def check_yaml(value):
    top = ["schema","candidate_id","title","evaluation_date","source_commit",
        "fixed_epoch","scope_literal","evaluator_authority","evaluator_version",
        "evaluator_authority_sha256","obstruction_id","candidate_definition","family",
        "phase_space","dynamics","parameters","parameter_provenance","arithmetic_origin",
        "clock","normalization","determinant_convention","orbit_cutoff","precision",
        "training_data","forbidden_data","artifact_paths","a0","a1","a2","a3","a4",
        "tuple","overall_verdict","route_b_invocation_allowed","route_b_lock_reason",
        "scope_flags","theorem_status","finite_evidence_role","source_owner_tokens"]
    exact_keys(value,top,"YAML top")
    need((value["schema"],value["candidate_id"],value["obstruction_id"],
        value["evaluation_date"],value["source_commit"],value["fixed_epoch"],
        value["scope_literal"]) == ("route-a-evaluation-v0.2.0","HCS-C350","HEN-O334",
        "2026-09-03",SOURCE,1788393600,SCOPE),"YAML identity")
    need(value["evaluator_authority"]==AUTHORITY,"YAML authority")
    need(value["evaluator_version"]=="0.2.0" and value["evaluator_authority_sha256"]==EVALUATOR,"YAML evaluator")
    need(value["artifact_paths"]==["results/c350_schnakenberg_evidence.json","THEOREM_PACKAGE.md","paper/main.pdf"],"YAML artifacts")
    for index,key in enumerate(("a0","a1","a2","a3","a4")):
        exact_keys(value[key],["verdict","evidence_status","strongest_evidence","strongest_failure"],f"YAML {key}")
        need(value[key]["verdict"]==VERDICTS[index],f"YAML {key} verdict")
        need(value[key]["evidence_status"]==("PROVED" if index<2 else "STOP_SCOPED"),f"YAML {key} status")
    need(value["tuple"]==VERDICTS and value["overall_verdict"]=="ROUTE_A_REJECTED","YAML outcome")
    need(value["route_b_invocation_allowed"] is False,"YAML Route B")
    need(value["scope_flags"]==FLAGS,"YAML flags")
    need(value["theorem_status"]=="PROVABLE_AS_STATED","YAML theorem")
    need(value["source_owner_tokens"]==["10.1016/0022-5193(79)90042-0","10.1098/rstb.1952.0012"],"YAML sources")


def main():
    if sys.flags.optimize:
        raise RuntimeError("C350 checker refuses optimized Python")
    parser=argparse.ArgumentParser()
    parser.add_argument("--evidence",type=Path,default=DEFAULT)
    parser.add_argument("--evaluation",type=Path,default=DEFAULT_YAML)
    args=parser.parse_args()
    data=strict_json(args.evidence)
    evaluation=strict_yaml(args.evaluation)
    need(hashlib.sha256(args.evaluation.read_bytes()).hexdigest()==YAML_RAW,"YAML raw")
    need(hashlib.sha256(canonical(evaluation)).hexdigest()==YAML_SEMANTIC,"YAML semantic")
    check_yaml(evaluation)
    top=["schema","candidate_id","obstruction_id","evaluation_date","source_commit",
        "fixed_epoch","scope_literal","evaluator","route_a_yaml","model","theorem_contract",
        "finite_grid","collision_boundary","nonclaims","references","route_a","scope_flags",
        "case_rows","mode_rows","length_wall_rows","enumeration","payload_sha256"]
    exact_keys(data,top,"evidence top")
    body=dict(data); claimed=body.pop("payload_sha256")
    need(type(claimed) is str and claimed==hashlib.sha256(canonical(body)).hexdigest(),"payload hash")
    need((data["schema"],data["candidate_id"],data["obstruction_id"],data["evaluation_date"],
        data["source_commit"],data["fixed_epoch"],data["scope_literal"]) ==
        ("hcs-c350-schnakenberg-evidence-v1","HCS-C350","HEN-O334","2026-09-03",SOURCE,1788393600,SCOPE),"identity")
    need(data["evaluator"]=={"authority":AUTHORITY,"version":"0.2.0","sha256":EVALUATOR},"evaluator")
    need(data["route_a_yaml"]=={"relative_path":"evaluations/route_a/HCS-C350/2026-09-03.yaml",
        "raw_sha256":YAML_RAW,"semantic_sha256":YAML_SEMANTIC},"YAML binding")
    need(data["model"]=={"domain":"(0,L) with homogeneous Neumann boundary conditions",
        "parameters":"a,b,d_u,d_v,L>0",
        "pde":"u_t=d_u u_xx+a-u+u^2 v; v_t=d_v v_xx+b-u^2 v",
        "equilibrium":"s=a+b; (u_*,v_*)=(s,b/s^2)",
        "neumann_modes":"mu_n=(n*pi/L)^2"},"model")
    need(data["theorem_contract"]=={
        "equilibrium":"unique positive spatially homogeneous equilibrium only",
        "kinetic":"det J=s^2 and kinetic asymptotic stability iff tau=(b-a)/s-s^2<0",
        "modal":"after complexification, the complete compact-resolvent spectrum is the union of the two eigenvalues of M(mu_n)",
        "continuous_window":"under tau<0, an open unstable wavenumber window exists iff B>0 and Q=B^2-4d_u d_v s^2>0",
        "finite_domain":"linear Turing instability iff some n>=1 satisfies mu_-<mu_n<mu_+",
        "count":"N_unst=max(0,ceil((L/pi)sqrt(mu_+))-floor((L/pi)sqrt(mu_-))-1)",
        "boundaries":"endpoint modes are neutral; equal diffusion has no window; Q=0 is neutral contact; zero diffusion is excluded"},"contract")
    need(data["route_a"]=={"tuple":VERDICTS,"overall":"ROUTE_A_REJECTED","route_b_invocation_allowed":False},"Route A")
    need(data["scope_flags"]==FLAGS,"flags")
    need(data["collision_boundary"]=={
        "C311":"Brusselator ODE Hopf normal form, not a spatial two-species Turing spectrum",
        "C304":"scalar fourth-order Cahn-Hilliard shells, not unequal two-species diffusion",
        "C347":"nonlocal Kuramoto probability PDE, not local Schnakenberg kinetics",
        "C202":"scalar Fisher-KPP traveling fronts, not stationary modal instability"},"collisions")
    need(data["nonclaims"]==[
        "no nonlinear patterned branch or bifurcation theorem",
        "no nonlinear global well-posedness, attractor, or pattern-selection theorem",
        "no zero-diffusion extension of the uniformly parabolic theorem",
        "no priority claim for Schnakenberg kinetics, Turing instability, or modal analysis",
        "no target arithmetic local data, Euler factors, root number, automorphy, target zero match, Hilbert-Polya operator, or Route B"],"nonclaims")
    need(data["references"]==[
        {"authors":"J. Schnakenberg","year":1979,
         "identifier":"DOI:10.1016/0022-5193(79)90042-0",
         "url":"https://www.sciencedirect.com/science/article/pii/0022519379900420",
         "role":"primary source for the named reaction kinetics"},
        {"authors":"A. M. Turing","year":1952,
         "identifier":"DOI:10.1098/rstb.1952.0012",
         "url":"https://royalsocietypublishing.org/doi/10.1098/rstb.1952.0012",
         "role":"original reaction-diffusion instability lineage"}],"references")
    summaries,modes,walls=independent_rows()
    need(data["case_rows"]==summaries,"case rows")
    need(data["mode_rows"]==modes,"mode rows")
    need(data["length_wall_rows"]==walls,"wall rows")
    for row in data["case_rows"]:
        exact_keys(row,["case","a","b","d_u","d_v","ell_squared","s","f_u","f_v","g_u","g_v","tau","det_J","B","Q","kinetic_state","continuous_window","double_wall","complete_mode_cutoff","unstable_indices","neutral_indices","finite_domain_turing","count_formula_value"],"case row")
        need(row["count_formula_value"] == (len(row["unstable_indices"])
             if row["continuous_window"] else None), "count formula/list agreement")
    for row in data["mode_rows"]:
        exact_keys(row,["case","n","mu","trace","determinant","state"],"mode row")
    for row in data["length_wall_rows"]:
        exact_keys(row,["case","n","ell2_polynomial","discriminant","strict_between_roots_is_unstable"],"wall row")
    need(data["finite_grid"]=={"case_rows":len(summaries),"mode_rows":len(modes),"length_wall_rows":len(walls),"uses_ell_squared":True,"records_count_formula":True},"grid")
    need(data["enumeration"]=={"all_arithmetic_exact":True,"floating_point_used":False,
        "finite_evidence_proves_continuum_theorem":False,"case_sha256":digest(summaries),
        "mode_sha256":digest(modes),"length_wall_sha256":digest(walls)},"enumeration")
    # Explicitly lock the designed adversarial boundary outcomes.
    by={row["case"]:row for row in summaries}
    need(by["window_no_mode"]["continuous_window"] and not by["window_no_mode"]["finite_domain_turing"],"continuous/discrete split")
    need(by["two_unstable_modes"]["unstable_indices"]==[2,3],"two-mode result")
    need(by["lower_endpoint_neutral"]["neutral_indices"]==[1],"endpoint neutral")
    need(by["upper_endpoint_neutral"]["neutral_indices"]==[1],"upper endpoint neutral")
    need(by["double_wall_neutral"]["Q"]=="0" and by["double_wall_neutral"]["neutral_indices"]==[1],"double wall")
    print(f"C350 independent Schnakenberg checker: PASS {CHECKS} assertions")


if __name__=="__main__":
    main()
