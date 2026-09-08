# P7 continuation: invariant fibres and the singular-stratum gate

2026-09-08 UTC. This is one continuation of the original source-owned
question, not a fresh conjecture or new paper slot. Only this directory
is writable by this delegate. The coordinator owns all admission decisions.

## Unchanged full contract

Use the exact seven branches and resolved state set in
[round-seven P7](../../continuation_round7/charp_scout/FROZEN_CONTRACTS.md#p7--finite-field-q-painlevé-i-uniform-native-periods).
For every finite field $\mathbb F_q$, every $s,t_0\in\mathbb F_q^*$ and
$r=\operatorname{ord}(s)$, retain every state over phases
$t\in t_0\langle s\rangle$ in
$$
\bigl(\{0\}\times(\mathbb F_q^*)^2\bigr)
\sqcup\bigsqcup_{j=1}^4\bigl(\{j\}\times\{0\}\times\mathbb F_q\bigr).
$$
The native clock is one original update, always including $t\mapsto st$.
The target is the original assertion
$$
\ell/r\le q+1+2\sqrt q
$$
for the least native period $\ell$ of every such state. The four exceptional
lines, their zero coordinates, all phase orders and all characteristics
remain in scope. Torus-only dynamics, generic fibres and bounded $r$ do
not replace this question.

This is Joshi–Roffelsen, Conjecture 1.2.A in the
[accessed v2 body](https://arxiv.org/html/2508.18578v2).
Its invariant construction is prior ownership. The body's explicit
conjecture labels, not the stronger metadata abstract, govern this attempt.

## Proposed mechanism and first falsification check

The proposed full proof has three separate obligations:

1. Construct the actual dynamical pencil on the resolved surface over
   $\mathbb F_q$, identify the fibre containing each ordinary state,
   and prove that the phase-return map preserves that fibre.
2. Prove its geometrically connected smooth fibres have genus one, with
   a valid finite-field argument including characteristics two and three.
   A complex-analytic period-map statement cannot simply be reduced
   modulo every prime.
3. Classify every surviving singular/reducible/nonreduced fibre and its
   component action. Prove the required orbit bound there, not merely
   on a generic smooth normalization.

The first cheap gate is the third obligation. A reducible multiplicative
fibre with a nontrivial component permutation could in principle have
longer cycles than its individual rational components. This is an
unproved concern to test, not a claimed counterexample. Begin with exact
exceptional-chart dynamics and the autonomous $s=1$ pencil, then determine
which conclusions genuinely extend to arbitrary $r$.

In parallel with that hand analysis, inspect the cited Halphen-pencil
construction and the source's spectral equation after the substitution
$Z=z^r$. A genus-one spectral quotient is not automatically the same
curve as the dynamical invariant fibre: an explicit identification,
controlled correspondence or equivariant injection is required.

**Success:** a complete all-parameter proof, or an exactly justified
counterexample with the full original state, phase and least-period checks.
**Failure boundary:** retain `NOT CURRENTLY JUSTIFIED` if the genuine
finite-field fibre identification, exceptional-component action or the
passage from spectral data to all resolved points is missing. A restricted
autonomous lemma or another sampled field is subordinate evidence only.

## Execution gate

No mathematical program is currently planned or executed. Hand algebra and
targeted primary-source reading come first. No author's small-field census
or old accepted program will be rerun.

If a specific unresolved mechanism later justifies the lane's one permitted
new exact diagnostic, its precise finite input list, purpose, outputs,
failure interpretation and resource limits will be written here **before**
implementation or execution. It must fit the parent limit of 60 CPU seconds
and 256 MiB working memory. No silent range enlargement is permitted.

## Authority and provenance

The root/Hénon instructions, current live state, full batch skill/workflow,
[round-eight plan](../PLAN.md), original P7 contract and prior source audit
were read. `research-lit` supplies local-first retrieval, `proof-writer`
governs the derivation and honest status, and ARS is limited to its selected
fact-check/source-verification route. No Socratic reset, full pipeline,
external model, GPU, Git operation, global edit or source-PDF saving is
authorized here. No target Euler factor, root number, automorphy or
zero-matching assertion follows from this source-system question.
