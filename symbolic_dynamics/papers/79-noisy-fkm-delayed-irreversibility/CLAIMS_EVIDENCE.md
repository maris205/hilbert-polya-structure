# Claims and evidence

| Claim | Proof/evidence |
|---|---|
| Stationarity, ergodicity, and strict-noise full support | `main.tex`, Theorem 3.1 |
| All consecutive block laws through length `k` are uniform | `main.tex`, Lemma 4.1 |
| The first reversal defect is exactly at length `k+1` | `main.tex`, Lemma 4.2 and Theorem 4.3 |
| BSC noise preserves a quantitative `l2` and total-variation defect away from fair noise | `main.tex`, Theorem 4.3 |
| Entropy rate is `h_b(epsilon)` | `main.tex`, Theorem 5.1 |
| Nonfair one-sided observations recover the persistent phase | `main.tex`, Theorem 5.2 |
| Excess entropy is `k` off fair noise and zero at fair noise | `main.tex`, Corollary 5.3 and Section 6 |
| Strictly noisy nonfair laws have infinite Markov order; endpoints are classified | `main.tex`, Theorem 5.4 and Section 6 |
| Nonfair laws are ergodic but not mixing | `main.tex`, Proposition 5.5 |
| FKM, reversal, channel, covariance, and entropy identities pass finite checks | `code/verify_noisy_debruijn.py`; counts in `CONTROL_RESULTS.md` |

Uniform de Bruijn contexts and transition-noise models are explicitly
subtracted as prior art.  The residual package concerns an oriented FKM edge
under persistent-phase emission noise.  External release remains on hold.
