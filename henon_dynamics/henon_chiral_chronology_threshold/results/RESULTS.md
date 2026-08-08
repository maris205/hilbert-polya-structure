# HCS-C21 results

## Exact geometry

For the published period-six chiral doublet,

\[
\operatorname{Gal}(E_6/\mathbb P^1_A)
\simeq D_6\simeq S_3\times C_2,
\qquad |D_6|=12,
\]

and

\[
\boxed{g(E_6)=1}.
\]

Over the radical line $\eta^2=A-3$, the cubic discriminant and
Riemann--Hurwitz ledger are

\[
\Delta(\eta)=16\eta^4+88\eta^2+125,
\]

\[
2g(E_6)-2=6(-2)+4\cdot3=0.
\]

All four finite branch points are simple transposition points and infinity
is unramified.

## Exact chronology quotient

With $w$ the cubic Vandermonde and $v=\eta w$,

\[
\boxed{
\mathbb Q(E_6)^{\langle\tau\rangle}
=\mathbb Q(A,v),
\quad
v^2=(A-3)(16A^2-8A+5).
}
\]

Both (E_6) and its rotation quotient have genus one, so the degree-six
quotient is unramified.  The chronological action is a six-torsion
translation and

\[
\boxed{
\tau^*|_{H^1(E_6)}=1,
\quad
\dim H^1(E_6)_{\tau\ne1}=0.
}
\]

## Scoped period threshold

| Period | Certified chiral object | Genus | Nontrivial $\tau$-isotypic $H^1$ dimension |
|---:|---|---:|---:|
| (n<6) | no chiral class in the source count | -- | -- |
| 6 | unique published chiral doublet, C21 ordered cover | 1 | 0 |
| 7 | HCS-C20 adopted certified component | 8 | 12 |

The valid threshold is restricted to source-identified and
repository-certified chiral ordered components through period seven.

## Lower-period marker shadow

\[
D^{\mathrm{mark}}_6(s_6)=4D_1(s_6/2),
\qquad
C^{\mathrm{mark}}_7(s_7)=D_1(s_7-2).
\]

The fiber product factors as

\[
(s_6-2s_7+4)(s_6+2s_7)=0.
\]

Its two normalized graph components meet in the non-normal fiber product at
((A,s_6,s_7)=(-1,-2,1)).  The common quadratic field is a period-one
shadow, not a primitive ordered-cover bridge.

## Verification ledger

- Producer schema: `HCS-C21-producer-1`.
- Independent checker schema: `HCS-C21-independent-check-1`.
- Certificate SHA-256:
  `5386c95cbc65e6a4323cfcf230de6b41f353be909d197818f9c4fbf0a75a96fc`.
- Independent result SHA-256:
  `0f14332f36f2f7df0ab238954c5a8531bcb9d759f8feeac60bc7bcc197452985`.
- Independent named checks: 133.
- Regression/fail-closed tests: 14 passed.

## Claim boundary

No full saturated exact-period classification, primitive cross-period
correspondence, Fredholm determinant, Riemann divisor, or Hilbert--Pólya
operator is claimed.
