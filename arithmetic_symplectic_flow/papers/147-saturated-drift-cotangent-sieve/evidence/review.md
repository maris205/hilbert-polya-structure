# Independent model review — ASFS-20260915-SDC01

**Date:** 2026-09-15.  
**Candidate status:** PRIME-ONLY HYPERBOLIC PACKETS AND ORDINARY ZETA ESTABLISHED; TARGET CLOCK AND OPERATOR OPEN.  
**Review finding:** the complete geometric, periodic and ordinary-zeta proofs
are supported; no mathematical blocker was found in Propositions 1--6.

## Scope and provenance

This is a bounded mathematical and ownership review by a separate agent.
The reviewer independently derived the main geometry, all-period exclusion,
prime momentum return and monodromy from the
[frozen card](../candidate-card.md) before reading the completed
[paper](../paper.md), then checked that actual prose, the
[claim ledger](../claim-ledger.md), and the [evidence index](README.md).
The reviewer inherited project context and used the same session model
family. This is not a blind review, human peer review, an external
publication judgment, calibrated error evidence, or a formal Route audit.
No other agent's review report was used.

The ARS review discipline is used only to separate supported claims,
limitations and concrete findings. No journal-fit panel, numerical
review score, submission readiness, or mandatory publication pipeline is
being introduced. The submitted manuscript was not edited by this reviewer.

## Independent mathematical checks

| Claim / paper anchor | Review derivation | Finding |
| --- | --- | --- |
| Proposition 1: global configuration map | Its derivative lies in (1,3/2], and its displacement from the identity is bounded on each fixed component; its limits at the two ends of the real line are the corresponding infinities | Global smooth increasing diffeomorphism supported; no elementary inverse formula is needed |
| Proposition 1: full symplectic owner | For Q=f(q) and P=p/f'(q), P dQ=p dq exactly; preceding phase and the inverse configuration map determine a unique full inverse | The cotangent lift is owned by the same arithmetic configuration update |
| Proposition 2: completeness | A finite positive or negative suspension time uses finitely many globally defined iterates, since the roof is one | Both directions are complete; noncompact escape is not finite-time escape |
| Proposition 3: all composite periods | A proposed period m=rK gives zero displacement equal to (1/2) sum tanh(q_t)+m a(n), which is strictly greater than m(a(n)-1/2); a composite has a(n)>=1 | Contradiction holds for every full state and every positive proposed period, not merely for a bounded orbit search |
| Proposition 4: prime positions | With all witnesses zero, a positive position strictly increases and a negative position strictly decreases under the same map | Only q=0 can be periodic |
| Proposition 4: all prime momenta | At q=0 the full momentum is multiplied by 2/3 per step | Only p=0 can return; the zero section is derived, not selected |
| Proposition 5: primitive and repeated stability | At the surviving state the derivative is diagonal with entries 3/2 and 2/3; cyclic phase enforces least period K_p | One primitive packet per prime and the displayed hyperbolic monodromy are supported; every repetition is nondegenerate |
| Section 4: fixed-iterate finiteness | A fixed point of the mth iterate must satisfy K_n<=m, hence n<=2^(m+1) | Finitely many full fixed points for each m; no trace-class inference |
| Proposition 6: absolute convergence | For sigma>log 2, comparison with all integers gives a convergent power sum; repetitions are bounded by a geometric factor | Normal logarithmic convergence on the stated half-plane is supported |
| Proposition 6: exact abscissa | At sigma=log 2, the first repetitions dominate prime reciprocals; the paper includes the finite Euler-product / harmonic-sum contradiction | Exact absolute-convergence abscissa log 2 is supported, without a prime number theorem or continuation claim |

The three arithmetic comparators were also checked. Zero witnesses leave
one packet for every integer. Block-cardinality witnesses eliminate every
n>=3 but retain the empty n=2 block. For the shifted test, a composite
n+1 at n>=3 has a proper divisor in the retained range 2,...,n-1, while a
prime n+1 has none; n=2 remains its stated exceptional empty block.

No finite computation or numerical precision assumption enters this review.
The full real-state, all-integer and all-period quantifiers are discharged
by the displayed exact arguments rather than by finite tests.

## Concrete clarification and retained limits

One minor ledger wording issue was reported to the author: SDC-N1 initially
described a general finite nonnegative-constraint realization without
repeating the integer-valued qualification given correctly in paper
Section 6. The composite domination proof uses a positive total witness
gap of at least one. Its scope should not silently expand to arbitrary
small positive real constraints. The minimum correction is to insert
the integer-valued qualification in that ledger row; the main proof
does not require repair.

**Author response verified — ADDRESSED.** The ledger now says
nonnegative integer-constraint realization. The abstract also distinguishes
the current nonexact periods from the search for a new exact-clock
candidate. These are scope clarifications only: the frozen formulae and
the reviewed proofs are unchanged. No mathematical rerun is required.

The following are limitations already acknowledged in the manuscript,
not grounds to discard its exact bounded positive result:

- The gain K_n is an explicit all-integer domination device. It does not
  demonstrate a uniquely forced arithmetic geometry, but it is not a
  per-prime fitted parameter or an external prime flag.
- Every integer fibre is present and the source acts in q itself. The
  conserved integer label means this is a constraint realization, not a
  time trajectory enumerating different primes or a conjugacy to the
  original causal sieve.
- Binary macrosteps retain the work of n-2 divisor tests. They yield
  logarithmic-order periods, not an equal-cost sequential primality
  algorithm or exact log p lengths. The equal lengths for 5 and 7
  explicitly exclude repair by one constant rescaling.
- Nonzero periodic-point denominators remove one obstruction present in
  the different 145 object. They do not establish a transfer operator,
  function space, global trace, Fredholm determinant, or analytic
  continuation for this object.
- The universal finite integer-constraint realization control limits
  explanatory naturalness. It does not negate the actually proved
  arithmetic dependence of the complete periodic ledger.

## Decision

**Advance** the exact candidate to a separately frozen, bounded
analytic-owner audit under the current research authorization. The
decisive reason is that source-internal prime selection, complete finite
packet multiplicity and nondegenerate repeated monodromy now coexist in
this one map. Retain the present ordinary-zeta result at its actual
strength. Any change of map, gain, roof, carrier or analytic convention
must receive its own owner card.

The same-object ledger remained intact in the reviewed claims. Formal
Route coordinates remain UNASSIGNED and Route B remains NOT INVOKED.
