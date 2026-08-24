# Proof package

## Claim

For every odd integer `N>=3`, let `h` be the inverse of two modulo `N`, let
`omega=exp(2*pi*i/N)`, and define on `C^N`

\[
Q|x\rangle=\omega^x|x\rangle,\quad P|x\rangle=|x+1\rangle,
\quad W(q,p)=\omega^{-hqp}Q^qP^p,
\]
\[
\mathcal F_{xy}=N^{-1/2}\omega^{xy},\quad
C_{xx}=\omega^{3hx^2},\quad U_N=C\mathcal F^{-1}.
\]

Then `U_N` is unitary and

\[
U_NW(q,p)U_N^{-1}=W(3q-p,q)
\]

for every `(q,p)` modulo `N`.  With coefficientwise conjugation `K` and
`Theta_N=F K`, one has

\[
\Theta_N^2=I,\qquad \Theta_NU_N\Theta_N^{-1}=U_N^{-1},
\qquad \Theta_NW(q,p)\Theta_N^{-1}=W(p,q).
\]

If `u_0=0`, `u_1=1`, and `u_{n+1}=3u_n-u_{n-1}`, then

\[
A^n=\begin{pmatrix}u_{n+1}&-u_n\\u_n&-u_{n-1}\end{pmatrix},\qquad
\|A^n-I\|_{\max}=u_{n+1}-1.
\]

Thus `N>u_{L+1}-1` implies that no power `1<=n<=L` has
`A^n=I mod N`; consequently no `U_N^n` in that interval is scalar.

## Status

`PROVABLE AS STATED` for the per-level family.  Cross-level projective
compatibility and semiclassical trace matching are not part of the claim.

## Assumptions

- `N` is odd and at least three.
- Residues and exponents are interpreted modulo `N`.
- `K` is conjugation in the standard position basis.
- The norm is the maximum absolute value of the four integer matrix entries.

## Proof strategy and dependency map

1. Fourier orthogonality proves that `F` is unitary; the chirp is diagonal
   unitary.
2. Generator conjugations determine the exact Weyl action, with the two
   half-phases cancelling.
3. Conjugating `F` and `C` coefficientwise proves the antiunitary identities
   without a scalar repair.
4. A second-order induction proves the matrix-power formula and the norm
   identity.
5. A nonzero integer matrix of max norm below `N` cannot vanish modulo `N`.

## Proof

Fourier orthogonality gives

\[
\sum_{y\bmod N}\omega^{(x-x')y}=N\,\mathbf 1_{x=x'},
\]

so `F` and therefore `U_N` are unitary.  From `PQ=omega^{-1}QP`,

\[
W(v)W(w)=\omega^{h(v_1w_2-v_2w_1)}W(v+w).
\]

Directly, `F^{-1}QF=P`, `F^{-1}PF=Q^{-1}`,
`CQC^{-1}=Q`, and `CPC^{-1}=W(3,1)`.  Hence

\[
U_NQU_N^{-1}=W(3,1),\qquad U_NPU_N^{-1}=W(-1,0).
\]

For general `(q,p)`, the prefactor `omega^{-hqp}` in `W(q,p)` is cancelled
by the product phase `omega^{hqp}` from
`W(3q,q)W(-p,0)`.  This proves exact Egorov and, by iteration, the unchanged
discrete clock.

Because `bar(F)=F^{-1}` and `bar(C)=C^{-1}`,

\[
(\mathcal FK)^2=\mathcal F\overline{\mathcal F}=I,
\]

and

\[
\Theta_NU_N\Theta_N^{-1}
=\mathcal F\overline{U_N}\mathcal F^{-1}
=\mathcal FC^{-1}=U_N^{-1}.
\]

The Weyl reversal follows from `K W(q,p) K=W(-q,p)` and one exact reordering
after Fourier conjugation.  No level-dependent anomaly is absorbed.

The matrix-power formula holds at `n=1`; multiplying by `A` advances the same
recurrence, so induction proves it for every `n`.  The recurrence is positive
and strictly increasing from `u_1` onward, and comparison of the four entries
of `A^n-I` gives the displayed max norm.  If `N` exceeds that norm and
`A^n-I` vanished modulo `N`, each entry would be a multiple of `N` with
absolute value below `N`, hence zero.  This contradicts the nonzero
off-diagonal entry `u_n`.  If `U_N^n` were scalar, its adjoint action would fix
every Weyl observable; injectivity of `(q,p) -> W(q,p)` would force
`A^n=I mod N`.  The claimed no-action-alias window follows.

## Corrections or missing assumptions

At even `N`, the congruence `2h=1 mod N` has no solution.  This blocks only
the literal frozen half-phase formula.  Doubled-phase and other separately
defined even-level Weil/metaplectic conventions are not ruled out.

## Open risks

- Relative phases between different odd levels are not compared.
- No trace asymptotic or classical-orbit matching statement is made.
- A target-facing divisor protocol remains absent.

## Strict assessment

The tuple is
`(A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)` and
`route_b_invocation_allowed: false`.
