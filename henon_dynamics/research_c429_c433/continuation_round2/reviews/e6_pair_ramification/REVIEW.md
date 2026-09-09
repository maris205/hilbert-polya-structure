# E6 — Independent review of the certified pair's ramification

2026-09-09 UTC. Nonauthor, proof-only review of
[PAIR_RAMIFICATION.md](../../a3_wild_local_tower/PAIR_RAMIFICATION.md).
This is a new claim review, not a repetition of the accepted B4/R2
displacement review or E2's single-pair computational audit. Both remain
frozen. Current-team mathematical review is not human peer review,
external-model-family evidence, formal evaluation, or paper admission.

## 1. Verdict and dependency boundary

**PASS for the stated single-pair deduction. Zero open mathematical or
source-applicability must-fixes.**

The exact accepted inputs are those of the
[E2 certificate review](../e2_local_as/REVIEW.md):

$$
k=\overline{\mathbb F}_3,\quad K=k((s)),\quad v(s)=1,
\quad P_s(z)=(1+s)z+z^2,
$$

the canonical monic degree-nine small factor $M_2$, a root $\alpha$
of valuation $2/3$ whose nine iterates are all its roots, and

$$
L=K(\alpha),\qquad
\operatorname{Gal}(L/K)=\langle\sigma\rangle=C_9,
\qquad \sigma\alpha=P_s(\alpha).
$$

The extension is totally ramified. The accepted polynomial
discriminant valuation is $144$, and the native degree-three quotient
has reduced AS class $[2s^{-4}+s^{-2}]$ and break $4$.
The initial displacement $4/3$ is also checked directly below.
E2's verdict and relevant input/normalization passages were read;
the accepted producer and checker were not rerun or re-audited here.

From those inputs the submitted deduction correctly proves

$$
\delta_0=4/3,\quad \delta_1=4,\quad
(b_1,b_2)=(4,28),\quad (u_1,u_2)=(4,12),
$$

$$
d_{L/K}=88,\qquad
\operatorname{length}_{k[[s]]}(O_L/k[[s]][\alpha])=28.
$$

Here $\delta_j=v(P_s^{\circ3^j}(\alpha)-\alpha)$ uses the
extension of the **base** valuation, whereas breaks and the different
exponent use $v_L=9v$. No unconditional independent recertification of
the input computation is asserted by this review. The proof is sound
from the accepted certificate, exactly as the author's statement says.
Write $R=k[[s]]$ throughout the lattice calculations below.

## 2. Polynomial distances determine the three-step displacement

For any two distinct orbit points $x,y$,

$$
\frac{P_s(x)-P_s(y)}{x-y}=1+s+x+y\equiv1\pmod{\mathfrak m_L}.
$$

Every iterate has the same residue-one difference quotient, by
multiplying these factors. In particular, consecutive displacements,
divided by $P_s(\alpha)-\alpha$, all have residue one. Their sum
over $a$ steps has residue $a$. For $a\in\{1,2,4,5,7,8\}$ this
is nonzero, so no leading cancellation occurs. The first displacement
has valuation

$$
v(s\alpha+\alpha^2)=\min(5/3,4/3)=4/3.
$$

For the three-step return $Q=P_s^{\circ3}$, the same quotient
property makes
$(Q^2\alpha-Q\alpha)/(Q\alpha-\alpha)$ have residue one.
The sum of the two displacements has nonzero residue two. Thus the
step-three and step-six differences have the same finite valuation $D$.
Finiteness follows from ordinary least period nine.

Since $M_2$ is monic with exactly this simple-root orbit,
$M_2'(\alpha)$ is the product of the eight nonzero differences.
All nine derivative values have the same valuation, either by the
distance preservation above or by the accepted Galois action. Hence

$$
v(\operatorname{Disc}M_2)
 =9\,v(M_2'(\alpha))
 =9\left(6\cdot\frac43+2D\right)=144.
$$

This gives $D=4$. The factor nine is required here: the discriminant
is the product of nine derivative values in the base-extended valuation.
This does not identify the polynomial discriminant with the field
different. In particular
$v(M_2'(\alpha))=16$ and $v_L(M_2'(\alpha))=144$,
not $88$.

## 3. Which degree-three quotient supplies the first break

The accepted native resolvent satisfies $\sigma y-y=1$, so its
stabilizer in $C_9$ is precisely $H=\langle\sigma^3\rangle$.
Thus $K(y)=L^H$ is the actual degree-three subextension of this
degree-nine field. It is not the separate native period-three root
field, whose break is two.

The reduced class has highest pole four, which is prime to three.
It gives quotient break four. Quotient compatibility of upper
numbering places this at $u_1$, and the first upper and lower
breaks agree. Hence $b_1=u_1=4$.
The source also supplies two distinct breaks for a totally ramified
cyclic degree-nine extension. After the first drop the group is $H$,
so the generator $\sigma$ has uniformizer displacement order five,
while $\sigma^3$ has order $b_2+1$ with $b_2>4$.
These conventions and hypotheses were checked in
[Elder–Keating, §2 and Lemmas 2.1–2.2](https://arxiv.org/html/2503.16830v1).
The source allows arbitrary perfect residue fields; finite residue
field or mixed-characteristic hypotheses are not being imported.

## 4. Uniformizer tails and coefficient-field dependence

The original field $k\subset K\subset L$ is an available coefficient
field and is fixed pointwise by both automorphisms. Its reduction is
the entire residue field of $L$. Completeness then gives
$O_L=k[[t]]$ for any chosen uniformizer $t$. Consequently every
coefficient $A_a$ in a uniformizer expansion is fixed, so

$$
(\tau-1)\alpha=\sum_a A_a\bigl(\tau(t^a)-t^a\bigr).
$$

This use of actual fixed constants is essential to the displayed
calculation. Merely choosing arbitrary residue representatives would
not justify dropping the differences of the coefficients. The author
does explicitly choose the original fixed $k$, so that problem does
not arise. A different uniformizer changes the coefficient values;
the deductions about their vanishing/nonvanishing follow anew for
each such uniformizer with this fixed coefficient field.

For a nontrivial automorphism with $\tau(t)=t(1+w)$ and
$v_L(w)=b>0$, write $a=3^j a_0$ with $3\nmid a_0$. Then

$$
(1+w)^a-1=(1+w^{3^j})^{a_0}-1
 =a_0w^{3^j}+\text{terms of higher valuation}.
$$

The coefficient is nonzero, proving the author's exact formula

$$
v_L(\tau(t^a)-t^a)=a+3^{v_3(a)}b.
$$

No tame approximation replaces this formula when $3\mid a$.
Automorphisms preserve the valuation and are continuous. The termwise
difference bounds tend to infinity with $a$, which justifies applying
the formula to the convergent infinite expansion.

For $\sigma$, the comparison is:

| Exponent in $\alpha$ | Difference order for $b_1=4$ | Consequence |
| --- | --- | --- |
| $6$ | $6+3\cdot4=18$ | Cannot affect orders eleven or twelve. |
| $7$ | $7+4=11$ | The unique possible order-eleven contribution. |
| $8$ | $8+4=12$ | The unique possible order-twelve contribution after $A_7=0$. |
| $a\ge9$ | $a+3^{v_3(a)}4\ge13$ | Entire tail lies in $t^{13}k[[t]]$. |

Since $v_L(\alpha)=6$, its first coefficient $A_6$ is nonzero.
The known difference order $9\delta_0=12$ first forces $A_7=0$,
then forces $A_8\ne0$. A higher-order term in the $t^7$ difference
cannot be used to supply order twelve: its nonzero order-eleven term
would already contradict the observed valuation.

For $\sigma^3$, let its lower break be $b_2>4$. The $t^6$
contribution now has order $6+3b_2$, strictly greater than
$8+b_2$ because their difference is $2b_2-2>0$.
The $t^7$ term is absent. The nonzero $t^8$ term has order
$8+b_2$, with nonzero leading coefficient. Every later monomial
has order at least $9+b_2$; convergence puts their whole tail in
that higher ideal. There is therefore exactly one lowest contribution.
The known $9\delta_1=36$ gives

$$
8+b_2=36,\qquad b_2=28.
$$

Finally $b_2-b_1=3(u_2-u_1)$ gives $u_2=12$.
The formula uses lower breaks for $L/K$ in $v_L$, not a base-rescaled
break for $L/L^H$. No extra factor of three belongs in this step.

## 5. Different exponent and the additive lattice index

The group orders and integer endpoints are

$$
|G_i|=9\ (0\le i\le4),\qquad
|G_i|=3\ (5\le i\le28),\qquad
|G_i|=1\ (i\ge29).
$$

Thus the different sum is $5\cdot8+24\cdot2=88$.
The endpoints include $G_0$ and the groups at both breaks.
There is no off-by-one error.

The author's alternate uniformizer calculation gives the same answer
without needing a separate group-sum assertion. Indeed $v(t)=1/9$
forces $[K(t):K]\ge9$, so $K(t)=L$. In the $K$-basis
$1,t,\ldots,t^8$, terms $a_it^i$ have distinct integer valuations
modulo nine. An integral sum therefore has all $a_i\in R$.
This proves $O_L=R[t]$. For its minimal polynomial $f$, the
monogenic different formula gives

$$
v_L(f'(t))
 =\sum_{\gamma\ne1}v_L(t-\gamma t)
 =6(4+1)+2(28+1)=88.
$$

The monogenic different formula and the field discriminant as the
norm of the different hold for finite separable extensions of
Dedekind domains, not only number fields; this was checked in
[Sutherland, Lecture 12, Proposition 12.23 and Theorem 12.17](https://math.mit.edu/classes/18.785/2019fa/LectureNotes12.pdf).
Here the maximal ideal has residue degree one, so norm converts
different exponent $88$ to base discriminant exponent $88$.
The definition used is the maximal-order trace-dual different, as
in [Stacks, §49.8](https://stacks.math.columbia.edu/tag/0BW0).

The integral primitive element $\alpha$ makes $R[\alpha]$ a full
rank-nine $R$-lattice in $O_L$. If $C$ is its basis matrix relative
to an integral basis, the Gram matrix is $C^{\mathsf T}TC$.
Thus its discriminant valuation is $v(\det T)+2v(\det C)$.
Over the DVR $R$, diagonalizing the lattice inclusion shows that
$v(\det C)=\operatorname{length}_R(O_L/R[\alpha])$.
This is the trace-form change-of-basis convention in
[Stacks, §9.20](https://stacks.math.columbia.edu/tag/0BIE).
Consequently

$$
144=88+2\ell,\qquad \ell=28.
$$

The output is an additive $R$-module length. It is not a finite
cardinality index (the residue field is infinite), nor an
$O_L$-module length of a quotient by an $O_L$-ideal.

## 6. Disposition, sources and binding artifacts

Primary-source pages above were accessed on 2026-09-09. Only their
relevant ramification, different and trace-form passages are used.
No result about finite-residue local fields was silently extended to
$\overline{\mathbb F}_3((s))$. The uniformizer-tail calculation
and distance deductions were checked directly, not inferred from a
source citation or from matching final numbers.

The research-review skill supplied the evidence/claim separation and
explicit gap audit. Its external-model workflow was excluded by the
current-session, no-upload task. The repository review gate likewise
requires the actual new claim, not a repeat of accepted computation.
No extra model, agent, mathematical execution, or manuscript upload
was used. No author, B4, prior E6, shared, Git, evaluation or built
PDF artifact was modified. Only this new assigned review was written.

The accepted conclusion is a **single-pair ramification control**.
Its standard ramification and lattice ingredients are source-owned.
It does not determine a Witt vector, prove an all-level break pattern,
settle the uniform local degree question, or solve global PC424-D.
It is auxiliary and does not warrant a separate paper admission.

| Binding input | SHA-256 |
| --- | --- |
| `a3_wild_local_tower/PAIR_RAMIFICATION.md` | `6478ba42fa8b597f22a1b63558f251a839c1fca40cb0b7a5b2c157d3ae1b5973` |
| Accepted `reviews/e2_local_as/REVIEW.md` | `04f6c63d86af4ac62194ef7fa2bd38dd62bf483731a94771d4831e72616f0a5d` |

The first file was read in full and its hash checked before and after
the audit. The second binds the imported certificate verdict, not a
new review of its underlying code. Hashes establish artifact identity,
not mathematical validity.

**ZERO_OPEN_MUST_FIXES; PAIR_RAMIFICATION_AUXILIARY_VERIFIED;
UNIFORM_LOCAL_AND_GLOBAL_CLAIMS_UNCLOSED.**

`NO_BAD_EULER_OR_ROOT_NUMBER`.
