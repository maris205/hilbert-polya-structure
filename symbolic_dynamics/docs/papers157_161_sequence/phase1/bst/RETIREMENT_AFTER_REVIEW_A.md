# P160 BST retirement after Hostile Review A

**Decision:** `KILL_STANDALONE_PAPER / REOPEN_P160_SLOT / HOLD_EXTERNAL`.  
**Date:** 2026-09-02 UTC.

The binary-projective Steiner triangle formulas are mathematically correct,
but the paper-level residual did not survive source subtraction.  The frozen
Round-0 manuscript and its Review-A evidence are retained as an auditable
negative result; they are no longer one of the five selected papers.

## Decisive primary-source collision

Masood Aryapoor, [*The pasch configuration and Steiner triple
systems*](https://arxiv.org/abs/1306.1257), arXiv:1306.1257v1 (2013), defines
on distinct triples the unordered map

```text
{a,b,c} -> {a star b, b star c, c star a}.
```

Its Section 2.1 defines the associated maps `phi_S` and `psi_S`.  Theorem 2.1
gives the general `n-3` inverse bound.  Proposition 2.2 identifies the
projective `PG(k,2)` equality case, supplies the exact `n-3` nonblock inverse
family for every block, and observes that the pair-sum image is again a
projective block.  This is precisely the free `S_3` quotient of the
distinct-coordinate part of the proposed ordered map.

After that result is subtracted, the ordered lift, universal equality-pattern
three-cycles, weak-component count, moments, zeta conversion, and rank
recovery are consequences of the same graph census.  They do not provide the
required independent theorem-level advance.  A citation-only repair would
therefore be misleading.

## Review evidence retained

- author verifier: 4,836,144 exact assertions, PASS;
- independent Review-A verifier: 3,166,113 exact assertions, PASS;
- mathematical formulas, boundary `r=2`, and PDF integrity all passed;
- formal review verdict: `KILL — 1 Critical / 0 Major / 2 Minor`;
- raw report: `papers/retired/160-binary-projective-steiner-triangle-collapse/HOSTILE_REVIEW_A.md`;
- reviewer controls: `docs/papers157_161_sequence/reviews/p160_a/`.

The kill is about contribution ownership, not a counterexample.  Reuse under
the P160 number requires a genuinely different literal system, new theorem
contract, new owner search, new proof/verifier, and new two-review cycle.
