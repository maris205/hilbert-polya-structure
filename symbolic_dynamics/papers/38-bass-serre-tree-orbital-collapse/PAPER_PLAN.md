# Paper 38 paper plan — SD-C40

Working title: **Empty on the Tree, Generic on the Orbits: A Bass--Serre
No-Go for the Affine Branch**.

One-sentence contribution: For the original `BS(1,r)` Bass--Serre object, the
literal full-tree geodesic ledger is empty and its Hashimoto operator owns no
ordinary Fredholm determinant, while the strongest group-orbital replacement
collapses to a generic necklace law (or balanced divergence) under an
incompatible marker.

Type: theory plus exact adversarial audit.  The final 17-page A4 build follows
the Paper 34--37 house style and includes references and two proof/ownership
appendices; its length preserves the complete same-object and determinant
firewalls rather than compressing them into unproved summaries.

## 1. Claims--evidence matrix

| Claim | Theorem evidence | Exact evidence | Planned section |
|---|---|---|---|
| The full-tree periodic ledger is empty | tree no-reduced-cycle lemma | finite rooted-tree controls | Sections 3--5 |
| The full-tree Hashimoto operator owns no ordinary Fredholm determinant | orthogonal-column noncompactness proof and trace-class necessity | exact column Gram/mass certificates | Sections 4--5 |
| Tree-lattice formulas do not transfer to the frozen action | faithful non-discrete image for `r>=2`; discrete image but infinite kernel/non-proper action for `r=1`; finite-stabilizer criterion | deliberate GBS stabilizer controls | Sections 2, 4--5 |
| The positive-height orbital substitute is generic or divergent | semidirect conjugacy, Burnside, Möbius, and Witt derivation | residue-orbit and degree-12 product checks | Sections 4, 6 |
| The new tree clock cannot inherit the old marker | translation-length proposition | elliptic collapse and many-to-one marker witnesses | Section 7 |
| No source-selective affine sector survives | combined theorem and generic-control firewall | prime/composite, balanced, GBS, and random eligibility controls | Sections 8--9 |

## 2. Section architecture

1. **Introduction.** State the final Paper 37 obligation, the full-tree/
   operator/orbital trilemma, strongest rational formula, marker change, and
   strict decision.  Place the hero figure here.
2. **Primary-source boundary.** Synthesize Bass--Serre geometry, discrete
   tree-lattice zeta, infinite graph determinant categories, conjugacy growth,
   and current graph-of-groups/double-coset work.
3. **Frozen new object.** Define `T_r`, actual-edge geodesic shift, canonical
   cocycle, full-tree versus quotient/orbital spaces, and the new marker.
4. **Terminal theorem.** State the complete theorem, object ledger, and
   `PROVES_TOO_MUCH` boundary.
5. **Tree emptiness and Fredholm failure.** Prove the no-cycle,
   orthogonal-column, modular-weight, `r`-split image/properness, and
   end-kernel claims.
6. **Orbital necklace collapse.** Derive the conjugacy quotient, Burnside
   count, primitive repetition ledger, rational Euler product, modular
   rescaling, and balanced divergence.
7. **Marker and control firewalls.** Prove translation length, compare old and
   new clocks, and report prime/composite plus GBS eligibility logic.
8. **Exact audit.** Report the corrected source/evaluator separation,
   `277/277` assertions, fresh A/B plus isolated cold C identity, `44/44`
   integration tests, `96/96` integrity checks, the 28-file result set,
   42-entry ledger, and finite/theorem evidence boundary.
9. **Route decision.** Resolve `A0`--`A4`, close the affine branch, and state
   the sole Paper 39 closure obligation.
10. **Appendix A.** Full proofs of conjugacy, necklace, primitive-root,
    translation-length, and determinant-category statements.
11. **Appendix B.** Scope declarations, forbidden substitutions, object
    ownership ledger, and reproducibility/disclosure.

## 3. Figure plan

| ID | Type | Comparison and message | Data source | Priority |
|---|---|---|---|---|
| Figure 1 | Hero trilemma | Full tree is empty; its operator is non-Fredholm; changing to group orbits yields only generic/divergent recurrence; all routes end at affine closure | theorem, manual TikZ | High |
| Figure 2 | Orbital derivation pipeline | Semidirect conjugacy to residue orbits to endpoint-identified necklaces to `(1-z)/(1-rz)`, with a visible same-object barrier | exact formulas, manual TikZ | High |
| Figure 3 | Marker/determinant firewall | Old generator clock versus tree height, and ordinary full-tree versus tree-lattice/groupoid/weighted determinant categories | theorem and source taxonomy, manual TikZ | High |

Figure 1 caption must expose the complete decision without surrounding prose.
All figures are pure TikZ, vector, grayscale-legible, and use line style and
labels in addition to color.  No data-driven plot is needed; the quantitative
audit belongs in tables and text.

## 4. Table plan

- full tree / quotient / group-orbital / end object ownership table;
- determinant-category hypothesis table;
- first-six prime/composite class and primitive count table;
- exact-control summary table;
- strict Route-A gate table.

## 5. Citation plan

- Introduction and geometry: Serre, Bass, Clair--Mokhtari-Sharghi, Abbott,
  and Fima et al.
- Determinant boundary: Bass, Clair--Mokhtari-Sharghi, Deitmar, and
  Lenz--Pogorzelski--Schmidt.
- Orbital/conjugacy boundary: Ciobanu--Evetts--Ho and Guo.
- Current neighboring invariants: Hong--Kwon and Marchionna.

Every citation is verified against a DOI, publisher/journal page, or official
arXiv record.  The bibliography contains only cited entries.

## 6. Front-matter and style checks

- The title states both the empty full-tree result and the generic orbital
  replacement.
- The abstract opens with the actual no-go, includes `277/277`, corrected
  fresh/cold reproducibility and the exact rational formula, and states the
  narrow scope; the full scientific digest remains in Sections 1 and 8.
- The introduction makes the What, Why, and So What explicit before setup.
- Figure 1 shows why moving between the three objects does not repair the
  candidate.
- Anonymous author line, boxed research status, modular sections, and concise
  appendices match the house style.
- Limitations and AI-assisted-research disclosure appear in Appendix B.

## 7. Length and evidence discipline

The main proof stays in the main body; routine algebra and expanded ownership
tables move to appendices.  Exact results are reported as deterministic
audits without error bars because no sampling estimator is used.  CPU-only,
integer/Fraction arithmetic, fresh/cold separation, metadata stability, and
second-materialization idempotence are stated explicitly.

The manuscript never promotes finite checks to an infinite theorem and never
uses experiment rows to infer novelty.

## 8. Review boundary and decision

No peer-review or LLM review loop is run by explicit instruction.  The
cross-review steps in the generic writing skills are omitted.  Allowed checks
are mathematical, source, citation, compilation, typography, deterministic
artifact, and direct visual inspection audits.

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_FAIL,
 A2_FAIL,
 A3_FAIL,
 A4_FAIL)

overall: ROUTE_A_REJECTED
route_b_invocation_allowed: false
branch: CLOSE_ENTIRE_AFFINE_BRANCH
```
