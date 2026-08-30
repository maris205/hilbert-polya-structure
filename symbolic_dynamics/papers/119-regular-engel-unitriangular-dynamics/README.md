# P119 — Regular Engel dynamics on unitriangular groups

Status: **ANONYMOUS INTERNAL AUTHOR DRAFT / EXTERNAL HOLD**.

Fix the regular element `J=I+N` in `U_n(F_q)` and iterate

```text
E(X)=X^(-1) J^(-1) X J.
```

For the filtration `gamma_k` of matrices whose first `k-1`
superdiagonals vanish, Bier 2013 already proves the fixed-`J` image equality
`E(gamma_k)=gamma_(k+1)` over arbitrary fields.  The manuscript reproduces
that equality for self-containment and gives it zero contribution credit.
Its finite-field refinement proves:

1. every target in the owned image has a left-coset fibre of exact size
   `q^(n-k)`;
2. every restricted iterated fibre;
3. every cumulative and exact depth layer, sharp height `n-1`, and deepest
   shell `(q-1)q^(binom(n,2)-1)`;
4. the one-component depth and filtration-typed predecessor census, unique
   recurrence, and zeta `(1-z)^(-1)`;
5. two materially different finite-field counts: centralizer cosets and
   triangular superdiagonal differences; and
6. a `U_4` counterexample showing failure for
   `J'=I+E12+E34`.

The claim ceiling is the literal fixed regular `J=I+N`. Bier's restricted
and iterated image theorems, Lang-map terminology, left Engel sequences and
sinks, regular centralizers, lower-central descent, and generic zeta
machinery receive zero contribution credit.  The `U_4` guard shows only that
the theorem does not extend to arbitrary unipotent `J`; it does not classify
all nonregular choices.  Novelty, priority, specialist clearance, and
external circulation remain **HOLD**.

## Exact controls

Run from this directory:

```text
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
```

The expected terminus reports:

```text
regular Engel exact control: PASS
assertions=1,491,877
```

The full canonical stdout is in `code/verification_output.txt`. The verifier
uses literal polynomial-basis models of six finite fields, exhausts 55,808
regular phase states and 20,514 near-regular counterexample states, and
byte-checks `code/exact_layer_table.tsv`.

## Build

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

See `BUILD.md` for the settled mechanical record. `main_round0_original.pdf`
is the frozen initial author build; `main.pdf` is the current **6-page**
author PDF.
