# Paper Improvement Log

The preserved baseline is `main_round0_original.pdf`.  Each round was reviewed
against the frozen Route-A records, derivation packages, result tables, and the
same-object/Route-B lock before edits were accepted.

## Round 1 — independent review

**Recommendation:** major revision before external sharing.

### Verified strengths

- The manuscript reports all six candidates on separate rows and never combines
  C05's arithmetic clock with C04's determinant.
- All Route-B flags remain locked, and cross-family ideas remain confined to
  the `ROUND2_CLUE` ledger.
- The quoted numerical counts agree with the frozen machine artifacts.
- The central conclusion is scoped to the audited candidates and theorem
  classes rather than symbolic dynamics as a whole.

### Required corrections

1. Define the completed Riemann target and state precisely what equality up to
   a zero-free entire factor means.
2. Make C03--C06 self-contained enough that their object, grammar, clock or
   observable, function space, and determinant status can be audited without
   consulting the repository.
3. Separate cited prior results from the paper's elementary scoped stop rules;
   avoid an unsupported global novelty claim.
4. Clarify that S/P/F are local cell summaries, whereas Route-A eligibility is
   the sequential conjunction A0 through A4 on a single frozen row.
5. Tighten the finite-memory determinant obstruction: state the higher-block
   reduction, nonzero-determinant hypothesis, zero/pole divisor convention,
   and exact finite-product/quotient boundary.
6. Bind the shareable paper to a fresh frozen test run and environment record.
7. Replace the prose-only obstruction summary with a seven-row theorem table.
8. Call the computational check a fresh frozen rerun, not an independent
   replication.
9. Increase the readability of the three-panel numerical figure.
10. Generate a reader-facing candidate table directly from the six evaluator
    records with fail-closed enum handling.

### Implemented actions

- Added the definition
  `xi(s)=s(s-1) pi^{-s/2} Gamma(s/2) zeta(s)/2` and the target convention
  `D_dyn=e^g xi` with entire `g`.
- Expanded the protocol and same-row sequential semantics, and generated the
  candidate matrix with explicit supported/partial/failed enum sets.
- Added the seven scoped obstructions SD-O01--SD-O07 and strengthened their
  hypotheses and proof boundaries.
- Expanded all six source-locked objects, including Mayer's operator domain,
  the wheel tail-space convention, and Knauf's finite-layer recursion.
- Rechecked Knauf's convergence statement against the primary source and kept
  the finite `k=22` prefix as a computational observation only.
- Added Bowen--Lanford and the 2013 Knauf source, with explicit attribution.
- Reworked Figure 2 to a page-readable two-row layout and added redundant
  text/color encodings to Figure 1.
- Added `TEST_REPORT.md`: 29 tests passed in the frozen environment.
- Added `Q_0=1` and the wheel base case so the level-zero tail component is
  defined explicitly.

### Round-1 artifact

- PDF: `main_round1.pdf` (19 pages)
- SHA-256: `f16cdd9c880a2fa3e17afa219b012ff9836ad9feee6f26eb5038a077552c336e`
- LaTeX warnings, undefined references/citations, overfull boxes, and underfull
  boxes: zero in the release build.

## Round 2 — independent verification

**Recommendation:** ready for external sharing as a scoped negative-result
preprint.

### Full review

The second reviewer re-read the modular LaTeX source, all six frozen Route-A
YAML records, the frozen JSON/CSV summaries used by the manuscript, the
Route-B lock, the obstruction and operator-obligation registries, and the
Session-4 scope rules.  The compiled PDF was also inspected at both page and
figure scale.

**Overall score: 8/10.**  The paper is mathematically careful and unusually
transparent about negative evidence.  Its strongest contributions are the
same-object discipline, the finite-memory divisor obstruction, the exact
periodic-collapse and acyclicity arguments, and the separation of theorem,
finite certificate, floating observation, modeling choice, and open problem.

**Critical issues:** none.  No source or artifact supports a change to the
scientific conclusion.  In particular:

- the finite-memory Jensen argument is valid for the stated positive,
  finite-range roof class and nonzero finite exponential determinants;
- the squarefree, renewal, unary-language, finite-twist, and wheel arguments
  retain their stated escape boundaries;
- the Mayer operator is used only as a source-supported A1--A2 success for
  its own modular species;
- Knauf's unsigned limit is confined to the proved half-plane, while the
  depth-22 prefix and signed behavior remain explicitly finite/open;
- every quoted count and error agrees with the frozen evaluator records and
  machine artifacts;
- no Riemann-zero fitting, row-wise coordinate assembly, Route-B invocation,
  or development of a cross-family `ROUND2_CLUE` appears in the paper.

**Major issues:** none remaining after Round 1.

**Minor issues requiring correction:**

1. A prose reference to ``Table 1'' pointed to the obstruction table rather
   than the generated candidate matrix.
2. The Bowen--Lanford BibTeX name suffix rendered in the wrong order.
3. The abstract and obstruction table could expose the positive-roof and
   finite-range hypotheses more literally.
4. The Mayer paragraph named $A_\infty(D)$ without defining the source
   disc and norm.
5. One section-overview sentence had singular agreement with a plural
   cross-reference.

**Remaining limitations:** the literature search is not a theorem of
exhaustiveness; the six candidates are a deliberately broad but finite
screen; and this is a 19-page research report rather than a venue-formatted
short submission.  These limitations are already stated and do not weaken
the scoped result.

### Fixes implemented

- Replaced the literal table number with
  `\Cref{tab:candidate-matrix}`.
- Corrected the Bowen--Lanford BibTeX suffix representation.
- Made the positive finite-range roof, finite-range weight, and fixed
  finite-dimensional cocycle boundary explicit in the abstract/table.
- Defined $D=\{z:|z-1|<3/2\}$, the boundary-continuous holomorphic Banach
  space $A_\infty(D)$, its supremum norm, and nuclearity of order zero.
- Corrected the section-overview agreement.

### Final validation

- `main_round0_original.pdf` preserves the pre-review baseline.
- `main_round1.pdf` preserves the Round-1 revision byte-for-byte.
- `main_round2.pdf` is the final Round-2 artifact and is byte-identical to
  `main.pdf`.
- Final PDF: 19 pages; all fonts embedded.
- Final SHA-256:
  `c2d87b185088e75e0cde7c7f2085ebd59a6fb1de97d0db9db1c7d1d68ab9520c`.
- LaTeX errors, warnings, undefined references/citations, overfull boxes, and
  underfull boxes: zero.

## Score progression

| Round | Score | Verdict |
|---|---:|---|
| Round 0 | 5/10 | coherent baseline; major self-containedness and scope repairs needed |
| Round 1 | 7/10 | strong release candidate; independent verification still pending |
| Round 2 | 8/10 | ready for scoped external sharing |
