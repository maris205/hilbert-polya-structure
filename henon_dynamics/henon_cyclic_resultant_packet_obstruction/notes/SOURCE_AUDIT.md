# Source Audit

## Primary sources

### Cyclic resultants

Christopher J. Hillar, *Cyclic Resultants*, Journal of Symbolic Computation
39(6), 653--669 (2005), DOI
[`10.1016/j.jsc.2005.01.001`](https://doi.org/10.1016/j.jsc.2005.01.001),
arXiv [`math/0401220`](https://arxiv.org/abs/math/0401220).

Used for the source-standard definition and reconstruction role of cyclic
resultants.  It does not provide an H6 prime correspondence.

### Polynomial recurrences

Christopher J. Hillar and Lionel Levine, *Polynomial Recurrences and Cyclic
Resultants*, arXiv
[`math/0411414`](https://arxiv.org/abs/math/0411414) (2004).

Used only to position all-index recurrence structure.  A recurrence for one
minimal polynomial is not promoted to a global H6 determinant.

### Primitive divisors in algebraic number fields

L. P. Postnikova and A. Schinzel, *Primitive Divisors of the Expression
$a^n-b^n$ in Algebraic Number Fields*, Mathematics of the USSR-Sbornik 4(2),
153--159 (1968), DOI
[`10.1070/SM1968v004n02ABEH002783`](https://doi.org/10.1070/SM1968v004n02ABEH002783).

Used as general prime-ideal context.  No all-prime distribution statement is
borrowed.

### Quadratic Lehmer--Pierce sequences

Anthony Flatters, *Primitive Divisors of Some Lehmer--Pierce Sequences*,
arXiv [`0708.2190`](https://arxiv.org/abs/0708.2190) (2007).

Theorem 1.4 applies to the period-four multiplier because it is a positive
real-quadratic unit of norm one.  It gives a primitive rational divisor for
every term beyond 12.  The period-one and period-three multiplier fields have
degree four, so this exact theorem is not applied to them.

## Metadata verification

- Hillar's journal metadata were verified through Crossref and arXiv.
- Postnikova--Schinzel metadata were verified through Crossref and MathNet.
- Hillar--Levine and Flatters metadata were verified on their arXiv records.
- No bibliography entry was generated from memory alone.

## Repository sources

The implementation hash-locks eight HCS-P46--P48 artifacts.  The P46 theorem
supplies algebraic-unit monodromy; P48 supplies exact primitive period 1, 3,
and 4 multipliers.  P49 introduces the signed period-three polynomial and
checks it as $f_{-L_3}(X)=f_{L_3}(-X)$.

## Source ceiling

No audited source proves:

- primitive divisors for both quartic H6 sequences with the exact required
  uniformity;
- a common all-orbit prime-ideal packet measure;
- an all-rational-prime von Mangoldt trace;
- analytic continuation or a functional equation for that packet trace;
- a Hilbert--Pólya operator.

Those statements remain `OPEN`.
