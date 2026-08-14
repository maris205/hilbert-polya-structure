# Preregistration — Paper 31 / SD-C33

Date frozen: 2026-08-14 UTC

## Question

Does a source-natural nonmultiplicative operation on finite full shifts break
Paper 30's transported multiplicative-UFD clone and, if so, can one stationary
symbolic transfer/cocycle turn that separation into an exact prime and
prime-power ledger with an honest same-object trace or Fredholm determinant?

## Frozen source enrichment

The single new source operation is finite-full-shift alphabet sum,
\[
  F_m\boxplus F_n\cong F_{m+n},
\]
used together with the inherited alphabet product
\(F_m\boxtimes F_n\cong F_{mn}\), the common unit \(F_1\), additive zero
\(F_0\), successor, successor order, quotient/remainder, congruence, and
entropy.  The paper tests addition--multiplication compatibility rather than
adding a prime-colored object or a terminal prime table.

## Information boundary

Allowed information is the finite-full-shift semiring skeleton, source
equality and congruence, exact entropy, exact rational/integer arithmetic,
deterministic cutoffs, and evaluator-only trial division used solely to audit
the candidate.  Source constructions must be natural under isomorphisms that
transport all operations and decorations.

Forbidden information is any supplied prime, prime-power, factor, atom-color,
orbit-projector, von Mangoldt, or target-zero table; a candidate-side
primality/factorization call; sampled Riemann ordinates; root matching;
coefficient fitting; post-control changes to the graph, terminal rule, roof,
or marker; and Route B.

## Frozen stationary grammar

For every \(n\geq2\), initialize \(r_{n,1}=1\) and update
\[
  r_{n,k+1}\equiv r_{n,k}(k+1)\pmod n.
\]
The graph block has states \(v_{n,k}=(F_n,F_k,F_{r_{n,k}})\), deterministic
successor edges, and a terminal return edge precisely when
\(F_{r_{n,n-1}}\cong F_{n-1}\).  A failed terminal state has no recurrent
return.  This rule is frozen simultaneously for all \(n\).

Every recurrent cycle receives nonnegative roofs satisfying
\[
  \sum_{e\in\Gamma_n}\tau(e)=\log n.
\]
The primary explicit allocation is uniform.  The graph-step marker \(z\) and
the source-weight parameter \(s\) are frozen before controls.

## Mandatory clone gates

1. **Bare-clone gate.**  Ordinary polynomial addition on Paper 30's monomial
   UFD clone must fail to extend the multiplicative map.
2. **Matched-clone gate.**  A relabeled semiring with transported sum,
   product, successor, congruence, entropy, states, roofs, and markers must
   reproduce every candidate datum exactly.
3. **Arbitrary-semiring gate.**  Boolean, finite modular, polynomial,
   tropical, seeded random operation-table, and relabeled finite-semiring
   controls must be classified by the source-lock axioms rather than by their
   printed names.
4. **Composite gate.**  All composites, including base-2 Fermat
   pseudoprimes in the frozen range, must fail the Wilson return relation.

The candidate may claim only separation from the precise bare clone in gate
1.  Exact agreement at gate 2 is required by naturality, not counted as a
failed experiment.

## Periodic-orbit gates

1. Prove the complete primitive census for all \(n\), rather than infer it
   from a finite table.
2. Distinguish one primitive orbit for \(p\) from its temporal repetitions,
   which carry the legitimate prime-power weights \(p^{-rs}\).
3. Retain the original graph-step marker \(z^{p-1}\) in the raw periodic
   product.
4. Treat Wilson's terminal congruence as a selector-equivalent total
   computation unless recurrence supplies an additional nonterminal
   mechanism.
5. Compile squares, powers of two, Fibonacci numbers, a seeded computable
   support, and arbitrary total deciders as `PROVES_TOO_MUCH` controls.

## Operator-ownership gates

1. A formal periodic trace or product is not an ordinary Hilbert-space trace
   or Fredholm determinant.
2. The primary recurrent operator must be compact before any ordinary
   determinant claim; trace class is required for the standard Fredholm
   trace-log identity.
3. First return must transport the graph-step time.  Replacing
   \(z^{p-1}\) by \(z\) is a change of object and marker.
4. A transient trace-class compiler receives no periodic credit for its
   acyclic verifier DAGs; deletion of those states must preserve all power
   traces and the determinant.
5. The parameter \(s\) must move weights on one fixed graph.  No
   parameter-dependent graph, prime list, or post-hoc orbit deletion is
   allowed.

## Falsification logic

- `GO_BARE_CLONE_SEPARATION` requires a formal contradiction to extending the
  exact Paper 30 monomial clone by ordinary addition.
- `STOP_UNIVERSAL_CLONE_SEPARATION` follows if a matched semiring clone copies
  the complete decorated grammar.
- `GO_EXACT_PRIMITIVE_LEDGER` requires one proved primitive class for each
  prime, no composite classes, and exact temporal repetitions.
- `STOP_WHOLE_VERTEX_FREDHOLM` follows if the primary recurrent adjacency is
  noncompact for every nonnegative exact-clock allocation.
- `FIRST_RETURN_COLLAPSE` follows if the induced determinant is honest only
  after replacing the raw graph-step marker.
- `PRUNING_EQUIVALENT` follows if a trace-class transient realization loses
  every verification state from its closed-walk ledger.
- `CLOSE_TERMINAL_SEMIRING_VERIFIER_BRANCH` follows when all terminal total
  deciders share the same pruning/dilution architecture.

## Frozen outcome

Alphabet sum reconstructs the additive monoid and breaks the bare
polynomial-UFD clone by \(x_2\neq2\).  A matched semiring clone transports the
entire construction exactly.  Wilson's theorem gives one primitive cycle of
length \(p-1\) per prime, with temporal weights \(p^{-rs}\), but the terminal
closure is selector-tautological.  Under total roof \(\log p\), a minimum-roof
edge has modulus tending to one, so the primary recurrent adjacency is
noncompact and lies in no finite Schatten class.  First return restores the
Euler determinant only after changing graph time; a transient version prunes
to the same prime diagonal.  Hence the strict tuple is

    (A0_STRUCTURAL_ARITHMETIC_RELATION,
     A1_PASS_ANALYTIC,
     A2_FAIL,
     A3_FAIL,
     A4_FAIL)

The overall decision is `ROUTE_A_REJECTED`, Route B is locked, and the branch
action is `CLOSE_TERMINAL_SEMIRING_VERIFIER_BRANCH`.
