# Source audit — C123

- Frozen source: two affine maps with exact uniform iid law; no sampled path,
  fitted probability, prime table, or zero table.
- Clock: one random-map step.  Word order is chronological and canonical phase
  is the lexicographically least rotation with `- < +`.
- Probability semantics: a canonical row's `2^-n` is the probability of that
  chosen rooted length-`n` iid block, not necklace total mass and not an
  infinite periodic-orbit probability.
- Cutoffs: every rooted word through length six; every monomial of total degree
  at most four.
- Number system: `Q(sqrt(2))` only because singular values are audited; all
  orbit states and moments are rational.
- Controls: remove the additive noise and compare the zero stationary
  covariance; retain the fourth cumulant to prevent an unjustified Gaussian
  closure.
- Independent checker and SymPy reconstruction do not import the producer;
  canonical replay and hostile mutations are deterministic.
- Literature novelty is unverified.  No external citation, reviewer score, or
  acceptance claim is made.
- Prime-like target correspondence, target-divisor matching, an analytic
  bridge, global nuclearity/Fredholm ownership, arithmetic/local data, Euler
  factors, root numbers, automorphy, Hilbert–Pólya, and Route B are explicit
  nonclaims.
