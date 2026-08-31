#!/usr/bin/env python3
"""Independent checker: no import from the producer."""
from __future__ import annotations
import hashlib,json
from fractions import Fraction
from pathlib import Path
import mpmath as mp
ROOT=Path(__file__).resolve().parents[1]; P=ROOT/"results/c267_wannier_evidence.json"; mp.mp.dps=90
SOURCE="a24c701881d22a4e49eaa2a44b94395c3c540b3d"; EVAL="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
TOL=mp.mpf("1e-68")
def val(s): return mp.mpf(s)
def cval(q): return val(q["re"])+1j*val(q["im"])
def phash(d):
 q=dict(d);q.pop("payload_sha256",None);return hashlib.sha256(json.dumps(q,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def K(F,J,r,n,m):
 th=mp.sign(F)*2*mp.pi*r; z=mp.mpf(0) if r in (0,1) else 4*mp.mpf(J)/F*mp.sin(th/2)
 return 1j**(n-m)*mp.exp(-1j*th*(n+m)/2)*mp.besselj(n-m,z),z,th
def main():
 d=json.loads(P.read_text()); a=0
 def ok(x):
  nonlocal a; assert x; a+=1
 ok(d["candidate_id"]=="HCS-C267");ok(d["source_commit"]==SOURCE);ok(d["fixed_epoch"]==1788048000)
 ok(d["scope_literal"]=="NO_BAD_EULER_OR_ROOT_NUMBER");ok(d["evaluator"]["sha256"]==EVAL);ok(d["payload_sha256"]==phash(d))
 ok(d["route_a"]["tuple"]==["A0_FAIL","A1_WEAK","A2_FAIL","A3_FAIL","A4_NATURAL_QUANTIZATION"])
 ok(d["route_a"]["overall"]=="ROUTE_A_REJECTED");ok(d["route_a"]["route_b_invocation_allowed"] is False)
 ok(d["fourier_contract"]["eigenvector"]=="phi_m(n)=J_{n-m}(2J/F)")
 ok(d["fourier_contract"]["gauge"]=="G=exp(-i(2J/F)sin(k)); Hhat=G^{-1}(-iF d/dk)G")
 ok(d["propagator_contract"]["least_identity_return"]=="2*pi/abs(F)")
 for x in d["scope_flags"].values(): ok(x is False)
 for row in d["regression"]["propagation_rows"]:
  F,J=row["F"],row["J"]; r=Fraction(row["period_fraction"]); _,z,th=K(F,J,r,0,0)
  ok(abs(val(row["z"])-z)<TOL);ok(abs(val(row["second_moment"])-z*z/2)<TOL)
  for e in row["kernel_entries"]:
   q,_,_=K(F,J,r,e["n"],e["m"]);ok(abs(cval(e["value"])-q)<TOL)
  for e in row["delta_shell"]: ok(abs(val(e["probability"])-mp.besselj(e["n"],z)**2)<TOL)
  # Independent differential-equation residual fixes every phase and index sign.
  t=2*mp.pi*mp.mpf(r.numerator)/(abs(F)*r.denominator); zp=2*J*mp.cos(th/2)
  for n in range(-3,4):
   m=1; q,_,_=K(F,J,r,n,m); order=n-m; pref=1j**order*mp.exp(-1j*th*(n+m)/2)
   dq=pref*((-1j*F*(n+m)/2)*mp.besselj(order,z)+zp*(mp.besselj(order-1,z)-mp.besselj(order+1,z))/2)
   qp,_,_=K(F,J,r,n+1,m);qm,_,_=K(F,J,r,n-1,m)
   ok(abs(1j*dq-(F*n*q-J*(qp+qm)))<mp.mpf("1e-60"))
  if r==0:
   for e in row["kernel_entries"]: ok(abs(cval(e["value"])-(1 if e["n"]==e["m"] else 0))<TOL)
  if r==1:
   for e in row["kernel_entries"]: ok(abs(cval(e["value"])-(1 if e["n"]==e["m"] else 0))<TOL)
  if J==0: ok(abs(val(row["second_moment"]))<TOL)
 for row in d["regression"]["eigen_rows"]:
  F,J,m=row["F"],row["J"],row["m"];aa=mp.mpf(2)*J/F; comp={x["n"]:val(x["value"]) for x in row["components"]}
  ok(abs(val(row["a"])-aa)<TOL);ok(row["energy"]==F*m)
  for n,v in comp.items(): ok(abs(v-mp.besselj(n-m,aa))<TOL)
  for n in range(-9,10): ok(abs(F*n*comp[n]-J*(comp[n+1]+comp[n-1])-F*m*comp[n])<mp.mpf("1e-60"))
 counts=d["regression"]["counts"];ok(counts=={"parameter_time_rows":210,"kernel_cells":1050,"shell_cells":5250,"eigen_rows":90,"eigen_cells":1890})
 # Analytic ledger checks are structural; their proofs are in THEOREM_PACKAGE/paper.
 ok(d["spectral_contract"]["resolvent_Sp"]=="iff p>1 for z outside F*Z")
 ok(d["spectral_contract"]["U_compact"] is False);ok(d["spectral_contract"]["resolvent_trace_class"] is False)
 print(f"C267 independent checker: PASS ({a} assertions; phase/PDE/eigen/shell/route locks)")
if __name__=="__main__":main()
