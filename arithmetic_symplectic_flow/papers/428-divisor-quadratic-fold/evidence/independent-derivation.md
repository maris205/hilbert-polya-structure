# Card-only raw derivation — Divisor quadratic fold

Candidate: `ANG-20260923-DQF01`; paper 428; date: 2026-09-23.
Batch: `SYMMETRY-FEEDBACK-20260923-P`, round 4/5 (425–429).
Reviewer: `/root/nonlocal_source_review`.
Root separately released mathematics after reporting full reading of CP1.
Scientific input: the entire frozen 99-line card, reread through its final line.
candidate-card.md SHA256 2e9f6f1bf43f2984aaf4d10f9a9be56c38b9414e0009ec15980387dd7347cfa0
scope-review.md — 113 lines — SHA256 1df34aadd577e9ef596ec7a5f51e674c95de36829ef3c99d0241227219f71371
Actual access: no 428 manuscript, README, ledger, Outcome, author/helper answer,
peer proof, sibling output or scout card was read. Older shared history remains.
AI-assisted, inherited-model internal review: NOT_CALIBRATED; no blind,
cross-model, human or external verification claim. Served identity not attested.
Exact derivation only; no scientific code, numeric census, literature/network,
Git, model change, PDF, operator or publication operation.

## 1. Own source rules, determinant and proper-divisor arrow

Write v=(x,y,z), A=floor x, B=floor y, C=floor z and N=A²+C.
All three owners retain the full X=R3 and their own Lebesgue3 measure.
MAIN legal sources satisfy B!=0, B divides N, q=N/B and Delta_q(v)!=0.
G assigns q_G=(N-r)/B for B!=0, 0<=r<abs(B), N-r divisible by abs(B);
for B=0 it assigns q_G=0. Its only further source test is Delta_(q_G)!=0.
In particular B<0 uses this signed quotient, not a positive-divisor quotient.
Q requires MAIN arithmetic permission but its map parameter is ALWAYS zero;
its further source test is Delta_0!=0, with no unused Delta_(N/B) test.
Each parameter is single-valued at its own legal source. The coordinate update
is simultaneous, and every arithmetic or critical failure remains terminal.

Direct differentiation of P_q=(yz-qx,zx-qy,xy-qz) gives

    DP_q = [ -q  z   y ]
           [  z -q   x ]
           [  y  x  -q ],
    Delta_q=det DP_q=-q³+q(x²+y²+z²)+2xyz.

The derivatives here belong to the assigned polynomial germ, not a falsely
differentiated global floor-dependent map. In particular Delta_0=2xyz.
At any legal source, the inverse germ has Jacobian determinant reciprocal
to Delta_q. Its prescribed IMAGE version and own clock will therefore be
J(Tv)=1/abs(Delta_q(v)) and kappa(v)=log abs(Delta_q(v)); Section 2 proves IMAGE.
No one-step clock is defined at a terminal object. Its identity has clock zero,
which does not create a zero-clock outgoing dynamics step or an absorbing loop.

On a complete proper-divisor cell (A,B,C)=(0,d,n), with n>=2 and 1<d<n,
N=n, so MAIN arithmetic permission is EXACTLY d divides n. If it holds,
q=n/d>0, x>=0, y>=d, z>=n and q<n. Consequently

    Delta_q >= q(d²+n²-q²) > 0.

Thus regularity on this particular permitted family follows by an additional
positive bound; it was not silently equated with divisibility. If d does not
divide n the arithmetic source gate fails. The feedback q enters every actual
output coordinate and changes the next floors. This proves the stated local
lineage mechanism, not prime recurrence or a natural conservative lift.

## 2. Complete countable atlas and own all-point IMAGE

For each integer q let E_(O,q) be the Borel set of legal sources of owner O
whose ACTUAL polynomial is P_q. For Q only E_(Q,0) is used; its arithmetic
quotient does not create additional polynomial labels or repeated branches.
These sets are Borel by the floor-cell rules and polynomial inequalities.
Let (U_m) be the frozen rational-ball enumeration. For fixed q call m eligible
when P_q is injective and nonsingular everywhere on U_m, as the card specifies.
Eligibility is a mathematical condition; no effective decision algorithm is
asserted. Every v with Delta_q(v)!=0 has an inverse-function neighborhood
where P_q is injective and nonsingular. A rational ball containing v and lying
inside that neighborhood exists, so the eligible balls cover every regular v.
Use the disjoint assigned sources

    B_(O,q,m)=E_(O,q) intersect
       (U_m minus union_{j<m, j eligible for q} U_j),  m eligible.

They partition the entire legal domain of O. Different q cannot duplicate an
actual source because its own parameter is unique; the first-ball rule removes
chart overlap for a fixed q. Empty assigned sets contribute no actual branch.
On an eligible ball P_q:U_m->V_m=P_q(U_m) is a smooth diffeomorphism:
local inverses exist at every point and agree by injectivity; V_m is open.
Its smooth inverse theta_(q,m) sends the Borel subset
Y_(O,q,m)=P_q(B_(O,q,m)) back to B_(O,q,m).
Y is Borel because it is theta_(q,m)^{-1}(B_(O,q,m)) inside the open V_m.
Restriction therefore gives actual Borel inverse domains, including assigned
floor faces. Neither branch domains nor targets are assumed open or legal
for a next step. Their ambient polynomial inverse germs supply the derivative.

For EVERY Borel F subset Y_(O,q,m), the usual diffeomorphism change of variables
on V_m, restricted to F, gives

    mu(theta_(q,m) F)=integral_F abs(det Dtheta_(q,m)(u)) dmu(u),
    J_(O,q,m)(u)=1/abs(Delta_q(theta_(q,m)u)).

This value is positive finite at every actual target and on every included
face; no a.e. choice is made at a periodic null stratum. If two eligible
charts surround the same source, their inverse derivative at that source is
the same inverse matrix, though the first-ball rule still assigns ownership.
The complete source partition retains every actual root exactly once.
For multiple roots over one target, these are DIFFERENT inverse branches;
their densities are not replaced by a total-preimage density or one favored root.

## 3. Explicit exhaustive inverse-root recipe

The atlas is supplemented here by algebraic root descriptions, so that full
incoming sets below are not a finite selection of local sheets. Write the
target u=(u_1,u_2,u_3). For each fixed q!=0 set x=t.
If t²!=q², the last two target equations give uniquely

    y=(q u_2+t u_3)/(t²-q²),
    z=(t u_2+q u_3)/(t²-q²).

The first target equation holds EXACTLY when

    (q u_2+t u_3)(t u_2+q u_3)
      -(u_1+q t)(t²-q²)² = 0.                         (I)

Take EVERY real root of this polynomial with t²!=q². It has nonzero
degree-five leading coefficient -q, so it is not identically zero.
No extraneous denominator root is accepted; substitute the displayed y,z.
The exceptional alternatives t=sigma q, sigma=+1 or -1, are treated separately.
They require u_3=-sigma u_2 and have exactly the roots

    y²+(u_2/q)y-q²-sigma u_1=0,
    z=sigma(y+u_2/q), x=sigma q.                     (II)

This follows from -q y+sigma q z=u_2 and yz-qx=u_1, and also suffices for
all three target equations. Take all real quadratic roots, counting a repeated
root once as a point. Cases (I) and (II) exhaust all real roots for q!=0.
Afterwards reject Delta_q=0 sources because T is undefined there, NOT because
the corresponding source object has been removed from X.

For q=0, every regular source has xyz!=0 and hence all target coordinates
are nonzero, with u_1 u_2 u_3=(xyz)²>0. Conversely under those conditions
the complete regular inverse set is exactly TWO roots

    x= +/- sqrt(u_2 u_3/u_1), y=u_3/x, z=u_2/x.     (III)

These satisfy all equations and have nonzero determinant. If a target coordinate
is zero or the product is negative, there are no regular P_0 preimages.
Any algebraic P_0 root over a target of product zero has xyz=0 and is critical;
all such roots are therefore excluded as outgoing sources by the frozen rule.
This disposes of any critical continuous inverse fiber without deleting its
points as terminal objects. Formula (III) never privileges one sign.

Define the explicit actual inverse operator I_O(u) as follows:
for MAIN/G, take all integers q and every real root in (I)–(III), then retain
only roots satisfying their reconstructed OWN floors, source rule, parameter
equality and Delta_q!=0. For Q take only (III), then its arithmetic permission;
Delta_0 regularity is already imposed. Do not re-enumerate Q through N/B.
This recipe is exact even for targets which are themselves terminal objects.
It specifies mathematical real root sets, not a numerical solver or an
effective infinite-q search. Finite regular fibers for each q give at most
countably many actual predecessors in MAIN/G; no global truncation is used.

For any target subset A define I_O(A)=union_{u in A} I_O(u), I_O^0(A)=A.
Then I_O^n({u}) consists EXACTLY of every legal n-step predecessor of u,
by induction using the own source test at every step. All intermediate floor
changes, quotient changes, signs and critical/terminal exclusions are enforced.
Every such inverse history belongs to its unique actual chart word; none is
lost by the chart partition. These formulas will be used without restricting
inverse roots to the four fixed-point discovery cells.

## 4. Full partial-map groupoid, kernels and physical phases

For each O let D_n be the legal n-step source domain, D_0=X, and let S_n be
the sum of its own log abs(Delta) along those n steps. S_0=0 on ALL X.
The full actual groupoid consists of (z,m-n,w) with z in D_m,w in D_n and
T^m z=T^n w; equal triples are identified. Inverses exchange endpoints and
negate lag. For composition align the two middle orbit prefixes at their
larger depth. The longer given legal prefix supplies the needed continuation
of the shorter one through the same actual point; no arbitrary padding beyond
a terminal point is used. This proves closure for this PARTIAL map.
For two witnesses of one triple, the larger pair differs by equal extra
depths. Those depths are legal because that witness already exists; the
additional clock sums begin at the same meeting point and cancel.
Thus c=S_m(z)-S_n(w) is well defined. The same aligned-prefix argument proves
additivity; inverses negate c. The forward arrow (Tz,-1,z) has -kappa(z).

The complete kernels, with legal witnesses understood, are

    K_lag={(z,0,w):T^n z=T^n w for some legal n};
    K_clock={(z,m-n,w):T^m z=T^n w, S_m(z)=S_n(w)};
    K_joint={(z,0,w):T^n z=T^n w, S_n(z)=S_n(w)}.

These retain nonunit coalescences. In general neither K_clock=K_lag nor
triviality of any full kernel follows from trivial extension isotropy.
All heights and arrows (w,h)->(z,h+c) are retained, with real height translation.

A nonzero source loop exists iff the source has an eventual periodic tail.
For eventual least source period r and signed cycle sum C, source isotropy
is r Z, clocks of these loops are nC, and the ENTIRE H is C Z.
Necessity comes from a legal repeated orbit segment; sufficiency uses the
indefinitely repeatable legal cycle, with its incoming prefix canceled.
Extension isotropy at every height is trivial if C!=0, and the entire r Z
if C=0. A source without a periodic tail has source/extension isotropy and H
equal to zero, including every terminal source object.

On ANY source component choose reference u_* and actual arrows
g_z=(z,l_z,u_*) FROM u_* TO z, and put b_z=c(g_z).
All arrows w->z are g_z u g_w^{-1}, for u in reference source isotropy.
If it is r Z, all lags/clocks are respectively
l_z-l_w+n r and b_z-b_w+n C, n in Z. If it is trivial, there is one triple
between every two sources, with the two differences alone.
This gives complete componentwise kernel tests by setting lag, clock or both
to zero. The FULL phase is [h-b_z] in R/H, with height translation by t.
For C!=0 this is one physical circle, primitive abs(C), repeats j abs(C),
j>=1. For H=0 it is a free real line, even when ineffective source isotropy
survives at C=0. No global Borel reference selector or quotient manifold is
asserted, and equal primitive values never identify different components.

For completeness, a terminating component has a unique terminal endpoint t.
Every source z in it has its finite terminal depth a_z and b_z=S_(a_z)(z).
It is EXACTLY union_{n>=0} I_O^n({t}); the unique triple w->z has lag
a_z-a_w and clock b_z-b_w. Its full phase is h-b_z in R; all kernels follow
from equal-depth/equal-clock tests. No source one-step clock at t is invented.
A nonterminating noneventual component also has trivial isotropy and the
unique-arrow/real-phase description above. Unexamined periodic components
have the general r,C formula, not an asserted enumeration or target verdict.

## 5. Exhaustive polynomial fixed equations and the four full cells

For a polynomial P_q, put a=q+1. Its fixed equations are

    yz=a x, zx=a y, xy=a z.                         (F)

If a!=0, any zero coordinate forces all three to vanish. If all are nonzero,
dividing these equations gives x²=y²=z²=a². Precisely the four nonzero
solutions are v=a(e_1,e_2,e_3), e_i in {+1,-1}, e_1e_2e_3=1.
If a=0, equations (F) describe the union of the three coordinate axes.
These are algebraic lemmas BEFORE floor/permission/regularity tests, not an
enumeration of actual fixed points in unexamined source cells.
At a nonzero polynomial fixed point the determinant simplifies to

    Delta_q=-q³+3q(q+1)²+2(q+1)³=(q+2)(2q+1)².

The four discovery cells all have nonzero coordinates; hence no axis family
is hidden in their half-open faces. Their exact readouts and selected germs are

| Full cell (A,B,C) | N | MAIN permission | MAIN/G q | Q map parameter |
| --- | --- | --- | --- | --- |
| (1,1,1) | 2 | yes | 2 | 0 |
| (-1,1,-1) | 0 | yes | 0 | 0 |
| (2,2,2) | 6 | yes | 3 | 0 |
| (-2,2,-2) | 2 | yes | 1 | 0 |

For G these same parameters follow from remainder zero, not from imposing
MAIN permission. This equality is restricted to these four complete cells;
MAIN and G remain distinct owners on the full carrier and in their histories.
The polynomial classification now gives ALL actual fixed sets in the window:

| Cell | MAIN | G | Q |
| --- | --- | --- | --- |
| (1,1,1) | empty | empty | p_+=(1,1,1) |
| (-1,1,-1) | p_-=(-1,1,-1) | p_- | p_- |
| (2,2,2) | empty | empty | empty |
| (-2,2,-2) | p_2=(-2,2,-2) | p_2 | empty |

Indeed q=2 requires absolute coordinates 3, excluded from the first cell;
q=3 requires absolute coordinates 4, excluded from the third. q=0 requires
absolute coordinates 1, giving exactly p_- in the second cell and p_+ in
the first for Q. In the fourth cell q=1 requires absolute coordinates 2,
giving exactly p_2, whereas Q's absolute-1 roots are outside; in particular
-1 is an excluded upper face of [-2,-1). All displayed cores are included
lower-face points, NOT interior approximations. There is no continuous fixed
family in any of these cells, because the exhaustive algebraic list has none.

The regularity tests are separate and owner-specific. On the first cell
Delta_2=-8+2(x²+y²+z²)+2xyz>=0, with equality only at p_+; thus p_+ is a
MAIN/G CRITICAL TERMINAL object, not a fixed point of either actual map.
For Q it has Delta_0=2 and is a legal fixed point. Copying the unused
Delta_2 test into Q would wrongly erase this core and its uniqueness failure.
On the second cell Delta_0=2xyz>0. On the third cell Delta_3>=25>0.
On the fourth cell Delta_1=-1+x²+y²+z²+2xyz>0 since x,z in [-2,-1),
y in [2,3); at p_2 it equals 27. Q has Delta_0>0 throughout all four
cells, since each sign pattern has positive xyz. Thus no displayed fixed
root is silently lost to a critical surface, and no terminal root is admitted.

## 6. Complete MAIN and G incoming, isotropy and phases of both cores

This section applies SEPARATELY with O=MAIN and O=G, using the OWN inverse
operator of Section 3 in each occurrence. At p_- its map parameter is 0,
Delta=2 and c_-=log2. At p_2 its map parameter is 1, Delta=27 and c_2=log27.
Both are actual least-1 fixed cores of each respective owner.
For each p in {p_-,p_2}, its full source component/incoming basin is EXACTLY

    B_O(p)=union_{n>=0} I_O^n({p}).                 (B)

Here I_O is the explicit all-integer-q polynomial-root recipe (I)–(III)
with own reconstructed source tests, not an abstract selected inverse or
a four-cell truncation. Formula (B) retains all depths and all floor cells.
Every member reaches p; conversely an actual common tail with fixed p is p,
so every point in its full source component appears in (B). The two basins
are disjoint by deterministic forward evolution. They cannot be merged by
a common numerical clock value or by reusing a root of another owner.
No equality of B_MAIN(p) and B_G(p), or their transient clocks, is claimed.

For z in B_O(p), let a_z be its LEAST hitting time of p and define

    b_z=S_(a_z)(z)=log product_{j=0}^{a_z-1}
                         abs(Delta_(q_O(T^jz))(T^jz)),
    beta_z=b_z-a_z c_p.

Empty products at p are 1. Every factor uses that owner's actual legal germ;
for Q the germ parameter would be zero, never the arithmetic quotient.
Every pair z,w in B_O(p) admits EVERY integer lag ell. To see this, choose
large m>=a_z,n>=a_w with m-n=ell; both iterates then equal the fixed p.
Conversely these are all triples on this component, and their clocks are

    c_O(z,ell,w)=beta_z-beta_w+ell c_p.             (C)

Indeed S_m(z)=b_z+(m-a_z)c_p once p is reached. Thus ALL incoming arrows,
not only the first-hit arrows, and both loop directions are included.
Source isotropy at every z is Z; its loop ell has clock ell c_p; ENTIRE
H_z=c_p Z. Extension isotropy is trivial because c_p is nonzero.
The full physical phase is [h-b_z]=[h-beta_z] modulo c_p Z.
It gives one primitive packet per basin, of least period c_p and all
repetitions j c_p. Incoming points are not additional closed packets.

The complete kernels on this basin are especially explicit:

    K_lag: all (z,0,w), z,w in B_O(p);
    K_clock: beta_z-beta_w+ell c_p=0;
    K_joint: (z,0,w) with beta_z=beta_w.

Equivalently, for rho_z=exp(b_z)/exp(c_p)^(a_z)>0 the clock-kernel equation
is rho_z/rho_w=exp(c_p)^(-ell); the joint-kernel equation is rho_z=rho_w.
These sets retain every nonunit equal-time merger; they are not replaced
by source isotropy alone. Changing hitting witnesses adds multiples of c_p
to b_z and corresponding source periods to lag, leaving the phase unchanged.

MAIN therefore has an actual primitive log27=log(3³) packet at p_2.
It is not an ordinary-prime logarithm and not a repetition of a smaller
primitive: the entire H is log27 Z, with NO log3 element. This SINGLE same-
owner core refutes MAIN's global prime-only necessary requirement. Nonemptiness
is established, but no full global periodic enumeration or prime coverage is
claimed. G has the same two window core times and its OWN log27 obstruction;
G is not used as a substitute for the MAIN counterexample.

## 7. Q's complete finite incoming basins and duplicate prime packets

At p_+ and p_- the selected map is P_0, Delta_0=2 and the own clock is log2.
For either p, formula (III) gives precisely the two real preimages p and -p.
Both are actual Q sources: p_+ has floors (1,1,1), N=2,B=1;
-p_+ has (-1,-1,-1), N=0,B=-1; p_- has (-1,1,-1), N=0,B=1;
-p_- has (1,-1,1), N=2,B=-1. All four satisfy Q's arithmetic permission.
At -p the determinant is -2, so its ABSOLUTE IMAGE factor is still 1/2
and its own clock is log2. A negative orientation is not a negative density.
Q(p)=p and Q(-p)=p. The product of the three coordinates of -p is -1,
whereas every real P_0 image has coordinate product (xyz)²>=0.
Thus -p has NO real P_0 preimage at all, not merely no permitted one.
It follows without an inverse-depth cutoff that

    B_Q(p_+)={p_+,-p_+},   B_Q(p_-)={p_-,-p_-}.

These two basins are disjoint, exhaustive for the two window cores, and
include their complete incoming from ALL R3, not just the selected cells.
This is an incoming calculation, not a new fixed-point census outside the
window. In each basin beta_z=0, and its entire groupoid is

    {(z,ell,w):z,w in {p,-p}, ell in Z}, c=ell log2.

The full lag, clock and joint kernels ALL equal the lag-zero pair groupoid
{(z,0,w):z,w in {p,-p}}, including the two nonunit coalescence arrows.
Source isotropy is Z at both points, ENTIRE H=log2 Z, extension isotropy is
trivial at every height, and the complete phase is [h] modulo log2.
Each basin supplies ONE primitive log2 circle and repeats j log2; -p does
not supply another packet. The TWO different fixed cores supply TWO distinct
prime-2 packets. Hence Q's prime uniqueness requirement FAILS on its own
full carrier. This does not assert global prime-only support for unexamined
Q cycles, nor transfer Q's source test, root multiplicity or verdict to MAIN.

## 8. Bounded gate and integrity disposition

The four-cell fixed classification is complete for MAIN/G/Q, including all
included/excluded faces and absence of fixed families. Each displayed core
has its full incoming from the unrestricted actual inverse atlas, with entire
H, all kernels, both isotropies, all height phases and repetition convention.
The full partial-map framework also retains every terminal, noneventual and
unexamined eventual component; its structural formulas are not a classification
of every unexamined cell or higher cycle. No enlarged fixed/high-period search
was used. MAIN already has a decisive actual log27 primitive obstruction.
Portfolio: STOP MAIN on same-owner prime-only failure; retain this negative
record and the separately scoped G/Q controls. No parameter/roof/root adjustment,
core deletion, clock division or label quotient repairs this frozen object.
All-prime coverage, strong naturalness, prime recurrence and conservative lift
remain unestablished; controls alone do not defeat the PROVES_TOO_MUCH concern.
The proper-divisor arrow is explicit, but arithmetic T1 is NOT PASSED.
Own inverse IMAGE/clock and bounded packet ledger are established; T3 NOT AUDITED;
classical NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED. No candidate admission.
Same-object ownership remains intact independently for MAIN, G and Q.
ARS supplied bounded evidence/claim discipline, not a venue/novelty judgment.
This raw is frozen before manuscript access; CP2/CP3 are NOT PERFORMED.
Root must personally read the whole raw before a separate PAPER UNLOCK.

EOF — card-only derivation complete; HOLD for manuscript unlock.
