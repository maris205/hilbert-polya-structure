# C156 narrative report

## Outcome

C156 turns the C151 class-by-class central rotation into an all-iterate finite
quadratic-module structure.  The horizontal quotient is explicitly known in
Smith form, its exponent is the true universal denominator bound, and its
group-theoretic primary pieces are orthogonal for the rotation polarization.

## Exact progress

For odd `n`, the quotient is `(Z/L_n Z)^2`; for even `n`, it is
`Z/F_n Z x Z/(5F_n) Z`.  A parity lemma proves that the rotation denominator
divides `L_n` or `5F_n`, rather than the earlier safe bound `2D_n^2`.  The
bound is observed sharp for every certified `2<=n<=14`, but no all-iterate
sharpness theorem is claimed.

Exact primary enumeration gives the global fixed-circle counts

```text
1,1,4,1,21,4,57,1,148,105,397,144,1041,57
```

through iterate fourteen.  Each count is independently reconstructed as the
product of the primary zero counts.

## Review-driven repair

The initial derivation risked identifying the canonical correction `q_B`
with the actual iterate cocycle.  They differ by an integer linear form, which
does not spoil the denominator theorem but does change zero counts.  The
release keeps that drift explicit.  A second audit corrected the displayed
polarization to
`v_1 u_2-u_1 v_2+m_1 u_2`; symbolic derivation and exact orthogonality
enumeration now test the same formula.

## Boundary

This is a group-theoretic primary decomposition of source-side clean fixed
fibres.  It is not an arithmetic local/Euler factorization and does not repair
the isolated-orbit or stability obstructions.
