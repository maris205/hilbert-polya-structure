# Paper

The review-ready manuscript is [paper.pdf](paper.pdf).  It includes an English
abstract, a simplified-Chinese abstract, full proofs, a trace-taxonomy table,
the T0--T7 certificate, separate candidate decisions, limitations,
declarations, and an artifact map.

Build with:

```bash
latexmk -xelatex -interaction=nonstopmode -halt-on-error manuscript.tex
```

`manuscript.pdf` is the build target; `paper.pdf` is the release copy.

