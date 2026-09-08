# Exact torsion-closure and projection kernel

Date: 2026-09-08 UTC. Auxiliary input to AF5-C, under
[the frozen contract](FROZEN_CONTRACT.md). This is an explicit classical
algebraic kernel, not a new candidate, admission, or novelty claim.

## Claim

Let $d\ge0$, let $\mu_\infty\subset\mathbb C^*$ denote the roots of
unity, and put $T_d=(\mathbb C^*)^d$ and $T_{d,\mathrm{tor}}=\mu_\infty^d$.
Given a finite list of Laurent polynomials

$$f_1,\ldots,f_s\in K[X_1^{\pm1},\ldots,X_d^{\pm1}],$$

with exact coefficients in a finite cyclotomic field, there is an explicit
terminating algorithm returning a finite union $U$ of **connected torsion
cosets** such that, for their common zero set $X\subseteq T_d$,

$$U=\operatorname{TC}(X):=\overline{X\cap T_{d,\mathrm{tor}}}^{\mathrm{Zar}},
\qquad U\subseteq X,
\qquad U\cap T_{d,\mathrm{tor}}=X\cap T_{d,\mathrm{tor}}.$$

Each output coset has an explicit torsion translating point and a saturated
integer character lattice. The translating points may require an explicitly
computed finite cyclotomic extension of $K$.

Finite unions of such cosets admit terminating exact intersection,
containment, equality, and coordinate-projection algorithms. For every
coordinate projection $\pi:T_d\to T_m$,

$$\pi(U\cap T_{d,\mathrm{tor}})
=\pi(U)\cap T_{m,\mathrm{tor}}.$$

In particular, $\pi(U)$ is closed; projection here does not mean replacing
a possibly nonclosed image by its closure.

## Status

**PROVABLE AS STATED**, with the finite exact input model below.
The construction is intentionally exhaustive, not a practical complexity
claim. No implementation or mathematical program has been run.

## Assumptions

- The base field has characteristic zero, and all geometric statements are
  over $\mathbb C$ (equivalently, an algebraic closure containing the specified
  cyclotomic numbers).
- The input gives finitely many exponents in $\mathbb Z^d$ and exact
  coefficients in $K=\mathbb Q(\omega)$, where
  $\omega=\zeta_N=\exp(2\pi i/N)$, with rational polynomial representations
  modulo the cyclotomic polynomial $\Phi_N$.
- A finite exact subfield of $\mathbb Q^{\mathrm{cyc}}$ is sufficient if its
  embedding into some such $K$ is supplied. If coefficients instead have
  exact algebraic-number descriptions with decidable equality, the promised
  cyclotomic embedding can be recovered by dovetailing $N$ and rational
  polynomial expressions in $\zeta_N$, testing equality for each input
  coefficient. The promise of cyclotomic membership makes that search
  terminate; no bound on its speed is asserted.
- The question concerns the underlying zero set, not scheme multiplicities.
  The defining ideal need not be radical and the zero set need not be pure
  dimensional, irreducible, or nonempty.

## Notation

For $a=(a_1,\ldots,a_d)\in\mathbb Z^d$, write
$x^a=\prod_i x_i^{a_i}$. For an integer $r\times d$ matrix $A$, let

$$h_A:T_d\longrightarrow T_r,\qquad
(h_A(x))_i=x^{A_{i,*}}.$$

Thus $h_A\circ h_B=h_{AB}$ whenever the matrix dimensions match.
For an integer $b\ge2$, put

$$P(b)=\prod_{\substack{p\text{ prime}\\p\le b}}p.$$

A lattice $L\subseteq\mathbb Z^d$ is saturated if
$na\in L$, $n\ne0$, implies $a\in L$. Set

$$H_L=\{x\in T_d:x^a=1\text{ for every }a\in L\}.$$

A connected torsion coset is $\xi H_L$, where $L$ is saturated and
$\xi\in T_{d,\mathrm{tor}}$. The trivial torus $T_0$ is the one-point
group; its unique point is torsion.

## Proof strategy

Expand cyclotomic coefficients into rational-weighted root-of-unity terms.
A rational Mann bound makes the ratios within each minimal vanishing block
finite to enumerate. Each ratio pattern yields binomial equations, whose
solutions and connected components are computed by Smith normal form.
The output contains every torsion zero and is contained in the original
zero set. Torsion density then identifies its Zariski closure exactly.
The same normal form provides projection images and torsion lifts.

## Dependency map

1. Step 1 proves the rational Mann bound needed for completeness. Its
   classical attribution and accessed-source boundary are recorded in
   [SOURCE_AUDIT.md](SOURCE_AUDIT.md).
2. Step 2 gives exact cyclotomic arithmetic and solves binomial systems by
   integer Smith normal form, retaining every connected component.
3. Steps 3–5 construct the torsion closure and prove soundness, coverage,
   density, and handling of systems of equations.
4. Steps 6–7 prove the effective set operations and exact torsion lifting.
5. Step 8 states the interface usable by the coordinator's correspondence
   algorithm. No Loxton, dynamical finiteness, or periodicity result enters
   this kernel proof.

## Proof

### Step 1. Rational Mann bound, including repeated roots and signed weights

**Lemma 1.** Suppose $b\ge2$, $q_i\in\mathbb Q^*$, and
$\theta_i\in\mu_\infty$ satisfy

$$\sum_{i=1}^b q_i\theta_i=0,$$

and no nonempty proper indexed subsum vanishes. Then, for every $i,j$,

$$\theta_i/\theta_j\in\mu_{P(b)}.$$

The roots need not be distinct. The weights may be negative; they are
required to be rational, not arbitrary cyclotomic coefficients.

**Proof.** Divide all roots by $\theta_1$, so that $\theta_1=1$, and
let $n$ be the least common multiple of their orders. For $n=1$ there is
nothing to prove. We show that $n$ is squarefree and every prime divisor
of $n$ is at most $b$.

Suppose $p^a\mid n$ with $a\ge2$ and $p^a$ the exact $p$-part of $n$.
Let $\rho$ be a primitive $n$th root. Every $\theta_i$ has a unique
expression of the form

$$\theta_i=\rho^{e_i}\eta_i,
\qquad 0\le e_i<p,\qquad \eta_i\in\mu_{n/p},$$

where uniqueness refers to the residue $e_i$ after an exponent of $\rho$
is chosen modulo $n$. Since

$$[\mathbb Q(\mu_n):\mathbb Q(\mu_{n/p})]
=\varphi(n)/\varphi(n/p)=p,$$

the powers $1,\rho,\ldots,\rho^{p-1}$ are linearly independent over
$\mathbb Q(\mu_{n/p})$. Grouping the relation by $e_i$ shows that
every occupied residue class is a vanishing indexed subsum. Minimality
therefore forces a single occupied residue class. Because $\theta_1=1$,
that class is $0$. Thus every $\theta_i$ lies in $\mu_{n/p}$, contradicting
the definition of $n$. Hence $n$ is squarefree.

Now let $p\mid n$, write $n=pm$ with $(p,m)=1$, and choose a primitive
$p$th root $\rho$. Write

$$\theta_i=\rho^{e_i}\eta_i,
\qquad 0\le e_i<p,\qquad \eta_i\in\mu_m.$$

The extension $\mathbb Q(\mu_{pm})/\mathbb Q(\mu_m)$ has degree
$p-1$, so the minimal polynomial of $\rho$ over $\mathbb Q(\mu_m)$ is
$1+Z+\cdots+Z^{p-1}$. Put

$$A_e=\sum_{i:e_i=e}q_i\eta_i.$$

The relation $\sum_{e=0}^{p-1}A_e\rho^e=0$ implies that all $A_e$
are equal: a polynomial of degree at most $p-1$ vanishing at $\rho$
is a scalar multiple of its displayed minimal polynomial. If $p>b$,
at least one residue class is empty, so one $A_e=0$ and consequently
all $A_e=0$. Minimality again forces a single occupied class, which is
$0$ because of $\theta_1=1$. This would put all roots in $\mu_m$ and
contradict the definition of $n$. Thus $p\le b$.

Therefore $n\mid P(b)$, which proves the assertion after restoring the
common factor $\theta_1$. The argument used indexed subsums, so repeated
roots and signed rational weights do not invalidate it. $\square$

### Step 2. Exact arithmetic and complete solution of binomial systems

Rational arithmetic and remainder reduction modulo $\Phi_L$ decide
equality in $\mathbb Q(\zeta_L)$. Finitely many cyclotomic fields are
embedded in a common one using the least common multiple of their
conductors. Roots of unity can be recorded as rational classes in
$\mathbb Q/\mathbb Z$, with addition of classes representing
multiplication. Thus both the rational-weighted zero tests below and
equalities between root-of-unity constants are exact finite operations.

Consider a binomial system

$$h_A(x)=\delta,\qquad A\in\mathbb Z^{r\times d},
\qquad \delta\in\mu_\infty^r.$$

Compute integer Smith normal form

$$UAV=D,\qquad U\in\operatorname{GL}_r(\mathbb Z),
\quad V\in\operatorname{GL}_d(\mathbb Z),$$

where $D$ has positive diagonal entries $s_1,\ldots,s_k$ and all
other entries zero. Integer Smith normal form is a terminating sequence
of Euclidean integer row and column operations. Define

$$x=h_V(y),\qquad \delta'=h_U(\delta).$$

Because $h_U$ and $h_V$ are automorphisms, the original system is
equivalent to

$$y_j^{s_j}=\delta'_j\quad(1\le j\le k),
\qquad 1=\delta'_j\quad(k<j\le r).$$

If one of the latter conditions fails, there are no solutions. Otherwise
enumerate every $s_j$th root $\rho_j$ of $\delta'_j$. More explicitly,
if all $\delta'_j\in\mu_L$ and $\delta'_j=\zeta_L^{a_j}$, the choices are

$$\rho_j=\zeta_{Ls_j}^{a_j+Lt},\qquad 0\le t<s_j.$$

For each independent tuple of choices, the corresponding solution set is

$$C_\rho=h_V\bigl(\rho_1,\ldots,\rho_k,
T_{d-k}\bigr)=\xi_\rho H,
\qquad
\xi_\rho=h_V(\rho_1,\ldots,\rho_k,1,\ldots,1).$$

The subtorus $H=h_V(\{1\}^k\times T_{d-k})$ is connected and isomorphic
to $T_{d-k}$. Its character lattice has as a basis the first $k$ rows of
$V^{-1}$. It is saturated because those rows belong to a basis of
$\mathbb Z^d$. These components are pairwise disjoint and exhaust the
system. In particular, no connectedness assumption about the original
binomial kernel has been made. The translating points lie in the explicit
field of conductor dividing $L\operatorname{lcm}(s_1,\ldots,s_k)$.

When $r=0$, this procedure returns $T_d$. When $k=0$, consistency is
the condition that all transformed constants equal $1$, and a consistent
system again returns $T_d$. The same formulation covers $d=0$ and returns
the singleton $T_0$ or the empty set.

### Step 3. Finite pattern enumeration for one Laurent polynomial

First combine repeated Laurent monomials by exact coefficient addition
and delete zero coefficients. A zero polynomial imposes no restriction.
A single nonzero Laurent monomial has no zero on $T_d$, since it is a
nonzero constant times a unit.

For every remaining polynomial, expand its coefficients in rational
powers of the fixed root $\omega$. Delete zero rational weights, obtaining
an exact finite expression

$$f(x)=\sum_{i=1}^r q_i\omega^{j_i}x^{u_i},
\qquad q_i\in\mathbb Q^*,\quad u_i\in\mathbb Z^d.$$

Expanded terms can share $u_i$; they remain indexed terms. The count $r$
is the number of expanded rational-weighted terms, not necessarily the
number of nonzero Laurent monomials in the original polynomial.

Enumerate all set partitions $\mathcal P$ of $\{1,\ldots,r\}$ with
every block of size at least two. For each block $B$, let $b=|B|$, choose
its smallest index $i_0$, and enumerate

$$\eta_{i_0}=1,\qquad \eta_i\in\mu_{P(b)}\quad(i\in B\setminus\{i_0\}).$$

Retain only tuples passing the exact test

$$\sum_{i\in B}q_i\eta_i=0.$$

For each collection of retained tuples, one per block, form the binomial
system

$$x^{u_i-u_{i_0}}
=\eta_i\omega^{j_{i_0}-j_i}
\quad(i\in B\setminus\{i_0\},\ B\in\mathcal P).\tag{1}$$

Solve each such system completely by Step 2 and collect its connected
torsion cosets. Call their union $U_f$. All enumerations are finite:
there are finitely many set partitions, each root-ratio set is finite,
and every binomial system has finitely many computed components.

It is unnecessary to test that a retained block is minimal. Minimality
is needed to bound the actual ratios in the completeness proof; soundness
uses only the retained exact weighted equality. Allowing extra nonminimal
patterns can create duplicate valid cosets, not false zeros.

### Step 4. Soundness, torsion coverage, and density

If $x$ satisfies one system (1), then within every block

$$\omega^{j_i}x^{u_i}
=\eta_i\omega^{j_{i_0}}x^{u_{i_0}}.$$

Therefore its contribution to $f(x)$ is

$$\sum_{i\in B}q_i\omega^{j_i}x^{u_i}
=\omega^{j_{i_0}}x^{u_{i_0}}
\sum_{i\in B}q_i\eta_i=0.$$

Summing over the blocks proves $U_f\subseteq V(f)$ for all complex
points of every generated coset, not only its torsion points.

Conversely, let $x\in T_{d,\mathrm{tor}}$ with $f(x)=0$ and put
$\theta_i=\omega^{j_i}x^{u_i}$. These are roots of unity. A finite
vanishing indexed sum of nonzero terms can be partitioned into minimal
vanishing subsums: choose an inclusion-minimal nonempty vanishing subset,
remove it, and repeat on the remaining vanishing sum until no terms remain.
Every chosen block has size at least two. Lemma 1 shows that its ratios
$\theta_i/\theta_{i_0}$ belong to $\mu_{P(|B|)}$. This exact partition
and these ratios are enumerated in Step 3, pass its weighted tests, and
give a system (1) satisfied by $x$. Step 2 does not discard a solution,
so $x\in U_f$.

Torsion points are Zariski dense in $T_e$ for every $e\ge0$. To prove
this, let a Laurent polynomial vanish on $\mu_\infty^e$ and multiply it
by a Laurent monomial to obtain an ordinary polynomial. For $e=1$,
infinitely many distinct roots force it to be zero. For $e>1$, fix
torsion values of the first $e-1$ variables. The resulting polynomial in
the last variable is zero, so each coefficient polynomial vanishes on
$\mu_\infty^{e-1}$. Induction proves every coefficient polynomial zero.
The case $e=0$ is the singleton assertion.

The monomial isomorphisms and torsion translations in Step 2 take dense
torsion sets to dense torsion sets. Thus torsion points are dense in each
generated coset and in the finite union $U_f$. Since $U_f$ is closed,
contains all torsion zeros of $f$, and is contained in $V(f)$, both
inclusions give

$$U_f=\overline{V(f)\cap T_{d,\mathrm{tor}}}^{\mathrm{Zar}}.$$

### Step 5. Systems of Laurent equations

For $X=\bigcap_{j=1}^sV(f_j)$ compute each $U_{f_j}$ and intersect their
finite unions by distributing intersection over the component lists.
An intersection of individual cosets is computed by stacking their
binomial equations and applying Step 2. Hence the resulting set $U$ is
again a finite union of connected torsion cosets.

Every common torsion zero belongs to every $U_{f_j}$, hence to $U$.
Also $U\subseteq X$, because each $U_{f_j}\subseteq V(f_j)$. Density
in every output coset then proves $U=\operatorname{TC}(X)$ and the
claimed equality of torsion-point sets. This is a proved special property
of these torsion closures; it is not an unqualified assertion that taking
arbitrary closures commutes with intersections.

For an empty input list the intersection is $T_d$. A nonzero constant
equation makes the output empty. For $d=0$, exact evaluation of all
constant equations decides between $T_0$ and the empty set. Polynomial
powers and nonradical input ideals cause no problem, since their zero
sets are the objects being computed.

### Step 6. Effective intersection, containment, equality, and equations

Intersection was already constructed in Steps 2 and 5. For containment,
write a connected output coset in parametric form

$$C=\{\xi\,h_B(t):t\in T_e\},$$

where $B\in\mathbb Z^{d\times e}$ is formed from the last $e$ columns
of the unimodular $V$ in Step 2. Let another connected coset $D$ be given
by finitely many basis equations $x^a=\beta_a$. Then $C\subseteq D$
if and only if, for every such basis row $a$,

$$aB=0\quad\text{and}\quad\xi^a=\beta_a.\tag{2}$$

Indeed, substituting the parametrization yields
$x^a=\xi^a t^{aB}$. A nontrivial Laurent monomial on a torus is not
constant, whereas the zero exponent gives the constant $\xi^a$.
Thus (2) is necessary and sufficient, and consists only of integer
arithmetic and equality tests between explicit roots of unity.

Equivalently, for $C=\xi H_L$ and $D=\eta H_M$, one needs
$M\subseteq L$ and $\xi^a=\eta^a$ on a basis of $M$. Integer normal
forms decide lattice containment.

A connected coset is irreducible: after the monomial coordinate change
of Step 2, its coordinate ring is a Laurent polynomial ring over a field,
which is an integral domain. An irreducible closed set contained in a
finite union of closed sets must be contained in one member. Consequently

$$\bigcup_i C_i\subseteq\bigcup_j D_j
\quad\Longleftrightarrow\quad
\text{for every }i\text{ there is }j\text{ with }C_i\subseteq D_j.$$

This gives terminating union-containment and equality tests; equality
requires containment in both directions. The empty-list cases use the
same quantified condition. Duplicates and contained components can be
removed by these tests but need not be removed for correctness.

For an ideal-based interface, a coset has the finite binomial ideal
generated by its basis equations. A finite union can be described by
the product of these finitely generated ideals: its zero set is the union.
Explicitly, take all products choosing one generator from each coset's
ideal. At a point outside every coset, each factor ideal has a nonzero
generator there, so one such product is nonzero. At a point on some
coset, every product vanishes. Use the zero ideal for the full torus and
the unit ideal for the empty set. No radical computation is required for
this zero-set representation. Laurent ideals can also be represented in
ordinary polynomial rings by adjoining inverse variables and the equations
$X_iY_i-1$.

### Step 7. Closed coordinate images and exact torsion lifting

Let $C=\xi h_B(T_e)$ be one connected coset as above and let $\pi$
select $m$ coordinates. Let $B'$ be the selected $m$ rows of $B$.
Then, as a set,

$$\pi(C)=\pi(\xi)h_{B'}(T_e).$$

Compute a rectangular Smith normal form

$$A B' W=D,\qquad A\in\operatorname{GL}_m(\mathbb Z),
\quad W\in\operatorname{GL}_e(\mathbb Z),$$

with positive entries $s_1,\ldots,s_k$ on the diagonal and zeros
elsewhere. On replacing parameters $t$ by $h_W(w)$ and applying the
target automorphism $h_A$, the image of $h_{B'}$ becomes the image of
$h_D$. Over $\mathbb C$, every nonzero number has an $s_j$th root.
Therefore

$$h_D(T_e)=\{z\in T_m:z_{k+1}=\cdots=z_m=1\}.$$

This proves directly that $\pi(C)$ is a closed connected torsion coset.
Its translating point is $\pi(\xi)$ and a saturated character-lattice
basis is given by the last $m-k$ rows of $A$.

Now take a torsion point $y\in\pi(C)$. The point

$$z=h_A\bigl(y/\pi(\xi)\bigr)$$

is torsion and satisfies $z_j=1$ for $j>k$. For each $j\le k$, choose
an $s_j$th root $w_j$ of $z_j$; such a root is itself a root of unity,
and can be explicitly listed as in Step 2. Set the remaining $w_j$ to
$1$. Then $h_D(w)=z$. Put $t=h_W(w)$ and
$x=\xi h_B(t)$. All its coordinates are roots of unity, $x\in C$,
and the displayed monomial identities give $\pi(x)=y$.

This proof neither assumes nor requires a connected projection kernel.
The empty parameter and rank-zero cases give the translating point as
a lift. Projection to $T_0$ also has that lift whenever $C$ is nonempty.
The reverse inclusion, projecting a torsion point to a torsion point,
holds coordinate by coordinate. Taking finite unions now proves

$$\pi(U\cap T_{d,\mathrm{tor}})=\pi(U)\cap T_{m,\mathrm{tor}},$$

and supplies a finite connected-coset description of the actual closed
image $\pi(U)$.

### Step 8. Exact correspondence interface

Let $R\subseteq T_{m+n}$ be any closed Laurent algebraic set with finite
exact cyclotomic coefficients, and let $\pi$ retain its first $m$
coordinates. Applying the preceding steps gives the exact closed set

$$Y=\pi\operatorname{TC}(R),$$

with the identity

$$Y\cap\mu_\infty^m
=\{u\in\mu_\infty^m:\text{there exists }v\in\mu_\infty^n
\text{ with }(u,v)\in R\}.\tag{3}$$

To justify (3), first use
$\operatorname{TC}(R)\cap\mu_\infty^{m+n}=R\cap\mu_\infty^{m+n}$,
and then use the torsion lifting in Step 7. Thus this operation solves
the existential torsion constraint exactly. If $R\subseteq V\times W$
for closed finite unions of torsion cosets, its image $Y$ is contained
in $V$ and is represented by finite exact data. Any later Noetherian or
dynamical use of this interface remains a separate theorem. $\square$

## Adversarial boundary checks by hand

1. **Cyclotomic weights cannot be fed directly into rational Mann.**
   For $f(x)=x-\zeta_\ell$ with prime $\ell>2$, the torsion solution
   has order $\ell$. Applying the two-term rational bound to $(x,1)$
   would be invalid because one coefficient is nonrational. In our
   expansion the root terms are $(x,\zeta_\ell)$ with rational weights
   $(1,-1)$, their ratio is $1$, and equation (1) gives $x=\zeta_\ell$.
2. **Repeated terms and coefficient cancellation.** The input $x-x$
   is zero after exact combination and returns the whole torus.
   For a primitive cube root $\omega$, the same is true of
   $(1+\omega+\omega^2)x$. No argument treats a cancelled coefficient
   as a surviving nonzero term.
3. **Nonprimitive lattice and disconnected kernel.** The equation
   $x^2=1$ has character lattice $2\mathbb Z$ before splitting. Its
   output is the two connected zero-dimensional cosets $\{1\}$ and
   $\{-1\}$, not a falsely connected kernel.
4. **Consistency and empty intersections.** A zero exponent equation
   $x^0=\zeta_3$ is inconsistent. The system $x^2=1$, $x=-1$ retains
   exactly $\{-1\}$, whereas $x^2=1$, $x=\zeta_3$ is empty.
5. **Projection with disconnected kernel.** The connected subtorus
   $C=\{(t^2,t):t\in\mathbb C^*\}$ projects onto the first torus.
   Its projection kernel has two points. Every root of unity nevertheless
   lifts by taking a square root, which is again a root of unity.
6. **One term, no terms, and no variables.** A nonzero Laurent monomial
   has no torus zero; a zero polynomial imposes no restriction; with no
   variables, exact constant tests return a singleton or the empty set.
7. **No absolute conductor bound is inferred.** A minimal block bounds
   ratios of its root terms. Its common root factor can have arbitrary
   order. Positive-dimensional cosets preserve that freedom; the algorithm
   never replaces their torsion points by a finite bounded-order sample.

## Corrections or missing assumptions

No weakening of the frozen geometric claim is needed. Its effective input
must be finite and exact: a black-box arbitrary complex coefficient is not
an admissible encoding. Connected output components need not be defined
over the original coefficient field, so the algorithm returns their finite
cyclotomic extensions explicitly.

## Open risks and provenance limits

- The construction is a proof of termination, not an implemented or
  benchmarked algorithm. Exhaustive partition enumeration can be extremely
  expensive. No complexity or feasibility assertion is made.
- The original Mann publisher record and extract were accessed, but its
  full 1965 theorem/proof pages were not obtained. The exact rational form
  is corroborated by primary research papers, and Lemma 1 is proved here
  rather than using inaccessible original text as an unchecked black box.
- The output remains current-team AI-assisted internal mathematical work
  pending a non-author full proof/source check. This kernel does not settle
  the main AF5-C root-length, dynamical, finiteness, or increment gates.
- Classical attribution is essential: explicit torsion-coset algorithms
  predate this package. No global novelty check, paper admission, target
  Euler/root-number result, or A2 promotion is asserted.
