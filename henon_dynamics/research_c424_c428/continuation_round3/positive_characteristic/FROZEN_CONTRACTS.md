# Round 3: original PC424-L, global regularity continuation

2026-09-08 UTC. One continuation is opened; the optional different second
question remains unused. This is a frozen research question, not an
admitted theorem. All writes are confined to this new lane.

## Unchanged complete object

For every odd prime $p$, every $c\in k=\overline{\mathbb F}_p$ and every
$h\in k[x]$, let

$$
f_c(x)=x^2+c,\qquad T_{c,h}(x,y)=(f_c(x),y+h(x))
$$

on all of $\mathbb A^2(k)$, with one ordinary application as one tick.
For every primitive geometric periodic orbit $O$ of $f_c$, count each
distinct point once in $S_h(O)=\sum_{x\in O}h(x)$. Define

$$
K_c=\{h:S_h(O)=0\text{ for every such }O\},\qquad
B_c=\{Q\circ f_c-Q:Q\in k[x]\}.
$$

The original question is $K_c=B_c$ for all the displayed parameters, or
a full uniform classification of $K_c/B_c$ if equality fails. No finite
field, degree cutoff, special $c$, prime-to-$p$ orbit restriction or
Frobenius replacement of the base is substituted for this object.

The native arithmetic carrier is additive fibre monodromy over nonlinear
base cycles. It is not a target Euler factor, root number or zero spectrum.

## Deducted inputs

The [R2 proof](../../continuation_round2/positive_characteristic/PROOF_PACKAGE.md)
and [coordinator follow-up](../../continuation_round2/COORDINATOR_PC_L_FOLLOWUP.md)
were read completely. Their binary-support detection, orbitwise
nilradical equivalence, Frobenius necessity

$$
M_n>\frac{2^{\lceil n/2\rceil}}{pD}
$$

for a hypothetical normal-form defect of degree $D$, and rational-transfer
pole lemma remain known inputs. Earlier polynomial normal forms,
set-function transfers and interpolation are likewise not new results.
The previous source audits retain all earlier exclusions; generic local
ramification statements have not supplied the needed global upper bound.

## New route and decisive boundary

First investigate a global subsequence bound
$\liminf M_n/2^{n/2}=0$, where $M_n$ is the largest root multiplicity of
$f_c^{\circ n}(x)-x$. The new avenues are choosing iterate lengths that
avoid multiplier orders or wild iteration, controlling repeated cycles
globally using the finite postcritical orbit, or replacing the multiplicity
argument by a full algebraic regularity construction. The finiteness of
the coefficient field is a potential proof input, not a license to replace
the full geometric domain by finitely many points.

A local germ bound must have the correct direction and quantify over all
relevant cycles; generic/minimal ramification and characteristic-zero
petal arguments cannot be imported silently. If a proposed bound still
requires a missing uniform/global step, that step stays explicit. New
local lemmas, special cases or conditional statements do not close the
original question by themselves.

The initial decisive work is hand proof and primary-source scope checking.
No mathematical program is authorized by this freeze: any actual finite
diagnostic requires its own exact input domain, failure condition and
execution record before running. No old program, broad census, TeX,
evaluation, Git operation or accepted artifact is modified or rerun.

Only if this original route genuinely stalls may at most one different,
source-grounded complete question be frozen after explicit subtraction
of the relevant characteristic-$p$ library. No old helper is renamed.

## Process boundary

The complete current plan, repository/Hénon guidance, batch skill/workflow,
idea-creator, research-lit and proof-writer were read. ARS-Codex is confined
to source fact-checking; its router, selected workflow, source-verification
role and required references were read in full. Candidate/proof authorship
remains native research reasoning. No external model, GPU pilot, full ARS
pipeline, programmatic resolver, human-read mark or optional runtime is
enabled. All source claims must distinguish actual body access from leads.
Only the coordinator may admit a contract. `NO_BAD_EULER_OR_ROOT_NUMBER`
remains unconditional.
