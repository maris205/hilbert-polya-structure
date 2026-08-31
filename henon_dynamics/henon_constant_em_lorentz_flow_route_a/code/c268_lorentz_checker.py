#!/usr/bin/env python3
"""Independent exact-matrix and scipy-expm checker; imports no producer code."""
from __future__ import annotations
import hashlib,json
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
from scipy.linalg import expm
import sympy as sp
ROOT=Path(__file__).resolve().parents[1];P=ROOT/"results/c268_lorentz_evidence.json";ETA=np.diag([1.,-1.,-1.,-1.]);TOL=1e-9
SOURCE="a24c701881d22a4e49eaa2a44b94395c3c540b3d";EVAL="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
def phash(d):
 q=dict(d);q.pop("payload_sha256",None);return hashlib.sha256(json.dumps(q,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def q(x):return Q(x)
def Aof(k,E,B):
 ex,ey,ez=E;bx,by,bz=B
 return sp.Matrix([[0,k*ex,k*ey,k*ez],[k*ex,0,k*bz,-k*by],[k*ey,-k*bz,0,k*bx],[k*ez,k*by,-k*bx,0]])
def arr(M):return np.array(M.tolist(),dtype=float)
def main():
 d=json.loads(P.read_text());n=0
 def ok(x):
  nonlocal n;assert x;n+=1
 ok(d["candidate_id"]=="HCS-C268");ok(d["source_commit"]==SOURCE);ok(d["fixed_epoch"]==1788048000);ok(d["scope_literal"]=="NO_BAD_EULER_OR_ROOT_NUMBER");ok(d["evaluator"]["sha256"]==EVAL);ok(d["payload_sha256"]==phash(d))
 ok(d["route_a"]["tuple"]==["A0_FAIL","A1_WEAK","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"]);ok(d["route_a"]["overall"]=="ROUTE_A_REJECTED");ok(d["route_a"]["route_b_invocation_allowed"] is False)
 ok(d["convention"]["three_force"]=="du_spatial/dtau=kappa*u0*(E+v cross B)");ok(d["dynamics_contract"]["parameter"]=="proper time, not coordinate time");ok(d["dynamics_contract"]["physical_worldline_closed"] is False)
 ok(d["generic_contract"]["Ph"]=="(A^2+b^2 I)/(a^2+b^2)");ok(d["generic_contract"]["Pr"]=="(-A^2+a^2 I)/(a^2+b^2)");ok(d["null_contract"]["exp"]=="I+tau A+tau^2 A^2/2")
 ok(d["invariant_contract"]["characteristic"]=="chi_A(z)=(z^2-a^2)(z^2+b^2)")
 ok(d["generic_contract"]["exp"]=="Ph[cosh(a tau)I+sinh(a tau)A/a]+Pr[cos(b tau)I+sin(b tau)A/b]")
 ok(d["null_contract"]["integral"]=="tau I+tau^2 A/2+tau^3 A^2/6")
 ok(d["dynamics_contract"]["velocity_period"]=="nonconstant iff b>0, Pr u0!=0, and (a=0 or Ph u0=0); least 2pi/b")
 for v in d["scope_flags"].values():ok(v is False)
 z=sp.symbols('z');eta=sp.diag(1,-1,-1,-1)
 for row in d["regression"]["cases"]:
  k=q(row["kappa"]);E=list(map(q,row["E"]));B=list(map(q,row["B"]));A=Aof(k,E,B);stored=sp.Matrix([[q(x) for x in r] for r in row["A"]])
  ok(A==stored);ok(A.T*eta+eta*A==sp.zeros(4));cp=sp.Poly(A.charpoly(z).as_expr(),z);c2=q(row["char_c2"]);c0=q(row["char_c0"])
  ok(sp.expand(cp.as_expr()-(z**4+c2*z**2+c0))==0);ok(A.trace()==0)
  a2=float(row["a2"]);b2=float(row["b2"]);ok(abs((a2-b2)-float(k*k*(sum(x*x for x in E)-sum(x*x for x in B))))<TOL)
  ok(abs(a2*b2-float(k**4*sum(E[i]*B[i] for i in range(3))**2))<TOL)
  An=arr(A);I=np.eye(4);null=row["class"] in ("null","zero")
  if row["class"]=="null":ok(A**3==sp.zeros(4));ok(A**2!=sp.zeros(4));ok(row["A3_zero"] is True)
  if row["class"]=="zero":ok(A==sp.zeros(4))
  if not null:
   D=a2+b2;Ph=(An@An+b2*I)/D;Pr=(-An@An+a2*I)/D
   ok(np.linalg.norm(Ph@Ph-Ph)<TOL);ok(np.linalg.norm(Pr@Pr-Pr)<TOL);ok(np.linalg.norm(Ph@Pr)<TOL);ok(np.linalg.norm(Ph+Pr-I)<TOL)
  for sample in row["samples"]:
   t=float(q(sample["tau"]));U=np.array(sample["exp"],float);Phi=np.array(sample["integral"],float);direct=expm(t*An)
   ok(np.linalg.norm(U-direct)<TOL);ok(np.linalg.norm(U.T@ETA@U-ETA)<TOL);ok(abs(np.linalg.det(U)-1)<TOL)
   block=np.block([[An,I],[np.zeros((4,4)),np.zeros((4,4))]]);directPhi=expm(t*block)[:4,4:]
   ok(np.linalg.norm(Phi-directPhi)<TOL)
   for i in range(4):
    for j in range(4):ok(abs(U[i,j]-float(sample["exp"][i][j]))<TOL);ok(abs(Phi[i,j]-float(sample["integral"][i][j]))<TOL)
 ok(d["regression"]["counts"]=={"cases":12,"time_samples":48,"matrix_cells":1536})
 print(f"C268 independent checker: PASS ({n} assertions; exact char/Lie/null + direct expm/integral)")
if __name__=="__main__":main()
