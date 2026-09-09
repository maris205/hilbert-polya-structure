# AS2-G: exact trace identities, a source-corollary branch, and the remaining gap

2026-09-08 UTC. The full question remains [the frozen AS2-G](FROZEN_QUESTIONS.md).
This is an author proof/gap package, not an admitted paper contract.
The selector is maximality of the multiplier order; time is hyperbolic
length. Write $\Gamma=\mathrm{PSL}_2(\mathbb Z)$ and
$\Gamma_N=\Gamma_0(N)/\{\pm I\}$.

## G1. The arithmetic selector is well-defined and survives every repetition

For a hyperbolic integral matrix $A$, its two real eigenvalues have
different absolute values. Consequently $A^m$ is nonscalar for every
$m\geq1$. As $\mathbb Q[A]$ is quadratic and
$\mathbb Q[A^m]\subseteq\mathbb Q[A]$, the two fields agree. Thus

$$
\mathcal O_{A^m}=\mathbb Q[A^m]\cap M_2(\mathbb Z)=\mathcal O_A,
\qquad f_{A^m}=f_A.
$$

Replacing $A$ by $-A$ changes neither field nor order. Conjugation by an
integral unimodular matrix preserves $M_2(\mathbb Z)$ and transports the
field, order and maximal order together. The selected condition therefore
descends to every required conjugacy class, including those at level $N$.

The source identity, proved in Maucourant's Lemma 2.1 and §2.2, is

$$
u_A=\gcd(b,c,d-a),\qquad
\operatorname{disc}(\mathcal O_A)=\frac{(\operatorname{tr}A)^2-4}{u_A^2}
=f_A^2\operatorname{disc}(K_A).
$$

This is prior arithmetic structure, not a new invariant introduced here.
For example,

$$
A_3=\begin{pmatrix}3&-1\\1&0\end{pmatrix},\qquad
A_3^2=\begin{pmatrix}8&-3\\3&-1\end{pmatrix}.
$$

Their contents are $1,3$ and their multiplier discriminants are both $5$,
although their raw characteristic discriminants are $5,45$. Applying a
raw squarefree/fundamental-trace test afresh to each repetition would
therefore destroy the frozen observable. See
[Maucourant, §§2.1–2.2](https://arxiv.org/html/2403.13383v1#S2).

## G2. No fixed finite congruence quotient recognizes this selector

For every integer $M\geq1$, there are primitive hyperbolic matrices
$A,B\in\mathrm{SL}_2(\mathbb Z)$ with $A\equiv B\pmod M$, but exactly
one has maximal multiplier order.

**Proof.** Let $A=A_3$ above. Choose an odd prime $q\nmid M$ and, by
the Chinese remainder theorem, an integer $t>2$ with

$$
t\equiv3\pmod M,\qquad t\equiv2\pmod {q^2}.
$$

Set $B=A_t=\left(\begin{smallmatrix}t&-1\\1&0\end{smallmatrix}\right)$.
Its content is one, so its multiplier discriminant is $t^2-4$. This is
divisible by the odd square $q^2$, and hence is not a fundamental
discriminant. By contrast, $A$ has discriminant $5$ and is maximal.

It remains to check primitivity; arbitrary matrices would not suffice.
If $A_t=C^m$ in $\Gamma$ with $m\geq2$, a lift of $C$ can be chosen
hyperbolic with positive trace $v\geq3$. Positive trace of $A_t$ then
forces equality with the positive-trace lift of $C^m$. Cayley–Hamilton gives

$$
C^m=c_m(v)C-c_{m-1}(v)I,
\quad c_0=0,\ c_1=1,\ c_{m+1}=vc_m-c_{m-1}.
$$

For $v\geq3$, induction gives $c_m\geq3$ for $m\geq2$.
All off-diagonal entries and the diagonal difference of $C^m$ are
divisible by $c_m$. This contradicts $u_{A_t}=1$. The same argument
applies to $A_3$. Thus both matrices are primitive. QED.

This rules out **a selector factoring through one fixed congruence
quotient**, including arbitrary class functions on that quotient. It does
not rule out infinite arithmetic information, a noncongruence coding,
or every conceivable transfer operator. It is a diagnostic auxiliary
lemma, not closure of the analytic question.

## G3. The entire level family has an exact native covering identity

Let $C_N=\Gamma_N\backslash\Gamma$, a finite set with the right
permutation action of $\Gamma$. For a primitive base class $[A]$ let
$\mathcal C_N(A)$ be the cycles of this permutation, with lengths $k(c)$.
Then, in $\Re s>1$,

$$
\zeta_N^{\rm max}(s)=
\prod_{[A]\in\operatorname{Prim}(\Gamma),\ f_A=1}
\prod_{c\in\mathcal C_N(A)}
(1-e^{-s k(c)\ell_A})^{-1}.
\tag{G3.1}
$$

Equivalently, writing $\chi_N(A^m)=\#\operatorname{Fix}_{C_N}(A^m)$,

$$
-\frac{(\zeta_N^{\rm max})'}{\zeta_N^{\rm max}}(s)
=\sum_{[A]\in\operatorname{Prim}(\Gamma),\ f_A=1}
\ell_A\sum_{m\geq1}\chi_N(A^m)e^{-s m\ell_A}.
\tag{G3.2}
$$

**Proof.** Lift one oriented primitive base-flow orbit to the finite
cover $\Gamma_N\backslash\mathrm{PSL}_2(\mathbb R)$. A coset cycle of
length $k$ closes after exactly $k$ base returns. It is primitive in the
cover by minimality of $k$, and has physical length $k\ell_A$.
Conversely every primitive orbit upstairs arises from one such cycle.
Its return matrix is an integral conjugate of $A^k$, so G1 preserves the
selector. This proves (G3.1). A $k$-cycle contributes $k$ fixed cosets to
$A^m$ exactly when $k\mid m$, proving (G3.2). Absolute convergence
follows from $0\leq\chi_N\leq[\Gamma:\Gamma_N]$ and the full base
prime-geodesic bound. QED.

There is no change of clock: $k\ell_A$ is the actual lifted period.
This finite permutation character does not implement the infinite
maximal-order selector. The formula is a standard covering argument
specialized to the frozen order-invariant observable, not a claim of a
new global spectral operator.

## G4. A genuine nonmeromorphic branch is already forced at level one

Let

$$
c_F=\frac{75}{112}\prod_{q\geq3\ {\rm prime}}
\left(1-\frac{2q}{q^3-1}\right),\qquad \beta=\frac{25}{26}.
$$

The product converges to a positive number: each factor is positive and
the sum of the omitted quantities converges by comparison with
$\sum n^{-2}$. Also $c_F<75/112<1$; in particular $c_F$ is not an
integer. No numerical experiment or assertion that $c_F$ is irrational
is needed.

**Source input, not a new counting theorem.** Hashimoto §3.1 identifies
primitive conjugacy classes with primitive indefinite forms, using the
narrow class number and the least positive norm-one unit. Section 4.3,
including Theorem 4.11 at modulus one, gives

$$
\pi_F(X):=\#\{[A]\in\operatorname{Prim}(\Gamma):
 f_A=1,\ e^{\ell_A}<X\}
=c_F\operatorname{li}(X)+O_\epsilon(X^{\beta+\epsilon}).
\tag{G4.1}
$$

Here the paper's unit bound is $x=\sqrt X$, so its exponent
$25/13+\epsilon$ becomes $25/26+\epsilon$ after renaming epsilon.
The coefficient and an earlier power saving are attributed there to
Raulf. The narrow-class convention keeps the source's primitive oriented
conjugacy classes; no extra factor two or orientation quotient is added.
This is a length-ordered theorem, unlike a density statement obtained
merely by sampling matrices in a Frobenius-norm ball.
[Hashimoto, §§3.1, 4.3](https://arxiv.org/html/1003.3716v2#S4.SS3).

**Proposition.** On the universal cover of
$H_\beta\setminus\{1\}$, where $H_\beta=\{\Re s>\beta\}$, the
level-one germ has the form

$$
\zeta_1^{\rm max}(s)=(s-1)^{-c_F}\exp h(s),
\qquad h\ \text{holomorphic on }H_\beta.
\tag{G4.2}
$$

In particular it has nontrivial monodromy $e^{-2\pi i c_F}$ around $1$
and no single-valued meromorphic continuation across $1$.

**Proof from (G4.1).** Choose $a>1$ below the smallest orbit norm and
extend the counting function by zero below its first jump. Put
$L_a(X)=\int_a^X dt/\log t$ and
$E(X)=\pi_F(X)-c_F L_a(X)$. The difference between $L_a$ and the
source's logarithmic integral is constant, so for every $\epsilon>0$,
$E(X)=O_\epsilon(X^{\beta+\epsilon})$, and $E(a)=0$.
The primitive contribution to the logarithmic derivative is

$$
\int_a^\infty (\log X)X^{-s}\,d\pi_F(X)
=c_F\frac{a^{1-s}}{s-1}
-\int_a^\infty E(X)\frac{d}{dX}((\log X)X^{-s})\,dX.
$$

The last integral is holomorphic on $H_\beta$ by locally uniform
convergence, choosing epsilon smaller than each compact set's distance
to the boundary. Also
$(a^{1-s}-1)/(s-1)$ is entire. All repetitions of order at least two give

$$
R(s)=\sum_{[A],f_A=1}\ell_A
\frac{e^{-2s\ell_A}}{1-e^{-s\ell_A}},
$$

which is holomorphic for $\Re s>1/2$, again by the full prime-geodesic
bound and a positive minimum length. Hence

$$
-\frac{(\zeta_1^{\rm max})'}{\zeta_1^{\rm max}}(s)
=\frac{c_F}{s-1}+H(s),\qquad H\in\mathcal O(H_\beta).
$$

Since $H_\beta$ is simply connected, integrate $-H$ and choose the
constant to match the original Euler product on the right of $1$.
This proves (G4.2). A meromorphic germ at $1$ would have an integer
residue in its logarithmic derivative, contrary to $0<c_F<1$. QED.

Thus this **particular scalar zeta** cannot equal a Fredholm determinant
or reciprocal/ratio known to be single-valued meromorphic near $1$.
No assertion is made about branched regularizations or every operator
class. The elementary passage from a source-owned counting law to a
branch is a source corollary, not a claimed independent paper increment.

## G5. Precisely what is not proved

The full AS2-G problem has not been closed. G4 disproves the subclaim
that every level has a global single-valued meromorphic zeta, but it
does not determine the maximal continuation domain even at level one,
let alone the complete singularity structure at every level $N$.
The line $\Re s=25/26$ is a **proved continuation threshold**, not a
proved natural boundary.

The conductor inclusion-exclusion identity is pointwise exact:
$1_{f_A=1}=\sum_{d\mid f_A}\mu(d)$. In the initial convergence
half-plane it may be summed in the trace. Indeed
$f_A\leq\sqrt{(\operatorname{tr}A)^2-4}<e^{\ell_A/2}$ and
$\tau(f_A)\ll_\epsilon f_A^\epsilon$, so absolute divisor summation
follows for every fixed $\Re s>1$ by taking epsilon small enough.
This supplies no normal convergence of the *continued* conductor
pieces. The additional content valuations $u_A$ and the covering
weights in (G3.2) must also be retained; they cannot be replaced by
one fixed finite quotient.

Missing are: continuation estimates for that full weighted conductor
sum beyond the initial half-plane, a proof of all relevant singularities
or actual boundaries, and any source-defined operator/domain/trace
realization claimed as an answer. Neither finite congruence calculations
nor the ordinary unfiltered Selberg determinant fills those obligations.
No finite census was run: it cannot settle these analytic gaps.

**Disposition:** `FULL_QUESTION_OPEN_IN_THIS_PACKAGE`;
`N1_BRANCH_SOURCE_COROLLARY_AUXILIARY`;
`NO_PAPER_CONTRACT_ADMISSION`.
`NO_BAD_EULER_OR_ROOT_NUMBER`.
