# FI2 proof package: exact quotients and conditional intersection reduction

## Claim and status

The frozen original question is FI2 in [REPORT.md](REPORT.md): determine
$J_N=L_2\cap(L_3\cdots L_N)$ for every $N\ge3$ in C4's generic
ordered Fricke family over $k=\mathbb Q(A,B,C,D)$, and distinguish
arithmetic from geometric intersections. **FI2 remains NOT CURRENTLY
JUSTIFIED.** The auxiliary propositions below are proved under precisely
their displayed hypotheses; none silently asserts full higher-period
Fricke monodromy or its linear disjointness.

## Assumptions and notation

All fields have characteristic zero and are embedded in compatible
separable closures. In the actual Fricke application, $P_n$ denotes
ordinary points of exact native period $n$ for $T=s_zs_ys_x$, and
$L_n/k$ is the splitting field of their coordinates. The accepted FG2
input, not reproved here, is

$$
W_2:=\operatorname{Gal}(L_2/k)=V_2\rtimes S_{11},\qquad
V_2=(\mathbb Z/2\mathbb Z)^{11},
\tag{1}
$$

with the same geometric group and $L_2\cap\overline{\mathbb Q}
=\mathbb Q$. Define the cycle splitting field $Q_2=L_2^{V_2}$.
It is Galois over $k$ with group $S_{11}$; this is not the degree-$11$
non-Galois cycle field denoted $E$ below.

A *divisor* means a prime codimension-one divisor on a normal model
of the parameter field. Its inertia subgroup is defined after choosing
a prolongation of the corresponding discrete valuation. Only its
conjugacy class matters. “Unramified in a splitting field” refers to
the whole extension, not only to the sheets near one selected point.

## Strategy and dependency map

1. Recover the two intrinsic quadratic characters of FG2 from its
   accepted point/cycle field presentation.
2. Prove the normal-closure inertia lemma for intersections, and its
   exact $S_{11}$ trichotomy if C4's all-higher-layer nodal input holds.
3. Independently prove the all-finite-family wreath-product reduction:
   distinct nonabelian simple factors make every remaining entanglement
   abelian, but do not remove that abelian entanglement.
4. Describe the arithmetic/geometric character relation lattices and
   the constant-field quotient. Pass to the infinite tower only as a
   directed union of finite intersections.

The elementary simplicity and perfectness of $A_r$ for $r\ge5$,
finite Galois theory, the inertia exact sequence, and the arithmetic/
geometric Galois exact sequence are classical inputs. The needed
group-theoretic reductions and character bookkeeping are proved here.

## Proof

### Proposition 1. The actual FG2 quadratic fields

Let $E/k$ be the degree-$11$ cycle field from FG2, with its intrinsic
element $q$ satisfying the presentation in the accepted first-pass
REPORT, equations (11)--(15). Its ordered point field is
$F=E(\delta)$, where $\delta^2=1-4q$.
Choose any primitive element $\theta$ of the separable extension
$E/k$, let $g_\theta$ be its monic minimal polynomial, and set

$$
p_2=\operatorname{Norm}_{E/k}(1-4q),\qquad
d_2=\operatorname{disc}(g_\theta)
\quad\text{in }k^\times/k^{\times2}.
\tag{2}
$$

The discriminant squareclass is independent of the primitive element:
it is the determinant of the trace form modulo squares of basis-change
determinants. The maximal abelian subextension of $L_2/k$ is exactly

$$
E_2^{\rm ab}=k(\sqrt{p_2},\sqrt{d_2}),
\qquad \operatorname{Gal}(E_2^{\rm ab}/k)=C_2\times C_2.
\tag{3}
$$

Its three quadratic subfields correspond respectively to total phase
parity, cycle-permutation sign, and their product. The second is
$Q_2^{A_{11}}=k(\sqrt{d_2})$.

**Proof.** Let $q_i$, $1\le i\le11$, be the conjugate cycle
coordinates, and choose compatible phases $\delta_i$ in the splitting
field. Their product satisfies
$(\prod_i\delta_i)^2=\prod_i(1-4q_i)=p_2$.
If an element of $W_2$ has phase vector $(a_i)$ and cycle permutation
$\sigma$, its action on this product is multiplication by
$(-1)^{\sum_i a_i}$; reordering the factors contributes no sign.
The product of differences
$\prod_{i<j}(\theta_i-\theta_j)$ is a square root of $d_2$ and
transforms by $\operatorname{sgn}\sigma$. These are independent
characters because FG2 attains the full wreath group: one coordinate
flip and a pure cycle transposition give their two independent values.
Thus none of $p_2,d_2,p_2d_2$ is a square in $k$.

The homomorphism

$$
(a,\sigma)\longmapsto
\left(\sum_i a_i,\operatorname{sgn}\sigma\right)
\tag{4}
$$

is the abelianization. Indeed commutators with permutations generate
all even-sum phase vectors, and commutators in $S_{11}$ generate
$A_{11}$. Hence its kernel is the commutator subgroup, proving (3).
This also proves the identification of the sign field inside $Q_2$.
$\square$

### Proposition 2. Inertia kills exactly a normal quotient

Let $L/k$ and $K/k$ be finite Galois extensions, let $v$ be a divisor
unramified in $K$, and let $I_v\le G=\operatorname{Gal}(L/k)$ be
an inertia subgroup. Then

$$
L\cap K\ \subseteq\ L^{\langle\!\langle I_v\rangle\!\rangle_G},
\tag{5}
$$

where double brackets denote normal closure. If there are several
such divisors, their normal closures may be combined. The assertion
applies unchanged to every finite compositum of fields unramified at
$v$.

**Proof.** The intersection $J=L\cap K$ is Galois over $k$. It is
unramified at $v$ because it is a subextension of the unramified
extension $K/k$. The inertia restriction map from $L$ to $J$ is
therefore trivial. Its kernel is normal in $G$, so it contains the
normal closure of $I_v$. This gives (5). After henselizing at $v$,
finite unramified extensions are finite étale extensions of the
henselian valuation ring; finite composita remain unramified. This
justifies the last assertion rather than inferring it from separate
local point calculations. $\square$

### Proposition 3. Exact FI2 trichotomy from a uniform nodal input

Assume the following single geometric input, called **NI**:

> There is a divisor $\mathcal S$ of the Fricke parameter field whose
> inertia on $L_2$ is generated by one coordinate phase flip, and
> every exact-native-period splitting field $L_n$, $n\ge3$, is
> unramified at $\mathcal S$.

Then for every $N\ge3$,

$$
J_N\subseteq Q_2,\qquad
J_N\in\{k,\ k(\sqrt{d_2}),\ Q_2\}.
\tag{6}
$$

The same assertion holds over $\overline{\mathbb Q}(A,B,C,D)$ if
NI holds geometrically. In particular the phase quadratic and its
product with the sign quadratic cannot occur as inter-level fields.
No hypothesis on the higher-layer Galois groups is needed for (6).

**Proof.** The normal closure in $W_2$ of one coordinate flip is all
$V_2$: conjugation by permutations gives each coordinate flip, and
these generate $V_2$. Apply Proposition 2 to $L=L_2$ and
$K=K_N=L_3\cdots L_N$. It gives $J_N\subseteq L_2^{V_2}=Q_2$.
Because $J_N/k$ is Galois, it corresponds to a normal subgroup of
$S_{11}$. The normal subgroups of $S_{11}$ are $1,A_{11},S_{11}$,
so the three possible fields are exactly those in (6).
The geometric proof uses the same accepted geometric $W_2$ group.
$\square$

**A precise completion test.** Suppose in addition there is a divisor
$\mathcal B$ with a transposition as its image on the eleven cycle
labels, and every $L_n$, $n\ge3$, is unramified there. The normal
closure of a transposition in $S_{11}$ is $S_{11}$, so another
application of Proposition 2 gives $J_N=k$ for every $N$.
It is enough to know that $k(\sqrt{d_2})\not\subseteq K_N$ for
all $N$: the alternative $Q_2$ already contains that quadratic field.
These are sufficient tests, not established higher-layer inputs.

**Branch-character interface.** On FG2's accepted nodal phase branch,
$p_2$ has odd valuation and $d_2$ has even valuation. On its accepted
smooth two-cycle fold branch, $d_2$ has odd valuation and $p_2$ has
even valuation. These are direct translations of the two inertia
characters in Proposition 1: over a residue-characteristic-zero
discrete valuation, a quadratic squareclass is ramified exactly when
its valuation is odd. FG2's fold has two point transpositions, one
cycle transposition, and locally unramified phase functions. No
global polynomial discriminant formula is needed for these parities.
The missing issue is whether a selected such divisor also ramifies
some *other* higher-period sheets.

### Proposition 4. Conditional reduction of all wreath entanglement

Let $I$ be a finite index set, and let $L_i/k$ be finite Galois
extensions with actual groups

$$
W_i=(\mathbb Z/m_i\mathbb Z)^{r_i}\rtimes S_{r_i},
\qquad m_i\ge1,\quad r_i\ge5.
\tag{7}
$$

Assume the integers $r_i$ are pairwise distinct. Let
$L=\prod_{i\in I}L_i$, let $H=\operatorname{Gal}(L/k)$ with its
faithful restriction embedding in $\prod_iW_i$, and let
$\pi_i:W_i\to W_i^{\rm ab}$ be abelianization. Then

$$
W_i^{\rm ab}=C_{m_i}\times C_2,
\qquad W_i'=\ker\pi_i\text{ is perfect},
\tag{8}
$$

and, writing $\pi=\prod_i\pi_i$,

$$
\prod_iW_i'\subseteq H,
\qquad H=\pi^{-1}(\pi(H)).
\tag{9}
$$

If $E_i=L_i^{W_i'}$ is the maximal abelian subextension, then

$$
L_i\cap\prod_{j\ne i}L_j
=E_i\cap\prod_{j\ne i}E_j.
\tag{10}
$$

In particular the $L_i$ are jointly linearly disjoint if and only if
their abelian subextensions $E_i$ are jointly linearly disjoint.
“Jointly” cannot be replaced by “pairwise.”

**Proof of (8).** Put $V=(\mathbb Z/m\mathbb Z)^r$ and
$V_0=\{(a_i):\sum_i a_i=0\}$. The sum and permutation-sign map
has kernel $V_0\rtimes A_r$. Its target is abelian. Commutators
of coordinate vectors with transpositions generate all differences
$a(e_i-e_j)$, hence all of $V_0$; and $S_r'=A_r$. Therefore
$W'=V_0\rtimes A_r$.

To prove perfectness, choose four distinct indices $i,j,k,\ell$.
The commutator of $(i\,j\,k)\in A_r$ with
$a(e_i-e_\ell)\in V_0$ produces $a(e_j-e_i)$, up to a harmless
commutator-convention sign. Such differences generate $V_0$.
Since $A_r$ is perfect for $r\ge5$, the commutator subgroup of
$V_0\rtimes A_r$ contains both factors and equals the whole group.
This includes $m=1$, when the vector factor is trivial.

**Composition-factor observation.** Every nonabelian simple
composition factor of $W_i$ is $A_{r_i}$; all other factors are
cyclic of prime order. The same observation for a subdirect product
uses induction: project onto all but its last factor. The kernel
embeds as a normal subgroup of the last factor, because the projection
onto that factor is surjective. Its composition factors belong to
those of the last factor; the image has the previous factors' list
by induction. Thus a subdirect product cannot introduce a new
nonabelian simple composition factor. This would be false for an
arbitrary subgroup without the surjective-projection hypothesis.

**Proof of (9).** Proceed by induction on $|I|$. For the last factor
$W_t$, let $H_0$ be the projection to the other factors. Both
projections $H\to H_0,W_t$ are surjective. Define

$$
N_0=\{h_0:(h_0,1)\in H\},\quad
N_t=\{w:(1,w)\in H\}.
$$

They are normal, and pairing the coordinates of an element of $H$
gives an isomorphism $H_0/N_0\simeq W_t/N_t=:Q$. This is the
elementary form of Goursat's lemma. If $Q$ had a nonabelian simple
factor, it would have to be $A_{r_t}$ from the last factor and also
one of the $A_{r_i}$, $i\ne t$, from $H_0$. These groups are
nonisomorphic because their orders $r_i!/2$ are strictly increasing.
Hence $Q$ is solvable.

The image of a perfect finite group in a solvable group is trivial:
its image equals its own commutator subgroup and is contained in
every term of the solvable group's derived series. Thus
$W_t'\subseteq N_t$. By induction $H_0$ contains
$D_0=\prod_{i\ne t}W_i'$, a perfect group, so $D_0\subseteq N_0$.
Consequently $H$ contains $D_0\times W_t'$. This proves the first
part of (9). Since this product is $\ker\pi$, containment implies
$H=\pi^{-1}(\pi(H))$.

**Proof of (10).** The intersection is a common quotient field of
$L_i$ and the other compositum. The composition-factor argument and
perfectness show it is abelian, so it lies in $E_i$. The maximal
abelian subextension of the other compositum is exactly
$\prod_{j\ne i}E_j$: its Galois group contains the perfect subgroup
$\prod_{j\ne i}W_j'$, its quotient is abelian by (9), and therefore
that perfect subgroup is its full commutator subgroup. Thus the
intersection lies in the right side of (10). The reverse containment
follows from $E_j\subseteq L_j$. Finally, (9) identifies full product
image with full product image on the abelianizations. $\square$

**Fricke specialization of this conditional proposition.** If the
actual higher layers up to $N$ have the displayed full wreath groups,
with all $r_n$, $2\le n\le N$, at least five and pairwise distinct
(including $r_2=11$ from FG2), then

$$
J_N\subseteq k(\sqrt{p_2},\sqrt{d_2}).
\tag{11}
$$

Combined with NI, (11) becomes
$J_N\in\{k,k(\sqrt{d_2})\}$.
Those higher-layer hypotheses are not provided by FG2, the centralizer
upper bound, or a finite period count. If some $r_n$ coincide, common
alternating quotients are possible and the proposition cannot be used
as stated. A diagonal subgroup of two identical factors is the exact
group-theoretic control for that omitted case.

### Proposition 5. Constants are a different relation test

In Proposition 4 additionally take
$k=\mathbb Q(t_1,\ldots,t_d)$ and assume each $L_i/k$ is regular
over $\mathbb Q$ with its geometric group also equal to $W_i$.
Let $C=L\cap\overline{\mathbb Q}$ be the constant field of the
compositum. Put

$$
\mathcal X=\bigoplus_{i\in I}
\operatorname{Hom}(C_{m_i}\times C_2,\mathbb Q/\mathbb Z).
$$

Pullback of characters along the actual layer representations gives
$\alpha:\mathcal X\to\operatorname{Hom}_{\rm cont}
(\operatorname{Gal}(k^{\rm sep}/k),\mathbb Q/\mathbb Z)$.
Let $R_{\rm ar}=\ker\alpha$, and let $R_{\rm geo}$ be the kernel
after restricting these characters to the geometric absolute Galois
subgroup. Then

$$
R_{\rm ar}\subseteq R_{\rm geo},\qquad
\operatorname{Hom}(\operatorname{Gal}(C/\mathbb Q),
\mathbb Q/\mathbb Z)\simeq R_{\rm geo}/R_{\rm ar}.
\tag{12}
$$

In particular $C/\mathbb Q$ is abelian here. Joint arithmetic linear
disjointness is equivalent to $R_{\rm ar}=0$; joint geometric linear
disjointness is equivalent to $R_{\rm geo}=0$. Individual regularity
does not assert either condition.

**Proof.** Let $H_{\rm ar}$ and $H_{\rm geo}$ be the arithmetic and
geometric groups of the compositum inside $\prod_iW_i$. Both are
subdirect by the individual group hypotheses, so Proposition 4 makes
both contain $D=\prod_iW_i'$. The constant-field exact sequence is

$$
1\longrightarrow H_{\rm geo}\longrightarrow H_{\rm ar}
\longrightarrow\operatorname{Gal}(C/\mathbb Q)\longrightarrow1.
$$

Thus its quotient is abelian and is detected on
$\prod_i(C_{m_i}\times C_2)$. Characters on a subgroup of a finite
abelian group extend to the whole group: decomposing successively
into cyclic extensions and choosing the needed roots in
$\mathbb Q/\mathbb Z$ proves the extension assertion. Consequently
$\mathcal X/R_{\rm ar}$ is the full character group of
$H_{\rm ar}/D$. The characters vanishing on $H_{\rm geo}/D$ are
exactly $R_{\rm geo}/R_{\rm ar}$, which is the dual of the quotient.
This proves (12). The final equivalences follow from (9). $\square$

**Exact logical control, not a Fricke counterexample.** Over
$k_0=\mathbb Q(t)$ the fields
$U=k_0(\sqrt t)$ and $V=k_0(\sqrt{2t})$ are individually rational
function fields over $\mathbb Q$, hence regular. They are distinct
quadratic extensions and are linearly disjoint because $2$ is not a
square in $\mathbb Q(t)$. Their compositum is
$\mathbb Q(\sqrt2)(\sqrt t)$ and has constant field
$\mathbb Q(\sqrt2)$. After extending constants to
$\overline{\mathbb Q}$ the two quadratic extensions coincide.
This proves why constants require their own test even after arithmetic
linear disjointness has been established. It does not identify any
actual Fricke common field.

### Proposition 6. The infinite intersection is a finite-stage question

The fields $K_N$ form an increasing sequence. Since $L_2/k$ is finite
Galois,

$$
L_2\cap\bigcup_{N\ge3}K_N=\bigcup_{N\ge3}J_N=J_{N_0}
\tag{13}
$$

for some finite $N_0$. Indeed every element of the left side belongs
to some finite $K_N$. The increasing sequence $J_N$ corresponds to
a decreasing sequence of subgroups of the finite group $W_2$, so
it eventually stabilizes. No numerical bound for $N_0$ follows.
The same assertion holds geometrically. Thus excluding each finite
intersection suffices for the infinite tower, but examining an
arbitrary finite initial segment does not prove that exclusion.
$\square$

### Proposition 7. Ordinary Fricke cycle counts have distinct sizes

Use the actual ordinary-sheet conclusion of
[C4's NI supplement, §6](../c4_uniform_fricke/PROOF_SUPPLEMENT.md),
not merely its separate inertia statement. It gives
$\nu_2=|P_2|=22$ and, for $n\ge3$,

$$
\nu_n=|P_n|=\sum_{d\mid n}\mu(n/d)u_d,\qquad
u_n=(2+\sqrt5)^n+(2-\sqrt5)^n,
\tag{14}
$$

where $\nu_n$ also counts exact-period-$n$ ordinary Cayley points
for $n\ge3$. The cardinalities $\nu_n$ are distinct notation from
the phase-norm squareclass $p_2$ in Proposition 1.
Then the native cycle counts $r_n=\nu_n/n$ are strictly increasing
for $n\ge2$, and in particular are pairwise distinct and at least
$11$. The distinctness assertion includes the exceptional layer
$r_2=11$, not merely the layers $n\ge3$.

**Proof.** The positive sequence starts at $u_0=2,u_1=4$ and
satisfies $u_{j+1}=4u_j+u_{j-1}$. Thus $u_{j+1}>4u_j$ for
$j\ge1$. Consequently, for every integer $m\ge1$,

$$
\sum_{j=1}^{m}u_j
<\frac43u_m<\frac13u_{m+1}.
\tag{15}
$$

For $n\ge3$, every proper divisor of $n$ is at most $n-2$.
Equation (14) and positivity therefore imply

$$
\nu_n\ge u_n-\sum_{\substack{d\mid n\\d<n}}u_d
\ge u_n-\sum_{j=1}^{n-2}u_j
>\frac{11}{3}u_{n-1}.
\tag{16}
$$

The ordinary Cayley interpretation gives $\nu_j\le u_j$ for every
$j\ge3$, since exact-period points are a subset of points fixed
by the $j$th iterate. For $n\ge4$ we obtain

$$
r_n>\frac{11}{3n}u_{n-1}
>\frac{u_{n-1}}{n-1}\ge r_{n-1},
\tag{17}
$$

where the middle inequality is $11(n-1)>3n$.
Finally $u_2=18$, $u_3=76$, so $r_2=11$ and
$r_3=(76-4)/3=24$. This handles the exceptional two-cycle
correction and proves the claim. $\square$

Accordingly, once C4's ordinary all-period sheet count is accepted,
the distinct-count and $r_n\ge5$ conditions in the **Fricke
application** of Proposition 4 are discharged for all $n\ge2$.
Actual full higher-layer wreath groups are still required. A
centralizer upper bound alone does not suffice: a subgroup of a
larger symmetric group can have $A_{11}$ as a composition factor,
even when the ambient symmetric degrees are different.

## Corrections or missing assumptions

1. C4's NI proof has been read in full, its imported length passage
   checked, and a minor ramified-germ wording issue corrected by C4.
   The dependency is retained explicitly while the coordinator's
   independent whole-proof acceptance is pending; Proposition 3's
   conditional formulation states exactly what NI supplies.
2. The high-layer full groups in Proposition 4 are explicit hypotheses,
   not established Fricke facts. Proposition 7 discharges its count
   conditions only on C4's actual ordinary all-period count, which
   has been read but is awaiting the coordinator's independent review.
3. Even with NI, the actual cycle-sign field
   $k(\sqrt{d_2})$ might or might not lie in a finite higher
   compositum. No genericity argument here decides it.
4. The sufficient branch test needs a divisor unramified in every
   higher layer. Local exclusion of new cycles at one collision does
   not exclude ramification of remote higher-period cycles.
5. None of these statements equates native time with Frobenius,
   constructs a target Euler factor, or assigns target prime weights.

## Open risks and source ownership

These are applications of classical finite Galois theory, Goursat's
lemma, inertia normal closures, and finite-group commutators. They are
not announced as new general theorems. The Fricke-specific input (1)
and the phase cover are the accepted FG2 result. The unresolved
Fricke content is the all-level branch/sign relation, not any algebra
hidden in the proof above. No mathematical program was executed.
