# Narrative Report

SD-C12 attacks a narrow analytic bottleneck left by the preceding symbolic
models. A diagonal tensor-prime transfer has the desired primitive loops but
is trace class only in `Re(s)>1`. Pairing adjacent entropy ranks changes the
question from the size of two divergent sectors to their relative difference.
The identity

```text
a^(-s)-b^(-s)=s integral_a^b x^(-s-1) dx
```

then sums over disjoint entropy intervals. It moves the difference into trace
class on every half-plane `Re(s)>0` without discarding the `r=1` trace.

The resulting Fredholm object is exact. Its product is the ratio of odd-rank
and even-rank prime factors, and its logarithm retains the relative trace at
every repetition. Multiplication by the reflected copy at `1-s` produces a
holomorphic determinant on the full critical strip. Unlike Paper09's balanced
double, this determinant is not vertically sterile: the second derivative of
its logarithm at the center of the critical line is strictly positive.

The improvement does not solve the arithmetic orientation problem. The same
grading that cancels the zero-order divergence assigns a fixed sign to each
prime according to entropy rank. That sign is present at every repetition;
it is not the power of an orbit holonomy. The logarithmic derivative therefore
contains alternating-rank von Mangoldt terms instead of the uniformly positive
prime-power ledger. Worse for the divisor goal, the reflected determinant is
zero-free throughout its proved strip.

A finite-block rigidity theorem turns this tradeoff into a reusable boundary.
For a fixed local coefficient pattern on consecutive asymptotically local
atoms, extension to all `Re(s)>0` is equivalent to zero block sum. The
all-positive pattern cannot satisfy that condition. Shifted pairings, larger
balanced blocks, and random increasing inventories retain the analytic result,
so the mechanism proves too much to identify primes or an RH-like divisor.

The next Symbolic-Dynamics-only branch should replace sector parity with an
entropy-rank Bloch unitary twist. Its first obligation is to determine whether
Fourier averaging can cancel the zero-order divergence while producing the
correct repetition-dependent phase, rather than another fixed signed ledger.

Route evaluation remains stricter than operator existence. The relative
determinant is exact as an auxiliary object, but A1 fails the target ledger,
and the reflected product is obtained tautologically by multiplication with
the copy at `1-s`. Therefore A3 fails rather than passes partially, and the
overall verdict is `ROUTE_A_REJECTED / STOP_SCOPED / PROVES_TOO_MUCH`.
