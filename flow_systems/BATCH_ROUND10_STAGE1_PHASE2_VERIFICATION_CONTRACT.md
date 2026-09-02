# Round 10 Papers 29–33 — Stage 1 Phase-2 verification contract

Date frozen: **2026-09-02 UTC**  
Scope: **ARS Phase 2 investigation only**

## Separation of duties

Each paper receives two logically separate passes:

| Paper | Bibliography seat | Independent verification seat |
|---|---|---|
| P29 | `BIB-SEAT-A` | `VERIFY-SEAT-C` |
| P30 | `BIB-SEAT-A` | `VERIFY-SEAT-C` |
| P31 | `BIB-SEAT-B` | `VERIFY-SEAT-A` |
| P32 | `BIB-SEAT-B` | `VERIFY-SEAT-A` |
| P33 | `BIB-SEAT-C` | `VERIFY-SEAT-B` |

The verification seat may correct metadata only in a separately recorded
errata table. It may not silently rewrite the bibliography seat's source
inventory, infer novelty, or produce Phase-3 synthesis.

## Corpus acceptance contract

For each paper:

- at least 15 unique included sources are required for ARS full mode;
- at least 60% must be peer-reviewed, except that a first-party authoritative
  software/theorem record is classified separately rather than falsely called
  peer-reviewed;
- foundational mathematical sources are exempt from recency penalties when
  the supported claim is foundational;
- every record must expose an exact title, author list, year, venue or source
  family, DOI when one exists, stable locator, document type, theme, metadata
  basis, and inspected-content status;
- exact search strings, interfaces, search date, inclusion/exclusion criteria,
  retained screening counts, deduplication rules, and limitations must be
  reproducible;
- search interfaces that do not expose a stable universe may report only the
  records actually inspected; estimated or invented hit totals are forbidden;
- search non-detection never proves novelty.

## Per-source verification outcomes

Only these existence/metadata outcomes are allowed:

```text
S2_VERIFIED
VERIFIED
PLAUSIBLE
UNVERIFIABLE
FABRICATED
```

`S2_VERIFIED` requires a recorded Semantic Scholar match under the ARS
similarity/year rule. `VERIFIED` requires an exact DOI or first-party metadata
match. `PLAUSIBLE` is reserved for a DOI-less source confirmed through an
authoritative catalog or exact-title search. `UNVERIFIABLE` is retained with
an explicit warning or excluded from claim-bearing use. `FABRICATED` is a
Critical integrity failure and must be removed.

API degradation must be recorded as degradation, never converted into a
negative match. Browser pages may make bounded first-party checks but may not
be used to evade a structured API rate limit.

## Mathematical evidence grading

The ARS Level-I--VII design ladder is recorded, but it is not misused as an
experimental hierarchy for pure mathematics. Original theorem/construction
papers are normally Level VI on the field-neutral ladder and are independently
graded A--F for fitness to the exact claim by mathematical field norms.

Each source-verification report must record:

1. source existence and metadata outcome;
2. field-neutral design level and claim-fitness grade;
3. peer-review/venue and predatory-venue assessment;
4. currency or foundational exemption;
5. disclosed or observable conflict limits;
6. the exact claim surface it can support;
7. the exact stronger claim it cannot support; and
8. retraction-status check or an explicit `NOT_CHECKED` limitation.

The verification seat writes both
`notes/stage1_phase2_source_verification.md` and the machine-auditable
`notes/stage1_phase2_source_verification.tsv`. The TSV has the exact header:

```text
source_id\texistence_outcome\tmetadata_match\tevidence_level\tclaim_fitness_grade\tvenue_assessment\tcurrency_assessment\tcoi_assessment\tretraction_assessment\tsupport_class\tverified_locator\tnotes
```

Every bibliography inventory `source_id` must appear exactly once; extra IDs
and silent omissions are forbidden.

## Paper-level Phase-2 disposition

Phase 2 may issue only one of:

```text
PHASE2_SOURCE_BASE_READY
PHASE2_SOURCE_BASE_READY_WITH_WARNINGS
PHASE2_SOURCE_BASE_INSUFFICIENT
PHASE2_INTEGRITY_BLOCK
```

These labels answer whether the verified corpus is fit for Phase 3. They are
not novelty verdicts, scientific results, formal Route-A tuples, or permission
to compute.

## Frozen route boundary

Route A and Route B remain governed by `skills/route-a-evaluator.md` and
`skills/route-b-evaluator.md`. Phase 2 cannot assign or promote a tuple. P30
retains `A0_FAIL / A2_NOT_ELIGIBLE / NO_ROUTE_PROMOTION`; P33 retains
`A0_INCONCLUSIVE_SYSTOLE_CONFOUNDED` and
`A0_CONTROL_PANEL_INCOMPLETE`; Route B remains closed for all five.
