# Preregistration — SD-C26

**Freeze date:** 2026-08-14  
**Candidate:** SD-C26  
**Primary family:** Symbolic Dynamics  
**Zero-data firewall:** active  
**Review loop:** excluded by instruction  
**Experiment status at freeze:** protocol only; no unexecuted count is
reported as a result

## 1. Research question

Can a stationary source-derived grammar use (O(\log n)) finite-alphabet
certificates, close them into recurrent primitive orbits of total roof
(\log n), distinguish primes from composites in the primitive algebra,
and retain a compact or trace-class whole one-step operator?

The three frozen closures are disjoint certificate cycles, a shared prefix-
trie/renewal return closure, and a countable one-symbol-per-atom diagonal.
Constrained-factorization and finite-prefix S-adic stationarizations are
secondary controls.

## 2. Primary hypotheses

**H1 — finite-code counting.**  A finite orbit-separating code for infinitely
many primes has a subsequence satisfying

\[
        \ell(p)\ge c_b\log p,
        \qquad c_b=\frac1{4\log b}.
\]

**H2 — connected-ledger disjointness.**  In a positive scalar graph whose
only primitive cycles have prime roofs, two distinct prime cycles cannot
share a vertex.  A shared recurrent core creates an additional primitive
cycle whose norm contradicts unique factorization.

**H3 — whole-operator obstruction.**  If the intended prime cycles are
vertex-disjoint, have total roof (\log p), and obey H1, then their weighted
adjacency has columns bounded away from zero along a weakly null sequence.
It is not compact and belongs to no Schatten class.

**H4 — marker rigidity.**  If the same trace-class graph determinant equals
(\prod_p(1-zp^{-s})) as a germ at (z=0), positivity forces every prime
orbit to have graph length one.  A finite visible alphabet cannot separate
infinitely many such loops.

**H5 — factorization mismatch.**  There is no injective homomorphism from
the commutative multiplicative monoid containing two primes into a free-word
monoid.  A renewal hub makes products of different atom returns into new
connected primitive necklaces rather than disconnected Euler selections.

**H6 — diagonal escape nonselectivity.**  A one-loop-per-selected-integer
diagonal is trace class on (\Re s>1) and has the requested Euler factors,
but the selected inventory is stored externally.  The same construction
passes prime, composite, square, Fibonacci, random, and hash controls.

**H7 — scoped S-adic failure.**  Every finite stationary prefix is compact,
but the frozen single countable union retains nonvanishing singular
witnesses.  This is a result about the preregistered stationarization, not
all S-adic systems.

**H8 — Route closure.**  H1–H7 imply the positive finite-local-code class
cannot pass A1 and A2 simultaneously.  With no analytic completion or
unitary lift, A3 and A4 fail and Route B stays locked.

## 3. Exact audit protocol

### E1 — code and Kraft ledger

At cutoffs (127,511,2047,8191), generate raw binary, Elias gamma, Elias
delta, and transparent framed-binary codes.  The encoder is target blind;
support is applied only in the evaluator.  Self-delimiting encoders must be
prefix-free with Kraft mass at most one; raw binary is the collision
control.

### E2 — positive roof simplex

For disjoint cycles and (\sigma\in\{1,2\}), test equal, concentrated, and
deterministic hashed positive roof allocations.  Every block must obey

\[
 \max_j e^{-\sigma\tau_{n,j}}
 \ge n^{-\sigma/\ell(n)},\qquad
 \|L_{n,\sigma}\|_1
 \ge \ell(n)n^{-\sigma/\ell(n)}.
\]

The inequalities, not a finite trend, decide the infinite claim.

### E3 — shared trie and primitive necklaces

Close each terminal leaf of a common prefix trie back to its root.  Verify
every intended loop has roof (\log n), then enumerate mixed primitive
return necklaces of lengths two through five.  At a finite cutoff verify
symbolically

\[
        \det(I-zA)=1-F(z),
        \qquad F(z)=\sum_n z^{|c(n)|+1}n^{-s},
\]

not an Euler product of the return factors.

### E4 — matched inventory controls

Run the same closures on primes, composites, and a deterministic matched
pseudorandom inventory.  The arbitrary diagonal must pass all of them and
therefore receive `SELECTOR_TAUTOLOGICAL | PROVES_TOO_MUCH`.

### E5 — factorization and S-adic controls

For a common-hub token grammar, count mixed two-token necklaces, norm
collisions, and the finite determinant (1-F_B).  For the frozen S-adic
stationary union, verify each finite prefix is finite while singular
witnesses remain bounded away from zero in the union.

### E6 — integrity

Run all exact self-tests; generate twice in clean temporary directories;
require byte identity; record per-file and combined SHA-256 digests.  The
experiment may use exact integers, rationals, symbolic determinants, and
theorem-led floating renderings.  It may not use network input, stochastic
fitting, or zero data.

## 4. Decision rule

`GO_NEW_ESCAPE` requires one frozen architecture to pass primitive purity,
finite-source selectivity, and whole-operator Fredholm gates simultaneously.

- `STOP_KRAFT_CLOCK_NONCOMPACT`: disjoint clean ledger, noncompact whole
  operator;
- `STOP_MIXED_PRIMITIVES`: shared recurrence, contaminated connected ledger;
- `ESCAPE_PAPER04`: clean countable diagonal with external inventory;
- `SELECTOR_TAUTOLOGICAL | PROVES_TOO_MUCH`: all matched inventories pass.

No general impossibility claim is preregistered for cancellation-valued
operators, anisotropic spaces, quotient constructions, or arbitrary
countable symbolic extensions.
