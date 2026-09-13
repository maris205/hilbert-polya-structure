# Paper30 author probe: nonlinear quantum periodic trace modules

Date: 2026-09-06. Status: author proof package, not an independent review,
candidate acceptance, scientific lock or manuscript. Batch07 remains 3/5.
Only the specified discrete symplectic Hénon maps and their natural Weyl
quantizations occur here. No Hilbert–Pólya, arithmetic determinant, operator
self-adjointness, numerical experiment or external publication is claimed.

## 1. Exact claims and assumptions

Let $K$ be a characteristic-zero field. Fix $k\ge1$ and monic polynomials
$p_i(t)\in K[t]$ of degrees $d_i\ge2$, with the indices extended $k$-periodically.
Put $\delta=\prod_{i=0}^{k-1}d_i$. Let $R=K[\hbar]$, or let $\hbar\in K$
be an arbitrary fixed value and put $R=K$. Define
$$
 A=R\langle x,y\rangle/(xy-yx-\hbar).
$$
The coefficients of the monic polynomials may also be independent central
parameters: the proofs work over the corresponding polynomial $K$-algebra.
All homology below is relative to $R$; tensor products and linear quotients
are over $R$. The quotients used below are not quotient algebras.

Define actual Weyl elements $X_i$ by
$$
 X_0=x,\qquad X_{-1}=y,\qquad
 X_{i+1}+X_{i-1}=p_i(X_i)\quad(i\in\mathbb Z).
$$
This defines both tails recursively. Every consecutive pair is a Weyl pair:
$$
 [X_i,X_{i-1}]=\hbar.                                      \tag{1}
$$
Indeed the next commutator is $[p_i(X_i)-X_{i-1},X_i]=\hbar$;
the same identity solves the reverse step. The macro automorphism $\sigma$
sends $X_i$ to $X_{i+k}$. Its existence follows by sending the generating
pair $(X_0,X_{-1})$ to $(X_k,X_{k-1})$ and reversing the recurrences.
Its reduction at $\hbar=0$ is the pullback of the corresponding area-preserving
Hénon composition, with the same phase convention as Paper29.

For $n\ge1$, set $N=kn$, $\tau=\sigma^n$ and
$$
 T_n=A/\operatorname{span}_R\{ab-b\tau(a):a,b\in A\}.
                                                               \tag{2}
$$
Thus $T_n=HH_0(A,A_\tau)$ in the convention in which the right action
on the coefficient bimodule is twisted by $\tau$.

**Claim Q1.** There is an explicit $R$-linear isomorphism between $T_n$
and the polynomial oscillatory quotient for the discrete cyclic action
$$
 S_N(z)=\sum_{i=0}^{N-1}P_i(z_i)-\sum_{i=0}^{N-1}z_i z_{i+1},
 \qquad P_i'=p_i,\quad z_N=z_0.                              \tag{3}
$$
It sends an ordered monomial to the class of the chronologically ordered
product of the actual Weyl orbit coordinates. In particular $T_n$ is free
over $R$ of rank $\delta^n$, with the bounded-exponent ordered-word basis.
This holds without a Morse, reducedness, generic-coefficient or
$\hbar\ne0$ assumption. Moreover $HH_j(A,A_\tau)=0$ for $j>0$.

**Claim Q2.** The induced action of $\sigma$ on $T_n$ is exactly the cyclic
macro shift of that basis, not merely an associated-graded action. Hence
$$
 \operatorname{tr}(\sigma^r\mid T_n)=\delta^{\gcd(n,r)}
 \quad(r\in\mathbb Z),                                    \tag{4}
$$
where $\gcd(n,0)=n$. These traces refer to a finite free algebraic module,
not to traces of an unbounded Hilbert-space operator.

**Claim Q3.** Let $g\in A$, write it in the infinite ordered orbit basis
defined in §6, and let $L(g)$ be the largest diameter of one nonconstant
word with nonzero coefficient. If $N=kn\ge3$ and $N>2L(g)$, then
$$
 \left[\sum_{j=0}^{n-1}\sigma^j g\right]_{T_n}=0
 \quad\Longleftrightarrow\quad
 g\in(\sigma-1)A.                                         \tag{5}
$$
This is a full finite twisted-trace-module test, or equivalently vanishing
against every $R$-linear twisted trace. It is not the test against one
arbitrarily chosen scalar trace, and not a point-evaluation assertion at
$\hbar\ne0$.

**Author status:** PROVABLE AS STATED, with the complete arguments below.
Independent verification is still required, especially for the quotient
identification and homological indexing. Novelty and natural long-paper
capacity have not yet been assessed on this complete package.

## 2. The commuting oscillatory complex

Put $B_N=R[z_0,\ldots,z_{N-1}]$ and define commuting $R$-linear operators
$$
 D_i=M_{\partial_iS_N}-\hbar\partial_i,
 \qquad Q_N=B_N/\sum_iD_iB_N.                              \tag{6}
$$
For $N\ge3$, $\partial_iS_N=p_i(z_i)-z_{i-1}-z_{i+1}$.
For $N=2$ the two neighbours coincide, giving $p_i(z_i)-2z_{1-i}$.
For $N=1$ the derivative is $p_0(z_0)-2z_0$. These repetitions must be
retained; there is no tacit restriction to distinct neighbours.
Commutativity follows from equality of mixed partial derivatives:
$$
 [D_i,D_j]=\hbar M_{\partial_j\partial_iS_N-
                                  \partial_i\partial_jS_N}=0.
$$

We use the following elementary filtered-Koszul fact. Suppose commuting
operators on a polynomial module have, for a positive integer weight
filtration, principal parts given by multiplication by distinct pure powers
$z_i^{a_i}$. Then their Koszul homology vanishes in positive homological
degrees, and the degree-zero quotient is free over the coefficient ring
with the standard monomials $0\le e_i<a_i$ as basis. Variables not among
the principal powers remain unrestricted.

Here is the justification over the coefficient ring, not just its fraction
field. Give the wedge basis vector for an operator the weight of its
principal power. The associated-graded differential is the ordinary
multiplication Koszul differential. Distinct monic pure powers form a
regular sequence over any coefficient ring: successive quotients are free
on the bounded monomials in the eliminated variables. Thus that graded
complex has no positive homology. For a filtered cycle, its largest weight
component is a graded boundary; subtract a lift of that boundary, reducing
the weight. The weights are nonnegative and the Koszul shifts are finite,
so repetition terminates. The same argument proves strictness of boundaries
in degree zero. Consequently its associated graded quotient is the monic
pure-power quotient. Reducing a largest monomial proves spanning by the
proposed representatives, and a hypothetical dependence would have a
nonzero largest graded dependence, which is impossible. This also proves
that the standard representatives form an actual basis.

Apply this fact to all $D_i$, with each variable of weight one. The
principal part of $D_i$ is multiplication by $z_i^{d_i}$: its neighbours
have degree one, lower coefficients of $p_i$ have degree at most $d_i-1$,
and the derivative lowers degree by one. The coefficient $\hbar$ has
weight zero. It follows that
$$
 Q_N\cong R^{\prod_{i=0}^{N-1}d_i}=R^{\delta^n},
 \qquad
 \mathcal B_N=\left\{\prod_{i=0}^{N-1}z_i^{e_i}:0\le e_i<d_i\right\}
                                                               \tag{7}
$$
is a basis, and the full $D$-Koszul complex has no positive homology.
This proof permits every specialization of $\hbar$ and of the monic
polynomial coefficients. General tame-polynomial Brieskorn-lattice
freeness is known prior work; freeness alone is not proposed as new here.

## 3. Explicit nonlinear bridge for $N\ge2$

Define the chronological ordering map
$$
 O_N:B_N\longrightarrow A,\qquad
 O_N\left(\prod_{i=0}^{N-1}z_i^{e_i}\right)
       =X_0^{e_0}X_1^{e_1}\cdots X_{N-1}^{e_{N-1}}.        \tag{8}
$$
It is only linear; it is not an algebra homomorphism.

For an interior index $1\le i\le N-2$, equation (1) gives
$$
 X_i^{e_i}X_{i-1}
 =X_{i-1}X_i^{e_i}+\hbar e_iX_i^{e_i-1}.
$$
Insert $p_i(X_i)=X_{i-1}+X_{i+1}$ in the ordered product. The right
neighbour already occurs in the correct order; the left neighbour crosses
only $X_i^{e_i}$. Thus, for every polynomial $f$,
$$
 O_N(D_if)=0\quad(1\le i\le N-2).                         \tag{9}
$$
There is no interchange of distant orbit coordinates in this argument.

Let
$$
 C_N=B_N/\sum_{i=1}^{N-2}D_iB_N.
$$
Choose positive integer weights $w_0,w_1$ and then successively choose
$w_{i+1}>\max\{d_iw_i,w_{i-1}\}$ for $1\le i\le N-2$.
The principal part of $D_i$ for this filtration is $-M_{z_{i+1}}$.
The filtered-Koszul argument of §2 proves that $C_N$ is free with basis
$z_0^az_1^b$, $a,b\ge0$, and the interior Koszul complex has no positive
homology. For $N=2$ this statement simply says $C_2=B_2$.
The elements $X_0,X_1$ generate $A$, since $y=p_0(X_0)-X_1$, and satisfy
$[X_1,X_0]=\hbar$. Their ordered powers $X_0^aX_1^b$ form the PBW basis.
Therefore (9) induces an actual isomorphism
$$
 \overline O_N:C_N\xrightarrow{\sim}A.                    \tag{10}
$$
This proves injectivity as well as surjectivity after eliminating interior
coordinates; it does not infer an isomorphism from a dimension guess.

All the $D_i$ commute, so $D_0,D_{N-1}$ descend to $C_N$. Directly at
the two ends the same nearest-neighbour calculation gives
$$
 O_N(D_0f)=X_{-1}O_N(f)-O_N(f)X_{N-1},
                                                               \tag{11}
$$
$$
 O_N(D_{N-1}f)=O_N(f)X_N-X_0O_N(f).                       \tag{12}
$$
The formulas include $N=2$: the two subtractions of the coincident
neighbour in (6) are exactly the left and right multiplications in these
identities. Since $X_N=\tau(x)$ and $X_{N-1}=\tau(y)$, the descended
operators are
$$
 E_y=L_y-R_{\tau(y)},\qquad -E_x=R_{\tau(x)}-L_x.          \tag{13}
$$
They commute, because
$$
 [E_x,E_y]=L_{[x,y]}-R_{[\tau(x),\tau(y)]}=0.
$$

For completeness, the span of the images of $E_x,E_y$ equals the span
in (2). Define $E_a=L_a-R_{\tau(a)}$. Left and right multiplications
commute and right multiplication reverses composition, giving
$$
 E_{ab}=E_aL_b+E_bR_{\tau(a)}.
$$
Both terms have their image in the image of the displayed leftmost $E$
operator. Equivalently, the direct induction uses the exact identity
$$
 abm-m\tau(a)\tau(b)
 =\bigl(a(bm)-(bm)\tau(a)\bigr)
  +\bigl(b(m\tau(a))-(m\tau(a))\tau(b)\bigr).
                                                               \tag{14}
$$
The first bracket is an $a$ relation and the second a $b$ relation;
their middle terms cancel. Applying this successively to words in $x,y$
shows that the generator relations imply all word relations, and linearity
handles every $a\in A$. Thus (10)–(13) identify $Q_N$ with $T_n$.
In this identity the left side of (14) is the relation for the word $ab$;
the right twist order is $\tau(a)\tau(b)$, in agreement with that word.

The relative Weyl bimodule Koszul resolution has length two. In $A^e$,
the elements $x_L-x_R$ and $y_L-y_R$ commute, since the two copies of
the central $\hbar$ cancel. Its exactness follows from the PBW filtration:
the associated graded is the diagonal Koszul resolution of the polynomial
algebra $R[x,y]$. Tensoring with the twisted bimodule gives precisely the
$E_x,E_y$ Koszul complex. This supplies the generator presentation of
$HH_0$ without an informal trace manipulation. Taking interior Koszul
homology first in the full $D$-complex reduces that complex to the
two-operator complex (13), by (10) and interior acyclicity. Its total
homology is therefore $HH_\bullet(A,A_\tau)$. Section 2 proves Q1,
including positive-degree homology vanishing, for $N\ge2$.

## 4. The one-coordinate case $N=1$

Here $k=n=1$. Use PBW order $x^ay^b$ and first eliminate $E_y=L_y-R_x$.
For the filtration by degree in $y$, this operator is injective and its
cokernel is freely represented by $R[x]$: its leading action raises the
$y$ degree by one with coefficient one, and all remaining terms have
smaller $y$ degree. The reduction terminates for each polynomial.
For $f\in R[x]$ the generator relation gives
$$
 [fy]=[xf+\hbar f'].
$$
The remaining operator $E_x=L_x-R_{p_0(x)-y}$ hence induces
$$
 f\longmapsto (2x-p_0(x))f+\hbar f'=-D_0f.                \tag{15}
$$
Its leading part is multiplication by $-x^{d_0}$, so it is injective
and its cokernel has basis $1,x,\ldots,x^{d_0-1}$. The two-step Koszul
homology is concentrated in degree zero, proving Q1 in this last case.
This is also the chronological map (8), not a different quantization.

## 5. Exact macro equivariance

The action of $\sigma$ on $A$ preserves the submodule in (2), since it
commutes with $\tau$. Also $[a]=[\tau(a)]$ follows by putting $b=1$
in (2), so the induced action has order dividing $n$.

Under (8), applying $\sigma$ translates each index by $k$. The ordered
product consists of a block with indices $k,\ldots,N-1$ followed by
the $\tau$-translate of the block with indices $0,\ldots,k-1$.
In $T_n$ the identity $[b\tau(a)]=[ab]$ moves exactly that last block
to the front. No pairwise reordering and no commutator correction occurs.
It follows that (8) intertwines $\sigma$ with cyclic translation by $k$
on the commuting variables of $Q_N$. This also follows on the differential
side from $k$-periodicity of the action (3).

The basis (7) is permuted exactly. Think of each group of $k$ consecutive
exponents as one letter from an alphabet of size $\delta$. A length-$n$
word is fixed by rotation through $r$ positions exactly when it is constant
on each of the $\gcd(n,r)$ index cycles. This proves (4).
If desired, the multiplicity of $e^{2\pi ij/n}$ over a splitting field is
$$
 \frac1n\sum_{r=0}^{n-1}\delta^{\gcd(n,r)}e^{-2\pi ijr/n}.
                                                               \tag{16}
$$
This is a finite cyclic-module character calculation; it is not an
identification of primitive geometric periodic orbits or an arithmetic clock.

## 6. Infinite quantum orbit words: the short inherited part

For every finitely supported sequence $e_i\in\{0,\ldots,d_i-1\}$,
define
$$
 M_e=\prod_{i\in\mathbb Z}^{\text{increasing }i}X_i^{e_i}.
                                                               \tag{17}
$$
The factors $X_i$ have the same highest ordinary-coordinate monomials
as in the commutative recurrence. Exchanging $x,y$ in PBW normal ordering
introduces $\hbar$ terms of degree two less. Thus the mixed-radix leading
monomials of (17) are still a one-to-one list of $x^ay^b$, $a,b\ge0$,
with coefficient one; the reversal of the order of the negative and
nonnegative blocks changes only lower total degrees. Induction on total
degree proves that (17) is an $R$-basis of $A$.

The automorphism $\sigma$ translates the ordered indices by $k$, so it
permutes this basis with the constant word fixed and every nonconstant
orbit infinite. Hence $g\in(\sigma-1)A$ if and only if its constant
coefficient and each nonconstant orbit coefficient sum vanish. A primitive
is recovered by finite cumulative sums of the coefficients on each orbit.
This is the PBW transport of Paper29's basis and elementary coinvariant
argument. It is used as a tool here, not counted as a second new theory.

Define $\operatorname{diam}(M_e)$ from the occupied indices, with diameter
zero for a singleton. Put
$$
 L(g)=\max\bigl(\{\operatorname{diam}(M_e):c_e\ne0,M_e\ne1\}
                 \cup\{0\}\bigr)
$$
for $g=\sum_ec_eM_e$. It is the maximum individual diameter, not the
diameter of the union of all occupied indices in $g$.

## 7. Quantum wrapping and the finite detection theorem

Let $M$ have diameter less than $N$. Its occupied indices are distinct
modulo $N$. In $T_n$, translating all its indices by a multiple of $N$
does not change its class, because $[\tau^qa]=[a]$ for every integer $q$.
After such a translation, its smallest occupied index lies in $[0,N-1]$
and its largest lies below $2N$. Split the ordered product into its
indices below $N$ and its indices at least $N$. The second block is
$\tau(a)$ for the wrapped low-index block $a$. Equation (2) changes
$[b\tau(a)]$ into $[ab]$. Consequently
$$
 [M]_{T_n}=\overline O_N(W_NM),                            \tag{18}
$$
where $W_NM$ is the commuting bounded-exponent monomial obtained by
wrapping indices modulo $N$. In particular this equality is exact for
every $\hbar$, not merely modulo $\hbar$ or to leading symbol order.

The combinatorial no-alias lemma is inherited from Paper29: when $N>2L$,
each wrapped nonconstant word of diameter at most $L$ has a unique cyclic
gap longer than $L$. Cutting there recovers the infinite word up to an
integer multiple of $N$. Macro equivalence is retained because $k\mid N$.
Its cyclic macro orbit has length exactly $n$, and distinct infinite
macro-word orbits give disjoint finite cyclic basis orbits. This argument
does not involve the coefficients or the quantum parameter.

Choose one representative $M_O$ occurring in $g$ for each of its finitely
many nonconstant macro orbits, and let $c_O$ be the corresponding sum
of coefficients. Let $c_0$ be the constant coefficient. Then (18) gives
$$
 \left[\sum_{j=0}^{n-1}\sigma^jg\right]_{T_n}
 =nc_0[1]+\sum_Oc_O\sum_{j=0}^{n-1}
             \overline O_N(W_N\sigma^jM_O).               \tag{19}
$$
By Q1 and no aliasing, the summands on the right have mutually disjoint
nonconstant basis supports, and all their individual coefficients are one.
Since $n$ is a unit in $R$, the expression is zero exactly when $c_0=0$
and every $c_O=0$. Section 6 proves the forward implication in (5).
Conversely, for $g=\sigma f-f$ the sum telescopes to $\tau f-f$, whose
class is zero by (2), without any diameter hypothesis. This proves Q3.

At $\hbar=0$ the module (2) is the full fixed-point scheme ring as a
vector space, and (18) is ordinary wrapping. At nonzero $\hbar$ it is
a twisted Hochschild quotient and is not a ring of quantum points.
The same exact basis supports thus persist through nonreduced classical
periodic collisions. No value at an individual geometric point is used.

## 8. Consequences that must be credited as short deductions

The ordinary degree of (17) equals the same sum of phase weights as in
Paper29. Therefore the existing degree-to-diameter formula immediately
converts (5) into a single-period bound $n_{\rm eff}(D)$ and rank at most
$\delta^4D^4$ for $D\ge1$. Likewise the already proved discrete convexity
of word degrees gives a primitive of degree at most $D$ when $\deg g\le D$.
These are consequences of the exact quantum wrapping bridge and inherited
estimates, not newly optimized quantum complexity results.

Every coordinate functional on the finite free basis (7) gives a twisted
trace $A\to R$ by composing with the quotient map. Their complete list
separates the classes in $T_n$. Neither the existence of these dual
functionals nor the general identification of twisted traces with
$HH_0^*$ is a new claim of this project. At $\hbar=0$ they can encode
nilpotent jet data rather than just geometric-point evaluations.

No Hamiltonian-domain, unitary realization, convergence of an oscillatory
integral or positivity of a twisted trace follows from these algebraic
calculations. The discrete-action polynomial gives a finite algebraic
complex here, not an analytically defined path integral.

## 9. Prior-work deductions and next checks

The landscape preflight has identified the following primary sources;
the independent literature report will record actual-read sections and
remaining overlap precisely:

- Fornæss–Weickert, *A quantized Henon map* (2000), establishes a unitary
  quantization framework, so quantizing Hénon itself is not new:
  https://www.aimsciences.org/article/doi/10.3934/dcds.2000.6.723.
- Douai–Sabbah, *Gauss–Manin systems, Brieskorn lattices and Frobenius
  structures (I)* (2003), provides general tame-polynomial lattice
  freeness and specialization, which must be deducted from §2:
  https://www.numdam.org/item/10.5802/aif.1974.pdf.
- Etingof–Stryker, *Short Star-Products for Filtered Quantizations, I*,
  treats twisted traces and their Hochschild interpretation, including
  linear Weyl automorphisms:
  https://arxiv.org/abs/1909.13588.
- Sharapov–Skvortsov, *Hochschild cohomology of the Weyl algebra and
  Vasiliev's equations*, treats linear symplectic twisting:
  https://arxiv.org/abs/1705.02958.

The proposed increment is the explicit chronological identification for
the nonlinear iterates, its exact cyclic equivariance and its compatibility
with short-word quantum wrapping, not the individual general tools.
A finite search not finding this bridge does not establish priority.

Required next actions: independently audit (10)–(15) with the relative
Weyl resolution and ordering convention, verify the universal coefficient
version and the exact wrapping (18), finish targeted primary-source
comparison, then assess whether the complete new argument has sufficient
independent value and natural 22–30-page substance after the deductions.
There is no current candidate PASS, draft authorization exception, PDF,
numerical run or change to accepted Papers27–29.
