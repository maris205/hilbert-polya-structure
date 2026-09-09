# Unicritical polynomial Livšic: a same-paper carry extension

2026-09-09 UTC. Current-team author proof in the allocated R4 directory.
The admitted quadratic theorem and its proof remain frozen. The present
generalization and its finite certificate are not a second contract.

## Claim

Let $p$ be an odd prime, $k=\overline{\mathbb F}_p$, $d\ge2$ an
integer with $d\not\equiv1\pmod p$, and $c\in k$. Put

$$f(x)=x^d+c,\qquad \Delta Q=Q\circ f-Q,\qquad B_f=\Delta k[x].$$

For an ordinary primitive $f$-cycle $O$, let
$S_h(O)=\sum_{a\in O}h(a)$, counting each distinct point once,
and define $K_f=\{h\in k[x]:S_h(O)=0\text{ for every }O\}$.
Then

$$K_f=B_f.\tag{U1}$$

The initially allocated range $p\nmid d(d-1)$ is proved by the
$d$-ary carry argument. The coordinator subsequently authorized
including the separate elementary branch $p\mid d$; together they
give the range stated above. This authorization does not modify the
frozen quadratic contract.

For any integer $M\ge1$ and $h\in k[x]$ of degree at most $M$
(including zero), define

$$n_M=3\lfloor\log_d M\rfloor+4,\qquad
F_j=f^{\circ j}-x,\qquad
\widetilde H_j(h)=\sum_{i=0}^{j-1}h\circ f^{\circ i}.$$

The following three conditions are equivalent:

1. $h\in B_f$.
2. $F_j\mid F_j'\widetilde H_j(h)$ for both $j=n_M,n_M+1$.
3. $\widetilde H_j(h)$ vanishes at every ordinary root of $F_j$
   for both $j=n_M,n_M+1$.

Thus every noncoboundary of degree at most $M$ is detected by an
ordinary primitive period dividing $n_M$ or $n_M+1$, and hence by
one of length at most $3\lfloor\log_d M\rfloor+5$. The two
iterate polynomials have degree at most $d^5M^3$. This is a degree
bound and exact finite certificate, not an optimized time complexity.

## Status and assumptions

**PROVABLE AS STATED — author proof complete; R4 nonauthor checking
pending.** No claim of worldwide priority or a second paper admission
is made. The proof uses full periodic algebras, not reduced schemes.
There is no restriction on $c$, the primitive lengths, or root
multiplicities. One application of $f$ is the native time step.

For $d\equiv1\pmod p$, this package proves only an explicit failure
of the Jacobian-test construction. It does not prove or refute (U1)
from ordinary cycle sums in that excluded range.

## Source subtraction and dependency map

The coordinator suggested the $d$-ary carry extension. Its antecedent
is the admitted [R3 A1 quadratic carry proof](../../continuation_round3/a1_periodic_normal_form/PROOF_PACKAGE.md),
read completely, including its finite certificate. The
[old quadratic cyclic proof](../../../research_c424_c428/continuation_round2/positive_characteristic/PROOF_PACKAGE.md)
already contains the normal-basis, leading-binary-digit and necessary
Jacobian mechanisms. The corresponding $d$-ary forms are established
below so the new parameter range does not rely on an unchecked analogy.
Their elementary algebra is not a separate novelty claim.

Classical pure-power monomial bases, normal-form coefficient extraction
and Jacobian traces are subtracted against Cattani--Dickenstein--Sturmfels,
[Computing Multidimensional Residues, Section 4](https://arxiv.org/pdf/alg-geom/9404011).
Finite binomial transfer matrices and comparison of successive
multiplier-weighted traces are also antecedents, as in
Cvitanović--Hansen--Rolf--Vattay,
[Beyond the periodic orbit theory, Section 4](https://cns.gatech.edu/~predrag/papers/contourNonl.pdf).
The present elementary argument does not import complex contour
integration into positive characteristic. The report records inspected
passages and source-search limits.

Dependency map:

1. Triangular polynomial elimination gives a normal space with positive
   exponents not divisible by $d$.
2. Degree-lowering cyclic reductions give the digit basis. Weighted
   local reductions isolate the leading base-$d$ digit coefficient.
3. A full-background weighted carry circuit reaches states $0,1$;
   normal exponents make its final carry at the source legal.
4. Exact source localization permits insertion/deletion of a weight-one
   zero-digit transition, proving adjacent-level coefficient stabilization.
5. Necessary Jacobian annihilation at two levels excludes a positive
   normal part when $p\nmid d(d-1)$. A fixed point excludes constants.
6. For $p\mid d$, $F_j'=-1$ gives the conclusion directly from the
   digit detector. The finite certificate and excluded-case control follow.

## Proof

### 1. The polynomial normal form for degree $d$

Let

$$V_d=k\oplus\bigoplus_{\substack{r\ge1\\d\nmid r}}kx^r.$$

For $s\ge1$, the polynomial $\Delta x^s=(x^d+c)^s-x^s$ is
monic of degree $ds$. Eliminating the largest remaining exponent
divisible by $d$ by a multiple of such a polynomial strictly lowers
the exponent being eliminated. Terms whose positive exponent is not
divisible by $d$ are retained in $V_d$. Repeated elimination terminates,
and does not raise degree. Thus every $h$ can be written

$$h=\Delta Q+v,\qquad v\in V_d,\qquad \deg v\le\deg h
\quad\text{when }h\ne0.\tag{1}$$

If $Q$ is nonconstant, $\deg\Delta Q=d\deg Q$, which is
positive and divisible by $d$. A nonzero element of $V_d$ either
is constant or has leading degree not divisible by $d$. Hence
$B_f\cap V_d=0$, and $k[x]=B_f\oplus V_d$. The normal part
$v$ is unique; $Q$ is unique up to a constant. For zero $h$, take
$v=Q=0$. This argument uses no invertibility of $d$ in $k$.

Telescoping gives $B_f\subseteq K_f$, with no division by a cycle
length. Consequently if $h\in K_f$, its normal part belongs to $K_f$.

### 2. The full cyclic algebra and its digit basis

For $n\ge1$, indices are in $\mathbb Z/n\mathbb Z$. Put

$$A_n=k[X_0,\ldots,X_{n-1}]/(X_i^d+c-X_{i+1}:0\le i<n).$$

Eliminating $X_1,\ldots,X_{n-1}$ gives inverse isomorphisms

$$A_n\simeq k[x]/(F_n),\qquad X_i\longmapsto f^{\circ i}(x),
\qquad x\longmapsto X_0.\tag{2}$$

Since $F_n$ is monic of degree $d^n$, this algebra has dimension
$d^n$. The monomials

$$X^{\mathbf e}=\prod_{i=0}^{n-1}X_i^{e_i},
\qquad 0\le e_i\le d-1,\tag{3}$$

span: replacing any factor $X_i^d$ by $X_{i+1}-c$ strictly
decreases total degree in each resulting term, even at wraparound.
Repeated replacement terminates at (3). There are exactly $d^n$
such monomials, so they form a basis of the full algebra.

Write $H_n(v)=\sum_{i=0}^{n-1}v(X_i)\in A_n$ and
$P_n=\prod_{i=0}^{n-1}X_i^{d-1}$. Under (2), $H_n(v)$ is
represented by $\widetilde H_n(v)$, and telescoping gives

$$H_n(\Delta Q)=0\quad\text{in }A_n.\tag{4}$$

The chain rule identifies the derivative class with

$$[F_n']=d^nP_n-1.\tag{5}$$

Here and below integer scalars are mapped into $k$. Equation (5)
also holds if $p\mid d$, in which case $F_n'=-1$ as a polynomial.

### 3. Leading base-$d$ coefficient detection

Suppose $v\in V_d$ has positive leading degree $D$, leading
coefficient $a_D\ne0$, and put $m=\lfloor\log_dD\rfloor$.
Write the base-$d$ expansion

$$D=\sum_{j=0}^{m}e_jd^j,\qquad 0\le e_j<d.$$

Normality gives $e_0>0$, and by the definition of $m$, $e_m>0$.
For $n>2m$ define the target basis monomial
$M_D=\prod_{j=0}^{m}X_j^{e_j}$. Then

$$[M_D]H_n(v)=a_D.\tag{6}$$

To prove this, reduce a term $X_i^r$, $r\le D<d^{m+1}$, in
the forward window $X_i,\ldots,X_{i+m}$, assigning the local
weights $1,d,\ldots,d^m$. Choosing $X_{i+j+1}$ in the relation
$X_{i+j}^d=X_{i+j+1}-c$ preserves weight, whereas choosing
$-c$ strictly lowers it. No term can reach a factor
$X_{i+m}^d$, whose weight would exceed $r$. The reduction
therefore stays in that window, which consists of distinct variables.

Fix a deterministic order of reductions. Its unique branch choosing
no constants ends at the base-$d$ digit monomial of $r$ in that
window, with coefficient one and weight $r$. All other branches
have lower weight. This argument is valid even if some lower
coefficients cancel in characteristic $p$.

If $m\ge1$, a circular interval of $m+1$ consecutive indices
containing both $0$ and $m$ must be the interval $[0,m]$, because
the other forward distance is $n-m>m$. Thus only source $i=0$
can contribute $M_D$. If $m=0$, each window is a singleton and
the same source conclusion holds. The target has weight $D$ there;
only the leading term $a_DX_0^D$ contributes it, with coefficient
$a_D$. Constants give no nonempty digit support. This proves (6).

### 4. Exact one-circuit full-background carry expansion

Fix a degree cap $M\ge1$, put $m=\lfloor\log_dM\rfloor$,
$L=m+1$, and let $1\le r\le M$ with $d\nmid r$. Suppose
$n\ge L$, and fix a source index $i$. We expand $P_nX_i^r$
by processing sites $i,i+1,\ldots,i+n-1$ in that cyclic order.

The source initially has exponent $d-1+r$, while every other
site has background exponent $d-1$. Set $t_0=r$. At step
$s\in\{0,\ldots,n-1\}$ put

$$b_s=(d-1+t_s)\bmod d,\qquad
q_s=\left\lfloor\frac{d-1+t_s}{d}\right\rfloor.\tag{7}$$

The local identity is

$$X_{i+s}^{d-1+t_s}
=X_{i+s}^{b_s}(X_{i+s+1}-c)^{q_s}
=\sum_{t_{s+1}=0}^{q_s}
\binom{q_s}{t_{s+1}}(-c)^{q_s-t_{s+1}}
X_{i+s}^{b_s}X_{i+s+1}^{t_{s+1}}.\tag{8}$$

A path consists of the finite integer sequence $(t_0,\ldots,t_n)$
with $t_0=r$ and these permitted transitions. Its weight is

$$w(t)=\prod_{s=0}^{n-1}
\binom{q_s}{t_{s+1}}(-c)^{q_s-t_{s+1}}\in k.\tag{9}$$

Zero-weight paths are retained. Since
$t_{s+1}\le(d-1+t_s)/d$, induction gives

$$t_s\le1+\frac{r-1}{d^s}.\tag{10}$$

The inequality $d^L>M-1$ implies $t_L<2$, so $t_L\le1$.
States zero and one never return to a larger state; hence $t_n\le1$.

The final factor lands back at the source, already left with exponent
$b_0$. Since $d\nmid r$, equation (7) gives

$$b_0=(r-1)\bmod d\le d-2.$$

Therefore $b_0+t_n\le d-1$. Unlike a general starting exponent,
this normal exponent requires no second circuit. The final digit
vector of the path has source digit $b_0+t_n$ and, at every other
site $i+s$, digit $b_s$ for $1\le s<n$. Denote it by
$\mathbf e(t,i)$. Equations (8)--(10) give the exact digit-basis
identity

$$P_nX_i^r=\sum_t w(t)X^{\mathbf e(t,i)}\quad\text{in }A_n.\tag{11}$$

This is a complete polynomial expansion followed by the already proved
uniqueness of the digit basis. It uses no radicality or cancellation-free
assumption. In particular digits greater than one are preserved, not
replaced merely by their support.

For later use, the eventual-state transitions are exactly:

| Incoming carry | Output digit | Outgoing carry | Weight |
| --- | --- | --- | --- |
| $0$ | $d-1$ | $0$ | $1$ |
| $1$ | $0$ | $1$ | $1$ |
| $1$ | $0$ | $0$ | $-c$ |

The output digit in the first row is nonzero for every integer $d\ge2$.
It is an exponent, not a scalar to reduce modulo $p$.

### 5. Source localization for any nonzero short digit target

Fix digits $e_0,\ldots,e_m$ with $0\le e_j<d$, not all zero,
and set all other target digits equal to zero. Let
$E=\{j\in[0,m]:e_j>0\}$. Suppose $n\ge L+1$ and a path
in (11) produces exactly this digit vector. Then its source satisfies

$$i\in\left(\bigcup_{s=0}^{L-1}(E-s)\right)\cup(E+1)
\subseteq[-m,m+1]\pmod n.\tag{12}$$

Indeed, it suffices to consider a source outside $E$ for which the
next $L-1$ sites also lie outside $E$. The final digit at the
source is zero, so $b_0+t_n=0$ as an equality of nonnegative
integers. In particular $t_n=0$ and $b_0=0$. The first $L-1$
non-source output digits are also zero.

If $t_L=0$, it remains zero throughout the rest of the circuit.
Because $n-1\ge L$, the final processed site has output $d-1>0$,
so $i-1\in E$.

If $t_L=1$, the terminal condition $t_n=0$ forces a first
$1\to0$ transition at a step from $L$ through $n-1$.
If it occurs at the last step, all later-state output digits are
zero and there are no subsequent sites with carry zero. Combined
with the preceding initial zero outputs and the zero source digit,
this would make the target empty. Thus the first drop must occur
at a step at most $n-2$. The last output is then $d-1>0$, again
giving $i-1\in E$. This proves (12). Some targets with digits
between $1$ and $d-2$ may have fewer contributing paths; no step
assumes otherwise.

For $n\ge3m+4$, representatives in (12) lie in the disjoint set

$$I_n=\{0,\ldots,m+1\}\cup\{n-m,\ldots,n-1\}.\tag{13}$$

The second block is empty when $m=0$. This bound is uniform for
every normal exponent $r\le M$.

### 6. Weight-preserving insertion and deletion

Assume $n\ge3m+4$ and put $j=2m+2$. Let a path at level $n$
produce the target of Section 5. Its source is in $I_n$. Neither
$j$ nor $j+1$ is a source, and both have target digit zero:
the lower source block ends at $m+1<j$, while the upper block
begins at $n-m\ge2m+4>j+1$.

When processing site $j$, at least $L$ steps have elapsed from the
source. For $0\le i\le m+1$ its forward distance is
$j-i\ge m+1=L$; for $n-m\le i\le n-1$ the forward distance
is $j+n-i\ge j+1\ge L$. The incoming carry is thus at most one.
Because the output at $j$ is zero, it must be one, by the transition
table. The next output at the non-source site $j+1$ is zero as
well, so the outgoing carry at $j$ must also be one. Its transition
is therefore $1\to1$ of weight exactly one.

Insert a site just after $j$ with output zero and transition
$1\to1$. Relabel old indices by

$$\iota_n(a)=
\begin{cases}
a,&0\le a\le j,\\
a+1,&j+1\le a<n.
\end{cases}\tag{14}$$

All original transitions occur in the same source-dependent cyclic
order. The source becomes $\iota_n(i)$; the initial carry, final
carry and source digit $b_0+t_n$ are unchanged. All target digits
are unchanged because they are supported in $[0,m]$. This produces
a level-$n+1$ path of the same weight.

Conversely every target-producing level-$n+1$ path has source in
$I_{n+1}$. Its source is neither $j+1$ nor $j+2$, since the
upper block starts at $n+1-m\ge2m+5>j+2$. Both these sites
have zero target digits, and the distance from the source to $j+1$
is at least $L$. The transition there is consequently $1\to1$
of weight one by the same two-output argument. Delete site $j+1$
and relabel later sites downwards by one. The result is a valid
level-$n$ path preserving the source digit, all other target digits,
and weight. The source blocks in (13) are carried to one another
by (14); no new source at the inserted site can contribute.

Insertion and deletion are mutual inverses. Summing (11) proves,
for every normal exponent $r\le M$ and the given digit target,

$$[X^{\mathbf e}]\left(P_n\sum_{i=0}^{n-1}X_i^r\right)
=[X^{\mathbf e}]\left(P_{n+1}\sum_{i=0}^{n}X_i^r\right).
\tag{15}$$

For a constant term $a_0$, $P_nH_n(a_0)=na_0P_n$ has no
coefficient at a nonzero target supported in $[0,m]$, since
$n>m+1$ and $P_n$ has nonzero exponent at every site. Thus for
every $v\in V_d$ of degree at most $M$,

$$C_{n+1}(v;\mathbf e)=C_n(v;\mathbf e),\qquad
C_n(v;\mathbf e)=[X^{\mathbf e}](P_nH_n(v)),
\quad n\ge3m+4.\tag{16}$$

This stabilization proof has not used any condition on $d$ modulo
$p$. The later Jacobian comparison is where the exceptional congruence
enters.

### 7. Ordinary cycle sums imply polynomial transfer in the carry branch

Assume $p\nmid d(d-1)$ and $h\in K_f$. Replace $h$ by its
normal part $v$ from (1). For any root $a$ of $F_n$, its native
primitive period $r_a$ divides $n$, and

$$\widetilde H_n(v)(a)=(n/r_a)S_v(O_a)=0.$$

At a root of multiplicity $e$, $F_n'$ has vanishing order at
least $e-1$, also when $p\mid e$. Multiplication by a polynomial
vanishing at the root reaches order at least $e$. Factoring over
$k$ therefore gives

$$F_n\mid F_n'\widetilde H_n(v),\qquad
(d^nP_n-1)H_n(v)=0\quad\text{in }A_n.\tag{17}$$

Only this necessary implication is used. Its converse at a single
level is not assumed.

Suppose $v$ has positive leading degree $D$ and leading coefficient
$a_D\ne0$. Use the target digit vector of $D$ in Section 3 and
take $n\ge3\lfloor\log_dD\rfloor+4$. Equations (6) and (17)
give

$$d^nC_n(v;\mathbf e_D)=a_D,
\qquad d^{n+1}C_{n+1}(v;\mathbf e_D)=a_D.\tag{18}$$

Stabilization (16) identifies the two $C$ values. Subtracting $d$
times the first equality from the second gives
$(d-1)a_D=0$, up to multiplication by $-1$. Since $p\nmid d-1$,
this contradicts $a_D\ne0$.

Thus $v$ is constant. The polynomial $f(x)-x$ has a root over
$k$; its ordinary fixed-point orbit has sum equal to $v$.
Therefore $v=0$, and $h\in B_f$. Together with telescoping,
this proves (U1) in the initially allocated range.

### 8. Separately authorized branch: $p\mid d$

Now let $p\mid d$. The base derivative is zero, so $F_n'=-1$
for every $n\ge1$. Hence $F_n$ is squarefree. For $h\in K_f$
and its normal part $v$, ordinary-root vanishing gives
$H_n(v)=0$ in $A_n$ for every $n$.

If $v$ has positive degree $D$, choose any
$n>2\lfloor\log_dD\rfloor$. The digit detector (6) says its
trace has nonzero leading-digit coefficient, a contradiction.
The remaining constant is zero by an ordinary fixed point. This
proves (U1) for $p\mid d$ without using carry stabilization.

The two branches cover exactly $d\not\equiv1\pmod p$.
Neither branch replaces the native clock by a Frobenius clock.

### 9. The exact two-return certificate

Fix $M\ge1$, $\deg h\le M$, and $n=n_M$. If $h=\Delta Q$,
telescoping gives
$\widetilde H_j(h)=Q(f^{\circ j}(x))-Q(x)$, divisible by
$F_j$, for every $j$. Thus condition 1 implies 2 and 3. The
root-multiplicity argument in Section 7 proves 3 implies 2.

Suppose 2 holds. Replacing $h$ by its normal part $v$, of degree
at most $M$, leaves 2 unchanged by (4). If $v$ has positive
degree $D$, then both chosen levels exceed $2\lfloor\log_dD\rfloor$.
In the branch $p\nmid d(d-1)$ they also meet the uniform
stabilization bound, so (18) contradicts the leading coefficient.
In the branch $p\mid d$, condition 2 simply gives $H_j(v)=0$,
contradicting (6) at either chosen level.

It remains that $v=a_0$ is constant. Condition 2 is
$F_j\mid ja_0F_j'$. The polynomial $F_j'$ is nonzero and has
degree less than $\deg F_j$: it is $-1$ if $p\mid d$, and
has leading coefficient $d^j\ne0$ otherwise. Thus $ja_0=0$
for both $j=n,n+1$. Subtracting gives $a_0=0$. Hence 2 implies
1, proving the stated equivalence of all three conditions.

If $h\notin B_f$, condition 3 fails for some root $a$ at one
of these levels $j$. If its primitive length is $r\mid j$,
then $\widetilde H_j(h)(a)=(j/r)S_h(O)\ne0$ implies
$S_h(O)\ne0$. No division in $k$ is used. This gives the
primitive detector bound. Finally, with $m=\lfloor\log_dM\rfloor$,

$$\deg F_j\le d^{n+1}=d^{3m+5}\le d^5M^3.$$

The finite tests concern the full $j$-step sums at every ordinary
root, not merely primitive cycles of exact length $j$. Nothing here
claims optimality of the cutoff or bounds all intermediate expressions.

### 10. An all-level Jacobian blind control when $d\equiv1\pmod p$

Let $d\ge2$ satisfy $d\equiv1\pmod p$, take $c=0$ and
$h(x)=x$. Then $f=x^d$ and, for every $n\ge1$,

$$F_n=x^{d^n}-x=xR_n,\qquad
R_n=x^{d^n-1}-1,\qquad F_n'=R_n.$$

The last equality uses $d^n=1$ as a scalar in $k$.
The polynomial $\widetilde H_n(x)=\sum_{i=0}^{n-1}x^{d^i}$
is divisible by $x$, so

$$F_n\mid F_n'\widetilde H_n(x)\quad\text{for every }n.\tag{19}$$

Nevertheless $1$ is a fixed point and its ordinary $h$-sum is
$1\ne0$. Also $x$ is not a polynomial coboundary by the
normal-form degree argument. Therefore even the entire collection
of Jacobian tests is insufficient in this excluded congruence class.
The control does not satisfy all ordinary sums and is not a
counterexample to (U1) from those sums. The ordinary-cycle theorem
for $d\equiv1\pmod p$ remains outside the present conclusion.

## Verification and open review risks

The proof is entirely by exact hand identities and finite bijections;
no mathematical program was run. The initial proposed degree recurrence
has been established, including its source localization, source-digit
wraparound and arbitrary digits greater than one. The claimed exceptional
range is attached to the Jacobian method, not promoted to a universal
no-go theorem for ordinary cycle data.

R4 nonauthor review remains pending. The principal audit points are
the full source digit $b_0+t_n$, the localization implication (12),
the insertion/deletion bijection with all sources summed, and the
normal leading-digit detector for composite $d$. Source novelty is
bounded by the searches and inspected passages recorded in the report;
the explicit ownership of the quadratic ancestor and classical trace
machinery remains part of this result's scope.
