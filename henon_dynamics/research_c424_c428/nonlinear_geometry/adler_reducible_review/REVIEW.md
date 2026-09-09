# NL424-3 reducible-boundary independent review

2026-09-08 UTC. Current-team nonauthor review under the repository adaptation
of `research-review`; no external-model or human-peer-review claim. This is
only the requested bounded branch, not an independent audit of the smooth
or irreducible-singular packages and not admission of the original contract.
Only this review directory was written. No mathematical program ran.

## Verdict and precise scope

**No blocking mathematical defect or counterexample was found.** The draft
correctly proves geometric reducedness of every invariant fibre, the exact
geometric reducibility criterion, and the complete ordinary rational
periodic-point classification on all reducible fibres. The three ordered
coincidence cases have the stated different native periods and intersection
actions. The twelve-cycle example is valid on the factorwise two-sided domain.

**Substantive judgment: retain this boundary atlas as an auxiliary part of
the single full Adler contract, not as a standalone paper.** Its completeness
is useful, especially for preventing pole/clock/intersection errors, but
after classical inputs are deducted the residual is explicit cubic
factorization and one-variable projective dynamics. The complete NL424-3
contract needs a separate integrated proof/source/substance decision. This
bounded positive mathematical review does not supply that decision.

One nonblocking presentation addition is recommended for integration: write
the full integer-iterate infinity orbit once, as below, so that the exact
two-sided survivor domain is explicit even in the infinite-order case.
The draft's existing periodic classification already excludes those points
correctly, so this is not a missing periodicity argument.

## Inputs read and integrity

Read all 214 lines of ADLER_REDUCIBLE_PROOF.md, all 57 lines of
ADLER_FOLLOWUP_PLAN.md and all 106 lines of FROZEN_SCOUTS.md, including the
original NL424-3 parameter/domain/invariant/clock quantifiers. Also read the
Adler regularity and primary-source entries of the initial scout report.
The following hashes were checked before and after the hand review:

| Input | SHA-256 |
| --- | --- |
| ADLER_REDUCIBLE_PROOF.md | `2c35e6f079af5598dea30d295d56f5c1c2898e26dbc4583f989d88d2d8a6699c` |
| ADLER_FOLLOWUP_PLAN.md | `36ab4fa329c032057d7de62c297ceab6529220d10a8927dcf42b838e9a18b6ef` |
| FROZEN_SCOUTS.md | `a44743719d556af4683075113306fc703fb2d8c93010f51b09aac9415512b588` |

## 1. Geometry and native factors

The invertible pair-sum transformation, inverse transformation, invariant
polynomial and signs in both ordered factors check directly. In particular
the first factor fixes u and the second fixes w; no parameter permutation
is silently inserted. Their preservation of F follows by multiplying out:
for A, the product term changes by b(v-w)-b^2/u while b*v changes by its
negative. For B the cancellation uses e=b-a. When the relevant difference
vanishes the operation really is a global swap, not a swap with a retained
artificial pole.

Each regular factor is an involution whose image has the same nonzero
pair sum. Thus reversing a finite closed sequence of regular factors gives
a regular inverse sequence. This justifies using finite closed words to
certify the two-sided native domain, without extending a simplified T.

The cubic's leading binary form is -UV(U+V), squarefree over the algebraic
closure. The proposed repeated-factor contradiction is valid for an affine
nonconstant factor: its highest-degree part is nonconstant and its square
would divide that binary form. Homogenization creates no infinity component.
The infinity points are also nonsingular: the relevant (U,V) gradients
are respectively (0,-1), (-1,0), and (1,1).

For a geometric line component, its leading direction must divide the same
binary form. Substitution of u=r or v=r forces r=0. Substitution of u+v=r
has quadratic coefficient -(t-r), so r=t, then a=b and c=-bt. This excludes
nonrational translated lines as well as omitted rational lines. A reducible
geometric cubic necessarily has such a line, completing the iff proof.

In the exactly-two-equal cases the remaining conic is projectively a
nonzero product equation, hence smooth. Its two infinity points differ from
the line's infinity point. With all parameters equal, the reducible level
is exactly uvw=0; t=0 makes three concurrent but still distinct lines.
Intersection multiplicity and nonreducedness are not being confused.

## 2. Independent two-sided-domain calculation

For any d!=0 define

`M(r)=t+d/r`, `D_Z(M)={M^j(infinity): j in Z}`.

It contains infinity, 0 and t. The full two-sided survivor parameters on
each displayed component are exactly `P^1(Q) minus D_Z(M)`, with ordinary
intersection points identified rather than counted twice. If M has finite
order, D_Z(M) is precisely the finite D_M used in the draft. If M has
infinite order, this statement describes nonperiodic survivors too; its
only periodic parameters remain the rational fixed points.

The one-step checks underlying that assertion are:

| Ordered parameter case | Forward transfer restrictions | Inverse transfer restrictions |
| --- | --- | --- |
| beta_1=beta_2!=beta_3 | L: r!=0; C: z!=0 | L: r!=t; C: z!=0 |
| beta_1=beta_3!=beta_2 | L: r!=0; C: z!=0 | L: r!=t; C: z!=0 |
| beta_2=beta_3!=beta_1 | L: r!=0; C: z!=0,t | L: r!=t; C: z!=0 and tz+b!=0 |

All parameters in this table are finite. The first two conics additionally
lose z=t after forward continuation because it maps to the forbidden line
parameter 0; it is not a new one-step pole on those conics. In the third
case the inverse checks are the original B denominator w=-b/z and then the
original A denominator t+b/z. Thus the additional condition tz+b!=0 is
real, but its excluded point is already in D_Z(M). For t=0 this condition
is automatic since b!=0; no division by t is needed.

For the first two cases put d=a and d=-b respectively and J(r)=-d/r.
Then L(r) maps to C(J(r)), C(z) maps to L(t-z), and

`J M J=M^(-1)`, `J(infinity)=0`.

Consequently J preserves D_Z(M). Both the even-return poles and the
intermediate component-transfer poles give exactly that one orbit, not an
unrelated second deletion set. For the third case the two component maps
are M and M^(-1) themselves. Their missing affine charts and both factor
poles also have precisely this saturated orbit. This proves necessity and
sufficiency of the claimed two-sided-domain description.

In particular the review did not test only the simplified rational whole
map or assume that being initially in an affine chart implied survival.

## 3. Möbius order, intersections and native clock

The rational finite-order classification is correct. The projective matrix
is never scalar and has determinant -d!=0. A finite nontrivial eigenvalue
ratio gives a rational algebraic integer `2+zeta+zeta^(-1)` in [0,4]. The
distinct-eigenvalue cases 0,1,2,3 give orders 2,3,4,6; value 4 is the
nonidentity unipotent case here and has infinite order. Conversely the
four displayed parameter conditions give those exact orders.

A nonfixed periodic point of a nonidentity projective transformation has
the full finite order: in diagonal coordinates only the two eigenpoints
can have smaller periods, and a nontrivial translation has no finite
orbit off its unique fixed point. This argument has no period cutoff.

The fixed parameters satisfy `r^2-tr-d=0`, exactly the ordinary line-conic
intersection equation. They are finite, nonzero and different from t,
and are outside D_Z(M). In the first two cases, T acts on the roots as
`r -> t-r`; distinct rational roots form one ordinary two-cycle and a
double root is one fixed point. In the third case each ordinary root is
fixed. Nonrational roots give no rational intersection point. No extra
point is created by tangency multiplicity or normalization branches.

Off these intersections, the first two cases exchange distinct components.
A return must have even length, so a least M-period m becomes exactly 2m.
In the third case the components are preserved, so it stays m. With all
three parameters equal the globally regular cyclic permutation has only
periods 1 and 3, on every level. This includes the concurrent triple-line
origin and points with vanishing pair sums.

The reducible-fibre period inclusion `{1,2,3,4,6,8,12}` is therefore correct.

## 4. Adversarial hand checks and the twelve-cycle

The following possible failures were tested analytically, not by a scan:

- A hidden geometric/nonrational line: the three-direction coefficient
  comparison forces exactly the stated lines over the algebraic closure.
- A concurrent nonreduced fibre: t=0, a=b=c=0 is three distinct lines,
  despite its triple ordinary intersection.
- A tangent intersection counted twice: in Case 4, t=2 and a=-1 give the
  single fixed point (u,v,w)=(0,1,1), or (x_1,x_2,x_3)=(0,0,1). Here the
  cancelled A pole at u=0 must not be reinstated.
- A fixed Möbius parameter incorrectly given the generic native period:
  in Case 4, t=0 and a=1 yield intersection parameters +/-1 exchanged by T,
  hence period 2, while the nonintersection period is 4. In Case 6, t=0
  and b=1 make the corresponding two intersections individually fixed.
- A missing inverse second-factor pole in Case 6: tz+b=0 is excluded by
  the same D_Z(M), including the t=0 edge case just described.
- A spurious finite order at a repeated eigenvalue: d=-t^2/4, t!=0 gives
  a nonidentity parabolic map, with only the intersection fixed point.

For the proposed beta=(0,0,-1/3), t=1 example, direct hand iteration gives
the following alternating component parameters:

| Even tick 2j: line r | Odd tick 2j+1: conic z=1/(3r) | Next line parameter |
| --- | --- | --- |
| 2 | 1/6 | 5/6 |
| 5/6 | 2/5 | 3/5 |
| 3/5 | 5/9 | 4/9 |
| 4/9 | 3/4 | 1/4 |
| 1/4 | 4/3 | -1/3 |
| -1/3 | -1 | 2 |

The six line parameters are distinct and not 0 or 1; every conic parameter
is nonzero. On the conic its w coordinate equals the preceding line r,
also nonzero. Thus both the forward and reverse B operations are regular,
and A is the everywhere-defined equal-parameter swap. The intersection
discriminant is -1/3, so there is no rational component intersection that
could shorten an odd return. The starting inverse pair-sum coordinates are
exactly (-3/2,3/2,1/2), with S=1/2 and h=0. This certifies ordinary native
least period twelve, without a mathematical program.

## 5. Source subtraction and substantive boundary

After the local definitions/source entries were inspected, two primary
sources were opened directly; no new search-query sweep was performed:

- [Veselov, math/0205335v2](https://arxiv.org/pdf/math/0205335v2): read the
  transfer definitions/theorem, three-site order, factorization/isospectral
  discussion and Adler formula (11), especially PDF pages 4--7. The source
  owns the map, transfer construction and generic integrability mechanism.
  Its fixed-site parameter and sign convention agree with this contract.
- [Kassotakis, SIGMA 2019/048](https://sigma-journal.com/2019/048/sigma19-048.pdf):
  read Proposition 5.3 and its proof, the relevant Corollary 5.7 passage and
  the three-site H_V recurrence in Section 5.2.1. Native transfer versus
  an extended transfer root is source-owned and changes the clock. This
  draft correctly keeps the former. No complete boundary-atlas theorem
  was inferred from those selected passages.

These were actual browser primary-PDF text accesses, not full-paper proof
audits or a local-PDF page-anchor certification. No unseen source theorem
was used. A bounded review cannot certify worldwide absence of the exact
atlas. There is no assertion that either source literally contains the
present exceptional-point table.

The substantive conclusion instead follows from the proof's actual
dependence: squarefree leading form, elementary line factorization, explicit
Riccati/Möbius reduction, rational projective finite-order classification,
and finite deleted-orbit bookkeeping. Component-return time and ordinary
intersection multiplicity are essential correctness details, not separate
new mechanisms or independently substantial paper contracts.

The two-involution/Poncelet-type translation mechanism and Mazur torsion
input of a future smooth-fibre integration must likewise be deducted.
Neither is needed to prove this reducible branch; this review does not
independently certify either smooth-fibre application. Adding them to this
boundary result does not by itself establish a new-method contribution.
The complete original Adler question may be assessed only after all its
quantifiers and native-domain cases are integrated and its remaining
result-level increment is explicitly identified.

## Handoff

Bounded mathematical review: no required correction. Recommended integration
clarification: include D_Z(M) and the inverse second-factor condition above.
Standalone boundary-paper recommendation: negative; preserve this complete
auxiliary proof within the single original contract. No smooth/singular
package, AM1 snapshot, shared state, TeX, release or Git object was modified.
No Route-A grade, target Euler factor, root number, automorphy or
Hilbert--Polya conclusion is asserted.
