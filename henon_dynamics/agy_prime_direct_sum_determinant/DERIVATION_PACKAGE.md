# Derivation Package

## Target

Determine whether the HCS-C27 fixed-prime finite-Weil AGY determinants admit
an undamped global assembly.  If they do not, derive a mathematically honest
prime-graded completion, determine its exact Schatten threshold, and state
what dynamical information survives.

## Status

COHERENT AFTER REFRAMING / EXTRA ASSUMPTION

The undamped one-clock target fails.  The coherent replacement is a
prime-direct-sum Fredholm family with an explicit Dirichlet parameter \(z\).
It is nontrivial and chronology preserving, but the added clock \(\log p\)
is not derived from the AGY roof.  Two canonical-looking alternatives also
fail: the counting-trace direct sum is noncompact, while the normalized-trace
large-\(p\) determinant germ converges to \(1\).

## Invariant Object

The invariant object is the chronological marked word trace

\[
A_{s,w}\Theta_p(g_w),
\qquad
A_{s,w}=
\frac{\lambda_w^{-(s+1)}}{\chi_w'(\lambda_w)}.
\]

The integer symplectic matrix \(g_w\) is formed in the full forward Rauzy
order before applying the finite Weil character.  Repetitions use
\(\Theta_p(g_w^r)\).  No averaged transition matrix, product of branch
characters, or absolute-value replacement is allowed.

## Assumptions

- HCS-C25 Theorem E.1 and Corollary E.2 give injectivity of fixed-start
  chronological Rauzy matrices and a free monoid on the countable AGY
  first-return generators.
- HCS-C26 supplies the common Bergman space
  \(\mathcal H_0=A^2(\Omega)\), bounded interior evaluation, bounded constant
  embedding, and normally summable branches: for every compact
  \(K\Subset\{\operatorname{Re}s>-\sigma_0\}\), there is a summable sequence
  \((M_{\gamma,K})_{\gamma\in\Gamma}\) such that
  \(\sup_{s\in K}\|K_{s,\gamma}\|_1\le M_{\gamma,K}\).
- HCS-C27 supplies
  \(\mathcal H_p=\mathcal H_0\widehat\otimes\mathbb C^{p^2}\), the
  trace-class operator
  \[
  \mathcal L_{s,p}=\sum_\gamma
  K_{s,\gamma}\otimes\rho_p(g_\gamma),
  \]
  and Thomas's exact character formula.
- The classical divergence of \(\sum_p1/p\) and Dirichlet's theorem on
  primes in reduced arithmetic progressions are used.

## Notation

- \(r(h)=\operatorname{rank}_{\mathbb Q}(h-I)\).
- \(k(h)=4-r(h)=\dim_{\mathbb Q}\ker(h-I)\).
- \(\Theta_p(h)=\operatorname{Tr}\rho_p(h\bmod p)\).
- When a frozen control uses another unimodular integral symplectic frame
  \(J_\star\), \(\Theta_{p,J_\star}\) denotes the character of the finite
  Weil representation pulled back through that frame; the frame subscript
  is suppressed when the surrounding C24 or C27 source lock makes it
  unambiguous.
- \(\|\cdot\|_q\) is the Schatten-\(q\) norm,
  \(1\le q\le\infty\).
- \(\mathcal H_\oplus=\bigoplus_{p\ {\rm odd}}\mathcal H_p\).
- \(d_h\) is the squarefree kernel of \(\det(I-h)\), when nonzero.
- \(\chi_h\) is the associated primitive quadratic Kronecker character.
- \(P_\chi(\zeta)=\sum_p\chi(p)p^{-\zeta}\) for
  \(\operatorname{Re}\zeta>1\).

## Derivation Strategy

First prove a large-prime character limit for every fixed integral
symplectic matrix.  Use that limit and the C25 matrix decoder to obtain a
sharp lower bound on every local Schatten norm; the C26 branch sum gives the
matching upper bound.  This classifies all weighted prime direct sums and
produces an ordinary Fredholm determinant exactly when
\(\operatorname{Re}z>3\).  Finally compare this positive construction with
the normalized-trace limit and with the exact C24-P073 fixed-plane control.

## Derivation Map

1. Rank stability modulo \(p\) plus Thomas's formula gives
   \(p^{-2}\Theta_p(h)\to\mathbf 1_{\{h=I\}}\).
2. Constant embedding and point evaluation compress
   \(\mathcal L_{s,p}\) to an \(\ell^1\) group-algebra sum.
3. Testing that compression against one inverse Weil matrix isolates one
   nonzero branch coefficient asymptotically.
4. Schatten Hölder gives the lower bound
   \(\|\mathcal L_{s,p}\|_q\gg p^{2/q}\); the branch tensor estimate gives
   the reverse inequality.
5. Hence
   \(\bigoplus_pc_p\mathcal L_{s,p}\in\mathcal S_q\) exactly when
   \(\sum_pp^2|c_p|^q<\infty\).
6. With \(c_p=p^{-z}\), the exact threshold is
   \(q\operatorname{Re}z>3\); the ordinary Fredholm region is
   \(\operatorname{Re}z>3\).
7. Word traces retain the full chronology and become orbit-dependent
   quadratic prime Dirichlet series with finite singular corrections.
8. The normalized-character limit is the regular trace.  The C25 free
   positive monoid has no nonempty identity word, so its normalized
   determinant germ tends to \(1\).
9. The C24-P073 fixed plane has \(\Theta_p=p\) for every odd \(p\), making
   its dimension-normalized marked prime sum equal to \(\sum_p1/p\).

## Main Derivation

### Step 1 — normalized finite-Weil characters converge to the regular trace

Let \(h\in\operatorname{Sp}(J_0,\mathbb Z)\) be fixed.  The rank of the
integer matrix \(h-I\) can drop modulo only finitely many primes: choose a
nonzero \(r(h)\)-minor and exclude its prime divisors.  For every remaining
odd prime,

\[
\dim_{\mathbb F_p}\ker(h-I)=4-r(h).
\]

Thomas's formula, in the exact form proved in C27, gives

\[
|\Theta_p(h)|=p^{(4-r(h))/2}.
\]

Consequently

\[
\boxed{
\frac{|\Theta_p(h)|}{p^2}=p^{-r(h)/2}
}
\]

outside a finite set.  If \(h\ne I\), then \(r(h)\ge1\), while
\(\Theta_p(I)=p^2\).  Therefore

\[
\boxed{
\frac{\Theta_p(h)}{p^2}\longrightarrow
\begin{cases}1,&h=I,\\0,&h\ne I.
\end{cases}}
\tag{1}
\]

This is an exact pointwise limit, not a numerical asymptotic.  On the
discrete integral cocycle group it is the regular character
\(\delta_I\).

### Step 2 — sharp local Schatten growth

Fix an interior point \(x_0\in\Omega\).  Let

\[
J_p:\mathbb C^{p^2}\longrightarrow\mathcal H_p,
\qquad J_pv=\mathbf 1\otimes v,
\]

and let \(E_p\) evaluate the Bergman component at \(x_0\).  Their operator
norms are independent of \(p\).  The compression is

\[
B_{s,p}:=E_p\mathcal L_{s,p}J_p
=\sum_{\gamma\in\Gamma}a_\gamma(s)\rho_p(g_\gamma),
\qquad
a_\gamma(s)=w_{s,\gamma}(x_0).
\tag{2}
\]

Every \(a_\gamma(s)\) is nonzero.  Boundedness of the two slice maps and the
common C26 majorant give a summable sequence \(A_{\gamma,K}\) with
\(\sup_{s\in K}|a_\gamma(s)|\le A_{\gamma,K}\).  In particular,
\[
\lim_{F\uparrow\Gamma}\sup_{s\in K}
\sum_{\gamma\notin F}|a_\gamma(s)|=0,
\]
which is the uniform-tail property used below.

More precisely, for every compact
\(K\Subset\{\operatorname{Re}s>-\sigma_0\}\), choose one branch \(\delta\)
and put

\[
m_{\delta,K}=\min_{s\in K}|a_\delta(s)|>0.
\]

The strict positivity follows because the exponential branch weight is
nowhere zero.  This number is the uniform lower-bound witness below.

Fix one branch \(\delta\).  C25 injectivity gives
\(g_\gamma g_\delta^{-1}\ne I\) for \(\gamma\ne\delta\).  Divide the trace
of (2), tested against \(\rho_p(g_\delta)^{-1}\), by \(p^2\):

\[
\frac1{p^2}\operatorname{Tr}\!\left(
B_{s,p}\rho_p(g_\delta)^{-1}\right)
=a_\delta(s)+\sum_{\gamma\ne\delta}a_\gamma(s)
\frac{\Theta_p(g_\gamma g_\delta^{-1})}{p^2}.
\tag{3}
\]

Each normalized character in the last sum tends to zero by (1), and its
absolute value is at most one because the Weil matrices are unitary.
Dominated convergence in the uniformly summable branch ledger gives,
uniformly for \(s\in K\),

\[
\frac1{p^2}\operatorname{Tr}\!\left(
B_{s,p}\rho_p(g_\delta)^{-1}\right)\longrightarrow a_\delta(s).
\tag{4}
\]

For all sufficiently large \(p\), the modulus of (4) is at least
\(m_{\delta,K}/2\), uniformly on \(K\).  For \(1\le q\le\infty\),
Schatten Hölder and
\(\|\rho_p(g_\delta)^{-1}\|_{q'}=p^{2/q'}\) imply from (4)

\[
\|B_{s,p}\|_q\gg p^{2/q}.
\]

Boundedness of \(E_p,J_p\) transfers this lower bound to
\(\mathcal L_{s,p}\).  Conversely,

\[
\|K_{s,\gamma}\otimes\rho_p(g_\gamma)\|_q
=p^{2/q}\|K_{s,\gamma}\|_q
\le p^{2/q}\|K_{s,\gamma}\|_1.
\]

Summing the C26 majorant proves the reverse bound.  Thus, locally uniformly
in \(s\),

\[
\boxed{
\|\mathcal L_{s,p}\|_q\asymp p^{2/q},
\qquad1\le q\le\infty.
}
\tag{5}
\]

In particular, C27's \(p^2\) trace-norm factor is the exact growth order,
not merely a proof artifact.

### Step 3 — complete prime-Schatten phase diagram

For complex scalars \(c_p\), set

\[
\mathbb L_s(c)=\bigoplus_{p\ {\rm odd}}c_p\mathcal L_{s,p}.
\]

The direct-sum Schatten formula and (5) give

\[
\boxed{
\mathbb L_s(c)\in\mathcal S_q
\quad\Longleftrightarrow\quad
\sum_{p\ {\rm odd}}p^2|c_p|^q<\infty.
}
\tag{6}
\]

For \(q=\infty\), (5) similarly gives

\[
\boxed{
\mathbb L_s(c)\text{ is compact}
\quad\Longleftrightarrow\quad c_p\to0.
}
\tag{7}
\]

The undamped direct sum is therefore not compact.

Take the Dirichlet weight \(c_p=p^{-z}\).  The series in (6) becomes

\[
\sum_p p^{2-q\operatorname{Re}z}.
\]

It converges exactly when \(q\operatorname{Re}z>3\).  At equality it is
the divergent prime harmonic series.  Hence

\[
\boxed{
\bigoplus_{p\ {\rm odd}}p^{-z}\mathcal L_{s,p}\in\mathcal S_q
\quad\Longleftrightarrow\quad q\operatorname{Re}z>3.
}
\tag{8}
\]

For integer \(m\ge2\), a regularized determinant \(\det_m\) is available
when \(\operatorname{Re}z>3/m\), but it deletes the trace orders below
\(m\).  Thus \(z=2\) gives \(\mathcal S_2\setminus\mathcal S_1\), and
\(z=1\) first permits \(\det_4\).  At \(z=0\) the operator is noncompact,
so no finite-order regularized determinant exists.

### Step 4 — ordinary prime-direct-sum Fredholm theorem

On the fixed Hilbert space

\[
\mathcal H_\oplus
=\bigoplus_{p\ {\rm odd}}
\left(A^2(\Omega)\widehat\otimes\mathbb C^{p^2}\right),
\]

define

\[
\boxed{
\mathfrak L_{s,z}
=\bigoplus_{p\ {\rm odd}}p^{-z}\mathcal L_{s,p}.
}
\tag{9}
\]

By (8), (9) is trace class exactly when
\(\operatorname{Re}z>3\).  The C26 locally uniform branch majorant makes
the sum trace-norm holomorphic in \((s,z)\) on

\[
\operatorname{Re}s>-\sigma_0,
\qquad
\operatorname{Re}z>3.
\]

The ordinary determinant

\[
\boxed{
\mathfrak D(s,z,u)
=\det_{\mathcal H_\oplus}(I-u\mathfrak L_{s,z})
}
\tag{10}
\]

is jointly holomorphic in \((s,z,u)\).  Finite prime-block truncations
converge in trace norm, and continuity of the Fredholm determinant gives the
locally normal, prime-order-independent product

\[
\boxed{
\mathfrak D(s,z,u)
=\prod_{p\ {\rm odd}}
\mathcal D_p(s,u p^{-z}).
}
\tag{11}
\]

This is an ordinary determinant; no \(\det_2\), zeta regularization, or
counterterm is hidden in (10)--(11).

### Step 5 — chronological global trace and arithmetic coefficients

For every \(n\ge1\), block diagonality gives

\[
\operatorname{Tr}\mathfrak L_{s,z}^n
=\sum_{p\ {\rm odd}}p^{-nz}
  \operatorname{Tr}\mathcal L_{s,p}^n.
\]

Substituting the C27 word formula yields

\[
\boxed{
\operatorname{Tr}\mathfrak L_{s,z}^n
=\sum_{w\in\Gamma^n}A_{s,w}
  \sum_{p\ {\rm odd}}p^{-nz}\Theta_p(g_w).
}
\tag{12}
\]

Later returns still multiply on the left inside \(g_w\).  A repetition
\(w^r\) contributes \(p^{-nrz}\Theta_p(g_w^r)\), never
\(p^{-nrz}\Theta_p(g_w)^r\).

If \(D_w=\det(I-g_w)\ne0\), then C27 gives, with a finite singular-prime
correction,

\[
\sum_{p\ {\rm odd}}p^{-nz}\Theta_p(g_w)
=P_{\chi_w}^{\rm odd}(nz)
 +\sum_{\substack{p\mid D_w\\p\ {\rm odd}}}
 p^{-nz}\bigl(\Theta_p(g_w)-\chi_w(p)\bigr).
\tag{13}
\]

For \(\operatorname{Re}\zeta>1\), use the Euler-product logarithm obtained by
continuation from positive real \(\zeta\).  Möbius inversion gives

\[
P_\chi(\zeta)
=\sum_{k\ge1}\frac{\mu(k)}k
  \log L(k\zeta,\chi^k).
\tag{14}
\]

Here \(\chi^k\) denotes the pointwise power, regarded modulo the same
conductor and allowed to be imprimitive.  Since (13) runs only over odd
primes, the exact form used there is

\[
P_\chi^{\rm odd}(\zeta)
=\sum_{k\ge1}\frac{\mu(k)}k\log L(k\zeta,\chi^k)
 -\chi(2)2^{-\zeta}.
\tag{15}
\]

Equations (12)--(15) are the arithmetic gain for every chronological orbit
with \(D_w\ne0\): such an orbit produces genuine quadratic prime-\(L\) data.
Fixed-space words instead retain the singular Gauss/prime-power character
law and are not covered by (13).  The regular word contributions are not one
common quadratic \(L\)-function because \(\chi_w\) and its conductor vary
with \(w\), and generally \(\chi_{w^r}\ne\chi_w^r\).

### Step 6 — the normalized-trace escape collapses to one

The normalized character limit (1) suggests dividing the fixed-prime trace
by \(p^2\).  C25 freeness says every nonempty positive AGY word has
\(g_w\ne I\).  The C27 absolutely summable word trace then gives, for every
fixed \(n\ge1\), locally uniformly for \(s\) in compact subsets of the
source half-plane,

\[
\frac1{p^2}\operatorname{Tr}\mathcal L_{s,p}^n
\longrightarrow0.
\tag{16}
\]

Equation (5) at \(q=\infty\) supplies a \(p\)-uniform operator norm bound,
while (5) at \(q=1\) bounds the normalized trace series.  For a compact
\(K\) in the source half-plane, let

\[
M_K=\sup_{s\in K,p}\|\mathcal L_{s,p}\|_\infty,
\qquad
\sup_{s\in K,p}p^{-2}\|\mathcal L_{s,p}\|_1\le C_{1,K}.
\]

Choose \(r_K<M_K^{-1}\).  On \(|u|\le r_K\), the logarithm
\(\Log_0\mathcal D_p(s,u)\) is the analytic branch fixed by value zero at
\(u=0\), and

\[
\left|p^{-2}\operatorname{Tr}\mathcal L_{s,p}^{\,n}\right|
\le C_{1,K}M_K^{n-1}.
\]

Dominated convergence of the logarithmic series, locally uniformly in
\((s,u)\), therefore gives

\[
\frac1{p^2}\Log_0\mathcal D_p(s,u)\longrightarrow0.
\]

Therefore

\[
\boxed{
\exp\!\left[p^{-2}\Log_0\mathcal D_p(s,u)\right]\longrightarrow1
}
\tag{17}
\]

on that disc.  This is a large-\(p\) limit, not a product over primes.  It
shows that the most canonical tracial normalization retains only identity
holonomy, while the one-sided free AGY monoid has no nonempty identity
loops.

### Step 7 — general marked normalization threshold and C24-P073

Let \(g\) be fixed in one frozen unimodular integral symplectic frame, let
\(\alpha\in\mathbb C\), and put

\[
k_{\mathbb Q}=\dim_{\mathbb Q}\ker(g-I).
\]

Outside finitely many primes,
\(|\Theta_p(g)|=p^{k_{\mathbb Q}/2}\).  Thus the orbit-resolved marked sum

\[
\sum_p p^{-\alpha}\Theta_p(g)
\]

is absolutely convergent exactly when

\[
\boxed{
\operatorname{Re}\alpha>1+\frac{k_{\mathbb Q}}2.
}
\tag{18}
\]

Dimension normalization corresponds to \(\alpha=2\), so a rational fixed
plane of dimension two lies exactly on the harmonic boundary.

The frozen C24 cycle P073 supplies an exact occurrence in the same Rauzy
family.  Its base-trivialized matrix is

\[
g_{073}=
\begin{pmatrix}
1&8&4&4\\
1&13&6&6\\
1&6&4&3\\
1&2&1&2
\end{pmatrix},
\]

with

\[
\det(xI-g_{073})=(x-1)^2(x^2-18x+1).
\]

All \(3\times3\) minors of \(g_{073}-I\) vanish and the gcd of its
\(2\times2\) minors is one.  Therefore the kernel dimension modulo every
prime is exactly two.  In the frozen C24 symplectic frame, quotient columns
\(0,1\) give Thomas's form

\[
Q_{073}=
\begin{pmatrix}1&0\\8&-4\end{pmatrix},
\qquad
\det Q_{073}=-4.
\]

For every odd prime,

\[
\boxed{
\Theta_p(g_{073})
=\left(\frac{-4}{p}\right)
 \left(\frac{-1}{p}\right)p
=p.
}
\tag{19}
\]

Hence its dimension-normalized marked coefficient is \(1/p\), and

\[
\sum_{p\ {\rm odd}}\frac{\Theta_p(g_{073})}{p^2}
=\sum_{p\ {\rm odd}}\frac1p
=\infty.
\tag{20}
\]

Among the 146 frozen C24 eventually-positive cycles, exact rational ranks
give fixed-space counts

\[
k_{\mathbb Q}=0:125,
\qquad
k_{\mathbb Q}=1:20,
\qquad
k_{\mathbb Q}=2:1,
\]

with P073 the unique two-dimensional case.

P073 is an ambient C24 Rauzy control.  It is not asserted to be a C26
positive-prefix induced branch.  Thus (20) proves failure of the full-Rauzy
dimension-normalized marked assembly, while the analogous all-word C26
induced statement remains open.

### Step 8 — raw character product witness

The C26 branch \(\gamma_*\) has

\[
\det(I-g_{\gamma_*})
=3^4\cdot7\cdot11\cdot71\cdot1039
=460097253,
\]

whose squarefree kernel and fundamental discriminant are \(5680213\).
The reduced classes \(2\) and \(3\) have quadratic character values
\(-1\) and \(+1\), respectively.  Dirichlet's theorem gives infinitely many
good primes of both signs.  Therefore the bare character product

\[
\prod_{p\ {\rm odd}}\Theta_p(g_{\gamma_*})
\]

does not converge.  This is a control against treating a character
coefficient as an Euler factor; the valid local factors in (11) tend to one
because the operator itself is damped by \(p^{-z}\).

## Remarks and Interpretation

- C28 yields a canonicality trilemma:
  \[
  \begin{array}{c|c}
  \text{counting-trace direct sum}&\text{noncompact}\\
  \text{normalized-trace limit}&\text{exists but determinant germ is }1\\
  \text{prime-norm damping}&\text{nontrivial Fredholm determinant, but adds }\log p
  \end{array}
  \]
- The exact threshold \(\operatorname{Re}z>3\) reflects both the prime
  harmonic boundary and the \(p^2\) fibre dimension.
- Scaling by \(p^{-2}\) does not give an ordinary determinant: it lies in
  \(\mathcal S_2\setminus\mathcal S_1\).  Switching to \(\det_2\) deletes
  the first marked trace and changes the object.
- A genuine global Weil representation uses local-field oscillator
  representations, an adelic Schwartz space, compatible splittings and
  almost-everywhere reference vectors.  The residue-field prime direct sum
  in (9) is not that restricted tensor product.

## Boundaries and Non-Claims

- The threshold in (8) is sharp for the declared block scaling
  \(p^{-z}\mathcal L_{s,p}\).  It does not classify unrelated cross-prime
  operators with non-block cancellations.
- P073 closes the full C24 Rauzy marked normalization, not the all-word C26
  induced language.
- The quadratic prime-series decomposition is orbit dependent.  It supplies
  no common conductor, automorphic representation, or standard primitive
  Euler factor.
- There is no continuation to \(z=0\), functional equation, gamma factor,
  Riemann--von Mangoldt law, \(\xi\)-divisor equality, self-adjoint
  Hilbert--Pólya generator, or RH statement.
- Route B is not authorized.

## Open Risks

- A two-sided based/path-groupoid dynamics could contain nonempty
  identity-holonomy loops and make the regular trace nontrivial, but it needs
  a new trace-class theorem.
- A genuine \(p\)-adic oscillator plus spherical test function and
  automorphic/theta kernel would be a new architecture, not a completion of
  the finite residue-field direct sum by notation.
- The C26 induced language could conceivably exclude every fixed-space
  dimension-two word.  Proving that theorem would clarify the marked
  normalized ledger but would not remove the direct-sum \(p^2\) threshold or
  the external prime clock.
