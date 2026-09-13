# Paper30 proof package: coefficient-uniform same-word three-point mixing

Date: 2026-09-06. Author proof V1; not a manuscript, selection decision,
Route evaluation, numerical certificate, or substantive-page acceptance.

## Claim

For every integer $d\geq2$ there is $\delta_d>0$ such that the following
holds for **every** prime $p\geq16d^2$ and **every** monic polynomial
$P\in\mathbb F_p[t]$ of degree $d$. Put
$$
H_j(x,y)=(P(x)+j-y,x),\quad j=0,1,
\qquad
\Omega_p=\operatorname{Conf}_3(\mathbb F_p^2).
$$
Here configurations are ordered triples of pairwise distinct points.
Each map acts on all three points simultaneously. Choose independently
at each time a map with law
$$
\mu_P=\tfrac12\delta_{\mathrm{id}}+
\tfrac18(\delta_{H_0}+\delta_{H_0^{-1}}+
\delta_{H_1}+\delta_{H_1^{-1}}).
\tag{1}
$$
Let $M_Pf(\mathbf z)=\mathbb E_{g\sim\mu_P}f(g\mathbf z)$.
With normalized counting measure on $\Omega_p$, the claim is
$$
\langle f,(I-M_P)f\rangle\geq\delta_d\operatorname{Var}(f)
\quad (f:\Omega_p\longrightarrow\mathbb C).
\tag{2}
$$
In particular this chain is irreducible, has uniform stationary measure
$u_p$, and, from every initial configuration, satisfies
$$
\|\mathcal L(Z_n)-u_p\|_{\mathrm{TV}}
\leq\tfrac12p^3e^{-\delta_dn}.
\tag{3}
$$
For any fixed $0<\varepsilon<1$, its worst-start total-variation mixing
time is $\Theta_{d,\varepsilon}(\log p)$ as $p\to\infty$, uniformly in
the coefficients of $P$.

## Status

`PROVABLE AS STATED` at author level. The main affine/word comparison is
being independently audited in a separate file. The quadratic quotient
lemma has an already completed independent derivation; the all-degree
quotient is being independently derived and checked. This status does not
prejudge those reports or the later novelty/value/capacity gate.

## Assumptions and boundaries

- The degree is fixed before $\delta_d$ is chosen; there is no claim of a
  gap uniform as $d$ tends to infinity.
- All lower coefficients may vary freely with $p$; no bounded integer
  lift for those coefficients is assumed.
- The field is prime and $p\geq16d^2$, hence $p>d$. Extension fields and
  the excluded small characteristics are not asserted.
- The walk is precisely the lazy symmetric law (1). It is not a
  forward-only walk, and the three coordinates do not use independent words.
- This is a Schreier/configuration-space result, not a Cayley expansion
  theorem for the full permutation group, and not a theorem for arbitrarily
  many simultaneous points.

## Notation

All $L^2$ norms and expectations below use uniform probability measure
on the finite space in question. For a permutation $T$ set
$$
\mathcal E_T(f)=\tfrac12\|f\circ T-f\|_2^2.
$$
For a symmetric probability law $\nu$ on permutations, set
$\mathcal D_\nu(f)=\langle f,(I-M_\nu)f\rangle$.
The elementary change of variables $z\mapsto Tz$ gives
$\|f\circ T^{-1}-f\|_2=\|f\circ T-f\|_2$, and therefore
$$
\mathcal D_{\mu_P}(f)=\tfrac18\sum_{j=0}^1
\|f\circ H_j-f\|_2^2.
\tag{4}
$$
Write $\mathscr A_p=\operatorname{ASL}_2(\mathbb F_p)$ and let $E$ be
orthogonal projection onto its invariant functions on $\Omega_p$.
Thus $Ef$ averages $f$ over each special-affine orbit, with its actual
uniform orbit measure.

## Proof strategy and dependency map

1. A translation conjugacy centers $P$ without changing the coefficient
   quantifiers or the random-walk spectrum.
2. Finite-difference words in the two Hénon generators produce four fixed
   affine generators, with word lengths depending only on $d$.
3. Bourgain–Gamburd's fixed-integer-generator theorem and
   Lindenstrauss–Varjú's affine theorem provide an orbit-internal gap.
4. An independent area calculation controls the special-affine orbit
   quotient. For $d\geq3$, the additive character bound and a deleted-zero
   estimate control its noncollinear block; a collinear escape estimate
   controls the remaining block. For $d=2$, a cubic-fiber count replaces
   the character-in-the-base-coordinate argument.
5. An orthogonal decomposition and energy comparison combine the two
   controls without assuming that the quotient kernel is reversible.

The linear/affine expansion theorems, the classical additive Weil bound,
finite-difference principle, and general energy-comparison principle are
prior inputs, not claimed as new results here.

## Proof

### Step 1. Centering is a conjugacy, not a long word

Write $a_{d-1}$ for the coefficient of $t^{d-1}$ in $P$ and put
$s=-a_{d-1}/d\in\mathbb F_p$. For $C_s(x,y)=(x+s,y+s)$ direct substitution
gives
$$
C_s^{-1}H_jC_s(x,y)=(Q(x)+j-y,x),\qquad
Q(t)=P(t+s)-2s.
\tag{5}
$$
$Q$ is monic of degree $d$ and its coefficient of $t^{d-1}$ is zero.
The same $C_s$ works for both values of $j$ and for their inverses.
It permutes $\Omega_p$ and preserves its uniform measure; hence the two
Markov operators are unitarily conjugate. No expression of $C_s$ as a
bounded word is required. It suffices to prove (2) for every centered $Q$.
For Steps 2–5 write $P$ for this centered polynomial.

### Step 2. Bounded extraction of coefficient-independent affine maps

Compose maps right to left and put $H=H_0$. Direct use of
$H_j^{-1}(x,y)=(y,P(y)+j-x)$ gives
$$
X=H_1H_0^{-1}=(x+1,y),\qquad
Y=H_1^{-1}H_0=(x,y+1).
\tag{6}
$$
Both words have length at most two in $H_0^{\pm1},H_1^{\pm1}$.
For $\Delta R(t)=R(t+1)-R(t)$ define
$$
S_1=Y^{-1}HXH^{-1},\qquad
S_{r+1}=Y^{-1}S_rYS_r^{-1}.
\tag{7}
$$
Substitution in the first identity gives $S_1(x,y)=(x+\Delta P(y),y)$;
substitution in the second sends a shear $x\mapsto x+R(y)$ to the shear
$x\mapsto x+\Delta R(y)$. Thus
$$
S_r(x,y)=(x+\Delta^rP(y),y),\qquad
\ell_r\leq10\,2^{r-1}-4.
\tag{8}
$$
Indeed $\ell_1\leq6$ and $\ell_{r+1}\leq2\ell_r+4$ prove the bound by
induction. Since $P$ is centered, all its terms below degree $d-1$ vanish
after $d-1$ differences, and
$$
\Delta^{d-1}P(t)=d!t+c_d,\qquad c_d=\frac{d!(d-1)}2\in\mathbb Z.
\tag{9}
$$
For completeness, the coefficient of $t$ in the difference of $t^d$ is
$d!$. Its constant term counts surjections from a $d$-element set onto a
$(d-1)$-element set: choose the unique pair in one fiber and biject the
$d-1$ fibers, giving $\binom d2(d-1)!=d!(d-1)/2$. This is also the
inclusion-exclusion formula for $\Delta^{d-1}t^d$ at zero. The identity
is integral and hence reduces modulo every prime under consideration.

Set $k=d!$, and interpret $X^{-c_d}$ by that fixed nonnegative integer
exponent, not by a coefficient-dependent representative modulo $p$.
Then
$$
U=X^{-c_d}S_{d-1}=(x+ky,y),\qquad
V=H^{-1}U^{-1}H=(x,y+kx).
\tag{10}
$$
Their lengths are bounded, respectively, by
$$
L_d=10\,2^{d-2}-4+2c_d,\qquad L_d+2.
\tag{11}
$$
In the second identity of (10), the $P(x)$ terms cancel exactly. All four
maps $X,Y,U,V$ are consequently independent of the remaining coefficients.

### Step 3. A uniform affine gap and transfer to any orbit representation

The fixed integer matrices
$$
U_k=\begin{pmatrix}1&k\\0&1\end{pmatrix},\qquad
V_k=\begin{pmatrix}1&0\\k&1\end{pmatrix}
\tag{12}
$$
generate a non-elementary subgroup of $\operatorname{SL}_2(\mathbb Z)$.
One verification uses the two cones $A=\{|x|>|y|\}$ and
$B=\{|y|>|x|\}$ in $\mathbb R^2\setminus\{0\}$. Since $k\geq2$, every
nonzero power of $U_k$ takes $B$ into $A$, and every nonzero power of
$V_k$ takes $A$ into $B$. The inequalities follow, for example, from
$|x+nky|\geq2|y|-|x|>|y|$ on $B$. A reduced alternating word with the
same generator at its two ends takes the opposite cone into that
generator's cone, so is not the identity. A word with different end
generators can be conjugated by a nonzero power of its first generator,
avoiding cancellation of its first exponent, to have matching end
generators. This proves freeness. If a finite-index subgroup were
solvable it would contain positive powers of both generators; the same
cone proof makes those powers a free nonabelian pair, impossible inside
a solvable group. This verifies the non-elementary condition.

For every $p>d$, $k\neq0$ in $\mathbb F_p$. Powers of $U_k$ supply every
upper elementary unipotent matrix and powers of $V_k$ every lower one.
These generate $\operatorname{SL}_2(\mathbb F_p)$ by row elimination
(the interchange and diagonal matrices are also products of these
elementary matrices). Thus the Cayley graph is connected for every such
prime, not just for an unspecified asymptotic set.

Bourgain–Gamburd's Theorem 1 supplies a positive gap for the symmetric
walk on this fixed pair as $p$ tends to infinity. The finitely many
remaining primes $p>d$ have positive top spectral gaps by connectedness;
taking the minimum gives $\epsilon_d>0$ for every $p>d$. This is a
dependence on $d$ alone, not an effective numerical value claimed here.
[Bourgain–Gamburd, Annals 167 (2008), Theorem 1, p.626](https://annals.math.princeton.edu/wp-content/uploads/annals-v167-n2-p07.pdf).

On $\mathscr A_p$ use the symmetric affine law
$$
\nu_d=\tfrac12\delta_{\mathrm{id}}+
\tfrac1{16}\sum_{T\in\{X,Y,U,V\}}(\delta_T+\delta_{T^{-1}}).
\tag{13}
$$
Its linear projection is $\tfrac34\delta_I+\tfrac14\sigma_d$, where
$\sigma_d$ is uniform on $U_k^{\pm1},V_k^{\pm1}$. This projected operator
is positive semidefinite since its eigenvalues are at least $1/2$, and
its norm gap off the constants is at least $\epsilon_d/4$.
For the action of (13) on a single point, its maximum point-to-point
transition probability is $\alpha=3/4$. Indeed, for a transition from a
point to itself, all four translations $X^{\pm1},Y^{\pm1}$ fail to fix
the point, removing mass $1/4$; for a transition to a different point,
the identity mass $1/2$ is absent. At the origin the four linear shears
fix the point, so the bound $3/4$ is attained.

Theorem 2 of Lindenstrauss–Varjú, in affine dimension two, therefore gives
a regular-representation gap at least
$$
\gamma_d=c_2\min\{\epsilon_d/4,1/4\}>0,
\tag{14}
$$
where $c_2>0$ depends only on the affine dimension. Here the theorem
uses the maximum point transition probability, not merely the largest
atom of the law on the group. Its hypotheses hold for the exact law (13).
[Lindenstrauss–Varjú, AFST 25 (2016), Theorem 2, p.976](https://www.numdam.org/item/AFST_2016_6_25_5_969_0.pdf).

Every irreducible unitary representation of a finite group occurs in its
regular representation. Decomposing the permutation representation on
$\Omega_p$ into irreducibles shows that the same gap applies on the
orthogonal complement of **all** affine invariants, including when there
are many affine orbits. Thus
$$
\gamma_d\|f-Ef\|_2^2\leq\mathcal D_{\nu_d}(f).
\tag{15}
$$
This does not assume affine transitivity on triples.

For a word $W=T_\ell\cdots T_1$ in the four Hénon letters, telescope its
successive point images. Cauchy–Schwarz and invariance of counting measure
under every intermediate permutation give
$$
\|f\circ W-f\|_2^2
\leq\ell\sum_{i=1}^{\ell}\|f\circ T_i-f\|_2^2
\leq\ell^2\sum_{j=0}^1\|f\circ H_j-f\|_2^2.
\tag{16}
$$
Using (4), (11), and
$\mathcal D_{\nu_d}=\tfrac1{16}\sum_{T=X,Y,U,V}\|f\circ T-f\|_2^2$,
we obtain
$$
\mathcal D_{\nu_d}(f)\leq C_d\mathcal D_{\mu_P}(f),\qquad
C_d=\frac{8+L_d^2+(L_d+2)^2}{2}.
\tag{17}
$$

### Step 4. The special-affine quotient and its actual stationary weights

Write $z_0=(x,y)$, $z_1-z_0=(u,r)$, $z_2-z_0=(v,s)$ and
$\Delta=us-vr$. The affine orbits are exactly:

- $\mathcal N_\Delta$ for each $\Delta\neq0$, the noncollinear triples
  of that fixed oriented area;
- $\mathcal C_a$ for each $a\neq0,1$, the collinear triples with
  $z_2-z_0=a(z_1-z_0)$.

For nonzero determinant, the transition between two difference frames
of that determinant has determinant one. For collinear triples,
$\operatorname{SL}_2$ is transitive on nonzero difference vectors and
preserves the ratio $a$. These observations prove both directions of
the classification. Counting base points and frames gives
$$
N_p=|\Omega_p|=p^2(p^2-1)(p^2-2),\quad
\pi_\Delta=\frac{p}{p^2-2},\quad \pi_a=\frac1{p^2-2}.
\tag{18}
$$
Let $K_{ij}$ be the probability that $H$ sends a uniform point in affine
orbit $i$ to orbit $j$. Since $H$ is a permutation, the weights in (18)
are stationary: $\sum_i\pi_iK_{ij}=\pi_j$. No reversibility is needed.
For an affine-invariant function $g$, with orbit values $g_i$,
$$
\mathcal E_H(g)=\tfrac12\sum_{i,j}\pi_iK_{ij}|g_j-g_i|^2.
\tag{19}
$$
Direct determinant expansion, with the above orientation, gives
$$
\Delta'=\Delta+F_P(x,u,v),\qquad
F_P=v(P(x+u)-P(x))-u(P(x+v)-P(x)).
\tag{20}
$$
In a uniform noncollinear orbit, $x$ is uniform on $\mathbb F_p$,
independently of $(u,v)$, which is uniform on
$\mathbb F_p^2\setminus\{(0,0)\}$. To check the latter assertion, each
nonzero $(u,v)$ has exactly $p$ solutions of $us-vr=\Delta$ and the same
$p^2$ choices of the base point.

Put $\mu_N=(p-1)^{-1}\sum_{\Delta\neq0}g_\Delta$ and
$$
V_N=\sum_{\Delta\neq0}\pi_\Delta|g_\Delta-\mu_N|^2,\qquad
V_C=\sum_a\pi_a|g_a-\mu_N|^2.
\tag{21}
$$
The minimizing property of the global mean gives
$\operatorname{Var}(g)\leq V_N+V_C$.

### Step 5. Noncollinear mixing for degrees at least three

Assume $d\geq3$. On the good set $uv(u-v)\neq0$, (20), as a polynomial
in $x$, has exact degree $d-2$ and leading coefficient
$\binom d2uv(u-v)\neq0$. The top $x^{d-1}$ coefficients cancel, and
terms of $P$ of degree below $d$ contribute at most degree $d-3$.
The bad set in the nonzero $(u,v)$ domain consists of three punctured
lines and has probability $b_p=3/(p+1)$; on that set $F_P=0$ identically.

Let $\eta$ be the distribution of the increment $F_P(x,u,v)$.
The additive Weil estimate for a polynomial of degree $n<p$ and a
nontrivial additive character is $(n-1)\sqrt p$. Applied conditionally
on each good $(u,v)$, with $n=d-2$, it gives, for all $\xi\neq0$,
$$
|\widehat\eta(\xi)|\leq r_{p,d}:=\frac{d-3}{\sqrt p}+\frac3{p+1}.
\tag{22}
$$
For degree one the relevant complete character sum is zero, consistent
with (22). Independently, a nonconstant polynomial of degree $d-2$ has
at most $d-2$ roots above any value, so
$$
\max_t\eta(t)\leq m_{p,d}:=\frac{d-2}{p}+\frac3{p+1}.
\tag{23}
$$
The cited character bound, including the condition that the degree is
not divisible by the characteristic, is stated in the research paper
[Wan–Wang, “Index bounds for character sums of polynomials over finite fields,”
arXiv:1507.00988, p.1, equation (1)](https://arxiv.org/pdf/1507.00988).
It is used as a classical theorem, not proved anew or claimed as new here.

Extend $q(\Delta)=g_\Delta-\mu_N$ to all of $\mathbb F_p$ by $q(0)=0$.
Its mean on $\mathbb F_p$ is zero. Finite Fourier orthogonality gives
$$
\frac12\sum_{z,t}\eta(t)|q(z+t)-q(z)|^2
\geq(1-r_{p,d})\sum_z|q(z)|^2.
\tag{24}
$$
Specifically the multiplier on a nonzero character is
$1-\operatorname{Re}\widehat\eta(\xi)$, which is bounded below by
$1-|\widehat\eta(\xi)|$; symmetry of $\eta$ is not assumed. The sums
in (24) use unnormalized counting in $z$, equally on both sides.
Deleting all directed edges with initial or terminal vertex zero
subtracts exactly
$$
\frac12\sum_{z\neq0}(\eta(z)+\eta(-z))|q(z)|^2
\leq m_{p,d}\sum_z|q(z)|^2.
\tag{25}
$$
The self-edge at zero has zero energy. Hence the noncollinear-to-
noncollinear part of (19) is at least
$(1-r_{p,d}-m_{p,d})V_N$.
For $p\geq16d^2$,
$$
r_{p,d}+m_{p,d}
\leq\frac{d-3}{4d}+\frac{d+4}{16d^2}<\frac12.
\tag{26}
$$
For instance the first term is at most $1/4$ and the second at most
$7/144<1/4$ for $d\geq3$. We conclude
$$
V_N\leq2\mathcal E_H(g)\qquad(d\geq3).
\tag{27}
$$

### Step 6. The quadratic noncollinear calculation

For $d=2$, (20) equals $uv(u-v)$, independently of $x$ and of all lower
coefficients. Write $n_t$ for the number of nonzero pairs $(u,v)$ with
$uv(u-v)=t$. Then $n_0=3p-3$. For $t\neq0$, substituting $v=au$ gives
$a(1-a)u^3=t$ with $a\neq0,1$. If $p\equiv2\pmod3$, cubing is bijective
and $n_t=p-2$. If $p\equiv1\pmod3$, a cubic character $\chi$ extended
by zero at zero yields
$$
n_t=p-2+\chi(t)J(\chi^2,\chi^2)+\chi(t)^2J(\chi,\chi).
\tag{28}
$$
Here $J(\alpha,\beta)=\sum_a\alpha(a)\beta(1-a)$.
To justify the needed absolute value without a second Weil input, put
$G(\chi)=\sum_x\chi(x)e^{2\pi ix/p}$. For any nontrivial multiplicative
character $\theta$, substituting $x=ty$ gives
$|G(\theta)|^2=(p-1)-\sum_{t\neq1}\theta(t)=p$.
Grouping $G(\chi)^2$ by $x+y$ gives
$G(\chi)^2=J(\chi,\chi)G(\chi^2)$; the zero-sum fiber vanishes because
$\chi^2$ is nontrivial. Consequently both Jacobi sums in (28) have
absolute value $\sqrt p$. Thus $n_t\geq p-2-2\sqrt p\geq p/2$ for
$p\geq29$. Our threshold $p\geq64$ is stronger.

For all nonzero areas $\Delta,\varepsilon$,
$K_{\Delta\varepsilon}=n_{\varepsilon-\Delta}/(p^2-1)\geq1/(2p)$.
Using the exact common weight $\pi_\Delta$ and the identity
$\sum_{i,j}|g_i-g_j|^2=2(p-1)\sum_i|g_i-\mu_N|^2$ gives
$$
\mathcal E_H(g)\geq\frac{p-1}{2p}V_N\geq\frac13V_N.
\tag{29}
$$
The zero increment uses $n_0$, not the nonzero-fiber formula.

### Step 7. Collinear escape and the uniform quotient bound

In $\mathcal C_a$, the vector $(u,r)$ is uniform nonzero, the base point
is independent uniform, and $(v,s)=a(u,r)$. For $d\geq3$ and $u\neq0$,
the polynomial $F_P(x,u,au)$ has degree $d-2$ and leading coefficient
$\binom d2a(1-a)u^3\neq0$. Since $\mathbb P(u=0)=1/(p+1)$, its actual
escape probability $\rho_a=\sum_{\Delta\neq0}K_{a\Delta}$ satisfies
$$
\rho_a\geq1-\frac1{p+1}-\frac{d-2}{p}\geq\frac12.
\tag{30}
$$
For $d=2$, the exact increment is $a(1-a)u^3$ and
$\rho_a=p/(p+1)\geq1/2$. Let $\rho_*\geq1/2$ be the common lower
bound; equal escape probabilities are not asserted in higher degree.
The inequality $|a+b|^2\leq2|a|^2+2|b|^2$ and stationary inflow give
$$
\begin{aligned}
\rho_*V_C
&\leq\sum_a\pi_a\rho_a|g_a-\mu_N|^2\\
&\leq2\sum_{a,\Delta\neq0}\pi_aK_{a\Delta}|g_a-g_\Delta|^2
+2\sum_{\Delta\neq0}\left(\sum_a\pi_aK_{a\Delta}\right)
|g_\Delta-\mu_N|^2\\
&\leq4\mathcal E_H(g)+2V_N.
\end{aligned}
\tag{31}
$$
Here $\sum_a\pi_aK_{a\Delta}\leq\pi_\Delta$ is an inequality for
stationary inflow from a subset of source orbits, not detailed balance.
Thus $V_C\leq8\mathcal E_H(g)+4V_N$. With (27) we obtain a bound of
$18\mathcal E_H(g)$ on $V_N+V_C$ in degrees at least three; with (29)
we obtain $23\mathcal E_H(g)$ in degree two. In particular, uniformly
over the entire stated class,
$$
\operatorname{Var}(g)\leq24\mathcal E_H(g)
\quad\text{for every affine-invariant }g.
\tag{32}
$$

### Step 8. Combining orbit-internal and quotient energies

For arbitrary $f$, write $g=Ef$ and $h=f-g$. Orthogonality, and the fact
that constants are affine invariant, give
$$
\operatorname{Var}(f)=\operatorname{Var}(g)+\|h\|_2^2,
\qquad
\|h\|_2^2\leq\frac{C_d}{\gamma_d}\mathcal D_{\mu_P}(f).
\tag{33}
$$
Since $H$ is unitary on this $L^2$ space,
$$
\begin{aligned}
\mathcal E_H(g)
&\leq2\mathcal E_H(f)+2\mathcal E_H(h)\\
&\leq2\mathcal E_H(f)+4\|h\|_2^2\\
&\leq8\mathcal D_{\mu_P}(f)+4\|h\|_2^2.
\end{aligned}
\tag{34}
$$
The last inequality follows exactly from (4):
$\mathcal E_H(f)\leq4\mathcal D_{\mu_P}(f)$.
Combining (32)–(34),
$$
\operatorname{Var}(f)\leq
\left(192+97\frac{C_d}{\gamma_d}\right)\mathcal D_{\mu_P}(f).
\tag{35}
$$
Choose $\delta_d=(192+97C_d/\gamma_d)^{-1}>0$. This proves (2) for the
centered polynomial. Step 1 transfers it to every monic polynomial in
the claim. The constants have no remaining coefficient dependence.

### Step 9. Irreducibility and the logarithmic mixing order

The inverse maps exist, and all generators preserve distinctness; thus
the uniform measure on $\Omega_p$ is stationary. If there were more
than one communicating class, the indicator of one class would have
positive variance and zero Dirichlet energy, contradicting (2).
The identity mass ensures all eigenvalues of $M_P$ lie in $[0,1]$.
Therefore its norm on the mean-zero subspace is at most $1-\delta_d$.
The density of a point mass relative to uniform measure, minus one,
has squared norm $N_p-1$. Cauchy–Schwarz yields
$$
\|\mathcal L(Z_n)-u_p\|_{\mathrm{TV}}
\leq\tfrac12\sqrt{N_p-1}(1-\delta_d)^n
\leq\tfrac12p^3e^{-\delta_dn},
$$
which is (3). In particular the mixing time is at most
$\delta_d^{-1}(3\log p+\log(1/(2\varepsilon)))$, rounded up and
replaced by zero if this expression is negative.

Conversely the law at time $n$ from any single initial configuration is
supported on at most $5^n$ points: this counts the five map choices in
(1), without assuming that their resulting words are distinct. A measure
supported on a set $S$ has total-variation distance at least
$1-|S|/N_p$ from uniform. Thus distance at most $\varepsilon$ requires
$$
n\geq\frac{\log((1-\varepsilon)N_p)}{\log5}.
\tag{36}
$$
Since $N_p\asymp p^6$, (36) and (3) prove the claimed logarithmic order.
$\square$

## Corrections or missing assumptions

No extra coefficient hypothesis was added. Centering in Step 1 is a
unitary conjugacy proof device, not a restriction to an already centered
subfamily. The explicit small-characteristic exclusion and laziness are
part of the original claim. A nonmonic leading coefficient or an
extension-field theorem is not silently included.

The nonlinearity condition matters: in degree one, both generators are
special-affine maps and preserve oriented area. Distinct nonzero-area
orbits then give nonconstant invariant functions, so the full three-point
chain has no spectral gap toward the uniform law on $\Omega_p$.
This is an obstruction, not an additional new theorem package.

## Open risks and actual provenance

- No proof obligation is intentionally left OPEN in the stated author
  theorem; independent checking of the exact assembled argument remains
  a separate, pending stage.
- The constant is positive but not advertised as numerically sharp or
  effective; no expanding-degree or small-prime conclusion is inferred.
- The affine and linear expansion inputs are strong prior theorems.
  The finite-difference mechanism has direct older literature; the
  separate prior supplement records that deduction. Novelty may only be
  assessed for the exact combined coefficient-uniform three-point result.
- The quadratic quotient derivation is retained in
  [its independently checked first-probe report](PAPER30_THREE_POINT_QUOTIENT_GAP_FIRST_PROBE_20260906.md).
  A separate all-degree quotient report and an independent full affine
  chain audit are being produced with disjoint file ownership.
- This file was written using the `proof-writer` structure after full
  instruction reading. The cited expansion statements were read in
  their primary published PDFs; they are not inferred from search snippets.
- There is no manuscript, page count, formal candidate score, external
  submission, upload, numerical experiment, or Route PASS associated
  with this proof package.
