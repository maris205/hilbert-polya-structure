# R10 A1: the all-level annihilator ideal

2026-09-10 UTC. One bounded proof-only follow-up; no new contract.

## Frozen exact target

For every odd prime $p$, let $k=\overline{\mathbb F}_p$, let $c\in k$,
and put $f(x)=x^2+c$. Retain an arbitrary full rational norm-one
function

$$w=\eta A/B,\qquad \eta\in\{1,-1\},\quad
\deg A=\deg B=m,\quad B(X)=(-1)^mA(-X),$$

where $A,B$ are monic and coprime. Set $F_n=f^{\circ n}-x$,
$H_n(x)=\eta^n\prod_{i=0}^{n-1}A(f^{\circ i}(x))-
\prod_{i=0}^{n-1}B(f^{\circ i}(x))$, and

$$I_w=\{S\in k[x]: F_n\mid S F_n'H_n\text{ for every }n\ge1\}.$$

The native clock is one application of $f$; every ordinary period,
including multiples of $p$, is retained. The original MS6 problem is
unchanged. Its cofinite ordinary primitive-cycle product condition
implies $I_w\ne0$ by accepted R9, but no inverse implication is assumed.

**Exact new target:** if $I_w\ne0$, force it to contain a nonzero
polynomial of degree bounded explicitly in terms of $m$ (any necessary
dependence on $p,c$ must be stated); preferably prove $I_w=0$ for every
nonconstant norm-one $w$. The latter is an all-annihilator separation
statement, not a restatement of (CP). A genuine counterexample to a
claimed bound is also a decisive outcome.

**Initial status: NOT CURRENTLY JUSTIFIED.** Use one finite-state/module
mechanism extending the accepted fixed-$S$ R9 certificate, not a second
mechanism or a degree/parameter ladder. Exact gcd/lcm ideal formulas
are allowed interfaces but are not themselves a new bridge. Noetherianity
does not give finite stabilization of arbitrary descending intersections
of principal ideals.

The [accepted R9 proof](../../continuation_round9/a1_general_quadratic_normone/REPORT.md)
is read-only. Its fixed-$S$ theorem and $\mathrm{(CP)}\Rightarrow I_w\ne0$
are imported with their stated scope, not reproved here. Only this
allocated report may be written. No mathematical program, census,
new/nested agent, external API/model upload, GPU, Git, old/shared-file
or PDF action is allocated. At most one targeted source batch is
permitted if genuinely needed.

## 1. Outcome and precise theorem

**Degree-bound target: PROVABLE AS STATED, author proof below.**
The stronger assertion $I_w=0$ for every nonconstant norm-one $w$
remains **NOT CURRENTLY JUSTIFIED**. No inverse implication to (CP),
new contract, or paper admission is claimed.

Put

$$b=m+2,\qquad D=4b^2,\qquad N=5D+1=20(m+2)^2+1,$$

and define the explicit polynomial

$$S_* = \prod_{r=1}^{D}(f^{\circ r}(x)-x),\qquad
\deg S_*=2^{D+1}-2. \tag{1.1}$$

For each $n\ge1$, let

$$q_n=\frac{F_n}{\gcd(F_n,F_n'H_n)},\qquad
L_N=\operatorname{lcm}(q_1,\ldots,q_N), \tag{1.2}$$

where gcd and lcm are monic.

**Theorem 1.1.** Under all the frozen hypotheses:

1. If $I_w\ne0$, every root of its monic generator has ordinary
   least period at most $D$; in particular $S_*\in I_w$.
2. Thus $I_w\ne0$ forces a nonzero annihilator of degree at most
   $2^{D+1}-2$, independent of the coefficients of $w$, of $p$, and
   of $c$. The polynomial supplying the bound depends on $c$ through
   $f$ as in (1.1).
3. The entire ideal has the finite decision rule

   $$I_w=\begin{cases}
   (L_N),& L_N\mid S_*,\\
   (0),& L_N\nmid S_*.
   \end{cases} \tag{1.3}$$

In particular $I_w\ne0$ if and only if the specific $S_*$ satisfies
the R9 identities at all levels $1\le n\le N$. None of these tests
is executed here.

The new bridge is not the gcd/lcm description by itself. It is the
uniform period bound obtained from a finite-dimensional coefficient
tensor, which makes the previously unknown $S$ replaceable by (1.1).
There is no assertion that the total number of exceptional points is
at most $D$.

## 2. Strategy and dependencies

The proof uses one finite-state mechanism: the four-block R9 matrix
representation bounds a split coefficient tensor's rank. A nonzero
annihilator makes the tensor supported on finitely many periodic
points. Polynomial evaluation gives the opposite rank bound when a
return is sufficiently long. Each already visible cycle can be kept
visible along arbitrarily long returns, forcing its period to be
bounded by the fixed matrix-space dimension.

The dependency map is:

1. Local derivative orders identify the annihilator ideal with a
   finite-support question, including all wild multiplicities.
2. The exact top-coefficient identity retains multiplicities modulo
   $p$ and expresses the R9 tensor as a sum over visible points.
3. The accepted R9 four-block representation gives rank at most
   $D$; two polynomial-evaluation matrices give rank equal to the
   number of visible points for sufficiently long returns.
4. The local return germ and finite multiplicative orders in
   $\overline{\mathbb F}_p$ retain a specified visible cycle along
   arbitrarily long returns. This proves the native period bound.
5. The period bound gives $S_*$, after which the accepted fixed-$S$
   R9 theorem gives the explicit finite decision rule (1.3).

The full R9 theorem is not reproved. The exact imported statements
are its Section 3 fixed-$S$ bound and Section 5 coefficient matrices,
specialized below to $S=1$. No external theorem or source-query batch
is needed for the additional elementary arguments.

## 3. The annihilator ideal is radical

For a root $a$ of $F_n$, write

$$e_n(a)=\operatorname{ord}_aF_n\in\mathbb Z_{\ge1}.$$

Locally $F_n=(x-a)^eG$ with $G(a)\ne0$. If $p\nmid e$, then
$\operatorname{ord}_aF_n'=e-1$. If $p\mid e$, differentiation
gives $\operatorname{ord}_aF_n'\ge e$. Consequently $q_n$ is
squarefree, with root set

$$B_n=\{a:F_n(a)=0,\quad
e_n(a)H_n(a)\ne0\text{ in }k\}. \tag{3.1}$$

For every $S\in k[x]$, divisibility by $F_n$ is therefore equivalent
to simple vanishing on $B_n$:

$$F_n\mid S F_n'H_n\quad\Longleftrightarrow\quad
q_n\mid S. \tag{3.2}$$

Set $\mathcal B=\bigcup_{n\ge1}B_n$. If $\mathcal B$ is infinite, its distinct points
cannot all be roots of a nonzero polynomial, so $I_w=(0)$. If $\mathcal B$
is finite, put

$$Q_{\mathcal B}=\prod_{a\in\mathcal B}(x-a),$$

with $Q_{\mathcal B}=1$ when $\mathcal B$ is empty. Equation (3.2) proves

$$I_w\ne0\quad\Longleftrightarrow\quad\mathcal B\text{ is finite},
\qquad I_w=(Q_{\mathcal B})\text{ in that case}. \tag{3.3}$$

This is an exact interface, not an appeal to stabilization of a
descending sequence of ideals.

Each $B_n$ is a union of full ordinary cycles. Indeed, at a point of
least period dividing $n$, cyclically permuting the $n$ factors shows
$H_n(f(a))=H_n(a)$. The multiplicities $e_n$ are also constant on a
cycle. If the cycle contains $0$, the derivative of $f^{\circ n}$
vanishes at every point of that cycle, so $F_n'=-1$ there and all
these multiplicities are one. Otherwise each cycle point is nonzero,
and the identity

$$F_n(f(x))=F_n(x)\bigl(2x+F_n(x)\bigr) \tag{3.4}$$

compares the orders at $a$: substitution by $f$ has local degree
one because $2a\ne0$, and the second factor on the right is a unit.
It follows that $e_n(f(a))=e_n(a)$. This proves the asserted cycle
invariance, and $f$ acts as a permutation on $B_n$.

## 4. The exact coefficient tensor, with multiplicities

Let $\mathcal A_n$ and $L_n$ be the cyclic quadratic algebra and its
top squarefree coefficient functional from R9. Under
$\mathcal A_n\simeq k[x]/(F_n)$, $L_n$ takes the coefficient of
$x^{2^n-1}$ in the remainder of degree below $2^n$.

For every polynomial $R\in k[x]$, one has

$$L_n(F_n'H_nR)
=\sum_{F_n(a)=0}e_n(a)H_n(a)R(a). \tag{4.1}$$

Here and below the positive integer $e_n(a)$ on the right is mapped
to $k$; the sum is over distinct roots. To prove (4.1), polynomial
division shows that its left side is the coefficient of $x^{-1}$
in the Laurent expansion of $F_n'H_nR/F_n$ at infinity. Factoring
$F_n$ over $k$ gives the rational identity

$$\frac{F_n'}{F_n}=\sum_{F_n(a)=0}\frac{e_n(a)}{x-a}.$$

The coefficient of $x^{-1}$ in $H_n(x)R(x)/(x-a)$ is
$H_n(a)R(a)$, by division by $x-a$. Summing proves (4.1), also when
some $e_n(a)$ vanish in characteristic $p$.

For a binary word $\epsilon=(\epsilon_0,\ldots,\epsilon_{n-1})$,
define

$$\mathcal T_n(\epsilon)=
L_n\!\left(F_n'H_n\prod_{i=0}^{n-1}X_i^{\epsilon_i}\right).$$

Equation (4.1) gives

$$\mathcal T_n(\epsilon)=
\sum_{a\in B_n}\gamma_n(a)
\prod_{i=0}^{n-1}f^{\circ i}(a)^{\epsilon_i},\qquad
\gamma_n(a)=e_n(a)H_n(a)\ne0. \tag{4.2}$$

In particular this is not an unweighted count of ordinary points,
nor has multiplication by $F_n'$ been inverted at wild roots.

For completeness, the exact R9 matrix interface used here is as
follows. For $h(X)=\sum_jh_jX^j$, let

$$T_h(r,s)=\sum_{q\ge s}\binom qs(-c)^{q-s}h_{2q+1-r},
\qquad 0\le r,s\le m+1.$$

Use $h=X^{j+\epsilon}A$ or $X^{j+\epsilon}B$, with
$j,\epsilon\in\{0,1\}$, and put

$$M_\epsilon=\operatorname{diag}\!\left(
2\eta T_{X^{1+\epsilon}A},\
\eta T_{X^\epsilon A},\
2T_{X^{1+\epsilon}B},\
T_{X^\epsilon B}\right),$$

$$E=\operatorname{diag}(I_b,-I_b,-I_b,I_b).$$

R9 Section 5 with $S=1$ gives

$$\mathcal T_n(\epsilon)=
\operatorname{tr}\bigl(E M_{\epsilon_0}\cdots
M_{\epsilon_{n-1}}\bigr). \tag{4.3}$$

Every matrix belongs to the block-diagonal algebra

$$\mathcal D=\bigoplus_{j=1}^{4}\operatorname{Mat}_b(k),
\qquad \dim_k\mathcal D=4b^2=D. \tag{4.4}$$

The Jacobian signs and the period-dependent powers of $\eta$ are
those of the accepted R9 formula. No reconstruction theorem from
trace characters is used.

## 5. Two rank bounds for the same split tensor

Fix $n$ and a cut $1\le h\le n-1$. Index a matrix $\mathcal F_{n,h}$
by binary words $u$ of length $h$ and $v$ of length $n-h$, with entry
$\mathcal T_n(uv)$, the value on their concatenation.

**Upper bound.** By (4.3), this entry is
$\operatorname{tr}(E M_uM_v)$. It is the value of one bilinear
pairing on the two elements $M_u,M_v\in\mathcal D$. Choosing a
$k$-basis of the $D$-dimensional space $\mathcal D$ factors
$\mathcal F_{n,h}$ through a space of dimension $D$, and gives

$$\operatorname{rank}\mathcal F_{n,h}\le D. \tag{5.1}$$

This does not require the trace pairing to be nondegenerate.

**Lower bound for long halves.** Write $t_n=|B_n|$, and assume

$$2^h\ge t_n,\qquad 2^{n-h}\ge t_n. \tag{5.2}$$

For each left word $u$, the polynomial
$\prod_{i=0}^{h-1}f^{\circ i}(x)^{u_i}$ is monic of degree
$\sum_i u_i2^i$. These are the distinct degrees from zero to
$2^h-1$, so the polynomials form a basis of the space of polynomials
of degree below $2^h$. Evaluation at the $t_n$ distinct points of
$B_n$ has rank $t_n$: the Lagrange interpolation polynomials of
degree below $t_n$ give every function on this set. Thus the matrix

$$V_{u,a}=\prod_{i=0}^{h-1}f^{\circ i}(a)^{u_i}
\quad(a\in B_n)$$

has full column rank $t_n$.

The right evaluation matrix is

$$W_{v,a}=\prod_{j=0}^{n-h-1}
f^{\circ j}(f^{\circ h}(a))^{v_j}.$$

Since $f^{\circ h}$ permutes $B_n$, the same polynomial basis and
interpolation argument, now with degrees below $2^{n-h}$, gives
full column rank $t_n$ for $W$. Equation (4.2) gives

$$\mathcal F_{n,h}=V\operatorname{diag}
\bigl(\gamma_n(a):a\in B_n\bigr)W^{\mathsf T}. \tag{5.3}$$

The diagonal matrix is invertible. The two full-column-rank matrices
have left inverses over $k$; multiplying (5.3) by a left inverse of
$V$ and a right inverse of $W^{\mathsf T}$ proves rank at least
$t_n$. The displayed factorization proves rank at most $t_n$.
Consequently

$$|B_n|=\operatorname{rank}\mathcal F_{n,h}\le D
\quad\text{whenever (5.2) holds}. \tag{5.4}$$

If $B_n$ is empty, this conclusion holds with rank zero.

## 6. A specified visible cycle persists at arbitrarily long returns

**Lemma 6.1.** Suppose $a\in B_{n_0}$. There are arbitrarily large
positive integers $q$ with

$$a\in B_{qn_0},\qquad
e_{qn_0}(a)=e_{n_0}(a),\qquad
H_{qn_0}(a)=H_{n_0}(a). \tag{6.1}$$

**Proof.** Put $g=f^{\circ n_0}$ and $\mu=g'(a)$. If $\mu\ne1$,
the multiplicity $e_{n_0}(a)$ is one. When $\mu=0$, the derivative
of $g^{\circ q}$ at $a$ remains zero, and the multiplicity remains
one for every positive $q$. When $\mu\ne0,1$, choose $q$ congruent
to one modulo the finite multiplicative order of $\mu$. Then
$\mu^q=\mu\ne1$, and the multiplicity again remains one.

If $\mu=1$, put $e=e_{n_0}(a)\ge2$ and write the local expansion

$$g(a+z)=a+z+u z^e+O(z^{e+1}),\qquad u\ne0.$$

The first nonlinear term exists because $\deg g=2^{n_0}>1$.
Composition adds the coefficients of $z^e$ modulo $z^{e+1}$, so
induction gives

$$g^{\circ q}(a+z)=a+z+quz^e+O(z^{e+1}).$$

Hence $q\equiv1\pmod p$ preserves the multiplicity $e$.

Set

$$\alpha=\eta^{n_0}\prod_{i=0}^{n_0-1}A(f^{\circ i}(a)),
\qquad \beta=\prod_{i=0}^{n_0-1}B(f^{\circ i}(a)).$$

Since $a$ is fixed by $f^{\circ n_0}$, the product over $q$
successive blocks gives

$$H_{qn_0}(a)=\alpha^q-\beta^q. \tag{6.2}$$

Every nonzero element among $\alpha,\beta,\mu$ has finite
multiplicative order, since $k=\overline{\mathbb F}_p$. Choose a
positive integer $M$ divisible by $p$ and by all those orders, and
take $q=1+jM$ for arbitrarily large integers $j\ge0$. Each nonzero
$\alpha$ or $\beta$ is unchanged by the $q$th power; a zero value
also remains zero. Thus (6.2) equals $\alpha-\beta=H_{n_0}(a)$.
In particular the case where exactly one of these products is zero
is included. Both cannot be zero here because $a\in B_{n_0}$.

The same choice of $q$ satisfies the multiplier and characteristic
conditions above. The multiplicity is unchanged as an integer and
its residue in $k$ remains nonzero. This proves (6.1). $\square$

## 7. Uniform native-period and degree bounds

Assume $I_w\ne0$, so $\mathcal B$ is finite by (3.3). If $\mathcal B$ is empty,
$I_w=(1)$ and the conclusions hold. Otherwise set $t=|\mathcal B|\ge1$.
Choose $a\in\mathcal B$ and an $n_0$ with $a\in B_{n_0}$, and let $r$
be the ordinary least period of $a$.

By Lemma 6.1, there are arbitrarily large $n=qn_0$ with
$a\in B_n$. Each $B_n$ contains the full $r$-cycle of $a$ by
Section 3. Choose one such $n$ large enough that, with
$h=\lfloor n/2\rfloor$,

$$h\ge1,\qquad 2^h\ge t,\qquad 2^{n-h}\ge t.$$

Since $|B_n|\le t$, the two bounds in (5.2) hold. Therefore

$$r\le|B_n|\le D. \tag{7.1}$$

This argument is applied separately to each already visible cycle;
it does not assume that all of $\mathcal B$ can be made visible at a single
return level.

Every $a\in\mathcal B$ is thus a root of at least one $F_r$ with
$1\le r\le D$. Consequently $Q_{\mathcal B}\mid S_*$, which proves
$S_*\in I_w$ and the degree bound in Theorem 1.1. This is the new
finite-state stabilization bridge. Its dimension bound concerns
each long-return visible set $B_n$; the total $|\mathcal B|$ need not be at
most $D$.

## 8. Eliminating the unknown annihilator with a finite decision rule

Let $L_N$ be as in (1.2). By (3.2), it generates the finite-level
intersection

$$\bigcap_{1\le n\le N}(q_n)=(L_N). \tag{8.1}$$

If $I_w\ne0$, Section 7 gives $S_*\in I_w$, so
$L_N\mid S_*$. This proves that $L_N\nmid S_*$ forces $I_w=(0)$.

Conversely, suppose $L_N\mid S_*$. Its degree is at most
$2^{D+1}-2$, and therefore its R9 integer $k_{L_N}$ is at most
$D+1$ (with $k_{L_N}=0$ if $L_N=1$). By definition, $L_N$ satisfies
all annihilation identities at levels $1\le n\le N$. The accepted
R9 fixed-$S$ theorem requires only levels through

$$k_{L_N}+16(m+2)^2
\le D+1+4D=N.$$

It follows that $L_N\in I_w$. Since $I_w\subseteq(L_N)$ by (8.1)
and $I_w$ is an ideal, equality follows. This proves (1.3).

Finally, $\deg S_*=2^{D+1}-2$ has R9 integer $k_{S_*}=D+1$.
Applying the same accepted theorem directly to $S_*$ proves the
equivalent finite test asserted after Theorem 1.1. $\square$

In module language, the cyclic $k[x]$-module generated by the
family $(F_n'H_n\bmod F_n)_{n\ge1}$ has annihilator $I_w$.
When this annihilator is nonzero, the module is isomorphic to
$k[x]/(L_N)$ and has dimension at most $2^{D+1}-2$. The rank argument
proves this bound; Noetherianity of $k[x]$ alone does not.

## 9. Boundaries, source subtraction, and freeze

The [R9 author proof, Sections 3 and 5](../../continuation_round9/a1_general_quadratic_normone/REPORT.md)
was actually read and is used only for the fixed-$S$ certificate and
its explicit coefficient matrices. Its accepted final 437-line
author hash is
`6c7a21d2ceaecf585f7c37f8c57dcce79ce1243d2ec9926059f826adc9e15d40`.
The coordinator reported completion of its full author/review read
with zero mathematical or provenance must-fixes. No R9 byte was
changed. The coordinator also independently checked the proposed
R10 rank/persistence interface and emphasized the zero-product and
multiplicity branches; those are proved explicitly above. This is
not represented as a completed independent R10 review.

The nonzero-annihilator degree-bound target is proved here at its
full stated parameter scope. This is more than the accepted fixed-$S$
R9 result: the unknown annihilator is replaced by one explicit $S_*$,
and (1.3) decides the all-level ideal from finitely many levels.

The proof does **not** show that the decision always yields $(0)$
when $w$ is nonconstant. To obtain all-annihilator separation from
(1.3), one still has to prove

$$L_N\nmid S_*\quad\text{for every nonconstant norm-one }w.$$

Nor is an inverse implication from $I_w\ne0$ to (CP) imported or
proved here. The stronger separation assertion and the original
general MS6 existence question remain **NOT CURRENTLY JUSTIFIED**.
The complete norm-one function and all its atom multiplicities
remain in the formulas; no factorwise (CP) inference is used.

No mathematical execution, census, new/nested agent, external
API/model upload, GPU, Git, old/shared-file or PDF action was
performed. No source-query batch was needed. Only this allocated
report was written. The proof-writer and Route-A workflow boundaries
are retained: author-proved auxiliary progress is not independent
review, a new contract, a completed paper, or target arithmetic.

**Frozen outcome:** Theorem 1.1 is an author proof awaiting
independent review; the preferred all-annihilator separation remains
open. This bounded finite-state attempt stops here, without a second
mechanism, parameter ladder, or change to the original MS6 question.
