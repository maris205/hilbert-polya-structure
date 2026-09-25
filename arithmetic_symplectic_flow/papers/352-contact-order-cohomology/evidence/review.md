# ARS Checkpoint 2 — COG01 mathematical review

**Date:** 2026-09-21. **Audit:** `ANG-AUDIT-20260921-COG01`.  
**Flow:** `ANG-20260921-RCF01`; round 3/5.  
**Verdict:** `PASS`, with one minor notation clarification.  
**Calibration:** `NOT_CALIBRATED`.

## Actual inputs and access

| Input | Personally read | SHA-256 |
| --- | --- | --- |
| [Original card](../candidate-card.md) | All 88 lines | `7335c5cbffe9e3f09e7ba63154b6a565478a7a597dc29c1377e7f35ac3bb1048` |
| [Author proof](../paper.md) | All 265 lines | `3c105e394824a626f7ccf2b288331435aef66fc8393c956ec501f1d9fb508af2` |

Earlier 348–351 author-input familiarity is retained. No peer report,
CP1 result, final surface, external source or other new scientific input
was read. No auxiliary agent, numerical experiment, source campaign or
Git operation was used; only this report was written. The previously read
ARS/stream instructions remain applicable. This is shared-history internal
AI review, with observed model/effective reasoning UNKNOWN, not blind,
cross-model, human or external peer verification.

## Mathematical checks and dispositions

**Local contact grading and actual orders — PASS, notation N1 below.**
The local coordinate substitution gives beta=dtheta+(x dy−y dx)/2 and
R=partial_theta; the stated horizontal X,Y annihilate beta and satisfy
[X,Y]=−R. The dilation therefore gives horizontal weight 1 and contact
weight 2, hence bundle weights (0,1,3,4). The displayed middle operator
contains the nonzero Y^2f term, establishing actual contact order 2;
the outer differentials have nonzero first-horizontal-derivative terms.
The local chart is not promoted to a global replacement of circular u.

**Minor N1 — distinguish horizontal coefficient from lift correction.**
Paper line 76 uses h(a) without defining it. For a=f dx,
d_Ha=(−Yf)Omega, so the horizontal coefficient c(a) is −Yf. The correction
called b in 351 is instead −c(a)=+Yf, and the actual lift is a+(Yf)beta.
That lift gives exactly the author's displayed
delta_1 a=beta wedge[(Rf−XYf)dx−Y^2f dy]. Thus the operator formula and
order claim are correct. Clarify that h(a) denotes c(a), not b; no
mathematical formula, weight or candidate needs changing. This clarification
has been sent to the parent; final appended wording is not yet reviewed.

**Unnormalized flat functional — PASS.** From (S,A,A,S), A=O+2S, the
frozen weights give −A+3A−4S=2O, hence D_ord=D_orb^2=zeta^−2, not a
half-normalized reciprocal. The exact absolute domains and continuation
are the same-owner orbit results. The arbitrary-weight identity reproduces
ordinary degree O−S and unweighted zero and demonstrates that merely
eliminating S is not a unique weight-selection criterion. The filtration
argument is separate from coefficient matching; no torsion claim follows.

**Full smooth product — PASS.** Fiber contraction reduces each circle
component to its circle and R3 to a point. Smooth forms on a topological
disjoint union are unrestricted component products. With no growth
condition, component primitives assemble in that same product, so the
reported product H^0/H^1 and vanishing higher degrees follow. No Hilbert
norm or ordinary trace is assigned to this product by implication.

**Compact-support direct sum and fiber proof — PASS.** The displayed line
homotopy has derivative g−rho integral(g) and satisfies H(df)=f for
compactly supported f. It vanishes outside a bounded interval containing
both supports. With parameters, the compact projected parameter support
and one common bound on line coordinates preserve joint compact support;
the usual graded iteration over the real fibers gives the stated shifts.
The displayed de Rham generators have the required normalized integrals;
351's support-preserving comparison transports their classes to the contact
complex. A compact set meets finitely many open components, giving a
direct sum, not the smooth product. Terminal H_c^3 is retained. This
justifies the specified ell2 generators in K_c^2 and K_c^3 without a
compact Hodge theorem or a physical-state restriction.

**Bounded-time homotopy and action — PASS.** The sign in
K_t=−integral_0^t(Phi^−s)*i_R ds agrees with differentiating backward
pullback. The union of pulled-back compact supports is the image of a
compact time interval times a compact spatial support under the complete
flow. Thus the homotopy works in the compact-support domain as well as
the smooth domain, including negative t by oriented integration. The
equivariant comparison gives identity on both cohomologies. Its extension
to each frozen nonzero K_c is the infinite-dimensional identity, hence
not trace class. This conclusion is specific to the defined owner.

**Finite component and changed-owner controls — PASS.** Terminal plus N
circles gives compact-support dimensions N and N+1 in degrees 2 and 3:
standard trace −1 and order-weighted trace −N−4, constant in time and
unable to equal the positive-time atomic cochain measure. No infinite
trace is defined by subtraction or passage to a cutoff limit. FACTOR-OFF
retains both real components and all integer circles, yielding −2 and
−N−8 for its finite controls and 2O_F for its own flat measure.
UNIT-HOLONOMY has only real components: zero physical flat trace but one
degree-3 compact class per component, giving −4 even on a single component
and non-trace-class identity on the full K_c^3. Source lag is not a period.

## Decision and limits

No Critical/Major mathematical issue was identified. N1 is a minor notation
clarification, not a failure of the contact-order calculation. The exact
positive results and the negative ordinary-cohomological trace conclusion
are supported within the frozen definitions; no universal other-space
no-go, analytic torsion, Fredholm or quantum result is established.
Same-object ownership is intact; naturalness remains OPEN, classical
A0/A1/A2 NOT APPLICABLE, formal UNASSIGNED and B NOT INVOKED.
ADVANCE the structural flat/cohomology results; STOP the specified ordinary
cohomological determinant route. The next source/clock-naturalness question
is unproved and needs a separate card for any changed transport. CP3 and
final wording, including N1's disposition, are outside this invocation.

EOF — COG01 CP2 PASS frozen; only this report written; no peer evidence read.

## ARS Checkpoint 3 — notation closure and final surfaces

**Date:** 2026-09-21. **Verdict:** `PASS`. **Calibration:** `NOT_CALIBRATED`.
The original 107-line CP2 prefix remains unchanged at SHA-256
`11f5dcf72db6896632c2f4fc2f15bd84ae3738dcf492290b154636ae14e6835c`.

Retaining the already-reviewed original inputs, actual new reading was:

| Surface | Read range | Measured full-file SHA-256 |
| --- | --- | --- |
| [Paper](../paper.md) | 266–276 | `bab75d73e67f2d22b4fad2832690f4f6b4053d5b399aa85f34eeacf6ce1836ab` |
| [README](../README.md) | All 28 lines | `fc3d31cf866d85e9dcb0a53d05b63962b0ff097afefbad2853312aa223da94f5` |
| [Ledger](../claim-ledger.md) | All 23 lines | `e4094388d67cb0fabb52eeedb7b7904ce535ccddd98e7ad09a8ce620385bb757` |
| [Card](../candidate-card.md) | 89–104 | `3289757a77ca857bef50677356435801f4b42add9a884aaa69ef4e8816ad0ad9` |

No peer proof, next card, batch log or external source was read. No
unchanged science was repeated, and only this report was appended.
Shared-history/internal-review and unknown model metadata limitations remain.

**N1: CLOSED BY ACTUAL TEXT.** Paper 269–274 explicitly sets h(a)=c(a)
by d_H a=c(a)Omega, distinguishes the correction b=−c(a), and gives
c(a)=−Yf, b=+Yf and lift a+(Yf)beta in the local example. The original
delta_1 formula and second-order term remain unchanged. This resolves
the identified ambiguity rather than relying on an acknowledgment alone.

The final surfaces preserve the actual contact orders and the unnormalized
factor 2: Theta_ord=2Theta_orb, D_ord=zeta^−2, initially Re s>1. They
keep smooth product cohomology distinct from compact-support direct sums,
and restrict the ordinary trace-class negative to the explicitly defined
nonzero K_c Hilbert completions. Finite-component identities are not
promoted into an infinite cutoff trace or a universal other-space no-go.

No half factor, analytic torsion, Fredholm/spectral/quantum interpretation
or stronger naturalness claim is introduced. The same physical owner is
retained, naturalness remains OPEN, classical A0/A1/A2 NOT APPLICABLE,
formal UNASSIGNED and B NOT INVOKED. Returning to clock naturalness is
stated as a new audit, with changed transport separately labelled, not as
a proved next-round outcome or a silent repair of this grading.

No unresolved correction or overclaim remains. CP3 returns `PASS`;
ADVANCE the scoped flat/cohomology calculations and STOP the specified
ordinary-cohomological determinant route. This ends the round-3 review.

EOF — COG01 CP3 PASS; N1 closed; prior prefix preserved; final report frozen.
