# Derivation package — Paper 31 / SD-C33

## 1. Derivation map

The calculation has four layers that must remain distinct:

1. **source layer:** alphabet sum/product reconstruct \(\mathbb N_0\) and
   define successor and congruence;
2. **orbit layer:** the Wilson recurrence closes one graph cycle for every
   prime and no composite;
3. **formal analytic layer:** finite power-diagonal sums exponentiate to a
   marked primitive product;
4. **operator layer:** the whole recurrent adjacency is noncompact, whereas
   first return and transient pruning produce different trace-class objects.

Moving from one layer to the next requires an explicit theorem.  Equality at
\(z=1\) is not permission to erase graph time.

## 2. Source arithmetic

### 2.1 Alphabet operations

Cardinality gives
\[
  |A_m\sqcup A_n|=m+n,
  \qquad
  |A_m\times A_n|=mn.
\]
The full-shift functor therefore produces
\[
  [F_m]\boxplus[F_n]=[F_{m+n}],
  \qquad
  [F_m]\boxtimes[F_n]=[F_{mn}].
\]
Distributivity is source-visible:
\[
  F_a\boxtimes(F_b\boxplus F_c)
  \cong(F_a\boxtimes F_b)\boxplus(F_a\boxtimes F_c).
\]
Repeated alphabet sum of \(F_1\) reaches every \(F_n\).  Entropy separates
positive indices, so the skeleton is the initial characteristic-zero
commutative semiring \(\mathbb N_0\).

### 2.2 Why the bare monomial clone fails

Paper 30's multiplicative transport records only prime-exponent vectors:
\[
  \Phi(mn)=\Phi(m)\Phi(n).
\]
Ordinary polynomial addition is not compatible with integer addition.  The
smallest witness already occurs at the unit:
\[
  \Phi(1+1)=\Phi(2)=x_2,
  \qquad
  \Phi(1)+\Phi(1)=2.
\]
No divisibility, prime, or zero table is needed to witness this failure.

### 2.3 Why a matched clone cannot fail

Define addition and multiplication on formal labels by transport:
\[
  y_m\oplus_Yy_n=y_{m+n},
  \qquad
  y_m\otimes_Yy_n=y_{mn}.
\]
The map \(F_n\mapsto y_n\) then commutes with every source operation.  The
remainder recurrence also commutes:
\[
  y_{r_{n,k+1}}
  =y_{,r_{n,k}(k+1)\bmod n}.
\]
Therefore the matched clone must reproduce the full residue word and terminal
edge.  Its success is a naturality requirement, not a positive-control
failure.

## 3. Wilson recurrence and orbit weights

### 3.1 Local residue dynamics

Starting from \(r_{n,1}=1\), induction gives
\[
  r_{n,k}=k!\bmod n.
\]
Indeed, if \(r_{n,k}\equiv k!\pmod n\), then
\[
  r_{n,k+1}\equiv r_{n,k}(k+1)
  \equiv(k+1)!\pmod n.
\]
The terminal relation is consequently
\[
  r_{n,n-1}=n-1
  \quad\Longleftrightarrow\quad
  (n-1)!\equiv-1\pmod n.
\]
Wilson's theorem turns this exact source relation into the prime-cycle
census.

### 3.2 Graph length versus roof time

The \(p\)-cycle contains \(p-1\) graph edges, so
\[
  \ell(p)=p-1.
\]
The exact source clock is imposed only on the full return:
\[
  T_p=\sum_{e\in\Gamma_p}\tau(e)=h(F_p)=\log p.
\]
Hence a complete traversal has weight
\[
  \prod_{e\in\Gamma_p}e^{-s\tau(e)}
  =e^{-sT_p}=p^{-s}.
\]
Repeating the cycle \(m\) times gives \(p^{-ms}\), while the graph-step
marker records \(z^{m(p-1)}\).

## 4. Power-diagonal ledger

Fix the uniform allocation.  On the \(p\)-block,
\[
  L_{s,p}=p^{-s/(p-1)}P_{p-1},
\]
where \(P_{p-1}\) is the cyclic permutation matrix.  Since
\[
  P_{p-1}^r
  \text{ has nonzero diagonal }
  \Longleftrightarrow p-1\mid r,
\]
one obtains
\[
  \sum_{v\in\Gamma_p}
  \langle L_s^r\delta_v,\delta_v\rangle
  =\begin{cases}
  (p-1)p^{-sr/(p-1)},&p-1\mid r,\\
  0,&p-1\nmid r.
  \end{cases}
\]
Summing over primes yields
\[
  \operatorname{Tr}_{\mathrm{per}}(L_s^r)
  =\sum_{p-1\mid r}(p-1)p^{-sr/(p-1)}.
\]
The index set is finite because \(p-1\mid r\) forces \(p\leq r+1\).

## 5. Trace-log rearrangement and continuation

For \(\Re s\geq0\) and \(|z|<1\), begin with the absolutely convergent
periodic exponent
\[
  -\sum_{r\geq1}\frac{z^r}{r}
  \operatorname{Tr}_{\mathrm{per}}(L_s^r).
\]
For a fixed prime substitute \(r=m(p-1)\):
\[
  -\sum_{m\geq1}
  \frac{z^{m(p-1)}}{m(p-1)}
  (p-1)p^{-sm}
  =-\sum_{m\geq1}\frac{(z^{p-1}p^{-s})^m}{m}.
\]
Here \(|z^{p-1}p^{-s}|<1\), so using
\(-\sum_{m\geq1}u^m/m=\log(1-u)\) gives
\[
  D_W(s,z)=\prod_p(1-z^{p-1}p^{-s}).
\]

For \(|z|\leq\rho<1\) and \(\Re s\geq-M\),
\[
  |z|^{p-1}|p^{-s}|\leq\rho^{p-1}p^M.
\]
The majorant is summable, so the product converges normally on compact subsets
of \(\{|z|<1\}\times\mathbb C\) and continues the initial trace-log identity
to all \(s\).  The trace-log series itself is not asserted to converge for
arbitrarily negative \(\Re s\) at a fixed nonzero \(z\).  At \(z=1\),
ordinary Euler-product convergence requires \(\Re s>1\), and
\[
  D_W(s,1)=\zeta(s)^{-1}.
\]

The formal derivation uses finite periodic diagonal sums.  It does not imply
that \(L_s\) is trace class.

## 6. Exact-clock noncompactness

Let \(\sigma=\Re s>0\).  On a cycle of length \(p-1\), some edge has roof at
most the average:
\[
  \tau_{p,\min}\leq\frac{\log p}{p-1}.
\]
Its modulus is therefore bounded below by
\[
  e^{-\sigma\tau_{p,\min}}
  \geq p^{-\sigma/(p-1)}
  =\exp\left(-\sigma\frac{\log p}{p-1}\right)
  \longrightarrow1.
\]
These large edge weights occur between mutually orthogonal prime blocks.  No
finite-rank tail can remove them, so the essential norm is at least one and
the operator is noncompact.  Noncompactness rules out every finite Schatten
class and the ordinary trace-class Fredholm determinant.

For a general disjoint-cycle successor with length \(\ell(p)\), compactness
can be achieved by some nonnegative allocation exactly when
\[
  \frac{\log p}{\ell(p)}\longrightarrow\infty.
\]
Thus \(\ell(p)=o(\log p)\) is necessary and sufficient within that
architecture.  The Wilson length \(p-1\) lies far outside the compact regime.

## 7. Uniform spectrum

The eigenvalues of the uniform \(p\)-block are
\[
  \lambda_{p,j}=p^{-s/(p-1)}
  \exp\left(\frac{2\pi i j}{p-1}\right),
  \qquad0\leq j<p-1.
\]
Their radii converge to one and their arguments become dense modulo
\(2\pi\).  Choosing one normalized block eigenvector for each approximating
eigenvalue yields an orthonormal Weyl sequence.  Every point on the unit
circle therefore belongs to the essential approximate spectrum.  This is an
operator obstruction, not a Hilbert--Pólya spectrum.

## 8. First-return marker calculation

Induce on a base vertex \(b_p\in\Gamma_p\).  One return has weight
\[
  R_s(b_p,b_p)=\prod_{e\in\Gamma_p}e^{-s\tau(e)}=p^{-s}.
\]
Therefore
\[
  R_s=\operatorname{diag}_{p}(p^{-s}),
  \qquad
  \|R_s\|_{\mathcal S_1}=\sum_p p^{-\sigma}.
\]
The sum is finite exactly for \(\sigma>1\), and then
\[
  \det(I-zR_s)=\prod_p(1-zp^{-s}).
\]
The raw graph counts one traversal with \(p-1\) powers of \(z\), while the
induced graph counts the same traversal as one step.  Hence
\[
  D_W(s,z)\neq\det(I-zR_s)
\]
for generic \(z\).  Their equality at \(z=1\) forgets precisely the time
coordinate needed to distinguish the objects.

The exact cutoff-31 marker certificate at \(s=2\) gives the same rational
value at \(z=1\),
\[
  \frac{50722704772300800}{82920037520482019},
\]
but different values at \(z=1/3\):
\[
\begin{aligned}
 D_{W,31}(2,1/3)
 &=\frac{
 8457837536472886874908553785029164444770443956471271591972253937028145610752000}
 {9346944729756920656475158002219939531057388454052393153175266779072600363088951},\\
 \det(I-\tfrac13R_{2,31})
 &=\frac{3249654489118510789888}{3787604851842157567725}.
\end{aligned}
\]

## 9. Transient factorization

Let \(Q_s\) be the trace-class direct sum of acyclic verifier blocks, let
\(D_s=\operatorname{diag}_p(p^{-s})\) be the accept-loop block, and let
\(B_s\) contain the summable feed edges.  With the accepted space ordered
before the transient space,
\[
  T_s=
  \begin{pmatrix}
    D_s&B_s\\
    0&Q_s
  \end{pmatrix}.
\]
Although the countable operator \(Q_s\) need not be nilpotent, every finite
verifier block is nilpotent and the global graph is acyclic.  Consequently
\[
  \operatorname{Tr}(Q_s^r)=0
  \quad(r\geq1),
  \qquad
  \det(I-zQ_s)=1.
\]
Block triangularity gives
\[
  \det(I-zT_s)=\det(I-zD_s)
  =\prod_p(1-zp^{-s}).
\]
The entire verification computation is determinant-invisible.

## 10. Exact ownership table

| Object | Periodic marker | Analytic status | Ownership verdict |
|---|---|---|---|
| recurrent Wilson adjacency \(L_s\) | \(z^{p-1}\) | bounded for \(\Re s\geq0\), noncompact for \(\Re s>0\) | exact cycles, no ordinary Fredholm determinant |
| formal product \(D_W(s,z)\) | \(z^{p-1}\) | normal for \(|z|<1\); Euler specialization for \(z=1,\Re s>1\) | formal periodic function only |
| first-return operator \(R_s\) | \(z\) | trace class iff \(\Re s>1\) | honest determinant of a changed time object |
| transient verifier \(T_s\) | \(z\) | can be made trace class | pruning-equivalent to the accept diagonal |
| matched semiring clone | copies each marker | copies each analytic status | mandatory naturality control |

No object in this package owns a same-object functional equation, Gamma
factor, completed divisor, analytic continuation of an ordinary determinant
to the critical line, fixed self-adjoint Hilbert--Pólya carrier, or Route-B
claim.
