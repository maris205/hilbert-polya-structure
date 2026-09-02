#!/usr/bin/env python3
"""Strict producer-independent raw-Jacobian checker for HCS-C290."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from fractions import Fraction
from pathlib import Path
from typing import Any

import mpmath as mp
import sympy as sp
import yaml
from yaml.constructor import ConstructorError
from yaml.tokens import AliasToken, AnchorToken

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c290_cr3bp_evidence.json"
YAML_PATH = ROOT / "evaluations/route_a/HCS-C290/2026-09-02.yaml"
SOURCE = "7fbe9db30cc460a82883533d7cfb2edd988c5b65"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH = 1788307200
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
MODEL = {
    "problem": "planar circular restricted three-body problem in synodic normalized units",
    "primaries": "masses 1-mu and mu at (-mu,0) and (1-mu,0)",
    "range": "0<mu<=1/2; collision points are removed",
    "potential": "Omega=(x^2+y^2)/2+(1-mu)/r1+mu/r2",
    "equations": "xddot-2 ydot=Omega_x and yddot+2 xdot=Omega_y",
    "stability_meaning": "boundedness of the linearized flow, including resonant ratios; no nonlinear resonance or KAM claim",
}
THEOREM = {
    "equilibria": "exactly five equilibria: one in each collinear interval and the two equilateral points",
    "triangular_locations": "L4,L5=(1/2-mu, plus_or_minus sqrt(3)/2)",
    "collinear": "every collinear point has S>1 and saddle-times-center linear type",
    "triangular_polynomial": "lambda^4+lambda^2+(27/4)mu(1-mu)",
    "routh_boundary": "mu_R=(1-sqrt(23/27))/2 separates bounded elliptic linear flow from a Hamiltonian quartet",
    "critical": "at mu=mu_R and both L4,L5, each of plus_or_minus i/sqrt(2) has algebraic multiplicity 2 and geometric multiplicity 1, so solutions grow linearly and the equilibrium is not linearly stable",
}
PROOF = {
    "five_points": "Omega_y=0 forces y=0 or equal unit distances, giving three monotone collinear roots and two equilateral roots",
    "collinear_uniqueness": "Omega_x is strictly increasing on each of the three collision-free x intervals with opposite endpoint signs",
    "collinear_instability": "S>1 makes the constant term (1+2S)(1-S) negative, forcing one real and one imaginary eigenvalue pair",
    "triangular_hessian": "the raw Hessian gives trace 3 and determinant (27/4)mu(1-mu) in the rotating characteristic determinant",
    "critical_defect": "at both L4,L5 the two-by-two position pencil has rank one at lambda=plus_or_minus i/sqrt(2), hence one eigenvector per double eigenvalue and a nontrivial Jordan block",
    "finite_role": "finite root and parameter cells are regression evidence and do not prove the all-mu theorem",
}
ROUTE = {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}
FLAGS = {"arithmetic_local_data": False, "euler_factors": False, "root_numbers": False, "automorphy": False, "target_divisor_or_counting_law": False, "target_functional_equation": False, "target_zero_match": False, "hilbert_polya_operator": False, "route_b_input": False}
REFERENCES = [
    {"id": "Lagrange1772", "authors": "Joseph-Louis Lagrange", "title": "Essai sur le Probleme des trois Corps", "venue": "Prix de l'Academie royale des sciences de Paris, tome IX (1772); Oeuvres, tome VI", "identifier": "Lagrange-1772-Oeuvres-VI-229-331", "url": "https://fr.wikisource.org/wiki/M%C3%A9moires_extraits_des_recueils_de_l%E2%80%99Acad%C3%A9mie_des_sciences_de_Paris_et_de_l%E2%80%99Institut_de_France/Essai_sur_le_Probl%C3%A8me_des_trois_Corps", "ownership": "historical owner of the equilateral three-body configuration"},
    {"id": "Gascheau1843", "authors": "Gabriel Gascheau", "title": "Mouvements relatifs d'un systeme de corps", "venue": "These de mecanique, Faculte des sciences de Paris, Bachelier (1843), 36 pp. and plate", "identifier": "BnF-Gallica-ark-12148-bpt6k5789653w", "url": "https://gallica.bnf.fr/ark:/12148/bpt6k5789653w", "ownership": "first historical owner of the Newtonian triangular linear-stability criterion"},
    {"id": "Routh1874", "authors": "Edward John Routh", "title": "On Laplace's Three Particles, with a Supplement on the Stability of Steady Motion", "venue": "Proceedings of the London Mathematical Society s1-6 (1874), 86-97", "identifier": "10.1112/plms/s1-6.1.86", "url": "https://doi.org/10.1112/plms/s1-6.1.86", "ownership": "subsequent treatment and inverse-power-law generalization of triangular stability"},
    {"id": "MeyerHallOffin2009", "authors": "Kenneth R. Meyer, Glen R. Hall, and Dan Offin", "title": "Introduction to Hamiltonian Dynamical Systems and the N-Body Problem", "venue": "Springer, second edition (2009)", "identifier": "10.1007/978-0-387-09724-4", "url": "https://doi.org/10.1007/978-0-387-09724-4", "ownership": "authoritative modern source for the restricted problem and linear Hamiltonian stability"},
]
NONCLAIMS = [
    "the Lagrange equilibria and Gascheau-Routh threshold are classical and not claimed as literature originality",
    "the elliptic linearized flow is bounded also at resonant mass ratios; no nonlinear resonance, bifurcation, or KAM conclusion is claimed",
    "finite numerical root cells are regression evidence and do not replace the analytic existence and uniqueness proof",
]
TOP = {"schema","candidate_id","evaluation_date","source_commit","fixed_epoch","scope_literal","evaluator","model","theorem_contract","proof_contract","route_a","scope_flags","enumeration","triangular_cells","collinear_cells","critical_cell","boundary_cells","references","nonclaims","payload_sha256"}
TRI = {"mu","routh_parameter","routh_discriminant","charpoly_constant","lambda_square_sum","lambda_square_product","linear_type","linearly_stable"}
COL = {"mu","point","interval","x","omega_x_residual","S","lambda2_coefficient","constant_coefficient","linear_type","linearly_stable"}
CRIT = {"mu_formula","routh_parameter","charpoly","eigenvalues","algebraic_multiplicity_each","geometric_multiplicity_each","rank_cells","defective","linear_growth","linearly_stable"}
CRIT_RANK = {"point","mixed_hessian_sign","eigenvalue","matrix_rank","geometric_multiplicity"}

YAML_EXPECTED = {
    "schema": "hcs-route-a-evaluation-v0.2.0",
    "candidate_id": "HCS-C290",
    "evaluation_date": "2026-09-02",
    "source_commit": SOURCE,
    "fixed_epoch": EPOCH,
    "scope_literal": SCOPE,
    "evaluator_version": "0.2.0",
    "evaluator_authority_sha256": EVALUATOR,
    "title": "Lagrange equilibria and linear stability in the planar CR3BP",
    "obstruction_id": "HEN-O274",
    "tuple": ROUTE["tuple"],
    "overall_verdict": "ROUTE_A_REJECTED",
    "route_b_invocation_allowed": False,
    "route_b_lock_reason": "No intrinsic primitive-period family, arithmetic bridge, or target spectral bridge is proved.",
    "scope_flags": FLAGS,
    "theorem_status": "PROVABLE_AS_STATED",
    "finite_evidence_role": "regression_only_not_all_parameter_proof",
    "source_owner_tokens": [
        "Lagrange-1772-Oeuvres-VI-229-331",
        "BnF-Gallica-ark-12148-bpt6k5789653w",
        "10.1112/plms/s1-6.1.86",
        "10.1007/978-0-387-09724-4",
    ],
}
YAML_SEMANTIC_SHA = "8bae85795b5f694a177e856d2f2f2fab85c03af5738c67d1ae2ec0a4d158a366"


class Checks:
    def __init__(self): self.n = 0
    def ok(self, cond: bool, label: str):
        self.n += 1
        if not cond: raise AssertionError(label)


def reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out = {}
    for key, value in pairs:
        if key in out: raise ValueError(f"duplicate JSON key: {key}")
        out[key] = value
    return out


class UniqueYAMLLoader(yaml.SafeLoader):
    """Safe loader that rejects duplicate, merge, and non-string mapping keys."""


def construct_unique_yaml_mapping(
    loader: UniqueYAMLLoader, node: yaml.nodes.MappingNode, deep: bool = False
) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge" or key_node.value == "<<":
            raise ConstructorError("mapping", node.start_mark, "YAML merge keys are forbidden", key_node.start_mark)
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str:
            raise ConstructorError("mapping", node.start_mark, "non-string YAML mapping key", key_node.start_mark)
        if key in result:
            raise ConstructorError("mapping", node.start_mark, f"duplicate YAML key: {key}", key_node.start_mark)
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueYAMLLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_unique_yaml_mapping
)


def strict_load(path: Path) -> dict[str, Any]:
    result = json.loads(path.read_text(), object_pairs_hook=reject_duplicates, parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))
    if type(result) is not dict: raise TypeError("object required")
    return result


def strict_yaml_load(path: Path) -> dict[str, Any]:
    text = path.read_text()
    tokens = list(yaml.scan(text))
    if any(isinstance(token, (AnchorToken, AliasToken)) for token in tokens):
        raise ValueError("YAML anchors and aliases are forbidden")
    result = yaml.load(text, Loader=UniqueYAMLLoader)
    if type(result) is not dict:
        raise TypeError("YAML top-level object required")
    return result


def phash(data: dict) -> str:
    body = dict(data); body.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def exact_keys(c: Checks, value: Any, keys: set[str], label: str):
    c.ok(type(value) is dict, label+" object"); c.ok(set(value) == keys, label+" keys")


def validate_route_yaml(c: Checks, path: Path) -> dict[str, Any]:
    route = strict_yaml_load(path)
    exact_keys(c, route, set(YAML_EXPECTED), "route YAML")
    for key, expected in YAML_EXPECTED.items():
        c.ok(type(route[key]) is type(expected), f"route YAML {key} type")
    exact_keys(c, route["scope_flags"], set(FLAGS), "route YAML scope flags")
    c.ok(all(type(value) is bool for value in route["scope_flags"].values()), "route YAML flag types")
    c.ok(type(route["tuple"]) is list and all(type(value) is str for value in route["tuple"]), "route YAML tuple types")
    c.ok(type(route["source_owner_tokens"]) is list and all(type(value) is str for value in route["source_owner_tokens"]), "route YAML owner types")
    c.ok(len(route["source_owner_tokens"]) == len(set(route["source_owner_tokens"])), "route YAML owner uniqueness")
    c.ok(route == YAML_EXPECTED, "route YAML exact values")
    canonical = json.dumps(route, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    c.ok(hashlib.sha256(canonical).hexdigest() == YAML_SEMANTIC_SHA, "route YAML semantic hash")
    return route


def rat(c: Checks, value: Any, label: str) -> Fraction:
    c.ok(type(value) is str, label+" type")
    try: result = Fraction(value)
    except (ValueError, ZeroDivisionError) as error: raise AssertionError(label+" rational") from error
    c.ok(str(result) == value, label+" canonical"); return result


def raw_matrix(oxx: mp.mpf, oyy: mp.mpf, oxy: mp.mpf) -> mp.matrix:
    return mp.matrix([[0,0,1,0],[0,0,0,1],[oxx,oxy,0,2],[oxy,oyy,-2,0]])


def root_bisect(mu: mp.mpf, point: str) -> mp.mpf:
    eps = mp.mpf("1e-35")
    def f(x): return x-(1-mu)*(x+mu)/abs(x+mu)**3-mu*(x-1+mu)/abs(x-1+mu)**3
    intervals = {"L3": (mp.mpf(-4), -mu-eps), "L1": (-mu+eps, 1-mu-eps), "L2": (1-mu+eps, mp.mpf(4))}
    lo, hi = intervals[point]; flo, fhi = f(lo), f(hi)
    if not flo < 0 < fhi: raise AssertionError(point+" endpoint signs")
    for _ in range(310):
        mid = (lo+hi)/2
        if f(mid) < 0: lo = mid
        else: hi = mid
    return (lo+hi)/2


def main() -> None:
    parser = argparse.ArgumentParser(); parser.add_argument("input", nargs="?", type=Path, default=DEFAULT); parser.add_argument("--yaml", type=Path, default=YAML_PATH); args = parser.parse_args()
    data = strict_load(args.input); c = Checks(); exact_keys(c, data, TOP, "top")
    c.ok(type(data["payload_sha256"]) is str and re.fullmatch(r"[0-9a-f]{64}", data["payload_sha256"]) is not None, "hash syntax")
    c.ok(data["payload_sha256"] == phash(data), "payload hash")
    c.ok(data["schema"] == "hcs-c290-cr3bp-lagrange-stability-v1", "schema")
    c.ok(data["candidate_id"] == "HCS-C290" and data["evaluation_date"] == "2026-09-02", "identity")
    c.ok(data["source_commit"] == SOURCE and data["fixed_epoch"] == EPOCH and type(data["fixed_epoch"]) is int, "source epoch")
    c.ok(data["scope_literal"] == SCOPE, "scope")
    exact_keys(c, data["evaluator"], {"version","sha256"}, "evaluator"); c.ok(data["evaluator"] == {"version":"0.2.0","sha256":EVALUATOR}, "evaluator value")
    for name, expected in (("model",MODEL),("theorem_contract",THEOREM),("proof_contract",PROOF),("route_a",ROUTE),("scope_flags",FLAGS)):
        exact_keys(c, data[name], set(expected), name); c.ok(data[name] == expected, name+" value")
    c.ok(all(type(v) is bool and v is False for v in data["scope_flags"].values()), "flags")
    c.ok(type(data["route_a"]["tuple"]) is list and all(type(v) is str for v in data["route_a"]["tuple"]), "route tuple types")
    c.ok(type(data["route_a"]["overall"]) is str and type(data["route_a"]["route_b_invocation_allowed"]) is bool, "route primitive types")
    validate_route_yaml(c, args.yaml)

    mus = (Fraction(1,1000), Fraction(1,100), Fraction(1,50), Fraction(1,30), Fraction(1,25), Fraction(1,10), Fraction(1,4), Fraction(1,2))
    enum = data["enumeration"]; exact_keys(c, enum, {"mu_values","triangular_cells","collinear_cells","critical_cells","boundary_cells"}, "enumeration")
    c.ok(type(enum["mu_values"]) is list and all(type(v) is str for v in enum["mu_values"]), "enumeration mu types")
    c.ok(all(type(enum[key]) is int for key in ("triangular_cells","collinear_cells","critical_cells","boundary_cells")), "enumeration count types")
    c.ok(enum == {"mu_values":[str(x) for x in mus],"triangular_cells":8,"collinear_cells":24,"critical_cells":1,"boundary_cells":5}, "enumeration value")
    mp.mp.dps = 90
    tri = data["triangular_cells"]; c.ok(type(tri) is list and len(tri) == 8, "triangle list")
    seen_mu = set()
    for i, row in enumerate(tri):
        exact_keys(c, row, TRI, f"triangle {i}"); muq = rat(c,row["mu"],f"triangle {i} mu"); c.ok(muq in mus and muq not in seen_mu,f"triangle {i} key"); seen_mu.add(muq)
        rr=27*muq*(1-muq); dd=1-rr
        c.ok(rat(c,row["routh_parameter"],"routh") == rr,"routh value"); c.ok(rat(c,row["routh_discriminant"],"disc") == dd,"disc value")
        c.ok(rat(c,row["charpoly_constant"],"constant") == rr/4,"constant value"); c.ok(row["lambda_square_sum"] == "-1" and rat(c,row["lambda_square_product"],"product") == rr/4,"z roots")
        expected = "bounded_elliptic" if dd>0 else "unstable_hamiltonian_quartet"
        c.ok(row["linear_type"] == expected and type(row["linearly_stable"]) is bool and row["linearly_stable"] is (dd>0),"triangle regime")
        mu=mp.mpf(muq.numerator)/muq.denominator; oxx=mp.mpf(3)/4; oyy=mp.mpf(9)/4
        for sign in (-1, 1):
            oxy=sign*3*mp.sqrt(3)*(1-2*mu)/4
            M=raw_matrix(oxx,oyy,oxy); a=-sum((M*M)[j,j] for j in range(4))/2; determinant=mp.det(M)
            c.ok(abs(a-1)<mp.mpf("1e-75"),f"raw lambda2 sign {sign}"); c.ok(abs(determinant-mp.mpf(rr.numerator)/rr.denominator/4)<mp.mpf("1e-75"),f"raw determinant sign {sign}")
            eig=mp.eig(M,left=False,right=False)
            if dd>0: c.ok(max(abs(mp.re(z)) for z in eig)<mp.mpf("1e-70"),f"elliptic spectrum sign {sign}")
            else: c.ok(max(mp.re(z) for z in eig)>mp.mpf("1e-10"),f"quartet spectrum sign {sign}")
    c.ok(seen_mu == set(mus),"triangle grid")

    cols=data["collinear_cells"]; c.ok(type(cols) is list and len(cols)==24,"collinear list"); seen=set()
    for i,row in enumerate(cols):
        exact_keys(c,row,COL,f"collinear {i}"); muq=rat(c,row["mu"],"col mu"); point=row["point"]; key=(muq,point)
        c.ok(muq in mus and point in {"L1","L2","L3"} and key not in seen,"col key"); seen.add(key)
        c.ok(row["interval"] == {"L3":"(-infinity,-mu)","L1":"(-mu,1-mu)","L2":"(1-mu,infinity)"}[point],"interval")
        for name in ("x","omega_x_residual","S","lambda2_coefficient","constant_coefficient"): c.ok(type(row[name]) is str,"decimal type")
        mu=mp.mpf(muq.numerator)/muq.denominator; x=root_bisect(mu,point); stored=mp.mpf(row["x"]); c.ok(abs(stored-x)<mp.mpf("1e-58"),"independent root")
        def f(xx): return xx-(1-mu)*(xx+mu)/abs(xx+mu)**3-mu*(xx-1+mu)/abs(xx-1+mu)**3
        c.ok(abs(f(stored))<mp.mpf("1e-55") and abs(mp.mpf(row["omega_x_residual"]))<mp.mpf("1e-55"),"root residual")
        S=(1-mu)/abs(stored+mu)**3+mu/abs(stored-1+mu)**3; c.ok(S>1,"S>1"); c.ok(abs(S-mp.mpf(row["S"]))<mp.mpf("1e-58"),"S value")
        a=2-S; constant=1+S-2*S*S
        c.ok(abs(a-mp.mpf(row["lambda2_coefficient"]))<mp.mpf("1e-58"),"lambda2 value"); c.ok(abs(constant-mp.mpf(row["constant_coefficient"]))<mp.mpf("1e-56"),"constant value")
        c.ok(row["linear_type"]=="saddle_times_center" and row["linearly_stable"] is False,"col type")
        M=raw_matrix(1+2*S,1-S,mp.mpf(0)); raw_a=-sum((M*M)[j,j] for j in range(4))/2
        c.ok(abs(raw_a-a)<mp.mpf("1e-70") and abs(mp.det(M)-constant)<mp.mpf("1e-70"),"raw col charpoly")
        eig=mp.eig(M,left=False,right=False); c.ok(sum(abs(mp.im(z))<mp.mpf("1e-60") for z in eig)==2 and sum(abs(mp.re(z))<mp.mpf("1e-60") for z in eig)==2,"saddle center spectrum")
    c.ok(seen == {(mu,p) for mu in mus for p in ("L3","L1","L2")},"complete col grid")

    crit=data["critical_cell"]; exact_keys(c,crit,CRIT,"critical")
    c.ok(type(crit["eigenvalues"]) is list and all(type(v) is str for v in crit["eigenvalues"]), "critical eigenvalue types")
    c.ok(type(crit["algebraic_multiplicity_each"]) is int and type(crit["geometric_multiplicity_each"]) is int, "critical multiplicity types")
    c.ok(all(type(crit[key]) is bool for key in ("defective","linear_growth","linearly_stable")), "critical boolean types")
    expected_rank_cells=[
        {"point":point,"mixed_hessian_sign":sign,"eigenvalue":eigenvalue,"matrix_rank":3,"geometric_multiplicity":1}
        for point,sign in (("L4",1),("L5",-1))
        for eigenvalue in ("-i/sqrt(2)","i/sqrt(2)")
    ]
    expected_crit={"mu_formula":"(1-sqrt(23/27))/2","routh_parameter":"1","charpoly":"lambda^4+lambda^2+1/4=(lambda^2+1/2)^2","eigenvalues":["-i/sqrt(2)","i/sqrt(2)"],"algebraic_multiplicity_each":2,"geometric_multiplicity_each":1,"rank_cells":expected_rank_cells,"defective":True,"linear_growth":True,"linearly_stable":False}
    c.ok(crit==expected_crit,"critical values")
    rank_cells=crit["rank_cells"]; c.ok(type(rank_cells) is list and len(rank_cells)==4,"critical rank list")
    mu=(1-sp.sqrt(sp.Rational(23,27)))/2; oxx=sp.Rational(3,4); oyy=sp.Rational(9,4); lam=sp.Symbol("z")
    seen_rank=set()
    eigenvalue_map={"-i/sqrt(2)":-sp.I/sp.sqrt(2),"i/sqrt(2)":sp.I/sp.sqrt(2)}
    for i,row in enumerate(rank_cells):
        exact_keys(c,row,CRIT_RANK,f"critical rank {i}")
        c.ok(type(row["point"]) is str and type(row["mixed_hessian_sign"]) is int and type(row["eigenvalue"]) is str,"critical rank primitive types")
        c.ok(type(row["matrix_rank"]) is int and type(row["geometric_multiplicity"]) is int,"critical rank integer types")
        key=(row["point"],row["mixed_hessian_sign"],row["eigenvalue"]); c.ok(key not in seen_rank,"critical rank unique"); seen_rank.add(key)
        c.ok(row==expected_rank_cells[i],"critical rank exact row")
        oxy=row["mixed_hessian_sign"]*3*sp.sqrt(3)*(1-2*mu)/4
        M=sp.Matrix([[0,0,1,0],[0,0,0,1],[oxx,oxy,0,2],[oxy,oyy,-2,0]])
        ev=eigenvalue_map[row["eigenvalue"]]; rank=(M-ev*sp.eye(4)).rank()
        c.ok(sp.simplify(M.charpoly(lam).as_expr()-(lam**2+sp.Rational(1,2))**2)==0,f"critical charpoly {key}")
        c.ok(rank==row["matrix_rank"]==3 and 4-rank==row["geometric_multiplicity"]==1,f"critical geometric multiplicity {key}")
    c.ok(seen_rank=={(point,sign,eigenvalue) for point,sign in (("L4",1),("L5",-1)) for eigenvalue in eigenvalue_map},"critical rank complete")

    expected_boundaries=[
        {"name":"zero_mass","parameters":{"mu":"0"},"conclusion":"excluded degenerate limit; the unit circle is a continuum of rotating Kepler equilibria"},
        {"name":"equal_masses","parameters":{"mu":"1/2"},"conclusion":"included endpoint; L4 and L5 have an unstable Hamiltonian quartet"},
        {"name":"collisions","parameters":{"positions":"(-mu,0),(1-mu,0)"},"conclusion":"removed singular configurations and never counted as equilibria"},
        {"name":"critical_defect","parameters":{"mu":"mu_R"},"conclusion":"spectrally imaginary but defective with linear growth; not linearly stable"},
        {"name":"claim_level","parameters":{"chamber":"0<mu<mu_R"},"conclusion":"bounded linearized flow including resonant ratios; no nonlinear resonance, bifurcation, or KAM conclusion"},
    ]
    c.ok(type(data["boundary_cells"]) is list and data["boundary_cells"]==expected_boundaries,"boundaries")
    c.ok(type(data["references"]) is list and data["references"]==REFERENCES,"references")
    c.ok(type(data["nonclaims"]) is list and data["nonclaims"]==NONCLAIMS,"nonclaims")
    print(f"C290 independent raw-Jacobian checker: PASS ({c.n} assertions; strict duplicate-rejecting schema)")


if __name__ == "__main__": main()
