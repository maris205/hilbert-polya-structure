# Actual revisions after independent full-manuscript review

Date: 2026-09-06. Review input read completely:
../../positive_characteristic/REVIEW_C409_MANUSCRIPT.md.
That review inspected the actual seven-section manuscript, bibliography and
11-page PDF text. It found no counterexample or unresolved mathematical
proof gap and requested two narrow repairs.

## R1 — exact no-wild realizability locators

The first draft attributed c-integrality and rationality of r_n and p^{s}
to BCH Proposition 10.2.1 alone. The new §5.1 now separately cites
Proposition 10.2.1 for c and Proposition 10.2.2 for the rational values,
and states why the latter's integral-wild assumption holds when t=0.
CITATION_METADATA.md records the corrected locators and the author's
fresh direct reading of both propositions and proofs in BCH v2 pp. 97–99.
The frozen historical proof/source files have not been altered.

In the same deduction, the harmless empty-prime-set edge case mentioned
in the review is now explicit: g is already periodic, so the increasing
sequence of nonempty-S moduli is not needed in that case. This is a
clarification of the same deduction, not an added theorem.

## R2 — supported-conductor quantifier

The introduction's phrase “at each sufficiently high conductor” has been
replaced by “along an unbounded sequence of conductors in the nonzero
Fourier support”. This matches Lemmas 4.1–4.2 exactly. No stronger conductor
statement has been added; the full grids at supported conductors suffice
for density.

## Scope and next gate

Only the new C409 introduction, no-wild paragraph, citation metadata and
this revision/build record were edited. The theorem, its Fourier and
natural-boundary proofs, the example and the seven bibliography entries
are unchanged. No old experiment or finite check was rerun.

The changed draft was rebuilt successfully with zero remaining log warnings.
The same non-author reviewer then checked the actual affected passages,
provenance and rebuilt PDF text and appended a confirmation to the original
review receipt. Both requested repairs and the empty-S clarification passed.
This is a targeted follow-up, not a second full review or final
deterministic-build QA; the latter release checks remain separate.
