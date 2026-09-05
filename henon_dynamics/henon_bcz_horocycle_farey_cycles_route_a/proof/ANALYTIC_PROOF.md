# C395: complete BCZ Farey cycles and the continuous-family obstruction

## Claim and status

Status: PROVABLE AS STATED with the stated boundary convention. This is an
owner-heavy, source-local reconstruction of the classical BCZ section and
periodic-orbit theorems of Athreya and Cheung, not a literature-newness claim.
The proof below supplies the elementary arguments needed by this package.
It does not import their ergodicity theorem or the later Cheung--Quas weak
mixing theorem as a claim proved here.

Let
$$
\Omega=\{(a,b):0<a,b\leq1, a+b>1\},\quad
k(a,b)=\left\lfloor{1+a\over b}\right\rfloor,
\quad T(a,b)=(b,k(a,b)b-a),\quad R(a,b)={1\over ab}.
$$
The lower edge is excluded; the top and right edges are included; the floor
uses its exact integer value at equality. The theorem classifies every
periodic point, including those on floor walls. For
$$
\delta\in(1/(N+1),1/N],\qquad
S_N=\{(q,r)\in\{1,\ldots,N\}^2:\gcd(q,r)=1, q+r>N\},
$$
the set $\delta S_N$ is one primitive cycle of least period
$$
L_N=\sum_{j=1}^N\varphi(j),\qquad \varphi(1)=1.
$$
These are all periodic cycles, uniquely parametrized by $\delta\in(0,1]$.
Their total roof is $\delta^{-2}$. Starting at $(\delta q,\delta r)$, the
complete branch cocycle is
$$
M_{q,r}=\begin{pmatrix}1-qr&q^2\\-r^2&1+qr\end{pmatrix},\qquad
(M_{q,r}-I)^2=0,\quad M_{q,r}\ne I,
\quad M_{q,r}^{\ell}=I+\ell(M_{q,r}-I).
$$
This cocycle equals the derivative of the return iterate only when that
iterate has a constant branch itinerary in a neighborhood. It is not
declared to be a two-sided derivative at a floor wall.

The measure $d\mu=2\,da\,db$ is an invariant probability measure. For $p>0$,
$R\in L^p(\mu)$ if and only if $p<2$, and $\int R\,d\mu=\pi^2/3$.
Every $\operatorname{Fix}(T^n)$ is an explicit finite union of radial
half-open segments and is uncountable. Ordinary finite-cardinality
Artin--Mazur zeta is therefore undefined for the whole section. No
target determinant, rational-prime clock, functional equation, target
quantization, or Route B is asserted.

## Assumptions, notation, and dependencies

All arguments are over the real numbers unless integers are stated.
Column vectors are used. The integer branch matrix is
$A_k=\left(\begin{smallmatrix}0&1\\-1&k\end{smallmatrix}\right)$;
the product along a trajectory is ordered with the last branch on the left.
$\varphi$ is Euler's totient, $\gcd$ is the positive greatest common divisor,
and $\mu_{\rm M}$ below is the Moebius function, distinct from measure $\mu$.

Dependency map:

1. The section lattice and its first-return calculation prove invertibility,
   the roof formula, and irrational nonperiodicity.
2. An elementary Farey-neighbor lemma proves the single-cycle classification
   and exact least period without a finite-cutoff assumption.
3. Farey gaps and the lattice return equation prove the total roof and all
   branch-cocycle powers, including boundary itineraries.
4. Direct cusp integration proves the complete positive-$p$ moment boundary.
5. The cycle classification proves the fixed-set formula and the zeta
   obstruction. An elementary Moebius count compares the two clocks.

Only the Basel identity $\sum_{j\geq1}j^{-2}=\pi^2/6$ and elementary
Lebesgue change of variables are used as standard background facts. Classical
source ownership is documented separately; it is not mathematical novelty.

## 1. The exact section and first return

Write
$$
p_{a,b}=\begin{pmatrix}a&b\\0&a^{-1}\end{pmatrix},\qquad
h_s=\begin{pmatrix}1&0\\-s&1\end{pmatrix},\qquad
\mathcal L_{a,b}=p_{a,b}\mathbb Z^2.
$$
A unimodular lattice having a primitive positive horizontal vector of length
at most one has a unique representation $\mathcal L_{a,b}$ with
$(a,b)\in\Omega$. The primitive positive horizontal generator determines
$a$. Complete it to an oriented lattice basis. The second basis vector has
height $1/a$, and changing this vector by an integer multiple of $(a,0)$
changes its horizontal coordinate by an integer multiple of $a$. The interval
$(1-a,1]$ has length $a$ and includes exactly one representative. This
determines $b$ and proves uniqueness. A horizontal generator shorter than a
multiple is meant here; a nonprimitive horizontal vector is never counted as
a second representative of the section.

A vector of $\mathcal L_{a,b}$ has coordinates $(x,n/a)$ with
$x=am+bn$ and $m,n\in\mathbb Z$. At a positive time $s$ it becomes a positive
horizontal vector of length at most one exactly when
$$
0<x\leq1,\qquad n/a-sx=0.
$$
Then $n\geq1$. If $s<1/(ab)$, the displayed equation forces $x>nb$, hence
$m\geq1$ and $x\geq a+b>1$, a contradiction. At $s=1/(ab)$, the primitive
vector with $(m,n)=(0,1)$ becomes $(b,0)$. Thus the first return is exactly
$R=1/(ab)$; no earlier short horizontal vector has been missed.

At this return time the old basis is $(a,-1/b),(b,0)$. Choose the new basis
$(b,0),(-a+kb,1/b)$, where $k=\lfloor(1+a)/b\rfloor$. Setting $c=kb-a$ gives
$$
c\leq1<c+b,\qquad c>0.
$$
It follows that $(b,c)\in\Omega$ and that the first-return map is $T$.
The strict inequality $1<c+b$ remains strict even when the floor argument is
an integer. In matrix form,
$$
p_{T(a,b)}=h_{R(a,b)}p_{a,b}B_k,\qquad
B_k=\begin{pmatrix}0&-1\\1&k\end{pmatrix}=A_k^{\mathsf T}. \tag{1}
$$

This proves the first-return assertion for this section only. No assertion
that every orbit of the entire lattice space meets the section is needed;
short closed horocycles outside the section are not silently included.

## 2. Inverse, reversal, and invariant probability

If $T(a,b)=(b,c)$, then $a=kb-c$, and
$$
{1+c\over b}=k+{1-a\over b},\qquad 0\leq{1-a\over b}<1
$$
because $a+b>1$. Therefore
$$
T^{-1}(a,b)=\left(\left\lfloor{1+b\over a}\right\rfloor a-b,a\right).
$$
The same inequalities prove that this inverse maps $\Omega$ into itself.
For $J(a,b)=(b,a)$ this gives $JTJ=T^{-1}$ on the entire half-open domain,
not merely away from the walls. Also $R\circ J=R$.

On each open branch $T$ is linear with determinant one. The branch-wall set
is a countable union of line segments and has two-dimensional Lebesgue
measure zero. The inverse formula implies that branch images are disjoint
up to this null set and cover the domain. Applying change of variables branch
by branch proves invariance of area. Since $\Omega$ has area $1/2$,
$d\mu=2\,da\,db$ is invariant probability. In particular the associated
Koopman map is unitary on $L^2(\Omega,\mu)$, since $T$ is invertible almost
everywhere; this source operator is not a target quantization.

## 3. Periodicity forces rational slope

For a point of period dividing $n$, put
$s_n=\sum_{j=0}^{n-1}R(T^j(a,b))>0$. Iterating (1), and using the
commutativity of the $h_s$, gives
$$
p_{a,b}=h_{s_n}p_{a,b}B_{k_0}\cdots B_{k_{n-1}}.
$$
Consequently
$$
B_{k_0}\cdots B_{k_{n-1}}
=p_{a,b}^{-1}h_{-s_n}p_{a,b}
=\begin{pmatrix}1-ab s_n&-b^2s_n\\a^2s_n&1+ab s_n\end{pmatrix}. \tag{2}
$$
The left side is an integer matrix. The positive number $a^2s_n$ is
therefore a positive integer and $ab s_n$ is an integer. Their ratio is
$b/a$, proving rationality. This argument applies to every exact boundary
itinerary as well as interior points. In particular every irrational-slope
point is nonperiodic.

## 4. Farey-neighbor lemma with endpoint convention

Let $\mathcal F_N$ be all reduced fractions in $[0,1]$ of denominator at
most $N$, including $0/1$ and $1/1$. There are $1+L_N$ fractions and $L_N$
successive gaps. Extend the ordered list by integer translation to the real
line; fractions modulo one then have $L_N$ gaps per unit interval.

If $p/q<s/r$ and $qs-pr=1$, any intermediate reduced fraction $c/d$ obeys
$$
d=q(sd-rc)+r(qc-pd)\geq q+r, \tag{3}
$$
because both parentheses are positive integers. Thus when $q,r\leq N$ and
$q+r>N$ there is no intervening member of $\mathcal F_N$.

For completeness, every consecutive pair in $\mathcal F_N$ has determinant
one and denominator sum greater than $N$. This follows by induction from
$\mathcal F_1=(0/1,1/1)$. To pass from $N$ to $N+1$, insert the mediant
between each determinant-one pair whose denominator sum is $N+1$. The
mediant is reduced, and each of the two new pairs has determinant one. Every
new reduced $c/d$ with $d=N+1$ is obtained this way: choose
$q\in\{1,\ldots,d-1\}$ with $cq\equiv1\pmod d$, set
$p=(cq-1)/d$, $r=d-q$, and $s=c-p$. Then
$c=p+s$, $d=q+r$, $qs-pr=1$, and $0\leq p/q<c/d<s/r\leq1$.
Both denominators are at most $N$; equation (3) shows these parents are
neighbors at order $N$. This proves the induction and exhausts all fractions.

Conversely, each $(q,r)\in S_N$ occurs as exactly one consecutive denominator
pair modulo integer translation. Choose the unique $p\in\{0,\ldots,q-1\}$
with $pr\equiv-1\pmod q$, with $p=0$ if $q=1$, and set
$s=(1+pr)/q$. Then $0\leq p/q<s/r\leq1$ and $qs-pr=1$.
Equation (3) proves adjacency; the congruence proves uniqueness. This also
handles $(q,r)=(1,1)$ when $N=1$.

If $p/q,s/r$ are successive, their next neighbor in the translated list is
$$
{ks-p\over kr-q},\qquad k=\left\lfloor{N+q\over r}\right\rfloor.
$$
Indeed $t=kr-q$ satisfies $0<t\leq N$ and $t+r>N$; the determinant with
$s/r$ is one. Equation (3) again proves adjacency. At $1/1$ the next fraction
lies in the next unit interval; its denominator is the same as the first
fraction after $0/1$. This is a cyclic denominator list, not a duplicate
count of both endpoints.

## 5. Every rational layer is exactly one primitive cycle

Write a rational-slope point uniquely as
$(a,b)=(\delta q,\delta r)$ with $q,r$ positive coprime integers.
Let $N=\lfloor1/\delta\rfloor$. The conditions defining $\Omega$ are
equivalent to
$$
\delta\in(1/(N+1),1/N],\qquad(q,r)\in S_N.
$$
Writing $1/\delta=N+\theta$ with $0\leq\theta<1$ gives
$$
\left\lfloor{1+\delta q\over\delta r}\right\rfloor
=\left\lfloor{N+q+\theta\over r}\right\rfloor
=\left\lfloor{N+q\over r}\right\rfloor. \tag{4}
$$
The last equality holds since the integer remainder on division of $N+q$
by $r$ is at most $r-1$. Thus $T$ acts on $S_N$ as the successor operation
in Section 4. Every pair is visited once before returning, so the least
period is exactly $L_N$, not just a divisor. This proves both existence and
exhaustion for every rational slope. Uniqueness of the reduced pair and
scale proves that the distinct cycles are indexed by $\delta\in(0,1]$.

The first cases are $L_1=1$, $L_2=2$, $L_3=4$. At $N=3$ the cycle beginning
at $(1,3)$ is
$$
(1,3),(3,2),(2,3),(3,1).
$$
The lower endpoint $\delta=1/(N+1)$ does not belong to this layer. It belongs
to layer $N+1$ with its different cycle. The upper endpoint $1/N$ belongs
to layer $N$ and is included in (4).

## 6. The total roof and complete parabolic cocycle

For Farey neighbors the gap is
$s/r-p/q=1/(qr)$. Summing all gaps in a unit interval gives
$$
\sum_{(q,r)\in S_N}{1\over qr}=1.
$$
Therefore every primitive cycle of scale $\delta$ has physical return time
$$
\sum_{j=0}^{L_N-1}R(T^j(\delta q,\delta r))=\delta^{-2}. \tag{5}
$$
This is also the least positive horocycle period of its lattice. In fact
$p_{a,b}^{-1}h_s p_{a,b}$ is integral precisely when
$s\delta^2 q^2$, $s\delta^2 qr$, and $s\delta^2 r^2$ are integers.
As $\gcd(q^2,qr,r^2)=1$, Bezout's identity forces $s\delta^2$ to be an
integer. The value $s=\delta^{-2}$ works and is the least positive one.

Transpose (2), put $n=L_N$, and use (5). The ordered product of branch
matrices is
$$
A_{k_{L_N-1}}\cdots A_{k_0}
=\begin{pmatrix}1-qr&q^2\\-r^2&1+qr\end{pmatrix}=M_{q,r}. \tag{6}
$$
Writing $v=(q,r)^{\mathsf T}$ and $w=(-r,q)^{\mathsf T}$ gives
$M_{q,r}-I=vw^{\mathsf T}$. Since $w^{\mathsf T}v=0$ and neither vector
vanishes, this is a nonzero rank-one nilpotent. The binomial theorem proves
the stated power formula for every integer $\ell$, and both eigenvalues
are one. For physical repetitions $\ell\geq1$, the period-$\ell L_N$ total
roof is $\ell\delta^{-2}$.

If $\delta\in(1/(N+1),1/N)$, all the floor arguments in (4) are
nonintegral and all coordinates are below one. The finite itinerary is
therefore constant in some open neighborhood, and (6) is the actual
derivative of $T^{L_N}$ there. At $\delta=1/N$ the orbit contains
$(1,1/N)$, whose floor argument is $2N$. No global smoothness is claimed.
For example, at $(1,1/2)$ the exact map is $(1/2,1)$, whereas at
$(1-\varepsilon,1/2+\varepsilon)$ for small positive $\varepsilon$ its
limit is $(1/2,1/2)$. This is a discontinuity, not a differentiable
parabolic fixed point. Formula (6) remains an exact branch-cocycle identity
at this endpoint. In every smooth case $\det(I-M_{q,r})=0$, consistent with
the radial fixed family, so a nondegenerate isolated-orbit trace formula
cannot simply be imposed.

## 7. Roof integrability and comparison of the two clocks

By direct integration and monotone convergence,
$$
\int_\Omega R\,d\mu
=2\int_0^1{-\log(1-a)\over a}\,da
=2\sum_{j\geq1}{1\over j^2}={\pi^2\over3}. \tag{7}
$$
For $0<a<1/2$, the interval $1-a<b\leq1$ has length $a$, and $1/2<b\leq1$.
Thus the integral of $(ab)^{-p}$ over that interval is bounded above and
below by positive constant multiples of $a^{1-p}$. Its integral at zero
is finite exactly when $p<2$. Interchanging $a$ and $b$ handles the other
cusp, and on $a,b\geq1/2$ the roof is bounded. This proves the exact
threshold for every $p>0$, including logarithmic divergence at $p=2$.

There is also a uniform asymptotic comparison, not an equality of clocks.
Counting coprime pairs in $\{1,\ldots,N\}^2$ in two ways yields
$$
2L_N-1=\sum_{d=1}^N\mu_{\rm M}(d)\lfloor N/d\rfloor^2.
$$
Use $|\lfloor x\rfloor^2-x^2|\leq2x$ for $x\geq1$, the bound
$\sum_{d\leq N}d^{-1}\leq1+\log N$, and
$\sum_{d>N}d^{-2}\leq1/N$. Absolute Dirichlet convolution of
$\mu_{\rm M}$ with the constant-one function gives
$\sum_{d\geq1}\mu_{\rm M}(d)d^{-2}=6/\pi^2$. Consequently
$$
\left|L_N-{3N^2\over\pi^2}\right|
\leq N(1+\log N)+{N\over2}+{1\over2}. \tag{8}
$$
Since $N\leq1/\delta<N+1$, equations (5) and (8) imply
$\delta^{-2}/L_N\longrightarrow\pi^2/3$ uniformly over layer $N$ as
$N\to\infty$. The physical clock is continuous within a layer while the
discrete least period is constant there; their asymptotic ratio does not
identify them pointwise.

## 8. Exact fixed sets, source zeta, and Route A boundary

For every integer $n\geq1$ the classification gives
$$
\operatorname{Fix}(T^n)=
\bigcup_{\substack{N\geq1\\L_N\mid n}}
\bigcup_{(q,r)\in S_N}
\{(\delta q,\delta r):1/(N+1)<\delta\leq1/N\}. \tag{9}
$$
The union over $N$ is finite because $L_N\geq N$. All representations are
unique. Already $N=1$ contributes the diagonal
$\{(\delta,\delta):1/2<\delta\leq1\}$ to every fixed set. Thus these fixed
sets are uncountable, and the ordinary formula
$\exp(\sum_{n\geq1}\#\operatorname{Fix}(T^n)z^n/n)$ has no finite
coefficients. No analytic continuation can repair an undefined initial
coefficient in this definition. For one specified scale $\delta$, and only
for its finite cycle, the ordinary zeta is $(1-z^{L_N})^{-1}$.

The normalized Koopman operator is unitary on an infinite-dimensional
$L^2$ space, hence noncompact: an infinite orthonormal sequence retains all
pairwise distances under the operator. It is not trace class and does not
supply an ordinary Fredholm determinant on this space. This statement does
not forbid different regularized distributions or different spaces; none
is constructed here.

The source contains native coprime lattice arithmetic and an exact complete
primitive-cycle ledger, but not an intrinsic prime-to-orbit correspondence
with lengths $\log p$. The two clock formulas, the continuous families,
and the unipotent cocycle do not produce target amplitudes, signs, a target
functional equation, or target quantization. The conservative evaluation is
$\mathrm{A0\_WEAK\_ARITHMETIC\_RELATION}$, $\mathrm{A1\_WEAK}$, $\mathrm{A2\_FAIL}$,
$\mathrm{A3\_FAIL}$, $\mathrm{A4\_FORMAL\_HINT}$, overall REJECTED for the
target program, without downgrading the valid source-local theorems.
Route B remains disabled.

## Corrections and open risks

The floor-wall derivative claim has been replaced by the exact cocycle
statement, with the interior derivative qualification proved above.
There is no pending infinite-range proof gap in the stated theorem.
Finite computations are independent consistency controls, not proofs of
the universal quantifiers. Literature ownership is classical and heavy;
neither text search nor this reconstruction certifies newness. Strong
mixing, entropy classification, and a full spectral type are outside this
package. The entire lattice-space flow is not exhausted by this section.
