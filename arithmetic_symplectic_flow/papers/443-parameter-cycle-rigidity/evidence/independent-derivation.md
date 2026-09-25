# PCR01 — independent card-only derivation

Candidate: ANG-AUDIT-20260923-PCR01.
Batch ADMISSION-CLOCK-20260923-S; Paper443, round4/5.
Reviewer: pcr01_independent_review. Date: 2026-09-23 UTC.

## 0. Freeze, input and limitations

This raw derivation follows the separate RAW RELEASE after CP1. Its only
opened scientific input is the original 99-line candidate card, SHA256
`f9d2dac20d66d35e7a36ef63c53ca350827bd28a69dd98f36df5547df2ac9f2d`.
The reviewer has not opened author paper, README, claim ledger, peer results
or helper results. Inherited conversation context is not a blind-review wall.
Execution is separate-author, same-model internal AI work, NOT_CALIBRATED;
it is neither external peer review nor human/cross-model verification.
No numerical census, external search, Git mutation or manuscript edit occurs.
Everything below is an exact deduction from the frozen definitions.

Parameters are independent owners, not time and not an extra coordinate.
Any comparison between parameters is a statement about the specified family;
it does not identify the owners' packets, measures or height coordinates.

## 1. Every-point IMAGE owner and all actual histories

Fix one parameter lambda. On an actual source piece E_i(lambda), the assigned
map is the spatial C1 local diffeomorphism f_i(lambda,.). Cover its ambient
open domain by a countable rational-ball refinement on which this map is
injective. Such balls exist at every spatial point by the inverse function
theorem. Intersect with E_i(lambda), and subtract earlier members of the
fixed enumeration if a disjoint branch partition is desired. These subsets
are Borel; the restrictions retain the original ambient inverse germ.

For any such branch with ambient inverse theta and actual target set V,
every Borel B subset V obeys

    Leb(theta(B)) = integral_B |det D theta(y)| dy.

The ambient local diffeomorphism gives both Borel images and the ordinary
change-of-variables identity. Restricting this identity to actual Borel
pieces includes boundary pieces and null sets. The pointwise germ value is
assigned even on a null image; an a.e. density version is not substituted.
At an actual source x the resulting clock is exactly

    kappa_lambda(x) = log |det D_x f_i(lambda,x)|.

No determinant involving lambda enters. If different actual inverse branches
meet the same target, all are kept with their own derivatives. Countably
many local charts imply at most countably many actual predecessors per
target, not finitely many. Repeated charts describe one geometric branch,
not extra arrows or packet multiplicity.

Define Pre_0(A)=A and

    Pre_(n+1)(A) = {x legal : T x belongs to Pre_n(A)}.

This recursion uses every legal branch and all n>=0. The source component
of w is exactly all z for which some legal iterates T^m z and T^n w agree.
It includes terminal states with incoming histories; terminal does not mean
deleted or absorbing. These formulas are exact infinite descriptions, not
claims of a finite predecessor list or an orbit census.

## 2. Groupoid, all kernels, isotropy and height phases

Write S_n(x)=sum_(j=0)^(n-1) kappa(T^j x), whenever n steps are legal.
For g=(z,k,w), choose legal m,n with k=m-n and T^m z=T^n w; set

    c(g)=S_m(z)-S_n(w).

For two witnesses of the same triple, their two indices differ by the same
integer. Order the witnesses by that integer. The longer legal witness adds
the same clock along the common terminal segment to both sums, so c is
well-defined. For two composable arrows, extend the shorter middle witness
to the longer one using its already legal trajectory. The middle clock
cancels. Thus lag and c are additive; inversion reverses both. In particular
the actual forward arrow (T x,-1,x) has clock -kappa(x).

The complete kernels, without an injectivity or sign assumption, are

    ker(lag) = {(z,0,w): T^n z=T^n w for some legal n},
    ker(c)   = {(z,m-n,w): T^m z=T^n w, S_m(z)=S_n(w)},
    ker(lag,c) = ker(lag) intersect ker(c).

These equalities identify triples, not alternative witnesses. For a source
whose forward path terminates or is infinite and not eventually periodic,
isotropy is {0}. Indeed a nonzero lag returning to the same source implies
two unequal forward times agree, hence an actual eventual cycle. Conversely
an eventual least-q cycle gives source isotropy q Z. If C is that cycle's
signed clock, c on isotropy sends r q to r C.

The extension is the full X x R with g:(w,h)->(z,h+c(g)). For its orbit SET,
unrestricted height translation by t fixes the orbit precisely when an
isotropy arrow at w has clock t. Therefore the entire stabilizer is

    H={0}                           if there is no eventual cycle,
    H=C Z                          on an eventual cycle component.

For C!=0 the primitive positive generator is |C|, never |C|/q; extension
isotropy is zero. For C=0, H={0}, there is no positive primitive, and extension
isotropy remains q Z. Ordinary positive integer repeats are r|C|, r>=1.
The whole incoming basin cannot create a smaller H because all source
isotropy in that deterministic component is q Z with the same cycle clock.

Here is a complete phase description that also covers noninjective basins.
Choose a core a_0,...,a_(q-1), set K_j=S_j(a_0), K_0=0, K_q=C.
For z in its full basin, let d_z be first entry depth and e_z its entry phase:
T^d_z z=a_e_z. Put

    l_z=d_z-e_z,     b_z=S_d_z(z)-K_e_z.

All arrows between any two basin points, and no others, are

    (z, l_z-l_w+r q, w),     c=b_z-b_w+r C,     r in Z.

Consequently the lag, clock and joint kernels in this basin are obtained
respectively by l_z-l_w+r q=0, b_z-b_w+r C=0, or both. Every real phase is

    h-b_z mod C Z,

where quotient by {0} means the real number itself. All r, all predecessors
and all entry phases remain, including when C=0 and entry clocks are nonzero.

For a terminating component with terminal t, let d_z be its actual terminal
depth. Its unique arrow from w to z has lag d_z-d_w and clock
S_d_z(z)-S_d_w(w); its phase is h-S_d_z(z), with source and extension isotropy
zero and H={0}. Any two points of an infinite non-eventually-periodic
component likewise have a unique lag and clock: two different lags would
force an eventual cycle. Choose a set-level anchor a and the unique arrow
g_z from a to z, write b_z=c(g_z), and use the phase h-b_z in R.
No measurable selector, Hausdorff orbit quotient or canonical global choice
is asserted. Kernels on these components still follow the preceding exact
lag/clock equalities and need not be just units for a general owner.

## 3. Continuous actual cycle branch: signed-clock rigidity

On J let x_j(lambda)=T_lambda^j x(lambda), 0<=j<q, using the frozen ordered
word i_0,...,i_(q-1). The actual admission hypothesis and jointly C1 branch
maps imply that all x_j and all nonsingular matrices

    A_j(lambda)=D_x f_i_j(lambda,x_j(lambda))

are continuous. Hence the signed cycle sum

    C(lambda)=sum_j log |det A_j(lambda)|

is continuous. This uses the actual spatial germ at each phase, not a
derivative of the phase representative and not a parameter determinant.

Every lambda has the same least source period q by hypothesis. Section 2
therefore gives source isotropy q Z, entire H_lambda=C(lambda) Z, and,
if C(lambda)!=0, primitive |C(lambda)|. Prime-only positive primitive ledgers
impose exactly

    C(lambda) belongs to D={0} union {+log p,-log p : p ordinary prime}.

The set D is locally finite in R: a bounded interval can involve only primes
below a finite exponential bound, and zero is separated by log 2 from every
nonzero member. A continuous map from connected J into this discrete set
is constant. Thus precisely one of the following holds on the whole branch:

1. C identically zero. Source and extension isotropy are q Z; H={0}; the
   branch contributes no positive primitive at any parameter.
2. C identically +log p or identically -log p for one ordinary prime p.
   Source isotropy is q Z, extension isotropy zero, H=(log p) Z and the
   primitive log p at every parameter, with ordinary positive integer repeats.

There can be no zero crossing, sign change or change of prime within this
connected actual least-q branch under the hypothesis. No packet uniqueness
was used. Neither an empty positive ledger nor absent all-prime coverage
contradicts prime-only purity. The statement says nothing about continuity
or multiplicity of the owners' other periodic packets. Even constant C does
not identify distinct owners or imply an isomorphism of their basins/phases.

This is a necessary family condition, not an arithmetic-admission theorem.
Its contrapositive excludes uniform prime purity along a branch with varying
C; it does not exclude exceptional individual parameters or a zero-clock
branch. If the actual word, legality, least period or regularity changes,
the stated branch hypothesis must first be re-established.

## 4. Local actual persistence: joint C1 is sufficient

Let R(lambda,x) be the complete q-word return composition in the specified
joint-open neighborhood of (lambda_0,x_0). Every pair there legally executes
the word. The given jointly C1 branch maps make R jointly C1 on a smaller
joint-open neighborhood. No condition R(neighborhood) subset neighborhood
is needed to define R or apply the implicit function theorem.

Set F(lambda,x)=R(lambda,x)-x. At the given cycle F=0 and

    D_x F=M-I,     M=D_x T_lambda_0^q(x_0),

which is invertible by the frozen nonresonance assumption. The implicit
function theorem gives a local C1 branch x(lambda), x(lambda_0)=x_0,
unique among zeros in suitable local parameter/spatial neighborhoods.
Shrink these neighborhoods inside the joint legal q-word set. This branch
is an actual legal q-return point for every retained lambda, not just a root
of a formal composition. Its phase trajectories are jointly C1 in lambda.

For each 1<=r<q, the original least-q point satisfies
T_lambda_0^r(x_0)!=x_0. The finitely many intermediate differences along the
word are continuous; shrink the parameter interval so every such inequality
persists. The new actual period is therefore still least q. For q=1 this
last check is vacuous. The conclusion is local; it promises neither a global
continuation across an admission threshold nor persistence of other packets.
It also does not supply prime purity; Section 3 applies only if that separate
owner-level hypothesis holds on the local branch.

## 5. Total cycle-clock sensitivity in the joint C2 subclass

Assume now the additional joint C2 regularity. The implicit branch is C2;
write v_j=x_j'(lambda), A_j=D_x f_i_j(lambda,x_j), and
b_j=partial_lambda f_i_j(lambda,x_j). Differentiating each phase gives

    v_(j+1)=A_j v_j+b_j,       v_q=v_0.

With M=A_(q-1)...A_0, differentiation of the entire q-word yields

    (I-M) v_0 = r,
    r=sum_(j=0)^(q-1) A_(q-1)...A_(j+1) b_j,
    v_0=(I-M)^(-1) r.

An empty matrix product is the identity. Nonsingularity of I-M persists
after shrinking the local branch. The phase recurrence determines every
v_j, so the total derivative of the actual signed cycle sum is

    C' = sum_j tr( A_j^(-1) [ partial_lambda D_x f_i_j
                              + D_x(D_x f_i_j)[v_j] ] ),

with each derivative evaluated at (lambda,x_j(lambda)). The absolute value
in log|det| causes no extra sign: on nonsingular real matrices,
d log|det A|=tr(A^(-1)dA). Equivalently C'=tr(M^(-1) M'), where M' is the
total derivative along the moving cycle, not a fixed-x partial derivative.

Joint C1 alone gives continuous A_j and C but does not generally give these
second derivatives; this formula is not claimed there. If Section 3's
prime-purity hypothesis also holds, this total derivative is identically
zero. That is a necessary restriction, not a sufficient arithmetic mechanism.

## 6. Control A: a varying linear return

Fix lambda in (-1/2,1/2), a=2+lambda in (3/2,5/2). The full-line map
T(x)=a x is a global diffeomorphism. Its only inverse is theta(y)=y/a,
with J=1/a on every real y and every-Borel IMAGE factor 1/a. Its own
clock is kappa=log a>0. All signed iterates are T^k x=a^k x, k in Z.

All arrows are

    (z,k,a^k z),        c=k log a,        z in R, k in Z.

All three kernels are exactly units. Zero is the only periodic point,
least period one, with the singleton full incoming basin {0}. It has source
isotropy Z, extension isotropy zero, H=(log a) Z, primitive log a and every
positive integer repeat. Its phases are h mod log a. Nonzero points have no
eventual cycle, source and extension isotropy zero and H={0}.

For all nonzero histories choose epsilon in {+1,-1}, r in [1,a). The complete
base component is {epsilon a^n r:n in Z}, and this labelling is unique.
At its n-th point, a complete real phase is h+n log a; equivalently one may
shift the phase by the constant log r and write h+log|x|. Forward height
change -log a cancels the increment n->n+1. There are no terminal points.

The actual branch x(lambda)=0 persists on the whole interval and is always
least one; 1-a!=0. Its signed clock C=log(2+lambda) has total derivative
1/(2+lambda), with phase derivative zero. Exactly one positive packet is
present for each owner. It is prime-only exactly when a is an ordinary prime;
in this specified interval that is exactly lambda=0, giving log 2.
Thus A disproves uniform prime purity on the interval but does not exclude
the individual lambda=0 owner. No all-prime coverage or endogenous arithmetic
source is supplied by that exceptional one-packet benchmark.

## 7. Control B: nonlinear deformation with unchanged fixed clock

Fix b=lambda^2 in [0,1/4) and write f(x)=2x+b x^3. The derivative
f'(x)=2+3b x^2>=2 makes f an increasing onto global diffeomorphism of R.
The inverse theta(y) is the unique real solution of b s^3+2s-y=0;
at b=0 it is y/2. The joint implicit equation has nonzero spatial derivative
also at lambda=0, so no singular inverse convention is needed there.

The exact inverse IMAGE and forward clock are

    J(y)=1/(2+3b theta(y)^2),
    kappa(x)=log(2+3b x^2)>=log 2.

These hold at every point and for every Borel image. Every positive and
negative iterate is defined. Let D_k(x)=(f^k)'(x)>0, D_0=1; explicitly

    D_k(x)=product_(j=0)^(k-1) (2+3b (f^j x)^2),               k>0,
    D_(-k)(x)=1/D_k(f^(-k)x),                                k>0.

All arrows and their clocks are exactly

    (z,k,f^k z),        c=log D_k(z),        z in R, k in Z.

For k>0 the clock is at least k log 2>0; for k<0 it is negative. Thus all
three kernels are units, including at lambda=0. The only periodic point is
0: positive points strictly increase and negative points strictly decrease
under f. The inverse is unique, so the entire eventual basin of 0 is {0}.
There are no other eventually periodic points and no terminal points.

At zero the source isotropy is Z, extension isotropy zero, entire H=(log 2) Z,
primitive log 2, and phases h mod log 2. Every positive integer repeat remains.
All nonzero points have source/extension isotropy zero and H={0}. Their
complete components have unique labels epsilon in {+1,-1} and

    r in [1,f(1))=[1,2+b),
    x_n=epsilon f^n(r),              n in Z.

Indeed positive forward iterates diverge to infinity and backward iterates
decrease to zero, so they cross that half-open fundamental interval exactly
once. Oddness supplies the negative components with the same derivative
products. A complete real phase at x_n is

    h+log D_n(epsilon r).

The signed derivative product identity verifies invariance for every n,
including negative n. These anchors describe the entire nonperiodic line,
not a finite orbit sample.

The actual branch 0 persists with least period one and nonresonance 1-2=-1.
Its signed clock is identically log 2 although the map is nonlinear for
lambda!=0. In Section 5's notation v_0=0, partial_lambda f(lambda,0)=0,
and partial_lambda D_x f(lambda,0)=0, giving total clock derivative zero.
For every parameter the full positive ledger consists of exactly one
primitive log-2 packet; purity, nonemptiness and uniqueness hold, but not
all-prime coverage. This external control prevents a false conclusion that
every genuine parameter deformation must change a positive clock.

## 8. Control C: exact partial inverse and legal iterates

Fix lambda in (-1/2,1/2). Its full carrier remains R. The legal source set is
(lambda,infinity), T(x)=2x there; every x<=lambda is terminal, not fixed.
There is an actual predecessor of y if and only if y>2lambda, namely y/2.
Thus the actual inverse is theta(y)=y/2 on (2lambda,infinity), with J=1/2
and every-Borel IMAGE factor 1/2. In particular a target can be terminal
when 2lambda<y<=lambda. Every legal source has kappa=log 2; no forward
clock is assigned at an illegal source by borrowing the formal total map.

For n>=1 define D_n as the set on which n forward steps are legal. Directly
from the inequalities 2^j x>lambda for 0<=j<n,

    lambda<0:  D_n=(lambda/2^(n-1),infinity),  T^n(D_n)=(2lambda,infinity),
    lambda>=0: D_n=(lambda,infinity),          T^n(D_n)=(2^n lambda,infinity).

On these domains T^n x=2^n x. D_0=R. Consequently the complete depth-n
predecessor set of y is the singleton {y/2^n} if y belongs to the indicated
T^n(D_n), and is empty otherwise. This includes every inverse depth and
every terminal-target possibility, with all strict endpoints retained.

Every actual arrow has clock k log 2 for its lag k, by any legal witness.
Partial injectivity implies that a lag-zero arrow is a unit. Since log 2 is
nonzero, all three kernels are units for every parameter. The next three
subsections list all components; they also determine exactly which lags
exist between each pair, rather than granting all total-map arrows.

## 9. Control C when lambda<0

There are exactly four kinds of complete components.

### 9.1 Isolated terminals

Every t<=2lambda is terminal with no actual predecessor. Its sole base and
extension arrows are units. Source/extension isotropy are zero, H={0},
and every real h is a distinct extension phase over that singleton.
The endpoint t=2lambda is included here because its formal predecessor
lambda is illegal.

### 9.2 Terminal chains with all incoming depths

For each t in (2lambda,lambda], the complete component is

    x_n=t/2^n,             n>=0.

x_0=t is terminal; all x_n with n>=1 are legal and T x_n=x_(n-1).
Every predecessor depth exists and is unique. Every negative legal point
eventually reaches exactly one such t, so these chains cover all remaining
negative points in (2lambda,0). Between any i,j>=0 all arrows are exactly

    (x_i,i-j,x_j),          c=(i-j) log 2.

There are no extra lags or loops at t. All these points have source and
extension isotropy zero and H={0}; their complete phase is h-n log 2 at x_n.
This is also h+log|x_n| up to the fixed additive constant log|t|.

### 9.3 The actual fixed point

Zero is legal because lambda<0, and is the only periodic point. Its unique
predecessor is itself, so its full incoming basin is the singleton {0}.
All base arrows are (0,k,0), k in Z, with c=k log 2. Source isotropy is Z,
extension isotropy zero, H=(log 2) Z, primitive log 2, and phases h mod log 2.
There is exactly one positive primitive packet, with all positive integer
repeats; no all-prime coverage follows.

### 9.4 Positive bi-infinite components

Each has a unique r in [1,2) and states x_n=2^n r, n in Z. All these steps
and inverses are actually legal. The arrows and clocks are

    (x_i,j-i,x_j),          c=(j-i) log 2,       i,j in Z.

Source/extension isotropy are zero, H={0}, and the complete real phase at
x_n is h+n log 2. There are no other components or periodic points.

Together 9.1–9.4 cover the entire real line, all strict-cut endpoints, all
terminal incoming chains and every nonterminating history.

## 10. Control C when lambda=0

Every x<=0 is an isolated terminal: the actual inverse domain is (0,infinity),
so even zero has no predecessor and is not a fixed point. Its only arrows
are units, with zero source/extension isotropy, H={0}, and phase h.

The positive half-line decomposes into the bi-infinite components of 9.4,
with r in [1,2), n in Z, arrows (x_i,j-i,x_j), clocks (j-i)log 2 and phases
h+n log 2. All source and extension isotropy and entire stabilizers are zero.
There are no periodic points anywhere and the full positive ledger is empty.

## 11. Control C when lambda>0

Every t<=lambda is an isolated terminal with no predecessor: an actual
predecessor would require t>2lambda. Its phase is h, and both isotropies and
H are zero. This includes the formal zero and the strict cut x=lambda.

The whole legal region (lambda,infinity) decomposes uniquely into forward
rays with anchors

    r in (lambda,2lambda],      x_n=2^n r,       n>=0.

The anchor has no predecessor, because r<=2lambda, but it is a legal source.
The right endpoint r=2lambda belongs here; its formal predecessor lambda
is terminal and does not map to r. Every legal point has only finitely many
backward steps, determined by its n, and infinitely many forward steps.
For every i,j>=0 the exact arrows and clocks are

    (x_i,j-i,x_j),          c=(j-i) log 2.

All these points have zero source and extension isotropy and H={0}; the
complete real phase at x_n is h+n log 2. Distinct anchors give distinct
components, even though their clock formulas agree. There is no cycle,
no eventual cycle, and no positive primitive packet for this parameter.

## 12. C's actual-admission boundary and the family conclusion

The formal equation 2x=x gives x=0 for every lambda, but it is an actual
least-one branch only on the negative-parameter subinterval. There the
joint-open permission x>lambda contains each (lambda,0), nonresonance is
1-2=-1, the branch persists locally, and its signed clock is log 2.

At lambda=0 and every positive lambda, zero is terminal and has no actual
cycle clock. The nonresonant formal derivative cannot repair the failure of
actual admission. In particular no joint-open legal neighborhood of (0,0)
exists for the frozen complete word; the persistence theorem's hypothesis
fails at the threshold. The positive ledger changes from one log-2 packet
for lambda<0 to empty for lambda>=0, without contradicting the branch theorem.
Each owner remains prime-only in the sense of purity, including vacuously
the empty cases, but there is no actual continuous cycle branch through zero.

All three controls keep their full carriers and own IMAGE clocks. A supplies
a varying clock; B supplies a genuinely nonlinear deformation whose single
positive packet keeps its clock; C supplies an actual admission boundary
that no formal return equation can cross by itself. They establish neither
a prime-symbolic arithmetic mechanism nor coverage of all ordinary primes.

## 13. Raw conclusion and scope discipline

The frozen family contract supports the conditional signed-clock constancy
theorem, local actual least-period persistence under joint C1 and the stated
nonresonance/legal-neighborhood assumptions, and total sensitivity under
the separate joint C2 subclass. All three external controls have been
classified on their entire real carriers with all histories and phases.

No universal obstruction to an isolated parameter owner is proved. No
uniqueness of the general family ledger, global cycle continuation,
arithmetic admission, prime coverage, classical symplectic structure,
operator, target-zero result or formal Route result is inferred.
Classical NOT APPLICABLE; arithmetic T1 NOT PASSED; T3 NOT AUDITED;
formal UNASSIGNED; B NOT INVOKED. Same-object ownership is retained.

This file is now the pre-manuscript raw checkpoint. Any later correction
requires an explicit erratum, not replacement of the original derivation.
No author scientific surfaces may be read before a distinct PAPER UNLOCK.
