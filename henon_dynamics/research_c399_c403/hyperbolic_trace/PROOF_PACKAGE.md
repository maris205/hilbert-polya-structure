# Proof package: ordinary power traces and hyperbolic stability cancellation

## Claim

Let $M$ be a real invertible $d\times d$ matrix, $d\ge1$, with no eigenvalue
on the unit circle. Put $s_r=|\det(I-M^r)|$ for $r\ge1$.

1. For every real $p>0$ and every integer $R\ge\max(1,\lceil p\rceil)$,
   no operator $B\in\mathcal S_p$ on a complex separable Hilbert space has
   $\operatorname{Tr}B^r=s_r$ for all integers $r\ge R$.
2. There is a finite-dimensional graded realization of all $s_r$. After
   grouping equal exterior eigenvalue products, its least total dimension
   is an explicit integer $\sum_j|c_j|$, with equal even and odd dimensions.
3. For every finite $N$, a real normal finite matrix does realize the first $N$
   values $s_1,\ldots,s_N$. Thus no finite prefix alone excludes all ordinary
   finite-dimensional realizations of unrestricted dimension.
4. If all eigenvalues of $M$ are real, this finite-prefix blindness disappears
   under a self-adjoint realization requirement: for every even integer $K\ge2$,
   the $m\times m$ matrix $(s_{K+i+j})_{i,j=0}^{m-1}$ has exactly as many
   negative eigenvalues as there are negative grouped coefficients $c_j$.
   It supplies an explicit finite polynomial positivity certificate excluding
   self-adjoint realizations with trace-class $B^K$ on that moment window;
   for $B\in\mathcal S_p$, the condition $K\ge p$ suffices.

These are statements about one marked orbit's repeat sequence. They do not
exclude cancellation between different unmarked orbits, noncompact generalized
traces, or graded realizations. A natural global transfer-operator realization
is not constructed here.

## Status

PROVABLE AS STATED — author proof below; independent admission review pending.
This is a pre-admission research note, not a numbered or released paper.
The claim is broader than the repository's earlier scalar and one-dimensional
contracting tensor tests, but literature novelty and paper-level admission are
separate questions.

## Assumptions

- All matrices and operators use ordinary algebraic multiplicities.
- The repetition is the literal power $M^r$, not a fitted time change.
- $\mathcal S_p$ means summable $p$th powers of singular values; $0<p<1$
  is allowed as a quasi-ideal. No normality of $B$ or diagonalizability of $M$
  is assumed.
- A graded realization is a finite complex vector space
  $V=V_0\oplus V_1$ with an even endomorphism $A=A_0\oplus A_1$ and
  $\operatorname{Str}A^r=\operatorname{Tr}A_0^r-\operatorname{Tr}A_1^r$.

## Notation

The complex eigenvalues of $M$, repeated with algebraic multiplicity, are
$\lambda_1,\ldots,\lambda_d$. The real unstable invariant space is $E_u$;
its dimension is $d_u$. Set $\epsilon=\operatorname{sgn}\det(M|_{E_u})$,
with determinant $1$ on the zero-dimensional space.
For a subset $S\subseteq\{1,\ldots,d\}$ write

$$
\alpha_S=\epsilon\prod_{i\in S}\lambda_i,
\qquad c_S=(-1)^{d_u+|S|}.
$$

Empty products equal $1$. For each distinct nonzero $\alpha$ appearing here,
sum all corresponding $c_S$, and delete sums that vanish. Denote the remaining
distinct values and coefficients by $(\alpha_j,c_j)_{j=1}^m$.

## Proof strategy

The orientation identity converts the absolute determinant into a finite
signed exponential sum. Its regularized trace determinant has a genuine pole.
An ordinary Schatten determinant is entire, giving the obstruction even if
finitely many low traces are left free. Finite-dimensional power-sum uniqueness
then gives the optimal graded dimension. Newton identities give the contrasting
finite-prefix realization.

## Dependency map

1. Real spectral pairing proves the orientation identity, using hyperbolicity.
2. The determinant expansion proves the signed exponential representation,
   using invertibility to keep all $\alpha_j$ nonzero.
3. The canonical product and local power-series formula for integer-order
   regularized Fredholm determinants prove the all-tail obstruction.
4. Vandermonde invertibility proves the optimal graded dimension.
5. Newton identities and companion matrices prove finite-prefix realizability.
6. Lagrange interpolation and Sylvester inertia prove the finite self-adjoint
   certificate; they require the additional real-spectrum hypothesis.

The operator input in Step 3 is classical. A primary account of the
regularized product convention is Britz et al., equation (1.3):
[arXiv:2007.12834v2](https://arxiv.org/html/2007.12834v2).
All reductions particular to $s_r$ are proved here.

## Proof

### Step 1. Determine the absolute-value sign for every repetition

Each real stable eigenvalue $\lambda\in(-1,1)$ contributes
$1-\lambda^r>0$. A nonreal conjugate pair contributes
$|1-\lambda^r|^2>0$; hyperbolicity ensures it is not zero. A positive real
unstable eigenvalue contributes a negative factor for every $r$. A negative
real unstable eigenvalue contributes a positive factor for odd $r$ and a
negative factor for even $r$.

If $n_+$ and $n_-$ count positive and negative real unstable eigenvalues,
then $d_u\equiv n_++n_-\pmod2$ and $\epsilon=(-1)^{n_-}$.
The sign of the determinant is therefore

$$
(-1)^{n_+}(-1)^{(r+1)n_-}=(-1)^{d_u}\epsilon^r.
$$

Consequently

$$
s_r=(-1)^{d_u}\epsilon^r\det(I-M^r)
    =\sum_{j=1}^m c_j\alpha_j^r. \tag{1}
$$

The determinant depends only on algebraic eigenvalues, so Jordan blocks do
not require an extra hypothesis. Hyperbolicity also gives $s_r>0$ for all $r$.

### Step 2. A negative coefficient survives all multiplicative resonances

Before grouping, the coefficient sum is
$(-1)^{d_u}\sum_S(-1)^{|S|}=(-1)^{d_u}(1-1)^d=0$.
Grouping and deleting zero groups preserve that sum, so
$\sum_j c_j=0$. At least one coefficient survives, because otherwise (1)
would give $s_1=0$. Every surviving coefficient is a nonzero integer. Thus
there are both positive and negative $c_j$.

This argument does not assume multiplicative independence. Equal eigenvalue
products, repeated eigenvalues, negative signs and complex products have
already been grouped before identifying a pole.

### Step 3. No Schatten realization, even after deleting any finite prefix

Suppose $B\in\mathcal S_p$ obeys the asserted tail identities. Let
$k=\max(1,\lceil p\rceil)$. Then $B\in\mathcal S_k$, and $B^r$ is trace
class for $r\ge k$. Its integer-order regularized determinant is the entire
function

$$
F(z)=\det_k(I-zB)
=\prod_\nu(1-z\mu_\nu)
  \exp\left(\sum_{r=1}^{k-1}\frac{z^r\mu_\nu^r}{r}\right), \tag{2}
$$

where $\mu_\nu$ are the nonzero eigenvalues with algebraic multiplicity.
For $k=1$ the inner sum is empty. Summability of $|\mu_\nu|^k$ gives local
uniform convergence of this canonical product. For $|z|\|B\|<1$,

$$
\log F(z)=-\sum_{r=k}^\infty\frac{z^r}{r}\operatorname{Tr}B^r. \tag{3}
$$

The series is absolutely convergent: Schatten Hölder gives
$\|B^k\|_1\le\|B\|_k^k$, and
$\|B^r\|_1\le\|B^k\|_1\|B\|^{r-k}$. The equality with the eigenvalue
product uses the trace theorem for the trace-class powers; no normality is
needed.

Define the rational function

$$
Q(z)=\prod_{j=1}^m(1-\alpha_jz)^{c_j}.
$$

On a small disk around zero, its logarithm normalized by $\log Q(0)=0$
is $-\sum_{r\ge1}s_rz^r/r$. The assumed equality for all $r\ge R$ means
that $\log F-\log Q$ is a polynomial $P$ of degree at most $R-1$.
Hence $F=e^P Q$ on that disk.

Choose an index $j$ with $c_j<0$. Since the $\alpha_j$ are distinct and
nonzero, $Q$ has a pole of order $-c_j$ at $z=\alpha_j^{-1}$, with no
other factor able to cancel it. The factor $e^P$ is entire and nowhere zero.
The identity theorem extends $F=e^P Q$ to the plane with its finitely many
poles deleted; this set is connected. In a punctured neighborhood of the
chosen pole, the right side is unbounded with a pole while $F$ is holomorphic
across its center. This is a contradiction.

This also excludes any nonzero scalar amplitude $w^rs_r$: replace all
$\alpha_j$ by $w\alpha_j$, which preserves distinctness and coefficients.
Changing finitely many initial moments cannot remove the obstruction.

### Step 4. Construct and minimize the graded realization

For $c_j>0$, put $c_j$ copies of the scalar $\alpha_j$ on $V_0$; for
$c_j<0$, put $-c_j$ copies on $V_1$. This diagonal even operator realizes
(1) for every $r$. Its two dimensions are

$$
\dim V_0=\sum_{c_j>0}c_j,
\quad \dim V_1=-\sum_{c_j<0}c_j,
\quad \dim V=\sum_j|c_j|.
$$

The first two quantities are equal because $\sum_jc_j=0$.

For minimality, take any finite-dimensional graded realization and form the
union of its distinct nonzero eigenvalues and the $\alpha_j$. Subtract the
two signed moment representations. If this union is
$\beta_1,\ldots,\beta_\ell$, the difference coefficients $b_i$ satisfy
$\sum_i b_i\beta_i^r=0$ for $r=1,\ldots,\ell$. The matrix
$(\beta_i^r)_{1\le r,i\le\ell}$ is an invertible Vandermonde matrix times
an invertible diagonal matrix. Thus every $b_i=0$.

At $\alpha_j$, let the even and odd algebraic multiplicities be $e_j,o_j$.
The previous paragraph forces $e_j-o_j=c_j$ and therefore
$e_j+o_j\ge|c_j|$. Additional eigenvalues, zero eigenvalues and Jordan
blocks cannot lower the total dimension. Summing gives the lower bound,
attained by the constructed diagonal realization. Equality requires the
minimal signed multiplicities and no additional dimensions; it does not
force diagonalizability within equal-parity repeated eigenvalues.

A canonical, not necessarily minimal, realization is the exterior algebra
$\bigwedge^*\mathbb C^d$, with operator $\epsilon\bigwedge^*M$ and parity
shift by $d_u$. Its supertrace is (1). Compression after product collisions
preserves the repeat sequence but is not asserted to be functorial over a
global dynamical system.

### Step 5. Generic symplectic size and a resonant strict reduction

Suppose $M$ has positive symplectic eigenvalue pairs
$\lambda_i,\lambda_i^{-1}$, $\lambda_i>1$, for $i=1,\ldots,h$.
If the $\lambda_i$ are multiplicatively independent, grouping is encoded by
the Laurent polynomial

$$
\prod_{i=1}^h(t_i+t_i^{-1}-2).
$$

Distinct exponent vectors give distinct eigenvalue products. The sum of
absolute coefficients is the product of the one-variable sums, hence $4^h$.
The minimal even and odd dimensions are each $4^h/2$.

For two pairs $\lambda,\lambda^{-1},\lambda^2,\lambda^{-2}$, put
$t=\lambda^r$. The repeat weight is

$$
(t+t^{-1}-2)(t^2+t^{-2}-2)
=t^3+t^{-3}-2t^2-2t^{-2}-t-t^{-1}+4.
$$

The coefficient norm is $12$, with even and odd dimensions $6$, instead
of the generic $16$. This is an exact all-repetition reduction, not a fitted
   finite-prefix matrix.

### Step 6. Every finite prefix has an ordinary real normal realization

Fix $N\ge1$ and any real numbers $a_1,\ldots,a_N$. Define $e_0=1$ and
recursively

$$
e_j=\frac1j\sum_{r=1}^j(-1)^{r-1}e_{j-r}a_r,
\qquad 1\le j\le N.
$$

Let $C$ be the real companion matrix of the monic polynomial
$x^N-e_1x^{N-1}+e_2x^{N-2}-\cdots+(-1)^Ne_N$.
Newton identities applied to its roots show inductively that
$\operatorname{Tr}C^r=a_r$ for $1\le r\le N$. The identity between the
trace of a matrix power and the sum of powers of its algebraic eigenvalues
does not require simple roots.

The companion gives a convenient explicit real matrix, but normality can
also be imposed without changing any moments. The polynomial has real
coefficients, so its nonreal roots occur in conjugate pairs with matching
multiplicities. For each real root insert its scalar block; for each conjugate
pair $u\pm iv$, $v>0$, insert the real normal block
$\left(\begin{smallmatrix}u&-v\\v&u\end{smallmatrix}\right)$, repeated
with its algebraic multiplicity. Their orthogonal direct sum is a real normal
$N\times N$ matrix with the same eigenvalue multiset as the companion.
Its first $N$ power traces are therefore the prescribed $a_r$ as well.

Taking $a_r=s_r$ proves the finite-prefix assertion. These matrices lie
in every Schatten class, but must fail at some later repetition by Step 3.
No positivity, self-adjointness, contractivity, or dimension bound independent
of $N$ is asserted. The distinction is between self-adjoint and unrestricted
ordinary realizations, not between normal and nonnormal operators.

### Step 7. Finite self-adjoint certificates and exact Hankel inertia

Assume now that all eigenvalues of $M$ are real. Every distinct $\alpha_j$
in (1) is then real and nonzero. Fix an even integer $K\ge2$ and define
$H^{(K)}_{i\ell}=s_{K+i+\ell}$ for $0\le i,\ell<m$. With the invertible
Vandermonde matrix $V_{ij}=\alpha_j^i$, equation (1) gives

$$
H^{(K)}=V\,\operatorname{diag}(c_j\alpha_j^K)\,V^{\mathsf T}. \tag{4}
$$

Since $\alpha_j^K>0$, Sylvester's law of inertia proves that this real
symmetric matrix has exactly $\#\{j:c_j>0\}$ positive and
$\#\{j:c_j<0\}$ negative eigenvalues, and no zero eigenvalues.
In particular it is not positive semidefinite.

An explicit negative direction is also available. Choose $j_0$ with
$c_{j_0}<0$ and let

$$
P(x)=\prod_{j\ne j_0}\frac{x-\alpha_j}{\alpha_{j_0}-\alpha_j}
    =\sum_{i=0}^{m-1}v_i x^i.
$$

Then $v^{\mathsf T}H^{(K)}v=c_{j_0}\alpha_{j_0}^K<0$.
Suppose a self-adjoint $B\in\mathcal S_p$, with $K\ge p$, matches just
the moments $K,K+1,\ldots,K+2m-2$. Its even power $B^K$ is positive trace
class, and $P(B)$ is bounded, self-adjoint and commutes with $B^K$.
The positive trace-class operator $B^KP(B)^2$ would have trace
$v^{\mathsf T}H^{(K)}v<0$, a contradiction.

For a prescribed moment tail starting at $R$, choose an even
$K\ge\max(2,p,R)$. This gives a finite certificate inside that tail.
It does not extend the argument to unrestricted $B$, including real normal
matrices with nonreal eigenvalues: there
$B^KP(B)^2$ need not be positive, consistently with Step 6.
The extra real-spectrum assumption is used in (4) as a real congruence;
no claim about this exact inertia formula is made for nonreal eigenvalues.

For a concrete two-dimensional symplectic monodromy
$M=\operatorname{diag}(2,1/2)$, the values
$s_2=9/4$, $s_3=49/8$ and $s_4=225/16$ give the already negative minor

$$
\det\begin{pmatrix}s_2&s_3\\s_3&s_4\end{pmatrix}
=-\frac{47}{8}<0.
$$

Thus these three moments alone exclude every self-adjoint realization for
which $B^2$ is trace class, although an unrestricted real finite matrix
can match any prescribed finite prefix. $\square$

## Corrections or missing assumptions

Invertibility and positive dimension are used: for $M=0$ in positive dimension,
the weight is $1$ at every repetition and is realized by the scalar $B=1$.
In dimension zero the same exception holds. Hyperbolicity is a sufficient
condition, not claimed necessary: the excluded example $M=I$ has all weights
zero and is realized by $B=0$.

## Open risks

- Independent verification of this full proof has not yet occurred.
- Minimal graded size is an algebraic statement over complex spaces, not a
  construction of a bounded differential or a nuclear global complex.
- Earlier symbolic P25 already has the one-dimensional contracting case.
  Admission must assess the combined all-hyperbolic/all-tail classification,
  optimal graded size, finite-prefix contrast and self-adjoint finite
  positivity certificate, not claim the pole argument
  itself is a new discovery.
- The primary operator conventions were checked against a current accessible
  primary paper; a bounded search is not a global novelty certificate.
