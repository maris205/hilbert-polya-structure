# Independent internal review — nonnegative geometric quotient

Candidate: `ANG-20260920-GQF01`.
Package: `321-nonnegative-geometric-quotient`.
Status: `OWNED QUOTIENT CLOCK; NO SOURCE CYCLES — STOP / FORK`.
Review calibration: `NOT_CALIBRATED`; internal inherited-model review only.

## 1. Inputs, access order and three checkpoints

The only mathematical inputs actually read were the original 158-line
[candidate card](../candidate-card.md) and the released complete 364-line
[paper](../paper.md). Their measured SHA-256 bindings are:

| Input | SHA-256 |
| --- | --- |
| Original card, first 158 lines | `1075594549a9f0acc9ac94e999e4dde9fada719c65fc01b4ccaa947af0e53534` |
| Released and final paper, 364 lines | `554b6c267e57173e8ab5652b6062cfa602db2416dcfa5d8cc1ab477311289050` |

The card was originally read in full through its original EOF, with its
hash measured, before any manuscript access. The frozen prefix was measured
again before this report; the hash remained the same. No appended outcome
was read. The paper hash and line count were measured immediately before
reading all lines 1–364 through EOF, with no output truncation.

The actual sequence was:

1. Read the original card; independently complete and retain all main and
   three-control raw derivations. Send only metadata that ALL raw was ready.
2. Receive the author's first-draft lock notification: 364 lines and the
   paper hash above, reportedly locked before receipt of any raw mathematics.
3. On explicit authorization, release four messages containing ALL raw,
   ending with the complete raw commitment. Still do not read the paper.
4. Receive explicit paper unlock; measure and read the entire manuscript.
5. Compare every proof and scope claim, then conduct the final adverse check
   and write this reviewer-owned report.

This establishes raw-before-manuscript access. Notice order does not establish
the exact relative wall-clock times of the two agents' private derivations
or writes. The author reports the first draft was locked before receiving
raw findings and that no manuscript revision followed them. The released
and reviewed manuscript has the same actual hash. No earlier or different
manuscript was read; no correction or raw-influenced revision is claimed.

ARS supplied the three-checkpoint adversarial workflow, scope discipline and
fallacy/runtime checks, not mathematical evidence. Its router was fully reread
for this task; the previously read applicable workflow, DA and runtime
references governed the same role. No issue quota or venue verdict was used.

No auxiliary was delegated or consulted. No scout, ledger, other package,
historical proof, peer result or external source was read for this audit.
The paper's references to author-side sources were seen as manuscript text,
but those linked files were not opened or independently source-audited.
There was no numerical experiment, higher-period search, web access or
scientific computation. File hashes and line counts are metadata checks only.

The reviewer shares inherited model/context and substantial prior conversation
history with the author. This is not fully blinded ideation, cross-model
validation, external peer review, machine proof or independent-error evidence.

## 2. Checkpoint 1: complete source and owned clock

The following conclusions were all included in the released raw findings.
Write N(y,z)=1+y²+z for main. On X=[0,infinity)³,
T(x,y,z)=(y,z,N(y,z)/x) has actual domain D={x>0}.
For any target (u,v,w), its complete inverse is

    theta(u,v,w)=(N(u,v)/w,u,v),  E={w>0}.

The numerator is positive. Direct substitution proves a unique predecessor
on E and none on its complement. D and E are relatively open; the
actual branch is continuously invertible between them. This does not make
T onto X, delete a zero face, or give a terminal state a self-loop.
For example (1,0,0) has no predecessor but legally reaches terminal (0,0,1).

On integer inputs, d|(1+b²+c) is precisely integrality of the real
quotient. In particular (d,1,n−2), n≥2, realizes d|n. This is
an actual arithmetic readout, not source permission. All noninteger successors
remain; this audit neither inserts a divisibility gate nor selects integers.

The inverse determinant is −N(u,v)/w². Hence for every Borel A⊂E,

    mu(theta(A)) = integral_A N(u,v)/w² dmu.

This is the full IMAGE law, not an interval/whole-set mass ratio. Smooth
interior change of variables and the null-face correspondence include arbitrary
boundary-containing Borel sets. The analytic branch derivative specifies a
finite positive value at every retained point of E. Its null-point values
are part of the frozen full-point prescription, not forced by the a.e.
measure identity alone; no value is evaluated at illegal w=0.

For a legal source with new third coordinate w=N(y,z)/x,

    J(theta at Tz)=x/w,  kappa(z)=log(w/x).

Both logarithm arguments are positive even when y or z is zero. With
S_k the sum over an actually defined history, an arrow from v to u
meeting after lengths k,l has lag k−l, IMAGE exp(−S_k(u)+S_l(v))
and c=S_k(u)−S_l(v). Its extension sends (v,h) to (u,h+c).
In particular the actual forward arrow has lag −1 and clock −kappa;
the inverse has +kappa. Common legal future extension cancels two
presentations; composition aligns the middle histories at their longer defined
length. No terminal step is evaluated or artificially continued.

For main and separately for the first two controls, the positive interior
is invariant in both directions. There B=log(xyz) satisfies kappa=B∘T−B.
The complete boundary stopping depths are 0 for x=0, 1 for
x>0,y=0, and 2 for x,y>0,z=0. A boundary history cannot
merge with an interior history.

The full chain of a terminal anchor (0,a,b) is explicit. For b=0
there is no predecessor. For b>0,a=0 there is only (1/b,0,0).
For a,b>0 its two predecessors are

    p1=(N(0,a)/b,0,a),
    p2=(N(p1_x,0)/a,p1_x,0).

There is no third predecessor. Each control uses its own N in this
formula, not main's values. Thus all boundary tail classes are complete
chains of one, two or three states, not selected terminal representatives.

Give each terminal B=0 and every other boundary point B=−S, where
S is its own finite clock prefix to its terminal. This produces a
finite Borel potential on all X, satisfying kappa=B∘T−B on every legal
step and c=B(source)−B(range) on every arrow. No log0 is used,
and no global continuity of this piecewise potential is asserted.
Complete extension equivalence is source-tail equivalence plus equality of h+B;
on a boundary chain the phase is h−S. Every source isotropy time
image H is zero. This does not set nonloop cocycles to zero.

## 3. Checkpoint 1: main returns and complete group boundaries

All fixed states would be (t,t,t), t>0, with t²=1+t²+t,
which is impossible. A legal two-step return must satisfy z=x and

    xy=1+y²+x,  xy=1+x²+y.

Their sum gives 0=2+(x−y)²+x+y. The boundary termination result covers
all omitted-looking zero cases; there is no main fixed or two-step core.

The card-permitted short arbitrary-cycle test closes all source periods without
a census. For a supposed period P, its positive register sequence a_i
would satisfy a_i a_(i+3)=1+a_(i+1)²+a_(i+2), indices modulo P.
Summing gives

    sum a_i a_(i+3) = P + sum a_i² + sum a_i,

whereas cyclic permutation implies the left side is at most sum a_i².
Equivalently the nonnegative sum of (a_i−a_(i+3))² would equal
−2(P+sum a_i). This is a contradiction at every actual period.

There are therefore no periodic or eventually periodic main states, no
source isotropy, no nonzero time group and no extension isotropy anywhere.
Every positive history nevertheless continues indefinitely in both directions.
The theorem is not global termination, an asymptotic growth theorem or
an exclusion of every other notion of topological recurrence. Boundary chains
and all nonperiodic positive tail classes remain in the owner. No positive
primitive-time packet exists; an empty packet ledger cannot be repaired by
relabeling a zero-time class or importing a control cycle.

## 4. Checkpoint 1: each control's complete promised scope

### NUMERATOR-UNIT

Its own source is U=(y,z,1/x), x>0, with the same terminal face.
Its unique inverse is (1/w,u,v), w>0, IMAGE 1/w², and
kappa_U=−2log x. Its own interior log-product potential and its own
boundary prefixes give the all-point global coboundary and complete real phase.

Only on the positive interior, U³=(1/x,1/y,1/z) and U⁶=id.
The only fixed state is (1,1,1). All two-step states are
(r,1/r,r), r>0, with exact least period two unless r=1;
the partner is (1/r,r,1/r). The only U³-fixed point is the
unit state. Thus all remaining positive states have exact least period six.
This finite-iterate identity gives the complete 1/2/6 classification without
a higher-period search; U⁶=id is not asserted on terminal boundary states.

Injectivity makes the full basin of each core exactly its finite cycle:
its unique predecessor is already in that cycle, so no external tail can
enter. Source and extension isotropy are PZ for least P=1,2,6,
while H=0. The phase is the real value h+log(xyz), not a
positive-period circle. Boundary chains have trivial isotropy and their own h−S.

### SQUARE-OFF

Its own source is V=(y,z,(1+z)/x), x>0. The complete inverse is
((1+v)/w,u,v), w>0; IMAGE is (1+v)/w² and kappa_V=
log((1+z)/x²). Its own positive-generated boundary chains and its own
log-product/terminal-prefix potential establish global H=0 and the full real phase.

All fixed states reduce to (phi,phi,phi), phi=(1+sqrt(5))/2. All
two-step equations give xy=1+x=1+y, hence only that fixed state;
there is no least-two core. The fixed basin is a singleton by
unique inverse. Source and extension isotropy are Z, H=0, and the
real phase is h+3log phi. Higher source periods are UNCLASSIFIED.
An actual higher least-P cycle, if present, would keep its full PZ
source/extension isotropy and zero time image; H=0 does not erase cycles.

### DIVISOR-UNIT-SHIFT

This own source W=(y,z,(1+y²+z)/(x+1)) is defined on ALL X.
There is no terminal face. Its complete inverse is

    theta_W=(N(u,v)/w−1,u,v),
    E_W={u,v≥0, 0<w≤N(u,v)}.

The upper boundary is included and corresponds to x=0. Every target in
E_W has one predecessor; every other target stays a legal source object
without a predecessor. In particular (0,0,2) is such an object. The
same differentiation form gives its OWN IMAGE N(u,v)/w² on its OWN
domain, and its source clock is log(w/(x+1)), finite on all X.
The image is not assumed open at its upper boundary; no automatic
etale or smooth quotient conclusion is made.

All forward histories are infinite and every state is positive after three
steps. Fixedness would give 0=1; the full two-step equations sum to
0=2+(x−y)². For any supposed cycle, summing
(a_i+1)a_(i+3)=1+a_(i+1)²+a_(i+2) cancels the linear terms and yields
sum a_i a_(i+3)=P+sum a_i², again contradicting cyclic squares.
Thus all source, time and extension isotropy are trivial; no periodic
core or periodic basin exists. This uses W's own no-cycle argument.

On the interior its clock differs from the log-product step difference by
−log(1+1/x), so copying main's potential is false. No main terminal
prefix is available. No global Borel phase potential or transversal is
asserted. Setwise, within each acyclic actual tail class, an anchor and its
unique arrow to a point give the relative real phase h−c(anchor→point).
This preserves all objects and heights without adding a return or section.

## 5. Checkpoint 2: complete manuscript comparison

The measured 364-line manuscript was read in full after raw release and
explicit unlock. Sections 1–7 agree with the released derivations above.
All stated formulas, example substitutions, signs and scope boundaries were
checked against the frozen source rather than a transferred historical theorem.

In particular, the manuscript's full boundary depth and backward-chain arguments
support the global Borel potential, not merely an interior identity. Its
inverse-history and branch-pair IMAGE signs match the forward lag −1 convention.
The main arbitrary-cycle square identity has the correct additional positive
linear sum; W's different identity correctly cancels that sum instead.
The unit-control classification is confined to the positive interior and
retains zero-clock source isotropy. The square-off control explicitly leaves higher
source periods open. W's changed inverse range includes its upper boundary
and is not confused with main's domain or potential.

The paper uses P/P_tilde for the potential where the raw used B;
these are notation changes, not different owners. The reviewer supplied explicit
boundary predecessor formulas in raw; the manuscript's iterated-inverse argument
gives the same complete chains. No additional manuscript theorem had to be
retrospectively labeled a raw result. No scientific or editorial correction was
requested, and the reviewed paper remained the original released hash.

## 6. Checkpoint 3: strongest adverse tests and disposition

The strongest objections are ownership and scope objections, not a fabricated
minor flaw. Zero clock image by itself would not prove absence of
source cycles: the unit control demonstrates this concretely. Main therefore
needs its separate all-cycle contradiction, which is valid. Conversely the
square-off zero-time theorem cannot settle its unclassified higher source ledger.

An interior-only potential would leave null boundary packets uncontrolled. Here
all boundary histories terminate at the stated finite depths, and the
explicit full-point prefix construction closes that gap without log0. This
does not upgrade null values into consequences of an a.e. density alone.

The shifted denominator could invalidate both the main domain and telescoping
argument. Its own full-domain source, closed upper image boundary, finite
clock and separate all-cycle identity handle that change; no main result
is silently inherited. All three controls remain different owners, not repairs.

Absence of exact cycles is not absence of all recurrence, termination of
positive histories or a universal quotient-model obstruction. The manuscript keeps
these limits, retains the arithmetic integrality readout and all failed-integrality
real successors, and leaves stronger naturalness/canonical A0 open. The measure,
numerator and carrier are declared design choices, not proven canonical choices.

Final finding: no blocking or nonblocking manuscript correction is required.
The exact main result and scoped STOP / FORK are supported, with
the same-object ledger intact. Classical A0/A1/A2 are NOT APPLICABLE;
formal Route is UNASSIGNED, B is NOT INVOKED, and no T3,
operator, trace, determinant, smooth-flow or Hilbert–Polya result is supplied.
No new candidate, revised roof, measure or state restriction is proposed
by this review. The report freezes this bounded audit and ends further work.
