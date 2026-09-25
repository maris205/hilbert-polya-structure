# Gaussian-rational cycles and their owned area clock

Paper404 — `404-gaussian-cycle-norm`.
Candidate ID: `ANG-AUDIT-20260922-GCN01`; 2026-09-22.
Outcome: GAUSSIAN CYCLE NORM FILTER ESTABLISHED; NON-GAUSSIAN PRIME-3 CONTROL — CONDITIONAL FILTER / FORK
Classical NOT APPLICABLE; T3 NOT AUDITED; formal UNASSIGNED; B NOT INVOKED.

## Abstract

For one fixed partial complex rational-branch owner, with its own Lebesgue
area IMAGE and pointwise holomorphic derivative clock, we identify the entire
physical return group of every eventual cycle. If its cycle lies in Q(i),
each prime congruent3 modulo4 has even valuation in the positive primitive
multiplier. In particular such a cycle cannot supply primitive log3, log7,
or any log p with p congruent3 modulo4. This is a conditional filter, not a
new arithmetic source or a prohibition on all complex dynamics. Own linear
controls realize log2 and log5; an own quadratic control has TWO distinct
non-Gaussian fixed-basin packets of primitive log3. All terminals, critical
exclusions, inverse branches, cuts, incoming histories and phases remain.

## 1. Identity, question and provenance

The [frozen card](candidate-card.md) specifies full X=C, area mu, a fixed
Borel legal domain D with countably many disjoint Borel branches P_i, and
one f_i in Q(i)(z) per branch. On P_i there is no pole or critical point,
and f_i is injective with its actual Borel inverse. T=f_i there; all X\D
are forward terminals, not absorbing fixed points. The prescribed legal
step clock is kappa(z)=log|f_i'(z)|^2 using the displayed extension even
at assigned cuts. It is not an a.e.-only density chosen after seeing cycles.

| Item | This exact owner |
| --- | --- |
| Carrier and measure | Whole C with two-dimensional Lebesgue |
| Arithmetic input | Fixed rational branches over Q(i), no prime/zero data |
| Actual action | Partial deterministic Borel map with ALL actual inverses |
| Time | Owned area-Jacobian cocycle on full real extension |
| Packets | Actual retained-lag histories; full eventual cycles and phases |
| Classical map/roof/suspension | NOT APPLICABLE, not supplied |
| Trace, zeta, operator, quantum lift | NOT AUDITED / not constructed |
| Controls | Three separate full-plane owners, proved below |

The motivation is the prior divisor-symbolic to nonlinear complex geometry
arrow. This class test isolates an arithmetic limitation of that area clock;
it does not deliver the missing endogenous prime-symbolic source or inherit
another candidate's credit. Floored or piecewise constructions must still
give their own complete domains and pointwise prescription to use this lemma.
Strong naturalness, a classical realization and full prime coverage are not
established. No novelty claim, literature comparison or numerical census is
made. Definitions preceded CP1 release; informal mathematical design exposure
is not a blind prediction. Review is internal, shared-history NOT_CALIBRATED.

## 2. Every-Borel IMAGE from the same branches

Write f_i'=a+ib. Its real derivative matrix is [[a,-b],[b,a]], with determinant
a^2+b^2=|f_i'|^2>0. The inverse branch theta_i on f_i(P_i) therefore has
the prescribed positive finite local derivative

J_i(w)=1/|f_i'(theta_i(w))|^2.

The rational extensions are smooth away from their poles and critical
points. Cover each such regular region by countably many open inverse
charts; refine to disjoint Borel pieces and apply the ordinary real
change-of-variables identity on each. Injectivity of f_i on P_i prevents
duplicate source images. Countable additivity yields, for EVERY Borel
E subset f_i(P_i), mu(theta_i E)=integral_E J_i dmu. This applies to assigned
boundary and null subsets too; the fixed extension, not the measure identity
alone, supplies their all-point values. It is a branch IMAGE identity, not
a false global formula for overlapping many-to-one images.

For a valid prefix define A_m(z)=product_{j<m}|f_{i_j}'(T^jz)|^2>0,
A_0=1; S_m=log A_m. The product equals the real Jacobian of the composed
selected analytic germs, also when the actual itinerary lies on a cut.
It need not be a global derivative of a discontinuous piecewise T there.

## 3. Actual histories, kernels and the entire return group

Use all triples g=(z,m-n,w) with legal finite T^m z=T^n w, and identify equal
triples. The clock is c(g)=log(A_m(z)/A_n(w)). If another presentation has
the same lag, its two lengths differ by the same integer. After orienting
that difference positively, the added common tail contributes equally to
both sums. Thus c is independent of presentation. Common-tail refinement
also proves composition and inversion. No extra free branch words exist.

The FULL kernels, including nontrivial coalescing arrows, are exactly

K={ (z,m-n,w): T^m z=T^n w, A_m(z)=A_n(w) },
M={ (z,0,w): T^m z=T^m w for some valid m },
K intersect M={ (z,0,w): T^m z=T^m w, A_m(z)=A_m(w) }.

These existential descriptions are exact and not finite truncations. A
terminal or a point with no eventual cycle has source isotropy {0}. If a
point eventually enters a least q-cycle x_0,...,x_{q-1}, its source isotropy
is q Z: any nonzero return lag makes its forward tail periodic, and all
multiples of the least period occur. Let C=sum_{j<q}kappa(x_j). Tail terms
cancel, so c(jq)=jC and the ENTIRE H=C Z, not a larger group manufactured
by incoming branches. When C!=0 the physical primitive is |C| and the
extension isotropy is trivial. When C=0, H={0} but extension isotropy is
still q Z. Acyclic/terminal tails have both isotropies trivial and H={0}.

For a cycle O retain the full basin B(O)={w:T^Nw in O for some valid N},
with every actual inverse history, including non-Gaussian w. Distinct
periodic cores cannot share a basin: deterministic forward iteration
would otherwise eventually equal two disjoint cycles. This also prevents
packet merging merely because their C values agree.

The full extension has arrows (w,h)->(z,h+c), for ALL h in R, and only an
orbit SET is asserted. If T^Nw=x_j, the representative height at x_0 is
h-S_N(w)+S_j(x_0), modulo C Z. Changing N or cycle phase changes this by
a multiple of C. Thus phases are R/|C|Z when C!=0 and R when C=0; height
translation traverses one physical packet per eventual-cycle basin. All
repetitions are integer multiples in this same H. No nonexistent step
at a terminal is assigned a clock.

## 4. The Gaussian norm obstruction, with elementary proof

Take a legal least q-cycle with x_0 in Q(i). Forward rational evaluation
with no poles keeps every x_j in Q(i), and f_i'(x_j) in Q(i)^*. Hence

lambda=product_{j<q} f_{i_j}'(x_j) in Q(i)^*,
exp C=|lambda|^2=N(lambda) in Q_{>0}.

This is the COMPLEX derivative multiplier lambda; the REAL AREA multiplier
is its norm. They must not be identified. Since the entire H=C Z, if C!=0
the positive primitive multiplier is exp|C|=N(lambda) or its reciprocal.

Here is the needed number-theory restriction without a norm-classification
theorem. Write lambda=(a+ib)/c for integers a,b,c, c!=0 and (a,b)!=(0,0).
Let p be an ordinary prime congruent3 modulo4. If p divides a^2+b^2 and
does not divide b, (a/b)^2=-1 in F_p. Multiplication by a nonzero residue
permutes the p-1 nonzero residues, so cancellation of their product gives
t^(p-1)=1 for any t!=0. For a square root of -1 this instead equals
(-1)^((p-1)/2)=-1, a contradiction. Thus p divides b and then a. Factoring
out their common p-adic power reduces to a pair not both divisible by p,
whose square sum is not divisible by p. Consequently

v_p(a^2+b^2)=2 min(v_p(a),v_p(b)),
v_p(N(lambda))=v_p(a^2+b^2)-2v_p(c) is EVEN.

The formula permits one of a,b to vanish, with v_p(0)=infinity. Both cannot
vanish. Reciprocal norms simply negate these valuations, so the assertion
covers both signs of C. The multiplier p has v_p(p)=1 and is impossible.
Therefore NO Gaussian-rational cycle can supply primitive log p for any
p congruent3 modulo4 under this frozen clock. C=0 supplies no positive
primitive but does not remove its source lag isotropy.

This is necessary, not sufficient: no complete rational-norm theorem,
cycle existence, packet uniqueness, or prime coverage is inferred. In
particular an owner whose ALL periodic cores are Gaussian-rational cannot
cover all primes. An arbitrary owner in this class may have non-Gaussian
cores, and is not excluded. Incoming points can be irrational roots of
rational equations and need not lie in Q(i); they inherit the same core H.

## 5. Own linear controls N and S

N is full C with T_N(z)=(1+i)z; S is full C with T_S(z)=(2+i)z.
Each has its own area measure, global inverse w/a, inverse Jacobian
1/|a|^2 and every-Borel IMAGE from that linear map. Their clocks are
respectively log2 and log5, not borrowed from a divisor or selected atom.
Both are full bijections with no terminals. Their actual groupoids are
the Z-action triples z=T^{-k}w, with c=k log|a|^2.

Since |a|>1, T^q z=z forces z=0. Thus 0 is the unique periodic point,
least period1, and its complete incoming basin is {0}; all nonzero points
are nonperiodic and not eventually periodic. For each owner K=M=units
and their intersection is units. At0 source isotropy is Z, full H is
log2 Z or log5 Z, and extension isotropy is trivial. Elsewhere both
isotropies and H are zero. All real phases at0 are R/log2 Z or R/log5 Z;
nonzero source orbits retain all heights and have no physical returns.
The unique positive packet in each owner is separate, and repetitions
are its integer multiples. These are assigned-coefficient external
controls, not all-prime or endogenous arithmetic constructions.

## 6. Own quadratic control I and the non-Gaussian boundary

Here T_I(z)=z^2+3/4 at z!=0; 0 is retained terminal. The frozen H_+,H_-
partition assigns every nonzero source once, including the imaginary-axis
cuts. Each nonzero square-root pair has one element in each half-plane;
each forward branch image, equivalently each inverse branch DOMAIN, is
C\{3/4}. At3/4 the only algebraic root is excluded0,
so there is NO actual predecessor, not an extra chosen inverse. At target0
the roots +/-i sqrt3/2 are LEGAL predecessors; retain all their legal
backward histories even though the forward path then terminates.

The two actual inverse branches theta_+,theta_- use both roots and their
assigned source tests. Their own all-point J(w)=1/(4|theta(w)|^2)
=1/(4|w-3/4|)>0 follows from the inverse derivative. On branch cuts the
same local germ value applies. Section2's chart proof yields every-Borel
IMAGE. The own legal clock is kappa_I(z)=log(4|z|^2); it is not constant.

For each valid prefix A_m=4^m product_{j<m}|T_I^j z|^2. Substituting these
EXACT values in section3 gives the full global K,M,intersection and actual
c; noninjective coalescing histories cannot be replaced by units. For
example z and -z with z!=0 coalesce after one step, have equal A_1, and
give a nonunit arrow in K intersect M unless they are the same point.
All acyclic/terminal tails have H=0; each arbitrary legal least q-cycle
has C=q log4+2 sum log|x_j| and entire H=C Z, with precisely the signed/
zero extension-isotropy cases of section3. This is the general exact
ledger, NOT a higher-period census or a claim about its unknown cycle signs.

The COMPLETE fixed set solves z^2-z+3/4=0:

z_+=(1+i sqrt2)/2, z_-=(1-i sqrt2)/2.

Both are nonzero legal sources, with |z_+|^2=|z_-|^2=3/4. Their complex
derivatives are 1+i sqrt2 and 1-i sqrt2, and each OWN area multiplier is3.
Both lie outside Q(i), since sqrt2 is irrational (an integer reduced
fraction squared to2 would have numerator and denominator both even).
Each fixed core has source isotropy Z, entire H=log3 Z and trivial
extension isotropy, with phases R/log3 Z and repetitions n log3.

Their complete basins are B_+ and B_- defined by ALL legal inverse roots
of all depths, equivalently valid T^Nw=z_+ or z_-. These exact sets include
no truncation or representative selection. They are countable (at most
2^N sources at depthN), nonempty and disjoint by deterministic forward
iteration; each is one full primitive packet, not one packet per history.
The height formula of section3 applies to every incoming and every real
phase. Thus there are TWO different fixed-basin packets of primitive log3.
This illustrates BOTH why the Gaussian hypothesis matters and why an
allowed prime time does not establish uniqueness. It is not a counterexample
to section4: the actual fixed points are outside that section's hypothesis.
Other periods are deliberately not classified; the terminal basin is not
mistaken for a zero-clock cycle or deleted to improve multiplicity.

## 7. Assessment and next decision

| Gate / claim | Scoped result | Remaining boundary |
| --- | --- | --- |
| T0 owner / IMAGE | ESTABLISHED conditionally for each frozen full owner | No concrete endogenous source supplied |
| T1 clock | Same-area pointwise clock ESTABLISHED | Prime-symbolic naturalness not established |
| T2 arithmetic filter | Gaussian-cycle p=3 mod4 primitive obstruction ESTABLISHED | Non-Gaussian cores remain outside hypothesis |
| Controls | N/S complete; I complete fixed basins plus exact generic ledger | No higher-period I census |
| T3 | NOT AUDITED | No trace/zeta/operator |
| Classical/formal/B | NOT APPLICABLE / UNASSIGNED / NOT INVOKED | No Route credit |

Portfolio: stop this bounded audit as complete; FORK only to a separately
frozen source if it has a stated lineage and escapes the actual hypotheses.
It is not enough to rename a rational area clock, discard non-Gaussian
packets, rescale time or manually insert missing primes. No next candidate
is authorized within this fifth round. The same-object ledger is intact;
the three external controls neither repair nor convict a different owner.

Evidence: [CP1](evidence/scope-review.md),
[card-only raw](evidence/independent-proof.md),
[final internal review](evidence/review.md).
All scientific results above are exact derivations with displayed inputs;
there are no experiment commands, precision limits or finite cutoff claims.
Mechanical link/hash verification is separate and cannot prove mathematics.

AI assistance disclosure: AI agents supplied mathematical derivation, drafting
and internal review. No human or external mathematical verification is certified.
