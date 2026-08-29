# P108 — Capped Fibonacci dynamics

Internal Route-A short-paper package for

```text
T_a(x,y) = (y, min(a,x+y))
```

on the finite square `{0,...,a}^2`.

The paper proves an exact capped Fibonacci iterate, two fixed attractors,
pointwise and distributional transient formulas, sharp Fibonacci-threshold
maximum depth, and the full one-step image/fibre geometry.

The P1--P106 collision firewall separates this deterministic integer-square
recurrence from P83's Catalan renewal shift, P89's random reset/golden-mean
matrix product, and P101's random cap--floor interval compositions.  These
are different update rules and phase spaces, not parameter variants.

Within P107--P111, the remaining systems are respectively an
annihilator--power ideal map, a nilpotent image map on subspaces, a cyclic
shift--join map on partitions, and an iid positive Heisenberg product.
Their phase spaces, updates, and headline statistics do not coincide with
P108's capped Fibonacci half-plane clock.

Status: **FINAL MECHANICAL QA PASS / GO INTERNAL / EXTERNAL HOLD**.
`HOSTILE_REVIEW.md` consolidates the two independent reviews, while
`FINAL_QA.md` and `SHA256SUMS` record the deterministic artifact freeze.
Classical Fibonacci identities and saturation background receive zero
novelty credit.  No external posting, submission, contact, novelty, or
priority action is authorized.
