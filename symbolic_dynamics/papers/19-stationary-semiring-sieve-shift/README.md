# Paper 19 — A Semiring Sieve Shift

Candidate **SD-C21** asks how far one can push a countable Markov grammar
whose only arithmetic instructions come from the semiring of finite full
shifts.  For $F_n=A_n^{\mathbb Z}$, alphabet product and alphabet-sum give

\[
F_m\boxtimes F_n\cong F_{mn},\qquad
F_m\boxplus F_n\cong F_{m+n},\qquad h(F_n)=\log n.
\]

The paper expands trial division into local states $T_{n,d}$ and
$Q_{n,d,q}$.  Quotients are reached only by successor search; there is no
edge guarded by an existential factor oracle.  A prime input reaches one
self-loop $A_p\to A_p$, while a composite input reaches an acyclic cemetery
ray.  On the whole vertex space the source-weighted adjacency is trace class
for $\operatorname{Re}s>1$ and satisfies

\[
\operatorname{Tr}L_s^r=\sum_p p^{-rs},\qquad
\det(I-zL_s)=\prod_p(1-zp^{-s}).
\]

At $z=1$, the determinant is exactly $1/\zeta(s)$ in the
absolute-convergence half-plane.

## Main decision

The exact identity is real, but its dynamical meaning is sharply limited.
Every trial-division state lies in a transient feeding tree.  Pruning those
states leaves all power traces and the Fredholm determinant unchanged and
reduces the model to the diagonal prime-loop core of Paper 04.  A universal
total-decider wrapper constructs the same kind of determinant for every
decidable support, including squares, powers of two, Fibonacci numbers, and
arbitrary computable predicates.  The mechanism is therefore
**algorithmically non-oracular but dynamically selector-tautological**.

~~~text
GO_SOURCE_INTRINSIC_SEMIRING_VERIFIER
GO_EXACT_PRIMITIVE_REPETITION_LEDGER
GO_WHOLE_OPERATOR_TRACE_CLASS_RE_GT_1
GO_SAME_OBJECT_EULER_FREDHOLM_IDENTITY

STOP_RECURRENT_ARITHMETIC_ADVANCE
STOP_GLOBAL_ANALYTIC_STRUCTURE
STOP_ARITHMETIC_SELECTIVITY
SELECTOR_TAUTOLOGICAL
PRUNING_EQUIVALENT
PROVES_TOO_MUCH

(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_PASS_ANALYTIC,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
ROUTE_B_LOCKED
~~~

## Exact finite certificate

The frozen companion prototype passed 13/13 tests.  It matched independent
prime support through $512$; at cutoff $24$ its explicit quotient-search
graph had 296 vertices and 282 edges, of which exactly the nine $A_p$
vertices were recurrent.  Power traces were exact for $r=1,\ldots,12$.
The sealed source-oracle certificate traversed 1,651 explicit quotient-search
nodes/edges and found zero forbidden factor identifiers or calls.
An independent $37\times37$ rational matrix audit at cutoff $8$,
$s=2$, and $z=1/3$ gave

\[
\det(I-zL)=\frac{772486}{893025}
=\prod_{p\le8}\left(1-\frac{1}{3p^2}\right).
\]

These computations certify the implementation; the infinite statements are
proved independently.

## Reading map

- Paper: [main.pdf](main.pdf)
- Frozen object and roof convention: [SOURCE_LOCK.md](SOURCE_LOCK.md)
- Claims and falsifiers: [PREREGISTRATION.md](PREREGISTRATION.md)
- Proof package: [PROOF_PACKAGE.md](PROOF_PACKAGE.md)
- Operator derivation: [DERIVATION_PACKAGE.md](DERIVATION_PACKAGE.md)
- Research story: [NARRATIVE_REPORT.md](NARRATIVE_REPORT.md)
- Manuscript architecture: [PAPER_PLAN.md](PAPER_PLAN.md)
- Exact implementation report: [EXPERIMENT_REPORT.md](EXPERIMENT_REPORT.md)
- Primary-source and novelty audit: [LITERATURE_AUDIT.md](LITERATURE_AUDIT.md)
- Figure specification: [FIGURE_SPEC.md](FIGURE_SPEC.md)
- Cross-family ideas only: [ROUND2_CLUES.md](ROUND2_CLUES.md)
- Build verification: [COMPILATION_REPORT.md](COMPILATION_REPORT.md)

## Next in-family move

Paper 20 must forbid accept loops created after a completed atom verifier.
The smallest live object is a recurrent semiring-local grammar on all
nonunit full shifts, with no accept/reject predicate—for example an expanded
local presentation of $d\mid m+1$.  Its first obligation is to show that
arithmetic appears in primitive SCCs rather than in determinant-invisible
feeding trees.
