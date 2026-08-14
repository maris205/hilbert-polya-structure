# Paper 31 — Wilson Semiring Verifier Trichotomy

**Title:** *Wilson Semiring Verifiers in Symbolic Dynamics: Matched-Clone,
Pruning, and Clock-Dilution Obstructions*

**Candidate:** SD-C33

Paper 30 proves that every isomorphism-natural invariant built only from the
multiplicative free-commutative-monoid structure and its transported
divisibility, join, incidence, roof, and Gram decorations is copied by a
formal UFD clone.  Paper 31 tests the smallest source-natural enrichment that
escapes that theorem: finite-full-shift alphabet sum
\(F_m\boxplus F_n\cong F_{m+n}\), together with successor and congruence.

Alphabet sum genuinely destroys the bare polynomial-UFD monomial clone:
ordinary polynomial addition would force \(x_2=1+1=2\).  This separation is
presentation-relative.  A matched semiring clone with transported addition
and multiplication copies the full source, the Wilson computation, every
cycle, every roof, and every marked ledger exactly.

The stationary Wilson graph has one simple primitive cycle of graph length
\(p-1\) for each rational prime \(p\).  Its graph-step product is
\[
  D_W(s,z)=\prod_p(1-z^{p-1}p^{-s}),
\]
which specializes to \(1/\zeta(s)\) only at \(z=1\) in the Euler half-plane.
The primary recurrent vertex adjacency is noncompact for every nonnegative
edge-roof allocation with total prime-cycle roof \(\log p\).  First return is
an honest trace-class diagonal operator for \(\Re s>1\), but it changes the
marker from \(z^{p-1}\) to \(z\).  A transient verifier can also be made trace
class, yet all verifier DAGs prune from its power traces and determinant.

The strict route record is

    (A0_STRUCTURAL_ARITHMETIC_RELATION,
     A1_PASS_ANALYTIC,
     A2_FAIL,
     A3_FAIL,
     A4_FAIL)

Decision: **ROUTE_A_REJECTED**.  Route B is locked.  Branch action:
**CLOSE_TERMINAL_SEMIRING_VERIFIER_BRANCH**.  No target-zero data, zero
fitting, supplied prime table, factor table, or Route-B operator enters the
paper.

## Writer-owned files

- `SOURCE_LOCK.md` — frozen source, research hashes, theorem boundary, and
  ownership limits
- `PREREGISTRATION.md` — candidate, information boundary, and falsification
  gates
- `PROOF_PACKAGE.md` — exact propositions, theorems, corollaries, and proofs
- `DERIVATION_PACKAGE.md` — trace-log, product, compactness, and return-time
  derivations
- `LITERATURE_AUDIT.md` — verified primary-source matrix and bounded novelty
  claim
- `NARRATIVE_REPORT.md` — theorem-led interpretation and branch decision
- `PAPER_PLAN.md` — claims/evidence matrix and manuscript architecture
- `ROUND2_CLUES.md` — closure consequences and the Paper 32 reopening
  obligation
- `FIGURE_SPEC.md` — pure-vector TikZ semantics and accessibility constraints
- `main.tex`, `math_commands.tex`, `sections/`, `figures/`, `references.bib`
  — manuscript source
- `main.pdf`, `COMPILATION_REPORT.md` — compiled artifact and objective build
  audit

Experiment code, experiment plans, result ledgers, evaluator files, route
evaluation YAML, manifests, repository-level documentation, plain-text
mirrors, and Git state are outside writer authority and are not modified here.

## Frozen authority status

The infinite conclusions are theorem-backed and do not depend on the cutoff.
The canonical exact authority evaluates all 4,095 integers from 2 through
4096, accepts 564 primes, rejects 3,531 composites and all 13 base-2 Fermat
pseudoprimes in range, reports zero bare-clone addition matches in 144 rows,
and reproduces all 169 sampled operations and every residue path in the
matched clone.  It also records 33 operation-table controls, 1,692
entropy-budget rows, 16 formal trace orders, two exact marker comparisons, and
five universal support wrappers.  The source-separated evaluator passes
26,620/26,620 checks, both the direct and isolated regression entry points pass
18/18 tests, and two fresh runs reproduce the 16 core artifacts byte for byte.
`SOURCE_LOCK.md` records the final authority hashes.
