# Hostile review — round 1

Date: 2026-08-14

Artifact reviewed: `paper/paper_round0_original.pdf`

Mode: read-only Devil's Advocate / theorem-interface stress test

## Strongest counter-argument

The manuscript proves a clean pressure pole only for the physical summand,
not for the Mahler-weighted amplitude that motivated the project.  A hostile
reader could therefore argue that the paper has merely recovered a standard
suspension-zeta singularity after discarding precisely the nonlocal arithmetic
information that made P53 interesting.  That objection is not fatal if the
paper treats the splitting itself as the result: the physical pole is a
source-backed theorem, the Galois excess is retained as a positive series, and
the remaining bridge is expressed as an exact open condition rather than
silently absorbed into the pressure clock.  The manuscript mostly does this,
but several interfaces need to be made explicit enough that no reader can
mistake a local zeta theorem for a continuation of the full Mahler amplitude.

## Findings

### CRITICAL

None.  The unconditional theorem is correctly scoped to the physical
summand, and the full-pole theorem is explicitly conditional.

### MAJOR

| # | Dimension | Issue | Evidence anchor | Confidence | Required repair |
|---|---|---|---|---|---|
| M1 | Source attachment | The two-parameter Parry--Pollicott normalization is only named, not fully mapped.  A reader must be able to verify the choices of `f,g,c,k`, the equilibrium state, and the denominator in the residue without reverse engineering the source. | equation: Sections 7, equations (7.2)--(7.4) | 5/5, checked against the official Astérisque text | Add the exact source parameter map and state that the conclusion is a local meromorphic germ. |
| M2 | Tail analyticity | The weighted repetition-tail argument says only “boundedness of psi and positivity of the roof.”  It omits the needed comparison between symbolic period and suspension length. | text: Section 7, proof of the conditional theorem | 5/5, direct estimate | Insert `m(gamma) <= hat ell_gamma/min hat tau` and dominate the absolute tail by the physical length-weighted tail. |
| M3 | Critical-line logic | At `sigma_Gal=1`, the abscissa alone neither proves nor excludes a singularity at one.  “Requires a weighted thermodynamic theorem” can be read as a conclusion rather than a description of the missing input. | text: Section 6, pressure-access trichotomy item 2 | 5/5, generalized Dirichlet-series boundary behavior | State that the boundary behavior is undetermined by the abscissa and needs a weighted theorem or equivalent analytic input. |

### MINOR

| # | Dimension | Issue | Evidence anchor | Confidence | Suggested repair |
|---|---|---|---|---|---|
| m1 | Primitive extraction | The proof of normal convergence can be made uniform in one line using the positive minimum primitive length, rather than splitting `k=2` and `k>=3` informally. | equation: Section 4, equation (4.4) | 5/5 | Add the compact-half-plane majorant with a geometric denominator. |
| m2 | Claim boundary | The Route-A tuple should use the evaluator's exact layer labels and explicitly say that the full Galois-weighted series remains `A2_FAIL`/open as a determinant object. | text: Section 8, Route-A paragraph | 4/5, evaluator schema | Replace prose subscripts by exact evaluator tokens and separate the physical subsystem from the full candidate. |
| m3 | Reproducibility | The manuscript reports the finite certificate but gives no one-command locator. | absence: Section 8 — expected executable command; checked paper and code README | 5/5 | Add `bash code/run_c54.sh` and state what it does not prove. |

## Adjudication

All three major findings are repairable without changing the main theorem.
The source theorem was independently checked in Parry--Pollicott, Astérisque
187--188 (1990), Theorems 6.3, 6.4 and 6.9 and Corollaries 6.3.1 and 6.4.1.
No finding justifies promotion of the full Mahler amplitude or Route B.
