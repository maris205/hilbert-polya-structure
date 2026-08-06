# Deep Novelty Check: Relative Heat-Trace Activation

**Date:** 2026-08-06  
**Method checked:** compare the heat traces of the equimeasurable radial and
one-step centered Hénon-warped Riemann--von Mangoldt-clock Schrödinger
operators at the fixed parameter \(a=51/50\).

## Core claims

| Claim | Novelty | Closest work | Honest boundary |
|---|---|---|---|
| Determinant-one Hénon warping leaves the classical clock invariant | low within this project | Paper 7 clock-invariance theorem; standard change of variables | reused foundation, not a Round-2 novelty claim |
| Symmetric rearrangement gives a global heat-trace ordering for equimeasurable potentials | low as a general theorem | Brascamp--Lieb--Luttinger (1974) and later symmetrization work | cite and specialize; do not claim the inequality itself |
| The centered one-step Hénon metric gives an explicit strictly positive first gradient carrier | high for this exact object | general Wigner--Kirkwood/heat-invariant expansions | candidate theorem is the Hénon-specific angular reduction and coefficient |
| The relative heat trace has leading term \(-a^2(24\pi)^{-1}\log^2(1/(2\pi t))\) | medium-to-high, conditional on remainder proof | resummed heat traces for confining potentials; relative heat traces for short/long-range perturbations | exponential, equimeasurable, non-short-range pair needs its own uniform proof |
| The result upgrades the Hénon deformation from coordinate-visible to spectrally active while preserving Q/W | medium-to-high as a synthesis | spectral rearrangement/isoperimetric theory | it closes only S; no prime or zero claim follows |

## Search result

Targeted searches for combinations of “Hénon”, “heat trace”,
“Wigner--Kirkwood”, “area-preserving rearrangement”, and “equimeasurable
Schrödinger potentials” found general heat-trace and rearrangement literature,
but no primary work treating this exact Hénon warp, the coefficient
\(a=51/50\), or its Riemann--von Mangoldt-clock pair.  Exact-parameter searches
likewise found no relevant primary paper.  Absence from this audit is not a
proof of global novelty; it supports a careful, application-specific claim.

## Closest prior work

| Work | Year | Overlap | Required differentiation |
|---|---:|---|---|
| Brascamp, Lieb & Luttinger, *A general rearrangement inequality for multiple integrals* | 1974 | supplies the multiple-integral ordering behind the heat-trace sign | specialize to the confining equimeasurable Hénon pair and prove the needed equality/limit conditions |
| Brothers & Ziemer, *Minimal rearrangements of Sobolev functions* | 1988 | equality classification for Pólya--Szegő | verify the critical-set hypothesis for the analytic radial ground state |
| Hitrik & Polterovich, *Regularized traces and Taylor expansions for the heat semigroup* | 2003 | heat-trace coefficients for Schrödinger perturbations | their standard perturbative setting does not by itself prove the non-short-range exponential Hénon asymptotic |
| Fucci, *Asymptotic Expansion of the Heat Kernel Trace of Laplacians with Polynomial Potentials* | 2018 | partially resummed diagonal expansion and termwise trace integration | extend/control the argument for the present exponential polynomial-warp potential |
| Smith, *On the trace of Schrödinger heat kernels and regularity of potentials* | 2018 | rigorous relative heat expansions | compactly supported-potential hypotheses differ materially from the present equimeasurable confining pair |
| Paper 7 local theorem package | 2026 | proves Q/W and coordinate nontriviality | new result must show a spectral invariant, not merely a non-Euclidean kinetic metric |

## Assessment

- **Recommendation:** proceed with caution.
- **Potential differentiator:** an exact Hénon-specific relative heat
  invariant for two operators whose entire classical phase-volume clock is
  identical.
- **Main reviewer risk:** “this is a routine application of standard heat
  invariants.”  The answer must be a complete noncompact remainder theorem,
  not just the formal coefficient.
- **Secondary risk:** interpreting non-isospectrality as arithmetic progress.
  The paper must say explicitly that the result upgrades S only.
- **Abandon criterion:** if the remainder cannot be made
  \(o(\log^2(1/t))\) under a clean, checkable hypothesis, retain only the
  strict rearrangement/non-isospectral lemma and do not advertise the full
  asymptotic.

## Primary sources

- https://doi.org/10.1016/0022-1236(74)90013-5
- https://doi.org/10.1515/crll.1988.384.153
- https://arxiv.org/abs/math/0105163
- https://arxiv.org/abs/1804.05407
- https://arxiv.org/abs/1809.05614
