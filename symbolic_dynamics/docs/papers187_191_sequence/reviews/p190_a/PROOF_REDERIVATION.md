# P190 Review A — proof rederivation

## Claim status and assumptions

**Formal status: proved as stated.**  Let

\[
B_n=\{0\}\cup([n]\times[n]),\qquad
(a,b)(c,d)=\begin{cases}(a,d),&b=c,\\0,&b\ne c,\end{cases}
\]

with absorbing zero, and let `*` transpose a matrix unit and fix zero.  For a
cyclic word of positive length `m`, define
`T(x)_i=x_i x_{i+1}x_i`.  Every index below is modulo `m`.  No proof step
assumes `n>=2` except the off-diagonal sharpness witnesses, and no step drops
`m=1,2`.

The source typo in Eq. (11) is separated from the theorem: the meaningful
matrix factor has exactly two indices, row `y_{i_j}^*` and column
`y_{i_{j+1}}`.

## 1. Literal filter and all times

For nonzero `u=(a,b)` and `v=(c,d)`, the product `(uv)u` is nonzero exactly
when `b=c` and `d=a`.  Equivalently, `v=(b,a)=u^*`, and the output is then
`u`.  If either relevant product is zero, the output is zero.  Therefore

\[
uvu=u\,\mathbf 1\{u\ne0,\ v=u^*\}.
\]

Write `g_i=1{x_i!=0, x_{i+1}=x_i^*}`.  I rederive by induction that

\[
(T^t x)_i=x_i\prod_{j=0}^{t-1}g_{i+j},\qquad t\ge0,
\]

where multiplication by the binary product means retain `x_i` iff every
factor is one, and the `t=0` product is empty.  At the induction step, the
two length-`t` survival windows at `i` and `i+1` unite to the length-`t+1`
window `i,...,i+t`; its first edge supplies the required inverse relation.
This argument remains valid after the window wraps around the cycle any
number of times.  Hence it is genuinely all-time, not merely a first-lap
formula.

## 2. Recurrence, pointwise tail, and parity sharpness

The formula only retains an original letter or changes it to zero, so support
never increases.  A non-all-good word loses every nonzero site after at most
`m` steps.  An all-good word is fixed, as is the all-zero word.  Thus every
recurrent point is fixed.

Any nonzero fixed word obeys `x_{i+1}=x_i^*` around the whole cycle.  If `m`
is odd, closure requires `x_0=x_0^*`, giving `n` diagonal choices.  If `m`
is even, any of the `n^2` units may start the alternating word.  Adding zero
gives `1+n` and `1+n^2` fixed points respectively.

For a word that is neither zero nor all-good, let `L` be the longest cyclic
run of good edges.  A coordinate at the start of such a run survives through
time `L`, while no coordinate survives time `L+1`; therefore its tail is
exactly `L+1`.

- If `n>=2` and `m` is odd, alternation from an off-diagonal unit over `m-1`
  edges leaves exactly the closing edge bad, so the maximum tail is `m`.
- If `n>=2` and `m` is even, one bad edge is impossible: the other odd number
  of inverse steps forces the omitted relation.  Two adjacent bad edges are
  attainable, so the maximum tail is `m-1`.
- If `n=1`, the only good edges are `ee`.  A mixed cyclic binary word has at
  most `m-2` consecutive good edges, attained by one zero and `m-1` copies of
  `e` for `m>=2`.  Thus the maximum is `max(0,m-1)`.

For `m=1`, zero and the `n` diagonal units are fixed and every off-diagonal
unit has tail one.  For `m=2`, each `(u,u^*)` is fixed and every other word
maps to zero in one step.  These directly settle the requested short-carrier
boundaries.

## 3. Trace and correctly oriented gap product

Define the output-labelled adjacency matrices with rows as current source
letters and columns as next source letters:

\[
M_y(u,v)=\mathbf 1\{uvu=y\}.
\]

Expanding the ordered trace gives

\[
\operatorname{tr}(M_{y_0}\cdots M_{y_{m-1}})
=\sum_{u_0,\ldots,u_{m-1}}
 \prod_i M_{y_i}(u_i,u_{i+1}),
\]

so its summands are exactly the cyclic source words mapped to `y`.  This also
fixes the row/column convention before any matrix simplification.  For a
nonzero letter `y`, `M_y` has its sole one at ordered pair `(y,y^*)`; for an
off-diagonal unit the reversed pair belongs to `M_{y^*}`, not `M_y`.

Let `A=M_0`.  A nonzero target at site `i_j` pins
`u_{i_j}=y_{i_j}` and `u_{i_j+1}=y_{i_j}^*`.  If `h_j` zero targets occur
before the next nonzero target, the number of compatible intervening paths is

\[
(A^{h_j})_{y_{i_j}^*,\,y_{i_{j+1}}}.
\]

Different gaps meet only at already pinned endpoints, hence their counts
multiply.  With no anchor, cyclic closure instead gives `tr(A^m)`.  Notice
that `A` happens to be symmetric, so a numeric check using only `A` cannot by
itself certify the declared direction; the entry-level test on nonzero `M_y`
is essential and is included in the reviewer verifier.

## 4. Zero-output spectrum

Put `r=n^2`.  The row of `A` indexed by zero is all ones.  A nonzero row
indexed by `u` is all ones except at column `u^*`.  Consequently `A` is
symmetric.  On vectors supported on units with coefficient sum zero,
`A=-P`, where `P` is the permutation induced by `u -> u^*`.

The involution has `n` fixed units and `(r-n)/2` two-cycles.  Its `+1` and
`-1` multiplicities are `(r+n)/2` and `(r-n)/2`.  Removing the all-unit
vector from the first subspace gives eigenvalue `-1` of `A` with multiplicity
`(r+n)/2-1`; the second gives eigenvalue `+1` with multiplicity `(r-n)/2`.

On the remaining span of `e_0` and the all-unit vector `w`,

\[
A e_0=e_0+w,\qquad A w=r e_0+(r-1)w.
\]

The corresponding block has trace `r`, determinant `-1`, and characteristic
polynomial `z^2-rz-1`.  Its root power sum has `s_0=2`, `s_1=r`, and
`s_k=r s_{k-1}+s_{k-2}`.  Since the symmetric matrix is diagonalizable,
adding all eigenvalue powers yields

\[
\operatorname{tr}(A^m)=s_m+(-1)^m\left(\frac{r+n}{2}-1\right)
+\frac{r-n}{2}.
\]

The verifier independently confirms the two nullities over the rationals,
the two-dimensional block, and traces through exponent 12 for `n=1,...,5`.

## 5. Image and mass

The anchored fibre product is positive precisely when every factor is.
For gap zero, `A^0=I`, giving next anchor `y^*`.  For gap one,
`A(y^*,z)=0` exactly when `z=y`.  For gap at least two, the zero letter gives
a path from any start to zero and then to any endpoint (with zero loops in
between), so all entries are positive.  The all-zero target has the all-zero
source.  This proves the stated image criterion in both directions.

Finally, every ordered source pair has exactly one local output, hence
`sum_y M_y=J_q`.  Distributivity in the ordered product gives

\[
\sum_{y\in B_n^m}|T^{-1}(y)|=\operatorname{tr}(J_q^m)=q^m.
\]

This includes empty fibres and `m=1`.  No theorem repair was required; the two
Round-0 presentation repairs in `DELTA.md` are accepted in Round 1.
