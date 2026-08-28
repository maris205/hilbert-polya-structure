# Final QA — P82

Checkpoint: 2026-08-28 UTC

Disposition: **GO; INTERNAL FREEZE; EXTERNAL HOLD**

## Canonical artifact

- PDF: `main.pdf`
- Pages: **6 A4 pages**
- Size: **336,857 bytes**
- SHA-256: `19e0eb0ec255fe04f18f94eda26c538350ebc50b025afc1033b54fb376c82b25`

## Build gate

- Final build chain: `pdflatex -> bibtex -> pdflatex -> pdflatex`.
- All four stages exited zero.
- Final `main.log` / `main.blg` scan found zero warnings, undefined
  references, undefined citations, overfull boxes, underfull boxes, LaTeX
  errors, emergency stops, or fatal errors.
- All six cited bibliography entries occur in `references.bib`; there are no
  uncited bibliography entries.

## PDF gate

- `pdfinfo` reports six A4 pages, no encryption, no JavaScript, and no suspect
  objects.
- `pdffonts` reports **24/24 font records embedded**, all subsetted and with
  Unicode mappings.
- The text layer contains no `TODO`, `FIXME`, `XXX`, `[VERIFY]`, unresolved
  citation marker, or unresolved reference marker.
- All six rendered pages were inspected.  The title/abstract, local-pair
  table, `8 x 8` matrix, proofs, temporal census table, and bibliography are
  legible and unclipped.

## Mathematical gate

- The local boundary calculation was reverse-read from the literal order
  `A_m` then `B_m`; the three restored coordinates are exactly
  `(b_j,c_j,a_{j+1})`.
- The transfer-matrix state ordering is consistently
  `a+2b+4c = 000,100,010,110,001,101,011,111`.
- The rank-two spectral proof explicitly establishes algebraic multiplicity
  six at zero and derives the remaining sum/product from
  `tr(M)=5`, `tr(M^2)=19`.
- The recurrence starts at `m=3`; no fictitious ring-size-zero fixed count is
  introduced.
- The `m=1` endpoint is included and is compatible with the cyclically shifted
  second layer.

## Space/time and ownership firewall

- `zeta_fr` is defined only for the **spatial three-site block shift on the
  frozen SFT**.
- The paper explicitly states that it does not compute a temporal
  Artin--Mazur zeta function of `T_m`.
- The observed temporal periods through `m=6` are not promoted to an
  unbounded-period theorem, cycle-index formula, or integrability claim.
- The control-on-one convention is explicit, and the text now identifies
  Fredkin--Toffoli's original table specifically as control-on-zero.
- Fredkin--Toffoli, Toffoli--Margolus/Kari, Morita, and the distinct
  Singh--Vasseur--Gopalakrishnan Fredkin staircase are all named in the
  ownership section.
- No absolute novelty or priority claim appears in the paper or package.

## Exact control gate

- Control command: `python3 code/verify_fredkin.py`.
- Status: PASS.
- Exhaustive states: **299,592** for `m=1,...,6`.
- Actual instrumented assertions: **1,878,811**.
- Maximum observed temporal periods: `3,4,8,18,32,74`.
- Complete cycle types and all control categories are recorded in
  `CONTROL_RESULTS.md`.

## Integration boundary

- The package is self-contained under
  `papers/82-shifted-fredkin-frozen-sft/`; batch-level reports and Git state
  are recorded separately under `docs/papers82_86_sequence/`.
- The canonical PDF was rebuilt and rechecked by the integrating pass after
  the independent hostile review.

This QA certifies internal mathematical and build integrity.  It does not
certify absolute novelty and does not authorize external release.
