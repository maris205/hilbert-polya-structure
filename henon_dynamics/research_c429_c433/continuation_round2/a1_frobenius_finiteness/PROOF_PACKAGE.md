# Round 2 A1: finite Frobenius dependence from ordinary cycles

2026-09-09 UTC. Frozen before substantial new proof work. First-pass files
and reviews are read-only. This is one continuation of PC424-L, not a new
independent paper question.

## Claim

For every odd prime $p$, $k=\overline{\mathbb F}_p$, $c\in k$, and
$f=x^2+c$, put $\Delta Q=Q\circ f-Q$ and

$$K_c=\{h\in k[x]:\sum_{a\in O}h(a)=0\text{ for every ordinary primitive }f\text{-orbit }O\},
\qquad B_c=\Delta k[x].$$

The original unchanged claim is $K_c=B_c$ (or a full defect classification
if equality fails). The exact bridge investigated here is

$$h\in K_c\Longrightarrow
\exists s\ge0,\ a_0,\ldots,a_s\in k,\ a_s\ne0,\ Q\in k[x]:
\sum_{i=0}^{s}a_i h^{p^i}=\Delta Q. \tag{F}$$

The coefficients, $s$, and $Q$ may depend on $(p,c,h)$, but not on a
finite field of periodic points or a period cutoff. Equivalently, the full
Frobenius orbit of the class of $h$ in $k[x]/B_c$ is linearly dependent
over $k$. This is not dependence of coefficientwise Frobenius twists.

## Status

Original claim and bridge (F): **NOT CURRENTLY JUSTIFIED** at freezing.
The original ordinary primitive-period quantifier is retained, including
periods divisible by $p$; each distinct orbit point is counted once.
One application of $(x,y)\mapsto(f(x),y+h(x))$ is the native clock.

## Imported inputs and source subtraction

- The accepted first-pass [A1 supplement](../../lanes/a1_periodic_coboundary/PROOF_SUPPLEMENT.md)
  and [E8 review](../../reviews/e8_coboundary/REVIEW.md) prove the free
  Frobenius-module structure of $K_c/B_c$, the zero-or-infinite dimension
  alternative, and descent of degree slices to a finite base field.
  They do not prove (F); those results will not be re-proved here.
- The R6 [algebraic-transfer descent](../../../research_c424_c428/continuation_round6/positive_characteristic/PROOF_AND_GAPS.md)
  is a proved conditional input. It starts with a compatible finite
  algebraic transfer and does not construct one from cycle data.
- Finite-field functional-graph interpolation and full cyclic-scheme
  binary-support detection are imported. Neither finite degree slices nor
  relations that depend on the finite field count as (F).
- A2's first-pass bounded-total-degree graph extraction is imported;
  the actual uniform total-degree premise is not supplied by interpolation.

## Strategy and cheap failure criterion

Test whether a genuine uniform Frobenius relation can be extracted from
finite-field cycle data, using characteristic-$p$ linear/étale cohomology
or an explicit coefficient mechanism. Before using any finiteness theorem,
identify its ambient space, scalar field, Frobenius operation and degree
or ramification bounds. A theorem for each bounded conductor/degree is not
a theorem for their unbounded union.

The decisive success is (F) with all original quantifiers. The decisive
negative control for a proposed compactness argument is an explicit
sequence of finite-level relations whose orders or supports necessarily
escape every bound, while preserving exactly the assumptions actually
used by that argument. Such a control refutes that extraction step, not
PC424-L unless it also has zero sums on every ordinary primitive orbit.

No mathematical program, old rerun, manuscript/PDF, evaluation, shared-index
or Git action is authorized in this lane. Only this new directory is writable.

## Round-2 outcome: an exact algebraic interface, not (F)

The new result of this continuation is the explicit identification below
of ordinary orbit traces, polynomial coboundaries, and periodic-scheme
coinvariants inside one finitely presented algebra. It does **not** prove
trace separation or Frobenius finiteness. General crossed-product
Hochschild-homology formulas are classical; the specialization and the
exact match to the frozen PC424-L quantifiers are the reusable interface,
not a claim of a new general homology theorem.

The constructions in Sections 1–3 below work for any algebraically closed
field $k$ and polynomial $f\in k[x]$ of degree at least two. Sections 4–5
return to the frozen positive-characteristic question.

### 1. The ascending dynamics algebra

Let $R=k[x]$ and $\sigma r=r\circ f$. Form the injective direct limit

$$D=\varinjlim(R\mathrel{\mathop{\longrightarrow}^{\sigma}}R
 \mathrel{\mathop{\longrightarrow}^{\sigma}}\cdots).
 \tag{1}$$

Write $x_i$ for the variable of stage $i$. Thus
$x_i=f(x_{i+1})$, and $D=\bigcup_{i\ge0}k[x_i]$ is a commutative
domain containing $R=k[x_0]$. The automorphism $\alpha$ of $D$ is
specified by $\alpha(x_i)=f(x_i)$ and $\alpha^{-1}(x_i)=x_{i+1}$;
it fixes $k$. In particular, $D=\bigcup_{N\ge0}\alpha^{-N}R$.

Define the skew Laurent algebra

$$A_f=D[T,T^{-1};\alpha],\qquad Td=\alpha(d)T,
\qquad A_f=\bigoplus_{n\in\mathbb Z}DT^n. \tag{2}$$

It has the finite presentation

$$A_f\cong k\langle X,T,U\rangle/
 (TU-1,UT-1,TXU-f(X)). \tag{3}$$

Indeed, in (2), $x_i=T^{-i}x_0T^i$, so $x_0,T,T^{-1}$ generate.
Conversely, in the presented algebra put $z_i=U^iXT^i$.
The relation gives $z_i=f(z_{i+1})$. Every two $z_i$ commute because
the earlier one is a polynomial in the later one. Hence the stage maps
define $D\to A_f$ and the indicated conjugation relation gives the
inverse homomorphism. These two constructions are inverse on generators.

### 2. Ordinary cycles classify all finite-dimensional simple modules

**Proposition 2.1.** The nonzero finite-dimensional simple unital
$A_f$-modules are parametrized by an ordinary primitive $f$-cycle $O$
of length $\ell$ and a scalar $\lambda\in k^\times$. Their dimension
is $\ell$. On such a module, $X$ is diagonal with each element of $O$
appearing once, and $T^{-\ell}=\lambda I$.

**Proof.** Let $V$ be a nonzero finite-dimensional simple module.
Here $T$ denotes the invertible operator representing the generator.
Let $E$ be the sum of the ordinary, not generalized, eigenspaces of
$X$. It is nonzero because $k$ is algebraically closed. The relation
$XT^{-1}=T^{-1}f(X)$ gives

$$Xv=av\quad\Longrightarrow\quad
 XT^{-1}v=f(a)T^{-1}v. \tag{4}$$

Thus $T^{-1}E\subseteq E$. Since $E$ is finite-dimensional and $T$
is invertible, this inclusion is equality. Consequently $E$ is stable
under $X,T,T^{-1}$, so simplicity gives $E=V$. This proves that $X$
is semisimple without using any derivative or a noncritical-cycle
assumption.

Let $S$ be its finite spectrum. Equation (4) and $T^{-1}V=V$ show
that $f:S\to S$ is surjective and therefore a permutation. Furthermore,
$T^{-1}V_a=V_{f(a)}$: no other eigenspace can map to this target,
and the direct-sum images fill $V$. Each cycle in $S$ gives a submodule,
so $S$ is one primitive cycle $O$ of length $\ell$.

The invertible return operator $T^{-\ell}$ preserves $V_a$. Choose
an eigenvector $0\ne w\in V_a$ with eigenvalue $\lambda\ne0$.
The vectors $w,T^{-1}w,\ldots,T^{-(\ell-1)}w$ have distinct
$X$-eigenvalues and are linearly independent. Their span is stable
under $X,T^{-1}$, including the last return $T^{-\ell}w=\lambda w$,
and therefore under $T$ as well. Simplicity makes this span all of $V$.

Conversely, for $O=(a_0,\ldots,a_{\ell-1})$ with
$f(a_i)=a_{i+1}$, use a basis $e_i$, put $Xe_i=a_ie_i$, and let
$T^{-1}e_i=e_{i+1}$, with $T^{-1}e_{\ell-1}=\lambda e_0$.
Equation (4) verifies the defining relation. An $X$-stable subspace
is stable under the polynomial spectral projections onto the individual
$ke_i$. Any nonzero submodule therefore contains one $e_i$, and
$T^{-1}$ then supplies all of them. The module is simple.
The spectrum and scalar return recover $O$ and $\lambda$, proving
the classification. $\square$

**Corollary 2.2 (exact trace interface).** For every $h\in R$,

$$\operatorname{tr}_{O,\lambda}h(X)=\sum_{a\in O}h(a),
\qquad
\operatorname{tr}_{O,\lambda}(h(X)T^n)=
\begin{cases}
 \lambda^{-n/\ell}\sum_{a\in O}h(a),&\ell\mid n,\\
 0,&\ell\nmid n.
\end{cases} \tag{5}$$

The second formula follows because a nontrivial cyclic shift has zero
diagonal, while $T^n=\lambda^{-n/\ell}I$ if $\ell\mid n$.
Every finite-dimensional module has a finite composition series and
the ordinary matrix trace is additive across invariant subspaces.
Consequently, with the original $f=x^2+c$,

$$K_c=\{h\in R:\operatorname{tr}\rho(h)=0
 \text{ for every finite-dimensional unital representation }\rho
 \text{ of }A_f\}. \tag{6}$$

Moreover, $h\in K_c$ makes $hT^n$ trace-zero in every such
representation, for every $n\in\mathbb Z$. Nothing here divides by
$\ell$, counts a repeated orbit point, or omits $p\mid\ell$.
Nonsemisimple modules, including possible Jordan blocks, give no
additional trace constraints beyond (6).

### 3. All graded commutator quotients

Write $[A_f,A_f]$ for the **linear span**, not the two-sided ideal,
of commutators. Its grading defines
$HH_0(A_f)=A_f/[A_f,A_f]$.

**Proposition 3.1.** There are canonical vector-space isomorphisms

$$HH_0(A_f)_0\cong R/(\sigma-1)R, \tag{7}$$

and, for $n\ne0$,

$$HH_0(A_f)_n\cong
\frac{R/(f^{|n|}(x)-x)}
 { (\sigma-1)\bigl(R/(f^{|n|}(x)-x)\bigr)}. \tag{8}$$

Here $f^m$ denotes composition iteration. Formula (8) uses the full
possibly nonreduced periodic scheme; the denominator is a linear
image in its coordinate ring, not an ideal.

**Proof of (7).** The degree-zero part of a homogeneous commutator is

$$[aT^i,bT^{-i}]=a\alpha^i(b)-b\alpha^{-i}(a)
 =(\alpha^i-1)(b\alpha^{-i}(a)). \tag{9}$$

For every integer $i$, the image of $\alpha^i-1$ lies in the image
of $\alpha-1$ by a finite geometric sum (also for negative $i$).
Conversely, $(\alpha-1)d=[T,dT^{-1}]$.
Taking degree-zero components of arbitrary commutators therefore gives

$$[A_f,A_f]\cap D=(\alpha-1)D. \tag{10}$$

The inclusion $R\to D$ induces a surjection
$R/(\sigma-1)R\to D/(\alpha-1)D$: for
$u\in\alpha^{-N}R$, the classes of $u$ and $\alpha^Nu\in R$
are equal. It is also injective. If $h=(\alpha-1)u\in R$ with
$u\in\alpha^{-N}R$ and $r=\alpha^Nu\in R$, then

$$\alpha^Nh=(\alpha-1)r,\qquad
\alpha^Nh-h=(\alpha-1)\sum_{j=0}^{N-1}\alpha^jh.
 \tag{11}$$

Both right-hand transfers are in $R$. Subtracting proves
$h=(\sigma-1)(r-\sum_{j=0}^{N-1}\sigma^jh)\in(\sigma-1)R$.
For $N=0$ the sum is empty. No algebraic-transfer theorem or R6
is needed for this direct-limit descent. Equations (10)–(11) give (7).

**Proof of (8).** For a nonzero integer $n$, let
$J_n=(\alpha^n(d)-d:d\in D)$ be the ideal of $D$ generated by
these differences. Identify $DT^n$ with $D$ by its coefficient.
The commutators $[a,bT^n]$ contain the whole ideal $J_n$, and
$[T,bT^{n-1}]$ contains $(\alpha-1)D$. Conversely, a general
homogeneous commutator with total degree $n$ has coefficient

$$a\alpha^i(b)-b\alpha^{n-i}(a).
 \tag{12}$$

The ideal $J_n$ is $\alpha$-stable, and $\alpha^n=1$ on $D/J_n$.
Thus (12), modulo $J_n$, is
$(\alpha^i-1)(b\alpha^{-i}(a))$, which is in the image of
$\alpha-1$. It follows that

$$HH_0(A_f)_n\cong D/\bigl(J_n+(\alpha-1)D\bigr). \tag{13}$$

We have $J_{-n}=J_n$, so assume $n>0$. Since $\alpha^n=1$ on
$D/J_n$, every $x_i=\alpha^{-i}x_0$ is a nonnegative iterate
of $f$ applied to $x_0$, and $f^n(x_0)=x_0$. This gives a surjection
$R/(f^n-x)\to D/J_n$. It is an isomorphism: the inverse sends
$x_i$ to $f^{r_i}(\bar x)$, where $0\le r_i<n$ and
$r_i\equiv-i\pmod n$. These images respect $x_i=f(x_{i+1})$,
and the induced $\alpha$ is precisely $\sigma$. Quotienting by
the linear image of $\alpha-1$ proves (8). $\square$

Combining (6) and (7), if $\mathcal T_f$ denotes the intersection
of the kernels of all finite-dimensional characters on $HH_0(A_f)$,
then

$$K_c/B_c\cong\mathcal T_f\cap HH_0(A_f)_0. \tag{14}$$

This is the exact degree-zero trace-separation problem, not its solution.

### 4. What finite-dimensional quotients really imply in characteristic p

There is a standard $p$-semilinear map on the commutator quotient of
any associative $k$-algebra $A$ in characteristic $p$:

$$F:HH_0(A)\longrightarrow HH_0(A),\qquad [a]\longmapsto[a^p].
 \tag{15}$$

For completeness, cyclic rotation of a length-$p$ word in $a,b$
shows $[(a+b)^p]=[a^p]+[b^p]$: every mixed cyclic orbit has size
$p$ and identical classes. Further,
$[(ab-ba)^p]=[(ab)^p]-[(ba)^p]=0$, since the two latter words
are cyclic rotations. Additivity now proves well-definedness modulo
any finite sum of commutators. Scalar multiplication is $p$-semilinear.

For (2), $F$ sends grade $n$ to grade $pn$. More explicitly, the skew
Laurent multiplication gives, for $a\in D$,

$$F([aT^n])=
\left[\left(\prod_{j=0}^{p-1}\alpha^{jn}(a)\right)T^{pn}\right].
 \tag{15a}$$

Thus the general graded operation is a twisted norm, not coefficientwise
$p$-th power at a fixed nonzero grade. Its grade-zero restriction in (7)
is exactly $[h]\mapsto[h^p]$, the Frobenius operation in (F).
Thus (F) asks that every class in the right side of (14) satisfy a
nonzero scalar linear relation among its $F$-iterates. The accepted
first-pass freeness theorem then forces that class to vanish. No new
proof of the imported freeness theorem is claimed.

**Finite-quotient fact.** Let $Q$ be a finite-dimensional unital
$k$-algebra over an algebraically closed field of characteristic $p$.
If $a\in Q$ has zero trace on every simple $Q$-module, then there
exists $s=s(Q,a)$ with $[a^{p^s}]=0$ in $HH_0(Q)$.

Indeed, the semisimple quotient $Q/\operatorname{rad}Q$ is a product
of matrix algebras. The hypothesis says that the image of $a$ is a
sum of commutators there, so $a$ is a sum of commutators plus an
element $r$ of the radical. The radical is nilpotent. Equation (15)
gives $[a^{p^s}]=[r^{p^s}]=0$ when $p^s$ exceeds its nilpotence
bound. Conversely, Frobenius-nilpotence of the class forces zero
simple traces since $\operatorname{tr}(M^{p^s})=(\operatorname{tr}M)^{p^s}$.

Applied to all finite-dimensional quotients of $A_f$, this proves
only **local** Frobenius-nilpotence of a trace-radical class. The
exponent and the commutator expression may depend on the quotient.
Neither this fact, nor (8), gives a uniform relation in $HH_0(A_f)_0$.
Finite-level nilpotence must not be relabelled as (F).

### 5. Primary-source subtraction and a blanket-theorem negative control

The following primary texts were inspected on 2026-09-09.

- Etingof's [Rings, Ideals, and Modules, Section 1.9, Theorem 1.10](https://ocw.mit.edu/courses/18-706-noncommutative-algebra-spring-2023/mit18_706_s23_notes_by_pavel_etingof.pdf)
  states independence of finite-dimensional irreducible characters.
  Its assertion that the characters span the entire dual commutator
  quotient assumes the algebra itself is finite-dimensional semisimple.
  That latter hypothesis does not hold for $A_f$, which contains $k[x]$.
- Klep–Špenko's [A tracial Nullstellensatz, Theorem 3.1](https://igorklep.github.io/files/spurnullstellensatz7nov13v3.pdf)
  assumes an algebraically closed field of characteristic zero and
  trace equations in a free algebra evaluated on arbitrary matrix
  tuples of all sizes. Our hypothesis is instead positive characteristic
  and matrix tuples satisfying the algebra relations (3). The theorem
  is not a trace-separation theorem for this quotient algebra.
- Ara–Cortiñas's [Tensor products of Leavitt path algebras, Section 3 and Theorem 4.4](https://arxiv.org/pdf/1108.0352)
  provides the general graded crossed-product homology context and
  the Leavitt computation used in the control below. Equations (7)–(8)
  have been checked directly above; they are not asserted to supersede
  those general methods.

Here is an explicit obstruction to any proposed theorem saying
that *every finitely presented algebra* has a Frobenius-torsion
finite-representation trace radical. Let $L_2$ have generators
$u_1,u_2,v_1,v_2$ and relations $v_i u_j=\delta_{ij}$ and
$u_1v_1+u_2v_2=1$. On a unital module $V$ these operators give
inverse vector-space isomorphisms

$$V\oplus V\longrightarrow V,\ (a,b)\longmapsto u_1a+u_2b,
\qquad V\longrightarrow V\oplus V,\ w\longmapsto(v_1w,v_2w).
 \tag{16}$$

Thus there is no nonzero finite-dimensional unital representation;
this is an integer dimension argument, valid in characteristic $p$.
Nevertheless, Theorem 4.4 of Ara–Cortiñas identifies positive grade
$m$ of $HH_0(L_2)$ with the coinvariants of cyclic rotation on
length-$m$ words in $u_1,u_2$. The class of $u_1^m$ is nonzero:
the coefficient functional of that one-word rotation orbit vanishes
on rotation differences and takes value one there. Consequently
$[u_1^{p^i}]$, $i\ge0$, are nonzero in distinct grades and are
linearly independent. They all belong to the finite-representation
trace radical. This refutes the blanket theorem, **not** (F) for $A_f$.

The control is source subtraction, not a new standalone research claim.
It does not assert that $A_f$ lacks finite representations; Proposition
2.1 explicitly constructs them.

## Unchanged unresolved step and next discriminating target

Original PC424-L and (F) remain **NOT CURRENTLY JUSTIFIED** after
this continuation. A concrete next target is a theorem specific to
the ascending algebra (3) that upgrades the local finite-quotient
Frobenius-nilpotence in Section 4 to a finite Frobenius relation in
the grade-zero space (7). Such a theorem must have hypotheses that
distinguish this dynamics algebra from the control (16), and it must
not replace ordinary-cycle traces by full nonreduced-scheme tests.

The useful connection to the coordinator's periodic-nilradical lane
is (8): the nonzero graded pieces retain the coinvariants of the full
periodic coordinate rings, while their finite-dimensional character data in
(5) still consist only of the original reduced ordinary cycles.
No bounded nilpotence exponent, degree bound, or separation theorem
is supplied here. No mathematical computation was run, and no old
proof, manuscript, evaluation, shared index, or Git object was changed.
