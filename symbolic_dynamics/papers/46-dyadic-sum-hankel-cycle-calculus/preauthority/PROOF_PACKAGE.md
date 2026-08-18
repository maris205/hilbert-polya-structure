# Proof Package — Dyadic-Sum Hankel Operator

## Claim

Let $s\in\mathbb C$, $\sigma=\Re s$, and let $H_s$ be the matrix on
$\ell^2(\mathbb N)$ defined by

$$
H_s(m,n)=\mathbf 1_{\{m+n=2^a\text{ for some }a\ge1\}}(mn)^{-s/2}.
$$

Then:

1. $H_s$ is bounded and compact exactly when $\sigma>0$.
2. $H_s\in S_2$ exactly when $\sigma>1/2$.
3. $H_s\in S_1$ exactly when $\sigma>1$.
4. $H_s\cong\bigoplus_{k\ge0}2^{-ks}A_s$, where $A_s$ is the odd-vertex
   block.
5. For $\sigma>1/2$ and every $r\ge2$,
   $$
   \operatorname{Tr}(H_s^r)
   =\frac{\operatorname{Tr}(A_s^r)}{1-2^{-rs}},
   \qquad
   \det_2(I-zH_s)
   =\prod_{k\ge0}\det_2(I-z2^{-ks}A_s).
   $$
6. A cyclic system $n_i+n_{i+1}=q_i$, $q_i$ powers of two, has the exact
   odd/even solution classification proved below.

## Status

`PROVABLE AS STATED`

The ordinary Minkowski/Hankel all-$S_q$ generalization is not part of this
claim.

## Assumptions

- vertices are the positive integers;
- $2^a\ge2$ and loops are retained;
- the real logarithm fixes $n^{-s/2}$;
- $S_1$ and $S_2$ are the ordinary trace and Hilbert--Schmidt ideals;
- traces and determinants are asserted only in their displayed legal domains.

## Notation

- $N_a=2^a$;
- $A_s$ is the compression of $H_s$ to odd positive integers;
- $R_m$ is the absolute row sum of the modulus matrix;
- $q_i=2^{a_i}$ denotes an edge label in the cyclic solver.

## Proof strategy

The ideal thresholds are obtained from exact anti-diagonal sums and a
disjoint central matching lower bound.  The arithmetic structure is then
separated: $2$-adic valuation gives orthogonal self-similarity, while a direct
linear recurrence solves every labeled closed-walk system.  No finite-cutoff
limit is used to justify an endpoint.

## Dependency map

1. boundedness uses an absolute Schur row estimate;
2. compactness uses vanishing row tails and finite truncation;
3. $S_2$ uses an exact square-sum over dyadic anti-diagonals;
4. $S_1$ sufficiency uses entrywise absolute summability;
5. $S_1$ necessity uses trace duality against disjoint weighted matchings;
6. determinant identities use the valuation direct sum and standard ideal
   determinant identities inside the proved $S_2$ domain;
7. the cycle theorem uses only the recurrence $n_{i+1}=q_i-n_i$.

## Proof

### Step 1: complex phases do not affect singular values

Write $s=\sigma+it$ and let $U_t e_n=n^{-it/2}e_n$.  Then $U_t$ is unitary
and

$$
H_s=U_tH_\sigma U_t.
$$

Left and right multiplication by unitaries preserve every singular value.
All boundedness, compactness, and Schatten statements may therefore be
proved for real $s=\sigma$.

### Step 2: boundedness for $\sigma>0$

Fix $m\ge1$ and let $A=A(m)$ be the least integer with $2^A>m$.  The
neighbors of $m$ are $2^{A+j}-m$, $j\ge0$.  Hence

$$
R_m=m^{-\sigma/2}
\sum_{j\ge0}(2^{A+j}-m)^{-\sigma/2}.
$$

The $j=0$ summand is at most $m^{-\sigma/2}$.  For $j\ge1$,

$$
2^{A+j}-m\ge2^{A+j-1},
$$

and $2^A\ge m$.  Thus

$$
R_m\le m^{-\sigma/2}
+C_\sigma m^{-\sigma/2}2^{-A\sigma/2}
\le m^{-\sigma/2}+C_\sigma m^{-\sigma}.
$$

The right side is uniformly bounded and tends to zero as $m\to\infty$.
The modulus matrix is symmetric, so the Schur test gives a bounded operator.

### Step 3: compactness for $\sigma>0$

Let $P_N$ project onto $\operatorname{span}\{e_1,\ldots,e_N\}$.  Given
$\varepsilon>0$, choose $M$ so that $R_m<\varepsilon$ for $m>M$.  For the
finitely many rows $m\le M$, absolute summability gives an $N\ge M$ whose
tail row sums are below $\varepsilon$.  Every row sum of
$H_\sigma-P_NH_\sigma P_N$ is then below $2\varepsilon$.  Symmetry and the
Schur test yield

$$
\|H_\sigma-P_NH_\sigma P_N\|\le2\varepsilon.
$$

The finite-rank compressions converge in operator norm, proving compactness.

### Step 4: unboundedness for $\sigma\le0$

The row indexed by $m=1$ contains the entries associated with
$n=2^a-1$, $a\ge1$.  Its squared $\ell^2$ norm contains

$$
\sum_{a\ge1}(2^a-1)^{-\sigma}.
$$

This series diverges when $\sigma\le0$.  A row of a bounded operator on
$\ell^2$ must be an $\ell^2$ vector because it is the coordinate vector of
$H_s^*e_1$.  Therefore $H_s$ is unbounded.  Steps 2--4 prove the first
claim.

### Step 5: exact Hilbert--Schmidt threshold

The supports on distinct anti-diagonals are disjoint, so

$$
\|H_s\|_2^2
=\sum_{a\ge1}\sum_{m=1}^{2^a-1}
[m(2^a-m)]^{-\sigma}.
$$

For $0<\sigma<1$, comparison with the beta integral gives constants
$0<c_\sigma<C_\sigma<\infty$ such that

$$
c_\sigma 2^{a(1-2\sigma)}
\le
\sum_{m=1}^{2^a-1}[m(2^a-m)]^{-\sigma}
\le
C_\sigma 2^{a(1-2\sigma)}.
$$

The lower bound may also be obtained by restricting to
$2^{a-2}\le m\le3\cdot2^{a-2}$.  Therefore the outer series converges in
this range exactly when $\sigma>1/2$.

At $\sigma=1$,

$$
\sum_{m=1}^{N-1}\frac1{m(N-m)}=\frac{2H_{N-1}}N,
$$

so the dyadic levels are summable.  When $\sigma>1$, splitting at $N/2$
gives a level bound $O(N^{-\sigma})$.  These bounds prove
$H_s\in S_2$ exactly when $\sigma>1/2$.

### Step 6: trace-class sufficiency

For $\sigma>1$, the sum of the absolute values of all matrix entries is

$$
\sum_{a\ge1}\sum_{m=1}^{2^a-1}
[m(2^a-m)]^{-\sigma/2}.
$$

Applying the estimates of Step 5 with exponent $\sigma/2$ shows that the
$a$th level is $O(2^{a(1-\sigma)})$ for $1<\sigma<2$, is
$O(a2^{-a})$ for $\sigma=2$, and is $O(2^{-a\sigma/2})$ for $\sigma>2$.
The entrywise sum is finite.  A matrix with absolutely summable entries is
trace class, so $H_s\in S_1$.

### Step 7: trace-class necessity, including the endpoint

Put $Q_j=4^j$.  Let

$$
I_j=\mathbb Z\cap[Q_j/4,Q_j/3],
\qquad
J_j=\{Q_j-m:m\in I_j\}.
$$

All $I_j$ and $J_j$ are pairwise disjoint.  On $I_j\times J_j$, the only
possible power-of-two sum is $Q_j$, and the compression of $H_s$ is a
weighted matching.  For each $J$, choose a finite-rank partial isometry
$V_J$ mapping each $e_{Q_j-m}$, $j\le J$, to the corresponding $e_m$ with
the phase that makes the trace pairing positive.  The domains and ranges of
all these matches are orthogonal, so $\|V_J\|=1$.  If $H_s$ were trace
class, trace duality would give, for every $J$,

$$
\sum_{j\le J}\sum_{m\in I_j}[m(Q_j-m)]^{-\sigma/2}
=|\operatorname{Tr}(V_J^*H_s)|
\le\|H_s\|_1.
$$

The $j$th inner sum is comparable to $Q_j^{1-\sigma}$.  The outer sum
diverges for every $\sigma\le1$, including the endpoint, contradicting the
uniform bound as $J\to\infty$.  Thus
$H_s\in S_1$ exactly when $\sigma>1$.

### Step 8: exact $2$-adic direct sum

If $m+n=2^a$ and $v_2(m)\ne v_2(n)$, then
$v_2(m+n)=\min\{v_2(m),v_2(n)\}<a$, a contradiction.  Hence every edge has
$v_2(m)=v_2(n)=k$.  Writing $m=2^ku$, $n=2^kv$ with $u,v$ odd yields
$u+v=2^{a-k}$ and

$$
(mn)^{-s/2}=2^{-ks}(uv)^{-s/2}.
$$

The valuation subspaces are mutually orthogonal and exhaust
$\ell^2(\mathbb N)$, proving

$$
H_s\cong\bigoplus_{k\ge0}2^{-ks}A_s.
$$

### Step 9: legal traces and determinants

When $\sigma>1$, diagonal entries occur exactly at $m=2^k$, $k\ge0$.
Absolute trace convergence from Step 7 permits diagonal summation:

$$
\operatorname{Tr}(H_s)
=\sum_{k\ge0}2^{-ks}=\frac1{1-2^{-s}}.
$$

When $\sigma>1/2$, $H_s$ and $A_s$ are Hilbert--Schmidt.  Therefore
$H_s^r$ and $A_s^r$ are trace class for every $r\ge2$.  Applying Step 8 to
the $r$th power gives

$$
\operatorname{Tr}(H_s^r)
=\sum_{k\ge0}2^{-krs}\operatorname{Tr}(A_s^r)
=\frac{\operatorname{Tr}(A_s^r)}{1-2^{-rs}}.
$$

The direct-sum law for the Hilbert--Carleman determinant and
$\sum_k\|2^{-ks}A_s\|_2^2<\infty$ give

$$
\det_2(I-zH_s)
=\prod_{k\ge0}\det_2(I-z2^{-ks}A_s).
$$

The product converges locally uniformly in $z$.  Equivalently, near zero,

$$
\log\det_2(I-zH_s)
=-\sum_{r\ge2}\frac{z^r}{r}
\frac{\operatorname{Tr}(A_s^r)}{1-2^{-rs}}.
$$

### Step 10: complete cyclic edge-label solver

Fix $r\ge1$ and powers of two $q_i=2^{a_i}\ge2$.  Iterate
$n_{i+1}=q_i-n_i$.  For $2\le i\le r+1$,

$$
n_i=(-1)^{i-1}n_1+
\sum_{j=1}^{i-1}(-1)^{i-1-j}q_j.
$$

The closing equation is

$$
(1-(-1)^r)n_1
=\sum_{j=1}^r(-1)^{r-j}q_j.
$$

If $r$ is odd, there is exactly one candidate,

$$
n_1=\frac12(q_1-q_2+q_3-\cdots+q_r).
$$

All other $n_i$ are then fixed by the recurrence.  A positive-integer closed
walk exists exactly when every derived $n_i$ is positive.  Integrality is
automatic because every $q_i$ is even.

If $r$ is even, a solution exists only if

$$
q_1-q_2+q_3-\cdots-q_r=0.
$$

Under this condition $n_1$ is a free integer and every other $n_i$ is an
affine function with coefficient $+1$ or $-1$.  The inequalities $n_i>0$
cut out an explicit finite open interval; the positive integers in that
interval are exactly the solutions.  In the odd block one additionally
requires $n_1$ odd, after which every $n_i$ is odd.

This solves every labeled cyclic system and supplies a trace evaluator that
does not use matrix multiplication.

## Corrections or missing assumptions

- No correction to the frozen claim is required.
- An all-$S_q$ interpolation claim is deliberately absent.
- For nonreal $s$, the operator is complex symmetric but is not asserted to
  be Hermitian or self-adjoint.

## Open risks

- The final paper must cite the precise direct-sum theorem used for
  $\det_2$, or reproduce its short ideal proof.
- Novelty remains search-bounded; no priority claim follows from absence of
  an exact source hit.
