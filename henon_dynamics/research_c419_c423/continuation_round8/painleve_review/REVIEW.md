# P7 independent mathematical review

2026-09-08 UTC. Reviewer: arithmetic delegate, separately assigned by the
root coordinator. Author: the characteristic-p delegate. Review-only
output; no author proof, source file or global status was changed here.

## 1. Verdict and exact scope

**PASS: the complete original P7 upper-bound claim is proved by the
reviewed package. No remaining mathematical correction is required.**

The conclusion is for every finite field $k=\mathbb F_q$, every
$s,t_0\in k^*$, every phase order $r=\operatorname{ord}(s)$, and every
ordinary state in the original torus-plus-four-lines domain. For its
least native period $\ell$,

$$r\mid\ell,\qquad \ell/r\le q+1+2\sqrt q.$$

This verdict is not restricted to generic fibres, prime fields, odd
characteristic, nonzero exceptional-line coordinates, or small $r$.
It is not an admission, a worldwide novelty clearance, or an external
peer-review certificate. The coordinator retains those decisions.

Reviewed inputs:

- the full [original P7 contract](../../continuation_round7/charp_scout/FROZEN_CONTRACTS.md#p7--finite-field-q-painlevé-i-uniform-native-periods),
  including all seven branches;
- the full [round-eight freeze](../painleve/FROZEN_ATTEMPT.md);
- the entire [author proof](../painleve/PROOF_PACKAGE.md), initially
  572 lines, then the two explicitly identified editorial/denominator
  clarifications leading to the reviewed 573-line version;
- the full 158-line [source ledger](../painleve/SOURCE_LEDGER.md);
- the actual primary sections listed in Section 7 below.

The review was not blind. The author sent the mechanism outline while
writing, and the reviewer independently reconstructed the lattice and
face-endpoint equations and sent a corroborating, explicitly provisional
message before the full-file handoff. The reviewer did not coauthor or
edit the proof. The final verdict is based on the complete saved argument
and primary-source inspection, not that earlier outline.

## 2. Exact state domain and native map: checked

The four corner blowups are $E_2,E_4,E_5,E_7$ in the author's indexing;
$E_5$ is the second blowup over $(0,0)$, at a boundary node. The remaining
four blowups are at smooth boundary points. Nonzero $s,t$ ensure that
none of these latter centres collides with a node, in any characteristic.
This yields precisely the eight $(-2)$ curves in author equation (2),
with their displayed cyclic intersections, and
$D=-K_S=2H_x+2H_y-\sum E_i$.

The accessible curves are exactly $E_1,E_3,E_6,E_8$ minus one point each.
Their local coordinates agree with the source's four charts. Intermediate
exceptional curves are in the removed divisor, not additional ordinary
states. Every finite coordinate on each accessible line remains in $U$.

I substituted the native torus formula into each of the five extension
rows in Section 2.1. All identities check. For example, on input $L_2$,
write $A=t+uv$ and $B=su^2A-1$. Then the target $L_3$ coordinate is
$a=uAB/t$, and its second coordinate follows from

$$
t-AB^2=u\bigl(-v+2suA^2-s^2u^3A^3\bigr).
$$

This verifies the potentially delicate expression with $B^3$ in its
denominator. The denominators are units at every input-line point;
the coefficients $2$ and $3$ are not inverted. The last $L_4\to L_1$
formula is regular even at $v=0$, and gives the stipulated zero-line
branch there, not an omitted pole.

I also checked all seven inverse-state rows. In particular the inverse
of an output $L_4$ coordinate $W$ at phase $T$ is the $L_3$ coordinate
$T(W+s)/s^3$ at phase $T/s$. This has the correct power of $s$.
Thus the finite phase-union is genuinely permuted and has no tails.

## 3. Boundary lattice, adjunction and uniform poles: checked

For an integral curve disjoint from $D$, solve the eight orthogonality
equations in the integral Picard basis. In the author's parameters the
solution is exactly

$$
a=2u,\ b=u+v,\ m_1=2v-u,\ m_2=m_3=v,\
m_4=m_5=m_6=u,\ m_7=m_8=2u-v.
$$

Independent substitution into $2ab-\sum m_i^2$ gives
$-8(u-v)^2$. Since $K_S\cdot Z=0$, adjunction gives
$p_a(Z)=1-4(u-v)^2\ge0$. Hence $u=v$ and $Z\sim dD$.
The conclusion is integral linear equivalence because this is the actual
free Picard basis, not merely a real intersection space. Ample
intersection forces $d>0$. Characteristic two does not reduce the
integer intersection number $8$ to zero.

The uniform-pole lemma also checks. Choosing a constant avoiding the
finitely many constant boundary residues ensures the zero divisor has no
boundary component. Its intersections with the eight boundary curves are
nonnegative and sum to zero. The cycle Laplacian then forces every polar
multiplicity to equal one positive integer $m$. This argument is over
the algebraic closure, an infinite field; it does not need to choose
such a constant inside a small finite field.

The resulting zero and pole divisors are disjoint by positivity of local
intersection multiplicities. Thus the claimed map to $\mathbb P^1$ has
no unresolved base point. Every finite fibre is disjoint from the whole
boundary, not merely from its generic points.

## 4. Minimal-pole obstruction: checked without a characteristic shortcut

The eight toric valuations give precisely the polygon

$$
\operatorname{conv}\{(-m,0),(0,m),(m,0),(m,-m)\}.
$$

There is no hidden cancellation issue: along a toric boundary, different
monomials of the same valuation are different Laurent characters. The
unique top-$y$ vertex has nonzero coefficient because its boundary pole
order is exactly $m$.

I checked all four face polynomials using the actual blowup coordinates.
In particular $E_6$ uses the valuation $a+2b$ and coordinate
$v=x^2/y$; it is not interchangeable with the earlier $(0,0)$ blowup.
Regularity at an accessible exceptional divisor forces multiplicity at
least $m$ of the numerator at its blowup centre. Restriction to the
boundary gives divisibility by the $m$th power of the corresponding
linear factor, even when binomial coefficients vanish in the field.

With the author's vertex names $A,B,C,E$, the four relations are

$$
C=(-1)^mE,\quad A=(-t)^mB,\quad A=(-t)^mE,\quad C=(-s)^mB.
$$

Since $tB\ne0$, these imply $E=B\ne0$ and $s^m=1$.
No derivative, factorial, complex period, or division by $m$ occurs.
Thus $r\mid m$ is justified for every possible pole order, including
ones divisible by the characteristic.

## 5. Source invariant, specialization and all finite fibres: checked

The explicit matrix and trace in equation (11) agree with the source's
proved integral after setting the irrelevant gauge variable to one.
The invariant identity is an identity over the cyclotomic integer ring.
Because $r\mid q-1$, the cyclotomic specialization exists with $p\nmid r$.
Clearing powers of $x,y,t,s,sx-y$ is legitimate on the generic torus
with $s,t$ units; no integer denominator or smooth-fibre specialization
is assumed. The final author clarification makes this denominator list
explicit.

The forward chart morphisms carry the generic point of each accessible
line to a torus after at most four steps, with nonzero line-coordinate
slopes. Invariance therefore excludes a pole along each accessible line.
All other prime divisors of $U$ meet the torus. Normality of the smooth
surface then excludes a pole supported only at a special closed point.
This is a valid codimension-one extension argument, not a pointwise
evaluation of a formula with zero denominators.

The leading $x^{-r}$ coefficient is independently reproduced by the
idempotent matrix $V$ in Section 5.3. It is $-t^r\ne0$ in every allowed
characteristic. Thus the exact polar divisor really is $rD$.

For an arbitrary finite geometric fibre, write its divisor as
$\sum n_jZ_j$. The preceding lattice lemma gives $Z_j\sim d_jD$ with
$d_j>0$. Each such *linear* equivalence supplies a rational function
with poles exactly $d_jD$, so the minimal-pole lemma applies separately
to every component. The equality

$$\sum n_jd_j=r,\qquad r\mid d_j$$

then forces one component with multiplicity one. This is the decisive
all-fibre step: irreducibility is not inferred from a generic example.
The fibre is Cartier in a smooth surface and therefore has no embedded
associated points; generic multiplicity one makes the entire fibre
reduced. Adjunction gives its arithmetic genus one.

This also disposes of reducible component permutations and multiple
finite fibres. No classification of translations, Kodaira types,
quasi-elliptic fibres, or spectral-to-dynamical identifications is needed.

## 6. Singular fibres, rational points and the clock: checked

A smooth fibre containing an ordinary state has a rational point and
is an elliptic curve, so the usual all-finite-field Hasse bound applies.

For a singular geometrically integral arithmetic-genus-one fibre, the
normalization sequence gives $1=g+\sum\delta_Q$. There is therefore
exactly one geometric singular point and the normalization has genus
zero. Every smooth rational point has a unique rational lift. A
genus-zero smooth projective curve with a rational point is $\mathbb P^1$;
if it has no rational point, its point count is zero. Consequently
$\#C(k)\le q+2$, without assumptions on node splitting or the presence
of a smooth rational orbit point. This is sufficient in every $q\ge2$.

Finally $t\ne0$ makes the phase period exactly $r$. The native least
period is a multiple of $r$, and the return map at a fixed phase has
least period exactly $\ell/r$. Those are distinct ordinary points of
one finite fibre. This proves the original bound, not a scheme-length
or Frobenius-count replacement.

## 7. Primary-source and substantive-delta assessment

Freshly read for this review:

- [Joshi–Roffelsen v2](https://arxiv.org/html/2508.18578v2): introduction
  and Conjecture 1.2; Sections 2.1--2.2 with every chart and branch;
  Section 3.1 including the full integral proof; Section 3.2 and conclusion.
  The target and genus assertions are explicitly conjectural in the
  accessed body. The actual invariant theorem is used, not either conjecture.
- [Carstea–Takenawa v2](https://arxiv.org/pdf/1005.3586v2): introductory
  surface/index definitions; Section 2, Theorem 2.2 and proof;
  Remark 2.3 and the opening of Section 3. This establishes prior
  ownership of the root-of-unity Halphen mechanism, with a complex
  period-map/deformation proof in the inspected result.
- [Sutherland, Lecture 7](https://math.mit.edu/classes/18.783/2021/LectureNotes7.pdf):
  Sections 7.1--7.2 and Theorem 7.3. The theorem has no odd-characteristic
  restriction; the subsequent character-sum example is separate.
- [Stacks delta invariants](https://stacks.math.columbia.edu/tag/0C3Q),
  particularly Lemmas 33.39.2--33.39.4, and
  [genus versus geometric genus](https://stacks.math.columbia.edu/tag/0CE0),
  particularly Lemmas 53.18.2--53.18.4 and the normalization sequence.

The source-owned content is substantial and must remain credited: the
map, domain, invariant, conjectured upper bound and Halphen framework
are not new. After deducting that ownership, the reviewed package still
contains a genuine complete proof obligation absent from the inspected
statements: the finite-characteristic minimal-pole calculation and
the lattice-based exclusion of every reducible or multiple finite fibre.
It is not simply “an invariant exists, therefore Hasse applies.” It
closes the unchanged full P7 question, unlike an autonomous or generic
helper. The techniques themselves are classical; this review does not
declare worldwide originality or replace the coordinator's independent
current-literature/substantiveness gate.

The proof does not establish the bin distribution, proposed discriminant,
or generic smoothness in all characteristics. Those are not required by
P7 and were not silently used.

## 8. Corrections and execution receipt

During review the author fixed the displayed `\qquad` rendering in (15)
and explicitly included powers of $t$ in the allowed specialization
denominators in Section 5.1. Both corrected passages were inspected.
These are clarifications, not repairs to the central geometric proof.
No further mathematical correction is requested.

Reviewer mathematical program executions: **0**. All checks above were
hand derivations and primary-source reads. Reviewer search-query
submissions: **0**; direct primary opens do not duplicate the author's
seven queries or the coordinator's separate novelty queries. No census,
old mathematical rerun, saved source PDF, GPU, external model, Git
mutation, manuscript, or global-index edit occurred. Only this review
file was written in the separately assigned `painleve_review/` lane.

The batch skill retained the full-claim gate; proof-writer kept the
all-characteristic proof and singular-stratum obligations explicit;
research-lit and bounded source verification kept prior ownership
separate from the new proof. NO_BAD_EULER_OR_ROOT_NUMBER is preserved.
