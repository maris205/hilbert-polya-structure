# Paper 7 analytic-v3 revision plan

## Revision objective

Produce a separately versioned mathematical-physics manuscript that preserves
the frozen Round-2 paper and upgrades the central ``active deformation'' claim
from a geometric identity plus finite-sample dynamics to two exact spectral
theorems for the scalar one-warp family:

1. strict ground-state activation,
   \(\lambda_1(H_{a,h})>\lambda_1(H_{0,h})\) for every fixed
   \(a>-1\), \(a\ne0\), and \(h>0\);
2. a uniform small-time relative heat-trace expansion whose leading
   coefficient is nonzero and explicit.

The manuscript remains a Hilbert--Pólya-motivated candidate audit, not a
zeta-zero model or an RH claim.

## One-sentence contribution

An area-preserving Hénon warp can preserve an exact classical comparator
carrying the two growing Riemann--von Mangoldt terms and the corresponding
two growing quantum counting terms while provably changing the scalar
spectrum, as witnessed by a strict ground-state inequality and an explicit
relative heat invariant.

## Claims--evidence matrix

| ID | Manuscript claim | Evidence type | Location in v3 | Boundary |
|---|---|---|---|---|
| Q | Fixed self-adjoint operator, compact resolvent | theorem | Sections 3--4, Appendix | fixed parameters |
| W | exact classical clock and two growing quantum terms | theorem | Sections 3--4, Appendix | safe nonoptimal remainder |
| S-op-1 | Hénon warp is strictly non-isospectral | theorem (rearrangement) | Section 5, Appendix | scalar, nonmagnetic, one warp |
| S-op-2 | relative heat trace has explicit nonzero asymptotic | theorem (Feynman--Kac/Brownian bridge) | Section 5, Appendix | fixed \(a,h\); one warp; no magnetic field |
| S-cl | sampled nonlinear classical activity | frozen computation | Section 6 | no ergodicity or positive-measure theorem |
| R | finite-window orthogonal-like to unitary-like response | frozen computation | Section 7 | no RMT universality theorem |
| C | relative spectral objects are admissible | theorem | Section 8, Appendix | no first-resolvent comparability |
| P | endogenous prime-power trace | open | Section 8 | no \(r\log p\) family derived |
| Z/RH | zeta-zero identification / RH | not authorized | Abstract, Sections 1, 8, 9 | explicitly excluded |

## Structural changes

- Revise title, abstract, and introduction so the two new analytic spectral
  results are the primary novelty; retain the Weyl clock and numerical
  diagnostics as the wider candidate audit.
- Expand closest work with rearrangement inequalities, equality cases, and
  noncompact heat-trace/Feynman--Kac context.
- Rebuild Section 5 in the order: variable metric; strict ground-state
  theorem; relative heat theorem and analytic figure; antiunitary audit.
  Keep the relative container and prime-power boundary together in Section 8
  to avoid duplicating their hypotheses and caveats.
- Add full proofs to the theory appendix.  The Brownian proof must retain the
  good/bad bridge split and the dominated-differentiation repair from the
  accepted proof package.
- Split the gate-ledger S row into operator-level proof and classical sampled
  dynamics.
- Update conclusion and all figure captions that currently describe S as
  only sampled.

## Figure plan

Add one data-derived vector figure from
`results/r300_heat_activity/records.csv`:

- left: exact first-gradient carrier bracket and its closed-form asymptotic
  against \(L=\log(1/(2\pi t))\);
- right: the cancellation-free lower-tail representation of the scaled
  residual, demonstrating stable numerical evaluation of the exact identity
  and asymptotic polynomial.

The caption must state that the plot illustrates, rather than proves, the
analytic theorem.

## Citation plan

Add and verify primary sources for:

- Brascamp--Lieb--Luttinger rearrangement inequalities;
- Brothers--Ziemer equality cases for Pólya--Szegő;
- a rigorous Brownian-bridge Feynman--Kac formula on manifolds/Euclidean
  space;
- noncompact confining heat-trace asymptotics/phase-space estimates.

No citation may be inferred from title alone, and no unverified bibliographic
field is to be added.

## Version and review contract

- Do not edit `../paper/` or its frozen Round-2 PDF.
- Compile this directory to `paper7_analytic_v3_round0.pdf`.
- Run two independent review--revision rounds, retaining the corresponding
  PDFs and review reports.
- Report compilation warnings, page count, tests, and SHA-256 hashes.
- External Codex-MCP review is unavailable; independent subagent reviews are
  the explicit fallback, with no fabricated model score.
