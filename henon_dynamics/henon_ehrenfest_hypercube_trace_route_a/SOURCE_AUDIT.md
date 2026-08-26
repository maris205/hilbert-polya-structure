# C171 source audit

- Candidate: `HCS-C171`.
- Frozen source commit: `ee8af7b8e265fa4f901d5ed2d1c2edd51475b06f`.
- Evaluation date: 2026-08-26.
- Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.
- Object: the Ehrenfest coordinate-flip Markov operator
  \(P_df(x)=d^{-1}\sum_{i=1}^d f(x^{(i)})\) on
  \(\{-1,+1\}^d\), for every integer \(d\geq1\).
- One clock tick is one uniformly selected coordinate flip.  The measure is
  uniform probability and the determinant is \(\det(I-zP_d)\).
- Permitted inputs are hypercube combinatorics, Walsh characters, binomial
  coefficients and Krawtchouk polynomials.  There are no fitted parameters.
- Registered bibliography/citation population: zero.  No novelty or priority
  claim is made.

## Arithmetic gate

The object has no intrinsic rational-prime source: all positive integers
\(d\) obey the same formulas, no primitive closed walk is labelled by a prime,
and neither a \(\log p\) clock nor a von Mangoldt weight appears.  Randomized
labels, composite-only dimension labels, neighboring dimensions and a lazy
kernel control leave the mechanism generic.  The honest verdict is `A0_FAIL`.

## Integrity boundary

The all-\(d\) statements are proved symbolically.  The ledgers through
\(d=18\) and \(n=24\) are regression sentinels only.  The natural operator is
self-adjoint, but replacing its Markov evolution by \(e^{-itP_d}\) changes the
clock and path weights; consequently A4 is only `A4_FORMAL_HINT`.
No target zero/divisor table, prime table, arithmetic local datum, Euler
factor, root number, automorphy, Hilbert--Pólya construction or Route-B input
is used.

## Stage 2.5 pre-computation integrity audit

1. **Implementation bug — N/A at design time.** No computed value had yet
   been accepted; the plan required an independent checker, SymPy and brute
   walk enumeration before any release claim.
2. **Hallucinated citation — CLEAR.** The registered citation population was
   frozen at zero, with no literature or priority statement.
3. **Hallucinated experimental result — CLEAR.** The design described only
   future deterministic checks and did not report them as already completed.
4. **Shortcut reliance — CLEAR.** The all-\(d\) proof was mandatory and finite
   ledgers were pre-labelled regression sentinels.
5. **Bug-as-insight — N/A at design time.** No anomalous output existed; the
   protocol prohibited promoting one without independent reconstruction.
6. **Methodology fabrication — CLEAR.** Every intended formula, cutoff,
   checker layer and command was specified before evidence generation.
7. **Frame-lock — CLEAR.** The pivot rule and non-arithmetic controls required
   rejection if the all-parameter compression failed or genericity was hidden.

## Stage 4.5 post-result integrity audit

1. **Implementation bug — CLEAR.** The independent checker, brute walks,
   SymPy reconstruction, byte replay and mutation attacks all pass.
2. **Hallucinated citation — CLEAR.** The final registered citation population
   remains exactly zero.
3. **Hallucinated experimental result — CLEAR.** Every numerical count in the
   report is emitted by a checked deterministic command and stored evidence.
4. **Shortcut reliance — CLEAR.** The Walsh/Krawtchouk proof carries the
   all-parameter claim; no finite sentinel is used as proof.
5. **Bug-as-insight — CLEAR.** Independent formulas reproduce the ledger and
   repaired-hash corruptions are rejected rather than interpreted.
6. **Methodology fabrication — CLEAR.** Released commands, cutoffs, hashes and
   artifacts match the frozen validation protocol.
7. **Frame-lock — CLEAR.** Controls expose the absent arithmetic source; the
   outcome was downgraded to `ROUTE_A_REJECTED` instead of preserving a desired
   narrative.
