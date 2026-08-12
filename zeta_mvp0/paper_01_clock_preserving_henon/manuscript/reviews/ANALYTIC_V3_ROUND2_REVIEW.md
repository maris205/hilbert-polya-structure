# Analytic-v3 Round-2 closure review

Date: 2026-08-06

No external-review score is reported.  The configured external Codex-MCP
endpoint was unavailable, so the same three independent read-only subagents
performed focused closure audits after the Round-1 revisions.

## Final verdicts

| Audit | Final verdict | Closure evidence |
|---|---|---|
| Strict ground-state theorem and relative-container references | **ACCEPT** | All Round-1 proof clarifications remain present.  Moving Proposition 8.1 did not alter its statement or Appendix A.6.  A final `\FloatBarrier` places Table 5 before the proposition instead of between its enumerated items. |
| Relative heat theorem and analytic figure | **ACCEPT** | Theorem 5.2, the appendix, Section 8, abstract, conclusion, and figure agree in sign and every coefficient.  Seven plotted residuals agree with an independent 60-digit calculation to maximum absolute error \(1.25\times10^{-14}\). |
| Scope, citation, notation, and PDF drift | **ACCEPT** | All nine editorial items closed.  The audit additionally detected and corrected a file-level mismatch between the cited 17-page H\'enon manuscript and a different 21-page Zenodo expansion. |

## Citation-integrity closure

The cited manuscript

> *An Area-Preserving H\'enon-Map Model for the Riemann Zeros: A
> Deterministic-Dynamics Approach with Quantum and Dissipative Solvers*

is the 17-page PDF at fixed public Git commit
`f86bf21a32ad5bcb21ba81d312cc68e91bcc7db0`.  Its repository and local
copies share SHA-256
`23dad812162728316f633081e1a1995d4c00614a70d0f5877d425c68d0c726b9`.

Zenodo record `10.5281/zenodo.19084735` contains a different 21-page expanded
manuscript, SHA-256
`a414cef5072126a67ff6b9089b19c00536ad31168e31b32095493ade36d0a46b`.
The final BibTeX therefore contains no Zenodo DOI for the cited 17-page item;
it points only to the fixed-commit PDF.  Both citation audits record the
distinction.

## Final build and regression

- Final artifact: `paper7_analytic_v3_round2_final.pdf`
- Pages: 45
- SHA-256:
  `e961e1b65963b2b769d7454e27913bbfa57c60d9e46849b4c8f5834a900ab0ff`
- Tests: 58 passed
- BibTeX database / printed references: 77 / 67
- Undefined citations or references: 0
- Rerun warnings: 0
- Overfull boxes: 0
- Nonfatal underfull boxes: 22
- Fonts: all embedded and subsetted

The immutable Round-2 baseline remains byte-for-byte unchanged at SHA-256
`8ad75ae285244bef380d6474b7e1a4ecb943b6fe96d03fa99c9efd44192a3339`.

## Accepted claim boundary

The final manuscript proves strict ground-state ordering and uniform
short-time relative heat activity only for the centered one-step scalar,
nonmagnetic subfamily at fixed \(a>-1\), \(a\ne0\), and fixed
\(\hbar>0\).  It does not extend those theorems to magnetic fields, higher
H\'enon iterates, varying \(\hbar(t)\), individual higher-eigenvalue
ordering, an all-time heat ordering, a prime-power trace, zeta-zero
identification, or RH.
