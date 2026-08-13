# SD-C12 Experiment Report

## Executive result

SD-C12 solves a real analytic problem and fails the Route-A arithmetic
problem.

The entropy-adjacent difference is trace class on every Re(s)>0, its
relative Fredholm determinant is exact, and the reflected product moves
strictly on the critical line. But the same determinant is zero-free on the
entire primary critical strip, and its fixed super-grading assigns negative
prime-power coefficients to every even-rank atom at every repetition.

    trace-class extension:    PASS / PROVED
    exact relative product:   PASS / PROVED
    reflection:               PASS / PROVED
    critical-line motion:     PASS / PROVED
    z=1 critical divisor:     FAIL / PROVED ZERO-FREE
    positive Euler ledger:    FAIL / FIXED SIGNED GRADING
    specificity:              FAIL / PROVES_TOO_MUCH
    Route B:                  LOCKED

No Riemann-zero or target-spectrum data were loaded.

## Frozen parity

The implementation matches the writer source lock:

| entropy rank | super-sector | determinant position |
|---|---|---|
| odd rank p_(2n-1) | plus / even | numerator |
| even rank p_(2n) | minus / odd | denominator |

\[
R(s,z)=\prod_n
\frac{1-zp_{2n-1}^{-s}}{1-zp_{2n}^{-s}}.
\]

Reversing orientation would invert R; no orientation was chosen after the
experiment.

## Convergence audit

The main audit used 16,384 adjacent pairs and 32,769 internally generated
tensor atoms, ending at 386,117. The exact tail certificate is

\[
\sum_{n>N}|p_{2n-1}^{-s}-p_{2n}^{-s}|
\le\frac{|s|}{\Re s}p_{2N+1}^{-\Re s}.
\]

At real s:

| sigma | l1 sum at N=4,096 | increment to N=16,384 | l1 sum at N=16,384 | certified tail after N=16,384 |
|---:|---:|---:|---:|---:|
| 0.10 | 0.293887 | 0.023061 | 0.316948 | 0.276267 |
| 0.25 | 0.375805 | 0.009439 | 0.385244 | 0.040116 |
| 0.50 | 0.346095 | 0.000934 | 0.347029 | 0.001609 |
| 1.00 | 0.269600 | 4.730e-6 | 0.269605 | 2.590e-6 |

Complex points 0.1+3i, 0.25+10i, 0.5+25i, and 1+40i were audited with the
same cutoffs. Their larger trace norms remain below the explicit
|s|/sigma tail majorants. Both raw relative traces and log R Cauchy
increments are saved in results/trace_class_convergence.csv.

## Exact finite-prefix algebra

For three opaque atom pairs and repetitions 1 through 10:

- every relative trace coefficient is exact;
- every log R coefficient equals minus sum_n(a_n^r-b_n^r)/r;
- every rational-product Taylor coefficient is exact;
- multiplying the truncated series by the complete denominator gives zero
  residual through the preregistered order.

The implementation uses local-factor polynomial convolution rather than a
floating-point fit or a global symbolic rational expansion.

## Reflection and motion

\[
H(s,z)=R(s,z)R(1-s,z)=H(1-s,z).
\]

Reflection residual was exactly zero at all frozen complex samples.
The critical-line curvature

\[
\left.\partial_t^2\log H(1/2+it,1)\right|_{t=0}>0
\]

was:

| pair cutoff | curvature | alternating tail bound |
|---:|---:|---:|
| 64 | 2.0354 | 3.4731 |
| 256 | 2.6373 | 2.2989 |
| 1,024 | 3.0674 | 1.4556 |
| 4,096 | 3.3455 | 0.8932 |
| 16,384 | 3.5275 | 0.5344 |

The exact monotonicity proof establishes strict motion. The frozen height
grid 0<=t<=80 is only a visualization of nonconstancy; it is not a root
census.

## Zero-free theorem

For primary z=1, the local factor margin and trace-class convergence give

\[
H(s,1)\ne0\qquad(0<\Re s<1).
\]

Generic certified strips were also computed. For example:

| abs(z) | certified H strip |
|---:|---|
| 0.5 | 0 < Re(s) < 1 |
| 1.0 | 0 < Re(s) < 1 |
| 1.25 | 0.321928 < Re(s) < 0.678072 |
| 1.4 | 0.485427 < Re(s) < 0.514573 |
| 1.5 | empty by this local bound |

This is a theorem-level zero-free certificate. No target zeros, sign-change
scan, or argument-principle computation is involved.

## Proves-too-much controls

### Pairings

- offsets 1, 2, 3 all pass;
- all 16 independent within-pair orientation seeds pass;
- all 32 random bounded-block pairings pass trace-class convergence;
- all 32 random bounded-block pairings show nonzero critical-line motion.

The random controls pair only inside fixed width-eight entropy blocks. This
keeps bounded overlap explicit. Unbounded global random matchings are outside
the theorem and are not presented as passes.

### Inventories

Within-block shuffled primes, composites, consecutive integers, and
bounded-gap random increasing integers all pass the same relative
trace-class mechanism and all show reflected motion. The analytic result is
therefore a local cancellation theorem, not an arithmetic selector.

### Block weights

At s=1 and 4,096 blocks:

| pattern | coefficient sum | partial l1 |
|---|---:|---:|
| [1,-1] | 0 | 0.269600 |
| [1,-2,1] | 0 | 0.082193 |
| [1,1] | 2 | 2.690017 |
| [1,1,1] | 3 | 2.728710 |

The exact finite-block theorem requires zero coefficient sum to reach every
Re(s)>0. An all-positive block cannot satisfy this linear constraint.

## Fixed parity versus cocycle phase

The exact audit gives:

| repetition r | fixed supertrace | primitive phase -1 |
|---:|---|---|
| 1 | a-b | a-b |
| 2 | a^2-b^2 | a^2+b^2 |
| 3 | a^3-b^3 | a^3-b^3 |
| 4 | a^4-b^4 | a^4+b^4 |

They agree only at odd repetitions. A fixed sector sign is not a phase
raised by repetition. Consequently the SD-C12 relative ledger cannot be
relabelled as the uniformly positive prime-power ledger or as an ordinary
orbit holonomy.

## Route-A verdict

Following the evaluator's target ledger rather than merely rewarding the
analytic theorem:

    A0_ANALYTIC_ARITHMETIC_ORIGIN
    A1_FAIL
    A2_ANALYTIC_DETERMINANT
    A3_FAIL
    A4_FAIL

    ROUTE_A_REJECTED
    STOP_SCOPED / PROVES_TOO_MUCH
    ROUTE_B_LOCKED

## Reproduction

From the Paper10 directory:

    python code/sdc12_relative_determinant_experiment.py
    pytest -q code/test_sdc12_relative_determinant_experiment.py
    sha256sum -c results/SHA256SUMS.txt

Frozen test result: 9 passed.
