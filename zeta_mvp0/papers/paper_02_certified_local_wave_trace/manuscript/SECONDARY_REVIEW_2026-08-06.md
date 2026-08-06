# Paper 02 secondary review record

Review date: 2026-08-06 UTC  
Mode: independent secondary-agent, read-only, release-blocking review  
External review-model score: not available and not invented

## First disposition: REVISE

No critical error, fabricated result, citation mismatch, or Hilbert--Pólya
claim inflation was found.  Two major issues blocked release.

1. The whole-shell globalization argument needed an explicit reason that a
   phase-aligned primitive orbit close to the fast harmonic circle crosses a
   sufficiently small oriented local section exactly once per circuit.  A
   primitive orbit can otherwise cross a section more than once.
2. The finite-time CRR lemma incorrectly called flow fixed points on a
   periodic orbit isolated.  The geometric periodic orbits are discrete
   modulo time translation; the corresponding fixed component is the clean
   one-dimensional flow orbit, with nondegeneracy in transverse directions.

Minor issues were visible `qquad`/`pm` LaTeX errors, four malformed BibTeX
accents, three incomplete certificate paths, and an attribution that did not
separate the role of the published Wang (2026) paper from the later Hénon
preprint.

## Repairs

- Added a `Unique oriented local crossing` lemma to Appendix D and the A4.8
  proof record.  The proof uses the simple event zero at the positive turning
  point, a uniform negative event slope, endpoint sign preservation under
  bounded-time C1 convergence, and separation of the complementary compact
  orbit arc from the local section.
- Rephrased the CRR finite-time gate using geometric periodic-orbit
  discreteness modulo the flow direction, transverse nondegeneracy, and clean
  one-dimensional fixed components.
- Corrected all listed typesetting, bibliography, path, and attribution
  issues.
- Rebuilt the manuscript from a clean auxiliary state.

## Final disposition: ACCEPT

The same reviewer confirmed that both major issues were closed.  The revised
PDF has 31 pages, 33 cited and 33 present bibliography keys, no undefined
references or citations, and no recurrence of the visible text errors.

The review also reconfirmed the manuscript's non-promotion boundary:

- A4.9 has a positive but nonquantitative trace threshold;
- A4.12--A4.13 prove only the frozen local-box branch and its determinant
  gap on the explicit epsilon interval;
- R401-SC at delta 0.01 is a diagnostic;
- no rational-prime trace, zeta-zero spectrum, Hilbert--Pólya theorem, or RH
  claim is licensed.
