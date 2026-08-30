# Narrative report

## One-sentence story

A parity-triggered local-looking graph update is exactly linearized by recursively splitting odd components through graph complementation, and this pointwise clock lifts to an all-depth labelled EGF and a closed recurrent zeta census.

## Why the paper has two complementary proof routes

The temporal route follows one graph. Component partitions can only refine; an odd connected block either enters a complement two-cycle or splits into smaller blocks, and only its odd children can continue. This yields the pointwise depth recursion and the sharp order bound.

The enumerative route works by labelled classes. Co-connected odd connected blocks form the recurrent base class. A depth-`t` odd connected block is either already co-connected or is the complement of a nontrivial SET of even connected blocks and depth-`t-1` odd blocks. Odd extraction translates the already-proved pointwise depth recursion into an exact recursive EGF. It produces different outputs from the temporal argument, but does not claim logical independence from it.

## Contribution subtraction

Gallai's component/co-component decomposition, cograph/cotree theory, modern labelled cotree enumeration, the exponential formula, and classical connected labelled graph counts are interfaces, not results of P123. The residual value lies in the literal parity-triggered dynamics, its exact entrance clock, the sharp all-order transient bound, and the full temporal census including zeta data.

## Release posture

The primary-source audit was bounded and found no direct owner for this literal theorem package. Owner risk remains nonzero. The manuscript is suitable for internal mathematical review only; novelty, priority, and external release remain HOLD.
