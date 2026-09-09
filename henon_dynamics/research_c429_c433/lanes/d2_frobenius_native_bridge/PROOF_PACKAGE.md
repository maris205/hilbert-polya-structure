# D2 proof package: native cycles are not Frobenius closed points

## Claim

Let $q=p^e$ be any odd prime power, $k=\overline{\mathbb F}_p$, and

$$
X=\{(x,y,z)\in k^3:x^2+y^2+z^2-xyz=4\}.
$$

Set $s_x(x,y,z)=(yz-x,y,z)$, $s_y(x,y,z)=(x,xz-y,z)$,
$s_z(x,y,z)=(x,y,xy-z)$, and $T=s_zs_ys_x$, rightmost first.
Arithmetic Frobenius is $\Phi_q(x,y,z)=(x^q,y^q,z^q)$.

**Theorem D2.** For every odd integer $N\ge3$ prime to $p$, choose a
primitive $N$th root of unity $\zeta_N\in k$, and put

$$
P_N=(\zeta_N+\zeta_N^{-1},2,\zeta_N+\zeta_N^{-1}),
\qquad O_N=\{T^jP_N:j\in\mathbb Z\}.
$$

Then the following statements hold.

1. $O_N$ is a finite ordinary primitive cycle in the smooth locus of
   $X$. Its least native period $n_N$ is greater than $2$, and is exactly

   $$
   n_N=\min\{n\ge1:M^n\equiv I\text{ or }-I\pmod N\},
   \qquad M=\begin{pmatrix}-1&-2\\-2&-3\end{pmatrix}.
   \tag{1}
   $$

2. For every $r\ge1$ and $s\in\mathbb Z$,

   $$
   \Phi_q^r(P_N)=T^s(P_N)
   \iff M^s\equiv q^rI\text{ or }-q^rI\pmod N.
   \tag{2}
   $$

   In particular such a relation forces

   $$
   q^{2r}\equiv(-1)^s\pmod N,
   \qquad q^{4r}\equiv1\pmod N.
   \tag{3}
   $$

   If $\Phi_q^r(O_N)=O_N$, its action on $O_N$ has order at most
   $2$. It is never transitive. Thus **no** finite extension, even one
   chosen separately for each $N$, makes $O_N$ one arithmetic closed
   point whose geometric points are precisely that native cycle.

3. Let $f_N=\min\{r\ge1:\Phi_q^r(O_N)=O_N\}$ be its Frobenius
   packet length, equivalently its minimal cycle field-of-definition
   degree. It exists and satisfies the exact criterion

   $$
   f_N=\min\{r\ge1:\exists s\in\mathbb Z,
           M^s\equiv\pm q^rI\pmod N\},
   \tag{4}
   $$

   together with the genuine lower bound

   $$
   f_N\ge\frac{\log(N+1)}{4\log q}.
   \tag{5}
   $$

   In particular the packet degrees are unbounded at every fixed $q$,
   even with $N$ restricted to odd primes different from $p$. No
   $\mathbb F_{q^r}$ makes every geometric primitive $T$-cycle stable.

4. More precisely put

   $$
   a_N=\min\{a\ge1:q^a\equiv1\text{ or }-1\pmod N\}.
   \tag{6}
   $$

   This is the arithmetic degree of $P_N$ over $\mathbb F_q$.
   One has $f_N\mid a_N\mid2f_N$. If $s_N$ is the unique residue
   modulo $n_N$ with $\Phi_q^{f_N}(P_N)=T^{s_N}(P_N)$, then

   $$
   a_N=f_N\frac{n_N}{\gcd(n_N,s_N)}.
   \tag{7}
   $$

   The packet consists of $f_N$ distinct primitive native cycles and
   $\gcd(n_N,s_N)$ arithmetic closed points, all of degree $a_N$.
   Either $s_N=0$, giving $n_N$ arithmetic owners per packet, or
   $n_N$ is even and $s_N=n_N/2$, giving $n_N/2$ owners per packet.

The word “owner” in part 4 refers only to closed points of this source
variety. It does not label rational primes or assert target Euler factors.

## Status

**PROVABLE AS STATED.** The positive compatibility proposed in the
frozen question is **refuted**, both at uniform descent and at transitive
primitive ownership. The theorem is a complete scoped counterexample
mechanism, not an all-Fricke classification or a universal arithmetic no-go.

## Assumptions and notation

All cycles are sets of distinct points; no scheme multiplicity or
characteristic-$p$ trace is used. One application of $T$ is a native tick.
$n_N$ is not the three-factor update count, $r$ is not a native iterate,
and $N$ is a torsion order, not a varying characteristic or a target
prime label. A sign $\pm$ in a matrix congruence is one common scalar
sign, not independent signs on coordinates. Arithmetic Frobenius, not
its inverse, is used throughout.

## Proof strategy and dependency map

The Cayley torus presentation is classical background; it is verified
directly here to fix descent, the quotient sign, and the ordered word.
The new test is the determinant restriction after cyclic-vector rigidity.

1. The explicit quotient gives two commuting actions on the same points.
2. The vector $v=(1,0)^t$ is cyclic for $M$ modulo every odd $N$.
3. Hence a pointwise Frobenius/native return forces a scalar **matrix**
   relation, not only an equality on one arbitrary torsion vector.
4. Determinants force order at most two on the quotient native cycle.
5. Elementary two-permutation packet bookkeeping proves the exact
   descent and ownership statements.

## Proof

### Step 1. The quotient, descent, and the native lift

Let $\mathbb T=(k^\times)^2$ and define

$$
\pi(u,v)=(u+u^{-1},v+v^{-1},uv+(uv)^{-1}).
$$

Expansion verifies that $\pi(\mathbb T)\subseteq X$. Every fibre of
$\pi$ consists exactly of $(u,v)$ and $(u^{-1},v^{-1})$, allowing these
to coincide. Indeed the first two coordinate equalities force
$u'\in\{u,u^{-1}\}$ and $v'\in\{v,v^{-1}\}$, since they are the
roots of the quadratics $t^2-xt+1$ and $t^2-yt+1$. The two potentially
different third coordinates are

$$
uv+u^{-1}v^{-1},\qquad uv^{-1}+u^{-1}v.
$$

Their difference is $(u-u^{-1})(v-v^{-1})$. If it is zero, at least
one coordinate equals its own inverse, so a mixed inversion also
represents one of the two simultaneous-inversion pairs. If it is
nonzero, the third coordinate chooses the simultaneous pair uniquely.

For completeness, this map is onto $X$: choose roots $u,v$ of the two
quadratics for prescribed $x,y$. The two displayed third coordinates
have sum $xy$ and product $x^2+y^2-4$. They therefore exhaust the roots
of $z^2-xyz+x^2+y^2-4$, which is the equation for the prescribed $z$.
Replace $v$ by $v^{-1}$ if needed. The defining expressions have
integer coefficients in Laurent coordinates, so they commute with
$\Phi_q$, including after every finite base extension.

The respective torus lifts of $s_x,s_y,s_z$ are

$$
S_x(u,v)=(uv^2,v^{-1}),\quad
S_y(u,v)=(u^{-1},u^2v),\quad
S_z(u,v)=(u,v^{-1}).
$$

For $S_x$, the second coordinate trace remains $y$, the product trace
remains $z$, and the first becomes
$uv^2+u^{-1}v^{-2}=yz-x$. For $S_y$, the first trace remains $x$,
the product trace remains $z$, and the second becomes
$u^2v+u^{-2}v^{-1}=xz-y$. For $S_z$, the first and second traces
remain $x,y$ and the product trace becomes $xy-z$.
These prove each equivariance identity without changing the word.

On column exponent vectors the three matrices are

$$
M_x=\begin{pmatrix}1&2\\0&-1\end{pmatrix},\quad
M_y=\begin{pmatrix}-1&0\\2&1\end{pmatrix},\quad
M_z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
$$

Thus $M_zM_yM_x=M$ and $\det M=-1$. Matrix multiplication has the
same rightmost-first convention as point-map composition here. The
map $T$ is defined over $\mathbb F_p$, and $T\Phi_q=\Phi_qT$.

### Step 2. Smoothness, periodicity, and a cyclic vector

Write $b=\zeta_N+\zeta_N^{-1}$. Since $\zeta_N$ has odd order
$N\ge3$, it is neither $1$ nor $-1$, and $b\ne\pm2$. At
$P_N=(b,2,b)$ the derivative in $y$ of the defining polynomial is
$4-b^2\ne0$. Thus $P_N$ is smooth. The polynomial involutions are
automorphisms of $X$, so all of $O_N$ is smooth.

The torus group $\mu_N^2$ is finite, and $M$ is invertible over
$R_N=\mathbb Z/N\mathbb Z$. Hence $T$ permutes its finite image
and $P_N$ is periodic, not merely preperiodic. Put $v=(1,0)^t$.
The fibre calculation in Step 1 gives

$$
T^n(P_N)=P_N\iff M^nv=\pm v\text{ in }R_N^2.
\tag{8}
$$

The matrix with columns $v,Mv$ is
$\left(\begin{smallmatrix}1&-1\\0&-2\end{smallmatrix}\right)$,
whose determinant $-2$ is a unit in $R_N$. It is therefore a basis
over this ring, including when $N$ is composite. If $M^nv=\epsilon v$
for a common sign $\epsilon$, commuting with $M$ gives
$M^nMv=\epsilon Mv$. Thus $M^n=\epsilon I$. This proves (1).

The off-diagonal entries of $M$ are $-2$, while

$$
M^2=\begin{pmatrix}5&8\\8&13\end{pmatrix}.
$$

Neither matrix is $I$ or $-I$ modulo an odd $N\ge3$: such an $N$
divides neither $2$ nor $8$. Therefore $n_N>2$.

### Step 3. Frobenius/native compatibility forces a scalar matrix

Frobenius sends $(\zeta_N,1)$ to $(\zeta_N^{q^r},1)$. Step 1 gives

$$
\Phi_q^r(P_N)=T^s(P_N)
\iff M^sv=\epsilon q^rv\quad(\epsilon\in\{1,-1\}).
$$

The matrix $M^s-\epsilon q^rI$ commutes with $M$, including for
negative $s$ because $M$ is invertible. As in Step 2 it kills the
basis $v,Mv$, so it is zero. The reverse implication follows by
applying the matrix congruence to $v$. This proves (2).
Taking determinants proves
$(-1)^s=(\epsilon q^r)^2=q^{2r}$ in $R_N$, and squaring gives (3).

Commutation implies $\Phi_q^r(O_N)=O_N$ exactly when
$\Phi_q^r(P_N)=T^s(P_N)$ for some $s$. On a stable cycle the action
is the single rotation $T^s$ at every point, with $s$ unique modulo
$n_N$. Equation (3) gives

$$
\Phi_q^{2r}(P_N)=\pi(\zeta_N^{q^{2r}},1)
=\pi(\zeta_N^{(-1)^s},1)=P_N.
$$

Commutation then shows that $\Phi_q^{2r}$ fixes every point of
$O_N$. A permutation of order at most two cannot act transitively
on more than two points. Since $n_N>2$, part 2 follows.
If the cycle is stable over $\mathbb F_{q^r}$, its reduced finite
subscheme splits into Frobenius closed points of degrees one or two;
it is not a single degree-$n_N$ closed point.

### Step 4. Packet degrees and the quantifier obstruction

Since $q$ is a unit modulo $N$, it has finite multiplicative order;
some power of $\Phi_q$ fixes $P_N$. The orbit of the cycle $O_N$
under Frobenius is therefore finite. Its least length is $f_N$,
and the equivalence in Step 3 proves (4). A finite set of geometric
points descends to $\mathbb F_{q^r}$ exactly when it is a union of
$\Phi_q^r$-orbits, equivalently when it is stable as a set. This
also verifies the field-of-definition interpretation; a chosen point
need not itself descend to the cycle field.

Applying (3) at $r=f_N$ shows that the positive integer
$q^{4f_N}-1$ is divisible by $N$. Consequently
$q^{4f_N}-1\ge N$, proving (5). There are arbitrarily large odd
primes different from $p$, so $f_N$ is unbounded with $q$ fixed.
For any proposed uniform extension exponent $r$, choose such an
$N>q^{4r}-1$. Equation (3) then forbids $\Phi_q^r(O_N)=O_N$.
This refutes $\exists r\ \forall O$; it does not dispute the true
finite-packet statement $\forall O\ \exists r$.

### Step 5. Exact primitive ownership within a packet

The fibre criterion gives (6) as the exact point degree. More
generally consider any commuting permutations $T,\Phi$ of a set,
and a primitive $T$-cycle $O$ of length $n$ whose Frobenius packet
has finite length $f$. Choose $P\in O$ and the unique $s\pmod n$
with $\Phi^fP=T^sP$.
If $\Phi^aP=P$, then $\Phi^aO=O$, so $f\mid a$. Write $a=ft$.
Commutation gives $\Phi^{ft}P=T^{st}P$, which equals $P$ exactly
when $n\mid st$. The least positive $t$ is $n/\gcd(n,s)$.
Every point in the packet is $\Phi^jT^iP$ for some $j,i$; both
commuting permutations preserve its Frobenius period. Thus all
arithmetic point-orbits in the packet have length
$a=fn/\gcd(n,s)$, and their number is $fn/a=\gcd(n,s)$.
This proves (7) and the packet assertion without a cohomological trace.

For $O_N$, Step 3 gives $2s_N=0\pmod {n_N}$. Its two possibilities
are $s_N=0$, or $n_N$ even and $s_N=n_N/2$. Formula (7) gives
$a_N=f_N$ or $a_N=2f_N$, respectively. This proves all of part 4.
The two possibilities are alternatives, not a claim that both occur
for every $(q,N)$. All claims of Theorem D2 are now proved. $\square$

## Corrections, boundary cases, and reusable interface

- Excluding even $N$ is essential to this cyclic-vector proof because
  its basis determinant is $-2$. No claim about the omitted even-torsion
  stratum is needed for the counterexample to a universal bridge.
- Excluding $p\mid N$ ensures ordinary primitive roots of order $N$
  exist. No nonreduced $p$-power group scheme is substituted.
- The source surface is singular, but all witnesses and their native
  cycles lie in its smooth locus. Thus removing the four nodes does
  not repair the proposed bridge.
- A Frobenius/native equivariant bijection preserving primitive cycles
  transports their packet degree, native length, and rotation order.
  It therefore preserves this obstruction. A semiconjugacy which merges
  cycles, or a changed descent datum involving an additional $T$-twist,
  is outside that interface and would need a new contract.
- More generally, for a rank-two monomial map with exponent matrix
  $A\in\mathrm{GL}_2(\mathbb Z)$ and a torsion exponent vector $v$
  with $\det[v,Av]$ a unit modulo $N$, an equality on the simultaneous-
  inversion quotient forces $A^s=\pm q^rI$ and hence
  $q^{2r}=\det(A)^s$. This is the exact hypothesis to check before
  transferring the argument to another word or torus factor.

## Source and open-risk boundary

The torus quotient and its monomial equivariance are not new. They are
documented in Cantat–Loray, *Holomorphic dynamics, Painlevé VI equation
and character varieties*, §2.1 of the [author preprint](https://arxiv.org/pdf/0711.1579),
and Cerbu–Gunther–Magee–Peilen, *The cycle structure of a Markoff
automorphism over finite fields*, §3.3/Lemma 3.3 of the
[served arXiv v2](https://arxiv.org/pdf/1610.07077).
The direct proof above fixes sign and matrix conventions and does not
import a complex-analytic theorem into positive characteristic.

The determinant obstruction is an elementary consequence of that
classical linearization plus a cyclic-vector condition. This package
does not certify worldwide priority or independent paper-level
substance. A nonauthor review is requested from the coordinator and
has not been claimed to have occurred. No mathematical program ran.
No target Euler weights, target determinant, root number, automorphy,
zero/divisor correspondence, or Hilbert–Pólya claim is supplied.
