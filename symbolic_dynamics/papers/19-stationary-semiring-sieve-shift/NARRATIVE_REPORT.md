# NARRATIVE REPORT — SD-C21

## One-sentence result

A full-shift semiring can drive an explicit quotient-search Markov verifier
whose whole trace-class adjacency has determinant (1/\zeta(s)), but the
verifier is completely invisible to periodic traces and the same wrapper
compiles every decidable support.

## Why this candidate was attempted

The previous tensor and cocycle papers repeatedly obtained attractive Euler
factors while overproducing mixed primitive cycles or relying on a visible
accepted inventory.  The natural next move was to change the symbolic
grammar itself.  Finite full shifts already carry two elementary operations:
Cartesian product multiplies alphabet sizes and disjoint alphabet union adds
them.  Entropy reads (\log n).  This gives enough local structure to run
trial division inside Symbolic Dynamics.

## What was built

For each (n\ge2), the graph begins at (I_n), tests successive divisors at
(T_{n,d}), and exposes the putative quotient through the chain
(Q_{n,d,2},Q_{n,d,3},\ldots).  Equality (dq=n) is reached only after local
successor steps.  Composite inputs then enter an acyclic ray; inputs passing
the square-root test enter a loop (A_n\to A_n).  Trial-division correctness
therefore implies that the loops are exactly (A_p).

Entropy-derived edge roofs make the complete, unpruned weighted adjacency
trace class for (\operatorname{Re}s>1).  Its closed walks are precisely the
temporal repetitions of the accepted loops, so

\[
\operatorname{Tr}L_s^r=\sum_p p^{-rs},\qquad
\det(I-zL_s)=\prod_p(1-zp^{-s}).
\]

This is a genuine same-operator result: computation edges and determinant
belong to one operator, and no prime or zero table is loaded.

## Where the advance stops

The determinant cannot see a path that never closes.  Every square test,
quotient step, rejection, and cemetery edge is transient.  Deleting all of
them leaves the traces and determinant unchanged.  The recurrent pruning is
just the prime diagonal loop model.  The arithmetic proof is sound, but the
periodic dynamics do not perform it.

The decisive control is universal.  Replace trial division by the complete
configuration trace of any total deterministic decider.  Give accepted
inputs one loop and rejected inputs one cemetery ray, with a summable
time-index roof.  The resulting trace-class adjacency has the Euler product
of the chosen decidable support.  Squares, powers of two, Fibonacci numbers,
and a hash predicate work exactly like primes.  Effective factorial monoids
give a second family of controls; (\mathbb F_q[t]) yields (1-q^{1-s}).

Thus the right description is not “circular.”  It is **algorithmically
non-oracular, but dynamically selector-tautological**.  The selector is
computed before the recurrent support is created, and the determinant sees
only that support.

## Route decision

The source semiring and quotient search earn a structural arithmetic
coordinate.  The exact orbit ledger and whole Fredholm determinant earn
analytic A1/A2 coordinates.  No continuation or operator-theoretic RH
mechanism follows, and the universal compiler destroys arithmetic
selectivity.

~~~text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_PASS_ANALYTIC,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
ROUTE_B_LOCKED
SELECTOR_TAUTOLOGICAL
PRUNING_EQUIVALENT
PROVES_TOO_MUCH
~~~

## Next move

The next grammar must have no accepted-object self-loops created by a
completed verifier.  Arithmetic must alter recurrent transitions among all
objects.  A minimal test is an expanded successor-divisor relation such as
(d\mid m+1), followed first by exact SCC and primitive-cycle
classification, and only later by determinant analysis.
