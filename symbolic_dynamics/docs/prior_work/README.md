# Prior Work Guide

> **Session-4 evidence warning (2026-08-12).** This guide describes the
> intended research lineage; it is not a verification record.  Several claims
> below were materially downgraded or refuted on recheck, including the Paper-1
> sieve limit/conjugacy and twin-constant claim, the Paper-4 chronological
> propagator interpretation, and the independent-certification status of the
> very recent Paper-6 benchmark.  Use the
> [Paper-01 prior-work audit](../../Ra-1-arithmetic-symbolic-dynamics/papers/01-falsification-first-audit/docs/PRIOR_WORK_AUDIT.md)
> for claim grades.

This directory contains the six core papers that provide the main intellectual background for the HP-Dynamics project.

The purpose of this README is intentionally narrow:

> **summarize what each paper studies, what mathematical idea it contributes, and what lesson it leaves for later exploration.**

It is not a Route-A / Route-B specification, not an evaluation protocol, and not a candidate-selection manual. Those belong in separate project documents and skills.

These papers should be read as a sequence of ideas rather than as a completed theory.

---

# 1. Directory Structure

```text
docs/prior_work/

├── README.md
│
├── papers/
│   ├── 1-The emergence of prime distribution from low-dimensional deterministic chaos.pdf
│   ├── 2-Transient Chaos and Topological Bounds in Prime Dynamics.pdf
│   ├── 3-A Sequential Birkhoff Theorem.pdf
│   ├── 4-riemann_logistic_v4_fixed.pdf
│   ├── 5-An Area-Preserving Henon-Map Model.pdf
│   └── 6-zeta-two-thirds.pdf
│
└── legacy/
    ├── paper1_code/
    ├── paper2_code/
    ├── paper3_code/
    ├── paper4_code/
    └── paper5_code/
```

The first five papers form the original internal research lineage.

Paper 6 is a new external frontier result that is included because it gives a rigorous modern connection between prime-side arithmetic, the explicit formula, and finite-dimensional operator geometry.

---

# 2. Overall Research Trajectory

The six papers can be read as the following progression:

```text
Prime distribution and low-dimensional chaos
                ↓
Topological constraints and one-dimensional obstructions
                ↓
Sequential / non-autonomous dynamical systems
                ↓
Finite transfer-operator spectral experiments
                ↓
Area-preserving Hénon and conservative geometry
                ↓
Prime-side arithmetic ↔ finite operator geometry
```

The first five papers mainly explore dynamical-system candidates and their structural limits.

The sixth paper approaches the Riemann zeta function from the opposite direction: it starts from the explicit formula and prime powers, compresses Weil's Hermitian form to a finite-dimensional space, and extracts rigorous information about zeros through linear algebra.

Together they motivate a broader question:

> Can arithmetic structure, dynamical structure, and operator geometry be connected within one natural mathematical object?

---

# 3. Paper 1 — The Emergence of Prime Distribution from Low-Dimensional Deterministic Chaos

## Core idea

This paper explores whether prime/composite structure can arise from a low-dimensional deterministic chaotic system, with the Logistic-type quadratic map near a distinguished critical regime as the main prototype.

The central perspective is that apparently irregular arithmetic sequences may admit a deterministic dynamical representation.

## Main ingredients

- low-dimensional quadratic dynamics;
- symbolic coding of trajectories;
- critical and band-merging regimes;
- prime/composite observables;
- parity and sieve-inspired structures;
- numerical comparison between arithmetic and dynamical sequences.

## Main contribution

The paper provides the original arithmetic-dynamical starting point of the project:

```text
prime distribution
        ↕
symbolic dynamics
        ↕
low-dimensional deterministic chaos
```

Its main value is not that the Logistic map has already been identified as the final Riemann system, but that it supplies a concrete and computable arithmetic seed from which stronger dynamical constructions can be explored.

## Main lesson

Low-dimensional deterministic chaos can reproduce nontrivial arithmetic structure, but numerical correspondence alone does not establish a spectral or operator identity.

---

# 4. Paper 2 — Transient Chaos and Topological Bounds in Prime Dynamics

## Core idea

This paper asks how far one-dimensional symbolic dynamics can be pushed before topology itself becomes an obstruction.

Rather than only searching for positive numerical matches, it studies forbidden structures and finite-stage failures.

## Main ingredients

- transient chaotic dynamics;
- symbolic admissibility;
- parity constraints;
- finite-word and shift obstructions;
- topological limitations of one-dimensional maps.

## Main contribution

The paper converts several failed constructions into structural information.

Its basic message is:

> A one-dimensional dynamical system may reproduce useful projections of arithmetic structure without possessing enough topological freedom to encode the full arithmetic problem.

## Main lesson

Failure is informative.

The paper motivates moving from one-dimensional systems toward higher-dimensional geometric systems rather than endlessly optimizing a single Logistic-type model.

---

# 5. Paper 3 — A Sequential Birkhoff Theorem

## Core idea

This paper studies sequential and non-autonomous dynamical systems in which the map changes with time.

Instead of a single autonomous transformation

\[
x_{n+1}=f(x_n),
\]

one considers a sequence

\[
x_{n+1}=f_n(x_n).
\]

The goal is to understand when statistical laws analogous to Birkhoff's ergodic theorem remain valid under controlled temporal variation.

## Main ingredients

- sequential dynamical systems;
- non-autonomous evolution;
- inducing methods;
- statistical convergence;
- spectral-gap or uniformity assumptions;
- slowly varying dynamics.

## Main contribution

The paper provides mathematical tools for treating parameter drift as a genuine dynamical process rather than merely as a numerical schedule.

## Main lesson

A slowly varying parameter is not by itself an explanation of arithmetic or spectral structure.

Non-autonomous models require their own mathematical evolution theory and cannot be justified only by fitting a time-dependent parameter.

---

# 6. Paper 4 — Non-Autonomous Logistic Spectral Experiments

## Core idea

This paper investigates whether non-autonomous Logistic-type dynamics can generate spectral structures resembling the Riemann-zero spectrum.

The main numerical tool is a finite-dimensional approximation of transfer dynamics followed by eigenvalue/eigenphase analysis.

## Main ingredients

- non-autonomous Logistic dynamics;
- transfer-matrix approximations;
- finite-dimensional spectral calculations;
- eigenphase statistics;
- comparison with Riemann-zero data;
- numerical parameter exploration.

## Main contribution

The paper establishes a reproducible numerical baseline and exposes the difference between:

```text
finite spectral resemblance
```

and

```text
an intrinsic dynamical spectral mechanism.
```

## Main lesson

A time-averaged transition matrix can destroy chronological orbit information.

Therefore a finite matrix whose eigenvalues resemble Riemann zeros should be treated as a numerical clue, not as evidence that the underlying dynamics possesses the required zeta or determinant structure.

---

# 7. Paper 5 — An Area-Preserving Hénon-Map Model

## Core idea

This paper lifts the search from one-dimensional dissipative dynamics toward two-dimensional conservative dynamics.

The Hénon family is used as a bridge because an area-preserving version naturally introduces phase-space geometry while remaining computationally accessible.

## Main ingredients

- Hénon-type maps;
- two-dimensional phase space;
- area preservation;
- conservative chaotic dynamics;
- periodic orbits;
- spectral statistics;
- possible classical-to-quantum connections.

## Main contribution

The paper marks the transition from a primarily symbolic one-dimensional viewpoint to a geometric dynamical viewpoint:

```text
Logistic-type dynamics
        ↓
Hénon-type dynamics
        ↓
conservative / symplectic geometry
```

## Main lesson

The Hénon map is most valuable as a geometric bridge rather than necessarily as the final target.

Its importance is that it suggests a natural dimensional upgrade from low-dimensional arithmetic dynamics toward richer conservative and symplectic systems.

---

# 8. Paper 6 — More Than Two Thirds of the Zeros of the Riemann Zeta Function Lie on the Critical Line

## Core result

This 2026 work proves unconditionally that at least

\[
\frac{2}{3}
\]

of the nontrivial zeros of the Riemann zeta function lie on the critical line, and that at least the same proportion are simple zeros on the critical line.

It also proves that at least

\[
\frac{5}{6}
\]

of the zeros are distinct.

With an optimized test family, the critical-line/simple-zero constant is improved to approximately

\[
0.6725.
\]

## Core idea

The paper revisits Montgomery's pair-correlation framework.

The prime-side second-moment calculation is already unconditional. The classical difficulty is that, without assuming the Riemann Hypothesis, the zero side is no longer a positive sum over real ordinates.

The paper replaces that missing positivity with finite-dimensional linear algebra.

## Main ingredients

- Weil's Hermitian form;
- Weil's explicit formula;
- a finite-dimensional Gabor-type test family;
- finite compression of the Hermitian form;
- Sylvester's law of inertia;
- rank-trace inequalities;
- von Neumann's trace inequality;
- Montgomery's prime-side pair-correlation second moment;
- prime powers and von Mangoldt weights.

## Structural picture

On the zero side:

- a zero on the critical line contributes a positive rank-one form;
- an off-line symmetric pair
  \[
  \{\rho,1-\bar\rho\}
  \]
  contributes a two-dimensional block of signature
  \[
  (1,1).
  \]

On the arithmetic side, the trace and second trace moment of the same finite compression are evaluated using the explicit formula and sums over prime powers.

Schematically:

```text
prime powers
      ↓
explicit formula
      ↓
finite Weil compression
      ↓
trace + second moment
      ↓
rank / inertia
      ↓
rigorous information about critical-line zeros
```

## Main contribution

For the HP-Dynamics project, the most important conceptual contribution is not the numerical constant 0.6725 itself.

It is the rigorous bridge:

```text
prime-side arithmetic
        ↔
finite-dimensional operator geometry
        ↔
zero distribution
```

This provides a modern example in which prime powers, an operator-like finite compression, and spectral information are connected without relying on numerical zero fitting.

## Main lesson

A useful Riemann-related operator structure should ultimately remain anchored to prime-side arithmetic.

Spectral resemblance alone is much weaker than an identity in which the same mathematical object can be read from both the prime side and the zero/operator side.

---

# 9. Combined Lessons from the Six Papers

The six papers collectively suggest several recurring themes.

## 9.1 Arithmetic structure must remain primary

The project began from a direct attempt to relate prime distribution to deterministic dynamics.

Paper 6 independently reinforces the importance of keeping prime powers and von Mangoldt-type arithmetic visible in the mathematics.

## 9.2 Low-dimensional systems are useful prototypes

Logistic-type systems are valuable because they are explicit, computable, and symbolically transparent.

Their limitations are equally valuable because they identify which structures require a dimensional or geometric lift.

## 9.3 Hénon provides a natural geometric bridge

The move from Logistic to area-preserving Hénon dynamics is not merely a change of model.

It introduces phase-space geometry while retaining a tractable relationship to low-dimensional chaotic dynamics.

## 9.4 Non-autonomous dynamics needs genuine mathematics

Slow parameter evolution can be useful, but only when embedded in a well-defined sequential dynamical framework.

## 9.5 Finite spectral matching is only exploratory evidence

Finite matrices and eigenphase fits are useful for discovery and debugging, but they are not substitutes for an intrinsic analytic or operator construction.

## 9.6 Prime-side arithmetic and operator geometry can meet rigorously

Paper 6 shows that finite-dimensional operator geometry can extract new information about Riemann zeros when its trace data are rigidly tied to the explicit formula and prime powers.

This is an important conceptual benchmark for future arithmetic-dynamical models.

---

# 10. How to Use This Directory

Use these papers for:

- understanding the origin of the project;
- identifying reusable mathematical ideas;
- learning from earlier successful and failed constructions;
- generating hypotheses about arithmetic dynamical systems;
- comparing new candidates with known structural constraints.

Do not treat any single paper as the final theory.

The intended reading order is:

```text
Paper 1
  ↓
Paper 2
  ↓
Paper 3
  ↓
Paper 4
  ↓
Paper 5
  ↓
Paper 6
```

The first five papers trace the internal dynamical exploration.

Paper 6 adds a new external arithmetic/operator benchmark and should be read as a complementary frontier result.

---

# 11. Scope of This README

This README has one job:

> **document the six core papers and the ideas they contribute.**

Evaluation protocols, candidate gates, Route-A / Route-B definitions, proof obligations, and agent instructions should live elsewhere.

Keeping those concerns separate makes the project easier to navigate and prevents the prior-work guide from becoming a general-purpose project specification.
