# Card-only raw derivation — Logarithmic monomial owner bridge

Candidate: `ANG-AUDIT-20260923-LMB01`; paper 433; date: 2026-09-23.
Batch: `GLOBAL-GATE-FEEDBACK-20260923-Q`, round 4/5 (430–434).
Reviewer: `/root/nonlocal_source_review`.
Root separately released mathematics after reporting full reading of CP1.
Input: the full frozen 85-line card, personally reread through EOF.
candidate-card.md SHA256 7a144234a0f1502c403b0e1e1ee2d8ab28a02fd2eed382ffbbed5267b9bd00cd
scope-review.md — 125 lines — SHA256 c5daef2d982a0a4999112450ac743530af44d339a274864a7d17ed40c15c26b3
No 433 author surface, author/helper answer, peer proof, sibling output or
scout card was read. Older shared history remains; this is not a blind seat.
AI-assisted inherited-model internal review, NOT_CALIBRATED; served identity
not independently attested. No external/human/cross-model verification claim.
Exact mathematical work only: no scientific code, numerical census, external
literature/network, Git, PDF, operator, model change or publication operation.

## 1. Entire positive-cone inverse and its own Lebesgue IMAGE

Use T for the original partial owner and F for its log-coordinate map, to
avoid confusion with the control named U. Put alpha_i=log a_i,
M_i=abs(det A_i)>0, L_i=log M_i, s(u)=sum_r u_r and phi(x)=s(log x).
Every original x has strictly positive finite coordinates; zero axes and
infinity are NOT objects of this frozen carrier, and none are added below.
The full germ f_i is exp o (u->A_i u+alpha_i) o log. Since A_i is invertible,
it is a real-analytic diffeomorphism of the ENTIRE positive cone onto itself,
with inverse theta_i(y)=exp(A_i^{-1}(log y-alpha_i)). Negative exponents
are harmless on this carrier. No extra positive root is created by a
nonunit integer determinant: this is not a torus covering or a complex power.

Restrict f_i to the actual Borel E_i. Its image W_i=f_i(E_i) is Borel under
the full homeomorphism; theta_i|W_i is its actual Borel inverse. For any
target y, the complete predecessor set is exactly

    I_T(y)={theta_i(y):theta_i(y) in E_i}.

An overlapping image retains each different actual predecessor. The disjoint
E_i assign each source one branch, so they do not create duplicate point
predecessors or additional integer-lag arrows. Thin/empty pieces cause no
exception: empty pieces contribute nothing, and nonempty thin pieces remain.

With rows indexing outputs as frozen, direct differentiation gives

    Df_i(x)=diag(f_i(x)) A_i diag(1/x),
    abs(det Df_i(x))=M_i exp(phi(f_i(x))-phi(x)),
    Dtheta_i(y)=diag(theta_i(y)) A_i^{-1} diag(1/y),
    J_i^X(y)=M_i^{-1} exp(phi(theta_i(y))-phi(y)).       (1)

All factors are finite and positive at every actual point, including assigned
cuts and null strata. Change of variables for the full analytic diffeomorphism,
restricted to EVERY Borel B subset W_i, proves

    dx(theta_i B)=integral_B J_i^X(y) dy.

This is the prescribed all-point inverse-germ version. It is not reconstructed
from an a.e. restriction of f_i on a thin piece. Its original own clock is

    kappa_X(x)=L_i+phi(Tx)-phi(x), x in E_i.           (2)

No kappa_X is assigned on X minus D. Terminals remain objects with identities
and legitimate inverse histories, not absorbing dynamics or zero-step roofs.
For each finite legal inverse word the actual restricted domain requires every
successive inverse to belong to its own E_i. Composition preserves injectivity;
successive Borel substitution proves the product IMAGE identity at all depths.

## 2. The TWO log-coordinate measures and their own IMAGE versions

The full log map ell:X->Y=R^d is a diffeomorphism. The actual log dynamics is
F(u)=A_i u+alpha_i on H_i=ell(E_i), with terminals on the complement.
Its inverse germ is eta_i(v)=A_i^{-1}(v-alpha_i), restricted to F(H_i).
All histories and actual predecessors correspond under ell, including terminals.

FIRST measured comparison: nu=ell_*dx. Substitution x=exp u gives

    dnu(u)=rho(u)du, rho(u)=exp(s(u)).

This is positive sigma-finite, not ordinary du. Its actual inverse IMAGE is

    J_i^nu(v)=M_i^{-1} rho(eta_i(v))/rho(v)
             =M_i^{-1} exp(s(eta_i(v))-s(v)).          (3)

Indeed integral_(eta_i B) rho(u)du equals
integral_B M_i^{-1}rho(eta_i(v))dv, which equals integral_B J_i^nu dnu
for EVERY Borel B in the actual inverse domain. No normalization is changed.
Equations (1),(3) give J_i^nu(ell y)=J_i^X(y), hence
kappa_nu(ell x)=kappa_X(x) at every legal point.

SECOND measured comparison: ordinary du, a separately selected measured owner.
The same affine inverse has constant Jacobian M_i^{-1}, so

    J_i^0(v)=M_i^{-1}, kappa_0(u)=L_i.               (4)

Affine change of variables proves its EVERY-Borel identity on each actual
domain. Pulling this measure back by ell would give multiplicative Haar,
exp(-phi(x))dx, NOT the original dx; we never substitute that measure for dx.
All three measured owners have prescribed finite positive all-point versions.
The weighted version (3) is not merely abs(det Deta_i); its density ratio is
essential. This remains true on assigned cuts and periodic null strata.

## 3. All-arrow clock bridge and the height-map sign

For a legal m-step history define
K_m(x)=sum_(j=0)^(m-1) L_(i(T^j x)), with K_0=0. It is S_m^0(ell x).
Telescoping (2) proves at EVERY legal source

    S_m^X(x)=S_m^nu(ell x)=K_m(x)+phi(T^m x)-phi(x). (5)

The log map induces an exact lag-preserving groupoid isomorphism
g=(z,l,w) -> ell g=(ell z,l,ell w). It preserves actual witnesses in both
directions and does not rely on full D, surjectivity of T, or periodicity.
For a common-tail witness T^m z=T^n w the terminal potentials cancel, giving

    c_X(g)=c_nu(ell g)
          =c_0(ell g)+phi(w)-phi(z).                 (6)

This is an ALL-arrow statement, including inverse, nonzero-lag, zero-lag,
terminal-connected and non-eventual arrows. The clocks in different measures
are not called identical: only X and its ACTUAL pushforward have equal clocks.
On the original-to-nu height extension the map is (x,h)->(ell x,h).
For the separately measured du extension the correct height map is

    Xi(x,h)=(ell x,h+phi(x)).                       (7)

Check the sign directly: an original arrow (w,h)->(z,h+c_X) is sent to
heights h+phi(w) and h+c_X+phi(z); their difference equals c_0 by (6).
The inverse height change subtracts phi. Both maps commute with translation
by the SAME physical t; there is no rescaling, averaging or new roof.

Under the base-groupoid identification, lag kernels coincide, but

    K_c^X=K_c^nu={g:c_0(g)=phi(z)-phi(w)},
    K_c^0={g:c_0(g)=0};
    K_joint^X=K_lag intersect K_c^X,
    K_joint^0=K_lag intersect K_c^0.                 (8)

The original and weighted kernels here are identified by ell. These formulas
allow different full clock/joint kernels. For a SOURCE LOOP z=w, endpoint
terms cancel, so entire H, source isotropy and extension isotropy agree
between all three owners. The height isomorphism does not preserve the
zero-height section, explaining why it need not preserve the base clock kernel.

## 4. Full partial groupoids, incoming, isotropy and phases

For each own map use all actual legal triples (z,m-n,w), equal triples
identified, with c=S_m(z)-S_n(w). Two witnesses with equal lag differ by
adding the same number to both indices; the extra legal tail has equal
initial point and cancels. This proves descent. To compose, align the two
middle prefixes at their larger depth, using the continuation already given
by the longer prefix. No terminal is extended without such a legal history.
The same cancellation proves additivity; inverse clocks negate and forward
arrows (Tz,-1,z) have -kappa(z). All quantities are Borel by countable branch
and legal-witness conditions; choosing the first witness yields the same c.

For each owner the complete global kernels are

    K_lag={(z,0,w):T^m z=T^m w for some legal m};
    K_c={(z,m-n,w):T^m z=T^n w, S_m(z)=S_n(w)};
    K_joint=K_lag intersect K_c.                    (9)

The inverse formula of Section 1, iterated on its actual domains, gives ALL
legal predecessors I_T^m(y). The full source component of w is exactly
union_(n:T^n w exists) union_(m>=0) I_T^m(T^n w). Its log image is the
identical component for both F measures. This is an exact mathematical
description, not a finite or effective enumeration for arbitrary Borel pieces.

A nonzero source-isotropy lag is equivalent to eventual periodicity, since
it asserts two unequal legal iterates of one point agree. If the eventual
least cycle length is r, source isotropy is r Z, and its clock values are nC,
where C is the own forward sum over that cycle. Incoming prefixes cancel.
For the three measured owners, (5) gives the SAME

    C=sum_(j=0)^(r-1) L_(i(T^j p)), ENTIRE H=C Z.  (10)

This neither supplies a cycle nor classifies prime products; it is the loop
consequence of the bridge. A non-eventual source, terminating or not, has
isotropy and H zero. Extension isotropy is r Z if C=0, trivial if C!=0,
and trivial on non-eventual components. All statements hold at every height.

On any source component choose a reference p and actual arrows g_z=(z,l_z,p).
Let b_z be their own clock. Every arrow w->z is g_z u g_w^{-1}; in the
eventual case all lags/clocks are l_z-l_w+n r and b_z-b_w+n C. In a
non-eventual component there is exactly one triple, with the two differences.
Setting lag, clock or both to zero gives every kernel element, including
nonunit coalescences. The complete height phase is [h-b_z] in R/H.
With du reference clocks b_z^0, an equivalent original/nu phase is

    [h+phi(z)-b_z^0] in R/H,                       (11)

up to the constant phi(p). This follows from (6),(7), not a borrowed clock.
For H=C Z with C!=0 there is one physical circle per source component, least
positive period abs(C), repeats n abs(C). For H=0 it is a free real line,
even when nontrivial zero-clock source isotropy remains. Equal H values do
not identify distinct components. No global Borel selector/manifold is asserted.
In a terminating component the reference can be its unique terminal t:
l_z is the terminal hitting depth, b_z its legal prefix sum, H=0 and phase
h-b_z. There is no invented kappa(t); the identity alone has S_0=0.

## 5. Global unimodular discriminator

If EVERY A_i is unimodular, M_i=1 and the du clock vanishes on EVERY legal
step and arrow. Equations (2),(6) then read

    kappa_X(x)=phi(Tx)-phi(x),
    c_X(z,l,w)=phi(w)-phi(z),
    ENTIRE H_z={0} for EVERY z in X.                (12)

The last assertion holds on all loops directly, whether cycles exist or not,
and also on terminals. No Markov property, graph realization or finite census
is required. The positive physical packet ledger is empty globally, so the
nonemptiness requirement fails for this subclass. Cyclic source dynamics
cannot repair it, and no outside point is discarded to obtain the result.
Nevertheless the original/weighted arrow clocks need NOT vanish. Their exact
clock kernel is equal-potential endpoints; the du clock kernel is the whole
groupoid. Joint kernels are respectively the equal-potential part of K_lag
and all K_lag. The source isotropy of every eventual r-cycle is still r Z,
and it ALL survives as extension isotropy. Physical phases in the original
and weighted owner are h+phi(z) in R on each component; in du they are h.
Thus zero H is not confused with zero clock, no cycles, or trivial kernels.
This is only the unimodular discriminator, not a stop for all nonunimodular
integer monomial owners and not the separate 434 classification problem.

## 6. Control U — full quarter-turn source dynamics with globally zero H

On the full positive quadrant U(x,y)=(y,1/x) is a global analytic bijection.
Its inverse on the full target is (X,Y)->(1/Y,X), with own Lebesgue IMAGE
J_U(X,Y)=Y^(-2); hence kappa_U(x,y)=-2 log x. Direct substitution/change of
variables proves this EVERY-Borel identity, including x=1 or y=1 strata.
In log coordinates write u=log x,v=log y, s=u+v. The map is
F_U(u,v)=(v,-u), determinant1. For nu=e^(u+v)du dv its inverse IMAGE is
exp(-2v) at target (u,v); for ordinary du dv it is1, with clock0.
These agree with Section 2 but were computed from this control's own inverse.

U^2(x,y)=(1/x,1/y), U^3(x,y)=(1/y,x), U^4=id on the FULL source.
In log coordinates F_U^2=-id. The origin (0,0), i.e. (1,1), is the only
fixed point; it is also the only point fixed by F_U^2. Every other point
therefore has least source period4. There are no nonperiodic, preperiodic
off-cycle or terminal points. Each incoming history is the unique U^(-m)
predecessor and stays on that complete one- or four-point cycle.

The FULL actual groupoid, written in log coordinates, is

    z=F_U^(-l)w, l in Z, c_X=c_nu=s(w)-s(z), c_0=0. (13)

This includes all repeated-lag arrows, not only four representatives. For
w=(u,v), the full original/nu clock kernel is given by this residue table:

| l mod4 | range z | c_X | clock-zero condition |
| --- | --- | --- | --- |
| 0 | (u,v) | 0 | all w |
| 1 | (-v,u) | 2v | v=0 |
| 2 | (-u,-v) | 2(u+v) | u+v=0 |
| 3 | (v,-u) | 2u | u=0 |

K_lag is the unit subgroupoid because U is bijective; K_joint is also units.
K_c includes nonunit arrows on the displayed strata and all cycle loops;
it is not the whole groupoid in the original or weighted owner. In the
ordinary-du owner K_c is the WHOLE groupoid, while K_lag and K_joint are units.
The log axes u=0,v=0 and the line u+v=0 are retained; they correspond to
x=1,y=1,xy=1 inside the positive source, not added zero-coordinate axes.

At (1,1) source isotropy and extension isotropy are Z; on every other source
they are 4Z. ENTIRE H=0 everywhere for all three measured owners. Each whole
source cycle gives a free physical line, phase h+u+v=h+log(xy) in original/nu,
and h in ordinary-du coordinates. There is NO positive primitive or positive
repetition, despite all the source cycles. Arbitrary forward sums are
S_m^X=s(F_U^m w)-s(w), with the four explicit iterates above; histories,
signed arrows and all height phases are therefore completely specified.
The necessary nonempty positive ledger FAILS. This external control verifies
the global unimodular boundary without making all original arrows zero.

## 7. Shared notation for the TWO fixed expansion/reflection controls only

For the remainder b denotes ONLY 2 (control E) or sqrt2 (control R), not a
parameter search or a newly admitted family. Put lambda=log b>0 and
V_b(x,y)=(1/x,y^b). Its actual full inverse is (X,Y)->(1/X,Y^(1/b)).
The derivative gives, directly for each own Lebesgue measure,

    J_b^X(X,Y)=b^(-1) X^(-2)Y^(1/b-1),
    kappa_b^X(x,y)=lambda-2 log x+(b-1)log y.       (14)

These analytic positive finite versions satisfy EVERY-Borel IMAGE by the
global change of variables; both controls are total bijections on the whole
positive quadrant. Real powers in R are single-valued analytic here. R is
not an integer-exponent-class member, even though the same calculus applies.
Their log maps are F_b(u,v)=(-u,bv). The nu inverse IMAGE at target (u,v) is
b^(-1)exp(-2u+(1/b-1)v); its clock equals (14) in log coordinates. The
ordinary-du inverse IMAGE is b^(-1), with its OWN constant clock lambda.

Every forward and inverse history is explicit:

    F_b^n(u,v)=((-1)^n u,b^n v), n in Z,
    V_b^(-m)(x,y)=(x^((-1)^m),y^(b^(-m))), m>=0,
    S_m^X=m lambda+((-1)^m-1)u+(b^m-1)v,
    S_m^0=m lambda.                               (15)

The FULL groupoid, including all integer lags, is

    z=F_b^(-l)w=((-1)^l u,b^(-l)v), l in Z,
    c_X=c_nu=l lambda+[1-(-1)^l]u+[1-b^(-l)]v,
    c_0=l lambda.                                 (16)

For example l=-1 gives -kappa_b^X at the forward arrow, checking the sign.
All lag and joint kernels are units, since the source map is invertible.
In ordinary-du measure the clock kernel is ALSO units, as lambda>0.
The original/nu clock kernel includes precisely the units plus ALL arrows
whose source log coordinates obey, for nonzero l,

    l even: v=-l lambda/(1-b^(-l));
    l odd: 2u+(1-b^(-l))v=-l lambda.               (17)

There is no division by a vanishing denominator here. Formula (17) covers
both signs of l and every source stratum, including v=0 and u=0 when they
satisfy it. Such nonunit clock-zero arrows are NOT source loops. For example,
l=1,w=(-lambda/2,0) gives z=(lambda/2,0), c_X=0 but c_0=lambda!=0.
It does not create a smaller element of a source isotropy clock group.

## 8. Complete periodic and nonperiodic classification for E and R

From (15), a positive source return requires v=0, since b^n!=1 for n>0.
When also u=0 there is one fixed core. When u!=0 there is exactly the
two-point core { (u,0),(-u,0) } of least source period2. These are ALL
periodic points. Invertibility gives no preperiodic off-core ancestors;
each core's complete incoming stays on the core, with the histories in (15).
In original coordinates the periodic locus is the entire y=1 line: the
fixed (1,1), and all distinct pairs {(e^a,1),(e^(-a),1)}, a>0.

At the fixed core, source isotropy Z has clock l lambda; ENTIRE H=lambda Z,
extension isotropy is trivial, phase h mod lambda, primitive lambda and
repetitions n lambda. This holds for original, nu and ordinary-du owners.
For a two-cycle choose a>0 and points z_j=((-1)^j a,0), j=0,1.
The forward original increments are lambda-2a and lambda+2a. They may be
signed or zero individually, but their complete cycle sum is 2lambda.
Source isotropy is 2Z and ENTIRE H=2lambda Z; extension isotropy is trivial.
All core arrows are the restrictions of (16), and their kernels exactly the
restrictions of (17) and the unit lag/joint kernels, not a selected arrow.
The full physical phases can be written

    original/nu: [h+(-1)^j a+j lambda] mod 2lambda;
    ordinary du: [h_0+j lambda] mod 2lambda.       (18)

They correspond under h_0=h+u+v. Every pair supplies ONE circle of primitive
2lambda and repetitions 2n lambda. The continuum of different a values
labels genuinely different source packets, never one packet per equal time.

Every remaining source has v!=0 and is non-eventual. The COMPLETE normalized
classification of its source orbit is

    O_(sigma,r,a)={z_n=((-1)^n a,sigma b^n r):n in Z},
    sigma=+1 or -1, 1<=r<b, a in R.               (19)

Indeed write uniquely |v|=b^n r in this half-open range, set sigma=sign v
and a=(-1)^n u. Iteration changes n but not sigma,r,a, proving both coverage
and uniqueness. The half-open boundary simply selects a representative; no
point is deleted. a=0 retains x=1,y!=1, and both signs of v retain y>1 and
0<y<1. All nonzero log-axis and other strata are accounted for.
Each such orbit is bi-infinite with unique incoming at every depth. Source
and extension isotropy and ENTIRE H are zero, despite the du step clock lambda.
For the point z_n, complete physical phases are

    original/nu: h+(-1)^n a+sigma b^n r+n lambda in R;
    ordinary du: h_0+n lambda in R.                (20)

These differ from the reference-arrow phases only by a componentwise constant.
An arrow z_m->z_n has lag m-n; (16) verifies (20) directly. Translation is
free, with no positive primitive or repetition. Equations (15)–(20), together
with the fixed and two-cycle cases, exhaust ALL points, arrows and histories.

## 9. Separate target dispositions of the full E and R owners

E has b=2, lambda=log2 and integer exponent matrix diag(-1,2), abs(det)=2.
Its ENTIRE positive packet ledger consists of ONE fixed primitive log2 and
a continuum of distinct two-cycle primitives log4, one per a>0. Full incoming,
all kernels and phases are (14)–(20) with this exact b; no source is omitted.
The log4 periods are primitive because H=log4 Z on each two-cycle; nonunit
clock-zero arrows do not insert a log2 loop. E FAILS prime-only support.
Nonperiodic components add only the free lines of (19),(20), not new periods.

R has b=sqrt2 and lambda=log sqrt2. Its actual full inverse, IMAGE and
histories are separately (14)–(20) with b=sqrt2; no integer exponent was
substituted for its real exponent. It has ONE fixed primitive log sqrt2,
which is not log of an ordinary integer prime since 1<sqrt2<2.
It also has a continuum of distinct two-cycle primitives 2lambda=log2,
each with ENTIRE H=log2 Z, source isotropy 2Z, trivial extension isotropy
and all phases (18). Thus R FAILS prime-only at its fixed packet AND prime
uniqueness on its two-cycle continuum. It is an EXTERNAL real-exponent
boundary control, not a counterexample within the integer-exponent class.
No all-prime coverage or new arithmetic source is supplied by either control.

The three controls retain all positive-cone states. Their included log axes
and lines x=1,y=1 are explicitly classified; excluded zero-coordinate axes
were never source objects. Coefficients are the three frozen choices, not
post-result tuning. A prime-log occurrence alone does not prove naturalness;
the full packet and measure ledgers expose why these examples do not admit
an arithmetic candidate or discharge the future PROVES_TOO_MUCH question.

## 10. Bounded conclusion and freeze gate

Established: full own monomial inverses and every-point Lebesgue IMAGE;
separate nu and du IMAGE/clock formulas; exact ALL-arrow bridge and height
sign; complete kernel/isotropy/incoming/phase transport; global unimodular
H=0 without cycle assumptions; and all three controls' complete dynamics.
The unimodular subclass has an empty positive physical ledger globally.
Nonunimodular integer owners are not globally stopped or prime-classified
here. No Markov/IR realization, new grammar, 434 splicing theorem or cycle
existence result is claimed. Arbitrary Borel pieces remain exactly as frozen.
Portfolio: retain the conditional owner bridge/filter; STOP the unimodular
positive-ledger route; no arithmetic candidate admission or new round follows.
Same-object ledgers are intact: measures are named separately and the change
of height is proved, not a substituted clock. Arithmetic T1 NOT PASSED;
geometric clock COMPONENT only; T3 NOT AUDITED; classical NOT APPLICABLE;
formal UNASSIGNED; B NOT INVOKED. Strong naturalness remains OPEN.
This raw precedes manuscript access; CP2/CP3 are NOT PERFORMED.
Root must fully read this frozen raw before a distinct PAPER UNLOCK.

EOF — independent card-only derivation complete; HOLD for manuscript unlock.
