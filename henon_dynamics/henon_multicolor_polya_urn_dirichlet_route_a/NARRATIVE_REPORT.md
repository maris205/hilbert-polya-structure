# Narrative report

The paper takes one complete stochastic owner from chronology to its limiting
random environment.  Multiplying predictive probabilities along a word first
removes chronology: only color multiplicities remain.  This yields the entire
Dirichlet--multinomial finite-time law rather than a sample estimate.  The same
formula simultaneously provides beta--binomial marginals and arbitrary
multi-index factorial moments.

The second half identifies the source of exchangeability.  A Dirichlet vector
mixed against iid categorical draws gives exactly the urn word law.  Bayes'
rule returns the urn predictive probability, so the relation is not a
one-directional analogy.  Conditional laws of large numbers then identify the
almost-sure martingale limit as that same Dirichlet vector.

Boundary discipline matters.  Dividing by `c` is legal only when `c>0`; the
`c=0` system is iid and is proved separately.  Zero initial masses define
lower-dimensional invariant faces, not zero-parameter Dirichlet densities.
The deterministic single-color face is retained.

This complete source theorem does not advance Route A: growing total mass
precludes a nontrivial periodic-orbit owner, and no target arithmetic input is
present.
