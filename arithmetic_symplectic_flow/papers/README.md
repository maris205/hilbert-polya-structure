# Markdown paper registry

**Current state:** no candidate-specific paper has been created yet. To perform
P0, first create the numbered package and its `candidate-card.md`; after every
required identity/ownership field is frozen, populate `paper.md` from the
template as the first candidate-specific paper. No theorem, computation, or
Route claim precedes that freeze.

This directory is intentionally lighter than historical Flow/Symplectic
pipeline trees. Each substantive result is a self-contained Markdown paper
package; it may report a theorem, a certified computation, a negative result,
an obstruction, an inconclusive audit, or a methodological result. No result is
promoted merely because it has a paper.

## Registry

| ID | Candidate | Status | A0 | A1 | A2 | Paper |
| --- | --- | --- | --- | --- | --- | --- |
| — | No candidate frozen | `NOT STARTED` | `OPEN` | `OPEN` | `OPEN` | — |

Update this table only after the detailed package exists and names a frozen
candidate ID. Do not merge different objects into a single row.

## Required package layout

Create one new, stable directory per candidate-level result:

```text
papers/NNN-short-slug/
  README.md                 # status card, links, object ID, one-paragraph outcome
  paper.md                  # complete Markdown paper; authoritative prose record
  candidate-card.md         # versioned P0 object/ownership specification
  claim-ledger.md           # scoped claims, evidence class, controls, status
  evidence/README.md        # provenance / reproducibility index, if applicable
```

`NNN` is monotonically increasing and must not be reused. Additional material
may be added when genuinely needed, but do not recreate a heavyweight generic
`code/experiments/results/notes/PDF` tree by habit. Keep an exact result with
its inputs and reproducibility record; keep exploratory scratch material clearly
separate from a paper's supported claims.

## What every `paper.md` must contain

Start from [paper-template.md](paper-template.md). At minimum, a paper must
state:

1. title, date, paper ID, candidate ID, and evidence/status label;
2. exact mathematical object and the same-object ownership table;
3. research question and the strongest claim actually supported;
4. allowed data, sources, parameters, normalizations, and methods;
5. results, with theorem/computation/heuristic labels kept distinct;
6. adversarial controls, failed tests, uncertainties, and scope limits;
7. precise A0/A1/A2 status (`PASS` only when formally supported; otherwise
   `OPEN`, `NOT_TESTABLE`, scoped `FAIL`, etc.); and
8. an explicit next decision: continue, stop, or fork.

The paper must never use a symbolic roof, physical flow, determinant, and
operator from different owners without calling that a failure of the candidate.

## Format boundary

All papers in this Round-2 directory are Markdown (`.md`) only. Do not create
LaTeX or PDF artifacts unless a later user request explicitly changes that
scope. A Markdown source should be complete enough to read and audit without a
compiled companion.
