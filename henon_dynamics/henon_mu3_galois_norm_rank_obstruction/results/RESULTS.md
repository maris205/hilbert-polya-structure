# HCS-C45 exact results

## Ordinary norm

For every split prime \(p\le499\), exact enumeration verifies

\[
N_{p,1}(0)=p-3,
\qquad C_{p,1}=-6,
\qquad \operatorname{vdeg}N_p=2(p-1).
\]

There are 45 primes in the frozen ledger.  The largest certified ordinary
norm virtual degree is \(996\), at \(p=499\).  Adding a rational prefactor
whose absolute virtual degree is bounded by a fixed \(M\) leaves the exact
triangle lower bound \(2(p-1)-M\); hence it cannot give uniformly bounded
finite rank.

## Normalized logarithmic norm

The exact first normalized moment is

\[
c_{p,1}=\frac{-6}{(p-1)/2}=\frac{-12}{p-1}.
\]

Together with the uniform higher-moment estimate

\[
|c_{p,n}|\le4\,4^n\quad(n\ge2),
\]

this gives a locally uniform, nonzero Euler germ on

\[
\operatorname{Re}s>\frac12.
\]

This is the strongest positive analytic result of C45.  It does not by itself
produce a rational/Fredholm determinant: divisibility of every divisor
multiplicity of \(N_p\) by \(d_p=(p-1)/2\) is still required.

## Frozen chronological second moments

| \(p\) | \(N_{p,2}(0)\) | \(C_{p,2}\) | \(c_{p,2}\) | \(C_{p,2}+6\) |
|---:|---:|---:|---:|---:|
| 7 | 322 | -6 | -2 | 0 |
| 13 | 2158 | -6 | -1 | 0 |
| 19 | 6802 | -6 | -2/3 | 0 |
| 31 | 29326 | -30 | -2 | -24 |
| 37 | 50986 | 18 | 1 | 24 |
| 43 | 78346 | -54 | -18/7 | -48 |
| 61 | 227530 | 18 | 3/5 | 24 |
| 67 | 302170 | 42 | 14/11 | 48 |
| 73 | 387922 | -30 | -5/6 | -24 |
| 79 | 494698 | 42 | 14/13 | 48 |
| 97 | 911218 | -30 | -5/8 | -24 |

Thus multiplying by \((1-z)^6\) cancels only the first logarithmic
coefficient.  It is not a certified all-order Tate cancellation.
