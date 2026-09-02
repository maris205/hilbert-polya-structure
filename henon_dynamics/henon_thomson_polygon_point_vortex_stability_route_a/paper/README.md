# Deterministic manuscript build

The source contains three substantive revision layers selected by
`\CRevisionRound`:

- round 0: Hamiltonian, raw Hessian, DFT theorem, sharp threshold;
- round 1: symmetry slice, all parameter faces, independent reconstruction;
- round 2: strict evidence/schema receipt, source-owner audit, nonclaims, and
  Route-A firewall.

For revision `r`, run two settled passes in a fresh directory:

```bash
SOURCE_DATE_EPOCH=1788307200 FORCE_SOURCE_DATE=1 TZ=UTC \
  lualatex -interaction=nonstopmode -halt-on-error -jobname=main \
  '\def\CRevisionRound{r}\input{/absolute/path/to/paper/main.tex}'
```

Repeat the command once in the same fresh directory.  The release manifest
does this twice for every round and requires both byte streams to equal the
archived PDF.  `paper/main.pdf` is byte-identical to `main_round2.pdf`.
