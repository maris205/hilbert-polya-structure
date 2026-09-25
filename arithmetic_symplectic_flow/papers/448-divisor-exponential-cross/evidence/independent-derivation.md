# DEC01 — independent card-only derivation

Candidate: ANG-20260924-DEC01.
Batch: ADMISSION-EXIT-20260924-T; Paper448, round4/5.
Reviewer: pcr01_independent_review. Date: 2026-09-24 UTC.

## 0. Input and scope

The original 98-line frozen card is the only scientific input opened for
this independent derivation. Its SHA256 is
`1fbc720d1894c9c9c8df5f9143b4f700d34f54469d6dc84092d9f16980640d38`.
Root reported its full read of CP1 and issued the distinct RAW RELEASE.
No author paper, README, ledger, peer answer, helper result or old proof was
opened. This is separate-author, same-model internal work, NOT_CALIBRATED;
inherited shared context prevents a blind or external-review claim.

All reasoning below is exact. There is no numerical root search, scientific
census, network call, Git mutation, PDF or external publication. Fixed-point
classification is restricted to the four frozen cells. Incoming histories
of the resulting cores are unrestricted, as required by the card; studying
their predecessors is not a fixed-point search in additional cells.

## 1. Actual owners, signed quotients and full spatial derivative

At z=(x,y), let A=floor x, B=floor y, N=1-A. For MAIN, arithmetic permission
is B!=0 and B divides N, and the actual integer label is q=N/B. For G,
if B!=0 use the unique remainder r with 0<=r<abs(B), N-r divisible by abs(B),
and q_G=(N-r)/B; if B=0 set q_G=0. This is the specified signed quotient,
not a substitute floor(N/B) rule when B<0. Q keeps only MAIN arithmetic
permission and uses the germ F_0 regardless of the unused arithmetic label.

For any fixed integer label q,

    F_q(x,y) = (exp(y)-q x, exp(x)-q y),
    D F_q(x,y) = [[-q, exp(y)], [exp(x), -q]],
    delta_q(x,y) = det_R² D F_q = q²-exp(x+y).

The MAIN and G legal domains require their own delta_q!=0. Q has
delta_0=-exp(x+y), which never vanishes, so its only legal restriction is
its own arithmetic permission. Q does not inherit the critical set of a
discarded nonzero label. Every excluded state remains a terminal object
with a unit and all actual incoming arrows, not an absorbing fixed point.

The label is frozen for differentiation of its germ. The spatial derivative
is not a derivative through a floor cut. Both output coordinates are then
reread at the next actual step. In the source cells A=1-n, B=d with
n>=2 and 1<d<n, MAIN arithmetic permission is exactly d|n, since N=n.
This is the declared divisor-symbolic connection; the further regularity
test remains a separate geometric gate, not an assertion that every point
in an arithmetically permitted cell is legal.

## 2. All inverse roots and the countable atlas

For a target w=(s,t), every MAIN or G predecessor is obtained by taking
every q in Z and every real solution (u,v) of

    exp(v)-q u=s,       exp(u)-q v=t,

and checking the actual source readouts, that owner's label law and its
own nonzero delta_q. These tests are sufficient as well as necessary:
each retained point is legal for that owner and maps to exactly w.
There is no additional permission test on the target. Thus a critical or
arithmetic-terminal target can still possess all its actual predecessors.

For each q, enumerate the rational open balls B on which delta_q has no
zero and F_q is injective. Around every regular source, the inverse
function theorem gives an open injectivity neighborhood; a rational ball
containing the source and contained in that neighborhood exists. Therefore
these eligible balls cover every actual regular source. This is an exact
countable definition, not an effective finite test of ball eligibility.

Let B_(q,j) be the enumeration and let L_(O,q) be the Borel actual source
set of owner O with label q, including its regularity condition. Put

    P_(O,q,j) = L_(O,q) intersect
               (B_(q,j) minus union_(i<j) B_(q,i)).

The nonempty P form disjoint Borel source pieces covering all legal sources.
The ambient F_q on B_(q,j) is a C-infinity local diffeomorphism and, being
injective, a homeomorphism onto its open image. Its inverse theta_(q,j)
is smooth there. Restrict it to V_(O,q,j)=F_q(P_(O,q,j)); this target set
is Borel by the ambient homeomorphism. On these restricted domains,

    F_O(theta_(q,j)(w))=w,
    theta_(q,j)(F_O(z))=z       for z in P_(O,q,j).

Both inverse identities are actual-owner identities, not just solutions
of a formal fixed-label equation. All real roots are included because
every regular legal source belongs to one P. A source cannot be duplicated
by another label because its actual law fixes one q, nor by another ball
after the first-eligible assignment. Distinct sources remain distinct
inverse branches even when they have the same target. Fibres are at most
countable through this atlas, but no finite-fibre theorem is asserted.

For Q there is an explicit complete inverse:

    theta_Q(s,t)=(log t,log s),       s>0, t>0,

retained exactly when B=floor(log s)!=0 divides 1-floor(log t). There is
no other real inverse. The source label used in the permission test does
not create multiple copies of this inverse. The same local-ball mechanism
can also describe this restriction of the globally injective germ F_0.

## 3. Every-point inverse IMAGE and own clock

At any retained MAIN/G inverse source (u,v), the full inverse derivative is

    D theta = 1/(q²-exp(u+v)) * [[-q,-exp(v)],[-exp(u),-q]],
    J_theta(s,t) = 1/abs(q²-exp(u+v)).

Its value is finite and strictly positive by actual source regularity.
This formula assigns the ambient inverse-germ value at every retained
point, including floor faces and null pieces. For every Borel E contained
in the actual inverse domain V, ambient change of variables gives

    Leb(theta(E)) = integral_E J_theta(w) dw.

Restriction to a Borel piece does not remove null-point germ values or
silently replace them by an arbitrary a.e. version. The actual step clocks
are consequently

    kappa_MAIN/G(x,y)=log abs(q_O(x,y)²-exp(x+y)).

All signs, including zero, are retained; this is not an imposed positive
suspension roof. For Q,

    D theta_Q(s,t) = [[0,1/t],[1/s,0]],
    J_Q(s,t)=1/(s t),          kappa_Q(x,y)=x+y.

These use Q's own actual inverse domain and ordinary two-dimensional
Lebesgue measure. The same every-Borel identity follows directly. No
terminal source has a next-step clock; an inverse at a terminal target
still has the clock of its legal forward source.

## 4. Every history, complete arrows and all three kernels

For each owner separately, let Inv_O(w) be exactly the retained inverse
set above. Define Pre_0(S)=S and

    Pre_(n+1)(S) = union_(w in Pre_n(S)) Inv_O(w).

No depth or root is truncated. An infinite backward history means a
compatible sequence of these actual choices at every finite depth.
The whole source component of w is exactly

    union over all legal n>=0 and all m>=0 of Pre_m({F_O^n w}).

This includes all forward and incoming histories, terminal endpoints,
coalescence and possible eventual cores. It is an exact recursive owner
description, not a finite census or a classification of cycles outside
the authorized fixed cells.

Let S_n(z)=sum_(j=0)^(n-1) kappa(F_O^j z) for a legal n-step history,
with S_0=0. Keep the groupoid triples

    g=(z,m-n,w),       F_O^m z=F_O^n w legally,
    c(g)=S_m(z)-S_n(w).

If two witnesses represent the same triple, both indices change by the
same integer. The longer witness adds the same legal common-tail clock
to both sums, so c descends to the triple. For composition, extend the
shorter of the two middle histories to the longer one, using its already
legal common forward segment. The middle sums cancel. Thus c is additive,
inversion changes its sign, and the actual forward arrow (F_O z,-1,z)
has clock -kappa(z).

Without any unproved injectivity claim for MAIN or G, the complete kernels
are exactly

    ker lag = {(z,0,w): F_O^n z=F_O^n w for some legal n},
    ker c = {(z,m-n,w): F_O^m z=F_O^n w and S_m(z)=S_n(w)},
    ker(lag,c) = ker lag intersect ker c.

These retain all nonunit merging arrows and all cancellations allowed by
the actual clock. For Q, restriction of the injective F_0 is injective,
so ker lag and the joint kernel are units. A more explicit complete form
of Q's clock kernel is the units together with all arrows

    (z,n,F_Q^n z),    n>=1, all n actual steps legal, S_n(z)=0,

and their inverses. This follows by cancelling the common iterate in any
positive-lag witness; partial injectivity justifies that cancellation.
Here S_n is Q's own sum of the actual x_j+y_j. No unsupported simplification
of this clock kernel to units is made.

## 5. Entire stabilizers, source/extension isotropy and all phases

The extension uses the full R² x R and acts by

    (w,h) -> (z,h+c(z,k,w)).

Physical time is unrestricted height translation on its orbit SET. It is
not quotienting source coordinates, choosing a preferred packet or adding
an extra geometric measure direction.

For any source whose path is not eventually periodic, including terminating
paths, source isotropy is zero: a nonzero-lag loop would exhibit unequal
forward times with equal state and hence an actual eventual cycle. Suppose
instead its path reaches a least-ell cycle with signed sum C. Every source
loop has lag in ell Z, every such lag occurs by extending to the core, and
c maps r ell to r C. Thus on the full incoming component,

    source isotropy = ell Z,
    entire H = C Z,
    extension isotropy = ell Z if C=0, and {0} otherwise.

The equality for entire H follows because height translation by t preserves
an extension orbit if and only if some source isotropy arrow has clock t.
It is not merely a lower bound from one known loop. Non-eventual components
have H={0} and extension isotropy zero. For C!=0 the primitive is |C| and
its positive repetitions are r|C|, r>=1, not |C| divided by the source
period. A zero-clock cycle has no positive physical return.

For full cyclic-basin coordinates, choose a_0,...,a_(ell-1) on its core,
let K_j=S_j(a_0), K_0=0, K_ell=C. For any point z in the full incoming
basin choose its first-entry depth d_z and phase e_z, so F_O^d_z z=a_e_z.
Set l_z=d_z-e_z and b_z=S_d_z(z)-K_e_z. Then all its component arrows are

    (z,l_z-l_w+r ell,w),       c=b_z-b_w+r C,      r in Z.

Lag, clock and joint kernels are obtained by setting the respective lag,
clock, or both equal to zero. A complete extension phase is h-b_z mod C Z,
with quotient by {0} meaning the real value itself. This retains all phases
and arbitrary incoming entry clocks even for a zero-clock core.

For a terminating component with terminal t and actual terminal depth d_z,
the unique arrow from w to z has lag d_z-d_w and clock
S_d_z(z)-S_d_w(w). Its complete phase is h-S_d_z(z) in R. For an infinite
non-eventually-periodic component, choose one set-level reference a and its
unique arrow g_z:a->z; the phase is h-c(g_z) in R. Two different lags between
the same points would force an eventual cycle, so the reference clock is
unique. No measurable global selector or nice quotient topology is assumed.
These formulas are universal descriptions of the frozen owner's histories;
they do not assert or enumerate additional cores.

## 6. Exhaustive fixed gate in the four complete cells

Denote the frozen cells by

    C1=[-1,0) x [-1,0),
    C2=[-3,-2) x [2,3),
    C3=[-2,-1) x [2,3),
    C4=[0,1) x [0,1).

A fixed point for a fixed label must satisfy both equations

    exp(y)=(q+1)x,       exp(x)=(q+1)y,

and must independently be legal for the relevant actual owner.

### 6.1 Cell C1

Here A=B=-1, N=2. MAIN permission holds and its signed q=-2.
G also has remainder zero and q_G=-2. Q permission holds but its germ is F_0.

For MAIN/G the fixed equations are exp(y)=-x and exp(x)=-y. If x!=y,
the mean-value theorem yields

    abs(exp(x)-exp(y)) = exp(xi) abs(x-y) < abs(x-y),

because xi lies strictly below zero. The fixed equations would instead
make those absolute differences equal. Hence x=y=-alpha, where alpha is
the unique root of alpha=exp(-alpha) in (0,1). Existence follows from the
opposite signs of a-exp(-a) at 0 and 1; strict derivative 1+exp(-a)>0 gives
uniqueness. In particular the point is in the interior of C1, not a lost
floor-boundary point. Put p=(-alpha,-alpha).

At p, the actual derivative for MAIN and separately G is

    D F_(-2)(p) = [[2,alpha],[alpha,2]],
    delta_(-2)(p)=4-alpha² > 3.

Thus p is actually regular and fixed for both owners, not merely a formal
root. It has least source period one. Q has no fixed point in C1, because
its first fixed equation x=exp(y)>0 contradicts x<0; this uses Q's own germ,
whose regularity never fails.

### 6.2 Cell C2

A=-3, B=2, N=4. MAIN and G both use q=2, with MAIN arithmetic permission
true. Their first fixed equation exp(y)=3x is impossible because x<0.
This excludes every formal root, hence every actual fixed point, regardless
of any further regularity test. Q is arithmetically permitted here but its
first fixed equation x=exp(y)>0 is equally incompatible with the cell.

### 6.3 Cell C3

A=-2, B=2, N=3. MAIN and Q arithmetic permission fails because 2 does not
divide 3. Every point of this cell is terminal for those two owners, not
a fixed point. G has remainder 1 and q_G=1; its first fixed equation
exp(y)=2x is impossible for x<0. Thus G also has no actual fixed point here.

### 6.4 Cell C4

A=B=0, N=1. MAIN and Q fail the B!=0 permission, so the complete cell is
terminal for both. G uses q_G=0 and is regular everywhere in the cell.
A G fixed point would satisfy x=exp(y)>=1, contradicting x<1. No fixed
point exists, including on either included lower boundary.

### 6.5 Gate result, without enlarging the search

The complete four-cell fixed set is exactly {p} for MAIN, exactly {p} for G,
and empty for Q. All half-open boundaries have been covered by the exact
cell readouts and strict sign or range exclusions above. There is no
continuous fixed set in the frozen union. Nothing here classifies fixed
points in other cells or cycles of higher least period.

## 7. The unrestricted incoming basins of the found cores

The general inverse recursion already retains every incoming depth. In
this case one can additionally solve all predecessors of p exactly, for
MAIN and G separately, without a bounded source-cell restriction.

For any actual inverse root (u,v) of p with integer label q, the equations
give

    q u=exp(v)+alpha>0,       q v=exp(u)+alpha>0.

Thus q!=0 and u,v have the sign of q. Subtracting equations shows that,
if u!=v, q=-exp(xi) for a real xi strictly between u and v. For q>0 this
is impossible by sign. For q<0, both u and v are negative, so it would
give -1<q<0, impossible for an integer label. Therefore every inverse
root of p has u=v=s with the sign of q.

If q>0, let a=floor s>=0. If a=0, MAIN has B=0 and is illegal, while G's
actual label is 0, not q>0. If a>=1, N=1-a<=0 and B=a>0; MAIN's permitted
quotient cannot be positive, and G's (N-r)/B cannot be positive either.
Therefore no positive-label actual predecessor exists for either owner.

For q<0 put a=floor s=-m, m>=1. MAIN permission requires m divides m+1,
so m=1 and its only possible label is q=-2. On this whole diagonal source
cell, the equation is exp(s)+2s=-alpha. Its left-hand side is strictly
increasing, and s=-alpha is a solution. Hence MAIN has exactly the
predecessor p, already shown regular.

For G the actual signed remainder law gives q_G=-2 if m=1 and q_G=-1 if
m>=2. The m=1 case again yields only p. To rule out every m>=2 source,
first note the exact elementary bounds

    alpha < 3/5,       exp(-1) < 2/5.

For the first, exp(3/5)>1+3/5+(3/5)²/2=89/50>5/3, so exp(-3/5)<3/5;
strict monotonicity of a-exp(-a) places its root below 3/5. For the second,
exp(1)>1+1+1/2=5/2. These are exact inequalities, not numerical estimates.
If m>=2 then s<-1, and therefore

    exp(s)+s <= exp(-1)-1 < -3/5 < -alpha.

It cannot satisfy the q_G=-1 inverse equation exp(s)+s=-alpha. Thus G
also has exactly the predecessor p. This argument tested every real
inverse root with every integer q and every actual source readout; it
did not assume the predecessor was in one of the four search cells.

Consequently

    Inv_MAIN(p)={p},      Inv_G(p)={p},
    union_(n>=0) Pre_n({p})={p}     for each respective owner.

The full incoming basins really are singletons; no incoming branch from
another cell or terminal can alter their packet structure. This extra
incoming result concerns only the already found p, not other fixed points.
Q has no found core to which a positive-packet calculation could be attached.

## 8. Exact full packet, clocks, kernels, phases and primitive obstruction

Let D=4-alpha². For MAIN and independently for G, every base arrow on the
entire packet of p is

    (p,k,p),          k in Z,          c=k log D.

The source isotropy is Z, its entire clock image is H=(log D) Z, and the
lag, clock and joint kernels on this full packet consist only of its unit.
The extension has zero isotropy, acts on the full real fibre by h->h+k log D,
and has all phases h mod log D. Unrestricted height translation on these
extension orbits has exactly the stabilizer (log D) Z. The least positive
physical return is log D and all positive repetitions are n log D, n>=1.
This is a source-fixed core, not a longer source orbit whose period has
been divided by an assumed repetition count.

Since 0<alpha<1,

    3 < D < 4,          log 3 < log D < log 4.

There is no integer, hence no ordinary prime, strictly between 3 and 4.
The actual primitive log D is therefore not log of an ordinary prime.
No transcendence assertion or decimal root approximation is needed.
MAIN has an actual nonempty positive ledger containing this wrong primitive,
so its prime-only benchmark fails. This is sufficient for the frozen STOP
condition; no global periodic census or absence statement is required.

G supplies a separately derived negative control with the same coordinates
and clock, but its result is not transferred to MAIN. Each owner has one
found packet in the four-cell gate. No global packet multiplicity outside
that gate is asserted, and packets of different owners are not identified.
Q's empty four-cell fixed set is only that bounded control result, not a
claim of an empty global positive ledger or a substitute success for MAIN.

## 9. Conclusion and preserved limits

The full same-object atlas, IMAGE clock, history groupoid, kernels and
entire stabilizer/phase conventions are established by exact constructions.
The four-cell gate yields the single actual fixed core p for MAIN and G,
no Q fixed core, and the unrestricted incoming calculation gives singleton
basins for the two found cores. MAIN's primitive log(4-alpha²), alpha=exp(-alpha),
lies strictly between log 3 and log 4 and fails prime purity. Portfolio
decision: STOP this MAIN / FORK to a separately frozen architecture.

No other-cell fixed search, higher-period census, time rescaling, parameter
repair, quotient selection or imported clock was used. Other periodic
structure of these owners remains unclassified; the decisive negative
does not need it. Naturalness and PROVES_TOO_MUCH remain OPEN.
Classical NOT APPLICABLE; arithmetic T1 NOT PASSED; T3 NOT AUDITED;
formal UNASSIGNED; B NOT INVOKED. No arithmetic source or later Route credit
is inferred from the completed owner-level construction or the controls.

This pre-manuscript raw record will be frozen after full self-read. Later
corrections, if needed, must be explicit errata rather than rewrites after
manuscript exposure. Await root's full raw read and distinct PAPER UNLOCK.
