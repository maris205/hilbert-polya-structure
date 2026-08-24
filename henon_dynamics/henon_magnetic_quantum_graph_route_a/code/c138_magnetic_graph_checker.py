#!/usr/bin/env python3
"""Independent exact reconstruction for C138; does not import producer."""
from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT/"results/c138_magnetic_graph_evidence.json"
LENGTHS = (1,2,3)


def fs(x):
    q = Fraction(x)
    return f"{q.numerator}/{q.denominator}"


def ms(mat):
    return [[str(sp.factor(mat[i,j])) for j in range(mat.cols)] for i in range(mat.rows)]


def canon(word):
    return min(word[i:]+word[:i] for i in range(len(word)))


def is_primitive(word):
    n = len(word)
    return all(word != word[:d]*(n//d) for d in range(1,n) if n%d==0)


def rev(word):
    return tuple((state+3)%6 for state in reversed(word))


def name(state):
    return ("+" if state < 3 else "-")+str(state%3+1)


def token(word):
    amp = Fraction(1); length=0; winding=[0,0,0]
    for j,state in enumerate(word):
        nxt=word[(j+1)%len(word)]; e,f=state%3,nxt%3
        amp *= Fraction(-1,3) if e==f else Fraction(2,3)
        length += LENGTHS[e]; winding[e] += 1 if state<3 else -1
    assert sum(winding)==0
    states=",".join(name(s) for s in word)
    ca=",".join(name(s) for s in canon(word)); rv=",".join(name(s) for s in canon(rev(word)))
    return f"{states}:A={fs(amp)}:L={length}:m={winding[0]},{winding[1]},{winding[2]}:canon={ca}:reverse={rv}",amp,length,tuple(winding)


def words(n):
    if n%2: return []
    return [tuple(edges[i]+3*((start+i)%2) for i in range(n)) for start in (0,1) for edges in product(range(3),repeat=n)]


def validate(data: dict) -> None:
    receipt=data.pop("payload_sha256")
    assert hashlib.sha256(json.dumps(data, sort_keys=True, separators=(",", ":")).encode()).hexdigest()==receipt
    data["payload_sha256"]=receipt
    assert set(data)=={"candidate_id","controls","date_utc","graph","laurent_determinant","magnetic_family","nonclaims","oriented_orbit_ledger","payload_sha256","progress","route_a","scattering","schema","scope","scope_flags"}
    assert data["schema"]=="HCS-C138-magnetic-theta-graph-v1" and data["candidate_id"]=="HCS-C138" and data["date_utc"]=="2026-08-24"
    assert data["scope"]=="NO_BAD_EULER_OR_ROOT_NUMBER"
    assert data["graph"]=={"clock":"one metric length per traversed directed bond","directed_bond_order":["+1","+2","+3","-1","-2","-3"],"edge_lengths":[1,2,3],"hilbert_space":"C^6 on directed bonds","vertex_condition":"degree-three Kirchhoff","vertices":["L","R"]}
    C=sp.Rational(2,3)*sp.ones(3)-sp.eye(3); Z=sp.zeros(3); S=Z.row_join(C).col_join(C.row_join(Z)); J=Z.row_join(sp.eye(3)).col_join(sp.eye(3).row_join(Z))
    assert data["scattering"]=={"C_orthogonal":True,"S_orthogonal":True,"bond_reversal_J":ms(J),"global_S":ms(S),"kirchhoff_C":ms(C)}
    assert data["magnetic_family"]=={
        "phase_split":"P_alpha(k)=diag(exp(i(k*l_j+alpha_j)/2), exp(i(k*l_j-alpha_j)/2))",
        "operator":"U_alpha(k)=P_alpha(k) S P_alpha(k)","unitary_for_real_k_alpha":True,
        "common_phase_gauge":"alpha_j -> alpha_j+c leaves U_alpha(k) unchanged because D_c S D_c=S",
        "gauge_invariant_flux_coordinates":["alpha_1-alpha_3","alpha_2-alpha_3"],"antiunitary":"Theta=J K",
        "antiunitary_identity":"Theta U_alpha(k) Theta^{-1}=U_{-alpha}(k)^{-1}",
        "orientation_statement":"individual orbit phases invert under orientation reversal; only the full determinant is even under alpha -> -alpha"}
    x1,x2,x3,q1,q2,q3,rho,c,t=sp.symbols("x1 x2 x3 q1 q2 q3 rho c t", nonzero=True); xs=(x1,x2,x3); qs=(q1,q2,q3)
    Xp=sp.diag(*(xs[i]*qs[i] for i in range(3))); Xm=sp.diag(*(xs[i]/qs[i] for i in range(3)))
    D=sp.factor((sp.eye(3)-rho**2*C*Xm*C*Xp).det())
    coeffs={str(p):str(sp.factor(sp.expand(D).coeff(rho,p))) for p in (0,2,4,6)}
    sec=data["laurent_determinant"]
    assert set(sec)=={"T1","T2","X_minus","X_plus","closed_form","common_q_scaling_invariant","convention","q_inversion_invariant","rho_coefficients","rho_degree","zero_flux_c133_factor"}
    assert sec["convention"]=="D(rho;x,q)=det(I_3-rho^2*C*X_-*C*X_+)" and sec["X_plus"]=="diag(x1*q1,x2*q2,x3*q3)" and sec["X_minus"]=="diag(x1/q1,x2/q2,x3/q3)"
    assert sec["rho_coefficients"]==coeffs and sec["rho_degree"]==6
    assert sec["T1"]=="1/9*sum_i x_i^2+4/9*sum_(i<j) x_i*x_j*(q_i/q_j+q_j/q_i)"
    assert sec["T2"]=="1/9*sum_(i<j) x_i^2*x_j^2+4/9*sum_(i<j) x_i*x_j*x_k^2*(q_i/q_j+q_j/q_i), k=complement"
    assert sec["closed_form"]=="1-rho^2*T1+rho^4*T2-rho^6*(x1*x2*x3)^2"
    assert sp.factor(D.subs({q1:c*q1,q2:c*q2,q3:c*q3})-D)==0 and sec["common_q_scaling_invariant"] is True
    assert sp.factor(D.subs({q1:1/q1,q2:1/q2,q3:1/q3})-D)==0 and sec["q_inversion_invariant"] is True
    zero=sp.factor(D.subs({q1:1,q2:1,q3:1,x1:t,x2:t**2,x3:t**3,rho:1}))
    expected=-sp.Rational(1,9)*(t-1)**3*(t+1)*(t**2+1)*(t**2+t+1)*(3*t**2-2*t+3)*(3*t**2+5*t+3)
    assert sp.factor(zero-expected)==0 and sec["zero_flux_c133_factor"]==str(zero)
    ledger=data["oriented_orbit_ledger"]
    assert set(ledger)=={"periods_through_8","phase_rule","primitive_cycles_through_8","primitive_product_germ","rooted_closed_walks_through_8","shortest_orientation_witnesses","token_fields"}
    rt=pt=0
    for n,row in enumerate(ledger["periods_through_8"],1):
        ws=words(n); lines=[token(w)[0] for w in ws]; ps=sorted({canon(w) for w in ws if is_primitive(w)}); plines=[token(w)[0] for w in ps]
        expected_row={"n":n,"rooted_closed_walks":len(ws),"primitive_cycles":len(ps),"rooted_ledger_sha256":hashlib.sha256("\n".join(lines).encode()).hexdigest(),"primitive_ledger_sha256":hashlib.sha256("\n".join(plines).encode()).hexdigest()}
        assert row==expected_row; rt+=len(ws); pt+=len(ps)
    assert rt==ledger["rooted_closed_walks_through_8"]==14760 and pt==ledger["primitive_cycles_through_8"]==1905
    assert ledger["token_fields"]==["directed states","signed rational amplitude","metric length","winding vector","canonical rotation","reverse id"]
    assert ledger["phase_rule"]=="A_p*rho^n*exp(i*k*L_p)*product_j q_j^m_j"
    assert ledger["primitive_product_germ"]=="product_[p primitive](1-rho^n_p*A_p*exp(i*k*L_p)*q^m(p))"
    expected_w=[]
    for i in range(3):
        for j in range(3):
            if i==j: continue
            w=(i,j+3); tok,amp,length,winding=token(w)
            expected_w.append({"oriented_pair":[i+1,j+1],"word":[name(s) for s in w],"amplitude":fs(amp),"metric_length":length,"winding":list(winding),"phase":f"q{i+1}/q{j+1}","ledger_token":tok})
    assert ledger["shortest_orientation_witnesses"]==expected_w
    controls=data["controls"]
    assert set(controls)=={"common_phase_gauge","direction_asymmetric_reverse_length","pi_flux","pi_over_2_fixed_alpha_reversal","wrong_vertex_normalization","zero_flux_recovery"}
    assert controls["zero_flux_recovery"]=={"factor":str(zero),"passes":True}
    assert controls["common_phase_gauge"]=={"operator_defect_nonzero_entries":0,"passes":True}
    pi=sp.factor(sp.expand(D.subs({q1:-1,q2:1,q3:1})-D.subs({q1:1,q2:1,q3:1})).coeff(rho,2))
    assert pi==sp.Rational(16,9)*x1*(x2+x3) and controls["pi_flux"]=={"changes_determinant":True,"q":[-1,1,1],"rho2_coefficient_change":"16/9*x1*(x2+x3)"}
    u=(1+sp.I)/sp.sqrt(2); Pa=sp.diag(u,1,1,sp.conjugate(u),1,1); Pm=sp.diag(sp.conjugate(u),1,1,u,1,1); Ua=Pa*S*Pa; Um=Pm*S*Pm
    correct=(J*Ua.conjugate()*J-Um.inv()).applyfunc(sp.simplify); wrong=(J*Ua.conjugate()*J-Ua.inv()).applyfunc(sp.simplify)
    norm=sp.simplify(sum(sp.conjugate(v)*v for v in wrong))
    assert correct==sp.zeros(6) and sum(v!=0 for v in wrong)==8 and norm==sp.Rational(64,9)
    assert controls["pi_over_2_fixed_alpha_reversal"]=={"alpha":["pi/2","0","0"],"correct_alpha_to_minus_alpha_defect_nonzero_entries":0,"wrong_fixed_alpha_defect_nonzero_entries":8,"wrong_fixed_alpha_frobenius_norm_squared":"64/9"}
    Cbad=sp.Rational(1,2)*sp.ones(3)-sp.eye(3); bad=(Cbad.T*Cbad-sp.eye(3)).applyfunc(sp.factor)
    assert controls["wrong_vertex_normalization"]=={"coefficient":"1/2","nonzero_defect_entries":9,"unitarity_defect":ms(bad),"unitary":False}
    v=sp.symbols("v",nonzero=True); P=sp.diag(v,v**2,v**3,v,v**2,v**4); Ua2=P*S*P; asym=(J*Ua2.subs(v,1/v)*J-Ua2.inv()).applyfunc(sp.simplify)
    assert controls["direction_asymmetric_reverse_length"]=={"directed_lengths":[1,2,3,1,2,4],"preserves_reversal":False,"reversal_defect_nonzero_entries":sum(z!=0 for z in asym)}
    assert data["progress"]=={"full_laurent_determinant":"PASS_EXACT","gauge_and_antiunitary_structure":"PASS_EXACT","magnetic_unitary_family":"PASS_EXACT","orientation_sensitive_orbit_ledger":"PASS_EXACT"}
    assert data["route_a"]=={"overall":"ROUTE_A_EXPLORATORY","route_b_invocation_allowed":False,"tuple":["A1_WEAK","A2_FAIL","A3_FAIL","A4_UNITARY_OR_SCATTERING_CANDIDATE"]}
    assert data["scope_flags"]=={"claims_automorphy":False,"claims_euler_factors":False,"claims_hilbert_polya":False,"claims_root_number":False,"claims_target_divisor":False,"uses_prime_table":False,"uses_zero_table":False}
    assert data["nonclaims"]==["no prime-like orbit correspondence","no target divisor or zero census","no target functional equation or counting law","no arithmetic Euler factors or root number","no Hilbert--Polya operator or external spectral identification"]


def main():
    path=Path(sys.argv[1]) if len(sys.argv)>1 else DEFAULT
    validate(json.loads(path.read_text()))
    print("C138 independent checker: PASS (14,760 rooted / 1,905 primitive orbit receipts)")


if __name__=="__main__": main()
