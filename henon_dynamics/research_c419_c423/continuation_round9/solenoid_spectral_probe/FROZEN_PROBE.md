# AS1 round-nine independent spectral probe

2026-09-08 UTC. Bounded helper lane; no admission or new paper contract.

## Original object and exact target

Keep the complete original [AS1 contract](../../arithmetic_spectral/FROZEN_CONTRACTS.md).
The accepted [round-seven proof](../../continuation_round7/spectral_scout/AS1_PROOF_PACKAGE.md)
and its [independent review](../../continuation_round7/spectral_review/INDEPENDENT_REVIEW.md)
are imported without rerunning their all-depth peripheral theorem.
Write $L_{\chi,k}=\varphi^{-1}V_k^{-1}T_{\chi,k}V_k$, where
$V_k=\operatorname{diag}(v)$, $v=\varphi$ on even states and $v=1$
on odd states. Thus $L_{1,k}$ is a Markov matrix and
$\|L_{\chi,k}\|_{\infty}\le1$.

The bounded target is to decide whether nonperipheral eigenvalues of
$L_{\chi,k}$ can approach nonreal points of $S^1$ as $k\to\infty$, or
to prove a uniform spectral/resolvent exclusion on compact nonreal arcs.
This is only a helper to the full exponentiated-zeta continuation problem.

## One frozen mechanism

Test **quantitative short-cycle phase frustration**. A near-peripheral
eigenvector of a twisted Markov matrix should nearly align the two allowed
edge phases. Propagate this alignment to the fixed $b$ and $ab$ cycles,
using projective memory $m_k=\lceil k/3\rceil$. Derive an explicit
inequality relating $1-|\lambda|$ to
$|\chi(\lambda_b^2/\lambda_{ab})-1|$ and the transport cost to those
cycles. The known quotient generates the finite image of $1+8\mathbb Z_2$.

Success requires a lower bound uniform in $k$ on any prescribed compact
arc disjoint from $\{1,-1\}$, or an independently justified construction
of true eigenvalues converging to such an arc. A bound deteriorating with
$m_k$ or character order is a helper only. Matching finitely many periodic
traces is not operator-norm approximation, an approximate eigenvector, or
evidence for a true eigenvalue.

## Decisive failure boundary and resources

If fixed-cycle holonomies can become arbitrarily close to the target
length phases while the transport estimate degenerates with $k$, this
mechanism does not establish uniform exclusion. Record the precise missing
estimate rather than conclude that actual eigenvalues accumulate.

Hand derivation is the default. **No mathematical program is authorized
for this initial probe.** Any proposed execution requires a separately
recorded exact input protocol and coordinator review, at most 60 seconds
CPU and 256 MiB memory. No old census, finite-depth peripheral proof,
GPU, external model, PDF download, Git write, or global-state edit.

## Skill and source scope

The repository batch skill preserves the complete-contract admission gate;
`proof-writer` governs explicit hypotheses and missing steps. Sources will
be checked only if the derivation uses an external nontrivial theorem.
No source theorem is currently imported beyond the accepted local input.
Actual fresh web query count at freezing: **0**. Mathematical executions:
**0**. All writes belong to this directory only.
