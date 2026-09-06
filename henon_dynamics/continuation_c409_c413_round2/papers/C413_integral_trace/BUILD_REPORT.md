# C413 author build and manuscript handoff

2026-09-06. Status: `FULL_MANUSCRIPT_WRITTEN_INITIAL_BUILD_PASS`.
This is not the final two-directory release receipt. A non-author must
still review the actual manuscript, and every final page must be inspected.

## Inputs and initial build

The manuscript has `main.tex`, six included `sections/*.tex`, and five
actually cited verified bibliography entries. Its argument is self-contained;
the [proof package](../../nonlinear_geometry/PROOF_PACKAGE.md),
[independent proof review](../../REVIEW_TRACE_ROOT.md), and
[exact verification record](../../nonlinear_geometry/VERIFICATION.md) are
provenance, not substitutes for omitted proof steps.

Actual command in this paper directory:

```text
env SOURCE_DATE_EPOCH=1788652800 FORCE_SOURCE_DATE=1 latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Actual environment: latexmk 4.76; pdfTeX 3.141592653-2.6-1.40.22,
TeX Live 2022/dev/Debian; BibTeX 0.99d. All prerequisites were found locally.
One latexmk invocation finished with exit 0, including its normal multi-pass
reference resolution. There was no TeX compilation error or corrective
error loop. Intermediate first-pass undefined references disappeared in
the final log.

Initial PDF: 10 pages, 352730 bytes, letter size, anonymous metadata.
Initial SHA256:
`9f7d55c1484714b51d148b9aa65c05ca3230495aa354d8b680b9d6334af4fc52`.
The conclusion ends on page 9; references occupy page 10. No venue or
page limit has been selected. All 21 font entries reported by `pdffonts`
are embedded Type 1 fonts, with no Type 3 entries.
The final `main.log` and `main.blg` contain no `Warning`, `Overfull`,
`Underfull`, `undefined`, or `Missing` match (rg exit 1 = no matches).
The author read extracted text over pages 1–10; this is not visual QA.

After that initial build, two prose clarifications were made before
non-author handoff: the two-column itinerary table is traversed by its
numeric index, and whole-group finiteness explicitly implies single-map
periodicity but not conversely. The misleading compact-level wording was
removed. These edits do not change any equation or proof hypothesis.
The initial hash above identifies the pre-clarification PDF only; the
final build receipt will identify the reviewed, rebuilt PDF separately.

## Reverse outline and claim coverage

1. The introduction states the all-lattice theorem, complete orbit table,
   exact level consequence, and credited classical families/escape theory.
2. Scalar words and the twelve-triple table prove existence, least periods,
   endpoint `m=1`, heights, levels, and disjointness.
3. Every maximum case is resolved: modulus-two equality, both zeros,
   exactly one zero, all four nonzero signed cases, and the full unit cube.
4. The discrete-bijection lemma proves proper escape; all-level orbit,
   fixed-point and zeta formulas are derived; positive factorization proves
   that square and quadratic supports intersect only at four.
5. The rational 2-cycle and whole-group counterboundary prevent domain
   inflation. The finite diagnostics have exact scope. The final paragraph
   excludes target arithmetic/zero and Hilbert–Pólya conclusions.

No new experiments were run while writing. Unchanged supplementary checks
retain their original receipts, and the theorem does not depend on them.
Internal manuscript review, affected repairs, final fresh builds, all-page
visual QA, and the final release hash remain separate unfinished gates.
