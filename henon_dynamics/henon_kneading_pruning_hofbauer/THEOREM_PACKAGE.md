# Theorem and certificate package

## Finite-prefix proposition

For each (1\le n\le12), the producer and independent checker enumerate the
same set of binary words whose every cyclic suffix is decided and lies between
the frozen lower and upper bounds.  The language is rotation invariant.

## Primitive inversion

If (t_n) is the rooted-word count and (p_n) the primitive-necklace count,
then exact integer Möbius inversion gives

\[
t_n=\sum_{d\mid n} d p_d.
\]

## Formal determinant prefix

The coefficients of (D_N(z)=\exp(-\sum_{n\le N}t_nz^n/n)) are computed by

\[
n[z^n]D_N=-\sum_{k=1}^n t_k[z^{n-k}]D_N.
\]

The checker and SymPy independently verify the coefficients through degree 12.

## Verdict

`A1_OPEN`: infinite Hénon coding and completeness are not established.

`A2_CERTIFIED_PREFIX`: the finite source-locked trace/determinant prefix is
reproducible; no analytic Fredholm determinant is claimed.
