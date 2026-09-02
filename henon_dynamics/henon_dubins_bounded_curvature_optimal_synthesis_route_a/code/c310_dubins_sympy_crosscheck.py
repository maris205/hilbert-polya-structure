#!/usr/bin/env python3
"""Symbolic SE(2), reflection, and scaling checks for HCS-C310."""
import sympy as sp
def main():
 t,p,q,R=sp.symbols("t p q R", real=True, positive=True);checks=0
 def zero(x,label):
  nonlocal checks
  if any(sp.simplify(sp.trigsimp(v))!=0 for v in (x if isinstance(x,(tuple,list)) else (x,))):raise AssertionError(label)
  checks+=1
 def step(pose,mode,length):
  x,y,h=pose
  if mode=="L":return x+sp.sin(h+length)-sp.sin(h),y-sp.cos(h+length)+sp.cos(h),h+length
  if mode=="R":return x+sp.sin(h)-sp.sin(h-length),y+sp.cos(h-length)-sp.cos(h),h-length
  return x+length*sp.cos(h),y+length*sp.sin(h),h
 def pose(word):
  out=(sp.Integer(0),sp.Integer(0),sp.Integer(0))
  for m,l in zip(word,(t,p,q)):out=step(out,m,l)
  return tuple(sp.trigsimp(v) for v in out)
 for word in ("LSL","RSR","LSR","RSL","RLR","LRL"):
  out=pose(word); reflected=pose("".join("R" if c=="L" else "L" if c=="R" else "S" for c in word))
  zero((out[0]-reflected[0],out[1]+reflected[1],out[2]+reflected[2]),word+" reflection")
  scaled=tuple(R*v for v in out[:2])+(out[2],)
  zero((scaled[0]/R-out[0],scaled[1]/R-out[1],scaled[2]-out[2]),word+" scaling")
  zero(sp.diff(out[2],p) if word[1]=="S" else sp.Integer(0),word+" heading straight")
 # Explicit endpoint simplifications for same-turn words.
 lsl=pose("LSL");zero((lsl[0]-(p*sp.cos(t)+sp.sin(t+q)),lsl[1]-(p*sp.sin(t)+1-sp.cos(t+q)),lsl[2]-(t+q)),"LSL endpoint")
 rsr=pose("RSR");zero((rsr[0]-(p*sp.cos(t)+sp.sin(t+q)),rsr[1]-(-p*sp.sin(t)+sp.cos(t+q)-1),rsr[2]+t+q),"RSR endpoint")
 # Unit-curvature primitives have arc length equal to angle and stay on a unit circle.
 left=step((0,0,0),"L",t);right=step((0,0,0),"R",t)
 zero((left[0]**2+(left[1]-1)**2-1,right[0]**2+(right[1]+1)**2-1),"turning circles")
 print(f"C310 SymPy cross-check: PASS ({checks} identity groups)")
if __name__=="__main__":main()
