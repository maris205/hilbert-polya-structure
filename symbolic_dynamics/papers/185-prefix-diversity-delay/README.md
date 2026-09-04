# P185 — prefix-diversity delay

**Round:** `ROUND2_DUAL_REVIEW_FREEZE`  
**Owner gate:** `OWNER_AMBER`  
**External lifecycle:** `HOLD_EXTERNAL`

The paper replaces each coordinate of `w in [n]^n` by the number of distinct
letters in its strict prefix.  It proves the all-time pointwise delay formula,
unique recurrent identity, exact point clock, time images, every-time
every-target fibre product, depth CDF, and complete sharp-depth population.

The paper-local replay is byte-stable and ends with **10,430,175 exact
assertions** over all `n^n` words through `n=7`.  Two process-separated
hostile reviews add 5,782,239 assertions, close the sole Round-0 Minor scope
finding, and leave zero open findings.  The frozen final PDF has three A4
pages.

## Exact replay

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p185.py
PYTHONDONTWRITEBYTECODE=1 python3 verify_p185.py | cmp - CANONICAL.txt
```

## Deterministic build

```bash
export SOURCE_DATE_EPOCH=1704067200
export TZ=UTC
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

`main_round0_original.pdf` preserves the author artifact;
`main_round1.pdf` preserves the accepted scope repair; `main_round2.pdf` is a
byte-identical Review-B receipt.  Two source-only cold builds reproduce the
final PDF.  No external action is authorized.
