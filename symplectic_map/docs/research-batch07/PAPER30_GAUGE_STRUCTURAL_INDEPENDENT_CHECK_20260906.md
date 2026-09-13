# Paper30 gauge structural claims — independent mathematical check

Date: 2026-09-06. Reviewer task: `/root/p30_gauge_structural_math_check`.
Scope: two frozen author proof notes and their stated, accepted Paper29
dependencies. This is an independent mathematical review of those notes,
not an author proof, a machine-checked proof, a human review, a model-version
verification, a novelty/capacity judgment, a Route evaluation, or PDF acceptance.
Route applicability: `NOT_APPLICABLE`.

## 1. Inputs, authority, and conclusion

The two full author inputs were read and their line counts and SHA256 values
verified. They have not been edited by this reviewer.

| Input | Lines | SHA256 |
| --- | ---: | --- |
| [Orbit-linear proof](PAPER30_ORBIT_LINEAR_GAUGE_PROOF_20260906.md) | 190 | `2f6e4e603fef5ca331e0f829c4493d426c0e57bf62e930c17e1ac3b965e7a183` |
| [Uniform formal gauge proof](PAPER30_UNIFORM_FORMAL_GAUGE_PROOF_20260906.md) | 214 | `052366584730be71cd4426fae0e5d5470fc7ffa1fb8928b1f5c4005bf40ee3a0` |

**Mathematical status of both claims: `PROVABLE AS STATED`.** No extra
mathematical assumption, weakening, generic-parameter restriction, or change
of perturbation family is needed. The source-expression issue described next
is a literal correction, not a different theorem.

Orbit-linear input line 28 contains a vertical-tab encoding error inside its
second parameter command. The unique intended expression is
$$
C_\varepsilon
=\exp\!\left(\operatorname{ad}_{\varepsilon h+
\varepsilon^2h_2+\cdots}\right).
$$
This interpretation is already fixed by that input's lines 142–156. The author
subsequently supplied the separate [literal erratum](PAPER30_ORBIT_LINEAR_GAUGE_TEXT_ERRATUM_20260906.md),
24 lines, SHA256
`b818cdfc8b31f12f703b34edfc40d137eac31d3bd273f3c65713dfc75581e57c`.
Its lines 12–20 have been checked: they restore precisely this parameter
command and make no mathematical change. **The literal issue is closed by
that erratum; the original 190-line input remains frozen.**

The review follows the `proof-writer` claim/status/proof discipline and the
`research-review` independent claims-matrix discipline. It is one independent
review, followed by the narrow author clarification/erratum above; it does not
invent a multi-round mathematical consensus. No concurrent degree-specific
author report, action-author report, candidate opinion, or score was read.
No numerical experiment or symbolic test is used as proof.

## 2. Exact claims, assumptions, and notation

In the orbit-linear claim, $K$ is a characteristic-zero field,
$A=K[x,y]$, $p(t)=at^d+\cdots$ has exact degree $d\ge2$ with $a\ne0$,
and $\sigma=H^*$ for $H(x,y)=(p(x)-y,x)$. The convention is
$$
\{f,g\}=f_xg_y-f_yg_x,\qquad
\operatorname{ad}_f(g)=\{f,g\},\qquad
X_0=x,\quad X_{-1}=y,\quad \sigma X_i=X_{i+1}.
$$
For $h=b+\sum_i a_iX_i$ with finitely many nonzero $a_i$, the precise claim is
$$
[\{h,\sigma h\}]=0
\quad\hbox{in }A/((1-\sigma)A+K)
\quad\Longleftrightarrow\quad
\#\{i:a_i\ne0\}\le1.
$$
The claimed conjugacy concerns the prescribed full curve
$U_\varepsilon=\exp(\varepsilon\operatorname{ad}_{h-\sigma h})\sigma$,
with $U_\varepsilon=C_\varepsilon\sigma C_\varepsilon^{-1}$ and the
Hamiltonian first term $\varepsilon h$. In the allowed cases,
$C_\varepsilon=\exp(\varepsilon\operatorname{ad}_h)$ is asserted to suffice.

The uniform claim fixes $d\ge2$ and $D\ge0$, allows every complex polynomial
$p$ of exact degree $d$ and every complex $h$ of ordinary degree at most $D$,
and asserts a single $N(d,D)\ge2$ such that conjugacy for this same prescribed
full curve is equivalent to conjugacy modulo $\varepsilon^{N(d,D)+1}$.
The full conjugator is unique among those tangent to the identity. The
parameter locus is closed relative to the open set where the leading
coefficient is nonzero, and its equations are homogeneous in the coefficients
of $h$. The recursion is explicit order by order; $N$ is only existential.

All automorphisms and derivations here are over the given coefficient field
or ring, fix $\varepsilon$, and are continuous for the $\varepsilon$-adic
topology. The algebra is $A[[\varepsilon]]$: each parameter coefficient is a
global polynomial, with no uniform spatial-degree bound on the entire series.
It is not a completion in $x,y$. These are the standard base-linear meanings
of the author statements, not extra analytic or local hypotheses.

## 3. Dependency map and accepted sources

The following local mathematical sources are sufficient. Their field-case
proofs are accepted dependencies, not reopened as a separate Paper29 review.
The additional coefficient-ring extension needed here is checked in Section 5.

1. [Paper29 Section 2](../../papers/29-filtered-henon-cohomology/paper-successor-20260906-transcription-v1/sections/2_orbit_algebras.tex),
   SHA256 `a36bebf59d412cc72ba52b38eb38da5f65cda0d0e79500642a7599004cb9520f`:
   lines 46–129 give the basis and the unit-leading-coefficient reduction;
   lines 132–160 give the meaning of the normal constant coefficient and
   the shift action. Only the scalar specialization $k=1$ is used.
2. [Paper29 Section 3](../../papers/29-filtered-henon-cohomology/paper-successor-20260906-transcription-v1/sections/3_filtered_primitives.tex),
   SHA256 `e8e5410a2df50f5591da6a4eacaebbe350fad7c4c179911d39f259fc176e4bf1`:
   lines 28–94 give the distinct highest monomials; lines 96–153 give
   infinite nonconstant word orbits, the coefficient-sum criterion, and
   uniqueness modulo constants. Lines 155–159 distinguish normal and
   ordinary constant coefficients. The bounded-primitive and rational
   reduction theorems are not needed for the present claims.
3. The formal BCH identity and the Hilbert basis theorem are deducted general
   tools. The relevant hypotheses and the precise consequences used below
   are stated explicitly; no unverified specialized theorem is needed.

The orbit-linear theorem uses the orbit criterion plus the continuant leading
word and the order-two BCH identity. The uniform theorem uses the universal
word basis, an explicit splitting of $1-\sigma$, the Hamiltonian logarithm,
the canonical recursion, and finally Noetherianity. The cited 2026 Melnikov
article in uniform-input lines 199–205 is not a necessary dependency. This
report makes no claim to verify that comparison or any novelty attribution.

## 4. Orbit-linear theorem: complete independent check

### 4.1 Bracket signs and continuants

Because $\sigma$ is Poisson and $\{x,p(x)-y\}=-1$, one has
$\{X_i,X_{i+1}\}=-1$ for every integer $i$, including negative indices.
For fixed $i$, write $B_j=\{X_i,X_j\}$. The recurrence for $X_j$ gives
$$
B_{j+1}=p'(X_j)B_j-B_{j-1},\qquad B_i=0,\quad B_{i+1}=-1.
$$
Thus, for $j>i$,
$$
\{X_i,X_j\}
=-K_{j-i-1}(p'(X_{i+1}),\ldots,p'(X_{j-1})),
$$
where $K_0=1$, $K_1(t_1)=t_1$, and
$K_m=t_mK_{m-1}-K_{m-2}$. This verifies the sign in orbit-input equation (1).

The matching formula for $K_m$ follows by separating matchings of the path
according to whether its last vertex is unmatched or paired with its preceding
vertex. Consequently every derivative factor occurs at most once. As
$\deg p'=d-1<d$, each expanded product is already a standard word: no orbit
relation can change its apparent degree or create additional top terms.

For the formal word degree $|e|=\sum_i e_i$, the only degree
$(d-1)(j-i-1)$ term is
$$
-(da)^{j-i-1}\prod_{s=i+1}^{j-1}X_s^{d-1}.
$$
The empty matching and the leading coefficient from each derivative give this
term. A nonempty matching deletes two derivative factors; a lower coefficient
in any remaining derivative lowers the degree by at least one. When $j=i+1$,
the displayed expression is the constant $-1$. Antisymmetry handles $j<i$.

### 4.2 The extreme term cannot cancel in a translation orbit

For nonsingleton support, let $L$ and $R$ be its least and greatest indices,
and let $r=R-L\ge1$. In
$$
\{h,\sigma h\}=\sum_{i,j=L}^R a_i a_j\{X_i,X_{j+1}\},
$$
the largest possible positive endpoint distance is $r+1$, attained only at
$(i,j)=(L,R)$. The largest magnitude in the opposite direction is $r-1$.
Every other nonzero bracket has distance at most $r$ and hence formal word
degree at most $(d-1)(r-1)$. The equal-index bracket is zero.

The extreme bracket itself can have further terms of degrees between these
bounds and the maximum, but all are strictly below $(d-1)r$. Therefore the
whole sum has exactly one word at its maximum formal degree:
$$
W=\prod_{s=L+1}^{R}X_s^{d-1},\qquad
[W]\{h,\sigma h\}=-a_La_R(da)^r\ne0.
$$
This last inequality uses a field, characteristic zero, $a\ne0$, and the
definition of $L,R$. It does not use positivity, real coefficients, or a
generic choice of lower coefficients of $p$.

The word $W$ is nonconstant. Index translation preserves formal word degree,
so no lower-degree word can contribute to its translation orbit. Since $W$
is the unique top-degree word, the complete coefficient sum on that orbit
is exactly $-a_La_R(da)^r$. The accepted coefficient criterion proves that
$\{h,\sigma h\}\notin(1-\sigma)A+K$.

If the support is empty, the bracket is zero. If $h=b+uX_i$, then
$\{h,\sigma h\}=-u^2\in K$. These cases give the reverse implication.

### 4.3 Necessity and exact sufficiency for conjugacy

The bracket convention gives
$[\operatorname{ad}_f,\operatorname{ad}_g]=\operatorname{ad}_{\{f,g\}}$
by the Jacobi identity, and Poisson invariance gives
$\sigma\operatorname{ad}_f\sigma^{-1}=\operatorname{ad}_{\sigma f}$.
For $H_\varepsilon=\varepsilon h+\varepsilon^2h_2+\cdots$,
$$
C_\varepsilon\sigma C_\varepsilon^{-1}\sigma^{-1}
=\exp(\operatorname{ad}_{H_\varepsilon})
 \exp(-\operatorname{ad}_{\sigma H_\varepsilon}).
$$
Its logarithm through order two is
$$
\operatorname{ad}_{\varepsilon(h-\sigma h)+
\varepsilon^2((1-\sigma)h_2-\tfrac12\{h,\sigma h\})}
\pmod{\varepsilon^3}.
$$
An inner Hamiltonian derivation vanishes exactly when its Hamiltonian is
constant: evaluation on $x,y$ gives both vanishing partial derivatives.
Equality with the prescribed exponential therefore requires
$$
(1-\sigma)h_2-\tfrac12\{h,\sigma h\}\in K.
$$
Section 4.2 rules this out for nonsingleton support.

For singleton or empty support, the bracket is constant and the two
derivations $\operatorname{ad}_h$ and $\operatorname{ad}_{\sigma h}$ commute.
Their exponential product is therefore exactly
$\exp(\varepsilon\operatorname{ad}_{h-\sigma h})$ at every parameter order.
This proves the stated conjugacy with $C_\varepsilon=
\exp(\varepsilon\operatorname{ad}_h)$. Positive parameter order makes all
these expressions well defined regardless of analytic flow completeness.

**Status for orbit-input lines 8–36 and 59–177: `PROVABLE AS STATED`, with
the already-closed literal erratum at line 28.**

## 5. Uniform theorem: coefficient-ring and specialization check

Let
$$
R_0=\mathbb Q[a_0,\ldots,a_d,a_d^{-1}],\qquad
R=R_0[(b_{uv})_{u+v\le D}],\qquad A_R=R[x,y].
$$
The number of coefficient variables is finite. The orbit coordinates are
polynomials over $R_0$ and $\sigma$ fixes $R$.

### 5.1 A direct verification that the basis survives all allowed parameters

The accepted pure-power reductions use only $a_d^{-1}$, and their confluence
identities are identities over $R$. There is also a short unit-triangular
verification of the extension, which makes the specialization issue explicit.
For $j\ge0$, the highest homogeneous parts are
$$
\operatorname{top}(X_j)
=a_d^{(d^j-1)/(d-1)}x^{d^j},\qquad
\operatorname{top}(X_{-1-j})
=a_d^{(d^j-1)/(d-1)}y^{d^j}.
$$
These formulas follow by induction in the recurrence; the subtracted
neighbor has strictly smaller degree at each noninitial step. For each
standard word $M_e$, its highest homogeneous part is therefore
$$
c_e x^{\alpha(e)}y^{\beta(e)},\qquad c_e\in R_0^*,
$$
where
$$
\alpha(e)=\sum_{i\ge0}e_i d^i,\qquad
\beta(e)=\sum_{i\le-1}e_i d^{-1-i}.
$$
Base-$d$ digit expansions give a bijection from the allowed words to pairs
$(\alpha,\beta)\in\mathbb Z_{\ge0}^2$. For each ordinary monomial, subtracting
the unique word with that highest monomial, divided by its unit $c_e$, lowers
ordinary degree. Induction proves spanning over $R$. In a putative finite
linear relation, the words of greatest ordinary degree give distinct ordinary
monomials with unit leading coefficients. Their coefficients must vanish;
descending in degree proves independence over $R$.

This argument uses no division by a lower coefficient, resultant, determinant
depending on a special locus, or coefficient of $h$. It remains valid after
every specialization to a characteristic-zero field with $a_d\ne0$.
Since the specialized words are still a basis, specialization of the unique
universal normal form is the unique specialized normal form. This proves
the required compatibility, not merely generic compatibility.

### 5.2 The splitting and the constant normalization

For every nonconstant translation orbit select its unique representative
$M_O$ whose least support index is zero. Nonconstant words have infinite
translation orbit because their finite nonempty supports cannot be fixed by
a nonzero translation. The maps in uniform-input lines 68–81 are
$$
P(1)=1,\quad P(\sigma^rM_O)=M_O,\quad G(1)=0,\qquad
G(\sigma^rM_O)=
\begin{cases}
-\sum_{j=0}^{r-1}\sigma^jM_O,&r>0,\\
0,&r=0,\\
\sum_{j=r}^{-1}\sigma^jM_O,&r<0.
\end{cases}
$$
Extend them $R$-linearly. Write $\pi_0(f)$ for the scalar coefficient of the word $1$,
viewed as a constant polynomial, and $P_+=P-\pi_0$.

Direct telescoping on each word gives the three useful identities
$$
(1-\sigma)G=1-P,\qquad
P(1-\sigma)=0,\qquad
G(1-\sigma)=1-\pi_0.
$$
For example, if $r>0$, applying $1-\sigma$ to
$-\sum_{j=0}^{r-1}\sigma^jM_O$ gives $\sigma^rM_O-M_O$;
the negative-index sum has the same telescoping boundary. The third identity
follows from $G(\sigma^rM_O)-G(\sigma^{r+1}M_O)=\sigma^rM_O$.
Constants are separately sent to zero by $G$ and fixed by $P$.

It follows that
$$
P_+f=0\iff f\in(1-\sigma)A_R+R,
\qquad
(1-\sigma)f\in R\Longrightarrow f\in R.
$$
If $P_+f=0$, use $f=(1-\sigma)Gf+P(f)$, with $P(f)$ constant.
If $f\in(1-\sigma)A_R+R$, apply $P_+$ to obtain $P_+f=0$.
For the last implication apply $G$ and obtain $f-\pi_0(f)=0$.
In particular $\ker(1-\sigma)=R$.

The maps $P,G,\pi_0$ are finite sums on any input word and involve only fixed
integer coefficients in the word basis. Combined with Section 5.1, this proves
that they commute with every allowed specialization and always return global
polynomials. Their normalization is the **normal** constant coefficient, not
the coefficient of $x^0y^0$ in the ordinary monomial basis.

**Status for uniform-input lines 55–100: `PROVABLE AS STATED`.** The explicit
unit-triangular argument above supplies an independent check of the compressed
ring-extension assertion; no additional assumption is needed.

## 6. Uniform theorem: logarithms, recursion, and uniqueness

### 6.1 Every tangent-to-identity symplectic logarithm is Hamiltonian

If $C=1+T$ with $T$ raising parameter order by at least one, the series
$L=\log C$ and $\exp(tL)$ are well defined order by order. At any fixed order,
$\exp(tL)(f)$ is polynomial in $t$ with polynomial coefficients in $x,y$.
For every nonnegative integer $t$, it equals the iterate $C^t$, so the
multiplicativity identity holds at all those integers. A polynomial over a
characteristic-zero field vanishing there is zero; coefficientwise
differentiation at $t=0$ gives the Leibniz identity for $L$. Applying the
same argument to the Poisson identity gives that $L$ is a Poisson derivation.
This reasoning also holds in a fixed truncated parameter ring: coefficientwise
polynomial identities remain available, or a finite Vandermonde argument over
the rational numbers gives the same result.

Each coefficient $V=a\partial_x+b\partial_y$ of $L$ is polynomial and
Poisson. Evaluating bracket preservation on $x,y$ gives $a_x+b_y=0$.
Conversely this equation makes the bracket-preservation defect vanish on
the generators and hence on every polynomial. Integrate $b$ in $x$ to a
polynomial $F_0$. Then $-a-(F_0)_y$ is independent of $x$, so it has a
polynomial primitive in $y$. Adding that primitive gives
$F_x=b$ and $F_y=-a$, and thus $V=\operatorname{ad}_F$ for the stated sign
convention. Characteristic zero supplies the needed denominators.

Coefficientwise, therefore,
$$
C_\varepsilon=\exp(\operatorname{ad}_{H_\varepsilon}),\qquad
H_\varepsilon=\sum_{n\ge1}\varepsilon^n h_n.
$$
The Hamiltonians are unique after $\pi_0(h_n)=0$ is imposed, because two
potentials for the same derivation differ by a scalar. Exponential and
logarithm are mutually inverse in the parameter filtration. No spatial
completion or convergence hypothesis has entered the argument.

### 6.2 The canonical recursion is defined before imposing any obstruction

Set $h_1=h-\pi_0(h)$ and, for $n\ge2$, define
$$
E_n=[\varepsilon^n]\operatorname{BCH}
\left(\sum_{j<n}\varepsilon^j h_j,
-\sigma\sum_{j<n}\varepsilon^j h_j\right),\quad
h_n=-G(E_n),\quad \Theta_n=P_+(E_n).
$$
At each fixed parameter order there are only finitely many BCH Lie words.
The coefficients of those words are rational; the Poisson bracket, $\sigma$,
and the maps of Section 5 all preserve $A_R$. Thus these formulas define
universal elements of $A_R$ at every stage, even at parameter points where an
earlier obstruction is nonzero. No division by an obstruction or solvability
assumption is used in defining the next stage.

Adding $\varepsilon^n h_n$ to the partial Hamiltonian changes the order-$n$
BCH coefficient only by $(1-\sigma)h_n$, since a bracket involving that term
and any other input has parameter order at least $n+1$. Consequently the
corrected coefficient is $P(E_n)$, whose induced derivation vanishes exactly
when $\Theta_n=0$. As a sign cross-check,
$$
E_2=-\tfrac12\{h_1,\sigma h_1\},\qquad
h_2=\tfrac12G\{h_1,\sigma h_1\}.
$$
This is precisely the obstruction in Section 4.3, with its constant part
discarded for the justified reason that constants induce zero derivations.

### 6.3 Finite-order existence is equivalent to these very equations

After specialization, vanishing of $\Theta_2,\ldots,\Theta_m$ makes every
corrected coefficient of orders $2$ through $m$ constant. The first BCH
coefficient is $h-\sigma h$. Applying the inner-derivation map and exponentiating
gives the desired conjugacy modulo $\varepsilon^{m+1}$.

Conversely, take a symplectic conjugator through order $m$, tangent to the
identity, and write its logarithm as a normalized Hamiltonian
$F=\sum_{j=1}^m\varepsilon^j f_j$. At order one,
$(1-\sigma)(f_1-h_1)$ is constant. Section 5.2 and the normalization give
$f_1=h_1$. If $f_j=h_j$ for $j<n$, the order-$n$ equation is
$$
(1-\sigma)f_n+E_n\in\mathbb C.
$$
Applying $P_+$ gives $\Theta_n=0$. The canonical $h_n$ then solves the same
equation modulo constants, and subtraction gives
$(1-\sigma)(f_n-h_n)\in\mathbb C$. The zero-normal-constant condition makes
$f_n=h_n$. This proves necessity and uniqueness at each finite order.

The full recursion therefore gives a compatible full conjugator exactly when
all obstructions vanish. It also proves uniqueness of the full conjugator;
no separate choice or inverse-limit existence principle is being assumed.
Hamiltonian potentials remain nonunique without the explicitly stated
constant normalization.

Even if the wording of the finite-order clause were read as not prescribing
the constant term of its conjugator, it would not change its existence
assertion: at order zero, $C_0\sigma C_0^{-1}=\sigma$. Multiplication on the
right by the constant automorphism $C_0^{-1}$ makes the conjugator tangent to
the identity without changing the conjugacy equation.

**Status for uniform-input lines 104–166: `PROVABLE AS STATED`.** In particular,
arbitrary finite-order symplectic solutions cannot evade the canonical
obstruction equations by choosing different polynomial Hamiltonians.

## 7. Uniform theorem: Noetherianity, equation zeros, and homogeneity

Each $\Theta_n$ has finite support in the representative-word basis. Let
$I_m\subset R$ be generated by all its scalar coefficients for $2\le n\le m$.
These ideals form an ascending chain, and $I_\infty=\bigcup_{m\ge2}I_m$ is
an ideal. The finite-variable polynomial ring over $\mathbb Q$ is Noetherian
by the Hilbert basis theorem, and localization preserves Noetherianity.
Hence $I_\infty$ has finitely many generators. Each belongs to some $I_m$;
taking the largest of these finitely many indices, and at least $2$, gives
$$
I_\infty=I_{N(d,D)}.
$$
All data here were defined once over the universal ring for fixed $d,D$.
Thus the chosen integer is uniform in every allowed coefficient of $p,h$.
If the ideal is zero, taking $N=2$ meets the stated convention.

For a complex parameter point $\phi:R\to\mathbb C$, Section 5.1 gives
$$
\phi(\Theta_n)=0\text{ as a polynomial}
\iff
\phi(c)=0\text{ for each representative coefficient }c\text{ of }\Theta_n.
$$
This equivalence uses the specialized basis, not a generic linear
independence assertion. Therefore $\phi(I_N)=0$ is equivalent to vanishing
of all obstruction stages. Section 6.3 gives exactly the claimed equivalence
between conjugacy modulo $\varepsilon^{N+1}$ and full formal conjugacy.
In particular the finite-order statement does not replace a fixed prescribed
curve by an arbitrary choice of higher-order perturbation terms.

The locus is $V(I_N)$ in the coefficient space $a_d\ne0$. Coefficients in $R$
are Laurent polynomials in $a_d$; multiplying each of the finitely many
equations by a sufficiently large power of $a_d$ produces ordinary polynomial
equations with the same zeros on this coefficient space. Thus the use of
the word “polynomial” for the equations introduces no hidden restriction.
No claim of closedness across the boundary $a_d=0$ is needed or made.

Give $b_{uv}$ weight one and $a_j,a_d^{-1}$ weight zero. The orbit coordinates
and all basis changes depend only on the $a$ variables; hence $\sigma,P,G$
and $\pi_0$ preserve this grading. The normalized $h_1$ has weight one.
If $h_j$ has weight $j$ for $j<n$, each BCH Lie word contributing at parameter
order $n$ has input orders summing to $n$ and hence coefficient weight $n$.
The Poisson bracket differentiates only $x,y$, so it adds those coefficient
weights. It follows that $E_n,h_n,\Theta_n$ are homogeneous of weight $n$.
The zero polynomial is allowed at any of these homogeneous weights.

Consequently the obstruction ideals have homogeneous generators in the
$h$-coefficients, and each fixed-$p$ fiber is an algebraic cone. Clearing a
power of $a_d$ does not alter this grading. Also
$h\mapsto h+c$ leaves $h_1$ and the full curve unchanged, so all constant
Hamiltonians lie in every fiber, not merely the zero Hamiltonian.

**Status for uniform-input lines 170–195 and the main claim at lines 8–35:
`PROVABLE AS STATED`.** The proof provides neither a numerical value of $N$
nor a stopping test. An equality at a finite pair of successive ideals is
not a certificate that later stages cannot add equations.

## 8. Special cases and scope checks

| Case or boundary | Verified outcome |
| --- | --- |
| Arbitrary constant and lower coefficients of $p$, including zero | Allowed throughout. Only the leading coefficient must remain nonzero; the extremal word and the unit-triangular basis do not depend on lower coefficients. |
| $d=2$ | Allowed. The highest derivative degree is one, the extremal word has degree $r\ge1$, and all basis/splitting arguments still apply. |
| Nonmonic $p$ | Allowed. Powers of its nonzero leading coefficient are units in the universal ring; no monic coordinate normalization is assumed. |
| $D=0$, or any constant $h$ | $h_1=0$, all $E_n,\Theta_n,h_n$ vanish, $U_\varepsilon=\sigma$, and the unique tangent-to-identity conjugator is the identity. One may take $N(d,0)=2$. |
| $h=0$ | Included in the preceding case and in every homogeneous cone. |
| Empty or singleton orbit-linear support, at any integer index | The bracket is respectively $0$ or $-u^2$; the exact commuting-derivation conjugacy applies. |
| Nonsingleton orbit-linear support with gaps or complex coefficients | Only the two extreme nonzero coefficients are used; gaps and cancellation of other coefficients cannot remove their unique top word. |
| Positive characteristic, $d<2$, or $a_d=0$ | Outside the statements. Characteristic zero is used in derivatives, logarithms/BCH, and Hamiltonian integration; exact degree is used in the basis and top-word arguments. |

No assertion is made about a spatially local formal category, analytic
convergence, uniformly bounded spatial degrees of the conjugator, an effective
bound or recognizable termination for $N$, a finite classification for
unbounded $D$, or finite determinacy under arbitrary changes of higher
perturbation coefficients. No general-polynomial classification is inferred
from the orbit-linear calculation.

## 9. Claim matrix, necessary repairs, and final findings

| Claim | Input binding | Status |
| --- | --- | --- |
| Continuant formula and unique highest standard word | Orbit lines 61–104 | `PROVABLE AS STATED` |
| Nonsingleton orbit-linear support has a nonzero second-order class | Orbit lines 108–138 | `PROVABLE AS STATED` |
| Second-order necessity and exact singleton conjugacy | Orbit lines 140–177 | `PROVABLE AS STATED` |
| Universal basis, splitting, and all-specialization compatibility | Uniform lines 55–100 | `PROVABLE AS STATED` |
| Every formal/truncated tangent-to-identity symplectic automorphism has a normalized polynomial Hamiltonian logarithm | Uniform lines 104–129 | `PROVABLE AS STATED` |
| Canonical recursion, finite-order equivalence, and unique full conjugator | Uniform lines 133–166 | `PROVABLE AS STATED` |
| Uniform finite index, closed locus, and homogeneous cone equations | Uniform lines 170–195 | `PROVABLE AS STATED` |
| A computed/effective index or arbitrary-perturbation finite determinacy | Explicitly excluded by uniform lines 31–35 and 209–214 | Not claimed; not supplied by this review |

The only required correction was the malformed parameter command in orbit
line 28; the separately hash-bound literal erratum closes it. There is no
remaining mathematical repair or missing hypothesis for either reviewed
claim. For manuscript preparation, the unit-triangular ring argument, the
identity $G(1-\sigma)=1-\pi_0$, and the treatment of Laurent equations in this
report can be incorporated as expository expansions of already valid steps.
They do not alter the scientific statement or reopen accepted Paper29 results.

The review outcome is limited to these frozen claims and the stated
dependencies. It grants no novelty, candidate-selection, long-manuscript
capacity, Route, or artifact-acceptance status. The author comparison to the
Melnikov literature and any subsequent extension require their own evidence.

Final findings: both mathematical claims survive unchanged; the literal
erratum is verified; no unresolved proof blocker or counterexample was found.
The completed report's SHA256 is to be supplied with the handoff, since a file
cannot contain its own final content hash without changing that content.
