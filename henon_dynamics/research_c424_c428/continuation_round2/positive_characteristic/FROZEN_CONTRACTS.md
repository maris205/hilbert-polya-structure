# Round 2 positive-characteristic contract freeze

2026-09-08 UTC. The user authorized the next bounded round of the same
C424–C428 batch. **One continuation is frozen here; the optional second
question is not yet used.** This is an AI-generated research route, not
an admitted theorem or a manuscript. No new mathematical program has run.

## R2-PC-L — original PC424-L, with a new algebraic detection attempt

The question and all its quantifiers are retained from the
[original contract](../../positive_characteristic/FROZEN_CONTRACTS.md).
For every odd prime $p$, put $k=\overline{\mathbb F}_p$. For every
$c\in k$ and every $h\in k[x]$, consider
$$
f_c(x)=x^2+c,\qquad
T_{c,h}(x,y)=(f_c(x),y+h(x))
$$
on all of $\mathbb A^2(k)$. One application is one native tick. There
is no Frobenius substitution in either update, no degree restriction,
and no restriction to a single finite field or special parameter.

For each ordinary primitive geometric periodic orbit $O$ of $f_c$, use
each distinct orbit point exactly once in
$$
S_h(O)=\sum_{a\in O}h(a).
$$
Define
$$
K_c=\{h:S_h(O)=0\text{ for every such }O\},\qquad
B_c=\{Q\circ f_c-Q:Q\in k[x]\}.
$$
The intended complete theorem is $K_c=B_c$ uniformly in $(p,c)$, or,
if equality fails, a full uniform classification of $K_c/B_c$. A single
low-degree counterexample would refute equality but would not fulfill
the retained defect-classification alternative.

### New route to test

Attempt direct algebraic detection using the polynomials
$$
H_{n,h}(x)=\sum_{i=0}^{n-1}h(f_c^{\circ i}(x)),\qquad
F_{n,c}(x)=f_c^{\circ n}(x)-x.
$$
Orbitwise vanishing gives reduced-root information for every $n$.
The proposed new route asks whether reduced divisibility, iteration
compatibility and leading-degree growth force the polynomial class of
$h$ to vanish. Repeated roots, lengths divisible by $p$ and cancellation
under composition must be treated explicitly. Any use of periods prime
to $p$ is a proof device only, not a restriction of the contract.

A second possible argument within this same route is to study rational
or algebraic solutions of the difference equation and prove their
regularity using poles and finite invariant branch loci. Such a transfer
must actually be constructed; a hypothetical rational transfer cannot
be assumed from set-function solvability.

### Arithmetic carrier and mandatory subtraction

The carrier is native additive monodromy on nonlinear geometric base
cycles. The elementary return translation of order $1$ or $p$, arbitrary
set-function solutions, finite-field interpolation, polynomial
normal-form reduction and Frobenius saturation are already proved
helpers in the [previous proof package](../../positive_characteristic/PROOF_PACKAGE.md).
They are inputs and limitations, not this round's proposed new result.
The earlier source audit's real hyperbolic Livšic theorem is not a
positive-characteristic polynomial-regularity theorem.

The old Frobenius-base trace sums, radicial fibre updates, Drinfeld,
semilinear Hénon, binomial, inverse-tree and wild-dynatomic candidates
remain excluded. The native $p$-power component problem is not reopened
under this contract. A new external theorem will be used only after its
actual parameter, characteristic, regularity and proof scope are checked.

### Cheap decisive test and replacement boundary

First perform symbolic hand arguments on reduced iterate divisibility,
degree separation and pole propagation. No large finite-field census,
polynomial factorization sweep or old mathematical rerun is authorized.
If a new finite diagnostic becomes necessary, freeze its exact finite
domain and its meaningful failure condition before execution.

If the new argument still cannot pass from all orbit constraints to
one polynomial transfer, report that exact remaining implication as
unproved. A proved special case, new rational-transfer lemma or explicit
counterexample is a helper unless it closes the original full question.
Only then may the unused second slot freeze one genuinely different,
source-grounded complete problem; no cosmetic model renaming is allowed.

## Workflow and output boundaries

The main agent read the complete second-round plan, repository and Hénon
guidance, batch skill/workflow, idea-creator, research-lit and proof-writer.
ARS-Codex is used only for its bounded source-verification/fact-check
role, with ordinary browsing and explicit access limits. It does not
author mathematical conclusions or initiate a full pipeline. The current
selected team replaces legacy external-model examples. No paid model,
GPU pilot, bibliographic resolver, human-read attestation or optional
full-runtime profile is enabled.

All new files are confined to this round's positive-characteristic lane.
Prior proofs and snapshots, shared state, Git, TeX and formal evaluators
are not written. Final delivery must separate proof status, source
ownership and substantive increment. Only the coordinator can admit a
contract. `NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional.
