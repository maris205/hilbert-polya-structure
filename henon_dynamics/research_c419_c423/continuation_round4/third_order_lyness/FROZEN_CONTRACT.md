# LY4: signed integral third-order Lyness returns

Frozen 2026-09-08 before new mathematical computation. This is a
source-first research candidate, not an admitted contract or a paper.

## Exact object and complete question

For every `a in Z`, take

`L_a(x,y,z) = (y,z,(a+y+z)/x)`.

The domain is the ordinary two-sided affine orbit with every scalar
coordinate a nonzero integer. No blow-up continuation, canceled `0/0`,
positive-only restriction or bounded coefficient sample is substituted.
The inverse is `(x,y,z) -> ((a+x+y)/z,x,y)`. A unit of time is one
application of the displayed map. Cyclic words represent the same
orbit only up to rotation, not reversal or sign change.

The full question is an explicit necessary-and-sufficient classification
of every such integral periodic orbit for every integer parameter,
including all exceptional parameters and exact least periods. An
infinite family or infinite periodic locus must be stated explicitly;
no finite total-count zeta is assumed. A parameter-dependent finite
search bound alone is not paper-level success.

## Source ownership and proposed residual

The exact recurrence is classical third-order Lyness/Todd dynamics.
Global order eight at `a=1`, the real positive invariant foliation,
rotation-number theorems and elliptic translation are not new claims.
The initial local search found C173/C390 and later two-dimensional
Lyness/QRT rejection records, whose exact scopes must be read before
deduction. Those are not automatically an all-signed-integral
third-order classification. Initial primary leads are Cima–Gasull–Mañosa,
*Dynamics of the third order Lyness' difference equation*,
[arXiv:math/0612407](https://arxiv.org/abs/math/0612407), and the
authors' global-periodicity work. Actual theorem access is recorded
separately; search snippets do not establish applicability.

The proposed residual is a genuinely parameter-uniform arithmetic
exhaustion of ordinary integral periodic words after the above
classical structure is deducted. Its possible new mechanism is a
difference identity eliminating `a`, followed by a full recurrence
section/core theorem. This mechanism is a hypothesis, not yet a lemma.

## Cheap screen and stop boundary

First read closest original statements and existing local contracts.
Reject literal/classical containment before computation. Then derive
the parameter-free recurrence constraints and test whether every
nonexceptional orbit must enter a uniform finite arithmetic section.
Seek explicit section-avoiding families before any census. Do not
assert that real dense rotations correspond to rational points.

No numerical or symbolic program is currently frozen or authorized by
this file. If an exact diagnostic becomes informative, append its
specific finite scope and falsifier before writing/running it. Do not
scan arbitrary parameter/height/period boxes or repeatedly increase a
failed cutoff. An exceptional globally finite-order parameter or a
short invariant identity cannot replace the full theorem for admission.

Stop if the full question is already owned, only a short companion
remains, or a uniform arithmetic component remains without a new
closing mechanism. Preserve that precise gap, not a claim of global
impossibility or novelty. No evaluator, manuscript, C-number or target
arithmetic conclusion follows from the candidate.

## One exact parameter-free falsifier, frozen before execution

Subtracting adjacent scalar equations gives

$$x_{i+1}(x_{i+4}+1)=x_{i+3}(x_i+1).$$

Thus all parameter values at once can be represented by the four-state
successor

$$G(x,y,z,w)=(y,z,w,w(x+1)/y-1),\qquad a=xw-y-z.$$

The parameter is invariant whenever the ordinary successor is defined.
This identity is a proof device, not a newly claimed integrability result.
The classical two-integral mechanism must still be deducted.

The single diagnostic freezes the alphabet
$$V=\{-8,-7,\ldots,-1,1,\ldots,8\}.$$
Build every one of the $16^4=65,536$ ordered states in $V^4$ and every
exact successor remaining in that set, then extract **all** directed
cycles without a period cap. This covers all integer parameters for
cycles confined to this alphabet, not all heights for any parameter.
It is not a selected coefficient rectangle or a rational-point census.

The specific unproved core hypothesis to falsify is: outside the
classical $a=1$ global-order-eight parameter, all cycles with no $-1$
coordinate and least period greater than three have height at most four.
This is an exploratory hypothesis, motivated only by the elementary
three-cycle family and a hand-derived five-cycle at $a=13$, not by a
theorem or a claim that the threshold four is likely correct.

Report all finite cycle words, their parameter and exact period, period
counts, and every counterexample to that hypothesis. Reconstruct each
reported cycle using the original third-order equations and verify its
least period. Use explicit failure exceptions, not `assert`. A complete
output may be exclusively created once in the new directory; never
overwrite an existing result. A failed core hypothesis requires a new
analytic mechanism, not a larger alphabet or a silently raised bound.
No further mathematical run is preauthorized by this freeze.
