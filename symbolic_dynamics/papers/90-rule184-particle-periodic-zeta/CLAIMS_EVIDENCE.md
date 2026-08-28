# Claims and evidence — P90

| Claim | Analytic evidence | Independent deterministic control |
|---|---|---|
| Rule orientation, conservation, and particle–hole/reflection symmetry | local formula (1) and the explicit substitution `F_n Theta = Theta F_n` | all binary rings through `n=14` |
| min-plus formula for labeled particles | Lemma 3.1, by induction from the lifted nearest-particle recurrence | every low-density state through `n=12`, for every `0<=t<=2n` |
| sharp layerwise entry depth | Theorem 3.2; monotone sliding-window upper bound plus the displayed solid-block evolution | every layer through `n=14`, including a sharp witness in every layer |
| particle-weighted iterate-fixed polynomial | Theorem 4.1; rotation-period reduction and explicit alternating two-cycle correction | every `n<=12` and `1<=k<=2n` by direct functional iteration |
| Lucas/gcd fixed count | specialization of Theorem 4.1 | direct fixed-state enumeration and orbit reconstruction |
| exact temporal orbit count and finite-map zeta | Theorem 5.1; divisor Möbius inversion with the parity identity isolated | complete core functional graphs through `n=13` |
| particle-resolved temporal orbit ledger | primitive cyclic hard-core inversion in Theorem 5.1 | exact cycle-length/weight census through `n=13` |
| microcanonical recurrent exponent | Section 6; exact cyclic independent-set count followed by Stirling | finite hard-core counts through `n=16`; asymptotic step is analytic |

The program follows distinct paths: literal cellular iteration, lifted
particle motion, cyclic hard-core enumeration, functional-graph extraction,
and closed Möbius formulas. Finite checks guard conventions and endpoints;
they do not replace the all-size proofs.

The no-`11`/no-`00` recurrent-phase description is explicitly cited prior
input. The residual claims have passed internal proof and control review, but
their external novelty remains **HOLD** pending a broader owner audit.
