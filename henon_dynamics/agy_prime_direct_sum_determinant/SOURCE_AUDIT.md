# HCS-C28 source and claim audit

## 1. Audit purpose

This file records which parts of C28 are inherited, which parts are new
proofs, and which exact computations are controls.  It also freezes the
terminology needed to prevent a prime direct sum of residue-field fibres from
being mislabeled as an adelic Weil representation.

## 2. Frozen local artifacts

| Stage | File | SHA-256 | C28 use |
|---|---|---|---|
| C24 | `rauzy_metaplectic_obstruction/results/c24_certificate.json` | `4b4fe5943262137eeeb3eda4de887725a0663402a1f39f8cc43e089bcc91e778` | P073 and the 146-cycle full-Rauzy control census only |
| C25 | `agy_metaplectic_transfer_obstruction/results/c25_certificate.json` | `a35cee22714abbb9dc9aadcc165720d1ff77aff3b7f29071f53a1b451760bd12` | fixed-start matrix decoder, fixed-fibre symplectic matrices, and free positive first-return monoid |
| C26 | `agy_holomorphic_slice_obstruction/results/c26_certificate.json` | `1c0289b9b47e65e0603ea001be7cce263aea13d58c66e4609eac88edf8f7ce4a` | common Bergman domain, trace-norm branch sum, nonzero weights, constants/evaluation, and scalar word atom |
| C27 | `agy_finite_weil_determinant/results/c27_certificate.json` | `8676d17c5a0e4444dded88b5a76f5ea1fa974275528aa0a51400730759d8b029` | full finite Weil fibres, fixed-prime trace-class family, Thomas character, and word trace |

The C28 producer and independent checker verify these hashes before using
their contents.  The independent checker imports no producer module.

## 3. Exact inherited theorems

### 3.1 C25 matrix statement actually used

C25 Theorem E.1 is stronger than a bounded collision check.  For a fixed
starting labeled Rauzy permutation, the full nonnegative integral Rauzy
matrix determines the complete directed edge word: the first edge is the
unique winner/loser choice whose winner row dominates the loser row, and
row subtraction peels that edge.  The total entry sum strictly decreases,
so the decoder terminates at the identity.

C25 Corollary E.2 gives the application used here:

- distinct AGY first-return paths based at the frozen state have distinct
  full matrices;
- because the crossing form is nondegenerate in the present
  \(\mathcal H(2)\) model, no relative-homology quotient destroys that
  distinction;
- concatenations of first-return words decode uniquely and split at visits
  to the base state.

Thus the positive first-return matrix monoid is free.  C28 uses precisely

\[
g_\gamma g_\delta^{-1}\ne I\quad(\gamma\ne\delta),
\qquad
g_w\ne I\quad(w\ne\varnothing).
\]

No claim is made that characteristic polynomials, spectra, conjugacy
classes, or finite-Weil characters are injective.  C24 and C27 explicitly
show that they are not.

### 3.2 C26 analytic statement actually used

For every compact \(K\) in the C26 source half-plane,

\[
\sup_{s\in K}\sum_\gamma\|K_{s,\gamma}\|_1<\infty.
\]

Here "locally uniform branch sum" includes uniform tails: for every
\(\varepsilon>0\), a finite \(F\subset\Gamma\) satisfies
\[
\sup_{s\in K}\sum_{\gamma\notin F}\|K_{s,\gamma}\|_1<\varepsilon.
\]

The common Bergman space contains bounded constant fibre slices and has a
bounded interior evaluation.  At a fixed real interior point \(x_0\),

\[
a_\gamma(s)=w_{s,\gamma}(x_0)
\]

is holomorphic, nowhere zero, and uniformly \(\ell^1\) on compact
\(s\)-sets, including the analogous uniform finite-branch tail.  For each
fixed word length, the scalar word atoms likewise have uniform finite-word
tails on compact \(s\)-sets.  The scalar word trace is

\[
A_{s,w}
=\frac{\lambda_w^{-(s+1)}}{\chi_w'(\lambda_w)}.
\]

C28 does not reopen the construction of \(\Omega\) or the scalar trace
formula; it records them as named analytic inputs.

### 3.3 C27 finite-Weil statement actually used

For an odd prime, the full \(p^2\)-dimensional genuine finite Weil
representation is used in the correct source symplectic frame.  Its
character satisfies

\[
|\Theta_p(h)|^2=|\ker(h-I)|.
\]

When \(\det(I-h)\ne0\), all but finitely many primes are regular and

\[
\Theta_p(h)=\left(\frac{\det(I-h)}p\right).
\]

The fixed-prime operator is trace class, and a chronological word contributes

\[
\Theta_p(g_w)A_{s,w}.
\]

Repetitions use \(\Theta_p(g_w^r)\).  C28 never replaces this value by
\(\Theta_p(g_w)^r\).

## 4. New C28 proof boundary

The following statements are new deductions from the frozen inputs, not
fields copied from a finite certificate:

1. eventual rank stability gives
   \(p^{-2}|\Theta_p(h)|=p^{-r(h)/2}\) for a fixed integral \(h\);
2. normalized characters converge pointwise to the regular character;
3. the constant/evaluation compression and C25 injectivity give the sharp
   local lower Schatten bound;
4. the direct-sum Schatten criterion is an `if and only if` statement;
5. the ordinary prime-graded Fredholm region is exactly
   \(\operatorname{Re}z>3\);
6. normalized positive-AGY moments vanish and the normalized determinant
   germ tends to one.

The finite certificate verifies the algebraic sentinels and theorem
parameters.  It is not substituted for these operator-theoretic proofs.

## 5. Uniformity and limit-order audit

The lower-bound proof fixes one branch \(\delta\) and uses

\[
\tau_p\!\left(B_{s,p}\rho_p(g_\delta)^{-1}\right)
=a_\delta(s)
+\sum_{\gamma\ne\delta}a_\gamma(s)
  p^{-2}\Theta_p(g_\gamma g_\delta^{-1}).
\]

For a compact \(K\), the off-diagonal sum converges to zero uniformly in
\(s\) by a finite-head/uniform-tail argument:

1. choose a finite branch set whose coefficient tail is uniformly small on
   \(K\);
2. use pointwise character convergence on the finite head;
3. bound every normalized character by one on the tail.

Since \(a_\delta\) is nowhere zero,

\[
m_{\delta,K}=\min_{s\in K}|a_\delta(s)|>0.
\]

This supplies one prime threshold and one positive lower constant for the
whole compact set.  No exchange of an uncontrolled prime limit with a
countable branch sum occurs.

The normalized determinant statement is written only as

\[
\exp\!\left[p^{-2}\operatorname{Log}_0\mathcal D_p(s,u)\right]
\longrightarrow1,
\]

where \(\operatorname{Log}_0\) is fixed by value zero at \(u=0\).  For a
compact \(K\), choose

\[
M_K=\sup_{s\in K,p}\|\mathcal L_{s,p}\|<\infty
\]

and any disc \(|u|<r_K<M_K^{-1}\).  This is the common compact-uniform
disc on which the Fredholm logarithm is justified.  No global fractional
power or full-plane convergence is claimed.

## 6. Arithmetic formula audit

Quadratic \(L\)-data are used only for a word with

\[
D_w=\det(I-g_w)\ne0.
\]

Let \(\varepsilon_w\) be the corresponding quadratic Kronecker character.
This notation is distinct from the scalar characteristic polynomial
\(\chi_w\) in the word atom.  With

\[
P_\chi(\zeta)=\sum_p\chi(p)p^{-\zeta},
\]

the odd-prime version is

\[
P_\chi^{\mathrm{odd}}(\zeta)
=P_\chi(\zeta)-\chi(2)2^{-\zeta}.
\]

The C28 word sum uses \(P_{\varepsilon_w}^{\mathrm{odd}}\) and equals that
odd prime series plus finitely many corrections
at the odd primes dividing \(D_w\).  For \(\operatorname{Re}\zeta>1\),
the Euler logarithm uses the branch determined by its absolutely convergent
series at infinity, and

\[
P_\chi(\zeta)
=\sum_{k\ge1}\frac{\mu(k)}k
 \operatorname{Log}L(k\zeta,\chi^k).
\]

Here \(\chi^k\) is the pointwise power and may be imprimitive.  No
continuation of the prime series or choice across zeros of \(L\) is used.

For a complex marked exponent \(\alpha\), the absolute convergence
criterion is stated with \(\operatorname{Re}\alpha\):

\[
\operatorname{Re}\alpha>1+\frac12\dim_{\mathbb Q}\ker(g-I).
\]

## 7. C24-P073 scope passport

P073 is read from the frozen C24 eventually-positive **full labeled Rauzy**
ledger.  Its exact facts are:

- primitive directed labeled cycle;
- all cyclic phases eventually positive;
- characteristic polynomial
  \((x-1)^2(x^2-18x+1)\);
- rank \(g-I=2\) over every finite field, certified by zero
  \(3\times3\) minors and gcd one among \(2\times2\) minors;
- Thomas quotient determinant \(-4\) in the C24 symplectic frame;
- in the frozen C24 frame,
  \(\Theta_{p,\mathrm{C24}}(g)=p\) for every odd prime.

Therefore P073 proves

\[
\texttt{FULL\_C24\_RAUZY\_DIMENSION\_NORMALIZED\_MARKED\_ASSEMBLY\_FAILS}.
\]

It does not prove that the C26 induced language contains a fixed-plane word.
Every occurrence in the paper and theorem package calls P073 a C24 control,
never a C26 branch.  The C26 all-word fixed-space gate remains open.

## 8. Terminology audit

### Authorized

- finite-Weil prime fibre;
- prime-weighted Hilbert direct sum;
- prime-graded Dirichlet--Fredholm determinant;
- quadratic prime series with orbit-dependent character;
- normalized-character regular-trace limit.

### Not authorized

- adelic Weil representation;
- automorphic \(L\)-function;
- common quadratic conductor;
- same-clock intrinsic prime law;
- self-adjoint Hilbert--P\'olya operator;
- \(\xi\)-divisor or Riemann-zero match.

A genuine adelic Weil representation is constructed from local-field
oscillator representations in a restricted tensor product with compatible
global additive characters, splittings, measures, and almost-everywhere
reference vectors.  C28's residue-field direct sum is a different object.

## 9. Primary external sources and claim mapping

| Source | Verified identifier | Claim used |
|---|---|---|
| Avila--Gou\"ezel--Yoccoz | DOI `10.1007/s10240-006-0001-5` | AGY induced section and exponential-tail context |
| Thomas | DOI `10.1112/jlms/jdm098`; arXiv `math/0610644` | exact finite/local Weil character formula |
| Gurevich--Hadani | DOI `10.4310/JSG.2009.v7.n4.a4`; arXiv `0705.4556` | canonical finite-field Weil representation |
| Simon | DOI `10.1090/surv/120` | Schatten ideals and Fredholm determinants |
| Britz et al. | arXiv `2007.12834` | higher regularized determinants and their counterterms |
| Apostol | DOI `10.1007/978-1-4757-5579-4` | prime harmonic divergence, Dirichlet characters, Euler products |
| Weil | DOI `10.1007/BF02391012` | local/global oscillator and Weil-representation background |

Bibliography entries are included only when cited in the paper.  No source is
used to support a claim stronger than the statement mapped above.

## 10. Final non-claims

C28 proves an exact prime-Schatten phase diagram and an ordinary determinant
after prime damping.  It proves no analytic continuation toward \(z=0\),
functional equation, gamma factor, automorphic factorization, prime-orbit
theorem, self-adjoint generator, Riemann-zero correspondence, or Riemann
hypothesis statement.  Route B is not invoked.
