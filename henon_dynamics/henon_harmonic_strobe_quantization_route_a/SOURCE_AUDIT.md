# C178 source and integrity audit

- Candidate: `HCS-C178`
- Frozen source commit: `100e5f601a0196710d53784bdeef40d2bff89fa8`
- Evaluator: Route-A evaluator `0.2.0`, SHA-256
  `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`
- Evaluation date: 2026-08-26
- Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`
- Route-B invocation allowed: `false`

## Source lock

The sole source is the Hamiltonian \(H=(q^2+p^2)/2\) on the canonical
plane, with physical unit-frequency time \(\theta\in\mathbb R\).  The strobe
is its exact flow \(T_\theta=\Phi_\theta\).  Its classical and Gaussian
projections are \(2\pi\)-periodic.  The Gaussian Koopman convention is
\(U_\theta f=f\circ T_\theta\), and the quantum convention is
\(Q_\theta=e^{-i\theta\widehat H}\) for
\(\widehat H=(-d^2/dx^2+x^2)/2\).  The quantum unitary family is retained on
real time: \(Q_{\theta+2\pi}=-Q_\theta\) and
\(Q_{\theta+4\pi}=Q_\theta\).  It is only projectively \(2\pi\)-periodic and
is not silently descended to the classical quotient.  These conventions are
frozen before any finite ledger is generated.

Allowed inputs are rotation algebra, fixed-set cardinality, Gaussian polar
coordinates, generalized Laguerre orthogonality, Hermite functional calculus,
canonical commutators, and operator-ideal definitions.  No target zero or
prime table, arithmetic local datum, Euler factor, root number, automorphy
object, Hilbert--Pólya assertion, heat/Wick clock replacement, or Route-B
input is allowed.

## Citation and data population

This source-locked proof note makes no literature novelty or priority claim.
It has no bibliography, citation, external dataset, fitted parameter, human
or animal subject, or private data.  The exact JSON ledger is internal and
serves only as a regression sentinel.

## Stage 2.5 integrity gate

The mandatory seven-mode ARS taxonomy was applied before final drafting:

1. **Implementation bug -- CLEAR.**  A producer-independent checker, separate
   SymPy reconstruction, byte replay, and repaired-hash mutations attack the
   fixed-set, phase, normalization, and clock formulas.
2. **Hallucinated citation -- CLEAR / not applicable.**  Registered citation
   and reference populations are both zero.
3. **Hallucinated experimental result -- CLEAR / not applicable.**  The note
   makes theorem claims, not empirical claims; finite rows are labeled
   deterministic sentinels.
4. **Shortcut reliance -- CLEAR.**  Finite rational denominators, Hermite
   levels, and Laguerre indices never prove an all-angle or infinite-basis
   statement; the displayed analytic proofs do.
5. **Implementation bug reframed as insight -- CLEAR.**  Continuum fixed sets
   and non-trace-class unitaries follow from exact theorems rather than failed
   numerical determinant calls.
6. **Methodology fabrication -- CLEAR.**  Every named code, mutation, build,
   font, replay, and manifest procedure is executable in the release; no
   external review or acceptance score is represented.
7. **Early-stage frame-lock -- CLEAR.**  Rational resonances, infinite radial
   multiplicity, the metaplectic \(2\pi\) sign, quantum phase conventions,
   and the A0 failure remain visible rather than being quotiented or
   regularized away.

## Stage 4.5 post-draft gate

The same mandatory taxonomy was repeated against the final manuscript:

1. **Implementation bug -- CLEAR.**  Final claim-bearing identities agree
   with the separate checker and symbolic reconstruction.
2. **Hallucinated citation -- CLEAR / not applicable.**  The PDF has no
   citations, bibliography, or unsupported attribution.
3. **Hallucinated experimental result -- CLEAR / not applicable.**  No finite
   receipt is presented as statistical or extrapolative evidence.
4. **Shortcut reliance -- CLEAR.**  The paper proves completeness and
   infinite multiplicity; it does not infer them from truncated ledgers.
5. **Implementation bug reframed as insight -- CLEAR.**  Classical and
   operator obstructions are each proved independently of software failure.
6. **Methodology fabrication -- CLEAR.**  Internal passes are described as
   internal; no prose review is called external or statistically independent.
7. **Early-stage frame-lock -- CLEAR.**  The final verdict remains
   `ROUTE_A_REJECTED`, A4 is not used to compensate for A0--A3, and the
   quantum global sign is retained despite the classical \(2\pi\) quotient.

Verdict: `PASS_WITH_EXPLICIT_OBSTRUCTIONS`.
