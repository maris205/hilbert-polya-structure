# CTM: complete one-step inverse, incomplete global time axis

Author: `/root/twenty_eighth_finite_scout`. No independent review claimed.

## Claims and status

**PROVABLE AS STATED:** the full-carrier coordinate update, the surjective
parameterized cubic trace factor, the full one-step source decoder and its
evaluated kernel, and the zero-target fibre formula below.

**NOT CURRENTLY JUSTIFIED:** a complete all-$q$ temporal/recurrent theorem
for CTM on $M_2(\mathbb F_q)$, a sharp global entrance clock, a global
maximum-fibre theorem or a fresh two-axis admission contract.

Assume throughout that $q$ is an odd prime power. The only literal rule is
that in INTAKE.md. Every algebraic calculation is over $\mathbb F_q$.
There is no premise from a finite pilot. The dependency chain is:
invertible entry coordinates and Cayley--Hamilton -> coordinate equations
-> trace factor and inverse scalar choices -> linear/conic branches ->
zero fibre by an independent rank-one image-line argument.

## 1. Exact full-carrier coordinates

For $A=\begin{psmallmatrix}a&b\\c&e\end{psmallmatrix}$ put

$$s=a+e,\quad k=b-c,\quad u=a-e,\quad v=b+c,\quad d=ae-bc.$$

The first four coordinates are a bijection with $\mathbb F_q^4$:

$$A=\frac12\begin{pmatrix}s+u&v+k\\v-k&s-u\end{pmatrix},
\qquad 4d=s^2+k^2-u^2-v^2. \tag{1}$$

The inverse uses the invertibility of $2$, which is why even $q$ is not
in the contract. Cayley--Hamilton for a $2\times2$ matrix gives
$A^2=sA-dI$, hence

$$T(A)=sA^{\mathsf T}A-dA^{\mathsf T}. \tag{2}$$

Direct multiplication gives

$$\operatorname{tr}(A^{\mathsf T}A)=s^2-2d+k^2,$$
$$ (A^{\mathsf T}A)_{11}-(A^{\mathsf T}A)_{22}=su-kv,$$
$$ (A^{\mathsf T}A)_{12}+(A^{\mathsf T}A)_{21}=sv+ku.$$

Writing the next coordinates with primes, (2) and determinant
multiplicativity give the exact identities

$$d'=d^3,\qquad k'=dk,\qquad s'=s(s^2-3d+k^2), \tag{3}$$
$$\begin{pmatrix}u'\\v'\end{pmatrix}
=\begin{pmatrix}s^2-d&-sk\\sk&s^2-d\end{pmatrix}
\begin{pmatrix}u\\v\end{pmatrix}. \tag{4}$$

In particular (4) is linear only after specifying the *moving* scalar
coordinates; it is not a full-carrier fixed-parameter linearization.
No claim excluding every possible conjugacy is made.

## 2. The determinant factor does not settle time

For each $k_0\in\mathbb F_q$, let

$$X_{k_0}=\{A:d=1,\ k=k_0\}.$$

Equation (3) proves that this set is invariant and that trace intertwines
its update with

$$f_{k_0}(s)=s^3+(k_0^2-3)s. \tag{5}$$

Trace is surjective on this stratum. To prove that assertion, fix any
$s\in\mathbb F_q$ and set $R=s^2+k_0^2-4$. The set of squares in an odd
finite field, including zero, has $(q+1)/2$ elements: each nonzero square
has exactly two roots, paired by sign. Therefore the sets
$\{u^2:u\in\mathbb F_q\}$ and $\{R-v^2:v\in\mathbb F_q\}$ have sizes
whose sum is $q+1$. They intersect. Choose $u,v$ with $u^2+v^2=R$;
(1) then gives a matrix with the required trace, determinant and skew.
This proves a genuine onto factor on the entire $q$-element scalar carrier,
not a sparse orbit observation.

Equation (5) is an obligation, not a solution of its cycle structure.
For special coefficients it can simplify, but no special-$k$ restriction
is proposed as a fresh candidate. Nor is this a claim that every cubic
polynomial occurs: the coefficients here are specifically $k_0^2-3$.
An all-size classification of these factors and their matrix lifts has
not been proved in this desk. Finiteness alone supplies no qualifying axis.

For contrast, the singular sector has a spent power mechanism. If $d=0$,
then $B=T(A)=sA^{\mathsf T}A$ is symmetric of rank at most one. Thus
$T(B)=B^3$, and induction gives

$$T^t(A)=B^{3^{t-1}}\quad(t\ge1). \tag{6}$$

If $r=\operatorname{tr}B\ne0$, then $B^2=rB$, $P=B/r$ is idempotent,
and (6) is $r^{3^{t-1}}P$. If $r=0$, Cayley--Hamilton gives $B^2=0$,
so $T^2(A)=0$. These formulas include $B=0$. They use elementary matrix
and scalar powering, and classify no invertible source with $d\ne0$.
The invariant singular-sector restriction is not promoted into a paper.

## 3. Every target's one-step source set

Let an arbitrary target $Y$ have coordinates $(S,K,U,V)$ as in (1),
and determinant $D$. Choose triples $(d,k,s)\in\mathbb F_q^3$ satisfying

$$d^3=D,\qquad dk=K,\qquad s(s^2-3d+k^2)=S. \tag{7}$$

For each triple put

$$\alpha=s^2-d,\qquad \beta=sk,\qquad
R=s^2+k^2-4d,\qquad \Delta=\alpha^2+\beta^2.$$

Take precisely the pairs $(u,v)\in\mathbb F_q^2$ satisfying

$$\alpha u-\beta v=U,\qquad \beta u+\alpha v=V,
\qquad u^2+v^2=R. \tag{8}$$

For every such tuple reconstruct $A$ by (1). This is a bijection onto
$T^{-1}(Y)$.

Necessity follows from (1), (3) and (4). For sufficiency, the norm equation
in (8) says that the reconstructed matrix has determinant exactly the
chosen $d$. Equations (7)--(8), inserted into (3)--(4), then give exactly
the four target coordinates. Coordinate inversion identifies that output
with $Y$. A source recovers its unique $s,k,u,v,d$, proving disjointness
across all scalar choices and no overcounting. This includes $D=0$,
$d=0$, zero traces, isotropic sources and unreachable targets.

This decoder is target-local: it is not an enumeration of every source
matrix followed by application of the original map. Its scalar-root and
quadratic-form primitives are assigned no novelty credit.

## 4. Evaluated kernel in the full inverse

Let $N_q(\alpha,\beta,R;U,V)$ count (8). Summing the following explicit
kernel over the triples in (7) gives $|T^{-1}(Y)|$ for every target.

### 4.1 Invertible linear branch

If $\Delta\ne0$, the sole possible pair is

$$u=(\alpha U+\beta V)/\Delta,\qquad
v=(-\beta U+\alpha V)/\Delta.$$

The kernel is one when its squared norm is $R$, and zero otherwise.
This follows by multiplying the inverse of the displayed $2\times2$
matrix in (4), followed by the sole remaining equation.

### 4.2 Zero linear branch

If $\alpha=\beta=0$, the kernel vanishes unless $U=V=0$. In that case,
write $\epsilon=\chi(-1)\in\{1,-1\}$ for the quadratic character of $-1$.
The exact kernel is

$$C_q(R)=\begin{cases}
q+(q-1)\epsilon,&R=0,\\
q-\epsilon,&R\ne0.
\end{cases} \tag{9}$$

For $R=0$, a nonzero $u$ permits two $v$ when $-1$ is square and none
otherwise; the zero pair contributes one. For $R\ne0$, the invertible
change $(x,y)\mapsto(x-y,x+y)$ bijects solutions of $x^2-y^2=R$ with
pairs of nonzero factors of $R$, so there are $q-1$ solutions. Counting
the same solutions by $x$ gives
$\sum_x\chi(x^2-R)=-1$, with $\chi(0)=0$. Consequently
$\sum_u(1+\chi(R-u^2))=q-\chi(-1)$, which proves (9).

### 4.3 Rank-one isotropic linear branch

Suppose $\Delta=0$ and $(\alpha,\beta)\ne(0,0)$. Then both $\alpha$
and $\beta$ are nonzero. The two linear equations are consistent exactly
when $\alpha V=\beta U$, because the second matrix row is $\beta/\alpha$
times the first. If that condition fails, the kernel is zero.

Under consistency, substitute $u=(U+\beta v)/\alpha$. Since
$\alpha^2+\beta^2=0$, the norm equation becomes

$$U^2+2U\beta v=\alpha^2 R. \tag{10}$$

If $U\ne0$, its coefficient of $v$ is nonzero and the kernel is exactly
one. If $U=0$, consistency also gives $V=0$. The kernel is then $q$ for
$R=0$ and zero for $R\ne0$. This handles every singular coefficient
case, including characteristics dividing $3$; only odd characteristic was
used. Thus (7), (9) and the three branches are an evaluated complete
one-step count, not an unclassified conic equation.

## 5. Independent exact zero-target fibre

**Theorem.** For every odd $q$,

$$|T^{-1}(0)|=\begin{cases}
q^2,&-1\text{ is nonsquare in }\mathbb F_q,\\
3q^2-2q,&-1\text{ is square in }\mathbb F_q.
\end{cases} \tag{11}$$

If $T(A)=0$, its determinant $d^3$ vanishes, hence $d=0$. By (2),
$T(A)=sA^{\mathsf T}A$. First count $s=d=0$. Such a matrix is
$\begin{psmallmatrix}a&b\\c&-a\end{psmallmatrix}$ with $bc=-a^2$.
At $a=0$, there are $2q-1$ pairs $(b,c)$. For each nonzero $a$,
there are $q-1$ choices of nonzero $b$ and a unique $c$. The count is
$(2q-1)+(q-1)^2=q^2$. Every such matrix has square zero and is a source
of the zero target.

It remains to count $d=0$, $s\ne0$ sources with $A^{\mathsf T}A=0$.
They have rank one. Fix their image line and a nonzero representative
$w\in\mathbb F_q^2$; every matrix with that image line has a unique
form $A=wr^{\mathsf T}$ for a nonzero row vector $r^{\mathsf T}$.
Then

$$A^{\mathsf T}A=(w^{\mathsf T}w)rr^{\mathsf T},\qquad
\operatorname{tr}A=r^{\mathsf T}w.$$

The matrix $rr^{\mathsf T}$ is nonzero, since a nonzero coordinate of $r$
has nonzero square. The image line must therefore be isotropic for the
standard dot product. In dimension two there are no isotropic lines when
$-1$ is nonsquare, and exactly two when $-1$ is square: a nonzero
isotropic vector has nonzero first coordinate and slope solving $z^2=-1$.

For each such line, the nonzero linear functional $r\mapsto r^{\mathsf T}w$
has $q$ vectors in its kernel and $q^2-q=q(q-1)$ vectors outside. The
latter are exactly the required nonzero-trace matrices. Different image
lines give disjoint sources, and these sources are disjoint from the
$s=0$ branch. Adding their counts proves (11). ∎

The theorem identifies one complete target fibre, not the maximum over
all targets. The full decoder does not supply an evaluated sharp maximum
without a separate comparison across (7). No such extremal claim is made.

## Open risks and author disposition

The full invertible temporal/recurrent structure remains unproved; so do
the global sharp clock and maximum-fibre classification. The primary and
internal collision search is bounded and does not establish direct-owner
clearance. The correct inverse and singular-sector identities do not
replace the missing full-carrier time axis. **HOLD_PROOF_SOURCE /
NO_PROMOTION** is the author handoff. No pilot or independent gate is
recommended merely to turn this negative boundary into a seat.
