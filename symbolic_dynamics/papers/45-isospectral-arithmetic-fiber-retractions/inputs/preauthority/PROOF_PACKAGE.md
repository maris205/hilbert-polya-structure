# Proof package

## Main theorem: paired all-\(h\) arithmetic retractions

Let \(h\ge2\), \(s\in\mathbb C\), and \(\sigma=\Re s\). On
\(c_{00}(\mathbb N)\), set

\[
S_{h,s}e_n=n^{-s/2}e_{\tau_h(n)},\qquad
M_{h,s}e_n=n^{-s/2}e_{\omega_h(n)}
\]

with

\[
\tau_h(n)=\prod_p p^{\min(v_p(n),h-1)},\qquad
\omega_h(n)=\prod_p p^{v_p(n)\bmod h}.
\]

Then all statements in the following ledger hold.

1. \(S_{h,s}\) extends boundedly and compactly exactly for \(\sigma>0\).
   \(M_{h,s}\) extends boundedly and compactly exactly for
   \(\sigma>1/h\).
2. For \(k\ge1\) and \(0<q<\infty\),

   \[
   S_{h,s}^k\in\mathcal S_q\iff k\sigma q>2,
   \]

   \[
   M_{h,s}^k\in\mathcal S_q
   \iff\sigma>1/h\text{ and }k\sigma q>2.
   \]

3. On their common bounded domain the simple nonzero eigenvalues are
   \(m^{-s/2}\), \(m\in\mathcal F_h\). If additionally \(k\sigma>2\),

   \[
   \operatorname{Tr}(S_{h,s}^k)
   =\operatorname{Tr}(M_{h,s}^k)
   =\frac{\zeta(ks/2)}{\zeta(hks/2)}.
   \]

   Every common legal Fredholm or integer-order regularized determinant is
   consequently identical.
4. \(S_{h,s}\) is boundedly similar to a compact normal diagonal operator
   exactly for \(\sigma>1\). \(M_{h,s}\) is so similar throughout its
   bounded domain \(\sigma>1/h\).
5. The saturated projection maximum obeys the exact primorial optimizer and
   the three asymptotic regimes proved below.
6. The singular and eigenvalue sequences obey

   \[
   s_n(S_{h,s})\sim
   \left(\frac{C_{h,\sigma}}n\right)^{\sigma/2},
   \qquad
   s_n(M_{h,s})\sim
   \left(\frac{D_{h,\sigma}}n\right)^{\sigma/2},
   \]

   \[
   |\lambda_n|\sim
   \left(\frac{1/\zeta(h)}n\right)^{\sigma/2},
   \]

   with the explicit constants below and
   \(C_{h,1}=D_{h,1}=1\).
7. For \(0<q<\infty\),

   \[
   [S_{h,s}^*,S_{h,s}]\in\mathcal S_q\iff\sigma q>1,
   \]

   \[
   [M_{h,s}^*,M_{h,s}]\in\mathcal S_q
   \iff\sigma>1/h\text{ and }\sigma q>1.
   \]

## Status

PROVABLE AS STATED. A complete proof is supplied below. The status is
mathematical, not an authority or novelty decision. Later implementation
must independently verify the frozen formulas and source boundary.

## Assumptions and notation

1. \(\mathbb N=\{1,2,\ldots\}\), and \(v_p(n)\) is the ordinary prime
   exponent.
2. \(\mathcal F_h=\{m:v_p(m)<h\ \forall p\}\).
3. Schatten classes \(\mathcal S_q\) are used for all \(0<q<\infty\);
   for \(q<1\) this is the standard quasi-ideal convention.
4. Singular values are counted with multiplicity and arranged
   nonincreasingly.
5. The self-commutator convention is
   \([T^*,T]=T^*T-TT^*\).
6. An empty exponent sum is zero and an empty product is one.
7. All trace statements are ordinary operator traces and therefore require
   trace class. Regularized determinant order is a positive integer.

## Dependency map

\[
\begin{array}{c}
\text{prime-exponent fibers}\\
\downarrow\\
\text{orthogonal rank-one blocks and exact masses}\\
\downarrow\\
\text{boundedness, compactness, powers, Schatten walls}\\
\downarrow\\
\text{common eigenvalues, legal traces, determinants}
\end{array}
\]

\[
\begin{array}{c}
\text{block angles}\\
\downarrow\\
\text{Riesz norms}\longrightarrow\text{similarity iff}
\longrightarrow\text{primorial maximal order},\\
\text{block masses}\longrightarrow\text{positive Dirichlet series}
\longrightarrow\text{Tauberian Weyl law},\\
\text{block angles and masses}\longrightarrow\text{commutator ideals}.
\end{array}
\]

## Lemma 1: exact fibers

For \(m\in\mathcal F_h\), define

\[
J_h(m)=\{p:v_p(m)=h-1\}.
\]

Then

\[
\tau_h^{-1}(m)
=\left\{m\prod_{p\in J_h(m)}p^{r_p}:r_p\ge0\right\}.
\]

Indeed, if \(v_p(m)\le h-2\), the equality
\(\min(v_p(n),h-1)=v_p(m)\) forces \(v_p(n)=v_p(m)\). If
\(v_p(m)=h-1\), it forces only \(v_p(n)\ge h-1\), giving the displayed
extra exponent. No new prime can occur.

Likewise,

\[
\omega_h^{-1}(m)=\{ma^h:a\ge1\},
\]

because \(v_p(n)\equiv v_p(m)\pmod h\) with
\(0\le v_p(m)\le h-1\) is equivalent to
\(v_p(n)=v_p(m)+h\,v_p(a)\). Both maps fix every \(m\in\mathcal F_h\).
\(\square\)

## Lemma 2: orthogonal rank-one blocks

For either retraction \(f\), let

\[
\mathcal H_m^f
=\overline{\operatorname{span}}\{e_n:f(n)=m\}.
\]

The fibers partition \(\mathbb N\), so

\[
\ell^2(\mathbb N)=\bigoplus_{m\in\mathcal F_h}\mathcal H_m^f.
\]

The range of the restriction \(T_m\) is contained in
\(\mathbb Ce_m\). For finitely supported \(x\in\mathcal H_m^f\),

\[
T_mx=\left(\sum_{f(n)=m}x_n n^{-s/2}\right)e_m.
\]

Thus \(T_m\) is bounded exactly when its coefficient sequence is square
summable, and its unique nonzero singular value satisfies

\[
\rho_T(m)^2=\sum_{f(n)=m}n^{-\sigma}.
\]

Using Lemma 1 gives

\[
\rho_S(m)^2
=m^{-\sigma}
\prod_{p\in J_h(m)}\sum_{r\ge0}p^{-r\sigma}
=m^{-\sigma}\prod_{p\in J_h(m)}(1-p^{-\sigma})^{-1}
\]

for \(\sigma>0\), and

\[
\rho_M(m)^2
=m^{-\sigma}\sum_{a\ge1}a^{-h\sigma}
=m^{-\sigma}\zeta(h\sigma)
\]

for \(\sigma>1/h\). Since \(e_m\) belongs to its own fiber,

\[
T_me_m=m^{-s/2}e_m.
\]

Writing \(\lambda_m=m^{-s/2}\), rank one immediately gives

\[
T_m^k=\lambda_m^{k-1}T_m.
\]
\(\square\)

## Proposition 3: exact existence and compactness domains

For \(S\), if \(\sigma\le0\), the block
\(m=p^{h-1}\) contains \(p^{h-1+r}\), \(r\ge0\), and

\[
\sum_{r\ge0}p^{-(h-1+r)\sigma}=\infty.
\]

Hence no bounded extension exists. Suppose \(\sigma>0\). Every
non-saturated local contribution \(p^{-e\sigma}\), \(1\le e\le h-2\), is
less than one. A saturated local contribution is

\[
b_p=p^{-(h-1)\sigma}(1-p^{-\sigma})^{-1}.
\]

It tends to zero, so only finitely many \(b_p\) exceed one. Their product
is a finite uniform bound for all \(\rho_S(m)^2\). Thus \(S\) is bounded.

To see compactness, let \(m\to\infty\) through \(\mathcal F_h\). Since all
exponents are bounded by \(h-1\), some prime divisor of \(m\) tends to
infinity. Its corresponding local contribution tends to zero, all but
finitely many other local contributions are at most one, and the exceptional
finite product is uniformly bounded. Hence \(\rho_S(m)\to0\). An orthogonal
direct sum of rank-one blocks with norms tending to zero is compact.

For \(M\), the \(m=1\) coefficient square mass is \(\zeta(h\sigma)\), which
is finite exactly when \(\sigma>1/h\). On that domain,

\[
\rho_M(m)=\zeta(h\sigma)^{1/2}m^{-\sigma/2}\to0,
\]

so \(M\) is bounded and compact. This proves both exact domain statements.
\(\square\)

## Proposition 4: Schatten classes and powers

For \(S\), orthogonality of the blocks gives

\[
\sum_{m\in\mathcal F_h}\rho_S(m)^q
=\prod_p\left[
1+\sum_{e=1}^{h-2}p^{-e\sigma q/2}
+p^{-(h-1)\sigma q/2}(1-p^{-\sigma})^{-q/2}
\right].
\]

For \(h\ge3\), the first local term is \(p^{-\sigma q/2}\). For \(h=2\),
the saturated term is asymptotic to \(p^{-\sigma q/2}\). The positive Euler
product therefore converges exactly when

\[
\sigma q/2>1.
\]

For \(M\),

\[
\sum_{m\in\mathcal F_h}\rho_M(m)^q
=\zeta(h\sigma)^{q/2}
\sum_{m\in\mathcal F_h}m^{-\sigma q/2}.
\]

The first factor requires \(\sigma>1/h\), and

\[
\sum_{m\in\mathcal F_h}m^{-a}
=\frac{\zeta(a)}{\zeta(ha)}
\]

converges exactly when \(a>1\). This gives the \(k=1\) assertions.

By Lemma 2, the unique singular value of \(T_m^k\) is

\[
|\lambda_m|^{k-1}\rho_T(m).
\]

Thus the saturated \(q\)-sum has Euler factors

\[
1+\sum_{e=1}^{h-2}p^{-ek\sigma q/2}
+p^{-(h-1)k\sigma q/2}(1-p^{-\sigma})^{-q/2},
\]

which converge exactly when \(k\sigma q/2>1\). The modulo sum is

\[
\zeta(h\sigma)^{q/2}
\frac{\zeta(k\sigma q/2)}{\zeta(hk\sigma q/2)},
\]

whenever both displayed factors are legal. Hence

\[
S^k\in\mathcal S_q\iff k\sigma q>2,
\]

\[
M^k\in\mathcal S_q
\iff\sigma>1/h\text{ and }k\sigma q>2.
\]

At equality the corresponding prime harmonic sum diverges, so every
endpoint is strict. \(\square\)

## Proposition 5: common cyclic ledger and legal determinants

On block \(m\), the only nonzero eigenvalue is
\(\lambda_m=m^{-s/2}\), with eigenvector \(e_m\). Since \(\sigma>0\) on
either bounded domain, \(|\lambda_m|=m^{-\sigma/2}\) is strictly decreasing
in \(m\). Thus the global nonzero eigenvalues are simple and are the same
for both operators.

If \(T^k\) is trace class, the trace of its rank-one block is
\(\lambda_m^k\). On the common bounded domain and for \(k\sigma>2\),
absolute convergence gives

\[
\operatorname{Tr}(T^k)
=\sum_{m\in\mathcal F_h}m^{-ks/2}
=\prod_p\sum_{e=0}^{h-1}p^{-eks/2}
=\frac{\zeta(ks/2)}{\zeta(hks/2)}.
\]

If \(k\sigma\le2\), the positive modulus sum diverges, so no ordinary trace
is asserted.

For an integer \(r\ge1\), if \(\sigma>1/h\) and \(r\sigma>2\), both
operators lie in \(\mathcal S_r\). The regularized Fredholm product depends
only on the algebraic nonzero eigenvalues with multiplicity:

\[
\det_r(I-zT)
=\prod_{m\in\mathcal F_h}
\left[
(1-z\lambda_m)
\exp\left(\sum_{j=1}^{r-1}\frac{(z\lambda_m)^j}{j}\right)
\right].
\]

It is therefore identical for \(S\) and \(M\). For \(r=1\), this is the
ordinary Fredholm determinant and requires \(\sigma>2\). No determinant is
used to infer similarity. \(\square\)

## Proposition 6: Riesz projections and bounded similarity

The Riesz idempotent for \(\lambda_m\) on block \(m\) is

\[
\Pi_{T,m}=\lambda_m^{-1}T_m.
\]

Consequently,

\[
\|\Pi_{T,m}\|=\rho_T(m)/|\lambda_m|.
\]

The block formulas give

\[
\|\Pi_{S,m}\|
=\prod_{p\in J_h(m)}(1-p^{-\sigma})^{-1/2},
\qquad
\|\Pi_{M,m}\|=\sqrt{\zeta(h\sigma)}.
\]

We now justify the iff rather than only sufficiency. If
\(T=XNX^{-1}\) with \(N\) compact normal, its distinct nonzero spectral
projections are conjugates of orthogonal projections, so

\[
\sup_m\|\Pi_{T,m}\|\le\|X\|\,\|X^{-1}\|<\infty.
\]

Conversely, a rank-one idempotent with range \(\mathbb Ce_m\) is, relative
to \(\mathbb Ce_m\oplus e_m^\perp\), the projection onto the first summand
along the graph of a bounded functional. The elementary graph transform
conjugates it to the orthogonal projection with the transform and its
inverse bounded by a function of the idempotent norm. Therefore a uniform
bound on all \(\Pi_{T,m}\) gives a uniformly bounded direct sum of these
graph transforms. It conjugates \(T\) to the diagonal normal operator with
entries \(\lambda_m\) and zero on the complementary block kernels. The
diagonal is compact because \(\lambda_m\to0\).

For \(M\), the projection norm is the same finite number for every block
throughout \(\sigma>1/h\). For \(S\),

\[
\sup_m\|\Pi_{S,m}\|
=\left(\prod_p(1-p^{-\sigma})^{-1}\right)^{1/2}
\]

as a finite value or \(+\infty\), because every finite prime set can occur
as \(J_h(m)\). The Euler product is finite exactly when \(\sigma>1\).
Thus

\[
S\sim_{\mathrm{bd}}\text{ normal}\iff\sigma>1,
\qquad
M\sim_{\mathrm{bd}}\text{ normal}\iff\sigma>1/h.
\]
\(\square\)

## Proposition 7: exact primorial optimizer and maximal order

Let \(p_1<p_2<\cdots\) be the primes,
\(P_k=\prod_{j\le k}p_j\), and \(P_0=1\).
Choose the largest \(k=k(x)\) for which

\[
P_k^{h-1}\le x,
\]

and put \(m_x=P_k^{h-1}\). If \(k=0\), the maximum is the empty-product
value at \(m=1\). Suppose henceforth that \(k\ge1\). Every \(m\le x\) with
\(r\) saturated primes
has

\[
\prod_{p\in J_h(m)}p^{h-1}\le m\le x.
\]

If \(r\ge k+1\), the left side is at least
\(P_{k+1}^{h-1}>x\), impossible. For fixed \(r\le k\), replacing any
saturated prime by a smaller omitted prime decreases the cost and increases
the factor \((1-p^{-\sigma})^{-1/2}\). Adding another saturated prime
increases the projection norm. Hence the exact maximum is attained at
\(m_x\):

\[
\max_{\substack{m\le x\\m\in\mathcal F_h}}\|\Pi_{S,m}\|
=\prod_{p\le p_{k(x)}}(1-p^{-\sigma})^{-1/2}.
\]

Let \(y=p_{k(x)}\). The prime number theorem gives

\[
(h-1)\vartheta(y)\sim\log x,\qquad
y\sim\frac{\log x}{h-1}.
\]

If \(\sigma>1\), the Euler product converges and

\[
\max_{m\le x}\|\Pi_{S,m}\|\longrightarrow\sqrt{\zeta(\sigma)}.
\]

If \(\sigma=1\), Mertens' product theorem gives

\[
\max_{m\le x}\|\Pi_{S,m}\|
\sim\sqrt{e^\gamma\log\log x}.
\]

If \(0<\sigma<1\), then

\[
\log\max_{m\le x}\|\Pi_{S,m}\|
=\frac12\sum_{p\le y}-\log(1-p^{-\sigma})
\sim\frac{y^{1-\sigma}}{2(1-\sigma)\log y}.
\]

Substituting the asymptotic for \(y\) yields

\[
\log\max_{m\le x}\|\Pi_{S,m}\|
\sim
\frac{(h-1)^{\sigma-1}(\log x)^{1-\sigma}}
{2(1-\sigma)\log\log x}.
\]

This proves the exact coefficient in all three regimes. \(\square\)

## Proposition 8: saturated Tauberian Weyl law

For \(\sigma>0\), define

\[
w_{h,\sigma}(m)
=m\prod_{p\in J_h(m)}(1-p^{-\sigma})^{1/\sigma}.
\]

Then

\[
\rho_S(m)=w_{h,\sigma}(m)^{-\sigma/2}.
\]

The positive generalized Dirichlet series has Euler factorization, initially
for \(\Re z>1\),

\[
F_{h,\sigma}(z)
=\sum_{m\in\mathcal F_h}w_{h,\sigma}(m)^{-z}
=\prod_p L_p(z),
\]

\[
L_p(z)=\sum_{e=0}^{h-2}p^{-ez}
+p^{-(h-1)z}(1-p^{-\sigma})^{-z/\sigma}.
\]

Factor one zeta function:

\[
F_{h,\sigma}(z)=\zeta(z)G_{h,\sigma}(z),
\qquad
G_{h,\sigma}(z)=\prod_p(1-p^{-z})L_p(z).
\]

On a compact subset of \(\Re z>a\), expansion of the last local factor gives

\[
(1-p^{-z})L_p(z)
=1+O(p^{-h\Re z})
+O(p^{-(h-1)\Re z-\sigma}),
\]

uniformly for large \(p\). Therefore \(G_{h,\sigma}\) converges locally
uniformly and is holomorphic in

\[
\Re z>\theta_{h,\sigma}
=\max\left(\frac1h,\frac{1-\sigma}{h-1}\right).
\]

Because \(h\ge2\) and \(\sigma>0\), this number is strictly below one.
At \(z=1\), the residue of \(F\) is the positive convergent product

\[
C_{h,\sigma}=G_{h,\sigma}(1)
=\prod_p(1-p^{-1})
\left[
\sum_{e=0}^{h-2}p^{-e}
+p^{-(h-1)}(1-p^{-\sigma})^{-1/\sigma}
\right].
\]

The coefficients define a positive locally finite counting measure. Any
finitely many generalized weights below one can be rescaled or removed
without affecting the asymptotic. The continuation above supplies a simple
pole at one with residue \(C_{h,\sigma}\) and no other singularity on the
line \(\Re z=1\). Wiener--Ikehara applied to the nondecreasing function

\[
A_S(x)=\#\{m\in\mathcal F_h:w_{h,\sigma}(m)\le x\}
\]

gives

\[
A_S(x)\sim C_{h,\sigma}x.
\]

Since the number of singular values at least \(t\) is
\(A_S(t^{-2/\sigma})\), asymptotic inversion yields

\[
s_n(S_{h,s})
\sim\left(\frac{C_{h,\sigma}}n\right)^{\sigma/2}.
\]
\(\square\)

## Proposition 9: modulo and eigenvalue Weyl laws

The \(h\)-free counting theorem gives

\[
\#\{m\in\mathcal F_h:m\le x\}\sim\frac{x}{\zeta(h)}.
\]

For \(M\),

\[
\rho_M(m)=\zeta(h\sigma)^{1/2}m^{-\sigma/2}.
\]

Thus the number of singular values at least \(t\) is asymptotic to

\[
\frac{\zeta(h\sigma)^{1/\sigma}}{\zeta(h)}
t^{-2/\sigma}.
\]

With

\[
D_{h,\sigma}
=\frac{\zeta(h\sigma)^{1/\sigma}}{\zeta(h)},
\]

inversion gives

\[
s_n(M_{h,s})
\sim\left(\frac{D_{h,\sigma}}n\right)^{\sigma/2}.
\]

The same count without the fiber multiplier gives the common eigenvalue
law

\[
|\lambda_n|
\sim\left(\frac{1/\zeta(h)}n\right)^{\sigma/2}.
\]

At \(\sigma=1\), the local bracket in \(C_{h,1}\) is

\[
\sum_{e=0}^{h-2}p^{-e}
+p^{-(h-1)}(1-p^{-1})^{-1}
=\sum_{e=0}^{\infty}p^{-e}
=(1-p^{-1})^{-1}.
\]

Every local factor of \(C_{h,1}\) is therefore one. Also

\[
D_{h,1}=\frac{\zeta(h)}{\zeta(h)}=1.
\]

Hence \(C_{h,1}=D_{h,1}=1\), with no claimed ordering away from one.
\(\square\)

## Lemma 10: rank-one self-commutator singular values

Write a nonzero rank-one block as

\[
T=\rho\,u\otimes v,
\]

where \(u,v\) are unit vectors and the convention is chosen so that the
unique nonzero eigenvalue has modulus

\[
a=\rho|\langle u,v\rangle|.
\]

Then

\[
T^*T=\rho^2 v\otimes v,\qquad
TT^*=\rho^2 u\otimes u.
\]

On \(\operatorname{span}\{u,v\}\), their difference is self-adjoint,
traceless, and has determinant
\(-\rho^4(1-|\langle u,v\rangle|^2)\). Its two eigenvalues are therefore

\[
\pm \rho^2\sqrt{1-a^2/\rho^2}.
\]

The two singular values are the common absolute value

\[
c=\rho^2\sqrt{1-a^2/\rho^2},
\]

possibly zero in a one-dimensional block. \(\square\)

## Proposition 11: exact self-commutator ideals

For \(S\),

\[
\frac{|\lambda_m|^2}{\rho_S(m)^2}
=\prod_{p\in J_h(m)}(1-p^{-\sigma}).
\]

Lemma 10 and \(c_m\le\rho_S(m)^2\) show sufficiency:

\[
\sum_m c_m^q
\le\sum_m\rho_S(m)^{2q}<\infty
\quad\text{when}\quad\sigma q>1,
\]

by Proposition 4 with exponent \(2q\).

For necessity when \(h\ge3\), fix a prime \(p_0\) and take

\[
m_r=p_0^{h-1}r
\]

as \(r\) varies over primes other than \(p_0\). Here \(r\) has exponent one,
so \(J_h(m_r)=\{p_0\}\). The angle factor is a fixed positive constant and
\(c_{m_r}\asymp r^{-\sigma}\). Hence
\(\sum_r c_{m_r}^q\) diverges for \(\sigma q\le1\).

For \(h=2\), exponent one is saturated. Fix \(p_0\) and instead take

\[
m_r=p_0r.
\]

Now \(J_2(m_r)=\{p_0,r\}\), while

\[
1-\prod_{p\in J_2(m_r)}(1-p^{-\sigma})
\ge p_0^{-\sigma}.
\]

Again \(c_{m_r}\asymp r^{-\sigma}\), and the prime sum diverges at and
below \(\sigma q=1\). Thus

\[
[S^*,S]\in\mathcal S_q\iff\sigma q>1.
\]

For \(M\),

\[
\frac{|\lambda_m|^2}{\rho_M(m)^2}
=\frac1{\zeta(h\sigma)}.
\]

The angle factor is a positive constant throughout the bounded domain, so
\(c_m\asymp m^{-\sigma}\). Therefore

\[
\sum_{m\in\mathcal F_h}c_m^q<\infty
\iff\sigma q>1,
\]

in addition to \(\sigma>1/h\). This proves the modulo statement.
\(\square\)

## Proposition 12: exact \(h=2\) Hilbert--Schmidt control

For squarefree \(m\), put

\[
\Lambda_m=\prod_{p\mid m}(p^\sigma-1)^{-1},
\qquad
\Delta_m=\prod_{p\mid m}(1-p^{-\sigma}).
\]

Then \(\rho_S(m)^2=\Lambda_m\) and
\(|\lambda_m|^2/\rho_S(m)^2=\Delta_m\). Every nonzero commutator block
therefore has two singular values

\[
\Lambda_m\sqrt{1-\Delta_m}.
\]

For \(\sigma>1/2\), the two positive sums below converge separately, and
Euler factorization gives

\[
\|[S^*,S]\|_2^2
=2\left\{
\prod_p\left[1+(p^\sigma-1)^{-2}\right]
-\prod_p\left[1+\frac{p^{-2\sigma}}{1-p^{-\sigma}}\right]
\right\}.
\]

Indeed, the first product sums \(\Lambda_m^2\), while the second sums
\(\Lambda_m^2\Delta_m\), since

\[
(p^\sigma-1)^{-2}(1-p^{-\sigma})
=\frac{p^{-2\sigma}}{1-p^{-\sigma}}.
\]

At \(\sigma=1/2\), separate convergence fails and Proposition 11 already
shows that the commutator is not Hilbert--Schmidt. \(\square\)

## Endpoint and sharpness ledger

1. At \(\sigma=0\), saturated fiber square masses diverge.
2. At \(\sigma=1/h\), the modulo \(m=1\) fiber is the harmonic series
   \(\sum_a a^{-1}\).
3. At \(k\sigma q=2\), the relevant positive prime sum diverges.
4. At \(k\sigma=2\), the ordinary trace is not defined by an absolutely
   convergent trace-class sum.
5. At \(\sigma=1\), \(C=D=1\), \(M\) is similar to normal, and \(S\) is not.
6. At \(\sigma q=1\), the fixed-prime families in Proposition 11 force
   commutator divergence.
7. The \(h=2\) necessity witness requires a second saturated prime; the
   exponent-one construction is reserved for \(h\ge3\).
8. Equal eigenvalues and regularized determinants do not imply bounded
   similarity, as the full band \(1/h<\sigma\le1\) demonstrates.

## Delete-shared-method conclusion

After removing generic weighted-composition, rank-one, Schatten,
regularized-determinant, oblique-projection, and free-UFD methods, the exact
all-\(h\) paired similarity classification, primorial maximal-order
coefficient, Tauberian singular constants and crossover, and commutator
phase law remain. The proof therefore supports GO_WITH_FIREWALL for the
paired theorem and STOP for an \(h=2\)-only paper.
