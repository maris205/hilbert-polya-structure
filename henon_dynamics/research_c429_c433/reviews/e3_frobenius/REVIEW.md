# E3 nonauthor review: D2 Frobenius/native-cycle bridge

Date: 2026-09-09 UTC. This is an independent current-team, nonauthor
proof/source review, not human peer review or an external-model review.
The only authored artifact is this report. No mathematical program, old
certification, build, evaluator, Git operation, external-model/API upload,
or additional agent was used.

Reviewed in full:
[D2 proof package](../../lanes/d2_frobenius_native_bridge/PROOF_PACKAGE.md)
and [D2 report](../../lanes/d2_frobenius_native_bridge/REPORT.md).
The root/Hénon/batch instructions and SCOUT_PLAN were read. The relevant
C12 derivation and Frobenius-obstruction proof, C425 line-return and
level-count proofs, and the earlier two-clock collision record were read
as source subtraction, without reopening their completed certifications.

## Recommendation and criterion-bound judgement

**Mathematics: the stated Theorem D2 is proved. No mathematical must-fix
was found. The stated positive control is valid.**

**Disposition: COMPLETE AUXILIARY OBSTRUCTION; do not admit it as an
independent C429–C433 paper on this evidence.** This is a recommendation
under the batch's substantial-question/source-subtraction criterion,
not a formal Route-A grade or a claim of journal rejection. The theorem
does settle the frozen question negatively; auxiliary disposition does
not mean its proof is incomplete.

The research-review and repository batch guidance governed claim scoping,
source subtraction and separate nonauthor output. Their old external-model
examples were not executed. ARS domain-review guidance was used only for
source applicability, evidence anchoring and contribution assessment; no
full five-seat ARS panel, calibration, venue alignment, or mechanical
editorial process is claimed. `NOT_CALIBRATED`;
`criteria_binding_unavailable` for any external venue.

| Criterion | Authority and evidence | Judgement | Limitation / decision bearing |
| --- | --- | --- | --- |
| Exact object, clock and quantifiers | SCOUT_PLAN; D2 Claim and Report's frozen question | Meets | Native tick is the whole ordered word; yes |
| Quantified proof including exceptions | Theorem D2 and Steps 1–5; independent audit below | Meets | Odd characteristic, odd prime-to-p torsion only; yes |
| Arithmetic ownership distinguished from native cycles | Theorem D2 parts 2–4; packet argument below | Meets | Reduced source points, not target prime owners; yes |
| Source subtraction | Source checks in §6 below | Meets for bounded audit | No worldwide-priority certificate; yes |
| Independent paper-level increment after subtraction | Batch workflow §2; standard quotient plus the displayed scalar/determinant argument | Does not meet on current evidence | Elementary consequence is useful but does not establish a substantial independent paper; yes |
| Target arithmetic/Route B | Explicit boundary in both D2 artifacts | Not assessed | No target mechanism supplied and no formal evaluation authorized |

## 1. Original contract versus what is actually proved

The frozen object is one fixed Cayley surface

\[
X:x^2+y^2+z^2-xyz=4
\]

over each fixed odd finite field \(\mathbb F_q\), with the native
automorphism \(T=s_zs_ys_x\), composed rightmost first. The arithmetic
action is the coordinatewise q-power map \(\Phi_q\). The original
question asks for a single extension exponent \(r\) making **every**
geometric primitive native cycle stable, without merging primitive
owners. Its stronger ownership demand asks that Frobenius be transitive
on each such cycle, so that the cycle itself is one closed point.

The theorem supplies smooth cycles \(O_N\), one for every odd
\(N\ge3\) with \(p\nmid N\), and proves two separate statements:

1. Their minimal setwise descent degrees \(f_N\) are unbounded at fixed
   q. Thus the weakest uniform requirement
   \(\exists r\ \forall O,\ \Phi_q^rO=O\) is false.
2. For each of these cycles separately, **every** Frobenius power that
   stabilizes it has rotation order at most two, whereas its native
   period is greater than two. Thus even
   \(\forall O\ \exists r\) cannot repair transitive ownership for
   this family.

This matches the frozen decisive counterexample criterion. It is not a
weakened finite-period substitute for that question. Conversely, it is
not a negative answer to all possible arithmetic carriers, all Fricke
parameters, all choices of cycles, or all kinds of descent data.

## 2. Quotient ownership, signs and the exact native word

**Evidence anchor:** equation: Proof Package, Step 1, the quotient,
three torus lifts and three exponent matrices.

The fibre calculation is correct over the algebraically closed field.
Equality of the first trace coordinates gives \(u'=u\) or \(u^{-1}\),
and independently \(v'=v\) or \(v^{-1}\). The difference between the
two potentially distinct product traces is
\((u-u^{-1})(v-v^{-1})\). If nonzero, only the simultaneous pair
survives; if zero, one coordinate is self-inverse and mixed inversion
already belongs to that same pair. Thus the fibre is precisely

\[
\{(u,v),(u^{-1},v^{-1})\},
\]

with repetitions removed. There are no independent coordinate signs and
no independently chosen signs at different prime factors of composite N.
The onto argument using the two roots of the z-quadratic is also valid.
Only this geometric fibre statement is needed; a stronger scheme-level
quotient theorem is not being assumed without proof.

Applying the three lifts in the stated order gives

\[
(u,v)\longmapsto(uv^2,v^{-1})
\longmapsto(u^{-1}v^{-2},u^2v^3)
\longmapsto(u^{-1}v^{-2},u^{-2}v^{-3}).
\]

Consequently column exponent vectors are acted on by

\[
M=\begin{pmatrix}-1&-2\\-2&-3\end{pmatrix},
\qquad \det M=-1.
\]

This is not a transpose/contravariance convention silently taken from
another paper. It follows directly from the point maps. One native tick
is this product, not one factor. All Laurent formulas are defined over
the prime field, so \(T\Phi_q=\Phi_qT\) is justified.

## 3. Smoothness, composite moduli, and least native periods

**Evidence anchor:** equation: Proof Package, equations (1), (8), and
Step 2's cyclic-vector matrix and M-squared.

For \(b=\zeta_N+\zeta_N^{-1}\), the equalities \(b=\pm2\)
would imply \(\zeta_N=\pm1\). This is impossible for the admissible
odd order \(N\ge3\). At \((b,2,b)\), the y-derivative is
\(4-b^2\ne0\). Each Vieta involution is an automorphism, so the
entire native cycle is smooth. In particular removing the four Cayley
nodes does not remove the witnesses.

The finite group \(\mu_N^2\) is preserved and permuted by the torus
automorphism. Thus these are genuinely periodic points, not merely
preperiodic ones. Let \(R=\mathbb Z/N\mathbb Z\) and
\(v=(1,0)^t\). The matrix with columns \(v,Mv\) is

\[
B=\begin{pmatrix}1&-1\\0&-2\end{pmatrix}.
\]

Its determinant is a unit for every odd N, whether prime, a prime power,
or composite. If a matrix C commuting with M annihilates v, it also
annihilates Mv, so \(CB=0\) and \(C=0\). This is legitimate
matrix invertibility over a ring, not invalid cancellation over a field.

Taking \(C=M^n-\epsilon I\), with the one common quotient sign,
proves the exact projective-order formula for \(n_N\). The first
off-diagonal entries are \(-2\), and those of

\[
M^2=\begin{pmatrix}5&8\\8&13\end{pmatrix}
\]

are 8. No admissible odd N divides 2 or 8. Therefore neither the first
nor second power is a scalar sign, and \(n_N>2\), including N=3.

All stated characteristic boundaries are sufficient. Odd p is explicit;
\(p\nmid N\) gives ordinary roots of exact order N; odd N supplies
the invertible determinant. Characteristic 3 has no extra exception
when \(3\nmid N\). The proof does not need to divide by the native
period, by f, or by the packet's cardinality, so periods divisible by p
cause no new defect. The omitted even-torsion and p-primary strata are
not classified; they are unnecessary for this counterexample.

## 4. Frobenius rigidity and closed-point ownership

**Evidence anchor:** equation: Proof Package, equations (2)–(7),
Steps 3–5.

By the geometric fibre criterion,

\[
\Phi_q^rP_N=T^sP_N
\iff (M^s-\epsilon q^rI)v=0
\iff M^s=\epsilon q^rI\pmod N.
\]

The last equivalence uses exactly the cyclic-vector argument above.
It also covers negative s because M is invertible over R. Determinants
then give \(q^{2r}=(-1)^s\pmod N\). Applying Frobenius twice
therefore sends the lift to its original simultaneous-inversion fibre:

\[
\Phi_q^{2r}P_N
=\pi(\zeta_N^{(-1)^s},1)=P_N.
\]

This last quotient step matters: the determinant congruence is stronger
than merely \(q^{4r}=1\), and it yields order two, not order four,
on the quotient cycle. Commutation propagates the identity to every
point of a stable O_N. Its rotation is consequently identity or a
half-turn, never a transitive permutation of more than two points.

A native cycle can be the full geometric support of one closed point
over \(\mathbb F_{q^r}\) only if it is setwise stable **and**
Frobenius-transitive. If it is not stable, it does not descend as that
support. If stable, D2 proves nontransitivity. These exhaust all r and
establish the claimed obstruction even for an extension chosen anew
for each cycle. Closed points mentioned after extension have degree
one or two over that extension, not necessarily over the original
\(\mathbb F_q\).

Some Frobenius power fixes \(\zeta_N\), hence fixes P_N and its
whole native orbit; f_N therefore exists. At its minimal value,
\(N\mid q^{4f_N}-1\), giving precisely the displayed logarithmic
lower bound. For any fixed r one can choose an odd prime
\(N\ne p\) greater than \(q^{4r}-1\). The fixed-r divisibility
then fails. No density theorem or conjecture about orders modulo primes
is hidden in this unboundedness argument.

For packet counting, f is the number of **native cycles**, not the
number of points or closed points. Each has n points. If
\(\Phi^fP=T^sP\), a Frobenius return to P must occur at a time
ft, and this time is a return exactly when \(n\mid st\). Thus

\[
a=f\frac{n}{\gcd(n,s)},\qquad
\#\{\text{closed points in the packet}\}=\gcd(n,s).
\]

All packet points have that same arithmetic degree: they are obtained
from P by commuting invertible powers of T and Frobenius. Distinct
native cycles in the packet are disjoint. Hence the cardinality fn and
division by a are justified. With \(2s=0\pmod n\), this gives
exactly \(a=f\) or \(2f\), and n or n/2 closed points. These
counts do not assume irreducibility of a periodic-point scheme and
contain no nonreduced lengths or characteristic-p traces.

## 5. The reflection-line positive control is genuine and separate

**Evidence anchor:** equation: D2 Report, “Positive control from the
existing Fricke line package”; C425 sections 5 and 7, affine return
and quadratic-level identities.

Suppose an injective line parametrization over \(\mathbb F_q\)
satisfies \(T^jP(t)=P(-t+\beta)\) and
\(K(P(t))=Q(t)=t^2-bt+c\). Invariance gives
\(Q(-t+\beta)=Q(t)\). Comparing linear coefficients gives
\(2\beta=2b\), so \(\beta=b\) in odd characteristic.
On an irreducible quadratic level, Frobenius exchanges the two roots
t and b−t, proving \(\Phi_qP=T^jP\) with a nontrivial exchange.
Since \(T^{2j}P=P\) but \(T^jP\ne P\), the least native
period h is even and \(j=h/2\pmod h\). This is the same finite
permutation phenomenon, but it is transitive if h=2.

The explicitly supplied example needs no inherited finite-field atlas:

\[
A=B=C=0,\quad P(t)=(t,0,0),\quad
T(P(t))=(-t,0,0),\quad K(P(t))=t^2.
\]

For any nonzero nonsquare \(D\in\mathbb F_q\), the polynomial
\(t^2-D\) is separable and irreducible; its roots are nonzero and
distinct, and \(t^q=-t\). Therefore
\(\{(t,0,0),(-t,0,0)\}\) is one exact native two-cycle and
one degree-two arithmetic closed point. Its support is smooth since
the x-derivative is 2t, which is nonzero. Since 4 is a nonzero square,
such D cannot be the Cayley level 4. No contradiction with D2 occurs.

The transfer uses polynomial identities, not C425's integer exhaustion
theorem as if it classified finite-field points. In particular a
nonzero translation excluded from integer periodicity can become
periodic in characteristic p. D2 makes no such invalid exhaustion
transfer. A finite return time on a retained line also is not silently
called its least native period; the control checks the latter directly.

## 6. Closest primary-source collision and actual access

The following are bounded original-source checks, not assertions that
the complete papers or all later literature were read. Browser-extracted
PDF text was inspected. Screenshot requests were also made, but they
did not supply usable image content to this review; one returned a
timeout. No visual-read claim depends on those requests, and no local
PDF preflight or full bibliographic resolver was run.

- **Cantat–Loray**, *Holomorphic dynamics, Painlevé VI equation and
  character varieties*, arXiv:0711.1579v2, §2.1, printed pp. 12–13.
  This gives the simultaneous-inversion quotient and the descended
  monomial action. Its trace coordinates use the plus-xyz equation;
  negating all three coordinates produces D2's convention. This is
  direct ownership of the main linearizing model, not a finite-field
  determinant theorem. The present direct algebra appropriately
  supplies positive-characteristic validity.
  [Original preprint](https://arxiv.org/pdf/0711.1579).
- **Cerbu–Gunther–Magee–Peilen**, *The cycle structure of a Markoff
  automorphism over finite fields*, arXiv:1610.07077, served §3.3,
  equations (3.2)–(3.5), Lemma 3.3 and its proof; introduction and
  Theorem 1.5 also inspected. This is the closest method collision:
  integral trace coordinates and monomial equivariance already underpin
  finite-field cycle analysis. Their long-cycle theorem varies the
  characteristic prime; D2 fixes q and varies geometric torsion order.
  No identical Frobenius packet/transitivity theorem was located in
  these passages. That is not a proof of global novelty. D2 should
  continue citing the actual trace formulas rather than transferring
  a convention-dependent matrix without its direct calculation.
  [Original preprint](https://arxiv.org/pdf/1610.07077).
- **Robin Zhang**, *A Galois–dynamics correspondence for unicritical
  polynomials*, arXiv:1610.00807, introductory Definition 1.1,
  Example 1.2 and Remarks 1.3–1.4 inspected. Nontrivial Galois action
  agreeing with a nontrivial native iterate is an established question;
  cycle-exchanging counterexamples and the commuting-action viewpoint
  precede this package. Such a relation need not be transitive on an
  entire native cycle. D2's ownership demand is stronger, and no
  unicritical theorem applies automatically to the Fricke surface.
  [Original preprint](https://arxiv.org/pdf/1610.00807).

Two bounded searches combining Cayley cubic, Frobenius, monomial action,
periodic cycles and Galois terminology found no closer exact statement
that this review could verify. Irrelevant and secondary hits were not
used as evidence. This is a search-bounded result, not absence of prior
work. The decisive contribution concern does not depend on a worldwide
exact-duplication claim: the deduction after the verified classical
linearization is visibly elementary.

Local subtraction is also substantive. C12 already has the commuting
native/Frobenius action, finite closed-point products, and the failure of
rectangular counts to recover the joint action. Its
[Frobenius proof](../../../henon_frobenius_scheme_obstruction/paper/sections/4_frobenius_obstruction.tex)
is not a proof of D2's infinite Cayley packet statement, but owns the
finite-set interpretation. C425 already owns the retained affine
reflection and quadratic-level machinery in
[section 5](../../../research_c424_c428/papers/C425_fricke_return/sections/05_line_exhaustion.tex)
and [section 7](../../../research_c424_c428/papers/C425_fricke_return/sections/07_level_counts.tex).
The earlier [two-clock scout](../../../continuation_c414_c418_round2/frobenius_clocks/SCOUT_REPORT.md)
records that mixed Hénon/Frobenius fixed counts are already owned by
C401. None of those results should be counted again as this lane's
increment.

## 7. Must-fixes, allowed claims and precise remaining gaps

### Must-fixes for the present auxiliary theorem

**None identified.** This is not a blanket proof certificate: the audit
covers the displayed theorem and control, the three specified sources,
and the exact transfer boundaries, not all other statements in the
research stream. No numerical validation is missing for this purely
algebraic proof.

The empty mathematical-defect finding is supported by the coverage in
§§2–5: geometric quotient fibres and common signs; direct native matrix;
smoothness and ordinary torsion; ring-level cyclic-vector rigidity;
least period greater than two; all extension exponents; packet/cardinality
accounting; and the nonsquare quadratic control were each checked.

### Allowed claims

- Theorem D2, with its odd-q and admissible-N hypotheses, including the
  exact scalar criterion, native projective order, unbounded packet
  degrees, and failure of one-closed-point ownership after every base
  extension.
- A complete negative answer to the retained uniform all-cycle Cayley
  bridge, not merely an inconclusive search.
- A reusable elementary rank-two cyclic-vector/determinant obstruction
  on simultaneous-inversion quotients, after checking the hypotheses.
- Preservation under bijections intertwining both specified actions.
- The stated degree-two positive control, as a separate source-level
  example on nonsquare levels, not another paper.

### Not established; do not promote these as consequences

- An all-torsion or all-cycle classification, even on the Cayley
  surface. Noncyclic exponent vectors and even torsion are not covered.
- An all-parameter Fricke incompatibility theorem. The positive control
  explicitly shows why such wording would be false.
- A classification of successful arithmetic carriers or intrinsically
  selected subfamilies preserving intended owners.
- A no-go under noninjective semiconjugacies, cycle mergers, or changed
  descent data such as a Frobenius/native-time twist.
- Recovery of omitted multiplicities, polynomial-transfer descent,
  Galois groups of periodic loci, target prime labels, target Euler
  weights, root numbers, automorphy, a zero/divisor map, or a
  Hilbert–Pólya realization.

### Why this should not fill a paper slot

The genuinely additional deduction is: one selected torsion vector is
cyclic; a commuting operator scalar on it is scalar on the whole
rank-two module; determinant forces a sign; inversion turns that sign
into a two-step Frobenius return. The logarithmic packet bound is then
integer divisibility, and ownership counts are elementary commuting
permutation bookkeeping. All parameter uniformity in the theorem is
real, but it does not by itself make this a substantial new mechanism.

The original universal conjecture is already quite demanding: even a
single rational native cycle of length greater than one prevents that
cycle from becoming one closed point after extension. D2's useful
improvement is the uniform infinite-family packet obstruction, not a
discovery that native and arithmetic orbits are generally different.
Consequently the evidence supports retaining a clean theorem/interface,
not declaring a new complete all-Fricke classification or partitioning
its four consequences into separate contributions.

No unresolved lemma remains **inside the frozen D2 contract**. What is
missing for independent paper admission is a substantial further result
after the classical and local source subtraction, not an extra census,
PDF build, or another favorable review. Any new full question requires
the coordinator's explicit scope decision; this review does not expand
the task or demand that the already proved theorem be reopened.

`NO_BAD_EULER_OR_ROOT_NUMBER` remains unchanged.
