# P116 — Switching-Induced Growth for a Neutral Max-Plus Pair

Status: **ANONYMOUS AUTHOR DRAFT / COMPILED / EXTERNAL HOLD**.

This package studies the iid max-plus cocycle

```text
A = [[-2,-1],[ 1,-1]] with probability p,
B = [[-1, 1],[-1,-2]] with probability q=1-p,
M_n = X_n ⊗ ... ⊗ X_1,  X_1 acts first,
H_n = maximum entry of M_n,  H_0=0.
```

## Core theorem package

- Each deterministic generator has tropical spectral radius zero, bounded
  powers, and tropical rank two. At `p=0,1`, `H_n=n mod 2`, so the growth
  rate and fixed-tilt pressure are zero.
- No word of length one or two has tropical rank one. Exactly four words of
  minimal length three do: `ABA`, `ABB`, `BAA`, and `BAB`, with constant
  output gaps `-3,0,0,3`, respectively. These are projective reset words.
- The literal projective gap takes exactly the five reachable values
  `{-3,-2,0,2,3}`. Grouping negative, zero, and positive gaps gives a strong
  reward lumping to `N,Z,P`.
- The full finite-time transform is

  ```text
  E[y^H_n] = e_Z^T Q_p(y)^n 1,
  Q_p(y) = [[0,p/y,qy],[py,0,qy],[py,q/y,0]].
  ```

  Its characteristic polynomial is

  ```text
  r^3 + (2pq-1-pq y^2)r - pq y.
  ```

- For `0<p<1`, the exact stationary law is

  ```text
  pi_N=p/(1+p), pi_Z=(1-pq)/(2+pq), pi_P=q/(1+q).
  ```

  The SLLN drift and CLT variance are

  ```text
  mu_p = 3pq/(2+pq),
  sigma_p^2 = 4pq(1-pq)(5-2pq)/(2+pq)^3.
  ```

- The pressure is the logarithm of the Perron root of `Q_p(e^t)` and gives a
  Legendre-transform LDP. The attainable heights are exactly
  `{n mod 2, n mod 2+2, ..., n}`; exactly two alternating words attain the
  upper bound for `n>=1`.
- For `0<p<1`,

  ```text
  Lambda_p(t)-t -> (1/2)log(pq)       as t -> +infinity,
  Lambda_p(t)   -> (1/2)log(1-2pq)    as t -> -infinity.
  ```

The manuscript derives the variance twice: from an explicit Poisson
solution and bounded martingale differences, then from the second implicit
derivative of the cubic Perron equation.

## Owner subtraction and internal comparisons

General max-plus/topical automata, projective semigroups, random Lyapunov
exponents, reset/coupling and memory loss, laws of large numbers, CLTs, LDPs,
switching-system models, and finite Perron theory are established
background. Direct owner subtraction includes Gaubert (1995), Mairesse
(1997), Baccelli--Hong (2000), Blondel--Gaubert--Tsitsiklis (2000), Merlet
(2010), Goverde--Heidergott--Merlet (2011), van den Boom--De Schutter (2012),
and Kordonis--Maragos--Papavassilopoulos (2018). The residual is only this
pair's explicit five-gap/table/rational/cubic/word-edge/temperature package;
equivalence classes have not been exhausted. In particular, P89 and this
paper both have reset/coupling features, but use different state spaces,
observables, and proof packages. See the manuscript and
`CLAIMS_EVIDENCE.md` for the exact scope.

## Exact verifier

From this directory, run:

```bash
PYTHONDONTWRITEBYTECODE=1 python code/verify.py
```

The clean author run passed **1,183,356 exact assertions**. It exhausts all
131,071 words through length 16, classifies all reset words through length
three, constructs every parity-compatible height, and checks biased
laws/PGFs through time 32.
Only integers and `fractions.Fraction` are used. Stored stdout is in
`code/verify.out`; coverage and non-evidence boundaries are in
`CONTROL_RESULTS.md`.

## Build

The environment does not provide `latexmk`; use the deterministic manual
sequence:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

See `BUILD.md` for the recorded author build and page/warning counts.

## Files

- `main.tex`, `math_commands.tex`, `sections/*.tex`, `references.bib` —
  anonymous amsart source.
- `main.pdf` — compiled paper.
- `PAPER_PLAN.md`, `NARRATIVE_REPORT.md` — claim structure and derivation
  spine.
- `CLAIMS_EVIDENCE.md`, `CONTROL_RESULTS.md` — traceability and exact
  controls.
- `HOSTILE_REVIEW_A.md`, `HOSTILE_REVIEW_B.md`, `HOSTILE_REVIEW.md` — the
  two independent reviews and this revision's resolution ledger.
- `code/verify.py`, `code/verify.out` — verifier and stored fresh output.
- `BUILD.md` — reproducible author-build record.

This directory intentionally contains no final-QA report, hash seal, Git
record, public-release action, or priority decision.
