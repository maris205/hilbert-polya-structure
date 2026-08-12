# Adversarial Controls and Gate Decision

Status: **PROVED CONTROLS — NO NUMERICAL RUN REQUIRED**

## Claim-deletion controls

| Control | Frozen modification | Expected result | Interpretation |
|---|---|---|---|
| Clock erasure | Remove $d\circ\pi=\kappa$ | A one-point factor has a fixed point | Periodicity alone carries no arithmetic fidelity |
| Periodic grading | Factor level modulo $m$ | An $m$-cycle appears | One target state would need multiple prime values |
| Partial decoder | Define $d$ only on $\pi(X)$ | Boundary cycles may exist | Their clock is undefined, so no inherited A0/A1 ledger exists |
| Discontinuous extension | Extend $d$ arbitrarily to a boundary fixed point | Exactness on the image coexists with a boundary cycle | The boundary label is post-hoc rather than continuous inheritance |
| Clock compactification | Add $\infty$ to the clock codomain | A continuous decoder and boundary fixed point coexist | Lagged clock-pair closure meets the diagonal at $(\infty,\infty)$ |
| Periodic control clock | Replace $\kappa_k$ by $c_k$ with $c_{k+m}=c_k$ | The level-mod-$m$ factor has an exact decoder | Nonrecurrence of the clock is a sharp hypothesis |
| Broken semiconjugacy | Drop $\pi\sigma=S\pi$ | Levels can be mapped to an arbitrary cycle | The construction is not a dynamical factor/recoding |
| Stored sequence | Put $(q_k)$ in the target state | Exact recovery becomes tautological | A0 fails by hard-coding |
| Reset/wrap edge | Add a return to an earlier level | Cycles appear | The grammar has changed specifically to manufacture cycles |
| Independent orbit rule | Label new target cycles by a new formula | Potentially testable only as a new candidate | `SD-C05` arithmetic credit does not transfer |

## Route-A reading

This project proves an obstruction class; it does not freeze a new candidate.
Accordingly no Route-A candidate YAML is created.

- A0: the source wheel recursion has a proved arithmetic origin, but a new
  factor/recoding may not inherit that verdict automatically.
- A1: any exact-clock factor has no periodic points; a continuous exact-clock
  orbit-closure recoding also has no periodic points when its lagged clock
  pairs remain separated from the diagonal.
- A2: `NOT_TESTABLE`; no determinant is defined.
- A3: `NOT_TESTABLE` for the new theorem class.
- A4: `NOT_TESTABLE`; Route B is locked.

Outcome for the frozen mechanism:

```text
THEOREM_STOP
```

Claim boundary:

```text
exact pointwise clock
+ shift-compatible semiconjugacy
+ surjective factor
or continuous total decoder on the orbit closure with lag-pair separation
=> no inherited periodic points
```

## Proves-too-much audit

The argument applies to every graded symbolic source with an injectively
drifting discrete clock, not specifically to primes.  This is the intended
scope of the structural lemma.  It does **not** certify an RH-like statement,
a determinant, or a spectral conclusion for the wheel system or for a
control.  Therefore its generality is not a `PROVES_TOO_MUCH` failure.

The arithmetic conclusion is deliberately narrower: the wheel application
uses the independently proved fact that its endogenous clock is the sequence
of rational primes.  No claim about other clocks is promoted to arithmetic
evidence.

## Route-B decision

```text
route_b_invocation_allowed: false
hilbert_polya_claim_allowed: false
```

There is no periodic-orbit ledger, determinant, Hilbert space, operator, or
domain to audit.  Route B cannot be used to rescue this theorem-stopped
mechanism.
