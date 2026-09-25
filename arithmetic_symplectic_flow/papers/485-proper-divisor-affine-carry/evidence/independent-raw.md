# DAC01 — independently derived affine-carry owner and complete MAIN ledger

Candidate ANG-20260925-DAC01; Paper485; batch AB, round1/5.
Reviewer dpc01_independent_review. Environment date2026-09-25.
Result: OWNED AFFINE CARRY; ONE LOG2 PACKET — PRIME-COVERAGE STOP / FORK.
This file is a pre-manuscript derivation, not the later CP2/CP3 comparison.

## 0. Input, authorization and exposure

The sole new scientific input is the original candidate-card.md,88 lines,
FULL1–88 through EOF, SHA256
`ee3e019ee38939ce6188ffd91c6f9d7a530c9410cfdc86672c0dd5edecdf5d9d`.
The scope-only evidence/scope-review.md was frozen at92 lines, SHA256
`b68ac2b9abcdf042ae6ab9687b31e08a41a152c55b7ee1a09cb754191a606deb`.
Root reported a full scope read and issued a DISTINCT RAW RELEASE.
Current paper/README/ledger, author/helper/peer answers and old proofs have
not been read. Only this raw file is written at this stage.

ARS scope/derivation/comparison separation, adverse-control discipline and
explicit limitations are used under personally read/retained instructions.
Shared model, inherited design context and retained474/476/480 exposure
remain: NOT_CALIBRATED, not blind, external or error-independent review.
No scientific code, numerical sampling, network, Git mutation, PDF, old edit
or490 work is used. All calculations below are exact symbolic reasoning.
No source/clock theorem from another candidate is an input to this proof.

## 1. Constructing the actual Borel affine owner

Throughout, cell labels n are nonnegative integers, X=[0,infinity), and
I_n=[n,n+1). MAIN has one chart for each integer pair n,d with
1<d<n and d|n. Write n=dq, q>=2, and x=n+t with 0<=t<1. Then

`f_(n,d)(n+t)=2q+t/d`,
`f_(n,d)(I_n)=[2q,2q+1/d)`,
`f_(n,d)^(-1)(2q+s)=dq+d*s`, for `0<=s<1/d`.

The displayed intervals are half-open actual domains and images. Both
inverse identities hold on those entire intervals. In particular their
integer endpoints remain, and the excluded upper endpoint is not re-added.
There are countably many such chart/inverse pairs. Each label is a
positive-slope affine map with rational coefficients.

Here is a full construction that also applies separately to each control.
For a finite oriented word w in that owner's generators/inverses, let
g_w be its composed affine label. Its legal domain D_w is the intersection
of X with the inverse images of all successive chart domains under the
preceding partial compositions. Every such inverse image is a rational
half-open interval, so D_w is Borel, possibly empty. The empty word has
label id and domain X. For each rational affine label g put

`D_g = union { D_w : g_w=g }`,
`G = { (g,x) : x in D_g }`.

The union is countable; hence every D_g is Borel. The arrow has source x
and range g*x. Inverse words prove `(g,x)^(-1)=(g^(-1),g*x)` is retained;
legal concatenation proves composition `(h,g*x)(g,x)=(h*g,x)`.
Units are all `(id,x)`, including every no-outgoing object. Conversely every
retained arrow has a finite legal presentation by construction. This is
exactly the generated wide subgroupoid, not the full affine action.
Two words are identified precisely when their label g and source x agree.
Different labels fixing the same point are not identified. No word length
or preassigned integer lag is an additional arrow coordinate.

Use the ORIGINAL Lebesgue measure mu on X, which is sigma-finite and not
a probability. A label g(x)=a*x+b, a>0, scales interval lengths by a.
The interval identity extends to every Borel set by uniqueness of the
sigma-finite Borel measure; in particular, for every Borel E subset D_g,

`mu(g E)=a*mu(E)`.

This remains true for infinite measure and for E crossing any number of
cells. It follows from the actual global affine map, not from adding
overlapping word images. Its specified all-point IMAGE version is the
positive finite constant a, including at null singleton endpoints.
After this identity define `c(g,x)=-log a`. The affine label makes it
presentation-independent; slopes multiply, so c is additive and reverses
sign under inversion. No density change or external roof is used.

The same construction retains every finite incoming word. For an exact
description of all compatible paths, allow either orientation of each
listed generating chart and require membership in its actual domain at
each step. Every finite prefix is a word just used in D_g; conversely every
legal word occurs this way. Compatible infinite sequences, when considered,
do not create extra source objects, limit arrows or multiplicity copies.
No completion of the generated groupoid or limiting clock is adjoined.

## 2. Entire stabilizers, kernels and phases: general facts

On X times R the arrow is `(x,h)->(g*x,h-log a)`. Height translation
commutes with every arrow and therefore acts on the extension's orbit SET.
At x the source isotropy consists of actual labels fixing x. Its entire
clock image is `H_x={-log a : (g,x) in G_x^x}`. Indeed, translating height
by u fixes the class of `(x,h)` exactly when an isotropy arrow has c=u.
This proves the entire stabilizer statement, not merely a loop inclusion.

`ker c` consists of the actual translations: labels `g(x)=x+b` with
x in their actual D_g. An extension fixed-object isotropy arrow must have
a=1 and g*x=x, hence b=0. Thus extension fixed-object isotropy is the unit
group for ALL sources of all four owners in this file. Nontrivial source
isotropy is not silently quotiented away; its nonzero clock moves height.

For each base orbit choose an anchor and transport heights to it. Different
transport arrows differ by source isotropy, so the remaining phase set is
exactly R/H. Height translation is transitive on that set. Distinct base
orbits give distinct physical packets even if their H agree. When
H=L Z with L>0 the least positive primitive is L and repetitions are kL,
k>=1. H=0 gives a free real orbit. A dense H has no least positive element;
R/H is retained as a set of cosets, not collapsed using a topological closure.

## 3. First decisive MAIN gate: the full orbit and isotropy of x=4

Let C be the set of positive composite integers. At integer sources the
MAIN generators and inverses preserve integrality, because
`n=dq -> 2q` and `2q -> dq`. Every endpoint is in C. No generator or
inverse touches an integer outside C. Thus an integer orbit cannot acquire
a noninteger or a prime by a longer inverse composition.

Every even N>=4 maps to4 using d=N/2. For any odd composite n choose a
proper divisor d; its image 2n/d is even and at least4. Therefore the
ENTIRE integer orbit of4 is C, with all integers outside C isolated.
This proves the whole orbit, not just selected forward descendants.

For an integer edge from n to m=2n/d its slope is m/(2n). For an inverse
edge from n to m its slope is 2m/n. Consequently every finite path from
integer n to integer m has slope

`a=(m/n)*2^k`, with `k in Z`.

Here k is deduced from the slope and endpoints; it is not an added lag
label. In a loop at4, every possible slope is therefore a power of2.
The actual chart f_(4,2) fixes4 with slope1/2, and its inverse fixes4
with slope2. Their powers realize every power of2. Since an affine label
fixing4 is uniquely determined by its slope, the ENTIRE isotropy is

`G_4^4={ (x -> 4+2^k*(x-4),4) : k in Z }`,
`H_4=(log 2) Z`.

Extension fixed-object isotropy is trivial, and the positive primitive is
exactly log2. The orbit C gives ONE packet with this primitive, not one
packet per composite integer or per presentation. Conjugation along any
actual integer path preserves slope, so every n in C has the same entire
return-slope group, with labels `x -> n+2^k*(x-n)`.

## 4. Complete MAIN classification, including every noninteger

### 4.1 Necessity and sufficiency of the full arrow normal form

A generating MAIN edge sends `(n,t)` to `(m,t/d)`, m=2n/d. Its inverse
sends `(m,s)` to `(n,d*s)` on s<1/d. Thus along ANY finite legal path,
integer cell labels stay in C, fractions stay zero or stay strictly positive,
and from n+t to m+s the actual slope and endpoint obey

`a=(m/n)*2^k`, `s=a*t`, `k in Z`, `0<=s<1`,
`g(z)=m+a*(z-n)`.

Every point in a cell I_n with n not in C has only its unit: neither
orientation of a MAIN generator has any such point in its domain.

For sufficiency first construct a half-contraction on EVERY composite cell.
When n is even, f_(n,2) is `n+t -> n+t/2` on all I_n. When n is odd,
choose a proper divisor d and set m=2n/d. The legal composition

`f_(n,d)^(-1) o f_(m,2) o f_(n,d)`

sends `n+t -> n+t/2` on all I_n: before the last inverse, the fraction
is t/(2d)<1/d. Its inverse doubles the fraction on [n,n+1/2).
Therefore any dyadic rescaling within one cell is legal whenever its final
fraction is below1; expansion steps respect every strict upper boundary.

Fix n,m in C and one integer path between them. Write its slope as
a_0=(m/n)2^(k_0). The same finite word is legal for a sufficiently small
right neighborhood of n: a legal point in finitely many half-open domains
has a positive right margin at every step. Given t in[0,1) and a proposed
a=(m/n)2^k with s=a*t<1, first contract t by 2^(-N) at n until this path
is legal. Choose N also so N+k-k_0>=0. After following the path, expand
at m by 2^(N+k-k_0). The final fraction is s, so all expansion steps
remain legal. The total slope is exactly a and the total label is
m+a*(z-n). This realizes EVERY arrow of the displayed normal form.

It follows that the normal form is an exact characterization of ALL
generated arrows, including arbitrary inverse compositions and all incoming
labels. No word-length bound is used. It also covers t=0 and proves all
integer source/target slope possibilities directly.

### 4.2 All isotropy, the clock kernel and noninteger packets

For n in C and t>0, a return requires m=n and s=t, hence a=1 and k=0.
Its affine label is id. Thus EVERY noninteger source has trivial source
isotropy and H=0; the inactive cells have this property as well. There is
no hidden noninteger rational exception. This argument uses the entire
normal form, not almost-everywhere measure information.

On the active noninteger locus the actual fractional coordinate gives
the finite real potential `V(n+t)=log t`. Indeed

`c(n+t -> m+s)=-log a=log t-log s`.

The potential is not extended across t=0; those endpoints have the genuine
nonzero return clocks just computed. No endpoint is discarded to make
this potential global.

The exact full clock kernel is: all units, together with translations
`n+t -> m+t` for n,m in C and `m/n in 2^Z`, for every 0<=t<1.
Necessity follows by putting a=1 in the normal form; sufficiency was proved
above. Thus the clock kernel can contain off-diagonal arrows even though
every extension fixed-object isotropy group is trivial.

Two active noninteger sources n+t and m+s lie in the same base orbit
exactly when `(s/m)/(t/n)` is a power of2. Hence these orbits are classified
by the positive number t/n modulo multiplication by 2^Z. Each has exactly
one representative `4+eta` with `1/2<=eta<1`: choose the unique dyadic
rescaling of 4t/n in that half-open interval and apply the normal form.
Every orbit has a free real phase, explicitly `h+log t`. No rational
fraction, equal phase value or shared numerical time identifies distinct
base orbits. Inactive-cell points each remain their own base orbit with
free height h.

For the composite integer orbit an arrow n->m has
`c=log n-log m-k log2`. Its phase is therefore
`h+log n mod (log2) Z`. Every height/phase is retained. All nontrivial
source isotropy and all repetitions are the powers already classified.

### 4.3 MAIN full ledger and the target decision

The complete MAIN physical ledger consists of:

- ONE closed physical packet from the entire composite-integer orbit C,
  with primitive log2 and repetitions k log2;
- a free real physical orbit for each active noninteger dyadic class;
- a free real physical orbit for every inactive-cell point.

There are no other source types. The target fails COVERAGE for every odd
prime. It is not rescued by the occurrence of one log2 packet or by the
prime/composite predicate in the permissions. This is a conclusive global
stop for the frozen prime-primitive target, without changing any arrow,
measure, endpoint, clock or packet convention.

## 5. Control L: least-proper-divisor owner and complete ledger

For every composite n let ell(n) be its least proper divisor. It is prime:
otherwise a nontrivial factor of ell(n) would be a smaller proper divisor
of n. The L chart is `(n,t)->(2n/ell(n),t/ell(n))`, with its own image
`[2n/ell(n),2n/ell(n)+1/ell(n))` and inverse `y->ell(n)*y-n`
on that whole image.
Construct D_g^L from these words, not MAIN words. Section1's measure
argument applied to these actual labels gives L's own every-Borel IMAGE.

An even composite n has ell(n)=2, so its chart stays in cell n. An odd
composite n maps to the even cell M=2n/ell(n). No even cell maps to a
different cell. Thus the integer-cell components are the finite stars

`C_M={M} union { odd composite n : 2n/ell(n)=M }`,
one for each even M>=4. All noncomposite cells remain units only.

More explicitly, write M=2q. If q is even there are no odd leaves.
If q is odd, the leaves are exactly n=pq where p is an odd prime with
`3<=p<=p_min(q)`, where p_min(q) is the smallest prime factor of q,
also when q itself is prime. Indeed the smallest prime factor of pq
is p precisely under that inequality. This proves finiteness and excludes
unlisted cell-to-cell connections.

Along an L edge the slope is target-cell/(2*source-cell), and along its
inverse it is twice the cell ratio. Therefore every L arrow from n+t to
m+s has a=(m/n)2^k and s=a*t, with n,m in the SAME C_M. Conversely the
root has its whole-cell half-contraction; conjugating that contraction
along a leaf edge gives a whole-cell half-contraction at each leaf.
Contract, traverse the finite star path, then expand to the requested
endpoint exactly as in the explicit legality argument of Section4.1.
This proves the displayed normal form is both necessary and sufficient
for L itself, with no inherited MAIN orbit equivalence.

At every integer in C_M the entire source return-slope group is 2^Z:
the upper bound follows from the cell-ratio calculation and the lower
bound from the root contraction and its transported inverse. Thus each
C_M supplies its OWN primitive log2 packet, with all integer phases
`h+log n mod(log2)Z`, source isotropy Z, and trivial extension isotropy.
Different even roots remain distinct packets. There are countably infinitely
many log2 packets, not one identified by their common time.

Every active noninteger return has a=1 and equal cell, so is the unit.
Its orbit is classified by C_M and t/n modulo 2^Z, with free phase
h+log t. All other points are isolated free-height packets. For L the
ENTIRE clock kernel is units: distinct cells in a star have ratio 2/p,
p/2 or p/p' with odd primes p!=p', never a power of2. The normal form
then rules out every off-diagonal slope-one arrow.

In particular the L integer orbit of4 is exactly {4}, not MAIN's C,
while its entire H_4 is still(log2)Z. This control has prime-coverage AND
log2-multiplicity failure, despite the same numerical local primitive.
All legal incoming words, full domains and compatible chains belong to
this star owner; no extra leaves or common-time identifications are made.

## 6. Control Z: zero-carry owner and complete ledger

With n=dq, q>=2, the Z chart and its actual inverse are

`n+t -> q+t/d`, image `[q,q+1/d)`,
`q+s -> dq+d*s`, on `0<=s<1/d`.

Build D_g^Z using only these words. Every label is now pure scaling
g(x)=a*x, with a positive rational; every-Borel IMAGE is its own slope a.
Images and inverse permissions are not those of MAIN. All of [0,2) has
units only. Since a positive x fixed by a pure scaling requires a=1,
every positive source has trivial isotropy. At0 there are only units too.
Thus the entire source/extension isotropy and H are trivial everywhere;
ker c is also units because a=1 is the identity global label.

For completeness the full Z orbit classification can be given, not only
this no-return argument. An edge preserves
`rho=t/n` for x=n+t, n>=2. At a prime cell n=p, there are no forward
charts and an inverse needs t<1/d<=1/2. Therefore every prime-cell point
with 1/2<=t<1 is isolated. Define the active locus to contain all composite
cells, and the lower half 0<=t<1/2 of every prime cell p>=2.
Every such point has `0<=rho<1/4`.

Each active point reaches `2+2rho` legally. If n=p is prime, first use
the inverse d=2 to reach cell2p, then its forward divisor p to reach cell2.
If n is composite, choose a prime factor p of n. First divide by n/p
to reach cell p, then do the same two moves. In the prime case the inverse
doubling is legal because `2p*rho=2t<1`; in the composite case it is legal
because `2p*rho<=n*rho=t<1`. These constructions also work when t=0.
Thus every active orbit is EXACTLY

`O_rho={ n*(1+rho) : n composite, n*rho<1 }
        union { p*(1+rho) : p prime, 2p*rho<1 }`,
for `0<=rho<1/4`.

Conversely all generators preserve rho, all listed points are active,
and the displayed paths connect them to the same cell2 representative.
This proves the complete equivalence relation with the correct strict
upper endpoints. For rho=0 the orbit is all integers n>=2. For rho>0
it is finite because n<1/rho. Every point outside these sets is isolated.
Between two points n(1+rho),m(1+rho) in O_rho the UNIQUE affine label is
g(x)=(m/n)x, and it is actual by the connecting paths. This characterizes
all arrows, not just all endpoints.

The potential V(x)=log x on the active locus gives
`c(x->y)=log x-log y`. The phase is h+log x, and every physical orbit
is free real with no positive primitive. Isolated points retain height h.
The whole integer orbit of4 is all integers>=2, but its entire H_4 is0.
This demonstrates why MAIN's return group cannot be transferred after
removing the carry. Full incoming words are generated by the stated Z
inverses with their own strict bounds, not MAIN's inverse strips.

## 7. Control A: own IMAGE, full rational return groups, qualified remainder

### 7.1 Its actual owner and strata

A has every pair n>=3, integer 2<=d<n, without divisibility. On n+t its
map and full inverse are

`n+t -> (2n+t)/d`, image `[2n/d,(2n+1)/d)`,
`y -> d*y-n` on that exact half-open image.

If m=floor(2n/d) and r=2n-dm, its fractional formula is
`n+t -> m+(r+t)/d`, where 0<=r<d. The image stays in that one cell;
if r=d-1 its upper integer endpoint is excluded. For r!=0 the fractional
coordinate is NOT simply scaled, and integer/noninteger strata need not
be invariant. Build its own D_g^A by finite legal words. The affine
measure argument proves its own every-Borel IMAGE and c=-log a.

Every source generator lies at x>=3, and every target is STRICTLY above2
because n>d. Hence [0,2] has only units. Rational affine labels preserve
rational versus irrational type. At an irrational x, any fixing label
satisfies `(a-1)x=-b` with rational a,b, forcing a=1,b=0. Therefore ALL
irrational sources have trivial source/extension isotropy and H=0,
independently of the still-unclassified details of their orbit domains.

### 7.2 The entire rational orbit of4

For each integer N>=3 the two legal A moves at4

`f_(4N,2N)^(-1)` followed by `f_(4N,8)`

give the affine label S_N(x)=N*x/4 and send4 to N. The permissions hold:
2N<4N and8<4N. The first endpoint is4N and the second is N, so no
intermediate domain is inferred merely from the composed label.

For any rational z=u/v>2 with positive integers u>2v, apply S_u and
then f_(u,2v). Both are legal at the indicated points. The resulting
path P_z sends4 to z with exact label and slope

`P_z(x)=(z/8)*x+z/2`, slope `z/8`.

Thus every rational above2 belongs to the orbit of4. No irrational or
point at most2 can belong, by the type/domain facts above. Consequently
the ENTIRE A orbit of4 is `Q intersect(2,infinity)`.

### 7.3 Entire return slopes, not a finite loop certificate

Let z be rational in[n,n+1) with n>=3 and put y=(z+n)/2. The loop
`P_y^(-1) o f_(n,2) o P_z` is actually legal at4 and has slope
`z/(z+n)`. Composing with the inverse of f_(4,2), itself an actual
loop at4 of slope2, gives an actual return slope `2z/(z+n)`.

For every integer k>=8 choose
`z=3*(k+1)/(k-1)`, which lies strictly between3 and4. The displayed
return slope is then exactly `(k+1)/k`. Finite products and inverses
therefore realize A/B for ANY integers A,B>=8, by telescoping consecutive
ratios. Given ANY positive rational u/v, multiply numerator and denominator
by an integer K large enough that Ku,Kv>=8. It follows that u/v is an
actual return slope at4. The reverse inclusion follows from the frozen
rational affine label group. Hence the ENTIRE return-slope group is

`S_4^A=Q_(>0)`,
`G_4^4={ (x -> 4+a*(x-4),4) : a in Q_(>0) }`,
`H_4=log(Q_(>0))`.

This additive group is dense in R, since positive rationals meet every
interval (exp alpha,exp beta). It has no least positive element. There is
NO positive primitive to select from a log2 loop, a log3 loop or any other
individual return. Extension fixed-object isotropy is still the unit group.

Transport by P_z preserves slopes, so EVERY rational z>2 has this entire
source isotropy and entire dense H. In fact for rational z,w>2 and any
a>0 rational, `P_w o L o P_z^(-1)` realizes the unique label
`x -> a*x+(w-a*z)` when L is the return at4 with slope a*z/w.
Thus A restricted to the rational orbit is the full rational-affine action
there, proved from legal presentations rather than assumed at the outset.
Its clock kernel on this orbit consists of ALL rational translations
between retained endpoints. Its real phase set is R/log(Q_(>0)); it is
not replaced by a point or a chosen circle. All these cosets remain.

### 7.4 What is and is not closed for A

All source return groups and all physical stabilizers are now decided:
[0,2] has units, every irrational has trivial isotropy/H, and every
rational above2 has the full rational slope group and dense H. Thus A
has NO positive primitive anywhere, despite many individual log-prime
clock arrows and loops. This is an entire-group conclusion.

The full closed-form classification of A's irrational base orbits and
the domains of its off-diagonal translations is not completed here: OPEN.
Their exact reconstructible owner remains the countable D_g^A word union,
with `ker c={ (x->x+b,x):x in D_(1,b)^A }`; no claim that all rational
affine labels are legal at an arbitrary irrational is made. Each such
actual base orbit has a free R phase by its trivial isotropy. All finite
incoming words and compatible chains are retained by the legal-domain
construction, without a bounded census or a replacement equivalence.
This explicitly allowed control remainder is not promoted to a global
affine-action theorem and does not postpone MAIN's decisive stop.

## 8. Controls, ownership limits and disposition

Arithmetic: MAIN uses all actual proper divisors; L removes the branching
choice, while A removes divisibility entirely. Their different complete
integer/rational return behavior shows why the predicate alone cannot
certify a prime packet. L's infinitely many equal-log2 packets are kept.
A's dense H is kept rather than selecting a desired log-prime subgroup.

Geometric/map and ownership: Z changes the affine carry, and its orbit
and return ledger is derived from its own maps and images. Lebesgue measure
and full X remain fixed in every control, but no relation, return group or
clock is inherited across owners. No smooth or symplectic interpretation
is being tested, so classical geometric-lift criteria are NOT APPLICABLE.

Robustness: all conclusions stated as complete use exact all-point domains
and unbounded finite compositions. There is no precision or numerical
cutoff to vary; those empirical controls are NOT APPLICABLE. Half-open
boundary equalities, zero fractions, all incoming labels and phase cosets
were checked explicitly. Only the stated A irrational-orbit/domain closure
is OPEN, with no finite check offered in its place.

PROVES_TOO_MUCH: A actually has every positive rational slope as a return
at4, so occurrence of an individual log p is not a prime-orbit mechanism.
Likewise equal primitive values do not identify L's different packets.
These are exact controls against selecting arithmetic-looking loops or
discarding multiplicity; they are not transferred positive credit.

The proposed lineage is realized at the stated observable/action level:
proper divisibility controls which uniform real maps are available, and
the resulting real cell determines the next available source divisors.
This does not establish strong naturalness, a prime generator, Logistic/
Henon conjugacy, a conservative lift, a trace or an operator. No external
prime acceptor, prime table, log-prime roof, von Mangoldt weight or zero
data has entered any owner.

Established: the exact measured generated-groupoid owner, its all-point
IMAGE cocycle and the COMPLETE MAIN source/orbit/stabilizer/phase ledger.
Negative: MAIN's only positive primitive packet has length log2, so the
required every-prime coverage fails. Portfolio STOP / FORK, preserving
this owner and its negative record rather than tuning it into a new object.
T0 ownership is established; the prime-target T1/T2 promotion is NOT PASSED.
T3 NOT AUDITED; classical fields NOT APPLICABLE; formal Route coordinates
UNASSIGNED; Route B NOT INVOKED. No determinant, spectrum, RH or general
arithmetic-dynamics no-go is claimed.

The raw derivation is to be frozen after full self-read. The reviewer then
HOLDs; current-manuscript comparison requires root's full raw read and a
DISTINCT PAPER UNLOCK. Agreement with a later paper would not constitute
external or calibrated verification.

EOF — ANG-20260925-DAC01 independent raw derivation.
