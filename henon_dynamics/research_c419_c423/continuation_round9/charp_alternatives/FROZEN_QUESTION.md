# CP9: the characteristic-three equal-weight obstruction

Frozen 2026-09-08 UTC after primary-source screening, before the
period-two hand derivation. Coordinator approved the exact scope by
message. Status at freeze: one generated and frozen question, no
admission, no mathematical execution. This is a known open case selected
for attack, not a newly invented conjecture.

## Exact complete question

For **every** field L of characteristic 3, fix an algebraic closure
Lbar and write k = Fbar_3 inside it. Put

    f(x) = x^4 + x^6,   F_lambda(x) = f(x) + lambda,

and for every alpha,beta in L define

    Prep(alpha,beta) = {lambda in Lbar : alpha and beta are both
                       preperiodic under ordinary iteration of F_lambda}.

Determine a necessary and sufficient condition on alpha,beta for
Prep(alpha,beta) to be infinite. The candidate answer to prove or
correct is

    Prep(alpha,beta) infinite  iff  alpha,beta in k or f(alpha)=f(beta).

A correction must still classify **all** pairs and all fields for this
fixed polynomial. Neither one counterexample, a finite-field census, a
single pair, a single parameter, nor a prescribed-period statement closes
this question. No claim is frozen for other equal-weight binomials.

The clock is ordinary compositional iteration n >= 0, the observable is
an infinite set of common-preperiodicity **parameters**, and points are
geometric points. No scheme multiplicity, Frobenius-time substitution,
additive-module orbit, artificial Euler factor or root number is involved.
NO_BAD_EULER_OR_ROOT_NUMBER.

## Source ownership and exact remaining obligation

[Lee–Nam, arXiv:2509.15079v2](https://arxiv.org/html/2509.15079v2),
Theorem 1.5 / 4.4 and Remark 4.5, is the directly read primary source.
Its binomial exponents have equal weights
3^0(4-1)=3^1(2-1)=3. It proves that an infinite parameter set for a
nonconstant pair forces f(beta)-f(alpha) in {0,1,-1}. The authors explicitly
exhibit this polynomial as a limitation of their fixed-fibre local-height
method: that method cannot exclude the two nonzero possibilities.
Its Theorem 2.1 supplies equality of local canonical heights for every
parameter under infinite common preperiodicity. The paper's standard
function-field reduction is retained, not assumed for arbitrary L without
justification.

[Ghioca–Hsia, Acta Arith. 222 (2026), 1–26](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/222/1/116254/simultaneously-preperiodic-points-for-families-of-polynomials-in-characteristic-p)
is verified at publisher abstract level; its exact strict-inequality
hypothesis is read through Lee–Nam Theorem 1.2. No unaccessed proof is
represented as read. [Asgarli–Ghioca, Math. Z. 313 (2026), article 29](https://link.springer.com/article/10.1007/s00209-026-04043-2)
was checked against the author PDF abstract and main theorem: its proved
family is x^d+lambda, not this binomial.

Thus a complete proof must exclude or fully characterize the exceptional
nonconstant pairs with f(beta)-f(alpha)=+1 or -1. The easy directions and
the reduction to these exceptions remain attributed, not counted as a
new contribution.

## Changed mechanism and hand-only attempt

Test a parameter making alpha part of a genuine two-cycle, rather than
the already exhausted parameters putting it in a one-step fixed fibre.
If t is chosen with f(t)+t=f(alpha)+alpha and t!=alpha, set
lambda=t-f(alpha). Then alpha maps to t and t maps to alpha.
Use the characteristic-three difference identity, the algebraic relation
between t and alpha, and an extension of a pole valuation of alpha to
try to force beta's orbit beyond the escape radius. All roots, possible
cancellations, and the two signs must be addressed uniformly; proving
escape for a numerical alpha or just one branch is insufficient unless
that branch is shown to exist for every nonconstant alpha.

Success: a complete all-pair proof using this mechanism, with the borrowed
height bridge explicit, submitted for nonauthor proof/source review.
Decisive failure boundary: if the two-cycle relation creates another
bounded cancellation, or only a restricted subfamily can be handled,
record the exact remaining exception and stop without weakening CP9.

This is independent of M1/AS2/IR1/P7 and the earlier wild fixed-point
zeta, FAD/Kummer, Nagata and P7-fibre branches. It is not a fifth admission
until actual full proof review and substantive-increment adjudication.
Mathematical programs: 0; no diagnostic allowance has been requested.
