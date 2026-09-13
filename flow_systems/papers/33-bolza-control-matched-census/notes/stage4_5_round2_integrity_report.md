# P33 Stage 4.5 Round 2 integrity report

## Verdict

**FAIL — corrections proposed, not applied. Stage 5 remains closed.**

| Phase | Denominator | Result |
|---|---:|---|
| A references | 22/22 | PASS |
| B citation contexts | 48/48 checked; 0 verified | FAIL |
| C data/tables/C4 | 196/196; tables 2/2; figures 0 | PASS |
| D originality | 38/72 body; 38/38 changed body; 82/82 searches | PASS WITH NOTES |
| E registered claims | 376/376; 62 UNVERIFIABLE | FAIL |
| E6 revision operations | 50/50 across 2 rounds | PASS (none detected by recorded semantic review) |
| Seven failure modes | Mode 4 SUSPECTED; Mode 2 INSUFFICIENT EVIDENCE | FAIL |
| Isolated build | 4/4 commands; 18 pages; final citations clean | PASS |
| Schema 12 compliance | PRISMA-trAIce adaptation + RAISE full; non-SR contribution | WARN (separate) |

## Blocking findings

1. `IL-SERIOUS-1`: all 48 literature uses are `anchor=none` and `claim_to_passage=INCONCLUSIVE`. A bounded identifier endpoint is not passage verification.
2. `IL-MEDIUM-1`: one generator authored the synthetic fixtures, expected oracle, and harness; an independent oracle/runtime has not ruled out shortcut or circular agreement.

The correction list is `stage4_5_round2_integrity_correction_list.json` (bea2015859f5ac196380098fb419a2b916b082fc50186ffda0494ace8e2f1601). No correction, manuscript/Bib edit, scientific execution, canonical promotion, Route change, or Stage-5 action was authorized or performed.

The independent Schema-12 compliance report is `stage4_5_round2_compliance_report.json` (b001858f66ed01344dd95e1c6948175798cd638fb390bc86587ca61fa316602b) with `overall_decision=warn`. This compliance contribution does not dilute, replace, or manufacture the Phase-B/E and Mode-4 integrity findings.

The pre-authority originality attempt remains archived as `ATTEMPT1_INVALID`, and two post-authority aborted attempts remain fail-closed incident records. None of their partial material was reused; the controlling 82-query raw record is bound to the fresh collector.

## Mandatory C4 boundary

This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS.

## Assurance boundary

The FAIL verdict concerns the audited evidence chain. It does not assert that the prospective certificate architecture or underlying mathematics is false.
