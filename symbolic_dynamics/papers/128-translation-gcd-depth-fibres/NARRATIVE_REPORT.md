# Narrative report

## The short-paper story

The dynamics is deliberately not sold as a new system.  For a monic
polynomial over `F_q`, repeatedly replace `f` by `gcd(f(x),f(x+1))`.  The
elementary orbit fold, the order-`p` clock, and the invariant ring were
already known inside the project, and translation-fixed irreducibles are
directly owned by Garefalakis and Reis.  The paper asks a narrower question:
after all of that is subtracted, can one count every transient layer and
every terminal fibre exactly?

The answer has one common spine.  Translation permutes each nonfixed
irreducible family in a `p`-cycle.  The terminal core takes the minimum of
the `p` exponents.  Once that minimum is removed, the remaining vector has
at least one zero.  Its time to disappear is precisely its longest cyclic
run of positive entries.  Positive heights contribute `u=y/(1-y)`, so a
`(t+1)`-state run automaton counts the local residuals that die by time `t`.
The formal orbit Euler product over all nonfixed irreducible orbits then counts every
degree and every depth threshold.

The same minimum subtraction gives the second output.  Each polynomial
splits uniquely as an invariant terminal core times a residual in
`Q^(-1)(1)`.  This is a graded set bijection, not a quotient by a monoid
homomorphism.  Dividing the all-monic generating function by the
invariant-core generating function gives `(1-qz^p)/(1-qz)`.  Multiplication
by any chosen invariant target transports that unit fibre to the target
fibre, giving both exact-degree and capped counts.

## Why the conjunction is worth recording internally

Neither standard transfer matrices nor the terminal split is independently
the point.  The useful result is the closed all-parameter package: one local
run series gives every temporal layer, while one two-term rational series
gives every target-refined terminal fibre.  The extension-field controls
exercise characteristic two, odd characteristic, genuine extensions,
intermediate depth, fixed irreducibles, repeated factors, and every target
in the enumerated boxes.

## What the paper does not say

- It does not claim the literal map, window identity, finite clock, fixed
  ring, fixed counts, or old depth data as new.
- It does not claim the Garefalakis/Reis fixed-irreducible formula.
- It does not claim a generic semilattice-fold mechanism; P110 already owns
  the order-dual join version internally.
- It does not call `Q^(-1)(1)` a kernel or claim `Q` is multiplicative.
- It does not use finite computation as proof or bounded search as novelty.
- It does not authorize external release.

## Status

Internal manuscript workflow only.  `HOLD_EXTERNAL` remains in force through
all review and build rounds.
