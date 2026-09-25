# HCH01 — independent raw-card derivation

Result: the full frozen conditional owners and all-point clocks exist. MAIN has a genuine primitive physical time strictly between log 2 and log 3: **STOP / FORK, no promotion**.
All histories, null periodic paths, actual lags and phases remain. Three controls have their own ledgers below; FINITE-TWO has source periods but no positive physical returns.

## 1. Input and independence boundary

Sole scientific input: [candidate card](../candidate-card.md), original complete 88 lines, SHA256 `d970a8ed78a30f2bd70323c88b322ecdfe7d4b5abdd5b2490d029e4fb82755bd`.
The card was fully read at CP1 and its hash reverified after root's explicit mathematical release; no main manuscript, peer report, other raw proof or old scientific document was read.
Candidate ANG-CONTROL-20260922-HCH01; MEASURED-HISTORY-20260922-E, fifth round. Retained ARS and stream instructions apply.
Shared history and prior scope access are disclosed: same-model internal derivation, NOT blind, NOT_CALIBRATED, not independent peer review.
No network, scientific numerical computation, auxiliary delegation or model change. Only this file is written; the 75-line scope report remains frozen.
No theorem from 065/367/371 or another owner is imported. This is explicitly a nearest-neighbor / Markov boundary CONTROL, not an infinite-memory escape.

## 2. Complete conditional probability owners

The following calculation is instantiated separately for MAIN, UNCONSTRAINED and GEOMETRIC-LAW; FINITE-TWO is handled on its own two-state carrier in Section 8.
Let alpha be the prescribed positive probability on A={2,3,...}; let s(a,b) be the own symmetric admission indicator.
Set Z_alpha(a)=sum_b alpha(b)s(a,b), C_alpha=sum_a alpha(a)Z_alpha(a), pi_alpha(a)=alpha(a)Z_alpha(a)/C_alpha, and P_alpha(a,b)=alpha(b)s(a,b)/Z_alpha(a).
MAIN has alpha(a)=1/[a(a-1)] and s(a,b)=1 iff gcd(a,b)=1. Telescoping sum_(a=2..N)(1/(a-1)-1/a)=1-1/N proves sum alpha=1.
GEOMETRIC-LAW has alpha(a)=2^(1-a) and the same hard admission; its geometric series also sums to 1.
For both hard owners every a has infinitely many legal neighbors ka+1, k>=1. Thus 0<Z_alpha(a)<=1 and 0<C_alpha<=1; all displayed denominators are positive finite.
UNCONSTRAINED has the MAIN alpha but s=1 on all pairs, hence its OWN Z=1, C=1, pi=alpha and P(a,b)=alpha(b).
In each of these three owners rows of P sum to 1 and pi sums to 1. Directly,
pi(a)P(a,b)=alpha(a)alpha(b)s(a,b)/C=pi(b)P(b,a).
Summing in a proves sum_a pi(a)P(a,b)=pi(b). Reversibility here concerns the transition law; it does NOT say that the one-sided shift is bijective.

Let X_alpha be the entire own allowed one-sided path space. The finite-cylinder probabilities pi(x_0) product_(i=0..n-2)P(x_i,x_(i+1)) are compatible by row normalization.
The countable-alphabet product probability extension gives a probability on A^N0; every forbidden adjacent event has probability zero, so their countable union does too.
Restriction to the closed allowed path space therefore gives the claimed probability on the ENTIRE X_alpha, not a restricted set of sample paths.
Every nonempty allowed finite cylinder has positive probability and has a legal continuation, proving full support in the relative product topology.
Stationarity gives shift invariance on cylinders by summing their predecessors, hence on all Borel sets by uniqueness of finite measures.
The alphabet is discrete and countable; the allowed path space is a standard Borel subspace of the countable product. No compactification or extra boundary path is inserted.

Every allowed transition has 0<P(a,b)<1 in these three infinite-alphabet owners: each row has at least two positive alternatives.
There are NO atoms, including at periodic paths. Indeed if mu({x})=epsilon>0, invariance gives mu({T^n x})>=epsilon for every n.
An infinite forward orbit would contain infinitely many distinct atoms of mass at least epsilon, impossible for a probability; thus x is eventually periodic.
For an eventually periodic x, cylinder masses along repeated copies of its tail cycle have a factor q^j with 0<q<1, the product of its cycle transitions.
Continuity from above then gives mu({x})=0, a contradiction. This proves the atom statement at every path, not merely almost everywhere.

## 3. All inverse branches and EVERY-Borel IMAGE

For each permitted letter a, E_a={y:s(a,y_0)=1} is clopen, and I_a(y)=ay is a homeomorphism from E_a onto {x in X:x_0=a}.
T I_a=id on E_a and I_(x_0) T x=x for every x. Every predecessor has exactly this form, with no other predecessor and no missing legal letter.
All histories are obtained by finite legal prefixes; infinitely long histories mean coherent choices of these actual predecessors, not an extra source state.
For a cylinder B=[b_0,...,b_(n-1)] contained in E_a, detailed balance gives
mu(I_a B)=pi(a)P(a,b_0) product_(i<n-1)P(b_i,b_(i+1))=P(b_0,a)mu(B).
On each fixed b_0 piece this extends from cylinders to EVERY Borel subset by finite-measure uniqueness; countable disjoint summation covers all E_a.
Consequently mu(I_a B)=integral_B j_a dmu for every Borel B subset E_a, with j_a(y)=P(y_0,a) on the ENTIRE declared domain.
j_a is positive finite and locally constant. For every y, every allowed cylinder neighborhood fixing y_0,...,y_n has exactly this IMAGE ratio.
Thus the specified version is fixed at every null periodic or nonperiodic path by the same cylinder law, not reassigned after a return calculation.
Also sum_a j_a(y)=sum_a P(y_0,a)=1, so decomposing T^-1 B into the disjoint I_a(B intersect E_a) reproves full shift invariance.

For a finite word u of length m, I_u(t)=ut has domain D_u consisting of tails for which this entire concatenation is allowed; the empty word is the identity on X.
The domain is empty for an internally forbidden word, and otherwise is the exact last-letter admission domain. These are ALL finite inverse histories.
Writing x=ut, repeated IMAGE substitution gives
j_u(t)=product_(i=0..m-1)P(x_(i+1),x_i), and mu(I_u B)=integral_B j_u dmu for EVERY Borel B subset D_u.
This can equally be checked on cylinders and extended as above; it is not a branch-mass heuristic. Put A_m(x)=-log j_u(T^m x), A_0=0.
For legal u,v and t in D_u intersect D_v, the prefix replacement I_u I_v^-1 has IMAGE derivative j_u(t)/j_v(t) at y=vt, by the two integral identities.
All such maps are Borel homeomorphisms of their actual domains; they cover every arrow of the frozen lag groupoid.

## 4. All-arrow clock, complete kernels and incoming arrows

Write G={g=(z,k,y): T^m z=T^n y for some m,n>=0, k=m-n}, with source y and range z; equal triples, and only equal triples, are identified.
Composition adds k and inverse negates k. The common-tail representation is z=ut, y=vt, m=|u|, n=|v|, with both concatenations legal.
c(g)=A_m(z)-A_n(y)=-log(j_u(t)/j_v(t)) is therefore the actual negative-log IMAGE of that prefix replacement.
If a second representation has the same k, its two indices differ from m,n by a common integer; after ordering them, both A sums acquire the same common-tail sum.
It cancels, proving descent on equal triples, including periodic triples. Aligning common tails proves composition; equivalently the all-point IMAGE ratios multiply.
Thus c is a genuine real Borel cocycle, with c(g^-1)=-c(g), and keeps the frozen inverse-arrow direction.

Here is an explicit finite-product description of the FULL kernels, requiring no unproved logarithmic independence.
For each of the three infinite owners put Lambda(a)=Z(a)/alpha(a), Q(u)=product_(letters of u)Lambda(a), Q(empty)=1.
Direct multiplication yields exp A_m(x)=Q(x_0...x_(m-1)) Z(x_m)/Z(x_0), including m=0.
Hence for z=ut,y=vt the exact clock multiplier is Delta(g)=Z(y_0)Q(u)/[Z(z_0)Q(v)].
The FULL clock kernel consists of ALL legal common-tail triples satisfying Z(y_0)Q(u)=Z(z_0)Q(v).
The FULL lag kernel consists of ALL legal triples represented by |u|=|v|; its intersection with the clock kernel imposes BOTH that equality of lengths and the preceding product equality.
These necessary-and-sufficient tests cover empty prefixes, arbitrary tails and all lags; they are not restricted to isotropy, cycles or a chosen word family.
No endpoint-only or effective quotient replaces G, and no assertion that either global kernel is merely units is made.

For any range point z, all incoming arrows are precisely (z,m-|v|,v T^m z), where m>=0 and v is any legal finite prefix for T^m z, including empty.
Representations yielding the same triple are identified, but different retained lags are never identified. This lists every predecessor branch and every incoming finite history.
In the extension, the corresponding incoming arrow to (z,h) starts at (v T^m z,h-c(g)); EVERY real h is retained.

## 5. Entire isotropy, packets, repetitions and physical phases

For a one-sided sequence x, a nonzero isotropy lag means T^m x=T^n x with m!=n, which is equivalent to eventual periodicity.
If x is not eventually periodic its entire source isotropy is {0}. Otherwise let L be the least period of its eventual tail.
Every equality of sufficiently shifted tails has lag divisible by L, and every multiple of L occurs beyond the preperiod; hence the entire source isotropy is LZ.
For completeness, if a tail has a least period L and a second period k, shifting farther into that periodic tail and dividing k by L gives a period k mod L; minimality forces that remainder to vanish.
This is groupoid isotropy, not direct T-periodicity of every predecessor: T^n x=x for n>0 holds exactly when x itself is purely periodic and its least word period divides n.
An arbitrary finite incoming prefix may therefore have no direct T return while retaining the eventual cycle's full groupoid isotropy.

An eventual periodic class has a unique primitive cyclic word w=(a_0,...,a_(L-1)) up to rotation, with every cyclic adjacent pair legal, and w not a proper word power.
Conversely every such word gives the periodic path w^infinity and its entire class
O_[w]={u T^j(w^infinity): u any finite prefix making a legal path, j=0,...,L-1}.
Two such classes coincide exactly when their primitive words differ by rotation: common eventual tails force equality of the primitive cycles.
This retains every incoming prefix and phase; it is not selection of a periodic representative as the carrier.

For each of the three infinite owners, the cycle clock is
tau_alpha(w)=sum_(i=0..L-1)-log P(a_(i+1),a_i)=log product_(i=0..L-1)[Z_alpha(a_i)/alpha(a_i)], with indices cyclic.
Although individual Lambda(a) need not exceed 1, each allowed transition is strictly below 1; therefore tau_alpha(w)>0.
At EVERY x in O_[w], cancellation of the finite preperiod gives c(x,jL,x)=j tau_alpha(w) for all j in Z.
Thus source isotropy is LZ, extension isotropy is {0}, and the ENTIRE physical stabilizer is H_x=tau_alpha(w)Z on the whole class.
At a non-eventually-periodic x both source and extension isotropy are {0}, and H_x={0}. In particular extension isotropy is trivial everywhere in these three owners.
All powers of the primitive source cycle remain distinct lag arrows; the j-th positive repetition has source lag jL and physical time j tau_alpha(w).

To verify physical ownership directly, fix any source orbit O and a base b only as a proof coordinate, not as a restriction on states.
Map [(x,h)] to h+c(g) modulo H_b for any arrow g:x->b. Two choices differ by isotropy at b, so this is well-defined, and two points have the same value exactly when extension arrows identify them.
It gives the full orbit SET over O as R/H_b, with physical action adding t. Its entire stabilizer is exactly H_b.
Thus every O_[w] contributes the phase circle R/[tau_alpha(w)Z] and ALL its height phases; every non-eventually-periodic source orbit contributes a free real line.
These are identifications of sets with a real action only; no quotient topology, smooth geometry or invariant flow measure is asserted.
Distinct primitive cyclic classes remain distinct packets even when their times coincide. The exact multiplicity at t>0 is
N_alpha(t)=#{[w] cyclic: w primitive, cyclically allowed, log product_(a in w)[Z_alpha(a)/alpha(a)]=t}.
This is the full packet ledger with repetitions as above; it does not assume finiteness of N_alpha(t), merge colliding lengths or select representatives as states.
Written powers must first reduce to their least word period; no positive primitive or repetition is inferred from the written length alone.

## 6. MAIN: exact decisive packet, no numerical approximation

For MAIN constants are forbidden because gcd(a,a)=a>1. The word (2,3) is legal cyclically and primitive because its distinct letters prevent period 1.
Its periodic core has least T-period 2; every point in its whole eventual class has source isotropy 2Z, trivial extension isotropy, and H=log Q_23 Z, where Q_23=12 Z(2)Z(3).
To bound this EXACTLY, write
Z(2)=sum_(k>=1)1/[2k(2k+1)]=integral_0^1 t/(1+t) dt=1-log 2.
The integral identity follows by summing the nonnegative integrands t^(2k-1)(1-t); no exchange of conditionally convergent terms is used.
For 1<u<2, 1/u<3/2-u/2, so log 2<3/4. Also substituting u=(1+t)/(1-t) gives
log 2=2 integral_0^(1/3)1/(1-t^2) dt>2 integral_0^(1/3)(1+t^2)dt=56/81.
Consequently 1/4<Z(2)<25/81.
The legal letters {2,4,5,7,8} alone contribute 1/2+1/12+1/20+1/42+1/56=27/40 to Z(3), and more legal letters exist, so Z(3)>27/40.
The forbidden letters 3 and 6 contribute 1/6+1/30=1/5, with further forbidden letters, so Z(3)<4/5.
Therefore 2<81/40<Q_23<80/27<3. Its least positive physical time is strictly between log 2 and log 3, and cannot be log p for any prime p.
These statements apply to EVERY legal prefix, both cyclic source phases and ALL height phases of O_[(2,3)], not just its periodic points.
All its positive repetitions have time j log Q_23; none changes its primitive generator into the target by relabelling. No clock rescaling is permitted.
This is a decisive scoped target failure. The full formulas above already retain every other primitive cyclic word and all nonperiodic histories, without a census or deletion.

## 7. UNCONSTRAINED: full independent owner

Here ALL pairs are legal, X=A^N0, pi=alpha=1/[a(a-1)], and mu is the full product probability. Every I_a has domain ALL X.
Its own every-Borel IMAGE is j_a=alpha(a), locally constant at every point; invariance and absence of atoms follow from Section 2 (also each cylinder shrinks by at most 1/2 per letter).
For a word u define D(u)=product_(a in u)a(a-1), D(empty)=1. Its history IMAGE is 1/D(u), so c(ut,|u|-|v|,vt)=log[D(u)/D(v)].
Its FULL clock kernel is D(u)=D(v); its FULL lag kernel is |u|=|v|; their intersection imposes both, on all actual common-tail triples.
All incoming arrows, extensions and phases are precisely Sections 4–5 with this own source; no hard-admission branch or stationary weight is retained.
Every primitive cyclic word over A is allowed, including constants. On its whole eventual class the source isotropy is LZ, extension isotropy is {0}, H=log D(w) Z, and the physical packet has least time log D(w)>0.
Outside eventual periodicity source/extension isotropy and H are trivial, with the full real-line phase. Distinct cyclic words and colliding D products keep their multiplicity.
The complete multiplicity is #{primitive cyclic [w]:D(w)=exp(t)}; repetitions have time j log D(w), not a new primitive label.
For its entire (2,3) class, D=2*6=12, source isotropy is 2Z and H=log 12 Z; the periodic core has least T-period 2 and the whole class's least physical time exceeds log 3 exactly.
This control also contains the constant-3 primitive of time log 6. Neither packet nor clock is transferred to MAIN.

## 8. FINITE-TWO: atomic source cycles versus free physical time

The own source is exactly x=(2,3,2,3,...) and y=(3,2,3,2,...), each with mass 1/2. These are its two atoms and its entire support.
T swaps x and y. I_2 is defined only on {y}, I_3 only on {x}; no other letter or history is admitted.
Both inverse maps preserve their atom mass, so their every-Borel IMAGE is j=1 on the WHOLE domain. The inverse is the same swap and the probability is invariant.
Every finite legal history consequently has IMAGE 1; kappa=0 and c=0 at every retained arrow, with no null-version issue or borrowed infinite-source formula.
The actual triples satisfy range z=T^(-k)(source); their lags form the full Z action, not the two-point effective relation.
The FULL clock kernel is all G; the FULL lag kernel is exactly the units, so the intersection is the units.
At each point source isotropy is 2Z, extension isotropy remains 2Z, and H={0}. All even lags remain distinct zero-clock isotropy arrows.
All incoming arrows to z are (z,k,T^k z), k in Z; their extension heights equal the target height, for every real height.
The full source has one orbit; its extension orbit SET is R and physical height translation is free. All real phases remain.
The primitive SOURCE word is (2,3), with source repetitions 2j; there is NO least positive physical time, positive primitive physical packet or positive-time repetition.
In particular its zero cycle clock is not a stationary physical flow and is not the MAIN positive clock on the same written word.

## 9. GEOMETRIC-LAW: own probability, kernels and exact adverse packet

This owner uses all MAIN legal histories but alpha_G(a)=2^(1-a), its own Z_G,C_G,pi_G,P_G and the probability constructed in Section 2.
All denominators are positive finite, detailed balance and invariance hold for these OWN weights, full support holds, and every individual path is nonatomic.
Every I_a has the hard-admission domain, but its every-Borel all-point IMAGE is the OWN j_a(y)=alpha_G(a)/Z_G(y_0), not MAIN's value.
All finite-history products and full kernel tests of Sections 3–4 apply with Lambda_G=Z_G/alpha_G and Q_G; both kernels and their intersection use these weights separately.
If desired each Z_G is an exact finite expression: Z_G(a)=[sum_(1<=r<a,gcd(r,a)=1)2^(1-r)]/(1-2^(-a))-1, by grouping b by residue modulo a and removing the excluded b=1 term.
Every primitive cyclically allowed word has source isotropy LZ on its entire eventual class, trivial extension isotropy and H=tau_G(w)Z, with tau_G(w)=log Q_G(w)>0.
Non-eventually-periodic classes have trivial source/extension isotropy and H; all incoming arrows, phases, multiplicities and repetitions are the OWN instances of Sections 4–5.
For the entire (2,3) class, Z_G(2)=sum_(k>=1)4^(-k)=1/3, and Z_G(3)=1-sum_(k>=1)2^(1-3k)=1-2/7=5/7.
Since alpha_G(2)=1/2 and alpha_G(3)=1/4, Q_G(2,3)=(1/3)(5/7)/[(1/2)(1/4)]=40/21.
Thus 1<40/21<2: its periodic core has least T-period 2, every point of the full eventual class has source isotropy 2Z and ENTIRE H=log(40/21) Z, and least physical time lies strictly between 0 and log 2.
It is a genuine wrong-time primitive on every legal incoming prefix and both cyclic phases, with repetitions j log(40/21); it is not a measure adjustment offered to rescue MAIN.

## 10. Scoped decision and stopping boundary

The frozen full owners, all-point conditional IMAGE laws, actual lags, all kernels, isotropy and physical phases have been accounted for without discarding any state.
MAIN fails the declared positive primitive-time target on the precommitted ENTIRE (2,3) class; the controls separately show their own positive wrong times or zero-clock source-cycle behavior.
All-prime coverage and any analytic operator/trace were not established. No finite data, floating-point approximation, selected-representative carrier or external roof was used.
Strong naturalness remains OPEN; classical A0/A1/A2 NOT APPLICABLE; T3 NOT AUDITED; formal UNASSIGNED; B NOT INVOKED.
Disposition: STOP / FORK, no promotion of this nearest-neighbor boundary CONTROL and no claimed infinite-memory escape or universal no-go.
This fifth-round result does not authorize a sixth round. Root owns the final review/integration and subsequent user-confirmation boundary.

EOF — independent raw proof frozen; full owner and controls, exact wrong-time witness, internal NOT_CALIBRATED.
