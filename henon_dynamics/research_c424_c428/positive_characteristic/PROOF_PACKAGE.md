# Proof package: PC424-L regularity gap

## Claim

For every odd prime $p$, every $c\in k=\overline{\mathbb F}_p$, and
$f_c(x)=x^2+c$, the frozen question asks whether
$$
K_c=\{h\in k[x]:\sum_{a\in O}h(a)=0
\text{ for every ordinary primitive periodic orbit }O\}
=B_c=\{Q\circ f_c-Q:Q\in k[x]\}.
$$
If equality fails, the frozen alternative is a complete uniform
classification of the defect, not one isolated counterexample.

## Status

**NOT CURRENTLY JUSTIFIED.** The original all-parameter question survives
unchanged and is not solved here. The statements proved below are short
structural checks, not a replacement theorem or paper admission.

## Assumptions

- $p$ is odd, $k=\overline{\mathbb F}_p$, and $c\in k$.
- $h$ and all transfer functions called polynomial belong to $k[x]$.
- Orbit sums use each distinct point in a primitive orbit once, even when
  its length is divisible by $p$.
- A finite field $\mathbb F_q\subset k$ is chosen containing $c$ and all
  coefficients of a fixed $h$ whenever finite-field notation is used.

## Notation

Write $\Delta_cQ=Q\circ f_c-Q$ and
$V=k\oplus xk[x^2]$. Elements of $V$ have a constant term and only odd
positive exponents. A set-theoretic transfer $U:k\to k$ is not assumed
polynomial. Its difference is $\Delta_cU=U\circ f_c-U$.

## Proof strategy

Separate finite functional-graph solvability, which is elementary, from
polynomial regularity, which is the missing implication. Use leading
degrees and differentiation to rule out two tempting shortcuts.

## Dependency map

1. Polynomial coboundaries have zero orbit sums by telescoping.
2. The converse for arbitrary functions uses eventual periodicity of every
   algebraic finite-field point; polynomial regularity is not used.
3. Finite-field interpolation uses only distinct points and gives a bound
   growing with field size.
4. The normal form uses the leading term of $\Delta_c x^j$.
5. Frobenius saturation uses $p\ne2$, differentiation, and perfection of $k$.
6. The requested equality still needs every nonzero normal-form class to
   be detected by some primitive periodic orbit.

## Proof

### Step 1. Coboundaries and native lifted periods

If $h=\Delta_cQ$ and $O=\{a,f_c(a),\ldots,f_c^{r-1}(a)\}$ has primitive
length $r$, summing consecutive differences gives $S_h(O)=0$. Therefore
$B_c\subseteq K_c$.

Direct induction on $r$ gives, for the frozen skew map,
$$
T_{c,h}^{\,r}(a,y)=(a,y+S_h(O)).
$$
Any return of $(a,y)$ must have length divisible by $r$, because its
projection has primitive period $r$. Translation by a nonzero element of
$k$ has additive order $p$: the prime field acts faithfully on each
nonzero element. Thus the lifted primitive period is $r$ when $S_h(O)=0$,
and $pr$ otherwise. This calculation is background and does not classify
$K_c/B_c$.

### Step 2. Arbitrary functions and finite fields

Every point of $k$ lies in a finite extension of $\mathbb F_q$ preserved
by $f_c$, so its forward orbit eventually enters a cycle. If $h\in K_c$,
choose one point on each cycle and give $U$ an arbitrary value there.
On a cycle define consecutive values by
$U(f_c(a))=U(a)+h(a)$. The zero sum is exactly the consistency condition
on returning to its first point.

For a point at positive depth in a preperiodic tree, define
$U(a)=U(f_c(a))-h(a)$ after defining the value at its image. Every point
has one forward image, so this defines a function on all of $k$ satisfying
$\Delta_cU=h$. Conversely, any such function telescopes on every cycle.
Thus $K_c$ is precisely the polynomials which are coboundaries in the
space of **all functions** $k\to k$. No degree bound follows.

For each integer $r\geq1$, perform the same construction on the finite
functional graph of $f_c$ on $\mathbb F_{q^r}$. Choose the initial cycle
values in $\mathbb F_{q^r}$. All constructed values remain in that field.
Interpolation at its $q^r$ distinct points gives
$Q_r\in\mathbb F_{q^r}[x]$ with $\deg Q_r<q^r$ and
$$
Q_r(f_c(x))-Q_r(x)\equiv h(x)\pmod{x^{q^r}-x}.
$$
The interpolation assertion follows from the Lagrange basis; its
denominators are differences of distinct field elements and are nonzero.
Conversely, these congruences for every $r$ imply all geometric primitive
orbit sums vanish, since any such orbit is contained in one of the fields.
This is a complete finite-level equivalence, not polynomial regularity.

### Step 3. The precise uniform-degree obstruction

For a fixed nonzero $h$ of degree $D$, suppose there is an integer $M$
such that the congruence in Step 2 has a solution with $\deg Q_r\leq M$
for arbitrarily large $r$. Choose one such $r$ with
$q^r>\max(2M,D)$. Then
$$
R_r=Q_r\circ f_c-Q_r-h
$$
has degree at most $\max(2M,D)$ and vanishes at all $q^r$ field elements.
A nonzero polynomial over a field has at most its degree many distinct
roots, so $R_r=0$. This gives a polynomial transfer.

Conversely, suppose a polynomial transfer exists. Subtract its constant
term so that $Q(0)=0$. Let $Q^{[q]}$ mean raising each coefficient of $Q$
to its $q$th power, leaving its exponents unchanged. Since $f_c$ and $h$
have coefficients in $\mathbb F_q$, $\Delta_c(Q^{[q]}-Q)=0$. A
nonconstant polynomial of degree $m$ has difference of degree $2m$,
so this difference operator has only constants in its kernel.
The normalization at $0$ forces $Q^{[q]}-Q=0$. Thus $Q\in\mathbb F_q[x]$
and it supplies the same fixed degree bound at every finite level.
Step 2 supplies a field-size-dependent bound, not such a uniform $M$.
For $h=0$, the transfer $Q=0$ already suffices.

### Step 4. Polynomial normal form

For every $j\geq1$,
$$
\Delta_c x^j=(x^2+c)^j-x^j
$$
has degree $2j$ and leading coefficient $1$. Given any polynomial,
eliminate its largest positive even exponent using the corresponding
$\Delta_c x^j$, then repeat. Each subtraction creates only smaller
exponents than the eliminated one, so the process terminates and produces
$h=\Delta_cQ+v$ with $v\in V$.

If $\Delta_cQ=v\in V$ and $Q$ is nonconstant of degree $m$, then
$\deg\Delta_cQ=2m$, a positive even integer. A nonzero element of $V$
has either degree $0$ or an odd positive degree. This is impossible.
Hence $Q$ is constant and $v=0$. Thus
$$
k[x]=B_c\oplus V
$$
as vector spaces over $k$. This is not a decomposition of rings.
The requested equality is equivalent to $K_c\cap V=\{0\}$. Detecting all
nonzero odd-support polynomials by primitive orbit sums is not proved.

### Step 5. Frobenius saturation does not create the old ambiguity

For any $h$, the identity $S_{h^p}(O)=S_h(O)^p$ gives
$h^p\in K_c$ if and only if $h\in K_c$.

If $h\in B_c$, then $h^p\in B_c$ by taking the $p$th power of its transfer.
Conversely, suppose $h^p=\Delta_cQ$. Differentiation gives
$$
2x\,Q'(x^2+c)-Q'(x)=0.
$$
If $Q'\ne0$ has degree $m\geq0$, the first term has degree $2m+1$
with nonzero leading coefficient (because $p$ is odd), whereas the
second has degree $m$. They cannot cancel. Therefore $Q'=0$.
In characteristic $p$ this means that all nonconstant exponents of $Q$
are divisible by $p$. Since $k$ is perfect, there is $R\in k[x]$ with
$Q=R^p$, including its constant term. Consequently
$$
h^p=(\Delta_cR)^p.
$$
Injectivity of Frobenius in the field $k(x)$ gives $h=\Delta_cR$.
Thus $h^p\in B_c$ if and only if $h\in B_c$.

This is a short exclusion of a radicial shortcut; it is not a solution
of the quotient problem.

### Step 6. A small boundary check is not an all-degree theorem

If $h=ax+b$ vanishes in orbit sum on all fixed points and $c\ne1/4$,
the two distinct roots of $x^2-x+c$ force $a=b=0$.
If $c=1/4$, the fixed-point condition gives
$h=a(x-1/2)$. In this case
$$
f_c^2(x)-x=(x^2-x+c)(x^2+x+c+1).
$$
The second factor has discriminant $-4$, nonzero for odd $p$, and shares
no root with the first: their difference is $2x+1$, whose root $-1/2$
does not solve $x^2-x+1/4=0$. Its two roots therefore form one primitive
two-cycle with point sum $-1$. The sum of $h$ along that cycle is $-2a$,
so $a=0$. Hence $K_c$ contains no nonzero polynomial of degree at most
$1$, for every allowed $p,c$.

## Corrections or missing assumptions

No quantified conclusion is weakened to obtain an admission. The missing
lemma is a uniform polynomial-regularity statement for the transfer in
Step 2, or an equivalent all-degree orbit-detection statement in Step 4.
Finite interpolation, Step 5, and Step 6 do not supply it.

## Open risks

- The frozen equality may be false; no all-degree counterexample or
  classification of a defect is established.
- Characteristic-$p$ cancellation on long orbits must be controlled
  using primitive orbit sums, not sums of repeated cycles.
- The classical real hyperbolic Livšic theorem does not provide polynomial
  regularity over $k$; its hypotheses and conclusion are different.
- These elementary checks have not received a nonauthor proof review.
  They are initial scouting evidence, not a formal evaluation.
