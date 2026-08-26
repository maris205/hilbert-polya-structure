# C172 proof package

## Definition

Let \(Q=p^e\geq2\), let \(a\) generate the cyclic group
\(\mathbb F_Q^\times\), put \(N=Q-1\), and define
\(T_a(x)=ax\) on \(\mathbb F_Q\).  Let \(U_af=f\circ T_a\) on normalized
counting \(L^2(\mathbb F_Q)\).

## Theorem (all-prime-power multiplier certificate)

For every prime power \(Q\geq2\) and every primitive \(a\):

1. Zero is fixed and \(\mathbb F_Q^\times\) is one cycle of length \(N\).
   Consequently
   \[
   \#\operatorname{Fix}(T_a^n)=1+N\mathbf 1_{N\mid n}
   =\begin{cases}Q,&N\mid n,\\1,&N\nmid n.\end{cases}
   \]
2. The Artin--Mazur zeta is
   \[
   \zeta_{T_a}(z)=\exp\!\left(\sum_{n\geq1}
   \#\operatorname{Fix}(T_a^n)\frac{z^n}{n}\right)
   =\frac1{(1-z)(1-z^N)}.
   \]
3. \(U_a\) is unitary, with one extra eigenvalue \(1\) from zero and every
   \(N\)-th root of unity once from the nonzero cycle.  Hence
   \[
   \det(I-zU_a)=(1-z)(1-z^N)=\zeta_{T_a}(z)^{-1}.
   \]
4. The involution \(I(0)=0\), \(I(x)=x^{-1}\) for \(x\ne0\), obeys
   \(IT_aI=T_a^{-1}\).  Thus
   \(\Theta f(x)=\overline{f(Ix)}\) is a same-clock antiunitary reversal.
5. \(U_a\) is self-adjoint if and only if \(N\leq2\), equivalently
   \(Q\leq3\).

## Proof

Every nonzero element has a unique form \(a^k\), \(k\in\mathbb Z/N\mathbb Z\),
and \(T_a(a^k)=a^{k+1}\).  This is one \(N\)-cycle and proves part 1.
Then
\[
 \sum_{n\geq1}\#\operatorname{Fix}(T_a^n)\frac{z^n}{n}
 =\sum_{n\geq1}\frac{z^n}{n}
 +\sum_{m\geq1}N\frac{z^{mN}}{mN}
 =-\log(1-z)-\log(1-z^N),
\]
which proves part 2 as a formal identity and analytically for \(|z|<1\).

Composition with a permutation is unitary for normalized counting measure.
The fixed point contributes a one-dimensional \(1\)-eigenspace; Fourier
characters of \(\mathbb Z/N\mathbb Z\) diagonalize the long cycle and give all
\(N\)-th roots once.  Their characteristic product is \(1-z^N\), proving
part 3.

For \(x\ne0\),
\[
 IT_aI(x)=I(ax^{-1})=a^{-1}x=T_a^{-1}(x),
\]
and zero is fixed throughout, proving the reversal.  A unitary is self-adjoint
exactly when it equals its inverse.  A permutation has that property exactly
when all cycles have length at most two.  Here the only nontrivial cycle has
length \(N\), proving part 5. \(\square\)

## Controls and edge cases

- \(Q=2\): \(N=1\), so both points are fixed; the formula gives
  \(\zeta=(1-z)^{-2}\) and \(\det(I-zU)=(1-z)^2\).
- \(Q=3\): the nonzero cycle has length two and \(U\) is self-adjoint.
- \(Q\geq4\): a nonreal \(N\)-th root or a cycle longer than two obstructs
  self-adjointness.
- Multiplication by \(a^h\) has \(\gcd(h,N)\) nonzero cycles, each of length
  \(N/\gcd(h,N)\); this detects primitivity.
- A fixed point plus translation on an abstract cyclic set, or any permutation
  of cycle type \((1)(N)\), has the same zeta and determinant.  Thus the proved
  invariants do not by themselves characterize finite fields or target
  arithmetic.
