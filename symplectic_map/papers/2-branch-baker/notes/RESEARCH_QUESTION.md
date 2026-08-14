# Research Question Brief

## Topic area

Branch-resolved, compact, piecewise-symplectic realizations of the
post-critically finite quadratic map inherited by the symplectic-map session.

## Primary research question

Does the minimal branch-resolved Markov--baker realization of
\(f_u(x)=1-u x^2\) at the post-critically finite parameter \(u=u_c\) qualify
as a Route-A arithmetic symplectic carrier under exact carrier,
primitive-orbit, and clock criteria?

This is an evaluative question.  A negative answer is a complete outcome if
the carrier succeeds geometrically but fails an arithmetic gate for a proved
reason.

## FINER assessment

| Criterion | Score | Justification |
|---|---:|---|
| Feasible | 5/5 | The candidate is finite-state and piecewise affine.  Its geometry, orbit counts, multipliers, and determinants admit exact algebraic checks; the complete verification budget is below one CPU-hour. |
| Interesting | 4/5 | It directly tests the unresolved alternative left by the smooth-factor obstruction: retain branch history explicitly instead of hiding it in a smooth memory coordinate. |
| Novel | 2/5 | Natural extensions, generalized baker maps, finite-state zeta functions, baker quantization, the \(RLR^\infty\) determinant, and the boundary period-doubling mechanism all have direct prior art.  Possible novelty is restricted to the symplectic-carrier audit, the convention-sensitive orientation cancellation, and the resulting finite-clock Route-A no-go statement. |
| Ethical | 5/5 | No human or sensitive data are involved.  The main integrity risk is overclaiming a classical construction or suppressing a negative arithmetic result; the source lock forbids both. |
| Relevant | 4/5 | The result distinguishes a solvable geometric carrier problem from an unsolved arithmetic-clock problem and gives a concrete stopping rule for finite-state symplectic lifts. |
| **Average** | **4.0/5** | Above the required threshold, with novelty deliberately scoped. |

## Scope boundaries

### In scope

- The unique real root \(u_c\) of
  \(u^3-2u^2+2u-2=0\), isolated in
  \((3859/2500,15437/10000)\).
- The invariant core \([-d,1]\), where \(d=u_c-1\), and the Markov
  intervals
  \(I_0=[-d,0]\), \(I_1=[0,d]\), and \(I_2=[d,1]\).
- The two-sided shift defined by the PCF transition graph and its canonical
  Parry-affine three-rectangle Markov--baker realization.
- Piecewise exact symplecticity on branch interiors, a half-open deterministic
  convention, and a two-sided relation on partition boundaries.
- Exact primitive/repetition counts, branch-baker monodromy, the unsigned
  Artin--Mazur object, the separately named factor-orientation-weighted
  object, and the parent-factor boundary quotient.
- A matched dissipative control, a label-erasure control, an anti-symplectic
  implementation control, a dyadic-baker ledger control, and an
  all-positive-sign phase null.
- A general finite-edge, locally constant clock obstruction to an exact
  \(\log p\) ledger.

### Out of scope

- Repairing or retuning the sealed H\'enon candidate.
- Claiming a globally smooth symplectomorphism or a smooth-submersion factor
  of the critical quadratic map.
- Nonlinear generalized-baker realizations, countable-state towers, smooth
  branch regularizations, coupled maps, or higher dimension.  Each would be
  a new candidate and require a new source lock.
- Prime tables, Riemann-zero tables, zero fitting, von Mangoldt weights,
  Riemann-targeted determinants, and Route B.
- Calling a standard baker quantization canonical for this labeled,
  discontinuous realization.

### Key assumptions

1. The arithmetic provenance inherited from earlier work is attributed but
   unverified beyond a mod-2 symbolic shadow.
2. The candidate preserves branch history at the symbolic-factor level; it
   does not preserve the raw quadratic coordinate as a smooth projection.
3. Locally constant edge slopes and clocks are part of the frozen candidate,
   not a theorem about every geometric natural extension.
4. The parent derivative cocycle and the Markov--baker monodromy are distinct
   objects and will never be substituted for one another.
5. The finite shift/baker is a branch-history carrier and symbolic factor.
   It is not claimed to be homeomorphic to the full inverse-limit continuum
   of the quadratic map.
6. The factor-orientation-weighted zeta is not the Lefschetz zeta.  The former
   is \(1-z\) after the boundary quotient in this convention, whereas the
   latter is \(1/(1-z)\) for the interval map.
7. The edge signs record the one-dimensional parent-branch/unstable-coordinate
   orientation.  They are neither the two-dimensional symplectic orientation
   (every branch has determinant \(+1\)) nor a Maslov or quantum phase.

## Sub-questions

1. Does the PCF branch graph admit a compact, almost-everywhere invertible,
   piecewise exact-symplectic affine realization with an explicit boundary
   convention?
2. What are the exact primitive cycles, stability multipliers, unsigned and
   factor-orientation-weighted determinants, and parent-factor boundary
   correction?
3. Which observables survive the matched dissipative and sign controls, and
   does any surviving object meet Route A's arithmetic-origin and clock
   requirements?

All three sub-questions inherit the parameter, phase-space, data-prohibition,
and no-smoothing boundaries above.  There are no scope deviations.

## Candidate questions considered

| Candidate | FINER average | Decision |
|---|---:|---|
| Minimal PCF Markov--baker carrier | 4.0/5 | Selected: it directly addresses the branch-extension clue and is exactly falsifiable. |
| Nonlinear physical-measure natural extension of the raw quadratic map | 3.1/5 | Deferred: substantially larger measure-theoretic and regularity burden, with no stronger arithmetic provenance. |
| Coupled/high-dimensional H\'enon lift | 2.8/5 | Rejected for this round: it does not target the identified critical-factor or noncompact-carrier obstruction. |
| Modular/cat-map arithmetic carrier | 3.2/5 | Retained only as a negative control family; it changes the inherited arithmetic source and has strong existing prior art. |

## Pre-test interpretation boundary

Passing the exact carrier checks earns only
`PRE_A0_STRUCTURAL_PASS`.  If the frozen locally constant clock gives a
lattice multiplier ledger or the matched dissipative control reproduces a
code-only effect, the formal arithmetic outcome is
`A0_FAIL / STRUCTURAL_ONLY`; no downstream prime, zero, zeta-fitting, or
quantization branch may be opened.

## Direct-prior-art boundary recorded at design freeze

The parent kneading determinant is not a new result.  Alsed\`a, Bobok,
Misiurewicz, and Snoha (2025) explicitly give

\[
K_{\sqrt2}=RLR^\infty,
\qquad D_{\sqrt2}(z)=\frac{1-2z^2}{1+z},
\]

and identify the two-renormalized first return with the full tent map.
Hofbauer's Markov-diagram treatment of piecewise monotone maps already
accounts for boundary codings that change apparent periods.  Accordingly,
the reciprocal parent zeta and its single period-doubling quotient are
verification baselines, not novelty claims.  The candidate remains worthwhile
only if it cleanly separates those known symbolic facts from symplecticity and
from the arithmetic-clock gate.
