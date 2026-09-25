# Divisor-permitted fractional returns: a fixed geometric clock and a wrong primitive

Candidate ANG-20260922-DFR01; paper385; version1; 2026-09-22.
Batch GEOMETRIC-RETURN-20260922-H, round1/5.
Outcome: `OWNED GEOMETRIC CLOCK; NONINTEGER PRIMITIVE — STOP / FORK`
Full source, measure and geometric-clock ownership established; target STOP.
Strong naturalness OPEN; T3 NOT AUDITED; classical A0/A1/A2 NOT APPLICABLE;
formal UNASSIGNED; Route B NOT INVOKED.

## Abstract

The complete divisor-permitted infinite-code carrier has no isolated points.
Its relative-metric branch derivative fixes the clock at every point,
including null periodic paths. Its own nonstationary Markov probability is
atomless and has the prescribed every-Borel IMAGE, a different cocycle.
The entire primitive ledger is classified by cyclic legal primitive words.
The prescribed 23 packet has least time 2log(4+sqrt15), whose exponential
is irrational, so the necessary prime-time target fails. Three controls
retain their own carriers, clocks, measures, inverse domains and packets.

## 1. Frozen carrier, actual topology and all boundaries

The [71-line card](candidate-card.md) fixes digits a>=2, all infinite words
Sigma satisfying a_(i+1) divides a_i+1, and F_a(y)=1/(a+y).
The lineage is divisor/composite admission -> legal symbolic words -> actual
nonlinear return branches, not a geometric lift or a claimed novel architecture.
On [0,1], each F_a maps into [1/(a+1),1/a] and is at most 1/4-Lipschitz.
Thus F_(a_0)...F_(a_(n-1))(0) converges, independently of the terminal
value in [0,1], defining pi(a). All tail values belong to (0,1/2):
their first digit gives a positive lower bound, and their next tail is positive.
Writing x=pi(a), the exact identities are
\[
 x=F_{a_0}(\pi(\sigma a)),\quad
 a_0=\lfloor1/x\rfloor,\quad T(x)=1/x-a_0=\pi(\sigma a). \tag{1}
\]
The open first-digit intervals (1/(a+1),1/a) are disjoint. Successively
recovering digits proves injectivity. Uniform contraction proves continuity;
local constancy of any finite recovered prefix proves continuity of the
inverse. Hence pi is a homeomorphism onto X with its relative Euclidean
topology. Its Borel structure is exactly the full symbolic one.

Every such x is irrational: for reduced rational x=p/q the next positive
remainder is (q-a_0p)/p with numerator strictly below p. Repetition would
give an infinite strictly decreasing sequence of positive numerators.
Thus rational finite expansions, 0 and branch endpoints are not points of
this frozen infinite-code carrier. No closed-interval completion is claimed.
This excludes no legal infinite word, periodic path or null path.

From any digit a there is a legal continuation, for instance a+1.
An odd a>=3 has two distinct successors 2 and a+1. From an even a every
successor divides an odd number and is odd. Therefore every finite legal
prefix admits a fork after at most one further transition. Extending both
choices gives different infinite words agreeing to arbitrarily large depth.
Their images approach the original point by contraction. X has no isolated
points, also within each open digit cylinder and each inverse domain below.

## 2. Every actual inverse and the intrinsic geometric clock

For every a>=2, let B_a be the union of cylinders with first digit b dividing
a+1. The actual inverse is I_a=F_a restricted to ALL B_a, with range X_a.
T I_a is the identity on B_a and I_a T is the identity on X_a by (1).
For a target with first digit b, ALL predecessors have indices
a>=2 with a congruent to -1 modulo b; each is retained.
These domains, not all of X, are the correct domains for the restricted map.

If x' approaches x within X, it eventually has the same first digit. Then
\[
 \frac{T(x')-T(x)}{x'-x}=-\frac1{xx'}\longrightarrow-\frac1{x^2}.
                                                               \tag{2}
\]
The nonisolation just proved makes this an intrinsic relative-metric limit
with uniquely determined value, not an arbitrary ambient extension derivative.
The same argument on B_a gives I_a'(y)=-1/(a+y)^2. Therefore
\[
 \tau(x)=\log|T'(x)|=-2\log x>2\log2.                    \tag{3}
\]
Every point, including every null periodic point, has this fixed value.
No measurable-version choice is left in this geometric definition.
The lower bound makes accumulated forward step-time diverge along every path;
it is not a classical symplectic or invertible mapping-torus construction.

## 3. Own Markov probability, atom status and every-Borel IMAGE

Let eta_a=2^(1-a), Z_a=sum_(b>=2,b|a+1)2^(-b), and P(a,b)=2^(-b)/Z_a
on legal edges. Sum_a eta_a=1, and every Z_a is finite and positive.
The consistent probabilities eta_(a_0)product_(i<n)P(a_i,a_(i+1))
construct the full path law and its pushforward mu on X. Every nonempty
legal cylinder has positive measure, so mu has full support.

It is atomless, not just generically non-atomic. At an odd digit a, 2 is
allowed; any chosen successor b!=2 has probability at most
2^(-b)/(1/4+2^(-b))<=1/3. If 2 is chosen, the next digit is forced to
be 3; the two probabilities from 3 are 4/5 and 1/5. An even initial digit
first leads to an odd one. Consequently every four-transition block along
ANY legal path has probability product at most 4/5. Cylinder masses are
bounded by eta_(a_0)(4/5)^floor(n/4), tending to zero at every point.

This mu is not stationary. A predecessor of digit 2 must be odd, so
mu(T^(-1)X_2)<=sum_(a odd>=3)eta_a=1/3<eta_2=1/2.
For every Borel E subset B_a, conditional cylinder factorization and
uniqueness of finite measures give
\[
 \mu(I_aE)=\int_E j_a(y)\,d\mu(y),\qquad
 j_a(y)=\frac{\eta_aP(a,b)}{\eta_b}=\frac{2^{-a}}{Z_a}>0,
                                                               \tag{4}
\]
where b is the first digit of y. The final value is constant on the entire
actual domain, finite and fixed at EVERY point; all null tails remain.
For every finite legal prefix u, on its complete legal tail domain,
the IMAGE is J(u)=product_(a in u)j_a. Replacing v by u over any Borel
subset of their common tail domain has IMAGE J(u)/J(v).
This proves the entire measured transport, not an assumed invariant law.

IMAGE IS NOT THE GEOMETRIC CLOCK: Z_2=1/8, so j_2=2 and -log j_2=-log2,
while tau(I_2 y)=2log(2+y)>0. No identification of these cocycles is made.

## 4. Full geometric cocycle, Borel extension and kernels

For a finite prefix u=(a_0,...,a_(m-1)), including the empty prefix, put
\[
 M_a=\begin{pmatrix}0&1\\1&a\end{pmatrix},\quad
 M_u=M_{a_0}\cdots M_{a_{m-1}}
     =\begin{pmatrix}A_u&B_u\\C_u&D_u\end{pmatrix}.
\]
An empty product is the identity. Multiplication and differentiation give,
on the entire actual tail domain,
\[
 I_u(t)=\frac{A_ut+B_u}{C_ut+D_u},\quad
 |I_u'(t)|=(C_ut+D_u)^{-2},\quad
 A_m(I_ut)=2\log(C_ut+D_u),                             \tag{5}
\]
where A_m(x)=sum_(i<m)tau(T^i x); the scalar A_m is not a matrix entry.
Use exactly G={(z,m-n,w):T^m z=T^n w}, m,n>=0, with source w, range z,
retained lag ell=m-n, and equal triples identified. For common tail t,
z=I_ut and w=I_vt, its geometric cocycle is
\[
 c=A_m(z)-A_n(w)=2\log\frac{C_ut+D_u}{C_vt+D_v}.          \tag{6}
\]
Different presentations append equally many common-tail edges, whose sums
cancel. Aligning tails proves addition; inversion changes the sign.
Its exponential exp(-c) is the actual metric derivative magnitude of
prefix replacement, not the probability IMAGE in (4).
Countably many Borel prefix charts make c Borel. Thus all arrows
(w,h)->(z,h+c(z,k,w)) define the full Borel extension on X times R.

There is a particularly explicit FULL clock kernel. If c=0, irrationality
of t and the integer coefficients force C_u=C_v and D_u=D_v.
For a nonempty u, C_u>0 and
D_u/C_u=[a_(m-1);a_(m-2),...,a_0]. The last digit of this finite
continued fraction is at least 2: recover its successive digits by floor
and reciprocal, stopping at an integer. This uniquely recovers u.
The empty word has C=0 and cannot coincide with a nonempty word.
Hence u=v, z=w and m=n: ker c consists EXACTLY of units.
The full lag kernel is {(z,0,w):T^Nz=T^Nw for some N>=0};
its intersection with ker c is units. No incoming history is omitted.

## 5. Entire isotropy, primitive packets and phases

Via pi, a nonzero source isotropy arrow is precisely equality of two shifted
infinite words. Thus an eventually periodic word with least tail period q
has ENTIRE source isotropy qZ; every other word has trivial isotropy.
The periodic core is a finite legal cyclic word w, not a proper power,
modulo cyclic rotation. Every periodic tail gives one, and two such primitive
words have equal tails after finite shifts iff they are cyclic rotations.
Conversely repeating any legal cyclic word gives a point of X; injectivity
makes its least source period the length of its primitive word.
This exhausts the ledger without selecting a recurrent core or a finite census.

At its periodic point x_w, M_w(x_w,1)^t=lambda_w(x_w,1)^t, with
lambda_w=C_w x_w+D_w>1. Therefore the entire return data are
\[
 L(w)=2\log\lambda_w,\quad H_x=c(G_x^x)=L(w)\mathbb Z,
 \quad c(x,kq,x)=kL(w)                                 \tag{7}
\]
for EVERY eventually periodic incoming x with this core; its finite transient
part cancels. Otherwise H_x={0}. Extension isotropy is trivial everywhere.
Retain all O_x={u T^n x:u any finite legal incoming prefix, n>=0}.
Here u T^n x denotes I_u(T^n x), always on its full actual legal domain.
For a reference a in O_x and any arrow g:y->a, the phase of (y,h) is
h+c(g) modulo H_a. Choices differ by isotropy; conversely equal phases
give an actual arrow after an isotropy correction. The quotient over O_x is
exactly R/H_x. Height translation is a complete R-action on the orbit SET.
No Hausdorff, smooth or measure-preserving quotient is asserted.
There is ONE physical packet per primitive cyclic word, least time L(w),
all phases R/L(w)Z and repeats kL(w), k>=1. Source phases are not extra
packets. Aperiodic source classes instead have phase line R and no returns.

The determinant of M_w is epsilon=(-1)^q and its trace t_w is a positive
integer. Since C_w>0 and x_w is irrational, lambda_w is irrational.
Its characteristic equation gives lambda_w^2=t_w lambda_w-epsilon,
also irrational. Thus EVERY geometric primitive in this frozen fractional
family has a noninteger exponential, not an ordinary prime. This conclusion
does not extend to arbitrary fractional-linear families or metric clocks.

## 6. The precommitted MAIN discriminator

The word 23 is legal cyclically: 3 divides 2+1 and 2 divides 3+1.
Its two digits differ, so its least source period is 2. Directly,
\[
 M_{23}=\begin{pmatrix}1&3\\2&7\end{pmatrix},\quad
 \lambda=4+\sqrt{15},\quad
 H=2\log(4+\sqrt{15})\,\mathbb Z.                       \tag{8}
\]
The least positive time is L=log(31+8sqrt15), not log p for any integer p.
This is the ENTIRE H, not a chosen return or an inferred repetition.
All incoming uT^n x have phase h+A_n(x)-A_(|u|)(uT^n x) modulo L.
Both source phases and every real height remain. The necessary target stops;
there is no need to enumerate further cycles or test prime coverage.

## 7. Three own controls

For each control o, use its actual G_o={(z,m-n,w):T_o^mz=T_o^nw},
on its own X_o, and the full height extension with its own geometric c_o.
For D and C, the contraction, irrationality, coding, intrinsic derivative,
matrix and packet proofs above apply to their OWN legal word sets.
Both sets branch at every digit, so the nonisolation proof is immediate.
Their actual finite-prefix domains are rebuilt from their own adjacency.
In each control every eventually periodic core has source qZ, geometric
H=LZ and trivial extension isotropy; every other source has H={0}.
The full orbit and phase construction of Section 5 retains every legal
incoming prefix and height. No probability or clock is imported after changing owner.

**D, no arithmetic gate.** All words on a>=2 are retained; B_a=X_D for all a.
The own law is iid eta, P(a,b)=eta_b. Cylinder products prove full support,
atomlessness (every digit probability <=1/2) and stationarity.
Every-Borel IMAGE is j_a=eta_a on every point of X_D, and finite histories
have product density. The geometric clock remains -2log x, not -log eta_a.
All predecessor digits are allowed. The exact clock kernel is units;
the lag kernel and its intersection are as in Section 4 on this source.
The primitive word 2 has q=1, lambda=1+sqrt2 and ENTIRE
H=log(3+2sqrt2) Z, an irrational-multiplier primitive, with its full phase circle.

**C, coprime gate.** The own legal edges satisfy gcd(a,b)=1, with
Z_a^C=sum_(b>=2,gcd(a,b)=1)2^(-b), P^C(a,b)=2^(-b)/Z_a^C and initial eta.
Every Z_a^C>0, and cylinders give a probability with full support.
For odd a a successor other than 2 has probability <=1/3; if 2 occurs,
the next transition has maximal probability P^C(2,3)=3/4.
An even digit first leads to an odd digit. Thus every three-transition
product is <=3/4, proving atomlessness on ALL paths.
Only odd digits can precede 2, so its incoming mass is <=1/3<eta_2:
this law is not stationary. Its exact B_a^C consists of tails whose first
digit b has gcd(a,b)=1; EVERY such inverse index is retained.
Every-Borel j_a=2^(-a)/Z_a^C follows from its own cylinder law.
The full geometric clock kernel is units, with the full lag/intersection
kernels and incoming phases as above. The legal primitive word 25 has
q=2, M_25=[[1,5],[2,11]], lambda=6+sqrt35, and ENTIRE
H=log(71+12sqrt35) Z: its least positive time is again not a log-prime.

**L, actual affine branches.** Keep MAIN words and its symbolic Markov law,
but construct pi_L from L_a(y)=1/a-y/[a(a+1)] on [0,1].
Contraction is at most 1/6; disjoint open digit intervals recover every digit.
This independently gives a homeomorphism onto X_L, with no isolated points.
The actual inverses are L_a restricted to the full divisor-permitted
tail domains. The forward branch is T_L(x)=a+1-a(a+1)x.
Its intrinsic derivative is -a(a+1); tau_L=log[a(a+1)]>=log6.
The own pushforward probability has full support, is atomless and
nonstationary by the SAME symbolic estimates, not by MAIN's geometry.
Every-Borel j_a=2^(-a)/Z_a and product-history IMAGE follow anew under pi_L.
For a prefix u put Q(u)=product_(a in u)a(a+1). Then
c_L=log[Q(u)/Q(v)]; its FULL clock kernel is Q(u)=Q(v) on actual common
tails. Its lag kernel has equal prefix lengths; the intersection requires
both conditions. Common-tail cancellation and Borel prefix charts prove
descent/additivity and the full extension for this own product formula.
A primitive word has ENTIRE H=log Q(w) Z, source qZ,
trivial extension isotropy and all phases/incoming histories of Section 5.
Aperiodic sources have H={0}. Every nonempty Q(w) is composite.
For 23, the two coded coordinates are 32/71 and 21/71, since
L_2 L_3(x)=4/9+x/72. Its least source period is 2 and ENTIRE H=(log72)Z.
These rational INFINITE-code points are retained. They are not discarded
by MAIN's rational-boundary argument, which does not apply to this owner.
Endpoint/completion points outside pi_L(Sigma) are still not added.

## 8. Scope, decision and reproducibility

The same-object ledger is intact: arithmetic admission, full coding, own
measure, actual inverses and geometric clock belong to one frozen carrier.
T0/geometric-clock ownership is established. Equation (8) fails the necessary
target; no sufficiency, prime-coverage or multiplicity pass is asserted.
Strong naturalness OPEN: both gate and coordinate family are design inputs.
T3 NOT AUDITED; classical A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED;
B NOT INVOKED. No probability-version repair, rescaling or packet deletion.

Exact proofs, not scientific numerics or higher-cycle scans, support this
record. Inputs: [card](candidate-card.md); scope: [ledger](claim-ledger.md);
navigation: [README](README.md). The author supplied the definition scout
and shares earlier authorship/history; no evidence/raw/peer or other new main
was read. ARS writing discipline leaves review root-owned; internal scrutiny
is NOT_CALIBRATED, not external peer review or novelty certification.
Data: definitions and proofs here. AI: definition, derivation and drafting.
Human subjects: N/A; human CRediT, funding and conflicts were not supplied.

EOF — complete geometric-return owner; scoped STOP / FORK.
