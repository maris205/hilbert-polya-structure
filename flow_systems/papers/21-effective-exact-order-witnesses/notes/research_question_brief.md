# Paper 21 research-question brief

Date: **2026-08-24**
Status: **PHASE-2 REVISED — RELATIVE-CONDUCTOR PROOF GATE**

## Primary question

For fixed primes `p` and `r` with `r != p` and fixed `m>=1`, quantify the
rational primes `ell` satisfying

```text
v_r(ell-1)=m,
v_r(ord_ell(p))=m.
```

The exact Kummer--cyclotomic Frobenius construction in Paper 15 already yields
a selected Chebotarev subfamily of density `r^(-(m+1))`.  Phase-2 source and
group auditing upgrades the union of all exact-order classes to density
`(r-1)/r^(m+1)` and verifies generic effective bounds.  Can an exact
calculation of the relative Artin conductors for `E/Q(zeta_r)` give a
genuinely stronger least-witness theorem?  Unconditional and GRH-conditional
results must be stated separately.

## Subquestions

1. Freeze the precise finite Galois extension and target conjugacy class for
   odd `r` and for `r=2`.
2. Retain the verified degree `r^(m+1)(r-1)`: for odd `r`, each of the
   `r-1` admissible cyclotomic components contributes a conjugacy class of
   size `r-1`, giving total density `(r-1)/r^(m+1)`; for `r=2` there is one
   class of size one and density `2^(-(m+1))`.  Compute the local relative
   Artin conductors at `p` and `r` rather than stopping at a
   full-discriminant bound.
3. Apply the strongest matching effective Chebotarev theorem and translate
   its conclusion back to both exact valuations.
4. Separate an asymptotic/density theorem from the least-prime corollary.
5. Test small parameters to expose missing exceptional cases and compare the
   proved bound with observed first witnesses.

## FINER screen

| Criterion | Score / 5 | Reason |
|---|---:|---|
| Feasible | 4 | Paper 15 already freezes the extension and qualitative class |
| Interesting | 4 | turns an existential classification input into quantitative arithmetic |
| Novel | 4 | novelty depends on the exact simultaneous valuation package and explicit parameter dependence |
| Ethical | 5 | pure mathematics; conditional hypotheses and numerical evidence can be cleanly separated |
| Relevant | 4 | directly answers Paper 15's least-witness limitation |

Mean score: **4.2/5**.

## Owner and nonclaims

- The owner is the off-local exact-order lemma; the diagonal `r=p` branch is
  outside this project unless separately frozen.
- The project does not prove or assume injectivity of `kappa` and does not
  compare arbitrary prime pairs.
- It makes no packet, flow, trace, operator, determinant, complexity-optimal,
  or Route claim.
- A GRH-dependent bound may not be described as unconditional.

## Decisions

- **Promote:** a relative-conductor specialization that gives a nonvacuous
  improvement beyond the verified generic bounds.
- **Merge/short note:** retain the exact density and generic unconditional/
  GRH bounds if no conductor improvement survives.
- **Stop/revise:** parameter dependence, exceptional primes, or the return from
  Frobenius data to exact valuations cannot be closed.
