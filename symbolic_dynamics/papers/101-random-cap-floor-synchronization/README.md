# P101 — Random Cap–Floor Synchronization

Status: theorem-bearing package refrozen after two author-side hostile-review
passes, one independent internal cross-hostile repair, and final mechanical
QA; external release **HOLD**.

This package studies iid cap and floor maps of `[0,1]`.  It proves an exact
clamp-or-constant finite-word normal form, a distribution-free finite-time
synchronization law, a geometric-sum representation and explicit moments,
and an exact expected-diameter formula for uniform thresholds.

## Main theorem package

- Forward composition is fixed as `Phi_n = g_n o ... o g_1`. Every finite
  word is either the clamp `K_[A_n,B_n]` or a constant, with the latter case
  occurring exactly at `A_n >= B_n`.
- For iid atomless thresholds,
  `P(T>n)=sum_(j=0)^n p^j(1-p)^(n-j)`, independently of the threshold law.
- For `0<p<1`, `T` is distributed as the sum of independent geometric
  variables with parameters `p` and `1-p`, so
  `E[T]=1/(p(1-p))` and
  `Var(T)=(1-3p(1-p))/(p^2(1-p)^2)`.
- At `p=1/2`, survival is exactly `(n+1)2^(-n)`; off criticality its leading
  base is `max(p,1-p)` with the exact prefactor stated in the paper.
- For uniform thresholds,
  `E[diam Phi_n([0,1])] = P(T>n)/(n+1)`. Hence the critical mean diameter is
  exactly `2^(-n)`, while at `p=0,1` it is `1/(n+1)`.
- Conditional formulas given `N_n=j` are asserted only when that event has
  positive probability. The two endpoint diameter laws are also proved
  directly from pure cap/floor order statistics.
- Mixed sample paths collapse exactly after the almost-surely finite time
  `T`; this finite absorption is kept distinct from the finite annealed
  logarithmic rate of expected diameter.

The paper makes no absolute novelty or priority claim.  General iterated
random functions, monotone random-map synchronization, finite-chain
contraction semigroups, and standard rank/order-statistic facts are expressly
subtracted.  Specialist direct-owner review remains required.

## Build

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Exact control

```text
python3 code/verify_cap_floor.py
```

The verifier uses only the Python standard library and exact integer or
rational arithmetic. The frozen run completed **6,948,361 assertions**;
its literal output is stored in `code/verify_cap_floor.out` and explained in
`CONTROL_RESULTS.md`.

## Frozen artifact

`main.pdf` is an anonymous five-page A4 `amsart` short paper. All fonts are
embedded. The source, evidence documents, control program and output, and
PDF are covered by `SHA256SUMS`.

## Files

- `main.tex`, `references.bib`, `main.pdf` — paper source, bibliography, PDF
- `code/verify_cap_floor.py`, `code/verify_cap_floor.out` — exact verifier
  and stored output
- `CLAIMS_EVIDENCE.md`, `CONTROL_RESULTS.md` — proof/control traceability
- `HOSTILE_REVIEW.md` — honest two-pass author audit plus independent
  internal cross-hostile closure ledger
- `BUILD.md`, `FINAL_QA.md`, `SHA256SUMS` — build and freeze evidence
