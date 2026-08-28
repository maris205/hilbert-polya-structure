# P82 — shifted Fredkin frozen-set SFT

Status: theorem-bearing internal freeze after hostile audit; external release **HOLD**.

This package studies a binary ring of length `3m` under two staggered layers
of the explicitly defined control-on-one three-bit Fredkin gate.  It proves
that the frozen configurations form an eight-symbol nearest-neighbor shift of
finite type with rank-two transfer matrix.  The resulting fixed count is

```text
f_m = ((5 + sqrt(13))/2)^m + ((5 - sqrt(13))/2)^m,
f_m = 5 f_{m-1} - 3 f_{m-2},  f_1 = 5, f_2 = 19.
```

The paper also proves reversibility, an explicit reversing involution,
Hamming-weight conservation, frozen-set entropy, and

```text
zeta_fr(z) = 1 / (1 - 5 z + 3 z^2).
```

Here `zeta_fr` is the Artin--Mazur zeta function of the **spatial block
shift on the frozen SFT**.  It is not a temporal zeta function of the
finite-ring map `T_m`.

## Artifacts

- `main.tex`, `references.bib`: paper source and cited-only bibliography.
- `main.pdf`: compiled six-page paper.
- `code/verify_fredkin.py`: dependency-free exhaustive finite control.
- `CLAIMS_EVIDENCE.md`: theorem-to-proof/control map.
- `CONTROL_RESULTS.md`: exact finite census and assertion count.
- `BUILD.md`: reproducible build instructions.
- `FINAL_QA.md`: release-audit record.

## Reproduce

```bash
python3 code/verify_fredkin.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The script exhausts all `299,592` states for `m=1,...,6`.  The computation
is a regression control and is not used as a proof of the all-`m` formulas.

## Ownership and claim boundary

The paper assigns the Fredkin gate to Fredkin--Toffoli, reversible block
architectures to the Toffoli--Margolus/Kari line, and directly compares the
different three-layer four-site Fredkin staircase model of Singh, Vasseur,
and Gopalakrishnan.  The residual claim is limited to the transfer matrix and
frozen-state invariants of this explicitly defined two-layer three-bit map.

There is no claim of inventing Fredkin dynamics, conservative logic,
partitioned reversible cellular automata, or integrability.  The observed
maximum temporal periods through `m=6` are not extrapolated to an unbounded
period theorem, and no temporal Artin--Mazur zeta function is asserted.

Literature cutoff: 2026-08-28 UTC.  No public posting, submission, or
absolute priority claim is authorized by this package.
