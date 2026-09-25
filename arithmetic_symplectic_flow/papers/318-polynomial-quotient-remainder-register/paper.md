# Polynomial quotient/remainder registers: owned clock, no one/two-step returns

Paper ID: `318-polynomial-quotient-remainder-register`.
Candidate ID: `ANG-20260920-PQR01`. Date: 2026-09-20.
Status: `OWNED REGISTER CLOCK; ONE/TWO-STEP RETURNS ABSENT — STOP / FORK`.
Scope: exact broadened-owner results; higher periods OPEN / UNCLASSIFIED.
Classical A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED.

## Abstract

On the entire signed real plane, freeze a partial register update
obtained by dividing x*xi+y by floor(y)*xi+1 when the
nonzero floor(y) divides floor(x). The next state is the
actual constant remainder followed by the actual quotient. Every disallowed
state remains terminal, with every incoming history. We prove its complete
inverse/image and Lebesgue IMAGE, yielding the owned full-point clock
-log|floor(y)|. The partial map is injective, not onto. Exact
whole-plane equations exclude ALL one-step and two-step returns, including
negative cells, units and cuts. They do NOT exclude higher periods.
The full time image at any possible higher periodic core would be
log(N)Z, with N its actual integer branch-product; existence, prime
selectivity and multiplicity remain OPEN. The two changed-permission controls
share the short-return obstruction through their own owners. Removing the
divisor's constant term instead gives exactly the unit square [1,2)^2
as the complete two-step return locus, with no external finite tails;
a product identity proves its time groups vanish at ALL periods.
The bounded round stops/forks as inconclusive
for the positive prime-packet target, without a global no-cycle claim.

## 1. Identity, lineage and frozen input

| Field | This owner |
| --- | --- |
| Carrier / category | Y=R^2, ordinary Borel structure and Lebesgue area |
| Source | Partial actual polynomial quotient/remainder update below |
| Arithmetic | Current signed floor-divisibility permission; no prime table |
| Clock | Derived actual inverse IMAGE, specified on all retained points |
| Orbit convention | Full actual retained-lag groupoid and Y x R extension |
| Packet / repetition | Entire time subgroup; least positive generator if present |
| Controls | DIVISIBILITY-OFF, DIVISIBILITY-SHIFT, DIVISOR-CONSTANT-OFF |
| Classical base / roof / mapping torus | NOT APPLICABLE |
| Operator / trace / determinant | NOT SUPPLIED; no borrowed owner |

The [original card](candidate-card.md) was frozen before this proof.
Its first 164 lines have SHA-256
`ab764785594498f289f04c026d3ee38de66a1ba3a6585236f8fe41389d4ce099`.
The [317 frontier](../317-noncommutative-central-carry-flow/evidence/scout-record.md)
was read in full, 206 lines, SHA-256
`ee6989b090c666066d50efe511aa9f8be23112fd026053f382dfc7fc96059957`.
Definition-author access and subsequent review exposure are distinguished in
the [source record](evidence/scout-record.md) and [review](evidence/independent-review.md).

At an actual integer seed (n,d), n,d>=1, the step exists
iff d|n and its output is (d-n/d,n/d). Thus a
proper-divisor symbol 1<d<n is an actual permission and quotient, not
a label appended to an unrelated flow. The lineage arrow is current
divisor-symbolic admissibility -> real polynomial division -> new real registers
and a new current admissibility test. No time-dependent fitting schedule.
This declared deformation does not prove stronger naturalness: floor(y), the
constant 1, register order and reference area are design choices.
No conservative lift, Logistic/Henon conjugacy or canonical prime clock follows.

## 2. Complete partial source and exact inverse

For z=(x,y), set a=floor(x), b=floor(y). A step is legal
iff b!=0 and b|a. On every such half-open cell
U_ab=[a,a+1) x [b,b+1),

    x*xi+y = (x/b)*(b*xi+1)+(y-x/b),
    T(x,y)=(y-x/b,x/b).

The remainder is a constant polynomial, not an integer-division remainder
restricted to an interval. All other states are terminal, including the
whole strip 0<=y<1. T^0 exists everywhere; terminal states are
not given artificial self-loops. All units, negative cells, axes and cuts
remain. Every formula uses the floor of the actual current coordinate.

For each legal pair a,b the affine inverse and its full domain are

    I_b(s,t)=(b*t,s+t),
    V_ab={b<=s+t<b+1, a<=b*t<a+1}.

Substitution gives T(I_b(s,t))=(s,t) throughout V_ab; conversely
I_b(T(x,y))=(x,y) on U_ab and T(U_ab)=V_ab.
Thus there are no missing branches or extra domain points.

For an arbitrary target (s,t), put B=floor(s+t). The ENTIRE
predecessor ledger is exactly

    if B!=0 and B|floor(B*t): one predecessor (B*t,s+t);
    otherwise: no predecessor.

Indeed B is the only possible b, and floor(B*t) is the
only possible a. Therefore T is a Borel partial injection,
with exact image E={B!=0, B|floor(B*t)}. This is not
surjectivity: (0,0) has no predecessor. Lack of a predecessor
does not imply terminality: (1,-1) has B=0, hence no
incoming step, but its own b=-1 permits T(1,-1)=(0,-1).
These distinctions also retain targets on all integer cuts and axes.

## 3. Actual IMAGE and the full retained-lag clock

The inverse derivative and its absolute determinant are

    D I_b = [[0,b],[1,1]],     J_b=|b|>0.

The affine change of variables on any Borel E0 subset V_ab gives

    mu(I_b(E0)) = integral_(E0) |b| dmu.

This is an image-measure statement, not an assigned runtime or roof.
The same analytic branch determinant specifies the FULL-POINT value on
every retained cut/axis/null boundary, only on its actual domain. Area
alone determines an a.e. class, NOT unique null values; we explicitly
own this version and insert no atoms. At a legal source,

    kappa(z)=-log J_b(Tz)=-log|floor(y)|.

For an actual length-k history define D_k(z)=product_(0<=i<k)|b_i|,
where b_i is the current floor of the second register; D_0=1.
No factor is evaluated at a terminal state beyond its last legal step.
The inverse of that exact history has IMAGE D_k. A finite branch
pair from a w-history of length l to a z-history of length k,
with common future, has IMAGE D_k(z)/D_l(w) on its full actual
domain. Finite branch maps are affine there; arbitrary Borel subsets and
the prescribed all-point determinants obey the same multiplication rule.

Define only

    G={(z,k-l,w): T^k z=T^l w, k,l>=0, all steps legal},
    c(z,k-l,w)=-log D_k(z)+log D_l(w).

The inherited Borel structure in Y x Z x Y is used; this is
a countable union of Borel equal-future relations. Equal triples are one
arrow, not different history words. For two presentations of the same
triple, the two history lengths differ by the same integer. Extending
the shorter pair to the longer pair adds identical factors at their
common future, so c is independent of presentation. For composition,
extend the two histories of the shared middle object to their longer
length; matching future factors cancel. This proves the cocycle law
pointwise, also for length-zero terminal histories.

Keep every (z,h) in Y x R, with arrows
(w,h)->(z,h+c), and R-translation in h. The actual forward
step corresponds to (Tz,-1,z), with clock +log|b|; the
inverse arrow has clock -log|b|. No sign reversal is hidden in
the orbit convention. Only a Borel/set quotient is asserted; no smooth,
etale, Hausdorff or invariant-area-times-dh conclusion is needed or claimed.

## 4. ALL fixed and two-step returns

### 4.1 Fixed points: none

If a legal point were fixed, x/b=y from the second equation.
The first then gives x=y-y=0, hence y=0. But y=0
has b=0 and is terminal. Thus no full-state fixed point exists.
Terminal T^0 identities are not fixed points of a nonexistent T step.

### 4.2 Two-step returns: none

Suppose both steps exist and T^2(x,y)=(x,y). Let b=floor(y)
and q=x/b, d=floor(q); b,d are nonzero integers. Then

    T(x,y)=(y-q,q),
    T^2(x,y)=(q-(y-q)/d,(y-q)/d).

The return equations imply y=(y-q)/d, q=(1-d)*y and
x=q-y=-d*y. Since y!=0 whenever b!=0, combining x=b*q
gives b*(1-d)=-d, or

    (b-1)*(d-1)=1.

Its integer solutions are (b,d)=(2,2) or (0,0); the latter
is illegal. In the former q=-y, whereas floor(y)=floor(q)=2
would require BOTH y and -y in [2,3), a contradiction.
This exhaustive integer equation and exact half-open membership close the
whole-plane test; no positivity assumption, seed sampling or cell cutoff.
The divisibility filter was not needed in this contradiction, but all
actual permissions were retained. No primitive source period 1 or 2
exists; this is not a proof about periods 3 or above.

## 5. Complete packet rule and the unresolved higher-period gate

An injective partial map has no nontrivial finite tails entering a
cycle. To prove this, a cycle point already has its cycle predecessor;
uniqueness of the actual predecessor forces any incoming predecessor to
be that point. Iterate backwards along any proposed finite incoming tail.
Consequently every eventually periodic state is already periodic, and the
full actual-tail equivalence class of a periodic core is exactly its
finite cycle, without omitted incoming states. This applies to this owner
and to each separately proved injective control below.

Conditionally, let a state belong to an actual least-period-P cycle,
and let N be the product of |b_i| around the entire cycle.
N is a positive integer, and the COMPLETE groups are

| Case | Source isotropy | Entire time image H | Extension kernel |
| --- | --- | --- | --- |
| N=1 | PZ | {0} | PZ |
| N>=2 | PZ | (log N)Z | {0} |
| Nonperiodic state, including terminals | {0} | {0} | {0} |

For the cycle cases, c(z,rP,z)=-r*log N. This proves the
least positive primitive is log N when N>=2, not an
arbitrarily selected larger return. Its positive repetitions r*log N are
of that same cycle packet. For a chosen core z_0 and
z_j=T^j z_0, set S_j=sum_(0<=i<j)kappa(z_i). The arrow
z_0 -> z_j has clock -S_j, so the full extension packet
coordinate is h+S_j modulo log N if N>=2, and h
when N=1 (every factor is then a unit). Distinct cycles are
distinct packets even if their N or times agree. No root-fibre
representative or measure-zero deletion replaces this full identity.

This conditional result is not existence evidence. It does not establish
a prime-only ledger, exclude composite N, or prove an arbitrary integer
product can occur. Main positive higher-cycle existence, complete higher-cycle
classification and their multiplicities remain OPEN / UNCLASSIFIED. The
short-return test yielded no positive packet; a positive prime-packet target
is NOT established, but neither globally refuted by that test. Stop this
bounded round and fork rather than extending an unplanned period census.

For completeness, terminal histories are also retained exactly. A terminal
anchor omega has its full basin consisting of every legal iterate of
its unique partial inverse. For a basin state z, let d_z be
its stopping depth and S_z its kappa sum to omega. Between two
basin states the only lag is d_z-d_w, with c=S_z-S_w;
the full extension coordinate is h-S_z. All three isotropy groups
are zero. Different terminal anchors never merge. This uses no nonexistent
terminal step and inserts no absorbing loop.

## 6. Controls: their OWN domains, clocks and returns

### 6.1 DIVISIBILITY-OFF

The legal source now requires only b=floor(y)!=0. Its own update
is (y-x/b,x/b); its own inverse is I_b(s,t)=(b*t,s+t)
on b<=s+t<b+1, without an integer-divisibility filter. Thus its
exact image is {floor(s+t)!=0}, and each image point has
exactly one predecessor. Its own derivative is [[0,b],[1,1]],
IMAGE |b| and kappa=-log|b|, including its own actual cuts.
The finite-composition and cocycle proof uses these domains, not main
permission. It is a different partial injection. The equations in Section
4 use only b,d!=0 and current floor membership, so prove ALL
its one/two-step returns absent as well. Its higher cycles remain OPEN;
if one exists, its own N and groups obey Section 5, not a
borrowed main orbit. Removing divisibility does not resolve the short-return gate.

### 6.2 DIVISIBILITY-SHIFT

The source permission is b!=0 and b|(floor(x)+1). For a
target put B=floor(s+t). Its exact image is

    E_shift={B!=0, B|(floor(B*t)+1)}.

Every such target has exactly one predecessor (B*t,s+t), and
no other target has one. These are its OWN inverse domains;
substitution verifies its changed permission. The inverse derivative again
gives its own IMAGE |B| and legal-source kappa=-log|b|,
with its analytic full-point version. Section 4's permission-independent algebra
proves ALL its one/two-step returns absent. It retains all terminal and
incoming histories and the same general injective-packet proof. Its higher
periods, positive existence and multiplicities remain OPEN, not main evidence.

### 6.3 DIVISOR-CONSTANT-OFF

Here the divisor is b*xi, the remainder is y and the quotient
x/b. Main permission b!=0, b|floor(x) is retained, but
the OWN source is T_0(x,y)=(y,x/b), with OWN inverse

    I_b^0(s,t)=(b*t,s),
    W_b={b<=s<b+1, b!=0, b|floor(b*t)}.

Put B=floor(s). The exact image is {B!=0, B|floor(B*t)},
with exactly one predecessor (B*t,s) at each image point.
No other b can be its source floor. Direct substitution proves both
inverse identities. Its own derivative [[0,b],[1,0]] gives IMAGE
|b| and kappa_0=-log|b| on the whole actual branch. This
is not removal of unit-integer states. Finite branch pairs and all-point
clock consistency follow exactly by its own affine composition.

For a fixed point, x=y=t and t/b=t. Since b!=0
implies t!=0 here, b=1; conversely every t in [1,2)
is legal and fixed. Hence the FULL fixed locus is precisely

    {(t,t):1<=t<2}.

For any two-step return let b=floor(y), d=floor(x/b) be
the nonzero legal divisors. The second iterate is (x/b,y/d).
Its equality to (x,y) and y!=0 force d=1; then
x/b in [1,2), so x!=0 and x/b=x forces b=1.
Thus both x,y lie in [1,2). Conversely on the entire
square Q=[1,2)^2 the main permission holds and T_0 swaps
the registers, so the full two-step return locus is EXACTLY Q.
The included lower and excluded upper edges use the original floor rule.

Every diagonal point in Q has least source period 1; every
off-diagonal pair (x,y),(y,x) has least source period 2.
Both own branch factors are 1. The entire H is {0}; source
and extension isotropy are Z or 2Z respectively. Unique inverse
ownership proves there are no external finite tails entering Q. Full
packets are exactly the unordered register pairs with the same real h;
the diagonal singleton convention is retained. There are continuum many such
zero-time packets, not positive closed time orbits. No equal-time label
collapses them, and no control packet transfers to the main source.
Cycles outside Q must have period >=3; their complete source
classification is UNCLASSIFIED. In fact the retained unit-boundary states give
the exact period-three cycle (1,-1)->(-1,-1)->(-1,1)->(1,-1),
with b=-1,-1,1 and legal permissions at all three distinct points.
This single boundary check is not a higher-period census. Their TIME
groups can nevertheless be decided globally by the following short identity.
At any actual cycle all x_i,y_i are nonzero, since y_i has
nonzero floor and x_i/b_i=y_(i+1). At every step of that cycle,

    |x_(i+1)*y_(i+1)|=|x_i*y_i|/|b_i|.

Multiplication over the whole cycle gives N=product |b_i|=1.
Hence EVERY actual periodic core of this control has H={0}
and extension kernel equal to its source isotropy. Nonperiodic points
have all isotropy groups zero. Thus all its time groups vanish,
without classifying higher source cycles and without asserting its step clock
is globally zero or extending the logarithm of a zero product.
This all-period TIME result does not transfer to the main source.

## 7. Gate assessment, integrity and decision

| Audit | Result for ANG-20260920-PQR01 | Limitation |
| --- | --- | --- |
| T0 carrier / source / inverse | ESTABLISHED, full partial injection | No classical symplectic claim |
| T1 owned arithmetic / IMAGE clock | ESTABLISHED in the declared design | Stronger naturalness OPEN |
| T2 short-return discriminator | No source periods 1 or 2 | Higher periods and prime-packet target OPEN |
| T3 trace / zeta / operator | NOT SUPPLIED / NOT PURSUED | No borrowing from controls or prior work |
| Classical A0/A1/A2 | NOT APPLICABLE | Not formal coordinates |
| Formal Route / Route B | UNASSIGNED / NOT INVOKED | No Route evaluation |

Portfolio: STOP / FORK after the precommitted bounded gate, not a global
impossibility verdict. The same-object ledger remains intact: real polynomial
division, current permissions, full terminal carrier, actual inverse area, all
retained lags and complete discovered packets refer to this frozen source.
The changed-permission controls expose a permission-independent short-return
obstruction; the divisor-constant control has globally zero return times rather
than supplying a positive main orbit. The PROVES_TOO_MUCH risk of a
non-prime/composite higher packet remains unresolved, not waived.

Proofs are exact and elementary; no scientific numerics, cutoff, sampling,
external reference, prime data or zero data were used. This is not
a complete all-period source classification, external peer review, independence certificate, RH result
or Hilbert--Polya construction. ARS original-card/synthesis/final-adverse checkpoints
and their actual access order are recorded separately. Shared-model/history
review is NOT_CALIBRATED. No PDF/LaTeX, upload, publication or Git commit.

Evidence: [card](candidate-card.md), [ledger](claim-ledger.md),
[reproduction/locks](evidence/README.md), [review](evidence/independent-review.md),
[source/frontier](evidence/scout-record.md), [package index](README.md).
Positive 304 and all older packages remain unchanged; 241/242 paused;
programme goal active. Any next definition requires a separate freeze and
fresh owner audit; no status, clock or theorem transfers automatically.
