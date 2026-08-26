# Paper 21 — Effective exact-order witnesses

## Current status

- Stage: **Phase 3 proof PASS with quantitative framing revision**.
- Working title: *Effective Exact-Order Kummer--Chebotarev Witnesses*.
- Primary owner: the exact finite extensions and Frobenius classes used by
  Paper 15's qualitative exact-order-prime lemma.
- The proof stage is complete.  Manuscript/PDF composition awaits the
  research checkpoint; Route evaluation, submission, and release remain out
  of scope.

## Intended increment

The exact-condition density is `(r-1)/r^(m+1)` and the selected single-class
subfamily has density `r^(-(m+1))`.  The Phase-3 calculation proves

```text
Q(E/Q(zeta_r))=p^(r-1) r^[m(r-1)+1]     for odd r,
Q(E/Q)=p 2^(m+1)                         for r=2.
```

Its Thorner--Zaman specialization is an eventual unconditional improvement
over the exact `|D_E|^310` Kadiri--Wong bound.

## Gate

The honest paper shape is a focused short note: Thorner--Zaman's published
theorem has an unprinted absolute implied constant, so no particular small
triple or named cutoff is certified; under ERH, the Bach--Sorenson
logarithmic-square bound remains better.

See the [batch design lock](../19-standardized-nerve-cohomology/notes/papers19_23_batch_design_lock_v1.md),
[research-question brief](notes/research_question_brief.md), and
[methodology blueprint](notes/methodology_blueprint.md), and
[Phase-2 effective-Chebotarev screen](notes/phase2_effective_chebotarev_screen.md), and
[Phase-3 relative-conductor theorem](notes/phase3_relative_conductor_theorem.md).
