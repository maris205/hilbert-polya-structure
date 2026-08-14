# Derivation Package — SD-C23

## 1. From full shifts to the successor–divisor grammar

Let \(F_n=A_n^{\mathbb Z}\) denote the full shift on an \(n\)-letter
alphabet.  Two alphabet-level operations give

\[
 F_m\boxtimes F_n\cong F_{mn},
 \qquad
 F_m\boxplus F_n\cong F_{m+n}.
\]

Here \(\boxplus\) is the full shift on the disjoint union of alphabets; it is
not a topological disjoint union of phase spaces.  Define the intrinsic
successor operation

\[
 S(F_n)=F_n\boxplus F_1\cong F_{n+1}.
\]

Demanding a nonunit tensor factor gives

\[
 S(F_n)\cong F_d\boxtimes F_q
 \quad\Longleftrightarrow\quad
 n+1=dq,qquad d\ge2, q\ge1.
\]

After forgetting the exposed quotient \(q\) but retaining the factor \(d\),
the transition rule is

\[
 n\to d\iff d\mid n+1,quad d\ge2.
\]

The quotient is uniquely recoverable as \(q=(n+1)/d\).  This derivation uses
successor, multiplication, and equality only; it does not call a prime
predicate.

## 2. From entropy to endpoint weights

Full-shift entropy is \(h(F_n)=\log n\).  The symmetric endpoint roof is

\[
 \tau(n,d)=h(F_n\boxtimes F_d)=\log n+\log d.
\]

Its Laplace weight is

\[
 e^{-s\tau(n,d)}=(nd)^{-s}.
\]

For the column-source convention,

\[
 (L_s)_{d,n}=\mathbf1_{d\mid n+1,\ d\ge2}(nd)^{-s},
\]

so

\[
 L_se_n=\sum_{d\mid n+1,\ d\ge2}(nd)^{-s}e_d.
\]

For a cyclic word

\[
 \gamma=(n_0,n_1,\ldots,n_{\ell-1}),
 \qquad n_\ell=n_0,
\]

the edge product telescopes only in the sense of endpoint multiplicity:

\[
 \prod_{j=0}^{\ell-1}(n_jn_{j+1})^{-s}
 =\prod_{j=0}^{\ell-1}n_j^{-2s}
 =N(\gamma)^{-2s},
\]

where \(N(\gamma)=\prod_jn_j\).  Every cyclic vertex occurs once as a source
and once as a target.  The exponent two is therefore forced by the frozen
roof.

## 3. Recurrence mechanism

Two special quotients already determine the large-scale dynamics:

\[
 q=1:quad n\to n+1,
\]

\[
 q=2:quad 2k-1\to k.
\]

The first moves monotonically upward; the second folds every odd vertex back
toward the origin.  Combining them yields descent to \(2\), ascent from
\(2\), and the canonical closure

\[
 k\to k+1\to\cdots\to2k-1\to k.
\]

Thus the same local grammar produces both recurrence and the nonselective
cycle flood.

## 4. Derivation of finite confinement

Consider a length-\(r\) closed walk and rotate it so that its first vertex is
a maximum \(M\).  Write the first transition as \(M\to d\).  The successor
choice \(d=M+1\) cannot occur at a maximum.  Hence \(d\) is a proper divisor
of \(M+1\), giving

\[
 d\le\frac{M+1}{2}.
\]

Every later edge \(x\to y\) satisfies \(y\le x+1\).  After the first drop,
only \(r-1\) edges remain, so

\[
 M\le d+(r-1).
\]

Substitution gives

\[
 M\le\frac{M+1}{2}+r-1,
\]

and hence

\[
 M\le2r-1.
\]

The equality conditions are simultaneous:

\[
 d=\frac{M+1}{2}=r,
 \qquad
 y=x+1\ \text{on every remaining edge}.
\]

Therefore the unique extremal class is

\[
 2r-1\to r\to r+1\to\cdots\to2r-1.
\]

This inequality is the bridge from a countably infinite graph to exact
finite-order traces.

## 5. Row-nuclear derivation

Fix a target row \(d\\).  The edge condition is equivalent to

\[
 n=kd-1,qquad k\ge1,qquad kd-1\ge2.
\]

Thus row \(d\) is the rank-one operator

\[
 R_{d,s}x
 =\left(
   \sum_{\substack{k\ge1\\kd-1\ge2}}
   [d(kd-1)]^{-s}x_{kd-1}
  \right)e_d.
\]

A rank-one functional-to-vector map has nuclear norm equal to the
\(\ell^2\)-norm of its coefficient vector:

\[
 \|R_{d,s}\|_1^2
 =\sum_{\substack{k\ge1\\kd-1\ge2}}
  [d(kd-1)]^{-2\sigma}.
\]

Because \(kd-1\ge kd/2\),

\[
 [d(kd-1)]^{-2\sigma}
 \le2^{2\sigma}k^{-2\sigma}d^{-4\sigma},
\]

and therefore

\[
 \|R_{d,s}\|_1
 \le2^\sigma\zeta(2\sigma)^{1/2}d^{-2\sigma}.
\]

The outer row sum has exactly the threshold

\[
 \sum_{d\ge2}d^{-2\sigma}<\infty
 \quad\Longleftrightarrow\quad
 \sigma>\frac12.
\]

This proves sufficiency.  An entrywise \(\ell^1\) estimate would sum over
both \(d\) and \(k\) without taking the row \(\ell^2\)-norm and would obscure
the sharp range.

## 6. Fourier-diagonal necessity

Diagonal modulation by \(U_t e_n=e^{int}e_n\) transforms a matrix entry by

\[
 (U_tL_sU_t^*)_{d,n}=e^{i(d-n)t}(L_s)_{d,n}.
\]

The first Fourier coefficient

\[
 \mathcal E_1(L_s)
 =\frac1{2\pi}\int_0^{2\pi}
 e^{-it}U_tL_sU_t^*\,dt
\]

retains exactly \(d-n=1\).  These entries are precisely the successor edges:

\[
 \mathcal E_1(L_s)e_n=[n(n+1)]^{-s}e_{n+1}.
\]

If \(L_s\) were trace class, the Bochner integral would be trace class and
contractive in trace norm.  For a unilateral weighted shift, the singular
values are the moduli of the weights.  Therefore a necessary condition is

\[
 \sum_{n\ge2}[n(n+1)]^{-\sigma}<\infty,
\]

which is equivalent to \(2\sigma>1\).  This closes the gap left by the row
upper bound and proves the if-and-only-if statement.

## 7. Trace-to-determinant derivation

In the trace-class half-plane, Fredholm theory gives

\[
 \log\det(I-zL_s)
 =-\sum_{r\ge1}\frac{z^r}{r}\operatorname{Tr}L_s^r
\]

for \(z\) near zero.  The order-\(r\) trace is

\[
 \operatorname{Tr}L_s^r
 =\sum_{\substack{n_0\to n_1\to\cdots\to n_{r-1}\to n_0}}
  \prod_{j=0}^{r-1}(n_jn_{j+1})^{-s}.
\]

Finite confinement makes this a finite sum, supported on
\(2\le n_j\le2r-1\).  If a primitive orbit \(\gamma\) of length \(d\mid r\)
is repeated \(r/d\) times, its contribution has weight

\[
 \left(N(\gamma)^{-2s}\right)^{r/d}
\]

and \(d\) rooted representatives.  Hence

\[
 \operatorname{Tr}L_s^r
 =\sum_{d\mid r}d
  \sum_{\substack{[\gamma]\ \mathrm{primitive}\\\ell(\gamma)=d}}
  N(\gamma)^{-2s r/d}.
\]

Substitution into the logarithmic determinant and use of
\(-\log(1-x)=\sum_{m\ge1}x^m/m\) yields

\[
 \det(I-zL_s)
 =\prod_{[\gamma]\ \mathrm{primitive}}
  \left(1-z^{\ell(\gamma)}N(\gamma)^{-2s}\right)
\]

locally in \(z\).  The whole Fredholm determinant is primary; the local
primitive product is a derived representation.

## 8. First exact orders

The absence of loops gives

\[
 t_1(s):=\operatorname{Tr}L_s=0.
\]

The unique primitive length-two class \(C_2=(2,3)\) gives

\[
 t_2(s)=2(2\cdot3)^{-2s}=2\,6^{-2s}.
\]

The unique primitive length-three class \(C_3=(3,4,5)\) gives

\[
 t_3(s)=3(3\cdot4\cdot5)^{-2s}=3\,60^{-2s}.
\]

At length four, the double traversal of \(C_2\) and the primitive classes

\[
 (2,3,4,5),
 \qquad
 (4,5,6,7)
\]

give

\[
 t_4(s)=2\,6^{-4s}+4\,120^{-2s}+4\,840^{-2s}.
\]

Writing

\[
 D_{\rm SD}(s,z)=\sum_{m\ge0}a_m(s)z^m,
 \qquad a_0=1,
\]

the Newton recurrence is

\[
 ma_m(s)=-\sum_{r=1}^m t_r(s)a_{m-r}(s).
\]

Thus

\[
 a_1=0,
 \qquad
 a_2=-6^{-2s},
 \qquad
 a_3=-60^{-2s},
\]

\[
 a_4=-120^{-2s}-840^{-2s}.
\]

The repeated \(C_2\) term cancels from \(a_4\), exactly as multiplication of
the primitive factors predicts.  At \(s=1\),

\[
 a_0,a_1,a_2,a_3,a_4
 =1,0,-\frac1{36},-\frac1{3600},-\frac1{14112}.
\]

## 9. Marked target comparison

The source determinant begins

\[
 D_{\rm SD}(s,z)=1+0\,z+O(z^2).
\]

The marked prime Euler determinant begins, for \(\sigma>1\),

\[
 D_{\mathbb P}(s,z)
 =\prod_p(1-zp^{-s})
 =1-z\sum_pp^{-s}+O(z^2).
\]

For real \(s>1\), the prime sum is strictly positive.  The mismatch is
therefore coefficientwise, absolute, and independent of target-zero data.
It is stronger for ledger comparison than a numerical test at \(z=1\).

## 10. Quotient filters and the minimal successor obligation

For an edge \(n\to d\), restore its unique quotient label

\[
 q=(n+1)/d.
\]

The inventory \(Q=\{1,2\}\) keeps both

\[
 n\to n+1
 \quad\text{and}\quad
 2d-1\to d,
\]

so it retains every \(C_d\).  More generally, \(Q=\{1,q\}\) retains

\[
 C_{d,q}=(d,d+1,\ldots,qd-1),
 \qquad
 \ell(C_{d,q})=d(q-1).
\]

Thus no memoryless positive quotient inventory containing the successor and
one return quotient can restore prime selectivity.  Paper22 must either prove
a finite-state symbolic no-go or demonstrate signed/character cancellation
coefficientwise in the whole determinant, with all blocks reported.

## 11. Analytic and route boundary

The derivation proves only the same-object domain

\[
 \operatorname{Re}s>\frac12.
\]

It supplies no continuation to the boundary, no functional equation, no
Gamma completion, no Riemann–von Mangoldt counting law, and no Weil/Hermitian
compression.  Therefore own-object analyticity earns A2 but not A3.  The
frozen verdict remains

\[
(\mathrm{A0\_STRUCTURAL\_ARITHMETIC\_RELATION},
 \mathrm{A1\_WEAK},
 \mathrm{A2\_ANALYTIC\_DETERMINANT},
 \mathrm{A3\_FAIL},
 \mathrm{A4\_FAIL}),
 \qquad
 \mathrm{ROUTE\_A\_REJECTED}.
\]
## 12. Authority exact-certificate integration

The authority implementation instantiates the preceding finite identities without changing the graph, roof, orientation, or primitive-cycle convention. Sparse exact propagation certifies all rooted traces through order $32$ at the theorem cutoff $2r-1$, and all four finite-cutoff flags at $N=7,15,31,63$ agree with that certificate. Exact rational propagation covers $s=1,2,3$ through order $16$.

The explicit directed-rotation inventory contains $667$ primitive classes through length $16$. Newton recurrence and the independent primitive-product construction agree on all $51$ coefficient rows through degree $16$. The source firewall audits $30{,}626$ edges through source $4096$, with zero quotient-identity mismatches and no loops.

The implementation suite has $19$ declared tests, all passing. The final orchestration regenerates all results twice under fixed hash and bytecode settings, applies the strict Route-A and source-policy integrity gates, and requires the SHA-256 result ledger to be byte-identical. These computations are finite certificates for the analytic derivation, not replacements for the confinement, sharp $\mathcal S_1$, or cycle-flood proofs.
