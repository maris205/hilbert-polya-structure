# Bounded mathematical review — ASFS-20260915-DCH01

**Date:** 2026-09-15.  
**Scope:** propositions, full-state ownership and claim strength in the
[paper](../paper.md), [card](../candidate-card.md), and
[claim ledger](../claim-ledger.md).  
**Result:** no mathematical defect found in the displayed construction or
proofs; one abstract-level quantifier clarification recommended.  
**Candidate status retained:** ARITHMETIC RETURN AND FULL SYMPLECTIC LEDGER
ESTABLISHED; PRIME-LOG CLOCK FAILS. Portfolio: retain positive control; fork.

This is a separately assigned internal model check, not human peer review,
a calibrated review panel, a journal recommendation, or formal Route
evaluation. The reviewer saw the candidate manuscript and the bounded task,
but no other reviewer report. Model/context separation does not establish
independent error processes. No cross-model service or manuscript upload was
used. ARS review integrity boundaries are applied only at this bounded scope:
anchored claims, preserved uncertainty, and a separate report rather than
edits to the submitted manuscript. No full ARS panel or editorial workflow is
claimed.

## 1. Reconstruction and exact checks

The reviewed object has all integer labels n>=2, scan phases
J_n=Z/max(1,n-2)Z, counters Z/nZ and a plane over every discrete state. The
only arithmetic update is the displayed guarded proper-divisor test. The
transverse coefficient is the fixed number 3; the roof is the fixed number 1.
There is no selected prime subfamily or later change of owner.

| Exact claim | Independent check | Finding |
| --- | --- | --- |
| Proposition 1: smooth two-dimensional carrier | The index set is countable; the disjoint union of countably many Euclidean charts is Hausdorff and second countable. Every component is open. | Correct; neither connectedness nor compactness follows or is claimed. |
| Proposition 1: global inverse and symplecticity | Recover previous j, subtract h at that j, then use (q,p)=(3q'-p',q'). Pullback dp wedge (3dp-dq) equals dq wedge dp. | Correct for every component, including n=2 and n=3. |
| Section 2: complete suspension | Positive unit roof and all positive/negative iterates give finitely many roof crossings on bounded time intervals. Returning height modulo one requires integer elapsed time. | Correct; flow lengths equal full base periods. The three-dimensional suspension is not called symplectic. |
| Proposition 2: arithmetic count | A full scan visits d=2,...,n-1 for n>=3. The n=2 guarded test is zero. Thus 0<=a_n<=n-2<n, and a_n=0 exactly for primes. | Correct; the strict bound excludes counter wraparound falsely identifying a composite as prime. |
| Theorem 3: discrete periods and packet multiplicity | Returning j requires k L_n steps; the counter then returns exactly when n divides k a_n. Least k is n/gcd(n,a_n). Dividing n L_n states by their common least period gives g_n cycles. | Correct; all counters and cyclic phases are retained. |
| Theorem 3: full geometric periodic set | Eigenvalues of B are (3 plus/minus sqrt(5))/2, positive with one strictly above and one strictly below 1. Hence B^m-I is invertible for every positive integer m. | Correct; every periodic point on the entire manifold must have q=p=0. This is a solution of the full equations, not centre selection. |
| Low-integer boundary | For n=2 and n=3, L_n=1, a_n=0 and g_n=n. | There are exactly five distinct primitive base fixed-point orbits, hence five primitive suspension circles of length 1. No exceptional multiplicity is lost. |
| Monodromy | The derivative along every component step is B; an ell_n orbit therefore has B raised to ell_n. Its det(I-B raised to ell_n) is nonzero, not identically 1. | Correct; no operator trace follows from the area Jacobian. |
| Proposition 4: ordinary product | With sigma>0, g_n<=n and ell_n>=max(1,n-2). The absolute log sum is bounded by a constant times sum n exp(-sigma ell_n). | Correct, locally uniformly on Re(s)>0. This proves the declared scalar product, not a Fredholm determinant or continuation. |
| Proposition 5: prime clock | For p>=3, a_p=0 gives g_p=p and ell_p=p-2; at p=2 the length is 1. | Correct. Any fixed positive scaling still gives length/log(p) tending to infinity. |

No numerical experiment was needed: the finite permutation order, matrix
eigenvalue argument and convergent-series bound cover all states and all
positive periods exactly. There is no orbit cutoff, numerical tolerance or
finite-to-infinite extrapolation in this review.

## 2. One wording issue: marked existence versus universal return

The initial abstract says that primality is equivalent to return after one
complete scan. Read literally as a claim for every complete state, this would
be too strong: even at prime n, any nonzero transverse vector fails to return.
The formal statement (5) is correct and has the needed quantifiers:

~~~text
n is prime iff Fix(F raised to L_n) intersects the marked fibre M_n.
~~~

The minimum clarification is to make the abstract say that a marked integer
fibre contains a full-state return after one complete scan exactly when its
label is prime. Alternatively it may explicitly discuss zero counter
displacement, rather than unconditional full-state return. No theorem,
formula, frozen definition or status needs to change. This report records
the recommendation; manuscript integration is owned by the root author.

**Adjudication, 2026-09-15: ADDRESSED.** The root author changed the abstract
to the marked-fibre existence formulation quoted above; the reviewer checked
that exact revised sentence in the current paper. This is a textual
quantifier clarification only, with no formula, candidate definition, roof,
proof or status change. The original finding is retained as the review
history, and no further mathematical rerun is needed. This report has no
paper-hash binding to update.

The same qualification should accompany summaries: the proof uses conserved
n and the scan normalization L_n. It does not establish that an unmarked
orbit length alone canonically identifies a prime.

## 3. Source and gate interpretation

The distinction from [052](../../052-hyperbolic-wheel-packet-lift/paper.md)
is substantive but limited. Here h is evaluated by the actual map and changes
the full-state return order. Suppressing h changes composite returns, while
constant forcing prevents the marked one-scan selector. The source is thus
not merely a precomputed prime label attached to a source-independent
periodic permutation. The separate [140 construction](../../140-cyclic-divisor-counter/paper.md)
is an antecedent with the same discrete formulas; the present proof supplies
its own geometric owner, full periodic classification and roof.

The strongest remaining objection is naturalness, not the proved arithmetic
count: finite counters and a generic hyperbolic plane can realize many
bounded witness predicates. Conservation of an integer label does not by
itself refute endogenous local divisibility, but the construction does not
prove that its marked labels are canonically recovered from unmarked
symplectic geometry or that this arithmetic algorithm is privileged by the
Riemann problem. The manuscript appropriately keeps those issues OPEN.

The owner-level periodic ledger and ordinary-product results are correct.
They should continue to be called components or positive controls, not an
unqualified A0+A1+A2 success chain: prime multiplicity is p, composites remain,
the owned prime clock fails the logarithmic target, and no operator or trace
has been supplied. No formal Route coordinate is warranted. Route B remains
NOT INVOKED.

## 4. Handoff

The same-object ledger survives this check. Retain the exact source-return,
geometric and local analytic results, clarify the marked-return quantifier,
and keep the portfolio decision to fork on clock/target architecture. Do not
repair the target fit by replacing the roof, selecting one of the p packets,
or claiming that the scalar product supplies an unavailable operator owner.
