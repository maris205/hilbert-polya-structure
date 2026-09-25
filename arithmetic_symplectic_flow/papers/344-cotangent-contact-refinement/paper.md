# A full contact realization of factor refinement with one primitive orbit per prime

**Paper ID:** `344-cotangent-contact-refinement`  
**Candidate ID:** `ANG-20260920-CCR01`  
**Date / status:** 2026-09-20; exact construction and full return classification.  
**Portfolio status:** `OWNED CONTACT PRIME PACKETS — SCOPED ADVANCE; NATURALNESS OPEN`.  
**Route state:** broadened owner T0–T2 only; T3 NOT AUDITED;
classical A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED.

## Abstract

The frozen source refines a singleton into its complete factor word and
coalesces longer words by gcd. Its full contact atlas has coordinates
q>0 and xi,z real on EVERY finite positive-integer word. A source step with
leading entry a transports (q,xi,z) to (q/a,a xi,z). The actual retained-lag
quotient is a Hausdorff three-dimensional contact manifold: one noncompact
terminal component and one cylinder times a plane for every prime. This is
proved from the full source basin ledger and all incoming branches, not by
selecting centres. The frozen physical flow becomes
(u,v,z)->(u+t,exp(2t)v,exp(2t)z). Its ENTIRE nonstationary periodic ledger is
exactly one primitive orbit of least period log r per prime r, with all
repetitions on that orbit. Source isotropy and source IMAGE clock are zero;
neither is the physical time stabilizer. Three complete controls isolate
factor refinement, geometric holonomy and the transverse physical dynamics.
This is an engineered, non-Reeb contact flow, not a classical ASFS suspension,
a natural-A0 theorem, an analytic determinant, or a Route result.

## 1. Candidate identity and same-object ledger

| Item | Frozen owner | Status here |
| --- | --- | --- |
| Full atlas | Y=W x T*(R>0) x R, disjoint charts | All words and transverse points retained |
| Contact/symplectic data | alpha=dz-xi dq; cotangent form dq wedge dxi on charts | Exact chart preservation proved |
| Partial source transport | S(w,q,xi,z)=(Cw,q/a,a xi,z) | All branches, terminal and incoming retained |
| Groupoid / full quotient | Actual triples (y,m-n,x), S^m y=S^n x; Q=Y/G | Principal étale owner; Hausdorff contact Q |
| Physical time | Phi^t=(exp(t)q,exp(t)xi,exp(2t)z) | Complete conformal-contact flow on Q |
| Arithmetic | Cover-factor word, gcd coalescence, all positive entries | Basins classified directly below |
| Packet / repetition | Entire Q-flow orbit; stabilizer H=L Z | One per prime; repetitions k log r |
| Measure | counting words x dq dxi dz on atlas | Source IMAGE 1; physical inverse IMAGE exp(-4t) |
| Classical base / roof / mapping torus | Not supplied | NOT APPLICABLE |
| Trace / operator / determinant / quantum owner | Not supplied | T3 NOT AUDITED |

The [original card](candidate-card.md) fixes these definitions before the
reported proof. In particular q>0 belongs to the NEW cotangent base; no
part of old 304's real carrier is silently removed to obtain this result.
The atlas measure is not naively pushed through infinitely many incoming
charts to make a quotient volume. Q has its own descended contact volume,
locally equal to the chart volume; the infinite covering multiplicity remains.

## 2. Question and claim boundary

Can this exact symbolic source be realized by a genuine positive-dimensional
contact owner while its FULL intrinsic physical periodic ledger retains
one primitive log-prime orbit per prime, without selecting centres?

**Theorem (scoped answer).** The frozen Q is a countable disjoint union

```text
R^3  disjoint-union  coproduct_{r prime} ((R/(log r)Z) x R^2),
alpha = dz - v du,
Phi^t(u,v,z) = (u+t, exp(2t)v, exp(2t)z).
```

On the R^3 component u is real; on each prime component u is circle-valued.
The map from the ENTIRE original atlas to this manifold is precisely its
full G-orbit quotient. The only periodic flow orbits are (v,z)=(0,0) in
the prime components; each whole circle is one primitive packet of least
period log r. There are no stationary points and no other positive returns.

This theorem does not say that the factorization macro, scheduling,
representation or physical vector field is uniquely natural. It does not
provide a finite-dimensional global symplectic base map, an invariant-volume
physical flow, a Reeb realization, operator, trace formula, RH information
or formal Route A/B. It does not transfer any old candidate's theorem.

## 3. Definitions, inputs and provenance

W contains the empty word and all ordered finite positive-integer words.
For k>=2, C(a1,...,ak)=(gcd(a1,a2),a3,...,ak); for a singleton C(n)=fct(n).
The empty word is terminal. fct is the complete increasing atom-factor word,
with multiplicity, and fct(1) is empty. A cover atom is precisely an integer
greater than 1 with no proper divisor. No prime table or prime-labelled
return time is input. The normalizations S=(q/a,a xi,z) and Phi are fixed
uniformly at ALL source words, including composite and unit entries.

Elementary factor existence follows by induction: a non-atom n>1 splits
into smaller proper factors until all factors are atoms. For an atom r,
Bezout's identity implies r divides ab only if it divides a or b: if
gcd(r,a)=1, multiply ua+vr=1 by b. Repeated cancellation gives uniqueness
of the multiset of atom factors. Sorting supplies fct. This justifies the
definition; it neither bounds computational cost nor identifies cost with t.

Root saw old positive 304 and partial-positive 320 README outcomes, plus
304 and 268 original-card definitions. Preliminary thoughts predate the
freeze; discovery was not blind. This proof uses no old proof or theorem.
The exact exposure, pending independent source definitions and chronology
are in the [scout record](evidence/scout-record.md) and
[evidence record](evidence/verification.md). There is no external theorem
dependency beyond the elementary arguments explicitly supplied here, no
numerical evidence and no new literature/naturalness claim.

## 4. Method and exact proof

### 4.1 Entire source basin classification

For a word of length k>=2, k-1 consecutive gcd coalescences give its single
gcd g. For g=1 the next singleton step gives empty. For an atom r, (r) is
fixed. For composite g, fct(g) has length at least two; coalescing that
ENTIRE factor word gives r if every factor is r, and 1 if two distinct
atoms occur. Thus every source word reaches in finitely many steps either
empty or a unique singleton (r), r prime. In detail,

```text
B_r = {nonempty w: gcd(w)=r^e for an integer e>=1};
B_empty = {empty} union {all remaining words}.
```

These disjoint sets exhaust W. Every step from a nonterminal transient word
strictly shortens its remaining first-hit time. Therefore no other source
cycle or endlessly wandering source word has been omitted. Unit entries,
mixed prime factors, multiplicities and arbitrary order are all covered.

Let h(w) be the FIRST hitting time of the designated final singleton or
empty; it is zero on those roots. Let A_w be the product of leading entries
on these h(w) steps, with A_w=1 when h=0. These are derived quantities,
not inserted clocks. At the final chart the full geometry is
(q/A_w,A_w xi,z). An additional i>=0 steps at prime r give
(q/(A_w r^i),A_w r^i xi,z). Empty admits no additional step.

### 4.2 All inverses and every-Borel IMAGE

Every predecessor word of v is either a singleton n with fct(n)=v, or,
when v=(g,tail), a word (a,b,tail) with gcd(a,b)=g. These are exactly the
two mutually length-distinguished cases of C's definition. There is no
predecessor restriction on real coordinates. For each branch the inverse is
(Q,X,Z)->(aQ,X/a,Z) on the whole target chart, with a=n in the singleton
case. In particular (1) maps to empty, and every gcd pair is retained.

The forward and inverse real determinants are 1 and 1, respectively.
Moreover (a xi)d(q/a)=xi dq, hence S*alpha=alpha branchwise; the inverse
has the same strict-contact property. These linear diffeomorphisms preserve
Lebesgue measure on EVERY Borel set by change of variables. The formula
is exact at every point, including xi=z=0 and all null sets, not an arbitrary
Radon–Nikodym version at periodic points. Countable branch composition and
restriction yield the same identity on all actual bisections. One must not
sum infinitely many inverse branches and call the noninjective whole S
measure-preserving. The source inverse-IMAGE character is identically zero.

### 4.3 Full groupoid and actual quotient coordinates

Define on every source chart

```text
u_w = log q - log A_w;       v=q xi;       z=z.
```

On B_empty take u_w as a real coordinate. On B_r take its class modulo
L_r=log r. This defines a surjection pi from ALL Y to the displayed
disjoint-union manifold Q_*; each chart maps by a local diffeomorphism onto
its entire indicated component. pi is continuous and open because W is
discrete, and each ordinary real/circle chart projection is open.

For y in chart w_y and x in chart w_x, an actual common future is possible
only within the same basin, and it preserves v and z. In a prime basin it
exists exactly when

```text
v_y=v_x, z_y=z_x, u_y-u_x=j L_r for some j in Z.
```

Indeed after the first hits choose nonnegative i_y,i_x with i_y-i_x=j;
the displayed cotangent formulas give equal complete future states.
Conversely any common transient future can be advanced to the final chart;
a common prime future gives this same equation directly. The retained lag
is necessarily

```text
ell = h(w_y)-h(w_x)+j.
```

In the terminal basin equivalence requires u_y=u_x, v_y=v_x, z_y=z_x,
and its lag is h(w_y)-h(w_x); a common transient future can be advanced
only until empty, which is sufficient. These formulas prove pi(y)=pi(x)
if and only if an ACTUAL G-arrow joins x to y. All incoming classes are
included; no infinite extension past a terminal state has been used.

They also prove uniqueness of lag for every pair of endpoints. In
particular I_x=G_x^x={0} for EVERY x of the main object, including the
prime basins. A prime source-word loop is not a loop at q>0 in Y.

With the prescribed inherited topology, G is locally a graph of a
cotangent scaling between two word charts, at fixed lag. In the prime
case successive possibilities are separated by L_r>0 in u_y-u_x; in the
terminal case there is only one. Hence source and target are local
diffeomorphisms, inverse/composition are continuous and smooth on these
graphs, and G is Hausdorff and principal. Closure under composition also
follows directly by the endpoint/lag formulas (or by advancing two valid
common futures to their available later one). There is no discarded germ
or branch-history multiplicity. As pi is an open quotient map whose fibers
are exactly G-orbits, Q=Y/G is homeomorphic to Q_*. The local charts furnish
its smooth structure, not merely a chosen section of a possibly bad quotient.

On each chart xi dq=v du_w, so alpha=dz-v du_w. Constant changes of u
preserve this form. Therefore alpha descends globally to Q_*, with
alpha wedge d alpha=du wedge dv wedge dz nowhere zero. Each component is
Hausdorff and second-countable, as is their countable disjoint union. It is
a genuine 3D contact manifold. The source atlas measure is its local
contact volume because d(q,xi)/d(u,v)=1; its many-sheeted pushforward is
not asserted equal to that quotient volume.

### 4.4 Owned physical action, contact character and IMAGE

On the full atlas Phi^t exists for every real t, preserves q>0, has inverse
Phi^(-t), and obeys the group law. Its diagonal real action commutes with
every S branch and inverse; equivalently it respects the explicit G
endpoint/lag formulas. It therefore descends to the whole Q. Because A_w
is constant within a source chart, its quotient expression is exactly

```text
(u,v,z) -> (u+t, exp(2t)v, exp(2t)z).
```

Its pullback multiplies alpha by exp(2t). Its forward volume determinant is
exp(4t), and its inverse IMAGE is exp(-4t) on every Borel set, on Y and
locally/globally for the descended contact volume on Q. This is compatible
with source branch IMAGE 1: no claim equates these two distinct transports.
The generator is X=partial_u+2v partial_v+2z partial_z, with
alpha(X)=2z-v and Lie_X alpha=2alpha. It is nowhere zero. It is a complete
contact vector field, NOT the Reeb field of this alpha (which is partial_z),
and it is not volume-conservative. No Reeb time or invariant measure is
substituted after observing periods.

### 4.5 ENTIRE time stabilizers, packets, phases and repetitions

In the terminal R^3 component u+t=u forces t=0. In a prime component,
equality of the complete states is equivalent to

```text
t in (log r)Z,     (exp(2t)-1)v=0,     (exp(2t)-1)z=0.
```

For nonzero t the last two equations force v=z=0. Thus H_[x] is precisely
(log r)Z when x is in B_r with xi=z=0, and is {0} everywhere else.
There are no stationary, dense, or nondiscrete stabilizers. xi=0 is equivalent
to v=0 since q>0; it is a derived periodic locus, not a deleted-fiber rule.

For each prime the whole circle with v=z=0 is transitive under physical
time translation, hence ONE primitive flow orbit, not one for each q or
incoming word. The explicit pi above accounts for all phases and every
incoming word of that basin. Distinct primes lie in distinct full-G
components. The least positive period is log r, since k log r with k>=1
is its entire positive return group. k>1 is a repetition of that same
circle, not a composite-labelled primitive packet. The terminal basin and
every nonzero transverse point have no positive physical return.

Notably I_x={0} even on these circles, and the source IMAGE character is
zero, whereas H_[x] is nonzero there. Physical returns use arrows between
Phi^t x and x, not source loops based at x. Confusing these definitions
would incorrectly erase the very periods of this frozen object.

## 5. Results

The theorem in section 2 follows from 4.1–4.5 on the FULL atlas and quotient.
This is exact symbolic/integer and differential-geometric reasoning, not a
finite census, asymptotic clock estimate or selected-core construction.
Its advance beyond a purely symbolic clock is the explicit Hausdorff
contact owner with an entire primitive ledger and independently frozen
geometric time. It is not a naturalness advance established by these proofs.

## 6. Controls and adverse findings

### 6.1 FACTOR-OFF — composite primitives and retained unit isotropy

Every nonempty word now reaches the singleton n=gcd(w), which remains
fixed, including n=1. Empty is a separate terminal basin. Define h_F,A_F
from this source's own first hit and transports; all gcd inverses remain,
but the singleton inverse exists exactly for target (n). Their geometric
maps still have determinant 1, strict alpha preservation and every-Borel
IMAGE 1, by their own identical diagonal matrices, not the main fct fibers.

For n>=2, the same explicitly checked endpoint equation is
u_y-u_x=j log n with lag h_F(y)-h_F(x)+j, giving cylinder x R^2 and trivial
source isotropy. For n=1, there is no geometric scaling: equivalence is
equality of the three anchor coordinates, with ALL integer lags retained.
Thus each point in the unit basin has I_x=Z, wholly in the zero IMAGE
kernel; its coarse quotient is R^3. Empty has another R^3 with I_x=0.
These formulas verify the control's entire G, incoming and quotient data.

Phi commutes with these own branches and has the same exp(2t) contact
factor and exp(-4t) inverse IMAGE. In every n>=2 component its full return
group is (log n)Z precisely on v=z=0 and zero elsewhere. Unit and empty
components have H={0}, despite the former's lag isotropy. Consequently
EVERY integer n>=2, including composites, supplies one distinct primitive
log n packet. In particular the n=4 circle is not a repetition of the
n=2 circle: their source gcd basins differ. PROVES_TOO_MUCH applies to this
control; factor refinement is doing real arithmetic filtering in the main.

### 6.2 COTANGENT-FLOW — continuum multiplicity on the full fibers

This control has exactly the same specified C,S,G,mu, inverse branches and
quotient as the main object, so the above formulas with identical inputs
verify its ownership and source IMAGE 1. Its DIFFERENT physical action
Psi^t=(exp(t)q,exp(-t)xi,z) commutes with every branch, is complete, is
strict-contact and has forward/inverse IMAGE 1 on every Borel set. On Q it
is (u+t,v,z). Each prime component now has H=(log r)Z at EVERY point,
whereas the terminal component has H={0}. For each (v,z) in R^2 there is
one distinct primitive circle, and different pairs cannot be identified by
G or Psi. Thus continuum many full packets per prime remain. A selected
zero-section ledger would hide this genuine failure. This control shows
that the main's designed transverse dynamics, not cotangent geometry alone,
is responsible for its finite primitive multiplicity. It is not the Reeb
flow of the fixed alpha either; its alpha-value is -v, not identically 1.

### 6.3 UNIT-HOLONOMY — source cycles without physical returns

The arithmetic basins are as in 4.1, but all geometric branches and inverses
are identity on the full real chart, so every-Borel IMAGE is 1 and alpha
is strictly preserved. Equal geometry and the same source basin give
exactly this control's G equivalence. Every prime-basin point has full
source isotropy Z (all prime singleton loops are geometric identities);
terminal-basin points have isotropy 0. The IMAGE character is zero on all
of them. The coarse quotient is one R^3 for each prime basin and one for
empty, using u=log q, v=q xi, z, with all isotropy separately retained.

Phi commutes with these identity branches and descends with its own contact
factor exp(2t) and inverse IMAGE exp(-4t). Every quotient component has
u real, so H={0} at every point. There is no positive primitive time packet
anywhere, although the arithmetic singleton cycles and their full lag
kernels survive. Geometric holonomy, not source periodicity alone, is needed.

### 6.4 Residual design risk

All three controls retain the whole carrier and compute their own inverses,
IMAGE, source isotropy, physical groups and multiplicity. They establish
dependence on three frozen choices; they do not prove these choices canonical.
The macro factorization, gcd schedule, cotangent representation, positive
base and conformal transverse expansion remain engineered. Strong naturalness
is OPEN. The physical flow is nonconservative and non-Reeb. No smoothing,
rescaling, extra density, choice of centre or outside operator rescues that
unresolved gate. This object is retained as a scoped positive construction.

## 7. Gate assessment

| Gate | Evidence on this exact object | Status | Boundary |
| --- | --- | --- | --- |
| Lineage | Proper divisors -> factor/gcd source -> exact contact atlas | OWNED DEFORMATION / REALIZATION | Not a Logistic/Hénon theorem |
| T0 | All inverse branches, principal étale G, full Hausdorff contact Q | ESTABLISHED | Not a classical global symplectic F |
| T1 | Uniform frozen Phi and source cotangent holonomy give exact log r | OWNED CLOCK; NATURALNESS OPEN | Not IMAGE-height time or natural A0 |
| T2 | Full source basins, complete physical stabilizers and all incoming | ESTABLISHED PRIME PACKET LEDGER | One orbit per prime only for this owner |
| T3 | No operator/trace/zeta supplied | NOT AUDITED | No formal determinant credit |
| Classical A0/A1/A2 | Original ASFS contract not realized | NOT APPLICABLE | No rebranding of T-labels |
| Formal Route A / B | No formal evaluation | UNASSIGNED / NOT INVOKED | No Route coordinate or B readiness |

## 8. Conclusion and decision

Portfolio: **advance**, scoped to the exact contact realization and complete
prime-period ledger. **Stop promotion to strong natural A0** while the
designed macro/geometry/flow choices lack an independent justification.
Keep this positive object intact; do not label its untouched points a
failure or retune it. The next programme decision is to compare other
separately frozen source architectures or formulate a genuinely discriminating
naturalness obligation. No new trace/quantization or formal Route evaluation
is implied by completing this audit. Two unfrozen scout definitions are
pending separately, not ingredients or successes of this paper.

## Reproducibility / evidence index

- [Candidate card and appended outcome](candidate-card.md).
- [Claim ledger](claim-ledger.md).
- [Evidence, freeze/FIRST/review chronology and QA](evidence/verification.md).
- [Definition sources, bounded exposures and pending scouts](evidence/scout-record.md).
- [Independent same-model review](evidence/independent-review.md).
- [Package overview](README.md).

The proof has no cutoff, precision parameter, numerical script or external
source lock. File hashes and Markdown checks bind the artifacts, not their
mathematical truth. Same-model shared-history review is NOT_CALIBRATED,
not peer review and not evidence of independent error mechanisms.

EOF — complete first proof record; see evidence for any subsequent revision.
