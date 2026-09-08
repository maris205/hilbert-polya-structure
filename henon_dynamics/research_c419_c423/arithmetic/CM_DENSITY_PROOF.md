# Proof package: the frozen CM density conjecture

## Claim

Fix $D\in\mathbb Q^\times$, represented by its unique nonzero
fourth-power-free integer. For each prime $p\nmid 2D$, let
$$
\phi_D(x)=\frac{(x^2+D)^2}{4x(x^2-D)},\qquad
\rho_D(p)=\frac{\#\operatorname{Per}(\phi_D,\mathbb P^1(\mathbb F_p))}{p+1}.
$$
The projective rational map includes infinity and every finite pole. Its clock
is one iterate of $\phi_D$. Put
$$
\mathcal P_D(X)=\{p\le X:p\text{ prime},\ p\nmid2D\},\qquad
\mu_{D,X}=\frac1{\#\mathcal P_D(X)}\sum_{p\in\mathcal P_D(X)}\delta_{\rho_D(p)}.
$$
Here $\delta_t$ is unit mass at $t$, and the expression is used once its
denominator is positive. Define the finite positive measures
$$
I=\sum_{k=2}^{\infty}2^{-k}\delta_{2^{-k}},\qquad
S=\sum_{k=3}^{\infty}2^{1-k}\delta_{s_k},\qquad
s_k=\frac18+2^{-k-1}.
$$
The frozen conjecture, without changing its parameter quantifier, asserts
weak convergence on $[0,1]$ to
$$
\mu_D=\begin{cases}
I+S,& D\in\mathbb Q^{\times2}\cup-\mathbb Q^{\times2},\\
I+S-\frac14\delta_{3/16}+\frac14\delta_{1/2},
  &D\in2\mathbb Q^{\times2}\cup-2\mathbb Q^{\times2},\\
I+\frac12S+\frac14\delta_{1/2},&\text{otherwise}.
\end{cases}
$$
The corresponding prime means are $1/6$, $47/192$, and $1/4$.

## Status

**PROVABLE AS STATED**, using the explicitly imported classical inputs below.
This is an author-side bounded proof, not independent referee certification.
The statement is retained unchanged from the frozen conjecture. It is a short
classical specialization, and the author recommends **not counting it as a
substantial independent paper** in the present batch.

## Assumptions and imported results

1. The parameter $D$ is fixed before $X\to\infty$. No assertion is uniform
   in growing $D$, its height, or its bad-prime set.
2. Bell et al., *Density of Periodic Points for Lattès maps over Finite
   Fields*, Theorem 1.2 of the accessed 2021 preprint, supplies the exact
   finite-field density and its Hasse error bound. This result is imported
   in full, not a contribution of this note.
3. The base CM calculation is imported from local C382, Steps 1–3 of its
   [proved package](../../henon_cm_elliptic_frobenius_phase_zeta_route_a/proof/ANALYTIC_PROOF.md):
   at $p\equiv1\pmod4$, the two Frobenius eigenvalues for
   $E_1:y^2=x^3-x$ are the primary Gaussian generators $\pi,\bar\pi$ of
   the prime ideals above $p$, characterized by
   $\pi\equiv1\pmod{(1+i)^3}$. Thus
   $\#E_1(\mathbb F_p)=N(\pi-1)$ and its quadratic twist has order
   $N(\pi+1)$. C382 and its classical CM dependencies own this input.
4. Global class-field existence and reciprocity identify a ray class group
   with the Galois group of its ray class field, unramified away from the
   modulus. See Milne, *Class Field Theory*, v4.03, V.3.5–3.8.
5. The number-field Chebotarev theorem is used in its **natural-density**
   form for each fixed finite extension. Milne's displayed density theorem
   is stated for Dirichlet density; it is not silently substituted for
   natural density. The stronger number-field form is explicitly recorded
   in Sutherland, MIT 18.785 (2021), Remark 28.12, following Theorem 28.9.
   No effective bound uniform in the layer is invoked.

Primary URLs, accessed versions, and limits are in `SOURCE_AUDIT.md`.

## Notation

$K=\mathbb Q(i)$, $\mathcal O=\mathbb Z[i]$, $\lambda=1+i$,
$N(a+bi)=a^2+b^2$, and $v_\lambda(\lambda)=1$.
For positive integers, $v_2$ is the ordinary 2-adic valuation and
$\operatorname{odd}(n)=n/2^{v_2(n)}$. Since $2=-i\lambda^2$,
$v_2(N(\alpha))=v_\lambda(\alpha)$ for nonzero $\alpha\in\mathcal O$.
For $N\ge3$, $R_N$ is the ray class field of $K$ for modulus
$(\lambda^N)$. The letter $N$ indexing this field is not the norm symbol
when it appears as a subscript. Let $L_D=K(\sqrt D)$.

## Proof strategy and dependency map

1. The imported finite-field count reduces the observable to the two group
   orders; elementary doubling and quadratic twisting collapse all quartic
   twists to one quadratic character at split primes.
2. The imported C382 trace determines one Gaussian valuation shell and
   fixes the other valuation at two.
3. Ray class groups count each finite shell. The intersections
   $L_D\cap R_N$ determine all dependence on $D$.
4. Explicit tail densities justify the infinite-shell limit after the
   fixed-layer prime limits. Geometric sums then verify mass and mean.

## Proof

### Step 1. Domain and the imported finite-field formula

For $p\nmid2D$, the homogeneous formula is
$$
[X:Z]\longmapsto[(X^2+DZ^2)^2:4XZ(X^2-DZ^2)].
$$
Its two homogeneous coordinates have no common zero: at $X=0$ or $Z=0$
the first is nonzero, while a common zero with $XZ\ne0$ would require
$X^2=DZ^2=-DZ^2$, contrary to $p\nmid2D$. Hence it is an everywhere
defined degree-four morphism. Infinity is fixed and finite poles map to it.
The map is the $x$-coordinate quotient of doubling on
$E_D:y^2=x^3-Dx$, as follows from the tangent-and-chord doubling formula.

Write $a_D(p)=p+1-\#E_D(\mathbb F_p)$ and
$n_-=p+1-a_D(p)$, $n_+=p+1+a_D(p)$, the orders of the curve and a
quadratic twist. Bell's formula at multiplier two reads
$$
\rho_D(p)=\frac{\operatorname{odd}(n_-)+\operatorname{odd}(n_+)}{2(p+1)}.
\tag{1}
$$
In particular the expression is invariant under swapping the two orders.
If $u_\pm=v_2(n_\pm)$, that theorem also gives
$$
\left|\rho_D(p)-\frac12(2^{-u_-}+2^{-u_+})\right|
 <\frac1{\sqrt p+1/\sqrt p}.
\tag{2}
$$
All terms count ordinary periodic points, not multiplicities or weighted
traces. Formula (1), including its branch correction, is wholly imported.

### Step 2. The elementary twist collapse

At $p\equiv3\pmod4$, the character sum for $E_D$ is zero: under
$x\mapsto-x$, the polynomial $x^3-Dx$ changes sign, and the quadratic
character of $-1$ is $-1$. Thus $a_D(p)=0$ and
$$
\rho_D(p)=2^{-v_2(p+1)}\quad(p\equiv3\pmod4).
\tag{3}
$$
This includes every allowed inert prime and every nonzero $D\bmod p$.

Now let $p\equiv1\pmod4$ and let $\chi_p$ be its quadratic character.
If $\chi_p(D)=1$, write $D=t^2$ in $\mathbb F_p^\times$. Substitution
$x=tX$ in the character sum multiplies the base sum by $\chi_p(t^3)$.
Consequently $a_D(p)=\chi_p(t)a_1(p)$. The unordered order pair is the
base pair, so
$$
\rho_D(p)=\rho_1(p)\quad\text{if }\chi_p(D)=1.
\tag{4}
$$

If $\chi_p(D)=-1$, the only nonzero rational point of order two on $E_D$
is $(0,0)$, because the other two would have $x^2=D$. There is no rational
point of order four. Such a point would double to $(0,0)$, and the numerator
in the doubling formula would require $x^2=-D$; this is impossible because
$\chi_p(-1)=1$ and $\chi_p(D)=-1$. A finite abelian group with exactly
one nonidentity element of order two has cyclic 2-primary part. If its
order were divisible by four, that part would contain an element of order
four. It follows that $v_2(\#E_D(\mathbb F_p))=1$.

A quadratic twist of this curve has equation $y^2=x^3-t^2Dx$ for a
nonsquare $t$, so its coefficient still has quadratic character $-1$.
The same argument gives valuation one for its order. Formula (1) yields
$$
\rho_D(p)=\frac12\quad\text{if }p\equiv1\pmod4,\ \chi_p(D)=-1.
\tag{5}
$$
This collapse needs no claim about a quartic Galois representation.

### Step 3. Base split valuations and the first shell

Use the C382 primary generator $\pi=a+bi$, with $a$ odd, $b$ even,
$a+b\equiv1\pmod4$ and $a^2+b^2=p$. Set
$$
k(p)=v_\lambda(\pi-1)\ge3.
$$
The two conjugate generators give the same value, since conjugation
preserves the prime ideal $(\lambda)$. Since
$\pi+1=2+(\pi-1)$ and $v_\lambda(2)=2<k(p)$, the other valuation is
$v_\lambda(\pi+1)=2$. The two group-order valuations are therefore
$\{k(p),2\}$. Define $s_k=1/8+2^{-k-1}$ as above. Equation (2) gives
$$
|\rho_1(p)-s_{k(p)}|<p^{-1/2}.
\tag{6}
$$

Moreover,
$$
k(p)=3\quad\Longleftrightarrow\quad p\equiv5\pmod8.
\tag{7}
$$
Indeed, when $p\equiv5\pmod8$, one has $b\equiv2\pmod4$ and
$a\equiv3\pmod4$. Hence $(a-1)^2+b^2\equiv8\pmod{16}$.
When $p\equiv1\pmod8$, one has $b\equiv0\pmod4$ and
$a\equiv1\pmod4$, so the same norm is divisible by sixteen.
These are the two possible split congruence classes.

### Step 4. Every finite Gaussian shell has an exact prime density

The Gaussian integers have class number one and unit group
$\{1,-1,i,-i\}$. Its four units give the four distinct invertible classes
modulo $\lambda^3$, whose unit group has size four. Every ideal prime to
$\lambda$ therefore has a unique generator congruent to one modulo
$\lambda^3$. The ray class group for $\lambda^N$, $N\ge3$, is
$$
\operatorname{Cl}_{\lambda^N}(K)
 \simeq (\mathcal O/\lambda^N)^\times/\mathcal O^\times
 \simeq (1+\lambda^3\mathcal O)/(1+\lambda^N\mathcal O).
\tag{8}
$$
The last expression means the quotient of the corresponding local unit
groups, or equivalently their finite residue images. Its order is
$2^{N-3}$, since $\#(\mathcal O/\lambda^N)^\times=2^{N-1}$.
Consequently $[R_N:K]=2^{N-3}$.

For $k\ge3$, the shell $v_\lambda(\pi-1)=k$ consists of exactly one
primary residue class modulo $\lambda^{k+1}$, namely
$1+\lambda^k u$ with $u$ the unique nonzero residue modulo $\lambda$.
Chebotarev in the fixed abelian extension $R_{k+1}/K$ gives natural
density $2^{2-k}$ among prime ideals of $K$.

Prime ideals of degree two over $\mathbb Q$ have norm $p^2$ and contribute
$O(\sqrt X)$ to a norm count up to $X$; they have zero natural density.
Every split rational prime contributes two conjugate degree-one prime
ideals. The shell condition is conjugation invariant. Therefore the
corresponding density among rational primes is
$$
d\{p\equiv1\pmod4:k(p)=k\}=2^{1-k}.
\tag{9}
$$
The factor of two is required: the sum in (9) is $1/2$, not one.
Likewise, for $M\ge3$,
$$
d\{p\equiv1\pmod4:k(p)>M\}=2^{1-M},
\tag{10}
$$
because this is the identity ray class modulo $\lambda^{M+1}$.

### Step 5. Complete quadratic intersection classification, at every layer

For all $N\ge3$,
$$
L_D\cap R_N=\begin{cases}
K,&D\in\mathbb Q^{\times2}\cup-\mathbb Q^{\times2},\\
K,&D\in2\mathbb Q^{\times2}\cup-2\mathbb Q^{\times2},\ N=3,\\
K(\sqrt2),&D\in2\mathbb Q^{\times2}\cup-2\mathbb Q^{\times2},\ N\ge4,\\
K,&\text{all other }D.
\end{cases}
\tag{11}
$$
In the first case $L_D=K$. To see that these are exactly the rational
square classes becoming squares in $K$, square $r+si\in K$: its square
is rational only when $rs=0$, giving a positive or negative rational square.

In the second case $L_D=K(\sqrt2)$ and has degree two over $K$.
Its Artin character at an odd ideal of norm $n$ is the quadratic character
$(2/n)$ inherited from $\mathbb Q(\sqrt2)/\mathbb Q$; for a prime ideal
this follows from Frobenius on $\sqrt2$, and it extends multiplicatively
to ideals. It suffices to check integral ray generators: a fractional
generator which is a local unit at $(\lambda)$ can be multiplied by an
odd rational integer congruent to one modulo four that clears its
denominators. Both that integer and the resulting integral generator
are then congruent to one modulo $\lambda^4$. If an integral principal
ideal has generator
$\alpha\equiv1\pmod{\lambda^4}$, then $\alpha=a+bi$ satisfies
$a\equiv1\pmod4$, $b\equiv0\pmod4$, and $N(\alpha)\equiv1\pmod8$.
Its Artin character is therefore one. By reciprocity and the ray class
correspondence, $K(\sqrt2)\subseteq R_4$. Since $[R_4:K]=2$, equality
holds. The nesting of ray fields proves the assertion for $N\ge4$;
$R_3=K$ proves the remaining layer.

For the last case, replace $D$ by the squarefree integer $d$ in its
rational square class. At least one odd rational prime $q$ divides $d$;
otherwise its square class would be one of $1,-1,2,-2$. The extension
$K/\mathbb Q$ is unramified at $q$, so every prime $\mathfrak q$ above
$q$ has $v_{\mathfrak q}(d)=1$. The polynomial $T^2-d$ is Eisenstein
over $K_{\mathfrak q}$, proving that $K(\sqrt d)/K$ ramifies there.
Each $R_N/K$ is unramified outside $(\lambda)$. Since $[L_D:K]=2$, a
nontrivial intersection would be all of $L_D$, contradicting its odd-prime
ramification. This proves (11), for every finite layer, without assuming
independence from a finite sample.

When the last case holds, the two finite Galois extensions are linearly
disjoint, so
$$
\operatorname{Gal}(R_NL_D/K)
 \simeq\operatorname{Gal}(R_N/K)\times\operatorname{Gal}(L_D/K).
\tag{12}
$$
Chebotarev in this fixed compositum implies that each Gaussian shell splits
equally between $\chi_p(D)=1$ and $\chi_p(D)=-1$. In rational-prime
density, each half of the $k$-th shell has mass $2^{-k}$. In particular
the split nonresidue primes have total density $1/4$; this total also
follows directly by applying Chebotarev to $L_D/\mathbb Q$.

For $D=\pm\text{square}$, the character is always one on split primes.
For $D=\pm2\cdot\text{square}$, quadratic reciprocity gives
$\chi_p(D)=(2/p)$, which is negative exactly at $p\equiv5\pmod8$ in
the split chamber. By (7), this is exactly shell three. Thus its density
is $1/4$, and no other shell changes. The two exceptional parameter sets
are disjoint because $2$ is not a rational square.

### Step 6. Inert masses, tail control, and the weak limit

For $k\ge2$, the inert condition $v_2(p+1)=k$ is the single odd residue
class $p\equiv2^k-1\pmod{2^{k+1}}$. The prime number theorem in
arithmetic progressions, equivalently fixed cyclotomic Chebotarev, gives
its rational-prime density $2^{-k}$. For $M\ge3$ the inert tail
$v_2(p+1)>M$ is the class $p\equiv-1\pmod{2^{M+1}}$ and has density
$2^{-M}$.

Define $\eta_D(p)$ by (3) on inert primes, by $1/2$ on split nonresidue
primes, and by $s_{k(p)}$ on split residue primes. Equations (3)–(6) give
$$
|\rho_D(p)-\eta_D(p)|\le p^{-1/2}.
\tag{13}
$$
Let $f$ be any continuous function on $[0,1]$. Its uniform continuity
and (13) imply that the average of
$f(\rho_D(p))-f(\eta_D(p))$ over $\mathcal P_D(X)$ tends to zero: fix
the continuity tolerance, discard finitely many small primes, and bound
their contribution by their vanishing relative cardinality.

Fix $M\ge3$. Keep all split nonresidue primes, all inert shells
$k\le M$, and all split residue shells $k\le M$. Their finitely many
category frequencies have the exact natural-density limits proved above.
The omitted primes lie in the union of the inert tail and the base split
tail. Equations (10) and the inert congruence therefore give
$$
\limsup_{X\to\infty}
\frac{\#\{\text{omitted }p\in\mathcal P_D(X)\}}
     {\#\mathcal P_D(X)}
\le 2^{-M}+2^{1-M}=3\cdot2^{-M}.
\tag{14}
$$
Removing the finite set $p\mid2D$ changes none of these limits. The same
bound applies to the mass omitted from the claimed measure. Thus the
limsup error between the two full integrals of $f$ is at most
$6\|f\|_\infty2^{-M}$, after the vanishing error (13) is removed.
Letting $M\to\infty$ proves weak convergence. The limit order is
**fixed $D,M$; then $X\to\infty$; then $M\to\infty$**. No interchange
based on a layer-uniform Chebotarev estimate has occurred.

Applying (4), (5), (9), and (11) to these categories gives exactly the
three measures in the Claim. The split atoms describe the weak limit;
they do not assert that the finite-prime fractions equal $s_k$ exactly.

### Step 7. Independent mass and mean checks

Direct geometric summation gives
$$
I([0,1])=\sum_{k\ge2}2^{-k}=\frac12,\qquad
S([0,1])=\sum_{k\ge3}2^{1-k}=\frac12.
$$
The second case removes exactly the positive shell-three mass already in
$S$, so all three displayed measures are positive and have total mass one.
Their first-moment building blocks are
$$
\int t\,dI=\sum_{k\ge2}4^{-k}=\frac1{12},
\qquad
\int t\,dS=\frac1{16}+\sum_{k\ge3}4^{-k}
 =\frac1{16}+\frac1{48}=\frac1{12}.
$$
The three means are consequently
$$
\frac16,\qquad
\frac16-\frac14\frac3{16}+\frac14\frac12=\frac{47}{192},\qquad
\frac1{12}+\frac12\frac1{12}+\frac14\frac12=\frac14.
$$
Since $f(t)=t$ is bounded and continuous on $[0,1]$, weak convergence
establishes the actual prime-mean limits, not just formal moments.
The only accumulation points of the infinite atom families are $0$ and
$1/8$. There is no atom at zero; the mass at $1/8$ is precisely the inert
$k=3$ mass $1/8$, with no additional limiting-shell mass, by (14).
The hypotheses exclude $D=0$, where the good elliptic model and degree-four
formula degenerate. Changing representatives by a rational fourth power
gives a rational linear conjugacy and modifies at most finitely many
reduction primes, so the chosen normalization does not alter the law. ∎

## Corrections or missing assumptions

None to the frozen fixed-parameter weak-law claim. A growing-parameter
uniform version is not asserted and does not follow. Natural density was
kept distinct from Milne's displayed Dirichlet-density theorem.

## Residual contribution after ownership subtraction

Bell owns (1)–(2), and C382 owns the primary Frobenius input of Step 3.
Class field theory owns finite-level existence and equidistribution. What
remains is the elementary twist collapse, one rank-one residue-shell count,
the quadratic ramification intersection, and a geometrically summable tail.
These fit into a short corollary proof once the inherited facts are stated.
Writing out their quantifiers and boundaries makes a reliable research note,
but does not create a new dynamical carrier or a substantial independent
arithmetic theorem by itself. The three means are not three contributions.

## Open risks and disposition

The proof requires nonauthor checking before any reuse. The bounded source
search did not locate this exact displayed weak law, but supplies no worldwide
priority guarantee. No new theorem about full functional graphs, individual
cycle lengths, bad-prime Euler factors, or a target determinant is proved.
Author disposition: **retain as an unnumbered corollary note; reject as a
five-paper slot under the current substantive-increment rule**.
