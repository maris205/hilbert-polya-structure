# HCS-C32 Devil's Advocate Checkpoint 2

Date: 2026-08-12 UTC

Checkpoint ruling:

`ACCEPT_SCOPED_NEGATIVE_RESULT; REJECT_GLOBAL_PROMOTION; GO_TO_NEW_INVARIANT`

## 1. Strongest hostile reading

The harshest fair interpretation is:

> This project rediscovered the elementary fact that a quadratic Gauss sum
> sees only a discriminant square class, then found a small finite-field pair
> illustrating it.  Nothing here approaches Hilbert--Pólya.

Most of that criticism is correct.  The general local theorem is prior art,
the collision occurs in a bounded scan, and no Riemann-zeta structure follows.
The response is to make a narrower claim, not to inflate the result.  What is
newly useful to this program is that a specific proposed Hénon bridge has been
closed by an exact, source-certified counterexample.

## 2. Could the two local germs secretly differ in higher order?

Not in the declared setting.  Both Hessians are nondegenerate and the
characteristic is (61\ne2).  The henselian Morse lemma removes higher-order
terms.  The explicit Hessian congruence and equal critical value then identify
the complete henselian function germs.

This argument would fail at a degenerate point, and the release explicitly
retains that escape route.

## 3. Could extension fields restore the missing determinant?

No for this pair.  The matrix (C) is already defined over
(mathbb F_{61}), so it remains invertible and preserves the quadratic forms
over every finite extension.  Hasse--Davenport signs cannot separate two
quadratic sums connected by a literal change of variables.

Across many primes, quadratic characters may recover a global squarefree
class.  They still do not recover the complete determinant without additional
integral framing or a new global assembly theorem.

## 4. Is the Hill value really intrinsic?

The Hill determinant is intrinsic once the Hénon map and chronological orbit
are fixed.  Its identification with the coordinate Hessian uses the canonical
Hénon generating coordinates.  The standard unframed local sheaf discards the
coordinate volume because a general (operatorname{GL}_n) change of variables
is allowed.  Therefore the collision exposes a mismatch between two notions
of invariance; it does not show the Hill value itself is meaningless.

One can retain it by enriching the local object with the canonical volume
form.  That is a different, framed theory and must justify why the framing is
canonical under the dynamical equivalences relevant to Hilbert--Pólya.

## 5. Could global stationary phase still distinguish the orbits?

Yes.  Local factors need not determine their global assembly.  Critical-value
configuration, Galois permutation, parameter monodromy, and infinity can all
carry additional data.  Consequently, any wording that turns this result into
a global Artin--Schreier no-go is false.

This is the main scope firewall and the main reason to move next to a
discriminant family rather than abandon Hénon dynamics.

## 6. Multiple-comparisons and discovery bias

The (p=61,n=5) pair was found before the protocol was frozen.  The scan is
therefore exploratory.  Its registered replay protects arithmetic correctness
and completeness within the window; it does not convert the witness into a
preregistered statistical discovery.

The theorem does not require a rarity estimate.  One exact pair is sufficient
to refute universal recovery.  The claim that it is the only registered
collision is descriptive and should never be used as evidence of unexpected
arithmetic scarcity.

## 7. Code-independence challenge

The checker is structurally independent in three useful ways:

- it decomposes the full Hénon permutation into cycles instead of repeating
  the producer's state-period loop;
- it computes determinants recursively instead of using the producer's
  modular Gaussian elimination;
- it reconstructs and verifies the congruence matrix rather than trusting a
  boolean flag.

It is not a formal proof assistant.  Producer and checker share the same
mathematical specification and language runtime.  The human-readable matrices
and modular identities are therefore retained in the theorem package for
external replay.

## 8. Novelty challenge

No claim is made to the first Morse lemma, first quadratic vanishing-cycle
calculation, first finite-field Hénon map, first quantized Hénon map, or first
Hill formula.  The novelty claim is search-bounded and specialization-level:
the exact pair and its use as a no-recovery witness for this project gate.

That level is enough for a rigorous negative research output, but probably not
enough for a standalone broad paper.  It should become a substantial theorem
section in a later paper if the next global gate succeeds.

## 9. Falsifiers

The present conclusion must be withdrawn or narrowed if any of the following
occurs:

1. the stated matrix (C) is singular or fails (C^{\mathsf T}B_AC=B_B);
2. either word is not a primitive period-five Hénon orbit;
3. the two critical values differ;
4. one Hessian is degenerate;
5. the cited Morse theorem does not apply to the declared henselian function
   germ;
6. the claimed local invariant is actually a framed object whose morphisms
   must preserve the canonical Hénon volume.

Items 1--4 are exact checker gates.  Item 5 is covered by the primary-source
audit.  Item 6 would change the research question and reopen a framed, not
standard, local theory.

## 10. Final checkpoint decision

- Mathematical result: `PASS` as a scoped negative theorem.
- Computational reproducibility: `PASS` after released artifacts and manifest
  replay.
- General Artin--Schreier no-go: `REJECTED`.
- Positive Route-A construction: `REJECTED/NOT_TESTABLE`.
- Manuscript now: `HOLD`.
- Next research action: `GO` to the Hénon discriminant/monodromy family gate.

The recommended pivot remains inside Hénon-type dynamics.  It moves from
isolated local Morse data to parameter-dependent collision geometry, where the
lost Hill information can reappear intrinsically as the parabolic
discriminant.

