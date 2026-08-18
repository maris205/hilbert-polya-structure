# Plan self-audit — not the independent gate

Date: 2026-08-18 UTC.

This checklist records the writer’s own adversarial pass over
`PAPER_PLAN.md`.  It did not set `PLAN_READY`; the independent recheck in
`reviews/PLAN_RECHECK_FINAL.md` did so after all three major blockers from
`reviews/PLAN_REVIEW_RAW.md` were resolved.

## Quantifier and endpoint audit

- The main theorem quantifies over every integer `b >= 2`, every finite
  `q >= 1`, and complex `s`, with singular values depending only on
  `sigma = Re(s)`.
- The critical condition is strict and contains a maximum.  When
  `log_b(kappa_{b,q}) <= 1`, the universal wall is active and the column
  witness rejects equality at `sigma = 1`.  Independently, each digit-wall
  pinching construction is stated for its full nonmembership ratio
  `kappa_{b,q} b^(-sigma) >= 1`, including strict-below and equality cases.
- For `b >= 3`, same-shell blocks are nonzero and provide the digit-wall
  pinching sequence.
- For `b = 2`, the same-shell block is exactly zero because `C_0 = 0`.
  The plan therefore uses disjoint spaces `I_{2j} + I_{2j+1}` and the exact
  adjacent-shell norm throughout the full bad range.  Equality is the
  repaired endpoint; the same lower bound grows in the strict-below case.
  The plan never cites the higher-radix proof in the binary case.
- The quasi-Schatten range `0 < q < 1` is explicitly excluded because the
  sufficiency proof uses the Banach-ideal triangle inequality.

## Object and trace audit

- The source vertex set is the positive integers.  The zero word appears
  only in finite digit controls and must be deleted before interpreting a
  diagonal or temporal orbit.
- Complex phases are removed by unitary factors on the left and right;
  the plan does not call this a positive-operator identity for nonreal `s`.
- For `r >= 2` and `sigma > 1`, the proof location includes trace-class
  powers, finite-shell convergence, and absolute majorization.  It does not
  present the closed-walk expansion as merely formal.
- The ordinary trace and determinant are restricted to
  `sigma > alpha_b`; `det_2` is restricted to `sigma > 1`.
- The `det_2` logarithmic trace-power expansion is claimed only near
  `z = 0`, although the determinant itself is entire in `z`.
- Binary trace vanishing is structural after zero deletion.  For higher
  radix, positivity is asserted only for real `s`; no complex zero-free
  statement appears.
- Least periods are proved by support witnesses, not inferred from complex
  traces.  The plan rejects an unweighted Artin–Mazur zeta because the fixed
  sets are infinite.

## Evidence and ownership audit

- Every infinite theorem has a manuscript proof location independent of
  evaluator output.
- Finite evaluator counts, proof-auditor certificates, mutation results,
  Route results, and hostile replays are named by evidence type.  None is
  described as a proof of the infinite theorem.
- Kummer is restricted to prime radix; composite radix uses the direct
  no-carry predicate.
- All finite Pascal, Boolean, binomial, disjointness, tensor, circuit, and
  singular-value controls receive zero novelty credit.
- The source-search statement is bounded and conditional.  The plan contains
  no “first,” exhaustive, or world-priority wording.
- The plan contains no rational-prime emergence, completed target function,
  Hilbert–Pólya, or Route-B claim.

## Remaining independent-review risks

1. Check whether the title and hero figure make the positive-vertex
   convention visible early enough.
2. Check that the 16–20 page occupancy budget, which expressly includes the
   abstract, three figures, and two tables, leaves room for the two endpoint
   proofs and trace-power convergence in the main text.
3. Check that related work is a synthesis rather than a source-by-source
   list despite the large ownership ledger.
4. Check whether the validation section should precede or follow temporal
   consequences; the current order keeps the theorem proof uninterrupted.
5. Check every bibliography role against `evidence/SOURCE_VERIFICATION.md`.

## Phase-gate audit

- `PLAN_READY` is only the independently reviewed manuscript-plan gate.
- Protected-authority replay is a later publication/closure gate.  Passing
  plan review neither certifies protected bytes nor authorizes a final writer
  seal or manifest.
- At plan-review time, until a live protected manifest was injected and
  independently replayed, that later gate remained
  `WAIT_PROTECTED_AUTHORITY`.  Subsequent writer closure retired that state
  and is now `HOLD_FOR_INDEPENDENT_WRITER_AUDIT`; this historical plan audit
  did not itself certify the later transition.
