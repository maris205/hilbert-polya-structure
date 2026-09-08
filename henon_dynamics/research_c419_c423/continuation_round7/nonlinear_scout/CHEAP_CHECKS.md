# Cheap hand checks for the three frozen nonlinear screens

2026-09-08 UTC. The original contracts are in
[SCOUT_REPORT.md](SCOUT_REPORT.md). These two auxiliary results do not
answer either full structural classification question. They use zero
mathematical program executions. The AY zero-channel estimate was proposed
by the coordinator and checked/organized here; this is not an independent
nonauthor review.

## Claim

**AY helper.** For every integer $k\ne0$, every ordinary integral periodic
orbit of
$$
Y_k(p,q,r,s)=\left(r-\frac{kp}{1+ps},s,p,q+\frac{ks}{1+ps}\right)
$$
has all four coordinates bounded in absolute value by
$C_k=\max(|k|+1,4)$. Consequently its entire fixed-parameter integral periodic
locus is obtained from a finite exact graph, with no period cutoff. For
$k=0$ the displayed ordinary map swaps the two coordinate pairs and has
native periods at most two.

**PG helper.** For each fixed $n\ge4$ and nonzero integers $P,Q$, the
ordinary integral periodic points of the frozen pentagram corner map with
$\prod_i x_i=P$, $\prod_i y_i=Q$ form the cycles of a finite exact graph
on ordered signed factorizations of $P$ and $Q$.

## Status

Both auxiliary claims: `PROVABLE AS STATED`.

Original AY7 and PG7 structural atlas questions:
`NOT CURRENTLY JUSTIFIED`. Neither helper is promoted to an admission.

## Assumptions and notation

Use exactly the two-sided native domains of the scout report, including
the displayed pole exclusions. Every coordinate at every point of each
periodic orbit is an integer. Periodicity is in the one-step native clock.
No sign, reversal or relabelling quotient is taken.

For AY, write the $n$th orbit state as $(p_n,q_n,r_n,s_n)$, with all
indices interpreted periodically when summing. Put $B=|k|+1$. For PG the
spatial index is $i\in\mathbb Z/n\mathbb Z$; its use is unrelated to AY
time notation.

## Proof strategy and dependency map

1. AY transition integrality gives $1+p_ns_n\mid k$.
2. The scalar second-order recurrences exclude identically-zero channels
   by a telescoping sum and bound isolated zeros by their neighbors.
3. The resulting uniform fixed-$k$ box gives an exact finite graph.
4. PG's displayed update preserves its two products by telescoping;
   nonzero integer factors of a fixed nonzero integer range over a finite
   set.

The only inherited map inputs are the formulas in the scout report.
No external torsion theorem, integrability theorem or unproved height
claim is needed for these helper proofs.

## Proof

### Step 1: the AY divisor condition and recurrences

Let $D_n=1+p_ns_n\ne0$. Since
$r_n-p_{n+1}=kp_n/D_n$ is an integer, $D_n\mid kp_n$.
Every common divisor of $D_n$ and $p_n$ divides
$D_n-s_np_n=1$. Thus $\gcd(D_n,p_n)=1$ and
$$
D_n\mid k,\qquad h_n=\frac{k}{D_n}\in\mathbb Z.
$$
This includes $p_n=0$, where $D_n=1$. For $k\ne0$, $h_n$ never vanishes.

The displayed update gives
$r_n=p_{n-1}$ and $q_n=s_{n-1}$ on a two-sided orbit. Therefore
$$
p_{n+1}=p_{n-1}-h_np_n,\qquad
s_{n+1}=s_{n-1}+h_ns_n.                       \tag{1}
$$
If $p_ns_n\ne0$, then
$$
|p_ns_n|=|D_n-1|\le |k|+1=B.
$$
Both factors are nonzero integers, so $|p_n|,|s_n|\le B$.

### Step 2: identically-zero channels

If $p_n=0$ at every time, then $h_n=k$ and
$s_{n+1}-s_{n-1}=ks_n$. Multiply by $s_n$ and sum over any period $N$:
$$
\sum_{n=0}^{N-1}s_ns_{n+1}
-\sum_{n=0}^{N-1}s_ns_{n-1}
=k\sum_{n=0}^{N-1}s_n^2.
$$
The two sums on the left agree by the cyclic change of index
$n\mapsto n-1$. Because $k\ne0$ and $s_n$ are real, all $s_n=0$.
Then $q_n=r_n=0$, so the orbit is the origin.

If $s_n=0$ at every time, use
$p_{n+1}-p_{n-1}=-kp_n$ and the same cyclic sum with $p_n$ to conclude
$p_n=0$ at every time. Hence a nonzero periodic orbit has neither scalar
channel identically zero.

### Step 3: isolated zeros and the uniform bound

Two consecutive zero terms in either recurrence (1) force the whole
corresponding two-sided sequence to be zero: the recurrence solves forward
with coefficient $1$ on the backward term and also solves backward with
coefficient $1$ on the forward term.

Consider a nonzero periodic orbit and a time with $p_n=0$. Neither
$p_{n-1}$ nor $p_{n+1}$ is zero, and (1) gives
$p_{n+1}=p_{n-1}$. At each neighboring time, if the corresponding $s$
term is nonzero, Step 1 bounds it by $B$; if it is zero the same bound
still holds. Thus
$$
|s_{n-1}|,|s_{n+1}|\le B.
$$
At time $n$, $D_n=1$ and $h_n=k$, so
$$
|k|\,|s_n|=|s_{n+1}-s_{n-1}|\le2B.
$$
It follows that $|s_n|\le2(|k|+1)/|k|\le4$.

Now take a time with $s_n=0$. The same no-consecutive-zero property
gives nonzero $s_{n-1}$ and $s_{n+1}$. Step 1 bounds the neighboring $p$
terms by $B$ whether they are zero or nonzero. The first recurrence (1)
with $h_n=k$ yields
$$
|k|\,|p_n|=|p_{n-1}-p_{n+1}|\le2B,
$$
so $|p_n|\le4$. These arguments also cover a simultaneous zero
$p_n=s_n=0$. Combining with the nonzero-product case and the origin gives
$$
|p_n|,|s_n|\le C_k=\max(|k|+1,4)
$$
for every time. Since $q_n=s_{n-1}$ and $r_n=p_{n-1}$, all four state
coordinates satisfy the claimed bound.

### Step 4: exact fixed-parameter graph and the zero parameter

For $k\ne0$, take all integer states in $[-C_k,C_k]^4$ satisfying the
displayed forward and inverse denominator exclusions. Retain an edge
precisely when its exact rational forward image is another such integer
state in the box and the displayed inverse at that image returns the
starting state. All valid directed cycles lie in the ordinary two-sided
domain and are integral periodic orbits. Steps 1–3 put every ordinary
integral periodic orbit in this graph. Cycle lengths give exact least
native periods; no cutoff on the length is needed.

For $k=0$, the formula on its native domain is
$(p,q,r,s)\mapsto(r,s,p,q)$. Its square is the identity. The two-sided
domain still requires $1+ps\ne0$ and $1+rq\ne0$; these two conditions
are interchanged by the pair swap. States with $(p,q)=(r,s)$ are fixed,
and the other states in this domain have least period two.

This proves the AY helper, not an explicit all-$k$ structural cycle atlas.

### Step 5: PG product invariants and finite slices

Put $\phi_i=1-x_iy_i$, nonzero on every ordinary orbit state. Multiplying
the first displayed update over all spatial indices gives
$$
\prod_i x_i'
=\left(\prod_i x_i\right)
  \frac{\prod_i\phi_{i-1}}{\prod_i\phi_{i+1}}
=\prod_i x_i=P.
$$
Multiplying the second gives
$$
\prod_i y_i'
=\left(\prod_i y_{i+1}\right)
  \frac{\prod_i\phi_{i+2}}{\prod_i\phi_i}
=\prod_i y_i=Q.
$$
Both equalities hold for every $n\ge4$; the parity of $n$ does not affect
these telescoping products.

If all coordinates are nonzero integers, $x_i$ is a signed divisor of
$P$ and $y_i$ a signed divisor of $Q$. Each integer has finitely many
signed divisors, so the ordered factorization arrays with the specified
products form a finite set. Restrict to the frozen corner chart. Retain
only edges whose exact displayed forward value is another such integer
array and for which the ordinary birational inverse is defined and
returns the preceding array. Every valid directed cycle is an ordinary
integral periodic orbit. Conversely every orbit in the claim yields such
a directed cycle by the two preserved products.

The slice is therefore classified by its finite exact graph, with native
cycle lengths. This proves the PG helper. No graph was built or executed.

## Corrections or missing assumptions

The first informal AY scout observation treated zero channels as a
possible obstruction to any fixed-parameter height bound. Steps 2–3
remove that obstruction. They do not close the original structural atlas.

Zeros are retained in AY. They are explicitly outside the PG corner
chart, as frozen before its factorization observation. No zero-stratum
theorem for an enlarged PG compactification is asserted.

## Open risks and unproved original conclusions

- AY7 still needs a substantive uniform cycle-family/exhaustion theorem
  beyond running the finite graph separately for each $k$.
- PG7 still needs a structural classification across all $n,P,Q$ and all
  surviving ordinary exceptional fibres; a generic Jacobian translation
  does not supply it.
- HK7 received no global proof attempt. Its full integral atlas remains
  open in this scout.
- Neither mathematical correctness of these helpers nor source-search
  absence establishes an independent paper-level increment.
