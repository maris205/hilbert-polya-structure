# Research Proposal

## Hilbert–Pólya Dynamical Structure Exploration

---

# 1. Current Resources

This research session is based on the existing Hilbert–Pólya exploration repository.

The researcher should treat the repository as the primary source of truth.

---

# 1.1 Skills

The repository contains reusable research skills under:
注意，这个是路线图，不需要作为技能使用，当然，如果需要，也可以当作项目技能放到.agent目录下。

```

skills/

```

Current important skills:

```

skills/

├── route-a-evaluator.md

└── route-b-evaluator.md

```

These documents define the evaluation framework for candidate systems.

---

## Route A: Candidate Discovery and Validation

File:

```

skills/route-a-evaluator.md

```

Purpose:

Evaluate whether a proposed dynamical system contains meaningful structures
that justify further Hilbert–Pólya exploration.

Route A focuses on:

```

Dynamical System

```
    ↓
```

Primitive Unstable Periodic Orbits (UPOs)

```
    ↓
```

Weighted Periodic Orbit Data

```
    ↓
```

Dynamical Zeta / Fredholm Determinant

```
    ↓
```

Spectral Zeros

```

Main questions:

- Can periodic orbit structures be extracted reliably?
- Can weighted dynamical zeta functions be constructed?
- Are the resulting spectral structures stable?
- Does the candidate show non-trivial compatibility with RH-related structures?

Route A does not prove Hilbert–Pólya.

Its goal is:

> Discover promising dynamical candidates and identify structural constraints.

---

## Route B: Rigorous Hilbert–Pólya Evaluation

File:

```

skills/route-b-evaluator.md

```

Purpose:

Evaluate whether a strong Route-A candidate can be promoted toward a rigorous
Hilbert–Pólya realization.

Route B focuses on:

```

Candidate Dynamics

```
    ↓
```

Operator Construction

```
    ↓
```

Self-Adjoint Realization

```
    ↓
```

Spectral Theorem

```
    ↓
```

Riemann xi Determinant Identity

```

Main questions:

- Is there a natural Hilbert space?
- Is the corresponding operator well-defined?
- Can self-adjointness be established?
- Can the trace formula connect dynamics with prime data?
- Can the spectral determinant reproduce the completed Riemann xi structure?

Route B is only applied to strong Route-A candidates.

---
注意，codex本身安装了一些如论文检索等科研技能，可以有选择的使用。
是从这里安装的：https://github.com/Imbad0202/academic-research-skills-codex


- 

# 1.2 Existing Knowledge Base

## `docs/prior_work/README.md`

This directory contains the fixed prior knowledge base.

It includes:

- core references;
- foundational papers;
- previous mathematical observations;
- legacy code and experiments.

This material provides:

- search priors;
- candidate generation ideas;
- known limitations.

It should be treated as stable background knowledge.

Do not modify it unless necessary.

---

## `docs/related_programs/README.md`

This directory contains independent exploratory research programs.

These projects are not fixed assumptions.

They represent previous investigations into:

- chaotic dynamics;
- periodic orbit structures;
- dynamical zeta functions;
- transfer operators;
- arithmetic correlations.

Examples include:

- Ulam-type operator exploration;
- dynamical zeta construction;
- weighted Hénon zeta exploration;
- arithmetic-dynamics experiments.

These projects provide:

- reusable code;
- experimental methods;
- positive results;
- negative constraints.

---

# 2. Research Exploration Direction

## Overview

Explore whether Hénon-type dynamical systems and their extensions can provide
useful structures for a Hilbert–Pólya style spectral construction.

The main research chain is:

```

Nonlinear Dynamical Systems

```
    ↓
```

Periodic Orbits / Symbolic Dynamics

```
    ↓
```

Weighted Dynamical Zeta Functions

```
    ↓
```

Transfer Operators / Spectral Structures

```
    ↓
```

Possible Hilbert–Pólya Compatibility

```

---

# 2.1 Main Exploration Object

The primary exploration family is:

## Hénon Maps and Generalizations

Including:

- classical Hénon maps;
- reversible Hénon maps;
- area-preserving Hénon maps;
- dissipative Hénon maps;
- parameter families;
- higher-dimensional extensions;
- coupled Hénon systems;
- non-autonomous Hénon systems.

Possible directions:

```

H_n(x,y)

```
    ↓
```

H_{n,t}(x,y)

(time-dependent / non-autonomous)

```
    ↓
```

Coupled or high-dimensional systems

```

---

# 2.2 Non-Autonomous Dynamics

Non-autonomous systems are an important exploration direction.

Possible forms:

\[
x_{n+1}=F_{a_n}(x_n)
\]

or skew-product systems:

\[
(x_{n+1},\theta_{n+1})
=
(F_\theta(x_n),T\theta_n)
\]

The goal is to explore whether additional temporal structures can produce
richer periodic orbit and spectral structures.

---

## Important Constraint for Non-Autonomous Systems

A valid non-autonomous candidate must preserve genuine dynamical information.

The following is insufficient:

```

non-autonomous simulation

```
    ↓
```

time averaged transition matrix

```
    ↓
```

eigenvalue fitting

```

because chronological orbit information may be lost.

Valid directions should consider:

- autonomous extensions;
- cocycle dynamics;
- skew-product systems;
- well-defined transfer operators.

The final target remains:

```

Periodic Orbits

```
    ↓
```

Weighted Orbit Expansion

```
    ↓
```

Dynamical Zeta

```
    ↓
```

Spectral Structure

```

---

# 2.3 Research Questions

Each exploration should investigate:

## Dynamical Structure

- Does the system possess rich periodic orbit structures?
- Can UPOs be enumerated reliably?
- Is symbolic coding available?
- Are unstable multipliers computable?

---

## Zeta Structure

Study:

\[
Z(s)=
\prod_\gamma
(1-w_\gamma e^{-sT_\gamma})^{-1}
\]

Questions:

- Can meaningful weighted zeta functions be constructed?
- Are zeros/poles stable under increasing truncation?
- Are different formulations consistent?

---

## Spectral Structure

Investigate:

- transfer operators;
- Ruelle–Perron–Frobenius operators;
- finite-rank approximations;
- spectral determinants;
- possible operator interpretations.

---

# 3. Literature and Research Tools

Installed research skills may be used.

Examples:

- literature retrieval;
- paper search;
- paper summarization;
- mathematical verification;
- experiment planning;
- code generation.

Relevant research areas:

- dynamical zeta functions;
- thermodynamic formalism;
- hyperbolic dynamics;
- symbolic dynamics;
- transfer operators;
- quantum chaos;
- arithmetic dynamics.

All important references should be recorded in the project directory.

---

# 4. Research Output Requirements

Each meaningful research direction should become an independent project.

Create a directory under the repository root:

```

project_name/

├── README.md
├── paper/
├── code/
├── experiments/
├── results/
└── notes/

```

Multiple projects are allowed.

Each project should preserve:

- research question;
- mathematical hypothesis;
- implementation;
- experimental results;
- failures and limitations;
- draft papers.

---

# 4.1 Final Project Summary

After completing exploration, create:

```

README.md

```

containing:

- explored systems;
- main findings;
- successful directions;
- failed directions;
- relation to Hilbert–Pólya goals;
- future research possibilities.

---

# 5. Repository Synchronization

The final research package should be synchronized to:

```

[https://github.com/maris205/hilbert-polya-structure](https://github.com/maris205/hilbert-polya-structure)

````

Requirements:

1. Use SSH authentication.

The SSH key has already been configured.

2. Before pushing:

```bash
git pull
````

Always synchronize with the latest repository state.

3. Create a unique directory.

Do not overwrite existing projects.

Example:

```
research/

├── henon_nonautonomous_exploration/

└── cocycle_zeta_search/
```

4. Commit all research materials:

* code;
* documents;
* experiment results;
* README files.

---

# Final Goal

Build an AI-assisted exploration framework for discovering possible
Hilbert–Pólya dynamical structures.

The goal is not only to search for successful constructions.

The goal is also to discover:

* impossible dynamical families;
* necessary structural constraints;
* promising mathematical directions.

Every exploration result contributes to the global search landscape.


```

这个版本之后，一个新 session 只需要：

1. 读 `propose.md`
2. 读 `skills/route-a-evaluator.md`
3. 读 `skills/route-b-evaluator.md`
4. 看 `prior_work`
5. 开自己的 project folder

就可以独立工作了。

而且多个 Pro 账号并行时不会互相污染，因为每个 session 最终交付的是：

```

# 一个项目目录

README + paper + code + results

```

这和真实数学研究组的协作方式非常接近。
```
