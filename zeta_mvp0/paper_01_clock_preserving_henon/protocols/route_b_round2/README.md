# Route B Round 2: Analytic Hénon--Hilbert--Pólya Search

**Opened:** 2026-08-06  
**Mode:** breadth-first candidate discovery followed by pre-frozen fatal tests  
**Frozen parameter:** \(a=51/50=1.02\) in
\[
H_a(x,y)=(1-a x^2-y,x).
\]

This directory starts a new discovery round after the R108-C0 finite-element
branch was terminalized as `INVALID_OR_INCOMPLETE`.  It does not retry that
branch.  The objective is to find the smallest analytic addition that moves
the fixed Hénon programme through one genuine Hilbert--Pólya gate.

The authoritative gates are those in `../../../RH_DISCOVERY_PROTOCOL.md`:

- **Q:** one fixed self-adjoint quantum object with compact resolvent;
- **W:** the two growing Riemann--von Mangoldt counting terms;
- **S:** a non-removable, spectrally observable Hénon deformation;
- **P:** an endogenous *rational-prime-power* trace law;
- **Z:** an explicit-formula/divisor bridge, which is not tested before P.

The first candidate in this round targets **S**, not P: use a relative heat
trace to distinguish the radial and Hénon-warped operators even though their
classical phase volumes agree exactly.  A separate local-horseshoe candidate
targets only a clearly labelled generalized-prime gate \(P^*\); it must never
be described as a rational-prime result.

## Evidence discipline

1. No Riemann-zero ordinates or prime arrays may enter candidate generation or
   the first pilots.
2. The historical selection of \(a=1.02\) was RH-motivated and zero-exposed;
   this round makes no blindness claim.
3. A Ruelle/Artin--Mazur zeta, a spectral-triple zeta, and the Riemann zeta
   function are different objects unless an exact identity is proved.
4. A Hermitization of a transfer operator does not preserve its Fredholm
   determinant in general.
5. Every pilot is a fatal test, not a parameter-tuning exercise.

## Files

- `LITERATURE_LANDSCAPE.md`: primary-literature and internal death-log map.
- `DEATH_LOG.md`: routes excluded before ideation and new pilot outcomes.
- `IDEA_REPORT.md`: ranked candidate cards and final selection.
- `NOVELTY_CHECK.md`: closest-prior-work audit for the selected candidate.
- `INDEPENDENT_REVIEW.md`: independent critical review; no fabricated scores.
- `PILOT_PROTOCOL.md`: frozen definitions, success criteria, and kill rules.
- `R300_P1_UNIFORM_REMAINDER_PROOF.md`: complete Brownian-bridge proof of the
  \(O_{a,h}(tL^4)\) relative heat remainder.
- `R300_P1_INDEPENDENT_REVIEW.md`: two independent proof audits and the repair
  history for the only substantive draft gap.
- `refine-logs/`: final proposal and execution plan for the survivor.
