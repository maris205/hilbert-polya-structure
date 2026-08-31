# Narrative report

## Core story

A permutation of cycle type `lambda=1^(m_1)2^(m_2)...` has centralizer
`product_j(C_j wr S_(m_j))`.  Replace its cycle type by the orbit-size
partition of the centralizer's derived subgroup on the original points.
The literal group construction reduces to the nonlinear local threshold

```text
j^m -> 1^j  (m=1),  j^2  (m=2),  jm  (m>=3).
```

That structural reduction is owned background.  The residual paper is the
global dynamics produced when all local outputs are recollected: a tagged
coarsening theorem forces eventual period at most two, yields a safe
all-weight tail bound, classifies every recurrent partition, and supports
both ordinary generating functions and exact inverse coefficients.

## Proof spine

1. In `C_j^m semidirect S_m`, commutators with transpositions generate the
   sum-zero base, while top commutators generate `A_m`.  Their natural-point
   orbits give the three local cases.
2. Give every initial part an atomic tag.  A tag is always represented by
   one whole part of its mass or that many singletons.  Only a merge of
   distinct tags lowers the tag count.
3. Two consecutive noncrossing transitions force the intermediate reachable
   tagged state into a normal form consisting of dimers, a singleton residue
   of size at most two, and at most two opposite-phase whole/split
   oscillators.  Applying the map twice returns this state.
4. At most `ell(lambda)-1` crossings can occur.  Before recurrence, every
   pair of transitions contains a crossing, so the tail is at most
   `2 ell(lambda) <= 2n`.  This is not a sharp clock.
5. Stabilize the tags along a recurrent uncoloured orbit.  The clean normal
   form projects exactly to classes `B`, `O1`, equal `O2`, and unequal `O2`.
   Direct substitution proves the converse.  Weight marking gives both
   OGFs.
6. Independent choices of every source multiplicity give a multivariate
   product; the coefficient of the target monomial is its exact fibre.

## Evidence and limitations

The paper-local verifier is dependency-free and exact.  It checks 540,634
partitions through weight 45, all 28,628 targets through weight 30, 18
literal wreath products, and 118,634 reachable tagged states, for 7,130,840
assertions.  Those checks can refute the formulas but cannot prove the
unbounded theorems or establish novelty.

Centralizer orbit language, wreath decompositions, derived-subgroup
structure, generic multiplicity dynamics, and formal coefficient extraction
receive zero contribution credit.  The bounded owner search did not find
the exact residual tagged/recurrent/fibre package; that non-hit is not a
priority certificate.  External release remains on hold.
