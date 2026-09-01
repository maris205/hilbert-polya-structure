# Hostile review A — P142

Reviewer role: cross-paper mathematical, ownership, and reproducibility audit;
the reviewer did not author P142.  Reviewed 2026-09-01 UTC.  Verdict:
**ACCEPT FOR INTERNAL ROUND 1 WITH MINOR CLARIFICATIONS**.  External status
remains HOLD_EXTERNAL.

## Falsification attempts

1. **Equal valuations.**  Recomputed
   \(v_p(p^{2a}+p^{e-a})\).  The proof correctly separates \(3a\ne e\) from
   \(3a=e\), uses oddness only in the latter case, and gives the sharp binary
   counterexample.  No hidden cancellation occurs for odd \(p\).
2. **Band endpoints and overshoot.**  Checked all three residue classes of
   \(e\bmod 3\).  The parity argument in the \(e=3q+1\) case is necessary and
   correctly excludes the sole apparent overshoot \(2L-1\).
3. **Entry-time maximum.**  Tried to produce a second deepest state from the
   lower branch or an upper state \(e-b\) with \(b\ge2\).  The inequality
   \(L/b\le2^{m-1}\) excludes both when \(e\ge4\); the \(e=2,3\) boundary is
   stated separately and correctly.
4. **Temporal polynomial.**  Expanded the formula at \(e=2,3,4,8,128\).
   Its coefficients sum to \(e+1\), its constant coefficient is the recurrent
   census, and the displayed \(e=128\) example agrees with the formula.
5. **Every-target fibres.**  Solved both branches directly.  Both have the
   same admissibility inequality \(3b\le2e\), and branch coincidence is
   exactly \(3b=2e\); treating the display as a set union prevents double
   counting.
6. **Executable replay.**  Ran
   “PYTHONDONTWRITEBYTECODE=1 python3 verify_p142.py” and compared stdout with
   “verification_output.txt”.  The comparison was byte-identical and all
   319,074 exact assertions passed.

## Findings

- **No major mathematical defect found.**
- **Minor, prose only:** in the fibre proof, “the doubling branch applies
  precisely when” and “the reflection branch applies precisely when” overlap
  at \(3a=e\).  This is mathematically intentional because both formulas
  agree there, but one sentence explicitly saying that the branch labels
  overlap at equality would remove a possible reading objection.
- **Owner risk, medium:** after valuation conjugacy, the dynamics is a very
  elementary finite tent silhouette.  The paper already assigns that
  silhouette zero credit and makes the literal gcd lift plus the complete
  atlas the narrow residual.  A direct-owner hit or specialist judgment that
  the lift is decorative remains a kill condition; the source non-hit is not
  a novelty certificate.
- **Reproducibility:** canonical replay passes; settled build log has no
  unresolved citation/reference or bad-box warning.

## Required round-1 action

Add the one-sentence equality-overlap clarification in the fibre proof.  Do
not broaden the theorem or weaken the binary boundary.  Preserve the explicit
zero-credit and HOLD_EXTERNAL language.
