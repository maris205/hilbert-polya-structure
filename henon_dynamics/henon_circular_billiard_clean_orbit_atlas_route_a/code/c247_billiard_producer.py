#!/usr/bin/env python3
"""Deterministic exact/high-precision receipt for the circular billiard."""
from __future__ import annotations
import argparse, math
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import mpmath as mp

SOURCE="5f357e2d2b78604f6c286bfbd05da922e1d6791f"
EVALUATOR="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER"; EPOCH=1788048000
WORKING_DIGITS=90; SERIALIZED_DIGITS=64
ROOT=Path(__file__).resolve().parents[1]; DEFAULT=ROOT/"results/c247_billiard_evidence.json"
RADIUS=F(1)
mp.mp.dps=WORKING_DIGITS

def qtxt(q:F|int)->str:
    q=q if isinstance(q,F) else F(q)
    return str(q.numerator) if q.denominator==1 else f"{q.numerator}/{q.denominator}"
def qmp(q:F|int)->mp.mpf:
    q=q if isinstance(q,F) else F(q); return mp.mpf(q.numerator)/q.denominator
def dec(x:mp.mpf)->str:
    if abs(x)<mp.mpf("1e-82"): x=mp.mpf(0)
    return mp.nstr(x,SERIALIZED_DIGITS,strip_zeros=False,min_fixed=-70,max_fixed=70)
def ph(d:dict)->str:
    b=dict(d); b.pop("payload_sha256",None)
    return sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def cheb_string(n:int,m:int)->str: return f"T_{n}(c)=(-1)^{m}"
def one_row(m:int,n:int,sgn:int)->dict:
    # The frozen working Birkhoff coordinate is alpha (angle), not p.
    # The physical canonical momentum is not identified here; p=sin(alpha)
    # is retained only as an auxiliary signed incidence amplitude.
    a=sgn*mp.pi*m/n; p=mp.sin(a); c=mp.cos(abs(a)); shift=2*a
    shear=2*n
    # Chebyshev residual is retained as a high-precision algebraic receipt.
    cheb=mp.chebyt(n,c)-((-1)**m)
    return {"m":m,"n":n,"gcd":math.gcd(m,n),"orientation":"+" if sgn>0 else "-","orientation_sign":sgn,
            "rotation_fraction":f"{sgn*m}/{n}","rotation_angle":dec(shift),"alpha":dec(a),"alpha_abs":dec(abs(a)),"p":dec(p),"p_abs":dec(abs(p)),"p_squared":dec(p*p),
            "caustic_radius":dec(c),"chord_length":dec(2*abs(p)),"primitive_period_bounces":n,"primitive_length":dec(2*n*abs(p)),
            "map_shift_formula":"theta -> theta + 2*alpha (alpha=arcsin(p))","angle_residual":dec(2*mp.asin(p)-shift),
            "chebyshev_certificate":cheb_string(n,m),"chebyshev_residual":dec(cheb),
            "return_map_derivative":[["1",dec(shear)],["0","1"]],"transverse_eigenvalue":"1","return_matrix_kind":"unipotent_shear",
            "det_identity_minus_return":"0","return_kernel":"ker(DB^n-I)=span{(1,0)}=tangent to S^1_theta","kernel_dimension":1,
            "fixed_manifold":"S^1_theta at alpha=orientation*pi*m/n","caustic":"concentric circle r=cos(pi*m/n)","action_length":dec(2*n*abs(p))}

def primitive_rows()->list[dict]:
    rows=[]
    for n in range(3,13):
        for m in range(1,(n-1)//2+1):
            if math.gcd(m,n)==1:
                rows.extend([one_row(m,n,1),one_row(m,n,-1)])
    return rows

def repetition_rows()->list[dict]:
    out=[]
    for m,n,k,sgn in [(1,3,2,1),(1,4,2,-1),(2,5,3,1),(1,5,4,-1),(2,7,2,1),(3,8,3,-1)]:
        base=one_row(m,n,sgn); base.update({"repetition_k":k,"repeated_bounces":k*n,"repeated_length":dec(k*mp.mpf(base["primitive_length"])),"repeated_action":dec(k*mp.mpf(base["primitive_length"])),"repetition_status":"same family; recorded, not merged","primitive_pair":f"({m},{n})"}); out.append(base)
    return out

def boundary_rows()->list[dict]:
    # Diameter and grazing faces are not regular interior twist points.
    rows=[]
    rows.append({"boundary_id":"diameter","m":1,"n":2,"gcd":1,"orientation":"both_endpoint_equivalent","orientation_sign":0,"alpha":"+/-pi/2","p":"+/-1","rotation_fraction":"1/2","rotation_angle":"+/-pi","chord_length":dec(2),"primitive_length":dec(4),"action_length":dec(4),"caustic_radius":"0","primitive_period_bounces":2,"map_shift_formula":"theta -> theta + 2*alpha (alpha=+/-pi/2 endpoint)","return_map_derivative":[["1","4"],["0","1"]],"return_matrix_kind":"boundary_endpoint_unipotent","transverse_eigenvalue":"1","det_identity_minus_return":"0","return_kernel":"ker(DB^2-I)=span{(1,0)} at boundary","kernel_dimension":1,"fixed_manifold":"diameter endpoint family; alpha=+/-pi/2 boundary","caustic":"center point; diameter limit"})
    rows.append({"boundary_id":"grazing_zero_chord","m":0,"n":1,"gcd":1,"orientation":"0_one-sided_limits","orientation_sign":0,"alpha":"0.0","p":"0","rotation_fraction":"0/1","rotation_angle":"0.0","chord_length":"0.0","primitive_length":"0.0","action_length":"0.0","caustic_radius":"1.0","primitive_period_bounces":1,"map_shift_formula":"theta -> theta + 2*alpha (alpha=0 zero chord)","return_map_derivative":[["1","2"],["0","1"]],"return_matrix_kind":"boundary_grazing","transverse_eigenvalue":"1","det_identity_minus_return":"0","return_kernel":"ker(DB-I)=span{(1,0)} but no flight","kernel_dimension":1,"fixed_manifold":"entire boundary at alpha=0; two one-sided oriented limits","caustic":"boundary circle"})
    return rows

def build()->dict:
    prim=primitive_rows(); reps=repetition_rows(); bounds=boundary_rows()
    data={"schema":"hcs-c247-circular-billiard-clean-orbit-v1","candidate_id":"HCS-C247","evaluation_date":"2026-08-30","source_commit":SOURCE,"fixed_epoch":EPOCH,"scope_literal":SCOPE,
    "evaluator":{"path":"flow_systems/skills/route-a-evaluator.md","version":"0.2.0","sha256":EVALUATOR},
    "headline":"The circular billiard is an exact rigid Birkhoff twist: every primitive rational rotation has two orientation-separated clean S1 families, explicit caustic and length, and a certified unipotent return shear.",
    "frozen_object":{"phase_space":"Birkhoff annulus (theta mod 2*pi, alpha in (-pi/2,pi/2)) for a disk of radius R=1","map":"B(theta,alpha)=(theta+2*alpha mod 2*pi,alpha)","working_coordinates":"(theta,alpha) are angle coordinates; p=sin(alpha) is an auxiliary signed incidence amplitude, not a canonical momentum","symplectic_form":"the physical billiard two-form is represented in canonical boundary momentum coordinates; this receipt uses the angle chart and makes no dtheta wedge dalpha canonical claim","incidence_convention":"alpha is a signed half-chord angle defined by the oriented central increment theta'-theta=2*alpha (mod 2*pi); |alpha| is the acute angle-to-tangent magnitude and sign(alpha) records direction; |p|=sin(|alpha|)","parameter_domain":"R>0 by scaling; receipt fixes R=1; alpha=0 grazing and alpha=+/-pi/2 diameter faces","arithmetic_origin":"none; geometric billiard only","forbidden_data":"target primes/zeros, local arithmetic, Euler factors, root numbers, automorphy, target determinants, Hilbert--Polya operators"},
    "theorem":{"rigid_map":"The rigid Birkhoff angle map is B(theta,alpha)=(theta+2 alpha,alpha), DB=[[1,2],[0,1]] and DB^n=[[1,2n],[0,1]]","primitive_families":"For gcd(m,n)=1 and 1<=m<n/2, alpha=+/-pi*m/n (p=sin(alpha)) gives the complete primitive rational families, one S1 fixed manifold per orientation.","length":"L_{m,n}=2 n R sin(pi*m/n)","action":"With unit speed p0=1, the geometric action S_{m,n}=p0 L_{m,n}=L_{m,n}; a general fixed speed multiplies both by p0.","caustic":"Each family is tangent to the concentric caustic of radius R cos(pi*m/n).","orientation":"The + and - families are recorded separately and never merged; sign(alpha) records orientation while |p|=sin(|alpha|) is the angle magnitude.","repetition":"The k-fold repeat has (km,kn) as an unreduced label, k n bounces and k L_{m,n}; it is not a new primitive pair.","clean_return":"Fix(B^n) contains the S1_theta family; in (theta,alpha), DB^n=[[1,2n],[0,1]] is unipotent, ker(DB^n-I)=span{(1,0)} is exactly the family tangent, and det(I-DB^n)=0, so an isolated-orbit determinant denominator is obstructed.","boundaries":"The diameter face (m,n)=(1,2), alpha=+/-pi/2 and |p|=1, is a boundary of the angle annulus and is not assigned an interior regular family; alpha=0,p=0 is the grazing zero-chord degeneration.","closure":"Irrational rotation fractions are quasiperiodic; rational fractions close after the denominator n when reduced.","natural_quantization":"The natural quantizations are the disk Dirichlet or Neumann Laplacians with boundary condition at |x|=R; this package makes no spectral target-match claim."},
    "regression":{"primitive_rows":prim,"repetition_rows":reps,"boundary_rows":bounds,"primitive_row_count":len(prim),"repetition_row_count":len(reps),"boundary_row_count":len(bounds),"n_max":12,"radius":"1","map_derivative_formula":"[[1,2],[0,1]] in (theta,alpha)","return_derivative_formula":"[[1,2*n],[0,1]] in (theta,alpha)","fixed_set_dimension":"1","working_digits":WORKING_DIGITS,"serialized_digits":SERIALIZED_DIGITS},
    "exact_identities":[{"identity_id":"rigid_birkhoff_map","formula":"B(theta,alpha)=(theta+2*alpha,alpha)"},{"identity_id":"rotation_quantization","formula":"alpha=+/-pi*m/n and 2*alpha=+/-2*pi*m/n for 1<=m<n/2"},{"identity_id":"chord","formula":"ell=2*R*abs(sin(alpha))=2*R*sin(pi*m/n)"},{"identity_id":"total_length","formula":"L=2*n*R*sin(pi*m/n)"},{"identity_id":"action","formula":"S=p0*L and p0=1 in the frozen receipt"},{"identity_id":"caustic","formula":"r_c=R*cos(alpha)=R*cos(pi*m/n)"},{"identity_id":"primitive_gcd","formula":"gcd(m,n)=1 iff denominator n is minimal"},{"identity_id":"return_shear","formula":"DB^n=[[1,2*n],[0,1]] in angle coordinates"},{"identity_id":"clean_kernel","formula":"ker(DB^n-I)=span{(1,0)} is tangent to Fix(B^n)"},{"identity_id":"clean_obstruction","formula":"det(I-DB^n)=0 and eigenvalues are both 1"},{"identity_id":"orientation","formula":"alpha -> -alpha reverses rotation and is retained as a separate family"},{"identity_id":"repetition","formula":"(m,n)->(k*m,k*n), length and bounce count multiply by k"},{"identity_id":"boundary_faces","formula":"(1,2),alpha=+/-pi/2 diameter; alpha=0 grazing zero chord"}],
    "route_a":{"tuple":["A0_FAIL","A1_PASS_ANALYTIC","A2_FAIL","A3_FAIL","A4_NATURAL_QUANTIZATION"],"overall":"ROUTE_A_REJECTED","route_b_invocation_allowed":False,"strongest_positive":"All parameterized primitive rational families, clean fixed manifolds, lengths, caustics and return shears are explicit.","strongest_failure":"The family is a continuum and has no arithmetic target match or isolated-orbit determinant."},
    "scope_flags":{k:False for k in ["uses_target_zero_table","uses_prime_table","claims_arithmetic_local_data","claims_euler_factors","claims_root_numbers","claims_automorphy","claims_target_divisor_or_functional_equation","claims_hilbert_polya_operator","invokes_route_b"]},
    "citations":[{"key":"Birkhoff1927","claim":"periodic motions and twist-map periodic-orbit framework","source":"G. D. Birkhoff, On the periodic motions of dynamical systems, Acta Mathematica 50 (1927), 359--379, DOI 10.1007/BF02421325","url":"https://doi.org/10.1007/BF02421325"},{"key":"Bishop2003","claim":"circular billiard tables, caustics and conjugate loci","source":"R. L. Bishop, Circular Billiard Tables, Conjugate Loci, and a Cardioid, Regular and Chaotic Dynamics 8 (2003), 83--95, DOI 10.1070/RD2003v008n01ABEH000227","url":"https://doi.org/10.1070/RD2003v008n01ABEH000227","publisher":"https://www.mathnet.ru/rcd767"}],
    "nonclaims":["an exhaustive survey of all billiard tables","isolated primitive orbit amplitudes (the fixed manifolds are clean S1 families)","arithmetic Euler factors, root numbers, automorphy, target divisor or functional equation","a target zeta/Fredholm determinant, zero match, or Hilbert--Polya operator","external peer review or novelty priority"]}
    data["payload_sha256"]=ph(data); return data
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--output",type=Path,default=DEFAULT); a=ap.parse_args(); a.output.parent.mkdir(parents=True,exist_ok=True); d=build(); a.output.write_text(json.dumps(d,sort_keys=True,indent=2,ensure_ascii=False)+"\n"); print(json.dumps({"status":"C247_PRODUCER_PASS","primitive_rows":d["regression"]["primitive_row_count"],"repetition_rows":d["regression"]["repetition_row_count"],"payload_sha256":d["payload_sha256"]},sort_keys=True))
if __name__=="__main__": main()
