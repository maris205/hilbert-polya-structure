# Research Question

## Frozen identity

- Candidate ID: `cat_prime_shell_multiplicity_obstruction_v1`.
- Safe title: **A Multiplicity Audit for Prime-Torsion Euler Products of
  the Cat Map**.
- Date and literature cutoff: **2026-08-14 UTC**.
- Intended paper type: scoped negative mathematical note.
- Intended terminal assessment:
  `GO_SCOPED_NEGATIVE_NOTE_LOW_NOVELTY`.
- Route decision:
  `A0_FAIL_GLOBAL_NORMALIZATION_ONLY / ROUTE_B_NOT_OPENED`.

The symplectic map is frozen as

$$
A=\begin{pmatrix}2&1\\1&1\end{pmatrix}
\in \mathrm{SL}_2(\mathbb Z)=\mathrm{Sp}_2(\mathbb Z),
\qquad
T_A(x)=Ax\pmod{\mathbb Z^2}
$$

on $\mathbb T^2=\mathbb R^2/\mathbb Z^2$.  No matrix, shell, potential,
normalization, or orbit selector may change after source lock.

## Prime shells and multiplicity

For each rational prime $p$, let

$$
V_p=\mathbb T^2[p]\setminus\{0\}
\simeq \mathbb F_p^2\setminus\{0\}.
$$

Every point of $V_p$ has exact additive order $p$.  Let $\Gamma_p$ be the
set of primitive $A$-orbits in $V_p$, let $|\gamma|$ be the least dynamical
period of an orbit $\gamma\in\Gamma_p$, and define

$$
m_p=|\Gamma_p|.
$$

The first question is exact and local:

> How many primitive dynamical orbits occur inside one additive-order-$p$
> shell, and can any unweighted ordinary orbit product assign exactly one
> Euler factor to that shell?

The target classification uses the characteristic polynomial

$$
\chi_A(X)=X^2-3X+1,
\qquad \operatorname{disc}(\chi_A)=5.
$$

It must include all three odd-prime cases and the binary exception:

1. $p=2$: $V_2$ is one orbit of length $3$, so $m_2=1$.
2. Odd split primes $p\ne5$, with $(5/p)=1$: if
   $\tau_p=\operatorname{ord}(A\bmod p)$ and
   $h_p=(p-1)/\tau_p$, then
   $m_p=(p+1)h_p\ge p+1$.
3. Odd inert primes, with $(5/p)=-1$: if
   $h_p=(p+1)/\tau_p$, then
   $m_p=(p-1)h_p\ge p-1$.
4. The ramified prime $p=5$: four nonzero points have period $2$ and
   twenty have period $10$, giving two cycles of each length and $m_5=4$.

Thus $p=2$ must be proved to be the unique prime with $m_p=1$, and the
uniform bound frozen for the note is

$$
m_p\ge p-1\qquad\text{for every odd prime }p.
$$

No maximal-order conjecture for $\tau_p$ is assumed.

## Two products that must not be conflated

Let $L(x)=\log\operatorname{ord}(x)$ on torus torsion.  On $V_p$ it is the
constant $\log p$.  There are two different constructions.

### 1. Point-potential / raw-return product

The genuine return-time construction uses Birkhoff sums of the point label:

$$
Z_{\mathrm{raw},p}(s)
=\exp\!\left(
\sum_{n\ge1}\frac1n
\sum_{x\in V_p\cap\operatorname{Fix}(A^n)}
e^{-sS_nL(x)}
\right)
=\prod_{\gamma\in\Gamma_p}
\left(1-p^{-s|\gamma|}\right)^{-1}.
$$

This product retains both the dynamical return length and shell
multiplicity.  For $p\ne5$ it is

$$
Z_{\mathrm{raw},p}(s)
=\left(1-p^{-s\tau_p}\right)^{-m_p},
$$

while at $p=5$ it is

$$
Z_{\mathrm{raw},5}(s)
=\left(1-5^{-2s}\right)^{-2}
 \left(1-5^{-10s}\right)^{-2}.
$$

It is not a local Riemann factor.

### 2. Orbit-label product

If the global orbit label $\log p$ is assigned once to every primitive
orbit, independently of $|\gamma|$, the distinct formal construction is

$$
Z_{\mathrm{lab},p}(s)
=\prod_{\gamma\in\Gamma_p}
\left(1-p^{-s}\right)^{-1}
=\left(1-p^{-s}\right)^{-m_p}.
$$

Its logarithm is

$$
\log Z_{\mathrm{lab},p}(s)
=\sum_{r\ge1}\frac{m_p}{r}p^{-rs}.
$$

The frozen multiplicity question is whether a natural local or scalar
potential can turn the coefficient $m_p/r$ into $1/r$ for every repeat,
without discarding or globally renormalizing the shell.

## Repair mechanisms to audit

The note will distinguish four operations.

1. **Ordinary nonzero scalar weights.**  Test pure denominator products
   $\prod_{\gamma\in\Gamma_p}(1-w_\gamma p^{-s})^{-1}$ with every
   $w_\gamma\ne0$, fixed independently of the local variable $p^{-s}$.
   Finite scalar or Hölder potentials give nonzero exponential orbit weights
   and are within this test when used in this ordinary scalar form.  Matrix
   weights, numerator/alternating cancellation, and Fredholm or
   cohomological determinants are not within it.
2. **Naive equal weights.**  The choice $w_\gamma=1/m_p$ fixes only the
   first logarithmic coefficient and must fail at repetitions $r\ge2$.
3. **Fractional shell normalization.**  The formal product

   $$
   \prod_{\gamma\in\Gamma_p}
   (1-p^{-s})^{-|\gamma|/(p^2-1)}
   $$

   gives one Euler factor because
   $\sum_{\gamma\in\Gamma_p}|\gamma|=p^2-1$.  This is an admitted exact
   identity, but it uses complete-shell cardinality and fractional global
   exponents.  The same construction works on a composite-order shell after
   replacing $p^2-1$ by its total cardinality, so it has no prime
   specificity.
4. **One-orbit selection.**  Keeping one $\gamma\in\Gamma_p$ also gives one
   factor, but introduces an additional global selector and discards the
   other orbits.  No canonical selector is present in the frozen system.

The centralizer action and possible quotient constructions are a genuine
escape reserved for Paper 10.  The inert shell is transitive under the
finite-field centralizer; the split shell has the two eigenlines and their
complement as natural strata; and the ramified shell separates the nonzero
Jordan kernel from its complement.  This note neither constructs nor rules
out an enriched quotient or canonical selector, and any such construction
would depend on the $p$-shell centralizer while receiving its prime label from
the externally specified additive-order shell.

## Global analytic scope

For the unweighted label product

$$
Z_{\mathrm{lab}}(s)
=\prod_p(1-p^{-s})^{-m_p},
$$

the safe global claims are deliberately non-sharp:

- for real $1<s\le2$, its positive logarithmic series diverges;
- for complex $s$ with $1<\operatorname{Re}s\le2$, the logarithmic series
  is not absolutely convergent;
- it is absolutely convergent for $\operatorname{Re}s>3$.

No claim is made about conditional convergence or analytic continuation in
$2<\operatorname{Re}s\le3$, and no exact abscissa is claimed.

## Registered-audit question

Can a later independently authorized exact audit reproduce the five
inherited prime-shell controls

$$
p\in\{2,3,5,7,11\}
$$

and verify the formal product and normalization identities without scanning
new primes, evaluating $s$ or logarithms numerically, or accessing any prime
or Riemann-zero dataset?

The audit is a falsification control for an already proved theorem.  It is
not evidence for the infinite-prime convergence statements and is not
authorized by this source-design package.

## Required conclusion and nonclaims

If the proof and later fixed audit pass, the conclusion is:

`PRIME_SHELL_MULTIPLICITY_OBSTRUCTION_CERTIFIED /
A0_FAIL_GLOBAL_NORMALIZATION_ONLY / ROUTE_B_NOT_OPENED`.

The note does not claim a prime-orbit bijection, a new dynamical-zeta
formalism, a transfer or Fredholm determinant, a canonical selector, an exact
global abscissa, a centralizer quotient, a prime/zero correspondence, a
quantization, or historical priority.
