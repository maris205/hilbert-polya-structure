# Research Proposal

## Session 3 — Symplectic Maps: Hamiltonian Chaos, Conservative Geometry, and Dissipative Controls

---

# 1. Session Identity

This session explores **Symplectic Maps only**.

The central question is:

> Can the arithmetic structures suggested by low-dimensional chaotic prototypes be lifted into conservative/symplectic dynamics, where periodic-orbit geometry, phase information, Hamiltonian chaos, and natural quantization become available?

The conceptual research chain is:

```text
Logistic-type arithmetic seed
        ↓
Hénon-type geometric bridge
        ↓
Symplectic maps / Hamiltonian chaos
        ↓
Periodic-orbit geometry
        ↓
Dynamical Zeta / trace structure
        ↓
Possible quantum / operator lift
```

The session should remain focused on **symplectic discrete-time dynamical systems**.

The working principle is:

```text
one session
=
one dynamical-system family
```

If a promising idea requires leaving symplectic maps and becoming an independent flow, quantum graph, symbolic-only system, operator-algebra program, cosmological model, or unrelated Hamiltonian theory, record it as:

```text
ROUND2_CLUE
```

and do not expand that branch in this session.

---

# 2. Research Philosophy

This session should be **bold in hypothesis generation and strict in later validation**.

The preferred research style is:

```text
大胆假设
    ↓
快速构造
    ↓
数值与结构探索
    ↓
记录异常信号
    ↓
再逐步严格求证
```

> Hypothesis generation may be aggressive and speculative. Proof obligations can be closed later, but every claim must be labeled honestly.

Do not reject a potentially interesting direction merely because a theorem is not immediately available.

At the same time:

- numerical evidence is not proof;
- GUE-like statistics are not arithmetic evidence;
- a beautiful symplectic structure is not enough by itself;
- prime/prime-power information must ultimately arise intrinsically;
- target Riemann zeros must not be used to define the candidate.

The purpose of the first round is to **discover structure, map obstructions, and identify promising symplectic families**.

---

# 3. Current Resources

The repository is the primary source of truth.

## 3.1 Evaluation skills

Use when needed:

```text
skills/
├── route-a-evaluator.md
└── route-b-evaluator.md
```

These documents define the evaluation framework.

This proposal does not duplicate their detailed gates.

### Route A

Use Route A to evaluate:

```text
A0 arithmetic relevance
A1 primitive periodic orbits
A2 dynamical Zeta / Fredholm determinant
A3 analytic structure / Weil-compression compatibility
A4 natural quantization or operator lift
```

### Route B

Route B should only be used for strong candidates that have a natural operator-level continuation.

Do not use Route B to rescue a weak Route-A construction.

---

## 3.2 Core prior work

Read:

```text
docs/prior_work/README.md
docs/prior_work/papers/
```

The six core papers provide the project lineage:

```text
prime / chaos relation
        ↓
one-dimensional obstruction
        ↓
non-autonomous dynamics
        ↓
finite spectral experiments
        ↓
area-preserving Hénon / conservative geometry
        ↓
prime-side arithmetic ↔ finite operator geometry
```

For this session, especially relevant ideas include:

- the arithmetic seed from low-dimensional dynamics;
- one-dimensional topological obstructions;
- the Hénon map as a geometric bridge;
- the distinction between dissipative and area-preserving dynamics;
- periodic-orbit / Fredholm thinking;
- the 2026 Weil finite-compression benchmark linking prime powers to operator geometry.

These papers provide clues and constraints, not conclusions.

---

## 3.3 Literature tools

Codex may freely use installed academic-research skills for:

- literature search;
- paper retrieval;
- citation tracing;
- mathematical verification;
- experiment design;
- code generation;
- numerical analysis.

Use literature **on demand**.

Do not create a large `related_programs/` knowledge base for this session.

Keep the fixed context small and let Codex explore freely inside the symplectic-map family.

---

# 4. Main Research Objective

Explore whether symplectic maps provide a more natural geometric carrier for arithmetic dynamical structure than one-dimensional or dissipative systems.

The main conceptual contrast is:

```text
dissipative chaos
vs.
conservative / symplectic chaos
```

The session should determine what is gained when one imposes:

\[
F^*\omega=\omega
\]

or, in two dimensions,

\[
\det DF = 1.
\]

Important questions include:

- Does symplecticity produce richer primitive periodic-orbit geometry?
- Does it preserve phase information needed for signed/complex orbit sums?
- Does it improve stability of dynamical Zeta constructions?
- Does it provide a natural path to unitary/Fourier-integral quantization?
- Can arithmetic structure survive the lift from Logistic/Hénon-type prototypes?
- Which features disappear when the same map is made dissipative?

The dissipative case is primarily a **matched control**, not a separate main research family.

---

# 5. Primary Exploration Family

The session may explore, among others:

```text
area-preserving Hénon maps
standard / Chirikov–Taylor maps
kicked-rotor maps
kicked-Harper-type maps
cat maps and perturbed cat maps
twist maps
reversible symplectic maps
coupled symplectic maps
higher-dimensional symplectic maps
symplectic map lattices
time-dependent compositions of symplectic maps
symplectic cocycles that remain discrete-time map systems
```

This list is not restrictive.

Codex may propose other symplectic-map families when mathematically natural.

The primary object must remain a **discrete symplectic map or a composition/coupling of such maps**.

Area-preserving Hénon may be used as the bridge from the Hénon session, but this session should not simply repeat the Hénon exploration.

---

# 6. Conservative vs Dissipative Comparison

This is one of the defining themes of Session 3.

Whenever possible, construct matched pairs:

```text
conservative / symplectic version
        vs.
dissipative perturbation
```

For example, compare:

- \(\det DF = 1\) against \(|\det DF|<1\);
- area-preserving Hénon against dissipative Hénon;
- symplectic coupling against weak damping;
- reversible maps against irreversible perturbations.

Compare the following quantities:

- periodic-orbit count;
- primitive/repetition structure;
- monodromy spectrum;
- Lyapunov structure;
- recurrence;
- orbit actions or return times;
- dynamical Zeta stability;
- spectral determinant stability;
- phase/sign structure;
- quantization naturality.

The purpose is to isolate:

> Which structures are genuinely consequences of conservative/symplectic geometry?

A negative result is valuable.

---

# 7. Core Research Questions

## 7.1 Arithmetic naturality

The first hard question remains:

> Why should this symplectic system have anything to do with rational primes?

Do not treat generic Hamiltonian chaos, GUE statistics, or a rich UPO set as sufficient.

Search for intrinsic mechanisms that could produce or preserve:

\[
p \longleftrightarrow \gamma_p
\]

and

\[
p^r \longleftrightarrow \gamma_p^r.
\]

A stronger target is a natural orbit scale satisfying:

\[
T_{\gamma_p}\sim \log p
\]

and repetition amplitudes analogous to:

\[
A_{\gamma_p,r}
\sim
(\log p)p^{-r/2},
\]

including correct sign, phase, orientation, and multiplicity structure.

Do not define orbit periods as \(\log p\) by hand.

Do not insert von Mangoldt weights manually.

Do not tune the candidate using a Riemann-zero table.

If arithmetic structure is inherited from a lower-dimensional parent, prove or numerically demonstrate how it survives the symplectic lift.

---

## 7.2 Primitive periodic-orbit geometry

For each candidate, determine:

- primitive periodic orbits;
- repeated orbits;
- stability matrices;
- elliptic / hyperbolic classification;
- stable and unstable directions;
- Maslov-like or orientation information where natural;
- actions / generating functions where available;
- orbit bifurcations;
- completeness and missed-orbit risk.

A central question is whether the symplectic system supports an orbit ledger substantially richer than the Logistic or ordinary Hénon prototypes.

---

## 7.3 Dynamical Zeta / Fredholm determinant

Study natural orbit products such as:

\[
Z_{\mathrm{dyn}}(s)
=
\prod_{\gamma}
\left(1-w_\gamma e^{-sT_\gamma}\right)^{-1}
\]

or transfer/Fredholm objects:

\[
D(s)=\det(I-\mathcal L_s).
\]

Investigate:

- primitive/repetition consistency;
- convergence;
- cycle expansion;
- signed/complex cancellations;
- cutoff stability;
- precision stability;
- extra/missing divisor structure;
- analytic continuation;
- \(T\log T\)-type counting where meaningful.

The determinant must arise from the same dynamical object.

Do not glue incompatible orbit and spectral constructions.

---

## 7.4 Hamiltonian-chaos structure

Investigate whether symplecticity provides structures absent in dissipative systems:

- action variables;
- generating functions;
- canonical transformations;
- stable/unstable manifolds;
- homoclinic/heteroclinic geometry;
- KAM-to-chaos transitions;
- periodic-orbit action spectra;
- natural phases;
- semiclassical trace ingredients.

The goal is not merely to show "Hamiltonian chaos exists".

The goal is to identify structures potentially useful for an arithmetic trace formula.

---

## 7.5 Natural quantization

For the strongest candidates, ask whether the map admits a natural quantization:

\[
F \longrightarrow U_F
\]

with \(U_F\) unitary, or an equivalent canonical quantum map/Fourier-integral operator construction.

Questions:

- Is the quantization intrinsic?
- Is the Hilbert space natural?
- Are boundary conditions fixed before looking at target zeros?
- Does the classical orbit structure appear in the quantum trace?
- Are orbit phases and Maslov-type data preserved?
- Does the conservative system quantize more naturally than its dissipative control?

This is exploratory unless Route A explicitly reaches A4.

---

# 8. Suggested Research Stages

Every research stage must produce **one paper project** under `papers/`.

The following stages are recommended as an initial roadmap.

Codex may refine or split them if the mathematics demands it, but each distinct stage must remain within the symplectic-map family.

---

## Stage 1 — Conservative vs Dissipative Structural Baseline

Suggested paper directory:

```text
papers/1-symp-vs-diss/
```

Goal:

Compare matched conservative and dissipative map families and determine which periodic-orbit and spectral structures are specifically promoted by symplecticity.

Focus:

```text
Route A: A0–A1
```

Possible outputs:

- matched Hénon/standard-map controls;
- UPO census;
- monodromy comparison;
- recurrence / phase-space diagnostics;
- first arithmetic-naturalness audit;
- negative theorem or numerical obstruction.

---

## Stage 2 — Symplectic Periodic-Orbit Zeta

Suggested paper directory:

```text
papers/2-symp-zeta/
```

Goal:

For the strongest map from Stage 1, construct the most natural primitive-orbit ledger and dynamical Zeta/Fredholm object.

Focus:

```text
Route A: A1–A2
```

Possible outputs:

- complete low-period UPO ledger;
- primitive/repetition decomposition;
- stability weights;
- signed/complex cycle weights;
- cycle-expansion convergence;
- cutoff and precision tests;
- analytic or numerical determinant study.

---

## Stage 3 — Arithmetic Symplectic Search

Suggested paper directory:

```text
papers/3-arith-symp/
```

Goal:

Search boldly for symplectic mechanisms that generate, preserve, or geometrically realize arithmetic structure without directly encoding prime tables.

Focus:

```text
Route A: A0–A2
```

Questions:

- Can arithmetic coding from lower-dimensional prototypes survive a symplectic lift?
- Can return times/actions naturally acquire logarithmic arithmetic scaling?
- Can group, orientation, symmetry, or canonical phase data generate signed/complex weights?
- Can repeated orbit structure resemble prime powers without manual construction?

This stage is explicitly encouraged to make bold hypotheses.

Proof may follow later.

---

## Stage 4 — Higher-Dimensional / Coupled Symplectic Maps

Suggested paper directory:

```text
papers/4-highdim-symp/
```

Goal:

Test whether higher-dimensional or coupled symplectic maps overcome structural limitations found in 2D systems.

Focus:

```text
Route A: A1–A3
```

Explore:

- coupled maps;
- symplectic map lattices;
- multi-degree-of-freedom maps;
- high-dimensional hyperbolic structures;
- orbit-counting growth;
- determinant growth;
- phase cancellation;
- possible \(T\log T\)-type behavior.

This is the natural place to test whether the dimensional lift genuinely increases arithmetic capacity.

---

## Stage 5 — Symplectic Quantization and Trace Interface

Suggested paper directory:

```text
papers/5-symp-quant/
```

Open this stage only for candidates that survive the earlier stages.

Goal:

Study the natural classical-to-quantum interface of the strongest symplectic candidate.

Focus:

```text
Route A: A3–A4
limited Route B only if justified
```

Investigate:

- unitary quantization;
- Fourier-integral operators;
- wave/trace formulas;
- periodic-orbit contributions to spectral oscillations;
- finite Weil-compression analogues;
- prime-side / operator-side compatibility.

Do not claim Hilbert–Pólya unless the corresponding Route-B gates are actually closed.

---

# 9. Weil / Explicit-Formula Benchmark

The sixth core paper provides a rigorous benchmark:

```text
prime powers
        ↔
explicit formula
        ↔
finite Hermitian compression
        ↔
trace / second moment / inertia
        ↔
zero information
```

For strong symplectic candidates, investigate whether a natural finite compression can be derived from the candidate.

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

The central question is:

> Can the same symplectic object be read from both an orbit/geometric side and an arithmetic prime-power side?

Do not artificially add a Weil-type form only to pass this benchmark.

If no natural bridge exists, record the obstruction.

---

# 10. Falsification and Controls

Exploration should be bold, but serious candidates must eventually face controls.

Useful controls include:

- dissipative versions of the same map;
- randomized orbit lengths;
- randomized phases;
- shuffled arithmetic labels;
- matched-density non-prime sequences;
- neighboring parameters;
- simpler parent maps;
- known false-RH analogues when mathematically relevant.

A mechanism that proves too much should be rejected or scoped.

Use the evaluator skills for formal gate decisions.

---

# 11. Scope Discipline

## Allowed

Stay within the symplectic-map family while varying:

- dimension;
- coupling;
- map family;
- conservative parameter regime;
- dissipative control perturbation;
- symplectic cocycle;
- time-dependent composition of symplectic maps;
- transfer operator;
- natural Zeta;
- natural quantization.

## Not allowed as a new main branch

Do not independently launch:

- continuous Hamiltonian-flow projects;
- pure symbolic-dynamics projects;
- quantum-graph projects;
- cosmological models;
- von Neumann-algebra programs;
- unrelated operator constructions.

When such a direction appears:

```text
ROUND2_CLUE
```

Record it and return to the symplectic-map session.

---

# 12. Local Session Output Standard

All outputs in the current session directory are considered the **local working copy**.

The session directory must contain:

```text
README.md
papers/
```

Create `papers/` immediately when the session starts.

---

## 12.1 Paper project structure

Every research stage must generate one paper project.

Each paper project is a subdirectory under:

```text
papers/
```

Naming convention:

```text
<sequence_number>-<short_paper_name>/
```

The sequence number starts at `1` and increases monotonically.

Examples:

```text
papers/
├── 1-symp-vs-diss/
├── 2-symp-zeta/
├── 3-arith-symp/
├── 4-highdim-symp/
└── 5-symp-quant/
```

The short name should be concise and descriptive.

Do not use long titles as directory names.

---

## 12.2 Required contents of every paper project

Each paper directory should contain at least:

```text
<sequence>-<short_name>/

├── README.md
├── paper/
│   ├── manuscript.tex
│   ├── references.bib
│   ├── figures/
│   └── paper.pdf
│
├── code/
├── experiments/
├── results/
└── notes/
```

Additional subdirectories are allowed when needed.

The paper project must be self-contained enough to reproduce its main results.

---

## 12.3 Paper author information

All papers are non-anonymous.

Use:

```text
Liang Wang
School of Artificial Intelligence and Automation
Huazhong University of Science and Technology (HUST)
wangliang.f@gmail.com
```

Do not use anonymous author placeholders.

---

## 12.4 PDF requirement

Every paper project must eventually produce a compiled PDF:

```text
paper/paper.pdf
```

The PDF may initially describe exploratory or partial results.

Claims must still be labeled according to their evidence level.

A speculative paper is allowed.

A misleading paper is not.

---

# 13. Session README Standard

Create at session root:

```text
README.md
```

Every time a paper project reaches a meaningful stage, append **one line** to this file.

Required format:

```text
论文子目录名称 - 当前阶段 - 主要进展
```

Examples:

```text
1-symp-vs-diss - Route A / A0-A1 - 建立保守与耗散匹配对照，确认辛结构对周期轨道稳定性和相位信息的影响
2-symp-zeta - Route A / A1-A2 - 构造统一 primitive/repetition ledger 与动力学 Zeta，完成首轮截断稳定性测试
3-arith-symp - Route A / A0-A2 - 找到一个不直接编码素数表的候选算术辛提升机制，进入后续验证
```

The session README is a **progress index**, not a full paper summary.

Do not overwrite previous lines.

Append new progress chronologically.

---

# 14. Session-Level Final Summary

At the end of Session 3, the root `README.md` and/or a final session summary should make it easy to answer:

1. Which symplectic-map families were explored?
2. Which conservative/dissipative comparisons were decisive?
3. Which candidates had genuine arithmetic relevance?
4. Which primitive-orbit structures were strongest?
5. Which candidates produced natural Zeta/Fredholm objects?
6. Which obstructions were found?
7. Did higher dimension help?
8. Did symplecticity provide useful phase/sign structure?
9. Which candidates had a natural quantization?
10. Which `ROUND2_CLUE` items should survive?
11. What is the strongest positive result?
12. What is the strongest negative result?

The final session result may be a surviving candidate, an impossibility theorem, or a map of structural constraints.

All are valuable.

---

# 15. GitHub Synchronization Standard

The GitHub repository is:

```text
git@github.com:maris205/hilbert-polya-structure.git
```

Inside that repository create exactly one session subdirectory:

```text
symplectic_map/
```

The GitHub target should therefore look like:

```text
hilbert-polya-structure/
└── symplectic_map/
    ├── README.md
    ├── papers/
    ├── propose.md
    ├── skills/
    ├── docs/
    └── any other files present in the local session directory
```

The rule is:

> Everything in the local session directory should be synchronized into the GitHub `symplectic_map/` subdirectory.

Do not scatter Session 3 outputs across unrelated repository locations.

Do not create nested duplicate paths such as:

```text
symplectic_map/symplectic_map/
```

---

## 15.1 Synchronization procedure

Before pushing:

```bash
git pull
```

Then synchronize the current session directory into:

```text
symplectic_map/
```

Preserve:

- paper projects;
- code;
- experiments;
- results;
- README;
- proposal;
- skills used by the session;
- local notes needed for reproducibility.

Commit with clear messages.

Push only after checking that no unrelated project directory is overwritten.

---

# 16. Research Execution Policy

Codex should operate autonomously inside the defined scope.

It may:

- search literature;
- formulate hypotheses;
- write code;
- run numerical experiments;
- derive formulas;
- attempt proofs;
- produce counterexamples;
- create paper projects;
- revise failed ideas;
- compare conservative/dissipative controls.

The desired research behavior is:

```text
大胆假设
+
快速实验
+
持续记录
+
严格区分证据等级
```

Do not wait for complete proof before exploring a promising idea.

But once a claim is promoted into a theorem or a Route-A/Route-B pass, apply the relevant evaluator strictly.

---

# 17. Final Goal

The purpose of Session 3 is to determine whether **symplectic dynamics is a plausible geometric mother family for arithmetic Hilbert–Pólya candidates**.

The key hypothesis to explore is:

```text
Logistic supplies an arithmetic seed
        ↓
Hénon supplies a geometric bridge
        ↓
Symplectic maps supply the conservative geometric mother structure
```

This is a research hypothesis, not an assumption.

The session should test it aggressively.

The most valuable outcomes include:

- a natural arithmetic symplectic candidate;
- a rigorous periodic-orbit Zeta;
- a conservative-vs-dissipative structural theorem;
- a higher-dimensional symplectic lift;
- a natural quantization;
- a strong obstruction;
- a reusable `ROUND2_CLUE`.

The session should remain easy to understand:

```text
one system family
one sequence of paper projects
one root README progress index
one GitHub directory
```

Keep the scientific imagination broad.

Keep the project structure simple.

**Bold conjectures are encouraged. Proof can come later.**
