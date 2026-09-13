# Paper template — `NNN-short-slug`

> First create `papers/NNN-short-slug/candidate-card.md` and complete the P0
> freeze. Then copy this file into `paper.md`. Replace every bracketed field;
> do not retain a template statement as if it were evidence.

## Title

`[Precise result title for Candidate ASFS-…]`

**Paper ID:** `NNN-short-slug`<br>
**Candidate ID:** `[ASFS-…]`<br>
**Date / status:** `[YYYY-MM-DD; PROPOSAL | THEOREM | COMPUTATIONAL | NEGATIVE | INCONCLUSIVE]`<br>
**Route state:** `[owner-level A0/A1/A2 evidence …; formal Route-A tuple …; Route B NOT INVOKED unless actually evaluated]`

> An owner-level P3 same-object determinant result is not a formal Route-A A2
> `PASS`: the full Route-A evidence contract, including its target/divisor
> requirement, must be evaluated separately. A limited early audit never
> changes Route B from `NOT INVOKED` or issues a B coordinate.

## Abstract

State the exact object, question, main supported result, controls, and what is
not claimed. Do not mention RH, a Hilbert--Pólya realization, a Riemann-zero
match, or a Route pass unless the body supplies the required candidate-specific
evidence.

## 1. Candidate identity and same-object ledger

| Item | Frozen definition / owner | Status |
| --- | --- | --- |
| Phase space \((M,\omega)\) | `[…]` | `[frozen/open]` |
| Base symplectic map \(F\), parameters | `[…]` | `[frozen/open]` |
| Roof \(\tau\), mapping torus, suspension flow | `[…]` | `[frozen/open]` |
| Arithmetic source / allowed data | `[…]` | `[frozen/open]` |
| Coding / orbit ledger / repetitions | `[…]` | `[frozen/open]` |
| Transfer operator / zeta / determinant | `[…]` | `[frozen/open]` |
| Controls / future operator owner | `[…]` | `[frozen/open]` |

Explain any relation between the symplectic base map, the odd-dimensional
suspension flow, and an optional future Hamiltonian/contact/quantum lift. Do
not call them identical without a construction.

## 2. Question and claim boundary

### Question

`[Exact A0, A1, A2, or scoped methodological question.]`

### Strongest supported claim

`[One scoped statement. State whether it is a theorem, finite computation, negative result, heuristic, or not testable.]`

### Explicit nonclaims

- `[…]`
- `[No cross-object determinant/clock/operator transfer.]`
- `[No Route-B or RH/zero-matching claim unless formally supported.]`

## 3. Definitions, inputs, and provenance

Give formal definitions, source identities, parameter-selection rule,
normalizations, allowed/prohibited data, and any input locks. Specify which data
were unavailable at model selection or validation time.

## 4. Method / proof / computation

State enough detail to distinguish exact derivation, certified numerical work,
and exploratory observation. For computations include exact commands/methods,
inputs, precision, cutoff, enumeration coverage, and output locations.

## 5. Results

Present the result with its hypotheses and scope. For closed orbits and
determinants, show that the same roof/clock, primitive convention, normalization,
and owner are used throughout.

## 6. Controls and adverse findings

Report applicable arithmetic, geometric, ownership, robustness, and
`PROVES_TOO_MUCH` controls. Preserve failed controls, mismatches, uncertainty,
and negative conclusions rather than removing them from the narrative.

## 7. Gate assessment

| Gate | Evidence for this exact candidate | Status | Limitation / next obligation |
| --- | --- | --- | --- |
| A0 | `[…]` | `[OPEN / NOT_TESTABLE / PASS / scoped FAIL]` | `[…]` |
| A1 | `[…]` | `[OPEN / NOT_TESTABLE / PASS / scoped FAIL]` | `[…]` |
| A2 | `[…]` | `[OPEN / NOT_TESTABLE / PASS / scoped FAIL]` | `[…]` |
| Route B | `[not evaluated unless justified]` | `[NOT INVOKED / …]` | `[…]` |

If this paper reports only an owner-level analytic P3 result while target/divisor
validation is deliberately out of scope, record formal A2 as `UNASSIGNED` /
`NOT EVALUATED`, not `PASS`.

## 8. Conclusion and decision

State whether this candidate continues to the next named gate, stops, or forks.
If it forks, name the new candidate ID and make clear that previous credit is
not silently inherited.

## Reproducibility / evidence index

Link the candidate card, claim ledger, inputs, source records, commands, and
generated evidence. Explain all limits that prevent an independent reader from
reproducing a stated result.
