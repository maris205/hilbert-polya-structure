# Claims and evidence ledger — P152

**Status: ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL.**

The proof column carries the all-parameter theorem. The exact-control column
is finite falsification only. The subtraction column prevents background
ownership from being counted as a contribution.

| Claim interface | Symbolic evidence | Exact counterexample pressure | Zero-credit boundary |
|---|---|---|---|
| Strong count lumping | Theorem 1(i) and Section 2: a private flip clears one selected bit; a spine flip complements all bits | every nonzero imbalance vector through r=9; 2,026 assertions | local triad update, XOR/triadic dual, signed-book carrier, static count classes |
| Joint (T,J) transform | Section 3: marked Bellman equation, reflected-index elimination without dividing by u, Chebyshev recurrence, terminal condition | full transform vectors at four rational points through r=20; 4,416 assertions | generic finite resolvents, Bellman rationality, Chebyshev identities |
| Boundary completion | direct r=1 law, r=2 self-loop and removable (3+zu) cancellation, Bellman value at z=0; coincident-arrow rule | 278 assertions for r=1, r=2, and z=0 | no claim that the unreduced ratio is pointwise valid |
| Quadratic mean and sharp extrema | Section 4: reflected mean elimination gives second difference -1; terminal condition fixes the quadratic; concavity and endpoint comparison give extrema | direct rational mean systems through r=60; shared 3,958-assertion lane | generic tail sums, linear systems, quadratic concavity |
| Spine parity | signed Bellman equation and bounded stopping under the absorption certificate | direct rational parity systems through r=60; shared 3,958-assertion lane | generic parity-transform specialization |
| Exact mean/parity inverse | explicit candidate domain `m>0`, `0<q<1`; integer feasible image, converse construction, uniqueness, central case, and scalar collisions | every state through r=300; criterion versus the literal image on 7,335 bounded exact candidates, of which 7,266 are rejected; 12 gate-specific infeasible pairs including negative/zero scale, and both printed scalar collisions; 7,655 assertions in the iff/collision lane | no noisy stability, one-scalar inverse, full sign-state recovery, or unknown carrier class |
| Absorption certificate | a pre-generated block of r private edge types forces absorption; Markov iteration gives the tail | deterministic clearing for every start through r=300; exact Fraction mass over 8,190 private/spine words and 546 finite tail-bound instances through r=12; 648 assertions in the new probability/tail lane | generic triadic/hypergraph convergence and drift program |

## Mandatory counterexamples retained

- Coincident quotient targets occur when k-1=r-k; masses add.
- For r=2,k=1, the spine arrow is a self-loop and is retained.
- q=1/2 is a valid central inverse case for even r.
- Parity alone collides: (1,1) and (4,2) both give q=1/3; the
  verifier checks equality of q, inequality of the corresponding means, and
  distinctness of the states.
- Mean alone collides: (2,2) and (3,1) both give m=2; the verifier checks
  equality of the means, inequality of q, and distinctness of the states.
- On a friendship/windmill carrier the count law is deterministic; this is not
  the theorem's triangular-book carrier.

## Evidence hierarchy

1. The symbolic proofs in main.tex are dispositive for the mathematics.
2. verify_p152.py is an independent exact falsifier and debugging control.
3. SOURCE_VERIFICATION.md supports subtraction and metadata only.
4. A bounded source non-hit supports no novelty, priority, ownership, or
   external-release conclusion.

Review B's sole Minor is closed by testing `m>0` and `0<q<1` before forming
the inverse square root.  Surviving severity is 0 Critical / 0 Major / 0
Minor.
