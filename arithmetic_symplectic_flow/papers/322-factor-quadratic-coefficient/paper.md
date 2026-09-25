# Factor-to-coefficient feedback: owned clock, terminating divisor seeds

Paper ID: `322-factor-quadratic-coefficient`.
Candidate ID: `ANG-20260920-FQC01`. Date: 2026-09-20.
Status: `OWNED TWO-ROOT CLOCK; DIVISOR SEEDS TERMINATE — STOP / FORK`.
Classical A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED.

## Abstract

We freeze the whole signed real plane with ordinary area and the partial
transport T(x,y)=(y,x+y/x), permitted when a=floor x is
nonzero, a divides floor y, and y differs from x^2. The
integer factor pair is transported to its quadratic product/sum coefficients.
Both actual inverse roots are retained with their exact permission filters.
Their IMAGE gives the full-point clock log|1-y/x^2|, finite
on every legal step. Complete fixed and two-step equations have no
legal return. More decisively for the stated lineage, every nonnegative
integer state terminates after at most one step; the positive proper-divisor
seed cannot supply a periodic packet. The declared critical restriction also
stops the middle divisor of a square, so a no-accepted-divisor test
would already misclassify 4. Higher signed-real source periods remain
UNCLASSIFIED; no global no-period or zero-time theorem is inferred. Three
controls own their full domains, clocks and short-return results. The same
object passes the ownership calculation but stops/forks at the arithmetic-return gate.

## 1. Frozen owner and exact lineage

| Field | This owner |
| --- | --- |
| Carrier / measure | Y=R^2, Borel, ordinary Lebesgue area |
| Source | Partial real factor-to-product/sum update, exact floor permission |
| Arithmetic origin | Divisor-symbolic seed to actual factor pair to coefficient feedback |
| Clock | Own inverse IMAGE, declared analytic full-point version |
| Periodic convention | Complete retained-lag groupoid, all real heights and actual tails |
| Controls | DIVISIBILITY-OFF, DIVISIBILITY-SHIFT, REAL-DIVISION-OFF |
| Classical base / suspension / roof | NOT APPLICABLE |
| Operator / trace / determinant | NOT SUPPLIED / NOT PURSUED |

The [original card](candidate-card.md), first 161 lines, was frozen before
these claims, SHA-256
`d18baee8f8918e64474b7229c3834e9f364e68e308228fbda166748fc841012a`.
Root read all 199 lines of the
[321 frontier](../321-nonnegative-geometric-quotient/evidence/scout-record.md),
SHA-256 `bc8f249e4f456b2f62bb59e9ffed77c2a1e5331382988d20e6fa3050258f5bb5`.
Actual source access, old outcome exposure and transcription QA are distinguished
in [provenance](evidence/scout-record.md); no previous result transfers.

For a=floor x,b=floor y define the full partial source

    D={a!=0, a|b, y!=x^2},
    T(x,y)=(y,x+y/x).                              (1)

The condition a!=0 implies x!=0. All points outside D remain
terminal objects with T^0 and actual incoming histories. Signed points,
units, zero dividend, axes and every floor cut are retained. No
critical point is given a limiting step or clock. The denominator
is real x, not a. No extra polynomial coordinate is introduced:

    (xi-x)*(xi-y/x)=xi^2-(x+y/x)*xi+y.             (2)

At a positive integer seed (d,n), n>=2,d>=1, the arithmetic
permission is d|n, with proper divisor symbols 1<d<n. The
actual next state, when allowed, is (n,d+n/d): the factor pair
has become product-before-sum coefficients, which feed the next permission.
But n=d^2 stops even if d|n. This is an explicit
partial-action deformation, NOT a lossless lift of all original divisor arrows.
The critical restriction, floor readout, ordering and area are declared design;
stronger naturalness, canonical A0 and conservative/Henon/symplectic realization OPEN.
No prime/factor table, zeros, per-prime choices or prescribed prime clock.

## 2. Entire inverse, exact counts and retained terminal points

At target (s,t), put Delta=t^2-4s. Any predecessor has
y=s and solves x^2-t*x+s=0. The legal nondegeneracy condition
makes the two roots distinct. Thus the ENTIRE predecessor set is

    I_sigma(s,t)=(r_sigma,s),
    r_sigma=(t+sigma*sqrt(Delta))/2, sigma=+/-1,    (3)

retaining a root exactly when

    Delta>0, a_sigma=floor(r_sigma)!=0,
    a_sigma divides floor(s).                      (4)

Every retained r is nonzero, and s=r*(t-r) shows
r-s/r=2r-t=sigma*sqrt(Delta), so its source is noncritical.
Substitution proves each retained root is an actual predecessor. Conversely
every legal predecessor satisfies (3)-(4), with sigma determined by its
actual sign x-y/x. Hence there are exactly zero, one or
two predecessors, with no root selection and no label multiplicity.

For fixed a,b and sigma the U/V charts in the card
are a Borel bijection. They are restrictions of a smooth diffeomorphism
between open geometric sheets x!=0, sigma*(x-y/x)>0 and their
actual root images. The floor cuts merely restrict those sheets; they
do not change the inverse formula. Both sheets may share target points,
but correspond to different actual predecessor objects, not extra copies.

Missing incoming arrows and terminality differ. These exact main examples give
all three predecessor counts:

- (1,2) has Delta=0 and no predecessor, but is itself legal
  and maps to (2,3). No derivative is invented at its discriminant.
- (0,1) is terminal because its first floor is zero. It has
  exactly one predecessor (1,0), since the other root zero is illegal.
- (-1,1) is terminal because y=x^2. Its two predecessors are
  ((1+sqrt5)/2,-1) and ((1-sqrt5)/2,-1). Their floors are
  1 and -1, both dividing -1. Both are retained.

The last example explicitly shows that the critical terminal locus is
not removed and need not lack incoming histories. An object at Delta<=0
has no incoming root, but uses its OWN (x,y) for outgoing permission.

## 3. Own area IMAGE and full-point clock

On each actual inverse sheet with Delta>0, implicit differentiation gives

    dr/ds=-sigma/sqrt(Delta),
    dr/dt=sigma*r/sqrt(Delta),
    det D I_sigma=-sigma*r/sqrt(Delta).

Consequently the exact Borel IMAGE on every allowed chart V is

    mu(I_sigma E)=integral_E J_sigma dmu,
    J_sigma=|r_sigma|/sqrt(Delta)>0, E Borel subset V.       (5)

The geometric sheets are smooth and the legal domains are Borel restrictions,
so change of variables applies to all such E, including floor boundaries.
The displayed analytic derivative specifies the FULL-POINT version at those
retained cuts. It is finite and positive at every actual inverse point;
it is not uniformly bounded near a deleted branch domain boundary. The
measure identity alone does not force null-point values. Delta=0 is
not assigned a branch, density or infinite-clock repair.

At the actual predecessor (x,y), sqrt(Delta(T(x,y)))=|x-y/x|.
Thus the own clock is

    kappa(x,y)=-log J_(B_v)(Tv)
              =log(|x^2-y|/x^2)=log|1-y/x^2|.     (6)

It is finite on D and can have either sign or vanish: legal
(1,1/2), (1,-1), (1,0) give respectively log(1/2),
log2 and 0. These are step values, NOT primitive periods.
No positive roof, runtime or prescribed prime-log follows.

For every actual finite history let S_m(v)=sum_(0<=i<m)kappa(T^i v),
with S_0=0. Its selected actual inverse branch has IMAGE exp(-S_m).
Each finite branch pair from w to v meeting after lengths m,n
has its OWN IMAGE exp(-S_m(v)+S_n(w)). Retain exactly

    G={(v,m-n,w):T^m v=T^n w,both histories defined},
    c(v,m-n,w)=S_m(v)-S_n(w).                       (7)

Equal triples are one arrow, source w and range v. If two
presentations have the same lag, both lengths differ by the same integer;
the longer legal common future cancels. Composition aligns the middle histories
at their longer defined length. These prove pointwise descent and additivity
even with mixed inverse sheets and terminal T^0. The actual forward
arrow (Tv,-1,v) has clock -kappa(v), inverse +kappa(v).
All (v,h) remain, with arrows (w,h)->(v,h+c) and full
h-translation. Only a Borel/set quotient is claimed, not a smooth,
etale or Hausdorff space or invariance of area times dh.

## 4. Complete short-return equations and arithmetic-sector obstruction

### 4.1 All signed-real fixed and two-step states

A fixed state must satisfy y=x with x!=0. Its second equation
would be x=x+1, impossible. For any actual two-step return,
the first coordinate of T^2 is x+y/x. Equality to x forces
y=0. But the intermediate first coordinate is then zero, so the
second step is not legal. Thus there are NO fixed or two-step
returning states anywhere in the full signed plane, including all cuts.
There is no discovered short core or associated periodic basin to select.

### 4.2 Every nonnegative integer state terminates within one step

An integer first coordinate d=0 is terminal. For d>=1,n>=0,
failed d|n or n=d^2 also gives immediate terminality. If a
legal state has n=0 it maps to (0,d), terminal. Otherwise
n=dq with positive integer q. Its first output is

    (n,d+q)=(dq,d+q).                              (8)

For a second step, n must divide d+q. This is impossible:

- If min(d,q)=1 and n>=2, d+q=n+1, not divisible by n.
  The case n=1 would have d=q=1 and was already critical.
- If d,q>=2 and unequal, (d-1)(q-1)>=2 gives
  dq>d+q>0, again excluding divisibility.
- If d=q, the initial point was critical and had no first step.

This exhausts the entire nonnegative integer carrier, not a seed sample.
Every legal such history has at most one step; some terminate immediately.
In particular every positive proper-divisor symbol ends before any return,
and all its extension time groups are zero. No noninteger continuation is
hidden after (8), since both output coordinates remain integer.

The loss is also visible before iteration: for n=4, the sole
proper divisor d=2 gives (2,4), which is terminal because of
the declared critical restriction. Thus absence of an accepted proper-divisor
arrow is NOT a primality criterion for this owner. We do not
silently relabel its arithmetic permission as the original full divisor sieve.

### 4.3 Nonnegative real cycles also absent; global signed ledger open

A nonnegative source cycle could contain no zero coordinate, because first
coordinate zero is terminal and a zero second coordinate becomes terminal
after the next step. Write its positive cyclic register sequence as a_i.
Every legal step of (1) would require

    a_(i+2)-a_i=a_(i+1)/a_i>0.

Summing around the cycle gives 0>0, a contradiction. Positive trajectories
stay positive as long as defined, so no nonnegative point is eventually
periodic either. This is a short sign identity, not a higher-period census.
It also does NOT prove every noninteger positive history terminates.

The theorem is confined to the nonnegative sector. Higher SIGNED-real source
periods, their existence, time groups and multiplicity remain UNCLASSIFIED.
The complete fixed/two-step obstruction alone would not exclude them. No
global clock potential, global H0 or global no-cycle theorem is asserted.
The candidate stops/forks because the stated native arithmetic seeds cannot
return, and the nondegenerate deformation does not preserve the original
proper-divisor test. No search of further periods is needed to record this.

## 5. Full actual tails, isotropy and conditional repetitions

For ANY state that terminates, let d(v) be its exact finite
depth, A(v)=T^d(v)v its terminal anchor and S(v)=S_d(v)(v).
Every ancestor is retained by recursively taking BOTH roots passing (4).
There is no uniform finite-depth or finite-total-size assertion for these
full incoming trees; each inverse level has at most twice the previous
size. Selecting only an original seed would omit legitimate histories.

For two terminating states, actual tail equivalence holds exactly when their
terminal anchors agree. The retained lag is necessarily d(v)-d(w),
and its clock S(v)-S(w). Thus source isotropy, time image and
extension isotropy are all trivial on the ENTIRE terminating basin, with
full extension equivalence

    A(v)=A(w), h-S(v)=h'-S(w).                     (9)

No terminal step is evaluated. This covers the complete incoming trees
of every integer seed's terminal anchor, even ancestors outside that sector.
It does not claim every state belongs to a terminal basin.

For clarity about the unclassified part, suppose an actual cycle of least
source period P>=3 exists, with core q_j=T^j q_0. Write

    K=sum_(0<=j<P)kappa(q_j),
    R=product_(0<=j<P)|1-y_j/x_j^2|>0, K=log R.    (10)

Its COMPLETE tail class is the union of all actual finite predecessors
of all its core points, using both legal roots, not just the core.
At every point of that class source isotropy is PZ and the entire
time group is KZ. Extension isotropy is zero if K!=0, and
PZ if K=0. If K!=0 the least positive time is |K|;
if K=0 there is no positive primitive. The real product R
is not assumed an integer, above one or prime. This is a
conditional statement, not evidence that any such cycle exists.

For a point v hitting q_j after d steps, let A_j=S_j(q_0).
The complete phase at q_0 is

    h-S_d(v)+A_j modulo |K| if K!=0;
    h-S_d(v)+A_j as a real value if K=0.            (11)

Changing the legal hit representation changes this by a multiple of K.
All points, branches and phases remain; equal K does not merge different
cycles. Nonperiodic, non-eventually-periodic states have no source isotropy and
hence trivial time/extension isotropy, regardless of their nonloop clock values.

## 6. Three controls, each with its own domain and clock

### 6.1 DIVISIBILITY-OFF

The own domain is floor(x)!=0,y!=x^2, with the same real
transport. Its complete inverse retains both roots (3) with Delta>0
and floor(r)!=0, without any divisibility test. This is not the
main image: every removed permission condition must remain removed here.
The own restricted-sheet derivative gives J=|r|/sqrt(Delta), hence its
own kappa=log|1-y/x^2| on its own domain. Full IMAGE,
pointwise composition and lag descent follow from its actual charts as above.

All fixed and two-step returns are absent by the same geometric equations,
now checked against this own domain. The nonnegative-cycle sign proof also
applies, but the MAIN integer one-step termination proof does not: its
second-step divisibility obstruction is not a permission condition in this control.
Higher signed-real cycles remain UNCLASSIFIED. All terminal trees use this
control's unfiltered roots; (9)-(11) apply only with its OWN histories.

### 6.2 DIVISIBILITY-SHIFT

The own domain is a!=0,a|(b+1),y!=x^2, same actual transport.
Its ENTIRE inverse retains each root iff Delta>0, a_sigma!=0 and
a_sigma|(floor(s)+1). Its own J and kappa have the same
analytic expressions, but not the main branch domain, histories or basin.
No root is retained merely because it passed main permission.

For example (2,3) has both (1,2) and (2,2) as predecessors
under main and OFF; SHIFT retains only (1,2), since 2 does
not divide 3. This witnesses an actual difference between full owners.

All fixed and two-step returns are absent; the nonnegative-cycle sign proof
holds on every permitted cyclic history. Higher signed-real periods UNCLASSIFIED.
No main integer-seed termination theorem transfers across the changed gate.
Complete conditional trees, groups and phase use its own (9)-(11).

For both controls, (1,2) still has no incoming root but a legal
outgoing step, (0,1) has one predecessor and is terminal, and
(-1,1) has both golden-ratio roots and is critical-terminal. These
examples pass their OWN filters; they are not borrowed predecessor counts.

### 6.3 REAL-DIVISION-OFF

This control keeps main D but changes transport to L(x,y)=(y,x+y).
Its complete inverse is I_L(s,t)=(t-s,s), allowed exactly when

    a=floor(t-s)!=0, a|floor(s), s!=(t-s)^2.        (12)

There is one predecessor on this image and none outside. The derivative
determinant is -1, so its OWN Borel IMAGE is 1, its
full-point kappa and entire cocycle are identically zero. Neither main's
discriminant image nor two-root derivative transfers. For example (1,2)
has no predecessor because its possible predecessor (1,1) is critical,
but is itself legal. The critical-terminal point (2,4) DOES have
predecessor (2,2), passing its own domain and inverse (12).

Fixedness and two-step equations for this LINEAR transport reduce to (0,0),
which is terminal and cannot return. Moreover its matrix [[0,1],[1,1]]
has distinct eigenvalues phi=(1+sqrt5)/2>1 and -1/phi, of
absolute value below one. No positive power has eigenvalue one. Any
actual source cycle would therefore be the zero vector, which is illegal.
This short exact linear argument excludes ALL control cycles and eventual
cycles, not merely the one/two-step cores. All its source/time/extension
isotropy is trivial. Complete extension equivalence is actual source-tail
equivalence plus equality of h, because its OWN cocycle is zero.
Each terminal basin retains its own inverse chain and phase h; no
uniform finite-depth claim is made. This control-only all-period proof was
adopted from the raw review after the first manuscript lock. It does
not decide main/OFF/SHIFT higher signed-real periods or assign their
integer-termination result or clock formula (10) to this linear owner.

## 7. Audit decision and limits

| Audit | Result for ANG-20260920-FQC01 | Limit |
| --- | --- | --- |
| T0 full carrier / inverse / IMAGE | ESTABLISHED, entire two-root owner | Critical terminal objects and all incoming trees retained |
| T1 arithmetic mechanism / clock | Explicit partial divisor deformation and owned clock | Original divisor arrows not fully preserved; stronger naturalness OPEN |
| T2 native arithmetic returns | FAILS: all nonnegative integer seeds terminate within one step | Higher signed-real source periods UNCLASSIFIED |
| T3 trace / zeta / operator | NOT SUPPLIED / NOT PURSUED | No borrowed analytic object |
| Classical A0/A1/A2 | NOT APPLICABLE | No symplectic base/suspension construction |
| Formal Route / Route B | UNASSIGNED / NOT INVOKED | No formal evaluation |

Portfolio STOP / FORK. The same-object ledger stayed intact: actual
factor transport, floor permission, critical terminal rule, area IMAGE, full-point
clock and complete lag/packet conventions belong to one frozen owner. It
was not repaired by choosing one root, restoring a critical arrow, changing
the measure, importing a prime time or borrowing a control packet.

The native seed obstruction is exact and structural, not a numerical lack
of success. It is not a theorem that the entire signed-real carrier
has no higher period or no positive time. The all-plane short-return
test, nonnegative no-cycle identity and nonnegative INTEGER one-step termination
are different statements with different domains; all three limits are retained.

All arguments are exact, without scientific numerical runs, precision/cutoff,
external literature or source/zero data. Internal ARS original-card, synthesis
and adverse review is NOT_CALIBRATED, not external peer review, machine
proof or independent-error evidence. No RH or Hilbert--Polya claim follows.

Evidence: [card](candidate-card.md), [ledger](claim-ledger.md),
[inputs/checks](evidence/README.md), [review](evidence/independent-review.md),
[source/frontier](evidence/scout-record.md), [package](README.md).
Positive 304, partial-positive 320 and older packages unchanged; 241/242
paused; goal active. Markdown only; no publication/upload, PDF/LaTeX,
Git staging or commit.
