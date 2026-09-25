# 450 — independent card-only derivation

Candidate `ANG-20260924-DAQ01`; batch `TRANSPORT-PACKET-20260924-U`, round 1/5, exactly 450–454.
This raw follows root's distinct release after its full CP1 read; no manuscript access has occurred.
Scientific input: the entire original 93-line `candidate-card.md`, reread through EOF, SHA256 `853f2b6f2bb36613c162614ebadf7fadf2a2f447a6f24669ed1766b0e45f8b59`.
ARS and local governance reads are retained from the completed CP1 and are recorded there; the card alone supplies the present scientific definitions.
Frozen CP1: `evidence/scope-review.md`, 74 lines, SHA256 `f5bb27781067b9ff8232ea0db49a1423b9c4a33a29bd2dbdbe12300f185840c4`.
Prior 442/445 and other shared-history exposure remains disclosed; no old proof, author surface, Outcome, peer/helper answer, or sibling scientific file was opened for this derivation.
Same inherited model, **NOT_CALIBRATED**: internal, non-blind AI work, not human/external/cross-model validation or a claim of independent errors.
All arguments below are analytic. No scientific code, numerical census, network, Git, PDF, delegation, new candidate, or higher-period census was used.

## 1. Full source and legal maps

Let X=(0,∞)², n=⌊x⌋, d=⌊y⌋, and A={n,d≥1, d divides n}, with the original measure dμ=dxdy/(xy).
MAIN has domain A and additive parameter a_M=n/d; G has domain X and a_G=0 if d=0, otherwise a_G=⌊n/d⌋; Q has domain A and a_Q=0.
In each case T_O(x,y)=(y,(x+a_O)/y). Since x,y>0 and a_O≥0, every legal image lies in X.
The floors and source domains are Borel; none of the integer cuts is removed. μ is σ-finite and non-atomic, with positive locally finite density on X.
Outside A, MAIN/Q have no positive-length outgoing history. Their unit arrows and all legal incoming histories remain; they are not absorbing loops.
G is total, including d=0, n=0, and other zero-quotient branches. Its totality must not be confused with surjectivity.

## 2. All inverses, with exact source and image domains

Fix target Z=(U,V)∈X and put d_Z=⌊U⌋, m_Z=⌊UV⌋.
For an integer additive parameter a≥0, the analytic branch inverse is θ_a(U,V)=(UV−a,U), on UV>a.
Indeed the first output forces the source y=U and the second forces x=UV−a; these identities prove necessity and uniqueness within that branch.
Conversely any such point satisfying its own parameter/domain law maps exactly to Z. There is no additional inverse root.
The exact integer identity ⌊UV−a⌋=m_Z−a holds also at every integer cut.

For MAIN, a=q≥1 and source admission requires d_Z≥1 and m_Z−q=d_Z q.
Thus its full image is B_M={Z: d_Z≥1, m_Z=(d_Z+1)q for an integer q≥1}, and its unique inverse there is
ι_M(Z)=θ_q(Z), q=m_Z/(d_Z+1).
Here UV≥m_Z=(d_Z+1)q≥2q>q, so the positivity guard is automatic after this exact domain test.
The reconstructed source has n=d_Z q≥1 and the required d=d_Z; this proves sufficiency as well as necessity.

For G, if d_Z=0, the reconstructed source must have a_G=0; every such target has the unique inverse θ_0(Z).
If d_Z≥1, its law a=⌊(m_Z−a)/d_Z⌋ is equivalent to
m_Z=(d_Z+1)a+r, with integer 0≤r<d_Z.
Write m_Z=(d_Z+1)b+r in ordinary Euclidean division, 0≤r≤d_Z. Then an inverse exists exactly when r<d_Z, and a=b.
Consequently B_G={d_Z=0}∪{d_Z≥1, m_Z mod(d_Z+1)<d_Z}, with ι_G=θ_0 in the first case and θ_b in the second.
Positivity is automatic: if b=0, UV>0; if b≥1, UV≥m_Z≥(d_Z+1)b>b. The reconstructed n=d_Z b+r has precisely quotient b.
The omitted residue r=d_Z represents genuine missing targets, not states to delete from X.

For Q, the only analytic inverse is θ_0(Z)=(UV,U); its exact image is B_Q={Z: d_Z,m_Z≥1, d_Z divides m_Z}.
On B_Q this reconstructed source is in A; outside B_Q there is no legal Q predecessor.
All displayed image domains are Borel. For any fixed parameter, the actual source branch is Borel and its image is the analytic inverse's preimage of that source set.
This exhausts every original label in the card's enumeration and proves that each whole partial T_O is injective, not merely each analytic branch.
No source-label cutoff, principal branch, selected predecessor, or control-domain transfer has been used.

## 3. Original log-measure IMAGE and its every-point clock

On UV>a, Dθ_a=[[V,U],[1,0]], so |det_R² Dθ_a|=U. With ρ(x,y)=1/(xy),
J_a(U,V)=ρ(θ_a(U,V))U/ρ(U,V)=UV/(UV−a).
This is positive and finite at every actual inverse point; J_0=1. It is not the bare Lebesgue inverse determinant U.
The analytic θ_a is a diffeomorphism from {U,V>0, UV>a} onto X, with inverse (x,y)↦(y,(x+a)/y).
For every Borel E in its actual restricted image domain, ordinary change of variables gives
μ(θ_a E)=∫_E [1/(UV−a)] dU dV=∫_E J_a dμ,
including when the integral is infinite. Restriction to the actual floor/domain set preserves this identity.
At assigned cuts the card's fixed-a analytic extension supplies exactly the displayed value; no a.e. change is made at the null fixed points.
At a legal source, UV=x+a, hence κ_O(x,y)=−log J_a(T_O(x,y))=log[x/(x+a)].
Thus κ_M<0 everywhere legal; κ_G≤0, with equality exactly on a_G=0; κ_Q=0 everywhere legal.
There is no terminal step clock, no new density, no clock rescaling, and no imposed positive roof.

## 4. Exact actual-history groupoid and all kernels

Write D_O^(r) for the domain of the legal r-fold iterate, D_O^(0)=X, and S_r(z)=Σ_{j=0}^{r−1}κ_O(T_O^j z), S_0=0.
The card's arrows are (z,k,w), k=r−s, whenever T_O^r z=T_O^s w legally; source w and range z.
If two witnesses have the same k, their depths differ by the same integer. Advancing the shallower witness adds the same tail sum to both S terms.
That tail is legal because the deeper witness exists. It cancels, proving that c(z,k,w)=S_r(z)−S_s(w) is well defined on equal actual triples.
For composition, align the two depths at the shared middle object by advancing the shallower meeting; its legal longer middle history guarantees the required advance.
Prefix sums then cancel at that middle object, proving c(gh)=c(g)+c(h). Units and inverses have clocks 0 and −c(g).
In particular the actual forward arrow (T_O z,−1,z) has c=−κ_O(z), as frozen.

Global injectivity lets one cancel the smaller of the two meeting depths. Therefore the following is an exact complete description, not a word groupoid:
for k≥0, (z,k,w) exists iff z∈D_O^(k) and w=T_O^k z, with c=S_k(z);
for k≤0, it exists iff w∈D_O^(−k) and z=T_O^(−k)w, with c=−S_{−k}(w).
At k=0 these descriptions give only (z,0,z). Hence the full lag kernel and the full joint lag/clock kernel are units for all three owners.
For MAIN, every nonempty sum S_r is strictly negative. Its entire clock kernel is also units.
For G, a positive-lag arrow has clock zero exactly when every edge of its actual iterate segment has a_G=0; negative-lag arrows obey the reversed condition.
This gives its full clock kernel, with all genuine zero-clock loops retained; it does not declare different words to be extra arrows.
For Q, c≡0 on the whole actual groupoid, so its full clock kernel is the entire groupoid, while lag and joint kernels remain units.

## 5. All incoming depths, source isotropy, extension isotropy, and phase

For every owner and every target w, define I_O^0(w)={w} and recursively I_O^(j+1)(w)=⋃_{v∈I_O^j(w)∩B_O}{ι_O(v)}.
The explicit B_O and ι_O above make this an exact unrestricted inverse recursion. Each level has at most one point; no upper depth is imposed.
Its union retains every finite incoming history, including a backward-infinite chain when one exists. A repeated state at different legal depths is not a deletion of its retained lag.
An injective partial functional graph has only chains or cycles: it has no merging branches, and a cycle cannot have an extra incoming feeder.
Indeed each cycle point already has its cycle predecessor, the unique inverse. This statement does not enumerate any higher-period cycles.

For a terminal point t∉Dom(T_O), its entire source class is C_t=⋃_{j≥0}I_O^j(t).
Each z∈C_t reaches t at a unique finite depth ν(z); uniqueness follows because a terminal point cannot be iterated further.
Put B(z)=S_{ν(z)}(z). The exact arrows in this class are (z,ν(z)−ν(w),w), with c=B(z)−B(w).
All its source and extension isotropy is trivial, H_z={0}, and its complete extension phase is η=h−B(z)∈R.
The physical action translates η by time t; it has no positive return. G has no terminal class because it is total.

For an arbitrary z, let P_O(z)={p≥1: z∈D_O^(p), T_O^p z=z}.
If this set is empty, source isotropy is trivial: a hypothetical equal-depth-offset meeting would cancel to an actual positive period by injectivity.
If nonempty, let p be its minimum and K=S_p(z). Euclidean division of periods along the legal cycle proves P_O(z)=p{1,2,…}.
Its source isotropy is {(z,mp,z):m∈Z}, c(z,mp,z)=mK, and the ENTIRE H_z=KZ, including H_z={0} when K=0.
At every extension point (z,h), isotropy is the subgroup of those m with mK=0: all pZ if K=0 and only the unit if K≠0.
These formulas apply to every point without a higher-period census; the existence or enumeration of periods≥2 is not being asserted.
For MAIN, any actual cycle has K<0, so extension isotropy is trivial everywhere; H is {0} at nonperiodic points and |K|Z on a cycle.
For G, a cycle has K=0 iff all its own cycle quotients vanish; otherwise K<0. For Q, H_z={0} everywhere, regardless of source isotropy.

For every source class C, choose one reference o and actual arrows o→z with clocks b_z, with b_o=0, solely to express coordinates.
The class's extension orbits are exactly parametrized by η=h−b_z modulo H_o.
Invariance follows because any two arrows o→z differ by isotropy clock in H_o; completeness follows by composing the reference arrows with that isotropy.
This is a per-class algebraic description, not a claimed global measurable selector and not deletion of any point or phase.
Physical time is η↦η+t. If H_o={0}, it is free translation on R; if H_o=LZ with L>0, it is one circle trajectory with least positive period L.
In the latter case repetitions have precisely lengths rL, r≥1. Different source classes remain distinct packets even if their lengths coincide.
For Q specifically, the entire extension orbit set is the set of source classes times R, because c≡0; its physical action has no positive return anywhere.
That last statement follows from the full zero clock, not from a higher-period source census and not by transfer to MAIN.

## 6. Complete GLOBAL fixed sets

A fixed point necessarily has x=y=t>0 and t²=t+a_O(t,t). This covers the entire carrier, including all cuts; terminal units are not map fixed points.
For MAIN, admission forces m=⌊t⌋≥1, and the quotient m/m is exactly 1. Thus t²−t−1=0 has the unique positive solution
φ=(1+√5)/2, with 1<φ<2. It is admitted since n=d=1. Therefore Fix(T_M)={(φ,φ)}.
For G, if 0<t<1 its quotient is 0, and t²=t has no solution in that interval.
If t≥1 the quotient is 1 and the same quadratic gives φ. Therefore Fix(T_G)={(φ,φ)} as well, for its separate owner.
For Q, t²=t has the unique positive solution t=1, whose source is in A; therefore Fix(T_Q)={(1,1)}.
In particular the integer-cut fixed point of Q is retained with its prescribed all-point clock. No other positive integer cut supplies a fixed point.

## 7. Entire fixed-core packets, not selected orbit representatives

Let f=(φ,φ). Since φ²=φ+1 lies in (2,3), its target integers are d_Z=1 and m_Z=2.
Both MAIN and G have exactly the inverse with additive parameter 1 there, giving ι_M(f)=ι_G(f)=(φ²−1,φ)=f.
Consequently I_M^j(f)=I_G^j(f)={f} for every j≥0; the entire source class of this fixed core is the singleton {f}, with no omitted feeder.
This singleton state class nevertheless retains ALL integer-lag isotropy arrows (f,k,f), k∈Z, not merely the identity.
At f, J=(φ+1)/φ=φ and κ=−log φ. Thus c(f,k,f)=−kL, where L=log φ>0.
For each of MAIN and G, source isotropy is Z, ENTIRE H_f=LZ, lag/clock/joint kernels on this class are units, and extension isotropy is trivial at every height.
The full physical phase is h mod L, with all phases retained. There is exactly one primitive physical packet in this whole source component, of length L, and repeats rL.
No incoming state or phase representative was discarded to obtain that multiplicity; the absence of extra predecessors was proved from the full inverse law.

Let e=(1,1) be Q's fixed point. Here d_Z=m_Z=1 and the unique inverse is ι_Q(e)=θ_0(e)=e.
Thus its entire source class is also a singleton and I_Q^j(e)={e} at every depth, while all lag arrows (e,k,e), k∈Z, remain.
Their clocks all vanish. Source isotropy and extension isotropy at every (e,h) are Z, H_e={0}, and the clock kernel is all these arrows.
The lag and joint kernels on this core are units. Its phase is the full h∈R with free physical translation, not a circle and not a positive primitive packet.
Zero-clock source repetitions are preserved but are not counted as positive physical repetitions.

## 8. Bounded verdict and nonclaims

The MAIN fixed packet itself is decisive: 1<φ<2, so L=log φ is not log p for any ordinary prime p≥2.
This is an actual least positive generator of the ENTIRE H of a complete source component, not a single-return clock that might reduce further under extra incoming histories.
Therefore MAIN fails the frozen prime-log purity condition and is **STOP / FORK**. Its positive ledger is already nonempty; no all-prime coverage or uniqueness claim is needed to establish this failure.
G has the same adverse fixed-core length as its own separate control result. Q has a zero-clock fixed source loop and no positive physical period; neither control is used to convict MAIN.
No complete ledger of MAIN/G higher-period cycles, no all-prime coverage, no global nonconjugacy/novelty theorem, and no stronger naturalness or PROVES_TOO_MUCH result is claimed.
The full source, original log measure, all-point analytic-germ version, integer lag, extension clock, incoming objects, phases, and owner boundaries remain unchanged.
Classical NOT APPLICABLE; arithmetic T1 NOT PASSED; T3 NOT AUDITED; formal coordinates UNASSIGNED; Route B NOT INVOKED.
Only this raw file was written. The original card and CP1 remain untouched; no author surface has been accessed.

EOF — independent raw complete; full self-read and hash receipt precede freeze. HOLD for root's full read and DISTINCT PAPER UNLOCK.
