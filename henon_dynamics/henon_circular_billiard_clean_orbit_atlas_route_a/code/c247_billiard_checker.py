#!/usr/bin/env python3
"""Producer-independent checker for the circular-billiard receipt."""
from __future__ import annotations
import argparse, math, re
from hashlib import sha256
import json
from pathlib import Path
import mpmath as mp

ROOT=Path(__file__).resolve().parents[1]; DEFAULT=ROOT/"results/c247_billiard_evidence.json"
SOURCE="5f357e2d2b78604f6c286bfbd05da922e1d6791f"; EVAL="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"; SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER"; EPOCH=1788048000
mp.mp.dps=100
TOP={"schema","candidate_id","evaluation_date","source_commit","fixed_epoch","scope_literal","evaluator","headline","frozen_object","theorem","regression","exact_identities","route_a","scope_flags","citations","nonclaims","payload_sha256"}
FLAGS={"uses_target_zero_table","uses_prime_table","claims_arithmetic_local_data","claims_euler_factors","claims_root_numbers","claims_automorphy","claims_target_divisor_or_functional_equation","claims_hilbert_polya_operator","invokes_route_b"}
ROW_KEYS={"m","n","gcd","orientation","orientation_sign","rotation_fraction","rotation_angle","alpha","alpha_abs","p","p_abs","p_squared","caustic_radius","chord_length","primitive_period_bounces","primitive_length","action_length","map_shift_formula","angle_residual","chebyshev_certificate","chebyshev_residual","return_map_derivative","transverse_eigenvalue","return_matrix_kind","det_identity_minus_return","return_kernel","kernel_dimension","fixed_manifold","caustic"}
REP_EXTRA={"repetition_k","repeated_bounces","repeated_length","repeated_action","repetition_status","primitive_pair"}
BOUNDARY_KEYS={"boundary_id","m","n","gcd","orientation","orientation_sign","alpha","p","rotation_fraction","rotation_angle","chord_length","primitive_length","action_length","caustic_radius","primitive_period_bounces","map_shift_formula","return_map_derivative","return_matrix_kind","transverse_eigenvalue","det_identity_minus_return","return_kernel","kernel_dimension","fixed_manifold","caustic"}
NUM=re.compile(r"^-?(?:0|[1-9][0-9]*)(?:\.[0-9]+|[eE][+-]?[0-9]+)?$")
def ph(d):
    b=dict(d); b.pop("payload_sha256",None); return sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def close(v,x,label,ck,tol="2e-35"):
    ck(isinstance(v,str) and NUM.fullmatch(v) is not None,label+" syntax")
    if isinstance(v,str) and NUM.fullmatch(v): ck(abs(mp.mpf(v)-x)<=mp.mpf(tol)*max(1,abs(x)),label+" value")
def expected_pairs():
    for n in range(3,13):
        for m in range(1,(n-1)//2+1):
            if math.gcd(m,n)==1:
                for s in (1,-1): yield m,n,s
def validate(d):
    c=0
    def ck(ok,label):
        nonlocal c;c+=1
        if not ok: raise AssertionError(label)
    def ex(a,b,label): ck(type(a) is type(b) and a==b,label)
    ck(set(d)==TOP,"top closure"); ex(d["schema"],"hcs-c247-circular-billiard-clean-orbit-v1","schema"); ex(d["candidate_id"],"HCS-C247","candidate"); ex(d["evaluation_date"],"2026-08-30","date"); ex(d["source_commit"],SOURCE,"source"); ex(d["fixed_epoch"],EPOCH,"epoch"); ex(d["scope_literal"],SCOPE,"scope"); ex(d["evaluator"],{"path":"flow_systems/skills/route-a-evaluator.md","version":"0.2.0","sha256":EVAL},"evaluator"); ex(d["payload_sha256"],ph(d),"payload")
    ex(d["route_a"]["tuple"],["A0_FAIL","A1_PASS_ANALYTIC","A2_FAIL","A3_FAIL","A4_NATURAL_QUANTIZATION"],"route tuple"); ex(d["route_a"]["overall"],"ROUTE_A_REJECTED","route verdict"); ex(d["route_a"]["route_b_invocation_allowed"],False,"route B"); ck(set(d["scope_flags"])==FLAGS,"flag keys"); ck(all(v is False for v in d["scope_flags"].values()),"flags false")
    for phrase in ("rigid Birkhoff","primitive rational","clean","unipotent","quasiperiodic","isolated-orbit determinant","Dirichlet or Neumann"):
        ck(phrase in json.dumps(d["theorem"],ensure_ascii=False),"theorem "+phrase)
    ex(d["theorem"]["rigid_map"],"The rigid Birkhoff angle map is B(theta,alpha)=(theta+2 alpha,alpha), DB=[[1,2],[0,1]] and DB^n=[[1,2n],[0,1]]","rigid angle convention")
    ex(d["theorem"]["clean_return"],"Fix(B^n) contains the S1_theta family; in (theta,alpha), DB^n=[[1,2n],[0,1]] is unipotent, ker(DB^n-I)=span{(1,0)} is exactly the family tangent, and det(I-DB^n)=0, so an isolated-orbit determinant denominator is obstructed.","clean-return theorem")
    reg=d["regression"]; ex(reg["radius"],"1","radius"); ex(reg["n_max"],12,"n max"); ex(reg["fixed_set_dimension"],"1","fixed dimension"); ex(reg["primitive_row_count"],44,"primitive summary"); ex(reg["repetition_row_count"],6,"repeat summary"); ex(reg["boundary_row_count"],2,"boundary summary"); ex(reg["map_derivative_formula"],"[[1,2],[0,1]] in (theta,alpha)","map derivative formula"); ex(reg["return_derivative_formula"],"[[1,2*n],[0,1]] in (theta,alpha)","return derivative formula")
    prim=reg["primitive_rows"]; idx=0
    for m,n,s in expected_pairs():
        row=prim[idx];idx+=1; ck(set(row)==ROW_KEYS,"primitive keys %d"%idx); ex(row["m"],m,"m %d"%idx); ex(row["n"],n,"n %d"%idx); ex(row["gcd"],1,"gcd %d"%idx); ex(row["orientation_sign"],s,"sign %d"%idx); ex(row["orientation"],"+" if s>0 else "-","orientation %d"%idx); ex(row["rotation_fraction"],f"{s*m}/{n}","fraction %d"%idx); ex(row["map_shift_formula"],"theta -> theta + 2*alpha (alpha=arcsin(p))","map formula %d"%idx); ex(row["primitive_period_bounces"],n,"bounces %d"%idx); ex(row["return_matrix_kind"],"unipotent_shear","shear kind %d"%idx); ex(row["transverse_eigenvalue"],"1","eigen %d"%idx); ex(row["det_identity_minus_return"],"0","det %d"%idx); ex(row["return_kernel"],"ker(DB^n-I)=span{(1,0)}=tangent to S^1_theta","kernel %d"%idx); ex(row["kernel_dimension"],1,"kernel dimension %d"%idx); ex(row["fixed_manifold"],"S^1_theta at alpha=orientation*pi*m/n","fixed set %d"%idx); ex(row["caustic"],"concentric circle r=cos(pi*m/n)","caustic text %d"%idx)
        a=s*mp.pi*m/n; pp=mp.sin(a); cc=mp.cos(abs(a)); sh=2*a; shear=2*n
        for k,x in (("alpha",a),("alpha_abs",abs(a)),("p",pp),("p_abs",abs(pp)),("p_squared",pp*pp),("caustic_radius",cc),("chord_length",2*abs(pp)),("primitive_length",2*n*abs(pp)),("action_length",2*n*abs(pp)),("rotation_angle",sh),("angle_residual",2*mp.asin(pp)-sh),("chebyshev_residual",mp.chebyt(n,cc)-((-1)**m))): close(row[k],x,f"{k} {idx}",ck)
        ex(row["chebyshev_certificate"],f"T_{n}(c)=(-1)^{m}","cheb certificate %d"%idx); ck(isinstance(row["return_map_derivative"],list) and len(row["return_map_derivative"])==2 and all(len(z)==2 for z in row["return_map_derivative"]),"matrix dimensions %d"%idx); ex(row["return_map_derivative"][0][0],"1","matrix 00 %d"%idx); close(row["return_map_derivative"][0][1],shear,"matrix shear %d"%idx,ck); ex(row["return_map_derivative"][1],["0","1"],"matrix lower %d"%idx)
    reps=reg["repetition_rows"]; ex(len(reps),6,"repeat rows")
    for i,row in enumerate(reps):
        ck(set(row)==ROW_KEYS|REP_EXTRA,"repeat keys %d"%i); m,n,k,s=[(1,3,2,1),(1,4,2,-1),(2,5,3,1),(1,5,4,-1),(2,7,2,1),(3,8,3,-1)][i]; ex(row["m"],m,"repeat m");ex(row["n"],n,"repeat n");ex(row["repetition_k"],k,"repeat k");ex(row["repeated_bounces"],k*n,"repeat bounces");ex(row["primitive_pair"],f"({m},{n})","repeat pair");ex(row["repetition_status"],"same family; recorded, not merged","repeat status"); close(row["repeated_length"],k*2*n*mp.sin(mp.pi*m/n),"repeat length",ck); close(row["repeated_action"],k*2*n*mp.sin(mp.pi*m/n),"repeat action",ck); ex(row["orientation_sign"],s,"repeat sign")
    bounds=reg["boundary_rows"]; ex(len(bounds),2,"boundary rows")
    for i,row in enumerate(bounds):
        ck(set(row)==BOUNDARY_KEYS,"boundary keys %d"%i)
        if i==0:
            for k,v in (("boundary_id","diameter"),("m",1),("n",2),("gcd",1),("orientation","both_endpoint_equivalent"),("orientation_sign",0),("alpha","+/-pi/2"),("p","+/-1"),("rotation_fraction","1/2"),("rotation_angle","+/-pi"),("chord_length","2"),("primitive_length","4"),("action_length","4"),("caustic_radius","0"),("primitive_period_bounces",2),("map_shift_formula","theta -> theta + 2*alpha (alpha=+/-pi/2 endpoint)"),("return_matrix_kind","boundary_endpoint_unipotent"),("transverse_eigenvalue","1"),("det_identity_minus_return","0"),("kernel_dimension",1),("fixed_manifold","diameter endpoint family; alpha=+/-pi/2 boundary"),("caustic","center point; diameter limit")): ex(row[k],v,"diameter %s"%k)
            ex(row["return_map_derivative"],[["1","4"],["0","1"]],"diameter matrix")
        else:
            for k,v in (("boundary_id","grazing_zero_chord"),("m",0),("n",1),("gcd",1),("orientation","0_one-sided_limits"),("orientation_sign",0),("alpha","0.0"),("p","0"),("rotation_fraction","0/1"),("rotation_angle","0.0"),("chord_length","0.0"),("primitive_length","0.0"),("action_length","0.0"),("caustic_radius","1.0"),("primitive_period_bounces",1),("map_shift_formula","theta -> theta + 2*alpha (alpha=0 zero chord)"),("return_matrix_kind","boundary_grazing"),("transverse_eigenvalue","1"),("det_identity_minus_return","0"),("return_kernel","ker(DB-I)=span{(1,0)} but no flight"),("kernel_dimension",1),("fixed_manifold","entire boundary at alpha=0; two one-sided oriented limits"),("caustic","boundary circle")): ex(row[k],v,"grazing %s"%k)
            ex(row["return_map_derivative"],[["1","2"],["0","1"]],"grazing matrix")
    ids={x.get("identity_id") for x in d["exact_identities"]}; ex(len(d["exact_identities"]),13,"identity count")
    for x in ("rigid_birkhoff_map","rotation_quantization","chord","total_length","action","caustic","primitive_gcd","return_shear","clean_kernel","clean_obstruction","orientation","repetition","boundary_faces"): ck(x in ids,"identity "+x)
    ex(len(d["citations"]),2,"citation count"); ex(d["citations"][0]["url"],"https://doi.org/10.1007/BF02421325","Birkhoff DOI"); ex(d["citations"][1]["url"],"https://doi.org/10.1070/RD2003v008n01ABEH000227","Bishop DOI"); ex(len(d["nonclaims"]),5,"nonclaims")
    return c
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--evidence",type=Path,default=DEFAULT);ap.add_argument("--quick",action="store_true");a=ap.parse_args();d=json.loads(a.evidence.read_text())
    if a.quick: assert set(d)==TOP and d["candidate_id"]=="HCS-C247" and d["payload_sha256"]==ph(d);print("C247 quick hostile preflight: PASS")
    else: print(f"C247 independent checker: PASS ({validate(d)} assertions; rigid map, primitive families, clean shears)")
if __name__=="__main__": main()
