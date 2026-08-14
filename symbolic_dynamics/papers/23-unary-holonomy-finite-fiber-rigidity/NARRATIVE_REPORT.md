# Narrative Report — SD-C25

**Paper type:** mathematical theory with exact implementation
preregistration  
**Primary field:** Symbolic Dynamics  
**Tone:** positive structural theorem followed by a decisive scoped no-go  
**Route outcome:** ROUTE_A_REJECTED

## One-sentence contribution

The source-derived cofactor word \(1^{k-1}2\) reduces every fixed finite
fiber to eventual periodicity and every fixed linear fiber to an LRS, while
growing and countable repairs either memorize arbitrary support, prune the
computation, or clock-dilute, and none changes the underlying factorial
roof.

## What the paper is about

Paper22 found a positive result: holonomy two selects exactly the canonical
primitive cycles

\[
        C_k=(k,k+1,\ldots,2k-1)
\]

for every \(k\ge2\).  Product holonomy cannot distinguish their lengths,
but the ordered quotient labels retain the run length:

\[
        W(C_k)=1^{k-1}2.
\]

The natural next question is whether a finite noncommutative or weighted
fiber can read this word and keep only prime \(k\).  Paper23 answers that
question exactly.

## Central reasoning chain

The story has five steps.

1. A finite semigroup sees only the power \(a^{k-1}b\).  Powers in a finite
   semigroup are eventually periodic.  Any accepted length set is therefore
   ultimately periodic, while an infinite prime-only set cannot be.
2. A fixed finite-dimensional weighted fiber produces
   \(u^{\mathsf T}A^{k-1}Bv\) or
   \(\operatorname{tr}(A^{k-1}B)\).  Cayley–Hamilton makes either response an
   LRS; SML makes its exact support ultimately periodic.
3. Increasing the dimension evades the asymptotic theorem only by storing
   the finite answer vector in a nilpotent shift.  The same construction
   fits any bit string, so finite-cutoff success is a control rather than
   evidence.
4. Infinite exact memory can compute primality, but the two licensed
   Paper19/Paper20 wrappers do not preserve the desired mechanism.  Transient computation
   disappears from traces; recurrent long computation with total roof
   \(\log n\) is noncompact; inducing collapses the word and changes the
   marker.
5. These memory obstructions are independent of a second same-object
   failure.  The original cycle already has length \(k\) and endpoint roof
   \(2\log((2k-1)!/(k-1)!)\).  A filter cannot convert those invariants into
   a one-step \(k^{-s}\) prime loop.

## Strongest theorem

The strongest result is a hierarchy rather than one isolated impossibility:

\[
\boxed{
\begin{array}{c}
\text{fixed finite memory: eventual periodicity}\\
\Downarrow\\
\text{fixed linear memory: SML support rigidity}\\
\Downarrow\\
\text{growing finite memory: arbitrary-prefix memorization}\\
\Downarrow\\
\text{licensed countable wrappers: pruning or clock dilution}\\
\Downarrow\\
\text{same base cycle: factorial roof persists}.
\end{array}}
\]

The hierarchy closes every immediate ordered-word repair suggested by
Paper22.

## Why the result matters

A negative paper is valuable here because the candidate has several
features that can look deceptively successful:

- it derives its word from the symbolic source;
- it has a noncommutative order-sensitive fiber;
- it supports a trace-class block adjacency on \(\Re s>1/2\);
- any finite prime prefix can be fitted exactly;
- a countable decider can produce an exact Euler product.

The theorem separates those facts.  Source origin does not imply prime
selectivity; an honest Fredholm determinant does not imply the correct
primitive ledger; finite fit does not imply asymptotic structure; exact
computation does not imply recurrence-visible computation.

## Literature positioning

The classical ingredients are not new.  Unary automata, prime recognition,
multiplicity automata, and SML have long histories.  De Jong 2026 is the
closest direct collision because it already uses SML to classify dynamical
period sets and treats least periods in finitely presented systems.

Paper23's defensible contribution is the exact cofactor reduction and its
integration with the previous branch's operator, wrapper, marker, and roof
constraints.  The paper must cite de Jong near the first novelty statement,
not bury it in related work.

## Counterarguments handled

### “Use a larger finite group”

The period may become large, but it remains finite.  A fixed group cannot
support infinitely many prime-only accepted lengths.

### “Use complex weights instead of Boolean acceptance”

Exact nonzero support remains governed by a fixed LRS.  SML blocks an
infinite prime-only support.  The paper does not overextend this to arbitrary
threshold semantics.

### “The finite experiment fits all tested primes”

A nilpotent shift fits every target vector through the same cutoff.  Prime
fit must be compared with square, random, and hash controls.

### “Use a countable primality machine”

That is computationally possible but explanatorily weak.  If the computation
is transient, traces see only its accepted terminal loops.  If it is made
recurrent under a short total roof, clock dilution destroys compactness.

### “Induce to one prime return”

Inducing removes the internal word and changes \(z^k\) to \(z\).  The
resulting diagonal object is not the original vertex determinant.

### “Change the roof after selection”

The source endpoint roof is factorial.  Forcing \(\log k\) across a length
\(k\) orbit triggers clock dilution.

## Figures

Figure 1 should let a skim reader recover the whole hierarchy from one
diagram: canonical word, finite-periodic branch, LRS branch,
growing-memory control, countable wrappers, and the factorial ledger.

Figure 2 should isolate the memory/roof incompatibility: fixed memory fails
selection, growing memory proves too much, countable transient memory
prunes, recurrent memory is noncompact, and inducing changes the marker.

## Exact audit narrative

The experiment section is an audit, not empirical evidence.  It verifies:

- word construction and source firewall;
- eventual-period certificates;
- exact characteristic recurrences;
- arbitrary nilpotent memorization;
- block power traces and determinants;
- countable wrapper invariants;
- factorial monomials and marker mismatch.

No test uses Riemann-zero data.  No result count is invented before the
integrated implementation finishes.

## Limitations

The finite-dimensional theorem covers exact supports and fixed-level sets,
not signs or cutpoints.  The countable theorem covers the licensed
Paper19/Paper20 total-decider wrappers, not all countable symbolic systems.  The paper does not close
every possible source-derived infinite-memory grammar.

The full block factor, its first trace-log term, the marked bilinear
observable, and the separate one-dimensional oracle deletion control are
four distinct ledgers.  Exterior powers extend LRS rigidity to every
coefficient of the full block factor; a vanishing first trace alone does
not remove an orbit.

These limitations define Paper24 rather than weakening Paper23: any
successor must construct a genuinely new recurrent grammar with
\(O(\log n)\) symbolic length and intrinsic roof \(\log n\) before it earns
another experiment.

## Final narrative sentence

The ordered cofactor word preserves enough information to prove a strong
memory hierarchy, but not enough to turn the successor–divisor cycles into
the prime Euler ledger.
