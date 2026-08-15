# Proof Package

## Status and frozen scope

- Candidate: `cat_prime_shell_multiplicity_obstruction_v1`.
- Matrix:

  $$
  A=\begin{pmatrix}2&1\\1&1\end{pmatrix}.
  $$

- Proof status: **PROVABLE AS STATED** within the qualifications below.
- Paper status sought: `GO_SCOPED_NEGATIVE_NOTE_LOW_NOVELTY`.
- Route status: `A0_FAIL_GLOBAL_NORMALIZATION_ONLY / ROUTE_B_NOT_OPENED`.

The finite-field orbit classification is classical and is re-derived here so
that the product semantics and the negative conclusion are checkable from one
source-locked argument.  This package does not claim a new classification or
a new dynamical-zeta theorem.

## Definitions and assumptions

For a rational prime $p$, write

$$
V_p=\mathbb F_p^2\setminus\{0\}
   \simeq \mathbb T^2[p]\setminus\{0\}.
$$

Let $\Gamma_p$ be the set of primitive $A$-orbits in $V_p$, let
$|\gamma|$ be the least period of $\gamma$, and put
$m_p=|\Gamma_p|$.  The characteristic polynomial of $A$ is

$$
f(X)=X^2-3X+1,
\qquad \operatorname{disc}(f)=5.
$$

For $p\ne5$, let $\tau_p$ denote the order of $A$ in
$\mathrm{GL}_2(\mathbb F_p)$.  The Legendre symbol $(5/p)$ is used only for
odd $p\ne5$.

Two formal local variables must remain separate:

- the point-potential/raw-return product uses the additive point observable
  $L(x)=\log p$ on $V_p$ and therefore accumulates $|\gamma|\log p$ on a
  primitive orbit;
- the orbit-label product assigns $\log p$ once to each primitive orbit,
  independently of $|\gamma|$.

The scalar-weight obstruction concerns finite products

$$
\prod_{\gamma\in\Gamma_p}(1-w_\gamma z)^{-1}
$$

with fixed, nonzero, scalar coefficients $w_\gamma$ that do not depend on
the local variable $z$.  This includes the ordinary orbit weights
$w_\gamma=\exp(S_\gamma\phi)$ of a finite scalar/Hölder potential when they
are placed in this pure scalar orbit-label product.  It does not cover
matrix-valued weights, numerator cancellations, alternating or
cohomological determinants, or weights allowed to vary with $z$.

## Main theorem

**Theorem (prime-shell multiplicity and scalar Euler-factor obstruction).**
For the frozen matrix $A$ above, the following statements hold.

1. At $p=2$, $V_2$ is one orbit of length three, so $m_2=1$.
2. If $p$ is odd, $p\ne5$, and $(5/p)=1$, then every point of $V_p$ has
   exact period $\tau_p$, where $\tau_p\mid p-1$.  With
   $h_p=(p-1)/\tau_p$,

   $$
   m_p=\frac{p^2-1}{\tau_p}=(p+1)h_p\ge p+1.
   $$

   More precisely, the two eigenlines contain $2h_p$ cycles in total and
   their complement contains $(p-1)h_p$ cycles.
3. If $p$ is odd and $(5/p)=-1$, then every point of $V_p$ has exact period
   $\tau_p$, where $\tau_p\mid p+1$.  With
   $h_p=(p+1)/\tau_p$,

   $$
   m_p=\frac{p^2-1}{\tau_p}=(p-1)h_p\ge p-1.
   $$
4. At $p=5$, four points have exact period two and twenty points have exact
   period ten.  They form two cycles of each length, so $m_5=4$.
5. Consequently $p=2$ is the unique prime with $m_p=1$, and
   $m_p\ge p-1$ for every odd prime $p$.
6. The point-potential/raw-return factor is

   $$
   Z_{\mathrm{raw},p}(s)
   =\prod_{\gamma\in\Gamma_p}
      (1-p^{-s|\gamma|})^{-1}.
   $$

   Thus it equals $(1-p^{-s\tau_p})^{-m_p}$ for $p\ne5$, whereas

   $$
   Z_{\mathrm{raw},5}(s)
   =(1-5^{-2s})^{-2}(1-5^{-10s})^{-2}.
   $$

   The distinct unweighted orbit-label factor is

   $$
   Z_{\mathrm{lab},p}(s)
   =\prod_{\gamma\in\Gamma_p}(1-p^{-s})^{-1}
   =(1-p^{-s})^{-m_p},
   $$

   and its coefficient at repetition $r$ in the logarithm is exactly
   $m_p/r$.
7. For every odd $p$, no pure scalar product with fixed nonzero coefficients
   $w_\gamma$ can equal one Riemann local factor:

   $$
   \prod_{\gamma\in\Gamma_p}(1-w_\gamma z)^{-1}
   \ne (1-z)^{-1}.
   $$

   If zero weights are admitted, equality requires precisely the multiset
   $\{1,0,\ldots,0\}$.  In particular, a finite scalar/Hölder potential has
   nonzero exponential orbit weights and cannot perform this collapse.
8. The fractional shell product

   $$
   \prod_{\gamma\in\Gamma_p}
   (1-p^{-s})^{-|\gamma|/(p^2-1)}
   =(1-p^{-s})^{-1}
   $$

   is an exact repair, but it is a global normalized-counting identity, not
   an ordinary scalar-potential weight.  The same identity holds for every
   composite exact-order shell after replacing $p^2-1$ by its shell
   cardinality, so the repair is not prime-specific.
9. For the global unweighted label product, its positive logarithmic series
   diverges for real $1<s\le2$; its logarithmic series is not absolutely
   convergent for complex $s$ with $1<\operatorname{Re}s\le2$; and it is
   absolutely convergent for $\operatorname{Re}s>3$.  No assertion is made
   in the gap $2<\operatorname{Re}s\le3$ beyond these bounds, and no exact
   abscissa or analytic continuation is claimed.

## Dependency map

| Claim | Dependencies | Nature |
|---|---|---|
| split classification | diagonalization of $f$ over $\mathbb F_p$ | exact algebra |
| inert classification | norm-one root in $\mathbb F_{p^2}$ | exact algebra |
| binary and ramified boundaries | Cayley--Hamilton and a rank-one Jordan calculation | exact algebra |
| two product formulas | primitive-orbit repetition ledger | formal identity |
| scalar no-go | polynomial degree and power sums | formal identity |
| fractional repair | partition of a finite shell into cycles | finite counting tautology |
| global safe bounds | $p-1\le m_p\le p^2-1$ and Euler's prime harmonic divergence | classical analysis |

No finite audit is a dependency of the theorem.  The inherited five-prime
ledger is a later falsification control only.

## Proof

### Step 1: split primes

Let $p$ be odd, $p\ne5$, and $(5/p)=1$.  The polynomial $f$ has distinct
roots $\lambda,\lambda^{-1}$ in $\mathbb F_p$, so $A$ is conjugate over
$\mathbb F_p$ to $\operatorname{diag}(\lambda,\lambda^{-1})$.  Set
$\tau_p=\operatorname{ord}(\lambda)$.  The two diagonal entries have the
same multiplicative order, hence this is also the order of $A$.

For a nonzero vector $(x,y)$, the equality

$$
A^k(x,y)=(x,y)
$$

forces $\lambda^k=1$ on every nonzero coordinate; conversely that condition
fixes the vector.  Since at least one coordinate is nonzero and both
$\lambda$ and $\lambda^{-1}$ have order $\tau_p$, every nonzero vector has
least period $\tau_p$.  As $\lambda\in\mathbb F_p^\times$,
$\tau_p\mid p-1$.

The $p^2-1$ nonzero vectors therefore partition into

$$
m_p=\frac{p^2-1}{\tau_p}=(p+1)\frac{p-1}{\tau_p}
$$

cycles.  Each eigenline has $p-1$ nonzero points, hence the two eigenlines
give $2(p-1)/\tau_p=2h_p$ cycles.  The remaining $(p-1)^2$ points give
$(p-1)^2/\tau_p=(p-1)h_p$ cycles.  Since $h_p$ is a positive integer,
$m_p\ge p+1$.

### Step 2: inert primes

Let $(5/p)=-1$.  The polynomial $f$ is irreducible over $\mathbb F_p$.
Identify the two-dimensional $\mathbb F_p$-space with $\mathbb F_{p^2}$ so
that $A$ acts by multiplication by a root $\lambda$ of $f$.  The Frobenius
conjugate of $\lambda$ is the other root, hence

$$
\lambda^p=\lambda^{-1}
\quad\text{and}\quad
\lambda^{p+1}=1.
$$

Thus $\tau_p=\operatorname{ord}(\lambda)$ divides $p+1$.  For nonzero
$v\in\mathbb F_{p^2}$,

$$
A^k v=v
\iff (\lambda^k-1)v=0
\iff \lambda^k=1.
$$

Every nonzero vector has exact period $\tau_p$, and consequently

$$
m_p=\frac{p^2-1}{\tau_p}
=(p-1)\frac{p+1}{\tau_p}=(p-1)h_p\ge p-1.
$$

### Step 3: the binary boundary

Modulo two, $f(X)=X^2+X+1$ is irreducible.  Cayley--Hamilton gives
$A^2+A+I=0$, hence $A^3=I$.  Since $1$ is not a root of $f$, there is no
nonzero fixed vector.  All three nonzero vectors therefore form one
three-cycle.  Hence $m_2=1$.

### Step 4: the ramified boundary

Modulo five, set $N=A+I$.  Direct multiplication gives

$$
A=-I+N,\qquad N^2=0,\qquad \operatorname{rank}N=1.
$$

The kernel of $N$ has five elements.  On its four nonzero elements,
$A=-I$, so each point has exact period two.  These points form two cycles.

For all $k\ge1$, the nilpotent binomial formula gives

$$
A^k=(-1)^k(I-kN).
$$

Let $v\notin\ker N$.  If odd $k$ fixed $v$, applying $N$ to
$-(I-kN)v=v$ would give $-Nv=Nv$, hence $Nv=0$, a contradiction in
characteristic five.  For even $k$, the equality $A^kv=v$ is equivalent to
$kNv=0$, hence to $5\mid k$.  The least positive even multiple of five is
ten.  All twenty vectors outside $\ker N$ therefore have exact period ten
and form two cycles.  Thus $m_5=2+2=4=5-1$.

Steps 1--4 prove the all-prime classification, the odd-prime lower bound,
and the uniqueness of $m_p=1$.

### Step 5: primitive-orbit expansion of the raw-return product

On $V_p$, $L(x)=\log p$.  A primitive orbit $\gamma$ of length
$\ell=|\gamma|$ contributes fixed points to the $n$th return sum exactly
when $n=r\ell$.  It then contributes its $\ell$ points, and every one has
$S_{r\ell}L=r\ell\log p$.  Its total logarithmic contribution is

$$
\sum_{r\ge1}\frac{\ell}{r\ell}p^{-sr\ell}
=\sum_{r\ge1}\frac{p^{-sr\ell}}r
=-\log(1-p^{-s\ell}).
$$

Multiplying over primitive orbits proves the raw-return formula.  The
uniform-period split, inert, and binary cases give
$(1-p^{-s\tau_p})^{-m_p}$; the two length-two and two length-ten cycles at
$p=5$ give the stated mixed factor.

The orbit-label construction instead places the same variable $p^{-s}$ on
each primitive orbit.  Therefore

$$
\log Z_{\mathrm{lab},p}(s)
=m_p\sum_{r\ge1}\frac{p^{-rs}}r,
$$

so natural repetition preserves the excess multiplicity $m_p$ at every
repeat and gives coefficient $m_p/r$.

### Step 6: fixed scalar weights cannot collapse the label factor

Put $z=p^{-s}$ and suppose

$$
\prod_{\gamma\in\Gamma_p}(1-w_\gamma z)^{-1}
=(1-z)^{-1}
$$

as a formal identity.  Clearing denominators gives

$$
\prod_{\gamma\in\Gamma_p}(1-w_\gamma z)=1-z.
$$

If every $w_\gamma$ is nonzero, the polynomial on the left has degree
$m_p$ and nonzero leading coefficient.  It can equal the degree-one
polynomial on the right only if $m_p=1$.  Every odd prime has $m_p\ge2$, so
the desired equality is impossible there.

If zero coefficients are admitted, remove the zero factors.  Unique
factorization over $\mathbb C[z]$ then shows that exactly one remaining
coefficient is $1$; equivalently, the multiset is
$\{1,0,\ldots,0\}$.  Such zeros discard all but one orbit.  Exponential
weights of finite scalar or Hölder potentials never vanish.

The logarithmic form gives the equivalent conditions

$$
\sum_{\gamma\in\Gamma_p}w_\gamma^r=1
\qquad(r\ge1).
$$

In particular, $w_\gamma=1/m_p$ fixes the $r=1$ condition but gives
$m_p^{1-r}$ at repetition $r$, so it fails for every $r\ge2$ when
$m_p>1$.

### Step 7: exact fractional normalization and its tautological extension

The primitive cycles partition $V_p$, hence

$$
\sum_{\gamma\in\Gamma_p}|\gamma|=|V_p|=p^2-1.
$$

Raising the common label factor to fractional orbit-mass exponents therefore
gives

$$
\prod_{\gamma\in\Gamma_p}
(1-p^{-s})^{-|\gamma|/(p^2-1)}
=(1-p^{-s})^{-1}.
$$

The exponent depends on the complete shell size and is applied outside the
ordinary scalar factor.  It is normalized counting measure on a finite
permutation, not a local multiplicative potential repair.

For any integer $q\ge2$, let $E_q\subset\mathbb T^2$ be the exact
additive-order-$q$ shell.  Since $A$ is an integral automorphism, it
permutes $E_q$.  Its cycles again partition the shell, whose size is the
Jordan totient

$$
|E_q|=J_2(q)
=q^2\prod_{\substack{\ell\mid q\\ \ell\ \mathrm{prime}}}
(1-\ell^{-2}).
$$

Consequently the same normalization, with $|\gamma|/J_2(q)$, gives
$(1-q^{-s})^{-1}$ for composite $q$ as well.  This proves that the mechanism
has no intrinsic prime specificity.

### Step 8: safe global convergence bounds

Let $s=\sigma+it$.  For $\sigma>3$, use
$m_p\le|V_p|=p^2-1$ and, for all sufficiently large $p$,

$$
\sum_{r\ge1}\frac{|p^{-rs}|}{r}
=-\log(1-p^{-\sigma})\le C_\sigma p^{-\sigma}.
$$

It follows that the absolute logarithmic series is bounded by a constant
times

$$
\sum_p p^{2-\sigma}\le\sum_{n\ge2}n^{2-\sigma}<\infty.
$$

Thus the label product is absolutely convergent for $\sigma>3$.

For $1<\sigma\le2$, the $r=1$ terms and the odd-prime bound give

$$
\sum_p m_pp^{-\sigma}
\ge\sum_{p\ \mathrm{odd}}(p-1)p^{-\sigma}.
$$

For $p\ge2$, the right-hand summand is at least a fixed positive multiple of
$p^{1-\sigma}$, which is at least a fixed positive multiple of $1/p$ when
$\sigma\le2$.  Euler's divergence of $\sum_p1/p$ proves divergence.  For
real $s$ all logarithmic terms are positive, so the logarithm diverges; for
complex $s$ the same estimate proves failure of absolute convergence.  The
argument intentionally says nothing sharp in $2<\sigma\le3$.

This completes the proof.  $\square$

## Exact inherited audit ledger (control only)

The later registered audit, if separately authorized, is restricted to the
following Paper-8-seen records.

| $p$ | type | point-period profile | orbit ledger | $m_p$ | raw-return factor | fractional orbit exponents |
|---:|---|---|---|---:|---|---|
| 2 | inert/binary | $3:3$ | one $3$-cycle | 1 | $(1-2^{-3s})^{-1}$ | $1$ |
| 3 | inert | $4:8$ | two $4$-cycles | 2 | $(1-3^{-4s})^{-2}$ | $1/2$ each |
| 5 | ramified | $2:4,\ 10:20$ | two $2$-cycles, two $10$-cycles | 4 | $(1-5^{-2s})^{-2}(1-5^{-10s})^{-2}$ | $1/12$ on each $2$-cycle; $5/12$ on each $10$-cycle |
| 7 | inert | $8:48$ | six $8$-cycles | 6 | $(1-7^{-8s})^{-6}$ | $1/6$ each |
| 11 | split | $5:120$ | twenty-four $5$-cycles; $4$ eigenline and $20$ off-line | 24 | $(1-11^{-5s})^{-24}$ | $1/24$ each |

This table is development-seen.  Reproduction cannot prove the all-prime
theorem or any convergence statement.

## Centralizer escape boundary (Paper 10 only)

The scalar theorem above does not close quotient constructions.  In the
inert case the finite-field centralizer identifies with
$\mathbb F_{p^2}^{\times}$ and acts transitively on the nonzero shell.  In
the split case the diagonal centralizer has three natural strata: the two
nonzero eigenlines and their complement.  At $p=5$, the Jordan structure
separates the nonzero kernel from its complement.  These symmetries are a
real escape route, not a mechanism disproved here.

Any quotient proposal would depend on a $p$-shell centralizer and would still
receive the prime label from the externally specified additive-order shell.
Whether such a quotient supplies a canonical, dynamically meaningful local
factor is reserved for Paper 10.  Paper 9 neither develops nor rules it out.

## Mandatory nonclaims and failure modes

- The finite-field classification, rational-lattice orbit theory, and
  finite-permutation Euler products are not claimed as new.
- The degree obstruction applies only to pure scalar denominators with
  fixed nonzero coefficients independent of the local variable.
- Matrix-valued weights, vector bundles, transfer/Fredholm determinants,
  cohomological superdeterminants, and numerator or alternating cancellation
  are outside the theorem.
- The result does not prove that no canonical selector or centralizer
  quotient can exist.
- The fractional normalization is an exact identity; the negative conclusion
  is that it is shell-global, tautological, and not prime-specific.
- Selecting one orbit per prime produces one factor but breaks the frozen
  all-orbit construction and discards $m_p-1$ orbits.  No impossibility
  theorem for enriched selectors is asserted.
- There is no claim of an exact abscissa, conditional convergence,
  meromorphic continuation, a prime/zero correspondence, quantization, or
  Route B.
- If an independent audit finds a different $p=5$ cycle split, a nonbinary
  prime with $m_p=1$, a violation of the odd-prime lower bound, or a failure
  of either formal product identity, the source lock must be rejected rather
  than repaired after execution.

## Proof audit checklist

- [x] All assumptions and all local variables are explicit.
- [x] Split, inert, binary, and ramified cases are exhaustive.
- [x] No maximal-order assumption for $\tau_p$ is used.
- [x] Point-potential and orbit-label products are derived separately.
- [x] Repetition coefficients are checked for every $r$.
- [x] The scalar theorem's denominator-only and nonzero-weight scope is
  explicit.
- [x] The exact fractional repair and its composite-shell extension are
  admitted.
- [x] The convergence gap $2<\operatorname{Re}s\le3$ remains unclaimed.
- [x] The centralizer quotient remains an explicit outside-theorem escape.
- [ ] A fresh independent reviewer is bound to the final source-lock hash.
