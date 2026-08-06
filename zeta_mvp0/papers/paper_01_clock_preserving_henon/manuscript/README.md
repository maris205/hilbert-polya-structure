# Paper 7 analytic-v3

This directory is the separately versioned analytic upgrade of Paper 7.  It
does not overwrite the immutable baseline in `../paper/`.

## Final manuscript

- `paper7_analytic_v3_round2_final.pdf` — accepted two-round final artifact
- `main.tex` — manuscript entry point
- `sections/appendix_analytic_activity.tex` — complete strict ground-state
  and uniform relative-heat proofs
- `MANUSCRIPT_STATUS_ANALYTIC_V3.md` — final result and verification summary
- `ANALYTIC_V3_IMPROVEMENT_LOG.md` — version-by-version change ledger
- `reviews/ANALYTIC_V3_ROUND1_REVIEW.md` and
  `reviews/ANALYTIC_V3_ROUND2_REVIEW.md` — independent review records
- `CITATION_AUDIT_ANALYTIC_V3.md` — theorem-specific and prior-work citation
  provenance

Final PDF SHA-256:

```text
e961e1b65963b2b769d7454e27913bbfa57c60d9e46849b4c8f5834a900ab0ff
```

## Build and regression

From this directory:

```bash
./compile_paper.sh
```

From the project root:

```bash
pytest -q
```

The frozen final regression is 58 passing tests, 45 PDF pages, 77 BibTeX
entries/67 printed references, zero unresolved citation or cross-reference,
zero overfull box, and fully embedded fonts.

## Claim boundary

The strict ground-state and relative heat theorems cover only the centered
one-step, nonmagnetic scalar family for fixed \(a>-1\), \(a\ne0\), and fixed
\(\hbar>0\).  They are nonisospectrality certificates, not a prime-power
trace, zeta-zero identification, or RH claim.
