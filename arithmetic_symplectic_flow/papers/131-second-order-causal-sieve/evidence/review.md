# Independent model review — ASFS-SCOUT-20260914-95

**Date:** 2026-09-14.

**Reviewed status:** PRE-P0 STOP — REVERSIBLE PRIME GENERATION; ZERO-SEED ORBIT HAS UNBOUNDED PROJECTED PERIODS.

**Result:** no mathematical correction required for the stated proofs.

**Type:** independent delegated model audit, not external peer review or a
novelty/Route assessment.

The reviewer read the [card](../candidate-card.md), [paper](../paper.md),
[claim ledger](../claim-ledger.md), and [evidence](README.md), and compared the
source rule with [050](../../050-causal-binary-sieve-fixed-point-screen/paper.md).
The assessed object is the unchanged two-register map R on the complete
binary product. No finite cutoff substitutes for that carrier.

## Proof checks

- **Inverse and source generation:** XOR cancellation proves the inverse in
  both directions. Finite coordinate dependence proves continuity of the map
  and its inverse. G(0)=1 and G(1)=pi hold directly from trial divisibility,
  so the stated second iterate is correct without prime input.
- **Dyadic exponent blocks:** if 2^j<=m<2^(j+1), then floor(m/2) belongs to
  block j-1. The divisor-product indices include each earlier block and a
  nonempty part of block j-1, with no block j index. Equality within blocks
  at the preceding two times therefore gives the same forcing for every m
  in block j; idempotence of binary factors removes repetitions. The zero
  and one time slices establish the induction, including the empty-product
  case j=0. This verifies Lemma 3 for exactly the stated zero seed.
- **Bit identity:** subtraction of one flips the lower zero bits and the
  first nonzero bit; at zero it flips every bit modulo 2^K. Hence the j-th
  bit of u XOR (u-1) is exactly the product of the lower zero-bit indicators.
  This verifies the encoded recurrence (3), including its wraparound case.
- **Explicit solution:** in K-bit arithmetic, -k is the complement of k-1.
  The even update is therefore (-k) XOR k XOR (k-1)=complement(k)=-(k+1).
  The next update is k XOR complement(k) XOR complement(k+1)=k+1.
  Together with U_0=U_1=0 these identities prove (4) for every k>=0.
- **Primitive period:** at time 2k the pair (-k,k) is zero precisely for
  2^K dividing k. At time 2k+1 the pair (k,-k-1) cannot be zero in modulus
  2^K>=2. The least pair period is therefore 2^(K+1). A full-state period
  would be a period of every one of these factors, which is impossible.
  Invertibility also excludes the later generated state from entering a
  periodic orbit.

The finite diagnostic code and its stated coverage were inspected. No repeat
of those computations was needed for this review: the infinite nonreturn
result rests on the independently checked exact identities above. The review
does not independently certify the stored diagnostic stdout.

## Scope and decision

The manuscript correctly limits the negative theorem to the zero-seed orbit,
including its prime-containing second iterate. It does not infer that the
complete map has no periodic points, nor transfer 050's strict-causality
theorem to a map with same-coordinate memory. Other complete-state periodic
packets remain OPEN.

The source relation is explicit and remains owned by R; a roof, geometric
realization, analytic owner, and global prime orbit family are absent.
Classical A0/A1/A2 remain UNASSIGNED and Route B remains NOT INVOKED.
**Stop the zero-seed mechanism; portfolio fork** is supported by the proof.
