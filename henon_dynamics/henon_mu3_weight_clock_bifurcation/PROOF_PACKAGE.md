# HCS-C51 proof package

## Claim

For the source-ordered Hénon moment geometry at \(n=2,3,4\):

1. the exact normalized coefficient is the sum of one pure weight-zero and
   one pure weight-one Frobenius trace;
2. the ranks of the two packets are \((4^n+5)/3\) and
   \(2(4^n-4)/3\);
3. the leading Euler logarithm is exactly the \(2/n\) multiple of a
   standard cohomological logarithm, up to a nonzero residual on
   \(\Re s>0\);
4. the leading odd centers align at zero, whereas the even centers and the
   higher denominator tower do not;
5. twisting cannot repair this factorwise mismatch;
6. a direct source-native \(K\)-compatible finite-rank realization of the
   fractional leading roots is impossible at \(n=3,4\);
7. the \(n=4\) Hodge ledger forces a rank-two extreme projector gate.

## Status

**PROVABLE AS STATED.**

The closed rank identity is conditional on smoothness of the displayed
\((2,3)\) family member.  Its application to the Hénon source is restricted
to \(n=2,3,4\), for which predecessor packages establish smoothness outside
finite bad sets.  The denominator-cleared \(n=3,4\) functional equations
are not part of the proved claim.

## Assumptions

1. \(K=\mathbf Q(\rho)\), \(\rho^2+\rho+1=0\).
2. \(p>3\) is a good split prime unless stated otherwise.
3. The phase, clock, and normalization are exactly (1)--(2) of
   THEOREM_PACKAGE.md.
4. The cubic \(S_n\) and complete intersection \(X_n\) are smooth in the
   rows where purity and the cohomological rank formula are invoked.
5. Geometric Frobenius and the convention
   \(F_p\mid\mathbf Q_\ell(-1)=p\) are used.
6. The C50 \(n=2\) modular continuation and functional equation are
   inherited; no corresponding hypothesis is silently added for \(n=3,4\).

## Notation

- \(P_m(p)=1+p+\cdots+p^m\).
- \(A_{p,n}\) is the primitive cubic deviation in \(\#S_n\).
- \(B_{p,n}\) is the middle-cohomology deviation in \(\#X_n\).
- \(E_n\) and \(O_n\) are the weight-zero and weight-one packets.
- \(j\ge1\) is the canonical denominator index in
  \(1/(p-1)=\sum_{j\ge1}p^{-j}\).
- \(\operatorname{Log}_0\) is the Euler logarithm vanishing at \(+\infty\).

## Proof strategy

The proof moves in one direction:

\[
\text{radial strata}
\Longrightarrow
\text{projective cancellation}
\Longrightarrow
\text{pure trace packets}
\Longrightarrow
\text{Euler logarithm}
\Longrightarrow
\text{center and rank obstructions}.
\]

The Hodge calculation is independent of the Euler analysis and supplies
the successor gate.

## Dependency map

| Result | Inputs | External theorem |
|---|---|---|
| projective cancellation | homogeneous cubic plus quadric | none |
| weights and square-root bounds | smooth \(S_n,X_n\) | Deligne purity |
| cubic rank | cubic Jacobian ring | Griffiths residue/Jacobian-ring description |
| intersection rank | Chern class and weak Lefschetz | SGA 2 |
| logarithmic extraction | trace identity and Euler logarithm | none beyond weights |
| center map | standard pure-weight reflection convention | motivic convention only |
| \(n=2\) factor FE | C50 elliptic decomposition | Caraiani--Newton; Godement--Jacquet |
| \(O_4\) Hodge types | \(\chi_y\) and weak Lefschetz | Hirzebruch--Riemann--Roch |

## Proof

### 1. Radial strata

For a nonzero vector \(x\), homogeneity gives

\[
 \Phi(tx)=t^2(2t\mathcal C_n(x)+\mathcal Q_{n,\rho}(x)).
\]

If both \(\mathcal C_n(x)\) and \(\mathcal Q_{n,\rho}(x)\) are nonzero,
there is one nonzero root
\(t=-\mathcal Q_{n,\rho}(x)/(2\mathcal C_n(x))\).
If exactly one of them vanishes, there is no nonzero root.  If both vanish,
all \(p-1\) nonzero scalars are roots.  Adding the origin,

\[
\begin{aligned}
Z_{p,n}
&=1+\#\!\left(\mathbf P^{2n-1}\setminus(S_n\cup Q_n)\right)
 +(p-1)\#X_n\\
&=1+P_{2n-1}-\#S_n-\#Q_n+p\#X_n.
\end{aligned}
\]

This proves the radial identity without an averaging step.

### 2. Tate cancellation

Insert

\[
 \#S_n=P_{2n-2}+A_{p,n},\quad
 \#Q_n=P_{2n-2}+p^{n-1},\quad
 \#X_n=P_{2n-3}-B_{p,n}.
\]

The polynomial identity

\[
 1+P_{2n-1}-2P_{2n-2}+pP_{2n-3}=p^{2n-1}
\]

gives

\[
 Z_{p,n}=p^{2n-1}-p^{n-1}-A_{p,n}-pB_{p,n}.
\]

Applying the normalization in (2) gives

\[
 C_{p,n}=-2-\frac{2A_{p,n}}{p^{n-1}}
              -\frac{2B_{p,n}}{p^{n-2}}.
\]

### 3. The two pure traces

Because \(S_n\) has even dimension, its primitive middle trace has positive
sign in the Lefschetz trace formula.  Because \(X_n\) has odd dimension,
its middle trace has negative sign.  Hence

\[
 A_{p,n}=\operatorname{Tr}(F_p\mid H^{2n-2}_{\mathrm{prim}}(S_n)),
\]

\[
 B_{p,n}=\operatorname{Tr}(F_p\mid H^{2n-3}(X_n)).
\]

The twists in the definitions of \(E_n\) and \(O_n\) divide these traces
by \(p^{n-1}\) and \(p^{n-2}\).  The original weights
\(2n-2\) and \(2n-3\) become \(0\) and \(1\), respectively.  Therefore

\[
 C_{p,n}=-2\left(
 \operatorname{Tr}(F_p\mid E_n)+\operatorname{Tr}(F_p\mid O_n)
 \right).
\]

Deligne purity also gives uniform bounds
\(\operatorname{Tr}(F_p\mid E_n)=O(1)\) and
\(\operatorname{Tr}(F_p\mid O_n)=O(p^{1/2})\).

### 4. The two split primes agree

Under the substitution

\[
 x_0=\rho^2y_{2n-1},\qquad x_i=y_{i-1}\quad(1\le i\le2n-1),
\]

the cubic is invariant because \((\rho^2)^3=1\).  A cyclic reindexing of
the quadric sends the coefficient on its closing edge from \(\rho\) to
\(\rho^2\).  Thus the two reductions are \(K\)-conjugate and isomorphic.
Their trace equality supplies the factor two in the split-prime
\(K\)-Euler logarithm.

### 5. Cubic rank

For a smooth cubic in \(\mathbf P^{2n-1}\), the primitive middle Hodge
groups are graded pieces of

\[
 R_n=\mathbf C[x_0,\ldots,x_{2n-1}]/(x_0^2,\ldots,x_{2n-1}^2).
\]

Its Hilbert series is \((1+t)^{2n}\).  Summing the relevant primitive
pieces, equivalently evaluating the standard cubic primitive Betti
formula, gives

\[
 b^{\mathrm{prim}}_{2n-2}(S_n)=\frac{4^n+2}{3}.
\]

The expression is integral because \(4^n\equiv1\pmod3\).

### 6. Complete-intersection rank

The normal sequence for \(X_n=(2,3)\subset\mathbf P^{2n-1}\) gives

\[
 c(TX_n)=\frac{(1+H)^{2n}}{(1+2H)(1+3H)}.
\]

Since \([X_n]=6H^2\), Gauss--Bonnet gives

\[
 \chi(X_n)=6[H^{2n-3}]
 \frac{(1+H)^{2n}}{(1+2H)(1+3H)}.
\]

The partial fraction

\[
 \frac1{(1+2H)(1+3H)}
 =-\frac2{1+2H}+\frac3{1+3H}
\]

reduces the coefficient to two finite binomial sums; evaluating them yields

\[
 [H^{2n-3}]
 \frac{(1+H)^{2n}}{(1+2H)(1+3H)}
 =\frac{3n+1-4^n}{9}.
\]

Thus

\[
 \chi(X_n)=\frac{2(3n+1-4^n)}{3}.
\]

Weak Lefschetz identifies all nonmiddle cohomology with projective-space
cohomology.  There are \(2n-2\) even Tate dimensions, while the middle
degree \(2n-3\) is odd.  Therefore

\[
 b_{2n-3}(X_n)
 =(2n-2)-\chi(X_n)=\frac{2(4^n-4)}{3}.
\]

Adding the trivial line in \(E_n\) proves
\(\operatorname{rank}(E_n\oplus O_n)=4^n-1\).

### 7. Logarithmic extraction and residual

Let \(\ell_n^{(S)}\) be the logarithmic sum over good split primes
\(p\notin S\).  The field-degree normalization gives

\[
 c_{p,n}=-\frac{4(e_{p,n}+o_{p,n})}{p-1}.
\]

Hence

\[
 -\frac{\ell_n^{(S)}(s)}n
 =\frac4n\sum_{\substack{p\equiv1(3)\\p\notin S}}
 (e_{p,n}+o_{p,n})\sum_{j\ge1}p^{-ns-j}.
\]

For the two degree-one primes above a split \(p\), the degree-one term of

\[
 \frac2n\operatorname{Log}L_K^{(S)}(E_n\oplus O_n,ns+1)
\]

is exactly

\[
 \frac4n(e_{p,n}+o_{p,n})p^{-ns-1}.
\]

This cancels the \(j=1\) term.  For \(j\ge2\), the remaining odd trace is
bounded by \(O(p^{-n\Re s-3/2})\).  For Euler-logarithm powers \(m\ge2\),
the worst weight-one term is
\(O(p^{-mn\Re s-m/2})\).  Inert primes outside the finite bad set \(S\)
have norm \(p^2\) and satisfy the same boundary.  These prime sums converge
normally for \(\Re s>0\).
Their difference is therefore holomorphic there, and its exponential
\(H_{n,S}\) is nonzero for the good-prime sum.  The difference
\[
 -\frac{\ell_n(s)-\ell_n^{(S)}(s)}n
 =-\frac1n\sum_{\substack{p\in S\\p\equiv1(3)}}c_{p,n}p^{-ns}
\]
is a finite entire Dirichlet polynomial.  Its exponential is nonzero and
is included in \(H_{n,S}\).  This proves (15) for the full source sum.

The original series has worst term
\(O(p^{-n\Re s-1/2})\), proving its stated initial domain
\(\Re s>1/(2n)\).

### 8. Center map

For a pure weight-\(w\) completion, the standard reflection is
\(u\mapsto w+1-u\).  Under the forced substitution \(u=ns+j\), the
reflected \(s\)-variable is

\[
 s'=\frac{w+1-2j}{n}-s.
\]

Its center is

\[
 s_{n,j}(w)=\frac{(w+1)/2-j}{n}.
\]

At \(w=1,j=1\), all three rows have center zero.  At \(w=0,j=1\), the
centers are \(-1/4,-1/6,-1/8\).  For \(w=1,j\ge2\), they are
\(-(j-1)/n\).  Therefore no common factorwise standard pure-motive center
exists for the full source tower.

### 9. Twist invariance

A Tate twist \(k\) sends the weight to \(w-2k\).  To preserve the same
source term, it sends the intercept to \(j-k\).  Substitution gives

\[
 s_{n,j-k}(w-2k)
 =\frac{(w-2k+1)/2-(j-k)}n
 =s_{n,j}(w).
\]

This proves invariance for integral \(k\) and, formally, for half-integral
\(k\).  A fixed-clock half twist changes the local coefficients, so it is
outside the source lock.

### 10. Direct compatible-system no-go

A semisimple direct finite-rank system \(W_n\) producing a factorwise
\(2/n\) power with the same trace would satisfy
\[
 n\Tr(F_{\mathfrak p}\mid W_n)
 =2\Tr(F_{\mathfrak p}\mid E_n\oplus O_n)
\]
at all good degree-one primes.  Such primes have density one in \(K\).
Chebotarev density and Brauer--Nesbitt therefore give
\[
 n[W_n]=2[E_n\oplus O_n]
\]
in the semisimple representation ring.  Since the two source summands have
different pure weights, the identity separates weightwise.  Hence the
dimensions of \(W_n\) would be \(2/n\) times the source dimensions.  At
\(n=3\), they would be \(46/3\) and \(80/3\).  At
\(n=4\), their sum would be \(255/2\).  Since compatible-system ranks are
integers, the direct source-native \(K\)-packet is impossible.

This argument does not survive unchanged under every change of category.
Restriction of scalars doubles ranks and removes the numerical \(n=4\)
parity failure, although it changes prime organization.  It leaves
\(92/3\) and \(160/3\) at \(n=3\).  Galois counterpackets and
normalized-semifinite determinants are not classified by this proof.

### 11. Odd denominator clearing

The leading odd factor exponents are \(1,2/3,1/2\).  Multiplication by the
least common denominator \(6\) gives exponents \(6,4,3\).  Each standard
weight-one reflection under \(u=ns+1\) becomes \(s\mapsto-s\).
Therefore the product in (23) has that reflection if the three completed
factors exist.  Only the \(n=2\) existence and functional equation are
proved here; the rest is a formal expected skeleton.

### 12. The \(n=4\) Hodge gate

Hirzebruch--Riemann--Roch applied to
\((2,3)\subset\mathbf P^7\) gives the coefficient formula (26).
Expanding through degree five gives
\(\chi_y=1-82y^2+82y^3-y^5\).  Weak Lefschetz leaves only
\(h^{4,1}=a\) and \(h^{3,2}=b\) unknown in the middle row, and writes

\[
 \chi_y=1+(a-1)y+(1-b)y^2+(b-1)y^3+(1-a)y^4-y^5.
\]

Coefficient comparison gives \(a=1,b=83\).  After twist by \(2\), the
extreme types \((2,-1)\) and \((-1,2)\) show that \(O_4\) is not itself
an abelian \(H^1\).  Hodge theory alone does not produce an algebraic
projector, so the C52 gate has exactly the stated strength.

## Corrections or missing assumptions

- The family rank formula requires smooth \(X_n\); no source smoothness is
  asserted beyond \(n=4\).
- Standard functional equations for \(O_3,O_4\) are expected, not proved.
- Fractional powers use \(\operatorname{Log}_0\) only in the nonvanishing
  Euler domain.
- The compatible-system obstruction is direct, over \(K\), factorwise, and
  trace-preserving.  It is not a universal categorical no-go.

## Open risks

1. The \(O_4\) Hodge decomposition may fail to be algebraic over \(K\).
2. Even if a projector exists, its factors may not be automorphic or may not
   interact with the residual \(H_{n,S}\).
3. The complete denominator tower still has separated centers.
4. No mechanism here continues the full Hénon object through
   \(\Re s=1/5\).
5. No self-adjoint global generator or Riemann divisor is constructed.
