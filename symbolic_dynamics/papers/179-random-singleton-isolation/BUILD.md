# Build record — P179

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

The four Round-0 commands exited zero.  The settled log contains no warning, bad box,
undefined reference/citation, multiply defined label, or error.

## Round-0 initial metrics

```text
pages:            3
paper:            A4, 595.276 x 841.89 pt
bytes:            256075
fonts:            20/20 embedded and subsetted
metadata:         Title/Author/Creator/Producer blank
JavaScript:       none
encryption:       none
visual audit:     3/3 rasterized pages inspected; no clipping/overlap/blank page
```

The final verifier was replayed in a fresh Python process and matched
`code/CANONICAL.txt` byte for byte:

```text
assertions:       252320
verifier SHA256:  200b1b2ded1158bff7632ccf8b8cd27403da3757abeb713f82f99c297034a6c5
canonical SHA256: e0264ffec9f83da16e45d00ed1801963137c107368c75ef46204addec609f2cf
```

The immutable author Round-0 receipt is:

```text
c0a97f79c22799e90b3c2bd95d0060b4b75b38b28536332e5d60fe38f2a5f923  main_round0_original.pdf
```

Review A requested an explicit `n>=1` model boundary and internal collision
subtraction against P169/P110.  The repaired source compiled cleanly:

```text
pages:            3
bytes:            256754
main.tex SHA256:  cb7886a6846a4a8019c6636f77bbe9faa5cd8fbc342bbde6c822d57286938b7b
Round-1 PDF:      9c6018baa87f9e772a46e70cafb59cc804f6711c3a1b82852327df4b00f8bd7d
main.pdf equals main_round1.pdf: yes
fonts:            20/20 embedded, subsetted, and Unicode mapped
metadata:         identifying fields blank
```

The final science audit then found that the support lemma's prose accidentally
excluded a nonempty residual block of size one, although the downstream
formulas and original verifier used the correct literal action.  The lemma and
proof now retain every nonempty residual; a new exhaustive support-formula
oracle contributes 127,202 assertions.  The two original reviewers re-entered
on this exact Round-2 source, replayed their controls, and report zero open
findings.  Reviewer A closes 120,977 independent assertions and Reviewer B
closes 209,583.  The final receipt is:

```text
main.tex SHA256:
94ff9a5e84d50473b9c48afeb79098bd83cec1e848612e18b71b0b24ac03bbb6
Round-2/live PDF:
6c93451aa6116c32164ee0d255315f88e0299b60c2ba17879d73c75309e1773c
two source-only cold builds: byte-identical PASS
final visual pages inspected: 3/3 PASS
```

See `FINAL_QA.md` for the final gate.
