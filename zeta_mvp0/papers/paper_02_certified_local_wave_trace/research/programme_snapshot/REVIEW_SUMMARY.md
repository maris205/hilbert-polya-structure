# Review Summary

## Review mechanism

The external Codex/GPT review endpoint specified by the research-refinement
workflow was unavailable in this environment. No external-model score is
reported. Independent subagents were used instead for:

- the magnetic Weyl proof and symmetry audit;
- the relative spectral-shift/P-gate audit;
- the fourth-order finite-difference cross-check;
- literature and novelty positioning;
- manuscript scope and overclaim review.

The final round-2 record is
`paper/reviews/ROUND2_REVIEW.md`.  After implementation and regression of
all findings, the mathematical, numerical/citation, and claim-drift auditors
reported no residual issue.  No numerical review score is fabricated.

## Main issues raised and dispositions

| Issue | Disposition |
|---|---|
| A designed mean clock is weak evidence for Hilbert--Pólya. | Accepted. The paper's main analytic contribution is controlled deformation, not discovery of the zeros. P remains open throughout. |
| Any area-preserving warp has the same phase volume; Hénon may be decorative. | The general theorem is stated first. A unitary coordinate identity shows the Hénon warp becomes a nonconstant kinetic metric, and the Hamiltonian flow is tested directly. |
| Hénon-map chaos does not imply chaos of the static Hamiltonian flow. | Accepted. Only FTLE/SALI of the autonomous Hamiltonian flow are used. |
| A nonzero magnetic field does not by itself prove GUE. | Accepted. The antiunitary statement is proved only for standard reflected-conjugation repair in centered \(n=1,2\), and spectral evidence is finite-window. |
| One finite-difference family could manufacture the crossover. | R107/R107A adds a gauge-covariant fourth-order stencil. It is labelled an independent-order check, not a fully independent family. |
| The first-resolvent spectral-shift route may be invalid. | The first-resolvent trace-class claim was removed. Third resolvent powers, the discrete relative staircase, heat trace, and tempered wave trace remain rigorous. |
| The \(+1\) in the classical clock may be mistaken for a quantum constant. | The quantum theorem is written only at the two growing orders; all occurrences explicitly deny a quantum \(7/8\) or constant-term result. |
| \(a=1.02\) may look post-hoc. | It is explicitly identified as prior-frozen from an RH-motivated, zero-exposed lineage and is not claimed to be statistically blinded.  The current operator, theorem, and runs are zero-input, and the mean theorem is independent of \(a\). |

## Remaining submission-level risks

1. Obtain a genuinely different magnetic finite-element or Galerkin
   discretization and several higher spectral windows.
2. Expand the classical phase-space census beyond four adaptive control
   states.
3. Obtain ordinary referee-level checking of the fixed-iterate magnetic
   bracketing proof.
4. Keep the relative wave trace as a container until a nonzero-time
   periodic-orbit theorem is proved.
5. Do not run a held-out zeta-zero comparison before an endogenous P
   mechanism is frozen.
