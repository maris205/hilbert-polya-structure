# Exact control results — P152

**Status: ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL.**

## Frozen command

~~~bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p152.py
~~~

The deterministic output is frozen in verification_output.txt. A fresh replay
on 2026-09-02 UTC matched that file byte for byte.

~~~text
P152 triangular-book exact verifier
BTB Chebyshev elimination: 4416
BTB inverse iff grid/collisions: 7655
BTB inverse/absorption certificate: 180600
BTB literal lumpability: 2026
BTB mean/parity/extrema: 3958
BTB private-block probability/tail: 648
BTB r=1/r=2/z=0 boundaries: 278
explicit_infeasible_candidates=12
inverse_grid_accepted=69
inverse_grid_candidates=7335
inverse_grid_rejected=7266
private_block_words=8190
single_statistic_collision_pairs=2
tail_bound_instances=546
assertions=199581
arithmetic=integer_and_Fraction_only
enumeration_is_not_proof=1
external_status=HOLD_EXTERNAL
PASS
~~~

Transcript SHA-256:
`da908cb14d7825573b0c43870c96155c55b1b40d4d394eef3f1e972071fa1083`.

## Audited boxes

- Literal states: every nonzero bit vector for 1<=r<=9.
- Joint transform: complete vectors for 1<=r<=20 at
  (z,u)=(1/4,-1/2),(1/3,0),(2/5,1/3),(1/2,1).
- Small boundaries: r=1, removable-factor continuation at r=2, and z=0
  through r=20.
- Mean, parity, extrema: independently solved systems for 1<=r<=60.
- Positive-state inverse identities and deterministic private clearing: every
  1<=k<=r<=300.
- Inverse iff: the criterion is compared with an independently enumerated
  literal image on 7,335 exact candidate pairs.  The grid contains 69 feasible
  pairs and 7,266 exact rejections; its stated mass/probability bounds make
  r<=24 a complete envelope.  Twelve hand-picked candidates separately hit
  the `m>0`/open-q domain, negative or zero scale, square, integrality, and
  admissible-count rejection gates. Domain failure is rejected before any
  real square root is formed.
- Scalar nonidentifiability: both printed collision pairs are asserted,
  together with inequality of the complementary statistic.
- Probability/tail certificate: exact Fraction mass over all 8,190
  private/spine words through block length 12, plus 546 exact survival-versus-
  bound comparisons for n=0,...,6 and every start through r=12.

Direct transform, mean, and parity values come from deterministic
Gauss--Jordan elimination over fractions.Fraction; the closed expressions are
computed separately. No floating-point arithmetic, random seed, network
request, or third-party package is used.

Finite enumeration does not prove the all-parameter transform, inverse iff,
or tail theorem; exhaust source owners; establish novelty or priority;
validate noisy inverse stability; or authorize release.

Review B's candidate-domain Minor is closed in the theorem and proof: `m>0`
and `0<q<1` are required before the real square root is formed.  The verifier
and frozen transcript were unchanged because the negative-mean sentinel
already followed that rejection order.
