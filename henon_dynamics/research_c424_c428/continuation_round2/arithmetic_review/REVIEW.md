# Independent internal review of AR2-1

2026-09-08 UTC. Reviewer: current-team nonauthor of the arithmetic lane.
This is a substantive AI-assisted mathematical/source/increment review,
not human peer review, a publication decision, or a formal Route-A
evaluation. The coordinator retains admission authority.

## Three separate judgments

| Gate | Judgment | Meaning |
| --- | --- | --- |
| Frozen mathematics and separately read addendum | **PROVABLE AS STATED: complete parameterwise atlas** | The 64 rational labels and iff edge guards exhaust the frozen full Laurent family; the separate mixed-cycle restriction $a^2=1$ is also proved. No mathematical blocking defect was found. |
| Source applicability | **R1 CORRECTED AND READ BACK; bounded scope check closed** | The original audit incorrectly specialized a degree-at-least-three Ingram bound to degree two. The author removed that comparison and recorded the error; the reviewer verified both affected passages and the correction trail. |
| Independent paper increment | **AUXILIARY_ONLY; DO NOT ADMIT on the current package** | After C418 and classical sources are deducted, the residual is a useful but short two-place compatibility extension of the existing sign/offset architecture. Correctness does not make it a substantial independent paper under this batch's contract. |

The absence of a flattened mixed-cycle/parameter-stratum table is **not**
a missing implication in the theorem that was actually stated. Conversely,
an exact constant-size graph is not automatically enough independent
substance to count as another paper. These statements must not be collapsed
into either an invented proof gap or an automatic admission.

## Frozen artifact and actual review scope

The complete [author proof](../arithmetic/PROOF_PACKAGE.md), all 459 lines,
was read. A read-only SHA-256 check returned exactly the announced value:

```
66bca7ae41a1fe409e8c7967f5b37e2ce0e1c05ddabf439272a70857bc22aeb3
```

This is an integrity identification, not mathematical verification by hash.
Also read in full: [frozen question](../arithmetic/FROZEN_QUESTIONS.md),
[probe code](../arithmetic/mixed_sign_probe.py),
[saved result](../arithmetic/mixed_sign_probe_result.json),
[source audit](../arithmetic/SOURCE_AUDIT.md), and
[execution record](../arithmetic/EXECUTION_RECORD.md). Both existing PDF
preflight sidecars were read and retain `UNAVAILABLE`; no local PDF or
new local page anchor was used by this reviewer.

The closest predecessor's [contract](../../../continuation_c414_c418_round2/function_field/CONTRACT.md),
[complete 488-line proof](../../../continuation_c414_c418_round2/function_field/PROOF_PACKAGE.md),
and [source audit](../../../continuation_c414_c418_round2/function_field/SOURCE_AUDIT.md)
were read in full. Their proofs, not earlier favorable review summaries,
decide the C418 subtraction below. No C418/AM1 program, certificate or
manuscript build was rerun. C417, C412 and AM1 are acknowledged exclusions;
this review does not pretend to have freshly audited their entire proofs.

Repository/Hénon guidance, current-state prefix, active continuation plan,
batch skill/workflow, research-review and proof-writer instructions were
read. The batch's authorized current-team fallback replaces the legacy
external-model example in research-review; no external review upload or
paid call occurred. Bounded primary-source verification follows the
already-read research-lit/ARS fact-check scope, not a full research pipeline.

## Exact object that survives review

For every field $k$ with $\operatorname{char}k\ne2$, every $a\in k^*$,
every nonconstant $c\in k[t,t^{-1}]$, and transcendental $t$, the domain
is all of $k(t)^2$ under one native application of

$$
H(x,y)=(y,y^2+c-a x).
$$

Only ordinary rational periodic points are counted. The method does not
pass to an algebraic closure or completion, discard characteristic three,
identify signs, assume separability of $t\mapsto t^m$, or impose a period
cutoff. The one-pole branches are supplied by C418 and inversion of $t$.
The new theorem's numbered reduction treats the genuine two-pole branch.

Here a finite field-arithmetic criterion means coefficient equalities
and square-existence tests in the given field, not a claim that arbitrary
abstract fields have a computable presentation or a uniform square-root
algorithm. This interpretation preserves the mathematical quantifiers.

## Mathematical reconstruction and adversarial checks

### 1. All rational coordinates and both principal parts

At a prime different from $t$, a maximal pole of order $h>0$ would give
order $2h$ in $y_i^2+c$ and at most $h$ in its two neighbors. Thus no
such pole exists. At either parameter pole, the maximal-order argument
forces every coordinate's order to be half the parameter order. This
works separately in each orbit and depends only on $c$, so it also
justifies using the same principal parts across coexisting orbits.

The descending positive-coefficient recursion divides only by twice a
nonzero leading coefficient. Negative powers enter a product with the
positive principal part only below its top degree; a constant enters
at that degree, not above it. Hence neither interferes with the equations
from degree $2m$ down to $m+1$. The negative recursion is the corresponding
argument at zero. Therefore every periodic coordinate is uniquely

$$
y_i=e_iU+d_iV+b_i,\qquad e_i,d_i\in\{1,-1\},\ b_i\in k.
$$

The functions $U,V,1$ are linearly independent by their extreme exponents.
No derivative of $t^m$ is taken anywhere. In particular, characteristic
dividing $m$ does not invalidate this reduction.

### 2. Cross-orbit compatibility, not just within one word

Subtracting the recurrences of any two periodic coordinates puts their
square difference in $\operatorname{span}_k(U,V,1)$. Different sign products
give a nonzero coefficient $\pm4$ of $UV$. Its largest exponent is below
$\deg U$ and its smallest exponent is above the least exponent of $V$.
Thus membership in this span forces $UV\in k^*$, and the two extreme
product exponents force $U=u t^m$, $V=v t^{-m}$.

This is a genuine globally quantified compatibility statement, including
different cycles. The proof does not assume the entire periodic set is
already finite. If $UV$ is nonconstant, at most one sign product can pass
the square-completion identity: two passing products would again force
$UV$ into that three-dimensional span and hence make it constant.

After a passing square completion, the equations depend only on $P,1$.
Reading C418 Steps 4--8 confirms that its seven-row proof thereafter uses
only this independence, not polynomial integrality. All its rows and
small-characteristic overlaps therefore transfer to Laurent $P$ exactly
as stated. This branch is complete and inherited, not new classification
content merely because its base function is now Laurent.

### 3. The exceptional graph labels are injective in every allowed field

In the monomial-pair branch, the three coefficient equations (19) are
necessary and sufficient for the actual rational-function recurrence.
The first equation at two consecutive indices gives the two offsets
$B_0,B_1$ in (8). Thus all periodic points occur among the 64 labels.

From a label, independence of $U,V,1$ determines
$e_0,d_0,e_1,d_1,B_0,B_1$. One then recovers

$$
e_{-1}=\frac{2e_0B_0+\alpha-e_1}{a},\qquad
e_2=2e_1B_1+\alpha-ae_0.
$$

Since $a\ne0$ and $1\ne-1$, no two states have the same point. This
explicit reconstruction handles small fields as well as characteristic
zero; it does not rely on generic coefficients being distinct.

### 4. Both directions of the edge test

Expanding $H(E(s))$ gives the pair

$$
\bigl(e_1U+d_1V+B_1,\ e_2U+D_2V+B_2\bigr).
$$

If this is any target label, its two visible positive signs must be
$e_1,e_2$, its two visible negative signs must be $d_1,D_2$, and its
offsets must be $B_1,B_2$. The recovered preceding positive sign is
$e_0$; the recovered following positive sign is $E_3$. Therefore
$D_2^2=E_3^2=1$ is necessary and the target must be (12). Conversely
these two guards make all six target signs legal and make its offset
formulas exactly $B_1,B_2$. This proves sufficiency as well.

There is no missing separate negative-sign equation: the second guard
recovers the next offset-compatible positive sign, while the first
guard recovers the negative sign in the actual image. Future negative
compatibility is checked by subsequent edges around the cycle.

Invertibility of $H$ and label injectivity give indegree at most one.
Consequently graph cycles are precisely actual ordinary cycles, with
the same least period and no coexistence double counting. The finite
64-point and 64-period bounds are justified, although not asserted sharp.
The adjacency matrix in the ordinary-count/zeta identity should be
understood over $\mathbb Z$ (and its determinant over $\mathbb Z[z]$),
not reduced modulo the characteristic of $k$. Making that convention
explicit was a useful editorial clarification, not a proof repair; the
final addendum now supplies it, as recorded below.

### 5. The six-value assertion and the witness

Eliminating offsets gives (20) with the stated sign. Outside
$\{\pm1,\pm2,\pm1/2\}$ the nine expressions $\eta+a\theta$ are
distinct: any collision gives the displayed nonzero difference ratio.
This uses no division by three. It forces an alternating product word,
then two-periodic signs and offsets. A two-coordinate cycle satisfies
$(p-q)(p+q+a+1)=0$, so its two pole-sign products cannot differ.
The contradiction proves the necessary six-value restriction in the
frozen proof. It was not claimed sufficient or sharp.

The saved four-cycle is independently checkable without running its
producer: with $A=t-1/(4t)$ and $P=t+1+1/(4t)$ one has
$A^2=P^2-2P$. The two kinds of positions in $(A,-P,-A,-P)$ give,
respectively, $-2P$ and zero on both sides of the recurrence. The four
pair states are distinct in every characteristic different from two.
Thus the witness does refute the inherited-only shortcut. The probe's
11 tested systems and stopping at length four are consistent with its
saved output, but are not an exhaustive theorem or a reviewer rerun.

### 6. Coordinator's separate sharpening, not part of the frozen bytes

During review the coordinator supplied a stronger hand argument:

$$
\text{mixed product word}\quad\Longrightarrow\quad a^2=1.
$$

I independently checked that reasoning. For a maximal run of one product
sign, write $C_w=(\alpha-w\beta)/2$. A run of length at least three has
an interior giving $C_w=0$ and an endpoint giving a nonzero single term
$a e_{i-1}$, a contradiction. A run of length two has endpoint equations
$C_w=a e_{i-1}=e_{i+2}$, forcing $a=\pm1$. If $a\ne\pm1$, all runs
therefore have length one. The product word alternates, and the four
values $\pm1\pm a$ are distinct. Equation (20) fixes the two neighbors'
signs in each product class, giving a two-periodic coordinate word and
the same contradiction as above.

This is valid in every allowed characteristic. It strengthens, rather
than corrects, the frozen six-value assertion. It is credited to the
coordinator, not retrospectively attributed to the frozen author proof.
An author addendum was requested separately; no unseen addendum is
counted as reviewed in the initial record. Subsequently the complete
initial [120-line addendum](../arithmetic/ADDENDUM_MIXED_DETERMINANT.md) was
actually read. Its proof is exactly the valid run argument reconstructed
above. Its consequences are also correct: at $a=\pm1$ the necessary
coefficient set is the field image of $\{-2,-1,0,1,2\}$; outside these
determinants all cycles are pure; and an ordinary period greater than
two anywhere in the full Laurent family requires $a^4=1$, combining
this result with the inherited rows. **The addendum is PROVABLE AS
STATED**, with no blocking correction found. Its actual SHA-256 is
`fce7e2d970c6465e58341d9c53041e6405e5427cd02bf07535ac74abc79d3d0f`;
the main proof's announced hash was confirmed unchanged at that check.
This does not make the coefficient condition sufficient. The strengthening remains a short
combinatorial consequence and does not change the paper-level judgment.

**Final editorial readback.** Before the author's stop took effect, the
addendum gained an integer-adjacency convention and a scoped admission
paragraph. The resulting 140-line file has actual SHA-256
`28de90b5dc90acf646cea981afc188078aa3194816664539b178cac96ef6cf93`.
The earlier `fce7...` identity above accurately identifies the 120-line
mathematical version reviewed first; it is not the final file hash.
The newly added ending was actually read: guards are evaluated in $k$,
but $A$ and $\operatorname{tr}(A^n)$ are over $\mathbb Z$, and the
determinant/zeta convention is the ordinary one. This closes the optional
counting clarification without altering labels, guards or the mixed-cycle
proof. The stated auxiliary disposition does not reopen a mathematical
gap. **The final addendum review is closed**, with no new mathematical
execution or need to rerun the full unchanged proof.

## Primary-source applicability and the required correction

Three primary PDFs were opened directly and the relevant bodies, not just
search snippets, were inspected. No fresh broad search or worldwide
priority assertion was made in this review. These are source-scope
checks; clinical study levels and sample metrics are inapplicable.
Journal indexing, ORCID, retraction and comprehensive COI checks were
not performed and are not marked PASS.

### S1 / required correction R1: Ingram's degree boundary

The [accessed Ingram v1](https://arxiv.org/pdf/1111.3609v1) states
Theorem 1.2 in the source normalization corresponding to $a=-1$ here.
Its introduction, Section 3's opening and concluding argument, and
Lemma 4.2 with proof were checked. Section 3 explicitly assumes
$d\ge3$ and routes quadratics separately through Theorem 1.4. Therefore
the audit's original substitution $d=2,s=2$ into $(3d^6)^s$ to claim
36864 is unsupported by that proof. The required correction was to remove
that numerical comparison and its cross-reference, retaining scoped finiteness and
bad-place/half-pole ownership. This is not a claim that 36864 is false,
only that the cited derivation does not establish it. C418's old source
audit already records the same degree warning. The atlas itself does
not use that bound.

At initial review the author and coordinator were notified of R1.
The author audit's original lines 50--53 and explanation at lines 115--118
were the affected locations. The author subsequently removed the numeric
comparison, made the degree restriction explicit in both passages, and
added acknowledged correction records in the source audit and execution
record. All those changed passages were actually read back. **R1 is
closed**, with no replacement unsupported numerical bound and no hidden
rewrite of the original mistake. The frozen mathematical proof is
unaffected. This closes the identified source-scope defect, not a global
bibliographic certification or the independent materiality gate.

### S2: Gauthier--Vigny

The [v1 definitions, Main Theorem and following corollary](https://arxiv.org/pdf/2010.16291v1)
were checked. The characteristic-zero nonisotrivial regular-automorphism
finiteness statement applies here. The author's fixed-point trace
product test is valid: the two fixed-coordinate roots have product $c$,
so the conjugacy-invariant product of their Jacobian traces is $4c$,
which cannot be constant. The corollary therefore owns bare finiteness
in this branch; it does not state the Laurent point labels or mixed-sign
compatibility theorem. No full published-proof audit is claimed.

### S3: Allen--DeMark--Petsche

The [primary v3 PDF](https://arxiv.org/pdf/1610.04271) was checked at its
field assumptions, parameter region and Theorem 28 with its proof. The
source's complete locally compact field and odd residue characteristic
hypotheses remain essential to this comparison. The conjugacy
$(x,y)\mapsto(-y,-x)$ gives parameters $(-c,-a)$ as stated. The source
owns the local two-sided binary horseshoe, not the global $k(t)$-rational
intersection or these finite rational labels. Its preparatory lemmas
were not all reread; no full-paper review is claimed.

## C418 subtraction and independent substance

| Component in AR2-1 | Ownership / residual assessment |
| --- | --- |
| Ordinary clock, recurrence, good-place pole escape | Existing/classical setup and method |
| One-pole positive and negative parameter families | C418, with $t\mapsto1/t$ for the second |
| Offset equations after one common sign product | Exactly the C418 coefficient system |
| Seven pure rows, ordinary lifts and their exceptional-characteristic overlaps | C418 in full; the Laurent substitution adds no rows |
| Finite graph injection, inverse-map indegree proof, trace/zeta consequence | Existing proof architecture and elementary packaging |
| Opposite global products force a constant $UV$, hence a monomial pair | Genuine new compatibility lemma relative to the inspected predecessor |
| Five-term parameter form and 64 labels with two guards | Correct explicit extension of the same finite-memory construction |
| Six-value restriction, strengthened separately to $a^2=1$ | New short compatibility consequences, not a completed exceptional-stratum classification |

There is real mathematical progress: the one-pole rigidity shortcut is
false for Laurent parameters, and the proof correctly finds and controls
the additional behavior. Calling the entire result merely identical to
C418 would be inaccurate. It also does substantially more than state a
finite cardinality bound: every input parameter has a complete finite
point-and-cycle reconstruction.

Nevertheless, the *remaining independent increment* is small under this
batch's stricter substantial-paper contract. The key new global step is
one square-difference/span argument followed by the elementary Laurent
unit classification. Once that is available, most parameters return to
C418 unchanged. On the exceptional monomial-pair family, adding two pole
signs and recovering two offsets yields the enlarged graph by direct
coefficient comparison, using the same injection and partial-permutation
strategy as C418. The determinant restrictions are short consequences
of these equations. The current package does not yet extract from that
graph a substantial new structural classification of mixed parameter
loci, coexistence phenomena or sharp arithmetic restrictions beyond those
compatibility lemmas.

This judgment is about theorem content and dependency, **not** the number
of proof pages, the number 64, search volume, or whether the result would
be publishable somewhere. A concise theorem can be substantial; this one
currently functions most naturally as a Laurent companion to C418.
Source absence cannot establish the missing materiality.

A proven full mixed-stratum/least-period/coexistence classification, if
it reveals genuinely new structure, could warrant a later reassessment.
It is not logically required to make the existing graph theorem true,
not an automatic guarantee of paper admission, and not authorization
for a larger census. Merely printing the same graph or more parameter
examples would not answer this concern. The present review recommends
retaining the complete theorem as **AUXILIARY_ONLY**, with no new paper
slot and no weakening of the already proved mathematical status.

## Stop and verification boundary

The reviewer ran zero mathematical programs, zero new or old probes,
zero censuses, zero builds and zero formal evaluations. Read-only file
inspection, frozen-proof/addendum integrity identification and primary-source
browsing were used. Only this reviewer-owned file was written. A separate current-team
nonauthor read the full author proof and independently reconstructed the
64-label injection and both directions of the edge criterion. Their
returned reasoning was read: it recovers the same six signs and offsets,
checks $D_2^2=E_3^2=1$ iff a target label exists, and explicitly retains
characteristics dividing $m$. They found no mathematical defect in that
bounded target, ran no program and wrote no file. This is a supplementary
algebra check, not a second source/increment review or admission vote.

No source arithmetic, finite trace or rational zeta here implies target
Euler factors, root numbers, automorphy, target divisor correspondence,
or a Hilbert--Pólya realization. `NO_BAD_EULER_OR_ROOT_NUMBER` remains
unconditional. No formal route grade, manuscript admission or batch
completion is implied by this report.
