# C412 complete draft and author-side check

2026-09-06. Status: `COMPLETE_DRAFT_READY_FOR_NONAUTHOR_MANUSCRIPT_REVIEW`.
This is an author report, not peer review, independent manuscript review,
a final reproducible-build receipt, or a Route-A evaluation.

## Manuscript delivered

- [Complete English LaTeX article](main.tex), with nine included section
  files: abstract, seven numbered sections, and Appendix A.
- [Actual author-build PDF](author_build/main.pdf): **14 pages**,
  **367,848 bytes**.
- [Frozen-contract paper plan](PAPER_PLAN.md).
- [Verified citation metadata and access boundaries](CITATION_AUDIT.md),
  with five actually cited entries in [references.bib](references.bib).
- [Final author-build log](author_build/main.log).

The theorem covers every integral pair `(a,b)` in
`H_{a,b}(x,y)=(y,y^2+by+a-x)`, starting from rational periodic points and
proving their integrality. It includes both parity tables, the integer
translation and coordinate back-translation, all exact-period and
degeneracy checks, both infinite-parameter six-symbol reductions, the
complete common six-case local proof, and all parameter overlaps.
The eight-point equality locus is explicit in the abstract, main theorem,
and final proof: `b=2q+1`, `a-q^2+q=-4`.

Section 5 specifies exact alphabets, maps, set pruning, word expansion,
and pseudocode. Appendix A prints **all thirteen even and all seventeen
odd finite-complement rows**, including every stabilization cardinality
and every cycle word. It also specifies the independent full-box
transitive-closure method. The article does not substitute a working-tree
proof link or a total-count comparison for those certificates.

The ordinary-time return law is a corollary of the finite rational
periodic set. Neither it nor the classification is described as a
target Euler-product, root-number, zero-correspondence, automorphy, or
Hilbert–Pólya result. Monicity, integral coefficients, and Jacobian `+1`
remain explicit. Source comparisons retain the unread Silverman 1994
subscription-text limitation and do not assert global priority.

## Accepted proof inputs reused without rerunning

The complete author read of the two proofs and the root review preceded
drafting. Their existing receipts are inputs, not new manuscript checks:

- [Even proof](../../../research_c409_c413/nonlinear_geometry/PROOF_INTEGER_HENON.md).
- [Odd addendum](../../../research_c409_c413/nonlinear_geometry/ADDENDUM_INTEGER_HENON_ODD.md).
- [Root proof/source review and independent full-set receipts](../../../research_c409_c413/REVIEW_INTEGER_HENON_ROOT.md).

The sealed 48-file tree was neither edited nor re-tested. Its outdated
draft-side pending labels remain untouched. The paper transcribes the
accepted mathematics into complete prose; it does not claim that the
old proof review already reviewed this new manuscript.

## Actual author compilation

Run from this paper directory:

```text
env SOURCE_DATE_EPOCH=1788652800 FORCE_SOURCE_DATE=1 latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=author_build main.tex
```

Actual environment: Latexmk 4.76; pdfTeX
`3.141592653-2.6-1.40.22` (TeX Live 2022/dev/Debian); LaTeX2e
`2021-11-15` patch level 1; BibTeX 0.99d; installed `plainnat.bst`.
Class is anonymous 11pt `article`, with one-inch margins. No conference
style or page-count quota was imposed.

The first completed compilation exited 0 and exposed duplicate PDF
destinations after resetting the appendix table counter. Setting a
distinct appendix `theHtable` fixed both destinations. The only other
source clarification in that pass was to state the finite-pruning lemma
directly for the periodic set in `X`, removing an unnecessary qualifier.
The second compilation exited 0. Its final log has no LaTeX/package/PDF
warnings, no overfull or underfull boxes, and no undefined references or
citations. Initial multi-pass cross-reference warnings resolved normally.

A text-extraction attempt made before that second build had completed
reported an incomplete PDF trailer; repeating the extraction after the
process exited succeeded. No persistent PDF error remained. The final
PDF was not modified after the completed compilation.

Final author PDF SHA-256:

```text
4974c90cd98a0529d00baf16a47b789fdba3ac37d9be432d2e8a2c3e6a8f7659
```

Final author log SHA-256:

```text
99cf923a1017a3c30db1c90b3d6226df19e7c4b709126e93de45ec5f1863f19d
```

These hashes identify this author-build artifact; they are not a new
package manifest or a substitute for mathematical correctness.

## Text, structure, and limited visual checks

Actual read-only checks on the new manuscript found:

- 55 unique labels and 48 distinct referenced labels; no missing reference
  or duplicate label.
- Five cited keys and five bibliography entries; no missing or unused
  bibliography entry.
- All nine section files are included by `main.tex`; no orphan section.
- No `TODO`, `FIXME`, `XXX`, `[VERIFY]`, undefined-reference `??`, or
  undefined-citation `[?]` marker in the checked source/PDF text.
- All 21 font records reported by `pdffonts` have `emb=yes`.
- The eight local Markdown links in the plan and citation audit resolve.

The reverse-outline pass followed the actual paragraph openings through
the complete parameter statement, coefficient reductions, lattice bounds,
local symbol proof, finite closure, sharp count, and return corollary.
No evidence-free contribution or unrelated experimental section was
added. The tables were compared against the accepted word/range/degeneracy
statements while transcribing, without executing the old checkers.

The author rendered and inspected PDF pages **2 and 13** at 100 dpi,
covering both main classification tables and both finite-complement
tables. Their text, formulas, row labels, and captions are readable and
unclipped. These two page images remain in `author_build/`. This is
explicitly a limited author layout check, **not** the final all-page
visual QA. Text on pages 1–3 and 12–14 was additionally extracted and
read, including the bibliography and scope statements.

## Handoff and remaining gates

The complete draft is ready for the assigned non-author to read the actual
article, citations, and proof provenance. No required mathematical or
typesetting issue is known from this author check. Non-author manuscript
review, any review-driven revision, root's two fresh-directory final
builds and byte comparison, full final-page visual QA, formal evaluations,
release sealing, global records, and Git remain with their assigned
owners. No external manuscript upload or publication was performed.

Only this C412 directory was written. A scoped Git status showed this new
directory untracked and no change in the sealed research tree; no Git
write operation was run.
