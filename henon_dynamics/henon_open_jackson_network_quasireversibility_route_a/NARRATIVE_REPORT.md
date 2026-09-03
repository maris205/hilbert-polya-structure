# Narrative report

## Result

The network theorem is complete in the frozen finite-node, single-class,
exponential-service model. The row traffic equation produces a unique positive
vector because \((I-P)^{-1}=\sum_{m\ge0}P^m\). Strict loads normalize a product
of geometric laws, and a state-by-state global-balance calculation proves
invariance. Conversely, any invariant probability forces its service
throughput vector to solve the same traffic equations. Critical load would
force one queue to be nonempty with probability one, contradicting the full
support supplied by the standard countable-state CTMC lemma: for an
irreducible conservative chain, an invariant probability implies positive
recurrence, uniqueness, and positive mass at every state.

Stationary reversal has the exact rates

\[
\widehat\alpha_i=\lambda_i p_{i0},\qquad
\widehat p_{ji}=\frac{\lambda_i p_{ij}}{\lambda_j},\qquad
\widehat p_{i0}=\frac{\alpha_i}{\lambda_i}.
\]

The index order is substantive: a forward \(i\to j\) route becomes a reverse
\(j\to i\) route. The reversed external inputs are independent Poisson
processes in the natural extension of the model that allows some reverse
external rates \(\widehat\alpha_i=\lambda_i p_{i0}\) to vanish. The jump-rate
calculation identifies the visible marked-jump law. Phantom self-routing marks
are state preserving and may be restored at the same conditional rates; they
do not enter the external-output claim. Under the time change
\(s\mapsto -s\), reversed inputs are precisely the forward external
departures, so the entire departure history before time \(t\) is independent
of the queue vector at \(t\). The package does not promote this to joint
independence of every internal arc flow.

## Evidence

The exact ledger contains 12 network rows, 1,020 global-balance rows, 12 reverse
network rows, 84 reverse-jump rows, and 6 boundary rows. Every number is a
rational string. Producer and checker use different traffic solvers; replay,
symbolic identities, strict parsing, repaired-hash attacks, and release closure
are separate lanes.

## Collision and route boundary

C285 owns closed fixed-population Gordon--Newell networks, C233 owns the
infinite-server immigration--death spectrum, and C342 owns directed reinforced
walks in Dirichlet environments. None owns open single-server routing with
external departure histories. Nonetheless, the queueing process has no
intrinsic prime carrier or deterministic primitive-orbit determinant. Every
Route-A layer fails, Route B remains false, and the scope literal is
NO_BAD_EULER_OR_ROOT_NUMBER.
