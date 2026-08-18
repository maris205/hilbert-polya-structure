# Research Question Brief — Paper 48

## Narrow question

For every integer radix \(b\ge2\), what is the exact Schatten critical
surface of the positive-integer adjacency operator whose endpoints add
without a base-\(b\) carry, and how do the finite digit singular values
control the infinite Dirichlet-weighted shell operator including equality?

## Frozen answer

Define

$$
B_{b,s}(m,n)
=\mathbf 1_{\{\text{the base-}b\text{ addition of }m,n
\text{ has no carry}\}}(mn)^{-s/2}
$$

on \(\ell^2(\mathbb N)\). Let

$$
C_b(a,c)=\mathbf 1_{\{a+c<b\}},
\qquad 0\le a,c<b,
$$

and for \(1\le q<\infty\) put

$$
\kappa_{b,q}=\|C_b\|_{S_q}.
$$

Then

$$
B_{b,s}\in S_q
\iff
\Re s>\max\{1,\log_b\kappa_{b,q}\}.
$$

Boundedness, compactness, and Hilbert–Schmidt membership are all equivalent
to \(\Re s>1\). If

$$
\tau_b=\|C_b\|_{S_1},
\qquad \alpha_b=\log_b\tau_b,
$$

then \(\tau_b>b\) and trace class is equivalent to
\(\Re s>\alpha_b\), with equality excluded.

The finite singular values are

$$
\left[
2\sin\frac{(2j-1)\pi}{4b+2}
\right]^{-1},
\qquad 1\le j\le b.
$$

The trace in the trace-class domain is the Dirichlet series over positive
integers whose digits are all at most \(\lfloor(b-1)/2\rfloor\). It is
identically zero for \(b=2\); for \(b>2\) it is positive on the real
trace-class half-line, with no complex zero-free claim. The least-period set
is \(\{r\ge2\}\) for \(b=2\) and all positive integers for \(b>2\).

## Contribution boundary

Kummer/Lucas carry criteria, finite Boolean/Pascal/disjointness matrices,
Kronecker products, and their finite spectra receive zero novelty credit.
The eligible result is the infinite weighted all-radix theorem: exact shell
norms, the strict \(S_q\) surface, equality pinching including the binary
exception, and the positive-vertex trace/period ledger.

## Non-goals

- no novelty claim for finite digit matrices or binomial parity;
- no use of Kummer outside prime-radix corollaries;
- no unweighted Artin–Mazur zeta, since fixed-point counts are infinite;
- no split binary paper;
- no rational-prime primitive claim;
- no target-zero fit or Hilbert–Pólya claim;
- no authority or publication authorization.

## Status

PROVABLE AS STATED / PREAUTHORITY THEORY INPUT
