# Bounded exact verification receipt for the wild PSL tower

2026-09-06. Scout diagnostics only; no candidate number or admission.

The new stdout-only script
[wild_psl_exact_checks.py](wild_psl_exact_checks.py) completed successfully
with exit code 0 using:

```sh
python3 -B henon_dynamics/research_c409_c413/positive_characteristic/wild_psl_exact_checks.py
```

The first complete run passed. No failed mathematical cases, hidden
restarts, large finite-field census, or old-batch retests occurred.
The prescribed primes, heights and series precision were fixed in the
script before this run. All computations below use exact finite-field
arithmetic or exact rational/integer arithmetic.

## First model: $p=5,7,11$

In the quotient field defined by
$w^p-w=v^{-(p+1)/2}$, symbolic polynomial reduction checked all $p+1$
listed roots of $X^{p+1}-tX+1$, the alternative root formula, and the
recovery of $v,w$ from three roots. The two standard generating matrix
actions preserve both the AS equation and $t$.

The discriminant was a nonzero constant in each case: $-1,1,1$ for
$p=5,7,11$ respectively. This is consistent with no finite branch point.
These checks verify the written formulas in three primes; they do not
replace the general first-model proof or its classical ownership.

## Local stability: $p=5,7,11$, precision 40

For $m=(p-1)/2$, set $A=\pi^{-m}$ and $B=A+\pi$. The script computes
their small inverse roots, normalized $m$th roots, and the associated
AS right sides in truncated Laurent series.

| $p$ | $v(s_A-s_B)$ | $v(v_A^{-(m+1)}-v_B^{-(m+1)})$ | Negative AS parts |
|---:|---:|---:|:---|
| 5 | 5 | 0 | identical |
| 7 | 7 | 0 | identical |
| 11 | 11 | 0 | identical |

Thus the stated local bound is attained in these examples. This tests a
specific pair of inputs in each prime, not every pole pair. The proof's
valuation argument supplies the general statement. Integral AS differences
being soluble uses algebraically closed residue constants, as in the proof.

## Abstract group checks: GAP, $p=5,7$, heights 1 and 2

The script builds the natural projective generators and their full
permutation wreath products. GAP's exact orders and the orbit lengths of
the stabilizer of one leaf on the *other* leaves were:

| $p$ | $n$ | $|W_n|$ | Other-leaf stabilizer orbit lengths |
|---:|---:|---:|:---|
| 5 | 1 | 60 | 5 |
| 5 | 2 | 2,799,360,000,000 | 5, 30 |
| 7 | 1 | 168 | 7 |
| 7 | 2 | 106,606,463,247,835,987,968 | 7, 56 |

There is no singleton orbit in these cases, as required by the elementary
no-simple-quotient argument. GAP does **not** compute the actual
function-field Galois groups here, and these tests do not prove the
no-simple-quotient lemma. That lemma is proved separately for every height.
The subprocess had a fixed 45-second time cap; it completed normally.

## Different and genus consistency

For $p=5,7,11$ and $n=1,2,3$, the script verified that the root-path
different plus the tame closure, the claimed inertia filtration, and
Riemann–Hurwitz all give identical integral results. In particular:

| $p$ | $n$ | $e_\infty$ | Different exponent | Genus |
|---:|---:|---:|---:|---:|
| 5 | 1 | 10 | 21 | 4 |
| 5 | 2 | 50 | 121 | 587,865,600,001 |
| 7 | 1 | 21 | 44 | 9 |
| 7 | 2 | 147 | 338 | 15,954,708,785,390,419,969 |
| 11 | 1 | 55 | 114 | 25 |

The verified lower break is $(p+1)/2$; the corresponding upper break is
$(p+1)/(p-1)$. These identities are consistency checks of the proposed
formulas, not independent calculations of geometric genera from equations.

## Boundaries

The proof and diagnostics exclude $p=2,3$. No finite-field forward-period
count, Artin–Mazur zeta, prescribed Euler factor, or spectral realization
is asserted. All-height validity and source-ownership decisions depend on
the written proof and independent reviews, not the successful finite tests.
