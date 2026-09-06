# First-return multiplicities under Frobenius-degree lifting

2026-09-06. Internal proof package. No paper number or admission is claimed.
All files in the preceding round remain sealed and unchanged.

## Claim and status

The original target was:

> For every odd prime $p$, every nonzero point of least period $L$ under
> $f(x)=x+x^{p+1}$ has $\operatorname{ord}_a(f^L-x)=p$.

**Original status: NOT CURRENTLY JUSTIFIED; in fact FALSE.** Section 1 gives
an exact counterexample with $p=3$, least period $12$, and multiplicity
$12$, using only arithmetic of degree at most $52$.

The replacement result proved here is a different, explicitly scoped
statement:

> For $f_q=xH(x)^q$, $q$ a positive power of the characteristic, all
> nonzero first-return coefficients of degree strictly below $q^2$ are
> determined by a finite product of orbit polynomials. Consequently, for a
> fixed finite field, a fixed polynomial $H$, and a fixed residue class of
> the Frobenius exponent, this product determines the first-return
> multiplicity of **every nonzero periodic point in that finite field**
> for all sufficiently large exponents. In odd characteristic, established
> local ramification theorems then determine its multiplicity at every
> later return time.

**Replacement status: PROVABLE AS STATED.** This is not a formula for the
ordinary periodic-point count over the algebraic closure. It must not be
advertised as solving the original ordinary-count problem.

## Assumptions and notation

- Composition is the clock: $f^n$ means the $n$-fold compositional iterate.
  Frobenius exponents index a family of maps, not a replacement time clock.
- $k$ is a field of characteristic $p>0$. For the local theorem it is
  enough that the specified cycle lies in $k$; one may pass to its algebraic
  closure without changing the computation.
- $q=p^s$, where $s\geq1$, and $H\in k[x]$ is nonconstant, with degree
  $e\geq1$. Set $f_q(x)=xH(x)^q$.
- $C=(a_0,\ldots,a_{L-1})$ is a nonzero cycle of least period $L$,
  indexed so that $f_q(a_i)=a_{i+1}$ modulo $L$. All $a_i$ are distinct,
  and every $H(a_i)$ is nonzero.
- For $P(T)=\sum b_jT^j$, write
  $P^{[q]}(T)=\sum b_j^qT^j$. This is a **coefficient** Frobenius twist;
  it is not the polynomial power $P(T)^q=P^{[q]}(T^q)$.
- $\operatorname{ord}_T(P-1)$ denotes the least positive exponent with
  nonzero coefficient in $P-1$. A congruence modulo $v^M$ determines the
  coefficients of degrees strictly less than $M$, not the degree-$M$
  coefficient.
- In the finite-field theorem $K=\mathbb F_{p^d}$, $P=|K|=p^d$, and
  $0\leq r<d$. The lifted exponents are $q_j=p^{r+jd}$, with
  $r+jd\geq1$. Here $P$ and $q_j$ are deliberately different symbols.

## Proof strategy and dependency map

1. The counterexample uses a displayed finite orbit, an irreducibility
   certificate, and an $h$-adic polynomial congruence. It needs no
   asymptotic theorem and no extrapolation from a census.
2. The local transfer lemma follows directly from multiplicative local
   coordinates and the characteristic-$p$ Frobenius identity. It gives a
   precise truncation, including its first omitted degree.
3. Finite-field exponent lifting uses $z^{p^d}=z$ for $z\in K$, then the
   degree bound $\deg B_C=eL$. This changes neither the finite graph nor
   the compositional clock.
4. The all-return multiplicity corollary additionally uses the explicitly
   attributed Nordqvist--Rivera-Letelier and Nordqvist local theorems.
   Those theorems do not supply the orbit-product transfer lemma.
5. A two-cycle calculation proves that the truncation exponent $q^2$ is
   sharp. The degree-$3^{4j+1}+1$ exceptional family is then an application
   of the general theorem, with the small exponent handled separately.

## 1. A counterexample for the original prime-exponent family

Work over $\mathbb F_3$ and put

$$
 f(X)=X+X^4,\qquad h(X)=X^4+2X^3+2.
$$

### 1.1. The field and the least period

The values of $h$ at $0,1,2$ are $2,2,1$. The three monic irreducible
quadratics over $\mathbb F_3$ are
$X^2+1$, $X^2+X+2$, and $X^2+2X+2$; the remainders of $h$ modulo these
polynomials are respectively $X$, $X+2$, and $X$. Thus $h$ has neither a
linear factor nor an irreducible quadratic factor. A reducible quartic
must have one of these factors, so $h$ is irreducible.

Let $a$ be the image of $X$ in
$K=\mathbb F_3[X]/(h)=\mathbb F_{81}$. Reduction using
$a^4=a^3+1$ gives the following orbit:

| $j$ | $f^j(a)$ |
|---:|---|
| $0$ | $a$ |
| $1$ | $a^3+a+1$ |
| $2$ | $2a^2+a$ |
| $3$ | $a^3+2a^2+1$ |
| $4$ | $a^3+2a^2+a+2$ |
| $5$ | $2a^3+a$ |
| $6$ | $a^3+a^2+2a$ |
| $7$ | $2a^3+2a+2$ |
| $8$ | $a^3+2a^2+2a+1$ |
| $9$ | $a^3$ |
| $10$ | $2a^3+a^2+2a+1$ |
| $11$ | $2a^2+2a+2$ |
| $12$ | $a$ |

Each next row is obtained by adding the fourth power of the preceding
row. The twelve degree-less-than-four representatives in rows $0$ to
$11$ are distinct. Uniqueness of representatives modulo $h$ proves that
$a$ has least period exactly $12$, not just a period dividing $12$.
None of these points is $0$ or $-1$.

### 1.2. A bounded $h$-adic certificate

Set $Q(X)=X^3+2X^2+X+1$. Exact polynomial arithmetic gives

$$
 f^{12}(X)-X\equiv h(X)^{12}Q(X)\pmod {h(X)^{13}}. \tag{1}
$$

Here is a complete finite procedure for verifying the displayed algebraic
identity without constructing the degree-$4^{12}$ iterate. All its
remainders have degree less than $52$:

```text
R = F_3[X]
h = X^4 + 2X^3 + 2
M = h^13
V = X
repeat exactly 12 times:
    V = remainder(V + V^4, M)
result: V - X = h^12 (X^3 + 2X^2 + X + 1)
```

Polynomial reduction commutes with polynomial substitution, so induction
shows that the value after the $j$th step is $f^j(X)$ modulo $M$. The last
identity is therefore the certificate (1), not a guessed recurrence.
The executable verifier is `verify_h_adic.py`. A separate translated-jet
verifier, `verify_period12.py`, computes the same local multiplicity by
twelve local compositions in $K[u]/(u^{19})$.

Since $Q$ is nonzero of degree less than $\deg h$, it is not divisible by
$h$. Thus (1) proves that the $h$-adic valuation of $f^{12}-X$ is exactly
$12$. Also $h'(a)=a^3\ne0$. Expanding at $a$ and reducing the leading
coefficient in $K$ gives

$$
 Q(a)a^{36}=a^2+a\ne0,
$$

and hence

$$
 f^{12}(a+u)-a-u=(a^2+a)u^{12}+O(u^{13}). \tag{2}
$$

The first-return multiplicity is $12=4p$, not $p=3$. This refutes the
original universal assertion. The previously tested periods at most $9$
could not have detected this period-$12$ cycle.

### 1.3. Why this also refutes the proposed ordinary count

Let $w(b)=\operatorname{ord}_b(f^{L(b)}-x)/3$ for nonzero periodic points
of this particular $f$. The first-return multiplicity is constant along
a cycle: $f$ is locally invertible there, because
$f'(b)=f(b)/b\ne0$, and the return germs are conjugate by the local maps
along the cycle. Thus all twelve points above have $w=4$.

Every nonzero periodic point has $w\geq1$. Consequently the first-return
weighted count $W_n$ and the ordinary nonzero count $N_n^\times$ satisfy

$$
 W_n-N_n^\times\geq36\qquad\text{whenever }12\mid n. \tag{3}
$$

Using the already established weighted formula at $n=12$ yields
$W_{12}=5\,592\,234$ and therefore
$N_{12}^\times\leq5\,592\,198$. Equality is **not** asserted: the
calculation has not classified all other geometric period-$12$ cycles.
Formula (3) is an infinite set of failed counting times caused by this
same cycle; it is not a proof of infinitely many distinct exceptional
primitive cycles for $x+x^4$.

## 2. The local orbit-product transfer theorem

Define, for each point of a nonzero cycle,

$$
 A_i(T)=\frac{H(a_i(1+T))}{H(a_i)},\qquad
 B_C(T)=\prod_{i=0}^{L-1} A_i(T). \tag{4}
$$

Every $A_i$ has degree $e$ and constant term $1$. Therefore $B_C$ has
degree exactly $eL$, constant term $1$, and

$$
 1\leq\nu_C:=\operatorname{ord}_T(B_C-1)\leq eL. \tag{5}
$$

In particular $B_C\ne1$ as a polynomial. The coefficients and $\nu_C$
are unchanged by cyclically choosing another starting point.

### Theorem 1. Local transfer, with exact precision

Let

$$
 G_C(v)=\frac{f_q^L(a_0(1+v))}{a_0}-1.
$$

Then

$$
 1+G_C(v)\equiv(1+v)B_C^{[q]}(v^q)\pmod {v^{q^2}}. \tag{6}
$$

If $\nu_C<q$, and $b_C=[T^{\nu_C}]B_C(T)\ne0$, then

$$
 \operatorname{ord}_{a_0}(f_q^L-x)=q\nu_C, \tag{7}
$$

with leading coefficient in the translated coordinate $u=x-a_0$ equal to

$$
 f_q^L(a_0+u)-a_0-u
   =a_0^{1-q\nu_C}b_C^q\,u^{q\nu_C}
        +O(u^{q\nu_C+1}). \tag{8}
$$

If $\nu_C\geq q$, the exact consequence of (6) is only
$\operatorname{ord}_{a_0}(f_q^L-x)\geq q^2$.

**Proof.** Use multiplicative coordinates centered at successive points:
$x=a_i(1+v)$. As $a_{i+1}=a_iH(a_i)^q$, the one-step normalized map is

$$
 G_i(v)=\frac{f_q(a_i(1+v))}{a_{i+1}}-1
       =(1+v)A_i(v)^q-1
       =(1+v)A_i^{[q]}(v^q)-1. \tag{9}
$$

This shows $G_i(v)=v+O(v^q)$ and $G_i'(0)=1$. Any finite composition
$V(v)$ of these maps is also $v+O(v^q)$: if two series have this property,
substitution and addition preserve it. Because $q$ is a power of the
characteristic,

$$
 V(v)^q=v^q+O(v^{q^2}). \tag{10}
$$

For a polynomial $A$, the difference $A(X)-A(Y)$ is divisible by $X-Y$.
Applying this with $X=V(v)^q$, $Y=v^q$, gives

$$
 A_i^{[q]}(V(v)^q)
       \equiv A_i^{[q]}(v^q)\pmod {v^{q^2}}.
$$

Thus (9) gives

$$
 1+G_i(V(v))\equiv(1+V(v))A_i^{[q]}(v^q)
                       \pmod {v^{q^2}}.
$$

Induction on the number of steps multiplies the $A_i^{[q]}$ factors and
proves (6). There is no restriction on $L$ in this congruence.

If $\nu_C<q$, the right side of (6), after subtracting $1+v$, has first
nonzero term $b_C^qv^{q\nu_C}$, of degree less than $q^2$. It cannot be
changed by the omitted terms. This proves (7). Substituting $v=u/a_0$
and multiplying the return displacement by $a_0$ proves (8). If
$\nu_C\geq q$, all coefficients visible in (6) vanish instead; it gives
only the stated lower bound. ∎

### A first-coefficient criterion

Differentiating (4) at $T=0$ gives

$$
 [T]B_C(T)=\sum_{i=0}^{L-1}\frac{a_iH'(a_i)}{H(a_i)}. \tag{11}
$$

Therefore the first-return multiplicity is exactly $q$ if and only if
this sum is nonzero. The converse follows as well from (6), since
$q<q^2$: vanishing of this coefficient rules out a degree-$q$ return
term. For $H=1+x$, (11) is the orbit-sum criterion used to locate the
counterexample. It is an exact criterion, not an assertion that the sum
is always nonzero.

## 3. Uniform lifting of every cycle in a fixed finite field

Fix $K=\mathbb F_{p^d}$, nonconstant $H\in K[x]$, and a residue
$0\leq r<d$. Define the finite set map

$$
 g_r:K\longrightarrow K,\qquad g_r(a)=aH(a)^{p^r}. \tag{12}
$$

The exponent $p^r=1$ is allowed when $r=0$ in this finite set map. The
lifted polynomial maps still have $q_j=p^{r+jd}\geq p$.

### Theorem 2. Finite-field first-return profile

For every allowed $j$,
$f_{q_j}|_K=g_r$. Hence every nonzero cycle $C$ of $g_r$ is a cycle of
the same least period $L_C$ for every $f_{q_j}$. Form $B_C$, $\nu_C$,
and $b_C$ by (4)--(5), using this fixed cycle. These polynomials and
integers are independent of $j$.

Whenever $q_j>eL_C$,

$$
 \operatorname{ord}_{a_0}(f_{q_j}^{L_C}-x)=q_j\nu_C. \tag{13}
$$

In particular the single sufficient bound

$$
 q_j>e(|K|-1) \tag{14}
$$

determines the first-return multiplicities of **all** nonzero periodic
points in $K$ at once. Their multiplicities divided by $q_j$ stabilize
to the finite profile $\{(C,L_C,\nu_C)\}$.

The leading coefficient in the translated coordinate at $a_0$ also
stabilizes. It is

$$
 a_0^{1-p^r\nu_C}b_C^{p^r}, \tag{15}
$$

independent of $j$ once (13) applies.

**Proof.** Each $z\in K$ satisfies $z^{p^d}=z$, so
$H(a)^{q_j}=H(a)^{p^r}$ and $f_{q_j}(a)=g_r(a)$. Equality of the set maps
preserves least periods, not just membership in a fixed-point set.

The construction of $A_i$ uses only $H$ and the finite orbit, so $B_C$ is
fixed. Its coefficient twist satisfies
$B_C^{[q_j]}=B_C^{[p^r]}$. Bound (5) and the inequality $q_j>eL_C$ allow
Theorem 1 to be applied. Nonzero cycles contain at most $|K|-1$ points,
giving (14). Finally $a_0^{q_j}=a_0^{p^r}$ and
$b_C^{q_j}=b_C^{p^r}$ in $K$; substituting these identities in (8) gives
(15). ∎

### Algorithmic content and its exact boundary

One can evaluate the finite map (12) at every element of $K$, decompose
its functional graph into cycles, multiply the degree-$e$ polynomials
(4) along each nonzero cycle, and read the first nonconstant coefficient
of every product. This is a terminating exact algorithm, with no
factorization of a degree-$(q_je+1)^{L_C}$ iterate. Its orbit calculations
and polynomial products are independent of the unbounded index $j$.

The elementary graph algorithm is not itself a claimed new algorithm.
The transfer theorem is the justification for reusing its finite output
as the complete local first-return profile of an infinite family of
different-degree polynomial maps.

The order of quantifiers is essential:

$$
 \text{for every fixed }(K,H,r),\quad
 \text{for all sufficiently large }j,\quad
 \text{for every periodic }a\in K.
$$

There is no uniform threshold here for all finite extensions of $K$.
Consequently this is not a full classification of the geometric periodic
points of one fixed $f_{q_j}$ over $\overline K$.

## 4. All later return times: a classical-input corollary

Assume in this section that $p$ is odd. For any $f=x\widetilde H(x)^p$
and any nonzero least-period point $a$, write its first-return germ in the
translated coordinate as

$$
 g(u)-u=(a+u)T(u)^p,\qquad
 T(u)=c u^m+O(u^{m+1}),\quad c\ne0. \tag{16}
$$

This form follows by writing the iterate as
$f^L(x)=x\prod_{i=0}^{L-1}\widetilde H(f^i(x))^p$ and subtracting $x$.
The product at $a$ equals $1$, since its $p$th power equals $1$ in a
field of characteristic $p$.

Thus the first-return multiplicity is $pm$. Put $i_0=pm-1$ and
$\ell=p-1$. The residue calculation is

$$
 \operatorname{Res}_{u=0}
    \frac{u^{(m-1)p}}{u-g(u)}=-(ac)^{-p}\ne0. \tag{17}
$$

Indeed the Laurent series equals
$-c^{-p}u^{-p}(a+u)^{-1}(1+O(u))^{-p}$. The last factor has no
nonconstant term below degree $p$, so the residue is determined by the
coefficient $a^{-p}$ of $u^{p-1}$ in $(a+u)^{-1}$.

For $m=1$, [Nordqvist--Rivera-Letelier, Theorem 2](https://arxiv.org/pdf/1904.04494)
applies with initial lower ramification number $p-1$; its iterative
residue is $(ac)^{-p}\ne0$. It gives $i_t=p^{t+1}-1$.
For $m\geq2$, [Nordqvist, Definition 2.2 and Theorem A](https://arxiv.org/pdf/1909.10782)
apply with $i_0=pm-1>p$ and second residue (17); they give
$i_t=mp^{t+1}-1$.

Both cases show that the multiplicity after a further $p^t$ returns is
$pm\,p^t$. If an additional iteration count $b$ is prime to $p$, then
for $h(u)=u+A u^M+O(u^{M+1})$ one obtains by induction
$h^b(u)=u+bA u^M+O(u^{M+1})$. This preserves the multiplicity.

Apply this with $\widetilde H=H^{q_j/p}$ to Theorem 2. For every nonzero
cycle $C$, every $q_j$ satisfying (14), and every positive integer $n$
divisible by $L_C$,

$$
 \operatorname{ord}_{a_0}(f_{q_j}^n-x)
       =q_j\nu_C\,p^{v_p(n/L_C)}. \tag{18}
$$

This is a corollary of established local ramification theory after the
new first-return calculation; it is not a newly proved general
ramification theorem. The powers in (18) concern repeated returns to the
same points. They do not construct new primitive cycles.

If additionally $H(0)=1$ and $m_0=\operatorname{ord}_0(H-1)$, then
$i_0(f_q)=qm_0$ is divisible by $p$. Sen's classical identity, as stated
in the two cited sources, gives

$$
 \operatorname{ord}_0(f_q^n-x)=1+qm_0p^{v_p(n)}. \tag{19}
$$

The origin is separate: it cannot be put into the nonzero coordinates
or assigned the profile (13). Combining (18)--(19) gives, if desired, the
entire local-intersection-length sum supported at $K$-rational fixed
points:

$$
 M_{q,K}(n)=1+qm_0p^{v_p(n)}
     +q\sum_{C:\,L_C\mid n}
           L_C\nu_Cp^{v_p(n/L_C)}. \tag{20}
$$

This observable includes multiplicity. The ordinary count on the finite
set $K$ is instead the elementary expression
$1+\sum_{C:L_C\mid n}L_C$, independent of $q_j$ in the fixed residue
class. Neither expression is the ordinary count on $\overline K$.

## 5. The precision $q^2$ is sharp

For $H=1+x$, a normalized local step has the form

$$
 G_c(v)=(1+v)(1+c v^q)-1,\qquad
 c=\frac{a^q}{1+a^q}\ne0. \tag{21}
$$

For two nonzero coefficients $c,d$, direct Frobenius expansion gives

$$
 G_d(G_c(v))-
       \big((1+v)(1+c v^q)(1+d v^q)-1\big)
       =d c^q v^{q^2}+O(v^{q^2+1}). \tag{22}
$$

To verify the coefficient, use
$G_c(v)^q=v^q+c^qv^{q^2}+c^qv^{q^2+q}$ and insert this in
$(1+G_c(v))(1+dG_c(v)^q)-1$. The coefficient of the first difference
term is $dc^q$, which is nonzero. Thus the congruence in Theorem 1
cannot in general be strengthened to one modulo $v^{q^2+1}$.

This occurs for genuine least-period-two cycles, not just unrelated
formal maps. If $q$ is odd, choose a root $y$ of
$y^{q+1}=-1$ in an algebraic closure and put $a=y-1$. Then $y$ is
neither $0$ nor $1$, and

$$
 f_q(a)=-\frac{a}{y},\qquad
 1+f_q(a)=\frac1y,\qquad
 f_q^2(a)=a.
$$

Since $f_q(x)-x=x^{q+1}$ has no nonzero root, the period is exactly
two. Both local coefficients in (21) are nonzero, so (22) applies to
this actual return map. Theorem 1 nevertheless determines its first
nonzero term when $\nu_C<q$: sharpness concerns the precision of the
full jet, not the validity of the leading-order result.

## 6. An infinite exceptional family of distinct degrees

Return to the cycle $C\subset\mathbb F_{81}$ in Section 1. Its ordinary
cycle polynomial is

$$
 \begin{aligned}
 P_C(X)&=\prod_{a_i\in C}(X-a_i)\\
 &= (X^4+2X^3+2)(X^4+2X^2+2)(X^4+X^2+X+1)\\
 &=X^{12}+2X^{11}+X^9+2X^6+X^4
      +2X^3+2X^2+X+1.
 \end{aligned} \tag{23}
$$

One may verify the middle identity using the orbit table and the fact
that Frobenius $a\mapsto a^3$ shifts its index by $9$. The three
quartics correspond respectively to the index classes $0,1,2$ modulo
$3$. They are disjoint and together exhaust this one twelve-cycle.

Multiplying $a_{i+1}/a_i=(1+a_i)^3$ gives
$\prod_i(1+a_i)=1$. Hence for $H=1+x$ the polynomial (4) is

$$
 \begin{aligned}
 B_C(T)&=\prod_i\left(1+\frac{a_i}{1+a_i}T\right)\\
       &=(1+T)^{12}P_C\left(-\frac1{1+T}\right)\\
       &=1+T^4+2T^5+2T^7+T^8+2T^{11}+T^{12}.
 \end{aligned} \tag{24}
$$

This calculation is checked in `verify_h_adic.py`. In particular
$\nu_C=4$ and $b_C=1$.

### Theorem 3. Infinite-degree family with excess first-return weight

For every integer $j\geq0$, let

$$
 q_j=3^{4j+1},\qquad F_j(x)=x+x^{q_j+1}.
$$

The twelve points of $C$ form a cycle of least period $12$ for $F_j$,
and

$$
 \operatorname{ord}_a(F_j^{12}-x)=4q_j. \tag{25}
$$

Thus the first-return multiplicity divided by the forced Frobenius
power $q_j$ equals $4$, rather than $1$, for every member of this
infinite family.

**Proof.** Frobenius on $\mathbb F_{81}$ has fourth power the identity,
so $F_j$ restricts to the same set map as $F_0=f$. The least period is
therefore always $12$. For $j\geq1$, $q_j\geq243>12$, and Theorem 2
with (24) gives (25). For $j=0$, $q_0=3$ is below the theorem's
threshold; the independent calculation (1)--(2), not an extrapolation
of (6), proves (25). ∎

The distinction at the threshold is visible in the coefficient. For
$j\geq1$, in the coordinate $x=a(1+v)$ the leading return term is
$v^{4q_j}$. At $j=0$, (2) gives instead $2v^{12}$, since
$(a^2+a)a^{11}=2$. Thus the formal product (24) cannot simply be used
past the precision stated in Theorem 1. In the translated coordinate,
the leading coefficient is $2a^2+2a$ for $j\geq1$ and $a^2+a$ for
$j=0$.

By (18), this same cycle has later-return multiplicity
$4q_j3^{v_3(n/12)}$ for every $12\mid n$. This all-time statement is
about a fixed primitive cycle for each family member.

### Distinct degrees and the non-dynamically-affine boundary

The degrees $q_j+1$ are distinct, so the maps are not merely coordinate
conjugates of one polynomial. They are separable, of degree prime to
$3$, with one finite critical point $-1$ of local degree $q_j$, and
infinity of local degree $q_j+1$. They are not dynamically affine in
the usual finite-group-quotient classification:

1. Additive and subadditive maps have degree a power of the characteristic,
   excluding degree $q_j+1$.
2. Power maps of that degree have both critical local degrees equal to
   $q_j+1$, excluding the local degree $q_j$ at $-1$.
3. A separable Chebyshev map of degree $q_j+1$ has $q_j$ distinct finite
   critical points in odd characteristic. This follows from its defining
   semiconjugacy $D_{q_j+1}(z+z^{-1})=z^{q_j+1}+z^{-q_j-1}$:
   the $2q_j$ roots of $z^{2(q_j+1)}=1$ other than $\pm1$, paired by
   inversion, give distinct finite critical points. Degree of the
   derivative shows these exhaust the finite critical points.
4. A separable Lattès map of degree greater than one cannot have a totally
   invariant point. If $\pi:E\to\mathbb P^1$ is its finite quotient
   and $\psi$ its affine elliptic lift, the lift here is separable because
   its degree $q_j+1$ is prime to $3$. For a totally invariant point $b$,
   the finite nonempty set $S=\pi^{-1}(b)$ would satisfy
   $\psi^{-n}(S)\subseteq S$, whereas it has $(q_j+1)^n|S|$ geometric
   points. This is impossible. Our polynomial has totally invariant
   infinity.

The classification itself is an input from
[Bridy, Sections 2--5](https://arxiv.org/pdf/1306.5267), not a new
classification theorem. Non-dynamically-affine status does not by itself
settle the ordinary Artin--Mazur zeta function.

## Corrections, scientific status, and open risks

- The original universal claim is false, and the original ordinary
  algebraic-closure count is not obtained here. Its precise remaining
  obstacle is classification of first-return multiplicities for all
  primitive cycles of one fixed map, including periods beyond the
  transfer threshold.
- The replacement theorem is a full-quantifier result for a different
  object: the local ramification profiles of Frobenius-degree lifts over
  a fixed finite field. It has a general $H$ theorem, an explicit
  threshold, a sharp jet precision, exact leading coefficients, and an
  infinite non-conjugate exceptional family.
- The main transfer argument is short and elementary. The all-return
  tower formula uses existing ramification theory. These are genuine
  limitations in assessing whether the result merits a standalone
  research paper; length of a write-up is not evidence of substance.
- No source checked in this bounded audit states the exact finite-field
  transfer/profile theorem, but this is not a global priority certificate.
  The main novelty risk is prior ownership as a sparse Nottingham-group
  composition calculation or a routine corollary of such a calculation.
- The finite-set ordinary count is elementary once its graph is known.
  It is not offered as a second theorem of independent scientific weight.
  No new weighted zeta paper is proposed.
- There is no demonstrated infinite sequence of exceptional primitive
  periods for the single polynomial $x+x^4$. The infinite family in
  Theorem 3 varies the polynomial degree, with one fixed primitive period.
- No C-number, Route-A evaluation, arithmetic local Euler factor,
  root number, functional equation, or target-zero correspondence is
  asserted. `NO_BAD_EULER_OR_ROOT_NUMBER` remains in force.

## Exact verification record and disclosure

The new targeted discovery search examined only $\mathbb F_9$,
$\mathbb F_{27}$, and $\mathbb F_{81}$ for $x+x^4$ and stopped at its
first counterexample. No large-degree global iterate or old census was
run. The counterexample was then checked by two author-side methods:
translated local jets and reduction modulo $h^{13}$. The coordinator
reported an additional independent standard-library polynomial check of
the same congruence and least period; its separately owned file is
outside this lane.

Two implementation-only failures during verifier preparation were fixed
before the passing outputs: the finite-field class's truth-value test was
replaced by an explicit comparison with zero, and a polynomial evaluation
call was changed from an unsupported keyword argument to a positional
argument. These were not failed mathematical identities. The final
verifiers assert exact equalities and print their results to stdout.

The universal transfer theorems are proved algebraically above; the
bounded checks do not replace their proofs. This package was developed
with AI assistance and internal team discussion. No external model
upload or human peer-review status is claimed. Source ownership and the
actual primary-body reading scope are recorded in `SOURCE_AUDIT.md`.
