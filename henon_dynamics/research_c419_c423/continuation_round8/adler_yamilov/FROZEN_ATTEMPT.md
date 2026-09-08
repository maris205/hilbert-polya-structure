# AY7 eighth-pass frozen mechanism

2026-09-08 UTC. This is a bounded continuation of the unchanged
[AY7 contract](../../continuation_round7/nonlinear_scout/SCOUT_REPORT.md),
not a new paper proposal. This lane owns only this directory.

## Original full question and retained inputs

For every $k\in\mathbb Z$, classify all ordinary integral periodic
states of
$$
Y_k(p,q,r,s)=(r-kp/(1+ps),s,p,q+ks/(1+ps))
$$
with their exact least one-step periods. All zero strata are retained;
both displayed forward and inverse denominators must remain nonzero at
every iterate, even at $k=0$. No parameter, height or period cutoff
replaces the structural all-parameter atlas.

The corrected classical invariants are
$I=pq+rs$ and $J=pqrs+ps+qr+krs$. The seventh-pass, independently
reviewed bound $\max(|p|,|q|,|r|,|s|)\le\max(|k|+1,4)$ for $k\ne0$
and the $k=0$ pair-swap classification are inputs, not new results.

## Concrete proposed mechanism

At a periodic orbit put $p_n=p$, $s_n=s$, $q_n=s_{n-1}$,
$r_n=p_{n-1}$ and $h_n=k/(1+p_ns_n)$. The exact recurrences are
$$
p_{n+1}=p_{n-1}-h_np_n,\qquad
s_{n+1}=s_{n-1}+h_ns_n.
$$
For $k\ne0$, integrality gives $h_n\in\mathbb Z\setminus\{0\}$.
The candidate is an all-parameter period-rigidity argument obtained by
combining these two adjoint scalar recurrences with $I,J$: either a
coercive cyclic identity forces a universal recurrent core, or a reduced
one-dimensional invariant curve yields a complete cycle-family theorem.
The first cheap step is to derive the cyclic bilinear identities and an
exact reduced map without dividing by a coordinate that can vanish.

The known identities $\sum_n h_np_n^2=\sum_n h_ns_n^2=0$ alone
only force mixed signs on nonzero channels. Mixed-sign denominators
are not a classification. Elliptic reduction, if obtained, must still
resolve its ordinary exceptional fibres and lift multipliers.

## Falsification and stopping boundary

A periodic ordinary integral family contradicting the proposed coercive
identity invalidates that identity, not the original atlas question.
A reduction with uncontrolled torsion, scaling monodromy or singular
fibres does not close the contract. Stop this bounded attempt with the
precise gap if no uniform rigidity or complete family theorem follows;
do not promote another fixed-$k$ finite graph or a parameter table.

Hand proof and targeted primary-source reading are the default. No
mathematical program has been run in this pass. Before using the optional
single new diagnostic, a separate written protocol must fix exact inputs,
purpose, expected output, failure interpretation, and a cap of at most
60 seconds CPU and 256 MiB. No old diagnostic, census expansion, GPU,
paid external model, Git mutation or global admission is authorized here.

## Current status

Original structural atlas: **NOT CURRENTLY JUSTIFIED**. Auxiliary claims
will be explicitly separated from it. All four current team slots are
occupied; no independent subtask is spawned by this lane at this point.
