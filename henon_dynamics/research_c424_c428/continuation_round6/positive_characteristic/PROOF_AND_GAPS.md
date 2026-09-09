# Algebraic additive transfers descend for tame-degree polynomial bases

2026-09-09 UTC. Current-team author hand proof; mathematical programs:
**0**. This is a complete auxiliary theorem for the one resumed
[PC424-L contract](FROZEN_QUESTION.md), not a new independent paper.

## Claim

**Auxiliary algebraic-descent theorem.** Let $k$ be an algebraically
closed field of characteristic $p>0$. Let $f\in k[x]$ have degree
$d\ge2$ with $\gcd(d,p)=1$, and put $K=k(x)$. Let $\sigma$ fix $k$
pointwise and send $x$ to $f(x)$. Suppose this field embedding extends
to a field containing an element $u$ algebraic over $K$, and suppose

$$\sigma(u)-u=h(x),\qquad h\in k[x]. \tag{1}$$

Then $u\in k[x]$. Consequently an algebraic additive transfer exists
if and only if a polynomial one exists. The polynomial transfer is
unique up to an additive constant in $k$.

Here an algebraic transfer includes a compatible embedding on the
extension field. A polynomial equation satisfied by unrelated values
at different base points does not constitute such a transfer.

**Original PC424-L statement.** For $f=x^2+c$, every odd $p$ and every
$c\in\overline{\mathbb F}_p$, determine whether vanishing of all
ordinary primitive orbit sums is equivalent to polynomial
coboundariness, or classify the full defect.

## Status

- Auxiliary algebraic-descent theorem: **PROVABLE AS STATED**.
- Original ordinary-cycle question: **NOT CURRENTLY JUSTIFIED /
  UNCLOSED**. Its original quantifiers survive unchanged.
- The precise missing bridge is written in Section 9; the auxiliary
  theorem does not assume that bridge under another name.

## Assumptions and notation

Write $\Delta Q=Q\circ f-Q$ for $Q\in k[x]$ or $k(x)$, and let

$$
B=\Delta k[x],\qquad
V_d=k\oplus\bigoplus_{\substack{j\ge1\\d\nmid j}}kx^j.
\tag{2}
$$

The direct sums refer to vector spaces: each polynomial has finite
support. They are not decompositions as rings. If $P(T)\in K[T]$,
then $P^\sigma$ means application of $\sigma$ to its coefficients,
leaving $T$ unchanged. Finite extensions below are allowed to be
inseparable unless explicitly called separable.

## Proof strategy and dependency map

1. The degree-$d$ base embedding forces every invariant of every
   positive power of $\sigma$ in a finite stable extension to be a
   constant.
2. The minimal polynomial of a separable transfer has an exact
   translation identity. Its Taylor coefficients at that transfer
   are invariant constants, forcing a finite additive translation
   Galois group.
3. The polynomial of a finite additive subgroup is a $p$-polynomial.
   Hence a separable algebraic transfer supplies
   $A(h)=\Delta b$ for a nonzero additive polynomial $A$ and rational
   $b$.
4. A polynomial coboundary has no rational finite-pole transfer.
5. The normal space (2) is stable under every additive polynomial
   when $p\nmid d$. Degree comparison eliminates all nonconstant
   normal defects; periodic invariants eliminate constant ones.
6. Raising to an appropriate $p$-power reduces any inseparable
   transfer to the separable case. The same normal-space argument
   descends back, and invariance makes the original transfer itself
   polynomial.

The finite-field interpolation, quadratic normal form and rational
pole principle were earlier inputs to this research line. The new
global part is the finite-extension translation argument and its
complete descent. No previous root-multiplicity estimate is assumed.

## Proof

### 1. Degree and invariant constants in a finite stable extension

Put $E=K(u)$. Equation (1) implies $\sigma(E)\subseteq E$. If
$m=[E:K]$, then

$$
[E:\sigma(K)]=md
=[E:\sigma(E)]\,[\sigma(E):\sigma(K)]
=[E:\sigma(E)]m.
$$

The first equality uses $[k(x):k(f(x))]=d$, valid also for inseparable
polynomials; the last uses that $\sigma$ is an isomorphism from $E$
onto its image. Thus

$$[E:\sigma(E)]=d,\qquad [E:\sigma^r(E)]=d^r\quad(r\ge1). \tag{3}$$

We claim $E^{\sigma^r}=k$ for every $r\ge1$. Let $w\in E$ satisfy
$\sigma^r(w)=w$. If $w\notin k$, algebraic closedness of $k$ implies
that $w$ is transcendental over $k$. The one-variable function field
$E$ is then a finite extension of $k(w)$. Since $\sigma^r$ fixes
$k(w)$, it identifies this finite extension with
$\sigma^r(E)/k(w)$, of the same degree. Applying the tower formula
to $k(w)\subseteq\sigma^r(E)\subseteq E$ now gives

$$[E:k(w)]=d^r[E:k(w)],$$

contradicting $d^r>1$. This proves the claim. The same proof applies
to any finite $\sigma$-stable extension of $K$.

### 2. The minimal-polynomial translation identity

Assume first that $u$ is separable over $K$. Let $P(T)$ be its monic
minimal polynomial, of degree $m$. Applying $\sigma$ to $P(u)=0$
gives $P^\sigma(u+h)=0$. Both $P(T)$ and $P^\sigma(T+h)$ are monic
of degree $m$ in $K[T]$. The former divides the latter by minimality,
so

$$P^\sigma(T+h)=P(T). \tag{4}$$

No claim that $\sigma$ is surjective on $K$ is used here. In
particular, (4) does not rely on a Hilbert-90 theorem for a finite
Galois action on the base.

Expand in an independent variable $Z$:

$$P(u+Z)=\sum_{j=0}^{m}b_jZ^j\in E[Z].$$

Applying $\sigma$ to its coefficients, fixing $Z$, and using (4),
gives

$$
\sum_j\sigma(b_j)Z^j
=P^\sigma(u+h+Z)=P(u+Z)=\sum_jb_jZ^j.
$$

Section 1 therefore gives $b_j\in k$ for every $j$. Consequently
$P(u+Z)\in k[Z]$. This argument uses ordinary polynomial
coefficients, equivalently Hasse derivatives, so it is valid even
when an ordinary derivative coefficient such as $m$ vanishes in
characteristic $p$.

### 3. Finite additive translation group and its polynomial

The polynomial $P(u+Z)$ is separable, monic and has $0$ as a root.
As $k$ is algebraically closed, all its distinct roots form a finite
set $W\subset k$. Every root of $P$ is of the form $u+w$ for
$w\in W$ and already lies in $E$. Thus $E/K$ is normal and
separable, hence Galois.

For $g\in\operatorname{Gal}(E/K)$ there is a unique $w_g\in W$
with $g(u)=u+w_g$. Since $g$ fixes $k$, composition gives
$w_{g_1g_2}=w_{g_1}+w_{g_2}$. The image is all of $W$ because the
Galois group acts transitively on the roots of the irreducible $P$.
Thus $W$ is a finite additive subgroup of $k$, including the case
$W=\{0\}$ when $m=1$.

Set

$$A(T)=\prod_{w\in W}(T-w).$$

We justify the classical additive-polynomial fact needed here.
Choose a basis of $W$ as a finite-dimensional $\mathbb F_p$-space.
For the zero-dimensional group its polynomial is $T$. If the
polynomial $A_U$ of a subspace $U$ is additive and
$W=U\oplus\mathbb F_pa$, then $A_U(a)\ne0$ and

$$
\begin{aligned}
A_W(T)
&=\prod_{j\in\mathbb F_p}A_U(T-ja)\\
&=\prod_{j\in\mathbb F_p}\bigl(A_U(T)-jA_U(a)\bigr)\\
&=A_U(T)^p-A_U(a)^{p-1}A_U(T).
\end{aligned}
$$

Induction proves that

$$A(T)=\sum_{i=0}^{s}a_iT^{p^i},\qquad a_s=1, \tag{5}$$

and in particular $A(T-S)=A(T)-A(S)$. Comparing the roots gives

$$P(T)=A(T-u)=A(T)-A(u).$$

Its constant coefficient shows $b:=A(u)\in K$. Because the
coefficients of $A$ lie in $k$ and are fixed by $\sigma$, (1) yields

$$A(h)=A(\sigma u)-A(u)=\sigma(b)-b=\Delta b. \tag{6}$$

This proves the required additive-polynomial relation, with no
division by $[E:K]$, and therefore includes wild finite extension
degrees. The elementary subgroup-polynomial construction itself is
classical; the current role is its use in (4)--(6).

### 4. A rational transfer for a polynomial right side is polynomial

We record a full proof of the pole input. Suppose $b\in k(x)$ and
$b\circ f-b\in k[x]$. For every finite $a\in k$, let $m(a)\ge0$
be the pole order of $b$ at $a$, with value $0$ when there is no
pole. Let $e_f(a)\ge1$ be the multiplicity of $a$ as a root of
$f(x)-f(a)$.

The pole order of $b\circ f$ at $a$ is $e_f(a)m(f(a))$. Since the
difference is regular at $a$, unequal pole orders are impossible:
the larger pole cannot cancel. Hence

$$m(a)=e_f(a)m(f(a))\quad\hbox{for every finite }a. \tag{7}$$

Only finitely many terms in either side have nonzero value. Since
$f$ is a degree-$d$ polynomial, every finite fibre has total
multiplicity $d$, and no finite value has an infinite preimage.
Summing (7) over all finite $a$ therefore gives

$$\sum_a m(a)=\sum_b m(b)\sum_{f(a)=b}e_f(a)=d\sum_bm(b).$$

The sum is a nonnegative integer and $d>1$, so it is zero. Thus
$b$ has no finite pole, and a rational function on $\mathbb P^1$
with no finite pole is a polynomial. This proof retains all finite
exceptional cycles and all ramification orders.

### 5. Tame-degree normal form

Let $a\ne0$ be the leading coefficient of $f$. For $j\ge1$,
$\Delta x^j$ has degree $dj$ and leading coefficient $a^j$.
Successively eliminate every positive exponent divisible by $d$,
working from highest to lowest, with scalar multiples of
$\Delta x^j$. Every subtraction creates only smaller exponents
than the one removed, so this terminates. It gives

$$k[x]=B\oplus V_d. \tag{8}$$

To check uniqueness of the residual representative, if nonconstant
$Q$ has degree $r$, then $\Delta Q$ has positive degree $dr$,
whereas a nonzero polynomial in $V_d$ has either degree $0$ or
positive degree not divisible by $d$. These cannot coincide.
If $Q$ is constant then $\Delta Q=0$.

Since $\gcd(d,p)=1$, the implication
$d\nmid j\Rightarrow d\nmid p^ij$ holds for every $i\ge0$.
Consequently $V_d$ is stable under $v\mapsto v^{p^i}$ and under
every polynomial of the additive form (5). If $v\in V_d$ is
nonconstant of degree $D$, then

$$\deg A(v)=p^sD>0,$$

because the highest term in (5) has strictly larger degree than
every other term. In particular $A(v)\ne0$.

### 6. Descent in the separable case

Decompose $h=\Delta Q+v$ by (8), and put $u_0=u-Q$. Subtracting
an element of $K$ preserves separability, and
$\sigma(u_0)-u_0=v$. Apply Sections 1--3 to $u_0$ to obtain a
nonzero additive polynomial $A$ and rational $b$ with
$A(v)=\Delta b$. Its right side is polynomial; Section 4 gives
$b\in k[x]$. Thus

$$A(v)\in B\cap V_d=\{0\}.$$

Section 5 rules out nonconstant $v$. Write the remaining constant
as $v=\beta\in k$. Iterating the transfer equation exactly $p$
times gives

$$\sigma^p(u_0)-u_0=p\beta=0.$$

Section 1 makes $u_0$ an element of $k$. Since $\sigma$ fixes $k$
pointwise, its original equation now gives $\beta=0$. It follows
that $h=\Delta Q$ and $u=Q+u_0\in k[x]$.

### 7. Purely inseparable part and uniqueness

For arbitrary algebraic $u$, choose $r\ge0$ such that
$w=u^{p^r}$ is separable over $K$. Such an $r$ exists: write the
irreducible minimal polynomial as $R(T^{p^r})$ with $R'$ nonzero;
$R$ remains irreducible and is the separable minimal polynomial of
$w$. We have

$$\sigma(w)-w=h^{p^r}.$$

The separable case proves $w\in k[x]$. Write again
$h=\Delta Q+v$ with $v\in V_d$. Frobenius commutes with $\Delta$,
so

$$\Delta\bigl(w-Q^{p^r}\bigr)=v^{p^r}.$$

The left side lies in $B$, and the right side lies in $V_d$.
Their common value is zero by (8). Frobenius is injective in a
field, so $v=0$ and $h=\Delta Q$. Now $u-Q$ is invariant under
$\sigma$ in the finite stable field $K(u)$, and Section 1 shows
$u-Q\in k$. Thus $u\in k[x]$ even before taking a $p$-power.

Conversely, if $h=\Delta Q$ for $Q\in k[x]$, then $u=Q$ in $K$
is an algebraic transfer. If two polynomial transfers differ, their
difference is invariant under $\sigma$ and is therefore a constant.
This completes the auxiliary theorem. $\square$

### 8. Exact wild-degree boundary, not a replacement question

The prime-to-$p$ condition cannot be simply omitted. For any
$q=p^r$, $r\ge1$, take $f(x)=x^q$ and $h(x)=x$. In the rational
function field $k(t)$ put

$$x=t^q-t,\qquad \sigma(t)=t^q.$$

Then $[k(t):k(x)]=q$, the extension is separable because the
derivative of $T^q-T-x$ in $T$ is $-1$, and

$$\sigma(x)=t^{q^2}-t^q=x^q,
\qquad \sigma(t)-t=x.$$

Thus $u=t$ is a genuine finite algebraic transfer. It is not a
polynomial in $x$: a nonconstant $Q$ gives
$\deg(Q(x^q)-Q(x))=q\deg Q\ge q$, so it cannot equal $x$; a
constant gives zero. This is a classical additive-cover boundary
example, not evidence that every wild-degree base fails descent.
It is also not a counterexample to the original odd-characteristic
quadratic question, whose degree $2$ is prime to $p$.

## 9. What remains missing for ordinary periodic data

Return to $f_c=x^2+c$ and odd $p$. Denote by $A_c$ the set of
$h\in k[x]$ admitting a compatible finite algebraic transfer as
defined above. The auxiliary theorem proves

$$A_c=B_c.$$

The old telescoping argument proves $B_c\subseteq K_c$. The
precise remaining obligation along this route is

$$
h\in K_c\quad\Longrightarrow\quad h\in A_c. \tag{9}
$$

Equivalently, the entire original problem is whether ordinary-cycle
data construct a finite stable algebraic transfer at all; there is
no further hidden rationality or polynomiality defect once one has
been constructed. This is a reduction, not a proof of (9).

The earlier finite-field interpolation supplies functions or
polynomials $Q_r$ satisfying congruences modulo $x^{q^r}-x$, with
bounds growing with $q^r$. It supplies neither a fixed-degree
algebraic relation over $k(x)$ nor an embedding on the corresponding
finite function-field extension. A graph of a function on
$\overline{\mathbb F}_p$ need not be an algebraic curve.

Roques' primary Mahler result begins with an already algebraic
formal Laurent solution over a monomial base. Neither it nor the
inspected Fernandes abstract establishes (9) from native ordinary
quadratic orbit sums. Formal conjugacy at infinity also does not
turn arbitrary transformed coefficients into rational Mahler
coefficients. No such source transfer is used here.

The R3 prime-period high-contact condition and R4 trace blind spot
remain valid old auxiliary information. This proof bypasses them
only *after* the new algebraicity premise has been supplied; it
does not exclude their hypothetical defects unconditionally.

## Corrections, remaining risks and execution boundary

The initially considered infinity-slope/Puiseux sketch was not used:
positive-characteristic ramification would require extra care, and
the minimal-polynomial argument proves the needed result directly.
No unproved Newton-polygon assertion is retained as evidence.

The auxiliary theorem is complete at author level and is made
available for independent internal checking. No non-author approval,
global novelty, or independent-paper admission is claimed by this
file. The mathematical source comparison is bounded by the actual
access recorded in [SOURCE_AUDIT.md](SOURCE_AUDIT.md).

No mathematical program, old certification, factorization census,
TeX/PDF build, GPU, external model/API or Git mutation was run.
This auxiliary result does not supply a target Euler factor, root
number, automorphy, zero correspondence, or Hilbert--Pólya operator.
