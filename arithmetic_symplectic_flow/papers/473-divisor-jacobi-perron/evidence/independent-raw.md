# DJP01 — independent card-bound raw derivation

Candidate: ANG-20260925-DJP01. Paper473, Batch Y round4/5.
Reviewer: `/root/rcr01_independent_review`, 2026-09-25 UTC.
Stage: DISTINCT RAW RELEASE; no current manuscript exposure.

## 0. Input and scope receipt

The scientific input is candidate-card.md93 lines, FULL read again at
1–93/EOF in this RAW stage, frozen SHA-256
`3d20f511c63b244d324f87c20e7cf9bc4f68d541d3bca291ca65df64d6b6b7f0`.
Root reported FULL reading scope152/EOF, SHA
`5f37603429c6c68aab44a201f5e7b7652cb88af46f4c5afc2af499e35d6f57c8`,
and then issued DISTINCT RAW RELEASE. Applicable ARS/local instructions
were personally refreshed at this473 CP1; the same bounded original-maths
adaptation continues. This file alone is writable at RAW stage.

Shared model/root/history and prior review tasks remain inherited, including
the earlier disclosed468 root-README-summary exposure. The present card
also discloses scout/root design exposures and informal feasibility before
freeze. NOT_CALIBRATED: not blind, human, external, cross-family, sealed,
or evidence of independent errors. No new current author/peer/helper/old
proof or outcome file was read. No scientific code/numerics, network, Git,
PDF or475 was used. All reasoning below is exact; no higher-period census
or change to the frozen measure, formula or permissions is made.

## 1. Actual digit cells, four domains and regularity

Let X=[0,1]^2 with original Lebesgue area. For x>0 define

    a=floor(1/x), b=floor(y/x),
    F(x,y)=(y/x-b,1/x-a).

Since 0<=y<=1 and x<=1, actual digits satisfy a>=1 and 0<=b<=a.
Define the disjoint Borel cells

    S_ab={z in X:x>0, a<=1/x<a+1, b<=y/x<b+1}.

Let the four allowed digit sets be

    Lambda_E={(a,b):a>=1,0<=b<=a},
    Lambda_P={(a,b):a>=3,2<=b<a},
    Lambda_M={(a,b) in Lambda_P:b divides a},
    Lambda_C={(a,b) in Lambda_P:b does not divide a}.

Each owner o has legal source E_o=union_{(a,b) in Lambda_o} S_ab and
T_o=F|E_o. Its terminal set is Z_o=X minus E_o. In particular Z_E is
exactly x=0; outer faces are not declared terminal indiscriminately.
The other owners retain all their illegal digit cells as terminal objects,
with units and every actual incoming arrow. None is removed or reset.

On the assigned smooth cell germ the digits are constants. Directly,

    DF=[[-y/x^2,1/x],[-1/x^2,0]],
    det DF=1/x^3>0.                               (1)

Thus the entire frozen permission domain of EVERY owner is regular; no
additional guard is inserted. The germ is smooth on ambient x>0, including
sources on x=1,y=0,y=1 or floor faces when their permission allows them.
Equation(1) does not assert differentiability of the floor functions.

Every legal image has both coordinates in [0,1). Write W=[0,1)^2.
The boundary targets with u=1 or v=1 consequently have no predecessor,
even when such a target can itself depart for a particular owner.

## 2. Exact inverse domains, full boundaries and no duplicate sources

For integers a>=1,b>=0 the candidate inverse is

    theta_ab(u,v)=(1/(a+v),(b+u)/(a+v)).            (2)

Its reconstructed source has 1/x=a+v and y/x=b+u. Therefore the actual
floor tests hold exactly when 0<=u<1 and 0<=v<1. Within W, x is in(0,1]
automatically, and y is in[0,1] exactly when b+u<=a+v. This gives ALL actual
inverse target domains for an allowed pair:

    B_ab=W                         if 0<=b<a,
    B_aa={(u,v) in W:u<=v}          if b=a.         (3)

For b>a there is no domain, since b+u>=a+1>a+v. Disallowed pairs for
owner o have no branch for that owner. Thus all M/P/C branches have domain
W; E additionally retains every diagonal-digit triangular branch in (3).
The inequality u<=v is non-strict: its equality is the source face y=1.
The cuts u=0 and v=0 are also retained. Neither u=1 nor v=1 is admitted.

For each allowed pair, theta_ab maps B_ab bijectively onto S_ab. The
equalities above prove floor consistency, square membership and forward
equality. Conversely any genuine predecessor has its unique actual a,b,
is of the form (2), and obeys (3); hence no predecessor is missing.
If two proposed branches produce the same source at the same target,
that source's unique actual floors make both a and b equal. There are
therefore no duplicate actual predecessors. Overlapping target domains
represent genuinely different source points, not a multiplicity to erase.

All S_ab and B_ab are Borel. The formulas are inverse smooth maps on
the ambient half-planes x>0 and a+v>0, so their restrictions are Borel
isomorphisms. This also proves Borel images for every Borel source subset.
No requirement that the target satisfy its OWN next-step permission was
used; in particular targets with first coordinate0 may have incoming.

These formulas retain all boundary examples structurally: x=1 has a=1
and inverse cut v=0, y=0 has b=0,u=0, and y=1 has b=a,u=v. Their own
permissions decide whether they depart, not a deletion of their objects.

## 3. Every-point IMAGE and the original-area clock

The analytic inverse derivative in (2) is

    Dtheta_ab=[[0,-(a+v)^(-2)],
               [(a+v)^(-1),-(b+u)(a+v)^(-2)]].

Consequently its prescribed absolute determinant is

    J_ab(u,v)=(a+v)^(-3)>0, finite.                (4)

This is fixed at EVERY point of its actual domain, including the
triangular edge, zero cuts and all null source faces. The smooth inverse
germ is unambiguous for the unique assigned digit pair. Restricting the
ordinary change-of-variables formula for these ambient diffeomorphisms
to any Borel A contained in B_ab proves

    area(theta_ab(A))=integral_A (a+v)^(-3) du dv.  (5)

This is an every-Borel identity, not a rectangle check or merely an a.e.
version. Nonnegative weighted substitution follows by simple-function
approximation and monotone limits. For each of M/P/C/E, its own branches
and domains in (3) supply its own IMAGE; the shared formula is proved on
those domains rather than borrowed from a different measured object.

Only after (4)–(5), the actual legal-step clock is

    kappa_o(x,y)=-log J_actual(T_o(x,y))=-3 log x. (6)

It is finite and nonnegative on each E_o. Zero is retained exactly at
x=1 when that owner permits the source, which here can occur only for E.
All other legal steps have positive clock. No outgoing clock is assigned
on Z_o, and original area is never replaced by an invariant density.

## 4. Complete global classification of actual fixed states

A legal fixed state has x>0 and, since it is its own image, x<1,y<1.
The two fixed equations for its actual digits are

    y=x^2+bx, y=1/x-a.

Elimination gives

    f_ab(x)=x^3+b x^2+a x-1=0.                   (7)

For all integers a>=1,b>=0, f_ab is strictly increasing on x>=0 because
f'_ab(x)=3x^2+2bx+a>0. It has exactly one positive root alpha_ab, since
f_ab(0)=-1 and f_ab(1)=a+b>0. Actual square sources require b<=a, already
proved in Section1. For EVERY such pair the following exact evaluations
give all remaining consistency and boundary checks:

    f_ab(1/(a+1))
       =[1+b(a+1)-(a+1)^2]/(a+1)^3 <0,
    f_ab(1/a)=1/a^3+b/a^2>0.                     (8)

The numerator in the first line is largest at b=a, where it equals -a.
Thus

    1/(a+1)<alpha_ab<1/a,
    eta_ab=1/alpha_ab-a=alpha_ab^2+b alpha_ab
            lies strictly between0 and1.         (9)

Also eta_ab/alpha_ab=b+alpha_ab with 0<alpha_ab<1. Hence the actual
floors of p_ab=(alpha_ab,eta_ab) are exactly a,b, and (7) gives its forward
equality. These are regular by (1). Conversely every actual fixed point
must arise this way. No outer face or zero-coordinate fixed state remains:
(9) puts every fixed state strictly inside the square, and x=0 is illegal.

Therefore the entire fixed set of each owner is

    Fix(T_o)={p_ab:(a,b) in Lambda_o}.             (10)

There is precisely one state for each allowed pair. In particular:

| Owner | Exact global fixed digit set |
|---|---|
| M | a>=3, 2<=b<a, b divides a |
| P | a>=3, 2<=b<a |
| C | a>=3, 2<=b<a, b does not divide a |
| E | a>=1, 0<=b<=a |

The table is a proved infinite parameter classification, not a finite
digit census. Each set is countably infinite: M contains (2m,2) for m>=2,
C contains (2m+1,2) for m>=1, and P/E contain those subsets. The unrestricted
E fixed states with b=0 and b=a are included, not discarded as digit edges.

## 5. Every fixed clock, arithmetic type and multiplicity

Set beta_ab=1/alpha_ab. Equations(7)–(9) give

    beta_ab in(a,a+1),
    P_ab(t)=t^3-a t^2-b t-1, P_ab(beta_ab)=0,
    lambda_ab=kappa(p_ab)=3 log beta_ab>0.        (11)

This is the clock owned by (4)–(6), including all four controls, not an
inserted symbolic length. The primitive assertion will follow from
ENTIRE isotropy in Sections7–8, rather than only from a one-step value.

For EVERY fixed pair in (10), P_ab is irreducible over Q. A reducible
cubic over Q has a rational root; monicity and constant term -1 restrict
that root to +/-1. But P_ab(1)=-a-b!=0 and
P_ab(-1)=b-a-2<=-2, since b<=a. Thus beta_ab has degree3 over Q.
If beta_ab^3 were rational q, then the same root would satisfy

    a beta_ab^2+b beta_ab+1-q=0,

a nonzero quadratic because a>=1. That contradicts degree3. Therefore

    exp(lambda_ab)=beta_ab^3 is irrational.       (12)

In particular no fixed primitive in this family can be log of an ordinary
prime, or even log of a positive rational, once (11) is identified with
the full primitive below.

Distinct fixed digit pairs have distinct lambda. Indeed equal positive
lengths force the same beta, and subtracting the two monic cubic equations
gives

    (a-a')beta^2+(b-b')beta=0.

If a!=a' this makes beta rational, impossible; otherwise b=b'. Distinct
fixed cores also cannot lie in one source component, because their forward
orbits remain at different points and never meet. Thus within each owner
there is one fixed packet per listed pair, with multiplicity1 at every
fixed primitive. Equal-time packets from any unclassified higher periods
are not removed or assumed absent. Packets of different owners are never
pooled into MAIN multiplicity.

## 6. Full inverse recursion and every actual history

Fix one owner and use its own allowed pairs and B_ab throughout. Put
D_0=X, T^0=id. For n>=1 let

    D_n={z:T^j z in E_o for every 0<=j<n},
    S_n(z)=sum_{j<n} kappa(T^jz), S_0=0,
    R_n(z)=product_{j<n} x(T^jz), R_0=1.

All sets and functions are Borel on their stated domains, and
0<R_n<=1, S_n=-3 log R_n. Last-step arrival at a terminal is allowed;
the next step is not presumed legal. If n+m steps are legal,
S_{n+m}(z)=S_n(z)+S_m(T^n z).

For every target t in the full X define

    Pre_o(t)={theta_ab(t):(a,b) in Lambda_o,t in B_ab},
    Pre_o^0(t)={t},
    Pre_o^{n+1}(t)=union_{w in Pre_o^n(t)} Pre_o(w). (13)

Sections1–2 prove the exact one-step equality to actual predecessors.
Induction then proves, for EVERY n,

    Pre_o^n(t)={z in D_n:T^n z=t}.                (14)

There is no digit or depth cutoff. Equal points inside a set can be
deduplicated, but distinct witness depths and integer lags are retained.
All compatible infinite backward histories are exactly sequences
z_0=t,z_1,... with z_{j+1} in Pre_o(z_j). This describes them without
inferring infinite compatibility from a finite tree and without replacing
X by an inverse-limit object. The recursion includes all terminal targets,
permission-excluded cells, faces and unclassified infinite forward classes.

### Complete incoming to every fixed core

For each allowed fixed pair d=(a,b), its full incoming basin is

    B_{o,d}=union_{n>=0} Pre_o^n(p_d).             (15)

This is EXACTLY its source component: a common future with a fixed point
means eventual equality to that point. Conversely every such equality
supplies an arrow. No further point can be equivalent without entering
(15). Distinct d give disjoint basins.

For M/P/C this has an especially explicit all-word form. Every branch has
domain W and maps the interior (0,1)^2 into itself, since 2<=b<a.
Consequently EVERY finite word of allowed pairs is admissible over p_d,
and

    B_{o,d}={theta_{d_0}...theta_{d_{n-1}}(p_d):
             n>=0, all d_j in Lambda_o}.          (16)

For E the same formula is used with the exact intermediate restrictions
from (3): each b=a letter requires u<=v at its own target. Formula(13)
is an equivalent unrestricted exact recursion enforcing all these tests;
no diagonal-digit branch is omitted or automatically admitted. In both
forms all source coordinates, permissions and intermediate domains are
actual, not freely chosen abstract symbolic sequences.

Because theta_d(p_d)=p_d, words with extra terminal repetitions of d can
represent the same point at different depths. They are not extra packets,
but the additional depths still witness distinct lags when appropriate.
Equations(13)–(16) retain all compatible infinite incoming histories and
give complete full-X incoming for EVERY fixed pair, not just the later
decisive witness.

## 7. Own history-pair IMAGE, descent and full source structure

Refine D_n by all its actual length-n digit itineraries, including every
intermediate permission/domain restriction. Each piece is Borel and T^n
is injective there because all individual branches are. Its image and
inverse are Borel, by composition of the explicit restricted smooth
branches. For an inverse history theta with z=theta(t), the pointwise
product density is

    J_theta(t)=R_n(z)^3=exp(-S_n(z)).              (17)

Repeated nonnegative weighted substitution from (5) proves every-Borel
IMAGE with (17), not only rectangles or an a.e. product. The zero-step
branch is identity on all X with J=1, including terminals.

Take an r-step inverse theta_a and s-step inverse theta_b on a common
actual target domain. Write z=theta_a(t), w=theta_b(t). The actual Borel
history-pair map w->z has IMAGE density

    J_pair(w)=J_theta_a(t)/J_theta_b(t)
             =[R_r(z)/R_s(w)]^3
             =exp[-S_r(z)+S_s(w)].                (18)

Indeed weighted substitution through theta_b and then theta_a proves
area(pair(A))=integral_A J_pair(w) dw for EVERY Borel source subset A.
All formulas are assigned smooth-germ products at every actual point.

Define retained-lag G as in the card. If (r,s) and (r',s') witness the
same triple (z,k,w), then r'-r=s'-s. Order the witnesses so this common
difference is nonnegative. The longer legal witness supplies that many
steps from their shorter common image, adding the same clock sum on
both sides. Thus

    c(z,k,w)=S_r(z)-S_s(w)
            =3 log[R_s(w)/R_r(z)]                (19)

descends. No fictitious terminal continuation is used.
For composition, align the two middle depths to their maximum; the
existing longer middle history supplies the needed extension of the
shorter equality. The middle clock sums cancel, proving additivity and
adding lags. Inverse reverses both, and units have lag/clock0. The forward
arrow (Tz,-1,z) has c=-kappa(z), with source z and range Tz.

The full height extension has objects (z,h) in X times R and arrows
(w,h)->(z,h+c). All real translations commute with this extension and act
on its orbit SET, without assuming a regular quotient or a selected section.

### Exact global kernels and equivalence tests

Membership of (z,k,w) means that some r,s>=0 with r-s=k satisfy z in D_r,
w in D_s and T^r z=T^s w. All witnesses can be represented by (13)–(14).
On these actual triples the COMPLETE kernels are

    K_lag: k=0,
    K_clock: R_r(z)=R_s(w),
    K_joint: k=0 and R_r(z)=R_s(w).                (20)

These include nonisotropy branch mergers and are not asserted to be units.
Extension equivalence of (w,h_w),(z,h_z) means some such triple also has
h_z-h_w=c(z,k,w). A zero-clock E step at x=1 is retained by these tests;
positive eventual-core clocks below do not erase such nonloop arrows.

### Terminals, non-eventual classes and all possible eventual cores

For a terminal t, its component is union_n Pre_o^n(t). The unique remaining
depth d(z) and W(z)=S_{d(z)}(z) give its unique arrow w->z:
k=d(z)-d(w), c=W(z)-W(w). Necessity follows by equal remaining depths
from a common image; sufficiency follows by arriving at t. K_lag means
equal d, K_clock equal W, and K_joint both. Source/extension isotropy and
H vanish; all real extension phases h-W(z) remain.

In an infinite non-eventual component there is exactly one retained-lag
arrow from an anchor a to each z: two unequal lags would force equality
of unequal forward iterates and hence eventual periodicity. Write its
lag ell(z) and clock b(z). Every arrow w->z has k=ell(z)-ell(w),
c=b(z)-b(w), giving all three kernels by the corresponding equalities.
Source/extension isotropy and H are zero, with exact real phase h-b(z).
This anchor is a set-theoretic coordinate, not a global Borel selector.

For ANY actual eventual least-q core, let C be its own cycle clock sum.
The complete source isotropy at its points and all incoming points is qZ:
unequal-iterate equality forces a period divisible by q, and every q
multiple is witnessed after entry. Transient sums cancel to give

    c(lq)=lC, ENTIRE H=C Z.                       (21)

There is no nontrivial zero-clock isotropy for these frozen owners.
Every point on an actual source cycle is in the image W and is legal,
so its x lies strictly between0 and1 and every clock in (6) is positive.
Thus C>0. This structural observation does NOT locate or enumerate any
higher-period core. Terminal/non-eventual classes have no isotropy at all.
Accordingly extension isotropy is zero everywhere. The x=1 zero-clock
steps remain actual nonloop arrows, not discarded data.

Choose anchor arrows a->z with lag k_z and clock b_z on an eventual
component. Every arrow w->z is, for exactly one integer l,

    k=k_z-k_w+lq, c=b_z-b_w+lC.                   (22)

Equation(20), or (22) with k/c set to0, gives its entire incoming kernels.
Extension phases are exactly h-b_z modulo ENTIRE C Z: equality modulo
C Z supplies an isotropy adjustment and is sufficient, while every arrow
implies it. The height-translation stabilizer is exactly C Z, primitive C,
with every positive integer repetition and both integer signs in (21).
When H=0 the same anchor construction gives all real phases and no
positive return. No closure of H, chosen subgroup or added orbit is used.

These formulas describe all possible component types and exact tests on
the full X. They leave higher-period locations, multiplicities and extra
lengths unevaluated, as the fixed-only gate requires.

## 8. Entire fixed-basin kernels, phases, repeats and ledger

For EVERY owner o and allowed fixed pair d, put p=p_d, lambda=lambda_d,
and on its full basin (15) define

    n_z=min{n:T^n z=p}, W_z=S_{n_z}(z),
    b_z=W_z-n_z lambda.                           (23)

The minimum exists by (15). Every integer k supplies an actual arrow
w->z in this basin, with

    c(z,k,w)=b_z-b_w+k lambda.                    (24)

For existence use arrival witnesses r=n_z+i,s=n_w+j and choose i,j>=0
with i-j=k-n_z+n_w. All extra steps at p are legal. Conversely any common
image of two basin points can be advanced to p; cancelling that common
tail gives exactly (24). Thus no incoming history adds a hidden extra
isotropy generator or removes an allowed lag.

The complete fixed-basin kernels are

    K_lag={(z,0,w):z,w in B_{o,d}},
    K_clock={(z,k,w):b_z-b_w+k lambda=0},
    K_joint={(z,0,w):b_z=b_w}.                    (25)

Here lambda>0. The clock test requires (b_w-b_z)/lambda to be the integer
k; it is not an equality imposed only at the central point. At every
point of the basin source isotropy is Z, its ENTIRE clock image is
lambda Z, and extension isotropy is zero. Exact extension phases are

    [h-b_z] in R/(lambda Z),

equivalently [h-W_z], since n_z lambda is an integer multiple. All phases
remain. Their circle is ONE full translation packet, not one packet per
height representative. Its primitive is precisely lambda, and repeats
are m lambda for every positive integer m. Signed isotropy uses all
integer multiples. This proves that (11), not a smaller selected subgroup,
is the actual primitive used in (12).

Thus each owner's complete FIXED ledger is indexed by Lambda_o, with one
full packet B_{o,d} per pair, full incoming (13)–(16), kernels(25),
ENTIRE H=lambda_d Z, all phase representatives, and every repetition.
Section5 proves the fixed primitive lengths are pairwise distinct and
all have irrational exponentials. These statements cover all fixed
packets of M/P/C/E; they neither claim an empty higher-period ledger nor
drop any equal-time packets that such an unevaluated ledger might contain.

## 9. Frozen lexicographic witness and decision

Only AFTER the global classification above, select the least actual
MAIN pair in lexicographic order (a,b). For a=1,2 there is no integer
1<b<a. For a=3 the only candidate b=2 does not divide3. At a=4, b=2
does divide4 and is the first permissible b. Hence the selected pair is

    d_*=(4,2).

Its actual regular fixed state is

    p_*=(alpha,alpha^2+2alpha),
    alpha^3+2alpha^2+4alpha-1=0,
    1/5<alpha<1/4.

Let beta=1/alpha in(4,5). Then beta^3-4beta^2-2beta-1=0 and the
ENTIRE fixed-basin clock stabilizer is (3 log beta) Z. Its positive
primitive is3 log beta, with every repetition and the full basin from
(15)–(16). By the irreducibility argument (12), beta^3 is irrational;
therefore this primitive is not log of any ordinary prime. This is an
owned MAIN nonprime witness, not a control clock or a chosen step with
uncomputed full isotropy. All other fixed packets remain in Section8.

The card's necessary prime-only condition therefore FAILS for the frozen
MAIN owner, so the prescribed decision is STOP / FORK. Nothing in an
unexamined higher-period ledger can remove an already-owned nonprime
packet without changing the frozen object. No higher-period census is
needed or performed. Distinct controls are not pooled as MAIN duplicates.

The seed (1/(N+rho),(d+eta)/(N+rho)) has the stated actual digits because
1/x=N+rho and y/x=d+eta, with both fractions in the prescribed half-open
ranges. For1<d<N the point is in X. Thus divisor information genuinely
enters current permission and regenerated coordinates; it is not thereby
a prime-only arithmetic mechanism. Strong naturalness and PROVES_TOO_MUCH
remain separate open issues, not prerequisites for this decisive refutation.

Same-object ownership is intact for all four original-area partial maps,
their all-point inverse clocks and actual full histories. Arithmetic T1
NOT PASSED; classical NOT APPLICABLE; T3 NOT AUDITED; formal coordinates
UNASSIGNED; Route B NOT INVOKED. No measure change, formula tuning,
selected section, additional period gate or Paper475 is introduced.
This raw is to be FULL self-read and frozen before manuscript access;
comparison requires root FULL raw read and DISTINCT PAPER UNLOCK.
