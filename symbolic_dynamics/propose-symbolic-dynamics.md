# Research Proposal

## Session 4 — Symbolic Dynamics: Arithmetic Skeleton vs Geometric Realization

---

# 1. Session Identity

This session explores **Symbolic Dynamics only**.

The central question is:

> Which structures required by a Riemann/Hilbert–Pólya dynamical model can already arise at the symbolic level, and which structures necessarily require a geometric dynamical realization?

The session should remain focused on symbolic dynamical systems as a system family.

Do **not** turn this session into a general Hilbert–Pólya search across unrelated models.

The working principle is:

```text
one session
=
one dynamical-system family
```

If a promising idea requires leaving symbolic dynamics and moving to an independent Hénon, symplectic, quantum-graph, operator-algebra, or flow model, record it as:

```text
ROUND2_CLUE
```

and stop that branch inside this session.

---

# 2. Current Resources

The repository is the primary source of truth.

## 2.1 Evaluation skills

Use when needed:

```text
skills/
├── route-a-evaluator.md
└── route-b-evaluator.md
```

The evaluator documents define the validation framework.

This `propose.md` should not duplicate their detailed gates.

### Route A

Use Route A to evaluate whether a symbolic candidate has a credible arithmetic origin, primitive-orbit structure, natural dynamical Zeta/Fredholm determinant, global analytic structure, and possible geometric/operator lift.

### Route B

Route B is only for strong candidates that are explicitly ready for operator-level analysis.

Do not use Route B to rescue a weak symbolic fit.

---

## 2.2 Core prior work

Read:

```text
docs/prior_work/README.md
docs/prior_work/papers/
```

The directory currently contains six core papers.

The first five papers provide the internal dynamical research lineage:

```text
prime / chaos relation
        ↓
one-dimensional topological obstruction
        ↓
sequential / non-autonomous dynamics
        ↓
finite spectral experiments
        ↓
area-preserving Hénon / conservative geometry
```

The sixth paper provides a new external arithmetic/operator benchmark:

```text
prime powers
        ↔
explicit formula
        ↔
finite Weil compression
        ↔
trace / second moment / inertia
        ↔
critical-line zero information
```

Use these papers for ideas, constraints, and mathematical context.

They are not fixed conclusions.

---

## 2.3 Literature tools

Codex may use installed academic-research skills when useful, including:

- literature search;
- paper retrieval;
- paper summarization;
- citation tracing;
- mathematical verification;
- experiment planning.

Use literature **on demand**.

Do not build a large static `related_programs/` knowledge base for this session.

The goal is to keep the context small and let the research process explore freely.

---

# 3. Main Research Objective

Explore whether natural symbolic dynamical systems can provide an **arithmetic skeleton** with the structural ingredients needed by a Riemann-type dynamical Zeta construction.

The key contrast is:

```text
symbolic structure
vs.
geometric realization
```

The session should determine how far one can go using symbolic dynamics alone.

A successful outcome does not need to solve the Hilbert–Pólya problem.

A valuable result may instead be:

- a natural arithmetic symbolic model;
- a rigorous symbolic Zeta/Fredholm determinant;
- a structural obstruction;
- a proof that a class of symbolic systems has insufficient divisor growth;
- a proof that positivity prevents the required cancellation;
- a clear statement that some missing structure must come from geometry.

---

# 4. Primary Exploration Family

The session may explore symbolic systems such as:

```text
subshifts of finite type
sofic shifts
countable Markov shifts
renewal systems
symbolic suspensions
substitution systems
coded systems
Markov partitions
group / unitary cocycles over symbolic dynamics
thermodynamic-formalism models
transfer operators associated with symbolic grammars
```

This list is not restrictive.

Codex may propose other symbolic families if they are mathematically natural.

The main restriction is that the primary object must remain a **symbolic dynamical system**.

---

# 5. Core Research Questions

## 5.1 Arithmetic naturality

The first question is not whether a symbolic system can be made to reproduce primes.

That is trivial if the prime sequence is inserted manually.

The real question is:

> Can a low-complexity, pre-specified symbolic grammar generate prime-like primitive structure intrinsically?

Investigate whether the system naturally produces structures analogous to:

\[
p \longleftrightarrow \gamma_p
\]

and

\[
p^r \longleftrightarrow \gamma_p^r,
\]

with a meaningful dynamical length or roof related to the arithmetic scale.

Do not regard a construction as informative if it simply defines:

```text
symbol p
roof = log p
weight = von Mangoldt weight
```

by hand.

The arithmetic content must emerge from the grammar, dynamics, cocycle, symmetry, or another intrinsic mechanism.

---

## 5.2 Primitive words, cycles, and repetitions

For each candidate, determine:

- what the primitive objects are;
- how primitive cycles are enumerated;
- how repetitions are represented;
- whether multiplicity is intrinsic;
- whether orientation or phase information exists;
- whether the primitive/repetition ledger is exact.

The symbolic analogue of the prime / prime-power distinction should be explicit.

---

## 5.3 Finite-state versus countable-state structure

One important goal of this session is to understand the structural difference between:

```text
finite-state symbolic dynamics
```

and

```text
countable-state / renewal-type symbolic dynamics.
```

Questions include:

- What zero-counting laws are possible?
- When is the dynamical Zeta rational?
- When can a determinant acquire richer analytic structure?
- Can \(T\log T\)-type divisor growth arise naturally?
- What new pathologies appear in the countable-state case?
- Does positivity force unwanted real zeros?
- What type of signed or complex cancellation is mathematically natural?

Negative results are especially valuable.

---

## 5.4 Natural Zeta and Fredholm structure

Study natural symbolic dynamical Zeta functions, transfer operators, and Fredholm determinants.

Typical objects may include:

\[
Z(s)
=
\prod_{\gamma\ \mathrm{primitive}}
\left(1-w_\gamma e^{-sT_\gamma}\right)^{-1},
\]

or

\[
D(s)=\det(I-\mathcal L_s).
\]

The exact determinant convention must come from the candidate.

Investigate:

- convergence;
- nuclearity / trace-class structure where applicable;
- primitive/repetition expansions;
- signed or complex weights;
- analytic continuation;
- divisor counting;
- extra and missing zeros;
- cutoff stability.

Do not construct a determinant only because its zeros can be fitted to the Riemann zeros.

---

# 6. Symbolic vs Geometry

This is the defining conceptual theme of Session 4.

For every strong symbolic candidate, ask:

> Is the symbolic object complete in itself, or does it require a geometric carrier?

Possible geometric questions include:

- Can the symbolic system arise as a natural Markov coding?
- Can it be realized as a Poincaré return grammar?
- Can symbolic primitive cycles lift to genuine geometric closed orbits?
- Can the roof function arise from a geometric return time or action?
- Can signed/complex cocycles arise from orientation, holonomy, symmetry, or phase?
- Which analytic structures are unavailable without geometry?

The session should **not** leave symbolic dynamics to build the geometric system.

Instead, record the result as a structural conclusion or `ROUND2_CLUE`.

Example:

```text
ROUND2_CLUE:
This symbolic grammar has the correct primitive/repetition structure,
but its required phase weights appear to need a symplectic geometric realization.
```

Such clues are intended for the second-round research program.

---

# 7. Suggested Exploration Ladder

This is a suggested order, not a rigid script.

## Stage S1 — Finite symbolic systems

Study finite-state systems first when useful:

```text
SFT
sofic shifts
finite adjacency grammars
```

Determine their exact Zeta/determinant structure and analytic limitations.

A rigorous impossibility result is a successful outcome.

---

## Stage S2 — Countable symbolic systems

If finite-state systems are too rigid, study:

```text
countable Markov shifts
renewal systems
coded systems
```

Focus on whether increased symbolic complexity can generate:

- logarithmic roofs;
- richer divisor counting;
- non-rational determinants;
- natural arithmetic structure.

---

## Stage S3 — Signed / complex symbolic structure

If positive weights create structural obstructions, investigate whether the symbolic system itself naturally supports:

```text
orientation signs
finite-group cocycles
unitary representations
complex phases
holonomy-like symbolic data
```

The phase mechanism must be intrinsic.

Do not choose phases from the Riemann-zero target.

---

## Stage S4 — Geometry compatibility audit

For the strongest surviving symbolic structures, determine what type of geometric system could realize them.

Do not construct that geometric system here.

The output should be a precise statement of the missing geometric obligations.

---

# 8. Weil / Explicit-Formula Benchmark

The sixth core paper provides an important modern benchmark.

Its conceptual structure is:

```text
prime powers
        ↔
explicit formula
        ↔
finite Hermitian compression
        ↔
trace / second moment / inertia
```

For a strong symbolic candidate, investigate whether an analogous finite compression can be derived naturally.

Possible quantities include:

\[
\operatorname{tr}G,
\qquad
\operatorname{tr}(G^2),
\qquad
n_+(G),
\qquad
n_-(G).
\]

The purpose is not to imitate the paper mechanically.

The question is:

> Can the same symbolic object be read both from its orbit/grammar side and from an arithmetic prime-power side?

If no natural analogue exists, record that honestly.

Do not introduce a Weil-type form artificially only to pass a benchmark.

---

# 9. Falsification and Controls

This session should be generative but adversarial.

For serious candidates, use the Route-A evaluator and apply appropriate controls.

Examples:

- randomized grammars;
- shuffled arithmetic labels;
- matched-density non-prime sequences;
- composites;
- randomized phases;
- neighboring grammar parameters;
- known false-RH analogues when mathematically relevant.

A mechanism that proves too much is evidence against the mechanism.

Strong numerical agreement without control separation is insufficient.

---

# 10. Scope Discipline

The main lesson from earlier sessions is that a session should not grow into many unrelated research programs.

Therefore:

## Allowed

Remain within the symbolic-dynamics family while varying:

- finite vs countable state;
- grammar;
- symbolic partition;
- roof function;
- cocycle;
- transfer operator;
- potential;
- symbolic suspension;
- natural determinant convention.

## Not allowed as a new main branch

Do not independently launch:

- Hénon-map projects;
- symplectic-map projects;
- Hamiltonian-flow projects;
- quantum-graph projects;
- cosmological models;
- von Neumann-algebra programs;
- unrelated operator constructions.

When such a direction appears, record:

```text
ROUND2_CLUE
```

and return to the symbolic session.

---

# 11. Research Output

The research root is itself the project container.  Its project name and
roadmap phase are recorded in the root `README.md`; shareable paper projects
sit directly under the root `papers/` directory:

```text
README.md
propose-symbolic-dynamics.md
skills/
docs/
papers/
└── <paper-project-name>/
    ├── README.md
    ├── main.pdf
    ├── main.tex
    ├── sections/
    ├── figures/
    ├── code/
    ├── experiments/
    ├── results/
    ├── evaluations/
    ├── notes/
    └── PAPER_MANIFEST.sha256
```

The paper-project directory is the complete unit of sharing and
reproducibility.  Do not add a roadmap-project wrapper, `stages/` layer, or
another redundant `paper/` layer inside it.  The paper-project name must be a
real descriptive name rather than the literal word `paper`.

Do not create a formal candidate only because an idea was mentioned.

First fix:

- the mathematical object;
- the grammar;
- the roof / potential;
- the cocycle if any;
- the function space;
- the determinant convention.

Then evaluate it.

---

# 12. Session-Level Final Summary

At the end of the session, create a single top-level summary for Session 4.

It should answer:

1. Which symbolic system families were explored?
2. Which structures were genuinely arithmetic?
3. Which primitive/repetition structures were natural?
4. Which systems admitted rigorous Zeta/Fredholm objects?
5. Which systems failed, and why?
6. What analytic obstructions were found?
7. What structures appear to require geometry?
8. Which `ROUND2_CLUE` items should survive into the next research round?
9. What is the strongest surviving symbolic candidate, if any?
10. What is the strongest negative theorem or obstruction?

A useful final conceptual outcome would be a statement of the form:

```text
Euler-product structure is largely symbolic,
but the required weights / phases / spectral symmetry
appear to require geometric realization.
```

This is a hypothesis to test, not a conclusion to assume.

---

# 13. Repository Synchronization

The final research package should be synchronized to:

```text
git@github.com:maris205/hilbert-polya-structure.git
```

Before pushing:

```bash
git pull
```

建一个子目录，名称为symbolic_dynamics，所有内容都传到这个子目录就行

Do not overwrite existing research directories.

Commit:

- code;
- mathematical notes;
- experiments;
- results;
- candidate evaluations;
- draft papers;
- session summary.

Use clear commit messages.

---

# 14. Final Goal

The purpose of Session 4 is not to solve the Riemann Hypothesis directly.

The purpose is to determine the **symbolic contribution** to a possible arithmetic dynamical system.

The session should clarify whether the future structure is best understood as:

```text
arithmetic symbolic skeleton
        ↓
geometric dynamical carrier
        ↓
spectral / operator realization
```

or whether symbolic dynamics itself can already provide substantially more.

The most valuable outcomes are:

- a natural symbolic candidate;
- a rigorous symbolic determinant;
- a structural impossibility theorem;
- a precise symbolic-to-geometric interface;
- a reusable obstruction;
- a high-quality `ROUND2_CLUE`.

Keep the exploration broad inside symbolic dynamics, strict at the system-family boundary, and honest about what is proved, numerical, heuristic, or still open.
