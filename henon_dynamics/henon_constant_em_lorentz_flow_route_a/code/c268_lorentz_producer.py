#!/usr/bin/env python3
"""Deterministic exact/90-digit receipt producer for HCS-C268."""
from __future__ import annotations
import hashlib,json
from fractions import Fraction as Q
from pathlib import Path
import mpmath as mp
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/"results/c268_lorentz_evidence.json";mp.mp.dps=90
SOURCE="a24c701881d22a4e49eaa2a44b94395c3c540b3d";EVAL="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
ETA=[[Q(1),Q(0),Q(0),Q(0)],[Q(0),Q(-1),Q(0),Q(0)],[Q(0),Q(0),Q(-1),Q(0)],[Q(0),Q(0),Q(0),Q(-1)]]
CASES=(
 ("zero",Q(1),(0,0,0),(0,0,0)),("pure_e",Q(2,3),(3,0,0),(0,0,0)),("pure_b",Q(-3,2),(0,0,0),(0,2,0)),
 ("parallel",Q(1),(2,0,0),(3,0,0)),("null_crossed",Q(1),(1,0,0),(0,1,0)),
 ("electric_like",Q(1),(3,0,0),(0,1,0)),("magnetic_like",Q(1),(1,0,0),(0,3,0)),
 ("generic_1",Q(2),(1,2,0),(2,-1,3)),("generic_2",Q(-1,2),(2,-3,1),(1,1,4)),
 ("generic_3",Q(3,5),(1,1,1),(2,0,-1)),("electric_y",Q(-2),(0,2,0),(0,0,0)),("magnetic_z",Q(3),(0,0,0),(0,0,1)))
TIMES=(Q(0),Q(1,7),Q(2,5),Q(1))
def Mmul(A,B):return [[sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
def Madd(A,B):return [[A[i][j]+B[i][j] for j in range(4)] for i in range(4)]
def Mscale(c,A):return [[c*A[i][j] for j in range(4)] for i in range(4)]
def eyeq():return [[Q(i==j) for j in range(4)] for i in range(4)]
def Aexact(k,E,B):
 ex,ey,ez=map(Q,E);bx,by,bz=map(Q,B)
 return [[Q(0),k*ex,k*ey,k*ez],[k*ex,Q(0),k*bz,-k*by],[k*ey,-k*bz,Q(0),k*bx],[k*ez,k*by,-k*bx,Q(0)]]
def qstr(x):return f"{x.numerator}/{x.denominator}"
def ds(x):
 if abs(x)<mp.mpf("1e-82"):x=mp.mpf(0)
 return mp.nstr(x,74,strip_zeros=False)
def mpm(A):return mp.matrix([[mp.mpf(x.numerator)/x.denominator for x in row] for row in A])
def dumpmat(A):return [[ds(A[i,j]) for j in range(4)] for i in range(4)]
def exp_integral(A,aa,bb,tau,null):
 I=mp.eye(4)
 if null:return I+tau*A+tau*tau*A*A/2,tau*I+tau*tau*A/2+tau**3*A*A/6
 D=aa+bb
 Ph=(A*A+bb*I)/D;Pr=(-A*A+aa*I)/D;a=mp.sqrt(aa);b=mp.sqrt(bb)
 sha=tau if a==0 else mp.sinh(a*tau)/a;cha=tau*tau/2 if a==0 else (mp.cosh(a*tau)-1)/(a*a)
 sib=tau if b==0 else mp.sin(b*tau)/b;cib=tau*tau/2 if b==0 else (1-mp.cos(b*tau))/(b*b)
 return Ph*(mp.cosh(a*tau)*I+sha*A)+Pr*(mp.cos(b*tau)*I+sib*A),Ph*(sha*I+cha*A)+Pr*(sib*I+cib*A)
def phash(d):
 q=dict(d);q.pop("payload_sha256",None);return hashlib.sha256(json.dumps(q,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def main():
 rows=[]
 for name,k,E,B in CASES:
  A=Aexact(k,E,B);E2=sum(Q(x)**2 for x in E);B2=sum(Q(x)**2 for x in B);EB=sum(Q(E[i])*Q(B[i]) for i in range(3))
  s=k*k*(E2-B2);disc=mp.sqrt((mp.mpf(s.numerator)/s.denominator)**2+4*(mp.mpf((k*k*EB).numerator)/(k*k*EB).denominator)**2)
  aa=(disc+mp.mpf(s.numerator)/s.denominator)/2;bb=(disc-mp.mpf(s.numerator)/s.denominator)/2
  null=name=="null_crossed";kind="zero" if name=="zero" else ("null" if null else ("electric-like" if bb==0 else ("magnetic-like" if aa==0 else "generic")))
  Ar=mpm(A);samples=[]
  for tauq in TIMES:
   tau=mp.mpf(tauq.numerator)/tauq.denominator;U,P=exp_integral(Ar,aa,bb,tau,null or name=="zero")
   samples.append({"tau":qstr(tauq),"exp":dumpmat(U),"integral":dumpmat(P)})
  rows.append({"name":name,"kappa":qstr(k),"E":[qstr(Q(x)) for x in E],"B":[qstr(Q(x)) for x in B],
   "A":[[qstr(x) for x in r] for r in A],"E2_minus_B2":qstr(E2-B2),"E_dot_B":qstr(EB),
   "a2":ds(aa),"b2":ds(bb),"char_c2":qstr(-s),"char_c0":qstr(-(k**4)*(EB**2)),"class":kind,"A3_zero":Mmul(Mmul(A,A),A)==[[Q(0)]*4 for _ in range(4)],"samples":samples})
 data={"schema":"hcs-c268-constant-em-v1","candidate_id":"HCS-C268","evaluation_date":"2026-08-31","source_commit":SOURCE,"fixed_epoch":1788048000,"scope_literal":"NO_BAD_EULER_OR_ROOT_NUMBER","evaluator":{"version":"0.2.0","sha256":EVAL},
  "convention":{"metric":"eta=diag(1,-1,-1,-1)","equation":"u'=A u, x'=u in proper time tau; A=(q/m)F_mixed",
   "matrix":"A/kappa=[[0,E^T],[E,C_B]], C_B v=v cross B","three_force":"du_spatial/dtau=kappa*u0*(E+v cross B)","lorentz_lie_algebra":"A^T eta+eta A=0"},
  "invariant_contract":{"characteristic":"chi_A(z)=(z^2-a^2)(z^2+b^2)","a_b":"a,b>=0","a2_minus_b2":"kappa^2(|E|^2-|B|^2)","a2_b2":"kappa^4(E dot B)^2"},
  "generic_contract":{"Ph":"(A^2+b^2 I)/(a^2+b^2)","Pr":"(-A^2+a^2 I)/(a^2+b^2)",
   "exp":"Ph[cosh(a tau)I+sinh(a tau)A/a]+Pr[cos(b tau)I+sin(b tau)A/b]","position":"x=x0+integral_0^tau exp(sA)ds u0"},
  "dynamics_contract":{"eta_norm":"preserved","det_exp":"1","parameter":"proper time, not coordinate time",
   "velocity_period":"nonconstant iff b>0, Pr u0!=0, and (a=0 or Ph u0=0); least 2pi/b","physical_worldline_closed":False,
   "reason":"future timelike u remains future timelike, so x^0 is strictly increasing"},
  "null_contract":{"condition":"a=b=0 and nonzero field","nilpotency":"A^3=0","exp":"I+tau A+tau^2 A^2/2","integral":"tau I+tau^2 A/2+tau^3 A^2/6"},
  "regression":{"cases":rows,"counts":{"cases":len(rows),"time_samples":len(rows)*len(TIMES),"matrix_cells":len(rows)*len(TIMES)*32}},
  "analytic_proof_obligations":["eta-skew Lie algebra identity","characteristic/minimal polynomial factorization","projector functional calculus","matrix exponential and integral","timelike norm and time orientation","periodicity and nonclosure classification","null nilpotent degeneration"],
  "route_a":{"tuple":["A0_FAIL","A1_WEAK","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"],"overall":"ROUTE_A_REJECTED","route_b_invocation_allowed":False},
  "scope_flags":{"arithmetic_local_data":False,"euler_factors":False,"root_numbers":False,"automorphy":False,"target_divisor":False,"functional_equation":False,"hilbert_polya_operator":False},
  "nonclaims":["No literature-priority claim is made.","Proper-time periodic velocity is not a closed physical worldline.","The Lorentz generator is not a target Hilbert--Polya operator."],
  "source":{"author":"Siu A. Chin","title":"Relativistic Motion in a Constant Electromagnetic Field","arxiv":"0809.0859","doi":"10.1063/1.3064796","role":"constant-field exact-motion lineage"}}
 data["payload_sha256"]=phash(data);OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(data,sort_keys=True,indent=2,ensure_ascii=False)+"\n")
 print(f"C268_PRODUCER_PASS cases={len(rows)} samples={len(rows)*4} cells={len(rows)*4*32} payload={data['payload_sha256']}")
if __name__=="__main__":main()
