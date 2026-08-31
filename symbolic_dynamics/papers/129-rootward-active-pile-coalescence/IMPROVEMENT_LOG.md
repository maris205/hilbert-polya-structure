# Paper improvement log — P129

## Round 0

- Anonymous five-page `amsart` manuscript compiled in an isolated four-stage
  build.
- Main theorem covers every rooted initial state and explicitly proves that
  the continuous-time clock construction has the literal uniform-active
  embedded jump chain.
- Full-start mean, asymptotic, PGF, support, and minimum mass are separated
  into proved claims.
- The maximum-time endpoint mass is retained only in the verifier under a
  `PILOT_ONLY / MANUSCRIPT_CLAIM=NO` label.
- Generic external coalescing machinery and P114/P117/P121/P126 internal
  silhouettes receive zero credit.

At the round-zero freeze, the pending stages were independent Review A,
round-one repairs, independent Review B, and round-two mechanical closure.

## Round 1 — implementation of Hostile Review A

Date: 2026-08-31 UTC.  Round zero remains immutable.  The Review-A findings
were repaired without enlarging the theorem ceiling or changing
`HOLD_EXTERNAL`.

| review item | round-one repair |
|---|---|
| MATH-1 | Replaced the unsupported “Pascal's identity gives” sentence by a complete stopped fair-walk proof: central-binomial meeting telescoping, ballot-probability telescoping, bounded optional stopping for the gap, separate root contribution, and the `m=1` boundary. |
| OWNER-1 | Added Assiotis (2018), Hitczenko--Wesołowski (2025), and Śniady--Urbán (2026) as primary direct neighbors and assigned their coalescing-flow, active-count/jump, interval-label, and coalescence-pattern mechanisms zero credit. The residual wording is narrowed to the specified deterministic-rootward uniform-active chain. |
| MINOR-1 | Restricted clocks to the finite accessible sites and invoked strong Markov for the finite Poisson vector at every effective stopping time, including newly occupied sites. |
| MINOR-2 | Added the induction that current piles carry ordered consecutive blocks of initial labels and that collisions merge adjacent blocks, including indirect/outside mergers. |
| MINOR-3 | Replaced the informal intensity by predictable `N_(t-)`, established the finite-time compensator identity, then used monotone convergence and the Lebesgue-null jump-time observation. |
| MINOR-4 | Standardized all executed ranges to means through `n=14`, complete laws through `n=11`, and pair/ballot checks through 80. |
| internal firewall | Corrected P117 to its labelled cyclic-word odd-run/boundary-parity eroder and distinguished P121's separator-selected product-plus-one/BST--Yule process from pile-selected, possibly noncoalescing P129 updates. |

The verifier and canonical transcript require no code change.  Fresh
byte-match, isolated build, visual/font/metadata audit, and round-one PDF
freeze are recorded in `CONTROL_RESULTS.md` and `BUILD.md`.

## Review B and round-two sign-off

Independent Review B reconstructed the complete stopped-walk calculation,
including the moving boundaries, root probability, bounded optional stopping,
and `m=1`, and ran 10,972 separate exact assertions.  It also rechecked all
owner subtractions, clock/label/compensator repairs, support and
`PILOT_ONLY` boundaries, canonical verifier, isolated build, bibliography,
fonts, metadata, and all six pages.  The result was critical 0, major 0,
blocking minor 0 and `GO_INTERNAL / HOLD_EXTERNAL`.

No theorem, source, code, or PDF repair was requested.  `main_round2.pdf` is
therefore byte-identical to `main_round1.pdf` and `main.pdf`, SHA-256
`5c64a88c1d003fd2729dd032eb229f9073975753040082919d0fc056d1c439f2`.
Paper-local final QA is complete: fresh canonical output matched byte for
byte, an isolated four-stage build reproduced the reviewed PDF, and the
round-two package is frozen by `SHA256SUMS`.  The terminal status is
`GO_INTERNAL / HOLD_EXTERNAL`.
