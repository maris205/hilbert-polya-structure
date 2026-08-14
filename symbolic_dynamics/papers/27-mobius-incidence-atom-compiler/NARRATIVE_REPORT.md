# Narrative Report — Paper27 / SD-C29

## Outcome

Paper27 closes the most important open obligation from Paper26. The selector
is no longer handed a list of atoms. Instead, the integer divisibility grammar
recognizes its covers of \(1\), which are exactly the rational primes, and
compiles their coordinates through incidence conjugation.

For every source object \(n\),

\[
q_n=\zeta\varepsilon_n\mu
\]

is an oblique primitive idempotent. Filtering this uniform family by the cover
predicate produces exact letter actions. Every mixed word vanishes before
trace, every composite source letter vanishes, and every temporal repetition
of one source atom survives with coefficient one and marker
\(u^{r\ell(p)}\). This is the strongest analytic A1 result on the current
line.

## Why the result is not tautological

The construction does not receive a prime projector inventory. It receives:

- every integer coordinate uniformly;
- the divisibility relation;
- zeta convolution and its inverse;
- the source-derived cover predicate.

Changing the relation changes the selected atoms. In the mutated-source
control where \(6\) is made a cover of \(1\), the compiler selects \(6\).
This is a correct equivariance property and also the precise
PROVES_TOO_MUCH boundary: rational primality comes from the frozen
factorization grammar, not from an independent spectral law.

## Why the result still collapses

At finite cutoff,

\[
q_n=\zeta\varepsilon_n\zeta^{-1}.
\]

More generally, every complete primitive lift with the same diagonal labels
is conjugate by a unit in the nilpotent radical to the coordinate family.
Thus every ordinary cyclic trace and determinant agrees with the diagonal
atom table.

The countable realization makes this concrete. Each \(q_p\) is a bounded
rank-one trace-class idempotent on \(H_\eta\) for \(\eta>1/2\), and the whole
family is boundedly similar to coordinate projectors when \(\eta>1\). Oblique
incidence geometry is real but ordinary trace invisible.

## Analytic result

On the absolute domain

\[
\sum_p|u|^{\ell(p)}p^{-\operatorname{Re}s}<\infty,
\]

the transfer family is trace class and

\[
\det(I-zT_\eta(s,u))
=\prod_p(1-zu^{\ell(p)}p^{-s}).
\]

Tensoring with the Paper25 holomorphic de Rham sector gives two independently
trace-class degree operators. Their graded determinant ratio has the same
product because incidence annihilation removes mixed labels and de Rham
cancellation removes the local fixed-point denominator.

At \(u=1\), the eigenvalues \(p^{-s}\) force a sharp trace-class barrier at
\(\operatorname{Re}s=1\). Scalar continuation of the Euler product is not
continuation of this operator family.

## Route meaning

The correct route record is:

~~~text
(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_PASS_ANALYTIC,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
ROUTE_B_LOCKED
~~~

A1 passes because the orbit selector is source-derived and exact for all
repetitions. A2 passes because both holomorphic degrees have honest
trace-class determinants on one common domain. A3 fails because the \(u=1\)
operator does not continue through its trace-class boundary. A4 fails because
no critical-line carrier or spectral mechanism has been built.

## Forward obligation

Ordinary products satisfy \(q_pq_q=0\) for \(p\ne q\), but adjoint products
need not: \(q_p^*q_q\) sees the shared range direction. Paper28 must test
whether this mixed Gram geometry contains a source-specific invariant or only
generic oblique rank-one overlap. Diagonal and mutated-poset controls are
mandatory; fitted regularization and target-zero comparison remain forbidden.
