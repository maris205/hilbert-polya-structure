# SD-C12 Derivation Package

## Outcome

Entropy-adjacent rank pairing produces a genuine relative trace-class
transfer on every half-plane Re(s)>0:

\[
D_s^+-B_s
=\operatorname{diag}\bigl(
p_{2n-1}^{-s}-p_{2n}^{-s}\bigr)\in S_1,
\]

where odd entropy ranks are the plus/super-even numerator sector and even
entropy ranks are the minus/super-odd denominator sector. Its relative
Fredholm determinant is

\[
R(s,z)=\prod_{n\ge1}
\frac{1-zp_{2n-1}^{-s}}{1-zp_{2n}^{-s}}.
\]

The reflection product

\[
H(s,z)=R(s,z)R(1-s,z)
\]

is symmetric and nonconstant on the critical line, but at z=1 it is
zero-free throughout 0<Re(s)<1. More importantly, the relative trace carries
a fixed negative sign on every even-rank atom at every repetition. It is not
the uniformly positive prime-power ledger required by Route A.

The final status is therefore:

    PROVE: relative trace-class and Fredholm determinant
    PROVE: reflection and critical-line motion
    STOP:  positive Euler orientation
    STOP:  divisor (proved zero-free)
    STOP:  specificity (bounded-local controls reproduce it)
    ROUTE_A_REJECTED / ROUTE_B_LOCKED

## Frozen source and parity convention

The atom inventory is the tensor-indecomposable finite full shifts F_p,
generated internally and ordered by entropy log(p). Adjacent ranks form
blocks

\[
(p_{2n-1}\mid p_{2n}).
\]

The writer-frozen convention is:

- odd entropy rank p_(2n-1): plus / super-even / numerator;
- even entropy rank p_(2n): minus / super-odd / denominator.

Let

\[
D_s^+=\operatorname{diag}(p_{2n-1}^{-s}),\qquad
B_s=U^*D_s^-U=\operatorname{diag}(p_{2n}^{-s}),
\]

with U the canonical adjacent-rank pairing. The primary normalization is
z=1. No prime table, target-zero data, fitted phase, scale, offset, pairing,
or sign enters the construction.

## 1. Paired trace class on Re(s)>0

For a<b and sigma=Re(s)>0,

\[
a^{-s}-b^{-s}
=s\int_a^b x^{-s-1}\,dx.
\]

Therefore

\[
|a^{-s}-b^{-s}|
\le |s|\int_a^b x^{-\sigma-1}\,dx.
\]

The intervals [p_(2n-1),p_(2n)] are disjoint, so

\[
\boxed{
\|D_s^+-B_s\|_1
\le \frac{|s|}{\sigma}2^{-\sigma}.}
\]

After N pairs, the same integral gives the explicit tail bound

\[
\boxed{
\sum_{n>N}|p_{2n-1}^{-s}-p_{2n}^{-s}|
\le \frac{|s|}{\sigma}p_{2N+1}^{-\sigma}.}
\]

For every repetition r>=1,

\[
\|(D_s^+)^r-B_s^r\|_1
\le \frac{|s|}{\sigma}2^{-r\sigma}.
\]

These locally uniform estimates prove trace-norm holomorphy on Re(s)>0.

The executable generated 32,769 tensor atoms, giving 16,384 complete pairs
and next atom 386,117. It audited sigma=0.1,0.25,0.5,1 and the complex points
0.1+3i, 0.25+10i, 0.5+25i, and 1+40i at pair cutoffs
16,64,256,1024,4096,16384.

For real s, the N=16,384 trace-norm partial sums were:

| sigma | partial l1 sum | rigorous remaining-tail bound |
|---:|---:|---:|
| 0.10 | 0.316948 | 0.276267 |
| 0.25 | 0.385244 | 0.040116 |
| 0.50 | 0.347029 | 0.001609 |
| 1.00 | 0.269605 | 2.590e-6 |

The bounds are deliberately conservative at small sigma; they certify the
infinite tail rather than fitting an extrapolation. At N=4,096 the observed
Cauchy increments to N=16,384 were 0.023061, 0.009439, 0.000934, and
4.730e-6, all below their rigorous tail bounds.

## 2. Exact coefficient and trace-log ledger

For a finite prefix of N pairs,

\[
R_N(s,z)=\prod_{n=1}^N
\frac{1-zp_{2n-1}^{-s}}{1-zp_{2n}^{-s}}.
\]

Inside the local logarithm branch,

\[
\boxed{
\log R_N(s,z)
=-\sum_{r\ge1}\frac{z^r}{r}
\sum_{n=1}^N
\left(p_{2n-1}^{-rs}-p_{2n}^{-rs}\right).}
\]

The code verifies opaque-variable coefficients for three pairs and
repetitions r=1,...,10. It computes the rational-product Taylor coefficients
by exact truncated local-factor convolution and independently verifies them
by multiplying back the complete denominator. Every coefficient and every
trace-log coefficient is exact.

For Re(s)>0 and |z|2^(-Re(s))<1,

\[
(I-zD_s^+)(I-zB_s)^{-1}-I
=-z(D_s^+-B_s)(I-zB_s)^{-1}\in S_1.
\]

Thus R is an ordinary Fredholm determinant of an I+S_1 relative quotient.
At z=1 the norm condition holds on all Re(s)>0.

Neither individual factor det(I-zD_s^+) nor det(I-zB_s) is claimed to exist
throughout that half-plane. The quotient is the invariant object.

## 3. Reflection product and strict motion

Both R(s,1) and R(1-s,1) exist precisely on the common strip
0<Re(s)<1. Multiplication gives the exact reflection relation

\[
H(s,z)=H(1-s,z).
\]

The numerical reflection residual was exactly zero at all frozen complex
points because the two scalar log factors are simply exchanged.

On s=1/2+it,

\[
H(s,1)=|R(s,1)|^2>0.
\]

Define

\[
g(x)=\frac{x^{-1/2}(\log x)^2}{(1-x^{-1/2})^2}.
\]

Then

\[
\left.\frac{d^2}{dt^2}\log H(1/2+it,1)\right|_{t=0}
=2\sum_n\bigl(g(p_{2n-1})-g(p_{2n})\bigr)>0,
\]

because g is strictly decreasing for x>1. The finite-prefix curvatures at
N=64,256,1024,4096,16384 pairs were respectively
2.0354, 2.6373, 3.0674, 3.3455, and 3.5275. The alternating-series tail
bound at the largest prefix was 0.5344. Positivity at every prefix and the
strict analytic theorem establish nonconstancy; the height grid is only a
finite illustration.

## 4. Certified zero-free strip

The local denominator bound is

\[
|1-zp^{-s}|\ge 1-|z|2^{-\sigma}.
\]

Together with paired trace-class convergence, this shows that every local
factor is nonzero and the factor-minus-one series is absolutely summable
when

\[
|z|2^{-\sigma}<1.
\]

For H, both reflected conditions give the certified strip

\[
\max(0,\log_2|z|)
<\Re(s)<
\min(1,1-\log_2|z|).
\]

At primary z=1 this is exactly 0<Re(s)<1. The relative quotient is
invertible there, and its Fredholm determinant cannot vanish:

\[
\boxed{H(s,1)\ne0\quad(0<\Re s<1).}
\]

No zero list or crossing census is used. This is a theorem-level STOP for a
critical-strip divisor, not a finite numerical absence of roots.

## 5. Pairing and inventory controls

The integral proof only needs bounded overlap/locality, not arithmetic.
The audit therefore includes:

- offsets 1, 2, and 3, implemented in blocks of width 2, 4, and 6;
- 16 independently oriented adjacent-pair controls;
- 32 random perfect pairings inside consecutive blocks of width 8;
- tensor primes, within-block shuffled primes, composites, consecutive
  integers, and bounded-gap random increasing integers.

All 32 random bounded-block pairings pass the Re(s)>0 trace-class theorem,
and all 32 have nonzero critical-line H motion. Every nonprime inventory
also passes and moves. These are PROVES_TOO_MUCH controls. They show that the
relative analytic mechanism is a bounded-local cancellation theorem, not a
prime-specific divisor mechanism.

Global random pairings are not silently included in the theorem: unbounded
pairing distance destroys the disjoint/bounded-overlap estimate and is
outside the frozen local class.

## 6. Finite-block rigidity

For one fixed coefficient pattern c_1,...,c_m on consecutive asymptotically
local blocks, discrete Abel summation shows that

\[
\sum_j c_j=0
\]

converts each block into a finite linear combination of adjacent
differences. This is sufficient for trace class on every Re(s)>0.

Under the frozen locality and reciprocal-divergence assumptions, it is also
necessary: if C=sum_j c_j is nonzero, the block at s=1 is asymptotic to C
divided by the local block scale, and the aggregate trace norm diverges.

Every all-positive pattern has sum_j c_j>0. Hence

\[
\boxed{\text{zero-sum cancellation and all-positive orientation are
incompatible in the fixed finite-block class}.}
\]

The numerical controls display the distinction. At s=1 and 4,096 blocks,
the partial l1 sums are 0.26960 for [1,-1] and 0.08219 for [1,-2,1], but
2.69002 for [1,1] and 2.72871 for [1,1,1], with the latter still growing.
Necessity comes from the theorem, not from declaring a finite growth curve
divergent.

## 7. Fixed super-parity is not a repetition cocycle

Let a be a plus-sector atom weight and b a minus-sector atom weight.
The fixed relative supertrace gives

\[
\operatorname{Str}(D^r)=a^r-b^r
\]

for every repetition r. A primitive orbit holonomy -1 instead produces

\[
a^r+(-1)^r b^r.
\]

They agree at odd repetitions and differ by -2b^r at even repetitions.
Equivalently, their products are different:

\[
\frac{1-za}{1-zb}
\quad\hbox{versus}\quad
(1-za)(1+zb).
\]

Thus the fixed negative sector cannot be reinterpreted as a legitimate
repetition-dependent orbit phase. It assigns a negative coefficient to one
rank parity at every prime power, which fails the Route-A positive
prime-power ledger.

## Claim boundary

    relative trace class on Re(s)>0:           PROVED
    all-order relative trace-log coefficients: PROVED
    relative Fredholm determinant:              PROVED
    reflection symmetry:                        PROVED
    critical-line nonconstancy:                 PROVED
    z=1 zero-free critical strip:                PROVED
    uniformly positive prime-power orientation: REFUTED
    fixed parity = cocycle phase:                REFUTED
    arithmetic specificity:                     REFUTED by controls
    target divisor / RH claim:                   NOT MADE
    fixed self-adjoint generator:                ABSENT
