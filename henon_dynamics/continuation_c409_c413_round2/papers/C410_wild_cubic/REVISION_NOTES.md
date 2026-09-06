# Precision revision after independent manuscript review

Date: 2026-09-06 (UTC). The complete non-author report
`../../nonlinear_geometry/REVIEW_C410_MANUSCRIPT.md` was read before this
revision. It found no blocking mathematical or source-boundary issue and
offered two optional presentation clarifications. The coordinator selected
the normal-form clarification for implementation before final source freeze.

In the proof of Lemma 3.1, the distinctness of the three displayed roots is
now checked directly: `beta != 0` gives `z not in F_3`, and the pairwise
differences are `a(z+1)`, `a(1-z)` and `az`, all nonzero. This replaces the
compressed inference from separability alone, which did not by itself
exclude duplicate entries in the displayed list. The field generators,
radical equations, discriminant, theorem statements and every invariant are
unchanged. No extra constant-field assumption or square root of `a` is used.

The optional descent parenthetical was not added: the reviewed tensor and
separability argument is already complete, and the coordinator requested
only the normal-form precision edit. No frozen proof/source file or old
experiment was changed or rerun.

The original non-author reviewer is asked to check this affected paragraph
and append an actual confirmation to the existing review. This note does
not pre-claim that confirmation. The existing author PDF predates this
source-only precision revision; the coordinator's final fresh builds and
all-page visual QA must use the revised source. No new author-side build is
claimed by this note.
