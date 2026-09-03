#!/usr/bin/env python3
"""Producer-independent exact/SymPy/high-precision checker for HCS-C320."""
from __future__ import annotations
import argparse, hashlib, json, re, sys
from fractions import Fraction
from pathlib import Path
import mpmath as mp
import yaml

ROOT=Path(__file__).resolve().parents[1]
DEFAULT=ROOT/"results/c320_darboux_halphen_evidence.json"
DEFAULT_EVAL=ROOT/"evaluations/route_a/HCS-C320/2026-09-03.yaml"
SOURCE="1ccbfe2d759fe007c6b53c9646e1ab031878b34a"; SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER"
EVAL_RAW="ec086cb94fd2131f75bf138675e4fa2ca1ad2b8331f01f03b9159c069541b220"
EVAL_SEMANTIC="843b788e9bbfcbbfbd0e6c926921dba4efe05ef35c6e1464c6f085478fa9b25f"
mp.mp.dps=100

def pairs(items):
    out={}
    for k,v in items:
        if k in out: raise ValueError(f"duplicate JSON key: {k}")
        out[k]=v
    return out

def strict_json(path): return json.loads(path.read_text(),object_pairs_hook=pairs,parse_constant=lambda x:(_ for _ in ()).throw(ValueError(x)))
class UniqueLoader(yaml.SafeLoader): pass
UniqueLoader.yaml_implicit_resolvers={k:[(tag,p) for tag,p in vals if tag!="tag:yaml.org,2002:timestamp"] for k,vals in yaml.SafeLoader.yaml_implicit_resolvers.items()}
def mapping(loader,node,deep=False):
    out={}
    for kn,vn in node.value:
        if kn.tag=="tag:yaml.org,2002:merge": raise ValueError("YAML merge forbidden")
        k=loader.construct_object(kn,deep=deep)
        if type(k) is not str or k in out: raise ValueError("duplicate/non-string YAML key")
        out[k]=loader.construct_object(vn,deep=deep)
    return out
UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,mapping)
def strict_yaml(path):
    raw=path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token,(yaml.tokens.AnchorToken,yaml.tokens.AliasToken)): raise ValueError("YAML alias forbidden")
    return yaml.load(raw,Loader=UniqueLoader)
def digest(data):
    body=dict(data); body.pop("payload_sha256",None)
    return hashlib.sha256(json.dumps(body,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def leaves(v):
    if type(v) is dict:return sum(leaves(x) for x in v.values())
    if type(v) is list:return sum(leaves(x) for x in v)
    return 1
def R(text):
    if type(text) is not str:raise AssertionError("rational not string")
    value=Fraction(text);canonical=str(value.numerator) if value.denominator==1 else f"{value.numerator}/{value.denominator}"
    if text!=canonical:raise AssertionError("noncanonical rational")
    return value
DECIMAL=re.compile(r"^[+-]?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?(?:e[+-]?[0-9]+)?$")
def complex_of(v):
    if set(v)!={"re","im"} or any(type(v[k]) is not str or DECIMAL.fullmatch(v[k]) is None or not mp.isfinite(mp.mpf(v[k])) for k in ("re","im")):raise AssertionError("noncanonical/nonfinite complex decimal")
    return mp.mpc(v["re"],v["im"])
def theta(j,tau): return mp.jtheta(j,0,mp.e**(mp.pi*1j*tau))
def xv(j,tau): return -2*mp.diff(lambda t:theta(j,t),tau)/theta(j,tau)
def close_complex(v,w,tol=mp.mpf("3e-68")):
    if abs(complex_of(v)-w)>tol*max(1,abs(w)): raise AssertionError("complex decimal mismatch")

def independent_coefficients(order):
    """Use Jacobi products, independent of the producer's series division."""
    out=[[Fraction(0) for _ in range(order+1)] for _ in range(3)]
    out[0][0]=Fraction(-1,2)
    for k in range(1,order+1):
        for n in range(1,order//2+1):
            even=2*n
            if k%even==0:
                r=k//even
                out[0][k]+=4*n-8*n*((-1)**(r-1))
                out[1][k]+=4*n
                out[2][k]+=4*n
            odd=2*n-1
            if k%odd==0:
                r=k//odd
                out[1][k]+=-4*odd*((-1)**(r-1))
                out[2][k]+=4*odd
    return out

def main():
    if sys.flags.optimize: raise RuntimeError("C320 checker refuses optimized Python")
    pa=argparse.ArgumentParser();pa.add_argument("--evidence",type=Path,default=DEFAULT);pa.add_argument("--evaluation",type=Path,default=DEFAULT_EVAL);args=pa.parse_args()
    data=strict_json(args.evidence); ev=strict_yaml(args.evaluation); checks=0
    sem=hashlib.sha256(json.dumps(ev,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
    if hashlib.sha256(args.evaluation.read_bytes()).hexdigest()!=EVAL_RAW or sem!=EVAL_SEMANTIC: raise AssertionError("evaluation digest")
    checks+=2
    if digest(data)!=data.get("payload_sha256"): raise AssertionError("payload digest")
    expected={"schema","candidate_id","obstruction_id","evaluation_date","fixed_epoch","source_commit","scope_literal","evaluator","route_a_yaml","model","theorem_contract","q_series","theta_numeric_rows","collision_rows_x1_eq_x2","axis_equilibrium_rows","boundary_atlas","collision_boundary","route_a","scope_flags","nonclaims","references","enumeration","payload_sha256"}
    if set(data)!=expected: raise AssertionError("top schema")
    if (data["schema"],data["candidate_id"],data["obstruction_id"],data["evaluation_date"],data["source_commit"],data["scope_literal"],data["fixed_epoch"])!=("hcs-c320-darboux-halphen-v1","HCS-C320","HEN-O304","2026-09-03",SOURCE,SCOPE,1788393600): raise AssertionError("identity")
    if data["evaluator"]!={"authority":"flow_systems/skills/route-a-evaluator.md","version":"0.2.0","sha256":"6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"}:raise AssertionError("evaluator")
    if data["route_a_yaml"]!={"path":"evaluations/route_a/HCS-C320/2026-09-03.yaml","raw_sha256":EVAL_RAW,"semantic_sha256":EVAL_SEMANTIC}:raise AssertionError("evidence YAML lock")
    if data["model"]!={"time":"tau in the upper half-plane","polynomial_system":"x1'=x2*x3-x1*(x2+x3), cyclically","nome":"Q=exp(pi*i*tau)","scaled_variables":"Xi=xi/(pi*i)=-2*Q*d_Q log(theta_i), i=2,3,4 mapped to 1,2,3"}:raise AssertionError("model convention")
    if data["theorem_contract"]!={"theta_seed":"x1=-2*d_tau log theta2, x2=-2*d_tau log theta3, x3=-2*d_tau log theta4","eisenstein_bridge":"X1+X2+X3=-E2/2=-1/2+12*sum_(n>=1)sigma1(n)*Q^(2n)","modular_covariance":"x tilde_i(tau)=(c*tau+d)^(-2)x_i(gamma tau)+c/(c*tau+d)","chazy":"S'''=-4*S*S''+6*(S')^2 for S=x1+x2+x3","discriminant":"Delta'=-2*S*Delta","collisions":"each pair-collision stratum has a reciprocal family and a coordinate-axis equilibrium family; the three axes meet at the origin","collision_parameters":"c,C,B are complex; reciprocal charts require tau!=c; one zero of a forces the axis branch by uniqueness"}:raise AssertionError("theorem contract")
    route={"tuple":["A0_WEAK_ARITHMETIC_RELATION","A1_FAIL","A2_FAIL","A3_PARTIAL_ANALYTIC_STRUCTURE","A4_FAIL"],"overall":"ROUTE_A_REJECTED","route_b_invocation_allowed":False}
    if data["route_a"]!=route or len(data["scope_flags"])!=9 or any(type(x) is not bool or x for x in data["scope_flags"].values()):raise AssertionError("route/scope")
    checks+=18
    if set(ev)!={"schema","candidate_id","title","evaluation_date","source_commit","fixed_epoch","scope_literal","evaluator_authority","evaluator_version","evaluator_authority_sha256","obstruction_id","candidate_definition","family","phase_space","dynamics","parameters","parameter_provenance","arithmetic_origin","clock","normalization","determinant_convention","orbit_cutoff","precision","training_data","forbidden_data","artifact_paths","a0","a1","a2","a3","a4","tuple","overall_verdict","route_b_invocation_allowed","route_b_lock_reason","scope_flags","theorem_status","finite_evidence_role","source_owner_tokens"}:raise AssertionError("evaluation schema")
    if (ev["candidate_id"],ev["source_commit"],ev["scope_literal"],ev["tuple"],ev["overall_verdict"],ev["route_b_invocation_allowed"],ev["scope_flags"])!=("HCS-C320",SOURCE,SCOPE,route["tuple"],"ROUTE_A_REJECTED",False,data["scope_flags"]):raise AssertionError("evaluation semantics")
    if ev["artifact_paths"]!=["results/c320_darboux_halphen_evidence.json","THEOREM_PACKAGE.md","paper/main.pdf"]:raise AssertionError("artifact paths")
    expected_verdicts={"a0":"A0_WEAK_ARITHMETIC_RELATION","a1":"A1_FAIL","a2":"A2_FAIL","a3":"A3_PARTIAL_ANALYTIC_STRUCTURE","a4":"A4_FAIL"}
    for key,verdict in expected_verdicts.items():
        lane=ev[key]
        if set(lane)!={"verdict","evidence_status","strongest_evidence","strongest_failure"} or lane["verdict"]!=verdict or lane["evidence_status"] not in {"PROVED","STOP_SCOPED"} or type(lane["strongest_evidence"]) is not str or type(lane["strongest_failure"]) is not str:raise AssertionError(f"evaluation lane {key}")
    checks+=12
    expected_boundary=[{"face":"Im(tau)>0 and theta constants nonzero","status":"main analytic theta chart"},{"face":"Q=0 cusp","status":"boundary limit X=(-1/2,0,0), not an interior time"},{"face":"c*tau+d=0","status":"excluded modular pole of the transformed chart"},{"face":"Delta=0","status":"invariant union of pair-collision strata"},{"face":"C=0 in the reciprocal collision family","status":"nonzero fully diagonal Riccati solution for c in C and tau!=c"},{"face":"a=0 on a pair-collision stratum","status":"coordinate-axis equilibrium family with B in C; all three axes meet at the origin"},{"face":"theta zero under continuation","status":"logarithmic-derivative pole; outside the regular chart"}]
    expected_collision={"C186":"Euler-top Jacobi action-angle flow, not a modular theta-constant polynomial flow","C244":"spherical-pendulum elliptic monodromy, not PSL2 covariance of Darboux--Halphen time","C17-C18":"modular scattering clocks and open traces, not the three-component theta ODE","C35":"adelic Henon--theta scattering quantization, not the classical complex-time Halphen phase portrait"}
    expected_nonclaims=["No priority is claimed for the Darboux--Halphen system, theta solution, modular covariance, or Chazy reduction.","No exhaustive meromorphic-solution classification beyond the stated transformations and strata is claimed.","Modular-form coefficients are not target arithmetic local data and no target Euler product is asserted.","No Hilbert--Polya operator, automorphy transfer, root number, functional equation, or target-zero match is claimed."]
    expected_references=[{"url":"https://ocu-omu.repo.nii.ac.jp/record/2009467/files/111F0000002-03202-12.pdf","role":"primary historical and theta-function account"},{"doi":"10.3842/SIGMA.2018.003","arxiv":"1709.09682","role":"modern Darboux--Halphen geometry and generalizations"},{"arxiv":"solv-int/9902012","role":"modular solutions and triangle-function lineage"}]
    if data["boundary_atlas"]!=expected_boundary or data["collision_boundary"]!=expected_collision or data["nonclaims"]!=expected_nonclaims or data["references"]!=expected_references:raise AssertionError("boundary/source ownership")
    checks+=10
    order=data["q_series"]["order"]
    if set(data["q_series"])!={"order","convention","rows"} or data["q_series"]["convention"]!="theta2=2*Q^(1/4)*sum_(m>=0)Q^(m(m+1)); theta3=1+2*sum_(m>=1)Q^(m^2); theta4=1+2*sum_(m>=1)(-1)^m Q^(m^2)" or order!=128 or len(data["q_series"]["rows"])!=129 or [r["power"] for r in data["q_series"]["rows"]]!=list(range(129)):raise AssertionError("series order/schema")
    coeff=independent_coefficients(order)
    for k,row in enumerate(data["q_series"]["rows"]):
        expected_e2=Fraction(-1,2) if k==0 else Fraction(12*sum(d for d in range(1,k//2+1) if (k//2)%d==0)) if k%2==0 else Fraction(0)
        if set(row)!={"power","X1","X2","X3","minus_half_E2","sum_bridge_residual","residuals"} or row["power"]!=k or [R(row[x]) for x in ("X1","X2","X3")]!=[Fraction(coeff[j][k]) for j in range(3)] or R(row["minus_half_E2"])!=expected_e2 or R(row["sum_bridge_residual"])!=0 or sum(R(row[x]) for x in ("X1","X2","X3"))!=expected_e2 or [R(x) for x in row["residuals"]]!=[0,0,0]:raise AssertionError(f"series row {k}")
        checks+=11
    expected_points=[("1/7","4/5"),("2/9","11/10"),("-1/5","3/2"),("3/13","7/10"),("-2/11","6/5"),("1/3","9/5")]
    if len(data["theta_numeric_rows"])!=6 or [(r["tau"]["re"],r["tau"]["im"]) for r in data["theta_numeric_rows"]]!=expected_points:raise AssertionError("numeric rows")
    for row in data["theta_numeric_rows"]:
        if set(row)!={"tau","x","ode_residual","T_residual","S_residual"} or set(row["tau"])!={"re","im"} or any(len(row[key])!=3 for key in ("x","ode_residual","T_residual","S_residual")) or any(set(z)!={"re","im"} for key in ("x","ode_residual","T_residual","S_residual") for z in row[key]):raise AssertionError("numeric row schema")
        tau=mp.mpf(Fraction(row["tau"]["re"]).numerator)/Fraction(row["tau"]["re"]).denominator+1j*mp.mpf(Fraction(row["tau"]["im"]).numerator)/Fraction(row["tau"]["im"]).denominator
        xs=[xv(j,tau) for j in (2,3,4)]
        dx=[mp.diff(lambda t,j=j:xv(j,t),tau) for j in (2,3,4)]
        rhs=[xs[1]*xs[2]-xs[0]*(xs[1]+xs[2]),xs[2]*xs[0]-xs[1]*(xs[2]+xs[0]),xs[0]*xs[1]-xs[2]*(xs[0]+xs[1])]
        residual=[dx[i]-rhs[i] for i in range(3)]
        tv=[xv(j,tau+1) for j in (2,3,4)]; tr=[tv[0]-xs[0],tv[1]-xs[2],tv[2]-xs[1]]
        sv=[tau**(-2)*xv(j,-1/tau)+1/tau for j in (2,3,4)]; sr=[sv[0]-xs[2],sv[1]-xs[1],sv[2]-xs[0]]
        for stored,w in zip(row["x"],xs):close_complex(stored,w)
        for key,vals in (("ode_residual",residual),("T_residual",tr),("S_residual",sr)):
            for stored,w in zip(row[key],vals):close_complex(stored,w)
            if max(map(abs,vals))>mp.mpf("5e-78"):raise AssertionError(f"{key} lock")
        checks+=30
    rows=data["collision_rows_x1_eq_x2"]
    expected_collision_coords=[(c,C,t) for c in (-3,-1,2) for C in (-2,0,3) for t in (4,7)]
    if len(rows)!=18 or [(r["c"],r["C"],r["t"]) for r in rows]!=expected_collision_coords:raise AssertionError("collision rows")
    for row in rows:
        if set(row)!={"c","C","t","a","b","a_prime","b_prime","residual_a","residual_b"}:raise AssertionError("collision row schema")
        u=Fraction(row["t"]-row["c"]); a=1/u;b=1/u+Fraction(row["C"],u*u);ap=-1/(u*u);bp=-1/(u*u)-2*Fraction(row["C"],u*u*u)
        if [R(row[x]) for x in ("a","b","a_prime","b_prime","residual_a","residual_b")]!=[a,b,ap,bp,Fraction(0),Fraction(0)]:raise AssertionError("collision")
        checks+=10
    axes=data["axis_equilibrium_rows"]
    if len(axes)!=15:raise AssertionError("axis rows")
    expected_axes=[]
    for zero_pair,axis in (((1,2),3),((2,3),1),((3,1),2)):
        for value in (-3,-1,0,2,5):expected_axes.append((list(zero_pair),axis,value))
    for row,expected_axis in zip(axes,expected_axes):
        if set(row)!={"zero_pair","free_axis","value","point","vector_field"}:raise AssertionError("axis row schema")
        zp,axis,value=expected_axis;point=[0,0,0];point[axis-1]=value
        x,y,z=point;vf=[y*z-x*(y+z),z*x-y*(z+x),x*y-z*(x+y)]
        if (row["zero_pair"],row["free_axis"],row["value"],row["point"],row["vector_field"])!=(zp,axis,value,point,vf):raise AssertionError("axis equilibrium")
        checks+=8
    enum=data["enumeration"]
    if set(enum)!={"q_series_rows","theta_numeric_rows","collision_rows","axis_equilibrium_rows","audited_leaf_count"}:raise AssertionError("enumeration schema")
    if (enum["q_series_rows"],enum["theta_numeric_rows"],enum["collision_rows"],enum["axis_equilibrium_rows"])!=(129,6,18,15):raise AssertionError("enumeration")
    body=dict(data);body.pop("payload_sha256")
    if enum["audited_leaf_count"]!=leaves(body):raise AssertionError("leaf count")
    checks+=4
    print(f"C320 independent checker: PASS ({checks} checks)")
if __name__=="__main__":main()
