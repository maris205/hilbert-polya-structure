# P97 — Sumset-squaring dynamics

Status: **internal Stage 2 mechanical PASS / external HOLD**.

For an odd prime `p`, this note studies the finite self-map

```text
Phi_p(A) = A + A
```

on the nonempty subsets of `F_p`.  This is a nonlinear Minkowski-sum
operation, not a pointwise finite-subset lift of another map.

The frozen theorem package is:

1. `Phi_p^t(A)` is the `2^t`-fold sumset of `A`;
2. the recurrent states are `F_p`, `{0}`, and the nonzero singletons;
3. if `h=ord_p(2)`, then the nonzero singletons form `(p-1)/h` cycles of
   length `h`, giving
   `Fix(Phi_p^n)=2+(p-1) 1_(h|n)` and
   `zeta=(1-z)^(-2)(1-z^h)^(-(p-1)/h)`;
4. Möbius inversion gives the complete least-temporal-period census;
5. the exact worst absorption depth on the `m`-element layer is
   `ceil(log_2((p-1)/(m-1)))`, attained by arithmetic progressions; and
6. the first fixed-count anomaly recovers both `p` and `ord_p(2)`.

Cauchy–Davenport growth, Vosper critical-pair rigidity, general iterated
sumset structure, and the Artin–Mazur construction are positively cited and
excluded from the residual claim.  The paper makes no absolute novelty or
priority claim.

Run the deterministic exact control with:

```bash
python3 code/verify_sumset_squaring.py
```

Build the manuscript with the explicit four-stage command in
[BUILD.md](BUILD.md).  Public release, submission, venue choice, author
contact, and specialist priority claims remain **HOLD**.
