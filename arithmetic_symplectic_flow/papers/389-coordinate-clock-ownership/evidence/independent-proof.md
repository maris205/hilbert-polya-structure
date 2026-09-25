# CCG01 — independent coordinate/cotangent ownership audit

Candidate `ANG-AUDIT-20260922-CCG01`; `GEOMETRIC-RETURN-20260922-H`, round5/5.
2026-09-22; reviewer `/root/nonlocal_source_review`.
Inputs: original54-line card plus its9-line pre-mathematics clarification.
Original prefix SHA256 d90790f1f22e80e8918722e8e5030f1d2994b014c0215c1869fd1f23588e6162.
Clarified63-line card SHA256 19bee24c132e6e7c10c51825b0b934546bac5d811b25e23d2d4c37f6e1929633.
Root explicitly released mathematics after the resolved CP1 check. No389
manuscript, peer proof,385 result or probability construction was accessed.
Shared-history internal review is NOT_CALIBRATED, not blind or external review.

## 1. Single-valued branch data and the entire conditional groupoid

Let F be a deterministic partial map on the declared X. Every iterate below
is used ONLY where all its steps are legal. At each actual step x->Fx the
clarified input assigns ONE finite positive inverse density Jacobian
J(x)=J_m I_x(Fx). Put kappa(x)=-log J(x), with no sign assumption, and
A_n(x)=sum_(0<=i<n)kappa(F^i x), A_0=0. Overlap ambiguity without a unique
assigned Jacobian is NOT a member of this defined-clock class: it stops.
No germ coordinate or extra history label is secretly added to X.

Keep G={(z,k-l,w):F^k z=F^l w}, with all legal k,l>=0 and equal triples
identified. Inversion reverses endpoints and lag. For two composable arrows,
pad the smaller of their middle exponents to the larger one. The requisite
additional steps exist because the larger middle iterate is already legal.
This proves composition by addition of lags even for a partial F.
Define c(z,k-l,w)=A_k(z)-A_l(w). Two witnesses of the same triple differ
by common padding, whose common-tail sums cancel; composition uses the same
padding argument. Thus c descends and is additive on the ACTUAL groupoid.

Its entire clock kernel is the legal triples with A_k(z)=A_l(w); its lag
kernel uses k=l; their intersection imposes both tests. Every actual incoming
arrow to z is obtained by all legal k,l and ALL points w satisfying
F^l w=F^k z. This includes all actual inverse branches and all prehistories.

Nonzero source isotropy is equivalent to eventual periodicity. If a legal
tail enters a cycle of least period d, its entire isotropy is dZ; all other
points, including terminating partial orbits, have isotropy{0}. Equality of
two distinct iterates creates a legal cycle; division of any subsequent
period by d gives that its difference is a multiple of d. A repeated cycle
can be iterated indefinitely, so the partial-domain condition adds no missing
isotropy multiples after that cycle has been reached.

Write S=sum kappa over the least cycle. On EVERY incoming point in its class,
c sends rd to rS, since transient prefixes cancel. The full height extension
has arrows(w,h)->(z,h+c(g)), retaining ALL real h. Translation acts on its
orbit SET. Its stabilizer is exactly H_x=c(G_x^x), because any chain returning
to source x composes to an isotropy arrow, and each such arrow gives a return.
Thus H=S Z on a periodic class and H={0} otherwise. Extension isotropy is
ker(c restricted to source isotropy): dZ if S=0, trivial if S!=0; it is
trivial on non-eventual classes. Source period alone does not imply time.

For an arrow g from a reference x to z, the complete phase of(z,h) is
h-c(g) modulo H_x. Consequently the whole part of the orbit SET above each
source orbit is R/H_x. If S!=0 it has least positive physical period |S|;
the oriented r-fold source traversal has signed clock rS. If S=0 there is
NO positive physical return, although source/extension isotropy remains.
Distinct cycles cannot merge under equal-tail arrows unless they are phases
of the same least cycle. These are set statements, not classical suspensions.

## 2. Coordinate changes with transported or replaced density

Let phi be the frozen C1 diffeomorphism, X'=phi(X), F'=phi F phi^(-1),
with domains and every inverse extension transported by the SAME phi.
For m'=phi_*m, the change-of-variables identity gives
J_(m') (phi I phi^(-1))(phi y)=J_m I(y) at every assigned branch point.
Thus kappa'(phi x)=kappa(x), c'(phi z,n,phi w)=c(z,n,w), and the full
height/groupoid conjugacy is (x,h)->(phi x,h), with unchanged physical time.

Alternatively fix a positive continuous target density n, such as standard
target-coordinate volume. Put r=d(phi^*n)/dm, a finite strictly positive
point function, and b=log r. In local volume coordinates m=rho(x)|dx| and
n=eta(z)|dz|, r(x)=eta(phi x)|det Dphi(x)|/rho(x). Absolute determinants
are essential: signed clocks are NOT logarithms of signed determinants.
The exact inverse-branch law is

    J_n(phi I phi^(-1))(phi y)=J_m I(y) r(Iy)/r(y).                   (1)

It follows that

    kappa'(phi x)=kappa(x)+b(Fx)-b(x),
    c'(phi z,k-l,phi w)=c(z,k-l,w)+b(w)-b(z).                         (2)

The full height conjugacy is therefore

    Gamma(x,h)=(phi x,h-b(x)).                                      (3)

Indeed the two image heights differ by c+b(w)-b(z), exactly as required.
Gamma is bijective and commutes with translation by the SAME real time.
No time-unit rescaling occurs. All incoming arrows, heights and phases are
transported; source isotropy and H are unchanged under the source conjugacy,
and extension isotropy is preserved. The cycle sum S telescopes unchanged,
so least positive times and oriented repetitions are unchanged as well.

The entire clock kernel need NOT be the old clock kernel as a subset of
unextended arrows: its new test is c(g)=b(z)-b(w). The lag kernel transports
unchanged, and the intersection adds zero lag to that new test. This is
consistent with height conjugacy, which moves the chosen zero-height sections.

Neither b nor phi's derivative needs a uniform bound on a noncompact domain.
Equations(1)–(3) use finite pointwise values and finite legal paths. They prove
no asymptotic estimate requiring bounded b and assert no positive-step roof.
On a nonmanifold X these are transformations of declared metric/Jacobian
data; they do not invent an ambient Lebesgue IMAGE law restricted to X.

## 3. Self-contained continued-fraction owner

Take sequences a_i>=2 with a_(i+1)|a_i+1. Each I_a(t)=1/(a+t) sends
[0,1/2] into itself with derivative magnitude <=1/4. Nested images for a
fixed infinite digit sequence are nonempty compact intervals of diameters
at most(1/2)4^(-n), hence meet in exactly one x. The same construction at
every tail gives x=1/(a_0+y), with 0<y<1/2 and 0<x<1/2.
Then floor(1/x)=a_0 and y=1/x-a_0, so digits are recovered uniquely.
Uniform contraction makes coding continuous; each finite recovered digit
is locally constant because its fractional tail is strictly between0 and1/2.
The coding is a homeomorphism onto the declared X, and shift is its return F.
The values are irrational: for a rational x, the positive fractional-return
algorithm strictly decreases its positive integer denominator until it must
terminate, incompatible with infinitely many strictly positive tails.

The full inverse domain E_a consists exactly of tails with first digit b
dividing a+1. Every actual preimage begins with one such a. A length-m prefix
u is legal exactly when its internal adjacent divisibilities hold and the
first tail digit divides u_(m-1)+1; the empty prefix has the whole domain.
No other symbolic or geometric point is used to supply an inverse.
The local analytic extensions are I_a(t)=1/(a+t) and
f_a(q)=1/q-a on V_a=(1/(a+1/2),1/a), mapped onto(0,1/2).
Their derivatives are -1/(a+t)^2 and -1/q^2, respectively.
For declared dx density, J I_a(y)=x^2 at x=I_a y, so

    kappa(x)=-2 log x=log|f_a'(x)|>log4.                            (4)

This is a specified metric branch clock, not a probability or Lebesgue IMAGE
claim on X. For a legal word u, set M_u=product_i [[0,1],[1,u_i]], with
bottom row(C_u,D_u). Then I_u(t)=(A_u t+B_u)/(C_u t+D_u),
|I_u'(t)|=1/(C_u t+D_u)^2, since each factor has determinant-1.
Denominators are positive on the actual domain. Consequently every legal
arrow(u t,|u|-|v|,v t) has

    c=2 log[(C_u t+D_u)/(C_v t+D_v)].                               (5)

Equation(5), equality of denominators, and equality of prefix lengths give
the complete clock-kernel, lag-kernel and intersection tests on this owner.
The incoming and height formulas in§1 apply to all legal prefixes, not a
selected cylinder, and require no probability normalization.

## 4. Entire23 packet, both phases and all incoming

The word23 is legal because3|2+1 and2|3+1. Its geometric phases solve
x=1/(2+y), y=1/(3+x), yielding

    x=(sqrt15-3)/2,  y=(sqrt15-3)/3,
    xy=4-sqrt15,  Lambda=(xy)^(-2)=(4+sqrt15)^2=31+8sqrt15>1.

They are distinct, so the least source period is2. Coding injectivity shows
that the ENTIRE source class O contains exactly every legal finite prefix
followed by either of these two periodic tails. Its source isotropy is2Z
at every point, not merely at x or y. Its cycle clock is

    S=-2 log(xy)=log Lambda=2 log(4+sqrt15)>0.                        (6)

On all O, extension isotropy is trivial, H=S Z, and the complete physical
packet is R/S Z, with all real offsets related by h-c(g) modulo S.
Its r-fold source cycle has lag2r and time rS, not a new primitive packet.
Every incoming state is obtained from the exact prefix domains of§3;
there is one packet for both phases and all their prefixes together.

## 5. Own coordinate controls, including the missing-endpoint issue

Q1 uses phi_1(q)=q/(1+q), mapping(0,1/2) onto(0,1/3).
Its full conjugate branch, on phi_1(E_a), is

    K_a(z)=(1-z)/(a+1-a z),  |K_a'(z)|=1/(a+1-a z)^2.

With standard dz, r_1(q)=1/(1+q)^2 and b_1=-2 log(1+q).
Its step clock is(4)+b_1(Fq)-b_1(q), and its complete height conjugacy is
(q,h)->(phi_1 q,h+2 log(1+q)). With pushed dx instead, target density is
(1-z)^(-2)dz and step clocks are exactly(4). These two target-density
descriptions must not be confused, although their full closed-loop times agree.

Q2 uses phi_2(q)=q^2, mapping(0,1/2) onto(0,1/4).
Its full conjugate branch, on phi_2(E_a), is

    K_a(z)=1/(a+sqrt z)^2,
    |K_a'(z)|=1/[sqrt z (a+sqrt z)^3].

With standard dz, r_2(q)=2q, b_2=log(2q), and the step clock is
-3 log q+log(Fq). The height conjugacy is(q,h)->(q^2,h-log(2q)).
Pushed dx instead has density(2 sqrt z)^(-1)dz and preserves step clocks.
There is NO uniform positive lower bound for r_2 on actual X: the legal
infinite sequence n,n+1,n+2,... gives source points tending to0 as n grows.
The endpoint0 is not a source point. Every actual r_2 and every value in the
height conjugacy is finite and positive where required; an unbounded gauge
does not obstruct this pointwise conjugacy or any finite closed-loop sum.

For EACH Q control all domains, prefixes, integer lags and real heights are
transported bijectively, with the full kernel law(2), not an assumed identical
clock kernel. On the entire image of O the source isotropy is2Z, extension
isotropy trivial and H=(log Lambda)Z. Both source phases, all incoming and
all positive primitive times/repetitions agree with(6), without rescaling.

## 6. Full cotangent control: separate owner and full fibers

Regularity boundary: a merely C1 base f need not make p/f'(q) differentiable
in q. Hence a classical pointwise cotangent determinant is NOT automatically
defined for that general class. The ACTUAL probe branches above are analytic;
all determinant statements below concern these branches, or an explicitly
sufficiently regular conditional subclass (C2 suffices). This does not stop
the actual analytic control or silently upgrade the general C1 hypothesis.

For such a local diffeomorphism f:V->W, retain ALL real p and define

    fhat(q,p)=(f(q),p/f'(q)).

Its derivative is triangular with diagonal f'(q),1/f'(q) and lower-left
-p f''(q)/(f'(q))^2. Thus det D fhat=1 everywhere. Also P dQ=p dq,
so the full smooth local map preserves the canonical two-form and Liouville
area. Every inverse has determinant1 as well: its full area clock is ZERO.
For a merely C1 f the same formula is a homeomorphism preserving area by
one-dimensional change of variables followed by fiber scaling; that is a
measure-transport statement, not an unproved differentiable determinant claim.

For the actual probe, fhat_a(q,p)=(1/q-a,-p q^2), and all actual inverses are
(y,P)->(1/(a+y),-P(a+y)^2) on E_a times R. The conditional lifted source
is the explicitly defined set X times R inside the local ambient cotangent
charts, NOT an intrinsic T*X or a globally admitted symplectic carrier.
Its point-lag relation retains all legal cotangent histories and all p.
Its clock kernel is the WHOLE actual lifted groupoid; its lag kernel is the
full zero-lag relation of lifted points, and their intersection is that lag
kernel. The extra extension height h is separate from the cotangent fiber p.

Let D_m(z) be the nonzero product of actual forward derivatives for m steps.
An arrow between lifted points over a base equality F^m z=F^n w exists
precisely when

    p_z/D_m(z)=p_w/D_n(w).                                         (7)

This is ALL incoming fiber transport, not a zero-section selection. Over a
pure23 phase, the2-step return sends p to p/Lambda; the2r-step return sends
p to p/Lambda^r. It is fixed for a nonzero integer r exactly when p=0.
Odd-step returns cannot fix the base phase. Along every incoming base prefix,
the nonzero multiplier D_m preserves whether the fiber is zero. Therefore
over the ENTIRE O, source isotropy of the lifted point-lag owner is2Z when
p=0 and trivial when p!=0. Nonzero fibers do NOT become periodic by projection.

For completeness, choose the base phase x as reference. Every lifted source
orbit over O meets its fiber. Its intersections there are exactly
{p Lambda^r:r in Z}; at p=0 this is a singleton. Equation(7) transports this
complete multiplicative class to every other base phase and legal incoming
history. Thus no nonzero fiber class or zero fiber is discarded.

Because the full area cocycle is zero, the extension's fixed-object isotropy
equals that source isotropy, and H={0} on EVERY lifted source orbit, including
the zero-section cycle. Each such orbit contributes a full real height line,
with phase h unchanged along incoming arrows. There is no positive physical
period from the full determinant clock, even at the actual2-periodic points.

The local return germ has derivative diag(Lambda,Lambda^(-1)) at(x,0), and
its nonzero powers have diag(Lambda^r,Lambda^(-r)), never the identity.
Thus fixing that point does not make the full local map or its germ an
identity. This particular isotropy has distinct return germs; the general
point-lag construction must NOT identify different lags merely because an
ambient germ elsewhere might be identity. Germ and point-lag quotients are
different contracts, and no theorem here exchanges them silently.

The zero section has zero two-dimensional Liouville area and carries no
induced one-dimensional density equal to dq from restriction of that area.
The projected derivative |f'| recovers a BASE-direction metric quantity,
not the full cotangent determinant. Choosing that direction, another action
or another metric as the clock would require a separately owned tuple.

## 7. Scoped decision

Coordinate controls are complete re-expressions of closed-loop clock data,
even with target standard volume and an unbounded pointwise height gauge.
The cotangent full-determinant clock changes owner and is zero; its actual
fiber recurrence and source isotropy do not supply positive physical times.
This establishes neither a global symplectic realization nor an obstruction
to every conservative lift or every separately owned action clock. Period
classification outside the declared conditional/local probe scope remains
unclaimed. Strong naturalness OPEN; T0–T2 conditional only; classical fields
NOT APPLICABLE; T3 NOT AUDITED; formal UNASSIGNED; Route B NOT INVOKED.
No numerical experiment, outside source, target fitting, Git/PDF/publication
action or sixth candidate was used. Proofs are exact from the clarified card.

EOF — card-only raw proof complete; freeze before any manuscript unlock.
