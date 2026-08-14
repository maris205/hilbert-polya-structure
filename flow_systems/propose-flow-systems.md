# Research Proposal

## Session 5 — Flow Systems: Classical Periodic Orbits, Quantum Spectra, and Trace Structures

---

# 1. Session Identity

This session explores **Flow Systems only**.

The central question is:

> Can continuous-time classical flows provide the natural periodic-orbit, action, phase, trace, and quantization structures required by an arithmetic Hilbert–Pólya candidate?

The conceptual research chain is:

```text
Arithmetic structure
        ↓
Symbolic / discrete dynamical skeleton
        ↓
Symplectic map geometry
        ↓
Continuous-time flow
        ↓
Primitive closed orbits
        ↓
Trace formula / dynamical Zeta
        ↓
Quantum spectrum / wave trace
        ↓
Possible Hilbert–Pólya realization
```

The defining theme of this session is:

```text
classical flow
vs.
quantum spectral realization
```

The session should remain focused on **continuous-time dynamical systems and their natural quantum/semiclassical counterparts**.

The working principle is:

```text
one session
=
one dynamical-system family
```

If a promising idea requires leaving flow systems and becoming an independent symbolic-only system, discrete symplectic-map project, quantum graph, cosmological model, operator-algebra program, or unrelated number-theoretic construction, record it as:

```text
ROUND2_CLUE
```

and do not expand that branch inside this session.

---

# 2. Research Philosophy

This session should be **bold in hypothesis generation and strict in later validation**.

Preferred workflow:

```text
大胆假设
    ↓
构造经典流
    ↓
找闭轨 / action / phase
    ↓
构造 trace / Zeta / quantization
    ↓
快速数值实验
    ↓
记录异常结构
    ↓
后续严格求证
```

The research policy is:

> Bold conjectures are encouraged. Proof may come later. Evidence levels must always remain explicit.

Do not reject an unusual flow because a complete theorem is not immediately available.

At the same time:

- numerical agreement is not proof;
- GUE statistics are not arithmetic evidence;
- a semiclassical trace formula is not automatically a fixed-operator identity;
- a local wave-trace contribution is not a global Riemann explicit formula;
- prime/prime-power information must ultimately arise intrinsically;
- Riemann-zero tables must not be used to define or tune the candidate.

The goal of the first round is to discover:

- viable flow families;
- structural obstructions;
- classical-to-quantum interfaces;
- arithmetic compatibility;
- trace-formula mechanisms;
- reusable negative results.

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

These documents define the validation framework.

This proposal does not duplicate their detailed gates.

### Route A

Use Route A to evaluate:

```text
A0 arithmetic relevance
A1 primitive periodic orbits / closed orbits
A2 dynamical Zeta / Fredholm determinant
A3 analytic structure / Weil-compression compatibility
A4 natural quantization or operator lift
```

### Route B

Use Route B only for strong candidates that already possess a coherent classical-to-quantum continuation.

Do not use Route B to rescue a weak classical-flow fit.

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

- arithmetic structure must remain primary;
- low-dimensional dynamics supplies prototypes and obstructions;
- Hénon provides a geometric bridge;
- symplectic structure supplies a classical Hamiltonian carrier;
- finite spectral resemblance is weaker than a trace identity;
- prime powers must ultimately appear on the arithmetic side;
- the 2026 Weil finite-compression result provides a rigorous arithmetic/operator benchmark.

These papers provide clues and constraints, not final answers.

---

## 3.3 Literature tools

Codex may freely use installed academic-research skills for:

- literature search;
- paper retrieval;
- citation tracing;
- mathematical verification;
- code generation;
- numerical experiments;
- trace-formula literature;
- semiclassical analysis;
- dynamical-systems computation.

Use literature **on demand**.

Do not create a large static `related_programs/` directory for this session.

Keep the fixed context small.

---

# 4. Main Research Objective

Explore whether continuous-time flows provide a stronger and more natural setting for the Hilbert–Pólya program than discrete maps alone.

The main structural hypothesis is:

> The arithmetic object may ultimately require genuine closed-orbit lengths, continuous return times, actions, phases, and a trace formula that are more naturally expressed by a flow than by a map.

The central classical-to-quantum comparison is:

```text
Classical flow
        ↓
primitive closed orbits
        ↓
actions / periods / stability
        ↓
trace formula
        ↓
quantum operator or propagator
        ↓
spectral fluctuations
```

The session should determine which parts of this chain can be made exact and which remain semiclassical or heuristic.

---

# 5. Primary Exploration Family

The session may explore, among others:

```text
Hamiltonian flows
Anosov flows
geodesic flows
contact Anosov flows
suspension flows
Axiom-A flows
hyperbolic billiard flows
open hyperbolic flows
scattering flows
continuous-time lifts of symplectic maps
coupled Hamiltonian flows
higher-dimensional conservative flows
```

This list is not restrictive.

Codex may propose other continuous-time flow families if mathematically natural.

The primary object must remain a **continuous-time flow**, not merely a discrete map with renamed variables.

---

# 6. Classical vs Quantum

This is the defining comparison of Session 5.

For each serious classical flow, ask whether there is a natural quantum or semiclassical counterpart.

Compare:

```text
classical primitive closed orbit
        ↔
quantum spectral oscillation
```

Possible quantum objects include:

- self-adjoint Hamiltonians;
- unitary propagators;
- Laplace-type operators;
- Schrödinger operators;
- scattering operators;
- transfer/resonance operators;
- Fourier-integral operators;
- natural quantizations of the classical flow.

The quantum object must arise from the classical system.

Do not define a quantum operator only because its eigenvalues can be fitted to Riemann zeros.

---

# 7. Core Research Questions

## 7.1 Arithmetic naturality

The first hard question remains:

> Why should this flow have anything to do with rational primes?

Generic Hamiltonian chaos is not enough.

Search for intrinsic mechanisms that could produce or preserve:

\[
p \longleftrightarrow \gamma_p,
\]

with primitive closed orbit \(\gamma_p\), and:

\[
p^r \longleftrightarrow \gamma_p^r.
\]

The ideal period law is:

\[
T_{\gamma_p}\sim \log p,
\]

or, more strongly,

\[
T_{\gamma_p}= \log p
\]

for a mathematically natural reason.

The ideal amplitude structure is:

\[
A_{\gamma_p,r}
\sim
(\log p)p^{-r/2},
\]

including:

- sign;
- phase;
- orientation;
- stability;
- repetition;
- multiplicity.

Do not insert `T_p = log p` by hand.

Do not insert von Mangoldt weights manually.

Do not tune the classical flow using Riemann-zero data.

If arithmetic structure is inherited from a symbolic or symplectic parent, study how it survives the continuous-time lift.

---

## 7.2 Primitive closed-orbit structure

For each candidate, determine:

- primitive closed orbits;
- repeated closed orbits;
- periods;
- actions;
- monodromy / Poincaré maps;
- stability exponents;
- Maslov-type indices where natural;
- orientation and phase information;
- orbit bifurcations;
- completeness / missed-orbit risk.

The flow should have a precise primitive/repetition ledger.

A central question is:

> Does continuous time produce an orbit-length structure unavailable in purely discrete systems?

---

## 7.3 Dynamical Zeta

Study natural continuous-time dynamical Zeta functions, including where appropriate:

\[
Z_{\mathrm{dyn}}(s)
=
\prod_{\gamma\ \mathrm{primitive}}
\left(1-w_\gamma e^{-sT_\gamma}\right)^{-1}.
\]

Possible frameworks include:

- Ruelle Zeta;
- Selberg-type Zeta;
- dynamical Fredholm determinants;
- transfer-operator determinants;
- resonance determinants;
- flow-specific Zeta constructions.

Investigate:

- convergence;
- meromorphic / entire continuation;
- primitive/repetition consistency;
- signed or complex weights;
- stability factors;
- extra/missing zeros;
- divisor counting;
- growth order;
- cutoff stability;
- relation to classical resonances.

Do not select a Zeta convention only because it resembles \(\zeta(s)\).

---

## 7.4 Trace formulas

This session should explicitly study trace formulas.

The target structural form is:

\[
\operatorname{Tr} f(H)
=
\text{smooth term}
+
\sum_{\gamma}
A_\gamma \widehat f(T_\gamma),
\]

or an equivalent wave-trace / propagator identity.

Questions:

- Is the trace formula exact or semiclassical?
- Is it local or global?
- Does it apply to one orbit or the full primitive orbit set?
- Are amplitudes intrinsic?
- Are phases intrinsic?
- Is the remainder controlled?
- Does the formula hold for a fixed operator or only in a semiclassical limit?

A central distinction is:

```text
local semiclassical orbit contribution
≠
global fixed-operator arithmetic trace formula
```

Do not exchange these two without a theorem.

---

## 7.5 Fixed-operator vs semiclassical limits

This is a mandatory conceptual audit.

Many classical/quantum trace results are obtained in a limit such as:

\[
\hbar\to0
\]

with energy in a controlled region.

Hilbert–Pólya ultimately requires a fixed operator and global high-energy information, conceptually closer to:

\[
\hbar=1,\qquad E\to\infty.
\]

For every quantum candidate, record explicitly:

- what parameter tends to infinity or zero;
- whether the operator changes with the limit;
- whether the result is local in energy;
- whether the trace identity is uniform;
- whether the fixed-operator high-energy regime is controlled.

Do not treat a local semiclassical theorem as a global spectral theorem.

---

## 7.6 Quantum spectral host

For strong candidates, investigate whether the quantum object has:

- a natural Hilbert space;
- a mathematically complete operator;
- self-adjointness;
- discrete spectrum or the appropriate resonance structure;
- compact resolvent or another precise spectral mechanism;
- Riemann–von Mangoldt-like counting;
- a natural spectral determinant.

This is where limited Route B analysis may begin.

---

# 8. Suggested Research Stages

Every research stage must produce **one paper project** under `papers/`.

Codex may refine or split these stages if necessary, but each project must remain within the Flow Systems session.

---

## Stage 1 — Classical Flow Baseline

Suggested paper directory:

```text
papers/1-classical-flow/
```

Goal:

Identify classical flow families with the richest and most natural primitive closed-orbit structure.

Focus:

```text
Route A / A0-A1
```

Possible tasks:

- compare Hamiltonian / Anosov / geodesic / suspension families;
- enumerate short primitive closed orbits;
- compute periods, actions and monodromy;
- identify natural symbolic codings;
- test arithmetic naturality;
- classify obvious obstructions.

A negative classification is a successful result.

---

## Stage 2 — Flow Zeta and Resonance Structure

Suggested paper directory:

```text
papers/2-flow-zeta/
```

Goal:

Construct the natural dynamical Zeta / Fredholm / resonance object for the strongest classical flow.

Focus:

```text
Route A / A1-A3
```

Possible outputs:

- primitive/repetition ledger;
- Ruelle-type Zeta;
- determinant identities;
- resonance calculations;
- analytic continuation;
- divisor-counting law;
- cutoff stability;
- signed/complex cancellation.

---

## Stage 3 — Classical vs Quantum Trace

Suggested paper directory:

```text
papers/3-trace-bridge/
```

Goal:

Test whether classical periodic-orbit data actually appears in a natural quantum trace or wave-trace object.

Focus:

```text
Route A / A3-A4
```

Investigate:

- wave trace;
- propagator trace;
- Gutzwiller-type formula;
- exact trace formulas where available;
- orbit actions / Maslov phases;
- local spectral oscillations;
- fixed-operator vs semiclassical distinction.

This stage should explicitly separate:

```text
one certified orbit contribution
```

from:

```text
full global trace formula
```

---

## Stage 4 — Arithmetic Flow Search

Suggested paper directory:

```text
papers/4-arith-flow/
```

Goal:

Search boldly for continuous-time mechanisms that could naturally produce prime/prime-power closed-orbit structure.

Focus:

```text
Route A / A0-A3
```

Questions:

- Can logarithmic prime-like periods emerge from a natural roof or action?
- Can a suspension flow geometrically realize an arithmetic symbolic skeleton?
- Can phase, holonomy, orientation, or representation data produce the required signed/complex weights?
- Can prime-power repetition arise without explicit prime encoding?
- Can a geometric flow naturally reproduce the arithmetic side of an explicit formula?

This stage is explicitly encouraged to make bold hypotheses.

Proof may follow later.

---

## Stage 5 — Fixed Quantum Operator Candidate

Suggested paper directory:

```text
papers/5-quantum-flow/
```

Open only for the strongest surviving flow candidate.

Goal:

Construct or identify a fixed quantum operator naturally associated with the flow and test whether it could serve as a spectral host.

Focus:

```text
Route A / A4
Route B / B1-B3 if justified
```

Investigate:

- operator definition;
- Hilbert space;
- domain;
- self-adjointness;
- spectral type;
- counting law;
- spectral determinant;
- high-energy behavior.

---

## Stage 6 — Prime Trace / Weil Interface

Suggested paper directory:

```text
papers/6-prime-trace/
```

Open only if previous stages produce a serious candidate.

Goal:

Test the strongest possible arithmetic/operator bridge.

Focus:

```text
Route A / A3-A4
Route B / B4 if justified
```

Investigate:

\[
\sum_p\sum_{r\ge1}
(\log p)p^{-r/2}
\]

against the candidate's primitive closed-orbit trace structure.

Also test possible finite Hermitian compressions:

\[
\operatorname{tr}G,
\qquad
\operatorname{tr}(G^2),
\qquad
n_+(G),
\qquad
n_-(G).
\]

Do not manually construct the arithmetic weights.

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

For strong flow candidates, investigate whether the same classical/quantum object admits a comparable finite compression.

The key question is:

> Can the arithmetic prime-power side and the classical/quantum trace side be two readings of the same mathematical structure?

This is a benchmark, not a template that must be copied literally.

If the bridge is not natural, record that as an obstruction.

---

# 10. Classical vs Quantum Controls

Whenever possible, compare:

```text
classical flow data
        vs.
quantum spectral data
```

using controls such as:

- randomized orbit periods;
- randomized actions;
- randomized phases;
- nearby Hamiltonians;
- integrable versions;
- weakly chaotic versions;
- dissipative perturbations;
- systems with similar Weyl law but different periodic-orbit structure;
- false-RH analogues where relevant.

This helps distinguish:

```text
generic spectral statistics
```

from:

```text
arithmetic-specific trace structure.
```

---

# 11. Scope Discipline

## Allowed

Remain within Flow Systems while varying:

- Hamiltonian flow family;
- hyperbolic / Anosov flow;
- geodesic flow;
- suspension flow;
- billiard / scattering flow;
- dimension;
- coupling;
- energy surface;
- classical transfer/resonance operator;
- dynamical Zeta;
- natural quantization;
- trace formula;
- fixed quantum counterpart.

## Not allowed as a new main branch

Do not independently launch:

- discrete symplectic-map programs;
- pure symbolic-dynamics programs;
- quantum-graph programs;
- cosmological models;
- general von Neumann-algebra programs;
- unrelated analytic-number-theory programs.

When such a direction appears:

```text
ROUND2_CLUE
```

Record it and return to the flow session.

---

# 12. Local Session Output Standard

All outputs in the current session directory are the **local working copy**.

The session root must contain:

```text
README.md
papers/
```

Create `papers/` immediately.

---

## 12.1 Paper project naming

Every research stage must generate one paper project under:

```text
papers/
```

Naming convention:

```text
<sequence_number>-<short_paper_name>/
```

The sequence number starts from `1` and increases monotonically.

Example:

```text
papers/
├── 1-classical-flow/
├── 2-flow-zeta/
├── 3-trace-bridge/
├── 4-arith-flow/
├── 5-quantum-flow/
└── 6-prime-trace/
```

The short name must remain concise.

---

## 12.2 Required paper project contents

Each paper project should contain at least:

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

Additional subdirectories are allowed.

The project should be self-contained enough to reproduce its main results.

---

## 12.3 Author information

All papers are non-anonymous.

Use:

```text
Liang Wang
School of Artificial Intelligence and Automation
Huazhong University of Science and Technology (HUST)
wangliang.f@gmail.com
```

Do not use anonymous placeholders.

---

## 12.4 PDF requirement

Every paper project must eventually produce:

```text
paper/paper.pdf
```

Exploratory, speculative, numerical, partial-theorem, and obstruction papers are all allowed.

Claims must remain honest about evidence level.

A speculative paper is allowed.

A misleading paper is not.

---

# 13. Session README Standard

Create at the session root:

```text
README.md
```

Whenever a paper project reaches a meaningful stage, append **one line**.

Required format:

```text
论文子目录名称 - 当前阶段 - 主要进展
```

Examples:

```text
1-classical-flow - Route A / A0-A1 - 完成多类经典流的闭轨与算术相关性基线比较，筛出两个值得继续的候选族
2-flow-zeta - Route A / A1-A3 - 构造候选流的 primitive/repetition ledger 与 Ruelle Zeta，完成首轮解析和截断稳定性测试
3-trace-bridge - Route A / A3-A4 - 认证经典闭轨对量子波迹的非零贡献，并明确局部半经典与固定算子全局极限的边界
4-arith-flow - Route A / A0-A3 - 提出一个不直接编码素数表的 arithmetic suspension/flow 候选并完成首轮对照
```

The root README is a **progress index**.

Do not overwrite old lines.

Append chronologically.

---

# 14. Session-Level Final Summary

At the end of Session 5, the root `README.md` and/or final summary should make it easy to answer:

1. Which flow families were explored?
2. Which had genuine arithmetic relevance?
3. Which had the strongest primitive closed-orbit structure?
4. Which admitted natural dynamical Zeta functions?
5. Which trace formulas were exact, semiclassical, or only heuristic?
6. Which classical orbit signals appeared in quantum spectra?
7. Which results were local and which were global?
8. Which candidates admitted natural self-adjoint operators?
9. Which had the correct high-energy counting scale?
10. Which obstructions prevented a prime-power trace formula?
11. Which `ROUND2_CLUE` items should survive?
12. What is the strongest positive result?
13. What is the strongest negative result?

The final result may be:

- a surviving flow candidate;
- a trace-formula theorem;
- a local classical-to-quantum bridge;
- an obstruction;
- an impossibility result;
- a precise second-round interface.

All are valuable.

---

# 15. GitHub Synchronization Standard

The GitHub repository is:

```text
git@github.com:maris205/hilbert-polya-structure.git
```

Inside that repository create exactly one session subdirectory:

```text
flow_systems/
```

The GitHub target should therefore look like:

```text
hilbert-polya-structure/
└── flow_systems/
    ├── README.md
    ├── papers/
    ├── propose.md
    ├── skills/
    ├── docs/
    └── any other files present in the local session directory
```

The rule is:

> Everything in the local session directory should be synchronized into the GitHub `flow_systems/` subdirectory.

Do not scatter Session 5 outputs across unrelated repository locations.

Do not create nested duplicate paths such as:

```text
flow_systems/flow_systems/
```

---

## 15.1 Synchronization procedure

Before pushing:

```bash
git pull
```

Then synchronize the current session directory into:

```text
flow_systems/
```

Preserve:

- paper projects;
- code;
- experiments;
- results;
- README;
- proposal;
- skills used by the session;
- reproducibility notes.

Commit with clear messages.

Push only after checking that no unrelated project directory is overwritten.

---

# 16. Research Execution Policy

Codex should operate autonomously inside the defined scope.

It may:

- search literature;
- formulate hypotheses;
- define classical flows;
- write simulation code;
- compute periodic orbits;
- compute actions and monodromy;
- construct dynamical Zeta functions;
- study resonances;
- construct or identify quantizations;
- test wave traces;
- attempt proofs;
- build counterexamples;
- create paper projects;
- revise failed hypotheses.

Desired behavior:

```text
大胆假设
+
快速实验
+
持续记录
+
严格区分证据等级
```

Do not wait for a complete theorem before exploring an interesting idea.

But once a claim is promoted into a Route-A / Route-B pass, use the evaluators strictly.

---

# 17. Final Goal

The purpose of Session 5 is to determine whether **continuous-time flow systems provide the missing bridge between arithmetic periodic-orbit structure and quantum spectral structure**.

The main hypothesis to test is:

```text
Arithmetic symbolic skeleton
        ↓
Symplectic geometric carrier
        ↓
Continuous-time flow
        ↓
Primitive closed orbits
        ↓
Trace formula
        ↓
Quantum spectrum
```

This is a research hypothesis, not an assumption.

The most valuable outcomes include:

- a natural arithmetic flow candidate;
- a rigorous Ruelle/Fredholm Zeta;
- a classical closed-orbit trace theorem;
- a certified classical-to-quantum spectral bridge;
- a fixed self-adjoint quantum host;
- a prime-power trace obstruction;
- a high-quality `ROUND2_CLUE`.

The session should remain easy to understand:

```text
one system family
one sequence of paper projects
one root README progress index
one GitHub directory
```

Keep the scientific imagination broad.

Keep the project structure simple.

**Bold conjectures are encouraged.**

**Classical and quantum structures should be compared aggressively.**

**Proof can come later, but formal Route-A / Route-B claims must be strict.**
