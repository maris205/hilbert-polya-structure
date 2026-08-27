# P79 — Noisy FKM Delayed Irreversibility

This short paper studies a uniformly phased binary FKM de Bruijn cycle of
order \(k\), observed through independent binary symmetric emissions.

The main theorem package is:

- every consecutive block law through length \(k\) is exactly uniform;
- the first time-reversal defect occurs at length \(k+1\) for every
  \(\varepsilon\neq 1/2\);
- the length-\((k+1)\) Euclidean and total-variation reversal gaps have
  explicit BSC lower bounds;
- the process is stationary and ergodic for every noise endpoint, and has
  full support for \(0<\varepsilon<1\);
- its entropy rate is \(h_{\mathrm b}(\varepsilon)\);
- for \(\varepsilon\neq1/2\), one side recovers the persistent phase and the
  excess entropy is exactly \(k\);
- under strict nonfair noise, the observed process has infinite Markov order;
- away from fair noise it is ergodic but not mixing.

All endpoint regimes and the reversible small orders \(k=1,2\) are handled
separately in the paper.

## Build

From this directory:

    latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

The expected artifact is main.pdf.

To clean only generated LaTeX intermediates:

    latexmk -c

## Exact controls

Run:

    python code/verify_noisy_debruijn.py

The script uses only the Python standard library. It independently checks the
definition-level Lyndon concatenation against the FKM recursion, de Bruijn
block multiplicities, the oriented clean witness, exact rational noisy block
laws, the two reversal lower bounds, phase separation, periodic covariance,
entropy sandwiches, and the endpoint exceptions.

## Scope and ownership

The paper does not claim the FKM construction, the random-phase de Bruijn
law, or uniform short-block statistics as new. Mohri et al. (arXiv:2603.28499,
2026) directly use a uniformly seeded de Bruijn successor model and mention a
full-support transition perturbation. Their state is the emitted context. In
P79, errors are emissions over a latent phase that continues to advance
deterministically. The residual contribution is the explicit FKM reversal
witness, quantitative BSC survival, and the persistent-phase package of
recoverability, excess entropy, nonmixing, and infinite observed Markov order.

No external submission or priority assertion is made by this internal draft.

## Files

- main.tex — complete theorem paper and proofs
- references.bib — cited, source-verified bibliography only
- code/verify_noisy_debruijn.py — exact finite controls
- main.pdf — compiled paper
