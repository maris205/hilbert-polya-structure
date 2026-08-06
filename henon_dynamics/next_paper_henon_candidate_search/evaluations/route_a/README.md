# Route-A evaluation status

No schema-complete Route-A YAML was created for generation
`HCS-2026-08-05`.  This is intentional: the frozen search protocol permits a
formal evaluation only after BF3, and no pilot reached BF3.

At the evaluator's input-validation stage, C02/C02B is formally
`NOT_TESTABLE`: no clock, normalization, determinant convention, or transfer
operator is frozen.  C02C now freezes unit discrete time and a signed *finite*
flat-trace denominator, but it still has no function space, infinite operator
or normalization.  It is therefore also formally `NOT_TESTABLE`.  The table
below is an **informal layer ceiling** used for research triage, not a valid
substitute for a Route-A record.

The conservative screening ceilings are:

| Candidate | A1 | A2 | A3 | A4 | Overall |
|---|---|---|---|---|---|
| C02/C02B | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_EXPLORATORY` |
| C02C effective finite-window pinning | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_EXPLORATORY` |
| C03 | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_FAIL` | `ROUTE_A_REJECTED` |
| C05 intrinsic fixed-\(z\) phase | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |

C02/C02B's A1 is weak because exact orbit/projective infrastructure exists,
but no intrinsic prime-like weight or frozen determinant has been supplied.
C03 has exact local finite factors but no justified global object.  C05 has an
exact phase ledger, yet gauge dependence and a one-symbol Maslov collapse
reject the proposed intrinsic absolute phase.

The C02/C02B/C02C `A4_FORMAL_HINT` comes only from the inherited exact
symplectic Hénon structure and known quantization context.  The C02C matching
identity supplies a natural signed local denominator, but no clock-preserving
Hilbert-space lift.  It therefore does not improve A2, A3 or A4.

C02C's exact endpoints, chronological gluing and matching/Hill identity do
strengthen the analytic infrastructure behind A1, but they introduce no
intrinsic prime-like weights or arithmetic local-to-global law.  The A1
ceiling remains `A1_WEAK`.  Moreover, Sterling--Dullin--Meiss already covers
the conjugate real SFT/uniqueness, while BPS covers the qualitative
pinning/absolute-residue mechanism.  Its current decision is
`RETAIN_EFFECTIVE_SPECIALIZATION; MANUSCRIPT_HOLD;
NOVELTY_DELTA_UNCONFIRMED`, not Route-A promotion.

`route_b_invocation_allowed` is false for all candidates.  Full C02C evidence
is in `../../results/c02c_finite_window/` and the first-round comparison is in
`../../refine-logs/EXPERIMENT_RESULTS.md`.

If a later candidate reaches BF3, save append-only evaluations under

```text
<candidate_id>/<timestamp>.yaml
```

using the exact schema and evidence labels from
`../../../skills/route-a-evaluator.md`.  Never backfill a formal YAML for this
round or overwrite an earlier verdict.
