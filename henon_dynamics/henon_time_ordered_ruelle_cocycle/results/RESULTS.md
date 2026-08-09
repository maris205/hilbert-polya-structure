# HCS-C22 T1--T3 results

**Verification status:** exact-rational producer PASS; nonimporting checker
PASS; 11/11 regression tests PASS

## Gate summary

| Gate | Result | Evidence |
|---|---|---|
| T1 common survivor | PASS | exact rational covering, contraction, and cone proof |
| T2 complete chronology aggregate | PASS | rational interval certificate over all 29/49 branches |
| T3 global collapse controls | PASS | Gröbner, Hill, and global-residue proof |
| T4 local determinant convergence | OPEN | not attempted in this artifact |
| T5 common nuclear operator | OPEN | next kill gate |

## T1 constants

\[
\frac{144}{25}<a<\frac{51}{8}
\]

is the strict signed-root self-map window for the frozen sign boxes, while

\[
\frac{289}{50}<a<\frac{99}{16}
\]

is the exact common strict-covering window for the four frozen h-sets.  The
frozen interval \([59/10,61/10]\) lies strictly inside both.

The uniform contraction and minimum covering margin are

\[
\theta=\sqrt{240/1003}<0.49,
\qquad
m_{\mathrm{exit}}=7/720.
\]

## T2 complete aggregate

Define

\[
Q_w(1)=\sum_{\Gamma\text{ above }[w]}|\Lambda_u(\Gamma)|^{-1}.
\]

| Matched control | Branches per sector | Certified difference |
|---|---:|---:|
| `0000101` minus `0001001`, same cyclic bigrams | 29 | \(-1.3708583106961748546651416963\times10^{-8}\) |
| `00101011` minus `00101101`, same cyclic trigrams | 49 | \(+1.7085211587469334242670389161\times10^{-9}\) |

The rational difference intervals have widths \(5.8\times10^{-64}\) and
\(9.8\times10^{-64}\), so both exclude zero by more than fifty decimal
orders beyond their enclosure width.

All branchwise cyclic and reversal mappings pass for both members of both
pairs.  Reversal is not removed from the Euler multiplicity.

## T3 collapse

For a nonzero length-\(n\) protocol, the cyclic fixed scheme has length
\(2^n\).  In the nondegenerate case,

\[
\sum_{\operatorname{Fix}F_w}\frac1{\det(I-DF_w)}=0,
\]

\[
\sum_{\operatorname{Fix}F_w}
\frac{\operatorname{tr}DF_w}{\det(I-DF_w)}=-2^n.
\]

Consequently the unit-numerator all-complex signed **residue determinant** is
identically one.  It agrees with the ordinary pointwise signed flat
determinant only if every repeated fixed scheme is reduced and
nondegenerate.  This is not a claim about the restricted local real absolute
or instability-weighted determinant, nor about determinants with other
insertions.

## Artifacts

- `c22_certificate.json`: full 90-digit rational interval certificate,
  including every branch.
- `c22_independent_check.json`: hash-bound nonimporting reconstruction.
- `TEST_REPORT.md`: commands and verification outcome.

No finite operator spectrum or Riemann-zero comparison is present.
