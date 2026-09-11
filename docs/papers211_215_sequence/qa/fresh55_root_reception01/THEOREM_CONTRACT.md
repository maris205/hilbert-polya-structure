# P214 bounded theorem contract

Frozen at admission 2026-09-11 UTC; original proof is
../../scouting/finite_residual_fresh55/PROOF_PACKAGE.md, independently gated
in ../../scouting/finite_residual_fresh55_gate/DECISION.md.

For every prime power q and m>=2 set R=F_q[t]/(t^m), I=tR,
F(x,y)=(y,x(t+y)) on the full I², and v(0)=m.

1. First hitting time of (0,0), with a=v(x), b=v(y), is
   tau=max{2(m-b),2(m-a)-1}. Zero is uniquely recurrent, of period one.
   Maximum depth 2m-2 is attained exactly when v(y)=1.
2. For 0<=h<=2m-2 there are q^h states of depth at most h; exact depth h>0
   has (q-1)q^(h-1) states. This is a temporal corollary, not a third axis.
3. At target (u,w), d=min(v(t+u),m-1). Reachability is equivalent to
   w in t^(d+1)R. A nonempty fibre consists of (x_0+k,u) for all
   k in t^(m-d)R and has q^d elements.
4. For 1<=d<=m-2 exactly (q-1)q^(2(m-d-1)) targets have q^d predecessors;
   q saturated targets (-t+c t^(m-1),0) have q^(m-1) predecessors.
   Image size is q+(q-1) sum_(j=1)^(m-2) q^(2j); remaining fibres are empty.
5. m=2 is the linear boundary. At m>=3 unequal positive fibres exclude
   conjugacy to any finite-group endomorphism. The linear map (y,tx) has
   the same pointwise clock and depth census; do not claim those shapes new.

No extension to arbitrary finite chain rings, all-time fibres, functional-
graph isomorphism classification, new general contraction method, global
priority, or nonlinear-factor absence. The full inverse is known-mechanism
evaluation through F=QMP, P(x,y)=(x,y+t), Q(u,w)=(u-t,w), M(a,b)=(b,ab).
The substantive temporal advance is its nonlinear cancellation-safe clock.

Prepare a standalone author verifier SOURCE only for q in {2,3,4} and
m in {2,3,4}, with explicit F4 arithmetic (not Z/4Z), all states, transitions,
actual depths and target predecessor sets, complete claim-by-claim checks
and deterministic full output. No cutoff enlargement or execution follows
from this document. A separate source reception/runtime grant is required.
Anonymous self-contained short article, ordinary article/AMS typesetting;
no conference submission scope. Two eligible reviews and all terminal
evidence remain mandatory. OWNER_AMBER / HOLD_EXTERNAL.
