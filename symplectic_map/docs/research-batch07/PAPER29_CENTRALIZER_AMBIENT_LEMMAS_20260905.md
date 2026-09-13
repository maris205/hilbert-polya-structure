# Ambient rigidity lemmas for a product-shear centralizer candidate

Date: 2026-09-05. Bounded author-side viability work for the next unselected
Paper29 question. Not a formal project, scientific lock, candidate PASS or
publication. The preceding cancellation candidate is not being enlarged.

## Claim and status

Let $r\ge3$, $2\le m<n$, and set
$$
Q=\prod_{i=1}^r q_i,\quad P=\prod_{i=1}^r p_i,\quad
x_i=q_ip_i,\quad c_i=x_i-x_r\ (i<r),\quad c_r=0.
$$
Use $\omega=\sum_i dq_i\wedge dp_i$ and the shears
$$
S(q,p)=(q_i,p_i+mQ^m/q_i)_i,\qquad
T(q,p)=(q_i+nP^n/p_i,p_i)_i,\qquad F=TS.
$$
These displayed quotients are polynomials. Define the algebraic torus
$$
\mathcal T=\{(q_i,p_i)\mapsto(a_iq_i,a_i^{-1}p_i):
 a_i\in\mathbb C^*,\ \prod_i a_i=1\}.
$$
For every polynomial symplectomorphism $G$ such that $GF^N=F^NG$ for a
positive integer $N$, the following assertions hold:

1. $G$ fixes the origin and normalizes $\mathcal T$.
2. The action of $G$ on the momentum algebra is a simultaneous index
   permutation: for some $\sigma\in S_r$,
   $$G^*c_i=c_{\sigma(i)}-c_{\sigma(r)}.$$
3. Its derivative at the origin has the form
   $$G^*q_i=a_iq_{\sigma(i)}+O(2),\qquad
     G^*p_i=a_i^{-1}p_{\sigma(i)}+O(2),\qquad
     (\prod_i a_i)^m=1.$$
4. After composing with the inverse simultaneous permutation, $G$ commutes
   with $\mathcal T$ and acts identically on $\mathbb C[c_1,\ldots,c_{r-1}]$.

There is also a separate kernel statement: an automorphism commuting with
$\mathcal T$ and acting identically on its whole invariant algebra belongs
to $\mathcal T$.

**Author status: PROVABLE AS STATED**, conditional only on the explicitly
identified, previously proved fixed-ring input below. This file does not
yet prove that the whole centralizer is $\mathcal T\rtimes S_r$ times
$\langle F\rangle$. That further assertion needs the precise generic
surface centralizer and its descent. It also needs independent checking
and a novelty/value/page assessment before selection.

## Input and dependency map

The input is the global fixed-ring assertion from
[the retained first-integral proof](PAPER29_CANDIDATE_PROOF_V1_20260905.md),
Theorem7:
$$
\mathbb C[q,p]^{F^N}=\mathbb C[c_1,\ldots,c_{r-1}]
\quad\text{for every }N\ge1.
$$
That mathematical result survived its independent proof checks but was
not selected as an independent long paper. Its use here does not convert
the old candidate into an accepted paper or give novelty credit for an
already obtained lemma. The present proof uses no fixed-fiber collision
classification and does not repeat the no-periodic-curve argument.

The new chain is: fixed ring $\to$ locally finite Hamiltonian derivations
$\to$ affine base action $\to$ torus normalization $\to$ signed simplex
weights $\to$ lowest nonzero jet. The final kernel statement is a UFD
argument in the original polynomial ring, not a torsor assertion about
singular fibers.

## Proof

### 1. A commuting symplectomorphism acts affinely on the momentum algebra

Commutation with $F^N$ makes $G^*$ an automorphism of the displayed fixed
ring. Write $G^*c_i=\phi_i(c)$, with $\phi$ a polynomial automorphism of
$\mathbb A^{r-1}$.

For $h\in\mathbb C[q,p]$ put $D_h(u)=\{u,h\}$, with
$\{q_i,p_j\}=\delta_{ij}$. Then
$$
D_{c_i}=q_i\partial_{q_i}-p_i\partial_{p_i}
       -q_r\partial_{q_r}+p_r\partial_{p_r}.
$$
These derivations are simultaneously diagonal on monomials and locally
finite over $\mathbb C$. Symplectic pullback conjugates Hamiltonian
derivations, so $D_{G^*c_i}$ is locally finite as well. Since the $c_j$
Poisson commute,
$$
D_{\phi_i(c)}=\sum_{j<r}\frac{\partial\phi_i}{\partial c_j}D_{c_j},
\qquad
D_{\phi_i(c)}^k(q_j)
 =\left(\frac{\partial\phi_i}{\partial c_j}\right)^k q_j
\quad(j<r).
$$
If any coefficient $h=\partial\phi_i/\partial c_j$ were nonconstant, the
polynomials $1,h,h^2,\ldots$ would be linearly independent over $\mathbb C$.
Indeed an algebraic relation over the algebraically closed field
$\mathbb C$ would force $h$ to be one of finitely many constant roots,
because the polynomial ring is a domain. Multiplication by nonzero $q_j$
preserves that independence. This contradicts local finiteness. Every
partial derivative is therefore constant, and
$$\phi(c)=Mc+b$$
with $M\in GL_{r-1}(\mathbb C)$.

### 2. The torus is normalized and the origin is fixed

The preceding conjugation identity says that $G$ preserves the span of
the $D_{c_i}$ under conjugation. This span is the Lie algebra of
$\mathcal T$. For completeness, normalization here can be seen directly
over $\mathbb C$: every point of $\mathcal T$ is the exponential of a
complex linear combination of these diagonal derivations. One chooses
logarithms of $a_1,\ldots,a_{r-1}$ and takes
$a_r=(\prod_{i<r}a_i)^{-1}$. Conjugating such a flow by $G$ gives the
flow of another linear combination of the same derivations, which is again
in $\mathcal T$. Apply the same argument to $G^{-1}$ for equality.
This proves normalization of the algebraic actions as well, since their
regular maps agree on all complex points. No dynamical analytic extension
or completeness assumption on a nonlinear Hamiltonian is used.

Every coordinate has a nontrivial $\mathcal T$-weight. Its common fixed
locus in $\mathbb A^{2r}$ is exactly the origin. A normalizing automorphism
maps that fixed locus to itself, so $G(0)=0$. Evaluating $G^*c_i$ at zero
now gives $b=0$.

### 3. The tangent representation allows only a permutation or full flip

In the character lattice of $\mathcal T$, let $w_i$ be the weight of
$q_i$; the weight of $p_i$ is $-w_i$. In a basis,
$$
w_i=e_i\ (i<r),\qquad w_r=-\sum_{i<r}e_i.
$$
For $r\ge3$ these $2r$ weights are distinct. The only linear relation
among the $w_i$ is a multiple of $\sum_iw_i=0$.

The invertible derivative $L=dG_0$ normalizes the tangent torus, so its
induced lattice automorphism permutes the weight set $\{\pm w_i\}$. It
therefore maps each pair $\{w_i,-w_i\}$ to another such pair. Write the
images of the $w_i$ as $\varepsilon_iw_{\sigma(i)}$, with
$\varepsilon_i\in\{1,-1\}$. The relation among their sum implies that
all $\varepsilon_i$ have the same sign. Symplecticity of $L$ then gives
exactly the two possibilities
$$
\begin{array}{ll}
L^*q_i=a_iq_{\sigma(i)},&L^*p_i=a_i^{-1}p_{\sigma(i)},\\
L^*q_i=a_ip_{\sigma(i)},&L^*p_i=-a_i^{-1}q_{\sigma(i)}.
\end{array}
$$
In particular the quadratic leading part of $G^*c_i$ is respectively
$c_{\sigma(i)}-c_{\sigma(r)}$ or its negative. Since the full $G^*c_i$
was already shown to be linear in the quadratic $c_j$, this leading part
is the entire polynomial. There are no higher-degree terms left in it.

### 4. The asymmetric lowest jet excludes the full flip

Let $a=rm-1$. Since $m<n$, the first nonidentity homogeneous part of $F$
has degree $a$ and is the nonzero vector field
$$
U(q,p)=(0,\ldots,0,mQ^m/q_1,\ldots,mQ^m/q_r).
$$
The next shear has larger initial degree $rn-1$, and substitutions into
it cannot produce a smaller degree. Thus
$$F^N(z)=z+NU(z)+\text{terms of degree greater than }a.$$
Comparing the degree-$a$ parts of $GF^N=F^NG$ gives
$$L\,U=U\circ L.$$
All terms of higher degree in $G$ cancel at this comparison: differentiating
a homogeneous term of degree at least2 against $U$ has degree at least
$a+1$. Characteristic zero permits cancellation of the scalar $N$.

In the full-flip case, the left side has a nonzero position block and
zero momentum block, whereas the right side has zero position block.
They cannot be equal. In the nonflipping case put $A=\prod_i a_i$.
The two momentum components in the same identity differ by the scalar
$A^m$, since
$$
U(Lz)_{p_i}=m A^m a_i^{-1}Q^m/q_{\sigma(i)},\qquad
(LU(z))_{p_i}=m a_i^{-1}Q^m/q_{\sigma(i)}.
$$
Their equality implies $A^m=1$.

Removing the simultaneous permutation leaves trivial action on the
character lattice and on every $c_i$. An algebraic torus automorphism is
determined by its character action, so the resulting $G$ commutes with
$\mathcal T$, not merely normalizes it. This proves assertions1–4.

### 5. The kernel over the full torus quotient is exactly the torus

The invariant algebra of $\mathcal T$ is
$$
R^{\mathcal T}=\mathbb C[x_1,\ldots,x_r,Q,P]/(QP-\prod_i x_i).
$$
To verify this, an invariant monomial has exponent differences in the
integer span of $(1,\ldots,1)$. Factoring paired $q_ip_i$ leaves either
a power of $Q$ or a power of $P$. The Laurent monomial normal form proves
that the displayed relation is the only one.

Let $H$ commute with $\mathcal T$ and fix this algebra pointwise. Then
$$H^*q_i\,H^*p_i=q_ip_i.$$
Both factors on the left are irreducible in the polynomial UFD, because
$H^*$ is an automorphism. Consequently they are constant multiples of
$q_i,p_i$ in one of the two orders. Torus equivariance excludes their
exchange, since $w_i\ne-w_i$. Hence
$$H^*q_i=b_iq_i,\qquad H^*p_i=b_i^{-1}p_i\quad(b_i\in\mathbb C^*).$$
The additional equality $H^*Q=Q$ gives $\prod_i b_i=1$, proving
$H\in\mathcal T$. This argument also excludes a momentum-dependent
rational torus multiplier that would fail to extend regularly to all of
affine space. $\square$

## What this reduces, and what remains unproved here

After removing a permutation, any commuting $G$ descends over
$K=\mathbb C(c_1,\ldots,c_{r-1})$ to the generic Danielewski surface
$$D_h:\ QP=h(x),\qquad h(x)=\prod_i(x+c_i).$$
It commutes with the surface automorphism induced by $F^N$. If an
independent proof establishes that this generic surface centralizer is
$\langle\phi\rangle$ when $\gcd(m,n)=1$, then the quotient image of $G$
is $\phi^k$ for one integer $k$. The map $F^{-k}G$ fixes the generic
quotient. Equalities of its invariant polynomials over $K$ are equalities
in the original domain, so Section5 would put it in $\mathcal T$.

Under exactly that pending input, the anticipated full answer would be
$$C_{\operatorname{Aut}_{\rm sympl}(\mathbb A^{2r})}(F^N)
 \cong(\mathcal T\rtimes S_r)\times\mathbb Z,$$
with the last factor generated by $F$. Its intersection with
$\mathcal T\rtimes S_r$ is trivial because positive iterates of $F$
have unbounded degree. This conditional conclusion is not recorded as an
independently accepted theorem here.

Known Danielewski automorphism-group and free-product centralizer results
are strong potential novelty deductions. The present ambient reduction is
compact; neither it nor the anticipated quotient computation should be
inflated into a long paper. A complete mathematical classification can
still fail the batch's value or substantive-page gate. No broader
polynomial-potential conjugacy classification, reversor theorem, or extra
claim is added to enlarge the candidate.
