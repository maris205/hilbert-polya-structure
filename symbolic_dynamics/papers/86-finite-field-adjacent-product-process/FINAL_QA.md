# Final QA

Release audit date: 2026-08-28 UTC.

## Result

- Decision: **GO; INTERNAL FREEZE; EXTERNAL HOLD**
- Exact control: `ALL EXACT CONTROLS PASSED`
- Build: explicit `pdflatex / bibtex / pdflatex / pdflatex` completed
- PDF: `main.pdf`, 7 pages, 318,027 bytes, A4, PDF 1.5
- Undefined references: 0
- Undefined citations: 0
- LaTeX warnings on final pass: 0
- Package warnings on final pass: 0
- Overfull boxes: 0
- Underfull boxes: 0
- Fonts: 23/23 embedded; all are subset fonts
- Source markers: no unresolved TODO, FIXME, XXX, or verification marker
- Bibliography: 5 cited keys and exactly 5 entries
- Visual inspection: all seven pages checked; title, equations, table,
  references, and page furniture render correctly
- SHA-256: `d6444b5f31e2a1f77155280b28bc2b0e857cb9ead34dde1645683f8cba77798e`

## Mathematical release checks

- The support proof handles finite, one-sided, bi-infinite, and all-zero
  runs, and uses field division only at nonzero elements.
- The word recurrence was checked from definition-level image enumeration,
  including the three low-index cases not supplied directly by
  Cayley--Hamilton.
- Infinite Markov order uses positive contexts with a common arbitrarily long
  zero suffix and strictly unequal consecutive predictive ratios.
- The entropy series conditions on the complete past through the last
  nonzero observation; its age weights sum to one and decay exponentially.
- The strict entropy gap uses Parry uniqueness only after proving that the
  support SFT is mixing.
- All-prime-power scope is proved algebraically and is represented in the
  controls by the nonprime field `F_4`.

## Ownership and review scope

The manuscript positively assigns the one-dependent/block-factor,
hidden-Markov entropy, variable-memory, and intrinsic-Markov frameworks to
their primary sources.  The negative
literature statement is explicitly bounded by date and search terms and does
not claim absolute priority.  An independent hostile proof review was
completed after the draft audit; its derivations, corrections, and independent
`F_4` controls are recorded in `HOSTILE_REVIEW.md`.
