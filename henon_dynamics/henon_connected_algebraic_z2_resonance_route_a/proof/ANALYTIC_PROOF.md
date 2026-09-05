# C388: connected algebraic action, lattice resonance and orbit-count failure

## Claim and status

Status: **PROVABLE AS STATED**, with the entropy identification explicitly a
classical sourced theorem. This is an owner-heavy, source-local reconstruction,
not a claim of a new entropy theorem or a new arithmetic determinant.

Let $\mathbb T=\mathbb R/\mathbb Z$ and
$$
 X=\{x\in\mathbb T^{\mathbb Z^2}:x_{i,j}+x_{i+1,j}+x_{i,j+1}=0\}.
$$
The shift is $(\alpha^{(a,b)}x)_{i,j}=x_{i+a,j+b}$. For every finite-index
sublattice $\Lambda\le\mathbb Z^2$, put $G=\mathbb Z^2/\Lambda$ and $N=|G|$.
The theorem gives an exact integer presentation of $\operatorname{Fix}_\Lambda$,
all its torus and finite invariant factors, a closed component-count formula,
the entire order-three continuous orbit stratum, the source entropy and its
classical Dirichlet-series value, and the failure of ordinary orbit-cardinality
zeta functions. No target divisor, bad Euler factor, root number or Route B is
claimed. The scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Assumptions, notation and dependency map

There are no fitted parameters, prime tables, zero tables or artificial roofs.
Every finite-index lattice has the unique column Hermite form
$\Lambda=\langle(a,0),(b,c)\rangle$ with $a,c>0$ and $0\le b<a$; hence $N=ac$.
Write $\omega=e^{2\pi i/3}$ and
$K=\{(i,j):i-j\equiv0\pmod3\}$.
The character convention is $\chi(g+h)=\chi(g)\chi(h)$.
For a real matrix, $P(A)$ means the product of its nonzero singular values,
not its determinant with zero factors retained.

Dependencies are: Pontryagin presentation and quotient permutations;
unit-torus zero classification; an integer-lattice covolume lemma;
the three-colour kernel lattice; Smith normal form; Jensen plus an absolutely
convergent integrated Fourier series; and the named entropy theorem of
Lind--Schmidt--Ward. Finite computations check certificates but do not prove
the universal quantifiers.

## 1. The source is compact and connected

The relation is a closed subgroup condition in a product of compact circles,
so $X$ is a compact metrizable abelian group and the shifts are commuting
automorphisms. Its discrete character group is
$$
 M=\mathbb Z[u^{\pm1},v^{\pm1}]/(1+u+v)
   \simeq\mathbb Z[u^{\pm1},(1+u)^{-1}].
$$
The second ring embeds in $\mathbb Q(u)$ and is torsion-free as an additive
group. The compact dual of a torsion-free discrete abelian group is connected;
thus $X$ is connected. The presentation follows by dualizing the kernel of
the continuous convolution map, or directly by taking the annihilator of the
relation and its translates. In particular this is not the characteristic-two
Ledrappier three-dot shift.

## 2. Every lattice has one exact integer presentation

Represent $G$ by $(i,j)$ with $0\le i<a$, $0\le j<c$. For any integers $i,j$,
write $j=qc+r$ with $0\le r<c$ and reduce to $((i-qb)\bmod a,r)$.
Let $S_1,S_2$ act on real coordinate vectors by $(S_kx)_g=x_{g+e_k}$.
These are commuting orthogonal integer permutation matrices. Set
$$
 A_\Lambda=I+S_1+S_2.
$$
Over the torus this gives exactly
$\operatorname{Fix}_\Lambda(\alpha)=\ker(A_\Lambda:\mathbb T^N\to\mathbb T^N)$.
The equality includes all fixed points, not a finite-box approximation.

If $U A_\Lambda V=\operatorname{diag}(d_1,\ldots,d_r,0,\ldots,0)$ is Smith
normal form, with $U,V\in\operatorname{GL}_N(\mathbb Z)$ and
$0<d_1\mid\cdots\mid d_r$, torus automorphisms induced by $U,V$ give
$$
 \operatorname{Fix}_\Lambda(\alpha)\simeq
 \mathbb T^{N-r}\times\prod_{k=1}^r\mathbb Z/d_k\mathbb Z. \tag{1}
$$
The factors with $d_k=1$ are trivial. This is an effective complete group
classification: the matrix is specified for every HNF triple and all $d_k$
are computed by exact integer row/column operations. It is not asserted that
the isomorphism or the splitting in (1) is canonical.

## 3. There are exactly two possible zero modes

Finite Fourier characters diagonalize both shifts. The eigenvalues of $A_\Lambda$
are $1+\chi(e_1)+\chi(e_2)$, one for each $\chi\in\widehat G$.
For unit complex numbers $z,w$, the equation $1+z+w=0$ implies
$1=|1+z|^2=2+2\operatorname{Re}z$, so $z=\omega$ or $\omega^2$ and
$w=\overline z$. Consequently the nullity is either zero or two.
The character $(i,j)\mapsto\omega^{i-j}$ descends to $G$ exactly when
$$
 \Lambda\subset K,
 \qquad\text{equivalently}\qquad 3\mid a,\quad b\equiv c\pmod3. \tag{2}
$$
Its conjugate descends under the same condition. Call (2) resonance.
If there is no resonance, (1) is finite and
$$
 |\operatorname{Fix}_\Lambda|=|\det A_\Lambda|
 =\prod_{\chi\in\widehat G}|1+\chi(e_1)+\chi(e_2)|. \tag{3}
$$
All repeated eigenvalues are retained with their character multiplicities.

## 4. Integer covolumes correct the singular determinant

**Lemma.** Let $A\in M_N(\mathbb Z)$ have rank $r$. Put
$L=\ker A\cap\mathbb Z^N$ and $L'=\ker A^t\cap\mathbb Z^N$.
With covolumes taken inside their real spans,
$$
 |\operatorname{tors}(\mathbb Z^N/A\mathbb Z^N)|
 =\frac{P(A)}{\operatorname{covol}(L)\operatorname{covol}(L')}. \tag{4}
$$
At rank zero, $P(A)=1$; at full rank, the two zero-dimensional kernel
covolumes equal one. These are the empty-product conventions.

**Proof.** An integer kernel lattice is saturated: if $kz$ is in the kernel
for a nonzero integer $k$, then $Az=0$. A basis of a saturated sublattice can
be extended to a unimodular basis of $\mathbb Z^N$. If $E=\operatorname{span}L$
and $\pi$ is orthogonal projection onto $E^\perp$, projecting the complementary
columns of that unimodular basis gives a basis of $\pi\mathbb Z^N$.
The block-volume formula for this basis says
$1=\operatorname{covol}(L)\operatorname{covol}(\pi\mathbb Z^N)$.
The dual lattice of $\pi\mathbb Z^N$ in $E^\perp$ is
$E^\perp\cap\mathbb Z^N$, because inner products against all integer vectors
are integral exactly for integer vectors. This also proves that orthogonal
complementary saturated integer lattices have equal covolumes.

The restriction $A:E^\perp\to\operatorname{im}A$ scales $r$-volume by $P(A)$.
Thus $A\mathbb Z^N=A(\pi\mathbb Z^N)$ has covolume
$P(A)/\operatorname{covol}(L)$ in its span.
Its saturation $\operatorname{im}A\cap\mathbb Z^N$ has covolume
$\operatorname{covol}(L')$ by the just-proved complement identity.
Their index is the torsion order of the cokernel. The ratio of these
covolumes proves (4). This proof applies to nonsymmetric matrices. $\square$

In the resonant case both real kernels are the same three-colour plane:
a vector is constant with respective values $A,B,-A-B$ on the residue classes
$i-j=0,1,2\pmod3$. This follows from the two conjugate Fourier modes and also
verifies both $Ax=0$ and $A^tx=0$ directly. Every class has $N/3$ elements,
because the surjective character has three equal fibres. The integer kernel
has the basis with colour values $(1,0,-1)$ and $(0,1,-1)$ and Gram matrix
$$
 \mathcal G=\frac N3\begin{pmatrix}2&1\\1&2\end{pmatrix},
 \qquad \det\mathcal G=\frac{N^2}{3}. \tag{5}
$$
No finite-index sublattice of this integer kernel is being substituted.
$A_\Lambda$ is normal because it is a polynomial in commuting orthogonal
shifts; hence its nonzero singular-value product is the product of the moduli
of its nonzero Fourier eigenvalues. Combining (1), (4), and (5) gives
$$
 \operatorname{Fix}_\Lambda\simeq\mathbb T^2\times F_\Lambda,
 \quad |F_\Lambda|=\frac3{N^2}
 \prod_{\chi:\,1+\chi(e_1)+\chi(e_2)\ne0}
 |1+\chi(e_1)+\chi(e_2)|. \tag{6}
$$
The finite group $F_\Lambda$ has the Smith factors in (1). The factor
$3/N^2$ is mandatory: a pseudodeterminant alone is not the component count.
For rectangles $(a,b,c)=(3,0,3),(3,0,6),(6,0,6)$ the component counts are
respectively $3,21,4116$; the corresponding pseudodeterminants are
$81,2268,1778112$.

### Version-specific source correction, not an entropy refutation

The accessed arXiv version `0912.5169v1`, Lemma 2.1 on printed page 3,
states a component formula without the covolume denominator. Its PDF was
actually rendered and inspected; this is not an HTML-extraction inference.
The smallest counterexample is already $\Lambda=K$, where $N=3$ and
$A=I+R+R^2$ is the three-by-three all-ones matrix on quotient coordinates.
Its integer image is $\mathbb Z(1,1,1)$, so its cokernel is $\mathbb Z^2$
and its torus kernel has one component. Its only nonzero eigenvalue is $3$.
Thus the uncorrected product gives $3$, whereas the correct component count
is $1$. The proof on printed page 4 identifies the image of the full integer
lattice with the image of its intersection with the nonzero-mode space.
For this example these images are $\mathbb Z(1,1,1)$ and
$3\mathbb Z(1,1,1)$, which differ.

This diagnosis is limited to that displayed finite-lattice identity in the
accessed version. Subsequent corrigendum status is not established. It does
not refute the entropy theorem: in this model the logarithmic correction
$\log(N^2/3)/N$ tends to zero. Example 3.2 of the same source already owns
the exact HNF resonance condition and the finite-versus-two-torus distinction;
those statements are positively attributed, not claimed as new literature.

## 5. The complete index-three continuous stratum

For $\Lambda=K=\langle(3,0),(1,1)\rangle$, the three quotient colours have
the single torus relation $A+B+C=0$. Thus $\operatorname{Fix}_K=\mathbb T^2$
with no extra components. On its coordinates $(A,B)$, $\alpha^{e_1}$ acts as
$$
 R(A,B)=(B,-A-B),\qquad
 R=\begin{pmatrix}0&1\\-1&-1\end{pmatrix},\quad R^3=I,\quad\det R=1, \tag{7}
$$
and $\alpha^{e_2}=R^{-1}$. Its full-$\mathbb Z^2$ fixed set consists of
the three constant arrays $A=B=C$ with $3A=0$. Every other point has exactly
the stabilizer $K$, and therefore a primitive orbit with three points.
There are uncountably many such distinct orbits, since quotienting an
uncountable set by equivalence classes of size three remains uncountable.

On this torus the one-step complex multipliers are $\omega,\omega^2$ and
the third-return derivative is $I$. These are tangent multipliers on the
specified torus, not an isolated hyperbolic monodromy on the whole space $X$.
Interchanging $i,j$ preserves the source relation and exchanges the two
shift generators; on this stratum it conjugates $R$ to $R^{-1}$.
It is not declared a same-clock reversor for every rank-one direction.

## 6. Classical joint entropy and its intrinsic arithmetic value

The Lind--Schmidt--Ward theorem for principal algebraic $\mathbb Z^d$-actions
identifies the joint topological entropy (also Haar entropy) here as
$$
 h(\alpha)=m(1+u+v)
 =\int_0^1\int_0^1\log|1+e^{2\pi is}+e^{2\pi it}|\,ds\,dt. \tag{8}
$$
This is their Theorem 3.1; the exact $1+u+v$ example already appears in their
introduction. We invoke that theorem with its full applicable hypotheses,
not prove a new entropy theorem. The local logarithmic singularities at the
two isolated torus zeros are integrable.

Jensen's one-variable formula reduces (8) to
$$
 m(1+u+v)=\frac2\pi\int_0^{\pi/3}\log(2\cos t)\,dt.
$$
To justify Fourier integration, first replace
$\log(2\cos t)$ by $\log|1+\rho e^{2it}|$ with $0<\rho<1$.
Its logarithm series converges uniformly. As $\rho\uparrow1$ these functions
converge uniformly on $[0,\pi/3]$ because $1+\rho e^{2it}$ stays uniformly
away from zero near $\rho=1$. The integrated series is dominated by
$\sum_{n\ge1}n^{-2}$, so
$$
 m(1+u+v)=\frac1\pi\sum_{n\ge1}
 \frac{(-1)^{n-1}\sin(2\pi n/3)}{n^2}
 =\frac{3\sqrt3}{4\pi}L(\chi_{-3},2), \tag{9}
$$
where $\chi_{-3}(n)$ is $0,1,-1$ for residues $0,1,2\pmod3$ and
$L(\chi_{-3},2)=\sum_{n\ge1}\chi_{-3}(n)n^{-2}$ is absolutely convergent.
Indeed the sine equals $\sqrt3\chi_{-3}(n)/2$, and separating the even
terms gives $\sum(-1)^{n-1}\chi_{-3}(n)n^{-2}=3L(\chi_{-3},2)/2$.
Equation (9) is the classical Smyth value, independently rederived here.
No Euler product, bad local data, root number, analytic continuation of an
$L$-function, or target-zero fit is used.

For exact arithmetic checks, the first $H$ paired terms
$L_H=\sum_{k=0}^{H-1}((3k+1)^{-2}-(3k+2)^{-2})$ satisfy
$$
 0<L-L_H\le\frac2{(3H+1)^3}+\frac1{3(3H+1)^2}. \tag{10}
$$
Each tail term is at most $2/(3k+1)^3$; a first-term-plus-integral comparison
proves the bound. It is a certified tail bound, not a floating-point match.

## 7. The cardinality zeta obstruction is unavoidable

The ordinary higher-rank orbit-count construction would require finite
$|\operatorname{Fix}_\Lambda|$ in
$$
 \exp\left(\sum_{[\mathbb Z^2:\Lambda]<\infty}
 \frac{|\operatorname{Fix}_\Lambda|}{[\mathbb Z^2:\Lambda]}
 z^{[\mathbb Z^2:\Lambda]}\right). \tag{11}
$$
The summand for $K$ already has an infinite cardinality at index three.
Equivalently there are uncountably many primitive three-point orbits; the
ordinary product over them cannot define a holomorphic germ at zero.
For any direction $v\in\mathbb Z^2$, the rank-one restriction
$T=\alpha^v$ satisfies $T^3=I$ on $\operatorname{Fix}_K$, so
$\operatorname{Fix}(T^3)$ is uncountable. Thus its ordinary Artin--Mazur
cardinality zeta also fails, including $v=0$.

Counting components instead of points is a different object and does not
repair the same orbit-cardinality trace. Lind--Schmidt--Verbitskiy explicitly
own general periodic-component growth results in the finite-unitary-variety
setting, which includes this example. No claim against their component
results, any measured or regularized construction, or a separately defined
operator determinant is made.

## Corrections, ownership and strict Route-A outcome

The singular pseudodeterminant must be divided by $N^2/3$. Joint entropy is
not a rank-one flight-time clock. The native arithmetic special value is a
single scalar, not a rational-prime-to-primitive-orbit correspondence or a
target determinant divisor. The source has reproducible fixed-group and
primitive-stratum information but no discrete complete prime-carrying ledger.
The strict tuple is
`(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`.
The A4 hint is only the native commuting Koopman unitaries of Haar-preserving
automorphisms; no privileged one-parameter generator, quantum Hamiltonian,
trace-class realization or Route B lift is constructed.

No universal proof rests on the finite evidence grid. The classical source
ownership is substantial and no literature-novelty certification is claimed.
The new-to-this-repository package is the exact all-lattice reconstruction,
resonant covolume correction and the explicit index-three clock obstruction.
