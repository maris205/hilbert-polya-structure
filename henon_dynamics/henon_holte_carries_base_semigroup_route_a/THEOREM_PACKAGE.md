# C194 theorem package

## 1. Frozen phase space and clock

Fix integers `n>=1` and `b>=2`.  The phase space is

\[
X_n=\{0,1,\ldots,n-1\}.
\]

At one clock step, independently sample
`d_1,...,d_n` uniformly from `{0,...,b-1}`.  From carry-in `i`, the carry-out is
the unique `j` satisfying

\[
 jb\le i+d_1+\cdots+d_n<(j+1)b.
\]

Rows act on row distributions.  This is a stochastic clock; it is not silently
replaced by a deterministic map on a larger path space.

## 2. Holte transition formula — classical theorem

Introduce the output remainder as a slack digit.  Holte's Theorem 1 gives

\[
P_b(i,j)=b^{-n}[x^{(j+1)b-1-i}]
 (1+x+\cdots+x^{b-1})^{n+1}.
\]

Equivalently,

\[
P_b(i,j)=b^{-n}\sum_{r\ge0}(-1)^r{n+1\choose r}
 {n+(j+1-r)b-1-i\choose n},
\]

where an inadmissible binomial coefficient is zero.  The producer reconstructs
the digit-sum polynomial by convolution; the independent checker instead uses
this slack-variable inclusion--exclusion formula.

## 3. Base semigroup — classical theorem with direct mixed-radix proof

For all integers `a,b>=2`,

\[
P_aP_b=P_{ab}.
\]

Indeed, first write
`i+sum(x_h)=a k+r` with `0<=x_h<a`, then
`k+sum(y_h)=b j+s` with `0<=y_h<b`.  The combined digits
`x_h+a y_h` are independent uniform base-`ab` digits, and

\[
i+\sum_h(x_h+a y_h)=abj+(as+r),\qquad0\le as+r<ab.
\]

Consequently `P_b^r=P_(b^r)` for every integer `r>=0`, with the zeroth power
interpreted as the identity.

## 4. Complete diagonalization and Eulerian stationarity — Holte Theorem 3

For `0<=k,j<n`, define

\[
V_{k j}=\sum_{r=0}^{j}(-1)^r{n+1\choose r}(j+1-r)^{n-k}.
\]

Holte proves

\[
V P_b V^{-1}=\operatorname{diag}(1,b^{-1},\ldots,b^{-(n-1)}).
\]

Thus the spectrum is simple and the left/right eigenvectors do not depend on
the base.  The first row of `V` is the Eulerian row, so the unique stationary
probability is

\[
\pi_n(j)=\frac{A(n,j)}{n!},\qquad0\le j<n.
\]

For `n=1`, `P_b=[1]`; this boundary is retained rather than excluded.

## 5. Exact operator corollaries

For every `r>=0`,

\[
\operatorname{tr}(P_b^r)=\sum_{k=0}^{n-1}b^{-rk},\qquad
\det(I-zP_b)=\prod_{k=0}^{n-1}(1-zb^{-k}),
\]

and

\[
\chi_{P_b}(x)=\prod_{k=0}^{n-1}(x-b^{-k}).
\]

Let `E_k` be the common spectral projectors determined by `V`.  Then

\[
P_b^r-E_0=\sum_{k=1}^{n-1}b^{-rk}E_k,
\]

an exact finite-dimensional convergence identity.  Diaconis--Fulman Theorem
3.3 additionally gives, for `n>=3`, every start `i`, and every `r>=0`,

\[
\lVert P_b^r(i,\cdot)-\pi_n\rVert_{\rm TV}
 \le \frac{(n-1)/2+i}{b^r}.
\]

The package attributes the convergence theory to its source; it does not claim
this as a new bound.

## 6. Prime/composite control and stopping boundary

The theorem depends on the integer base only through the displayed powers of
`b`.  Bases `2,3,5,7` and `4,6,8,9,10` are separately tagged in the evidence,
and both classes pass the same identities.  A prime base is not thereby a
rational-prime primitive orbit, and the clock is one digit column rather than
`log p`.

`det(I-zP_b)` is a finite Markov determinant.  The stochastic matrix has no
unweighted deterministic Artin--Mazur owner on the frozen state space.  A
chosen inner product can make a real simple-spectrum matrix self-adjoint by
similarity, but that construction is noncanonical and supplies only
`A4_FORMAL_HINT`.

## 7. Route-A verdict

The exact tuple is

`(A0_WEAK_ARITHMETIC_RELATION,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`.

Overall: `ROUTE_A_REJECTED`.  Route B is false.  Target tables, arithmetic
local data, Euler factors, root numbers, automorphy, target functional
equations and Hilbert--Polya claims are outside scope.
