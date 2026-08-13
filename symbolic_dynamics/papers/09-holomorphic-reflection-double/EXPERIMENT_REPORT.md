# SD-C11 Experiment Report

## Executive result

SD-C11 passes the reflection, common-ideal, and exact trace bookkeeping
tests, but fails the only test that could make it a moving Route-A divisor.
The pure atom sector is exactly independent of s. Every tested elementary
way to recover height motion introduces mixed atom masses.

    odd channel traces:                       zero
    even identity traces:                     2 sum_p p^(-r)
    first common integer Schatten class:      S_3
    det_3:                                    exact, reflected, s-independent
    cross-atom pairing:                       moves, but mixed ledger
    random pairings:                          32/32 move, 32/32 mixed
    random upper DAGs:                        24/24 ledger pass + singular motion
    direct-sum common S_1 domain:             empty
    Route B:                                  locked

No target zeros were loaded or compared.

## Frozen exact trace census

Three atoms; opaque loop and cross coefficients; powers 1 through 12:

| power | closed paths | mixed paths | identity survivors | mixed identity survivors |
|---:|---:|---:|---:|---:|
| 1 | 0 | 0 | 0 | 0 |
| 2 | 14 | 8 | 6 | 0 |
| 3 | 0 | 0 | 0 | 0 |
| 4 | 70 | 64 | 6 | 0 |
| 5 | 0 | 0 | 0 | 0 |
| 6 | 398 | 392 | 6 | 0 |
| 7 | 0 | 0 | 0 | 0 |
| 8 | 2,310 | 2,304 | 6 | 0 |
| 9 | 0 | 0 | 0 | 0 |
| 10 | 13,454 | 13,448 | 6 | 0 |
| 11 | 0 | 0 | 0 | 0 |
| 12 | 78,406 | 78,400 | 6 | 0 |

Total: 94,652 closed paths, 94,616 mixed paths, and zero mixed identity
survivors. Specializing the two loop variables at atom p to p^{-s} and
p^{-(1-s)} gives

\[
\Phi_2(C_s^{2r})=2\sum_p p^{-r}.
\]

At infinite atom count, r=1 is the divergent prime-harmonic cutoff term.
The honest retained det_3 trace series starts with r=2.

## Common ideal and determinant

The exact common Schatten condition is

\[
1/q<\Re s<1-1/q.
\]

The strips for q=1,2 are empty. The first nonempty integer strip is
1/3<Re(s)<2/3 for q=3. The direct sum T_s direct-sum T_(1-s) therefore has
no common trace-class domain.

On the S_3 strip,

\[
\det{}_3(I-zC_s)=\prod_p(1-z^2/p)e^{z^2/p}.
\]

The table in results/det3_reflection.csv audits cutoffs
N=2,3,8,16,32. Maximum residuals were:

- determinant product: 2.36e-16;
- vertical range: 2.37e-16;
- pure-block eigenvalues +-p^(-1/2): 5.58e-16;
- channel-swap reflection: exactly 0.

These are roundoff-scale confirmations of an exact algebraic identity, not
evidence for an approximately moving zero set.

## Escape controls

### Cross-atom pairing

The exact symmetric term is

\[
\frac{2}{\sqrt{pq}}
\cosh((s-1/2)\log(q/p)).
\]

The numeric formula residual was at most 1.37e-15, and reflection residual
was zero. For p different from q the term moves but has mixed support (p,q).
All 32 random pairings moved; their critical-line C^2 ranges were between
3.4794 and 5.3157. Every one violated the pure-atom ledger by construction.

### Cocycle relations

| control | first mixed identity | conclusion |
|---|---:|---|
| independent positive alphabets | none through 10; all-order proof | candidate pass |
| shared positive alphabet | none through 10; all-order proof | PROVES_TOO_MUCH |
| inverse reflected labels | 2 | immediate mixed leakage |
| finite C5 labels | 10 | finite relation leakage |

The C5 length is ten because graph closure requires an even number of cross
steps and the group relation requires a multiple of five.

### Random upper DAGs

All 24 frozen random complex upper-DAG controls retained the exact cyclic
ledger through powers 2, 4, 6, and 8. Maximum trace residual was 8.88e-16;
maximum det_3 vertical range was 1.39e-17. Nevertheless, all 24 showed
singular/Schatten-fourth motion, with ranges from 1.462 to 33.392.

Thus cyclic sterility plus nonnormal geometry is generic in a large control
class. It cannot support an RH-like conclusion.

### Inventories

Tensor atoms, shuffled tensor atoms, composites, and matched random integers
all have zero pure-reflection vertical range. The reflection theorem is
inventory-blind once positive masses are supplied.

## Falsification verdict

The promoted SD-C11 object is coherent and analytically regularizable, but
its determinant is vertically sterile. Cross-atom pairing recovers motion
only by changing the generalized orbit ledger. Finite label relations
similarly introduce unwanted mixed identity words.

    GO:   reflection rigidity theorem
    GO:   exact det_3 product as an obstruction object
    STOP: moving pure-prime divisor
    STOP: finite-channel monomial escape
    STOP: Route B

No crossing/root census was run. In particular there is no finite
sign-change count to mistake for an argument-principle computation.

## Reproduction

From this paper directory:

    python code/sdc11_reflection_double_experiment.py
    pytest -q code/test_sdc11_reflection_double_experiment.py
    sha256sum -c results/SHA256SUMS.txt

Frozen test result: 8 passed.
