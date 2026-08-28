# Final QA — P91

Final decision: **internal GO / external HOLD**.
Audit completed: 2026-08-28 UTC.

## Mathematical QA

- [x] Semidirect multiplication, inverse, and both conjugation signs
  rederived.
- [x] Directed source/target convention fixed and compared entrywise.
- [x] Strong connectivity, identity loop, mixing, and unique MME justified.
- [x] Zero, `t`, and quotient invariant spaces exhaust dimension `2N`.
- [x] Cubic factor, repeated eigenvalue, zero multiplicity, and rank checked.
- [x] Full-shift endpoint `N=t`, including `N=t=1`, handled separately.
- [x] Zeta signs checked against `det(I-zM)`.
- [x] `F_1`, `F_2`, admissible-root uniqueness, and explicit reverse graph
  isomorphism rederived.
- [x] Rigidity statement remains restricted to the named family.

## Reproducibility QA

- [x] `python3 code/verify_reverser_shift.py` passes **12,175 exact
  assertions** on 20 finite-abelian presentations.
- [x] Literal group-law and closed canonical-matrix paths are independent.
- [x] Rank uses exact rational elimination; spectra/zeta use exact SymPy
  polynomials; no random sampling or numerical tolerance occurs.
- [x] Four-stage LaTeX/BibTeX build succeeds.
- [x] No undefined citation/reference, rerun request, box warning, or other
  LaTeX/package warning remains in `main.log`/`main.blg`.
- [x] All fonts are embedded and subsetted.
- [x] PDF text extraction contains the anonymous Stage 2 marker, scope hold,
  and complete references.
- [x] All four A4 pages were rendered and visually inspected; no clipping,
  collision, missing glyph, or stranded heading was found.

## Artifact QA

- `main.pdf`: 4 pages, 296,997 bytes, PDF 1.5.
- SHA-256:
  `196160eff81a974c496e0259ca15f73e9b8fcf6a7838cf5afef193ef0c5c6df6`.
- `SHA256SUMS` covers the manuscript, bibliography, exact control, audit
  documents, README/build record, and PDF.

## Release gate

The proofs and registered controls support internal use. External release is
held because the owner scan was bounded and the construction combines mature
group-theoretic and SFT components. A broader terminology/citation audit and
human author review are required before posting, submission, or priority
language.
