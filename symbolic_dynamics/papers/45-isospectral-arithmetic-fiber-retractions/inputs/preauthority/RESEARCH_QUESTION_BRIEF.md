# Research question brief

## Narrow question

For every \(h\ge2\), do the saturated and exponent-modulo retractions

\[
\tau_h(n)=\prod_p p^{\min(v_p(n),h-1)},\qquad
\omega_h(n)=\prod_p p^{v_p(n)\bmod h}
\]

produce compact weighted composition operators that are indistinguishable
by their nonzero eigenvalues and legal cyclic traces, yet sharply
distinguishable by singular Weyl constants, normal-similarity domains,
maximal Riesz growth, and self-commutator ideals?

The quantifiers are fixed:

- \(h\) ranges over every integer \(h\ge2\);
- \(s\in\mathbb C\) and \(\sigma=\Re s\);
- \(k\) is a positive integer and \(0<q<\infty\);
- each operator begins on finitely supported vectors in
  \(\ell^2(\mathbb N)\);
- operator, power, trace, determinant, and commutator assertions are made
  only on their separately stated legal domains.

## Answer

Yes, after correcting every endpoint and the Weyl crossover.

The two maps fix the same basis labels \(\mathcal F_h\), so their simple
nonzero eigenvalues are exactly \(m^{-s/2}\). Their fibers are nevertheless
different:

\[
\tau_h^{-1}(m)
=\left\{m\prod_{p\in J_h(m)}p^{r_p}:r_p\ge0\right\},
\qquad
\omega_h^{-1}(m)=\{ma^h:a\ge1\},
\]

where \(J_h(m)=\{p:v_p(m)=h-1\}\). The resulting rank-one block norms are

\[
\rho_S(m)^2
=m^{-\sigma}\prod_{p\in J_h(m)}(1-p^{-\sigma})^{-1},
\qquad
\rho_M(m)^2=m^{-\sigma}\zeta(h\sigma).
\]

These formulas yield the strict domain and ideal walls, the exact
similarity iff statements, and the common trace formula

\[
\operatorname{Tr}(S_{h,s}^k)=\operatorname{Tr}(M_{h,s}^k)
=\frac{\zeta(ks/2)}{\zeta(hks/2)}
\]

only when \(\sigma>1/h\) and \(k\sigma>2\).

## The nontrivial crossover

The singular Weyl laws have constants

\[
C_{h,\sigma}
=\prod_p(1-p^{-1})
\left[
\sum_{e=0}^{h-2}p^{-e}
+p^{-(h-1)}(1-p^{-\sigma})^{-1/\sigma}
\right]
\]

and

\[
D_{h,\sigma}=\frac{\zeta(h\sigma)^{1/\sigma}}{\zeta(h)}.
\]

No global ordering between them is claimed. The exact universal equality is

\[
C_{h,1}=D_{h,1}=1.
\]

At that same parameter, \(M_{h,s}\) is boundedly similar to normal while
\(S_{h,s}\) is not. Thus eigenvalues, legal regularized determinants, and
even the leading singular Weyl constant at \(\sigma=1\) do not determine
the bounded similarity class.

## Why the all-\(h\) pair is the unit

The \(h=2\) saturated radical operator alone is not a paper-sized claim:
generic weighted-composition theory and Papers 27--28 absorb its basic
fiber, spectrum, projection, and Schatten mechanisms. The admissible unit
is the paired all-\(h\) classification, because the exact comparison leaves
the following joint arithmetic remainder:

- unequal existence domains with a shared eigenvalue ledger;
- a saturated similarity wall at one versus modulo similarity throughout
  its bounded domain;
- a three-regime primorial maximal-order law with an \(h\)-dependent
  coefficient;
- two Tauberian Weyl constants and their exact equality crossover;
- a self-commutator wall at half the operator-ideal exponent.

## Explicit non-goals

- no novelty claim for weighted composition, fiber orthogonality, rank-one
  singular values, oblique projections, Gram matrices, Schatten ideals, or
  regularized determinants in general;
- no novelty claim for the \(h\)-free part, radical, or exponent-modulo map;
- no claim that \(C_{h,\sigma}\) is always larger or smaller than
  \(D_{h,\sigma}\);
- no trace outside trace class and no formal power used to bypass the
  bounded-existence wall of \(M_{h,s}\);
- no rational-prime selector, Riemann-zero model, completed functional
  equation, or Hilbert--Polya operator;
- no use of a free-UFD clone as positive arithmetic evidence;
- no priority inference from failure to locate exact prior art;
- no authority or integration decision.

## Decision

The corrected all-\(h\) pair is PROVABLE AS STATED and remains
paper-sized after mandatory deletion of shared methods. Its preauthority
status is GO_WITH_FIREWALL, conditional on independent evaluator agreement,
mutation rejection, renewed exact-prior-art checking, and root authority.
