# Nonnegative geometric quotient: owned clock, no source cycles

Paper ID: `321-nonnegative-geometric-quotient`.
Candidate ID: `ANG-20260920-GQF01`. Date: 2026-09-20.
Status: `OWNED QUOTIENT CLOCK; NO SOURCE CYCLES — STOP / FORK`.
Classical A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED.

## Abstract

We freeze the full nonnegative real three-space with ordinary volume and
the actual quotient update (x,y,z)->(y,z,(1+y^2+z)/x) for x>0.
Its zero first-coordinate face remains terminal with all incoming histories.
Integer divisibility is an integrality readout of this transport, not an
acceptance gate deleting noninteger successors. The exact inverse and volume
IMAGE give kappa=log((1+y^2+z)/x^2). On the positive domain
this is the difference of log(xyz) across a step; an explicit
finite-prefix potential handles every boundary history without log0. Thus the
full actual clock is a global coboundary and has zero time image
on every source isotropy group. Independently, a one-line cyclic-square
identity excludes ALL main source periods, not merely fixed/two-step returns.
Positive histories are nevertheless infinite and nonperiodic. Three controls retain
their own boundaries, inverses and clocks; a unit-numerator control has
source periods 1,2,6 with zero time, while a shifted-divisor control
also has no source cycles. The main prime-packet target fails, and
the owner stops/forks without a higher-period enumeration or borrowed clock.

## 1. Identity, frozen source and symbolic lineage

| Field | This exact owner |
| --- | --- |
| Carrier / measure | X=[0,infinity)^3, relative Borel structure, restricted Lebesgue volume |
| Actual source | Partial real quotient update below; whole x=0 face terminal |
| Arithmetic | Integer quotient/remainder and integrality readout, not real permission |
| Clock | Derived own inverse IMAGE with declared analytic full-point version |
| Packets / repetitions | Complete actual retained-lag groupoid and X x R extension |
| Controls | NUMERATOR-UNIT, SQUARE-OFF, DIVISOR-UNIT-SHIFT |
| Classical base / roof / mapping torus | NOT APPLICABLE |
| Operator / trace / determinant | NOT SUPPLIED / NOT PURSUED |

The [original card](candidate-card.md), first 158 lines, was frozen
before these results, SHA-256
`1075594549a9f0acc9ac94e999e4dde9fada719c65fc01b4ccaa947af0e53534`.
Root read all 196 lines of the
[320 frontier](../320-divisible-sum-quotient-register/evidence/scout-record.md),
SHA-256 `b3bd8547a228782ee97b8e5ba70bc8f1d6d79199150daba668a5c9c3742999a5`.
The [source record](evidence/scout-record.md) and [review](evidence/independent-review.md)
separate actual author access, inherited history and manuscript exposure.

Write N(y,z)=1+y^2+z. The full source is

    D={x>0} subset X,
    T(x,y,z)=(y,z,N(y,z)/x) on D.                   (1)

Every point of x=0 is terminal, retaining T^0 and all incoming
histories; no reset, absorbing self-loop or infinity point. All y=0,
z=0, units and noninteger inputs use the same formula. The declared
carrier is nonnegative from inception, not a selected positive subsystem of
a signed owner. The positive domain below is used for analysis only;
the entire boundary remains in the actual source.

At integer a>0,b,c>=0, the third output is (1+b^2+c)/a.
Its integrality iff a divides 1+b^2+c is an actual readout,
NOT the real-source permission. Failed-integrality inputs continue to their real
noninteger successors. At (a,b,c)=(d,1,n-2), n>=2,d>=1,
this readout is d|n, with proper symbols 1<d<n retained.
The lineage is divisor-symbolic observation -> integer quotient integrality ->
continuous quotient transport retaining failed-integrality successors -> new numerator/divisor.
No prime list, factor table, integer-only trajectory selection or prescribed time.
The numerator, register cycle, carrier and volume are design choices;
stronger naturalness, canonical A0 and conservative/symplectic realization remain OPEN.
No Logistic/Henon conjugacy or older theorem is inherited.

## 2. Exact inverse, image and all retained boundaries

For any target (u,v,w) in X, the exact inverse is

    theta(u,v,w)=((1+u^2+v)/w,u,v), E={w>0}.        (2)

The numerator is at least one. Substitution proves theta(E)=D,
T(theta(w))=w on E and theta(Tz)=z on D. Thus T is
a Borel partial bijection D->E, not onto the full X. Every
target in E has exactly one predecessor; every target with w=0
has none. Chart subdivision cannot add multiplicities.

A missing inverse is not terminality. For example (1,0,0) has
no inverse, but a legal step to (0,0,1); this latter point
is terminal and has predecessor (1,0,0). Every zero face and
axis is retained, with no limit value assigned to an illegal divisor.

Let X_+=(0,infinity)^3. Both T and theta preserve X_+ and
are mutually inverse there, so every positive history continues indefinitely
forward and backward. On X\X_+, the first initial zero reaches
the first register before any generated positive third register can remove it:

    d(z)=0 if x=0;
    d(z)=1 if x>0,y=0;
    d(z)=2 if x>0,y>0,z=0.                          (3)

This is the exact stopping depth. No boundary state reaches X_+;
no positive history can merge with a boundary history. For a terminal
anchor omega=(0,a,b), the entire backward chain is its legal
theta iterates. If b=0 it has no predecessor. If b>0
it has theta(omega), whose third coordinate is a; a second
predecessor exists iff a>0 and then has third coordinate zero.
There is no third predecessor. These complete chains, not selected endpoints,
are the full boundary tail classes. They have at most three states.

## 3. Actual volume IMAGE and pointwise lag clock

Writing A(u,v)=1+u^2+v, the inverse derivative is

    D theta=[[2u/w,1/w,-A/w^2],[1,0,0],[0,1,0]],
    J_theta=A/w^2>0 on E.                           (4)

The chart extends smoothly across u=0 or v=0 while w>0
and A>0. Its change-of-variables identity on the relative nonnegative
domain is, for every Borel B subset E,

    mu(theta B)=integral_B (A/w^2) dmu.

Interior change of variables and the smooth null-face correspondence also
cover arbitrary boundary-containing Borel sets. The same explicit derivative
specifies the FULL-POINT version on every retained face. This is not
a claim that an a.e. density determines arbitrary null values, and
no inverse at w=0, atomic ratio or changed measure is inserted.

At an actual source z=(x,y,z3), with new third coordinate
z3'=N(y,z3)/x, the owned clock is

    kappa=log(N(y,z3)/x^2)=log(z3'/x).              (5)

It is signed in general, not a positive roof or runtime. For
S_k(z)=sum_(0<=i<k)kappa(T^i z), S_0=0, the inverse
of that actual history has IMAGE exp(-S_k(z)). A branch pair
from w to z, meeting after lengths k,l, has IMAGE
exp(-S_k(z)+S_l(w)), with its own full-point composition. Define

    G={(z,k-l,w):T^k z=T^l w,k,l>=0,both histories defined},
    c(z,k-l,w)=S_k(z)-S_l(w).                       (6)

The inherited Borel structure in X x Z x X is used; source
w, range z, equal triples one arrow. Common legal future extension
cancels in two presentations of the same lag. Composition aligns the
middle histories at their longer defined length and cancels the common
part. This proves pointwise well-definedness/cocycle, including terminal T^0
without evaluating a nonexistent terminal step. The actual forward arrow
(Tz,-1,z) has clock -kappa(z), its inverse +kappa(z).
Keep every (z,h), arrows (w,h)->(z,h+c), and full R-translation.
Only a Borel/set quotient is asserted, not a smooth/etale/Hausdorff
space or invariant-volume-times-dh result.

## 4. A GLOBAL clock potential, including every zero face

On X_+ define P(z)=log(x*y*z3). Equation (5) gives

    kappa(z)=P(Tz)-P(z).                            (7)

Do NOT evaluate this logarithm on the boundary. For every boundary
state use the finite depth (3), terminal anchor A(z)=T^d z,
and actual prefix S(z)=sum_(0<=i<d(z))kappa(T^i z). Define

    P_tilde(z)=log(x*y*z3) on X_+,
    P_tilde(z)=-S(z) on X\X_+.                     (8)

Terminal S is the empty sum zero. Since S(z)=kappa(z)+S(Tz)
at a legal boundary step, (7) holds there with P_tilde too.
The two invariant types never merge. Thus P_tilde is a finite
Borel potential on ALL X, with no log0 or terminal clock. On
every actual arrow,

    c(z,ell,w)=P_tilde(w)-P_tilde(z).                (9)

Consequently every source isotropy time image H is ZERO. This is a
theorem about the existing frozen clock, not replacing its density or
resetting it to zero. The cocycle need not vanish on nonloop arrows.
Full extension equivalence is precisely actual source-tail equivalence together
with equality of h+P_tilde(z). On boundary chains this is h-S(z).
This supplies the complete time-phase relation without selecting a favourable
orbit, branch or section, and without assuming the quotient is smooth.

Already (9) excludes every positive primitive time for this owner, at
ANY source period. The next short identity additionally decides whether
source periods themselves exist; zero H alone would not decide that.

## 5. Fixed, two-step and ALL-period source obstruction

A fixed state must have x=y=z=t>0. Its remaining equation
is t^2=1+t^2+t, impossible. For a two-step return, both
steps are legal and z=x>0, the next coordinate equals y>0.
The equations are

    x*y=1+y^2+x,    x*y=1+x^2+y.

Adding them gives 0=2+(x-y)^2+x+y, impossible. These are
complete full-state tests; no boundary return is omitted because (3)
already proves every boundary history terminates.

More strongly, suppose there were any actual source cycle of period p>0.
It must lie in X_+. Write its consecutive register sequence as
positive a_i, indexed modulo p; the coordinate shift in (1) forces
state i to be (a_i,a_(i+1),a_(i+2)). Its recurrence is

    a_i*a_(i+3)=1+a_(i+1)^2+a_(i+2).

Summing around the full actual cycle gives

    sum a_i*a_(i+3)=p+sum a_i^2+sum a_i.

But cyclic index permutation yields the exact contradiction

    0<=sum (a_i-a_(i+3))^2=-2*(p+sum a_i)<0.        (10)

Therefore ALL main source cycles are absent. This is one arbitrary-cycle
identity, not a finite-period census extended by guesswork. No state is
eventually periodic; all source isotropy, time image and extension isotropy
are trivial everywhere. Positive histories are still infinite in both
directions, so this is NOT a global termination theorem, nor a
claim about all topological recurrence or asymptotic growth. Boundary histories
are exactly the finite chains in Section 2. No positive prime packet
exists, and the candidate stops/forks.

## 6. Controls, each with its own inverse and clock

### 6.1 NUMERATOR-UNIT: complete source periods with zero time

The OWN source is U(x,y,z)=(y,z,1/x) for x>0, same
terminal face. Its exact inverse is (1/w,u,v) on w>0,
with unique predecessor and OWN IMAGE 1/w^2. At the source,
kappa_U=-2log x=log((1/x)/x), not the main numerator's density.
The boundary stopping depths and complete inverse-chain reasoning (3) apply
to THIS positive-generated map. On X_+, P=log(xyz) again satisfies
its OWN kappa_U=P(Uz)-P(z); on its boundary define its OWN
negative terminal prefix. Therefore its entire cocycle is also a global
coboundary and every H is zero, with exact h+P_tilde,U phase.

All fixed states reduce to (1,1,1). Its complete two-step locus is

    C_2={(r,1/r,r):r>0}.                            (11)

Indeed U^2=(z,1/x,1/y); equality forces exactly (11). On
the positive domain there is also the short exact identity

    U^3(x,y,z)=(1/x,1/y,1/z), U^6=id.               (12)

Thus every positive source period divides six. The only U^3-fixed
state is (1,1,1), so the COMPLETE least-period classification is:
period 1 at (1,1,1); period 2 on C_2 minus that point;
period 6 at every other positive state. Boundary states all terminate
and have no source isotropy. Unique inverse proves each periodic full
tail class is exactly its finite cycle, with no incoming external tail.
For a least-P positive cycle, source and extension isotropy are PZ,
H0, and full phase is the REAL value h+log(xyz), not a
phase modulo a positive time. Every point of each core remains.
These many genuine source cycles supply NO positive time primitive and
cannot rescue the main source, whose source cycle ledger is different.

### 6.2 SQUARE-OFF: fixed zero-time core, higher source periods open

The OWN source is V(x,y,z)=(y,z,(1+z)/x), x>0, same
terminal face. Its exact inverse ((1+v)/w,u,v) on w>0 has
OWN IMAGE (1+v)/w^2, hence

    kappa_V=log((1+z)/x^2).

This source too generates a positive third coordinate, has the boundary
depths (3), and maps X_+ bijectively to itself. Its OWN
kappa_V is P(Vz)-P(z) on X_+, with its OWN boundary
prefix extension. Thus global H0 and full h+P_tilde,V phase hold,
without borrowing main actions, prefixes or density values.

Fixedness gives t^2=1+t, so the only fixed state is
g_phi=(phi,phi,phi), phi=(1+sqrt5)/2. For ALL two-step returns,
z=x and x*y=1+x=1+y force x=y=phi. No least-period-two
core exists. Its unique inverse is itself, so the fixed basin is
singleton, source/extension Z, H0, and real phase h+3log phi
(equivalently h after one common constant shift). Higher source periods
are UNCLASSIFIED, not erased by the global zero-time theorem. Any
actual least-P cycle would retain source/extension PZ with H0;
nonperiodic states have trivial isotropy. No positive time packet is supplied.

### 6.3 DIVISOR-UNIT-SHIFT: full-domain owner and no source cycle

Here W(x,y,z)=(y,z,(1+y^2+z)/(x+1)) is defined on ALL X.
In particular x=0 is NOT terminal. The exact inverse is

    theta_W(u,v,w)=((1+u^2+v)/w-1,u,v),
    E_W={u,v>=0, 0<w<=1+u^2+v}.                    (13)

The upper boundary corresponds exactly to the retained source face x=0.
Every image target has one predecessor; targets outside E_W remain legal
source objects. For example (0,0,2) has no predecessor but has
a next step. Own differentiation gives J_W=(1+u^2+v)/w^2
on (13), including its upper boundary, and

    kappa_W=log((1+y^2+z)/(x+1)^2).                 (14)

This is not (5); the source denominator and inverse domain changed.
Finite-pair substitution/common-future cancellation still define its OWN lag
cocycle. No boundary terminal prefix from the main source may be used.
All forward histories are infinite, and after three steps every state is
strictly positive, because each new third coordinate is positive.

Fixedness would give t(t+1)=1+t^2+t, impossible. A two-step
return gives z=x and

    y*(x+1)=1+y^2+x,    x*(y+1)=1+x^2+y.

Their sum gives 0=2+(x-y)^2, impossible. For ANY source
cycle, write its register sequence a_i as above. Its actual recurrence is

    (a_i+1)*a_(i+3)=1+a_(i+1)^2+a_(i+2).

Summing cancels the linear terms and gives
sum a_i*a_(i+3)=p+sum a_i^2. Hence

    0<=sum (a_i-a_(i+3))^2=-2p<0,                  (15)

excluding ALL source cycles and eventual cycles. All source/time/extension
isotropy are therefore trivial. This conclusion uses its own no-cycle
proof, NOT the main coboundary. In fact on X_+ its own clock is

    kappa_W=P(Wz)-P(z)-log(1+1/x),

so simply copying the main potential identity would be false. No
global phase potential for this control is asserted. All actual arrows
and full height extension remain, with no source recurrence or positive packet.

## 7. Gate decision and claim limits

| Audit | Result for ANG-20260920-GQF01 | Limit |
| --- | --- | --- |
| T0 full source / inverse / boundaries | ESTABLISHED exact partial bijection | All terminal/incoming histories retained |
| T1 arithmetic readout / owned clock | ESTABLISHED within declared design | Integrality is not real permission; stronger naturalness OPEN |
| T2 positive prime-packet target | FAILS: global zero H and no source cycles | Not a theorem about other quotient architectures |
| T3 trace / zeta / operator | NOT SUPPLIED / NOT PURSUED | No borrowed analytic object |
| Classical A0/A1/A2 | NOT APPLICABLE | No classical symplectic/roof construction |
| Formal Route / Route B | UNASSIGNED / NOT INVOKED | No formal evaluation |

Portfolio STOP / FORK. The same-object ledger is intact: actual quotient,
integer integrality readout, full nonnegative carrier, ordinary volume, all-point
clock and retained-lag packets belong to this one frozen source. The
global zero-time proof includes boundaries; the independent cyclic-square proof
rules out source cycles as well. No choice of representative, control
packet, integer-only restriction, measure change or roof repairs this owner.

Controls show why zero time and absent source recurrence must stay distinct:
NUMERATOR-UNIT has periods 1,2,6 and zero H, while main and
shifted-divisor sources have no cycles at all. SQUARE-OFF's unclassified
higher source periods stay OPEN despite its global zero H. This is
a reusable control distinction, not accumulated Route credit.

All proofs are exact, no scientific numerical runs, cutoff, prime data or
external literature. The all-period results follow from explicit identities, not
from checking only fixed/two-step states. No invariant-volume quotient, smooth
flow, canonical arithmetic mechanism, RH or Hilbert--Polya construction follows.
Internal ARS three-checkpoint review is NOT_CALIBRATED, not external peer
review, machine proof or independent-error evidence.

Evidence: [card](candidate-card.md), [ledger](claim-ledger.md),
[inputs/checks](evidence/README.md), [review](evidence/independent-review.md),
[source/frontier](evidence/scout-record.md), [package](README.md).
Positive 304, retained partial-positive 320 and older packages unchanged;
241/242 paused; goal active. Markdown only; no PDF/LaTeX,
upload/publication, Git staging or commit.
