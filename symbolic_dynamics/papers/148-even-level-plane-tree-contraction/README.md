# P148 — even-level contraction of plane rooted trees

**Status: ROUND-2 INTERNAL REVIEW ACCEPTED / HOLD_EXTERNAL.**

The paper studies a literal finite self-map on `PT_{<=N}`: delete every
odd-depth vertex, promote its ordered grandchild blocks, reset parity, and
repeat.  The unordered one-step shadow is exactly the outward-contraction of
Soo--Khoussainov--Linz, arXiv:2111.13238v4, Definition 6.6.

## Review-frozen credit boundary

The direct-owned unordered one-step rule, its partition-tree interpretation,
and all cheap unordered all-rank consequences obtained by iteration—including
depth divisibility and the binary height/absorption clock—receive **zero
contribution credit**.  They remain in the paper as correct supporting
analysis.  The only residual retained for internal scoring is the conjunction

```text
ordered every-target size-refined inverse
+ exact-layer image criterion
+ algebraic image series.
```

Hostile Review A found **1 Critical / 0 Major / 2 Minor**.  After the direct
owner gate was reopened and the source, proof, and metadata repairs were
made, independent Hostile Review B returned **0 / 0 / 0, ACCEPT**.

## Frozen artifacts

- `main.pdf`: round-2 artifact, 5 A4 pages, 357,397 bytes, SHA-256
  `5c681793e5e97abb0ad718f876a2e0af11bd2d41585d860dc0c5b8c3992ed957`.
- Exact verifier: 216,905 assertions, canonical transcript PASS.
- Bibliography and visual checks: 5/5 references resolved; 5/5 pages accepted.
- A source-only isolated build is byte-identical to `main.pdf`.

## Reproduce

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p148.py
PYTHONDONTWRITEBYTECODE=1 python3 verify_p148.py | cmp - verification_output.txt
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

`main_round0_original.pdf` preserves the pre-review baseline;
`main_round1.pdf` is byte-identical to the accepted round-2 `main.pdf`.
Enumeration is a falsifier, not a proof or novelty certificate.  No external
release, posting, submission, specialist contact, or Git action is
authorized.
