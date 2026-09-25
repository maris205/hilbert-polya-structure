# Product/fractional-remainder transport: an owned plane clock and finite termination

Paper ID: `314-product-fractional-remainder-plane`.
Candidate ID: `ANG-20260920-PFR01`. Date: 2026-09-20.
Status: `OWNED PLANE CLOCK; EVERY HISTORY TERMINATES — STOP / FORK`.
Evidence: exact full-source theorem, not a finite trajectory experiment.
Formal coordinates UNASSIGNED; Route B NOT INVOKED.

## Abstract

This candidate reads integer divisibility directly from an actual real
point, with no independent integer-root coordinate. The whole nonnegative
plane is retained. We prove every inverse branch, exact image,
countable predecessor multiplicity and its own Lebesgue IMAGE clock, including
null axes and cuts. A two-step coordinate identity then proves
that EVERY actual forward history terminates after finitely many steps.
Strict decrease alone would not suffice; the proof excludes a
positive limiting coordinate at a floor boundary. Terminal anchors and
stopping depths classify every tail arrow, while finite clock sums
give the exact extension quotient and show that all time stabilizers
and both kinds of isotropy are trivial. No primitive closed
packet exists. Two changed-gate controls share this termination mechanism
but have different images and predecessor counts. The separately owned
FRACTION-OFF control instead has exactly one positive primitive, of time
log 2; it is not a repair of the main
candidate or an all-primes result. Stronger naturalness remains OPEN.

## 1. Identity, scope and lineage

The [original card](candidate-card.md) was frozen as 182 lines,
SHA-256 `c58f6f19f731bd48dc77510dafce381c4901dcc5fbc3c1cf545eb2247687c6aa`.
On Y=[0,infinity)^2 with plane Lebesgue measure, define

    a=floor(u), N=floor(u*v),
    T(u,v)=(u*v,(u-a)/v)

exactly for u>=1, v>0 and a|N. Other states
are terminal: T^0 exists but no successor loop is added.
The usual a|0 convention is retained. All axes, origins,
integer/product cuts and unit cases use this law.

| Ledger item | Same frozen owner | Boundary |
| --- | --- | --- |
| Arithmetic/geometric source | Current floor(u), floor(u*v), divisibility and actual product/remainder transport | No external integer label or time schedule |
| Measure and branches | Full closed quadrant, ordinary Lebesgue, all actual inverse branches | No atoms, weights or selected centres |
| Arrows and clock | Full partial retained-lag relation, own IMAGE cocycle | Analytic null-cut version explicitly frozen |
| Complete real time | All Y x R with actual arrows and translation | Borel/set-level quotient, not classical suspension |
| Primitive convention | Entire isotropy time image and actual arrow/time equivalence | No chosen recurrent subset |
| Analytic/later owner | NOT SUPPLIED / NOT PURSUED | No trace, determinant or operator transfer |
| Classical/formal status | A0/A1/A2 NOT APPLICABLE | UNASSIGNED; B NOT INVOKED |

At (u,v)=(d,n/d), n,d>=1, actual permission is
d|n. Proper-divisor symbols are therefore present as a full-carrier
inspection interface, not an invariant selected subsystem. The real output
performs multiplication and fractional-remainder transport, and supplies the next
integer readout. This is a concrete divisor-symbolic deformation, not
a proved Logistic/Henon conjugacy or conservative lift. The transport,
gate and measure remain declared designs; naturalness is OPEN.

The [313 source record](../313-gcd-normalized-radix-flow/evidence/scout-record.md),
SHA-256 `3ecbdd077c9f272bf69e26ce2d58458672ef143ca0f6d8d1dcc8ff0dc482d310`,
was read fully before freeze. Its Section 2 supplies this
tuple, not a theorem. Its carry proposal is a separate
unfrozen direction. The [prior-work guide](../../docs/prior_work/README.md)
supplies lineage context only. No old theorem or Route credit,
prime table, zero data, logarithmic roof or fitted parameter enters.

The precommitted question is full clock ownership followed by the
fixed and two-iterate return/termination gate. This paper proves a
global answer, not an inference from missing fixed points alone.

## 2. Every inverse and the exact full image

For a>=1,N>=0 with a|N, the complete source cell is

    U_(a,N)={a<=u<a+1, v>0, N<=u*v<N+1}.

At target (s,t), solving s=u*v and t=(u-a)/v
gives u*(u-a)=s*t and the unique permissible root

    R_a=(a+sqrt(a^2+4*s*t))/2,
    I_a(s,t)=(R_a,s/R_a).                         (1)

Its EXACT domain is

    s>0, t>=0, a|floor(s), s*t<a+1.             (2)

Indeed R_a>=a is automatic, and R_a<a+1 iff
s*t<a+1, since r*(r-a) is strictly increasing on
r>=a and equals a+1 at r=a+1. Substitution
proves both inverse identities; conversely every source lies in its
own unique a,N cell and gives (1)–(2). This
is an exhaustive list, not merely a sufficient subset.

Different a give different predecessors: R_a is strictly increasing in
a at fixed s,t, including t=0 where R_a=a.
For n=floor(s)>=1 the predecessor count is exactly

    #{a|n : s*t<a+1}.                            (3)

For 0<s<1, EVERY positive integer a with a+1>s*t
is a predecessor, so there are countably infinitely many. There
is no truncation of a|0 and no selected divisor. Since
the largest positive divisor of n>=1 is n, the FULL
image is

    {0<s<1, t>=0}
      union {s>=1, t>=0, s*t<floor(s)+1}.         (4)

Every s=0 point remains outside the image. Thus T is
partial, countable-to-one Borel, NOT finite-to-one and NOT onto.
Ordinary continuity fails even between DEFINED states. Use v=1:
u approaching 2 from below has a=N=1
and outputs approaching (2,1), while u=2 has a=N=2
and output (2,0). No etale or local-homeomorphism conclusion follows.

## 3. Own IMAGE and legal-history clock

On a fixed a branch the forward derivative is

    [[v, u], [1/v, -(u-a)/v^2]],
    det DT=-(2*u-a)/v.

It is nonzero throughout each actual source, including u=a.
The actual inverse therefore has positive Jacobian

    J_a(s,t)=s/[R_a*(2*R_a-a)],
    rho(u,v)=1/J_a(T(u,v))=(2*u-a)/v.            (5)

In particular at t=0, J_a=s/a^2, finite and strictly
positive for every point in its actual domain s>0. This
is the frozen analytic version on a null axis, not
an atom ratio. No value is assigned to a nonexistent
s=0 inverse. Formula (5) is also the stipulated version
at integer and product cuts, with the exact floor branch.

Each branch formula extends smoothly and invertibly near its actual
points: u>a/2 and v>0 is a suitable ambient region
for the positive quadratic root. Ordinary change of variables, restricted
to the Borel domain (2), proves for EVERY Borel E

    mu(I_a E)=integral_E J_a dmu.                (6)

Null boundary/cut subsets and their images are included; they do
not acquire atoms. Lebesgue measure is sigma-finite, nonatomic and
full-support, but a.e. IMAGE alone would not fix pointwise null
values. Our analytic completion is explicit and not claimed a.e.-forced.

On defined steps put kappa=log rho. With legal products
D_m(z)=product_(i<m)rho(T^i z), D_0=1, the full actual
retained-lag groupoid has source w, range z and

    g=(z,m-n,w), T^m z=T^n w,
    J_g=D_n(w)/D_m(z), c(g)=log D_m(z)-log D_n(w). (7)

Finite actual inverse-branch pairs cover all arrows. Countably many
branches give countable fibres; Borel equality sets of partial iterates
give the Borel arrow set in Y x Z x Y.
To compare two presentations of one triple, extend the shorter
one by their common index difference. The longer presentation already
guarantees those extra steps exist; equal common futures give the
same extra factors, which cancel. Aligning middle histories similarly
proves composition. Substitution gives (7) as each actual pair's
IMAGE, and c is pointwise additive on all legal histories.
No undefined terminal step is differentiated or silently completed.

Keep every (z,h) in Y x R and arrows
(w,h)->(z,h+c). All real translations exist and commute
with these arrows. An actual forward step w->Tw uses
(Tw,-1,w), hence clock -kappa(w), not +kappa(w).
The latter is the forward ITERATE sum/inverse-arrow clock. This
sign will also appear in the terminal-height coordinate below.

The local clock is not identically zero: at (1,1/2)
it is log 2, and at (1,2) it is
-log 2. Both steps are permitted and their next points
are terminals. Nonzero local clock does not establish a closed packet.

## 4. ALL histories terminate: the decisive theorem

First, there are no fixed states. At a defined fixed
point, u*v=u and u>=1 imply v=1; then
(u-a)/v=v would require u-a=1, contrary to floor(u)=a.
Terminals do not contribute artificial fixed loops.

For a current permitted point, put alpha=u-a. A SECOND
step exists exactly when alpha>0, u*v>=1 and
N=floor(u*v) divides floor(u*alpha). On this exact
two-step domain the full geometric iterate is

    T^2(u,v)=(u*alpha, v*(u*v-N)/alpha).

Consequently, for any two actual successive steps, the first coordinate obeys

    u_(j+2)=u_(j+1)*v_(j+1)=u_j*(u_j-floor(u_j)).  (8)

This identity does not discard any permission or boundary condition.
Assume an infinite legal forward history existed. Every u_j>=1
and v_j>0. Its even-coordinate subsequence x_r=u_(2r) satisfies

    1<=x_(r+1)=x_r*(x_r-floor(x_r))<x_r.

It would decrease to a finite L>=1. Because it approaches
L from above, floor(x_r) eventually equals floor(L), INCLUDING
when L is an integer. Taking limits in the eventual
single-cell identity gives

    L=L*(L-floor(L)), hence L-floor(L)=1,

which contradicts the definition of floor. This excludes infinite histories.
The floor-limit argument is essential: strict decrease alone would not
prove finite termination. Every state therefore reaches a terminal after
finitely many actual steps. No uniform bound over Y, numerical
escape threshold, discarded asymptotic orbit or compactness assumption is used.

## 5. Complete terminal classes, arrows and quotient time

Let Z be the exact terminal set:

    u<1, or v=0, or (u>=1,v>0 and floor(u) does not divide floor(u*v)).

Define n(z) as the finite number of steps until first
arrival in Z; n=0 for terminals. It is Borel,
since {n=r} is dom(T^r) intersect (T^r)^(-1)(Z).
Set p(z)=T^{n(z)}(z) and

    A(z)=sum_(i<n(z))kappa(T^i z).                (9)

These are Borel, A is finite at EVERY state and
A=0 on Z. No boundedness or continuity of A is
claimed. The exact arrow classification is

    G={ (z,n(z)-n(w),w) : p(z)=p(w) }.           (10)

If two histories meet, their terminal anchors agree and equality
of remaining stopping depths forces that lag. Conversely going to
the same terminal supplies that arrow. Thus there is precisely
ONE arrow between any two states in the same terminal
basin, and none between different anchors. All possible finite predecessors
are included, even when a branch has infinitely many predecessors.

Using the terminal presentation in (7) gives the global identity

    c(z,n(z)-n(w),w)=A(z)-A(w).                  (11)

All source isotropy is trivial, hence ALL H_z={0} and
all extension fixed-object isotropy is trivial. This is stronger than
merely saying a cocycle has zero periods: there is no
source recurrence either. No positive primitive or repetition exists anywhere.

The exact extension classes have the complete invariant

    (p(z), h-A(z)) in Z x R.                    (12)

Equality of (12) is equivalent to the actual extension-arrow
relation by (10)–(11). Every value is represented by its
terminal (p,h), providing an explicit Borel parameterization and section.
The induced time is (p,H)->(p,H+t), for all real
t, with no nonzero stabilizer. This is a Borel/set-level
quotient realization, not a claim about a Hausdorff coarse topology
or classical symplectic/positive-roof suspension.

Boundary check: the vertical axis s=0 has NO incoming
branch and is terminal, so each such state, including the
origin, is its own source class. At horizontal (s,0),
s>0, ALL immediate predecessors are

    (a,s/a), a>=1, a|floor(s).                  (13)

For 0<s<1 there are countably infinitely many; for s>=1
there are exactly the divisors of floor(s). They all have
stopping depth one, but their own predecessors may also join
the same full basin. No such branch joins different terminals.
Their null-axis inverse values are precisely s/a^2 from (5).

## 6. Three separately owned controls

### 6.1 GATE-OFF

Keep the transport on all u>=1,v>0. Its inverse (1)
now enumerates EVERY a>=1 with s>0,t>=0,s*t<a+1,
without divisibility. Its exact image is {s>0,t>=0};
EVERY image point has countably infinitely many predecessors. It is
not the main image (4). Its own branch derivative,
IMAGE and kappa are (5), proved on these changed domains.

The two-iterate identity (8) holds on its OWN legal
histories. The same eventual-floor limit argument proves finite termination
at its OWN terminal set {u<1 or v=0}. Hence
the constructions (9)–(12), with its own stopping depth,
anchors and clock sums, give all arrows, ALL H=0
and trivial source/extension isotropy. There are no fixed or
higher returns. No main stopping time or terminal anchor is reused.

### 6.2 GATE-SHIFT

Use permission a|(N+1). All inverse branches are (1),
with s>0,t>=0, a|(floor(s)+1), s*t<a+1.
For n=floor(s)>=0 the exact predecessor count is

    #{a|(n+1):s*t<a+1}.

The largest possible a=n+1 gives the exact image
{s>0,t>=0,s*t<floor(s)+2}. All image points have
finitely many predecessors, unlike both zero-modulus main branches and
GATE-OFF. Its own IMAGE remains (5) on these domains.

Its actual two-step identity again gives finite termination, but
at its OWN terminal set, including a not dividing N+1.
Reconstructing stopping depths, anchors and sums gives (10)–(12)
for this control, ALL H=0 and trivial source/extension
isotropy. No fixed/higher source return exists. Shifting permission
has changed the owner, not relabelled the main result.

### 6.3 FRACTION-OFF

Here T_F(u,v)=(u*v,u/v) on the original permission
domain. Its complete inverse is UNIQUE:

    I_F(s,t)=(sqrt(s*t),sqrt(s/t)),
    s,t>0, sqrt(s*t)>=1,
    floor(sqrt(s*t)) divides floor(s).            (14)

These conditions are its exact image. No a-enumeration or main
range inequality is retained. Smooth substitution for this inverse gives

    J_F=1/(2*t), rho_F=2*u/v, kappa_F=log(2*u/v). (15)

The version on retained cuts is its own analytic derivative;
zero axes are outside the inverse domain and remain terminal,
with no incoming branches. Full legal branch pairs again establish
its own cocycle and complete real extension.

The only fixed point is f=(1,1), which is permitted.
To settle ALL higher periods rather than guess from that,
observe on every legal two-step history

    T_F^2(u,v)=(u^2,v^2).                        (16)

If a point had any positive period r, all steps
in that cycle would be legal and (16) would give
T_F^(2r)(u,v)=(u^(2^r),v^(2^r))=(u,v).
Positive coordinates force u=v=1. Thus f is the ONLY
periodic point of ANY period. Its sole actual inverse (14)
is itself, so no other state is eventually periodic either.

At f, source lag isotropy is Z, H=(log 2)Z,
and extension fixed-object isotropy is trivial. Its whole source class
is {f}; its time packet has least positive time log 2
and repetitions r*log 2. Every other state has trivial
source/extension isotropy and H=0: a nonzero lag would imply
eventual periodicity, already excluded. Thus this changed owner has exactly
ONE positive primitive packet globally. No other primes are produced.
This is a positive recurrence/clock control, not a main repair,
natural A0 theorem or all-primes ledger.

It is NOT an all-termination control: (2,1)->(2,2)->(4,1)
->(4,4)->(16,1)->... is a legal infinite integer history.
Every displayed pair and its continued square/diagonal successors satisfy
the divisibility permission. Trivial isotropy away from f does not
mean finite termination, and the main termination theorem is not transferred.

## 7. Gate assessment and limitations

| Gate | Exact evidence | Decision / boundary |
| --- | --- | --- |
| T0 | Full partial Borel source, countable inverse enumeration, exact image, actual arrows | Established; not onto/finite-to-one/classical |
| T1 | Same actual plane transport owns analytic IMAGE and nonzero local clocks | Engineering result; stronger naturalness OPEN |
| T2 | Every main history terminates; exact terminal basins and time quotient | GLOBAL positive-primitive absence: STOP / FORK |
| T3 | No trace, transfer, zeta or determinant supplied | NOT PURSUED |
| Classical / formal | No symplectic base or positive-roof mapping torus | A0/A1/A2 NOT APPLICABLE; UNASSIGNED; B NOT INVOKED |

The decisive obstruction is finite termination of this actual transport,
not an external clock or an unresolved high-period census. Gate
removal does not restore recurrence, whereas changing the geometric remainder
does change it. These are scoped control theorems, not a
universal impossibility for divisor-symbolic geometries or an arbitrary-spectrum theorem.

The entire same-object ledger remains intact. No state, axis,
unit or terminal was deleted; no roof or measure was
changed; no source recurrence was manufactured from terminal identities. Portfolio:
**stop this candidate's positive-prime-packet promotion; retain the owned clock,
global terminal classification and controls; fork**. The independent carry
definition remains pending, without importing any of these conclusions.

## 8. Evidence and integrity

This is an AI-assisted exact derivation, not formal-machine verification
or external peer review. No scientific numerical experiment, finite orbit
cutoff, fitted constant or external literature campaign was used. Internal
ARS raw-card/synthesis/final-adverse review preserves actual access order and
scope; inherited/shared-context review is NOT_CALIBRATED, not cross-model
verification or a guarantee of independent errors.

See the [claim ledger](claim-ledger.md), [evidence/locks](evidence/README.md),
[internal review](evidence/independent-review.md), [source/frontier](evidence/scout-record.md)
and [package index](README.md). Positive 304, 313 and all
old packages/mirrors remain unchanged; 241/242 paused; programme goal
active. Markdown only; no PDF/LaTeX, staging, commit, publication
or upload. No formal Route evaluation or Route-B invocation.
