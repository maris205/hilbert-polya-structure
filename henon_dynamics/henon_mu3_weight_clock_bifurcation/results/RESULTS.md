# HCS-C51 code/results summary

Status: `RELEASE_CANDIDATE`.

The exact source normalization gives

\[
C_{p,n}=-2(e_{p,n}+o_{p,n}),\qquad
u_{n,j}=ns+j,\qquad
c_{s,n,j}=\frac{(w+1)/2-j}{n}.
\]

The full leading center spectrum is
`{-1/4,-1/6,-1/8,0}`.  The normalized odd-weight components align at
`s=0` exactly for the leading denominator term `j=1`; the higher clock
terms split that alignment.  The exact C50 second-moment factorization is
the minimal theorem-level factorwise obstruction.

The certificate additionally checks:

- all eleven common C48--C50 split-prime controls with exact rationals;
- `b_prim(S_n)=(4^n+2)/3`, `b_mid(X_n)=(2*4^n-8)/3`, and total rank
  `4^n-1` for every `2 <= n <= 20` by Chern coefficient computation.
  The Hénon source geometry is locked only for `n=2,3,4`; rows `n=5,...,20`
  are explicitly conditional smooth-model identities;
- integral Tate-relabel invariance and the physical failure of a fixed-clock
  half-weight mutation;
- coefficient-field exponents `2/n`, with fractional-power firewalls;
- the direct-`K` ordinary-compatible-system rank obstruction: at `n=3`
  the required even/odd ranks are `46/3,80/3`, and at `n=4` the even rank
  is `87/2`.  Restriction of scalars removes this numerical obstruction at
  `n=4`, so a `Q`-realization is not excluded;
- the denominator-cleared odd leading skeleton, whose integral exponents
  are `12/n=(6,4,3)` and whose common center is `s=0`; only the `n=2`
  functional equation is currently proved;
- the `n=4` `chi_y`, twisted Hodge ledger, and the full expected
  `Gamma_C` sector bookkeeping for `n=2,3,4`.

No full Hénon functional equation, RH statement, or Hilbert--Pólya operator
is claimed.
