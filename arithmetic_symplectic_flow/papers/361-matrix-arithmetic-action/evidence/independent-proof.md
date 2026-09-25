# Independent proof — full matrix arithmetic action

Candidate: `ANG-20260921-MAA01`.
Standing: actual Haar clock owned; paired extra primitives and nondiscrete
time groups give **STOP / FORK** for the full frozen object.
Internal derivation: `NOT_CALIBRATED`, not external peer review.

## 1. Input and scope

I personally read candidate-card.md lines 1–118 through its authorized EOF,
including the real-height clarification, and measured SHA-256
`67cbafaf771cbc6ae3849d21f8a13165ea9eb24863a98ded81fa49a66d0ab2f4`.
This was the sole new scientific input. No manuscript, peer, scout, prior
scientific file, network source, numerical experiment or auxiliary was read
or used. ARS router/DA/runtime/workflow instructions remain retained from
their prior complete reads. Same model and shared history, with the card's
disclosed expectations, do not constitute blindness or error independence.
The report covers all frozen cores and all column vectors, not an unrequested
classification of arbitrary matrix orbits. Findings were sent to root before
writing; author-manuscript review is not claimed. R below is the adelic ring;
all clocks, heights and physical times instead belong to the real line.

## 2. Actual action, domains and arithmetic interface

The specified ring is the restricted product of Q_p with respect to Z_p.
An element g of Gamma is exactly a family g_p in GL_2(Q_p) with
g_p in U_p=GL_2(Z_p) outside finitely many primes: both g and its inverse
must have adelic entries. U=product_p U_p. In particular invertibility is
not asserted merely from nonzero determinant in a ring with zero divisors.
The matrix-and-inverse topology makes multiplication, inversion and the
action on W continuous. Right multiplication by u preserves X exactly.
Thus D_(g,u)=X intersect g^{-1}X, interpreting left multiplication on matrices,
is a compact open additive subgroup. It is not necessarily all X.
The action restricts to a homeomorphism of D_(g,u) onto D_(g^{-1},u^{-1}).
Direct composition gives (g_2g_1,u_2u_1); direct inversion gives precisely
the card's inverse. This is the full reduction of the ambient action, so
all incoming to B are exactly (g,u,g^{-1}Bu) with g^{-1}Bu in X.
Every object retains its identity and globally legal unit arrows, including
zero; a forbidden label does not impose a terminal convention on the object.
Different actual labels remain different arrows. For example (aI,aI),
a in K^times, acts identically on all matrices but is not discarded.

At A_n=diag(n,1), the action of (diag(1/d,1),I) gives diag(n/d,1).
It lies in X exactly when n/d lies in K, equivalently v_p(d)<=v_p(n)
for every p, equivalently d divides the embedded integer n. This is the
promised exact divisor interface, not a selection of prime transitions.

## 3. Haar IMAGE on all Borel sets and the all-point character

Put chi(g)=product_p |det g_p|_p, a finite product. Locally, elementary
row shears and permutations preserve additive Haar on Q_p^2; diagonal
scaling by p^k multiplies it by p^{-k}, from subgroup coset indices, and
unit scaling preserves it. Elimination over the FIELD Q_p therefore gives
the IMAGE factor |det g_p|_p on a column. Two columns give its square.
Only finitely many local factors differ from 1; the remaining g_p preserve
the full local integral lattice. Hence nu(gX)=chi(g)^2.
The measure E -> nu(gE) is translation-invariant Haar; uniqueness with
the computed normalization gives the IMAGE equality on EVERY
Borel subset of W, not just cylinders or X itself. Right u contributes 1.
Consequently mu(theta_(g,u) E)=chi(g)^2 mu(E) for every Borel E subset D_(g,u).
Compact openness of gX also proves finite strict positivity directly.

Thus J(g,u)=chi(g)^2 is the actual frozen ambient IMAGE, and
c(g,u)=-log J=2 sum_p v_p(det g_p) log p.
Its multiplicative/additive laws follow from determinant multiplication.
This constant-on-label all-point version applies to every null source state;
it is specified and verified, not inferred as an a.e.-unique pointwise value.
Its FULL arrow kernel consists of the legal arrows with v_p(det g_p)=0
for EVERY p. Indeed a finite product of prime powers equals 1 only with
every exponent zero. This condition need not put g in U: nonintegral
determinant-one shears, for example, retain zero clock on their legal domains.
The extension and height translations are thus defined on all X times the
real line. We claim only the orbit set/quotient sigma-algebra, not a nice
coarse manifold. Every fixed-time induced map is measurable.

## 4. Entire stabilizers of the joint matrix cores

An idempotent e has e_p either 0 or 1. Set S={p:e_p=0} and T its complement.
All stabilizer descriptions below impose the global conditions g in Gamma,
u in U; thus local g is integral invertible outside finitely many primes.
At p in T both A_e and B_e equal I, so g_p=u_p without further restriction.
At p in S, A_e equals E=diag(0,1). The equation gE=Eu is exactly
g_p=[[a,0],[c,t]],   u_p=[[r,b],[0,t]],
where a in Q_p^times, c in Q_p, r,t in Z_p^times and b in Z_p.
This follows by comparing all four entries, so no stabilizing labels are lost.
At p in S, B_e is zero and the entire local stabilizer is instead arbitrary
g_p in GL_2(Q_p), u_p in U_p. These are the FULL source stabilizers.

For BOTH families the possible determinant valuations are arbitrary integers
at finitely many p in S and zero elsewhere. All these choices are attained.
Writing Lambda_S=sum_{p in S} Z log p, the entire groups are
H_(A_e)=H_(B_e)=2 Lambda_S.
Their isotropy-kernel and extension isotropy are exactly the displayed
stabilizers with every determinant valuation zero. For A_e this requires
a to be a p-adic unit but still permits the stated nonintegral c; for B_e
it permits every local determinant-unit matrix, not only U_p.
For I (S empty) the stabilizer is {(u,u):u in U}, H=0, and the entire
stabilizer remains extension isotropy. For 0=B_0 it is Gamma times U,
H=2 Lambda_all, with its full determinant-unit kernel retained.

If S={p}, the ENTIRE time group is 2 log p Z and its least positive element
is 2 log p, not merely the time of a chosen stabilizing arrow. If S has
at least two primes, Lambda_S is dense and nondiscrete: log p/log q is
irrational by unique prime factorization, and the elementary pigeonhole
approximation gives nonzero integer combinations arbitrarily close to zero.
Multiples of these approximate any real number. No primitive is assigned
to this dense group. S empty instead gives zero time, not a positive orbit.

## 5. All incoming, actual identifications and complete phase

Here are complete source-orbit tests for the frozen main cores. A matrix Y
lies in the orbit of A_e iff its local ranks are 2 on T and 1 on S,
Y_p is in U_p for all but finitely many p in T, and its entries generate
Z_p for all but finitely many p in S. It lies in the orbit of B_e iff
Y_p=0 on S, has rank 2 on T, and lies in U_p for almost all p in T.
Necessity uses unit left/right changes outside the finite exceptional set.
For sufficiency, an integral rank-one matrix has an entry of minimal
valuation: after factoring that power of p, a unit pivot allows integral
row/column elimination to E. Rank-two integral unit matrices already need
only a unit change. Use these changes at all good places and arbitrary
invertible changes at the finitely many remaining places; they assemble
to actual g in Gamma and u in U. This also proves no incoming was omitted.
The unrestricted label formula in section 2 retains every arrow between
these orbit objects, not a chosen elimination or normal-form quotient.

Local ranks are invariant under EVERY arrow and physical height translation.
Thus different e within either family never merge; A_e cannot merge with
any B_f unless both equal I. For every singleton S={p}, the two positive
packets above are therefore genuinely distinct at the same least time.
This is at least two packets, not a global matrix census. Zero, singular
and idempotent points are retained despite their zero singleton Haar mass.

In any owner, fix a core C and any arrow k:C->Y. Its complete extension
phase is h-c(k) modulo H_C; changing k changes this by exactly isotropy.
This describes ALL incoming phases, including ineffective isotropy, zero
and dense groups. Different source orbits cannot merge by time translation.

## 6. UNIT-ONLY: its own full action and all tested cores

Both left and right groups are U, every domain is all X, and the local
Haar argument gives J=1, c=0 on ALL arrows. Its full kernel is its entire
groupoid and H=0 at every matrix. Extension isotropy equals source isotropy.
At A_e its stabilizer is section 4 with a,c additionally integral and a a
unit; at B_e the zero-place groups are U_p times U_p; on T still g=u.
This includes I and 0. Its orbit tests are section 5 with no exceptional
primes allowed. Unit-pivot elimination proves sufficiency place by place.
All incoming labels are (g,u,g^{-1}Yu), now with g,u in U. Heights themselves
are the phases, and distinct tested cores retain the same rank separation.

## 7. ONE-COLUMN: full classification of stabilizers for ALL vectors

Its own domain is K^2 intersect g^{-1}K^2; every inverse and incoming is
g^{-1}wa with a in K^times. Right scalar units preserve its lattice and
Haar measure. The one-column Haar calculation gives
J_1(g,a)=chi(g), c_1=sum_p v_p(det g_p) log p, on every Borel set and point.
For arbitrary v in K^2 let v(p) be its local vector and S_v={p:v(p)=0}.
Outside S_v write v(p)=p^{m_p} L_p e_1, m_p=min_i v_p(v_i), L_p in U_p;
set m_p=infinity on S_v.
Such L_p exists by a unit pivot, and all L_p assemble to an element of U.
The ENTIRE local stabilizer at these places is
L_p^{-1}g_p L_p=[[a_p,b_p],[0,d_p]], b_p in Q_p, d_p in Q_p^times.
At p in S_v, g_p is arbitrary. The right a remains any global unit.
All local families must satisfy the usual restricted-product condition.
The free second direction, even when v has no zero components, realizes
any finitely supported determinant valuations. Therefore EVERY vector,
including zero, has the SAME entire H_v=Lambda_all, dense and nondiscrete.
Its isotropy-kernel/extension isotropy is this full stabilizer with every
determinant valuation zero. The full-arrow kernel uses that same character
condition, not a restriction to integral matrices. No positive primitive exists.
Two vectors v,w are in the same source orbit exactly when S_v=S_w and
m_p(v)=m_p(w) outside finitely many primes. Necessity follows from unit
changes; sufficiency uses the above frames and finitely many local scalings.
These are all incoming objects, with every actual label and the phase of
section 5 retained. A zero-set-only orbit classification would be incomplete.

## 8. CENTRAL-INDEX: actual group elements, own clock and cores

An actual g in Gamma_c has g_p=p^{k_p}V_p, V_p in U_p, with integers k_p
of finite support. The k_p are intrinsic; redundant choices of scalar unit
and V are not extra arrow labels. Scalar p^{k_p} acts on four additive
coordinates and the unit factors preserve Haar, so its own matrix IMAGE is
J_c=product_p p^{-4k_p}, so c_c=4 sum_p k_p log p.
For A_e, at every place its nonzero unit column forces k_p=0 in a
stabilizer. Hence its entire stabilizer is the UNIT-ONLY stabilizer and H=0.
For B_e the condition is k_p=0 on T, arbitrary finite-support k_p on S,
with g=u on T and otherwise arbitrary local scalar-times-unit g and u.
Thus H_(B_e)=4 Lambda_S, with the zero/single-prime/dense alternatives
as above. This includes H_0=4 Lambda_all and H_I=0. The full c-kernel has
all k_p=0, hence g in U; extension isotropy is the corresponding UNIT-ONLY
stabilizer. This is independently determined, not borrowed from MAIN.
The complete core orbit consists exactly of local unit left/right transforms
of p^{k_p}C_p with finite-support k_p; integrality requires k_p>=0 where
C_p is nonzero, while zero places impose no such constraint. The actual
inverse formula lists all incoming labels. Rank separation and section 5's
phase formula apply, with this own c_c and H, not MAIN's factor of two.

## 9. Adverse check and precise stop

The divisor interface and full Haar character are genuinely owned positives.
Nevertheless the paired single-prime cores produce distinct positive packets
at the same least time, and the full zero core has nondiscrete time. A common
time-unit change cannot remove either obstruction. No singular stratum,
ineffective kernel, right action or idempotent component may be discarded.
The control differences confirm the ownership boundary rather than repair
MAIN. No global classification of other matrices or new trace is asserted.
Strong naturalness remains OPEN; T3 is not audited, classical A0/A1/A2 are
not applicable, formal Route unassigned and Route B not invoked. Stop/fork
this candidate with its source, measure, clock and all-point version intact.

EOF — full joint diagnostic and three own controls; no manuscript read.
