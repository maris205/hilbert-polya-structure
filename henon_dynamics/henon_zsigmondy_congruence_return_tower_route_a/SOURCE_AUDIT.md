# C179 source, attribution, and integrity audit

- Candidate: `HCS-C179`
- Frozen source commit: `bbb809ee198bc9ad5f196383baab1e3d9de38e43`
- Evaluator: Route-A evaluator `0.2.0`, SHA-256
  `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`
- Evaluation date: 2026-08-26
- Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`
- Route-B invocation allowed: `false`

## Source lock

The sole input is a pair of coprime integers \(a>b\geq1\).  For every
\(N\geq2\) coprime to \(ab\), define \(q_N=ab^{-1}\pmod N\) and translate
the finite unit group by \(R_N(x)=q_Nx\), marked at \(x=1\).  One
multiplication is one discrete source step.  The normalization is unweighted
fixed-point cardinality; no logarithmic prime roof or prime weight is added.
The two globalizations are retained as different constructions rather than
silently identified.

Allowed computations are exact integer factorization, modular order,
valuation, permutation enumeration, Möbius inversion, and formal power
series.  Finite factorizations are deterministic regression sentinels
generated from \(a,b\), not imported prime data.  No target zero or prime
table, local arithmetic factor, root number, automorphy input, target
divisor, fitted parameter, Hilbert--Pólya assertion, or Route-B input occurs.

## Attribution registry

1. Karl Zsigmondy, “Zur Theorie der Potenzreste,” *Monatshefte für
   Mathematik und Physik* 3 (1892), 265–284,
   DOI `10.1007/BF01692444`.  Authority for primitive-divisor existence and
   the exact exceptions; explicitly `EXTERNAL_THEOREM_ATTRIBUTED_NOT_NEW`.
2. George D. Birkhoff and Harry S. Vandiver, “On the Integral Divisors of
   a^n-b^n,” *Annals of Mathematics* 5(4) (1904), 173–180,
   DOI `10.2307/2007263`.  Historical arithmetic context.
3. Michael Artin and Barry Mazur, “On Periodic Points,” *Annals of
   Mathematics* 81(1) (1965), 82–99, DOI `10.2307/1970384`.  Source of the
   fixed-point zeta convention.
4. Joseph H. Silverman, “Primitive Divisors, Dynamical Zsigmondy Sets, and
   Vojta's Conjecture,” *Journal of Number Theory* 133(9) (2013), 2948–2963,
   DOI `10.1016/j.jnt.2013.03.005`.  Modern context only; not used as a proof
   of any package theorem.

The package does not claim a new proof, strengthening, or priority for
Zsigmondy's theorem.  Its theorem increment is the source-locked synthesis
with the exact lift, complete finite-fiber dynamics, and globalization
nonselection result.

## Stage 2.5 integrity gate

The mandatory seven-mode audit was performed before final drafting.

1. **Implementation bug — CLEAR.**  A producer-independent checker, a
   separate SymPy path, byte replay, and repaired-hash attacks reconstruct
   claim-bearing formulas.
2. **Hallucinated citation — CLEAR.**  Four bibliographic records have fixed
   authors, titles, years, venues, and DOIs; classical and package claims are
   separated.
3. **Hallucinated experimental result — CLEAR / not applicable.**  This is a
   theorem package; finite rows are explicitly regression sentinels.
4. **Shortcut reliance — CLEAR.**  Bounds \(a\leq14\), \(N\leq120\), and
   \(k\leq4\) prove nothing beyond their range; every unbounded quantifier is
   discharged analytically in `THEOREM_PACKAGE.md`.
5. **Implementation bug reframed as insight — CLEAR.**  The owner ambiguity
   follows from two proved fixed ledgers, not from a failed determinant call.
6. **Methodology fabrication — CLEAR.**  Every reported executable, build,
   mutation, and manifest gate is included; no external review is simulated.
7. **Early-stage frame-lock — CLEAR.**  The attractive first-return relation
   is not inflated into A0 pass, A2 match, or uniqueness of a global owner.

## Stage 4.5 post-draft gate

The audit was repeated against the final manuscript.  Attribution remains
explicit; all-parameter claims are proved rather than inferred from ledgers;
the two globalizations remain distinct; finite Koopman unitarity is not
misstated as target spectral ownership; and limitations retain the strict
`A0_WEAK/A1_WEAK/A2_FAIL/A3_FAIL/A4_NATURAL_QUANTIZATION` boundary.

Verdict: `PASS_WITH_EXPLICIT_OWNER_NONSELECTION`.
