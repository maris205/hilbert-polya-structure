# Bounded computational checks

Run date: 2026-09-05. Result:
`FINITE_SANITY_PASS_NOT_INTERVAL_CERTIFIED` (exit 0).
Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

The unchanged [sanity.py](sanity.py) was read in full before execution.
It is a deterministic CPU-only finite calculation, without network,
target-zero data, imported producer results, or fitting of asymptotic
coefficients. [SANITY_OUTPUT.json](SANITY_OUTPUT.json) preserves the
actual complete standard output, including the coarse-grid discrepancy.
The output was captured from the process and saved using `apply_patch`;
a read-back comparison was byte-equal to the captured stdout. This
read-back is an integrity check, not another mathematical test.

Command from `/root/autodl-tmp/hilbert-polya-structure`:

```sh
python3 henon_dynamics/research_c399_c403/delta_comb/sanity.py
```

Environment: Python 3.12.3, SymPy 1.14.0, mpmath 1.3.0, Linux x86_64.
No packages were installed or settings changed. The script performs
high-precision bounds at 70 decimal digits; spectral routines use
ordinary binary64 arithmetic and are not interval certified.

## Exact and high-precision lanes

- Three symbolic differences vanish exactly: exponential-potential
  coefficient, heat-trace constant, and zeta principal part.
- The first 1,000 harmonic-cell endpoint pairs satisfy the tested
  exponential bound; maximum observed deviation is
  `0.5262051115958638804748887`, below 1. This is a finite
  high-precision check, not the all-cell proof.
- For `f(x)=x exp(-0.4 x)`, `kappa=1.5`, and 1,200 cells, the
  sampled-versus-integrated difference is
  `0.2534272797325425665304724`, versus the global bound `4.6875`.
  The cell integrals use an explicit antiderivative independently of
  the sampled sum. This tests one function and finite truncation only.

Exact integer divisor comparisons:

| Integer frequency | Direct pair count | Hyperbola count |
| ---: | ---: | ---: |
| 1 | 1 | 1 |
| 2 | 3 | 3 |
| 10 | 27 | 27 |
| 100 | 482 | 482 |
| 1000 | 7069 | 7069 |

## Spectral lanes and observed values

The first numerical method propagates exact free solutions and delta
jumps using a rounded Prüfer phase. The second independently assembles
piecewise-linear stiffness and consistent mass matrices, then counts
negative LDL pivots of `K-k^2 M`. It uses neither transfer matrices nor
trigonometry. Both calculate finite-head Dirichlet and Robin counts;
their matching integers are **numerical observations**, not certified
infinite-spectrum counts. The finite-element lane uses strict counts,
and no interval separation of test energies from eigenvalues was proved.

Let `F_kappa(k)=2k log k+[log(4 pi/kappa)+gamma-2]k`.
The following table is transcribed from the complete saved output.
`c_num` is the common shooting/two-finest-grid head count, not a
rigorously certified value of `N_kappa(k^2)`.

| kappa | k | Cells | c_num | F_kappa(k) | c_num - F_kappa(k) |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 0.5 | 10 | 2545 | 64 | 64.065572784 | -0.065572784 |
| 0.5 | 20 | 10085 | 156 | 155.857032791 | 0.142967209 |
| 0.5 | 40 | 40244 | 367 | 367.165840026 | -0.165840026 |
| 1 | 10 | 1282 | 57 | 57.134100979 | -0.134100979 |
| 1 | 20 | 5052 | 142 | 141.994089180 | 0.005910820 |
| 1 | 40 | 20132 | 339 | 339.439952804 | -0.439952804 |
| 2 | 10 | 660 | 50 | 50.202629173 | -0.202629173 |
| 2 | 20 | 2545 | 128 | 128.131145568 | -0.131145568 |
| 2 | 40 | 10085 | 312 | 311.714065582 | 0.285934418 |

All nine cases agree between the original and doubled shooting cutoff
and the FEM grids with maximum free phase 0.02 and 0.01. At those
levels the Dirichlet and Robin head counts also agree. The script
requires these equalities but does not require agreement on the two
coarser meshes. At `kappa=2, k=40`, the 0.08 and 0.04 meshes count
311, whereas the finer meshes and shooting count 312. Thus eight,
not nine, cases agree at **all** four FEM levels. This visible failure
of coarse discretization is retained and should not be hidden under PASS.

The smallest reported relative LDL pivot at the finest level is about
`7.844349e-6`; this is a diagnostic, not a bound on accumulated
roundoff or a spectral-gap certificate. Selected counts are numerically
stable under the tested refinements, but untested regimes are unknown.
The residuals in the table have absolute value below 0.44. Nine such
values cannot prove the stated logarithmic error, its constant, or
any stronger bounded-error claim.

## Why the cutoff is sensible, and what is still numerical

Cutoffs are `ceil(4 pi (k^2+kappa^2+1)/kappa)`. Splitting the
form at `x_N` and assigning the cut-vertex penalty to the head gives
a Robin head and a free-left-end tail for a lower comparison; a
Dirichlet split gives the upper comparison. The sampling estimate on
the tail (it does not need a left Dirichlet trace), followed by Young's
inequality with epsilon 1/2, yields the analytic tail lower bound

`kappa (N+1)/pi - 2 kappa^2`.

For the selected cutoffs its computed ratio to `k^2` lies between
4.0029 and 4.1281, well above one. This explains the tested head/tail
bracket. It does not turn rounded shooting or non-certified FEM
inertia into rigorous head counts. No interval arithmetic, a posteriori
eigenvalue enclosure, heat-trace numerical sum, spectral-zeta numerical
continuation, or strong-coupling numerical limit is claimed.

## Proof and internal-review relationship

The analytical claims are justified by the complete
[proof](PROOF_PACKAGE.md), not by these tests. The existing independent
current-team [mathematical review](../boole/REVIEW_OF_DELTA_COMB.md)
addresses that proof's actual 13-step argument and finds no blocking
mathematical gap. Its recorded proof SHA256 equals the current proof
hash below. That review explicitly did not validate this later numerical
script. This closeout inspected and executed the script but is not a
new independent proof review or journal peer review. The proof's old
"review pending" status text was left untouched to preserve its snapshot.

No proof/script change was needed. No extra experiment is necessary
for the proof-only claims; certified spectral values would require a
different, separately justified enclosure method if later claimed.

## Input/output identity

| Artifact | SHA256 |
| --- | --- |
| `PROOF_PACKAGE.md` | `7a63727caee39ba2926e2fe93dd249df17ea9ec4ba5ddf7b760432f02898b0af` |
| `sanity.py` | `0796b98534e6d9976608524dbb9df217208b1d501c649e7c2b32e3397b2070c5` |
| `SANITY_OUTPUT.json` | `68b7338ce7fbc867430bd0b513f1fb57bb5a21861d7a1a8e651d8dfa04f43641` |
| `../boole/REVIEW_OF_DELTA_COMB.md` | `ce6da9327d1b270774e961feb1d61ee37c71573e8723b738b5eb64064abe4ca8` |

These hashes establish artifact identity only. They do not certify
mathematics, numerical accuracy, completeness of prior-art searching,
paper admission, a release manifest, or target arithmetic.
