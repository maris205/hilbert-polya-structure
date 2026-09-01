# Narrative report

## The large step

The paper does not stop at writing the familiar peakon ODE.  Two conserved
quantities collapse the entire signed two-body problem to a single scalar
quadratic for `y=exp(q_2-q_1)`.  Its two real chambers have different global
meaning: a cosh branch gives complete elastic two-peak scattering, whereas a
sinh branch reaches collision in finite time with a quadratic gap and
reciprocal amplitude blow-up.  The same reduction also makes the energy
removed by an `alpha` continuation algebraic and auditable.

## Epistemic boundary

The post-collision family is part of the model definition: `alpha=0` preserves
the concentrated collision energy, `alpha=1` removes it and leaves the single
peak of momentum `P`, and intermediate values retain the declared fraction.
The package does not infer that this is the only possible weak continuation,
nor does it extend the two-body calculation to arbitrary `H^1` data.

## Route-A outcome

The system has no canonical isolated closed-orbit ledger: same-sign peakons
scatter and signed pairs collide.  The source integrable/Lax context supplies
only `A4_FORMAL_HINT`.  With A0–A3 failed, the strict overall verdict is
`ROUTE_A_REJECTED`; Route B remains false.
