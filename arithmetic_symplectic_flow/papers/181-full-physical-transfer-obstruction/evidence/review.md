# Separate mathematical review of the full physical transfer test

**Paper ID:** 181-full-physical-transfer-obstruction  
**Candidate ID:** ALF-20260915-PTO01  
**Candidate status:** STOP — FULL-STATE BOUNDED-FUNCTION TRANSFER NOT REALIZABLE; NATURALNESS OPEN.  
**Review outcome:** ACCEPT SCOPED NEGATIVE RESULT; NO UNRESOLVED CORE FINDING.  
**Review completed:** 2026-09-15 13:37:24 UTC.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

## Review remit and provenance

The actual reviewer invocation is `/root/physical_transfer_reviewer`,
separate from root's authoring invocation. It read the frozen card first,
derived the functional-analytic test before reading the completed paper,
then read all five final core Markdown files. The completed author response
was visible. This is a nonblind, same-model-family review with inherited
context, not evidence of independent error probabilities, a calibrated
review panel, human peer review or publication readiness.

The reviewer delegated only the natural-extension and period-continuity
subchecks to the distinct read-only invocation
`/root/physical_transfer_reviewer/clock_extension_check`. That invocation
inherited the same model/context and returned derivations, not a review
verdict. The reviewer independently checked those returned derivations
against the frozen formulas and final paper. No other new candidate author
package was used to manufacture corroboration. No external model/API call
or manuscript upload was made. Accountable human reviewer: none asserted.

ARS was used as a bounded theoretical-methodology aid: exact premises,
claim/evidence/reasoning, counterexamples and conclusion scope. The current
candidate card supplies the review criteria; no venue criteria, numeric
scores, full publication pipeline or editorial decision is asserted.
Calibration status: `NOT_CALIBRATED`. Venue criteria binding: unavailable.

## Criterion-bound findings

| Criterion from the frozen contract | Judgement | Evidence anchor | Reason and scope |
| --- | --- | --- | --- |
| Complete physical return and negative histories | MEETS | equation: paper Section 2, formulas (1)--(3), Lemma 1 | All inverse histories are reconstructed on the entire strip; no periodic subsystem substitutes for the natural extension. |
| Constant-containing bounded-function realization | MEETS AS A NEGATIVE TEST | equation: paper Proposition A, (4a)--(4c) | The image of 1 is unbounded, so the proposed full-state intertwining realization does not exist. |
| Actual variable physical period | MEETS | equation: paper Lemma 2, (4) | Continuity and divergence follow from regular inner motion and the displayed integral; no fitted logarithmic roof is used. |
| Additional sector compactness obstruction | MEETS | equation: paper Theorem 3, (4d)--(7) | The sector operator is genuinely bounded, and its spectrum contains the stated interval; it is not the full operator. |
| Same-object and nonclaim discipline | MEETS | table: paper Sections 7--8 | The full owner, its internal sector, the older scale comparator and untested analytic categories remain distinct. |
| Formal Route or naturalness passage | NOT ASSESSED | table: paper Section 8 | No formal Route protocol or naturalness gate is claimed or evaluated by this review. |

## Decisive reviewer finding and author response

While the initial card and author direction emphasized compactness, the
reviewer found an earlier obstruction within the same frozen definitions.
At the retained transverse level I=1/2, every n has f_n(I)=I. Consequently
tau_n(I)=T_n(1/2), with a uniform upper bound independent of n.
The full predecessor count nevertheless grows without bound.

The reviewer supplied the exact bound used in the final paper. Since
W(A)=1/(2c)<=1/2<W(1/2), A<1/2, and direct subtraction gives

    W(A)-W(q)
      =4(A^2-q^2)(1-A^2 q^2)/((1+A^2)^2(1+q^2)^2)
      >=(192/125)(A^2-q^2)
      >=A^2-q^2.

Here the first coefficient bound is
4(15/16)/(5/4)^4=192/125. With c>=1 this proves
T_n(1/2)<=4 integral_0^A [2(A^2-q^2)]^(-1/2)dq=sqrt(2) pi.
On the constant a_N source, the first N derived atoms are all allowed
predecessors, so L_s1>=N exp(-s sqrt(2) pi) for real s>0.
This contradicts J T_s e belonging to C_b(X).

The contradiction does not even use boundedness of T_s: it uses that
T_s e belongs to H and every element of J(H) is a bounded function.
Thus changing only the norm, permitting a noncompact operator, or
permitting an unbounded operator with 1 still in its invariant domain
does not fix the stated architecture.

Root adopted this finding as Proposition A and the final STOP reason,
preserving the version-1 definitions and appending the outcome. The old
spectral idea was retained only as an explicitly labelled internal sector
control. The final paper does not claim that a bounded noncompact full
operator, or a full-owner spectral interval, has been realized.

## Independent mathematical checks

**Full natural extension.** Each K_a preserves I and has the global inverse
(Q,P)->(exp(-h_a(I))Q,exp(h_a(I))P). A compatible inverse history of B_+
records exactly one weakly nondecreasing bilateral source. Given that source
and its present strip point, every past strip point is recovered by a finite
composition of the appropriate K_a inverses. Both reconstruction directions
are continuous in the stated product/inverse-limit topology. Local compactness
of the source is unnecessary. The explicit order x<=_D y iff y/x is a positive
integer in final Section 2 resolves the card's otherwise potentially ambiguous
phrase about divisibility on positive rationals.

**Clock.** The identity chi(t)+chi(1-t)=1 gives
integral_(-1)^0 g_n=epsilon_n(1-3delta_n/2)+3delta_n/2=n^-2.
Hence f_2(I) tends to -1/4 at the left boundary and the energy tends to c_2.
Regular transverse first return proves period continuity away from energy
endpoints. In the paper's substitution v=(1-q^2)/(1+q^2), one has
abs(dq/dv)=(1+v)^(-3/2)(1-v)^(-1/2) and
E-c_2 W(q)=c_2(v^2-d^2). This verifies formula (4), including its
coefficient. Its positive lower bound on [d,1/2] diverges as arcosh(1/(2d)).
Continuity and divergence, not unproved monotonicity, imply the interval
of period values used later.

**Actual sector and dual means.** Restriction to the least-atom source
has just one admissible predecessor. Thus R_s in (4d) is a well-defined
bounded weighted composition on C_b(U*), with norm at most one. This
sector is an internal control, never a replacement of the full X.
For z_j=K_2^j(1,I), the evaluation means have uniformly bounded dual
norm, value 1 on e, and the exact telescoping defect
lambda_I(delta_(-1)-delta_(N-1))/N. Banach--Alaoglu supplies a weak-star
convergent subnet even when H is nonseparable and the physical orbit
escapes every compact subset. Boundedness of T passes this relation to
the limit. The nonzero complex-linear dual functional annihilates
range(T-lambda_I), so lambda_I belongs to the spectrum, without asserting
a primal eigenvector. Spectrum closedness adds zero. Compactness is
incompatible with the resulting interval of nonzero spectral values.

No countably additive physical probability, compact transverse orbit,
point-selection rule, new closed packet or new determinant is inferred
from these dual means. The conclusions concern real s>0 only. Alternative
categories not satisfying bounded-function invariance with constants are
not excluded.

## Resolved minor findings and residual coverage

Before hash binding, the reviewer requested two final consistency repairs:
the reference paragraph now calls (6)--(7) a sector construction, not a
full-state construction; the ledger's primitive-orbit row now points to
Section 6, not Section 5. Root made these exact repairs, and the reviewer
checked the changed strings before computing the hashes below.

No unresolved mathematical weakness was found within the bounded remit.
The coverage for that statement is the natural-extension reconstruction,
uniform period estimate, unbounded constant image, regular-period/divergence
argument, sector boundedness, weak-star subnet and spectral implication,
and owner/claim boundaries listed above. It is not a correctness guarantee
or a survey ruling out all analytic constructions.

## Source and verification scope

The reviewer independently accessed
[Shirbisheh, Lectures on C*-algebras, arXiv:1211.3404v2](https://arxiv.org/pdf/1211.3404):
Theorem 2.0.4 and Theorem 2.4.24(iii), with adjacent compact-spectrum text,
support the standard weak-star compactness and complex-Banach compact-spectrum
steps. Proposition 2.4.15 was also inspected, but adjoint compactness is not
needed by the final proof. These are localized source checks, not a full-book
read or evidence for the new physical construction. A separate attempt to
fetch the Leiden course record timed out; this review does not treat that
attempt as independent verification of that additional reference.

This is a symbolic mathematical review, with no finite orbit sample,
floating-point experiment or empirical statistic. There are no recomputable
statistics of the statistical procedures described by ARS. The reviewer
verified the displayed algebra and exact inequalities directly, then used
`sha256sum` on the four final author files. Root retains ownership of the
integrated Markdown/link/status check; this review does not predeclare its
result.

## Reviewed author-file SHA-256 bindings

These bindings cover the final text reviewed, after the two minor repairs.
The evidence index is deliberately not bound because root may append the
final mechanical verification receipt there.

| File relative to this review | SHA-256 |
| --- | --- |
| [README.md](../README.md) | `0bcbb66ba5ef7fe56d771f2209c5451edc0c1306ac6e78552bcf8529bdeebcf4` |
| [candidate-card.md](../candidate-card.md) | `452175a732635e3d5e33a7b588227d096f0852f3e22059e134156692437dea42` |
| [paper.md](../paper.md) | `b627f673047f8efd1ee6aa2683b7ea8f6c22d221b7a0612647632d154a9d15b9` |
| [claim-ledger.md](../claim-ledger.md) | `b9ec1f87933978d44aa783fd7f0a5da5f9958d34ccc74d94e3a697a9fe63da90` |

Disposition: STOP the frozen full-state bounded-function transfer
architecture for the single decisive reason L_s1 is unbounded. Retain
the physical owner and its previously scoped orbit results without Route
credit. Any future analytic-category or owner change requires a fresh card.
