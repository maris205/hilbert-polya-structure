# Session 4 Final Synthesis — Symbolic Dynamics

Date: 2026-08-12

Primary system family: **Symbolic Dynamics only**

Route-B evaluations performed: **0**

Riemann-zero data loaded or fitted: **none**

## Executive verdict

Session 4 found no single symbolic construction that simultaneously supplies

\[
\text{rational primes}
\longleftrightarrow
\text{primitive cycles},
\qquad T_{\gamma_p}=\log p,
\qquad
\text{a natural Fredholm divisor},
\]

with the correct repetitions, phases, completed analytic structure, and a
same-clock lift.  Consequently, no candidate is Route-B ready.

The negative result is informative rather than merely inconclusive.  The
session isolates three capabilities in three different objects:

- `SD-C05` generates rational primes and the scale increment \(\log p\)
  endogenously, but its level graph is acyclic;
- `SD-C04` has a natural infinite-dimensional transfer operator and a genuine
  primitive/repetition determinant, but its primitive objects are periodic
  continued fractions and hyperbolic modular classes, not rational primes;
- `SD-C06` naturally produces an exact quotient of zeta functions, but as a
  Dirichlet partition function rather than a primitive-orbit Fredholm
  determinant, and its Liouville sign is additional arithmetic input.

These coordinates may not be combined across candidates.  Their separation
is itself the principal scope-controlled finding.

## Frozen Route-A matrix

| ID | A0 arithmetic | A1 orbit ledger | A2 determinant | A3 global structure | A4 lift | Overall |
|---|---|---|---|---|---|---|
| `SD-C01` | `A0_WEAK_ARITHMETIC_RELATION` | `A1_PASS_ANALYTIC` | `A2_ANALYTIC_DETERMINANT` | `A3_FAIL` | `A4_FAIL` | `ROUTE_A_REJECTED` |
| `SD-C02` | `A0_FAIL` | `A1_FAIL` | `A2_ANALYTIC_DETERMINANT` | `A3_FAIL` | `A4_FAIL` | `ROUTE_A_REJECTED` |
| `SD-C03` | `A0_FAIL` | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_FAIL` | `ROUTE_A_REJECTED` |
| `SD-C04` | `A0_WEAK_ARITHMETIC_RELATION` | `A1_PASS_ANALYTIC` | `A2_ANALYTIC_DETERMINANT` | `A3_PARTIAL_ANALYTIC_STRUCTURE` | `A4_FORMAL_HINT` | `ROUTE_A_EXPLORATORY` |
| `SD-C05` | `A0_STRUCTURAL_ARITHMETIC_RELATION` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FAIL` | `ROUTE_A_EXPLORATORY` |
| `SD-C06` | `A0_ANALYTIC_ARITHMETIC_ORIGIN` | `A1_FAIL` | `A2_FAIL` | `A3_PARTIAL_ANALYTIC_STRUCTURE` | `A4_FAIL` | `ROUTE_A_EXPLORATORY` |

The append-only records are under [`evaluations/route_a/`](evaluations/route_a/).
Every record retains `route_b_invocation_allowed: false`.

## 1. Which symbolic families were explored?

Six frozen families covered the main low- and countable-complexity routes:

1. finite-state full shifts and finite-memory weighted graph shifts;
2. an infinite arithmetic subshift defined by squarefree admissibility;
3. countable shared-base renewal shifts with complex weights;
4. the Gauss continued-fraction shift and Mayer transfer operator;
5. a recursive wheel-sieve Bratteli/level shift;
6. Knauf's number-theoretical binary spin-chain recursion.

The literature audit additionally covered finite/sofic rationality,
finite-group extensions, countable Markov thermodynamic formalism, unary
formal-language limits, and arithmetic \(\mathscr B\)-free shifts.  These were
used as proofs, controls, or collision checks, not promoted to extra candidate
families.  See [`docs/LITERATURE_AUDIT.md`](docs/LITERATURE_AUDIT.md).

## 2. Which constructions were genuinely arithmetic?

Three distinct meanings of “arithmetic” survived scrutiny:

- `SD-C01` is exactly arithmetic over \(\mathbb F_q[x]\): primitive necklaces
  have the monic irreducible-polynomial counts and the repetition ledger is
  exact.  This is function-field arithmetic, not a rational-prime source.
- `SD-C05` has the strongest rational-prime origin.  Starting from the wheel
  recursion, the next multiplier is the least surviving coprime integer, hence
  the successive multipliers are exactly \(2,3,5,7,\ldots\).  The scale roof
  \(\log(Q_{k+1}/Q_k)=\log q_{k+1}\) is derived rather than assigned from a
  prime table.
- `SD-C06` has the strongest analytic arithmetic identity.  Its endogenous
  multiplicities stabilize to Euler's totient, giving
  \(\sum\varphi(n)n^{-s}=\zeta(s-1)/\zeta(s)\) in the proved half-plane.

`SD-C02` contains rational primes directly in its exclusion grammar, so it
fails the strict emergence gate.  `SD-C03` can encode arbitrary analytic data
and therefore has no selective arithmetic origin.  `SD-C04` is naturally
arithmetic in the modular/continued-fraction sense but does not generate a
canonical rational-prime ledger.

## 3. Which constructions had a natural primitive/repetition ledger?

`SD-C01` and `SD-C04` pass A1 for their own arithmetic species.

For `SD-C01`, Möbius inversion gives the exact primitive-necklace counts,
and powers of a primitive word give the correct repetition expansion.  For
`SD-C04`, a primitive digit necklace gives a periodic continued fraction;
matrix products, the derivative roof

\[
T_w=-\log|\phi_w'(x_w)|=2\log\lambda_+(M_w),
\]

and \(T_{v^r}=rT_v\) are intrinsic to the same grammar.

The other objects fail for sharply different reasons.  The squarefree shift
has only the all-zero periodic point.  The renewal shift has natural cycles,
but free concatenation creates unwanted mixed primitive words such as \(ab\).
The wheel construction is a directed acyclic level graph.  The Knauf
recursion supplies a partition function, but no canonical primitive-cycle
decomposition was found.

## 4. Which constructions had a rigorous zeta or Fredholm determinant?

Three same-object determinants are rigorous but target different species:

- the finite full shift has \(D_q(s)=1-q^{1-s}\);
- the squarefree admissible shift has the trivial Artin–Mazur zeta
  \(1/(1-z)\), because it has one fixed point at every period;
- the Mayer operator gives a source-supported nuclear/Fredholm determinant
  for the Gauss/modular periodic objects in its stated function space and
  domain.

The renewal expression is also exact for its own free-concatenation grammar,
but it fails the target because mixed necklaces and arbitrary inverse design
are built into the mechanism.  The Knauf zeta quotient is a rigorous
Dirichlet-series limit, not automatically a dynamical Fredholm determinant.
No determinant in the session was shown to have the completed Riemann divisor.

## 5. Which candidates failed, and why?

- `SD-C01`: exact function-field analogy, but no rational-prime ledger and a
  proved \(O(R)\) divisor-growth mismatch.
- `SD-C02`: prime-square exclusions are inserted directly; moreover all
  nonzero periodic words are eliminated.
- `SD-C03`: arbitrary inverse design reconstructs both on- and off-circle
  controls, while mixed primitive words destroy independent Euler factors.
  It triggers `STOP_SCOPED / PROVES_TOO_MUCH`.
- `SD-C04`: the determinant is natural, but it counts quadratic
  irrationals/hyperbolic conjugacy classes rather than rational primes; exact
  trace collisions also rule out treating matrix trace as an injective label.
- `SD-C05`: its prime recursion and logarithmic scale are endogenous, but the
  strict level order proves that it has no periodic paths.
- `SD-C06`: the unsigned zeta quotient is genuine, but no primitive-cycle
  Fredholm ledger is supplied; the Liouville twist is an added number-theoretic
  observable and the wider convergence claim remains open.

## 6. What analytic obstructions were proved?

The strongest theorem is the finite-memory divisor obstruction.  For a finite
directed graph with finite-range roof and potential and a finite-dimensional
unitary cocycle,

\[
M(s)_{uv}=\sum_{e:u\to v}w_e e^{-s\tau_e}U_e,
\qquad D(s)=\det(I-M(s)),
\]

is a finite exponential polynomial whenever \(D\not\equiv0\).  Jensen's
formula then gives

\[
n_D(R)=O(R).
\]

Finite products and meromorphic quotients of such determinants retain
\(O(R)\) total divisor variation, whereas the Riemann–von Mangoldt law gives
\(\Theta(R\log R)\) nontrivial zeros in a comparable disk.  A zero-free
factor \(e^{g(s)}\) cannot repair the mismatch.

The theorem is deliberately limited to finite state, finite memory/range, and
finite representation dimension.  It does not cover infinite-memory Hölder
potentials, countable-state operators, or genuine infinite-dimensional
Fredholm determinants.

Four further exact obstructions were established:

- the squarefree admissible shift has no nonzero periodic point;
- a shared-base renewal grammar necessarily creates mixed primitive words;
- a finite-dimensional unitary cocycle cannot identically erase those mixed
  factors;
- a unary regular or context-free return grammar cannot select exactly the
  prime lengths, because its length set is ultimately periodic.

Proofs and scope boundaries are indexed in
[`docs/obstruction_registry.md`](docs/obstruction_registry.md).

## 7. Which missing structures appear to require geometry?

The evidence points to, but does not prove, a need for a separate carrier for
three obligations:

1. a canonical phase or holonomy behind the signed Gauss/Mayer sectors;
2. a genuine return-time realization that turns the wheel's scale increments
   into cycles without artificial resets;
3. a unitary, scattering, or Hamiltonian lift preserving the same clock,
   phases, and completed analytic normalization.

These are not developed as constructions in Session 4.  The precise external
ideas are recorded only in [`ROUND2_CLUES.md`](ROUND2_CLUES.md).  The session
does **not** claim a theorem that geometry is universally necessary; it shows
only that no examined symbolic object supplied these structures internally.

## 8. Which clues survive for a later round?

Five clues survive, without promotion to evidence:

- a modular-geometric carrier for the Gauss/Mayer parity sectors;
- a commutative-monoid or operator-algebra quotient to suppress mixed renewal
  words;
- a genuine return-time realization of the wheel scale;
- the spectral-radius/Ramanujan-graph interface noted in Knauf's work;
- a geometric compression that reads the same prime-side information through
  a Weil-type Hermitian block.

All five remain `ROUND2_CLUE`; none was simulated, quantified, or evaluated
under Route B.

## 9. What is the strongest surviving candidate?

There is no surviving full-chain Hilbert–Pólya candidate.

If “strongest” means the next same-family falsifiable research lead, it is
`SD-C05`: it uniquely derives rational primes and \(\log p\) from a short
symbolic recursion.  Its only legitimate next test is to construct or rule out
a stationary natural extension of comparable description complexity, without
prime-indexed components or post-hoc reset edges.  Until that exists, it is
not a dynamical-zeta candidate.

By other criteria, `SD-C04` is the strongest natural determinant and `SD-C06`
is the strongest exact zeta-identity collision.  Those strengths cannot be
transferred to `SD-C05`.

## 10. What is the strongest negative theorem?

`SD-O01`, the finite-memory divisor obstruction, is the strongest reusable
result of Session 4.  It rules out the entire class

\[
\text{finite graph}
+\text{ finite-range clock/weight}
+\text{ finite-dimensional cocycle}
\]

as an exact completed-Riemann determinant up to a zero-free entire factor.
It also shows that finite group phases can remove a local Perron–Frobenius
sector without changing the fatal linear divisor-growth order.  Therefore,
“add more finite states” or “add a finite unitary twist” is not a viable next
step.

## Numerical audit and reproducibility

The four frozen runners executed 29 tests in total: 12 core tests, five
Gauss-word tests, five wheel tests, and seven Knauf tests.  All passed on the
final independent reruns.  The largest exact/finite audits were:

- 63,319 primitive Gauss necklaces at the largest word cutoff, with zero
  cyclic, reversal, or repetition-ledger failures;
- 98,460 wheel vertices and 98,459 edges, with a complete acyclicity
  certificate;
- \(2^{22}=4,194,304\) Knauf states and a 100-decimal-digit precision audit.

Near-boundary lack of finite-cutoff stabilization and the observed cutoff
drift were retained as failures, not hidden by best-seed selection.  This is
not a theorem of asymptotic nonconvergence.  Complete commands, seeds, tables,
and claim boundaries are in [`EXPERIMENT_REPORT.md`](EXPERIMENT_REPORT.md).

## Final conceptual answer

Symbolic dynamics can naturally supply an exact primitive/repetition grammar,
an endogenous arithmetic recursion, or an infinite-dimensional analytic
determinant.  In the investigated families it did not supply all three in one
frozen object, and it did not supply the required completed divisor and
same-clock lift.  The defensible Session-4 conclusion is therefore a
candidate-level scoped separation finding and a set of falsifiable
interfaces—not a candidate assembled from the best coordinate of unrelated
systems.
