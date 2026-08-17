# Retrospective selection and provenance audit

## Governance facts

Terminal Paper 39 is read only at authority commit
`18530b90317f6efc43ec2e4601ed8cef57daaddc`, with Stage-1 parent
`0f194edbfd05af853153043a568ffafd6c2f8afb`.  Its sealed text says the six
Session-4 cards are historical non-affine **existence witnesses** only:
`ranking_performed: false`, `new/ranked/proposed=0/0/0`.  Therefore:

```text
P39 witness existence != candidate ranking != successor authorization.
```

The Paper-40 final research lock is separately readable and internally
complete, but is not used as authority integration for this package.  Its
research result addresses `SD-C04`/proposed `SD-C42`.  Its in-flight or
post-run corrections receive no novelty, priority, or selection credit here.

## Retrospective selection rule

The following Boolean rule is applied to the six immutable Session-4 Route
cards, using only fields already present in those cards:

```text
eligible(c) :=
  c.A0 == A0_ANALYTIC_ARITHMETIC_ORIGIN
  and c.A0.evidence_status == PROVED
  and c.A1 == A1_FAIL
  and c.A2 == A2_FAIL
  and c.A3 == A3_PARTIAL_ANALYTIC_STRUCTURE
  and c.A3.evidence_status == PROVED
  and c.next_smallest_test explicitly requests
      (canonical primitive-cycle construction or no-go)
      plus an endogenous-sign test.
```

The rule encodes a narrow research priority: take the strongest already
source-proved arithmetic/analytic collision for which the original card
itself asks for a primitive-ledger and sign-origin closure, while A1 and A2
remain failed.  It does not use paper number, P39 ordering, P40 selection, or
any Paper-40 corrective witness.

### Chronology limitation

This rule was constructed after all six cards, their Route results, and the
exact Paper-41 witnesses were known.  No earlier byte-stable preregistration
or outcome-blind selector exists.  Consequently:

```text
unique retrospective rule result != prospective selection
unique retrospective rule result != outcome-independent evidence
unique retrospective rule result != novelty or priority credit
```

In this package “independent selection provenance” means only that the rule
does not inherit ranking or authorization from P39 or P40.  Only the final
corrected input bytes are frozen before independent DA.

## Six-card application

| Card | Frozen tuple | Rule failure or pass |
|---|---|---|
| `SD-C01` | `(A0_WEAK_ARITHMETIC_RELATION, A1_PASS_ANALYTIC, A2_ANALYTIC_DETERMINANT, A3_FAIL, A4_FAIL)` | fails A0, A1, A2, A3 clauses |
| `SD-C02` | `(A0_FAIL, A1_FAIL, A2_ANALYTIC_DETERMINANT, A3_FAIL, A4_FAIL)` | fails A0, A2, A3 clauses |
| `SD-C03` | `(A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | fails A0, A1, A3 clauses |
| `SD-C04` | `(A0_WEAK_ARITHMETIC_RELATION, A1_PASS_ANALYTIC, A2_ANALYTIC_DETERMINANT, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FORMAL_HINT)` | fails A0, A1, A2 clauses |
| `SD-C05` | `(A0_STRUCTURAL_ARITHMETIC_RELATION, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)` | fails A0 and A3 clauses |
| `SD-C06` | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_FAIL, A2_FAIL, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)` | **passes every clause** |

The selector is unique: `{c : eligible(c)} = {SD-C06}`.

## Historical test executed

The immutable `SD-C06` card ends with:

> Construct or rule out a canonical primitive-cycle map for the frozen binary
> recursion and test whether a pre-existing symmetry produces the sign before
> any analytic target comparison.

Paper 41 proposes to rule out only the literal rooted-word-to-necklace descent,
the direct-limit append dynamics, and the literal scalar Liouville phase.  It
does not claim to rule out every extension.

## Non-duplication decision

- Paper 1 owns the source recursion, zeta quotient, and statement of the open
  bridge.  Paper 41 must add exact non-descent theorems, not restate the open
  bridge.
- Paper 33 proves operator non-descent for a Manin-relation quotient of a
  projective-residue graph.  Paper 41 uses a different source, quotient, and
  one-step witness.
- Paper 35 owns the general diagonal partition-trace firewall.  Paper 41's
  diagonal determinant calculation is labeled a comparison lemma only.
- Paper 40 owns the Gauss/Mayer pair ledger and projection firewalls.  The
  cyclic trace repair for the Knauf matrices is explicitly typed as a changed
  Farey/Gauss object and earns Paper 41 no positive A1/A2 credit.

## Authorization statement

This retrospective audit proposes `SD-C43`; it does not authorize it.
Independent DA must
approve the selection logic, theorem scope, and collision boundary.  Root
governance must separately authorize any authority directory, registry entry,
Route record, or Git operation.
