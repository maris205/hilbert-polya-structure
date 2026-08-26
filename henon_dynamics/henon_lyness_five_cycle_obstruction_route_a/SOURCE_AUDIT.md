# C173 source and integrity audit

- Candidate: `HCS-C173`
- Frozen source commit: `ee8af7b8e265fa4f901d5ed2d1c2edd51475b06f`
- Evaluation date: 2026-08-26
- Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`
- Route-B invocation allowed: `false`

## Source lock

The only mathematical source is the positive-quadrant birational map

\[
F(x,y)=\left(y,\frac{1+y}{x}\right),\qquad (x,y)\in(0,\infty)^2,
\]

with one application of (F) as one tick.  The measure is
\(d\mu=dx\,dy/(xy)\), the reversor is \(R(x,y)=(y,x)\), and the Koopman
convention is \(Uf=f\circ F\).  No parameter is trained or fitted.

Allowed inputs are rational-function algebra, the prime order (5),
change of variables, finite cyclic Fourier algebra, and local measurable
orbit tubes.  Target zero/divisor tables, prime tables, arithmetic local
data, Euler factors, root numbers, automorphy, Hilbert--Pólya assertions,
and Route B are forbidden.

## Citation and data population

The paper is a source-locked proof note and makes no novelty or priority
claim.  It has no bibliography, no external citation, no external dataset,
and therefore zero citation-verification records.  The JSON ledger is
generated internally and is only a regression sentinel.

## Stage 2.5 integrity gate

The mandatory seven-mode ARS taxonomy was applied before drafting:

1. **Implementation bug -- CLEAR.**  Exact rational iterates, the inverse,
   Jacobian density, and cyclic projection algebra are reconstructed by
   separate code paths; repaired-hash and stale-hash mutations must fail.
2. **Hallucinated citation -- CLEAR / not applicable.**  The registered
   citation and bibliography populations are both zero.
3. **Hallucinated experimental result -- CLEAR / not applicable.**  This is
   a proof note with no empirical experiment claim; every finite row is a
   deterministic regression sentinel generated from the frozen map.
4. **Shortcut reliance -- CLEAR.**  The all-point conclusions follow from
   explicit rational identities and measure algebra, never from the finite
   \(10\times10\) grid, numerical fitting, or an unreported seed.
5. **Implementation bug reframed as insight -- CLEAR.**  Negative determinant
   conclusions are derived from the proved uncountable fixed set and
   infinite-multiplicity spectrum, not from a failed computation.
6. **Methodology fabrication -- CLEAR.**  Producer, separate checker, SymPy
   reconstruction, replay, mutation suite, deterministic build, and manifest
   procedures all exist in the release and are directly executable.
7. **Early-stage frame-lock -- CLEAR.**  The candidate is explicitly rejected
   as a primary Route-A candidate; the audit preserves the obstruction rather
   than forcing an arithmetic or Hilbert--Polya interpretation.

## Stage 4.5 post-draft gate

The mandatory taxonomy was repeated against the final paper:

1. **Implementation bug -- CLEAR.**  Every claim-bearing identity still
   agrees with the separate checker and symbolic reconstruction.
2. **Hallucinated citation -- CLEAR / not applicable.**  The final paper has
   no citations or bibliography.
3. **Hallucinated experimental result -- CLEAR / not applicable.**  It makes
   no empirical claim and labels finite ledgers as non-proof sentinels.
4. **Shortcut reliance -- CLEAR.**  No finite cardinal or regularized trace
   replaces \(\#\operatorname{Fix}(F^5)\), and no grid row proves a global
   statement.
5. **Implementation bug reframed as insight -- CLEAR.**  The obstruction is
   separately implied by exact symbolic theorems and survives replay and
   semantic mutation tests.
6. **Methodology fabrication -- CLEAR.**  Every validation and build step
   named by the paper is present in the release artifacts; no external review
   or acceptance score is represented.
7. **Early-stage frame-lock -- CLEAR.**  The final verdict remains
   `ROUTE_A_REJECTED`; a natural unitary lift is not promoted to a
   self-adjoint or target operator.

Verdict: `PASS_WITH_EXPLICIT_OBSTRUCTION`.
