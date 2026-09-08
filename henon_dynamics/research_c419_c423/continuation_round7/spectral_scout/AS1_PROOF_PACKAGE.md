# AS1 seventh attempt: the entire finite-character tower and its exact radial residues

2026-09-08 UTC. AI-assisted proof draft, not yet independently reviewed.
This continues one old full question; it does not create a new paper slot.

## Original claim and status

The original [AS1 contract](../../arithmetic_spectral/FROZEN_CONTRACTS.md)
asks for the full meromorphic-continuation behavior of the switching-solenoid
zeta function at $|z|=R=(8\varphi)^{-1}$. Its status here is
**NOT CURRENTLY JUSTIFIED**: this document does not settle the entire circle.

The new auxiliary claims below are **PROVABLE AS STATED**. They establish
the peripheral spectrum at every finite congruence depth, exact parity
limits, and the radial residues of the complete weighted sum. In particular,
the previously proposed dense-nonzero-radial-residue route cannot work at
any depth. Finite-character approximation of prescribed length phases is
also proved, but is not promoted to spectral or analytic continuation.

No mathematical program was executed. The old six-layer computations and
two-real-point proof are not rerun. All arguments below are exact hand proofs.

## Assumptions, notation and inherited inputs

Use $A=\left(\begin{smallmatrix}3&1\\1&3\end{smallmatrix}\right)$,
$B=\left(\begin{smallmatrix}3&2\\2&4\end{smallmatrix}\right)$, and
chronological products $M_w=M_{w_n}\cdots M_{w_1}$ of based words of
length $n\geq1$. Both determinants are $8$. A word is active precisely
when it has no cyclic adjacent $aa$. Let $\mathcal W_n$ be these words.
The same native clock and based-word counting convention are kept.

From the [previous proof and its C14 inputs](../../arithmetic_spectral/solenoid_review/PROOF_STATUS.md),
we import, without reproving their old checks,

$$
L_n=|\mathcal W_n|=\varphi^n+(-\varphi^{-1})^n,
\quad \operatorname{tr}M_w\equiv(-1)^n\pmod8,
\quad D_w=\det(I-M_w)>0,
$$

where $\varphi=(1+\sqrt5)/2$. Define

$$
b_{n,k}=\#\{w\in\mathcal W_n:v_2(D_w)\geq k\},\qquad
a_n=\sum_{k\geq1}2^{-k}b_{n,k}.
$$

The inherited analytic decomposition is

$$
Z_2(z)=Z_\infty(z)e^{-G(z)},\qquad
G(z)=P(8\varphi z)+E(z),\qquad
P(u)=\sum_{n\geq1}a_n\varphi^{-n}u^n/n,
$$

where $E$ is holomorphic on a disk strictly larger than $|z|\leq R$, and
$Z_\infty$ is rational and nonzero and finite on $|z|=R$. Existing
nonmeromorphic behavior at $\pm R$ is retained, not counted anew.

For $k\geq1$ put $U_k=(\mathbb Z/2^k\mathbb Z)^\times$ and
$H_k=\operatorname{image}(1+8\mathbb Z_2\to U_k)$. A character always
means a homomorphism $U_k\to S^1$, not a character of the underlying
additive ring. Write $\widehat U_k$ for all these characters.

## Dependency map

1. Elementary characteristic-root and norm arguments give a length
   relation for the unit roots $\lambda_w$.
2. Finite-character orthogonality and a positive trigonometric kernel give
   simultaneous approximation of finitely many length phases.
3. Contracting fractional-linear maps give an exact, all-$n$ finite
   transfer trace for $\chi(\lambda_w)$, not the old scalar-resolvent graph.
4. Equality in the Perron bound, using only the cycles $b$ and $ab$,
   determines every finite-depth peripheral character and eigenvalue.
5. Character orthogonality, a dominated parity limit and Abel summation
   yield the exact radial residues of the full weighted series.
6. The passage to meromorphic continuation at all other directions
   remains a separate, unresolved assertion.

## 1. Unit roots, irrationality and the algebraic length relation

For $w\in\mathcal W_n$ the characteristic polynomial
$X^2-t_wX+8^n$, with $t_w=\operatorname{tr}M_w$ odd, has exactly one
odd root $\lambda_w\in\mathbb Z_2^\times$ and one even root
$\mu_w\in2\mathbb Z_2$. Indeed its two roots modulo $2$ are $1$ and
$0$, and the derivative $2X-t_w$ is odd at both; successive binary
lifting gives one root in each residue class. Their product gives
$\mu_w=8^n/\lambda_w$. Consequently

$$
v_2(D_w)=v_2(1-\lambda_w),\qquad
\lambda_w\equiv(-1)^n\pmod8.                 \tag{1.1}
$$

Here $1-\mu_w$ is a unit, which proves the valuation equality for every
$n,k$ without a short-length correction.

These roots are quadratic irrational algebraic integers. To check this
point rather than assume it, both matrices have least real singular value
at least $c=(7-\sqrt{17})/2>1$ (the least value for $A$ is $2$).
Thus $\|M_wv\|_2\geq c^n\|v\|_2$. The entries of $M_w$ are
positive. Writing them as $a,b,c',d$, its characteristic discriminant is
$(a-d)^2+4bc'>0$, its trace is positive and its determinant is positive.
Both real eigenvalues are therefore positive and, by the singular-value
inequality applied to an eigenvector, greater than $1$.

A rational $\lambda_w$ would be an integer dividing $8^n$. Since it is
odd, it would be $1$ or $-1$, contrary to those real eigenvalues. Its
degree is two and

$$N_{\mathbb Q(\lambda_w)/\mathbb Q}(\lambda_w)=8^n.\tag{1.2}$$

**Length-relation lemma.** For finitely many active words $w_j$ of
lengths $n_j$ and integers $e_j$,

$$\prod_j\lambda_{w_j}^{e_j}=1\quad\Longrightarrow\quad
\sum_j e_j n_j=0.                              \tag{1.3}$$

All the chosen roots lie in one number field
$K=\mathbb Q(\lambda_{w_1},\ldots,\lambda_{w_m})\subset\mathbb Q_2$.
By the tower law for the field norm, (1.2) gives
$N_{K/\mathbb Q}(\lambda_{w_j})=8^{n_j[K:\mathbb Q]/2}$.
Take the norm of the proposed multiplicative relation. The resulting
positive real power of $8$ is $1$ only when (1.3) holds. Negative $e_j$,
repeated words, shared quadratic fields and repetitions of a primitive
word cause no change in this argument. $\square$

## 2. Finite-character approximation: the exact limited statement

For any finite $w_1,\ldots,w_m$, any $\theta\in\mathbb R$, and any
$\varepsilon>0$, there are $k\geq1$ and $\chi\in\widehat U_k$ with

$$\max_j|\chi(\lambda_{w_j}\bmod2^k)-e^{i\theta n_j}|<\varepsilon.
                                                               \tag{2.1}$$

Here the depth may depend on the whole finite family and the accuracy;
there is no upper bound relating it to the longest word.

For completeness, the character-density step can be proved using only
finite orthogonality. Set $t_j=e^{i\theta n_j}$, and let $E_k\subset
(S^1)^m$ be the evaluation vectors of characters of $U_k$. Inflation
gives $E_k\subset E_{k+1}$. For any integer vector $\nu$, the average
of $x^\nu$ over $E_k$ is $1$ if
$\prod_j\lambda_{w_j}^{\nu_j}\equiv1\pmod{2^k}$, and $0$ otherwise.
The limit of these averages is therefore $1$ exactly for the exact
multiplicative relations. For those relations (1.3) implies $t^\nu=1$.

Suppose all $E_k$ avoid the neighborhood
$V=\{x:|x_j/t_j-1|<\varepsilon\text{ for all }j\}$; taking
$0<\varepsilon\leq1$ loses no generality. Choose an integer $s$ with
$2s>m$. For an integer $N\geq1$ put

$$
K_N(z)=C_N^{-1}|1+z+\cdots+z^{N-1}|^{2s},\qquad
C_N=[z^0]|1+z+\cdots+z^{N-1}|^{2s}.
$$

This Laurent polynomial has nonnegative real coefficients and constant
coefficient $1$. If $a_j$ are the coefficients of
$(1+z+\cdots+z^{N-1})^s$, then $C_N=\sum_j a_j^2$,
$\sum_j a_j=N^s$, and there are at most $sN$ indices. Cauchy--Schwarz
gives $C_N\geq N^{2s-1}/s$. Hence $K_N(z)\leq sN$ on $S^1$ and,
when $|z-1|\geq\varepsilon$,

$$K_N(z)\leq s(2/\varepsilon)^{2s}N^{-(2s-1)}.$$

The product $\prod_jK_N(x_j/t_j)$ is consequently at most
$s^m(2/\varepsilon)^{2s}N^{m-2s}$ outside $V$, which tends to zero.
On the other hand, for each fixed $N$ its average over $E_k$, as
$k\to\infty$, is the sum of its nonnegative coefficients supported on
exact multiplicative relations: all corresponding $t^{-\nu}$ equal $1$.
That limit is at least its constant coefficient $1$. Choosing $N$ large
contradicts avoidance of $V$. This proves (2.1). $\square$

This is an elementary version of compact character duality. It is not a
new duality theorem. It asserts neither a common fixed finite character
for infinitely many words nor operator-norm approximation of a cocycle.

## 3. An exact projective transfer trace at every depth

Use the projective vector $(1,r)^T$, $r\in\mathbb Z_2$. Define

$$
f_B(r)=\frac{2+4r}{3+2r},\quad h_B(r)=3+2r;
\qquad
f_A(r)=\frac{1+3r}{3+r},\quad h_A(r)=3+r\quad(r\text{ even}).
                                                               \tag{3.1}
$$

$B$ is allowed at every state and sends it to an even state. $A$ is
allowed only at even states and sends them to odd states. All displayed
denominators and multipliers are odd on these domains. For $C=A$ on its
domain, or $C=B$ everywhere,

$$f_C(r)-f_C(s)=\frac{8(r-s)}{h_C(r)h_C(s)}.       \tag{3.2}$$

Thus each allowed step contracts $2$-adic distance by $2^{-3}$.
The maps and multipliers reduce well modulo $2^k$.

On functions on $X_k=\mathbb Z/2^k\mathbb Z$ define the finite matrix

$$
(T_{\chi,k}F)(r)=\chi(h_B(r))F(f_B(r))+
\mathbf1_{r\ {\rm even}}\chi(h_A(r))F(f_A(r)).    \tag{3.3}
$$

Parallel edges, if present, are added, not identified. Its dimension is
$2^k$. Let $S_k=T_{1,k}$; these are new projective matrices, not the
old full-product residue matrices denoted by the same letter elsewhere.

Every closed walk has an active word, because an $A$ step goes to an
odd state, where another $A$ is forbidden, including at the cyclic join.
Conversely every active word has exactly one projective closed walk at
every depth. For a word starting with $A$, cyclic admissibility forces
its last letter to be $B$, and its product maps even states to even
states. If it starts with $B$, its first step is defined on every state;
its image has a fixed parity. In each case iteration takes place on an
invariant complete parity ball after at most one step. Formula (3.2)
gives a unique $2$-adic fixed point. At finite depth, any two possible
fixed residues would satisfy that their difference is divisible by
$2^{3n}$ times itself, and thus would coincide modulo $2^k$.
Binary reduction of the $2$-adic fixed point supplies existence.

Along the closed walk the product of the $h$ multipliers is the odd
eigenvalue of $M_w$ modulo $2^k$, hence is $\lambda_w\bmod2^k$.
The uniqueness of the odd characteristic root at finite depth follows
from the same binary lifting used in Section 1. Expanding the trace by
closed walks now gives, for every $n\geq1$,

$$\operatorname{Tr}(T_{\chi,k}^n)=
\sum_{w\in\mathcal W_n}\chi(\lambda_w\bmod2^k).  \tag{3.4}$$

This counts based words, including repetitions, exactly once each.
Using (1.1) and character orthogonality yields the all-length identity

$$b_{n,k}=\frac1{|U_k|}\sum_{\chi\in\widehat U_k}
\operatorname{Tr}(T_{\chi,k}^n).                 \tag{3.5}$$

No short-length determinant correction is required in (3.5).

## 4. Complete finite-depth peripheral spectrum

**Theorem.** For every $k$ and $\chi\in\widehat U_k$:

1. Every eigenvalue of $T_{\chi,k}$ has modulus at most $\varphi$.
2. An eigenvalue of modulus $\varphi$ exists if and only if $\chi$ is
   trivial on $H_k$.
3. In that case the only such eigenvalue is
   $\varphi\chi(-1)$; it is algebraically simple. All remaining
   eigenvalues have strictly smaller modulus.

**Proof.** Put $v(r)=\varphi$ for even $r$ and $v(r)=1$ for odd $r$.
The allowed transitions give $S_kv=\varphi v$. Therefore (3.3) has
operator norm at most $\varphi$ in the weighted supremum norm
$\max_r|F(r)|/v(r)$.

The directed graph of $S_k$ has exactly one closed strongly connected
component $C_k$. Indeed $B^\ell$ sends every state to the same fixed
residue $r_B$ for $3\ell\geq k$, by contraction. Any closed component
must contain $r_B$. The component containing $r_B$ is closed: a successor
of $r_B$ or of any state reachable from it can return to $r_B$ by
$B^\ell$. This also proves uniqueness. It is aperiodic, since the
$B$ edge at $r_B$ is a self-loop.

Every active periodic word has its unique projective cycle inside
$C_k$. Start at the even state $r_B$, apply the word repeatedly, and
use (3.2) until the fixed residue is reached. Starting with $A$ is
allowed there, and cyclic admissibility permits all repetitions.

Suppose $T_{\chi,k}F=\varphi e^{i\theta}F$ with $F\neq0$.
At a state maximizing $|F|/v$, equality in the weighted triangle
inequality forces every successor to maximize it too. Such states
therefore include $r_B$ and all of $C_k$. Writing $g=F/v$ on $C_k$,
the equality conditions for each edge $r\stackrel{C}{\longrightarrow}r'$
are

$$\chi(h_C(r))g(r')=e^{i\theta}g(r),             \tag{4.1}$$

with $|g|$ a positive constant. Multiplication along any closed walk
gives $\chi(\lambda_w)=e^{in\theta}$.

Apply this to $b$ and $ab$. Their unit roots have characteristic
polynomials $X^2-7X+8$ and $X^2-25X+64$, respectively. Unique binary
lifting gives

$$\lambda_b\equiv15\pmod{16},\qquad
\lambda_{ab}\equiv9\pmod{16},\qquad
g_0:=\lambda_b^2/\lambda_{ab}\equiv9\pmod{16}.    \tag{4.2}$$

Equation (4.1) forces $\chi(g_0)=1$. The image of $g_0$ generates
$H_k$. To verify this for $k\geq4$, start with $v_2(g_0-1)=3$.
For $x\equiv1\pmod8$,
$v_2(x^2-1)=v_2(x-1)+1$ because $v_2(x+1)=1$.
Induction gives $v_2(g_0^{2^j}-1)=3+j$, so its order modulo $2^k$
is $2^{k-3}=|H_k|$. For $k\leq3$, $H_k$ is trivial. It follows that
$\chi|_{H_k}=1$. Since $\lambda_b\in-(1+8\mathbb Z_2)$,
$e^{i\theta}=\chi(\lambda_b)=\chi(-1)\in\{1,-1\}$.

For the converse let $\chi|_{H_k}=1$ and set $\epsilon=\chi(-1)$.
By (1.1), the product of $\chi(h_C)/\epsilon$ on every closed walk
in $C_k$ is $1$. This edge cocycle is a coboundary. Explicitly choose
paths from a fixed vertex to each other vertex and define the value
of a diagonal gauge by the path product. If two such paths differ,
append one return path; the two resulting closed walks both have
product $1$, proving independence of the chosen path. Gauging (3.3)
on $C_k$ therefore gives exactly $\epsilon S_k|_{C_k}$.

Perron--Frobenius for this finite irreducible aperiodic nonnegative
matrix gives a simple eigenvalue $\varphi$ and strictly smaller
modulus for its others. No transient block has spectral radius
$\varphi$: the same maximum-norm equality would force a maximizing
state forward to $r_B$, contrary to a transient-supported eigenvector
whose closed-component entries are zero. Equivalently one applies
the strict Perron inequality to a transient component with an exiting
edge. Finite block triangularity then proves the assertion, including
algebraic simplicity for the full matrix. $\square$

There is a useful distinction from Section 2. For $\theta\notin\pi
\mathbb Z$, a sequence satisfying (2.1) for increasingly accurate
approximations to just $b,ab$ must have unbounded conductors. Otherwise
finitely many characters give a constant subsequence, whose exact
limit would violate (4.2). Approximation on finite word sets and exact
finite-depth peripheral eigenvalues are different assertions.

## 5. Exact parity limits and full weighted radial residues

For fixed $k$, the theorem and (3.5) give a number $\rho_k<\varphi$
such that

$$
b_{n,k}=d_{n,k}\varphi^n+O(2^k\rho_k^n),\qquad
d_{n,k}=\frac1{|U_k|}\sum_{\chi|_{H_k}=1}\chi(-1)^n.\tag{5.1}
$$

The error estimate follows by summing the remaining eigenvalues with
their algebraic multiplicities. Trace of a Jordan block contributes
only its size times the eigenvalue to the $n$th power, so no unproved
diagonalizability is used. There are $2^k$ eigenvalues per character.
No uniform bound for $\rho_k$ as $k\to\infty$ is asserted.

The finite character sum in (5.1) is

$$
\begin{array}{c|cc}
 &n\text{ odd}&n\text{ even}\\\hline
k=1&1&1\\
k=2,3&0&1\\
k\geq4&0&2^{3-k}.
\end{array}                                                    \tag{5.2}
$$

For example, for $k\geq3$ there are four characters trivial on $H_k$,
half taking each sign at $-1$, while $|U_k|=2^{k-1}$. The smaller
groups $U_1,U_2$ have sizes $1,2$ and give the first two cases.

The bound $0\leq b_{n,k}\varphi^{-n}\leq L_n\varphi^{-n}\leq2$
permits dominated passage through the sum defining $a_n$, separately
along the two parities. Consequently

$$
\lim_{\substack{n\to\infty\\n\text{ odd}}}a_n\varphi^{-n}=\frac12,
\qquad
\lim_{\substack{n\to\infty\\n\text{ even}}}a_n\varphi^{-n}
=\frac12+\frac14+\frac18+\sum_{k\geq4}2^{3-2k}
=\frac{11}{12}.                                                \tag{5.3}
$$

In particular

$$a_n\varphi^{-n}=\frac{17}{24}+\frac5{24}(-1)^n+\eta_n,
\qquad\eta_n\longrightarrow0.                                 \tag{5.4}$$

Let $Q(u)=uP'(u)$. For every $\zeta\in S^1$, (5.4) yields

$$
\lim_{r\uparrow1}(1-r)Q(r\zeta)=
\begin{cases}
17/24,&\zeta=1,\\
5/24,&\zeta=-1,\\
0,&\zeta\notin\{1,-1\}.
\end{cases}                                                     \tag{5.5}
$$

To justify the remainder uniformly in the direction, its absolute
contribution is bounded by $(1-r)\sum_{n\geq1}|\eta_n|r^n$, which
tends to zero: split at a fixed index and then make the tail uniformly
small using $\eta_n\to0$. The two constant-parity terms are geometric
series and give exactly (5.5).

Logarithmic integration also gives
$P(r)/\log(1/(1-r))\to17/24$ and
$P(-r)/\log(1/(1-r))\to5/24$: the $\eta_n$ contribution divided by
that logarithm tends to zero by the same fixed-head/small-tail split.
These sharpen the old bounds at the two real points; they are not
two new paper contracts.

## 6. What is now eliminated, and what remains open

The set of nonzero aggregate radial residues is **exactly** $\{1,-1\}$.
Thus the old sufficient closure proposal—dense nonzero aggregate
radial residues at deeper congruence levels—is false for this fixed
system. This is an all-depth proof, not extrapolation from the six
old matrices. It does not contradict those exact finite computations.

The original full-circle question remains open here. A zero radial
residue does not imply holomorphic continuation. Conversely poles
of finite-layer determinants outside the disk cannot simply be
declared poles of an infinite weighted sum. Section 2 supplies neither
a conductor-versus-memory bound for the projective cocycle nor a
uniform norm estimate for (3.3). The new matrices have growing size;
matching a finite set of periodic traces does not fill either gap.

A completion would need, for example, a justified uniform spectral /
resolvent estimate and convergence domain across nonreal arcs, or an
independent proof that accumulating singularities survive the full
sum there. None is supplied. In particular (5.4) gives $\eta_n\to0$,
not exponential decay, and does not enlarge the convergence disk.

## Scope and ownership

Field norms, finite character orthogonality, the character-density
principle, fractional-linear contraction, finite graph coboundaries
and Perron--Frobenius theory are classical inputs/methods. The new local
application is their explicit combination for these two fixed matrices,
with the all-depth character criterion and constants (5.3)--(5.5).
The original C14 definitions and earlier AS1 proofs are credited above.
No claim of worldwide priority, formal Route-A promotion, target Euler
factors, root numbers or zero correspondence is made.

Current disposition: retain the proved auxiliary classification and
the eliminated old closure mechanism; **do not admit AS1 as a complete
paper**. Independent internal checking is still pending at this draft.
