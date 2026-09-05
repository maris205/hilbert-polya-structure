# C394: a nonlinear symplectic map with an exact p-adic orbit decomposition

## Claim and status

Status: **PROVABLE AS STATED**. Let $p$ be a rational prime, let $v_p(p)=1$, and let $a\in\mathbb Z_p\setminus\{0\}$ have valuation $c=v_p(a)$. Assume $c\ge1$ for odd $p$ and $c\ge2$ for $p=2$. On $X=\mathbb Z_p^2$, with the maximum norm, freeze

$$F_a(x,y)=\bigl(x+a y^2,\ y+a(x+a y^2)^2\bigr).$$

There is a jointly restricted analytic map $G_a:X\times\mathbb Z_p\to X$ satisfying $G_a(u,n)=F_a^n(u)$ for every nonnegative integer $n$ and the full action law $G_a(G_a(u,s),t)=G_a(u,s+t)$. If $u\ne0$ and $r=\min(v_p(x),v_p(y))$, then

$$\|G_a(u,t)-G_a(u,s)\|_p=p^{-(c+2r)}|t-s|_p.\tag{1}$$

Every nonzero orbit closure is therefore a scaled isometric copy of $\mathbb Z_p$ on which $F_a$ is conjugate to addition by one; the origin is the only genuine periodic point. For every algebraic subvariety $V\subset\mathbb A^2_{\mathbb Q_p}$ and $u\in X$, the set $\{n\ge0:F_a^n(u)\in V\}$ is finite or is all of $\mathbb Z_{\ge0}$.

At every finite level $N\ge1$, a nonzero residue vector with minimum valuation $r<N$ has exact period

$$L_{N,r}=p^{\max(0,N-c-2r)}.\tag{2}$$

For every integer $n\ge1$, the number of fixed residue vectors is

$$\#\operatorname{Fix}(F_a^n\bmod p^N)=p^{2(N-R)},\qquad
R=\max\left(0,\left\lceil\frac{N-c-v_p(n)}2\right\rceil\right).\tag{3}$$

The map is symplectic, preserves normalized Haar measure, and has the same-clock reversor $R_0(x,y)=(-y,-x)$. Its Koopman map is unitary but not compact. None of these source statements constructs the Riemann target, target Euler factors, a target functional equation, root numbers, or a Hilbert--Pólya operator. Route B remains disabled.

## Assumptions, notation, and ownership

The phase space is the closed unit polydisc over $\mathbb Q_p$, not the complex plane, an algebraic closure, or merely a finite residue ring. Write $\mathbb Z_p\langle x,y,t\rangle$ for the Tate algebra with the coefficient Gauss norm. All infinite analytic assertions below concern this actual Banach algebra. The variable $t$ is a $p$-adic interpolation of the original integer iteration clock, not an inserted logarithmic roof. For $z=0$, set $v_p(z)=+\infty$; $r$ is used only for a nonzero vector.

The interpolation construction and its threshold are classical: Poonen, *p-adic interpolation of iterates*, Bull. Lond. Math. Soc. 46 (2014), 525--527, Theorem 1 and Remarks 2--3, DOI 10.1112/blms/bdu010. The broader dynamical Mordell--Lang method belongs to Bell, Ghioca, and Tucker, *The dynamical Mordell--Lang problem for étale maps*, Amer. J. Math. 132 (2010), 1655--1675, arXiv:0808.3266. Mukhamedov, arXiv:2607.14339v1 (2026), owns recent effective local Strassmann certificate developments; this package does not claim a new certificate algorithm. We give the specialized proofs and the exact orbit-radius/finite-quotient consequences self-containedly. This is a repository mechanism advance, not a literature novelty certification.

## Dependency map

1. Polynomial shear factorization gives inverse, symplecticity, reversibility, and congruence compatibility.
2. The coefficientwise near-identity bound gives contraction of the finite-difference operator and a convergent joint Mahler series.
3. Density of ordinary nonnegative integers gives the action law.
4. Rescaling by the radius and strict first-term dominance give (1), then minimal orbit closures and (2)--(3).
5. A proved one-variable zero bound gives the algebraic hit-set alternative.
6. Finite quotient permutations give Haar invariance; infinite-dimensional unitarity gives noncompactness.

## Proof

### 1. The original polynomial automorphism

Put $S_x(x,y)=(x+a y^2,y)$ and $S_y(x,y)=(x,y+a x^2)$. Then $F_a=S_yS_x$ and

$$F_a^{-1}(x,y)=\bigl(x-a(y-a x^2)^2,\ y-a x^2\bigr).\tag{4}$$

Each shear pulls $dx\wedge dy$ back to itself, so $F_a^*(dx\wedge dy)=dx\wedge dy$. In coordinates its derivative is

$$DF_a(x,y)=\begin{pmatrix}
1&2ay\\2a(x+ay^2)&1+4a^2y(x+ay^2)
\end{pmatrix},\qquad\det DF_a=1.\tag{5}$$

Both maps in (4) have integral coefficients. Evaluation of an integral polynomial is 1-Lipschitz on $X$, by factoring differences of monomials. Applying this first to $F_a$ and then to its inverse proves that $F_a$ is an isometry. It induces a permutation on every $(\mathbb Z/p^N\mathbb Z)^2$ and preserves residue balls of each radius up to permutation.

The involution $R_0$ satisfies $R_0S_xR_0=S_y^{-1}$ and $R_0S_yR_0=S_x^{-1}$. Their order in the composition yields $R_0F_aR_0=S_x^{-1}S_y^{-1}=F_a^{-1}$. This is reversal of the same integer clock, not a reversal only after changing the return section.

### 2. Joint Tate interpolation with an explicit ordinary tail bound

Let $A=\mathbb Z_p\langle x,y\rangle$ and define $\Delta h=h\circ F_a-h$. The two coordinates of $F_a-(x,y)$ lie in $p^c A$. For a monomial, successive replacement of its factors shows that $h\circ F_a-h\in p^c A$. Addition gives the assertion for integral polynomials; completeness and continuity of substitution extend it to $A$. Homogeneity under scalar multiplication gives

$$\|\Delta h\|\le p^{-c}\|h\|,\qquad
\Delta^m(x,y)\in p^{cm}A^2.\tag{6}$$

The polynomial $t(t-1)\cdots(t-m+1)$ has integral coefficients. Since $v_p(m!)\le m/(p-1)$, the terms of

$$G_a(u,t)=\sum_{m=0}^{\infty}\binom{t}{m}\Delta^m u\tag{7}$$

have joint Gauss norm at most $p^{-cm+v_p(m!)}$. The number $\delta=c-1/(p-1)$ is positive under the stated assumptions. Thus (7) converges in $\mathbb Z_p\langle x,y,t\rangle^2$ and, for every $M\ge0$,

$$\left\|G_a-\sum_{m=0}^{M}\binom{t}{m}\Delta^m u\right\|
\le p^{-(M+1)\delta}.\tag{8}$$

The bound is an ordinary sufficient Gauss-norm tail bound, not an optimal Strassmann certificate. At any integer $n\ge0$, terms with $m>n$ vanish, and the binomial theorem for the commuting operators $I$ and $\Delta$ gives $G_a(u,n)=(I+\Delta)^nu=F_a^n(u)$.

All coordinates of $G_a$ are integral and have norm at most one. Hence compositions in the action law are defined on $X\times\mathbb Z_p^2$. For integer $s,t\ge0$ the law follows from composition of iterates. Nonnegative integers are dense in $\mathbb Z_p$: every residue class modulo $p^k$ has a nonnegative representative. Continuity in both variables therefore proves the action law for every $s,t\in\mathbb Z_p$. In particular $G_a(u,0)=u$ and $G_a(\cdot,-t)$ is the inverse of $G_a(\cdot,t)$. Joint analytic identities may also be deduced coefficientwise by one-variable uniqueness in each time variable; continuity suffices for the stated action on points.

### 3. A strict first-term estimate and the exact original clock

For every integer $m\ge2$ and every admissible integer $d$ (that is, $d\ge1$ for odd $p$ and $d\ge2$ for $p=2$),

$$v_p(m)<d(m-1).\tag{9}$$

Indeed $v_p(m)\le m-1$ for all $m\ge2$. Equality can occur only for $m=2,p=2$: if $k=v_p(m)\ge1$ and $p\ge3$, then $m\ge3^k>k+1$, whereas for $p=2,k\ge2$ we have $m\ge2^k>k+1$. The remaining $p=2,k=1$ case has equality only at $m=2$, and $d\ge2$ makes (9) strict.

For $t\in\mathbb Z_p$, the value $\binom{t-1}{m-1}$ is integral. To see this without an unjustified coefficient claim, approximate $t$ by ordinary integers: integer binomial values, including negative upper indices, are integral, and the fixed polynomial is continuous. The identity

$$\binom{t}{m}=\frac{t}{m}\binom{t-1}{m-1}\tag{10}$$

therefore bounds its value by $|t|_p p^{v_p(m)}$. Notice that (10) is a bound on values, whereas (8) is a bound on coefficients; these two norms are not being identified.

Take a unit-radius vector $v=(v_1,v_2)$ and parameter $b$ of valuation $d$. The vector

$$F_b(v)-v=b\bigl(v_2^2,(v_1+bv_2^2)^2\bigr)$$

has norm $p^{-d}$: if $v_2$ is a unit the first coordinate does; otherwise $v_1$ and $v_1+bv_2^2$ are units. By (6), (9), and (10), every term $m\ge2$ of (7) has norm at most

$$|t|_p p^{-dm+v_p(m)}\le |t|_p p^{-d-1}.$$

The terms converge to zero, and their whole sum has this same upper bound. The $m=1$ term has norm exactly $|t|_p p^{-d}$, so nonarchimedean strict dominance proves

$$\|G_b(v,t)-v\|_p=p^{-d}|t|_p.\tag{11}$$

For nonzero $u=p^r v$, direct substitution gives $F_a(p^r v)=p^rF_{a p^r}(v)$. The integer-iterate identity and continuity extend this to $G_a(p^r v,t)=p^rG_{a p^r}(v,t)$. Now $d=c+r$, and (11) gives

$$\|G_a(u,t)-u\|_p=p^{-(c+2r)}|t|_p.\tag{12}$$

This is strictly smaller than $\|u\|_p=p^{-r}$, because $c+r>0$. Thus every $G_a(u,s)$ has the same minimum valuation $r$. Apply (12) with basepoint $G_a(u,s)$ and time $t-s$, using the action law. This proves (1), including its quantifier for all pairs of $p$-adic times. At $t=s$ both sides are zero.

### 4. Complete orbit closures and all finite quotient periods

For $u\ne0$, (1) makes $t\mapsto G_a(u,t)$ an injective continuous map from the compact space $\mathbb Z_p$ into the Hausdorff space $X$; it is a homeomorphism onto its image and is an isometry after multiplying the source metric by $p^{-(c+2r)}$. Density of nonnegative integers shows that the image is exactly the closure of the forward orbit. The action law conjugates $F_a$ on this image to $t\mapsto t+1$. The latter is minimal because each of its orbits meets every residue class. Two such orbit closures are disjoint or equal: a common point and the invertible action law identify both images. Together with the fixed origin they give a complete decomposition of $X$ into minimal invariant compact sets.

No nonzero $u$ can satisfy $F_a^n(u)=u$ for $n\ge1$, because (12) then has nonzero right-hand side. Also $F_a(0)=0$. At the origin, (5) gives $DF_a(0)=I$ and $DF_a^n(0)=I$. The fixed point is parabolic, not a positively expanding Lyapunov orbit. Consequently the genuine point-counting zeta is $(1-z)^{-1}$; this scalar source series is not a target determinant.

Fix $N\ge1$. A residue vector not equal to zero has a well-defined minimum valuation $0\le r<N$, independent of its lift. For any lift, (12) with integer $n\ge1$ says precisely that it returns modulo $p^N$ if and only if $c+2r+v_p(n)\ge N$. This proves (2). The zero residue has exact period one because both coordinates of every lift have valuation at least $N$ and $F_a$ respects congruence classes. Every vector with $c+2r\ge N$ is already fixed; no separate assertion of an isolated finite-level origin is made.

There are

$$S_{N,r}=p^{2(N-r)}-p^{2(N-r-1)}$$

vectors in shell $r<N$. Thus that shell has exactly $S_{N,r}/L_{N,r}$ cycles, all of length $L_{N,r}$. This integer quotient follows either from its partition into permutation cycles or from the displayed powers: if $L>1$, the exponent in the quotient is $N+c-2\ge0$. Summing shells and the zero residue gives $p^{2N}$ vectors. Different shells may have the same period and their cycle counts must be added, not treated as distinct period labels. Summing the shells with $r\ge R$ and the zero residue telescopes to (3). Since $c\ge1$ and $v_p(n)\ge0$, the stated $R$ lies between zero and $N$.

In particular, all finite quotient cycles have $p$-power lengths, although no nonzero one lifts to a finite-period point in $X$. The finite native zeta is exactly

$$\zeta_N(z)=\frac1{1-z}\prod_{r=0}^{N-1}(1-z^{L_{N,r}})^{-S_{N,r}/L_{N,r}}.\tag{13}$$

This product and (3) are equivalent by expansion of $-\log(1-z^L)$. They are kept separate from the genuine $X$-zeta.

### 5. A self-contained analytic zero bound and algebraic hitting times

Let $h(t)=\sum_{j\ge0}h_jt^j\in\mathbb Q_p\langle t\rangle$ be nonzero. Its Gauss norm is attained, and let $J$ be the largest index attaining it. Then $h$ has at most $J$ distinct zeros in $\mathbb Z_p$.

Here is a proof. If $h(b)=0$ with $b\in\mathbb Z_p$, define

$$q_j=\sum_{k\ge j+1}h_k b^{k-j-1}.$$

These sums converge, $q_j\to0$, and coefficient comparison, including the constant term using $h(b)=0$, gives $h(t)=(t-b)q(t)$. For $j\ge J$, every term defining $q_j$ has norm strictly less than $\|h\|$, and their maximum is also strictly less because the coefficients tend to zero. The coefficient $q_{J-1}$, when $J\ge1$, is $h_J$ plus strictly smaller terms; its norm is $\|h\|$. For $j<J-1$, the norms are at most $\|h\|$. Hence the largest norm-attaining index of $q$ is $J-1$. If $J=0$, a zero is impossible: $h_0$ strictly dominates all other terms at $b$. Dividing successively by distinct zeros preserves the remaining zeros and lowers the largest index once each time, so there are at most $J$ zeros. This proves the required form of Strassmann's theorem.

Choose finitely many polynomial equations $H_1,\ldots,H_k$ for $V$; such a choice exists because a polynomial ring over a field is Noetherian. Substitution in the jointly restricted analytic map gives $h_i(t)=H_i(G_a(u,t))\in\mathbb Q_p\langle t\rangle$. If all these functions are identically zero, every $p$-adic time, hence every nonnegative integer time, lies in $V$. Otherwise one nonzero $h_i$ has only finitely many zeros in $\mathbb Z_p$, so the simultaneous integer hit set is finite. This proves the alternative for every $u$ and every algebraic $V$, including the empty variety, the whole plane, and the fixed origin.

The theorem gives no uniform last-hit time and no finite algorithm that always decides whether every $h_i$ is identically zero. A certified coefficient dominating a tail gives an ordinary valid Strassmann upper bound; finite samples without that condition do not. We do not assert that the nonzero orbit closures are algebraic curves, nor that they are all Zariski dense.

A concrete finite-hit control is $u=(0,1)$ and $V=\{x=0\}$. The first coordinate of the $m=1$ term is $a t$, and the bounds of §3 make the sum of its higher terms strictly smaller for every $t\ne0$. Hence $|x(G_a((0,1),t))|_p=|a t|_p$, and the hit set is exactly $\{0\}$. For the origin and any variety containing it, the hit set is all times. These examples realize both alternatives without inferring an infinite result from sampled times.

### 6. Haar, reversibility, and operator limits

Normalized Haar measure on $X$ assigns mass $p^{-2N}$ to each residue ball modulo $p^N$. The finite-level permutation from §1 preserves the measure of every such ball, then of their finite unions. These sets generate the Borel sigma algebra, so uniqueness of finite measures gives Haar invariance of $F_a$. The same conclusion holds for every time map $G_a(\cdot,t)$: approximate $t$ by nonnegative integers and use continuity to see that it induces the eventually constant finite-level permutation. Its inverse is the negative-time map.

The Koopman operator $Uf=f\circ F_a$ on complex $L^2(X)$ is unitary by measure invariance and invertibility. The signed coordinate permutation $R_0$ also permutes every residue partition and preserves Haar measure. Thus the antiunitary $Jf=\overline{f\circ R_0}$ satisfies $J^2=I$ and $JUJ=U^{-1}$. This is a natural source Hilbert-space structure, not a quantization of the target. The Hilbert space is infinite dimensional (arbitrarily fine residue partitions give subspaces of unbounded dimensions), so an orthonormal sequence has images under $U$ at pairwise distance $\sqrt2$. Thus $U$ is not compact and is in no finite Schatten class; an ordinary trace-class Fredholm determinant of $I-zU$ does not follow.

Every nonzero orbit closure has Haar measure zero in the two-dimensional ambient space. For sufficiently large $N$, (2) shows that it meets exactly $p^{N-c-2r}$ residue balls modulo $p^N$, whose union has measure $p^{-N-c-2r}\to0$. This does not contradict minimality on each one-dimensional compact orbit or Haar invariance on $X$.

### 7. Boundaries and decisive controls

If $a=0$, the map is the identity and every point is fixed; the nonzero-parameter conclusions about the unique periodic point and scale in (1) do not apply. If $p=2$ and only coefficientwise congruence modulo 2 is assumed, the general interpolation statement is false: $f(x)=-x$ has a nonzero point of period two. A restricted analytic interpolant of its integer iterates at $x=1$ would be identically 1 on the infinite set of even times and therefore everywhere by the zero bound, contradicting its value -1 at odd times. This control shows the need for the stated sufficient threshold; it does not assert failure of every particular double-shear map outside it.

Pointwise identity on the residue field is weaker than coefficientwise near-identity. For example $x\mapsto x^p$ induces the identity on $\mathbb F_p$, but its difference from $x$ has unit coefficients and fails (6). The proof never substitutes this weaker condition. Finite residue cycles, analytic time interpolation, and genuine periodic points are three different objects. Prime-power quotient levels carry local arithmetic but do not label the set of rational primes by primitive source orbits or produce logarithmic prime lengths.

## Route-A boundary and remaining risks

The proposed strict tuple is $(A0\_WEAK\_ARITHMETIC\_RELATION,A1\_WEAK,A2\_FAIL,A3\_FAIL,A4\_FORMAL\_HINT)$. Local valuation arithmetic is intrinsic; the complete cycle and stability ledger is source-only. All nine target/Route-B claim flags and `route_b_invocation_allowed` are false. The exact firewall is `NO_BAD_EULER_OR_ROOT_NUMBER`.

Proof risks to review explicitly are the coefficient/value distinction in §3, strictness at $p=2$, radius preservation before replacing the basepoint, finite-level lift independence, and the simultaneous-equation zero-set quantifiers. The universal statements are proved above; finite exact tests audit formulas and implementations but are not proofs of these infinite statements. No external or human peer review is claimed.
