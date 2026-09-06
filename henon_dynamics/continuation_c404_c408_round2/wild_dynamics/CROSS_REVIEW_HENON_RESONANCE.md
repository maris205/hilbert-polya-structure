# Non-author internal review: resonant Hénon–Frobenius proof

Date: 2026-09-06. Reviewer: the round2 wild-dynamics lane, not the author
of the Hénon–Frobenius proof. This is AI-team internal review, not external
LLM certification or human peer review. No author files were edited and
no old or new mathematical census was rerun.

Verdict: **MATH_PASS_PENDING_SOURCE_OWNERSHIP_GATE**.

Blocking mathematical findings: **0**. Required mathematical corrections:
**0**. The existing restricted hypotheses and observable are essential.
This verdict is not a C-number assignment or a judgment that a complete
literature-priority audit has already passed.

## 1. Exact reviewed inputs

All paths are beneath
`continuation_c404_c408_round2/henon_resonance/`.

| Input | Scope read | SHA-256 |
|---|---|---|
| `PROOF_PACKAGE.md` | All 320 lines, §§1–8 | `0c59a129ba1dfbb3f22c527c40f4065cf8748cc570a302f0b3ba801a98289ea6` |
| `exact_checks.py` | Complete file, including finite-field implementation and main | `ccc71e0ac0409a7ae3df53233b3e06df743e98f58d6bc89df5bf58b0c58b72e1` |
| `exact_results.json` | All five cases and environment/method metadata | `5ec4a3e13fa0adfeb9868ad202edd92f65d3d13e8acca44b79495c89b893aa99` |
| `CHECK_RECEIPT.md` | Complete execution/method/failure-repair receipt | Read-only supporting receipt |
| `SOURCE_AUDIT.md` | All six sections, read after the author's completion notification | `d5288bd5375cfd29d4d9219736cd91d17cc77dce62859a70a2ea9def9497f611` |

The source audit arrived before this review was finalized and was read in
full. Its bounded claim and direct-vector-group exclusion are checked
below. Paper-level admission and global priority remain distinct from
this proof/source-scope review.

## 2. Reconstructed mathematical dependency chain

The system is the actual self-map S=H^{-1}Phi of A² over F_q-bar, where
H=(y,y^q+g(y)−a x), coefficients lie in F_q, 2≤m=deg g<q, and p∤m.
The coincidence equations H^n(P)=Phi^n(P) are the fixed scheme of S^n.
This scheme-level identification is valid: an automorphism applied to both
maps preserves their equalizer, and commutativity H Phi=Phi H gives the
iterate identity. S is finite radicial with function-field degree q²;
this fact alone is correctly not used as a point-count formula.

On F_q[x,y], T=H* and U=Phi* are commuting F_q-linear operators. Hence
delta=T−U lies in a characteristic-p operator algebra and
(T−U)^{p^v}=T^{p^v}−U^{p^v}. This step is legitimate even though delta
is not multiplicative. There is no nonlinear point-map binomial argument.

For a polynomial with unique leading homogeneous term c y^D, p∤D,
the leading contribution to delta is the j=1 binomial term with degree
q(D−1)+m. The remainder P_0 has degree at most D−1, so both T(P_0)
and U(P_0) have degree at most q(D−1), strictly smaller. Every j≥2 term
has degree at most q(D−j)+jm, again strictly smaller since m<q.
The coefficient c D b is nonzero. This verifies Lemma 3 without a hidden
mixed-monomial cancellation or lower-coefficient exception.

Inductively D_{j+1}=qD_j−(q−m), D_1=m and D_j≡m mod p. Thus the
nonvanishing condition survives all iterations of delta, with coefficient
b^j m^{j−1}. The closed formula
D_j=((m−1)q^j+(q−m))/(q−1) is an integer by the recurrence.

For n=rs, r=p^{v_p(n)}, each of the s terms in the linear
difference-of-powers factorization has the SAME top degree
q^{n−r}D_r and SAME coefficient c_r. Their sum has coefficient s c_r,
which cannot vanish since p∤s. No factor q^r is mistaken for r, and the
coefficient b is not incorrectly assumed to lie in F_p rather than F_q.

The first literal fixed equation has top monomial −x^{q^n}; the second
has a nonzero multiple of y^{q^{n−r}D_r}. These monomials are coprime.
The two-polynomial Gröbner criterion therefore gives exactly the rectangle
of standard monomials, so quotient length is q^n q^{n−r}D_r. Equivalently,
the actual-degree homogenizations have no common projective point at
infinity. This specifically resolves, instead of ignoring, the resonant
drop of the second equation's degree.

Finally D(Phi^n)=0 and det D(H^n)=a^n≠0. The Jacobian at every point of
this finite scheme is invertible. Thus all local rings are the geometric
ground field and quotient length equals ORDINARY geometric fixed-point
count. The result is not a local-multiplicity-weighted count such as the
one studied in my own wild-dynamics lane.

This recovers the stated all-parameter, all-n formula

    N_n=((m−1)q^{2n}+(q−m)q^{2n−p^{v_p(n)}})/(q−1).

## 3. Independent analytic check

After u=q²t, the count is A+B q^{−p^{v_p(n)}} with A,B>0 and A+B=1.
The divisibility-indicator expansion telescopes exactly. Its logarithmic
generating series yields the product with positive

    e_k = B p^{−k}(q^{−p^{k−1}}−q^{−p^k}).

The series of these coefficients is summable, and its associated log
series converges normally on every compact subdisk. This proves that the
product is a well-defined, nonzero analytic germ on |u|<1, not merely a
formal manipulation at a boundary point.

At a primitive p^a-th root of unity xi, the finitely many k<a factors
and the base factor have bounded logarithmic modulus along rho xi.
For k≥a, the ratio
log(1−rho^{p^k})/log(1−rho) lies in [0,1] and tends to 1. Dominated
convergence gives radial order sigma_a=sum_{k≥a} e_k. The proof's bound

    0<sigma_a≤B q^{−p^{a−1}}/p^a<1

is valid, and sigma_a tends to zero. A meromorphic function at xi would
instead have an integer radial order. For any fixed M, all sufficiently
high p-power orders have 0<M sigma_a<1. Their primitive roots are dense,
excluding continuation through every arc. This establishes exactly the
claimed meromorphic natural boundary for every fixed positive power
Z_S^M, and therefore excludes algebraicity and rationality.

No numerical estimate of sigma_a or fitted singularity is needed.

## 4. Probe inspection, without rerunning it

The sparse producer composes the point map literally. Its finite fields
are quotient fields implemented by p-adic digit codes, with each nonzero
element's inverse checked. In the two F4 cases codes 2 and 3 genuinely
mean alpha and alpha+1; they are not integers modulo 4. The q=9 and q=8
examples happen to have prime-subfield polynomial coefficients, so their
secondary Gröbner calculations over F3/F2 compute the same geometric
quotient length after base extension. The non-prime-field cases correctly
skip that SymPy step.

The JSON matches direct substitution into the proved recurrence:

* q=5,m=3,n=2: D_1=3, d_n=15, N=25·15=375.
* q=9,m=2,n=3: D_3=(729+7)/8=92, N=729·92=67068.
* q=4,m=3,n=2: D_2=(2·16+1)/3=11, N=16·11=176.
* q=4,m=3,n=4: D_4=(2·256+1)/3=171, N=256·171=43776.
* q=8,m=6,n=2 deliberately violates p∤m. The invalid formula would
  give degree 46 and 2944 points, while the actual leading degree is 44
  and count 2816. The program asserts this discrepancy, not equality.

For the F4 examples, b=alpha gives b²=alpha+1 and b⁴=alpha, agreeing
with the recorded second-equation leading coefficients. The Jacobians
also agree with a²=alpha and a⁴=alpha+1. These manual checks test the
coefficient conventions rather than merely comparing integer totals.

The receipt honestly distinguishes a producer/serialization failure from
the later successful run. The count from top monomials shares a classical
lemma with the proof and is not falsely described as an independent
universal proof. No correction to the probe or receipt is required.

## 5. Source scope and non-automatic admission

The bounded primary-source comparison relevant to my own lane included
[Bridy, arXiv:1202.0362](https://arxiv.org/pdf/1202.0362) and
[Byszewski–Cornelissen–Houben, arXiv:1904.04942](https://arxiv.org/pdf/1904.04942).
The former's inseparable-polynomial degree count is a ONE-DIMENSIONAL
statement; it does not justify N_n=q^{2n} on A². The latter's Theorem A
and tame-zeta discussion are about maps supplied with dynamically affine
data. Standard-coordinate nonadditivity of S is not by itself an exclusion
of every hidden group presentation, and the reviewed proof correctly
does not claim such a classification.

After the author's source audit arrived, I also opened
[BCH, arXiv:2209.00085v2](https://arxiv.org/html/2209.00085v2) and read its
preface/scope, Theorem 5.2.5 and nearby statements. The stated hypothesis
really is a confined endomorphism of a vector group, and its count has
the form c^n p^{−t_n |n|_p^{−1}} with c a power of p. More directly,
the author's coordinate-independent obstruction is correct: the fixed
set of a confined endomorphism of G_a^r is an F_p-vector space, hence has
p-power cardinality, while N_1=qm with m>1 and p∤m is not a p-power.
This excludes even a point-dynamical conjugacy to that direct vector-group
case. It does not exclude finite quotients or other algebraic groups.

The source audit's two-generator S-polynomial identity is also correct:
for f=x^Q+f_0 and h=y^d+h_0,
y^d f−x^Q h=f_0 h−h_0 f, and both products on the right have leading
monomials below x^Q y^d. The audit honestly labels the textbook as a
classical reference without claiming successful full chapter access.
I find no necessary correction to these source-scope statements. I did
not independently reread every source passage or every sealed repository
file listed by the author, and do not present this as a complete global
bibliographic audit.

The proof's exact nonlinear leading-degree lemma is the candidate's
substantive step. Classical commuting-operator binomial algebra, coprime
initial-monomial length, and natural-boundary methods should retain their
actual source ownership. The count and zeta consequence are one candidate,
not separate paper contributions. Additional source comparison by the
author/coordinator must determine whether this particular full-period
coefficient-uniform lemma or count has already appeared. This review does
not turn failed keyword searches into priority certification.

## 6. Allowed conclusion and follow-up

Allowed now: the reviewed restricted theorem and analytic corollary follow
by the supplied complete arguments; no mathematical revision is required.
Keep the current no-hidden-group-classification sentence and the explicit
clock/observable distinctions. Keep p∤m and coefficient field F_q.

Not licensed: arbitrary g over F_q-bar, p|m, nonmonic degree-q term,
arbitrary two-clock resonance, a full conjugacy classification, Hasse–Weil
zeta identification, arithmetic local factors, root numbers, target zeros,
or a new formal paper number without the remaining source/admission gate.

If the reviewed proof changes substantively, rebind this review to the new
hash after a targeted recheck. Merely finishing the source audit does not
require another polynomial census.
