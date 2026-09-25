# Evidence index — ANG-20260918-FVP01

**Evidence state:** exact symbolic screen; no numerical computation.  
**Decision:** PRE-P0 STOP — canonical successor/carry is not a bijection.

## Frozen inputs

- [candidate-card.md](../candidate-card.md) freezes the graph, path
  normalization, ordinary edge order, carry ray, cocycle, and stop rule.
- [paper.md](../paper.md) gives the cover-prime proof, the path-space
  identification, the no-maximal-edge obstruction, and the non-surjective
  no-carry control.
- [claim-ledger.md](../claim-ledger.md) separates exact positive source
  statements, exact negative statements, conditional formulas, and
  unavailable downstream gates.

## Exact evidence

1. A strict divisor-cover ratio is prime because a composite ratio supplies an
   intermediate rational, and an intermediate rational supplies a
   factorization.
2. Every prime-labelled bi-infinite word has a unique normalized path, so
   the all-2, alternating 2/3, and arbitrary mixed paths are retained.
3. The outgoing ordinary-order edge set has no maximal element: beyond any
   prime \(p\), a prime divisor of \(p!+1\) is larger than \(p\).
4. Since every digit is non-maximal, the frozen scan selects index 0
   immediately.  The actual map is \(p_0\mapsto\) next prime, with all other
   coordinates fixed; its image omits every path with \(p_0=2\), so it is not
   surjective.

These are hand-checkable elementary deductions from the frozen definition.
No prime list, generated table, floating-point computation, GPU job, or
external source was used.  No independent blind review is claimed; the
evidence is a bounded author-side proof readback.

## Correction receipt — 2026-09-18

The initial internal wording said that the missing maximal digit made the
carry undefined.  That was a logical error: the rule scans for the first
non-maximal digit, so it stops at index 0 on every path.  The corrected
obstruction is non-surjectivity of the actual next-prime update, not
undefinedness.  The frozen candidate, source carrier, and stop decision are
otherwise unchanged.

## Reproduction checks

The package contains exactly five Markdown records plus this evidence index.
The local links in the summary, paper, card, and ledger point only to files
inside this package or to the explicitly named comparison packages 148 and
163.  A future mechanical verifier should check IDs, link targets, and the
absence of root-level edits before registry integration.
