# Manuscript revisions

Round zero closes the full bounded coding. Round one adds variable-matrix
hyperbolicity, the complete primitive atlas and reversal. Round two adds
separate generating conventions, the exact arithmetic exclusion and audits.
These are three substantive versions of one paper, not three papers.

An internal author-swapped proof review checked bounded exhaustion, forward
and backward cone indexing, the negative-multiplier flat bound and rational
clock rescaling. It found no blocking proof issue. A symbolic test initially
used structural expression equality instead of simplifying the difference;
that test was corrected and rerun, not reframed as a mathematical finding.

The root reviewer then actually viewed all four final PDF pages; the receipt
is in paper/COMPILE_REPORT.md. Proof review, independent cyclic-system
recomputation and visual review have different purposes and are not counted
as independent human peer reviews.

The final read-only audit then reproduced a standalone-checker coercion bug:
false scope/Route-B values could be replaced by integer zero with a repaired
payload hash. The release source gate was stricter already, but this did not
excuse the independent checker. Two explicit boolean guards and two hostile
regression cases were added; the actual lane passed 36/36. The final paper's
audit count and correction receipt were updated and its PDF rebuilt. No
mathematical statement or frozen evidence value changed.
