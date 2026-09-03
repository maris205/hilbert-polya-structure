# Build record — P180

**Build date:** 2026-09-03 UTC.  
**Status:** `ROUND2_DUAL_REVIEW_FREEZE / HOLD_EXTERNAL`.

The deterministic manuscript preamble suppresses timestamps, trailer IDs,
engine metadata, and identifying PDF fields.  The intended explicit build is:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

All four Round-0 commands exited zero.  The settled log contains no warning, bad box,
undefined reference/citation, multiply defined label, or error.

## Round-0 initial metrics

```text
pages:            3
paper:            A4, 595.276 x 841.89 pt
bytes:            266340
fonts:            24/24 embedded and subsetted
metadata:         Title/Author/Creator/Producer blank
JavaScript:       none
encryption:       none
visual audit:     3/3 rasterized pages inspected; no clipping/overlap/blank page
```

The verifier replay matched `code/CANONICAL.txt` byte for byte:

```text
assertions:       770697
verifier SHA256:  1280ced45293a1b7ea22df577d3c4fa12cf5297b4b263d0666562fbd1811fd61
canonical SHA256: 1cc3b6253f83521f6b0cf0fa11a160d90aaa91683341655b78de0381467c024b
```

The immutable author Round-0 receipt is:

```text
3051dc087aa5c26bb2bcc69e363af75918fe51797dd509161979656fb8ecb248  main_round0_original.pdf
```

Review A required the missing time-zero identity fibre, explicit
`q`-prime-power/`m>=1` assumptions, and internal subtraction against
P102/P103/P125/P171.  The repaired verifier adds 46,702 identity-fibre
assertions.  Order-decomposition and characteristic-two wording was also
hardened.  The clean Round-1 receipt is:

```text
pages:            3
bytes:            268029
main.tex SHA256:  529bd4c0c091d3932c35de0b1ac8a6d347b3c65a838738bccfc1167207929991
Round-1 PDF:      d0b08ddc5de6a91a120282d6c31dcc56ca67c1bfdc5202d68b24a22335c80b59
main.pdf equals main_round1.pdf: yes
fonts:            24/24 embedded, subsetted, and Unicode mapped
metadata:         identifying fields blank
```

Reviewer A closes 243,393 independent assertions; Reviewer B closes
1,143,286 extension-field assertions over `GF(4/8/9/16/25/64)`, including
non-symmetric forms and all target fibres at `t=0,...,4`.  Both report zero
open findings.  Round 2 deliberately reproduces the accepted Round-1 bytes:

```text
main.pdf/main_round1.pdf/main_round2.pdf:
d0b08ddc5de6a91a120282d6c31dcc56ca67c1bfdc5202d68b24a22335c80b59
two source-only cold builds: byte-identical PASS
final visual pages inspected: 3/3 PASS
```

See `FINAL_QA.md` for the final gate.
