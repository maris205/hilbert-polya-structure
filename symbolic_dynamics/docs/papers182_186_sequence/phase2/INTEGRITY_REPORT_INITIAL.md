# Initial integrity report — P182–P186

**Audit date:** 2026-09-03 UTC.  **Mode:** pre-review registered-population
verification.  **Verdict:**
`PASS_INTERNAL_WITH_NOTES / RELEASE_TO_HOSTILE_REVIEW / HOLD_EXTERNAL`.

This report verifies named reference, citation-context, manuscript-claim, and
artifact populations.  It does not certify semantic extraction completeness,
the truth of unregistered claims, proof correctness, novelty, or actual
independent error processes.

This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS.

No experiments are reported.  The five exact programs are proof-regression and
finite-counterexample controls, not experiments and not substitutes for the
written all-parameter proofs.

## Verification summary

| category | registered population | passed | issues / notes |
|---|---:|---:|---|
| reference existence | 15 | 15 | 0 |
| bibliographic field accuracy | 15 | 15 after correction | P185 issue 16 -> 17 repaired before freeze |
| bibliography-to-body / body-to-bibliography keys | 15 | 15 | 0 orphan; 0 dangling |
| citation-context scope | 15 | 15 | all background/ingredient/boundary uses; no cited source is credited with a selected theorem |
| external statistical/data surfaces | 0 | 0 | none reported |
| internal exact-control surfaces | 5 | 5 | canonical byte replay and manifest PASS |
| registered claim groups | 47 | 47 | 32 theorem/control groups plus 15 cited-source scope groups; semantic extraction completeness `not_machine_detectable` |
| originality screen | 36 of 116 prose blocks | 36 | 31.0%; 0 close/verbatim matches |
| self-plagiarism | — | — | `NOT_CHECKED`: anonymous authors; no author publication list supplied |

The 32 theorem/control groups are the rows in the five paper-local
`CLAIMS_EVIDENCE.md` ledgers (excluding P182 C8, which explicitly says that a
bounded owner-search non-hit is not claimed).  Every group has a deductive
location; every finitely testable specialization has a canonical control.
Grouping is semantic and may omit claims, so the denominator is not described
as mechanically complete.

## Phase A — reference verification

Semantic Scholar DOI lookup returned HTTP 429 during the run; under the API
protocol this is `S2_API_UNAVAILABLE`, not a failed-existence verdict.  The gate
therefore fell back to item-by-item publisher/DOI WebSearch plus Crossref field
comparison.  Every DOI resolves to the cited work and all author, title, venue,
volume, issue, page/article-number, and publication-year conventions match the
paper after the one recorded repair.

| key | verdict | verified metadata surface |
|---|---|---|
| `Birkhoff1967` | VERIFIED | AMS Colloquium Publications 25 and third-edition catalog record: `https://bookstore.ams.org/COLL/25` |
| `GoldmanRota1970` | VERIFIED | `https://doi.org/10.1002/sapm1970493239` |
| `ChajdaLanger2019` | VERIFIED | `https://doi.org/10.1007/s00500-019-03866-y` |
| `Hong2022` | VERIFIED | `https://doi.org/10.1016/j.aam.2022.102362` |
| `GasanovaNicklasson2024` | VERIFIED | `https://doi.org/10.1007/s10801-023-01294-8` |
| `Brown2000` | VERIFIED | `https://doi.org/10.1023/A:1007822931408` and arXiv `math/0006145` |
| `YinZhu2016` | VERIFIED | `https://doi.org/10.1016/j.physa.2015.12.008` and arXiv `1412.2187` |
| `CirkovicEtAl2023` | VERIFIED | `https://doi.org/10.1093/comnet/cnad031` and arXiv `2201.03769` |
| `XuZou2009` | VERIFIED | `https://doi.org/10.1016/j.jalgebra.2008.09.029` and arXiv `0810.3164` |
| `AnashinKhrennikov2009` | VERIFIED | `https://doi.org/10.1515/9783110203011` |
| `KonyaginEtAl2016` | VERIFIED | `https://doi.org/10.1016/j.jctb.2015.07.003` and arXiv `1307.2718` |
| `MansourVajnovszki2013` | VERIFIED AFTER REPAIR | `https://doi.org/10.1016/j.ipl.2013.05.008`; correct issue is 17 |
| `Wachs1994` | VERIFIED | `https://doi.org/10.1016/0097-3165(94)90117-1` |
| `Stanley2012` | VERIFIED | Cambridge second-edition record, `https://doi.org/10.1017/CBO9781139058520` |
| `Fayers2023` | VERIFIED | `https://doi.org/10.1007/s00026-022-00577-4`; online 2022, volume issue 2023 |

Each exact title/author/year query, DOI query, and publisher result was inspected
on 2026-09-03.  The cited records are distinct; no same-author/title mashup or
DOI misdirection was observed.  This is an existence/metadata determination,
not an endorsement of any source's conclusions.

## Phase B — citation contexts

All 15 registered entries were checked in context, exceeding the initial 30%
minimum.  P182 cites lattice absorption, finite-subspace enumeration,
complements, and nearby lattice operators; P183 cites reciprocity ensembles,
growing reciprocal networks, and finite-semigroup chains; P184 cites broad
finite-ring, algebraic, and polynomial functional-graph dynamics; P185 cites
restricted-growth encodings and generation; P186 cites strict/weak shifts,
stars and bars, beta sets, and core-partition context.  Every manuscript
expressly assigns these ingredients zero contribution credit.

No citation is used as evidence that the literal map is new.  Every direct-owner
search result is bounded by date/query/surface and remains a non-hit, never a
novelty, priority, ownership-clearance, or freedom-to-operate conclusion.

## Phases C and E — data and claim alignment

There are no externally sourced data, figures, empirical tables, human subjects,
or experiments.  All displayed numerical examples are exact consequences of a
stated formula and/or retained canonical output.  Root replays matched all five
author canonicals byte for byte, totaling 24,359,132 assertions.

The registered theorem/control claim groups were checked against their proof
locations and finite controls.  No claim relies on a skipped or undocumented
experiment.  This establishes traceability inside the named registry only; it
does not by itself validate the proofs.  The two process-separated hostile
reviews remain responsible for adversarial mathematical checking.

## Phase D — originality

The separate `ORIGINALITY_AUDIT_INITIAL.md` records all 36 exact-phrase queries,
the 116-block denominator, sampling rates, and grades.  No qualifying close or
verbatim public-Web match was found.  Author-based self-reuse could not be
checked because author identities were not supplied.

> This originality screen uses public WebSearch heuristically and is not
> Turnitin, iThenticate, or equivalent professional software.  Closed-corpus,
> translated, and unsampled reuse can be missed.

## Issue and advisory ledger

- **Closed Medium bibliographic issue:** P185 Mansour--Vajnovszki issue number
  corrected from 16 to 17 before Round-0 freeze.
- **Closed source-rendering issues:** P182's malformed exponent and P186's stray
  summation comma were corrected and rebuilt before Round-0 freeze.
- **Open advisory:** self-plagiarism check not run because authors are anonymous.
- **Open advisory:** bounded exact-owner non-hits do not close owner status.
- **Open advisory:** registered-claim semantic extraction completeness is not
  machine-detectable.
- **Open lifecycle boundary:** all five papers remain `OWNER_AMBER /
  HOLD_EXTERNAL`.

There are zero open Critical, Serious, or Medium integrity issues in the named
registered populations.  The batch may enter hostile Review A; external release
remains prohibited.

