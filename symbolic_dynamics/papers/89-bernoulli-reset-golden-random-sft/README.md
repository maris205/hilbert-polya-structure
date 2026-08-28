# P89 — Bernoulli-Reset Golden Random Shift

Status: theorem package complete for internal freeze; external release
**HOLD**.

At each time an iid environment chooses the golden-mean adjacency matrix

```text
A = [[1,1],[1,0]]
```

with probability `1-p`, or the rank-one reset matrix

```text
E = [[1,1],[0,0]]
```

with probability `p`.  If `N_n` is the number of binary state paths through
the first `n` constraints, the paper proves the exact reset identity

```text
E A^k E = F_(k+2) E.
```

This makes `log N_n` a renewal-reward process.  The main results are:

- the exact quenched fibre entropy
  `h_q(p) = p^2 sum_(k>=0) (1-p)^k log F_(k+2)`;
- the exact annealed exponent
  `h_a(p) = log((1+sqrt(5-4p))/2)`;
- the strict gap `h_q(p) < h_a(p)` for every `0<p<1`, with equality only at
  the deterministic endpoints;
- a renewal central limit theorem for `log N_n` with the explicit positive
  variance
  `p^2 sum_(k>=0) (1-p)^k (log F_(k+2)-(k+1)h_q(p))^2`.

The manuscript is anonymous and uses `amsart`.  The formula package is
supported by a deterministic standard-library control program.

## Build

From this directory run:

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The expected artifact is `main.pdf`.

## Exact controls

Run:

```text
python3 code/verify_reset_golden.py
```

The program uses only the Python standard library.  Its discrete layer uses
integers and `fractions.Fraction`; floating-point entropy values are marked
as diagnostics and do not certify the theorems.

## Ownership and HOLD boundary

Furstenberg--Kesten own the general random-matrix-product setting.  Kifer
and Denker--Kifer--Stadlbauer own broad random-subshift thermodynamic
formalism.  Renewal-reward laws and central limit theorems are classical
regenerative probability, represented here by Asmussen.  The golden-mean
shift is standard.

This paper claims only an exact calculation for the displayed two-matrix
model.  It makes no absolute novelty or priority claim.  A bounded search
through 2026-08-28 found no direct source for the full combined formula
package, but that negative result is not exhaustive.  Public posting,
submission, or priority language remains unauthorized pending a separate
expert literature review.

## Files

- `main.tex` — complete anonymous manuscript and proofs
- `references.bib` — cited ownership bibliography
- `code/verify_reset_golden.py` — deterministic exact controls
- `CLAIMS_EVIDENCE.md` — theorem-to-proof/control map
- `CONTROL_RESULTS.md` — recorded control output and coverage
- `BUILD.md` — reproducible build instructions and artifact metadata
- `HOSTILE_REVIEW.md` — adversarial proof and ownership audit
- `FINAL_QA.md` — final release checklist
- `main.pdf` — compiled manuscript
