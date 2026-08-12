# Session-4 Experiment Report

Run date: 2026-08-12  
Master seed: 20260812  
Riemann-zero data loaded: no

Exact identities, exhaustive finite certificates, and floating-point
observations are separated below.  Every candidate is interpreted only against
its own frozen object.

## Raw comparison table

| Candidate | Independent variables / cutoff | Primary raw result | Evidence status |
|---|---|---|---|
| SD-C01 full \(q\)-shift | \(q=2,3,5\), degree \(\le12\) | \(N_q(12)=335,44220,20343700\); necklace, irreducible-polynomial, Euler, and repetition identities all pass | PROVED finite-degree identities |
| SD-C01 finite-memory controls | \(T=10,20,40,80\), 80 dps | lattice counts \(7,14,28,56\); nonlattice counts \(5,11,23,43\) | NUMERICAL_OBSERVATION supporting proved \(O(T)\) bound |
| SD-C02 squarefree shift | exact theorem; brute period \(\le14\); finite approximants through period 30 | infinite system \(\#\mathrm{Fix}\,\sigma^n=1\); three-square approximant has 4501 points at \(n=30\) | PROVED infinite statement; exact finite census |
| SD-C03 renewal | degree 12, 80 dps, seeds 20260813–16 | on-circle, off-circle, and generic polynomials all reconstructed coefficientwise exactly | PROVED inverse design; STOP_SCOPED |
| SD-C04 Gauss words | digits \(1{:}D\), \(D=2,3,4,5\); word length 4,6,8; 80 dps | at \(D=5,L=8\): 63,319 primitive necklaces; all cyclic/reversal/repetition failures 0 | exact finite ledger / NUMERICAL_OBSERVATION for orbit sums |
| SD-C05 wheel DAG | levels 0–7; 5 random seeds plus fixed/cyclic controls | 98,460 nodes, 98,459 edges; arithmetic unit Jaccard 1; every graph acyclic | NUMERICALLY_CERTIFIED finite ledger; PROVED acyclicity |
| SD-C06 Knauf | \(k=8,10,\ldots,22\), 16 fixed \(s\)-points, 100-dps audit | \(2^{22}\) states; complete totient prefix 23; deep \(\Re s>2\) convergence but slow near 2 | NUMERICAL_OBSERVATION against primary-source theorem |

## Candidate findings

### SD-C01

Observation:

- The nonlattice rectangle counts have identical coarse/fine winding numbers.
  The minimum boundary modulus over all rectangles is 0.35167, and the fitted
  count slope is 0.54087 per unit \(T\).
- The unitary lattice control has maximum unitarity residual
  \(5.83\times10^{-16}\) and exactly linear count ratio 0.7.

Interpretation:

The numerical controls behave like exponential polynomials.  They are not the
reason for the obstruction; the Jensen proof already gives \(O(T)\).

Implication:

Increasing the number of finite states or a finite representation dimension
cannot repair the \(T\log T\) divisor mismatch.

Next test:

Only a genuinely infinite-memory or infinite-dimensional same-object model
could escape the theorem.  Such a model must first pass A0; larger finite
matrices are not a next experiment.

### SD-C02

Observation:

- The infinite candidate has one fixed point for every period.
- At period 30, the three-square finite approximation has 4501 fixed points,
  while full binary and golden-mean controls have 1,073,741,824 and 1,860,498.

Interpretation:

Finite modular approximants retain many cycles, but the unbounded family of
prime-square exclusions eliminates every nonzero periodic support.

Implication:

Aperiodic language richness cannot substitute for a prime primitive-orbit
ledger.

Next test:

None within the Artin–Mazur candidate.  Any aperiodic zeta observable would be
a new convention and needs preregistration.

### SD-C03

Observation:

- All three degree-12 targets are exactly reconstructed in rational
  arithmetic.
- The on-circle control has 12/12 roots on the unit circle with maximum
  numerical radius error \(2.89\times10^{-15}\).
- The deliberately off-circle control has six roots inside and six outside,
  with maximum radius error \(4.00\times10^{-15}\).
- Nonnegative renewal controls have positive real roots at
  0.608286779731922 and 0.187315414361226, bracketed to width \(2^{-320}\).

Interpretation:

Root geometry is carried entirely by the free coefficients.  The mechanism
has no selectivity for a critical line or circle.

Implication:

The candidate triggers STOP_SCOPED / PROVES_TOO_MUCH; no Riemann fit was
performed.

Next test:

Require an independently specified low-complexity rule for all return weights
and rerun composite-only, pseudoprime, and matched-density controls before any
target comparison.

### SD-C04

Observation:

- At the largest cutoff, 63,319 primitive necklaces were enumerated.
- Cyclic invariance, reversal-transpose, repetition, and reverse-completeness
  each have zero failures.
- There are 7018 non-reversal trace-collision groups, showing that matrix
  trace is not an injective arithmetic label.
- The 40-to-80 dps maximum drift is \(5.28\times10^{-42}\).
- At \(s=1.5\), the largest-cutoff intrinsic orbit sum is 0.413943, versus
  0.201666 for the neighboring additive-roof control and 0.128915 for the
  neighboring digit alphabet.

Interpretation:

The exact symbolic/matrix ledger is robust, while finite orbit sums are
specific to the continued-fraction grammar and roof.  None of the diagnostics
turns its hyperbolic classes into rational primes.

Implication:

The experiment validates implementation and cutoff behavior, not a Fredholm
continuation or a Riemann divisor.

Next test:

Within symbolic dynamics, pre-register any proposed word-to-rational-prime map
and test it against trace collisions, shuffled words, composites, and
neighboring digit alphabets.  No map found here passes that gate.

### SD-C05

Observation:

- The generated multipliers are \(2,3,5,7,11,13,17\).
- The arithmetic residue lift matches the unit residues at every level
  (Jaccard 1).
- At level 7, matched fixed/cyclic/random branch controls have the same
  92,160 residues but Jaccard values ranging from roughly 0.14 to 0.41
  (0.35 for seed 20260816), while all controls remain acyclic.
- Kahn traversal processes all 98,460 vertices for every graph.

Interpretation:

The deletion rule—not degree sequence or size—carries the arithmetic unit-set
structure.  Acyclicity is caused by the level order and survives every matched
control.

Implication:

SD-C05 is the strongest A0 construction but fails A1 exactly.

Next test:

Prove or refute the existence of a stationary natural extension with the same
recursive rule and no artificial reset.  Do not add cycles post hoc.

Post-freeze Stage-02 update: the strict semiconjugate and inverse-limit
extension readings are now **PROVED impossible**, and finite strong
bisimulation quotients are also acyclic.  The remaining question is a
separately source-locked infinite factor or observational recoding; see the
[Stage-02 theorem screen](../stage_02_stationary_wheel_extension/README.md).

### SD-C06

Observation:

- The final cutoff has 4,194,304 states, maximum \(h=46368\), support size
  28,863, and complete totient multiplicities only through \(n=23\).
- For unsigned/Liouville observables, absolute errors at \(s=3\) are
  \(4.47\times10^{-3}\) and \(1.46\times10^{-4}\); at \(s=4\), they are
  \(6.92\times10^{-5}\) and \(1.59\times10^{-6}\).
- At \(s=2.125\), the errors remain 2.242 and 0.02887.  At \(s=1.6\), the
  Liouville benchmark error is 3.863 with successive-\(k\) drift 0.183.
- complex128 differs from the 100-dps direct sum by at most
  \(7.85\times10^{-15}\); 50 dps differs from 100 dps by at most
  \(4.43\times10^{-49}\).
- All three random-sign seeds are reported.  Because the protocol defines a
  distinct field for every \((\text{seed},k)\), their median cross-level
  difference 2.096 is a re-keyed baseline, not a cutoff-stability metric.
- The coherent symbolic-parity control has median successive-cutoff drift
  0.001303, below Liouville's 0.004361.  Small finite-depth drift is therefore
  not selective for the arithmetic sign.

Interpretation:

Deep in the proved half-plane, finite-depth behavior agrees with the exact
zeta ratios.  Convergence near the phase boundary is slow, and the critical
half-plane data do not establish the open theorem.

Implication:

The exact unsigned quotient is genuine arithmetic prior art.  The Liouville
sign remains an extra observable, and neither finite sum is a same-object
periodic-orbit Fredholm determinant.

Next test:

The smallest mathematical test is a canonical primitive-cycle construction
for the frozen binary recursion.  The open signed convergence theorem cannot
be replaced by increasing \(k\).

## Reproducibility commands

Run from the Stage-01 root:

    cd symbolic_dynamics/stages/stage_01_scope_screening

    python finite_state_arithmetic_skeleton/experiments/run_session4_core.py
    bash farey_gauss_transfer/experiments/run.sh
    bash wheel_sieve_level_shift/experiments/run.sh
    bash knauf_spin_chain_audit/experiments/run.sh

The core runner executes 12 unit tests; the Gauss and wheel runners execute
five each; the Knauf runner executes seven.  All passed on the final independent
reruns.  Candidate-specific JSON/CSV/gzip files contain the complete raw
tables, seeds, cutoffs, precision audits, hashes, and claim boundaries.

## Suggested next experiments

Only three follow-ups remain scientifically live:

1. source-lock a stationary, low-complexity factor or observational recoding
   of the endogenous wheel recursion; strict extensions are already closed;
2. test any pre-registered Gauss-word arithmetic map against its many exact
   trace collisions and neighboring-grammar controls;
3. search for an intrinsic symmetry that produces the Knauf sign before
   target inspection and a canonical primitive-cycle determinant for that same
   recursion.

They are independent tests.  Passing one coordinate in one candidate does not
transfer it to either of the others.
