# Paper 24 manuscript status

Date: **2026-08-28**

Current pipeline state: **ARS Stage 2 draft complete; Stage 2.5 awaiting user
confirmation.** Stage 2.5 has not been passed or claimed.

## Stage 2 deliverables

- manuscript.tex — complete English manuscript with an independent
  Traditional-Chinese abstract.
- references.bib — seven verified and fully cited primary/authoritative
  sources, natbib/plainnat numeric style.
- paper.pdf — 12-page LuaLaTeX/BibTeX build.
- stage2_manuscript_audit.md — integrity, citation, claim, structure, test, and
  reproducibility audit.

The post-review root Round-9 audit counts **4,029 English body words**, seven bibliography
entries, seven cited keys, no missing or orphan references, and all required
manuscript/declaration surfaces.

## Paper-level result

Title: **Congruence Trace Universality and the Limits of First-Jet Separation
in Bianchi Holonomy**

The paper proves, for a commutative ring \(R\), a non-zero-divisor \(m\), and
\(\gamma=I+mA\in\mathrm{SL}_2(R)\),
\[
\frac{\operatorname{tr}(\gamma)^2-4}{m^2}
=m^2\det(A)^2-4\det(A).
\]
Consequently, Gaussian level-three integrality is universal
principal-congruence algebra rather than a Gaussian-specific owner mechanism.
The paper also proves the level-conjugacy, inversion, and repetition laws of
the first congruence jet.

The exact 11,481-matrix panel has 145 scalar values and 517 joint scalar/jet
descriptors. The jet separates 372 of 11,336 scalar-collision rows, leaves
10,964, reduces the maximum bucket from 505 to 84, and produces no singleton
joint bucket. Four control families supply 6,396 exact witnesses, but cover
only two of the three canonical Route-A control types.

## Claim boundary

The manuscript is a negative-specificity theorem and necessary-refinement
paper. It does not claim a complete group/conjugacy/primitive census, an
orbit-to-prime-ideal map, a metric prefix, a dynamical determinant, a
prime/zero fit, or a spectral realization.

The marked-word proxy remains
\((A0_{\rm weak\ arithmetic\ relation},A1_{\rm weak},A2_{\rm fail},
A3_{\rm fail},A4_{\rm fail})\), overall Route-A exploratory. The complete
Bianchi flow remains unassigned. Route B was not run and is not invocable.

## Verification

- Full historical unit suite: **71/71 passed**.
- Round-8 reproducer: **14/14 passed**; existing artifacts verified.
- Final PDF build: clean LuaLaTeX, BibTeX, LuaLaTeX, LuaLaTeX chain.
- No Python cache files remain.

Earlier Stage-1 research development remains documented in
stage1_research_spine.md and the notes, results, experiments, and code
directories. The manuscript supersedes the former not-started status without
altering those frozen evidence records.
