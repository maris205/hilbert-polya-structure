# P170 — Endpoint histories in a random-permutation fixed-point sieve

**Round:** Round 2 dual-review no-change freeze  
**Gate:** `GREEN_OWNER_THIN_WITH_N3_REPAIR`  
**External lifecycle:** `HOLD_EXTERNAL`

This directory is the self-contained anonymous short note for the finite
random map

```text
A -> A ∩ Fix(pi),       pi uniform in S_n independently at each epoch.
```

The note gives the every-time/every-endpoint history count, the Boolean
containment spectrum, exact absorption transforms with the repaired `n=3`
boundary, and a cycle-marked refinement.  Its retained axis is the complete
endpoint-conditioned marked polynomial together with sharp minimum/maximum
total-cycle degrees and the exact conditional total-cycle expectation.

Common-fixed-point theory, one-permutation fixed-set laws,
inclusion--exclusion, semilattice spectra, standard hitting-time algebra,
and the ordinary symmetric-group cycle polynomial are explicitly assigned
zero contribution credit.  A bounded owner search is only a non-hit.  The
lifecycle is `HOLD_EXTERNAL`.

## Files

- `main.tex`, `references.bib`: anonymous source.
- `main.pdf`: canonical deterministic Round-2 PDF.
- `main_round0_original.pdf`: preserved byte-identical Round-0 copy.
- `main_round1.pdf`: byte-identical no-change post-Review-A copy.
- `main_round2.pdf`: byte-identical final dual-review copy.
- `verify_p170.py`, `verification_output.txt`: standalone author verifier
  and frozen stdout.
- `PAPER_PLAN.md`, `NARRATIVE_REPORT.md`, `CLAIMS_EVIDENCE.md`: theorem and
  evidence spine.
- `SOURCE_VERIFICATION.md`: primary-source owner audit and internal
  collision subtraction.
- `HOSTILE_REVIEW_A.md`, `HOSTILE_REVIEW_B.md`: two independent manuscript
  reviews.
- `IMPROVEMENT_LOG.md`: explicit no-change review closeout.
- `BUILD.md`, `SELF_QA.md`, `SHA256SUMS`: compilation, QA, and final
  integrity ledgers.

## Reproduce the exact checks

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p170.py
```

The author verifier is a single Python-standard-library file.  It imports no
scout, gate, paper, or earlier verifier.  The frozen stdout is
`verification_output.txt`.

## Build

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

See `BUILD.md` for the double source-only cold-build and PDF QA ledger,
`CLAIMS_EVIDENCE.md` for the theorem audit trail, and
`SOURCE_VERIFICATION.md` for primary-source subtraction.

Both hostile reviews returned `ACCEPT_INTERNAL / PROVABLE AS STATED` with
`0 Critical / 0 Major / 0 Minor`.  Review B used an independently written
fixed-set/cycle-polynomial engine and 3,001,398 assertions.  No review
changed the manuscript, bibliography, author verifier, theorem ceiling,
PDF, owner-thin decision, or lifecycle.
