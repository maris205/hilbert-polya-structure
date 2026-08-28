# P87 — Socle-Product Shifts over Finite Chain Rings

Status: **GO for internal theorem freeze; external release HOLD**.

Let `R` be a finite commutative chain ring with maximal ideal `(pi)`,
residue-field size `q`, and length `a+1`.  The paper studies the
nearest-neighbor shift defined by

```text
x_n x_(n+1) in Soc(R) \ {0}.
```

The theorem package is exact:

- valuation turns the edge rule into `v(x)+v(y)=a`;
- the graph is a disjoint union of complete bipartite components and, for
  even `a`, one full-shift component;
- every component has Perron value `rho=(q-1)q^(a/2)`, while the full
  adjacency rank is exactly `a+1`;
- there are `floor(a/2)+1` ergodic maximal-entropy measures;
- odd `a` gives only period-two maximal components, whereas even `a` gives
  exactly one mixing maximal component;
- all fixed-point counts, least-period orbit counts, and the Artin--Mazur
  zeta function are explicit;
- `F_1,...,F_4` recover `(q,a)`;
- all chain rings with the same `(q,a)` give one-block conjugate shifts,
  including the nonisomorphic pair `Z/p^(a+1)Z` and
  `F_p[t]/(t^(a+1))`.

## Build

`latexmk` is not installed in the release environment.  Use the reproducible
house fallback:

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
python3 code/verify_socle_shift.py
```

The program uses only the Python standard library.  It checks all abstract
valuation models for `q=2,3,4,5` and `a=1,...,5`, and independently realizes
the prime-residue cases in both `Z/p^r Z` and `F_p[t]/(t^r)` for
`r=2,...,6`.  It also realizes the nonprime case in `F_4[t]/(t^r)`.

## Ownership scope

The classical Anderson--Livingston zero-divisor graph has nonzero zero
divisors as vertices and joins distinct vertices when their product is zero.
The closest chain-ring spectral owner, Rattanakangwanwong--Meemark, studies
that zero-product graph and its principal-ideal-ring extension.  P87 instead
uses all nonzero ring elements, retains loops, and selects the preceding
valuation boundary where the product is a **nonzero socle element**.  Those
owners are positively cited and their graph theory is not claimed.

Dolžan (2026) is the closer fixed-product owner: his matrix has entries
`1_(xy=u)` for one prescribed ring element `u`.  P87's adjacency matrix is,
after deleting the zero row and column, exactly the sum of these matrices over
all `u in Soc(R)\{0}`.  P87 therefore does not claim fixed-product matrices or
their spectral theory.  Its residual package concerns the nonzero-socle union,
the resulting equal-entropy symbolic components, all periods, recovery, and
ring collapse.

A bounded search through 2026-08-28 found no direct source for the combined
socle-boundary symbolic theorem package.  This is not an absolute novelty or
priority claim.  Public posting, submission, author contact, venue selection,
and specialist priority clearance remain unauthorized and **HOLD**.

## Files

- `main.tex` — complete anonymous `amsart` manuscript and proofs
- `references.bib` — cited, source-verified bibliography
- `code/verify_socle_shift.py` — deterministic exact controls
- `CLAIMS_EVIDENCE.md` — theorem-to-proof/control map
- `CONTROL_RESULTS.md` — recorded control output and coverage
- `BUILD.md` — build instructions and artifact metadata
- `HOSTILE_REVIEW.md` — proof-feasibility and owner-boundary audit
- `FINAL_QA.md` — release checklist
- `SHA256SUMS` — artifact checksums
- `main.pdf` — compiled five-page manuscript
