# Prior Work Guide

This directory contains the five core papers and corresponding legacy code that form the starting point of the HP-Dynamics project.

These materials are not a final theory or a proven Hilbert–Pólya construction.

They provide:

1. Search priors
2. Mathematical constraints
3. Numerical baselines
4. Historical failures and lessons

The purpose of this directory is to provide an informed starting point for AI-driven exploration of arithmetic dynamical systems.

---

# 1. Directory Structure

```

docs/prior_work/

├── README.md

├── papers/
│   ├── paper1.pdf
│   ├── paper2.pdf
│   ├── paper3.pdf
│   ├── paper4.pdf
│   └── paper5.pdf

└── legacy/
├── paper1_code/
├── paper2_code/
├── paper3_code/
├── paper4_code/
└── paper5_code/

```

## papers/

Contains the five core research papers.

They represent the evolution of the research direction:

```

arithmetic symbolic dynamics
↓
topological constraints and obstructions
↓
non-autonomous dynamics
↓
finite spectral experiments
↓
conservative dynamical systems

```

## legacy/

Contains historical code and experiments.

Legacy code is preserved for:

- reproduction;
- regression testing;
- understanding previous assumptions;
- extracting useful components.

Legacy code is not considered proof.

A successful numerical experiment only establishes:

"this procedure generated this numerical observation under this configuration."

It does not establish:

- Hilbert–Pólya realization;
- self-adjointness;
- spectral identity;
- equality with the Riemann xi function.

---

# 2. Research Chain

The five papers provide the following research trajectory.

## Paper 1 — Prime–Chaos Framework

Role:

- arithmetic-symbolic dynamics prior;
- Logistic critical dynamics;
- sieve-inspired symbolic structures;
- parity-related observables.

Use:

- candidate generation;
- symbolic dynamics exploration;
- arithmetic constraints.

Do not assume:

- the Logistic map is the final Hilbert–Pólya system;
- numerical prime correlations imply spectral identity.

---

## Paper 2 — Topological Constraints and Obstructions

Role:

- identifies finite-stage failures;
- establishes limitations of one-dimensional symbolic models;
- shows that low-dimensional systems may capture only partial arithmetic structures.

Main lesson:

A one-dimensional chaotic system may provide useful arithmetic projections, but it is unlikely to contain the full required spectral structure.

Use:

- negative constraints;
- obstruction discovery;
- motivation for higher-dimensional lifting.

---

## Paper 3 — Sequential / Non-Autonomous Dynamics

Role:

- studies slowly varying dynamical systems;
- provides conditional tools for non-autonomous evolution.

Main lesson:

A parameter schedule alone is not a mathematical mechanism.

A valid non-autonomous candidate requires:

- a well-defined dynamical evolution;
- appropriate operator control;
- convergence theory.

A fitted schedule is only a modeling choice until justified.

---

## Paper 4 — Non-Autonomous Logistic Spectral Experiments

Role:

- finite-dimensional transfer matrix experiments;
- eigenphase analysis;
- spectral matching attempts.

Use:

- numerical baseline;
- reproducibility benchmark;
- failure analysis.

Important lesson:

Finite matrix eigenvalue matching is not equivalent to a dynamical Zeta function.

Averaged transition matrices may lose chronological orbit information.

The correct target is:

```

periodic orbits
↓
weighted orbit expansion
↓
dynamical Zeta / Fredholm determinant
↓
spectral zeros

```

not:

```

time-averaged matrix
↓
eigenphase fitting

```

---

## Paper 5 — Conservative Hénon-Type Dynamics

Role:

- two-dimensional conservative dynamics;
- area-preserving systems;
- possible quantization candidates.

Use:

- higher-dimensional lifting;
- symplectic candidate generation;
- Route-A exploration.

Important lesson:

GUE statistics, finite spectral matching, and chaotic behavior are necessary consistency checks, but they are not sufficient evidence for a Hilbert–Pólya operator.

---

# 3. Core Search Principle

The HP-Dynamics project is not searching for an arbitrary chaotic system.

The target is:

```

Candidate dynamics

```
    ↓
```

Primitive unstable periodic orbits (UPOs)

```
    ↓
```

Weighted orbit data

```
    ↓
```

Dynamical Zeta / Fredholm determinant

```
    ↓
```

Complex zeros

```
    ↓
```

Comparison with completed Riemann xi structure

```

The primary object is not a fitted spectrum.

The primary object is a natural periodic-orbit expansion.

---

# 4. Non-Autonomous Dynamics Principle

Non-autonomous systems are allowed, but only under strict conditions.

A useful form is:

\[
x_{n+1}=f_{u_n}(x_n)
\]

with

\[
u_n\rightarrow u_c
\]

where \(u_c\) is a mathematically distinguished critical parameter.

Examples:

- band-merging points;
- symbolic transition points;
- critical dynamical regimes.

The important idea is:

```

transient exploration

```
    ↓
```

critical regime

```
    ↓
```

limiting dynamical structure

```

The parameter drift itself is not the source of the spectrum.

The final limiting structure must provide the orbit/Zeta mechanism.

---

# 5. Non-Autonomous Candidate Requirements

A valid non-autonomous candidate must preserve periodic-orbit information.

A simple time average is insufficient.

The candidate should have at least one of:

## Option 1: Autonomous extension

Introduce additional variables:

\[
(x,\theta)
\]

such that:

\[
F(x,\theta)
\]

is autonomous.

Then periodic orbits satisfy:

\[
F^n(z)=z
\]

and can enter Route A.

---

## Option 2: Dynamical cocycle formulation

Use a chronological transfer structure:

\[
K_nK_{n-1}\cdots K_1
\]

with a mathematically defined determinant or trace formula.

---

Invalid shortcut:

```

non-autonomous simulation

```
    ↓
```

average transition matrix

```
    ↓
```

eigenvalues

```
    ↓
```

claim spectrum

```

This destroys time ordering and does not automatically define a dynamical Zeta function.

---

# 6. One-dimensional and Two-dimensional Search Strategy

## 1D systems

Examples:

- Logistic maps;
- unimodal maps.

Advantages:

- symbolic dynamics;
- explicit periodic orbit structure;
- easy computation.

Limitations:

- low-dimensional constraints;
- limited arithmetic expressiveness;
- difficult quantization.

Role:

```

baseline
obstruction discovery
symbolic prior

```

---

## 2D and higher-dimensional systems

Examples:

- Hénon maps;
- symplectic maps;
- kicked systems;
- suspension flows.

Advantages:

- richer periodic orbit structure;
- conservative dynamics;
- possible quantum lift.

Role:

```

primary candidate search space

```

---

# 7. Research Rules

All future AI agents must follow:

## Rule 1

Prior work provides clues, not conclusions.

## Rule 2

Numerical agreement is evidence, not proof.

## Rule 3

Fitted parameters must be labeled as fitted.

## Rule 4

GUE statistics are only secondary diagnostics.

## Rule 5

The main validation target is:

```

UPO
→ weighted Zeta
→ stable zeros
→ analytic structure

```

## Rule 6

No candidate may directly use:

- Riemann zero tables;
- prime tables;
- target spectrum fitting.

---

# 8. Current Research Direction

The project objective is:

> Use AI to search arithmetic dynamical systems whose natural periodic-orbit structure may produce a Hilbert–Pólya-compatible spectral determinant.

The search process:

```

Generate candidate

```
    ↓
```

Extract UPOs

```
    ↓
```

Construct dynamical Zeta

```
    ↓
```

Evaluate spectral structure

```
    ↓
```

Learn success/failure constraints

```
    ↓
```

Generate better candidates

```

The output of each exploration should become an independent project:

```

candidate_name/

├── README.md
├── paper/
├── code/
└── results/

```

The final knowledge is accumulated through papers, code, and reproducible experiments.
```