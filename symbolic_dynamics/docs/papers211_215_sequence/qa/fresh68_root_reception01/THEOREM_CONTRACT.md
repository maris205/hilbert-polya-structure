# P215 bounded prefix-drawdown theorem contract

Admission2026-09-11UTC. Author proof: ../../scouting/finite_residual_fresh68/DESK.md,
independent candidate gate: ../../scouting/finite_residual_fresh68_gate/DECISION.md.
Only systemA is admitted, not the separate interval-hull-complement negative.

For integers n,q>=0 take X={0,...,q}^n. For n>0 set
F(x)_i=max_(1<=j<=i)x_j-x_i; the empty word is fixed. Coordinates remain
labelled and ordered, with no sorting, wraparound or driving schedule.

1. Adjoin x_0=0. Delete zero successive differences and compress each
   same-sign run into one sign. Let R(x) be its length. For x!=0,
   R(Fx)=R(x)-1. Zero is uniquely recurrent and its exact first hitting
   time from every x is h(x)=R(x), including h(0)=0.
2. For positive n,q the maximum is n, attained exactly when all n
   initial-zero differences are nonzero and alternate signs. The empty
   and q=0 carriers have height0.
3. For n>0 a target has predecessors iff y_1=0. Let its zero positions
   be1=z_1<...<z_k, z_(k+1)=n+1, b_j=max_(z_j<=i<z_(j+1))y_i and
   B_j=max_(r<=j)b_r. Every predecessor is uniquely
   x_i=L_j-y_i on blockj, where0<=L_1<=...<=L_k<=q and L_j>=B_j.
4. Put c_i=q-B_(k+1-i), A_0=1 and for1<=m<=k
   A_m=binom(c_m+m,m)-sum_(i=1)^(m-1)
       A_(i-1)binom(c_m-c_i+m-i,m-i+1).
   Then the target fibre has sizeA_k. Use the zero convention for a
   lower binomial index exceeding its nonnegative upper index.
5. For n>0 the image has(q+1)^(n-1) elements. For positive n,q the
   unique largest fibre is at0^n, of sizebinom(q+n,n). Singleton
   boundaries have their unique fibre of size1.

Attribute the classical drawdown statistic and every static barrier-counting
primitive. Do not claim a new general enumeration method, all-time inverse
atlas, arbitrary poset extension, global priority or universal no-factor
theorem. The substantive residual is the exact pointwise autonomous clock
plus full record-height inverse reconstruction, under the received bounded
collision/source gate. A later exact owner/factor hit reopens admission.

Prepare one standalone author verifier SOURCE only for the fixed24boxes
n in{0,1,2,3,4,5}, q in{0,1,2,3}, all Cartesian states, including duplicate
singleton boundary boxes as separate parameter cases. Source-derived total
1798states is an expectation, not an executed count. Actual transitions,
repeat-only orbits/clocks, complete target-predecessor buckets, independently
constructed record heights, binomial recurrence values, image/maximal-fibre
sets and full named comparisons must appear in deterministic complete output.
No cutoff enlargement, random pilot, scientific import/parse/run, canonical
or build is authorized here; source reception and separate grant come first.
Prefer builtin-only arithmetic/iteration and a proved deterministic wire
encoder, retaining sys for argv/stdout, to keep the runtime boundary small.

Anonymous self-contained ordinary article/AMS short note with explicit
limitations; manuscript/source/proof/claim/parameter/schema roles follow the
existing batch contract. No template placeholders count as completed evidence.
Two distinct nonauthor reviews, exact deltas, physicalRound0/1/2, full
author/A/B replay keys, two final source-only builds and all-page views
remain mandatory. OWNER_AMBER/HOLD_EXTERNAL.
