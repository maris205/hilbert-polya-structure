# Pre-Review Citation and Data Integrity Summary

This focused report is superseded by the complete gate in
`paper/INTEGRITY_PRE_REVIEW.md`; it is retained as the requested
citation/data checkpoint.

## Snapshot

- Manuscript: `paper/manuscript.tex`
- SHA-256: `f0923046d4af14dc4373f4698781770bd3545f1a28a5c08d15558421c2903f4a`
- Citation audit: `notes/CITATION_VERIFICATION.md`
- Raw-data manifest: `results/final_result_manifest.json`

## Verdicts

- **Citations: PASS.** Thirteen bibliography keys are all used; 21
  citation-key occurrences have no missing, ghost, or unused entry.  Every
  context stays within the safe claim recorded in the citation audit.  The
  inherited Logistic parameter/motivation is now attributed to
  `wang2026prime`, while its prime-sieve claims and data are explicitly not
  reused.
- **Data: PASS WITH ONE NON-BLOCKING GRANULARITY ADVISORY.** Every numerical
  result in the manuscript resolves to a frozen artifact and all manifest
  hashes match.  The dyadic value 747 is predeclared in the source lock and
  asserted by a named passing test, while the raw preflight JSON stores only
  `dyadic_ledger_total=true`.
- **Figures: PASS WITH ADVISORIES.** All three figures have complete traces
  and one substantive manuscript reference each.  The unused fallback
  `figures/latex_includes.tex` retains stale Figure 3 wording, but the current
  manuscript caption is correct and does not input that file.
- **Originality: CLEAR WITH METHOD LIMITS.** Twenty-four of 54 substantive
  prose paragraphs were sampled (44.4%), and the full local duplicate scan
  found no substantial unattributed overlap with the archived Wang article or
  other prior manuscripts.
- **Build: PASS.** A clean isolated LaTeX/BibTeX build produced 16 pages with
  no unresolved citation/reference or duplicate label.

For the full evidence table, seven-mode assessment, experiment passport,
figure package, limitations, and resubmission triggers, use
`paper/INTEGRITY_PRE_REVIEW.md`.
