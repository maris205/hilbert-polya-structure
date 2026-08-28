# P93 — Random Push–Pop Stack Cocycles

Status: theorem-bearing package frozen after two hostile-review passes and
final QA; external release **HOLD**.

Let `X=A^N0`, with `|A|=b>=2`.  At each time an iid environment applies
the left shift `D` with probability `p`, or prefixes a uniformly sampled
letter with probability `1-p`.  For

```text
S_n = (# shifts) - (# prefixes),
M_n = max_(0<=k<=n) S_k,
```

the paper proves the finite pathwise normal form

```text
Phi_n = C_(u_n) D^(J_n),
J_n = M_n,
I_n = |u_n| = M_n - S_n.
```

Thus `Phi_n(X)` is exactly the cylinder `[u_n]`, its diameter is
`b^(-I_n)`, and every point of the image has exactly `b^(J_n)` preimages.

## Main theorem package

- quenched fibre growth:
  `g_q(p)=(2p-1)_+ log b`;
- quenched image contraction:
  `c_q(p)=(1-2p)_+ log b`;
- uniform synchronization exactly when `p<1/2`;
- at `p=1/2`, each of `J_n/sqrt(n)` and `I_n/sqrt(n)`, marginally,
  converges in law to a half-normal variable (no joint limit is claimed),
  and their expectations are asymptotic to
  `sqrt(2n/pi)`;
- for `A_n=E[b^(J_n)]` and `lambda=bp+(1-p)/b`, the exact annealed
  trichotomy
  - `p<1/(b+1)`: `A_n -> (1-r)/(1-br)`, `r=p/(1-p)`;
  - `p=1/(b+1)`:
    `A_n=((b-1)^2/(b(b+1)))n+O(1)`;
  - `p>1/(b+1)`:
    `A_n/lambda^n -> (1-rho)/(1-b rho)`,
    `rho=(1-p)/(p b^2)`;
- the annealed exponent
  `g_a(p)=log max{1,bp+(1-p)/b}` and the strict gap
  `g_a(p)>g_q(p)` for `1/(b+1)<p<1`;
- at `p=1/2`, typical logarithmic fibre growth is on the `sqrt(n)` scale,
  while the annealed fibre moment is asymptotic to
  `((b+1)/b)((b+b^(-1))/2)^n`.

## Build

From this directory run:

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The current artifact is `main.pdf`, an anonymous seven-page `amsart`
internal preprint.

## Exact control

Run:

```text
python3 code/verify_push_pop.py
```

The program uses only the Python standard library.  It completed 265,861
integer or rational assertions.  Five separately labelled floating-point
values illustrate convergence and are not theorem evidence.

## Owner subtraction and collision firewall

The paper does not claim the following ingredients: random-dynamical-system
formalism, bicyclic or zero-automatic monoid normal forms, random-walk
drift/entropy, ballot and reflection identities, gambler's ruin,
exponential tilting, or reflected birth--death chains.  The bibliography
credits representative owners for those frameworks.

The residual package couples a prefix--shift cocycle to exact symbolic
image cylinders and fibre multiplicities, then computes the complete
alphabet-dependent annealed trichotomy.  This is not a random SFT, a
rank-one reset/renewal model, or a hidden-output process.  A bounded search
did not locate a source for the full conjunction, but search absence is not
an absolute novelty claim.  Public posting, submission, author contact, and
priority language remain unauthorized pending specialist review.

## Files

- `main.tex` — complete anonymous manuscript and proofs
- `references.bib` — cited, owner-subtracted bibliography
- `code/verify_push_pop.py` — deterministic exact control
- `CLAIMS_EVIDENCE.md` — theorem-to-proof/control map
- `CONTROL_RESULTS.md` — recorded control output and coverage
- `BUILD.md` — reproducible build record
- `main.pdf` — compiled draft

- `HOSTILE_REVIEW.md` — two-pass adversarial proof audit and repair ledger
- `FINAL_QA.md` — final control, build, font, text, and visual checks
- `SHA256SUMS` — frozen source, evidence, and PDF hashes
