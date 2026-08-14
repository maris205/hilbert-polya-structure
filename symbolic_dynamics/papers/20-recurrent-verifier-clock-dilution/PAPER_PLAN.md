# PAPER PLAN — SD-C22

## Title

**Recurrent Verifier Cycles and Clock Dilution: An Operator Obstruction for
Arithmetic Countable Markov Shifts**

## Central claim

Closing an explicit quotient-search primality verifier creates the intended
prime primitive cycles, but exact entropy clock $\log p$ spread over
$\ell(p)\sim\frac12p\log p$ edges forces the natural weighted vertex
adjacency to have essential norm one.  The Euler product survives only as a
raw orbit product or after a first-return collapse to diagonal prime loops.

## Manuscript architecture

1. **Introduction.** Motivate recurrence as the missing step after SD-C21;
   state the positive orbit result and negative operator result together.
2. **Classical boundary.** Separate finite symbolic determinants, countable
   Markov zeta formalism, weighted shifts, suspensions, computation, and
   Fredholm determinants from the narrow claim made here.
3. **Semiring verifier.** Define the full-shift arithmetic skeleton, explicit
   $T/Q/R$ transitions, one-sided edge shift, roof class, and vertex operator.
4. **Cycle census.** Prove the exact contracted length and asymptotic.
5. **Weighted-cycle algebra.** Record powers, spectrum, singular values, and
   finite determinant of a single cyclic block.
6. **Clock dilution.** Prove noncompactness, essential norm one, absence from
   finite Schatten classes, and the essential approximate unit circle.
7. **Orbit product and first return.** Give the normally convergent raw
   product; establish the graph-step/return-step marker firewall and diagonal
   collapse.
8. **Universality and subdivision.** State the disjoint-cycle compactness
   criterion, padded total-decider control, and state-subdivision instability.
9. **Exact certificate.** Report the deterministic cutoff evidence and source
   roof control without promoting numerics to proof.
10. **Route decision.** Apply the frozen tuple, register exclusions, and state
    the next smallest Symbolic Dynamics obligation.
11. **Appendices.** Supply proof details and a same-object/nonclaim ledger.

## Figure plan

One pure-TikZ three-stage figure:

1. the expanded prime verifier closed into a long cycle;
2. the exact clock divided over many edges, producing a near-unit edge weight
   and noncompactness;
3. first return contracting the cycle to one diagonal loop while changing the
   step marker from $z^{\ell(p)}$ to $z$.

## Claim hierarchy

- **Theorem:** exact cycle length and asymptotic.
- **Theorem:** allocation-independent noncompactness and essential norm one.
- **Theorem:** no finite Schatten class and essential approximate unit circle.
- **Theorem:** raw orbit product and first-return marker firewall.
- **Theorem:** exact compactness criterion for disjoint weighted cycles.
- **Control theorem:** total-decider padding and state-subdivision instability.
- **Certificate:** twelve tests and finite exact census through 4096.
- **Nonclaim:** no general impossibility theorem for symbolic zeta functions,
  suspensions, regularized determinants, or overlapping grammars.

## Frozen terminology

- Say **source-weighted vertex adjacency**, never Ruelle operator.
- Say **alphabet-sum**, never categorical coproduct.
- Say **raw combinatorial orbit product**, never whole-operator determinant.
- Say **first-return contraction**, not recovery of the same object.
- Say **acceptance-independent uniformly prescribed padding**.

## Completion checklist

- [x] Source lock and preregistration.
- [x] Corrected contracted cycle convention.
- [x] Proof and narrative packages.
- [x] Primary-source novelty audit.
- [x] Deterministic experiment artifacts integrated.
- [x] Pure TikZ figure specification.
- [x] Modular LaTeX manuscript.
- [x] Four-pass clean compilation.
- [x] Font, citation, layout, and middleware audit.
- [x] Final PDF and compilation report.
