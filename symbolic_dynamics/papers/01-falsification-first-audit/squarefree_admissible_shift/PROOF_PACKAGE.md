# Proof Package: Periodic-Point Collapse in the Squarefree Shift

## Claim

For the squarefree admissible subshift \(X_{\rm sf}\), the only periodic point
is the all-zero sequence.  Hence its Artin–Mazur zeta is \(1/(1-z)\).

## Status

**PROVED**

## Assumptions

The shift is exactly the two-sided system in the frozen definition, with an
exclusion for every rational-prime square.  No finite-modulus approximation is
substituted for the infinite grammar.

## Notation

Let \(S=\operatorname{supp}(x)\).  If \(x\) has period \(n\), then \(S\) is a
union of residue classes modulo \(n\).

## Strategy

Assume a periodic point has a nonempty support.  Select a prime \(p\nmid n\).
A single occupied residue class modulo \(n\) then maps surjectively modulo
\(p^2\), contradicting admissibility.

## Dependency Map

Only Euclid's theorem (there is a prime not dividing a fixed integer) and the
Chinese remainder theorem are used.

## Proof

Let \(x\in X_{\rm sf}\) have period \(n\ge1\).  Suppose \(S\ne\varnothing\),
and choose \(a\in S\).  Periodicity implies

\[
a+n\mathbb Z\subseteq S.
\]

Choose a rational prime \(p\) with \(p\nmid n\).  Since \(n\) is invertible
modulo \(p^2\), the map

\[
k\longmapsto a+nk\pmod{p^2}
\]

is a bijection of \(\mathbb Z/p^2\mathbb Z\).  It follows that

\[
S\bmod p^2=\mathbb Z/p^2\mathbb Z,
\]

which violates the defining condition of \(X_{\rm sf}\).  Therefore
\(S=\varnothing\), so \(x=0^\mathbb Z\).

The zero sequence is fixed by every iterate.  Thus

\[
\#\operatorname{Fix}(\sigma^m)=1
\quad\text{for all }m\ge1,
\]

and

\[
\zeta_{X_{\rm sf}}(z)
=\exp\left(\sum_{m\ge1}\frac{z^m}{m}\right)
=\frac1{1-z}.
\]

## Corrections and Edge Cases

1. The prime \(p\) is chosen after the period \(n\), but it is not fitted to a
   numerical target; every \(p\nmid n\) gives the contradiction.
2. A finite set of prime-square exclusions does not prove the result, because
   a proposed period may share all the relevant modular structure.
3. Rich word complexity or positive entropy cannot replace the absent
   primitive periodic orbits in an Euler product.

## Open Risks

None for the stated periodic-point theorem.  Other notions of zeta for
aperiodic or hereditary structure would be different observables and require a
new preregistration; they cannot rescue this candidate's Artin–Mazur ledger.
