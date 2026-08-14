#!/usr/bin/env python3
"""Independent fail-closed checker for the HCS-C50 certificate."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from typing import Any, Callable

import sympy as sp


SCHEMA = "hcs-c50-certificate-v1"
FROZEN_PAYLOAD_SHA256 = "d2d78b6992d97bada0119416171d9d091f6d04eb9bcf93d9a71427f2589aed6a"
SOURCE_HASHES = {
    "henon_dynamics/henon_mu3_genus4_second_moment/results/c48_certificate.json": "92cd5c1079ebbaeaa27fc32e617852ae5d5989500ff3a816dd9fe306c32a32a8",
    "henon_dynamics/henon_mu3_fano_threefold_third_moment/results/c49_certificate.json": "b3ec1bf12ea0f05469054fda37bd34ee4b6748030813c8c6407752035a3c25d2",
}
FACTOR_ROWS = ((7,2,-4,2),(13,3,-1,-1),(19,7,-4,2),(31,25,-4,8),(37,26,-1,-7),(43,36,8,2),(61,47,-1,-7),(67,37,-4,-10),(73,8,11,-7),(79,23,-16,2),(97,35,2,2),(103,56,-4,8),(109,63,11,11),(127,107,-16,2),(139,96,20,8),(151,32,8,20),(157,12,-13,17),(163,104,8,-16),(181,48,-10,2),(193,84,-13,-1),(199,106,-4,20))
EXTENSION_COUNTS = {7:(12,66,372,2586),13:(18,270,2046,27414),19:(24,474,6744,129930),31:(24,1050,29640,926970)}
N4_ROWS = (
    (7,2,823690,156171,137600,22380,18914,-2772,6,7,2,7),(13,3,62719618,5381481,5231240,411906,152438,-9672,-342,13,-57,13),
    (19,7,893976790,50171439,49666400,2646492,511898,-32832,582,19,194,57),(31,25,27512444014,918818859,917116928,29634792,1731722,-51336,-354,31,-118,155),
    (37,26,94932973702,2641057041,2637047240,71410926,4060454,-140748,1602,37,89,37),(43,36,271817751322,6477111759,6471951200,150612360,5240066,-103716,-930,43,-310,301),
    (61,47,3142759524706,52391334009,52379274248,859151634,12286742,-478728,8970,61,299,61),(67,37,6060711080110,91846102719,91829264480,1370834004,17139002,-252456,-234,67,-78,737),
    (73,8,11047394090698,153459186429,153436479560,2102125302,23095886,-261048,-1662,73,-277,438),(79,23,19203877100890,246245014659,246204454400,3116628132,41053298,-122292,-10218,79,-262,79),
    (97,35,80798279594842,841725254181,841649709320,8677539006,76457534,-747288,-1038,97,-173,776),
)


class GateFailure(Exception):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise GateFailure(message)


def canonical_json(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def strict_equal(left: Any, right: Any) -> bool:
    if type(left) is not type(right):
        return False
    if isinstance(left, dict):
        return set(left) == set(right) and all(strict_equal(left[k], right[k]) for k in left)
    if isinstance(left, list):
        return len(left) == len(right) and all(strict_equal(a, b) for a, b in zip(left, right))
    return left == right


def digest(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def p1(p: int) -> list[tuple[int, int]]:
    return [(value, 1) for value in range(p)] + [(1, 0)]


def curve_count(p: int, rho: int) -> int:
    total = 0
    for r, s in p1(p):
        for t, u in p1(p):
            f = rho*r**3*(t**3+u**3)+s**3*t*u*(rho*rho*t-u)
            total += f % p == 0
    return total


def elliptic_trace(p: int) -> int:
    squares = {x*x % p for x in range(1, p)}
    count = 1
    for x in range(p):
        rhs = (x**3+69*x+22) % p
        count += 1 if rhs == 0 else (2 if rhs in squares else 0)
    return p + 1 - count


def convolution(a: list[int], b: list[int]) -> list[int]:
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


@lru_cache(maxsize=1)
def expected_factor_controls() -> list[dict[str, Any]]:
    result=[]
    for p,rho,ap,am in FACTOR_ROWS:
        count=curve_count(p,rho)
        require(count == p+1-2*(ap+am), f"curve trace p={p}")
        require(elliptic_trace(p)==ap, f"E+ trace p={p}")
        polynomial=convolution(convolution([1,-ap,p],[1,-ap,p]),convolution([1,-am,p],[1,-am,p]))
        result.append({"p":p,"rho":rho,"curve_count":count,"curve_trace":p+1-count,"E_plus_trace":ap,"E_minus_trace":am,"L_polynomial_coefficients_low_to_high":polynomial,"factorization_status":"THEOREM_DERIVED_FROM_GROUP_ISOGENY","finite_degree_one_control_pass":True})
    return result


def reduce_mod_rho(expression: Any, rho: Any) -> Any:
    numerator, denominator = sp.cancel(expression).as_numer_denom()
    numerator = sp.rem(numerator, rho*rho+rho+1, rho, domain="QQ(z)")
    denominator = sp.rem(denominator, rho*rho+rho+1, rho, domain="QQ(z)")
    return sp.cancel(numerator/denominator)


@lru_cache(maxsize=1)
def independent_group_identities() -> dict[str, bool]:
    rho,z=sp.symbols("rho z")
    f=-z*(rho*rho*z-1)/(rho*(z**3+1)); A=rho*rho/z
    B=-rho*rho*(z+1)/(z+rho*rho); h=(rho-1)/3
    return {
        "T1_squared_identity": reduce_mod_rho(A.subs(z,A)-z,rho)==0,
        "T2_squared_identity": reduce_mod_rho(B.subs(z,B)-z,rho)==0,
        "T1_T2_commute": reduce_mod_rho(A.subs(z,B)-B.subs(z,A),rho)==0,
        "f_T1_equals_minus_f": reduce_mod_rho(f.subs(z,A)+f,rho)==0,
        "f_T2_times_f_equals_h_cubed": reduce_mod_rho(f.subs(z,B)*f-h**3,rho)==0,
    }


@lru_cache(maxsize=1)
def independent_singular_basis() -> list[str]:
    require(shutil.which("Singular") is not None,"Singular missing")
    script="""ring A=0,(x0,x1,x2,x3,x4,x5,x6,x7,r),dp;
poly q=r*x0*x7+x6*x7+x5*x6+x4*x5+x3*x4+x2*x3+x1*x2+x0*x1;
ideal J=r^2+r+1,q,x7^2-x6-r*x0,x6^2-x5-x7,x5^2-x4-x6,x4^2-x3-x5,x3^2-x2-x4,x2^2-x1-x3,x1^2-x0-x2,x0^2-x1-r*x7;
option(redSB); ideal B=std(J); B;
"""
    run=subprocess.run(["Singular","-q"],input=script,text=True,capture_output=True,check=True,timeout=60)
    return [line.split("=",1)[1].strip() for line in run.stdout.splitlines() if line.startswith("B[")]


def newton_polynomial(p: int, counts: tuple[int,...]) -> list[int]:
    power=[p**k+1-count for k,count in enumerate(counts,1)]; coeff=[1]
    for k in range(1,5):
        value=-sum(power[j-1]*coeff[k-j] for j in range(1,k+1)); require(value%k==0,"Newton integrality"); coeff.append(value//k)
    return coeff+[p**(4-k)*coeff[k] for k in range(3,-1,-1)]


@lru_cache(maxsize=1)
def expected_extensions() -> list[dict[str,Any]]:
    factors={row["p"]:row["L_polynomial_coefficients_low_to_high"] for row in expected_factor_controls()}
    out=[]
    for p,counts in EXTENSION_COUNTS.items():
        poly=newton_polynomial(p,counts); require(poly==factors[p],f"Newton factor p={p}")
        out.append({"p":p,"curve_counts_degrees_1_to_4":list(counts),"Newton_polynomial_coefficients_low_to_high":poly,"matches_group_factorization":True})
    return out


@lru_cache(maxsize=None)
def source_ordered_chronology_zero_count(p: int, rho: int) -> int:
    """Independent literal DP with state (x0,current,residue)."""
    cubes=[2*x**3%p for x in range(p)]
    states={(start,start,cubes[start]):1 for start in range(p)}
    for _ in range(1,8):
        following: dict[tuple[int,int,int],int]={}
        for (start,previous,residue),multiplicity in states.items():
            for current in range(p):
                key=(start,current,(residue+previous*current+cubes[current])%p)
                following[key]=following.get(key,0)+multiplicity
        states=following
    return sum(multiplicity for (start,endpoint,residue),multiplicity in states.items() if (residue+rho*endpoint*start)%p==0)


def expected_n4_controls(payload_rows: list[dict[str,Any]]) -> None:
    require(len(payload_rows)==len(N4_ROWS),"n4 ledger length")
    for row,values in zip(payload_rows,N4_ROWS):
        p,rho,Z,S,Q,X,alpha,beta,cn,cd,nn,nd=values
        expected={"p":p,"rho":rho,"Z_p_4":Z,"S_cubic_sixfold":S,"Q_split_sixfold":Q,"X_complete_intersection_fivefold":X,"alpha_p":alpha,"beta_p":beta,"C_p_4":{"numerator":cn,"denominator":cd},"c_p_4":{"numerator":nn,"denominator":nd},"literal_eight_step_chronology_recomputed":p<=31,"X_direct_affine_CQ_control":X if p<=13 else None,"Weil_integer_bounds_pass":True}
        require(strict_equal(row,expected),f"frozen n4 row p={p}")
        if p<=31: require(source_ordered_chronology_zero_count(p,rho)==Z,f"source chronology p={p}")


def matrix_multiply(left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[sum((left[i][k]*right[k][j] for k in range(len(right))),Fraction(0)) for j in range(len(right[0]))] for i in range(len(left))]


def matrix_rank(source: list[list[Fraction]]) -> int:
    matrix=[row[:] for row in source]; rows=len(matrix); columns=len(matrix[0]); pivot_row=0
    for column in range(columns):
        pivot=next((r for r in range(pivot_row,rows) if matrix[r][column]),None)
        if pivot is None: continue
        matrix[pivot_row],matrix[pivot]=matrix[pivot],matrix[pivot_row]
        scale=matrix[pivot_row][column]; matrix[pivot_row]=[x/scale for x in matrix[pivot_row]]
        for r in range(rows):
            if r!=pivot_row and matrix[r][column]:
                factor=matrix[r][column]; matrix[r]=[a-factor*b for a,b in zip(matrix[r],matrix[pivot_row])]
        pivot_row+=1
    return pivot_row


def matrix_record(matrix: list[list[Fraction]]) -> list[list[dict[str,int]]]:
    return [[{"numerator":x.numerator,"denominator":x.denominator} for x in row] for row in matrix]


@lru_cache(maxsize=1)
def expected_idempotent_control() -> dict[str,Any]:
    zero=Fraction(0); one=Fraction(1); half=Fraction(1,2)
    delta=[[zero,-one],[one,-one]]; reflection=[[zero,one],[one,zero]]
    delta2=matrix_multiply(delta,delta)
    e_std=[[(2*one if i==j else zero)-delta[i][j]-delta2[i][j] for j in range(2)] for i in range(2)]
    e_std=[[x/3 for x in row] for row in e_std]
    e_j=[[(one if i==j else zero)/2+reflection[i][j]/2 for j in range(2)] for i in range(2)]
    plus=[[one if i==j and i<2 else zero for j in range(4)] for i in range(4)]
    minus=[[one if i==j and i>=2 else zero for j in range(4)] for i in range(4)]
    ej4=[[zero]*4 for _ in range(4)]
    for block in (0,2):
        for i in range(2):
            for j in range(2): ej4[block+i][block+j]=e_j[i][j]
    primitive_plus=matrix_multiply(plus,ej4); primitive_minus=matrix_multiply(minus,ej4)
    require(matrix_multiply(e_std,e_std)==e_std and matrix_multiply(e_j,e_j)==e_j,"2x2 idempotence")
    require(matrix_multiply(primitive_plus,primitive_plus)==primitive_plus and matrix_multiply(primitive_minus,primitive_minus)==primitive_minus,"primitive idempotence")
    return {"standard_delta_matrix":matrix_record(delta),"standard_reflection_j_matrix":matrix_record(reflection),"e_std_matrix":matrix_record(e_std),"e_j_matrix":matrix_record(e_j),"e_std_rank":matrix_rank(e_std),"e_j_rank":matrix_rank(e_j),"e_plus_rank_in_two_blocks":matrix_rank(plus),"e_minus_rank_in_two_blocks":matrix_rank(minus),"primitive_plus_rank":matrix_rank(primitive_plus),"primitive_minus_rank":matrix_rank(primitive_minus),"all_projectors_idempotent":True,"two_standard_blocks":True}


@lru_cache(maxsize=1)
def expected_chern_control() -> dict[str,int]:
    H=sp.symbols("H")
    cubic=int(sp.expand(sp.series((1+H)**8/(1+3*H),H,0,7).removeO()).coeff(H,6))
    complete=int(sp.expand(sp.series((1+H)**8/((1+2*H)*(1+3*H)),H,0,6).removeO()).coeff(H,5))
    cubic_euler=3*cubic; complete_euler=6*complete
    return {"cubic_top_chern_coefficient":cubic,"cubic_degree":3,"cubic_Euler_characteristic":cubic_euler,"cubic_primitive_middle_b6":cubic_euler-7,"complete_intersection_top_chern_coefficient":complete,"complete_intersection_degree":6,"complete_intersection_Euler_characteristic":complete_euler,"complete_intersection_middle_b5":6-complete_euler}


@lru_cache(maxsize=1)
def reverse_p181_points() -> list[list[int]]:
    p,rho=181,48
    found=[]
    for x7 in range(p):
        for x6 in range(p):
            reverse=[x7,x6]
            for index in range(1,7):
                reverse.append((reverse[index]**2-reverse[index-1])%p)
            xs=list(reversed(reverse))
            if (xs[1]+rho*xs[7]-xs[0]**2)%p or (xs[6]+rho*xs[0]-xs[7]**2)%p:
                continue
            cubic=sum(x**3 for x in xs)%p
            quadric=(sum(xs[index]*xs[index+1] for index in range(7))+rho*xs[7]*xs[0])%p
            if cubic==0 and quadric==0 and any(xs):
                found.append({"coordinates":xs,"C_mod_p":cubic,"Q_mod_p":quadric,"normalized_gradient_recurrence_pass":True})
    return sorted(found,key=lambda row:row["coordinates"])


def gate(name: str, function: Callable[[], None]) -> dict[str, str]:
    try:
        function()
        return {"gate": name, "status": "PASS"}
    except GateFailure as error:
        return {"gate": name, "status": "FAIL", "detail": str(error)}
    except Exception as error:
        return {"gate": name, "status": "ERROR", "detail": f"{type(error).__name__}: {error}"}


def exact_keys(value: Any, keys: set[str], label: str) -> None:
    require(type(value) is dict and set(value) == keys, f"{label} exact keys")


def recursive_schema(payload: dict[str, Any]) -> None:
    exact_keys(payload,{"material_passport","source_lock","curve_and_group","jacobian_decomposition","idempotent_matrix_control","local_factor_controls","extension_field_Newton_controls","second_moment_resummation","fourth_moment_geometry","exact_fourth_moment_controls","bad_reduction_control","analytic_continuation","tenth_order_regularized_determinant","route_a","scope"},"payload")
    exact_keys(payload["material_passport"],{"candidate_id","project_slug","artifact_status"},"passport")
    for row in payload["source_lock"]: exact_keys(row,{"path","sha256"},"source row")
    exact_keys(payload["curve_and_group"],{"base_field","curve","exact_identities","generators","group"},"curve/group")
    exact_keys(payload["curve_and_group"]["exact_identities"],{"T1_squared_identity","T2_squared_identity","T1_T2_commute","f_T1_equals_minus_f","f_T2_times_f_equals_h_cubed"},"identity map")
    exact_keys(payload["curve_and_group"]["generators"],{"delta","i","j"},"generators")
    exact_keys(payload["jacobian_decomposition"],{"genus_C","delta_quotient_genus","C3_invariant_differentials","i_fixed_points","i_quotient_genus","i_plus_dimension","i_minus_dimension","H0_representation","idempotents","elliptic_idempotent_rank","theorem","E_minus_group_idempotent_definition","Prym_description_status","E_plus_validation_model","E_minus_Q_Weierstrass_model_claimed"},"Jacobian")
    exact_keys(payload["idempotent_matrix_control"],{"standard_delta_matrix","standard_reflection_j_matrix","e_std_matrix","e_j_matrix","e_std_rank","e_j_rank","e_plus_rank_in_two_blocks","e_minus_rank_in_two_blocks","primitive_plus_rank","primitive_minus_rank","all_projectors_idempotent","two_standard_blocks"},"matrix control")
    for row in payload["local_factor_controls"]: exact_keys(row,{"p","rho","curve_count","curve_trace","E_plus_trace","E_minus_trace","L_polynomial_coefficients_low_to_high","factorization_status","finite_degree_one_control_pass"},"factor row")
    for row in payload["extension_field_Newton_controls"]: exact_keys(row,{"p","curve_counts_degrees_1_to_4","Newton_polynomial_coefficients_low_to_high","matches_group_factorization"},"Newton row")
    exact_keys(payload["second_moment_resummation"],{"curve_trace_identity","normalized_moment","w_substitution","F2_definition","theorem","L_curve_factorization","split_prime_first_log_coefficients","coefficient_ledger","H2_holomorphic_nonzero_domain","continuation_may_have_zeros"},"resummation")
    exact_keys(payload["second_moment_resummation"]["split_prime_first_log_coefficients"],{"zeta_power","curve_L"},"first coefficients")
    exact_keys(payload["second_moment_resummation"]["coefficient_ledger"],{"c2_constant_numerator","c2_elliptic_trace_multiplier","log_moment_divisor","split_prime_ideals_of_norm_p","Dedekind_zeta_exponent","curve_L_exponent"},"coefficient ledger")
    exact_keys(payload["fourth_moment_geometry"],{"chronological_phase","averaged_transition_matrix_used","norm_clock","direction_identity","split_quadric_count","char0_singular_ideal_reduced_basis_dp","char0_projective_smooth","cubic_sixfold_primitive_b6","complete_intersection_fivefold_b5","Chern_Betti_recomputation","moment_identity","good_prime_bound","all_split_prime_smoothness"},"n4 geometry")
    exact_keys(payload["fourth_moment_geometry"]["Chern_Betti_recomputation"],{"cubic_top_chern_coefficient","cubic_degree","cubic_Euler_characteristic","cubic_primitive_middle_b6","complete_intersection_top_chern_coefficient","complete_intersection_degree","complete_intersection_Euler_characteristic","complete_intersection_middle_b5"},"Chern control")
    for row in payload["exact_fourth_moment_controls"]: exact_keys(row,{"p","rho","Z_p_4","S_cubic_sixfold","Q_split_sixfold","X_complete_intersection_fivefold","alpha_p","beta_p","C_p_4","c_p_4","literal_eight_step_chronology_recomputed","X_direct_affine_CQ_control","Weil_integer_bounds_pass"},"n4 row")
    exact_keys(payload["bad_reduction_control"],{"p","rho","normalized_singular_points","singular_point_count","all_points_C_zero","all_points_Q_zero","scope"},"bad reduction")
    for row in payload["bad_reduction_control"]["normalized_singular_points"]: exact_keys(row,{"coordinates","C_mod_p","Q_mod_p","normalized_gradient_recurrence_pass"},"bad point")
    exact_keys(payload["analytic_continuation"],{"moment_walls","holomorphic_continuation_domain","continuation_may_have_zeros","full_functional_equation","elliptic_factor_functional_equation"},"analytic")
    exact_keys(payload["analytic_continuation"]["moment_walls"],{"n1","n2_after_resummation","n3","n4","n_ge_5"},"walls")
    exact_keys(payload["tenth_order_regularized_determinant"],{"semifinite_criterion","tau_L10_domain","tau_L9_domain","minimal_fixed_order_on_full_domain","raw_germ_identity","continued_identity","classical_Hilbert_Schatten_criterion","classical_S10_domain","standard_Hilbert_trace_class_domain","unregularized_tau_trace_class_domain","Hilbert_direct_sum_compact_domain","ordinary_Fredholm_determinant_claimed","positive_Fuglede_Kadison_equals_complex_G"},"Det10")
    exact_keys(payload["route_a"],{"A3","A3_evidence","full_FE","route_b_invoked"},"Route A")
    exact_keys(payload["scope"],{"Jacobian_isogeny_theorem","global_nonvanishing_claimed","Riemann_hypothesis_claimed","self_adjoint_Hilbert_Polya_operator_claimed","all_split_n4_smoothness_claimed","p181_contaminates_C48_curve"},"scope")


def static_claims(payload: dict[str,Any]) -> None:
    require(strict_equal(payload["material_passport"],{"candidate_id":"HCS-C50","project_slug":"henon_mu3_elliptic_resummation_fourth_moment","artifact_status":"RELEASE_CANDIDATE"}),"passport leaves")
    require(strict_equal({k:payload["curve_and_group"][k] for k in ("base_field","curve","generators","group")},{"base_field":"K=Q(rho), rho^2+rho+1=0","curve":"y^3=-x*(rho^2*x-1)/(rho*(x^3+1))","generators":{"delta":"(x,y)->(x,rho*y)","i":"(x,y)->(rho^2/x,-y)","j":"(x,y)->(-rho^2*(x+1)/(x+rho^2),((rho-1)/3)/y)"},"group":"C2 x S3"}),"curve/group leaves")
    jacobian_expected={"genus_C":4,"delta_quotient_genus":0,"C3_invariant_differentials":0,"i_fixed_points":2,"i_quotient_genus":2,"i_plus_dimension":2,"i_minus_dimension":2,"H0_representation":"Std_+ direct_sum Std_-","idempotents":"e_+/-=(1+/-i)/2; e_std=(2-delta-delta^2)/3; e_j=(1+j)/2","elliptic_idempotent_rank":1,"theorem":"Jac(C) is K-isogenous to E_+^2 x E_-^2","E_minus_group_idempotent_definition":"image((1-i)/2*(2-delta-delta^2)/3*(1+j)/2 on Jac(C))","Prym_description_status":"OPEN_NOT_USED_IN_THEOREM_OR_CERTIFICATE","E_plus_validation_model":"Y^2=X^3+69X+22","E_minus_Q_Weierstrass_model_claimed":False}
    require(strict_equal(payload["jacobian_decomposition"],jacobian_expected),"Jacobian leaves")
    resummation_expected={"curve_trace_identity":"a_C,p=2(a_+,p+a_-,p)","normalized_moment":"c_p,2=-(28+8(a_+,p+a_-,p))/(p-1)","w_substitution":"w=2s+1","F2_definition":"F2(s)=exp(-ell_2(s)/2)","theorem":"F2(s)=zeta_K(2s+1)^7*L(C/K,2s+1)*H2(s)","L_curve_factorization":"L(C/K,w)=[L(E_+/K,w)L(E_-/K,w)]^2","split_prime_first_log_coefficients":{"zeta_power":"14","curve_L":"4(a_++a_-)"},"coefficient_ledger":{"c2_constant_numerator":28,"c2_elliptic_trace_multiplier":8,"log_moment_divisor":2,"split_prime_ideals_of_norm_p":2,"Dedekind_zeta_exponent":7,"curve_L_exponent":1},"H2_holomorphic_nonzero_domain":"Re(s)>0","continuation_may_have_zeros":True}
    require(strict_equal(payload["second_moment_resummation"],resummation_expected),"resummation leaves")
    geometry_expected={"chronological_phase":"Phi_4=2*sum_i=0^7 x_i^3+sum_i=0^6 x_i*x_(i+1)+rho*x7*x0","averaged_transition_matrix_used":False,"norm_clock":"z_p=p^(-s)","direction_identity":"Z=1+#P7-#S-#Q+p*#X","split_quadric_count":"#Q=(p^3+1)(p^3+p^2+p+1)=#P6+p^3","char0_singular_ideal_reduced_basis_dp":["x7","x6","x5","x4","x3","x2","x1","x0","r^2+r+1"],"char0_projective_smooth":True,"cubic_sixfold_primitive_b6":86,"complete_intersection_fivefold_b5":168,"Chern_Betti_recomputation":expected_chern_control(),"moment_identity":"C_p,4=-2-2*alpha_p/p^3-2*beta_p/p^2","good_prime_bound":"|C_p,4|<=174+336*sqrt(p); c_p,4=O(p^(-1/2))","all_split_prime_smoothness":False}
    require(strict_equal(payload["fourth_moment_geometry"],geometry_expected),"geometry leaves")
    bad=payload["bad_reduction_control"]
    require(strict_equal({k:bad[k] for k in ("p","rho","singular_point_count","all_points_C_zero","all_points_Q_zero","scope")},{"p":181,"rho":48,"singular_point_count":12,"all_points_C_zero":True,"all_points_Q_zero":True,"scope":"bad only for n=4 complete-intersection reduction; C48 curve remains good at p=181"}),"bad-reduction leaves")
    require(strict_equal(payload["analytic_continuation"],{"moment_walls":{"n1":"0","n2_after_resummation":"0","n3":"1/6","n4":"1/8","n_ge_5":"1/5"},"holomorphic_continuation_domain":"Re(s)>1/5","continuation_may_have_zeros":True,"full_functional_equation":False,"elliptic_factor_functional_equation":True}),"analytic leaves")
    require(strict_equal(payload["route_a"],{"A3":"A3_PARTIAL_ANALYTIC_STRUCTURE","A3_evidence":"holomorphic continuation to Re(s)>1/5 with an explicit elliptic arithmetic divisor","full_FE":False,"route_b_invoked":False}),"Route-A leaves")
    require(strict_equal(payload["scope"],{"Jacobian_isogeny_theorem":True,"global_nonvanishing_claimed":False,"Riemann_hypothesis_claimed":False,"self_adjoint_Hilbert_Polya_operator_claimed":False,"all_split_n4_smoothness_claimed":False,"p181_contaminates_C48_curve":False}),"scope leaves")


def audit_certificate(certificate: dict[str, Any], project: Path) -> tuple[list[dict[str,str]], bool]:
    gates=[]
    gates.append(gate("envelope", lambda: (
        require(set(certificate)=={"schema","payload","payload_sha256"}, "top-level keys"),
        require(certificate.get("schema")==SCHEMA, "schema"),
        require(certificate.get("payload_sha256")==hashlib.sha256(canonical_json(certificate.get("payload"))).hexdigest(), "payload digest"))))
    payload=certificate.get("payload",{})
    gates.append(gate("frozen_full_payload",lambda: require(hashlib.sha256(canonical_json(payload)).hexdigest()==FROZEN_PAYLOAD_SHA256,"full payload exact digest/type lock")))
    schema_gate=gate("recursive_exact_schema",lambda: recursive_schema(payload))
    gates.append(schema_gate)
    if schema_gate["status"] != "PASS":
        return gates, False
    gates.append(gate("strict_static_leaves",lambda: static_claims(payload)))
    gates.append(gate("passport_and_sources", lambda: (
        require(payload["material_passport"]["candidate_id"]=="HCS-C50", "candidate"),
        require(payload["material_passport"]["project_slug"]=="henon_mu3_elliptic_resummation_fourth_moment", "slug"),
        require(payload["source_lock"]==[{"path":p,"sha256":h} for p,h in SOURCE_HASHES.items()], "source records"),
        require(all(digest(project/p)==h for p,h in SOURCE_HASHES.items()), "live source lock"))))
    gates.append(gate("group_and_isogeny", lambda: (
        require(strict_equal(payload["curve_and_group"]["exact_identities"],independent_group_identities()), "independent group identities"),
        require(payload["curve_and_group"]["group"]=="C2 x S3", "group"),
        require(payload["jacobian_decomposition"]["genus_C"]==4, "genus"),
        require(payload["jacobian_decomposition"]["C3_invariant_differentials"]==0, "C3 invariant"),
        require(payload["jacobian_decomposition"]["i_fixed_points"]==2, "fixed points"),
        require(payload["jacobian_decomposition"]["i_quotient_genus"]==2, "quotient genus"),
        require((2*payload["jacobian_decomposition"]["genus_C"]+2-payload["jacobian_decomposition"]["i_fixed_points"])//4==payload["jacobian_decomposition"]["i_quotient_genus"],"Riemann-Hurwitz"),
        require(payload["jacobian_decomposition"]["i_plus_dimension"]==2 and payload["jacobian_decomposition"]["i_minus_dimension"]==2,"i dimensions"),
        require(payload["jacobian_decomposition"]["elliptic_idempotent_rank"]==1, "rank"),
        require(payload["jacobian_decomposition"]["theorem"]=="Jac(C) is K-isogenous to E_+^2 x E_-^2", "isogeny"),
        require(payload["jacobian_decomposition"]["E_minus_group_idempotent_definition"]=="image((1-i)/2*(2-delta-delta^2)/3*(1+j)/2 on Jac(C))","E- idempotent"),
        require(payload["jacobian_decomposition"]["Prym_description_status"]=="OPEN_NOT_USED_IN_THEOREM_OR_CERTIFICATE","Prym scope"),
        require(payload["jacobian_decomposition"]["E_minus_Q_Weierstrass_model_claimed"] is False,"E- Q overclaim"))))
    gates.append(gate("matrix_idempotents",lambda: require(strict_equal(payload["idempotent_matrix_control"],expected_idempotent_control()),"standard representation projectors")))
    gates.append(gate("local_factors", lambda: require(strict_equal(payload["local_factor_controls"],expected_factor_controls()), "21-prime factor ledger")))
    gates.append(gate("extension_Newton",lambda: require(strict_equal(payload["extension_field_Newton_controls"],expected_extensions()),"extension controls")))
    gates.append(gate("resummation", lambda: (
        require(payload["second_moment_resummation"]["theorem"]=="F2(s)=zeta_K(2s+1)^7*L(C/K,2s+1)*H2(s)","F2"),
        require(payload["second_moment_resummation"]["H2_holomorphic_nonzero_domain"]=="Re(s)>0","H2 domain"),
        require(strict_equal(payload["second_moment_resummation"]["coefficient_ledger"],{"c2_constant_numerator":28,"c2_elliptic_trace_multiplier":8,"log_moment_divisor":2,"split_prime_ideals_of_norm_p":2,"Dedekind_zeta_exponent":7,"curve_L_exponent":1}),"coefficient ledger"),
        require(payload["second_moment_resummation"]["continuation_may_have_zeros"] is True,"zeros"))))
    gates.append(gate("n4_geometry",lambda: (
        require(payload["fourth_moment_geometry"]["averaged_transition_matrix_used"] is False,"averaging"),
        require(payload["fourth_moment_geometry"]["chronological_phase"]=="Phi_4=2*sum_i=0^7 x_i^3+sum_i=0^6 x_i*x_(i+1)+rho*x7*x0","phase"),
        require(payload["fourth_moment_geometry"]["norm_clock"]=="z_p=p^(-s)","clock"),
        require(payload["fourth_moment_geometry"]["char0_singular_ideal_reduced_basis_dp"]==independent_singular_basis()==["x7","x6","x5","x4","x3","x2","x1","x0","r^2+r+1"],"Groebner basis"),
        require(payload["fourth_moment_geometry"]["cubic_sixfold_primitive_b6"]==86,"b6"),
        require(payload["fourth_moment_geometry"]["complete_intersection_fivefold_b5"]==168,"b5"),
        require(strict_equal(payload["fourth_moment_geometry"]["Chern_Betti_recomputation"],expected_chern_control()),"Chern/Betti"),
        require(payload["fourth_moment_geometry"]["all_split_prime_smoothness"] is False,"smoothness overclaim"))))
    def check_n4():
        expected_n4_controls(payload["exact_fourth_moment_controls"])
        for row in payload["exact_fourth_moment_controls"]:
            p=row["p"]
            require(row["Z_p_4"]==1+sum(p**j for j in range(8))-row["S_cubic_sixfold"]-row["Q_split_sixfold"]+p*row["X_complete_intersection_fivefold"],f"direction p={p}")
            c=Fraction(row["C_p_4"]["numerator"],row["C_p_4"]["denominator"])
            require(c==Fraction(2*row["Z_p_4"],p**3)-2*p**4,f"C4 p={p}")
            norm=Fraction(row["c_p_4"]["numerator"],row["c_p_4"]["denominator"])
            require(norm==c/Fraction((p-1)//2),f"c4 p={p}")
            require(row["Weil_integer_bounds_pass"] is True,f"Weil p={p}")
    gates.append(gate("n4_exact_ledger",check_n4))
    gates.append(gate("p181_negative",lambda: (
        require(payload["bad_reduction_control"]["p"]==181,"bad p"),
        require(payload["bad_reduction_control"]["singular_point_count"]==12,"bad count"),
        require(strict_equal(payload["bad_reduction_control"]["normalized_singular_points"],reverse_p181_points()),"reverse recurrence exact values/types"),
        require(payload["bad_reduction_control"]["all_points_C_zero"] is True and payload["bad_reduction_control"]["all_points_Q_zero"] is True,"C/Q summary"),
        require(payload["scope"]["p181_contaminates_C48_curve"] is False,"C48 contamination"))))
    gates.append(gate("analytic_and_route",lambda: (
        require(strict_equal(payload["analytic_continuation"]["moment_walls"],{"n1":"0","n2_after_resummation":"0","n3":"1/6","n4":"1/8","n_ge_5":"1/5"}),"moment walls"),
        require(payload["analytic_continuation"]["holomorphic_continuation_domain"]=="Re(s)>1/5","domain"),
        require(payload["analytic_continuation"]["continuation_may_have_zeros"] is True,"zeros"),
        require(payload["analytic_continuation"]["full_functional_equation"] is False,"FE"),
        require(payload["analytic_continuation"]["elliptic_factor_functional_equation"] is True,"elliptic FE"),
        require(payload["route_a"]["A3"]=="A3_PARTIAL_ANALYTIC_STRUCTURE","A3 enum"),
        require(payload["route_a"]["full_FE"] is False and payload["route_a"]["route_b_invoked"] is False,"route scope"))))
    gates.append(gate("tau_Det10",lambda: (
        require(strict_equal(payload["tenth_order_regularized_determinant"],{"semifinite_criterion":"X_s in L^q(M,tau) iff q*Re(s)>2","tau_L10_domain":"Re(s)>1/5","tau_L9_domain":"Re(s)>2/9","minimal_fixed_order_on_full_domain":10,"raw_germ_identity":"G=exp(-sum_(n=1)^9 ell_n/n)*Det_10^gr(I-X_s)","continued_identity":"G_cont=F2_cont*exp(-sum_(1<=n<=9,n!=2) ell_n/n)*Det_10^gr(I-X_s)","classical_Hilbert_Schatten_criterion":"X_s in S^q iff q*Re(s)>3","classical_S10_domain":"Re(s)>3/10","standard_Hilbert_trace_class_domain":"Re(s)>3","unregularized_tau_trace_class_domain":"Re(s)>2","Hilbert_direct_sum_compact_domain":"Re(s)>0","ordinary_Fredholm_determinant_claimed":False,"positive_Fuglede_Kadison_equals_complex_G":False}),"full Det10 leaves/types"),
        require(payload["tenth_order_regularized_determinant"]["semifinite_criterion"]=="X_s in L^q(M,tau) iff q*Re(s)>2","tau criterion"),
        require(payload["tenth_order_regularized_determinant"]["tau_L10_domain"]=="Re(s)>1/5","tau L10"),
        require(payload["tenth_order_regularized_determinant"]["tau_L9_domain"]=="Re(s)>2/9","tau L9"),
        require(payload["tenth_order_regularized_determinant"]["minimal_fixed_order_on_full_domain"]==10,"minimal order"),
        require(payload["tenth_order_regularized_determinant"]["raw_germ_identity"]=="G=exp(-sum_(n=1)^9 ell_n/n)*Det_10^gr(I-X_s)","raw identity"),
        require(payload["tenth_order_regularized_determinant"]["continued_identity"]=="G_cont=F2_cont*exp(-sum_(1<=n<=9,n!=2) ell_n/n)*Det_10^gr(I-X_s)","continued identity"),
        require(payload["tenth_order_regularized_determinant"]["classical_Hilbert_Schatten_criterion"]=="X_s in S^q iff q*Re(s)>3","classical criterion"),
        require(payload["tenth_order_regularized_determinant"]["classical_S10_domain"]=="Re(s)>3/10","classical S10"),
        require(payload["tenth_order_regularized_determinant"]["standard_Hilbert_trace_class_domain"]=="Re(s)>3","classical trace class"),
        require(payload["tenth_order_regularized_determinant"]["unregularized_tau_trace_class_domain"]=="Re(s)>2","tau L1"),
        require(payload["tenth_order_regularized_determinant"]["Hilbert_direct_sum_compact_domain"]=="Re(s)>0","compactness"),
        require(payload["tenth_order_regularized_determinant"]["ordinary_Fredholm_determinant_claimed"] is False,"Fredholm overclaim"),
        require(payload["tenth_order_regularized_determinant"]["positive_Fuglede_Kadison_equals_complex_G"] is False,"FK phase"))))
    gates.append(gate("scope",lambda: (
        require(payload["scope"]["global_nonvanishing_claimed"] is False,"nonvanishing"),
        require(payload["scope"]["Riemann_hypothesis_claimed"] is False,"RH"),
        require(payload["scope"]["self_adjoint_Hilbert_Polya_operator_claimed"] is False,"HP"),
        require(payload["scope"]["all_split_n4_smoothness_claimed"] is False,"all split"))))
    return gates, all(row["status"]=="PASS" for row in gates)


def main() -> int:
    parser=argparse.ArgumentParser(); parser.add_argument("certificate"); parser.add_argument("--output",required=True); args=parser.parse_args()
    cert=json.loads(Path(args.certificate).read_text()); project=Path(__file__).resolve().parents[3]
    gates,passed=audit_certificate(cert,project)
    report={"schema":"hcs-c50-independent-check-v1","certificate_sha256":digest(Path(args.certificate)),"gates":gates,"overall":"PASS" if passed else "FAIL"}
    Path(args.output).write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
    print(report["overall"])
    return 0 if passed else 1


if __name__=="__main__": raise SystemExit(main())
