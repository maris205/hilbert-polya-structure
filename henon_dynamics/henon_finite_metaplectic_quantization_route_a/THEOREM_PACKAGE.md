# Theorem package

Let `N=7`, `omega=exp(2*pi*i/7)`, and `1/2=4 mod 7`.  On the basis
`|x>`, `x in Z/7Z`, define

\[
Q|x\rangle=\omega^x|x\rangle,\qquad
P|x\rangle=|x+1\rangle,
\]
\[
W(q,p)=\omega^{-qp/2}Q^qP^p,\quad
\mathcal F_{xy}=7^{-1/2}\omega^{xy},\quad
C_{xx}=\omega^{(3/2)x^2},\quad U=C\mathcal F^{-1}.
\]

## Theorem 1 — natural finite metaplectic lift

`U` is unitary and, for all 49 phase-space points,

\[
U W(q,p)U^{-1}=W(3q-p,q).
\]

Hence powers preserve the discrete time clock exactly and implement `A^n`.
With complex conjugation `K` and `Theta=F K`,

\[
\Theta^2=I,\qquad \Theta U\Theta^{-1}=U^{-1}.
\]

## Theorem 2 — exact action sum

For every `n>=1`,

\[
\operatorname{Tr}U^n=7^{-n/2}
\sum_{x_0,\ldots,x_{n-1}\in\mathbb F_7}
\omega^{\sum_j((3/2)x_j^2-x_jx_{j-1})}.
\]

The stationary equations are
`3*x_j-x_{j-1}-x_{j+1}=0 mod 7`, precisely the discrete Hénon recurrence.

## Proposition — same-convention even-modulus obstruction

The frozen Weyl phase uses `1/2 mod N`.  At the explicit control modulus
`N=8`, the congruence `2*h=1 mod 8` has no solution.  Therefore the literal
phase `omega^(-q*p/2)` used above is not directly defined by the same formula
at even level.  This is a convention-scoped negative result: it does not rule
out doubled-phase or other separately defined even-level Weil/metaplectic
conventions.

## Theorem 3 — finite-level aliasing obstruction

Exact cyclotomic arithmetic gives

\[
U^8=I,
\]

and the eigenvalues are the eight roots of unity except `-i`.  Thus

\[
\det(I-zU)=\frac{1-z^8}{1+iz}
=1-iz-z^2+iz^3+z^4-iz^5-z^6+iz^7.
\]

The trace is `7` when `8|n` and otherwise `-(-i)^n`.  By contrast, the
classical fixed count is `|det(A^n-I)|=Tr(A^n)-2`, which grows exponentially.
Therefore the fixed `N=7` quantum trace cannot be a global carrier of the
classical periodic-orbit growth.

## Strict assessment

Exact Egorov, unitarity, clock preservation, and antiunitary reversal justify
`A4_NATURAL_QUANTIZATION`.  The full tuple remains
`(A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`, and Route B remains
unauthorized.
