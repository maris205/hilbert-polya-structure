# Paper plan

Status: `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

## Contract

Carrier: every subgroup of D_{2n}, n at least 3.
Update: ambient subgroup normalizer.
Length target: five to six amsart pages.
State: anonymous and HOLD_EXTERNAL.

## Theorem axes

1. Temporal/fibre axis: t-fold parity halving, full binary forests, depth
   polynomial, every positive-time image, and every target fibre.
2. Inverse axis: iff graph signature (v2(n),sigma(odd part),tau(n)), explicit
   33/35 conjugacy, and common power-of-two lifts.

## Proof dependency

Owned subgroup coordinates and one-step normalizer -> t-fold halving.
Halving -> forest -> depths, images, and fibres.
Forest observables -> recover a and sigma(m).
Total vertex remainder -> recover tau(n).
Recovered signature -> iff classification and arithmetic collisions.

## Mandatory repair and boundaries

Recover tau(n) as total vertices minus sigma(m)(2^(a+1)-1). Do not compare
only with other roots, because m=1 has one root. Distinguish a=0 from a=1 by
the predecessor pattern when n is at least 3. Graph conjugacy is not group or
subgroup-lattice isomorphism. Every rotation feeds only H_(1,0).

No external model review is included, by task instruction. Two independent
internal hostile reviews are complete: Review A's three Minor findings were
closed in Round 1, and Review B returned `ACCEPT_INTERNAL — 0/0/0`. Review B
required no mathematical change. A later final cold-QA found a typesetting
font-expansion warning, closed in Round 2 by disabling microtype expansion
while retaining protrusion. The theorem plan, proof dependencies, evidence,
and claims are unchanged; only the build preamble and resulting PDF bytes
differ from Round 1.
