# LNR inverse and sharp fibre maximum — author proof package

2026-09-06 UTC. Mathematical contributor: `batch197_fosp_gate`.
Candidate only; not admitted, numbered, independently reviewed or released.
This contributor is an author and cannot independently review an eventual LNR paper.

## Claim

For the labelled cyclic carrier $\{0,1,2\}^n$, $n\ge3$, let
$$F(x)_i=\mathbf1_{\{x_{i-1}<x_i\}}+\mathbf1_{\{x_{i+1}<x_i\}}.$$
The inverse set of every target has the explicit zero-block decoder in
Step 2 below. Its cardinality is evaluated by the eight displayed kernels.
Let $L_0=2$, $L_1=1$, and $L_{t+2}=L_{t+1}+L_t$ be the Lucas numbers. Then
$$\max_{b\in\{0,1,2\}^n}|F^{-1}(b)|=L_{2\lfloor n/2\rfloor}.$$
All equality targets, at their original labelled positions, are precisely:

- for even $n=2m\ge4$, the two rotations of $(02)^m$;
- for odd $n=2m+1\ge5$, the rotations of $00(20)^{m-1}2$ and
  $011(02)^{m-1}$, giving exactly $2n$ targets;
- for $n=3$, the three rotations of $002$, the three rotations of $011$,
  and $000$, giving seven targets.

## Status

**PROVABLE AS STATED.** This is an author deduction, not a candidate-gate
decision. The classical value of the alternating fibre and the generic
trace/decoder mechanism receive no separate originality credit. The
potential residual is the sharp extremum over *all* target block words,
including mixed kernels, together with the complete equality classification.

## Assumptions

- Updates are synchronous and use strict comparisons of old values.
- The two cyclic neighbours are distinct because $n\ge3$.
- Rotations and reflections are symmetries, not quotient identifications.
- The alphabet is exactly $\{0,1,2\}$; no larger-alphabet theorem is inferred.

## Notation

For a target containing both zero and positive symbols, write its maximal
cyclic zero runs as $Z_1,\ldots,Z_r$, in forward cyclic order. The nonempty
positive word between $Z_j$ and $Z_{j+1}$ is $w_j$, with $Z_{r+1}=Z_1$.
The chosen start is a proof device only: the decoder keeps the original
coordinate indices. Put $a_j\in\{0,1,2\}$ for the common source height on
$Z_j$. Matrices below have row/column order $0,1,2$.

For a real square matrix $M$, $\|M\|_p=(\sum_i\sigma_i(M)^p)^{1/p}$ is
its Schatten $p$-norm, where $\sigma_i(M)$ are its singular values. Define
$$\lambda=(3+\sqrt5)/2.$$

## Proof strategy

Compress constant source heights on target-zero runs, enumerate the few
possible positive source runs, and count the resulting cyclic choices.
For the extremum, dominate five of the eight kernels entrywise by one
positive kernel $A$. The remaining kernels $A,J,B$ are controlled with
explicit Schatten-norm estimates and the target's length budget. Treat
zero or one positive block separately; enforce strictness before listing
the attaining targets.

## Dependency map

1. The inverse decoder uses only strict local comparisons and the ternary alphabet.
2. The eight-kernel table follows from the complete local source lists in Step 2.
3. The trace expression is a finite cyclic sum, not an asserted new transfer theorem.
4. The sharp bound uses Step 3's standard matrix Hölder inequality, the explicit
   spectra/norms in Step 4, and the length budget in Step 5.
5. Equality requires the separate small-$r$ analysis and strict mixed-kernel bounds.
6. The Lucas evaluation uses $A$'s quadratic characteristic equation. It does not
   depend on numerical tests or on root's independent temporal theorem.

## Proof

### Step 1. Zero blocks and bounded positive runs

Every source has a global minimum; at that coordinate its output is zero.
Thus a target without a zero has an empty fibre. If the target is $0^n$,
each source value is at most both neighbours. Applying the two inequalities
across each edge forces equality, so its inverse consists exactly of the
three constant sources.

Suppose now that a target has both zero and positive coordinates. Across
an edge whose two outputs are zero, both endpoint source values are at
most one another, so they are equal. Consequently each $Z_j$ has a common
source height $a_j$. At the two boundaries of this zero run, its source
height must be at most the adjacent positive-run source value. This
condition is needed even when the zero run has length one.

A positive target coordinate cannot have source value zero. Inside a
positive run of length at least three, an interior source value one would
have two neighbours in $\{1,2\}$ and output zero. Every interior source
letter is therefore two. A positive run of length at least five would
have three consecutive interior twos, whose middle output is zero. Hence
only lengths one through four can occur.

### Step 2. Complete local lists and exact cyclic decoder

For a positive target word $w$ and exterior zero-block heights $a,b$,
let $\mathcal P_w(a,b)$ be the positive source strings $u$ with the
following two properties: $a\le u_1$, $b\le u_{|w|}$; and applying the
literal comparison rule at the positions of $u$, with outside values
$a,b$, gives exactly $w$. These boundary inequalities guarantee zero
outputs on the adjacent zero blocks. Define
$$K_w[a,b]=|\mathcal P_w(a,b)|.$$

The complete lists are as follows. Conditions not listed give no string.
Separate bullet entries that apply at the same pair $(a,b)$ contribute
distinct strings, not duplicate ways of counting one source.

- $w=2$: $u=1$ if $a=b=0$; $u=2$ if $a,b\in\{0,1\}$.
- $w=1$: $u=1$ if $(a,b)\in\{(0,1),(1,0)\}$;
  $u=2$ if $(a,b)\in\{(0,2),(1,2),(2,0),(2,1)\}$.
- $w=11$: $u=11$ if $a=b=0$; $u=22$ if $a,b\in\{0,1\}$;
  $u=12$ if $(a,b)=(0,2)$; $u=21$ if $(a,b)=(2,0)$.
- $w=12$: $u=12$ if $a=0$ and $b\in\{0,1\}$.
- $w=21$: $u=21$ if $a\in\{0,1\}$ and $b=0$.
- $w=111$: $u=122$ if $a=0$ and $b\in\{0,1\}$;
  $u=221$ if $a\in\{0,1\}$ and $b=0$.
- $w=121$: $u=121$ if $a=b=0$.
- $w=1111$: $u=1221$ if $a=b=0$.

For length one this checks the two possible source heights. For length
two it checks exactly $11,12,21,22$. For length three Step 1 fixes the
middle source to two; $222$ fails, leaving $122,221,121$. For length four
Step 1 fixes the middle pair to $22$; positivity at those two positions
forces both endpoints to one. This proves completeness, not just
compatibility, of the list. The resulting matrices are
$$
A=K_2=\begin{pmatrix}2&1&0\\1&1&0\\0&0&0\end{pmatrix},\qquad
J=K_1=\begin{pmatrix}0&1&1\\1&0&1\\1&1&0\end{pmatrix},\qquad
B=K_{11}=\begin{pmatrix}2&1&1\\1&1&0\\1&0&0\end{pmatrix},
$$
$$
D=K_{12}=\begin{pmatrix}1&1&0\\0&0&0\\0&0&0\end{pmatrix},\qquad
K_{21}=D^T,\qquad
C=K_{111}=\begin{pmatrix}2&1&0\\1&0&0\\0&0&0\end{pmatrix},
$$
$$K_{121}=K_{1111}=E=\begin{pmatrix}1&0&0\\0&0&0\\0&0&0\end{pmatrix}.$$
Every other positive word has the zero matrix. In particular, equality
of two matrices does not identify their target words or their lengths.

Here is a full inverse-set bijection. Choose $a_1,\ldots,a_r$; fill each
actual zero-run position in $Z_j$ with $a_j$; independently choose and
place one string from $\mathcal P_{w_j}(a_j,a_{j+1})$ on each positive
run. Every constructed word has the desired output by the boundary
conditions and local lists. Conversely, Step 1 and the complete lists
recover exactly these choices from any source. Recoverability proves
injectivity. Therefore
$$|F^{-1}(b)|=\sum_{a_1,\ldots,a_r=0}^2
\prod_{j=1}^r K_{w_j}[a_j,a_{j+1}]
=\operatorname{tr}(K_{w_1}\cdots K_{w_r}).\tag{1}$$
This also handles $r=1$: the two exterior heights coincide, as imposed
by the trace. Choosing another start cyclically permutes factors and
does not multiply the answer or remove any labelled sources. Zero-run
lengths affect the coordinate reconstruction but not the matrices.

### Step 3. The matrix inequality used, with its precise hypotheses

For $r\ge2$ and real square matrices $M_1,\ldots,M_r$ of equal size,
$$|\operatorname{tr}(M_1\cdots M_r)|\le\prod_{j=1}^r\|M_j\|_r.\tag{2}$$
This is the standard multifactor Schatten Hölder inequality; neither
positivity nor commutation nor invertibility is required. One precise
source is Tropp's *Matrix Analysis*, Theorem 6.32, printed p. 52, with
the Schatten norms of Example 6.18; the actual relevant context is
recorded in [SOURCE_BOUNDARY.md](SOURCE_BOUNDARY.md).

For completeness, its reduction from the stated two-factor norm theorem
is explicit. That theorem, applied in Schatten norm $t\ge1$ with
conjugate exponents $p,q>1$, gives
$$\|UV\|_t\le\|U\|_{pt}\|V\|_{qt}.$$
In an induction building the first $s$ factors, use
$t=r/s$, $p=s/(s-1)$ and $q=s$, for $2\le s\le r$. It follows that
$\|M_1\cdots M_s\|_{r/s}\le\prod_{j=1}^s\|M_j\|_r$.
Finally $|\operatorname{tr}P|\le\|P\|_1$: in an SVD $P=U\Sigma V^T$,
cyclicity of trace gives a sum of singular values times diagonal entries
of the orthogonal matrix $V^TU$, all of absolute value at most one.
This proves (2) from that named standard theorem with no exponent gaps.

### Step 4. A bound for every word in the three remaining kernels

All entries are nonnegative, and $D,D^T,C,E\le A$ entrywise. Expanding
the trace as a sum of products shows that replacing any of these five
target-word kernels by $A$ cannot decrease (1). No matrix-order or
commutation assertion is being used.

Fix a product length $r\ge2$. Let $k$ be the number of $B$ factors and
$j$ the number of $J$ factors after these replacements. The nonzero
eigenvalues of $A$ are $\lambda,\lambda^{-1}$, both positive, so put
$$a_r=\|A\|_r=(\lambda^r+\lambda^{-r})^{1/r}.$$
The singular values of $J$ are $2,1,1$, and $\|B\|_2=3$ by summing
the squares of its entries. Monotonicity of finite-vector $\ell^p$
norms gives
$$\|J\|_r\le\sqrt6<\lambda<a_r,\qquad \|B\|_r\le3.$$
For $r\ge3$ we also have $\|J\|_r\le\sqrt[3]{10}$ and
$$3\sqrt[3]{10}<\lambda^2\le a_r^2.\tag{3}$$
For example $\lambda>13/5$ proves (3) by cubing and using
$169^3>270\cdot25^3$. The inequality $\sqrt6<\lambda$ follows from
$\lambda^2=(7+3\sqrt5)/2>6$.

If $k=0$, (2) bounds the trace by $a_r^r=\lambda^r+\lambda^{-r}$.
The bound is strict if $j>0$.

If $k=1$ and $j=0$, cyclicity puts $B$ first, and direct multiplication
of its leading $2\times2$ block gives
$$\operatorname{tr}(BA^{r-1})=\operatorname{tr}(A^r)
=\lambda^r+\lambda^{-r}.\tag{4}$$
Here $r-1\ge1$ kills the third row/column contribution. If $k=1$ and
$j>0$, for $r=2$ the product is $BJ$ and its trace is $4<7$.
For $r\ge3$, combine one $B$ and one $J$ *in the scalar product of
norm bounds* using (3); every additional $J$ has norm less than $a_r$.
Equation (2) again gives a strict bound below $a_r^r$.

If $k\ge2$, (2) instead gives
$$\operatorname{tr}(M_1\cdots M_r)\le a_r^{r-k}3^k
<\frac{10}{9}\lambda^{r-k}3^k
<\lambda^{r+\lfloor k/2\rfloor}.\tag{5}$$
To justify both strict inequalities uniformly, $\lambda^4>9$ yields
$(a_r/\lambda)^r=1+\lambda^{-2r}<10/9$, so the first holds for
$0\le r-k\le r$, including $r=k$. The second is equivalent to
$\frac{10}{9}3^k<\lambda^{k+\lfloor k/2\rfloor}$. Its cases $k=2,3$
are $10<\lambda^3$ and $30<\lambda^4$. Increasing $k$ by two
multiplies the left side by $9$ and the right by $\lambda^3>9$.
This proves (5) for every integer $k\ge2$.

### Step 5. Length budget and the sharp upper bound

Each positive run and a following nonempty zero run use at least two
target positions. Each $B=K_{11}$ uses at least one further position.
Therefore
$$n\ge2r+k.\tag{6}$$
The even Lucas subsequence satisfies
$$L_{2s}=\lambda^s+\lambda^{-s},\qquad s\ge0,$$
because both sides start at $2,3$ for $s=0,1$ and satisfy
$V_{s+2}=3V_{s+1}-V_s$. It is strictly increasing for $s\ge1$.

For $r\ge2$ and $k\le1$, Step 4 bounds the trace by $L_{2r}$,
which is at most $L_{2\lfloor n/2\rfloor}$ by (6). For $k\ge2$,
(5), (6) and $\lfloor n/2\rfloor\ge r+\lfloor k/2\rfloor$ give a
*strict* upper bound below $L_{2\lfloor n/2\rfloor}$.

The omitted cases cause no exception to the bound. With no positive
run the fibre is $3$. With one positive run the traces of
$J,A,B,D,D^T,C,E$ are $0,3,3,1,1,2,1$. Every other run has trace zero.
Thus for $n\ge4$, these cases are strictly below $L_4=7$. When $n=3$,
at most one positive run exists, and precisely $000$ and the rotations
of $002,011$ have fibre three. This proves the upper bound and the
stated equality list at $n=3$.

### Step 6. Exhaustive equality classification for larger lengths

Now let $n\ge4$ and suppose equality holds. Step 5 forces $r\ge2$,
$k\le1$, and
$$q:=n-2r\in\{0,1\}.$$
Indeed if $q\ge2$, then $L_{2r}<L_{2\lfloor n/2\rfloor}$.

If $q=0$, every positive run and zero run has length one. The only
nonzero kernels are $A,J$, and Step 4 makes any $J$ strict. Hence all
positive runs are $2$ and the target alternates $02$. Conversely such
a target has trace $\operatorname{tr}A^r=L_{2r}$.

If $q=1$, exactly one run, zero or positive, has one extra position.
When it is a zero run, every positive run has length one; absence of
$J$ is necessary and sufficient. Thus the target has a unique $00$
run, all other zeros isolated, and every positive run equal to $2$.
These are precisely the rotations of $00(20)^{r-1}2$.

When the extra position lies in a positive run, that run has length two.
The possible nonzero kernels are $B,D,D^T$; all remaining positive
runs have kernels $A$ or $J$. For $B$, Step 4 excludes any $J$ and
(4) proves equality when all other factors are $A$. The targets are
the rotations of $011(02)^{r-1}$.

For $D$ or $D^T$, the entrywise replacement makes $k=0$. If there is a
$J$, Step 4 already gives strictness. Without a $J$, strictness still
holds: $A^{r-1}$ has four strictly positive entries in its leading
$2\times2$ block, while both $A-D$ and $A-D^T$ are nonzero and
nonnegative in that block. Expanding the trace therefore gives
$$\operatorname{tr}(DA^{r-1})<\operatorname{tr}(A^r),\qquad
\operatorname{tr}(D^TA^{r-1})<\operatorname{tr}(A^r).$$
No longer positive run fits the single extra position. This exhausts
all cases with $q=1$ and proves necessity as well as attainment.

For an even length the alternating word has exactly two labelled
rotations. For an odd length the first family has a unique double-zero
run and the second a unique $11$ run. Either unique feature forbids a
nontrivial rotational stabilizer, giving $n$ distinct rotations per
family; the presence or absence of symbol one separates the families.
Thus there are exactly $2n$ odd-length equality targets. This completes
the claimed maximum and full equality classification. $\square$

## Corrections or missing assumptions

None for the stated ternary $n\ge3$ theorem. This document does not prove
root's temporal theorem and does not reuse it as an inverse premise.

## Open risks

The source/value gate is not complete merely because the proof is complete.
Classical crown order maps, independent sets and transfer matrices already
evaluate the alternating extremizers; they are explicitly deducted in
[SOURCE_BOUNDARY.md](SOURCE_BOUNDARY.md). An independent assessor must
decide whether a prior exact adapter also supplies the mixed-target sharp
comparison and all equality cases. No literature nonhit is a novelty proof.
Finite verification is evidence against implementation/proof transcription
errors, not the all-parameter justification above. HOLD_EXTERNAL remains.
