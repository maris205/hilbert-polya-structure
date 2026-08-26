# Formal proof package

## Theorem P71-A: degree pressure

**Statement.** `P_tau(t)=log sum_z k_z^(t+1)` with unique Bernoulli equilibrium `p_t(s) proportional to k_(tau(s))^t`; derivatives are the `r_t` mean and variance of `log k_z`.

**Engine.** Identify the natural extension with `S^Z`; construct the invariant-measure lift on finite inverse-limit cylinders and preserve entropy by generating partitions. Lift the potential to one coordinate, bound entropy rate by one-symbol entropy, and apply finite-alphabet Gibbs inequality. Equality forces both the marginal and Bernoulli independence.

## Theorem P71-B: profile rigidity

**Statement.** Topological conjugacy, equal fibre-size multisets, and equal degree-pressure curves are equivalent.

**Engine.** Conjugacy preserves local degree and fixed points, so degree-`k` fixed points count `k m_k`. Equal profiles give bijections `beta` on quotient symbols and `alpha` on future symbols with `kappa alpha=beta tau`. Equal pressure curves give finite exponential sums `sum m_k k^u`; recover the largest base and coefficient asymptotically, subtract, and recurse.

## Theorem P71-C: multifractal spectrum

**Statement.** Level sets are empty outside `[log k_min,log k_max]`; inside, their Bowen entropy is the constrained `S`-symbol entropy, equivalently `max_r(H(r)+alpha)` and `inf_t(P(t)-t alpha)`.

**Engine.** Remove one bounded boundary term. For the explicit product metric, prove that an `(n,2^(-M))` Bowen ball fixes exactly the initial `M` past symbols and `n+M` future symbols. Apply type cylinders at arbitrarily large lengths for the Carathéodory upper bound; apply Bernoulli local cylinder probabilities and the entropy distribution principle for the lower bound. Maximize conditional entropy uniformly within fibres, then use Gibbs equality for convex duality.

## Proposition P71-D: periodic identity

Fixed points of `F^n` are in bijection with `S^n` through the explicit aligned formula `x_i=s_(i mod n)` for `i>=0` and `x_(-j)=tau(s_((-j) mod n))` for `j>=1`; the orbit degree product factorizes, giving `Q(t)^n`.
Exponentiating the standard weighted periodic series gives
`zeta_tau(t,u)=(1-u Q(t))^(-1)`, whose first positive pole is `exp(-P(t))`.

## Owner-derived corollary

Martins--Mattos--Varão Theorems A--B give metric and folding entropy for Bernoulli extended shifts. For `p_t`, conditional laws inside each fibre are uniform, so their formulae reduce to `h=P-tP'` and folding entropy `P'`.
