# An Area-Preserving Hénon-Map Model for the Riemann Zeros

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19084735.svg)](https://doi.org/10.5281/zenodo.19084735)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

Code repository for the manuscript **"An Area-Preserving Hénon-Map Model for the Riemann Zeros: A Deterministic-Dynamics Approach with Quantum and Dissipative Solvers"** (Liang Wang).

## 1. What this work does

The Hilbert–Pólya viewpoint suggests asking whether the ordinates of the nontrivial Riemann zeros could be the spectrum of some self-adjoint operator. This repository explores one concrete candidate setting: the area-preserving Hénon map ($b=-1$, so $\det J=1$) near the edge of chaos. From the map's continuum limit we build a quartic-regularized Hamiltonian and compare its spectrum to the first 100 zeros with two numerically independent eigensolvers — a unitary Fourier (quantum) solver and a Markovian (dissipative) solver.

**These are numerical observations, not proofs.** We do not claim to have identified the Hilbert–Pólya operator, nor that the spectrum of our operator equals the zeros. A table in the manuscript classifies every statement as established (cited literature), published numerical observation, structural argument, numerical observation, heuristic, qualitative, or explicitly not claimed. Random matrix theory is treated as complementary, not as something this work challenges: the GUE correspondence concerns *unfolded local* statistics, and our local-statistics diagnostics (nearest-neighbor spacing, pair correlation, number variance, spectral rigidity) are reported as a consistency check, not as the distinctive result.

### Where the idea comes from

This is the third step in a sequence of numerical studies:

1. **Primes.** An observed symbolic correspondence between the Logistic map at its band-merging point and the prime sieve, with a quantity numerically close to the Hardy–Littlewood twin-prime constant appearing as a fixed point (Wang, *Research in Mathematics* 13(1), 2026). This is a reported numerical correspondence, not a proved isomorphism.
2. **Low-order zeros.** A fitted numerical correspondence between a non-autonomous quadratic map and the low-order zeros, with few free parameters and with its limitations stated explicitly (Wang, *Mathematical and Computational Applications* **2026**, 31(5), 193, [doi:10.3390/mca31050193](https://doi.org/10.3390/mca31050193)).
3. **This work.** The same programme in an area-preserving setting that can in principle host a unitary spectrum, compared against the first 100 zeros.

### Headline numbers (single-point anchoring, first 100 zeros)

| Solver | Best MAPE | Robust range |
| :--- | :--- | :--- |
| Unitary Fourier (quantum) | 2.3% (sharp optimum) | ≈10–20% across grids and regularizations |
| Markovian (dissipative) | 6.5% | — |

A globally fitted GUE surrogate shows systematic deviation in the same counting-function comparison. See the manuscript for the full caveats (finite-resolution aliasing, optimizer variability, the open tension between Floquet-eigenphase and reconstructed-energy statistics).

## 2. Figures

![Local spectral diagnostics](8-Spectral_Diagnostics.png)
*Nearest-neighbor spacing, pair correlation, number variance, and spectral rigidity for the Hénon Floquet eigenphases (red) and the true Riemann zeros (black), against GUE (blue) and Poisson (green). The eigenphases show GUE-type level repulsion; such statistics are generic to chaotic systems, so this is a consistency check rather than the distinctive result.*

![Comparison to 100 zeros](6-GUE_vs_1d2d-Quantum_White.png)
*Counting-function comparison against the first 100 zeros: the two solvers versus a globally fitted GUE surrogate. Native MAE at this scale: quantum solver 2.29%, Markovian solver 6.52%.*

## 3. Repository contents

| File | What it does |
| :--- | :--- |
| `1-henon_attractor.ipynb` | Phase portraits of the area-preserving Hénon map versus the control parameter $a$ |
| `2-henon_param_scan.ipynb` | Scan of orbit survival and the symbolic LL statistic versus $a$ |
| `3-henon_param_a_1.005.ipynb` | Numerical determination of the first homoclinic tangency ($a_c \approx 1.0056$) |
| `4-henon_param_a_1.02.ipynb` | Heuristic consistency check linking $a \approx 1.02$ to the solver resolution |
| `5-henon_match_6_zeros.ipynb` | Low-order comparison (first 6 zeros) |
| `6-heon_100_zeros_match.ipynb` | Comparison against the first 100 zeros, with the GUE surrogate |
| `7-henon_ustc_100_zeros_match.ipynb` | Qualitative comparison with a published hardware error profile |
| `8-spectral_diagnostics.py` | NNSD, pair correlation, number variance, spectral rigidity |
| `9-robustness_sensitivity.py`, `9b-robustness_reoptimized.py` | Sensitivity and re-optimized robustness of the fit |
| `5-…`, `6-…`, `9-…` `.py` / `.log` | Parameter scans, ablation tests, and their raw logs |

The manuscript source lives in `paper_npj/` (`main.tex`, `references.bib`, `figures/`); `paper/` holds the earlier Frontiers in Physics revision and its reviewer response.

## 4. Citation

```bibtex
@article{wang2026henon,
  author  = {Wang, Liang},
  title   = {An Area-Preserving {Hénon}-Map Model for the {Riemann} Zeros:
             A Deterministic-Dynamics Approach with Quantum and Dissipative Solvers},
  year    = {2026},
  note    = {Manuscript; code and data at \url{https://github.com/maris205/riemann_henon}}
}
```

The archived code snapshot is [10.5281/zenodo.19084735](https://doi.org/10.5281/zenodo.19084735).
