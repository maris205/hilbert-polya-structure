# Paper30: parity-sensitive reconstruction from complete action spectra

Date: 2026-09-06. AUTHOR_PROOF_PREFLIGHT, not a selected paper.
This new proof package strengthens the separate binomial-action probe; it
does not change that frozen input or any stopped formal-gauge candidate.
Route applicability: NOT_APPLICABLE. No manuscript or experiment is created.

## Claim

Let $d\ge3$ be odd, $B\in\mathbb C$, and fix
$$
p_{d,B}(x)=x^d+Bx,\qquad
P_{d,B}(x)=\frac{x^{d+1}}{d+1}+\frac B2x^2,\qquad
H_{d,B}(x,y)=(p_{d,B}(x)-y,x).
$$
Use the full periodic algebra, including short periods and local lengths,
$$
R_{n,B}=\mathbb C[x_0,\ldots,x_{n-1}]/
(x_i^d+Bx_i-x_{i-1}-x_{i+1})_i,
$$
and the characteristic polynomial $\chi_{n,B}$ of multiplication by
$$
\mathcal A_{n,B}=\sum_i(x_ix_{i+1}-P_{d,B}(x_i)).
$$
Indices are modulo $n$, with repeated neighbors retained for $n=1,2$.
Write $q=(d-1)/2$, $m=q+1$, and $\kappa=q/(q+1)$.

The claims are:

1. For every odd $d$ and $n\ge2$,
   $$
   \operatorname{Tr}(m_{\mathcal A_{n,B}}^q)
   =-n(d-1)d^{n-1}\left(-\frac\kappa2\right)^qB^m.
   \tag{A1}
   $$
2. If $d\equiv1\pmod4$, the complete spectra $\chi_1,\chi_2$ determine
   $B$ for all complex parameters. The smallest initial-period cutoff is
   exactly two, for every such $d\ge5$.
3. For $d=7$, equality of $\chi_1,\chi_2$ has exactly one nontrivial
   unordered parameter fiber, $\{2\mathrm i,-2\mathrm i\}$.
   The third-period spectra separate it. Thus the global minimum initial
   cutoff for the entire seventh-degree binomial family is exactly three.
4. In every degree $d\equiv3\pmod4$, $d\ge7$, the already constructed
   nonzero sign pairs share $\chi_1$ and *all* even-period spectra, but are
   not biholomorphically conjugate. This does not assert equality of all
   odd-period spectra or absence of a finite initial-period cutoff.

## Status

PROVABLE AS STATED at the author-proof stage. Independent mathematical
checking, current dedicated novelty assessment and candidate evaluation
remain separate obligations. The exact third-period distinction below
has a three-row hand-checkable trace certificate; it does not depend on
treating a large matrix computation as an unexplained oracle.

## Assumptions and dependencies

- The potential constant is fixed to zero, and the leading coefficient
  of $p$ is one. No coordinate-dependent re-normalization of action is used.
- The field is $\mathbb C$ and $d$ is fixed when parameters are compared.
- Spectra record characteristic polynomials and local lengths, not the
  full Jordan structure or the coordinate algebra itself.
- The frozen [binomial author probe](PAPER30_BINOMIAL_ACTION_HIGHER_DEGREE_PROBE_20260906.md),
  390 lines, SHA256
  `804be063faf1b07371c51b5dd8ca80bcd6fb402abdf7c678e411643aad363125`,
  was fully read by root. Its Steps 1–3 establish the full free basis,
  stationary action identity, and the following all-parameter factors:
  $$
  \chi_{1,B}(T)=T\left[T^q+
  \left(-\frac\kappa2\right)^q(B-2)^m\right]^2,
  \tag{A2}
  $$
  $$
  \chi_{2,B}(T)=T D_{-,B}(T)^2D_{+,B}(T)^2G_B(T)^4,
  \quad D_{\pm,B}(T)=T^q+(-\kappa)^q(B\pm2)^m.
  \tag{A3}
  $$
  Here $G_B\in\mathbb C[B,T]$ is monic of degree $q^2$.
  The proof treats reciprocal nonzero ratios $y/x$ on a nonempty simple
  parameter open, then extends polynomially to every parameter. It does
  not assume generic reducedness in the final result.
- The same probe proves the action-preserving even-period isomorphism and
  the weighted derivative-trace nonconjugacy test. They are restated below
  only to specify the exact interface, not counted as new root discoveries.

## Proof strategy

A homogeneous trace at total degree $d-1$ can return to a standard basis
monomial after exactly one reduction; that reduction must use a diagonal
linear term. This extracts the third power invariant $B^m$. The two
spectra also extract $(B-2)^m,(B+2)^m$ by the parity of factor multiplicities.
For odd $m$, reduction of roots of unity at a prime above two makes these
three translated powers an injective parameter map. When $m=4$, elementary
elimination leaves only the sign pair above. A three-variable, three-reduction
trace calculation separates that pair at the ninth action moment.

## 1. One-reduction trace lemma

More generally, over a characteristic-zero field let
$$
R=K[x_1,\ldots,x_n]/(x_i^d+\sum_jL_{ij}x_j)_i.
$$
The relatively prime monic leading terms $x_i^d$ give the standard basis
$x^\beta$, $0\le\beta_i<d$. Each substitution of $x_i^d$ by its linear
right-hand side reduces total degree by exactly $d-1$.

If $|\alpha|=d-1$, a contribution to the $x^\beta$ diagonal coefficient
of $x^\alpha x^\beta$ must therefore use exactly one substitution.
Using the $x_j$ term in the $i$th relation would require
$$
\alpha=d e_i-e_j.
$$
Nonnegative exponents force $j=i$ and $\alpha=(d-1)e_i$.
For this pure power the substitution is available precisely when
$\beta_i\ge1$, and its coefficient is $-L_{ii}$. Thus
$$
\operatorname{Tr}(m_{x^\alpha})=
\begin{cases}
-(d-1)d^{n-1}L_{ii},&\alpha=(d-1)e_i,\\
0,&\text{otherwise}.
\end{cases}\tag{A4}
$$
Further substitutions cannot contribute to the diagonal because they lower
degree again. This is a basis calculation, valid also at nonreduced fibers.

The stationary equations give
$$
\mathcal A_{n,B}=\kappa\left(\sum_i x_ix_{i+1}
-\frac B2\sum_i x_i^2\right).
\tag{A5}
$$
For $n\ge2$, $L_{ii}=B$. Since $2q=d-1$, the polynomial in (A5) raised
to the $q$th power is homogeneous of the degree required in (A4).
Its coefficient of each pure $x_i^{d-1}$ is $(-\kappa B/2)^q$;
no product containing an edge term can be a pure power. Summing (A4)
proves (A1), including the doubled edge in the two-period case.

## 2. Three translated powers are injective at every odd exponent

**Lemma.** If $m\ge3$ is odd, the map
$$
z\longmapsto\bigl(z^m,(z-2)^m,(z+2)^m\bigr)
\tag{A6}
$$
is injective on $\mathbb C$.

Suppose $z,w$ have the same image. If one of $z,z-2,z+2$ is zero,
the corresponding equality forces $w=z$. Otherwise all three are nonzero,
as are the corresponding expressions for $w$, and there are
$\zeta,\eta,\theta\in\mu_m$ such that
$$
w=\zeta z,\quad w-2=\eta(z-2),\quad w+2=\theta(z+2).
$$
Eliminating $z$ by cross multiplication, without dividing by any difference
of roots of unity, gives
$$
2\zeta-\zeta\eta-\zeta\theta-\theta-\eta+2\eta\theta=0.
\tag{A7}
$$
Take the ring of integers of $\mathbb Q(\mu_m)$ and a prime above $2$.
Reduction is injective on $\mu_m$: all $m$ roots are algebraic integers,
their product factorization reduces to $X^m-1$, and that polynomial is
separable in residue characteristic two because $m$ is odd. Distinct roots
therefore cannot acquire the same residue.

Reducing (A7) gives
$$
(\bar\zeta+1)(\bar\eta+\bar\theta)=0.
$$
The residue ring is a field. Injectivity implies either $\zeta=1$ or
$\eta=\theta$. The first case gives $w=z$. In the second, subtracting
the last two original equalities gives $4=4\eta$, so $\eta=1$ and again
$w=z$. This proves the lemma. The prime-above-two step is an elementary
cyclotomic argument, not a new general number-theoretic principle.

## 3. Complete two-period reconstruction for degrees one modulo four

From $\chi_1$ and the unique monic square root in (A2), recover $(B-2)^m$.
This also recovers $D_-$ in (A3). Divide $\chi_2$ by $TD_-^2$ and take
the unique monic square root, obtaining $D_+G_B^2$.

If $T^q+a$ has $a\ne0$, it has $q$ distinct nonzero roots; their odd
multiplicities in this product recover $T^q+a$. If $a=0$, the odd-root
support is empty or just the origin and cannot coincide with the nonzero
case. This recovers $(B+2)^m$ even at every collision parameter. Finally
(A1) at $n=2$ recovers $B^m$, since its known prefactor is nonzero.

When $d\equiv1\pmod4$, $m=(d+1)/2$ is odd, so (A6) determines $B$.
Conversely equal parameters give equal complete spectra.

The first period alone is insufficient: choose any nontrivial $m$th root
$\xi$ and compare $B=3$ with $B'=2+\xi$. They are distinct and satisfy
$(B-2)^m=(B'-2)^m=1$. Distinct parameters are not even biholomorphically
conjugate, by the invariant in Section 6 below. Hence the minimum initial
cutoff is exactly two for every $d=5,9,13,\ldots$.

## 4. All seventh-degree two-period fibers

Now $d=7$, $q=3$, $m=4$. Equality of the first two spectra gives equality
of $B^4,(B-2)^4,(B+2)^4$ by the same extraction. Since
$$
(B-2)^4+(B+2)^4=2B^4+48B^2+32,
$$
it also gives $B'^2=B^2$, so $B'=B$ or $B'=-B$.
In the latter case equality of the first spectrum requires
$$
(B-2)^4-(B+2)^4=-16B(B^2+4)=0.
$$
$B=0$ is not a distinct pair. The only possible nontrivial fiber is
$\{2\mathrm i,-2\mathrm i\}$. The action-preserving even-period
isomorphism in Section 6, together with (A2), proves that this pair really
has equal full $\chi_1,\chi_2$; it is not merely a low-moment ambiguity.

## 5. A three-row exact third-period separation certificate

Set $B=2\mathrm i$, $d=7$, $n=3$ and use variables $x,y,z$. The relations
are $x^7=-Bx+y+z$ and their permutations. Let
$$
f=xy+xz+yz-\mathrm i(x^2+y^2+z^2),\qquad
\mathcal A_{3,2\mathrm i}=\frac34f.
$$
Complex conjugation takes this algebra and action to those for $B=-2\mathrm i$.
It suffices to show that $\operatorname{Tr}(m_f^9)$ is not real.

A monomial of total degree $18$ can contribute to a basis diagonal only
after exactly three substitutions, each lowering degree by six. If $r_j$
counts substitutions at vertex $j$ and $s_j$ counts their linear outputs
at that vertex, then
$$
\alpha_j=7r_j-s_j,\qquad \sum r_j=\sum s_j=3.
\tag{A8}
$$
For monomials with all three exponents positive, this forces $r_j=1$.
Up to permutation the only possibilities are $(7,7,4),(7,6,5),(6,6,6)$.

For completeness, terms with support at most two contribute a real total.
In (A8), a zero exponent forces $r_j=s_j=0$, since $7r_j=s_j\le3$.
Thus their diagonal paths remain in the induced one- or two-vertex system,
and the unused basis exponents give a factor $7^{3-|S|}$. Every such
induced graph is bipartite. The substitution $x_j\mapsto\mathrm i(-1)^{c_j}x_j$
for a two-coloring maps parameter $B$ to $-B$ and preserves its action,
with the same check as Section 6 and edge weight one. Their action moments
are consequently real at $B=2\mathrm i$. Inclusion-exclusion over the
proper subsets $S\subset\{x,y,z\}$ isolates the proper-support total
and proves the assertion without discarding a possible imaginary term.

Here are all full-support contributions. $C_\alpha$ is the coefficient
of the displayed monomial in $f^9$, and $t_\alpha$ is its multiplication
trace in the full $343$-dimensional algebra.

| Exponent type $\alpha$ | Permutation multiplicity | $C_\alpha$ | $t_\alpha$ at $B=2\mathrm i$ |
| --- | ---: | --- | --- |
| $(7,7,4)$ | 3 | $6768-5544\mathrm i$ | $-588\mathrm i$ |
| $(7,6,5)$ | 6 | $12096-4536\mathrm i$ | $-672-588\mathrm i$ |
| $(6,6,6)$ | 1 | $12264+2352\mathrm i$ | $684$ |

The table is a finite arithmetic certificate with the following explicit
derivation of every column. The coefficients are the multinomial sums
$$
C_\alpha=\sum
\frac{9!(-\mathrm i)^{a+b+c}}{a!b!c!u!v!w!},
\quad
\begin{cases}
a+b+c+u+v+w=9,\\
2a+u+v=\alpha_1,\\
2b+u+w=\alpha_2,\\
2c+v+w=\alpha_3,
\end{cases}\tag{A9}
$$
over nonnegative integers. This directly evaluates to the three displayed
Gaussian integers; it does not use an eigenvalue calculation or interpolation.

To derive the traces, write the standard basis exponent as
$\beta\in\{0,\ldots,6\}^3$. Each substitution can occur only when the
current exponent is at least seven. In (A8) each vertex substitutes once.
For $(7,7,4)$ all three outputs must go to the third vertex. The coefficient
is $-B$, and the third vertex must have $\beta_3\ge1$. The other two
initial exponents always permit their substitutions. Thus
$t_{774}=-294B$.

For $(7,6,5)$ there is one output to the second vertex and two to the third.
According to which source supplies the output to the second vertex, the
products and the numbers of admissible basis exponents are
$$
\begin{array}{c|c|c}
\text{source of that output}&\text{coefficient}&\text{count}\\\hline
\text{first}&-B&7\cdot7\cdot6=294\\
\text{second}&B^2&7\cdot6\cdot6=252\\
\text{third}&1&7(7^2-1)=336.
\end{array}
$$
In the last case, either the second or the third initial exponent must be
positive to initiate their two-cycle; only their simultaneous zero fails.
Thus $t_{765}=-294B+252B^2+336$.

For $(6,6,6)$ the output assignment is a permutation. The identity has
coefficient $-B^3$ and count $6^3$; each of the three transpositions has
coefficient $-B$ and count $(7^2-1)6$; each of the two three-cycles has
coefficient one and count $7^3-1$. Consequently
$$
t_{666}=-216B^3-864B+684.
$$
Substituting $B=2\mathrm i$ proves the trace column. The counts use the
monic relations and include all basis vectors, so remain full-scheme traces.

The three imaginary contributions, including their multiplicities, are
respectively $-11938752$, $-24385536$ and $1608768$. Therefore
$$
\operatorname{Im}\operatorname{Tr}(m_f^9)=-34715520,
\quad
\operatorname{Im}\operatorname{Tr}(m_{\mathcal A_{3,2\mathrm i}}^9)
=-34715520\left(\frac34\right)^9
=-\frac{5338324845}{2048}\ne0.
\tag{A10}
$$
The conjugate parameter gives the conjugate trace. Equal characteristic
polynomials would give equal power sums, so $\chi_{3,2\mathrm i}\ne
\chi_{3,-2\mathrm i}$. Section 4 now proves global seventh-degree
reconstruction from the first three periods and exact minimality $N=3$.

## 6. Retained even-period obstruction and actual conjugacy distinction

For $d\equiv3\pmod4$ and even $n$, set $z_j=\mathrm i(-1)^jx_j$.
The periodic relations at $-B$ become nonzero scalar multiples of those
at $B$, and each kinetic term and each normalized potential term is
unchanged. This is an action-preserving isomorphism of the complete
periodic algebras, giving $\chi_{2k,B}=\chi_{2k,-B}$ for every $k$.
It also has the ordinary-map interpretation
$$
S H_{d,B}S^{-1}=JH_{d,-B},\qquad
S(x,y)=(\mathrm ix,-\mathrm iy),\quad J=-\mathrm{Id},
$$
where $J$ commutes with the odd map. Thus the common-even-iterate symmetry
is not asserted to be a new general conjugacy principle.

The additional first-period coincidence holds precisely at
$$
B=2\frac{1+\eta}{1-\eta},\qquad
\eta^m=1,\quad\eta\ne1,-1,
$$
for distinct nonzero sign pairs. There are $(d-3)/4$ unordered such pairs.
Their nonconjugacy, and that of any two distinct parameters in this binomial
family, follows from the full fixed-point derivative-trace invariant
$$
\mathcal D_d(B)=2d(d-1)-d(d-2)B.
$$
Indeed the fixed algebra is $\mathbb C[x]/(x^d+(B-2)x)$, so the trace of
multiplication by $p'_{d,B}(x)$ gives this expression directly. Its local
decomposition weights the actual derivative trace by the local fixed-point
length. Biholomorphic conjugacy preserves both derivative similarity and
these local lengths. The nonzero slope therefore forces $B=B'$.

## Corrections, limits and actual verification

- The general reconstruction theorem is only for the *binomial* subfamily,
  not arbitrary centered polynomials of the same degree.
- Degrees $d\equiv3\pmod4$ larger than seven still have unresolved odd-period
  separation and full initial-cutoff questions. No all-period collision is claimed.
- General LL finiteness, periodic free bases, trace identities, elementary
  root-of-unity algebra and finite symmetries are prior tools to deduct.
  No novelty or 22–30-page capacity PASS follows from the author proofs.
- An initial exact diagnostic over $\mathbb F_{101}$, with $\mathrm i=10$,
  returned ninth third-period traces $72,89$ at $B=20,81$. A separate
  Gaussian-integer multiplication calculation gave
  $\operatorname{Tr}((8m_{\mathcal A})^9)=
  -634722156601344-349852457041920\mathrm i$ at $B=2\mathrm i$.
  These corroborate (A10); the proof above instead supplies the explicit
  three-reduction counts and multinomial sums. No floating-point sampling,
  fitting, numerical experiment, external computation or stored matrix was used.
- The first probe and its short-stop assessment remain frozen. This new
  degree-uniform argument and exact global $N=3$ result have their own
  author status and still require independent verification before selection.
