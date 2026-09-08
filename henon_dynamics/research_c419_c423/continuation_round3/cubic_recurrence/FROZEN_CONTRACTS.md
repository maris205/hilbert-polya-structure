# Round 3: two exact arithmetic candidates

Date: 2026-09-07 UTC. Author: current internal Codex scout.
This is bounded candidate work, not an admission, manuscript, formal
evaluation, independent review, or a new C-number. Only this directory
is writable by this scout. M1, AS2, IR1 and all sealed packages are not
reopened or rerun. No GPU, paid API, Git operation or external upload.

## Selection comparison before computation

| Candidate | Exact complete question | Closest ownership and decisive risk | Decision |
|---|---|---|---|
| CR1: integer discrete Duffing | For every integer A, classify all ordinary periodic points of F_A(x,y)=(y,y^3-Ay-x) on Z^2, with unit iteration clock and exact least periods. | Sealed C417 already treats every monic integral conservative cubic on all Q^2. This candidate is the literal b=0,c=-A,a=0 subfamily. | Reject at source gate; no computation or fresh proof. |
| CR2: arithmetic McMillan locus | For every integer A, classify the entire rational periodic locus of M_A(x,y)=(y,A y/(1+y^2)-x), including exceptional/singular invariant fibres and exact least periods. | McMillan/QRT owns the invariant and elliptic translation; Mazur owns rational torsion restrictions. C115 owns one low-period map. A real action-angle atlas or a generic torsion reduction would be insufficient. | One remaining deep-screen candidate; freeze below before diagnostics. |

These are the only two candidates selected for this lane. The source-stage
rejection of CR1 consumes no numerical pilot. At most CR2 will receive a
new exact CPU diagnostic, if a precise lemma makes one informative.

## CR1: exact local containment, closed without a scan

The actual [C417 theorem and seven-template table](../../../continuation_c414_c418_round2/papers/C417_integral_cubic/sections/1_introduction.tex)
quantify over f(t)=t^3+bt^2+ct+a with (a,b,c) in Z^3, domain Q^2,
ordinary iteration, and oriented cycles modulo rotation, not reversal.
Its theorem states integrality, at most three coordinate values per
cycle, least periods {1,2,3,4,6}, and at most eleven periodic points,
with the exact equality family. The
[template proof](../../../continuation_c414_c418_round2/papers/C417_integral_cubic/sections/6_templates.tex)
was read to verify that this is an exhaustive classification and not
only a coefficient-dependent escape bound. Substitution a=b=0,c=-A
contains the requested Duffing family verbatim. No mathematical rerun
was used to establish this inclusion, and no new priority is claimed.

The two relative source links above are intended to point back to the
existing sealed batch; they will be checked before handoff.

## CR2: frozen full question

**Object and parameters.** The rational automorphism

    M_A(x,y) = (y, A*y/(1+y*y)-x),  A in Z.

**Domain.** All Q^2. The displayed denominator never vanishes over Q;
the inverse is (x,y) -> (A*x/(1+x*x)-y,x). A rational orbit is not
required to remain integral. We do not replace this by a bounded-height
sample or by rational points on only a chosen smooth fibre.

**Clock and observable.** One application of M_A is one time unit.
The observable is the set of rational periodic points with their
ordinary least periods. Cyclic rotation identifies the same orbit;
reversal and central sign are not silently quotiented. Infinite
periodic loci, if present, must be stated rather than put into a
finite Artin-Mazur point-count series.

**Classical structure to deduct.** The invariant pencil is

    C_(A,K): x^2*y^2+x^2+y^2-A*x*y=K, K in Q.

The invariant, QRT translation description, elliptic parametrization,
Mazur's torsion constraints, and low-period factorization alone are
not the proposed increment. The nearest currently accessed primary
source is Zolkin--Nagaitsev--Morozov, *Dynamics of McMillan mappings I.
McMillan multipoles*, [arXiv:2405.05652v2](https://arxiv.org/html/2405.05652v2),
especially section II, equations (1)--(5), and the octupole analysis.
Its actual version/access dates will be recorded separately; search
engine crawl dates are not publication dates. Local C115 uses the
coordinate-reversed convention with A=-4 and asks only low-period
questions. Local C390 and first-round Somos scouting already deduct
the generic elliptic-translation/torsion mechanism.

**Paper-level success.** An explicit necessary-and-sufficient arithmetic
atlas for every integer A and every rational starting point, with
nonempty rational loci and exact least periods, including all exceptional
parameters, singular fibres, and degeneracies. Merely saying “compute
M_A^n(P)=P for finitely many Mazur-allowed n” is not a substantial
classification. A complete parameter/locus closure must remain after
the classical structure is deducted.

**First cheap falsifier.** Before a census, derive the exact genus-one
translation/torsion and singular-fibre reductions. Try to disprove
any proposed fixed finite-alphabet or finite-total-point shortcut by
an explicit rational invariant fibre on which the map has finite order.
If a genuinely new arithmetic restriction is proposed, freeze that
restriction and one bounded exact test before executing it. A finite
search cannot establish the all-A or all-Q^2 quantifiers.

**Stop-loss.** Stop if (i) an accessed original theorem already gives
this complete atlas; (ii) the surviving statement is only a generic
QRT/Mazur corollary or finite procedure; or (iii) closure requires an
unproved uniform family of rational-point/Diophantine assertions with
no bounded rigorous mechanism. Preserve the precise collision or gap.
Do not open a third deep-screen candidate or broaden samples until
something looks favorable.

## Method and disclosure

The repository `henon-route-a-batch` workflow governs the research gate;
`research-lit` and `idea-creator` supply source-first selection. ARS is
used only for the bounded primary-source verification role, not as a
claim of a full systematic review or an independent review panel.
The current team replaces obsolete external-model/GPU examples in
those skills. Source retrieval is read-only, with no bibliographic
API clients, manuscript upload, or external model calls. No configured
Zotero/Obsidian or local matching PDF/arXiv helper was found in the
targeted availability checks; official browsing is the fallback.

Intrinsic arithmetic is a research preference, not an automatic A1/A2
promotion. No target Euler factors, root numbers, automorphy, target
zero correspondence, or Hilbert--Polya realization is asserted.
`NO_BAD_EULER_OR_ROOT_NUMBER` remains in force.

## Fixed-fibre diagnostic freeze (before its single execution)

CR2's first shortcut test now has a concrete target, found by hand:
$A=-5$, $K=4$, and the rational three-cycle word $(1,1/2,-3)$.
The same fibre is birational to

$$E:\quad Y^2=X^3-74X^2+1625X,$$

with $P=(125,1000)$. Its proposed diagnostic is **only**:

1. exact `Fraction` arithmetic verifies that displayed three-cycle;
2. explicit elliptic-curve addition reconstructs $[n]P$ for
   $1\le n\le12$, checks the curve equation at each step, and reports
   whether any is the identity;
3. for each of those finite points where the birational inverse is
   defined, verify its rational point on the fixed $K=4$ fibre and
   its exact three-step return under the original map;
4. display the first four multiples and preserve an output digest of
   the entire twelve-point rational list.

Expected decisive consequence if no multiple vanishes: Mazur's original
Theorem (7'), printed p. 35, bounds every rational torsion point's order
by twelve. Therefore $P$ is not torsion and this **one** invariant
fibre has infinitely many rational period-three points, once the
birational map and whole-fibre order-three identity are proved.
This refutes finite-total-point shortcuts; it is not a proof of the
all-parameter atlas and is not itself a proposed new paper.

No coefficient sweep, random point search, parameter expansion,
unbounded loop, floating-point arithmetic, downloaded package,
or previously completed program is part of this diagnostic. One
stdlib-only execution is sufficient unless a concrete failure requires
a correction. The explicit identities and exceptional denominators
are to be proved in the associated partial-proof/blockage document.

## Final bounded outcomes

CR1 is rejected as a literal completed C417 subfamily, without any new
mathematical execution. CR2's single frozen diagnostic passed. The
[partial proof](PARTIAL_PROOF.md) establishes infinitely many rational
least-three-period points on the smooth $A=-5$, $K=4$ fibre, including
all chart exclusions and the exact torsion-bound dependency.

This does not close the frozen all-integer-$A$, all-$\mathbb Q^2$ atlas.
The varying torsion-fibre rational loci and the complete singular-fibre
dynamics remain unclassified in this attempt. The
[source audit](SOURCE_AUDIT.md) deducts classical ownership; the
[scout report](SCOUT_REPORT.md) records the exact stop decision and
single execution. Neither candidate is admitted, and no third candidate
or broader parameter search is authorized by these outcomes.
