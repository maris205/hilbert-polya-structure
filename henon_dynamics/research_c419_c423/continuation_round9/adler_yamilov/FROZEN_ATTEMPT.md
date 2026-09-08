# AY9: frozen all-parameter structural-atlas attempt

2026-09-08 UTC. This is the ninth-pass continuation of the original
[AY7 contract](../../continuation_round7/nonlinear_scout/SCOUT_REPORT.md),
under the [round plan](../PLAN.md). AI-assisted author work; no new
contract, admission, mathematical review or manuscript is asserted.

## Original question, domain and clock retained

For every integer $k$, keep
$$
Y_k(p,q,r,s)=\left(r-\frac{kp}{1+ps},s,p,
q+\frac{ks}{1+ps}\right),
$$
and its displayed inverse
$$
Y_k^{-1}(p,q,r,s)=\left(r,s-\frac{kq}{1+rq},
p+\frac{kr}{1+rq},q\right).
$$
Classify all states whose entire ordinary periodic orbit is integral,
with the actual coordinates and exact least native period, for all $k$
without parameter, height or period cutoff. Ordinary means both displayed
formulas remain defined at all positive and negative iterates; neither
pole is filled even at $k=0$. Individual zero coordinates remain allowed.
One displayed forward application is one native step. Cyclic rotation
can present a cycle once but cannot change its least period.

**Full-atlas status on entry: NOT CURRENTLY JUSTIFIED.** A fixed-parameter
finite graph, a list of possible periods, or finitely many fixed-locus
equations without solving their integer families will not replace it.

## Accepted inputs, not rerun

The complete eighth-pass [proof](../../continuation_round8/adler_yamilov/PROOF_PACKAGE.md),
[nonauthor review](../../continuation_round8/adler_yamilov/COORDINATOR_HELPER_REVIEW.md)
and [source audit](../../continuation_round8/adler_yamilov/SOURCE_AUDIT.md)
were read as accepted inputs. For $k\ne0$, their conclusions include:

- $D_n=1+p_ns_n\ne0$, $E_n=D_{n-1}\ne0$, $D_n\mid k$ and
  $h_n=k/D_n\in\mathbb Z\setminus\{0\}$ on an integral cycle.
- The zero-safe quotient satisfies
  $D_{n+1}+D_{n-1}=a/D_n+k^2/D_n^2$ for one invariant $a$.
- Every nonzero rational periodic state has quotient least period
  $m\in\{3,4,5,6,7,8,9,10,12\}$ and native period $N=m$ or $2m$.
  This includes singular fibres and coordinate-zero states.
- Over a nonzero rank-one product matrix the return is a free rational
  scaling; an actual periodic lift requires its multiplier to be $1$
  or $-1$. Quotient torsion alone does not force such a lift.
- The origin is fixed. The unchanged $k=0$ pair-swap boundary has native
  periods one or two. The prior height bound and diagnostic are not new
  results in this pass.

## Concrete mechanism to test

Use the joint arithmetic restrictions, not just the period bound:

1. Express the quotient recurrence and the two coordinate-channel
   monodromies through the nonzero integer coefficients $h_n=k/D_n$.
   Keep the product-matrix compatibility and all zero-coordinate cases.
2. For each of the finitely many allowed quotient orders, combine its
   return condition with rational scaling multiplier $\pm1$ and
   $D_n\mid k$. Seek a uniform descent, a forced small coefficient,
   or an explicit finite family of Diophantine parametrizations.
3. Reconstruct every integral rank-one factorization and its native
   orbit. Prove necessity and sufficiency of all parameter/divisibility
   conditions and determine the actual least period, not a divisor bound.

A useful falsifiable stronger hypothesis is that nonzero integral
cycles might have only native periods three, six and eight. **This is
not assumed and is not a theorem.** An exact ordinary integral cycle
of another period would refute that rigidity proposal but would not
by itself answer or replace the full structural atlas.

## Success and failure boundaries

Success is an exhaustive all-$k$ family theorem, including exceptional
parameters, poles, zeros, sign variants and least periods, with every
direction proved and a clear deduction of classical/source ownership.
The coordinator retains nonauthor review and admission decisions.

Failure of the proposed rigidity, an unsolved higher-order arithmetic
stratum, or a reduction only to new per-$k$ boxes leaves the original
atlas unclosed. Record the exact obstruction; do not promote an isolated
new cycle, a low-order-only classification or a bounded census to a
smaller fifth contract. Do not rerun accepted eighth-pass mathematics.

## Execution and ownership boundary

No mathematical program has run in this pass at freeze time. At most
one new exact diagnostic is available, only after a separate protocol
records its fixed inputs, purpose, expected output, failure interpretation,
and caps of 60 CPU seconds and 256 MiB working memory. All actual
executions, including failures, must be recorded. No silent range
extension, old diagnostic rerun, GPU, paid model, source-PDF save or
Git mutation is authorized here.

Write only `continuation_round9/adler_yamilov/` with `apply_patch`.
No global index, P7 file, original contract or old proof is edited.
Any helper delegation first goes through the coordinator's reserved-slot
decision. The batch skill and proof-writer preserve the full-question
gate; research-lit/ARS are limited to actual primary-source verification.
No optional external-model, bibliography resolver or human-read
attestation is activated. NO_BAD_EULER_OR_ROOT_NUMBER remains unchanged.
