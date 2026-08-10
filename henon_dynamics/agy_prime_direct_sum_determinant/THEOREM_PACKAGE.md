# HCS-C28 theorem package: sharp prime--Schatten thresholds

## Material passport

- **Candidate:** HCS-C28, the odd-prime direct sum of the HCS-C27
  finite-Weil Rauzy--AGY transfer operators.
- **Date:** 2026-08-10.
- **Analytic input:** the common C26 Bergman domain and locally uniform
  trace-norm branch majorant.
- **Dynamical input:** the C25 fixed-start matrix decoder and its free-monoid
  corollary for concatenated AGY first returns.
- **Arithmetic input:** the full \(p^2\)-dimensional C27 finite Weil
  representation and Thomas character formula.
- **New theorem:** local Schatten norms have sharp order \(p^{2/q}\), and
  every scalar-weighted prime direct sum is classified exactly.
- **New positive object:** an ordinary prime-order-independent Fredholm
  determinant on \(\operatorname{Re}z>3\).
- **New negative result:** the undamped sum is noncompact, whereas the
  normalized-trace positive-AGY determinant germ converges to one.
- **Scoped ambient control:** C24-P073 defeats the dimension-normalized
  MARKED sum in the full C24 Rauzy ledger; it is not declared to be a C26
  induced branch.

The statements below distinguish theorem, exact finite certificate, finite
evidence, and open gate.  No Route-A score is assigned here.

## 1. Frozen hypotheses and chronology

Let \(\Omega\subset\mathbb C^3\) be the C26 bounded domain and put

\[
\mathcal H_0=A^2(\Omega).
\]

The countable induced alphabet is \(\Gamma\).  For
\(s\) in the source half-plane

\[
\mathfrak S=\{s\in\mathbb C:\operatorname{Re}s>-\sigma_0\},
\]

write \(K_{s,\gamma}\) for the scalar holomorphic weighted-composition
branch.  We use the following proved inputs.

### Hypothesis package H

1. **Locally uniform nuclear majorant.** For every compact
   \(K\Subset\mathfrak S\),
   \[
   C_{1,K}:=
   \sup_{s\in K}\sum_{\gamma\in\Gamma}
   \|K_{s,\gamma}\|_1<\infty.
   \tag{H1}
   \]
   For every \(\varepsilon>0\), there is a finite \(F\subset\Gamma\)
   such that
   \[
   \sup_{s\in K}\sum_{\gamma\notin F}\|K_{s,\gamma}\|_1
   <\varepsilon.
   \tag{H1-tail}
   \]
   In particular, for every \(1\le q<\infty\),
   \(\sum_\gamma\|K_{s,\gamma}\|_q\) has the same locally uniform
   majorant.
2. **Bounded slices.** There is a real interior point
   \(x_0\in\Omega\) for which constant embedding
   \(\iota_0:\mathbb C\to\mathcal H_0\) and evaluation
   \(E_0:\mathcal H_0\to\mathbb C\) are bounded.  Their tensor extensions
   have norms independent of the finite fibre dimension.
3. **Nonzero summable coefficients.** With
   \[
   a_\gamma(s)=w_{s,\gamma}(x_0),
   \]
   every \(a_\gamma\) is holomorphic and nowhere zero on \(\mathfrak S\),
   and
   \[
   \sup_{s\in K}\sum_\gamma|a_\gamma(s)|<\infty
   \tag{H2}
   \]
   for compact \(K\Subset\mathfrak S\).  For every
   \(\varepsilon>0\), there is also a finite \(F\subset\Gamma\) such that
   \[
   \sup_{s\in K}\sum_{\gamma\notin F}|a_\gamma(s)|<\varepsilon.
   \tag{H2-tail}
   \]
4. **Integral symplectic decoder.** Every branch has a matrix
   \(g_\gamma\in\operatorname{Sp}(J_0,\mathbb Z)\).  C25 Theorem E.1
   says that the full labeled fixed-start Rauzy matrix and the starting
   permutation recover the complete directed edge word.  C25 Corollary
   E.2 says that distinct first-return paths have distinct matrices and
   that concatenations split uniquely at base-state visits.  Hence the
   chronological matrix monoid is free on the countable first-return
   generators.  In particular,
   \[
   \gamma\ne\delta\Longrightarrow g_\gamma g_\delta^{-1}\ne I,
   \qquad
   w\ne\varnothing\Longrightarrow g_w\ne I.
   \tag{H3}
   \]
5. **Finite-Weil fibres.** For every odd prime \(p\),
   \(\rho_p\) is the full genuine finite Weil representation on
   \(\mathbb C^{p^2}\), pulled back to the source symplectic frame.  Put
   \[
   \mathcal H_p=\mathcal H_0\widehat\otimes\mathbb C^{p^2},
   \qquad
   \mathcal L_{s,p}
   =\sum_{\gamma\in\Gamma}
   K_{s,\gamma}\otimes\rho_p(g_\gamma\bmod p).
   \tag{H4}
   \]
   C27 proves trace-norm convergence and holomorphy for each fixed \(p\).
6. **Absolute word tails.** For each fixed \(n\), put
   \[
   A_{s,w}=\frac{\lambda_w^{-(s+1)}}{\chi_w'(\lambda_w)}.
   \]
   For every compact \(K\Subset\mathfrak S\) and every
   \(\varepsilon>0\), there is a finite \(W\subset\Gamma^n\) such that
   \[
   \sup_{s\in K}
   \sum_{w\in\Gamma^n\setminus W}|A_{s,w}|<\varepsilon.
   \tag{H5}
   \]

Later forward returns multiply on the left.  If
\(w=(\gamma_1,\ldots,\gamma_n)\) is an operator word, its fibre matrix is
the source-locked chronological product \(g_w\); no averaged matrix or
product of branch characters replaces it.  A repeated primitive word uses
\(\Theta_p(g_w^r)\), where

\[
\Theta_p(h)=\operatorname{Tr}\rho_p(h\bmod p).
\]

## 2. Normalized character limit

### Lemma 2.1 -- eventual rank and Weil magnitude

Let \(h\in\operatorname{Sp}(J_0,\mathbb Z)\) be fixed and set

\[
r(h)=\operatorname{rank}_{\mathbb Q}(h-I).
\]

Outside a finite set of odd primes,

\[
\operatorname{rank}_{\mathbb F_p}(h-I)=r(h)
\]

and

\[
\boxed{
\frac{|\Theta_p(h)|}{p^2}=p^{-r(h)/2}.
}
\tag{2.1}
\]

#### Proof

All minors of size larger than \(r(h)\) vanish integrally, while at least
one \(r(h)\)-minor is a nonzero integer.  Excluding its prime divisors fixes
the rank modulo \(p\).  The fixed-space dimension is then \(4-r(h)\).
C27's exact Thomas formula gives

\[
|\Theta_p(h)|^2=p^{4-r(h)},
\]

which is (2.1).  \(\square\)

### Corollary 2.2 -- convergence to the regular character

For every fixed integral cocycle element,

\[
\boxed{
\frac{\Theta_p(h)}{p^2}\longrightarrow
\delta_I(h)=
\begin{cases}
1,&h=I,\\
0,&h\ne I.
\end{cases}}
\tag{2.2}
\]

This is pointwise convergence on the fixed discrete integral cocycle group.
It is not a uniform assertion over words whose length grows with \(p\).
Since normalized finite-dimensional characters are positive definite,
\(\delta_I\) is naturally the regular character of that group.

## 3. Sharp local Schatten growth

For \(1\le q<\infty\), let \(\|\cdot\|_q\) denote the Schatten norm.

### Theorem 3.1 -- sharp finite-Weil multiplicity

For every compact \(K\Subset\mathfrak S\) and every
\(1\le q<\infty\), there are constants

\[
0<c_{q,K}\le C_{q,K}<\infty
\]

and a prime \(p_K\) such that, for every odd \(p\ge p_K\) and every
\(s\in K\),

\[
\boxed{
c_{q,K}p^{2/q}
\le\|\mathcal L_{s,p}\|_q
\le C_{q,K}p^{2/q}.
}
\tag{3.1}
\]

The operator norm likewise satisfies

\[
0<c_{\infty,K}
\le\|\mathcal L_{s,p}\|
\le C_{\infty,K}.
\tag{3.2}
\]

#### Proof: upper bound

The singular values of \(K\otimes U\), with \(U\) unitary on an
\(N\)-dimensional space, are the singular values of \(K\) repeated \(N\)
times.  Thus

\[
\|K_{s,\gamma}\otimes\rho_p(g_\gamma)\|_q
=p^{2/q}\|K_{s,\gamma}\|_q.
\]

The triangle inequality and (H1) yield

\[
\|\mathcal L_{s,p}\|_q
\le p^{2/q}\sum_\gamma\|K_{s,\gamma}\|_q
\le C_{1,K}p^{2/q}.
\]

The same branch sum without the multiplicity factor gives the uniform
operator-norm upper bound.

#### Proof: lower bound and uniformity

Tensor the maps in (H2) with the identity on \(\mathbb C^{p^2}\), and
write them as \(\iota_p\) and \(E_p\).  Their norms are independent of \(p\).
The exact compression is

\[
B_{s,p}:=E_p\mathcal L_{s,p}\iota_p
=\sum_{\gamma\in\Gamma}
a_\gamma(s)\rho_p(g_\gamma).
\tag{3.3}
\]

Fix one branch \(\delta\).  With
\(\tau_p=p^{-2}\operatorname{Tr}\),

\[
\tau_p\!\left(B_{s,p}\rho_p(g_\delta)^{-1}\right)
=a_\delta(s)
+\sum_{\gamma\ne\delta}a_\gamma(s)
 \frac{\Theta_p(g_\gamma g_\delta^{-1})}{p^2}.
\tag{3.4}
\]

Every off-diagonal matrix in (3.4) is nonidentity by (H3), so each
normalized character tends to zero by Corollary 2.2.  Its modulus is at most
one because it is the normalized trace of a unitary.

The convergence is locally uniform in \(s\), not merely pointwise.  Indeed,
given \(\varepsilon>0\), (H2) supplies a finite set \(F\subset\Gamma\)
whose complementary coefficient sum is less than \(\varepsilon\), uniformly
on \(K\).  The finitely many normalized characters indexed by
\(F\setminus\{\delta\}\) tend to zero independently of \(s\); the tail is
bounded by \(\varepsilon\).  Hence

\[
\tau_p\!\left(B_{s,p}\rho_p(g_\delta)^{-1}\right)
\longrightarrow a_\delta(s)
\quad\text{uniformly on }K.
\tag{3.5}
\]

The function \(a_\delta\) is continuous and nowhere zero, so
\(m_{\delta,K}=\min_{s\in K}|a_\delta(s)|>0\).  For all sufficiently large
\(p\), the absolute value in (3.5) is at least \(m_{\delta,K}/2\).

Let \(q'\) be conjugate to \(q\).  Schatten duality gives

\[
\begin{aligned}
\frac{m_{\delta,K}}2p^2
&\le
\left|\operatorname{Tr}
 (B_{s,p}\rho_p(g_\delta)^{-1})\right|\\
&\le
\|B_{s,p}\|_q
\|\rho_p(g_\delta)^{-1}\|_{q'}
=\|B_{s,p}\|_q p^{2/q'}.
\end{aligned}
\]

Therefore \(\|B_{s,p}\|_q\ge(m_{\delta,K}/2)p^{2/q}\).  The ideal
inequality

\[
\|B_{s,p}\|_q
\le\|E_p\|\,\|\mathcal L_{s,p}\|_q\,\|\iota_p\|
\]

transfers the lower bound to \(\mathcal L_{s,p}\).  Taking
\(q=\infty\) in the trace duality argument gives (3.2).  \(\square\)

### Scope of Theorem 3.1

The lower bound uses no finite prime window and no equidistribution theorem.
It needs the full-matrix injectivity in (H3), not injectivity of
characteristic polynomials or conjugacy classes.  It applies to the complete
countable C26 induced branch family because the tail in (3.4) is controlled
before the prime limit is taken.

## 4. Exact classification of prime block sums

Let \((c_p)_{p\ \mathrm{odd}}\) be complex scalars and define

\[
\mathbb L_s(c)
=\bigoplus_{p\ \mathrm{odd}}c_p\mathcal L_{s,p}
\quad\text{on}\quad
\mathcal H_\oplus=\bigoplus_{p\ \mathrm{odd}}\mathcal H_p.
\tag{4.1}
\]

### Theorem 4.1 -- weighted prime--Schatten criterion

For every fixed \(s\in\mathfrak S\) and every \(1\le q<\infty\),

\[
\boxed{
\mathbb L_s(c)\in S_q
\quad\Longleftrightarrow\quad
\sum_{p\ \mathrm{odd}}p^2|c_p|^q<\infty.
}
\tag{4.2}
\]

Moreover,

\[
\boxed{
\mathbb L_s(c)\text{ is compact}
\quad\Longleftrightarrow\quad c_p\to0.
}
\tag{4.3}
\]

If the scalar sum in (4.2) is finite, the \(S_q\)-valued family is locally
uniform in \(s\) on every compact set for which the C26 majorant is used.

#### Proof

For a block diagonal operator,

\[
\|\mathbb L_s(c)\|_q^q
=\sum_p|c_p|^q\|\mathcal L_{s,p}\|_q^q.
\]

Theorem 3.1 compares each summand, outside finitely many primes, with
\(p^2|c_p|^q\).  This proves (4.2).  Every prime block is compact; a block
diagonal sum of compact operators is compact exactly when its block norms
tend to zero.  Equations (3.2) and the uniform upper bound turn that
condition into \(c_p\to0\), proving (4.3).  \(\square\)

### Corollary 4.2 -- sharp Dirichlet phase diagram

For

\[
\mathfrak L_{s,z}
=\bigoplus_{p\ \mathrm{odd}}p^{-z}\mathcal L_{s,p},
\tag{4.4}
\]

one has

\[
\boxed{
\mathfrak L_{s,z}\in S_q
\quad\Longleftrightarrow\quad
q\operatorname{Re}z>3,
\qquad 1\le q<\infty.
}
\tag{4.5}
\]

It is compact exactly when \(\operatorname{Re}z>0\).  At
\(q\operatorname{Re}z=3\), the comparison series is
\(\sum_p1/p\), so equality is excluded.

## 5. Ordinary prime-graded Fredholm determinant

### Theorem 5.1 -- direct-sum determinant

On

\[
\mathfrak S\times\{z\in\mathbb C:\operatorname{Re}z>3\},
\]

the operator \(\mathfrak L_{s,z}\) is trace class and holomorphic with
values in \(S_1(\mathcal H_\oplus)\).  Hence

\[
\boxed{
\mathfrak D(s,z,u)
=\det_{\mathcal H_\oplus}(I-u\mathfrak L_{s,z})
}
\tag{5.1}
\]

is jointly holomorphic in \((s,z,u)\), and

\[
\boxed{
\mathfrak D(s,z,u)
=\prod_{p\ \mathrm{odd}}
\mathcal D_p(s,up^{-z}).
}
\tag{5.2}
\]

The product is locally normal and independent of the enumeration of the
odd primes.

#### Proof

On a compact set with \(\operatorname{Re}z\ge3+\varepsilon\), Theorem 3.1
and (H1) give

\[
\sum_p\|p^{-z}\mathcal L_{s,p}\|_1
\le C_K\sum_p p^{-1-\varepsilon}<\infty.
\]

The block terms are holomorphic in \((s,z)\).  Locally uniform summability
therefore gives an \(S_1\)-holomorphic direct sum.  The standard trace-class
determinant theorem gives (5.1).  Finite prime truncations factor blockwise;
their operators converge in trace norm, and determinant continuity gives
(5.2).  Absolute trace-norm convergence removes any dependence on prime
ordering.  \(\square\)

### Theorem 5.2 -- chronological trace expansion

Let

\[
A_{s,w}
=\frac{\lambda_w^{-(s+1)}}{\chi_w'(\lambda_w)}
\]

be the C26 scalar word atom.  For every \(n\ge1\),

\[
\boxed{
\operatorname{Tr}\mathfrak L_{s,z}^n
=\sum_{w\in\Gamma^n}A_{s,w}
 \sum_{p\ \mathrm{odd}}p^{-nz}\Theta_p(g_w).
}
\tag{5.3}
\]

All sums are absolutely convergent in the domain of Theorem 5.1.  If a
primitive word of length \(n\) is repeated \(r\) times, its fibre factor is

\[
p^{-nrz}\Theta_p(g_w^r),
\]

not \(p^{-nrz}\Theta_p(g_w)^r\).

## 6. Normalized-trace limit

### Theorem 6.1 -- regular-trace collapse of the positive monoid

For each fixed \(n\ge1\), locally uniformly in \(s\in\mathfrak S\),

\[
\boxed{
\frac1{p^2}\operatorname{Tr}\mathcal L_{s,p}^n
\longrightarrow0.
}
\tag{6.1}
\]

For every compact \(K\Subset\mathfrak S\), there is \(r_K>0\) such that,
on \(K\times\{|u|<r_K\}\), the logarithm fixed by its value zero at
\(u=0\) satisfies

\[
\boxed{
\frac1{p^2}\operatorname{Log}_0\mathcal D_p(s,u)\longrightarrow0,
\qquad
\exp\!\left[p^{-2}\operatorname{Log}_0\mathcal D_p(s,u)\right]
\longrightarrow1.
}
\tag{6.2}
\]

#### Proof

C27's absolute word trace gives

\[
\frac1{p^2}\operatorname{Tr}\mathcal L_{s,p}^n
=\sum_{w\in\Gamma^n}
A_{s,w}\frac{\Theta_p(g_w)}{p^2}.
\]

Every word is nonempty, so (H3) gives \(g_w\ne I\).  Corollary 2.2 makes
each normalized fibre factor tend to zero, while its modulus is at most one.
The locally uniform absolute word tail (H5) proves (6.1) by the same
finite-head/uniform-tail dominated-convergence argument.

Let \(M_K=\sup_{s\in K,p}\|\mathcal L_{s,p}\|<\infty\) and use
\(\|\mathcal L_{s,p}\|_1\le C_Kp^2\).  Then

\[
\frac1{p^2}
|\operatorname{Tr}\mathcal L_{s,p}^n|
\le C_KM_K^{n-1}.
\]

Choose \(r_K<M_K^{-1}\).  On that disc let
\(\operatorname{Log}_0\mathcal D_p(s,u)\) be the Fredholm logarithm whose
value at \(u=0\) is zero.  Its series converges absolutely, the displayed
bound dominates that series uniformly, and (6.1) applies term by term.  This
proves (6.2).  The exponential in (6.2) is branch-defined and is not a
globally chosen fractional power.  \(\square\)

### Exact scope of Theorem 6.1

The pointwise character limit is source-locked for every fixed integral
symplectic matrix.  Its dynamical application is source-locked for the
one-sided positive C26 AGY monoid because C25 proves (H3) and C27 proves the
absolute word trace.  The theorem does not apply to a new two-sided language
without checking identity words, does not assert convergence on the full
\(u\)-plane, and is a large-prime limit rather than a product over primes.

## 7. Orbitwise arithmetic

Suppose \(D_w=\det(I-g_w)\ne0\), and let \(\varepsilon_w\) be the quadratic
Kronecker character determined by the corresponding square class.  C27
gives, outside the finite set of odd primes dividing \(D_w\),

\[
\Theta_p(g_w)=\varepsilon_w(p).
\tag{7.1}
\]

Thus, for \(\operatorname{Re}\zeta>1\),

\[
\sum_{p\ \mathrm{odd}}p^{-\zeta}\Theta_p(g_w)
=P_{\varepsilon_w}^{\mathrm{odd}}(\zeta)+E_w(\zeta),
\tag{7.2}
\]

where \(E_w\) is an explicit finite singular-prime correction.  Write

\[
P_\chi^{\mathrm{odd}}(\zeta)
=P_\chi(\zeta)-\chi(2)2^{-\zeta}.
\tag{7.3}
\]

For \(\operatorname{Re}\zeta>1\), Möbius inversion of the Dirichlet Euler
logarithm, on the branch fixed by its absolutely convergent series at
infinity, gives

\[
P_\chi(\zeta)
=\sum_{k\ge1}\frac{\mu(k)}k
 \operatorname{Log} L(k\zeta,\chi^k).
\tag{7.4}
\]

Here \(\chi^k\) is the pointwise power of \(\chi\), and it may be
imprimitive.  No continuation across an \(L\)-zero, and no unrecorded
choice of logarithm, is used.

These are orbit-dependent quadratic prime series.  C27's 150-branch census
found 150 distinct signatures, which is finite evidence against one small
common conductor.  Neither (7.2) nor that census proves an all-length
fragmentation theorem.  Repetition generally changes \(D_w\), and
\(\Theta_p(g_w^r)\) may not be replaced by \(\varepsilon_w(p)^r\).

## 8. General marked normalization and C24-P073

### Proposition 8.1 -- marked absolute threshold

Let \(J_\star\) be a frozen unimodular integral symplectic form of rank four,
let \(\rho_{p,\star}\) be the full finite Weil representation pulled back to
that frame, and write
\[
\Theta_{p,\star}(g)
=\operatorname{Tr}\rho_{p,\star}(g\bmod p).
\]
The integral-minor proof of Lemma 2.1 and Thomas's magnitude formula apply
verbatim in this frame.

Let \(g\in\operatorname{Sp}(J_\star,\mathbb Z)\) be fixed and put

\[
k_{\mathbb Q}=\dim_{\mathbb Q}\ker(g-I).
\]

For complex \(\alpha\), the marked absolute prime sum

\[
\sum_{p\ \mathrm{odd}}|p^{-\alpha}\Theta_{p,\star}(g)|
\]

converges exactly when

\[
\boxed{
\operatorname{Re}\alpha>1+\frac{k_{\mathbb Q}}2.
}
\tag{8.1}
\]

#### Proof

Outside finitely many primes, the frame-general form of Lemma 2.1 gives
\(|\Theta_{p,\star}(g)|=p^{k_{\mathbb Q}/2}\).  Since
\(|p^{-\alpha}|=p^{-\operatorname{Re}\alpha}\), the result is the standard
convergence criterion for \(\sum_pp^{-\beta}\), including divergence at
\(\beta=1\).  \(\square\)

### Proposition 8.2 -- exact C24 fixed-plane control

The frozen C24 full-Rauzy cycle P073 has base-trivialized matrix

\[
g_{073}=
\begin{pmatrix}
1&8&4&4\\
1&13&6&6\\
1&6&4&3\\
1&2&1&2
\end{pmatrix}
\]

and

\[
\det(xI-g_{073})=(x-1)^2(x^2-18x+1).
\]

All \(3\times3\) minors of \(g_{073}-I\) vanish and the gcd of its
\(2\times2\) minors is one.  Hence its fixed-space dimension is two over
every finite field.  Write \(\Theta_{p,\mathrm{C24}}\) for the finite-Weil
character pulled back to the frozen C24 symplectic frame.  Quotient columns
zero and one give Thomas form

\[
Q_{073}=\begin{pmatrix}1&0\\8&-4\end{pmatrix}.
\]

For every odd prime,

\[
\boxed{
\Theta_{p,\mathrm{C24}}(g_{073})
=\left(\frac{-4}{p}\right)
 \left(\frac{-1}{p}\right)p=p.
}
\tag{8.2}
\]

Consequently

\[
\sum_{p\ \mathrm{odd}}
\frac{\Theta_{p,\mathrm{C24}}(g_{073})}{p^2}
=\sum_{p\ \mathrm{odd}}\frac1p=\infty.
\tag{8.3}
\]

Among the 146 frozen C24 eventually-positive cycles, the exact fixed-space
census is \(125,20,1\) in dimensions zero, one, and two, respectively;
P073 is the unique dimension-two cycle.

### Scope firewall for P073

P073 belongs to the C24 full labeled Rauzy control ledger.  It is not
asserted to be a branch of the C26 positive-prefix induced section.  Thus
(8.3) refutes the full-C24 dimension-normalized MARKED assembly, while the
all-word fixed-plane exclusion problem for the narrower C26 language remains
open.  This open question does not affect Theorems 3.1--5.1.

## 9. Regularized hierarchy

For an integer \(m\ge2\), Corollary 4.2 allows the regularized determinant
\(\det_m(I-u\mathfrak L_{s,z})\) exactly in the region

\[
\operatorname{Re}z>\frac3m.
\]

Near \(u=0\),

\[
\log\det_m(I-u\mathfrak L_{s,z})
=-\sum_{n\ge m}\frac{u^n}{n}
 \operatorname{Tr}\mathfrak L_{s,z}^n.
\]

Hence \(z=2\) yields an \(S_2\setminus S_1\) operator and a
\(\det_2\) that deletes the first trace; \(z=1\) first allows
\(\det_4\); and \(z=0\) gives a noncompact operator with no finite-order
regularized determinant.  Operator scaling
\(p^{-2}\mathcal L_{s,p}\) must not be confused with normalized fibre
trace \(p^{-2}\operatorname{Tr}\).

## 10. Interpretation and non-claims

The positive object is a **prime-graded Dirichlet--Fredholm determinant**.
It is not an adelic Weil representation.  A genuine adelic construction
requires local-field oscillator representations, compatible additive
characters and splittings, an adelic Schwartz space, and a restricted
tensor product with almost-everywhere reference vectors.  The direct sum of
the residue-field spaces \(\mathbb C^{p^2}\) supplies none of that
structure.

The exact canonicality trilemma is

\[
\begin{array}{c|c}
\text{unweighted counting-trace direct sum}&\text{noncompact}\\
\text{normalized-trace positive-monoid limit}&
   \text{determinant germ }1\\
\text{prime-norm damping}&
   \text{nontrivial ordinary determinant, external }z\log p.
\end{array}
\]

The package proves no continuation toward \(z=0\), functional equation,
gamma factor, common automorphic conductor, Riemann--von Mangoldt law,
\(\xi\)-divisor identity, self-adjoint Hilbert--P\'olya operator, or Riemann
hypothesis statement.  Route B is not authorized.

The next large structural candidates are a two-sided based path groupoid,
where nonempty identity-holonomy loops can survive the regular trace, or a
genuine local-field oscillator/automorphic architecture.  Either candidate
requires a new trace theorem and is not a relabeling of (5.1).
