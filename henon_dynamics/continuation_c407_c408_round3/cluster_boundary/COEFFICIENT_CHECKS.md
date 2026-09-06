# New effective-potential coefficient checks

2026-09-06. Command actually completed successfully:

`python henon_dynamics/continuation_c407_c408_round3/cluster_boundary/check_effective_coefficients.py`

It returned `all_assertions_passed`. This is a bounded exact SymPy check of
the newly derived truncated formal potentials and leading complementary
corrections. It is not a census and does not compute the original cyclic
local algebras. The coordinator independently owns that separate check.

| k | path L=3 coefficient | L=7 | L=11 | minimum gradient-residual order | cycle-axis coefficient | mixed quartic coefficient |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | -23 | -46 | -69 | 4 | -5 | -8 |
| 5 | 12 | 24 | 36 | 6 | 23/4 | 1 |
| 7 | 24 | 48 | 72 | 8 | 47/4 | 1 |

All path and axis leading degrees were exactly 2k. The script also verifies
that all full-gradient residuals at the proposed first complementary
correction have order at least k+1. Thus these finite checks target the
delicate coefficient and residual claims in Sections 6 and 7 of the proof
package, including the exceptional k=3 contributions.

The proof for arbitrary k and arbitrary path/cycle size remains the formal
argument in PROOF_PACKAGE.md. The checks are corroboration, not a substitute
for those quantified proofs. None of the frozen round-2 checks was rerun.

After adding the same-contract generating-function consequence, the current
script was run again and completed with all assertions passing. It also
enumerates labeled proper subsets of C_m for 1<=m<=8 with k symbolic and
checks their exact run-weight sum against the four-by-four companion-matrix
power trace plus `1+4(k-1)*1_(4|m)`. This finite Boolean-word calculation is
not a periodic-solution census. In particular it independently gives

`ell_1=2, ell_2=2k, ell_3=3k+2, ell_4=2k^2+12k`.

The all-m proof of this generating function is the marked-separator double
count in Section 10, not the eight-word-size check.
