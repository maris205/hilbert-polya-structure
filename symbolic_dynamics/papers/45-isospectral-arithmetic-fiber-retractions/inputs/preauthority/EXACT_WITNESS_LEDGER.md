# Exact witness ledger

## Status of this ledger

Every item below is a preregistered mathematical witness or later evaluator
target. None is an observed experiment result. A later run must record its
own inputs, outputs, precision, and source hashes rather than copying this
ledger as an expected-value fixture.

## W0: fixed \(h\)-free eigenline

For any \(m\in\mathcal F_h\),

\[
\tau_h(m)=\omega_h(m)=m,
\]

so

\[
S_{h,s}e_m=M_{h,s}e_m=m^{-s/2}e_m.
\]

This is the common nonzero eigenvalue witness. It says nothing about the
rest of either fiber.

## W1: \(h=2\), squarefree block

Let \(m=6\). Then

\[
\tau_2^{-1}(6)=\{2^{1+r}3^{1+t}:r,t\ge0\},
\qquad
\omega_2^{-1}(6)=\{6a^2:a\ge1\}.
\]

Therefore

\[
\rho_S(6)^2
=6^{-\sigma}(1-2^{-\sigma})^{-1}(1-3^{-\sigma})^{-1},
\]

\[
\rho_M(6)^2=6^{-\sigma}\zeta(2\sigma).
\]

The first fiber may increase only the already saturated primes 2 and 3; the
second may introduce any prime, but only in an even extra exponent.

## W2: \(h=3\), mixed saturated/nonsaturated block

Let \(m=12=2^2\cdot3\). Then

\[
J_3(12)=\{2\},
\qquad
\tau_3^{-1}(12)=\{12\cdot2^r:r\ge0\},
\]

\[
\omega_3^{-1}(12)=\{12a^3:a\ge1\}.
\]

Thus

\[
\rho_S(12)^2=12^{-\sigma}(1-2^{-\sigma})^{-1},
\qquad
\rho_M(12)^2=12^{-\sigma}\zeta(3\sigma).
\]

Mutating \(J_3(12)\) to \(\{2,3\}\) is a designated type failure.

## W3: direct finite block matrix

For any finite truncation \(E=\{n_0=m,n_1,\ldots,n_R\}\) of a fiber, the
matrix from \(\operatorname{span}\{e_n:n\in E\}\) to itself has only its
\(e_m\) row nonzero:

\[
B_E=
\begin{pmatrix}
m^{-s/2}&n_1^{-s/2}&\cdots&n_R^{-s/2}\\
0&0&\cdots&0\\
\vdots&\vdots&&\vdots\\
0&0&\cdots&0
\end{pmatrix}.
\]

Its exact invariants are

\[
\lambda(B_E)=m^{-s/2},\qquad
s_1(B_E)^2=\sum_{n\in E}n^{-\sigma},
\]

\[
B_E^k=m^{-(k-1)s/2}B_E.
\]

The increasing truncated square mass is a lower bound for the infinite
fiber mass, never a substitute for it.

## W4: existence-wall witnesses

- Saturated wall: for \(m=p^{h-1}\),

  \[
  \rho_S(m)^2
  =p^{-(h-1)\sigma}\sum_{r\ge0}p^{-r\sigma},
  \]

  which diverges at every \(\sigma\le0\).

- Modulo wall: for \(m=1\),

  \[
  \rho_M(1)^2=\sum_{a\ge1}a^{-h\sigma},
  \]

  which diverges at \(\sigma=1/h\) and below.

These witnesses prevent a formal power from bypassing operator existence.

## W5: ideal and trace endpoint witnesses

For \(h\ge3\), the exponent-one Euler term of the \(S^k\)
\(\mathcal S_q\) sum is \(p^{-k\sigma q/2}\). At
\(k\sigma q=2\), its prime sum diverges. For \(h=2\), the saturated local
term is asymptotic to the same quantity.

The common trace modulus sum contains

\[
\sum_{m\in\mathcal F_h}m^{-k\sigma/2}.
\]

At \(k\sigma=2\), this has the \(h\)-free harmonic divergence. Equality is
therefore excluded from both ledgers.

## W6: common trace and determinant witness

When \(\sigma>1/h\) and \(k\sigma>2\),

\[
\sum_{m\in\mathcal F_h}m^{-ks/2}
=\prod_p(1+p^{-ks/2}+\cdots+p^{-(h-1)ks/2})
=\frac{\zeta(ks/2)}{\zeta(hks/2)}.
\]

For every legal integer regularization order, both operators use the same
nonzero eigenvalue product. This witness is a negative control: equal
determinants must coexist with the different Riesz ledgers below.

## W7: projection-angle witness

\[
\|\Pi_{S,m}\|^2
=\prod_{p\in J_h(m)}(1-p^{-\sigma})^{-1},
\qquad
\|\Pi_{M,m}\|^2=\zeta(h\sigma).
\]

At

\[
m_y=\left(\prod_{p\le y}p\right)^{h-1},
\]

the saturated projection norm is

\[
\|\Pi_{S,m_y}\|
=\prod_{p\le y}(1-p^{-\sigma})^{-1/2}.
\]

This tends to infinity for \(0<\sigma\le1\), while the modulo norm remains
the fixed finite number \(\sqrt{\zeta(h\sigma)}\) on \(\sigma>1/h\).

## W8: exact primorial maximal-order coefficient

The largest admissible \(y\) satisfies

\[
(h-1)\vartheta(y)\le\log x.
\]

For \(0<\sigma<1\),

\[
\frac{
\log\max_{m\le x}\|\Pi_{S,m}\|
}{
(h-1)^{\sigma-1}(\log x)^{1-\sigma}/
[2(1-\sigma)\log\log x]
}\longrightarrow1.
\]

The factor \((h-1)^{\sigma-1}\) is mandatory. Deleting it, inverting it, or
replacing \(\log\log x\) by \(\log x\) is a hostile mutation.

## W9: Tauberian local cancellation

The saturated local series is

\[
L_p(z)=1+p^{-z}+\cdots+p^{-(h-2)z}
+p^{-(h-1)z}(1-p^{-\sigma})^{-z/\sigma}.
\]

Multiplication by \(1-p^{-z}\) cancels the first-order \(p^{-z}\) term.
Uniformly on compact subsets,

\[
(1-p^{-z})L_p(z)
=1+O(p^{-h\Re z})
+O(p^{-(h-1)\Re z-\sigma}).
\]

The two summability conditions are \(h\Re z>1\) and
\((h-1)\Re z+\sigma>1\), yielding the exact strip

\[
\Re z>\max\left(\frac1h,\frac{1-\sigma}{h-1}\right).
\]

## W10: mandatory \(\sigma=1\) crossover

At \(\sigma=1\),

\[
\sum_{e=0}^{h-2}p^{-e}
+p^{-(h-1)}(1-p^{-1})^{-1}
=(1-p^{-1})^{-1}.
\]

Hence each local factor in \(C_{h,1}\) is one, so

\[
C_{h,1}=1.
\]

Independently,

\[
D_{h,1}=\zeta(h)/\zeta(h)=1.
\]

The evaluator matrix must contain this row for every tested \(h\); a
universal strict inequality is a required rejection.

## W11: modulo and eigenvalue counts

The \(h\)-free density witness

\[
\#\{m\le x:m\in\mathcal F_h\}\sim x/\zeta(h)
\]

produces two different multipliers:

\[
D_{h,\sigma}=\zeta(h\sigma)^{1/\sigma}/\zeta(h)
\]

for modulo singular values, and \(1/\zeta(h)\) for the common eigenvalue
moduli. Confusing the two is a metric/cyclic type error.

## W12: rank-one commutator witness

For a block \(T=\rho u\otimes v\),

\[
T^*T-TT^*=\rho^2(v\otimes v-u\otimes u).
\]

The two singular values on \(\operatorname{span}\{u,v\}\) are

\[
\rho^2\sqrt{1-|\langle u,v\rangle|^2}
=\rho^2\sqrt{1-a^2/\rho^2}.
\]

Thus the commutator sees the square of the block scale and has wall
\(\sigma q=1\), distinct from the operator wall \(\sigma q=2\).

## W13: \(h=2\) necessity witness

Fix a prime \(p_0\) and let \(m_r=p_0r\) for varying primes
\(r\ne p_0\). Both primes are saturated, but

\[
1-(1-p_0^{-\sigma})(1-r^{-\sigma})
\ge p_0^{-\sigma}.
\]

The commutator block scale is therefore comparable to \(r^{-\sigma}\).
The prime sum diverges whenever \(\sigma q\le1\). This is the correct
\(h=2\) endpoint argument.

## W14: exact \(h=2\) Hilbert--Schmidt Euler control

For squarefree \(m\), define

\[
\Lambda_m=\prod_{p\mid m}(p^\sigma-1)^{-1},\qquad
\Delta_m=\prod_{p\mid m}(1-p^{-\sigma}).
\]

For \(\sigma>1/2\),

\[
\|[S^*,S]\|_2^2
=2\left\{
\prod_p[1+(p^\sigma-1)^{-2}]
-\prod_p\left[1+\frac{p^{-2\sigma}}{1-p^{-\sigma}}\right]
\right\}.
\]

Both products must be evaluated as separately convergent products. A
subtraction of divergent products at \(\sigma=1/2\) is forbidden.

## W15: formal free-UFD negative control

Let \(\mathfrak M\) be freely generated by atoms \(a_j\) and set
\(N(a_j)=p_j\), where \(p_j\) is the \(j\)th rational prime. Define
exponents, saturation, modulo reduction, and weights using \(N\), but give
the atoms no addition or rational-prime semantics.

The exponent combinatorics and norm Euler products are unchanged after the
relabeling \(p_j\leftrightarrow a_j\). Therefore every structural threshold
is reproduced. This is a required negative control against rational-prime
selectivity and receives zero novelty credit.

## Independent recomputation checklist

1. Generate fibers from the two raw maps, not from the closed fiber formulas.
2. Form finite matrices and independently compute singular, eigenvalue,
   power, projection, and commutator data.
3. Derive Euler factors from exponent states without importing matrix
   outputs.
4. Verify all strict walls from positive divergent subfamilies.
5. Verify local Tauberian cancellation, strip, residue, and positivity.
6. Compare exhaustive finite maxima with the exact primorial optimizer.
7. Include the mandatory \(C_{h,1}=D_{h,1}=1\) rows.
8. Reproduce the \(h=2\) second-saturated-prime endpoint.
9. Run the free-UFD clone only as a firewall.
10. Keep exact and numerical fields typed and retain independent method
    identities.
