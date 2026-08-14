#!/usr/bin/env python3
"""Independent fail-closed checker for HCS-C53."""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import sys


PROJECT = Path(__file__).resolve().parents[1]
REPO = Path(__file__).resolve().parents[3]
C51_PATH = REPO / "henon_dynamics/henon_mu3_weight_clock_bifurcation/results/c51_certificate.json"
C52_PATH = REPO / "henon_dynamics/henon_mu3_d12_calabi_yau_core_projector/results/c52_certificate.json"
EXPECTED_PAYLOAD_SHA256 = "8064224eda63fa9d890efd26ec9aa167c7cd9458662620be3135196a09494d41"
EXPECTED_SCHEMA_SHA256 = "e49a9e954c2bc4543ef356a31405a02cd1fa80ad01f44aab4e717b8570583937"
EXPECTED_C52_SHA256 = "a2b0b281bfb311f979c7ed65e441a184ebe338b05f5fec8a60768610965c9c94"
EXPECTED_C51_SHA256 = "daffc0070d06258d3a4c8f5613c9d54a816eb2203be41aa045dbbe05c0e3d593"
EXPECTED_C52_IMPLEMENTATION_COMMIT = "208feef86365cd92ace8dad02904acff6623eeec"


Pair = tuple[Fraction,Fraction]
ZERO: Pair = (Fraction(0),Fraction(0))
ONE: Pair = (Fraction(1),Fraction(0))
RHO: Pair = (Fraction(0),Fraction(1))
THETA: Pair = (Fraction(1),Fraction(2))
ONE_PLUS_RHO: Pair = (Fraction(1),Fraction(1))


def pair_add(left:Pair,right:Pair)->Pair:
    return left[0]+right[0],left[1]+right[1]


def pair_neg(value:Pair)->Pair:
    return -value[0],-value[1]


def pair_sub(left:Pair,right:Pair)->Pair:
    return pair_add(left,pair_neg(right))


def pair_mul(left:Pair,right:Pair)->Pair:
    a,b=left;c,d=right
    return a*c-b*d,a*d+b*c-b*d


def pair_tau(value:Pair)->Pair:
    a,b=value
    return a-b,-b


def pair_inv(value:Pair)->Pair:
    a,b=value
    norm=a*a-a*b+b*b
    if norm==0: raise ZeroDivisionError
    return (a-b)/norm,-b/norm


def pair_div(left:Pair,right:Pair)->Pair:
    return pair_mul(left,pair_inv(right))


def pair_pow(value:Pair,exponent:int)->Pair:
    out=ONE;base=value
    while exponent:
        if exponent&1:out=pair_mul(out,base)
        base=pair_mul(base,base);exponent//=2
    return out


def pair_string(value:Pair)->str:
    return f"{value[0]}+({value[1]})*rho"


def canonical_json(value)->str:
    return json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False)


def sha256_bytes(data:bytes)->str:
    return hashlib.sha256(data).hexdigest()


def reject_duplicate_pairs(pairs):
    value={}
    for key,item in pairs:
        if key in value:
            raise ValueError(f"duplicate JSON key: {key}")
        value[key]=item
    return value


def strict_json_loads(raw:bytes):
    return json.loads(raw,object_pairs_hook=reject_duplicate_pairs)


def strict_equal(left,right)->bool:
    if type(left) is not type(right): return False
    if isinstance(left,dict):
        return set(left)==set(right) and all(strict_equal(left[k],right[k]) for k in left)
    if isinstance(left,list):
        return len(left)==len(right) and all(strict_equal(a,b) for a,b in zip(left,right))
    return left==right


def schema_descriptor(value):
    """Recursively lock every key, container shape, and exact Python JSON type."""
    if type(value) is dict:
        return ["dict", [[key, schema_descriptor(value[key])] for key in sorted(value)]]
    if type(value) is list:
        return ["list", len(value), [schema_descriptor(item) for item in value]]
    if type(value) is bool:
        return "bool"
    if type(value) is int:
        return "int"
    if type(value) is float:
        return "float"
    if type(value) is str:
        return "str"
    if value is None:
        return "null"
    return f"forbidden:{type(value).__name__}"


def poly_add(left,right):
    out=dict(left)
    for exponent,coefficient in right.items():
        out[exponent]=pair_add(out.get(exponent,ZERO),coefficient)
        if out[exponent]==ZERO:del out[exponent]
    return out


def poly_scale(poly,scalar:Pair):
    return {exponent:pair_mul(coefficient,scalar) for exponent,coefficient in poly.items() if pair_mul(coefficient,scalar)!=ZERO}


def poly_mul(left,right):
    out={}
    for ea,ca in left.items():
        for eb,cb in right.items():
            exponent=tuple(a+b for a,b in zip(ea,eb))
            out[exponent]=pair_add(out.get(exponent,ZERO),pair_mul(ca,cb))
    return {e:c for e,c in out.items() if c!=ZERO}


def poly_pow(poly,exponent:int):
    dimension=len(next(iter(poly)))
    out={(0,)*dimension:ONE};base=poly
    while exponent:
        if exponent&1:out=poly_mul(out,base)
        base=poly_mul(base,base);exponent//=2
    return out


def linear_form(coefficients:list[Pair]):
    dimension=len(coefficients);out={}
    for index,coefficient in enumerate(coefficients):
        if coefficient!=ZERO:
            exponent=[0]*dimension;exponent[index]=1
            out[tuple(exponent)]=coefficient
    return out


def matrix_mul(left,right):
    rows=len(left);middle=len(right);columns=len(right[0])
    assert len(left[0])==middle
    return [[sum_pairs(pair_mul(left[i][k],right[k][j]) for k in range(middle)) for j in range(columns)] for i in range(rows)]


def sum_pairs(values):
    out=ZERO
    for value in values:out=pair_add(out,value)
    return out


def matrix_det(matrix:list[list[Pair]])->Pair:
    rows=[list(row) for row in matrix];n=len(rows);det=ONE
    for column in range(n):
        pivot=next((i for i in range(column,n) if rows[i][column]!=ZERO),None)
        if pivot is None:return ZERO
        if pivot!=column:
            rows[pivot],rows[column]=rows[column],rows[pivot];det=pair_neg(det)
        pivot_value=rows[column][column];det=pair_mul(det,pivot_value)
        inverse=pair_inv(pivot_value)
        rows[column]=[pair_mul(inverse,value) for value in rows[column]]
        for i in range(column+1,n):
            factor=rows[i][column]
            if factor==ZERO:continue
            rows[i]=[pair_sub(left,pair_mul(factor,right)) for left,right in zip(rows[i],rows[column])]
    return det


def all_n_independent(n:int)->dict:
    N=2*n
    labels=["u0"]
    for i in range(1,n):labels.extend([f"u{i}",f"v{i}"])
    labels.append(f"u{n}")
    index={label:i for i,label in enumerate(labels)}
    B=[[ZERO for _ in range(N)] for _ in range(N)]
    B[0][index["u0"]]=ONE
    for i in range(1,n):
        u=index[f"u{i}"];v=index[f"v{i}"]
        B[i][u]=ONE;B[i][v]=THETA
        factor=RHO if i%2==0 else ONE
        B[N-i][u]=factor;B[N-i][v]=pair_neg(pair_mul(factor,THETA))
    B[n][index[f"u{n}"]]=ONE if n%2 else ONE_PLUS_RHO
    determinant=matrix_det(B)
    assert determinant!=ZERO
    determinant_closed=pair_mul(
        pair_mul(pair_pow((Fraction(2),Fraction(4)),n-1),pair_pow(RHO,(n-1)//2)),
        ONE if n%2 else ONE_PLUS_RHO,
    )
    assert determinant==determinant_closed

    permutation=[(-i)%N for i in range(N)]
    phases=[1 if i!=0 and i%2==0 else 0 for i in range(N)]
    M=[[ZERO for _ in range(N)] for _ in range(N)]
    for i in range(N):M[i][permutation[i]]=pair_pow(RHO,phases[i])
    tau_B=[[pair_tau(value) for value in row] for row in B]
    assert matrix_mul(M,tau_B)==B
    assert all(permutation[permutation[i]]==i for i in range(N))
    assert all((phases[i]+2*phases[permutation[i]])%3==0 for i in range(N))

    forms=[linear_form(row) for row in B]
    C0={}
    for form in forms:C0=poly_add(C0,poly_pow(form,3))
    Qsub={}
    for i in range(N-1):Qsub=poly_add(Qsub,poly_mul(forms[i],forms[i+1]))
    Qsub=poly_add(Qsub,poly_scale(poly_mul(forms[N-1],forms[0]),RHO))
    Q0=poly_scale(Qsub,pair_neg(RHO))
    assert all(coefficient[1]==0 for coefficient in C0.values())
    assert all(coefficient[1]==0 for coefficient in Q0.values())

    # Independently check M on source polynomials by monomial substitution.
    Mforms=[]
    for i in range(N):
        coefficients=[ZERO]*N;coefficients[permutation[i]]=pair_pow(RHO,phases[i]);Mforms.append(linear_form(coefficients))
    Cmapped={}
    for form in Mforms:Cmapped=poly_add(Cmapped,poly_pow(form,3))
    Csource={}
    for i in range(N):
        coefficients=[ZERO]*N;coefficients[i]=ONE;Csource=poly_add(Csource,poly_pow(linear_form(coefficients),3))
    assert Cmapped==Csource
    Qmapped={}
    for i in range(N-1):Qmapped=poly_add(Qmapped,poly_mul(Mforms[i],Mforms[i+1]))
    Qmapped=poly_add(Qmapped,poly_scale(poly_mul(Mforms[-1],Mforms[0]),RHO))
    Qtau={}
    source_forms=[]
    for i in range(N):
        coefficients=[ZERO]*N;coefficients[i]=ONE;source_forms.append(linear_form(coefficients))
    for i in range(N-1):Qtau=poly_add(Qtau,poly_mul(source_forms[i],source_forms[i+1]))
    Qtau=poly_add(Qtau,poly_scale(poly_mul(source_forms[-1],source_forms[0]),pair_tau(RHO)))
    assert Qmapped==poly_scale(Qtau,RHO)

    def canonical_terms(poly):
        rows=[]
        for exponents in sorted(poly,reverse=True):
            coefficient=poly[exponents];assert coefficient[1]==0
            q=coefficient[0]
            rows.append({"exponents":list(exponents),"coefficient":{"numerator":q.numerator,"denominator":q.denominator}})
        return rows
    Cterms=canonical_terms(C0);Qterms=canonical_terms(Q0)
    exponent=Fraction(4,n)
    return {
        "n":n,"N":N,"variable_order":labels,"M_permutation":permutation,"M_phase_exponents":phases,
        "center_factor":"1" if n%2 else "1+rho","det_B":pair_string(determinant),
        "det_B_closed_formula_matches":True,
        "C0_monomial_count":len(Cterms),"Q0_monomial_count":len(Qterms),
        "C0_terms_sha256":sha256_bytes(canonical_json(Cterms).encode()),
        "Q0_terms_sha256":sha256_bytes(canonical_json(Qterms).encode()),
        "C_M_identity":True,"Q_M_identity":True,"cocycle_identity":True,"B_fixed_identity":True,
        "rational_coefficients":True,"Q_split_exponent":{"numerator":exponent.numerator,"denominator":exponent.denominator},
        "denominator_after_Q_descent":n//math.gcd(n,4),
        "source_geometry_scope":"CERTIFIED_SMOOTH" if n in (2,3,4) else "ALGEBRAIC_FORM_ONLY_SMOOTHNESS_OPEN",
    }


def monomial_map(row):
    return tuple(row["permutation_output_to_input"]),tuple(row["rho_phase_exponents"])


def compose(left,right):
    p,e=left;q,f=right
    return tuple(q[p[i]] for i in range(8)),tuple((e[i]+f[p[i]])%3 for i in range(8))


def normalize(item):
    p,e=item;c=e[0]
    return p,tuple((x-c)%3 for x in e)


def tau_map(item):p,e=item;return p,tuple(2*x%3 for x in e)


def inverse_map(item):
    p,e=item;pinv=[0]*8
    for i,j in enumerate(p):pinv[j]=i
    return tuple(pinv),tuple((-e[pinv[j]])%3 for j in range(8))


def independent_group_expected(c52_payload):
    group=c52_payload["projective_monomial_group"];elements=group["elements"];mul=group["multiplication_table_by_id"]
    M=((0,7,6,5,4,3,2,1),(0,0,1,0,1,0,1,0));lookup={normalize(monomial_map(row)):row["id"] for row in elements}
    Minv=inverse_map(M);assert Minv==tau_map(M)
    alpha=[]
    for row in elements:alpha.append(lookup[normalize(compose(compose(M,tau_map(monomial_map(row))),Minv))])
    assert sorted(alpha)==list(range(24));tests=0
    for i in range(24):
        for j in range(24):assert alpha[mul[i][j]]==mul[alpha[i]][alpha[j]];tests+=1
    r=next(row for row in elements if row["normal_form"]=={"kind":"rotation","exponent":1})
    s=next(row for row in elements if row["normal_form"]=={"kind":"reflection","exponent":0})
    assert alpha[r["id"]]==group["inverse_ids"][r["id"]]
    assert alpha[s["id"]]==mul[s["id"]][group["inverse_ids"][r["id"]]]
    inners=set()
    for h in range(24):
        hinv=group["inverse_ids"][h];inners.add(tuple(mul[mul[h][g]][hinv] for g in range(24)))
    assert tuple(alpha) not in inners
    fixed=[i for i,j in enumerate(alpha) if i==j];orbits=[];unseen=set(range(24))
    while unseen:
        seed=min(unseen);orbit=[];current=seed
        while current not in orbit:orbit.append(current);unseen.discard(current);current=alpha[current]
        orbits.append(orbit)
    return {
        "scheme":"nonconstant finite-etale Q-form mathscrG","rank_over_Q":24,"base_change_to_K":"constant Dih(C12)_K",
        "splitting_field":"K=Q(rho)","Galois_alpha_id_map":alpha,"Galois_orbits":orbits,
        "Q_rational_geometric_element_ids":fixed,"Q_rational_geometric_element_normal_forms":[elements[i]["normal_form"] for i in fixed],
        "generator_r_id":r["id"],"generator_s_id":s["id"],"alpha_r":"r^(-1)","alpha_s":"s*r^(-1)",
        "alpha_s_equivalent_normal_form":"r*s",
        "outer_twist":True,"constant_group_scheme":False,"all_24_graphs_Galois_permuted":True,
        "group_table_automorphism_tests":tests,"individual_24_Q_automorphisms_claimed":False,"Reynolds_sum_Galois_stable":True,
    }


def add_gate(gates,name,condition,detail):
    gates.append({"name":name,"status":"PASS" if condition else "FAIL","detail":detail})


def main()->int:
    parser=argparse.ArgumentParser();parser.add_argument("certificate",type=Path);parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args();gates=[]
    try:raw=args.certificate.read_bytes();certificate=strict_json_loads(raw)
    except Exception as error:
        result={"schema":"hcs-c53-check-v1","all_pass":False,"gate_count":1,"pass_count":0,"gates":[{"name":"strict_json_parse","status":"FAIL","detail":str(error)}]}
        args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n");return 1
    payload=certificate.get("payload") if type(certificate) is dict else None
    envelope=(type(certificate) is dict and set(certificate)=={"schema","payload","payload_sha256"} and
              certificate.get("schema")=="hcs-c53-certificate-v1" and type(payload) is dict and
              type(certificate.get("payload_sha256")) is str and len(certificate["payload_sha256"])==64 and
              all(character in "0123456789abcdef" for character in certificate["payload_sha256"]))
    add_gate(gates,"schema",envelope,"exact top-level keys and exact envelope types")
    computed_hash=sha256_bytes(canonical_json(payload).encode()) if type(payload) is dict else ""
    add_gate(gates,"payload_hash",computed_hash==certificate.get("payload_sha256"),"canonical payload digest")
    add_gate(gates,"frozen_expected_payload",computed_hash==EXPECTED_PAYLOAD_SHA256,"independent frozen full-payload digest")
    computed_schema_hash=sha256_bytes(canonical_json(schema_descriptor(payload)).encode()) if type(payload) is dict else ""
    add_gate(gates,"recursive_schema",computed_schema_hash==EXPECTED_SCHEMA_SHA256,"recursive keys, list shapes, and exact JSON scalar types")

    try:
        passport=payload["material_passport"]
        add_gate(gates,"passport",strict_equal(passport,{
            "candidate_id":"HCS-C53","project_slug":"henon_mu3_dihedral_core_rational_descent",
            "artifact_status":"RELEASE_CANDIDATE",
            "implemented_blocks":["B0_ALL_N_DESCENT","B1_EXPLICIT_N4_MODEL","B2_TWISTED_DIHEDRAL_CHOW_DESCENT","B3_COMPATIBLE_LOCAL_FACTORS"],
        }),"candidate, status, and implemented block contract")
    except Exception as error:add_gate(gates,"passport",False,str(error))

    try:
        c51raw=C51_PATH.read_bytes();c52raw=C52_PATH.read_bytes();c51=strict_json_loads(c51raw);c52=strict_json_loads(c52raw)
        locks=payload["source_lock"]
        condition=(sha256_bytes(c51raw)==EXPECTED_C51_SHA256 and sha256_bytes(c52raw)==EXPECTED_C52_SHA256 and
                   locks["C52_implementation_commit"]==EXPECTED_C52_IMPLEMENTATION_COMMIT and
                   locks["certificates"][0]["sha256"]==EXPECTED_C51_SHA256 and locks["certificates"][1]["sha256"]==EXPECTED_C52_SHA256 and
                   c51["payload_sha256"]==locks["certificates"][0]["payload_sha256"] and c52["payload_sha256"]==locks["certificates"][1]["payload_sha256"])
        add_gate(gates,"source_lock",condition,"C51/C52 bytes, payloads, and C52 implementation commit")
    except Exception as error:add_gate(gates,"source_lock",False,f"dependency failure: {error}");c52={"payload":{}}

    try:
        expected_controls=[all_n_independent(n) for n in range(2,11)]
        all_n=payload["B0_all_n_algebraic_descent"]
        actual_controls=all_n["exact_controls_n2_to_n10"]
        add_gate(gates,"all_n_exact_descent",strict_equal(actual_controls,expected_controls),"custom Q(rho) pair-polynomial replay n=2..10")
        expected_contract={
            "range":"every integer n>=2","N":"2n",
            "source_equations":{"C_n":"sum_(i=0)^(2n-1) x_i^3",
                                "Q_n_rho":"sum_(i=0)^(2n-2) x_i*x_(i+1)+rho*x_(2n-1)*x_0",
                                "chronological_closing_edge_preserved":True},
            "descent_data":{"tau":"tau(rho)=rho^2=-rho-1","theta":"theta=1+2rho; tau(theta)=-theta",
                            "sigma":"sigma(i)=-i mod 2n",
                            "phase_rule":"e_0=0; e_i=1 for nonzero even i and 0 for odd i",
                            "M_formula":"(M_n x)_i=rho^(e_i)*x_(sigma(i))",
                            "identities":["C_n(M_n x)=C_n(x)","Q_n,rho(M_n x)=rho*Q_n,rho^2(x)","M_n*tau(M_n)=I"]},
            "rational_forms":{"C0_formula":"u0^3+sum_(i=1)^(n-1)(2u_i^3-18u_i*v_i^2)+(-1)^(n+1)u_n^3",
                              "Q0_formula":"u0u1+3u0v1+sum_(i=1)^(n-2)(u_i*u_(i+1)+3u_i*v_(i+1)+3u_(i+1)*v_i-3v_i*v_(i+1))+terminal_n",
                              "terminal_odd_n":"u_(n-1)u_n+3u_n*v_(n-1)","terminal_even_n":"2u_(n-1)u_n",
                              "base_change":"C_n(B_nu)=C0_n(u); Q_n,rho(B_nu)=(1+rho)Q0_n(u)"},
        }
        add_gate(gates,"all_n_contract",all(strict_equal(all_n[key],value) for key,value in expected_contract.items()),
                 "source-ordered forms, phases, cocycle, and rational formulas")
        expected_fixed={
            "theta":"1+2rho","x0":"u0",
            "pair_odd_i":"x_i=u_i+theta*v_i; x_(2n-i)=u_i-theta*v_i",
            "pair_even_i":"x_i=u_i+theta*v_i; x_(2n-i)=rho*(u_i-theta*v_i)",
            "center_odd_n":"x_n=u_n","center_even_n":"x_n=(1+rho)*u_n",
            "fixed_identity":"M_n*tau(B_n)=B_n",
            "determinant_closed_formula":"det(B_n)=(2theta)^(n-1)*rho^floor((n-1)/2)*c_n, with c_n=1 for odd n and c_n=1+rho for even n",
            "determinant_nonzero_all_n":True,
        }
        expected_scope={"algebraic_descent_all_n":True,"source_ordered_smoothness_all_n_claimed":False,
                        "certified_smooth_motivic_rows":[2,3,4],"rows_5_to_10":"formula controls only"}
        add_gate(gates,"all_n_theorem_scope",strict_equal(all_n["fixed_basis"],expected_fixed) and
                 strict_equal(all_n["scope"],expected_scope),"closed determinant theorem and smoothness firewall")
    except Exception as error:
        add_gate(gates,"all_n_exact_descent",False,f"independent replay failure: {error}")
        add_gate(gates,"all_n_contract",False,f"contract failure: {error}")
        add_gate(gates,"all_n_theorem_scope",False,f"scope failure: {error}")

    try:
        expected_M={"permutation_output_to_input":[0,7,6,5,4,3,2,1],"rho_phase_exponents":[0,0,1,0,1,0,1,0],
                    "coordinate_formula":["x0","x7","rho*x6","x5","rho*x4","x3","rho*x2","x1"],
                    "C_identity":"C(Mx)=C(x)","Q_identity":"Q_rho(Mx)=rho*Q_rho2(x)","cocycle":"M*tau(M)=I8"}
        model=payload["B1_explicit_n4_Q_model"]
        expected_Q_model={
            "variable_order":["u0","u1","v1","u2","v2","u3","v3","u4"],"theta":"theta=1+2rho",
            "x_equals_Bu":["u0","u1+theta*v1","u2+theta*v2","u3+theta*v3","(1+rho)*u4",
                           "u3-theta*v3","rho*(u2-theta*v2)","u1-theta*v1"],
            "det_B":"24*theta=24+48rho",
            "C0":"u0**3 + 2*u1**3 - 18*u1*v1**2 + 2*u2**3 - 18*u2*v2**2 + 2*u3**3 - 18*u3*v3**2 - u4**3",
            "Q0":"u0*u1 + 3*u0*v1 + u1*u2 + 3*u1*v2 + u2*u3 + 3*u2*v1 + 3*u2*v3 + 2*u3*u4 + 3*u3*v2 - 3*v1*v2 - 3*v2*v3",
            "base_change":{"C":"C(Bu)=C0(u)","Q":"Q_rho(Bu)=(1+rho)*Q0(u)"},
        }
        add_gate(gates,"n4_explicit_model",strict_equal(model["K_model"],c52["payload"]["frozen_model"]) and
                 strict_equal(model["descent_M"],expected_M) and strict_equal(model["Q_model"],expected_Q_model) and
                 model["smoothness"]=="PROVED_BY_BASE_CHANGE_TO_C50_SMOOTH_K_MODEL" and model["degree"]==6 and model["dimension"]==5,
                 "explicit M, B determinant, C0 and Q0")
    except Exception as error:add_gate(gates,"n4_explicit_model",False,str(error))

    try:
        expected_group=independent_group_expected(c52["payload"])
        actual_group=payload["B2_twisted_dihedral_Chow_descent"]["group_scheme"]
        flattened=[element for orbit in actual_group["Galois_orbits"] for element in orbit]
        orbit_partition=(len(flattened)==24 and sorted(flattened)==list(range(24)) and
                         all(len(orbit) in (1,2) and len(set(orbit))==len(orbit) for orbit in actual_group["Galois_orbits"]))
        structural_keys={"Galois_alpha_id_map","Galois_orbits","generator_r_id","generator_s_id","alpha_r","alpha_s",
                         "alpha_s_equivalent_normal_form","all_24_graphs_Galois_permuted","group_table_automorphism_tests",
                         "Reynolds_sum_Galois_stable"}
        form_keys=set(actual_group)-structural_keys
        structural_match=(set(expected_group)==set(actual_group) and
                          all(strict_equal(actual_group[key],expected_group[key]) for key in structural_keys))
        form_match=all(strict_equal(actual_group[key],expected_group[key]) for key in form_keys)
        add_gate(gates,"twisted_group_scheme",structural_match and orbit_partition,"all 24 graphs, 576 multiplication pairs, and disjoint Galois orbits")
        add_gate(gates,"nonconstant_outer_twist",form_match,"nonconstant finite-etale form, only two fixed geometric elements")
    except Exception as error:
        add_gate(gates,"twisted_group_scheme",False,str(error));add_gate(gates,"nonconstant_outer_twist",False,str(error))

    try:
        block=payload["B2_twisted_dihedral_Chow_descent"]
        projectors=block["projectors"];motives=block["motives_over_Q"]
        expected_projectors={
            "pi5":"Delta_X0-sum_(i=0)^5 (1/6)h^(5-i) cross h^i",
            "e_mathscrG":"(1/24)sum_(g in mathscrG_K)[Gamma_g]","Reynolds_denominator":24,
            "Galois_stability":"alpha permutes all 24 graph cycles",
            "descent_mechanism":"restriction/corestriction with Q coefficients","quadratic_descent_transfer_denominator":2,
            "Reynolds_and_field_transfer_denominators_not_conflated":True,
            "pi_core0":"pi5*e_mathscrG","pi_level0":"pi5-pi_core0","raw_eG_called_middle_rank10":False,
        }
        expected_motives={
            "raw_middle":"(X0,pi5)","normalized_O4":"(X0,pi5,2)",
            "raw_core_M0":"M0=(X0,pi_core0), weight 5","CY_type_core":"M0(1), weight 3",
            "source_normalized_core":"M0(2), weight 1","source_normalized_level":"(X0,pi_level0,2), weight 1",
            "core_rank":10,"level_rank":158,"rank_sum":168,
            "raw_M0_Hodge":[{"p":1,"q":4,"multiplicity":1},{"p":2,"q":3,"multiplicity":4},{"p":3,"q":2,"multiplicity":4},{"p":4,"q":1,"multiplicity":1}],
            "CY_type_M0_twist1_Hodge":[{"p":0,"q":3,"multiplicity":1},{"p":1,"q":2,"multiplicity":4},{"p":2,"q":1,"multiplicity":4},{"p":3,"q":0,"multiplicity":1}],
            "source_normalized_M0_twist2_Hodge":[{"p":-1,"q":2,"multiplicity":1},{"p":0,"q":1,"multiplicity":4},{"p":1,"q":0,"multiplicity":4},{"p":2,"q":-1,"multiplicity":1}],
            "raw_level_Hodge_summary":[0,79,79,0],"same_projectors_Betti_deRham_all_ell":True,
        }
        condition=(strict_equal(projectors,expected_projectors) and strict_equal(motives,expected_motives))
        add_gate(gates,"descended_Chow_projectors",condition,"pi5 eG and rank 10+158 motives over Q")
    except Exception as error:add_gate(gates,"descended_Chow_projectors",False,str(error))

    try:
        local=payload["B3_compatible_local_factors"];rawblock=local["raw_core"];normalized=local["normalized_core"]
        condition=(rawblock["motive"]=="M0=(X0,pi_core0)" and rawblock["rank"]==10 and rawblock["weight"]==5 and
                   rawblock["frobenius_convention"]=="geometric Frobenius F_p; F_p acts on Q_l(-1) by p" and
                   rawblock["characteristic_polynomial"]=="chi_p(U)=det(U-F_p|M0_ell)" and rawblock["characteristic_polynomial_monic"] is True and
                   rawblock["good_local_polynomial"]=="P_p_raw(T)=det(1-F_p*T|M0_ell)=T^10*chi_p(T^(-1))" and
                   rawblock["good_local_polynomial_called_monic"] is False and rawblock["coefficients"]=="Z[T]" and rawblock["ell_independent"] is True and
                   rawblock["Q_coefficient_step"]=="algebraic-correspondence traces are ell-independent intersection numbers; Newton identities give the monic chi_p(U) in Q[U]" and
                   rawblock["Z_integrality_step"]=="the roots of monic chi_p(U) are algebraic integers; chi_p in Q[U] therefore lies in Z[U] by Gauss lemma, and coefficient reversal gives P_p_raw in Z[T]" and
                   rawblock["two_step_integrality_argument"] is True and strict_equal(normalized,{
                       "motive":"C4=M0(2)","rank":10,"weight":1,
                       "Frobenius_on_twist2":"F_C4=F_M0/p^2 under the geometric convention",
                       "local_polynomial":"P_p_C4(T)=P_p_raw(T/p^2)",
                       "coefficients":"Q[T] generally, not claimed integral"}))
        add_gate(gates,"compatible_raw_local_factors",condition,"geometric Frobenius, monic chi, Gauss integrality, coefficient reversal, and normalized twist")
        expected_reciprocity={"projector_self_transpose":True,"kernel_equals_image_orthogonal":True,
                              "restricted_pairing_nondegenerate":True,"Frobenius_commutes_with_projector":True,
                              "Frobenius_similitude_multiplier":"p^5","eigenvalue_pairing":"alpha <-> p^5/alpha"}
        add_gate(gates,"reciprocity_pairing",rawblock["reciprocity"]=="a_(10-k)=p^(25-5k)*a_k" and
                 strict_equal(rawblock["reciprocity_mechanism"],expected_reciprocity),
                 "self-transpose projector gives a nondegenerate p^5-similitude pairing")
    except Exception as error:
        add_gate(gates,"compatible_raw_local_factors",False,str(error))
        add_gate(gates,"reciprocity_pairing",False,str(error))

    try:
        local=payload["B3_compatible_local_factors"];packets=local["Q_packets"];split=local["split_prime"];exponents=local["all_n_split_exponent"]
        expected_packets={"E4_Q":"Q(0) plus H6_prim(Fermat_cubic_sixfold)(3)","E4_rank":87,
                          "O4_Q":"(X0,pi5,2)","O4_rank":168,"O4_refinement":[10,158],
                          "W4_Q":"E4_Q direct_sum O4_Q","W4_rank":255}
        condition=(strict_equal(packets,expected_packets) and split["condition"]=="p good and p splits as mathfrakp*bar_mathfrakp in K" and
                   split["two_K_polynomials_identical"] is True and split["K_exponent_from_C51"]=={"numerator":1,"denominator":2} and
                   split["Q_exponent_after_pairing"]=={"numerator":1,"denominator":1} and
                   split["identity"]=="Log0-root_1/2(L_K,mathfrakp(W4)*L_K,bar_mathfrakp(W4))=L_Q,p(W4_Q)" and
                   split["branch_scope"]=="local analytic Log0 branch at z=0 only" and
                   split["meaning_of_integral"]=="ordinary exponent-one rank-255 Q Euler factor; normalized polynomial need only lie in Q[T]" and
                   exponents["K_exponent"]=="2/n" and exponents["Q_exponent"]=="4/n" and exponents["n3"]=="4/3 remains fractional" and exponents["n4"]=="1 clears exactly")
        condition=(condition and strict_equal(exponents["certified_motivic_rows"],[2,3,4]) and
                   exponents["n_ge_5"]=="CONDITIONAL_ON_SMOOTH_SOURCE_PACKET_AND_C51_EXTRACTION")
        add_gate(gates,"split_half_root_rank255",condition,"two identical K-prime factors become one exponent-one Q factor")
    except Exception as error:add_gate(gates,"split_half_root_rank255",False,str(error))

    try:
        inert=payload["B3_compatible_local_factors"]["inert_prime"]
        # Independent scalar-root identity: product (1-a z)(1+a z)=1-a^2 z^2.
        scalar_controls=all((1-a*z)*(1+a*z)==1-a*a*z*z for a in (2,-3,5) for z in (1,2,-1))
        condition=(scalar_controls and inert["norm_clock"]=="N(mathfrakp)=p^2" and
                   inert["condition"]=="p good inert in K" and
                   inert["raw_identity"]=="P_K,mathfrakp(T)=product_i(1-alpha_i^2*T)" and
                   inert["equivalent_identity"]=="P_K,mathfrakp(z^2)=P_Q,p(z)*P_Q,p(-z)" and inert["Q_factor_recovered_as_half_root"] is False)
        add_gate(gates,"inert_base_change_dictionary",condition,"A^2 Frobenius and P(z)P(-z), no inert half-root")
    except Exception as error:add_gate(gates,"inert_base_change_dictionary",False,str(error))

    try:
        identity=payload["B3_compatible_local_factors"]["Artin_base_change"]
        add_gate(gates,"Artin_base_change",identity=="L_K(M0|K,u)=L_Q(M0,u)*L_Q(M0 tensor chi_K,u)",
                 "quadratic Artin formalism over Q/K")
    except Exception as error:add_gate(gates,"Artin_base_change",False,str(error))

    try:
        control=payload["finite_p7_control"]
        weighted=sum(a*b for a,b in zip(control["class_sizes"],control["twisted_fixed_counts"]))
        expected_control={"status":"PRE_C53_RECONNAISSANCE_REGRESSION_ANCHOR_UNCERTIFIED",
                          "independently_recomputed_in_C53":False,"rho_mod_7":2,"class_sizes":[1,1,2,2,2,2,2,6,6],
                          "twisted_fixed_counts":[22380,20224,20910,19734,19734,20028,19930,20028,19734],
                          "weighted_fixed_sum":481848,"quotient_stack_count":20077,"ambient_even_trace":19608,
                          "raw_core_trace":-469,"raw_local_a1":469,"normalized_twist2_trace":{"numerator":-67,"denominator":7}}
        condition=(strict_equal(control,expected_control) and weighted==481848 and control["weighted_fixed_sum"]==weighted and
                   control["quotient_stack_count"]==weighted//24 and control["ambient_even_trace"]-weighted//24==-469 and
                   control["raw_core_trace"]==-469 and control["raw_local_a1"]==469 and strict_equal(control["normalized_twist2_trace"],{"numerator":-67,"denominator":7}))
        add_gate(gates,"p7_reconnaissance_regression_anchor",condition,
                 "frozen literal arithmetic only; not theorem input; no independent geometric replay")
    except Exception as error:add_gate(gates,"p7_reconnaissance_regression_anchor",False,str(error))

    try:
        scope=payload["scope"];global_scope=payload["B3_compatible_local_factors"]["global_scope"];decisions=payload["decisions"]
        expected_decisions={"all_n_Q_descent":"PROVED_ALGEBRAICALLY","nonconstant_rank24_dihedral_group_scheme":"PROVED",
                            "rank10_plus_rank158_Chow_motives_over_Q":"PROVED","strict_compatible_raw_local_factors":"PROVED_AT_GOOD_PRIMES",
                            "n4_split_half_root_is_one_Q_factor":"PROVED","constant_D12_over_Q":"REFUTED_ONLY_TWISTED_FORM_DESCENDS",
                            "rank2_projector_beyond_group_algebra":"OPEN_NOT_CLAIMED","full_rank10_P10_computed":"NOT_RUN_NOT_REQUIRED"}
        expected_scope={"chronology_replaced_by_average":False,"closing_edge_deleted":False,"all_n_smoothness_claimed":False,
                        "24_individual_Q_automorphisms_claimed":False,"normalized_local_polynomial_called_integral":False,
                        "inert_half_root_claimed":False,"automorphy_claimed":False,"functional_equation_claimed":False,
                        "Riemann_hypothesis_claimed":False,"Hilbert_Polya_operator_claimed":False}
        condition=(strict_equal(scope,expected_scope) and strict_equal(decisions,expected_decisions) and strict_equal(global_scope,{
            "split_local_denominator_clearing":"PROVED","inert_Henon_completion":"OPEN_NOT_CLAIMED","automorphy":"OPEN_NOT_CLAIMED",
            "global_continuation":"OPEN_NOT_CLAIMED","functional_equation":"OPEN_NOT_CLAIMED"}))
        add_gate(gates,"scope_firewall",condition,"no constant D12, inert completion, automorphy, FE, RH, or rank2 promotion")
    except Exception as error:add_gate(gates,"scope_firewall",False,str(error))

    all_pass=all(gate["status"]=="PASS" for gate in gates);result={
        "schema":"hcs-c53-check-v1","candidate":"HCS-C53","certificate_sha256":sha256_bytes(raw),
        "payload_sha256":computed_hash,"gate_count":len(gates),"pass_count":sum(g["status"]=="PASS" for g in gates),"all_pass":all_pass,"gates":gates,
    }
    encoded=json.dumps(result,indent=2,sort_keys=True)+"\n";args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(encoded)
    print(f"HCS-C53 checker: {result['pass_count']}/{result['gate_count']} PASS")
    return 0 if all_pass else 1


if __name__=="__main__":raise SystemExit(main())
