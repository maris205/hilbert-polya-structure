# Universal canonical-height series for constant Hénon maps

## Claim, status and assumptions

**Author proof status: PROVABLE AS STATED. Independent review and source
admission remain pending; this is not a numbered paper.**

Fix a prime power $q$, an integer $d\ge2$, a polynomial
$f\in\mathbb F_q[X]$ of degree exactly $d$, and
$a\in\mathbb F_q^\times$. On $R^2$, where $R=\mathbb F_q[t]$, let

$$H(x,y)=(y,f(y)-ax),\qquad
H^{-1}(x,y)=(a^{-1}(f(x)-y),x).$$

Write $h(x,y)=\max(0,\deg x,\deg y)$, with $\deg0=-\infty$, and

$$\widehat h^\pm(P)=\lim_{n\to\infty}d^{-n}h(H^{\pm n}P),\quad
\widehat h(P)=\widehat h^+(P)+\widehat h^-(P),\quad
Z_H(s)=\sum_{P\in R^2}q^{-s\widehat h(P)}.$$

The limits exist. The full distribution of $\widehat h$ depends only on
$q,d$, not on the nonzero leading coefficient, lower coefficients, or $a$.
Its exact series is given in Step 4. It converges absolutely precisely in
the open half-plane $\Re s>1$ and continues meromorphically to $\Re s>0$.
In that latter half-plane its poles are exactly

$$s_{k,\ell}=\frac{d+1}{L_k}+
 \frac{2\pi i\ell}{L_k\log q},\qquad
 L_k=d^k+d^{1-k},\quad k\ge1,\ \ell\in\mathbb Z.$$

The poles with $k=1$ and $(d+1)\mid\ell$ are double; all other poles
are simple. Every point of $\Re s=0$ is an accumulation point of these
poles, so that line is a natural boundary for meromorphic continuation.
For $B\to\infty$ through arbitrary real values,

$$\#\{P\in R^2:\widehat h(P)\le B\}
 =\frac{d-1}{d+1}(q-1)q^{\lfloor B\rfloor+1}B+O_{q,d}(q^B).$$

These are canonical heights in units of $\log q$ on polynomial points.
No assertion concerns all rational-function points, nonconstant coefficients,
ordinary periodic-orbit zeta functions or a target Riemann divisor.

## Strategy and dependency map

The canonical-height construction and nonarchimedean escape mechanism are
classical (Kawaguchi, Ingram). Here the polynomial degree recursion gives a
self-contained proof of the required specialization. The new proposed
increment is the exact coefficient-uniform distribution together with its
aggregated pole divisor and natural boundary.

1. Degree escape and a unique valley give a disjoint orbit parametrization.
2. Exact leading-coefficient exclusion counts valley representatives.
3. A rational two-dimensional cone series sums all representatives.
4. Normal convergence of the shifted cone tails gives continuation.
5. An explicit **combined** residue excludes cancellations and determines
   every pole; their accumulating lattices give the boundary.
6. Direct positive counting gives the asymptotic, retaining its lattice
   oscillation. No Tauberian theorem with a single-pole assumption is used.

## Proof

### Step 1. Degree escape and exhaustion

Write the entire orbit as $H^jP=(x_j,x_{j+1})$, so that

$$x_{j+1}+ax_{j-1}=f(x_j),\qquad j\in\mathbb Z.$$

Set $b_j=\max(0,\deg x_j)$. If $b_j\ge1$ and $b_j\ge b_{j+1}$,
then $\deg f(x_j)=db_j>b_{j+1}$, hence $b_{j-1}=db_j$. Repetition
forces all earlier degrees to grow by the factor $d$. If $b_j\le b_{j+1}$
and $b_{j+1}\ge1$, the same degree comparison in the forward recurrence
gives $b_{j+2}=db_{j+1}$ and subsequent factor-$d$ growth. Two consecutive
zero values of $b_j$ mean two constant coordinates; invariance of
$\mathbb F_q^2$ under both $H$ and $H^{-1}$ then makes the whole orbit
constant. Thus a nonconstant orbit cannot have two consecutive zero degrees.

Consequently every nonconstant orbit escapes in both time directions. To
verify the direction not already covered by one of the preceding comparisons,
move towards that direction until a nondecreasing adjacent pair occurs in
that time orientation. Failure to find one would give an infinite strictly
decreasing sequence of nonnegative integers; a plateau at positive degree
forces escape, and a plateau at zero would imply a constant orbit. This also
proves that the global minimum of the bi-infinite degree sequence is attained.
Escape excludes periodicity and ensures that all integer orbit iterates are
distinct.

At a strict minimum $b_j=n$, write its two neighbors as $b_{j-1}=b$,
$b_{j+1}=c$. Both exceed $n$. If $n\ge1$ and $b\ne c$, the recurrence
forces $\max(b,c)=dn$. The pair comprising $x_j$ and the smaller neighbor
then has two positive degrees $m,n$ satisfying $m<dn$ and $n<dm$.
If $b=c=M$, the recurrence forces $M\ge dn$ when $n\ge1$; the same
inequality holds when $n=0$. If the minimum is attained by two consecutive
equal values $n\ge1$, that adjacent pair satisfies both strict inequalities.
There cannot be three consecutive equal positive degrees, by factor-$d$
escape. These cases exhaust the possibilities.

It follows that every nonconstant orbit has exactly one of the following
representatives:

- **Edge representative**: $(x,y)$ with $m=\deg x\ge1$,
  $n=\deg y\ge1$, $m<dn$ and $n<dm$.
- **Turn representative**: $(x,y)$ with $M=\deg x\ge1$,
  $d\max(0,\deg y)\le M$ and $\deg(f(y)-ax)=M$.

For uniqueness, an edge representative has adjoining exterior degrees $dm$
and $dn$, and all farther degrees grow geometrically. Therefore no other
adjacent pair in this orbit satisfies the edge inequalities and no turn of
the second type occurs. A turn representative has the degree pattern

$$\ldots,d^2M,dM,M,n,M,dM,d^2M,\ldots,\qquad n\le M/d.$$

Its falling-to-rising orientation specifies a unique ordered representative;
the reversed adjacent pair is not a second turn representative. Its pattern
contains no edge representative. This proves disjointness and exhaustion.

### Step 2. Heights and properness

For an edge representative, strict domination in both directions gives

$$\bigl(\widehat h^-(P),\widehat h^+(P)\bigr)=(m,n),\qquad
\widehat h(H^kP)=d^{-k}m+d^kn.$$

For a turn representative the corresponding formulas are

$$\bigl(\widehat h^-(P),\widehat h^+(P)\bigr)=(M,M/d),\qquad
\widehat h(H^kP)=M(d^{-k}+d^{k-1}).$$

Indeed one forward iterate of a turn has both a degree-$M$ coordinate and
an immediately escaping future, accounting for the factor $1/d$. Constants
have height zero. The displayed degree patterns prove existence of every
limit in the definition and also give $h(P)\le\widehat h(P)$ for every
polynomial point: outside a central representative the largest coordinate
degree is one of the two positive summands of its canonical height, and at
the central representative it is at most their sum. Hence every bounded
canonical-height set is finite and is contained in the naive degree box
$h(P)\le\lfloor B\rfloor$.

An edge representative minimizes its total height along its orbit uniquely:
the ratio $n/m$ lies strictly between $1/d$ and $d$, so its first height
differences in both directions are positive and the subsequent differences
increase. A turn has exactly two equal adjacent minima, at $k=0,1$.
These observations will bound the indices in the point-counting argument.

### Step 3. Exact multiplicities

There are $(q-1)q^m$ polynomials of degree $m\ge1$ and $q$ constants.
Every pair of polynomials with degrees in the open edge cone is admissible,
so the number of edge representatives of degree pair $(m,n)$ is
$(q-1)^2q^{m+n}$.

For a fixed turn degree $M$, if $d\deg y<M$, the second turn condition
holds automatically. There are

$$ (q-1)q^M q^{\lfloor(M-1)/d\rfloor+1} $$

such pairs. If $M=dk$ and $\deg y=k\ge1$, the leading coefficient of
$x$ must avoid exactly one nonzero value, namely the value causing the
leading terms of $f(y)$ and $ax$ to cancel. For each $y$, this leaves
$(q-2)q^M$ choices of $x$; in particular it leaves zero in the case $q=2$,
which is included without exception. These boundary pairs number
$(q-1)(q-2)q^{(d+1)k}$. Adding the two disjoint counts yields

$$D_M=\begin{cases}
(q-1)^2q^{(d+1)k},&M=dk,\quad k\ge1,\\
(q-1)q^{(d+1)k+r+1},&M=dk+r,\quad k\ge0,\ 1\le r<d.
\end{cases}$$

Only the degree and the nonvanishing of the two specified coefficients were
used. Thus these counts are uniform over every prime power and all allowed
coefficients, including inseparable polynomials.

### Step 4. Exact positive series and rational sector formulas

The disjoint parametrization gives

$$\begin{split}
Z_H(s)=q^2
&+(q-1)^2\sum_{\substack{m,n\ge1\\m<dn,\ n<dm}}
q^{m+n}\sum_{k\in\mathbb Z}q^{-s(d^{-k}m+d^kn)}\\
&+\sum_{M\ge1}D_M\sum_{k\in\mathbb Z}
q^{-sM(d^{-k}+d^{k-1})}.
\end{split}\tag{1}$$

Initially this is an identity of nonnegative counting measures, or of
absolutely convergent series once that convergence is established below.
Define the cone generating function

$$T_d(A,B)=\sum_{\substack{m,n\ge1\\m<dn,\ n<dm}}A^mB^n
=\frac{AB}{(1-A)(1-B)}
-\frac{A^dB}{(1-A)(1-A^dB)}
-\frac{AB^d}{(1-B)(1-AB^d)}.\tag{2}$$

The first formula counts all positive pairs, and the two subtractions remove
the disjoint closed tails $m\ge dn$ and $n\ge dm$. The apparent poles
at $A=1$ or $B=1$ in this expression are removable away from the two cone
denominators. To justify this without cancellation guesswork, let $\mathcal P_d$
be the lattice points in

$$\{\alpha(d,1)+\beta(1,d):0<\alpha\le1,\ 0<\beta\le1\}.$$

Every lattice point of the strict cone has a unique expression as a point
of $\mathcal P_d$ plus nonnegative integer multiples of $(d,1),(1,d)$.
This follows by taking the two unique real coordinates in those independent
vectors and subtracting their ceilings minus one. Therefore

$$T_d(A,B)=
\frac{\sum_{(r,t)\in\mathcal P_d}A^rB^t}
{(1-A^dB)(1-AB^d)}.\tag{3}$$

All coordinates in $\mathcal P_d$ are positive and the set is finite.
Also set

$$D_{q,d}(z)=\sum_{M\ge1}D_Mz^M
=\frac{(q-1)^2q^{d+1}z^d+
(q-1)q\sum_{r=1}^{d-1}(qz)^r}{1-q^{d+1}z^d}.\tag{4}$$

For $k\in\mathbb Z$ put

$$A_k=q^{1-sd^{-k}},\quad B_k=q^{1-sd^k},\quad
C_k(s)=(q-1)^2T_d(A_k,B_k),\quad
z_k=q^{-s(d^{k-1}+d^{-k})},\quad E_k(s)=D_{q,d}(z_k).$$

Symmetry gives $C_{-k}=C_k$ and $E_{1-k}=E_k$. Consequently (1) becomes

$$Z_H(s)=q^2+C_0(s)+2\sum_{k\ge1}C_k(s)+2\sum_{k\ge1}E_k(s).\tag{5}$$

### Step 5. Absolute convergence and meromorphic continuation

The two cone denominators of $C_k$ are

$$1-q^{d+1-sL_k},\qquad 1-q^{d+1-sL_{k+1}},$$

and the denominator of $E_k$ is the first one. Here $L_0=L_1=d+1$,
and $L_k$ increases strictly for integers $k\ge1$. Thus all sector
power series converge absolutely when $\Re s>1$. On a compact subset
of $\Re s\ge\varepsilon>0$, as $k\to\infty$ the quantities $A_k$
remain bounded, $B_k$ decay as $O(q^{-\varepsilon d^k})$, and $z_k$
decay as $O(q^{-\varepsilon d^{k-1}})$. Formula (3), whose numerator has
positive $B$ exponents, and formula (4) then give uniform summable bounds
on the tails; their denominators tend uniformly to one. This proves absolute
convergence of (5) in $\Re s>1$ and locally normal meromorphic convergence
in $\Re s>0$. It also proves that the displayed candidate pole lattices
are the only possible poles in that half-plane.

To see that the absolute-convergence abscissa is exactly one, put $j=m+n$.
The number of positive pairs in the strict cone with that sum is

$$b_j=j-2\lfloor j/(d+1)\rfloor-1
=\frac{d-1}{d+1}j+O_d(1).\tag{6}$$

This follows from the two strict bounds $j/(d+1)<m<dj/(d+1)$.
The $k=0$ terms alone diverge for real $s\le1$, and absolute values at
complex $s$ give those same terms with $s$ replaced by $\Re s$.

### Step 6. The combined residue: no hidden pole cancellation

Fix $k\ge2$ and $s_0=s_{k,\ell}$. Only $C_{k-1}$, $C_k$ and $E_k$
have a possible pole there, and each occurs with coefficient two in (5).
In (2), the coefficients of $(1-q^{d+1-sL_k})^{-1}$ from the two cone
sectors, evaluated at $s_0$, are respectively

$$\frac{(q-1)^2}{B_{k-1}(s_0)-1},\qquad
\frac{(q-1)^2}{A_k(s_0)-1}.$$

Set $A=A_k(s_0)$ and $v=(qz_k(s_0))^{-1}$. Since
$q^{d+1}z_k(s_0)^d=1$, we have $v^d=q$. Moreover

$$A B_{k-1}(s_0)=q^2z_k(s_0)=q/v.$$

Adding the numerator from (4), the full coefficient before the overall
factor two is

$$R= (q-1)^2\left(\frac1{A-1}+\frac{A}{q/v-A}+1\right)
 +(q-1)q\sum_{r=1}^{d-1}v^{-r}.\tag{7}$$

The finite geometric sum is $(q-v)/(q(v-1))$. Combining the rational
terms gives the exact factorization

$$R=\frac{(q-1)(q-v)(q-A)(vA-1)}
{(v-1)(A-1)(q-vA)}.\tag{8}$$

For completeness, after factoring $(q-1)(q-v)$, the remaining numerator
is $(q-1)A(v-1)+(A-1)(q-vA)=(q-A)(vA-1)$.
Let $u=q^{1/d}$. At the selected point $|v|=u$, and for $k\ge2$,

$$q/u<|A|=q^{1-(d+1)/(d^kL_k)}<q.$$

Every numerator and denominator factor in (8) is therefore nonzero:
$|v|>1$, $q>|v|$, $|A|>1$, $|A|<q$, and $|vA|>q>1$.
Thus every $s_{k,\ell}$ with $k\ge2$ is a genuine simple pole, with

$$\operatorname{Res}_{s=s_0}Z_H(s)=\frac{2R}{L_k\log q}.\tag{9}$$

For $k=1$, $C_0$ has both cone denominators equal. If
$B_0(s_0)=q^{1-s_0}\ne1$, its singular coefficient is
$2(q-1)^2/(B_0(s_0)-1)$ by (2). Therefore the same formulas (7)–(9)
hold. Now $|A|=q/u$, so $|vA|=q$; the denominator $q-vA$ vanishes
exactly when $B_0=1$. Excluding that case, all remaining factors are still
nonzero, proving a simple pole.

Finally $B_0(s_0)=1$ exactly when $(d+1)\mid\ell$. By (6), or directly
by (2) with $A=B=q^{1-s}$, the coefficient of $(s-s_0)^{-2}$ in $C_0$
is

$$\frac{(q-1)^2(d-1)}{(d+1)(\log q)^2}>0.$$

The other sectors have at most simple poles, so it cannot cancel. This
proves the entire claimed pole divisor, including every small-characteristic
and root-of-unity phase case. It is an aggregation proof, not summandwise
natural-boundary reasoning.

### Step 7. Natural boundary

As $k\to\infty$, $(d+1)/L_k\to0$ and the imaginary spacing
$2\pi/(L_k\log q)\to0$. For every real $\tau$, select an integer
$\ell_k$ nearest to $\tau L_k\log q/(2\pi)$. Then the genuine poles
$s_{k,\ell_k}$ converge to $i\tau$. A meromorphic extension to a
neighborhood of $i\tau$ would have poles accumulating at an interior
point; a meromorphic function has only isolated poles unless it is the
identically infinite object, which cannot agree with the initial series.
Such an extension is impossible. The imaginary axis is a meromorphic
natural boundary.

### Step 8. The height-count asymptotic

Let $N=\lfloor B\rfloor$ and $\alpha=(d-1)/(d+1)$. The central
edge contribution is, by (6),

$$ (q-1)^2\sum_{j\le N}b_jq^j
=\alpha(q-1)q^{N+1}N+O_{q,d}(q^N).\tag{10}$$

One may verify the leading coefficient using the finite derivative of the
geometric sum; equivalently $\sum_{j\le N}jq^j=
q^{N+1}N/(q-1)+O_q(q^N)$.

The contributions of $C_1$ and $C_{-1}$ are $O_{q,d}(q^B)$. For $C_1$
write $e=dn-m\ge1$. Its height is $(d+1)n-e/d$, and its weight is
$(q-1)^2q^{(d+1)n-e}$. For each fixed $e$, sum the geometric progression
in $n$ up to that height bound, enlarging to all admissible positive $n$.
The sum is at most a constant times $q^{B-(1-1/d)e}$; summing over
$e\ge1$ is convergent. Symmetry treats $C_{-1}$. For turn shifts $k=0,1$,
$D_M\le c_{q,d}q^{(1+1/d)M}$, and a geometric sum in $M$ gives the
same $O(q^B)$ bound.

For all edge shifts $|k|\ge2$, the open cone inequalities imply

$$m+n\le\alpha_2(d^{-k}m+d^kn),\qquad
\alpha_2=\frac{d+1}{d^2+d^{-1}}<1.$$

For turn shifts $k\notin\{0,1\}$, the analogous inequality is
$(1+1/d)M\le\alpha_2M(d^{-k}+d^{k-1})$. At height at most $B$, core
degrees are at most $B$ by minimality, and only $O_d(1+\log(1+B))$
shifts can contribute: every edge height is at least $d^{|k|}$, and every
turn height is at least $d^{\max(k-1,-k)}$. The remaining total is
therefore $O_{q,d}(B^2(1+\log(1+B))q^{\alpha_2B})=O_{q,d}(q^B)$.
Constants contribute $q^2$. Combine these bounds with (10) and replace
$N$ by $B$ in its leading linear factor, at cost $O(q^B)$. This proves
the stated real-$B$ asymptotic, including its nonconstant fractional-part
oscillation. The proof is complete.

## Verification, corrections and open risks

The executable `check_height_valleys.py` compared literal polynomial
iteration with the independently specified valley multiplicities in eleven
prime-field cases, testing 77,974 pairs. Every exact rational-height
distribution matched; coefficients, degree and Jacobian were varied. This
tests implementation and small cases, not arbitrary prime powers or the
infinite pole theorem. Its exact command and receipt belong in the check
record. Formula (8) is algebraic and will receive an independent symbolic
and proof review.

The original candidate's unspecified natural-boundary argument has been
replaced here by the combined-residue identity, proving every candidate pole,
not merely a dense subset. No domain enlargement was made. The classical
height construction is explicitly deducted from the proposed increment.
Independent non-author proof/source assessment remains the admission gate;
bounded web searching cannot establish worldwide priority. Hsia's original
full text has not yet been retrieved, and the exact accessible Takehira and
Ingram versions must be recorded without promoting metadata to full reading.
