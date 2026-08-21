# Theorem package

Let `T_H` be a C88 first-passage time.  For `0 <= r <= 6`, C89 certifies

`m_r = E[T_H^r]`, `f_r = E[(T_H)_r]`, and
`mu_r = E[(T_H-E T_H)^r]` exactly, together with cumulants `kappa_1` through
`kappa_6`.

If `S_H(k)=P(T_H>k)`, the certificate verifies

`m_r = sum_{k=0}^{15} ((k+1)^r-k^r) S_H(k)` and
`f_r = r! sum_{k=0}^{15} binom(k,r-1) S_H(k)`.

All identities are rational equalities over the finite uniform permutation
space, not asymptotic or arithmetic assertions.
