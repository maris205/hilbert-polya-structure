# Derivation Package: Renewal Determinants

## 1. Problem Setup and Target Quantity

Let \(A\) be the set of first-return atoms at a common base vertex.  Assign an
atom \(a\) a weight \(x_a\), which may combine a scalar potential and a roof.
Unique concatenation at the base gives

\[
F=\sum_{a\in A}x_a,\qquad
Z_{\rm ren}=\frac1{1-F}.
\]

The goal is to determine whether this flexibility supplies an explanatory
prime Euler product or merely an inverse-design language.

## 2. Assumptions and Modeling Choices

1. All atoms return to the same base and can therefore be concatenated freely.
2. The first-return code has unique factorization.
3. Complex weights are allowed but must be fixed before any target comparison.
4. Claims are restricted to the disk of absolute convergence unless a
   separate continuation theorem is supplied.

## 3. Notation

For the one-loop-per-length specialization,

\[
F(z)=\sum_{n\ge1}a_nz^n.
\]

For formal mixed-word bookkeeping, \(x_a,x_b,\ldots\) are algebraically
independent variables.

## 4. Derivation

Every based closed path is a word in the return atoms, so the based generating
series is

\[
1+F+F^2+\cdots=\frac1{1-F}.
\]

The logarithm reorganizes words into primitive necklaces:

\[
\log Z_{\rm ren}
=\sum_{r\ge1}\frac{F^r}{r}.
\]

This is the dynamical Euler ledger of the renewal system.  It is not the
independent-atom product

\[
Z_{\rm ind}=\prod_{a\in A}(1-x_a)^{-1}.
\]

Indeed, for two atoms,

\[
\frac1{1-x_a-x_b}
=1+x_a+x_b+x_a^2+2x_ax_b+x_b^2+\cdots,
\]

whereas

\[
\frac1{(1-x_a)(1-x_b)}
=1+x_a+x_b+x_a^2+x_ax_b+x_b^2+\cdots.
\]

The additional contribution is the mixed primitive necklace \(ab\).

For inverse design, let

\[
H(z)=1+\sum_{n\ge1}h_nz^n
\]

be any holomorphic germ.  The fixed assignment \(a_n=-h_n\) gives
\(D_{\rm ren}=H\) coefficient by coefficient.  Therefore arbitrary analytic
zero patterns near the origin are representable, including unrelated
controls.

## 5. Main Result

**PROVED:** unrestricted complex renewal weights are non-identifying: analytic
representability alone supplies no arithmetic evidence.  A natural
shared-base renewal also has mixed primitive words and therefore cannot
produce only the independent \(p^r\) factors of the Riemann Euler product.

## 6. Interpretation

Countable symbolic dynamics evades the finite exponential-polynomial
obstruction, but only by moving complexity into infinitely many return data.
Unless those data and their phases arise independently from a simple grammar,
the determinant is a re-encoding of the desired function.

## 7. Scope and Limitations

The argument does not forbid every countable Markov shift.  It applies to the
frozen shared-base renewal architecture and to low-complexity unary
regular/context-free attempts.  More powerful grammars require fresh A0 and
description-complexity audits.
