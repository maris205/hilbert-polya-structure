# P104 — Monomial Toggle Contraction Cocycles

Status: **FINAL QA PASS / INTERNAL FREEZE / EXTERNAL HOLD**.

Fix `0<a<1`. At each step choose `D=diag(a,1)` with probability `1-q` or
`R=[[0,1],[a,0]]` with probability `q`, and form the left product
`M_n=A_n...A_1`. The package gives an exact finite-word monomial normal form,
the complete finite-time singular spectrum, quenched Lyapunov exponents and
folded fluctuations, and an explicit annealed moment exponent.

## Main theorem package

- With `J_0=0`, `J_t` toggling exactly when `A_t=R`, and
  `U_n=#{0<=t<n:J_t=0}`,
  `M_n=S^(J_n) diag(a^(U_n),a^(n-U_n))`.
- If `Z_n=2U_n-n`, then
  `sigma_max=a^((n-|Z_n|)/2)`,
  `sigma_min=a^((n+|Z_n|)/2)`,
  `|det M_n|=a^n`, and `kappa_2=a^(-|Z_n|)`.
- At `q=0`, the quenched exponents are `(0,log a)`. For every `0<q<=1`,
  both are `(log a)/2`; the endpoint `q=1` has bounded parity splitting.
- For `0<q<1`, `Z_n/sqrt(n)` converges to
  `N(0,(1-q)/q)`. The centered log singular values therefore converge to
  positive and negative folded normal laws, and the log condition number
  has the corresponding positive folded law.
- For `s>0`, put `theta=-(s/2)log a` and `r=1-q`. The order-`s` annealed
  log-moment exponent is
  `s log(a)/2 + log(r cosh(theta)+sqrt(r^2 cosh(theta)^2-(r-q)))`.
  Its gap from `s` times the top quenched exponent is strict for
  `0<q<1` and closes at `q=0,1`.
- The signed occupation transform has an exact two-state transfer formula
  and a second-order Cayley–Hamilton recurrence at every finite time.

The paper makes no absolute novelty or priority claim. Furstenberg–Kesten
random-product theory, generalized-Lyapunov transfer methods, and the
martingale CLT are expressly subtracted. P91 and P93 are separated by an
explicit internal collision firewall. The bounded search result is not used
as novelty evidence.

## Exact control

```text
python3 code/verify_monomial_toggle.py
```

The verifier uses only the Python standard library and exact `Fraction`
arithmetic. The final run completed **741,486 assertions**. Its exact
stdout is stored in `code/verify_monomial_toggle.out` and explained in
`CONTROL_RESULTS.md`.

## Build

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

See `BUILD.md` and `FINAL_QA.md` for the frozen artifact record.

## Files

- `main.tex`, `references.bib`, `main.pdf` — anonymous short paper
- `code/verify_monomial_toggle.py`, `code/verify_monomial_toggle.out` —
  independent exact verifier and stored output
- `CLAIMS_EVIDENCE.md`, `CONTROL_RESULTS.md` — proof/control traceability
- `HOSTILE_REVIEW_A.md`, `HOSTILE_REVIEW_B.md`, `HOSTILE_REVIEW.md` — two
  nonauthor audits and their consolidated gate
- `BUILD.md`, `FINAL_QA.md`, `SHA256SUMS` — reproducible build, final QA,
  and verified seal

Public posting, submission, specialist contact, and novelty or priority
language remain **HOLD** despite the internal freeze.
