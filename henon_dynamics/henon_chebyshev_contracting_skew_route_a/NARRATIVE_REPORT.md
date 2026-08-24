# Narrative report — HCS-C126

## Result

The triangular polynomial system

\[
F(x,y)=(4x^3-3x,y/4+x)
\]

is an exact all-period laboratory.  Chebyshev composition gives
\(f^n=T_{3^n}\), the base fixed equation has exactly \(3^n\) simple real
solutions, and fiber contraction lifts each one uniquely.  This yields the
complete formula \(\#\operatorname{Fix}(F^n)=3^n\), Möbius primitive counts,
and \(\zeta_F(z)=(1-3z)^{-1}\).

The triangular derivative also retains more information than an orbit count.
At period \(n\), every fixed point is a saddle.  The unstable multipliers split
into endpoint value \(3^{2n}\) and interior values \(\pm3^n\), while the
stable multiplier is \(4^{-n}\).  Consequently the stability determinant,
orientation census, primitive orientation counts, and every repetition are
known exactly at all periods.

## Why this is progress

The progress criterion was deliberately stronger than “find another dynamics
with a cycle.”  Earlier variant packages had broad subtype coverage but often
ended at a finite word cutoff or a single low-period monodromy.  Conversely,
the global trace-class Fock construction had only the origin as a recurrent
base point.  C126 places nontrivial all-period recurrence, primitive/repeated
bookkeeping, an orbit-owned zeta, and stability data in one source model.

This is not yet the joint primitive-orbit/nuclear-operator bridge.  The
Artin–Mazur zeta uses unweighted fixed counts and is not promoted to a weighted
target-facing Fredholm determinant.

## Falsification

The coefficient \(1/4\) is structural.  Replacing it by one changes unique
fiber closure into an entire fixed line at \(x=0\) and no closure at
\(x=\pm1\).  The Chebyshev coefficient is equally structural: for
\(g(x)=4x^3-2x\), the second fixed polynomial factors with triple roots at
\(\pm1/2\), leaving only five distinct roots and a neutral two-cycle.  Thus
both controls break specific theorem clauses.

## Evidence and limitations

Exact receipts list primitive and stability rows through period twelve for
replay, but the proof does not stop there.  An independently written checker,
73 direct SymPy predicates, byte replay, and eighteen hostile mutations guard
against implementation drift.  No external review or novelty determination is
claimed.

The route verdict remains

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
ROUTE_A_EXPLORATORY; Route B unauthorized.
```

The missing advances are a natural global weighted transfer space with a
trace/nuclearity theorem, target-facing divisor validation, analytic
completion, and a natural unitary or scattering lift.
