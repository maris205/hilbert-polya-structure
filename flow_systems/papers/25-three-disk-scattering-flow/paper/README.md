# Paper 25 manuscript status

Date: **2026-08-28**

Current pipeline state: **ARS Stage 2 draft complete; Stage 2.5 awaiting user
confirmation.** Stage 2.5 has not been passed or claimed.

## Stage 2 deliverables

- manuscript.tex — complete English manuscript with an independent
  Traditional-Chinese abstract.
- references.bib — eight verified and fully cited primary sources,
  natbib/plainnat numeric style.
- paper.pdf — 12-page LuaLaTeX/BibTeX build.
- stage2_manuscript_audit.md — integrity, citation, claim, structure, test, and
  reproducibility audit.

The post-review root Round-9 audit counts **4,055 English body words**, eight bibliography
entries, eight cited keys, no missing or orphan references, and all required
manuscript/declaration surfaces.

## Paper-level result

Title: **Why a Unit-Roof Symbolic Determinant Does Not Transfer to the Physical
Three-Disk Flow**

For equal disks of radius \(a\) and equilateral center spacing \(d\), the paper
proves the exact physical mean roofs
\[
T_2/2=d-2a,\qquad T_3/3=d-\sqrt3a.
\]
Their positive gap \((2-\sqrt3)a\) proves that the physical roof is not
cohomologous to a constant, excludes every owner- and repetition-preserving
scalar transfer \(z=e^{-cs}\), and gives a minimax mean-error lower bound of
\((2-\sqrt3)a/2\).

The locked replay contains 2,241 physical-orbit rows: 747 at each of
\(d/a=29/5,6,31/5\). Per geometry, the period-two-derived constant matches
three period-two owners and disagrees with 744 other owners. The paper also
proves the exact \(q\)-symbol no-repeat unit-roof determinant family and the
universal two-dimensional hyperbolic half-density factorization.

## Claim boundary

The positive symbolic A1/A2 results belong only to the typed unit-roof
symbolic object. They do not transfer to the physical flight-length flow. The
symbolic tuple remains
\((A0_{\rm fail},A1_{\rm pass\ analytic},A2_{\rm analytic\ determinant},
A3_{\rm fail},A4_{\rm fail})\), overall Route-A rejected.

The physical flow remains unassigned. The manuscript does not claim a
nonconstant-roof physical determinant, equality with the exact quantum
multiple-scattering determinant, an arithmetic source, a resonance/prime/zero
fit, or a spectral realization. Route B was not run and is not invocable.

## Verification

- Full historical unit suite: **65/65 passed**.
- Round-8 verify-only reproducer: **12/12 passed**; existing artifacts
  verified.
- Final PDF build: clean LuaLaTeX, BibTeX, LuaLaTeX, LuaLaTeX chain.
- No Python cache files remain.

Earlier Stage-1 research development remains documented in the Round-5,
Round-7, and Round-8 research spines and the notes, results, experiments, and
code directories. The manuscript supersedes the former not-started status
without altering frozen evidence.
