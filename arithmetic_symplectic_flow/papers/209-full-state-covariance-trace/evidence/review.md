# Actual bounded covariance and trace review

**Paper ID:** 209-full-state-covariance-trace  
**Candidate ID:** AQC-20260916-QCV01  
**Research date:** 2026-09-16  
**Actual final-input review clock:** 2026-09-16 10:57:26 UTC.  
**Reviewer invocation:** `/root/carrier_boundary_audit`.  
**Disposition:** ACCEPT THE EXACT REGULARIZATION THEOREM AND ITS SCOPED ORBIT-TRACE MISMATCH; NO AUTHOR-FILE CHANGE REQUESTED.  
**Candidate status:** ADVANCE — INJECTIVE FULL-STATE TRACE-CLASS REGULARIZATION; SCOPED STOP AS AN UNREGULARIZED CLOSED-ORBIT TRACE; NATURALNESS OPEN.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

## Actual review and final input binding

This report comes from a different actual invocation, using the inherited
model and shared context. It is nonblind model checking, not human peer
review, cross-model replication or an independent-error certificate. The
reviewer had previously audited 204 and other cone packages. No helper
review tree, external model, new candidate or formal Route was invoked.
ARS was used only for bounded claim/evidence/reasoning and adverse controls.

During the read-only card stage, before receiving the author manuscript,
the reviewer restored local guidance, read the frozen card and relevant
204 dependency, and independently derived density, covariance faithfulness,
range point separation, trace orientation and the singleton-circle formula.
These preliminary findings were sent to root, then the reviewer went idle
until the actual final-text-ready message. That visible exchange makes the
process nonblind; it is not a second independent proof certificate.

At final readiness the reviewer read the entire 333-line
[paper](../paper.md), [README](../README.md),
[card including appended outcome](../candidate-card.md),
[ledger](../claim-ledger.md) and [evidence index](README.md).
All mathematical and summary claims were checked against the frozen
definitions. No final-text correctness or scope finding required a change.
The following final bytes were then bound by an actual `sha256sum` command:

| Reviewed core | SHA-256 |
| --- | --- |
| README.md | `2c08cd971fd9177894cb314e64fb29ec5e26ea87963d3f81991cc0048499515a` |
| candidate-card.md | `d4646b63fa858cac305667161336d2ba2e721abbdfafcc78ff8b8c1f3f78d3db` |
| paper.md | `21fb155ffd1b5c749fbf4da99d596f93aa7ae17391d764e7fc14bd98eeb1ccdd` |
| claim-ledger.md | `08e9319b63815f9dc2f6783b0ca313afa878520cdc16bab19f445a885c9115c1` |

The evidence index remains unbound for root's completion receipt. The
external Cardiff record is author-disclosed abstract/metadata context,
not a mathematical premise; this review does not attest to reading its
PDF, verify novelty or import a theorem from it. No integrated link/test
run or reopening of earlier packages was performed at final review.
Only this assigned review path is written by this invocation.

## Recomputed decisive arguments

### Enumeration, density and full support

A bound on the frozen height bounds every atom index, numerator,
denominator and tuple length. There are finitely many tuples below each
height, so height followed by lexicographic order gives the claimed
sequence. Coprime rational coordinates ensure vector-level uniqueness;
quotient repetitions are intentionally preserved.

To meet any basic all-norm neighborhood, one needs to control only
finitely many weighted norms. A sufficiently long positive truncation
retaining a nonzero coordinate makes all their tails small. Rational
approximation of the remaining finite coordinates completes the estimate.
The quotient map then sends this dense list to a dense list of quotient
states. Positive summable weights give a probability charging every
nonempty open set, even though no infinite-support state is itself a
sample. Those states remain in the domains of H and of the flow.

The noninvariance argument is also valid: a sampled point has positive
mass, while its actual orbit has arbitrarily many distinct points.
Invariance would replicate that same mass at all those points. This
uses the retained flow's absence of stationary states, not any replacement
by an invariant physical measure.

### Rank-one convergence, faithfulness and range separation

With the first-variable-linear inner product, the rank-one rule
(u tensor v)f=<f,v>u has trace <u,v> and trace norm norm(u)norm(v).
Thus the covariance series converges in trace norm, with remainder
at most B_0 times 2^(-N). Positivity and self-adjointness follow from
the positive partial sums and operator-norm convergence.

The identity

    <Cf,f> = sum_n 2^(-n) abs(f(x_n))^2

shows that ker C is zero: vanishing at the dense samples forces a
continuous actual function to vanish everywhere. Self-adjointness then
gives dense range. Neither property confuses the actual H with arbitrary
almost-everywhere classes in L2(mu).

For two distinct states let d=k_x-k_y. State separation by H implies
d is nonzero. Its continuous function is nonzero on at least one sampled
point, so <Cd,d> is strictly positive. Consequently the actual function
Cd in ran C satisfies

    (Cd)(x)-(Cd)(y) = <Cd,d> > 0.

This proves full point separation by the range itself, including pairs
of infinite-support states, rather than inferring it from rank or a
finite covariance matrix. Injectivity on infinite-dimensional H forces
infinite rank. Compactness precludes a bounded everywhere-defined inverse;
surjectivity would give such an inverse by the bounded inverse theorem,
so the ledger's nonsurjectivity boundary is consistent. No preservation
of constants or algebra closure has been established or assumed.

### Actual trace orientation and the two different tail estimates

Multiplying each rank-one term by the actual R_t gives
(R_t k_(x_n)) tensor k_(x_n). Its trace is

    <R_t k_(x_n),k_(x_n)> = kappa(phi_t x_n,x_n).

This is the forward kernel order, not its complex conjugate and not a
simultaneous shift of both arguments. Boundedness of R_t legitimizes
trace-norm multiplication and summation on the unchanged H. No commutation
of C and R_t is needed.

For finite partial sums, strong continuity of R_t implies trace-norm
continuity term by term. The trace-norm tails are uniformly controlled
on compact time intervals by exp(abs(t)/2) B_0 2^(-N), proving
trace-norm continuity of the full family.

The scalar estimate is stronger and genuinely global in time:
kernel Cauchy--Schwarz and the uniform evaluation bound give
abs(kappa(phi_t x_n,x_n)) at most B_0. Hence the scalar trace series
is uniformly absolutely convergent on the entire real line, its tail
is at most B_0 2^(-N), and abs(T(t)) is at most B_0. The manuscript
correctly distinguishes this estimate from the time-growing operator
trace-norm estimate. Each scalar term is continuous, so T is continuous.

This regularized family is not asserted to satisfy a group law. No trace
of unsmoothed R_t, bounded inverse regularization, positivity of T at all
times or determinant from the different 201 space is inferred.

### Prime circles, mixed states and the exact mismatch

On a singleton circle indexed by a, all w coordinates are constant and
the star feature accumulates phase 2 pi t/log(a). Substitution into the
unchanged kernel gives precisely

    kappa(phi_t x,x) = 1/4 + 2^(-a) + (1/4) exp(2 pi i t/log(a)).

The nonzero fundamental harmonic has least period log(a), with the
correct forward sign. It retains that real clock, but is not a singular
repeat-time distribution and does not assert all Fourier modes occur
in H. Mixed samples, including [q_2+q_3], have positive weights; their
kernel diagonals at zero are at least 1/2. Their contribution is therefore
present, not a hidden closed-state projection.

The geometric comparison distribution is explicitly separate from C.
Its primitive-period weights and positive repetitions give a locally
finite atomic measure: bounded time bounds both a and the repetition
number. It has a positive atom at log 2. In contrast T(t)dt, from a
continuous function, has no atoms. This proves the exact nonidentity
claimed, without denying possible future transformed, smoothed or
renormalized identities under new definitions.

Both sampling perturbations retain full support. Their covariance trace
difference at zero is epsilon times (3/4-5/8), namely epsilon/8,
while the geometry and periodic ledger are unchanged. They are valid
controls, not a revision of the candidate measure. The generic RKHS
control includes bounded evaluation norms, continuous functions and a
countable dense state set; it separately requires a bounded C0 pullback
group for the flow-trace assertion. Thus it does not assume such an
action on an arbitrary RKHS and correctly limits arithmetic specificity.

## Final scope decision

The README, frozen-card outcome, full proof and ledger agree on the
same result. Advance the positive injective full-state covariance and
the actual regularized time trace; stop identifying this trace with
the unregularized atomic closed-orbit benchmark. The original state
space, Hilbert norm, physical clock, source and periodic ledger remain
intact. Naturalness and intrinsic localization stay OPEN.

This review does not supply a self-adjoint generator, Euler determinant,
continuation, target divisor or formal Route result. Any new localization,
invariant regularizer or limit removing C requires a fresh card. The
bounded mathematical review is complete for the four hashes above;
root's integrated verification and closure receipt remain root's work.
