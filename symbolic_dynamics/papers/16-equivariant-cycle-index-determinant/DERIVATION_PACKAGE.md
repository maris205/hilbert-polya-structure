# DERIVATION PACKAGE — SD-C18

## 1. From the subset alphabet to two incompatible trace ledgers

For a finite atom set \(P\), the signed subset inventory is

\[
 b_P(x)=\sum_{\varnothing\ne S\subseteq P}
          (-1)^{|S|+1}x_S
        =1-\prod_{p\in P}(1-x_p).
\]

On the edge-state space \(V_P=\mathbb C[E(P)]\), the canonical full-shift
transfer is rank one:

\[
 A_x=u_P\otimes\ell_x,
 \qquad u_P=\sum_Se_S,
 \qquad \ell_x(e_S)=(-1)^{|S|+1}x_S.
\]

The relation \(A_x^2=b_P(x)A_x\) gives

\[
 \operatorname{tr}A_x^r=b_P(x)^r,
 \qquad
 \det(I-zA_x)=1-zb_P(x).
\]

At \(z=1\), this recovers the pure atom product.  This is the scalar shadow.

The canonical operator that instead keeps every subset line is diagonal:

\[
 D_xe_S=x_Se_S.
\]

With the subset sign used as a grading readout,

\[
 \operatorname{str}D_x^r
 =\sum_{S\ne\varnothing}(-1)^{|S|+1}x_S^r
 =b_P(x_1^r,\ldots,x_n^r).
\]

Thus the two ghost sequences are

\[
 \boxed{b_P(x)^r}
 \qquad\text{and}\qquad
 \boxed{b_P(x^r)}.
\]

They belong to different operators.  A resolved determinant cannot borrow
the first sequence while using the second operator.

## 2. Exact coefficient witness

Let \(n\ge2\), \(r\ge2\).  Every factor in \(b_P(x)^r\) has total degree at
least one.  To obtain the degree-\(r\) monomial \(x_1^{r-1}x_2\), every factor
must contribute a singleton.  There are \(r\) choices for the factor that
contributes \(x_2\), so

\[
 [x_1^{r-1}x_2]b_P(x)^r=r.
\]

Every exponent in \(b_P(x^r)\) is divisible by \(r\), hence

\[
 [x_1^{r-1}x_2]b_P(x^r)=0.
\]

The mismatch is formal.  It does not depend on primes, numerical precision,
or a cutoff.

## 3. Primitive squarefree words as cyclic set partitions

At content \(x_1\cdots x_n\), edge subsets are disjoint and cover the label
set.  A cyclic word is therefore a cyclically ordered set partition.  With
\(m\) blocks, the number of such words is

\[
 N_{n,m}=(m-1)!S(n,m),
\]

and the sign is

\[
 (-1)^{\sum_j(|S_j|+1)}=(-1)^{n+m}.
\]

Every squarefree word is primitive.  The total counts are

| \(n\) | total | positive | negative | scalar difference |
|---:|---:|---:|---:|---:|
| 2 | 2 | 1 | 1 | 0 |
| 3 | 6 | 3 | 3 | 0 |
| 4 | 26 | 13 | 13 | 0 |
| 5 | 150 | 75 | 75 | 0 |
| 6 | 1,082 | 541 | 541 | 0 |
| 7 | 9,366 | 4,683 | 4,683 | 0 |

The scalar difference vanishes because

\[
 -\log\prod_i(1-x_i)=\sum_i-\log(1-x_i)
\]

contains no squarefree mixed monomial for \(n\ge2\).  Dimension zero does
not imply equivariant cancellation.

## 4. The first residual before dimension

For \(P=\{p,q,r\}\), separate the six cyclic partitions by sign:

\[
 C_+=\{[pqr],[p][q][r],[p][r][q]\},
\]

\[
 C_-=\{[p][qr],[q][pr],[r][pq]\}.
\]

The orbit decompositions are

\[
 [C_+]=[S_3/S_3]+[S_3/C_3],
 \qquad
 [C_-]=[S_3/C_2].
\]

Therefore

\[
 \mathcal R_3=[C_+]-[C_-]
 =[S_3/S_3]+[S_3/C_3]-[S_3/C_2].
\]

The fixed-point table is

| subgroup | \(C_+\) fixed | \(C_-\) fixed | residual mark |
|---|---:|---:|---:|
| \(1\) | 3 | 3 | 0 |
| \(C_2\) | 1 | 1 | 0 |
| \(C_3\) | 3 | 0 | 3 |
| \(S_3\) | 1 | 0 | 1 |

Linearization uses

\[
 \mathbb C[S_3/C_3]=\mathbf1\oplus\mathbf{sgn},
 \qquad
 \mathbb C[S_3/C_2]=\mathbf1\oplus\mathbf{Std},
\]

so

\[
 R_3=\mathbf1\oplus\mathbf{sgn}-\mathbf{Std},
 \qquad \chi_{R_3}=(0,0,3).
\]

The nontrivial value occurs at a three-cycle, exactly where scalar dimension
has no resolution.

## 5. Power-compatible sign carrier

A negative scalar edge contributes \((-w)^r\) at repetition \(r\).  In an
ordinary representation \(\lambda\)-ring, applying Adams operations to the
integer coefficient \(-1\) leaves \(-1\); it does not produce \((-1)^r\).

Introduce the nontrivial \(C_2\) line \(\tau\).  At its nontrivial element
\(c\),

\[
 \tau(c)=-1,
 \qquad
 \psi^r(\tau)(c)=\tau(c^r)=(-1)^r.
\]

Coloring an edge \(S\) by \(\tau^{|S|+1}\) therefore reproduces the exact
scalar repetition sign.  This carrier repairs the formal power bookkeeping;
it does not create a commuting arithmetic symmetry.

The multidegree action is

\[
 \psi^r(x^\alpha)=x^{r\alpha}.
\]

For \(r>1\), no integral \(\alpha\) satisfies
\(r\alpha=(1,1,1)\).  Hence no higher-power term removes \(R_3\).

## 6. Semilinear family versus fixed arithmetic operator

Let \(\rho(g)e_S=e_{gS}\).  Since \(u_P\) is invariant,

\[
 \rho(g)A_x\rho(g)^{-1}=A_{g\cdot x}.
\]

This equation means that relabeling moves one weighted operator to another.
It is not a commuting action on one fiber.  Commutation holds precisely when

\[
 x_{gp}=x_p\quad\text{for every }p.
\]

At \(x_p=p^{-s}\), \(\operatorname{Re}s>0\), the moduli \(p^{-\operatorname{Re}s}\)
are distinct, so the stabilizer is trivial.

If weights are equalized to \(t\), the group action commutes with \(A_t\),
but

\[
 \operatorname{im}A_t=\mathbb Cu_P.
\]

Only the trivial isotype survives.  Every nontrivial character determinant is
one.  Equalization trades arithmetic label information for symmetry and then
removes the desired resolved motion.

## 7. Diagonal superdeterminant and mixed factors

The standard trace-log of the diagonal lift gives

\[
 \operatorname{sdet}(I-D_x)
 =\exp\left(-\sum_{r\ge1}\frac1r b_P(x^r)\right)
 =\prod_{S\ne\varnothing}(1-x_S)^{(-1)^{|S|+1}}.
\]

For \(n=2\),

\[
 \operatorname{sdet}(I-D_x)
 =\frac{(1-x_1)(1-x_2)}{1-x_1x_2}.
\]

At \((x_1,x_2)=(1/4,1/9)\),

\[
 \prod_i(1-x_i)=\frac23,
 \qquad
 \operatorname{sdet}(I-D_x)=\frac{24}{35}.
\]

The quotient is \(36/35\).  Regularization is not needed to see the
mismatch; the extra mixed denominator is already finite and exact.

## 8. Character-readout triangle

The three desired properties are:

\[
 \begin{array}{c}
 \text{pure Euler trace-log}\\
 \text{fixed arithmetic character fiber}\\
 \text{nontrivial resolved recurrent motion.}
 \end{array}
\]

Each canonical branch loses one:

- augmentation/dimension preserves the Euler ledger but kills \(R_3\);
- a nontrivial character/mark readout sees \(R_3\) but inserts a mixed
  \(x_px_qx_r\) primitive coefficient;
- arithmetic specialization preserves distinct roof weights but destroys the
  commuting \(S_P\) symmetry;
- equal weights restore symmetry but leave only the trivial rank-one image;
- the diagonal analytic lift keeps subset lines but changes the ghost sequence
  and determinant.

This is the SD-C18 incompatibility triangle.  It is a theorem for the frozen
canonical realizations, not a universal theorem about all group extensions.

## 9. Projective formal limit and raw operator limit

For \(P\subset Q\), zero-specialization gives

\[
 b_Q(x_P,x_{Q\setminus P}=0)=b_P(x_P).
\]

The same deletion acts on the multigraded cycle index, so formal finite-label
objects form a projective family.

Let \(i_{P,Q}e_S=e_S\) be the natural Hilbert-space embedding.  Then

\[
 A_Qi_{P,Q}e_T=\epsilon(T)x_Tu_Q,
 \qquad
 i_{P,Q}A_Pe_T=\epsilon(T)x_Ti_{P,Q}u_P.
\]

The maps do not intertwine.  In addition,

\[
 \|A_P\|
 =\sqrt{2^{|P|}-1}
  \left(\prod_{p\in P}(1+|x_p|^2)-1\right)^{1/2},
\]

which diverges along increasing prime sets.  Compatible compressions do not
produce a bounded raw-transfer inductive limit.

## 10. Schatten calculation

For the diagonal prime-subset operator,

\[
 \|D_s\|_{\mathcal S_q}^q
 =\sum_{S\ne\varnothing}\prod_{p\in S}p^{-q\sigma}
 =\prod_p(1+p^{-q\sigma})-1,
 \qquad \sigma=\operatorname{Re}s.
\]

The product is finite exactly when \(\sum_pp^{-q\sigma}\) converges, hence
exactly when

\[
 q\sigma>1.
\]

In particular, the standard Fredholm superdeterminant exists without
regularization for \(\sigma>1\), but it is the mixed-subset product of
Section 7.  Analytic existence does not repair algebraic identity.

## 11. Control interpretation

Every finite identity above depends only on the Boolean subset grammar and
formal weights.  Composite labels, shuffled weights, random rational weights,
and arbitrary free-commutative atoms reproduce the same results.  The
arithmetic specialization supplies a natural entropy scale and the prime
Dirichlet convergence threshold.  It does not supply a selective
character-resolved primitive mechanism.

The correct interpretation is therefore

```text
GO_FORMAL_EQUIVARIANT_LEDGER
STOP_CHARACTER_FREDHOLM_FIBERS
STOP_STANDARD_SUPERTRACE_INTERPRETATION
STOP_ARITHMETIC_SELECTIVITY
PROVES_TOO_MUCH
ROUTE_A_REJECTED
ROUTE_B_LOCKED
```
