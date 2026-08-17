# Retrospective selection and provenance audit

## Governance facts

Terminal Paper 39 supplies six historical non-affine existence witnesses and
explicitly records `ranking_performed: false` and `candidate_selected: false`.
Its handoff is not a ranking or successor authorization.

The final Paper-40 research seal is a collision/boundary input for proposed
`SD-C42`, not an authorization source. The frozen Paper-41 preauthority
package is likewise a collision/boundary input for proposed `SD-C43`, not an
integrated Route result and not a ranking source.

```text
P39 witness existence != ranking != authorization
P40 research seal != P42 selection authority
P41 preauthority freeze != P42 selection authority
```

## Retrospective six-card rule

The following semantic Boolean rule uses only fields already present in each
immutable Session-4 card:

```text
eligible_44(c) :=
  c.A0 == A0_WEAK_ARITHMETIC_RELATION
  and c.A0.evidence_status == PROVED
  and c.A1 == A1_PASS_ANALYTIC
  and c.A1.evidence_status == PROVED
  and c.A2 == A2_ANALYTIC_DETERMINANT
  and c.A2.evidence_status == PROVED
  and c.A3 == A3_FAIL
  and c.A3.evidence_status == PROVED
  and c.source clock is the constant finite-field degree clock log(q)
  and c's explicit A0 failure is the absence of a rational-prime
      primitive/factor correspondence.
```

This rule asks for the exact clock/factor projection closure of the historical
function-field analogue: retain a proved primitive ledger and determinant,
but close the rational-prime identification before any further analytic work.
It does not use paper number, P39 ordering, P40 corrections, P41 witnesses, or
an integrated-successor list.

## Six-card application

| Card | Frozen tuple | Rule result |
|---|---|---|
| `SD-C01` | `(A0_WEAK_ARITHMETIC_RELATION, A1_PASS_ANALYTIC, A2_ANALYTIC_DETERMINANT, A3_FAIL, A4_FAIL)` | **passes every clause** |
| `SD-C02` | `(A0_FAIL, A1_FAIL, A2_ANALYTIC_DETERMINANT, A3_FAIL, A4_FAIL)` | fails A0 and A1 |
| `SD-C03` | `(A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | fails A0, A1, and A2 |
| `SD-C04` | `(A0_WEAK_ARITHMETIC_RELATION, A1_PASS_ANALYTIC, A2_ANALYTIC_DETERMINANT, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FORMAL_HINT)` | fails the A3-fail and finite-field-clock clauses |
| `SD-C05` | `(A0_STRUCTURAL_ARITHMETIC_RELATION, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)` | fails A0, A1, and A2 |
| `SD-C06` | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_FAIL, A2_FAIL, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)` | fails A0, A1, A2, and A3 clauses |

Hence `{c: eligible_44(c)}={SD-C01}`.

## Chronology limitation

The rule was constructed after all six card outcomes and the Paper-42
witnesses were known. There is no earlier byte-stable selector. Consequently:

```text
unique retrospective result != prospective selection
unique retrospective result != outcome-independent evidence
unique retrospective result != novelty or priority credit
```

Only the final corrected package bytes are frozen before independent DA.

## Non-duplication boundary

- Paper 1 owns the full-shift ledger, necklace formula, determinant, and
  finite-memory divisor-growth theorem. Paper 42 may claim only the exact
  rational-prime clock/marker/multiplicity non-descent and repair typing.
- Paper 24 owns a general finite-alphabet prime-code/Fredholm trilemma. Paper
  42 does not re-prove Kraft noncompactness or quantify over arbitrary codes.
- Paper 40 owns the Gauss/Mayer pair ledger and its projection firewalls.
  Paper 42 has a finite-field full-shift object, a symbol marker, and no Mayer
  operator.
- Paper 41 owns rooted Knauf clock/sign non-descent. Paper 42 uses a cyclic
  clock that does descend perfectly on its own source; only the change from
  function-field norms to rational-prime factors fails.

## Authorization statement

This document proposes `SD-C44`; it does not authorize an authority directory,
Route record, registry entry, README edit, manifest, or Git operation.
Independent DA must approve the rule, theorem scope, source convention,
literature collision boundary, and strict Route tuple. Root governance must
separately authorize any integration.
