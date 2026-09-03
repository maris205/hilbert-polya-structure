# Claims and evidence

**Lifecycle:** `AMBER_INTERNAL_NEAR_P166 / HOLD_EXTERNAL`

| ID | Manuscript claim | Proof location | Author/scout-derived regression control | Boundary |
|---|---|---|---|---|
| C1 | Every rotation class has exact phase map `j -> j +/- k`. | Lemma 2.1 | `audit_rotation_classes` checks every pointed state through `n=18`. | Generic cyclic-phase reduction is zero credit. |
| C2 | `gcd(k,d)` generator cycles give a complete pointwise recurrent/transient classification. | Theorem 2.2 | `component_prediction` is compared with the literal local graph for every necklace through `n=18`. | Ordinary oriented-cycle facts are zero credit; only the constrained theorem package is retained. |
| C3 | Possible periods are `{1}` at `n=1`, otherwise `1`, `2`, and proper divisors at least `3`. | Theorem 3.1 | Literal possible-period set checked for every `1<=n<=18`. | P166's period inventory is different and does not transfer. |
| C4 | The sharp maximum preperiod is `n-2` for `n>=2`, with exactly two deepest states for `n>=3`. | Theorem 3.2 | Every literal state checked; boundary counts at `n=1,2` also checked. | The numerical value `n-2` is explicitly zero credit because it already occurs in P166. |
| C5 | Every target has the explicit two-branch inverse list and fibre size `0`, `1`, or `2`. | Theorem 4.1 | Reverse adjacency is compared target-by-target with `predicted_preimages`. | Indicator-style inverse presentation is zero credit. |
| C6 | The closed weight-layer fibre histogram and image formula hold. | Theorem 4.1 | Literal histogram compared with `predicted_fibre_histogram`. | Binomial conditioning is zero credit. |
| C7 | The displayed primitive-block Möbius sum equals the fixed census. | Theorem 4.2 | Literal fixed counts compared with `predicted_fixed_count`. | Primitive necklace counting and Möbius inversion are zero credit. |

## Control ceiling

The canonical run enumerates all `2^n` binary words for every
`1<=n<=18`.  It reports `2,828,503` assertions.  This computation is not
used to justify any all-parameter step; each claim above has a uniform
proof in `main.tex`.

Canonical transcript SHA-256:
`3d0947a4df32f8e583e28d1964a52523602d61c64dde7b259bfdd15e71e4003b`.
Verifier SHA-256:
`2dd56b882925c908565a9a213c42db7acccbf4fc214b54460619b71fe0587b50`.

## Kill conditions

The manuscript is killed internally if any of the following occurs:

1. a direct source owns the adaptive update together with one retained
   theorem;
2. the literal map is conjugate to a P166 subsystem;
3. the constrained generator-component theorem follows formally from
   P166's mass-exhaustion theorem without an additional argument; or
4. the author regression control or an independent hostile-review control
   fails beyond or within its frozen exact box.

## Provenance repair and independent cross-check

Review A established that `code/verify_p176.py` is scout-derived: its
executable core matches the discovery verifier, although it is standalone
and has valid internal prediction paths.  It is therefore recorded only as
the author regression control.  The independently implemented Review-A
bit-mask verifier lives under
`docs/papers172_176_sequence/reviews/p176_review_a/`, reaches `n=19`, and
passes 14,407,195 assertions.  This wording change repairs evidence
provenance and does not alter a mathematical claim.

Review B independently passed 19,758,014 assertions with a string-state,
slicing, Brent-orbit, and direct-component implementation.  Its source audit
also assigns Grošek--Hromada's fixed-weight rotation-class theory and Gupta
et al.'s ordinary coordinate-rotation treatment zero contribution credit.
Neither source owns the adaptive gluing or its functional graph.  Review B's
two mandatory package repairs are implemented and independently
delta-accepted; no review finding remains open.
