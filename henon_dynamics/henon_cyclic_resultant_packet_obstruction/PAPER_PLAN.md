# Paper Plan

**Title:** Cyclic Resultant Packets and a Square-Norm Obstruction for Hénon
Monodromy

**One-sentence contribution:** For every reciprocal algebraic-unit H6
multiplier, full multiplier-field norms are exact squares, whereas the
minimal trace-field half norms and principal-ideal packets survive but form
repetition-indexed collective sequences rather than one-prime-per-orbit
Euler labels.

**Format:** Session mathematical research note (Liang Wang / HUST)

**Type:** theorem + exact symbolic certificate + scoped obstruction

**Date:** 2026-08-14

## Claims–Evidence Matrix

| Claim | Evidence | Status | Paper location |
|---|---|---|---|
| Cyclic determinant ideals and full-field norms are squares | direct eigenvalue identity and unit association | PROVED | Main theorem |
| Primitive full-field cyclotomic norms are squares for every `n>2` | inversion-fixed half-cyclotomic integer in the trace field | PROVED | Main theorem |
| Minimal trace-field norms survive | norm transitivity and exact half norms | PROVED structure | Main theorem |
| Full-field scalarization cannot label rational primes | nonzero integer-square corollary | PROVED obstruction | Corollaries |
| The claim is sharp in its hypotheses | `n=2` nonsquares and a nonreciprocal polynomial with `C_3=13` | NUMERICALLY_CERTIFIED exact controls | Certificate section |
| Ideal packets remain a distinct collective candidate | canonical ideal factorization, no scalarization | PROVED structure / OPEN attachment | Discussion |
| Three H6 examples realize both prime and composite half-norms | exact resultants for repetitions `1..12` | NUMERICALLY_CERTIFIED | Table and JSON |

## Structure

1. **Abstract.** State the square-norm theorem, the 36 exact primitive rows,
   and the ideal-packet boundary.
2. **Introduction and prior gate.** Explain why P48 forces a collective
   object and why cyclic resultants are the smallest source-native test.
3. **Signed H6 monodromy and packets.** Define signed eigenvalues, trace
   fields, cyclic determinant ideals, and cyclotomic packets.
4. **Norm trilemma.** Prove canonicality and full-field squaring, then isolate
   the surviving minimal trace-field norm and ideal packet.
5. **Exact certificate.** Present the three minimal polynomials, repetitions
   through 12, selected half-norms, and adversarial controls.
6. **Primitive-divisor context.** Position cyclic-resultant and
   Lehmer–Pierce literature without importing an inapplicable quartic
   theorem.
7. **Route-A verdict and limitations.** Reject full-field scalar labels;
   retain trace-field sequences and ideal packets as OPEN; keep Route B
   unauthorized.
8. **Conclusion.** Select a prime-ideal packet assembly theorem as the next
   natural question.

## Figure and Table Plan

| ID | Type | Description | Data source | Priority |
|---|---|---|---|---|
| Figure 1 | TikZ algebraic flow | `M^r` → determinant ideal square; cyclotomic factor → trace-field half norm; scalar road stops, ideal road survives | theorem identities | HIGH |
| Table 1 | exact comparison table | selected signed H6 primitive norms and half norms, with prime/composite status | `results/c49_certificate.json` | HIGH |
| Table 2 | route comparison | scalar cyclic norm versus half norm versus ideal packet | theorem package | HIGH |

The hero figure is explanatory rather than decorative: a skim reader sees
that the norm map creates an unavoidable square while the principal ideal is
not deleted.

## Citation Plan

- Hillar (2005): definition and reconstruction role of cyclic resultants.
- Hillar–Levine (2004 preprint): polynomial recurrences of cyclic resultants.
- Postnikova–Schinzel (1968): primitive divisors in algebraic number fields.
- Flatters (2007 preprint): quadratic Lehmer–Pierce norms and the explicit
  boundary beyond which its theorem cannot be imported here.

All metadata are verified against arXiv and/or DOI records.  No citation is
used to prove the new square-norm theorem.

## Review Criteria

- The actual signed period-three eigenvalue must be used.
- `n>2` must never be silently widened to `n>=2`.
- A full-field square must not be presented as the minimal natural norm.
- An ideal packet or trace-field sequence must not be called one Euler prime.
- Primitive-divisor context must remain motivation, not attachment.
- Route A must not mix the rejected scalar lane with the open ideal lane.

## Next Steps

- [ ] Generate the exact JSON certificate and table.
- [ ] Draft the complete LaTeX note.
- [ ] Compile and inspect the PDF.
- [ ] Run hostile theorem/source/evaluator review.
