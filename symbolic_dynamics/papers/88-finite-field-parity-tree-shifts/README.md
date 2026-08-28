# P88 — Finite-Field Parity Tree Shifts

Status: internal short-paper freeze after proof and owner audit; external
release **HOLD**.

On the full rooted ordered `d`-ary tree, with `d >= 2`, label every vertex by
`F_q` and impose

```text
x_w = sum_j c_j x_{wj},       c_j != 0.
```

Here `q` is any prime power.  The paper proves the following exact package:

- height-`h` legal blocks are in bijection with arbitrary data on the
  `d^h` terminal vertices, so there are exactly `q^(d^h)` blocks;
- the boundary-, site-, and double-log-normalized complexities are,
  respectively, `log q`, `(d-1) log(q)/d`, and `log d`;
- uniform terminal data give compatible uniform block laws and a homogeneous
  joint-offspring block-Markov measure;
- every deterministic ray is iid uniform on `F_q`;
- the complete level reconstructs the root by an explicit nonzero linear
  functional;
- every proper coordinate subset of that level is independent of the root and has
  mutual information zero, whereas the complete level has mutual information
  `log q`.

The all-prime-power scope is proved algebraically.  The control script uses
prime-field enumeration and rank lanes plus an independent exhaustive
`F_4 = F_2[a]/(a^2+a+1)` regression lane.

## Build

From this directory, run:

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
python3 code/verify_parity_tree.py
```

The script uses only the Python standard library.  It combines
definition-level enumeration with modular Gaussian elimination and exits
nonzero on any failed identity.

## Ownership and internal firewall

The manuscript positively assigns finite-type tree shifts to Aubrun–Béal,
nonlinear tree-block recurrences and double-log entropy to Ban–Chang,
site-normalized tree entropy to Petersen–Salama, tree-indexed Markov
processes to Benjamini–Peres, binary joint-offspring kernels to Guyon, block
Markov chains on trees to Souissi, tree broadcasting/reconstruction to
Evans–Kenyon–Peres–Schulman, and perfect threshold secret sharing to Blakley
and Shamir.  The residual contribution is the combined finite-field
leaf/ray/simultaneous-level calculation.  A bounded search found no exact
owner of that combined package, but the manuscript makes no absolute
novelty or priority claim.

P49 studies parent–child hom-tree adjacency, transient phase allocation, and
Hausdorff dimension; P88 studies one star-linear sibling constraint and no
phase optimization.  P77 studies one-dimensional countable automatic orbit
closures and Cantor–Bendixson/endomorphism structure; P88 is an uncountable
free-semigroup tree shift and uses no automatic digit support.  These are the
frozen internal firewalls.

## Files

- `main.tex` — complete anonymous `amsart` manuscript and proofs
- `references.bib` — nine cited, primary-source entries with resolved DOIs
- `code/verify_parity_tree.py` — deterministic exact controls
- `CLAIMS_EVIDENCE.md` — theorem-to-proof/control map
- `CONTROL_RESULTS.md` — recorded control output and scope
- `BUILD.md` — reproducible build instructions and artifact metadata
- `HOSTILE_REVIEW.md` — adversarial proof, ownership, and collision audit
- `FINAL_QA.md` — final release checklist
- `main.pdf` — compiled internal manuscript
