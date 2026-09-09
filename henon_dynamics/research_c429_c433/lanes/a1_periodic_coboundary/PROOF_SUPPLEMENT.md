# Frobenius structure of a hypothetical PC424-L defect

2026-09-09 UTC. Auxiliary hand proof; no mathematical program was run.

## Claim

Fix an odd prime $p$, $k=\overline{\mathbb F}_p$, $c\in k$, and
$f=x^2+c$. Let $K_c$ and $B_c$ be exactly as in [REPORT.md](REPORT.md).
Put

$$V=k\oplus xk[x^2],\qquad N_c=K_c\cap V.$$

The imported normal form identifies $N_c$ with $K_c/B_c$. The following
claims concern the structure of this **possibly zero** space; they do not
determine whether it is zero.

1. With $\mathcal Fv=v^p$, the space $N_c$ is a free left module over the
   skew-polynomial ring $k[\mathcal F]$, whose relation is
   $\mathcal Fa=a^p\mathcal F$ for $a\in k$. It has a degree-adapted basis
   described below without invoking a theorem on skew principal ideal rings.
2. The dimension of $K_c/B_c$ over $k$ is either $0$ or countably infinite.
   In particular, **finite-dimensionality would imply the original equality**.
3. If $c\in\mathbb F_q$ and $D\ge0$, then $N_c\cap k[x]_{\le D}$ has
   a basis with coefficients in $\mathbb F_q$. Thus the existence of a
   nonzero defect over $k$ would imply one over the field of definition of
   the base, with no increase of degree.

## Status

Auxiliary claims 1--3: **PROVABLE AS STATED**, by the argument below.
Original PC424-L equality/full defect classification: **NOT CURRENTLY
JUSTIFIED**. In particular, the basis indices and generators below are
defined using $N_c$ itself and are not an effective or explicit classification
of the unknown defect. No independent-paper admission follows.

## Assumptions, notation and imported inputs

For an ordinary primitive orbit $O$, write
$S_h(O)=\sum_{a\in O}h(a)$, counting every distinct point once. Write
$k[x]_{\le D}$ for polynomials of degree at most $D$, including zero.

The initial [PC proof, Steps 1, 4 and 5](../../../research_c424_c428/positive_characteristic/PROOF_PACKAGE.md)
already proves $B_c\subseteq K_c$, $k[x]=B_c\oplus V$, and Frobenius
saturation. Only the forward Frobenius identity is needed below. The R6
finite algebraic-transfer descent theorem is **not needed** for these
auxiliary claims, and no algebraic transfer is constructed here.

## Strategy and dependency map

1. Ordinary sums show that $N_c$ is Frobenius-stable and has no nonzero
   constant.
2. Partition possible positive leading degrees into disjoint $p$-power
   chains. Choose the first degree that occurs on each occupied chain.
3. Leading-term cancellation proves spanning, and distinct leading degrees
   prove independence. This also gives the exact degree-filtration formula.
4. Coefficientwise $q$-Frobenius preserves each finite-dimensional degree
   slice. Uniqueness of a reduced row-echelon basis descends it to
   $\mathbb F_q$.

## Proof

### 1. Normal defects and Frobenius

Both $K_c$ and $V$ are $k$-vector spaces. The orbit-sum identity

$$S_{h^p}(O)=S_h(O)^p$$

holds because Frobenius preserves a finite sum. Since $p$ is odd, multiplying
an odd positive exponent by $p$ leaves it odd. Thus $h\in N_c$ implies
$h^p\in N_c$.

The map $f$ has a fixed point in the algebraically closed field $k$. The
sum of the constant polynomial $\beta$ on that one-point orbit is $\beta$.
Consequently

$$N_c\cap k=\{0\}. \tag{1}$$

Every polynomial has a unique normal representative modulo $B_c$. Because
$B_c\subseteq K_c$, normal reduction of an element of $K_c$ remains in
$K_c$, and restriction of the quotient map gives an isomorphism

$$N_c\simeq K_c/B_c. \tag{2}$$

The operator $\mathcal F$ is additive and satisfies
$\mathcal F(av)=a^p\mathcal F(v)$. It therefore defines the stated left
$k[\mathcal F]$-module structure. It is not a $k$-linear operator.

### 2. A degree-adapted free basis

Every positive odd integer has a unique expression $jp^e$ with $j$ odd,
$p\nmid j$ and $e\ge0$. Let $J_c$ be the set of such $p$-primitive
integers $j$ for which some nonzero element of $N_c$ has degree $jp^e$.
For $j\in J_c$, define

$$e_j=\min\{e\ge0:\exists v\in N_c,\ \deg v=jp^e\},
\qquad d_j=jp^{e_j}.$$

Choose a monic $v_j\in N_c$ of degree $d_j$. This choice is possible by
dividing the leading coefficient of a witnessing polynomial. Frobenius
stability gives, for every $r\ge0$,

$$v_j^{p^r}\in N_c,\qquad \deg(v_j^{p^r})=d_jp^r. \tag{3}$$

The degrees in (3), as $(j,r)$ varies, are pairwise distinct: their
$p$-primitive parts are $j$, and within one chain their $p$-valuations
are $e_j+r$.

Let $w\in N_c$ be nonzero. By (1), its degree is positive and odd;
write $\deg w=jp^e$ in the unique form above. The definition of $J_c$
puts $j$ in $J_c$, and minimality of $e_j$ gives $e\ge e_j$. If $a$ is
the leading coefficient of $w$, then

$$w-a v_j^{p^{e-e_j}}$$

is either zero or an element of $N_c$ of strictly smaller degree.
Repeating this cancellation terminates, since nonnegative integer degree
strictly decreases at each nonzero step. A remaining constant is zero by
(1). Hence the set

$$\mathcal B_c=\{v_j^{p^r}:j\in J_c,\ r\ge0\} \tag{4}$$

spans $N_c$ over $k$.

In any nonzero finite linear combination of elements in (4), exactly one
summand has the largest degree, by the pairwise distinctness just proved.
Its leading coefficient cannot cancel. Therefore (4) is linearly
independent. Grouping its elements into their $j$-chains proves

$$N_c=\bigoplus_{j\in J_c}k[\mathcal F]v_j, \tag{5}$$

with no module relations. If $J_c$ is empty, (1) implies $N_c=0$ and
(5) is the empty direct sum.

### 3. Filtration and dimension consequences

For every integer $M\ge0$, distinct degrees in (4) imply that the subset
of (4) of degree at most $M$ is a basis of $N_c\cap k[x]_{\le M}$.
Indeed, no nonzero summand of degree greater than $M$ could cancel with
another summand to produce an element of that slice. Consequently

$$
\dim_k(N_c\cap k[x]_{\le M})
=\sum_{\substack{j\in J_c\\d_j\le M}}
\left(1+\left\lfloor\log_p\frac{M}{d_j}\right\rfloor\right).
\tag{6}
$$

The sum is finite because the distinct positive integers $d_j\le M$
are finite in number. When $M=0$ it is empty and equals zero.

More directly, any nonzero $v\in N_c$ of degree $D$ supplies independent
elements $v,v^p,v^{p^2},\ldots$, with degrees $D,pD,p^2D,\ldots$. Thus
for $M\ge D$,

$$\dim_k(N_c\cap k[x]_{\le M})
\ge1+\left\lfloor\log_p\frac{M}{D}\right\rfloor. \tag{7}$$

Because $k[x]$ has a countable monomial basis, $N_c$ has at most countable
dimension. Equation (7) proves that a nonzero $N_c$ has countably infinite
dimension. In particular,

$$\dim_k(K_c/B_c)<\infty\quad\Longrightarrow\quad K_c=B_c. \tag{8}$$

Finite rank over $k[\mathcal F]$ is different from finite dimension over
$k$: a single nonzero summand in (5) is already infinite-dimensional.
Thus finite $k[\mathcal F]$-generation would **not** prove (8)'s premise.

### 4. Descent to the base finite field

Assume $c\in\mathbb F_q$, where $q$ is a power of $p$. For
$h=\sum a_mx^m$, define the coefficientwise map

$$h^{[q]}=\sum a_m^q x^m.$$

This is distinct from the full polynomial power $h^q$ used in (3).
It preserves degree and normal support. The $q$-power map on $k$ is
bijective. If $O$ is an ordinary primitive $f$-orbit, then
$O^{q^{-1}}=\{a^{q^{-1}}:a\in O\}$ is also an ordinary primitive
$f$-orbit, of the same length: $f$ commutes with both $q$-Frobenius and
its inverse because its coefficients lie in $\mathbb F_q$. Evaluation
gives

$$S_{h^{[q]}}(O)=S_h(O^{q^{-1}})^q. \tag{9}$$

Therefore coefficientwise $q$-Frobenius and its inverse preserve $K_c$,
and hence preserve

$$W_D=N_c\cap k[x]_{\le D}.$$

Regard $W_D$ as a subspace of $k^{D+1}$ through its coefficient vectors.
Choose its unique reduced row-echelon basis in the fixed column order
$1,x,\ldots,x^D$; the zero-dimensional case has the empty basis.
Applying coefficientwise $q$-Frobenius to the basis matrix does not
change zero entries, leading $1$ entries, or pivot positions. Its row
space is again $W_D$, by (9). It is thus a reduced row-echelon basis of
the same subspace in the same column order. Uniqueness of reduced
row-echelon form makes it the original matrix. Every matrix entry is
fixed by $q$-Frobenius and therefore lies in $\mathbb F_q$.

This proves claim 3. In particular, if $W_D\ne0$, one of its nonzero
row-echelon basis vectors gives a defect in $\mathbb F_q[x]$ of degree
at most $D$. It also permits the monic $v_j$ in Section 2 to be chosen
over $\mathbb F_q$: descending $W_{d_j}$, an element of degree $d_j$
exists, so an $\mathbb F_q$-basis contains one with nonzero leading
coefficient in that degree. Normalize that coefficient within
$\mathbb F_q$. This completes the auxiliary proof. $\square$

## Exact missing information and verification limits

Neither (5) nor (6) computes $J_c$, $e_j$, or $v_j$. These formulae encode
constraints on any hypothetical defect and do not classify its actual
membership. No bound on $\dim_k(K_c/B_c)$ or on a nonzero defect's degree
has been proved. The field descent in Section 4 does not limit the degree
of finite extensions containing detecting cycles.

The imported R6 theorem still needs a compatible finite algebraic
transfer constructed from ordinary cycle data. None of Sections 1--4
supplies one. The source comparison in REPORT.md is bounded; these
elementary deductions from imported inputs are not claimed globally novel
or independently publishable. This is AI-assisted author proof, not human
peer review or an assertion that a nonauthor check has already passed.
