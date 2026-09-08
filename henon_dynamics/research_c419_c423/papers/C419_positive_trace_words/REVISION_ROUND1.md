# C419 first manuscript-review response

2026-09-08 UTC. The coordinator read all 399 lines of the
[first full-manuscript review](../../manuscript_reviews/round1/C419_REVIEW.md),
SHA256 52a775d5cbfa00d282682a877a4c76ed0b464a0e9748cd44824963a08e8d50e6.
The review is PASS with zero mandatory findings. All three optional items
are adopted as presentation/precision improvements, not repaired false claims.

| Item | Actual edit | Scope |
| --- | --- | --- |
| O1 | A local samepage group keeps equation 4.2 with its predicate and proof conclusion. | No changed equation or proof. Table 3 can still float above the paragraph, but no longer separates equation 4.2 from its conclusion. |
| O2 | Lemma 5.1 now says “are pairwise disjoint above four”. | Makes the already proved pairwise assertion unambiguous. |
| O3 | Section 8 names Humphries–Manning (2015) and the title Curves of period two points for trace maps. | Uses metadata already verified in the original full source audit, lines 114–129. Its unread theorem list is still not excluded. No fresh body access or new theorem import. |

Only sections/4_locus.tex, sections/5_levels.tex and sections/8_scope.tex
changed. Their hashes are respectively:

    30846f2d9d58627b715537c5702d04c958aa798b51ce332a2995fa0c61056cd6
    931591e142cfecf5de455749ece415985abbb69c78293c49d88ad688cf906acc
    a36f96984547cdfe8779ef117b98718e1eef42104c809cf86f8e3ecf4a805b6c

All fourteen pre-review production files were preserved in
snapshots/author_polished/ before editing; all fourteen revised inputs
are in snapshots/round1/. Earlier baseline snapshots and PDFs remain intact.

One actual fresh-directory build used:

    env SOURCE_DATE_EPOCH=1788825600 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=builds/round1 main.tex

It exited 0 after normal BibTeX/LaTeX convergence. The actual
[revised PDF](builds/round1/main.pdf) has 11 pages, 346150 bytes, SHA256
eaeee202c03e9b25c67a53c98199027297f96fe64baf670f235a249d5a41215d.
Final main.log/main.blg scans found no warning, overfull, underfull,
undefined or error matches (rg exit 1 means no match). Pages 6–7 were
newly extracted, rendered at 100 dpi and visually inspected: equation 4.2
and its complete conclusion now appear together on page 7. The revised
Section 8 text on page 10 was read; its continuation and all final pages
remain part of the final release inspection, not preclaimed here.

No mathematical program, primary-source request or Git mutation was made
for these changes. This genuine revision is now the input to the second
nonauthor full-manuscript pass. Final identical-input builds, all-final-page
checks, evaluation and sealing remain distinct gates.
