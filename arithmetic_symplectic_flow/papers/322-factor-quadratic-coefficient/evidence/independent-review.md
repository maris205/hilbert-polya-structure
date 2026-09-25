# Independent internal review — factor-to-quadratic-coefficient feedback

Candidate: `ANG-20260920-FQC01`.
Package: `322-factor-quadratic-coefficient`.
Status: `OWNED TWO-ROOT CLOCK; DIVISOR SEEDS TERMINATE — STOP / FORK`.
Calibration: `NOT_CALIBRATED`; inherited-model internal review only.

## 1. Exact inputs, access order and provenance

The mathematical inputs actually read were the original 161-line
[candidate card](../candidate-card.md) and the released complete 378-line
[paper](../paper.md). The source locks and their different evidence status are:

| Version | SHA-256 | Access / evidence |
| --- | --- | --- |
| Original card, first 161 lines | `d18baee8f8918e64474b7229c3834e9f364e68e308228fbda166748fc841012a` | Measured and fully read to original EOF before manuscript access; prefix remeasured before report |
| Author's first paper, 368 lines | `89831a1a3b5805bb22aa6b58fad6f349850ca0c08c2d395d5a393377bd5abcfe` | Author-reported tool lock before receipt of raw mathematics; not read by reviewer |
| Released/final paper, 378 lines | `0bbc7bd103071a62e7c27fc60ab4998f229a286b612ae9d84bdff359f60a7821` | Measured, then fully read through EOF without truncation at checkpoint 2 |

The actual checkpoint sequence was:

1. Fully reread the current ARS router, retaining the previously read
   applicable workflow, DA and runtime guidance. Read only the original card.
2. Complete all main/control raw derivations personally and retain them.
   Send metadata-only ALL raw ready, without mathematical findings.
3. Receive the first-draft lock notification and explicit raw-release permission.
   Release all raw mathematics in five messages ending ALL RAW FINAL.
   Still do not read the manuscript.
4. Receive explicit unlock for the 378-line version, including the author's
   account of additions. Measure its hash and read all lines 1–378.
5. Compare every claim, verify manuscript-only additions, perform the final
   adverse checkpoint, and write this sole reviewer-owned artifact.

Notice order does not establish exact cross-agent private derivation/write times.
The author reports that the 368-line first draft was locked before any
raw mathematical receipt. That version was not independently opened or reconstructed.

The final paper is not an uninfluenced draft: after raw release, the
author adopted the reviewer's linear-control all-period exclusion and the target
(2,3) predecessor-count comparison. Conversely the first draft already contained
the nonnegative-integer one-step termination proof and the nonnegative-real cycle
obstruction. These two results were NOT in the reviewer's raw release;
they were first verified here at checkpoint 2, not retroactively credited
to raw work. They sharpen the final gate beyond the raw short-return result.

No auxiliary was delegated or consulted. No scout, ledger, card appendix,
historical card/proof, peer result or external research source was opened.
Author-source references seen inside the card/paper were not followed or
independently bibliography-audited. No web, scientific numerical computation, higher-period
census, parameter change or other research-file write was performed. Hashes and
line counts are metadata checks, not scientific runs.

ARS supplied checkpoint, adverse-reasoning and scope discipline, not mathematical
evidence or an issue quota. The same model/runtime and shared conversation
history were inherited. Raw-before-manuscript access does not establish fully blinded
ideation, cross-model verification, external peer review or independent-error evidence.

## 2. Checkpoint 1: complete inverse, image and ownership

Let a=floor x, b=floor y. Main's exact domain is
D={a≠0, a|b, y≠x²}; a≠0 guarantees actual x≠0. The
full map is T(x,y)=(y,x+y/x), without integer-only selection or
replacing x by a. Every point outside D is terminal, retaining
T⁰ and actual incoming histories, not an absorbing self-loop.

A predecessor of target (s,t) must be (r,s), with
r²−tr+s=0. Put Delta=t²−4s. Legal noncritical predecessors require
Delta>0 and are exactly

    r_sigma=(t+sigma*sqrt(Delta))/2,
    floor(r_sigma)≠0, floor(r_sigma)|floor(s).

Each root determines its unique cell and sign because
r−s/r=2r−t=sigma*sqrt(Delta). Thus the card's U/V branches
are exact bijections, with lower floor cuts included and upper cuts
excluded. Both distinct roots are tested. There are exactly zero, one
or two predecessors, counted by summing the two permission indicators; the
full image is where this count is nonzero. Labels locate branches,
not additional groupoid arrows. Delta≤0 has no legal predecessor, and
a root r=0 is always rejected by its actual floor.

The following raw examples were checked directly:

- (2,3) has both predecessors (1,2) and (2,2).
- (0,1) has the unique predecessor (1,0), although the target is terminal.
- (0,0) has none.
- Critical-terminal (-1,1) has both predecessors
  ((1+sqrt(5))/2,−1) and ((1−sqrt(5))/2,−1), whose floors
  are 1 and −1, both dividing −1.

These establish that terminality is not missing incoming status. All other
cuts and critical targets use the same exact enumeration, not a selected
sheet. In particular a retained critical target may receive perfectly regular
incoming arrows even though its own outgoing step is forbidden. Every
main state (x,0) with floor x≠0 legally maps to terminal (0,x).

On each geometric sheet, the rational map is smooth and invertible.
Its actual legal cell restrictions are Borel/half-open. This does not turn
the full partial owner into an everywhere-defined continuous self-map or prove
an etale/Hausdorff quotient. No object outside the domain is deleted.

The factor identity
(xi−x)(xi−y/x)=xi²−(x+y/x)xi+y is exact. At (d,n),
integer permission is d|n, but n=d² removes the outgoing arrow
by the frozen critical rule. This is the explicitly declared lossy
partial-action deformation, not a lossless preservation of all divisor arrows.
The raw audit did not mislabel that declared loss as an inconsistent
definition. Stronger naturalness of the floor gate, coefficient order, critical
exclusion and reference area remains open.

## 3. Checkpoint 1: all-Borel IMAGE and full-point cocycle

For delta=sqrt(Delta)>0, direct differentiation gives

    partial_s r_sigma=−sigma/delta,
    partial_t r_sigma=sigma*r_sigma/delta,
    det D I_sigma=−sigma*r_sigma/delta.

Hence the owned density is J_I=|r_sigma|/delta, finite and strictly
positive at every actual inverse point. On every allowed Borel chart V,
for ALL Borel E⊂V,

    mu(I(E))=integral_E J_I dmu.

This is analytic change of variables restricted to the actual domain,
not a whole-set mass ratio. The explicit analytic formula supplies its
declared full-point version at legal floor cuts. An a.e. measure law
alone does not choose those null-point values. No derivative or continuation
is invented at Delta≤0, a discarded root or a terminal outgoing step.

At the actual source, delta=|x−y/x|=|x²−y|/|x|, so

    J_Bv(Tv)=x²/|x²−y|,
    kappa(v)=log|1−y/x²|.

This is the log absolute forward determinant and is finite on D;
it can be positive, negative or zero. A legal y=0 step
has kappa=0. The critical exclusion prevents evaluating log0. A step
value equal to a prime logarithm would not itself be a primitive return.

For actual histories, the branch-pair IMAGE is exp(−S_m(v)+S_n(w)),
whereas c(v,m−n,w)=S_m(v)−S_n(w), source w and range v.
Thus the forward arrow (Tv,−1,v) has clock −kappa(v), its inverse
+kappa(v). Equal-lag presentations differ by a common legal suffix, which
cancels pointwise. Composition aligns the middle histories at their longer
defined length. This proves the prescribed cocycle even at null intersections
and terminal endpoints, without taking a nonexistent terminal step.

Each inverse level has at most twice as many histories as the
previous level. Both actual roots are retained, while equal triples remain
one arrow. The globally noninjective T must not be assigned an
unqualified single-sheet IMAGE formula that discards overlap multiplicity.

## 4. Checkpoint 1: short returns, full tails and conditional groups

All fixed states would have y=x≠0 and second coordinate x+1,
which cannot equal x. In a legal two-step return, the first
coordinate of T² is x+y/x; equality to x forces y=0,
but then the second step is illegal. Thus there are no fixed
or two-step returning states anywhere in the signed plane or at its cuts.

The raw conclusion was limited: these equations alone do not decide higher
signed-real cycles, a global potential, global H=0 or absence of all
positive packets. No periodic short core was discovered, and no artificial
periodic basin was supplied. The final stronger arithmetic gate comes from
the manuscript-only proofs verified in Section 6 below.

Every terminating basin is nevertheless specified completely by actual roots:
for terminal omega retain all v with T^d(v)v=omega after d legal
steps. Use both filtered roots at each depth, not only initial seeds.
The terminal anchor and depth are unique. Two such states are tail
equivalent exactly when their terminal anchors agree; their arrow has lag
d(v)−d(w) and c=S(v)−S(w). Source isotropy, H and extension
isotropy are all zero on that complete basin, with real phase h−S(v).
This neither bounds total tree size nor asserts that all states terminate.

For any actual eventual cycle of least P, if one exists, let
K be the sum of its own kappa around its full core. Then
source isotropy is PZ and H=KZ throughout its entire predecessor basin.
For K≠0 the least positive time is |K| and extension isotropy
is zero; for K=0 there is no positive primitive and extension
isotropy remains PZ. All these are conditional statements for unclassified cycles.

Choosing q_j=T^j q_0 on the core, a state hitting q_j after
d steps has phase h−S_d(v)+S_j(q_0), modulo KZ when K≠0
and as a real value when K=0. Different hit representations differ
by full-cycle sums. Equal times do not merge different cores, and the
full finite-predecessor basin is retained. No embedded-circle or quotient regularity
claim follows. Non-eventually-periodic classes have trivial isotropy/time/kernel even
when their nonloop clocks are nonzero.

## 5. Checkpoint 1: three own controls

### DIVISIBILITY-OFF and DIVISIBILITY-SHIFT

OFF drops divisibility but keeps floor x≠0 and y≠x². Its inverse
tests both roots with Delta>0 and floor r≠0 only. SHIFT instead
requires floor x|(floor y+1); its roots must satisfy
floor r|(floor s+1). Their exact images/counts use these OWN filters.
Their densities are |r|/sqrt(Delta) and their clocks log|1−y/x²|
on their own domains, not main's histories or predecessor trees.

Raw checked the owner difference at target (2,3): main and OFF
retain (1,2) and (2,2); SHIFT retains only (1,2), because
2 does not divide 3. Both controls retain the two incoming roots
of critical-terminal (-1,1), under their own permission tests. All fixed
and legal two-step returns are absent by the same geometric equations;
higher signed-real cycles were not classified. Terminal phases and conditional
cycle formulas use each control's own filtered history, not a main basin.

### REAL-DIVISION-OFF

This control keeps the full main D, including the critical exclusion,
but uses L(x,y)=(y,x+y). Its unique possible inverse is (t−s,s),
allowed precisely when floor(t−s)≠0, floor(t−s)|floor s and
s≠(t−s)². No discriminant or square-root derivative applies. Its own
inverse determinant has absolute value one, its all-Borel IMAGE density is
one, and its full-point kappa/cocycle are identically zero.

For example critical-terminal (2,4) has its unique predecessor (2,2),
whereas main has none at that target. Fixed and two-step equations
for the unrestricted linear map give only the origin, which is terminal.
The permitted short all-cycle argument uses eigenvalues phi>1 and −1/phi
of [[0,1],[1,1]]; no positive power has eigenvalue one. Every
actual cycle would therefore be the zero vector, which is illegal.
There are no actual cycles or eventual cycles in this control.

All its source/time/extension isotropy is zero. Full extension equivalence is
its actual source-tail equivalence plus equal h. Its terminal basins use
the unique permitted inverse at every depth, with no uniform finite-length
claim. This zero cocycle and all-period exclusion do not transfer to
the nonlinear main/OFF/SHIFT owners. The linear argument was in raw
and, by the author's account, was adopted after the first manuscript lock.

## 6. Checkpoint 2: full manuscript comparison and additional proofs

The released 378-line manuscript was hash-checked and read entirely. Its
inverse, IMAGE, signs, short equations, terminal trees, conditional groups and
controls agree with the raw results. The paper's additional no-inverse example
(1,2) was directly verified: Delta=0, but its own outgoing step
is legal and equals (2,3). The three signed step-clock examples pass
main permission. Every control example was checked under its own filter.

Two author-origin results were first verified at this checkpoint, not in raw:

1. ALL nonnegative integer states terminate within at most one step under
   main. For a legal positive pair (d,n), write n=dq. A
   second step requires dq|(d+q). If min(d,q)=1 and n≥2,
   the sum is n+1. If d,q≥2 are unequal,
   (d−1)(q−1)≥2 implies 0<d+q<dq. Equal d=q was
   already critical; n=1 is the excluded unit-square case. The remaining
   n=0 maps to first coordinate zero, and d=0 is terminal.
   This is a complete elementary first-iterate proof, not a sampled claim.
2. Any nonnegative cycle for main/OFF/SHIFT would be strictly positive:
   a zero first coordinate is terminal, and a zero second coordinate
   reaches terminality next. Its cyclic sequence must satisfy
   a_(i+2)−a_i=a_(i+1)/a_i>0. Summing gives a contradiction.
   Positivity persists as long as defined, excluding nonnegative eventual cycles
   too. This does not prove finite termination of all noninteger positive
   histories, and the signed sector remains outside the sign argument.

The integer seed theorem does not transfer to OFF or SHIFT because
the next-step divisibility condition changed. The nonnegative sign obstruction does
hold for each permitted cyclic history of those controls, separately.

The n=4 example is exact: its only proper divisor 2 is
stopped at (2,4). Consequently absence of an accepted proper-divisor arrow
is not a primality criterion here. This tests the already declared loss;
it does not accuse the frozen card of promising a lossless sieve.

These short exact proofs fall within the card's arithmetic/short-identity gate,
not an enlarged signed high-period census. They support the final native-seed
STOP / FORK more decisively than the reviewer's raw absence of short cores.
The signed-real higher ledger remains explicitly UNCLASSIFIED throughout the paper.

## 7. Checkpoint 3: strongest adverse scope checks and disposition

A first objection is that signed-real higher cycles might exist and could
have nonzero time. The paper allows that possibility. It establishes termination
of the stated native nonnegative integer seeds, not a global no-period or
global H=0 theorem. Any ancestor of such a terminating seed still lies
in its zero-isotropy terminal basin; retaining all incoming roots cannot turn
that basin into a periodic one. Unrelated signed cycles are not erased.

A second objection is that discarding one root or treating a critical
target as deleted would alter multiplicity. Neither occurs: the exact permission
test retains both roots, while terminal objects keep all legitimate incoming
histories. No divergent derivative is assigned to a nonexistent critical-source
branch. Full-point values on legal null cuts remain a declared version,
not a consequence of a.e. density uniqueness.

A third objection is that the common real formula might hide a
control-owner switch. The differing predecessor example, separate linear inverse and
control-specific history formulas prevent that. Step-clock signs are not primitive
times; a zero control cocycle does not establish zero main clock.

The declared lineage deformation and naturalness limits are preserved. Neither
the loss at squares nor the terminating native seeds proves that every
factor-to-coefficient architecture, every signed-real cycle, or every future arithmetic
deformation is impossible. No restoration of the critical arrow, changed measure,
chosen sheet, added roof or borrowed control packet is used as a repair.

Final finding: no manuscript correction is required. The final paper hash
above is supported within its exact stated scope, with the same-object
ledger intact. T3 is NOT SUPPLIED / NOT PURSUED; classical A0/A1/A2
are NOT APPLICABLE, formal Route is UNASSIGNED and B is NOT INVOKED.
No operator, trace, determinant, smooth quotient, RH or Hilbert–Polya claim
is supplied. This report freezes the bounded three-checkpoint audit; no further
period classification or architectural change is authorized by its conclusion.
