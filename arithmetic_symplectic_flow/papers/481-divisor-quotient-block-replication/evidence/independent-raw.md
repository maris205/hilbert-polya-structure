# DQR01 — independent card-only raw derivation

## Authority, input and exposure

ANG-20260925-DQR01; Paper481; batch AA round2/5; exact analytic short-gate audit.
Sole scientific input: candidate-card.md version1.1, FULL read1–96 through EOF.
96-line SHA25618404bee3127748731a39fa6b54c0ccd69ccaa3ae28bdff1db97e2901cee234e.
Original86-line prefix SHA256671ebc1e5ec7b91cc9f44d012dc58ae33f980d0410977b88cbf5aab1a5c52491.
Immutable CP1: scope-review.md,85lines, SHA256d4c8a85eeb2a89e179060654f268f0641d64a6bd89c0841659908cb5cc257b44.
Distinct RAW RELEASE followed root's full CP1 read; author manuscripts remain locked.
No author/peer/helper body, old proof or other current scientific file was read.
Retained same-model history, including475, is exposure, not proof input or blind review.
NOT_CALIBRATED; internal analytic work, not independent-error, human or external validation.
Previously personally read ARS/local instructions remain operative; no quota or numerical score.
Only this raw file was written; no helper, science code/numerics, network, Git, PDF or485 work.

## 1. Original probabilities and complete branch owners

Write e(a)=2^(-a), b>=1, and D(a,b) iff 1<a<b and a divides b.
The geometric sum of e(a) is1. For a=1, Z_1=1; for a>=2,
Z_a=1+sum_(j>=2)2^(-ja)=1+1/[2^a(2^a-1)].
Thus the declared positive transition probabilities P_ab sum to1.
The initial law e and these transitions give consistent finite-dimensional laws and hence mu.
Every cylinder has positive mass. P_a1<=1/2; for b>=2, P_ab<=2*2^(-b)<=1/2.
Consequently every length-r cylinder has mass at most2^(-r), so every singleton has mass0.
The iid law used by I/A has the same full support and singleton bound.
No stationarity, survivor conditioning or change of reference measure is used.
All X=N_(>=1)^N0 remains the source of each separately owned partial map.

For M/I, index every branch by d,q>=2 and B=(b_1,...,b_q):
U=(d,dq,B), V=(q,B^d). Its source is the entire cylinder[U], its image[V].
For R the same source parser has V=(q,B). For A take every d,n>=1 and |B|=n,
U=(d,n,B), V=(n,B^d). No letters or A unit cases are discarded.
The first pair and the prescribed block length uniquely determine the branch of each legal source.
Hence these source cylinders partition the legal domain; the maps are continuous on each piece
and globally Borel on their actual domains. Every piece is a prefix-replacement homeomorphism.
Illegal first pairs for M/I/R are terminal units, never absorbing dynamical fixed points.
A is total and retains its different parser and iid law; it is not a single-factor control.

For a target y, all one-step incoming points are given by the following exact rules.
M/I: let q=y_0. If q<2 there are none. Otherwise B=(y_1,...,y_q), and for every d>=2
for which y=(q,B^d,xi), include (d,dq,B,xi).
R: if q=y_0>=2, for every d>=2 include (d,dq,y_1,y_2,...); otherwise none.
A: let n=y_0 and B=(y_1,...,y_n); for every d>=1 for which y=(n,B^d,xi),
include (d,n,B,xi). In particular d=1 is always a valid incoming choice for A.
These enumerate every branch label and every overlapping output cylinder, not a selected inverse.
In each case I_U(V xi)=U xi has exact domain[V], T I_U=id and I_U T=id on[U].
Conversely the unique actual source parser recovers one of these labels from every predecessor.
No outgoing legality test on y is required; terminals can have incoming points.

## 2. Every-Borel Markov IMAGE, all-point version and actual signs

For t>=1 let nu_t be the Markov probability on tails beginning with t with transitions P.
For every Borel tail set E_t subset[t] and every nonempty finite W,
mu(W E_t)=F_mu(W,t)nu_t(E_t),
where F_mu(W,t)=e(W_0) product_(i<|W|-1)P_(W_i,W_(i+1)) P_(W_last,t).
This follows first for cylinders from the original law, then for all Borel sets by uniqueness
of finite measures. It keeps the initial law and the last-prefix/first-tail factor explicitly.
For any Borel E subset[V], pull E back to its tail set and partition by t=xi_0.
On each piece the preceding identity for U and V gives
mu(I_U E)=integral_E F_mu(U,xi_0)/F_mu(V,xi_0) dmu.
Summing the countable partition proves the asserted IMAGE for every Borel E.
The iid proof uses e(W)=product_(w in W)e(w), with ratio e(U)/e(V).
These positive finite ratios are the owner's prescribed values at EVERY point, including
all null tails; their pointwise uniqueness is not being inferred from an a.e. theorem.

Here U and V have the same last symbol, so their boundary P_(last,t) cancels after, not before,
the Markov identity is established. The resulting explicit branch values are useful for signs.
Put C(B)=(product_(i<q)P_(b_i,b_(i+1)))P_(b_q,b_1) and
A(d,q,b_1)=e(d)P_(d,dq)P_(dq,b_1)/[e(q)P_(q,b_1)]. Then
J_M=A(d,q,b_1)C(B)^(1-d), and J_R=A(d,q,b_1).
For I, J_I=2^[(d-1)sum B+q-d-dq]; for A, J_A=2^[(d-1)sum B-d].
In every case kappa(z)=-log J_U(Tz) for the uniquely parsed source branch.
No positivity or zero exclusion is imposed on this signed clock.

## 3. All depths, actual groupoid and exact kernels

Let P_U(y) be the complete one-step incoming set of section1, P_U^0(y)={y},
P_U^(r+1)(y)=union_(x in P_U^r(y))P_U(x). By adding/removing one actual legal step,
this is exactly every depth-(r+1) predecessor, for every finite r, with no cutoff.
All compatible infinite incoming histories are precisely chains y_0=y,
y_(j+1) in P_U(y_j) for all j>=0, with the repeated-block tests reapplied at every stage.
Equivalently they are coherent inverse-limit families of these finite histories.
Unbounded finite depths alone do not assert an infinite compatible branch.

Let D_r be the actual r-step domain, S_r(z)=sum_(i<r)kappa(T^i z), S_0=0.
The domains are Borel by iteration of the explicit partial Borel map.
Each finite itinerary can be restricted to countably many finite-prefix domains on which
the iterate is injective: intersect the finitely many parsed branch conditions, refining
the finite prefixes as needed. These cover every legal history and every null source.
The one-step every-Borel formulas compose on these domains by change of variables.
An inverse r-history ending at y=T^r z therefore has IMAGE exp(-S_r(z)).

G={(z,r-s,w):z in D_r,w in D_s,T^r z=T^s w}; equal triples only, source w, range z.
Composition adds lag and inversion negates it. Legal histories at the common middle source
can be aligned to the larger middle depth, proving closure without free-word arrows.
Two witnesses of the same triple extend by the same number of steps on their common tail;
the appended clocks cancel. Thus c=S_r(z)-S_s(w) descends and is additive.
Countably many Borel witness relations also make the actual groupoid and cocycle Borel.
The forward arrow(Tz,-1,z) has c=-kappa(z).
On every common-tail pair of injective histories, IMAGE is
exp(-S_r(z))/exp(-S_s(w))=exp(-c), for every Borel subset of the branch domain.
Alternative witnesses give the same value because c descends, including at null points.

Subject throughout to actual legal meetings, the full kernels are
ker(lag)={(z,0,w):T^r z=T^r w for some r};
ker(c)={(z,r-s,w):S_r(z)=S_s(w)};
ker(lag,c)={(z,0,w):T^r z=T^r w and S_r(z)=S_r(w) for some r}.
These are subgroupoids including non-loop arrows, not assertions that all kernels are units.
The height extension retains all X times R and sends(w,h) to(z,h+c).
Additivity makes it an action; height translation commutes with it and descends to the orbit SET.
No smooth/Hausdorff quotient, stationary flow measure or positive roof is presumed.

## 4. Entire H, zero isotropy, packets and phases for every actual core

A nonzero-lag loop at z is equality of two different legal iterates of that same z.
The intervening segment repeats legally, so z is actually eventually periodic for T.
Conversely every actual eventual least-ell core has source isotropy ell Z at every incoming point.
Let f_i=T^i f_0,0<=i<ell, C_i=S_i(f_0), and C=C_ell, with no sign restriction.
Every loop has lag j ell and c=jC: move any meeting into the core, cancel both transient
histories, then use its least source period. Every integer j is realized, not just a subgroup.
Thus source isotropy is ell Z, its entire clock image H=C Z, and extension isotropy is
ell Z if C=0 and trivial if C!=0. Non-eventual sources have trivial source/extension isotropy.
Clock-zero arrows between different sources remain in the kernels whether or not loops vanish.

The exact source class of any y is union_(s>=0,y in D_s) union_(r>=0) P_U^r(T^s y).
For a core its whole incoming component is B(f_0)=union_(r>=0,i<ell)P_U^r(f_i).
These equalities follow in both directions from the actual common-tail witnesses.
Choose z in that basin with first core arrival tau_z and arrival index epsilon_z.
Put d_z=tau_z-epsilon_z, B_z=S_(tau_z)(z)-C_(epsilon_z).
All arrows from w to z, without omissions, have lag d_z-d_w+j ell and
c=B_z-B_w+jC, j in Z. Arbitrarily late common core meetings realize every j.
Hence the complete phase is h-B_z modulo C Z.
If C!=0 the physical orbit is R/(|C|Z), with least positive primitive |C| and repetitions
m|C|,m>=1; the signed source-loop clock remains C, not forcibly +|C|.
If C=0 all phases are real and there is no positive physical return, despite source loops.
Indeed any equality[z,h+t]=[z,h] is a source loop at z; this proves the ENTIRE stabilizer H.

A terminal-ending class has a unique common terminal, with the depth and S differences
giving its sole arrow between each pair. Non-eventual infinite classes use the exact cofinality
test above; they too have one arrow per connected ordered pair and real phase h minus its clock.
No global selector is asserted. Equal-time different core components are never merged.
These conclusions classify H conditionally for every actual core, not by a higher-period census.

## 5. Complete global fixed sets: all words and all tails

For M/I, equality(d,dq,B,xi)=(q,B^d,xi) first forces d=q=m>=2.
Write s=m^2. After the first letter, (s,B,xi)=(B^m,xi), with |B|=m.
Comparing the first m symbols forces b_1=s and b_(i+1)=b_i, so B=s^m.
The remaining equation is xi=s^(m^2-m-1)xi. Since m^2-m-1>=1,
it forces xi=s^infinity. Conversely that word satisfies the actual branch identity.
For R, the first-letter comparison again gives d=q=m. Writing Y=B xi, the rest is
sY=Y, so Y=s^infinity, with no other tails possible.
Consequently Fix(M)=Fix(I)=Fix(R)={f_m=(m,(m^2)^infinity):m>=2}.

For A the first letter forces d=n=m>=1 and the residual equation is(m,B,xi)=(B^m,xi).
When m>=2 the same prefix comparison forces B=m^m and xi=m^infinity.
When m=1, B=(b), and (1,b,xi)=(b,xi) forces b=1 and xi=1^infinity.
Thus Fix(A)={g_m=m^infinity:m>=1}, with all unit cases included.
These comparisons began with arbitrary B and xi; constant tails are conclusions, not test inputs.
No illegal terminal is included in these dynamical fixed sets.

## 6. Signed fixed clocks, complete incoming and multiplicity

For s>=2 put b_s=1/P_ss=2^s Z_s. With t=2^s,
b_s=(t^2-t+1)/(t-1), whose numerator and denominator are coprime.
At f_m write s=m^2 and h_m=m^2-m-1. The source prefix is(m,s^(m+1));
the M/I output is(m,s^(m^2)), while the R output is(m,s^m).
For the Markov prefixes the shared e(m)P_(m,s) and boundary factors give exactly
J_M(f_m)=P_ss^(-h_m)=b_s^h_m, J_R(f_m)=P_ss=b_s^(-1).
The iid formula gives J_I(f_m)=2^(s h_m).
Thus kappa_M(f_m)=-h_m log b_s, kappa_I(f_m)=-s h_m log2,
kappa_R(f_m)=log b_s. At g_m, J_A=2^(m h_m), kappa_A=-m h_m log2,
where h_1=-1, so g_1 has kappa=+log2 and every m>=2 has negative kappa.
Every fixed clock here is nonzero. Each fixed component has source isotropy Z,
trivial extension isotropy and entire H=kappa(f)Z, with positive primitive L_f=|kappa(f)|.
All repetitions and real phases follow section4 with ell=1; these signs are not rescaled away.

For every fixed f, its exact full basin is union_(r>=0)P_U^r(f), using section1's entire atlas.
It is countable and mu-null (or iid-null), but all its points and real phases are retained.
Different fixed f cannot meet, since their futures stay at different fixed sources.
Accordingly every such basin supplies exactly one full positive physical packet, not one per
predecessor, phase representative or written repetition. No fixed packet is omitted.
For a basin point define tau_z as first arrival at f and B_z=S_(tau_z)(z).
All arrows have lag tau_z-tau_w+j, c=B_z-B_w+j kappa(f), j in Z;
the exact lag/clock/joint kernels impose respectively the first/second/both equations being zero.
The complete phase is h-B_z modulo |kappa(f)|Z, including at every null incoming source.

More explicitly M/I have the full star basin
B_U(f_m)={x_d=(d,dm,(m^2)^infinity):d>=2}, with x_m=f_m.
Every d is an incoming label to f_m. If d!=m, an incoming branch to x_d would have block
length d and require its second symbol dm to reappear after d positions in the constant m^2 tail.
This forces dm=m^2, a contradiction. Thus each off-core x_d has no incoming and enters f_m
in one step. All compatible infinite incoming chains ending at f_m remain constantly f_m;
arbitrarily many self-steps followed by an off-core leaf give finite histories only.
Such leaves still have source isotropy Z through their forward core, not through fake predecessors.

For R, all depth-r predecessors of f_m, r>=1, are precisely
(d_r,d_r d_(r-1),...,d_2 d_1,d_1 m,(m^2)^infinity), each d_i>=2;
for r=1 this means(d_1,d_1 m,(m^2)^infinity), and r=0 is f_m.
Every infinite choice d_1,d_2,... supplies a compatible incoming chain; this follows from the
exact R inverse, not compactness. Repeated core visits can give duplicate finite representations.
For A the exact all-depth basin and infinite-history test remain the unrestricted recursion
with y=(n,B^d,xi) at each node. This is an explicit equality test for every d>=1 and every depth,
not the unproved assertion that every eventually-m word reaches g_m.
Its first incoming layer is{(d,m^infinity):d>=1}; deeper layers use the entire repetition test.
Since d=1 always supplies predecessor1y, every A target has compatible infinite incoming chains.

The positive fixed lengths are respectively h_m log b_(m^2), m^2 h_m log2,
log b_(m^2), and |m h_m|log2 for M/I/R/A.
Within each owner they are strictly increasing in m: h_m increases for m>=2,
and b_s increases because (v+1/(v-1))-(u+1/(u-1))
=(v-u)[1-1/((u-1)(v-1))]>0 for v>u>=4.
For A, m=1 gives log2, m=2 gives2log2, and m h_m increases thereafter.
There are therefore countably many distinct fixed-core packets, one per listed m, with no
fixed-to-fixed equal-time collision within an owner. No comparison with higher cycles is claimed.

## 7. Precommitted gate and exact stopping boundary

For M, s=m^2>=4 and h_m>=1. The reduced rational b_s has denominator2^s-1>1,
so exp(L_f)=b_s^h_m remains a noninteger rational, never an ordinary integer prime.
Every listed MAIN fixed core is an actual positive nonprime primitive: the positive ledger is
nonempty and prime-only purity is refuted. This is a witness family, not just an empty prime window.
R fixed multipliers b_s are likewise noninteger. I fixed multipliers2^(m^2 h_m) are composite.
A has one prime-valued fixed packet at g_1 with multiplier2; all m>=2 fixed multipliers
2^(m h_m) are composite. This uniqueness is within the fixed subledger, not a global claim
excluding possible higher-period prime packets. Controls do not repair the MAIN failure.
Signed kappa, positive physical primitive and source-period repetition remain different notions.
The frozen combined arithmetic target fails by a MAIN nonprime primitive, so STOP/FORK.
No higher-period window, density/parser change, selected subsystem or parameter tuning is used.
The clock depends on the declared original law; stronger naturalness is not established.
This refutes this owner, not all divisor replication mechanisms. T1 NOT PASSED; T3 NOT AUDITED;
classical NOT APPLICABLE; formal coordinates UNASSIGNED; Route B NOT INVOKED.
EOF — card-only raw complete; full self-read/freeze followed by HOLD for distinct PAPER UNLOCK.
