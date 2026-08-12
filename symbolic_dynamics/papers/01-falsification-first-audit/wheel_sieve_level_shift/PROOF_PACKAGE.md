# Proof Package: Wheel-Sieve Arithmetic and Acyclicity

## Claim

The frozen recursion enumerates the rational primes and derives a logarithmic
primorial-ratio clock, but its level shift has no periodic point of positive
period.

## Status

**PROVED**

## Assumptions

\(Q_1=q_1=2\).  The canonical residue vertices at level \(k\) are the units
modulo \(Q_k\), lifted by all branches except the unique new nonunit branch.
Every graph transition raises the level from \(k\) to \(k+1\).  No reset or
stationarizing edge is appended.

## Notation

Let \(p_k\) be the \(k\)-th rational prime.

## Strategy

Use induction and the minimality in the recursion to prove
\(q_k=p_k\).  Then use strict level growth to exclude cycles.

## Dependency Map

The arithmetic step uses only elementary factorization: a composite integer
has a prime divisor not exceeding its square root.  The dynamical step is a
direct graph argument.

## Proof

### Step 1: prime enumeration

The base case is \(q_1=2=p_1\) and \(Q_1=2\).  Assume

\[
q_j=p_j\quad(1\le j\le k),\qquad
Q_k=\prod_{j=1}^{k}p_j.
\]

The next prime \(p_{k+1}\) is coprime to \(Q_k\), so the minimizing set is
nonempty and \(q_{k+1}\le p_{k+1}\).

Suppose the minimizer \(q_{k+1}\) were composite.  Let \(r\) be its least
prime divisor.  If \(r\le p_k\), then \(r\mid Q_k\), contradicting
\(\gcd(q_{k+1},Q_k)=1\).  If \(r>p_k\), then

\[
p_k<r<q_{k+1},\qquad \gcd(r,Q_k)=1,
\]

contradicting the minimality of \(q_{k+1}\).  Hence \(q_{k+1}\) is prime, and
there is no prime strictly between \(p_k\) and it.  Therefore
\(q_{k+1}=p_{k+1}\), closing the induction.

The update gives

\[
\frac{Q_{k+1}}{Q_k}=q_{k+1}=p_{k+1},
\]

so the frozen roof equals \(\log p_{k+1}\) as a derived scale ratio.

### Step 2: absence of periodic paths

For completeness, let \(X_k\) be the one-sided paths whose first edge begins
at level \(k\), and define the phase space

\[
X=\bigsqcup_{k\ge0}X_k.
\]

Deleting the first edge defines a self-map \(\sigma:X\to X\), with
\(\sigma(X_k)\subseteq X_{k+1}\).  After \(n\) shift steps, a path beginning
at level \(k\) lies in the disjoint component \(X_{k+n}\).  Equality with the
original path would require \(k+n=k\), impossible for \(n\ge1\).  Thus

\[
\operatorname{Fix}(\sigma^n)=\varnothing
\quad(n\ge1).
\]

There is no primitive-orbit Euler ledger to evaluate.  Equivalently, the
formal Artin–Mazur series of this noncompact disjoint-tail self-map has all
fixed-point coefficients zero, so \(\zeta_{\rm AM}=D_{\rm AM}=1\).

## Corrections and Edge Cases

1. The prime generator is endogenous to the recursion; this does not transfer
   A0 credit to another symbolic object.
2. A two-sided natural extension over positive levels has no bi-infinite path
   without adding new predecessor structure.
3. Adding \(k\to1\) reset edges creates cycles but has no independent
   arithmetic justification and changes the candidate.

## Open Risks

Stage 02 has now **resolved the strict-extension reading**: a semiconjugate
extension still has no periodic points, and the standard inverse-limit natural
extension is empty.  What remains **OPEN** is a genuinely new factor or
observational recoding of comparable description complexity that retains the
endogenous prime recursion and creates compatible primitive cycles without
resets or prime-indexed components.  See the
[Paper-02 theorem screen](../../02-wheel-sieve-stationarization-obstructions/README.md).
