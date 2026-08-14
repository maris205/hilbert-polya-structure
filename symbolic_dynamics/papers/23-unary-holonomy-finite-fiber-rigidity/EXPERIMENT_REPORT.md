# Experiment Report — SD-C25

## Outcome

The exact suite passes every preregistered E1–E10 audit and supports the
strict closure verdict

`(A0_STRUCTURAL_ARITHMETIC_RELATION, A1_WEAK, A2_ANALYTIC_DETERMINANT, A3_FAIL, A4_FAIL)`

with `ROUTE_A_REJECTED` and Route B locked. No target-zero data were used.

## Exact result census

| Audit | Result |
|---|---:|
| canonical cycles | 4,095 |
| canonical edges checked | 8,390,655 |
| unary maps | 288 |
| terminal/acceptance configurations | 1,054,474 |
| finite-state periodicity comparisons | 8,067,400 |
| Boolean-relation configurations | 1,024 |
| constructive composite witnesses | 11 |
| rational matrix cases | 48 |
| Cayley–Hamilton/LRS residuals | 2,832, all zero |
| nilpotent memorizer controls | 56, all exact |
| canonical block rows | 16 |
| block power-trace rows | 128, through period 32 |
| finite determinant checks | 12, all exact |
| directed-rounding trace rows | 144 |
| recurrent wrapper rows | 40 |
| exact roof/marker rows | 4,095 |
| tests | 32/32 PASS |

E1 certifies (W(C_k)=1^{k-1}2), length (k), holonomy two, unique
minimum marking, and primitivity for every (2\le k\le4096). Static AST
inspection finds no target/factorization call in the candidate constructor;
target predicates live in a separate evaluator.

E2–E4 return zero mismatch across all finite maps, Boolean relations,
constructive composites, exact matrix recurrences, and rational generating
functions. E5 then shows why finite-cutoff success is non-evidence: both
nilpotent architectures fit prime, square, power-of-two, Fibonacci, seeded
random, hash, and signed-rational targets merely by changing stored data.

## Matrix local-factor firewall

For a (d)-dimensional fiber the canonical primitive factor is

\[
  \det(I-w_kBA^{k-1}),\qquad w_k=z^kM_k^{-2s},
\]

not (1-w_k\operatorname{tr}(BA^{k-1})). The frozen exact control

\[
  A=I_2,\qquad B=\operatorname{diag}(1,-1)
\]

has

\[
  \operatorname{tr}(BA^{k-1})=0,
  \qquad \operatorname{tr}((BA^{k-1})^2)=2,
\]

while

\[
  \det(I-w_kBA^{k-1})=1-w_k^2.
\]

Thus first-trace cancellation does not delete the local factor or its second
repetition. The prime oracle appears only in a separate one-dimensional
orbit-level filter control.

## Analytic and wrapper boundary

The fixed finite-block operator retains the theorem-level trace-class domain
(Re s>1/2). The 144 directed-rounding rows are diagnostics only. The
Paper19 and Paper20 imports are certificate-locked and used only for their
licensed transient and recurrent wrapper architectures: the former prunes to
selected loops; the latter clock-dilutes under the frozen short roof and
changes (z^{\ell(n)}) to (z) on inducing. No universal countable-system
impossibility is claimed.

E9 verifies (prod_{(n,d)\in C_k}nd=M_k^2) for every frozen index. Even a
one-dimensional oracle filter keeps (z^kM_k^{-2s}); it does not produce a
one-step (zk^{-s}) factor.

## Reproducibility and scope

The canonical runner performs two complete generator, 32-test, and analysis
runs and requires byte-identical code/result snapshots. It then checks the
Route-A schema, scientific integrity predicates, cache cleanliness, and the
SHA-256 inventory. `source_commit`, `code_commit`, and
`source_lock.code_commit` are sealed by the external multi-stage provenance
protocol. The machine-readable Route-A record is authoritative for the
immutable snapshot hash.

This candidate constructs no self-adjoint carrier, critical-line mechanism,
or Route-B object. The experiments do not claim such mechanisms impossible
in other systems.
