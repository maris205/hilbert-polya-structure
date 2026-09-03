# P172 — Fresh-map self-image erosion

**Round:** final Round 2; both hostile reviews closed  
**Gate:** `PROVISIONAL_GREEN_OWNER_THIN`  
**External lifecycle:** `HOLD_EXTERNAL`

At each epoch this finite Markov chain samples a fresh uniform endomap of
`[n]` and replaces the current labelled subset `A` by `A intersect f(A)`.
The note gives a labelled endpoint-and-image-size Stirling formula, the
all-time labelled kernel, the complete algebraic spectrum, a forced `J_2`
block in the size quotient, and exact absorption/marked-transfer formulas.

The whole unmarked cardinality row is explicitly identified with O'Neill's
extended occupancy law `Occ(b|a,a,a/n)` and assigned zero credit, alongside
specified-cell occupancy, ordinary random images, generic marked-kernel
products, and triangular-chain algebra.  P158, P162, P170, and sibling P173
are individually subtracted.  The retained narrow conjunction is the
state-dependent self-image erosion, fixed-endpoint/total-image refinement,
coefficientwise labelled lift, and terminal `J_2`.  A bounded owner-search
non-hit is not a novelty claim; external circulation remains on hold.

## Reproduce

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p172.py

pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Both independent hostile reviews are present.  Review A passed after two
minor scope/source repairs.  Review B found no mathematical counterexample
but required three major owner/formalization repairs and five minor clarity
repairs; all eight findings are closed by read-only delta acceptance.  The
current source and `main_round2.pdf` are the accepted revision.  Final
cold-build logs and the complete SHA-256 manifest are part of the batch
closeout.
