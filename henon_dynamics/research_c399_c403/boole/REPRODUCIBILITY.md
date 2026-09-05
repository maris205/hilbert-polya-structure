# Exact admission evidence

This directory is author proof-admission material, not a paper/release
package. It has no PDF, formal evaluation or publication manifest.

## Actual command and result

Run from /root/autodl-tmp/hilbert-polya-structure:

    python henon_dynamics/research_c399_c403/boole/exact_check.py

The command actually completed with exit status 0 on 2026-09-05, using
Python 3.12.3 and SymPy 1.14.0. Its stdout is saved, unchanged, as
EXACT_CHECK_OUTPUT.json. The script is read-only apart from normal runtime
activity outside this directory and prints its own SHA256. It does not
write the output file or consume that file as expected evidence.

Script SHA256:
9c4a7dd0af9c2afc90fc4294d29ee998e1214d4e40ef64f9545c9594cbf35c2b.

## What was independently computed

For $b=1$, $a=1/4,1/2,3/4,1,2$ and $n=1,\ldots,4$, the script recursively
constructs rational-map numerators and denominators. It checks they remain
coprime, excludes fixed poles, checks squarefreeness when the fixed
polynomial is nonconstant, and counts its real roots by exact Sturm
methods. No floating-point root finder is involved.

If the iterate is $U/V$ and $P=U-xV$, then at a simple fixed root $r$,
$(T^n)'(r)-1=P'(r)/V(r)$. Partial fractions give
$$
\sum_{P(r)=0}\frac{V(r)}{P'(r)}
=\frac{[x^{\deg P-1}](V\bmod P)}{\operatorname{LC}(P)}.
$$
This quotient-ring computation reconstructs the sum over all finite
complex roots without evaluating the closed formula as its computation.
Only the subcritical two nonreal fixed-point contributions are then
discarded. The resulting real sums and Sturm counts are compared with the
proof's formulas: 40 comparisons. This is a meaningful independent
algebraic path for the selected finite instances, not a separate
independent all-parameter theorem.

Additional checks comprise 59 domain/squarefree guards, 18 critical
cubic/quintic/index identities for $n=1,\ldots,6$, and 22 exact algebra
checks covering fixed-order two-sided limits, the first resonance and
Cayley conjugacy. Total executed checks: 139, in the four separately
reported categories. Counts are not a quality score.

## What these tests do not establish

The data do not prove all periods, all parameters, Cantor completeness,
global divisor classification or local uniform convergence of an infinite
series. Those are proof obligations addressed in PROOF_PACKAGE.md.
The limit checks are at fixed order only. The scale $b$ is normalized in
the finite census, and its full invariance is proved, not sampled.
No GPU experiment, numerical target-zero fit, external-model review,
arithmetic-control PASS or release tamper audit is represented by this run.

The proof and source audit still require independent internal admission
review before any paper-level freeze. No formal C number has been assigned.
