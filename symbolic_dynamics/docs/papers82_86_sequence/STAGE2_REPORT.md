# Stage 2 report — Papers 82–86

Status: **five theorem-bearing manuscripts and PDFs generated**.
External release: **HOLD**.

## Artifact census

| Paper | Current pages | Concrete landed advance | Deterministic control |
|---|---:|---|---|
| P82 | 6 | rank-two frozen SFT, closed fixed count/spatial zeta, reversing involution and conservation | 299,592 states; 1,878,811 instrumented assertions |
| P83 | 4 | exact recurrence trichotomy, Gurevich entropy, maximal-return law and boundary fixed counts | 1,369 exact assertions through order 40 / parameter 50 |
| P84 | 4 | divisor periodic spectrum, rational zeta, period boundary, sharp odd mixing rate and rigidity | 19,901 exact matrix/divisor assertions |
| P85 | 4 | explicit cyclic-suspension normal form, `(p,Q)` classification, zeta and maximal law | 5,242 exact assertions across 340 schedules |
| P86 | 7 | support SFT, word recurrence, one-dependence/infinite memory, cylinder law and entropy series | four finite fields; 24 block lengths; 14,676 hidden words; 4,258 observed words; 199 exact context checks |

Final manuscript length after hostile-audit corrections: **25 pages**.  Exact
byte counts and digests are frozen in `FINAL_QA_REPORT.md` and
`CANONICAL_PDF_MANIFEST.sha256`.

## Paper packages

- [`papers/82-shifted-fredkin-frozen-sft/`](../../papers/82-shifted-fredkin-frozen-sft/)
- [`papers/83-colored-catalan-renewal-shifts/`](../../papers/83-colored-catalan-renewal-shifts/)
- [`papers/84-unitary-cayley-shifts/`](../../papers/84-unitary-cayley-shifts/)
- [`papers/85-periodic-alphabet-full-shifts/`](../../papers/85-periodic-alphabet-full-shifts/)
- [`papers/86-finite-field-adjacent-product-process/`](../../papers/86-finite-field-adjacent-product-process/)

Each package contains an anonymous `amsart` manuscript, cited-only
bibliography, canonical PDF, runnable exact control, build instructions, and
claim/evidence boundary.  No target venue is named.

## Claim discipline

- P82 labels its zeta as the spatial frozen-set zeta, not the temporal zeta of
  the finite-ring dynamics.
- P83 consistently uses Gurevich entropy and does not call its countable-state
  shift compact.
- P84 treats the unitary Cayley spectrum and finite-type determinant as owned
  inputs.
- P85 covers only unconstrained periodic alphabet schedules, not general
  rectangular transition cocycles.
- P86 distinguishes finite dependence range from finite Markov order and
  treats search absence only as a bounded firewall.

Writing-level source details are in
[`phase2/SOURCE_VERIFICATION_REPORT.md`](phase2/SOURCE_VERIFICATION_REPORT.md).
