# Author repair response to the first CEF hostile gate

**Date:** 2026-09-03 UTC  
**External:** `HOLD_EXTERNAL`

The first gate returned `AMBER_LOW`, with one Major and two minor findings.
The author files now respond as follows.

| finding | response |
|---|---|
| M1: generic affine Fourier fibres do not evaluate target dependence | Added the complete time-two spectrum (15), classified by integrated-mask radius with exact binomial target multiplicities, and the complete midpoint spectrum (16), classified by half-word weight with exact target multiplicities. |
| m1: repeated-root cyclic-code owner omitted | Added Zhao--Li--Yang--Fu--Shum and assigned zero credit to homogeneous kernel/weight-distribution machinery. |
| m2: CA name and inverse notation | Corrected the binary tail to Rule 102/153; all new statements use preimage notation `(T_q^t)^(-1)`. |

The V2 verifier attacks both spectrum values and every class multiplicity in
all six author boxes.  This response is not self-certification: CEF remains
`GREEN_REENTRY_PENDING_INDEPENDENT_HOSTILE_GATE` until a fresh hostile gate
reviews the repaired snapshot.

