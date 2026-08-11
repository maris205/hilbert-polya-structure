# HCS-C31 exact Bowen-pressure gate

## Decisive result

For the area-preserving Hénon map

\[
H_6(q,p)=(1-6q^2-p,q),
\]

on the inherited R058/R059 four-state survivor, let

\[
\tau(\omega)=\log\left|-12q_0(\omega)-\frac{123}{112}\mu_0^u(\omega)\right|
\]

be the positive adapted unstable roof. The certificate proves that the unique
zero \(h_*\) of \(P(-s\tau)\) satisfies

\[
\boxed{\frac{277980}{10^6}<h_*<\frac{277987}{10^6}}.
\]

The interval has width \(7\times10^{-6}\) and strictly contains the previous
finite-cycle numerical value \(0.277982981676189\). That old value is a
comparison only and is not used by any proof gate.

## Exhaustive cylinder construction

The radius is \(L=6\). Every length-13 state word

\[
e=(x_{-6},\ldots,x_6)
\]

is an edge from its length-12 prefix to its length-12 suffix. Exhaustive
enumeration gives 714 vertices and 1156 edges. The state-pair overlap retains
the 14 chronological signs \(\epsilon_{-7},\ldots,\epsilon_6\).

For each edge, all 14 coordinates start in their sign boxes

\[
[-5/8,-1/3]\quad\text{or}\quad[1/3,5/8].
\]

The exterior coordinates \(q_{-7},q_6\) remain free in those boxes. Up to 100
finite Jacobi rounds intersect each internal interval with the outward-rounded
signed-root image

\[
q_i=\epsilon_i\sqrt{(1-q_{i-1}-q_{i+1})/6}.
\]

Every finite round preserves every full itinerary in the cylinder; no claim
about convergence of an interval algorithm is needed. Starting with
\(\mu_{-6}\in[-1/2,1/2]\), exact interval graph transforms through
\(q_{-6},\ldots,q_{-1}\) enclose \(\mu_0\). This yields a certified interval

\[
J_e^-\le
\left|-12q_0-\frac{123}{112}\mu_0\right|
\le J_e^+
\]

on every edge cylinder. Across the complete ledger,

- the smallest \(J_e^-\) is approximately \(4.23296295047\);
- the largest \(J_e^+\) is approximately \(7.15167705543\);
- the largest edge interval width is approximately
  \(4.50866250198\times10^{-4}\);
- every lower endpoint exceeds the inherited expansion bound \(773/224\).

## Pressure enclosure and exact endpoint signs

For \(s\ge0\), define the lower- and upper-weight higher-block matrices by

\[
(M_s^-)_{uv}=\sum_{e:u\to v}(J_e^+)^{-s},
\qquad
(M_s^+)_{uv}=\sum_{e:u\to v}(J_e^-)^{-s}.
\]

Pointwise cylinder containment and pressure monotonicity give

\[
\log\rho(M_s^-)\le P(-s\tau)\le\log\rho(M_s^+).
\]

At \(s=277980/10^6\), a positive rational vector satisfies the strict lower
Collatz inequality

\[
\min_i\frac{(M_s^-v)_i}{v_i}>1,
\]

with certified margin approximately \(8.5290\times10^{-8}\). At
\(s=277987/10^6\), a second positive rational vector satisfies

\[
\max_i\frac{(M_s^+v)_i}{v_i}<1,
\]

with certified margin approximately \(1.6931\times10^{-6}\). Positivity of the
roof then gives the stated unique root bracket.

All square roots use integer `isqrt` and an outward \(10^{-50}\) grid.
Logarithms use the rational atanh series with an explicit tail; exponentials
use odd/even alternating Taylor bounds. Final weights and Collatz ratios are
pure rational numbers. Floating point supplies candidate vectors only.

## Scope

This is a meaningful all-word pressure theorem and closes the finite-cylinder
gate planned in `next_paper_henon_ruelle_operator`. Its machine interval status
is `NUMERICALLY_CERTIFIED`; the analytic implication from cylinder containment,
pressure monotonicity, and Collatz is `PROVED`. It is not a nuclearity, Fredholm-determinant,
meromorphic-continuation, prime-correspondence, or Hilbert--Pólya theorem.
Under the strict Route-A evaluator, a certified positive pressure zero does
not count as an A2 operator-zero theorem. The frozen evaluation is therefore

`(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)`, overall `ROUTE_A_REJECTED`.
