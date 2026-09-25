# Faithful deletion-only sieve dynamics cannot carry a nontrivial periodic update

**Paper ID:** `063-monotone-elimination-periodic-rigidity`  
**Record ID:** `ASFS-METHOD-20260914-09`  
**Date / status:** `2026-09-14; METHOD THEOREM / PRE-P0 STOP RULE`  
**Route state:** `No P0 or Route-A evaluation; Route B NOT INVOKED`.

## Theorem

Let `F:X->X` be a self-map and let `E:X->P(U)` record the objects eliminated by a sieve state. Assume that the reachable states obey

```text
E(x) subseteq E(Fx).
```

If `x` is periodic, say `F^q(x)=x` for `q>0`, then

```text
E(x) subseteq E(Fx) subseteq ... subseteq E(F^q x)=E(x),
```

so every inclusion is equality. Hence no step on a periodic orbit performs a new effective elimination.

If an encoding is additionally **state-faithful**—meaning that an intended sieve update is required to enlarge `E`—then a periodic orbit cannot execute that intended update. It may still be a fixed/static residue, but it is not a cyclic realization of the sieve evolution.

## Relation to the current lineage

The Eratosthenes source is intrinsically deletion-driven: newly discovered sieving factors mark additional composites. The primorial-wheel state records this through a strictly advancing stage (018--020); the causal and real-time local implementations instead retain a forward computation whose prime-bearing trajectory cannot recur (050--054). The theorem provides the common reason at the weaker level of a monotone eliminated-set observable, without requiring an integer stage coordinate, causality, a particular alphabet, or a finite cutoff.

This is useful as a breadth gate, not as a global no-go theorem. A possible future candidate may evade it only by defining a different exact arithmetic mechanism: for example a genuinely reversible law with an auditable rule for restored/reinterpreted data, or a spatial return mechanism not represented as successive deletion. Merely adding a history register, declaring formal inverses, or selecting a static wheel cycle does not make the original deletion update periodic; it changes or discards the owner that made the source endogenous.

## Gate consequence

| Gate | Evidence / decision | Status |
| --- | --- | --- |
| Source lineage | exact sieve crossing-out mechanism remains recognized | retained control |
| A0 | theorem does not create a new arithmetic mechanism | NOT EVALUATED |
| A1 | deletion-only update cannot be a nontrivial periodic orbit | scoped stop rule |
| A2 | no same-object orbit ledger or analytic owner | NOT EVALUATED |
| Route B | no Route-A-ready candidate | NOT INVOKED |

**Portfolio position: `fork`.** Future scouts should first state whether their prime-symbolic action has a monotone eliminated-set observable. If yes, test only its fixed residues and stop before an A1 investment. If no, document precisely what replaces monotone deletion and why it preserves the prior-work sieve lineage without being an external program or label.

## Evidence index

- [018 monotone sieve-clock obstruction](../018-monotone-sieve-clock-obstruction/paper.md)
- [020 wheel-event dichotomy](../020-wheel-event-dichotomy/paper.md)
- [050 causal binary-sieve control](../050-causal-binary-sieve-fixed-point-screen/paper.md)
- [053 real-time sieve CA](../053-realtime-sieve-ca-nonrecurrence/paper.md)
- [019 primorial gap recursion](../019-primorial-gap-recursion-control/paper.md)
