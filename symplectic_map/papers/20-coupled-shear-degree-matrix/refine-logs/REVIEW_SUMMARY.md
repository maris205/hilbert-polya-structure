# Paper20 — Author Self-Audit (not an independent review)

This file records an author-side consistency check only. No reviewer persona,
external panel, or independent review was run. The parent agent must commission
that step separately.

## Current disposition

`CONDITIONAL DESIGN GO` for the fixed \(\mathbb A^4\) family and `HOLD` for any
broader family, manuscript, experiment, or publication claim.

## Self-audit checklist

| Gate | Result | Evidence pointer |
|---|---|---|
| Dimension and parameter are unambiguous (\(\mathbb A^4\), integer \(g\ge5\)). | PASS | `RESEARCH_QUESTION.md`, `FINAL_PROPOSAL.md` |
| Potentials and shear order are literal. | PASS | Same files; `PROOF_PACKAGE.md` §1 |
| Symplecticity and inverse maps are proved. | PASS | Lemma 1 |
| Newton rows are tied to actual monomials, not free matrices. | PASS | `PROOF_PACKAGE.md` §1, Lemmas 2–3 |
| Full-step versus half-step matrix is separated. | PASS | Lemma 6 and matrix-phase warning |
| Cone selector inequalities are symbolic in all \(g\ge5\). | PASS | Lemmas 2–4 |
| Phase-return equality is handled. | PASS | Lemma 4 two-phase wording |
| No-cancellation hypothesis is explicit. | PASS | Lemma 5 |
| Total-degree visibility is stated. | PASS, must remain literal in any rewrite | Lemma 6 |
| Perron root calculation is exact. | PASS | Lemma 7 |
| P12–P19 collision table exists. | PASS | `NOVELTY_ASSESSMENT.md` |
| Citation claims are source-bounded and non-priority. | PASS | `CITATION_VERIFICATION.md` |
| Experiments or hidden CAS certificates were used. | NONE | `EXPERIMENT_TRACKER.md` |

## Remaining proof obligations before a paper claim

1. A second reader must independently expand the four selector inequalities and
   the carried-coordinate comparisons, without replacing them by a generic
   Newton-fan assertion.
2. The reader must check that the ratio interval is strict at the upper end and
   that \(f_g(1)>1\) for every allowed integer \(g\).
3. The reader must verify that the coordinate-degree maximum is always the
   second \(q\)-coordinate and that the Perron eigenvector is visible to it.
4. The reader must challenge the phrase “non-product” and confirm that it is
   restricted to the stated degree comparison/support coupling.
5. Any coefficient generalization must be postponed until a separate leading
   coefficient/resultant argument is written.

Failure of any item changes the state to `STATIC BLOCK`; no informal repair or
numerical example is sufficient.

## Prohibited interpretation

This self-audit is not an acceptance decision, novelty certificate, source
verification report, or permission to create a manuscript. It intentionally
ends before independent review.
