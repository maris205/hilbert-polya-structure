# Round-2 Clues — Paper27 / SD-C29

No manuscript-review loop is authorized. This file records only forward
research clues already licensed by the frozen package.

## Surviving datum

Ordinary multiplication sees

\[
q_pq_q=0\qquad(p\ne q),
\]

but the rank-one factorization \(q_p=|r_p\rangle\langle v_p|\) gives

\[
q_p^*q_q=|v_p\rangle\langle v_q|
\]

up to the shared range inner product. The common \(e_1\) direction makes this
mixed Gram kernel nonzero.

## Paper28 object

For fixed real \(\sigma\), retain the same source-derived projectors and form

\[
T_{\sigma+it,u}
=\sum_pu^{\ell(p)}p^{-\sigma-it}q_p,
\qquad
\mathscr C_{\sigma,u}(t)
=\begin{pmatrix}
0&T_{\sigma+it,u}^*\\
T_{\sigma+it,u}&0
\end{pmatrix}.
\]

The adjoint is not holomorphic in \(s\). Analytic work must begin with a
two-variable holomorphic/antiholomorphic family and only afterward restrict to
real \(t\).

## Mandatory tests

1. Derive the exact mixed Gram kernel.
2. Establish the maximal common Schatten domain for \(T,T^*,T^*T,TT^*\) and
   both holomorphic degrees.
3. Compare oblique, diagonal-coordinate, mutated-poset, and generic locally
   finite controls.
4. Test whether \(t\)-motion changes singular spectra beyond a basis artifact.
5. Permit at most one canonical source-derived regularization and prove
   reference independence.
6. Preserve necklace resolution and \(u^{r\ell(p)}\).

## Stop rule

If the chiral spectrum is generic Gram geometry, if orthogonalization removes
the motion, or if a regularized determinant depends on a chosen reference,
record:

~~~text
STOP_ADJOINT_GRAM_COLLAPSE
STOP_INCIDENCE_ROUTE
~~~

Do not build another ordinary selector.
