# Derivation Package

## Target

Derive, inside Symbolic Dynamics, a single countable symbolic system whose
primitive/repetition ledger is obtained from tensor factorization of finite
full shifts and whose weighted zeta is exactly the Riemann zeta function in
its Euler half-plane.  The immediate target is an exact identity, not an RH
claim:

\[
 Z_{\otimes}(s)=\zeta(s),\qquad
 D_{\otimes}(s)=\det(I-\mathcal L_s)=\zeta(s)^{-1},
 \qquad \Re s>1.
\]

## Status

**COHERENT AS STATED in \(\Re s>1\); global determinant/RH target remains
open.**

The arithmetic skeleton survives unchanged.  The hoped-for completed
Hilbert--Pólya determinant does not follow: the ordinary Fredholm determinant
has the inverse orientation, and the symbolic construction presently has no
intrinsic archimedean factor or operator-side continuation through the
critical strip.

## Invariant Object

The organizing invariant is the **entropy norm on the tensor monoid of finite
full shifts**:

\[
 \mathcal N(X):=e^{h_{\rm top}(X)}.
\]

Unlike a manually assigned prime roof, this norm is read from the symbolic
system itself and satisfies

\[
 \mathcal N(X\otimes Y)=\mathcal N(X)\mathcal N(Y).
\]

## Assumptions

1. \(F_n=(\{1,\ldots,n\}^{\mathbb Z},\sigma)\) is the two-sided full
   \(n\)-shift, for every \(n\ge1\).
2. The monoidal operation is the actual coordinatewise Cartesian product of
   symbolic systems, not an arbitrary operation on indices.
3. Objects are considered up to topological conjugacy.
4. The length/roof of a tensor atom is its intrinsic topological entropy.
5. The weighted diagonal transfer operator is considered first on
   \(\ell^2(\operatorname{At}(\mathsf{FSh}))\) for \(\Re s>1\).
6. No prime table, Riemann-zero table, fitted scale, or fitted phase occurs in
   the candidate definition.

## Notation

- \(\mathsf{FSh}=\{[F_n]:n\ge1\}\): isomorphism classes of finite full shifts.
- \(\otimes\): Cartesian product of shifts.
- \(\mathbf 1=[F_1]\): tensor unit.
- \(\operatorname{At}(\mathsf{FSh})\): nonunit tensor-indecomposable classes.
- \(h_n=h_{\rm top}(F_n)=\log n\).
- \(D_n^{\rm AM}(z)\): reciprocal Artin--Mazur determinant of \(F_n\).
- \(Y_\otimes\): diagonal countable Markov shift on the tensor-atom alphabet.
- \(\tau(a)=h_{\rm top}(a)\): roof on an atom symbol.
- \(\mathcal L_s\): diagonal weighted transfer operator on atom symbols.
- \(Z_\otimes\): weighted primitive-orbit zeta of \(Y_\otimes\).

## Derivation Strategy

Use a five-link exact chain:

\[
 \text{full-shift product}
 \longrightarrow \text{tensor atoms}
 \longrightarrow \text{diagonal atom shift}
 \longrightarrow \text{trace-class transfer operator}
 \longrightarrow \text{Euler/Dirichlet ledgers}.
\]

The full-shift invariants fix both the multiplicative norm and the roof.  The
countable diagonal shift turns categorical atoms into genuine symbolic
primitive loops.  Its repetitions yield prime powers without a separate
prime-power rule.

## Derivation Map

1. Product conjugacy \(F_m\otimes F_n\cong F_{mn}\) uses only the Cartesian
   product of alphabets.
2. Entropy and AM data identify the integer norm:
   \(h_n=\log n\) and \(D_n^{\rm AM}(z)=1-nz\).
3. Tensor indecomposability is therefore equivalent to integer primality.
4. The diagonal atom shift has one primitive loop per tensor atom and no
   mixed-symbol loops.
5. The intrinsic roof assigns \(\log p\) to that loop; its \(r\)-fold repeat
   has length \(r\log p=\log p^r\).
6. For \(\Re s>1\), the diagonal eigenvalue ledger is \(p^{-s}\), which is
   trace class and admits an ordinary Fredholm determinant.
7. Euler expansion, inverse expansion, and logarithmic differentiation yield
   the coefficients \(1\), \(\mu(n)\), and \(\Lambda(n)\), respectively.
8. Approximation enters only when the infinite registry is truncated for the
   finite experiment.  Every coefficient of mass \(n\le N\) is nevertheless
   exact when all objects \(F_1,\ldots,F_N\) are registered.

## Main Derivation

### Step 1 — Full shifts form the multiplicative tensor skeleton

Coordinatewise pairing of symbols gives a topological conjugacy

\[
 F_m\otimes F_n\cong F_{mn}.
\]

Moreover,

\[
 h_{\rm top}(F_n)=\log n,
 \qquad \#\operatorname{Fix}(\sigma^r|F_n)=n^r.
\]

Representing the full shift by the all-ones adjacency matrix gives the exact
reciprocal AM determinant

\[
 D_n^{\rm AM}(z)
 =\exp\!\left(-\sum_{r\ge1}\frac{n^rz^r}{r}\right)
 =1-nz.
\]

Thus entropy, fixed-point counts, and AM determinant all register the same
norm \(\mathcal N(F_n)=n\), and

\[
 h(F_m\otimes F_n)=h(F_m)+h(F_n),\qquad
 \mathcal N(F_m\otimes F_n)=\mathcal N(F_m)\mathcal N(F_n).
\]

These are identities.

### Step 2 — Tensor atoms are exactly primes

A nonunit \(F_n\) is tensor decomposable exactly when

\[
 F_n\cong F_a\otimes F_b
\]

for some \(a,b>1\), which is equivalent to \(n=ab\).  Hence

\[
 \operatorname{At}(\mathsf{FSh})
 =\{[F_p]:p\text{ prime}\}.
\]

The fundamental theorem of arithmetic simultaneously gives unique tensor
factorization

\[
 F_n\cong\bigotimes_p F_p^{\otimes v_p(n)}.
\]

This is a proposition with an elementary exact proof; it is not a numerical
pattern and does not require a stored list of primes.

### Step 3 — Turn categorical atoms into symbolic primitive loops

Let \(\mathcal A=\operatorname{At}(\mathsf{FSh})\) and define the countable
Markov shift

\[
 Y_\otimes=
 \{(a_j)_{j\in\mathbb Z}\in\mathcal A^{\mathbb Z}:a_{j+1}=a_j
 \text{ for every }j\}.
\]

Its adjacency matrix is the identity on \(\mathcal A\).  Thus every
\(a=[F_p]\) supplies exactly one primitive period-one orbit \(\gamma_a\),
and there are no mixed-symbol primitive cycles.  Define the intrinsic roof

\[
 \tau(a)=h_{\rm top}(F_p)=\log p.
\]

Then

\[
 \ell(\gamma_a^r)=r\tau(a)=r\log p=\log(p^r).
\]

This is the exact primitive/repetition ledger.  The use of a diagonal shift is
a modeling choice, but its alphabet and roof are categorical invariants, not
looked-up arithmetic labels.

The diagonal/no-mixing rule is structurally necessary for the von Mangoldt
ledger.  If two distinct atom symbols \(p,q\) are freely mixed, their weighted
two-symbol full-shift zeta becomes

\[
 Z_{p,q}^{\rm free}(s)=\frac{1}{1-p^{-s}-q^{-s}}.
\]

It has two ordered words of mass \(pq\), rather than the single commutative
factorization, and

\[
 -\frac{d}{ds}\log Z_{p,q}^{\rm free}(s)
 =\frac{(\log p)p^{-s}+(\log q)q^{-s}}
 {1-p^{-s}-q^{-s}}
\]

has coefficient \(\log p+\log q=\log(pq)>0\) at \((pq)^{-s}\).  The target
coefficient is \(\Lambda(pq)=0\).  Isolated atom loops, by contrast, give
\((1-p^{-s})^{-1}(1-q^{-s})^{-1}\): the Dirichlet coefficient at \(pq\) is
one while the logarithmic-derivative coefficient is zero.  Thus no-mixing is
an exact grammar obligation, not a numerical preference.

### Step 4 — Trace-class transfer operator and determinant

On \(\ell^2(\mathcal A)\), define

\[
 (\mathcal L_s f)(a)=e^{-s\tau(a)}f(a).
\]

For \(\sigma=\Re s>1\),

\[
 \|\mathcal L_s\|_1
 =\sum_{a\in\mathcal A}e^{-\sigma\tau(a)}
 =\sum_p p^{-\sigma}<\infty.
\]

Therefore \(\mathcal L_s\) is trace class and

\[
 \operatorname{tr}(\mathcal L_s^r)=\sum_p p^{-rs}.
\]

The ordinary Fredholm determinant is

\[
 D_\otimes(s)
 =\det(I-\mathcal L_s)
 =\prod_p(1-p^{-s}).
\]

This is an analytic determinant identity in \(\Re s>1\).

### Step 5 — Euler, determinant, and prime-power coefficients

The weighted orbit zeta is the inverse determinant:

\[
 \begin{aligned}
 Z_\otimes(s)
 &=\exp\!\left(\sum_{r\ge1}
    \frac{\operatorname{tr}(\mathcal L_s^r)}r\right)\\
 &=\prod_p(1-p^{-s})^{-1}
 =\sum_{n\ge1}n^{-s}
 =\zeta(s), \qquad \Re s>1.
 \end{aligned}
\]

Consequently,

\[
 D_\otimes(s)=\sum_{n\ge1}\frac{\mu(n)}{n^s},
\]

and

\[
 -\frac{Z_\otimes'(s)}{Z_\otimes(s)}
 =\sum_p\sum_{r\ge1}(\log p)p^{-rs}
 =\sum_{n\ge1}\frac{\Lambda(n)}{n^s}.
\]

The von Mangoldt factor arises by differentiating the entropy roof; it is not
inserted into the potential.

### Step 6 — Finite exact recovery statement

Register the opaque objects \(F_1,\ldots,F_N\), their partial tensor table,
entropy, fixed counts, and AM determinant.  Any proper factor of \(n\le N\)
is also at most \(N\), so tensor indecomposability is decided exactly inside
the finite registry.  All prime factors of every \(k\le N\) are recovered.
It follows that the coefficient ledgers of \(Z_\otimes\), \(D_\otimes\), and
\(-Z_\otimes'/Z_\otimes\) are exact through mass \(N\).

This is why the finite experiment is not merely a convergence test: it is an
exact prefix certification.

## Remarks and Interpretation

- The construction supplies a genuine countable symbolic phase space, not
  only a product written across unrelated systems.
- It is intentionally a minimal arithmetic skeleton: its base dynamics is a
  countable union of fixed points.  Complexity lives in the tensor category,
  not in chaotic mixing.
- The full-shift AM determinant is used as a registered invariant identifying
  the alphabet norm.  The global determinant is the Fredholm determinant of
  the derived atom shift; the two determinant data types are not conflated.
- The candidate is bold but deliberately transparent: finite-set
  cardinality under Cartesian product already contains unique factorization.
  The scientific question is whether this categorical origin satisfies A0
  strongly enough, not whether the coefficient identity is correct.

## Boundaries and Non-Claims

1. No RH statement is proved or numerically tested.
2. The operator-side Fredholm determinant is initially defined only for
   \(\Re s>1\).
3. The ordinary determinant is \(1/\zeta\), while the orbit zeta is \(\zeta\).
   This orientation does not yet give a Hilbert--Pólya spectral determinant.
4. The gamma factor, pole removal, functional-equation symmetry, and an
   intrinsic continuation mechanism are absent.
5. No natural Hermitian Weil compression has been derived from this diagonal
   atom shift.
6. No canonical quantization, self-adjoint generator with the required
   counting law, or Route-B object is claimed.
7. A category equivalently encoding integer multiplication can be criticized
   as arithmetic repackaging.  The current result is an exact arithmetic
   symbolic skeleton, not yet a nontrivial explanation of RH.

## Open Risks

1. **A0 naturality risk:** selecting all tensor atoms is a universal
   categorical rule, but it is extensionally the same set as the primes.
   Route A must decide whether this is emergence or a sophisticated encoding.
2. **PROVES_TOO_MUCH risk:** every free commutative factorization monoid admits
   an atom Euler product.  The control experiment shows that one must require
   the actual full-shift product, intrinsic entropy roof, and AM/fixed-point
   compatibility, not abstract UFD alone.
   Likewise, allowing atom symbols to mix freely produces spurious semiprime
   primitive terms; the presentation must retain one isolated primitive loop
   per tensor atom.
3. **Orientation risk:** a parity/superdeterminant trick could reverse
   \(D=1/\zeta\), but no intrinsic symbolic parity has yet been found.  Adding
   it by declaration would be a modeling choice.
4. **Continuation risk:** equality to \(\zeta\) imports known continuation; it
   does not explain continuation from transfer-operator estimates.
5. **Spectral-growth risk:** the diagonal atom spectrum does not by itself
   supply the Riemann--von Mangoldt \(T\log T\) zero count.
